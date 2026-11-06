"""Signing an agent's HTTP requests, and checking them.

RFC 9421 HTTP Message Signatures as Web Bot Auth profiles them
(draft-ietf-webbotauth-httpsig-protocol-01), in the form Cloudflare verifies
today:

- ``keyid`` is the key's JWK thumbprint; ``alg="ed25519"``; ``tag="web-bot-auth"``.
- ``Signature-Agent`` names ``https://post.<domain>``, which serves the key
  directory (``/.well-known/http-message-signatures-directory``) and the
  domain's agent cards. Sent as the bare string Cloudflare reads, not the
  draft's dictionary, until Cloudflare reads that (both verify at Pidgeon).
- Covered: ``@method``, ``@authority``, ``@path``, ``@query`` when there is
  one, ``signature-agent``, ``from`` (the agent's address, the header RFC 9110
  gives a robot's operator), ``post-grant`` when it carries grants, and
  ``content-digest`` when there is a body. So a signature holds for this
  request only, not for any request to the host.
- Valid for five minutes. Cloudflare suggests a minute; an agent behind a
  queue needs more.

The twin of ``packages/id/src/http.ts``, held to it and to the server's own
verifier (``src/lib/post/http-signature.ts``) by
``tests/unit/python-identity.test.ts``.

``signedFetch`` is a ``fetch``; its twin here is ``SigningAuth``, an
``httpx.Auth`` that signs every request a client sends — which is how an MCP
client over Streamable HTTP signs (``streamablehttp_client(url,
auth=SigningAuth(identity, agent=...))``) — and ``signed_request``, one
signed request. Signing happens on the request httpx is about to send, after
it has encoded the URL and the body, so what is signed is what goes out.
"""

from __future__ import annotations

import os
import re
import time
from collections.abc import Callable, Generator, Mapping, Sequence
from hashlib import sha256
from typing import Any

import httpx

from ._js import b64, from_b64, url_parts
from .keys import Identity, verify_bytes

__all__ = [
    "SIGNATURE_SECONDS",
    "TAG",
    "SigningAuth",
    "content_digest",
    "sign_request",
    "signed_request",
    "verify_request",
]

TAG = "web-bot-auth"
SIGNATURE_SECONDS = 300


def _quote(value: str) -> str:
    return '"' + value.replace("\\", "\\\\").replace('"', '\\"') + '"'


def _bytes_of(body: str | bytes) -> bytes:
    return body.encode("utf-8") if isinstance(body, str) else bytes(body)


def content_digest(body: str | bytes) -> str:
    """RFC 9530: ``sha-256=:<base64>:``."""
    return f"sha-256=:{b64(sha256(_bytes_of(body)).digest())}:"


def sign_request(
    identity: Identity,
    *,
    method: str,
    url: str | httpx.URL,
    headers: Mapping[str, str] | None = None,
    body: str | bytes | None = None,
    agent: str | None = None,
    now: float | None = None,
    label: str | None = None,
    tag: str | None = None,
    grants: Sequence[str] | None = None,
    seconds: int | None = None,
) -> dict[str, str]:
    """The headers that sign this request, lower-cased.

    ``signature-agent``, ``from`` (with ``agent``), ``post-grant`` (with
    ``grants``), ``content-digest`` (with a body), ``signature-input`` and
    ``signature``. Add them to the request as they are; change nothing they
    cover after. ``now`` is milliseconds since the epoch, as the TypeScript
    twin takes it, for tests. ``headers`` is accepted for parity and not read.
    """
    del headers
    parts = url_parts(url)
    label = label if label is not None else "sig1"
    created = int((now if now is not None else time.time() * 1000) // 1000)
    expires = created + (seconds if seconds is not None else SIGNATURE_SECONDS)
    sender = agent.strip().lower() if agent is not None else None
    if sender and not sender.endswith(f"@{identity.domain}"):
        raise ValueError(f"{sender} is not an address at {identity.domain}, whose key this is.")

    added: dict[str, str] = {"signature-agent": _quote(f"https://post.{identity.domain}")}
    if sender:
        added["from"] = sender
    if grants:
        added["post-grant"] = ", ".join(re.sub(r"\s+", "", jws) for jws in grants)
    data = None if body is None else _bytes_of(body)
    if data:
        added["content-digest"] = content_digest(data)

    values: list[tuple[str, str]] = [
        ("@method", method.upper()),
        ("@authority", parts.host),
        ("@path", parts.pathname),
    ]
    if parts.search:
        values.append(("@query", parts.search))
    values.append(("signature-agent", added["signature-agent"]))
    for name in ("from", "post-grant", "content-digest"):
        if name in added:
            values.append((name, added[name]))

    params = (
        f"({' '.join(_quote(name) for name, _ in values)})"
        f';created={created};expires={expires};keyid={_quote(identity.kid)};alg="ed25519"'
        f";nonce={_quote(b64(os.urandom(32)))};tag={_quote(tag if tag is not None else TAG)}"
    )
    base = "\n".join([*(f"{_quote(name)}: {value}" for name, value in values), f'"@signature-params": {params}'])
    signature = identity.sign(base.encode("utf-8"))
    return {**added, "signature-input": f"{label}={params}", "signature": f"{label}=:{b64(signature)}:"}


class SigningAuth(httpx.Auth):
    """Signs every request an ``httpx`` client sends, as ``agent``.

    ``signedFetch``'s twin, for anything that takes an ``httpx.Auth``::

        httpx.Client(auth=SigningAuth(identity, agent="support-agent@acme.com"))
    """

    requires_request_body = True

    def __init__(self, identity: Identity, *, agent: str, grants: Sequence[str] | None = None) -> None:
        self.identity = identity
        self.agent = agent
        self.grants = list(grants) if grants else None

    def auth_flow(self, request: httpx.Request) -> Generator[httpx.Request, httpx.Response, None]:
        body = request.content
        signature = sign_request(
            self.identity,
            method=request.method,
            url=request.url,
            body=body if body else None,
            agent=self.agent,
            grants=self.grants,
        )
        for name, value in signature.items():
            request.headers[name] = value
        yield request


def signed_request(
    identity: Identity,
    method: str,
    url: str,
    *,
    agent: str,
    grants: Sequence[str] | None = None,
    client: httpx.Client | None = None,
    **kwargs: Any,
) -> httpx.Response:
    """One request, signed as ``agent``. ``kwargs`` go to ``httpx.Client.request``."""
    auth = SigningAuth(identity, agent=agent, grants=grants)
    if client is not None:
        return client.request(method, url, auth=auth, **kwargs)
    with httpx.Client(follow_redirects=True) as own:
        return own.request(method, url, auth=auth, **kwargs)


# --- Verifying, for a receiver ---------------------------------------------------


def verify_request(
    *,
    method: str,
    url: str,
    headers: Mapping[str, str],
    body: str | bytes | None = None,
    key: Callable[[str, str | None], bytes | None],
    now: float | None = None,
    tag: str | None = None,
) -> dict[str, Any]:
    """Checks a request signed by ``sign_request`` or any Web Bot Auth signer that covers what it does.

    The components it names, inside its window, under the key ``key(keyid,
    agent)`` returns (``None`` for a key nobody publishes). ``now`` is
    milliseconds since the epoch. The answer is the TypeScript twin's:
    ``{"ok": True, "keyid", "agent", "from", "created", "components",
    "nonce"}``, or ``{"ok": False, "reason"}``. A receiver that wants who the
    agent is and whose it is asks Pidgeon instead (``POST /v1/verify`` with
    ``request``), which looks the key up and attaches the card.
    """
    lowered = {name.lower(): value for name, value in headers.items()}

    signature_input = lowered.get("signature-input") or ""
    tag = tag if tag is not None else TAG
    member = next((entry for entry in _split_top_level(signature_input) if f"tag={_quote(tag)}" in entry), None)
    if member is None:
        return {"ok": False, "reason": "unsigned"}

    eq = member.find("=")
    label = member[:eq].strip()
    params = member[eq + 1 :].strip()
    listed = re.match(r"^\(([^)]*)\)", params)
    if listed is None:
        return {"ok": False, "reason": "malformed"}
    components = [
        (match.group(1), match.group(2) or "")
        for match in re.finditer(r'"([^"]+)"((?:;[a-z]+(?:="[^"]*")?)*)', listed.group(1))
    ]

    def number(name: str) -> int | None:
        found = re.search(rf";{name}=(\d+)", params)
        return int(found.group(1)) if found else None

    keyid_match = re.search(r';keyid="([^"]+)"', params)
    keyid = keyid_match.group(1) if keyid_match else None
    created = number("created")
    expires = number("expires")
    if not keyid or created is None or expires is None:
        return {"ok": False, "reason": "missing_parameters"}

    current = int((now if now is not None else time.time() * 1000) // 1000)
    if expires <= current:
        return {"ok": False, "reason": "expired"}
    if created > current + 60 or expires - created > 86_400:
        return {"ok": False, "reason": "window"}

    found = re.search(rf"(?:^|,)\s*{re.escape(label)}=:([^:]+):", lowered.get("signature") or "")
    if not found:
        return {"ok": False, "reason": "malformed"}
    signature = found.group(1)

    parts = url_parts(url)

    def value(name: str, component_params: str) -> str | None:
        derived = {
            "@method": method.upper(),
            "@authority": parts.host,
            "@path": parts.pathname,
            "@query": parts.search or "?",
            "@target-uri": parts.href,
        }
        if name in derived:
            return derived[name]
        raw = lowered.get(name)
        if raw is None:
            return None
        raw = raw.strip()
        member_key = re.search(r';key="([^"]+)"', component_params)
        if not member_key:
            return raw
        entry = re.search(rf'(?:^|,)\s*{re.escape(member_key.group(1))}=("[^"]*")', raw)
        return entry.group(1) if entry else None

    lines: list[str] = []
    for name, component_params in components:
        found_value = value(name, component_params)
        if found_value is None:
            return {"ok": False, "reason": "missing_component"}
        lines.append(f"{_quote(name)}{component_params}: {found_value}")
    lines.append(f'"@signature-params": {params}')

    agent_raw = lowered.get("signature-agent")
    agent_raw = agent_raw.strip() if agent_raw is not None else None
    agent_match = re.search(r'"([^"]+)"', agent_raw) if agent_raw else None
    agent = agent_match.group(1) if agent_match else None
    public_key = key(keyid, agent)
    if not public_key:
        return {"ok": False, "reason": "unknown_key"}
    if not verify_bytes(public_key, "\n".join(lines).encode("utf-8"), from_b64(signature)):
        return {"ok": False, "reason": "bad_signature"}

    names = [name for name, _ in components]
    # As in TypeScript, an empty string is no body, while empty bytes are one.
    has_body = body is not None and (not isinstance(body, str) or body != "")
    if "content-digest" in names and has_body:
        if lowered.get("content-digest") != content_digest(body):  # type: ignore[arg-type]
            return {"ok": False, "reason": "body_changed"}

    sender = None
    if "from" in names and lowered.get("from") is not None:
        sender = lowered["from"].strip().lower()
    nonce = re.search(r';nonce="([^"]+)"', params)
    return {
        "ok": True,
        "keyid": keyid,
        "agent": agent,
        "from": sender,
        "created": created,
        "components": names,
        "nonce": nonce.group(1) if nonce else None,
    }


def _split_top_level(value: str) -> list[str]:
    """``label=(components);params`` members: commas outside quotes and parentheses."""
    out: list[str] = []
    depth = 0
    quoted = False
    start = 0
    for i, c in enumerate(value):
        if c == '"' and (i == 0 or value[i - 1] != "\\"):
            quoted = not quoted
        elif not quoted and c == "(":
            depth += 1
        elif not quoted and c == ")":
            depth -= 1
        elif not quoted and depth == 0 and c == ",":
            out.append(value[start:i].strip())
            start = i + 1
    if value[start:].strip():
        out.append(value[start:].strip())
    return out
