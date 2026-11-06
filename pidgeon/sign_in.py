"""Sign in with Pidgeon, for a website written in Python.

The Python twin of ``@pidgeon-ai/sign-in`` (``packages/sign-in/src/index.ts``):
the few routes a site needs so that verified AI agents sign up and sign in
with no password, no CAPTCHA and no person present, and people sign in the
ordinary way, as the one their agents act for. Pidgeon is a standard OpenID
Connect provider; this is the site's half.

**Hand-written, and it stays through regeneration**, like ``webhooks.py``:
``openapi-python-client`` rewrites ``api/``, ``models/`` and ``client.py`` and
leaves this alone.

**An agent** posts an RFC 7523 JWT-bearer grant to ``POST {base}/token``: the
ID token Pidgeon issued for this site, in a request signed with the agent's
key (HTTP Message Signatures, Web Bot Auth's profile). The ID token names that
key in ``cnf``, so a copy of it is useless to anyone else; the signature must
cover ``@method``, ``@authority``, ``@path`` and ``content-digest``, so it
holds for this request to this site and this body only; and its ``jti`` is
accepted once. ``GET {base}/token`` tells an agent the issuer and
``client_id``.

**A person** follows ``GET {base}/login`` (the button), signs in at Pidgeon,
and comes back to ``GET {base}/callback``: the authorization code flow with
PKCE and a nonce.

Either way the answer is a session: a cookie for the browser, a bearer token
for the agent, both read by :meth:`PidgeonSignIn.session`.

The verification rules are the TypeScript ones, check for check and message
for message, and ``tests/unit/python-sign-in.test.ts`` holds the two to the
same verdict on the same requests. Sessions are sealed the same way, so a
site moving between the two keeps its sessions.

Python sites run Django, Flask or FastAPI, so instead of adapters the core
takes a request as plain values and answers one::

    answer = pidgeon.handle(method, url, headers, body)   # None: not ours
    answer.status, answer.headers, answer.body

Flask::

    from flask import Flask, Response, abort, request
    from pidgeon.sign_in import pidgeon_sign_in

    pidgeon = pidgeon_sign_in(client_id="...", url="https://shop.example", secret=SECRET)

    @app.route("/api/auth/pidgeon/<action>", methods=["GET", "POST"])
    def pidgeon_routes(action):
        answer = pidgeon.handle(request.method, request.url, request.headers.items(), request.get_data())
        if answer is None:
            abort(404)
        return Response(answer.body, answer.status, answer.headers)

    session = pidgeon.session(request.headers.items())   # anywhere else; None when signed out

FastAPI (``handle`` makes blocking calls to Pidgeon, so it runs in the thread
pool)::

    from fastapi import FastAPI, HTTPException, Request, Response
    from starlette.concurrency import run_in_threadpool

    @app.api_route("/api/auth/pidgeon/{action}", methods=["GET", "POST"])
    async def pidgeon_routes(request: Request):
        answer = await run_in_threadpool(
            pidgeon.handle, request.method, str(request.url), request.headers.items(), await request.body()
        )
        if answer is None:
            raise HTTPException(404)
        response = Response(answer.body, answer.status)
        for name, value in answer.headers:
            response.headers.append(name, value)
        return response

The body must be the bytes the agent sent: the signature covers them. Read it
raw, before any form parser.

Where it differs from the TypeScript, deliberately: it is synchronous;
``replay`` stores are synchronous; ``http_client`` (an ``httpx.Client``)
stands in for ``fetch``; and input the TypeScript would crash on with a 500
(an ID token whose header is ``null``, a malformed key in the JWKS) is
refused here with the same refusal its neighbours get.
"""

from __future__ import annotations

import base64
import hashlib
import hmac
import json
import math
import re
import secrets
import time
from collections.abc import Callable, Iterable, Mapping
from dataclasses import dataclass, field
from typing import Any, Protocol
from urllib.parse import parse_qsl, quote, quote_plus, urlencode, urljoin, urlsplit

import httpx

__all__ = [
    "JWT_BEARER",
    "PIDGEON_ISSUER",
    "PidgeonSignIn",
    "ReplayStore",
    "SignInRefused",
    "SignInResponse",
    "acts_for",
    "jwk_thumbprint",
    "memory_replay_store",
    "pidgeon_sign_in",
    "sign_in_button_html",
]

JWT_BEARER = "urn:ietf:params:oauth:grant-type:jwt-bearer"
#: Pidgeon's production issuer.
PIDGEON_ISSUER = "https://post.pidgeon.email"

SESSION_COOKIE = "pidgeon_session"
FLOW_COOKIE = "pidgeon_flow"
SKEW = 60

#: Web Bot Auth's tag, which the agent's request signature carries.
_TAG = "web-bot-auth"

Headers = Mapping[str, Any] | Iterable[tuple[str, Any]]


class SignInRefused(Exception):
    """A sign-in this site will not accept: ``code`` is the OAuth error, ``status`` the HTTP status."""

    def __init__(self, code: str, message: str, status: int = 400) -> None:
        super().__init__(message)
        self.code = code
        self.message = message
        self.status = status


class ReplayStore(Protocol):
    """Remembers an ID token's ``jti`` until it expires; ``False`` when it was already used."""

    def use(self, jti: Any, expires_at: float) -> bool: ...


@dataclass
class SignInResponse:
    """What the site answers: hand it to the framework as it is."""

    status: int
    #: A list, not a dict: a sign-in sets two cookies.
    headers: list[tuple[str, str]] = field(default_factory=list)
    body: bytes = b""

    def header(self, name: str) -> str | None:
        for key, value in self.headers:
            if key.lower() == name.lower():
                return value
        return None

    def json(self) -> Any:
        return json.loads(self.body)


# --- Encoding ---------------------------------------------------------------------


def _b64url(data: bytes | str) -> str:
    raw = data.encode("utf-8") if isinstance(data, str) else data
    return base64.urlsafe_b64encode(raw).rstrip(b"=").decode("ascii")


def _from_b64url(text: str) -> bytes:
    """Lenient, like Node's ``base64url``: no padding needed. Raises ``ValueError`` on what cannot be bytes."""
    try:
        cleaned = text.strip().rstrip("=")
        return base64.urlsafe_b64decode(cleaned + "=" * (-len(cleaned) % 4))
    except Exception as cause:  # binascii.Error is a ValueError; anything else is too
        raise ValueError("not base64url") from cause


def _json_dumps(value: Any) -> str:
    """``JSON.stringify``: compact, Unicode as itself."""
    return json.dumps(value, separators=(",", ":"), ensure_ascii=False)


def _json_parse(data: bytes) -> Any:
    """``JSON.parse`` of bytes decoded as UTF-8, which has no ``NaN``."""

    def refuse(name: str) -> Any:
        raise ValueError(name)

    return json.loads(data.decode("utf-8", errors="replace"), parse_constant=refuse)


def _is_number(value: Any) -> bool:
    return isinstance(value, (int, float)) and not isinstance(value, bool)


def _truthy(value: Any) -> bool:
    """JavaScript's truthiness: an empty list or object is true there."""
    if value is None or value is False:
        return False
    if isinstance(value, (list, dict)):
        return True
    if _is_number(value):
        return value != 0 and not (isinstance(value, float) and math.isnan(value))
    if isinstance(value, str):
        return value != ""
    return bool(value)


def _js_string(value: Any) -> str:
    if value is None:
        return "null"
    if value is True:
        return "true"
    if value is False:
        return "false"
    if isinstance(value, str):
        return value
    if isinstance(value, list):
        return ",".join("" if item is None else _js_string(item) for item in value)
    if isinstance(value, dict):
        return "[object Object]"
    if isinstance(value, float) and value.is_integer():
        return str(int(value))
    return str(value)


def _encode_uri_component(value: str) -> str:
    return quote(value, safe="-_.!~*'()")


def _form(values: Mapping[str, str]) -> str:
    """``URLSearchParams``' encoding."""
    return urlencode(values, quote_via=quote_plus, safe="*-._")


def _first(pairs: list[tuple[str, str]], name: str) -> str | None:
    for key, value in pairs:
        if key == name:
            return value
    return None


def _query(url: str) -> list[tuple[str, str]]:
    return parse_qsl(urlsplit(url).query, keep_blank_values=True)


def _normalize_headers(headers: Headers | None) -> dict[str, str]:
    """Lower-cased names, trimmed values, repeats joined with ``, ``: what a ``Headers`` holds."""
    out: dict[str, str] = {}
    if headers is None:
        return out
    pairs = headers.items() if isinstance(headers, Mapping) else headers
    for name, value in pairs:
        key = str(name).lower()
        text = (value.decode("latin-1") if isinstance(value, bytes) else str(value)).strip(" \t\r\n")
        out[key] = f"{out[key]}, {text}" if key in out else text
    return out


def _cookies(headers: Mapping[str, str]) -> dict[str, str]:
    from urllib.parse import unquote

    out: dict[str, str] = {}
    for part in headers.get("cookie", "").split(";"):
        eq = part.find("=")
        if eq > 0:
            out[part[:eq].strip()] = unquote(part[eq + 1 :].strip())
    return out


# --- Exports --------------------------------------------------------------------------


def jwk_thumbprint(x: str) -> str:
    """RFC 7638: the key's thumbprint, which Web Bot Auth uses as ``keyid``."""
    return _b64url(hashlib.sha256(f'{{"crv":"Ed25519","kty":"OKP","x":"{x}"}}'.encode()).digest())


class _MemoryReplayStore:
    def __init__(self, now: Callable[[], float]) -> None:
        self._now = now
        self._seen: dict[Any, float] = {}

    def use(self, jti: Any, expires_at: float) -> bool:
        at = self._now()
        for key, until in list(self._seen.items()):
            if until < at:
                del self._seen[key]
        if jti in self._seen:
            return False
        self._seen[jti] = expires_at + SKEW
        return True


def memory_replay_store(now: Callable[[], float] | None = None) -> ReplayStore:
    """An in-memory ``ReplayStore``: right for one process; several need a shared one (Redis, the database)."""
    return _MemoryReplayStore(now or (lambda: math.floor(time.time())))


def acts_for(claims: Mapping[str, Any]) -> str | None:
    """Who an agent acts for here: its grant's grantor, else what its card says, else nobody named."""
    grant = claims.get("grant")
    grantor = grant.get("grantor") if isinstance(grant, Mapping) else None
    if _truthy(grantor) and isinstance(grantor, Mapping):
        return grantor.get("email") if grantor.get("type") == "person" else grantor.get("domain")
    return claims.get("on_behalf_of")


#: Sign in with Pidgeon's symbol, the Pidgeon figure, as an SVG path: the
#: TypeScript's ``PIDGEON_FIGURE``, and ``compactSpiralPath()`` in the app
#: (design-language decision 42). ``sign-in-button.test.ts`` holds all three equal.
PIDGEON_FIGURE = "M177.7 141.3L182.0 128.2L184.1 114.8L184.1 101.5L182.0 88.5L178.0 76.2L172.1 64.8L164.7 54.7L155.9 46.1L146.0 39.0L135.2 33.7L124.0 30.2L112.6 28.6L101.2 28.8L90.3 30.8L79.9 34.4L70.5 39.5L62.1 45.9L55.0 53.4L49.3 61.8L45.1 70.8L42.5 80.2L41.4 89.7L41.8 99.0L43.6 107.9L46.8 116.3L51.1 123.8L56.5 130.4L62.7 136.0L69.6 140.3L76.9 143.4L84.4 145.3L91.9 145.9L99.2 145.3L106.1 143.6L112.5 140.9L118.2 137.3L123.0 132.9L127.0 128.0L130.0 122.6L132.0 117.0L133.1 111.4L133.2 105.9L132.4 100.6L130.8 95.7L128.5 91.3L125.6 87.5L122.3 84.4L118.7 82.0L114.8 80.3L111.0 79.4L107.2 79.1L103.6 79.6L100.3 80.5L97.5 82.0L95.1 83.9L93.2 86.0L91.8 88.3L91.0 90.6"


def sign_in_button_html(href: str = "/api/auth/pidgeon/login", label: str = "Sign in with Pidgeon") -> str:
    """The button, as HTML, for a page with no framework."""

    def escape(value: str) -> str:
        return re.sub(r'[&<>"]', lambda m: {"&": "&amp;", "<": "&lt;", ">": "&gt;", '"': "&quot;"}[m.group(0)], value)

    return (
        f'<a href="{escape(href)}" class="pidgeon-sign-in" style="display:inline-flex;align-items:baseline;'
        "gap:.3em;padding:.6em 1em;border:1px solid currentColor;border-radius:.5em;font:inherit;"
        f'text-decoration:none;color:inherit">'
        f'<svg viewBox="31.3 18.4 163.1 137.6" width="0.863em" height="0.728em" aria-hidden="true" fill="none" style="flex:none;overflow:visible"><path d="{PIDGEON_FIGURE}" stroke="currentColor" stroke-width="20" stroke-linecap="round" stroke-linejoin="round"/></svg>'
        f"{escape(label)}</a>"
    )


def _origin_of(url: str) -> str | None:
    """A URL's origin as WHATWG URL writes it: scheme, lower-cased host, port unless the default."""
    parts = urlsplit(url)
    if not parts.scheme or not parts.hostname:
        return None
    try:
        port = parts.port
    except ValueError:
        return None
    default = {"http": 80, "https": 443}.get(parts.scheme.lower())
    host = f"[{parts.hostname}]" if ":" in parts.hostname else parts.hostname
    return f"{parts.scheme.lower()}://{host}" + (f":{port}" if port is not None and port != default else "")


def _same_origin(url: Any, issuer: str) -> bool:
    if not isinstance(url, str):
        return False
    origin = _origin_of(url)
    return origin is not None and origin == _origin_of(issuer)


def _safe_path(value: str | None) -> str | None:
    """A path on this site, never another origin."""
    if value and value.startswith("/") and not value.startswith("//") and "\\" not in value:
        return value
    return None


def _summary(claims: Mapping[str, Any]) -> dict[str, Any]:
    """What the site's answer tells the agent back: who it signed in as."""
    grant = claims.get("grant")
    scope = grant.get("scope") if isinstance(grant, Mapping) else None
    return {
        "sub": claims.get("sub"),
        "address": claims.get("email"),
        "acts_for": acts_for(claims),
        "scope": scope,
    }


# --- The agent's request signature (``@pidgeon-ai/id``'s ``verifyRequest``) --------------


def _quote(value: str) -> str:
    return '"' + value.replace("\\", "\\\\").replace('"', '\\"') + '"'


def _content_digest(body: bytes) -> str:
    return "sha-256=:" + base64.b64encode(hashlib.sha256(body).digest()).decode("ascii") + ":"


def _split_top_level(value: str) -> list[str]:
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


class _Url:
    """The parts of a URL the signature reads, as the WHATWG parser gives them."""

    def __init__(self, url: str) -> None:
        parts = urlsplit(url)
        self.scheme = parts.scheme.lower()
        host = (parts.hostname or "").lower()
        self.hostname = f"[{host}]" if ":" in host else host
        port = parts.port
        default = (self.scheme == "https" and port == 443) or (self.scheme == "http" and port == 80)
        self.port = "" if port is None or default else str(port)
        self.pathname = parts.path or "/"
        self.search = f"?{parts.query}" if parts.query else ""

    @property
    def authority(self) -> str:
        return f"{self.hostname}:{self.port}" if self.port else self.hostname

    @property
    def href(self) -> str:
        return f"{self.scheme}://{self.authority}{self.pathname}{self.search}"


def _verify_ed25519(public_key: bytes, message: bytes, signature: bytes) -> bool:
    from cryptography.exceptions import InvalidSignature
    from cryptography.hazmat.primitives.asymmetric.ed25519 import Ed25519PublicKey

    try:
        Ed25519PublicKey.from_public_bytes(public_key).verify(signature, message)
        return True
    except (InvalidSignature, ValueError, TypeError):
        return False


def _verify_request(
    *,
    method: str,
    url: str,
    headers: Mapping[str, str],
    body: bytes,
    key: Callable[[str, str | None], bytes | None],
    now: float,
    tag: str = _TAG,
) -> dict[str, Any]:
    """RFC 9421 as Web Bot Auth profiles it: the same checks, in the same order, as ``verifyRequest``."""
    signature_input = headers.get("signature-input", "")
    member = next((entry for entry in _split_top_level(signature_input) if f"tag={_quote(tag)}" in entry), None)
    if member is None:
        return {"ok": False, "reason": "unsigned"}

    eq = member.find("=")
    label = member[:eq].strip() if eq >= 0 else member[:-1].strip()
    params = member[eq + 1 :].strip() if eq >= 0 else member.strip()
    listed = re.match(r"^\(([^)]*)\)", params)
    if listed is None:
        return {"ok": False, "reason": "malformed"}
    components = [
        (match.group(1), match.group(2) or "")
        for match in re.finditer(r'"([^"]+)"((?:;[a-z]+(?:="[^"]*")?)*)', listed.group(1))
    ]

    def number(name: str) -> int | None:
        found = re.search(f";{name}=([0-9]+)", params)
        return int(found.group(1)) if found else None

    keyid_match = re.search(r';keyid="([^"]+)"', params)
    keyid = keyid_match.group(1) if keyid_match else None
    created = number("created")
    expires = number("expires")
    if not keyid or created is None or expires is None:
        return {"ok": False, "reason": "missing_parameters"}

    at = math.floor(now)
    if expires <= at:
        return {"ok": False, "reason": "expired"}
    if created > at + 60 or expires - created > 86_400:
        return {"ok": False, "reason": "window"}

    found_signature = re.search(f"(?:^|,)\\s*{re.escape(label)}=:([^:]+):", headers.get("signature", ""))
    if found_signature is None:
        return {"ok": False, "reason": "malformed"}

    target = _Url(url)

    def value(name: str, component_params: str) -> str | None:
        derived = {
            "@method": method.upper(),
            "@authority": target.authority,
            "@path": target.pathname,
            "@query": target.search or "?",
            "@target-uri": target.href,
        }
        if name in derived:
            return derived[name]
        raw = headers.get(name)
        if raw is None:
            return None
        raw = raw.strip()
        dictionary_key = re.search(r';key="([^"]+)"', component_params)
        if dictionary_key is None:
            return raw
        member_value = re.search(f'(?:^|,)\\s*{re.escape(dictionary_key.group(1))}=("[^"]*")', raw)
        return member_value.group(1) if member_value else None

    lines: list[str] = []
    for name, component_params in components:
        found = value(name, component_params)
        if found is None:
            return {"ok": False, "reason": "missing_component"}
        lines.append(f"{_quote(name)}{component_params}: {found}")
    lines.append(f'"@signature-params": {params}')

    agent_raw = headers.get("signature-agent")
    agent_match = re.search(r'"([^"]+)"', agent_raw.strip()) if agent_raw else None
    agent = agent_match.group(1) if agent_match else None
    public_key = key(keyid, agent)
    if not public_key:
        return {"ok": False, "reason": "unknown_key"}
    try:
        signature = base64.b64decode(found_signature.group(1) + "=" * (-len(found_signature.group(1)) % 4))
    except ValueError:
        signature = b""
    if not _verify_ed25519(public_key, "\n".join(lines).encode("utf-8"), signature):
        return {"ok": False, "reason": "bad_signature"}

    names = [name for name, _ in components]
    if "content-digest" in names and body:
        if headers.get("content-digest") != _content_digest(body):
            return {"ok": False, "reason": "body_changed"}

    sender = headers.get("from")
    nonce = re.search(r';nonce="([^"]+)"', params)
    return {
        "ok": True,
        "keyid": keyid,
        "agent": agent,
        "from": sender.strip().lower() if "from" in names and sender is not None else None,
        "created": created,
        "components": names,
        "nonce": nonce.group(1) if nonce else None,
    }


# --- The site -------------------------------------------------------------------------


class PidgeonSignIn:
    """The site's routes and sessions. Make one per process and keep it: it caches Pidgeon's keys."""

    def __init__(
        self,
        *,
        client_id: str,
        url: str,
        secret: str,
        issuer: str | None = None,
        issuers: Iterable[str] | None = None,
        base_path: str | None = None,
        after_sign_in: str | None = None,
        session_seconds: int | None = None,
        replay: ReplayStore | None = None,
        on_sign_in: Callable[[dict[str, Any]], None] | None = None,
        http_client: httpx.Client | None = None,
        now: Callable[[], float] | None = None,
    ) -> None:
        """
        ``client_id``: the site's ``client_id`` at Pidgeon, from registering it.
        ``url``: the site's origin, as agents and browsers reach it: ``https://shop.example``.
        ``secret``: at least 32 characters; signs the session and the sign-in in progress.
        ``issuer``: Pidgeon's issuer, default :data:`PIDGEON_ISSUER`. A person signs in here.
        ``issuers``: more issuers whose agents may sign in, beside ``issuer``: a company's own,
        self-hosted, as ``https://post.acme.com``. Only these are ever contacted; an ID token
        from any other is refused before anything is fetched. Default none.
        ``base_path``: where the routes live, default ``/api/auth/pidgeon``.
        ``after_sign_in``: where a person lands after signing in, default ``/``.
        ``session_seconds``: how long a session lasts, default a day.
        ``replay``: where used ``jti`` s are kept; the default is this process's memory.
        ``on_sign_in``: called once per sign-in, before the session is made: create the
        account here. Raise :class:`SignInRefused` to refuse.
        ``now``: seconds since the epoch, for tests.
        """
        if not secret or len(secret) < 32:
            raise ValueError("Sign in with Pidgeon needs a secret of 32 characters or more.")
        self.client_id = client_id
        self.url = url
        self.secret = secret
        self.issuer = re.sub(r"/$", "", issuer if issuer is not None else PIDGEON_ISSUER)
        #: Every issuer an agent may sign in from: ``issuer`` first, then ``issuers``.
        self.issuers: list[str] = list(dict.fromkeys([self.issuer, *(re.sub(r"/$", "", i) for i in issuers or [])]))
        self.base_path = re.sub(r"/$", "", base_path if base_path is not None else "/api/auth/pidgeon")
        self.after_sign_in = after_sign_in
        self.session_seconds = session_seconds if session_seconds is not None else 86_400
        self.on_sign_in = on_sign_in
        self._http = http_client or httpx.Client(follow_redirects=True)
        self._now = now or (lambda: math.floor(time.time()))
        self.replay = replay if replay is not None else memory_replay_store(self._now)
        self._discovery: dict[str, tuple[float, dict[str, Any]]] = {}
        self._keys: dict[str, tuple[float, dict[str, str]]] = {}

    @property
    def _origin(self) -> str:
        return re.sub(r"/$", "", self.url)

    @property
    def login_url(self) -> str:
        """The button's link."""
        return f"{self.base_path}/login"

    @property
    def token_url(self) -> str:
        """Where an agent signs in, absolute: what to tell agents, and what ``GET`` describes."""
        return f"{self._origin}{self.base_path}/token"

    @property
    def redirect_uri(self) -> str:
        return f"{self._origin}{self.base_path}/callback"

    # --- The routes ---------------------------------------------------------------

    def handle(
        self, method: str, url: str, headers: Headers | None = None, body: bytes | str = b""
    ) -> SignInResponse | None:
        """Answers a request under ``base_path``, or ``None`` for anything else.

        ``url`` is the request's URL, absolute or just its path and query;
        ``headers`` any mapping or list of pairs; ``body`` the raw bytes.
        """
        path = urlsplit(url).path
        if not path.startswith(f"{self.base_path}/"):
            return None
        action = path[len(self.base_path) + 1 :]
        verb = method.upper()
        normalized = _normalize_headers(headers)
        raw = body.encode("utf-8") if isinstance(body, str) else (body or b"")
        try:
            if action == "token" and verb == "GET":
                return self._metadata()
            if action == "token" and verb == "POST":
                return self._agent_token(url, verb, normalized, raw)
            if action == "login" and verb == "GET":
                return self._login(url)
            if action == "callback" and verb == "GET":
                return self._callback(normalized, url)
            if action == "logout":
                return self._logout()
            return None
        except SignInRefused as error:
            return SignInResponse(
                error.status,
                [("content-type", "application/json"), ("cache-control", "no-store")],
                _json_dumps({"error": error.code, "error_description": error.message}).encode("utf-8"),
            )

    def session(self, headers: Headers | None) -> dict[str, Any] | None:
        """The session a request carries: the agent's bearer token or the person's cookie.

        ``{"claims": ..., "exp": ...}``, or ``None``.
        """
        normalized = _normalize_headers(headers)
        header = normalized.get("authorization", "")
        bearer = header[7:].strip() if header.lower().startswith("bearer ") else None
        return self.read_session(bearer if bearer is not None else _cookies(normalized).get(SESSION_COOKIE))

    def read_session(self, token: str | None) -> dict[str, Any] | None:
        """A session token read back, or ``None`` when it is not one of ours or has expired."""
        value = self._unseal(token, "session")
        if isinstance(value, dict) and _is_number(value.get("exp")) and value["exp"] > self._now():
            return value
        return None

    def _metadata(self) -> SignInResponse:
        return SignInResponse(
            200,
            [
                ("content-type", "application/json"),
                ("cache-control", "public, max-age=300"),
                ("access-control-allow-origin", "*"),
            ],
            _json_dumps(
                {
                    "issuer": self.issuer,
                    "issuers": self.issuers,
                    "client_id": self.client_id,
                    "token_endpoint": self.token_url,
                    "grant_types_supported": [JWT_BEARER],
                }
            ).encode("utf-8"),
        )

    def _agent_token(self, url: str, method: str, headers: Mapping[str, str], raw: bytes) -> SignInResponse:
        """The agent: an ID token as a JWT-bearer grant, in a request its key signed."""
        # What `request.text()` gives: UTF-8, a leading BOM dropped, bad bytes replaced.
        text = raw.decode("utf-8-sig", errors="replace")
        form = parse_qsl(text, keep_blank_values=True)
        if _first(form, "grant_type") != JWT_BEARER:
            raise SignInRefused("unsupported_grant_type", f"Use {JWT_BEARER}.")
        assertion = _first(form, "assertion")
        if not assertion:
            raise SignInRefused("invalid_request", "assertion is the ID token from Pidgeon.")

        claims = self.verify_id_token(assertion)
        if claims.get("kind") == "person":
            raise SignInRefused("invalid_grant", "A person signs in through the browser, not here.")
        cnf = claims.get("cnf")
        jwk = cnf.get("jwk") if isinstance(cnf, dict) else None
        x = jwk.get("x") if isinstance(jwk, dict) else None
        if not _truthy(x) or not isinstance(x, str) or jwk.get("kty") != "OKP" or jwk.get("crv") != "Ed25519":
            raise SignInRefused("invalid_grant", "The ID token names no key for the agent.")

        # The same key that Pidgeon checked signs this request to us, covering the token itself.
        target = urlsplit(url)
        thumbprint = jwk_thumbprint(x)

        def key(keyid: str, _agent: str | None) -> bytes | None:
            if keyid != thumbprint:
                return None
            try:
                return _from_b64url(x)
            except ValueError:
                return None

        check = _verify_request(
            method=method,
            url=f"{self._origin}{target.path or '/'}{'?' + target.query if target.query else ''}",
            headers=headers,
            body=text.encode("utf-8"),
            key=key,
            now=self._now(),
        )
        if not check["ok"]:
            raise SignInRefused("invalid_grant", f"The request is not signed by the agent’s key ({check['reason']}).")
        for component in ("@method", "@authority", "@path", "content-digest"):
            if component not in check["components"]:
                raise SignInRefused("invalid_grant", f"The request’s signature must cover {component}.")
        if check["from"] is not None and check["from"] != claims.get("email"):
            raise SignInRefused("invalid_grant", "The request is from another address than the token’s.")

        jti = claims.get("jti")
        usable = isinstance(jti, str) or _is_number(jti)
        if not _truthy(jti) or not usable or not self.replay.use(jti, claims["exp"]):
            raise SignInRefused("invalid_grant", "That ID token has already been used. Get a new one.")

        if self.on_sign_in is not None:
            self.on_sign_in(claims)
        session = self._new_session(claims)
        return SignInResponse(
            200,
            [("content-type", "application/json"), ("cache-control", "no-store")],
            _json_dumps(
                {
                    "access_token": self._seal(session, "session"),
                    "token_type": "Bearer",
                    "expires_in": session["exp"] - self._now(),
                    "agent": _summary(claims),
                }
            ).encode("utf-8"),
        )

    def _login(self, url: str) -> SignInResponse:
        """The person: off to Pidgeon, with PKCE, a state and a nonce kept in a sealed cookie."""
        discovery = self._discover(self.issuer)
        verifier = _b64url(secrets.token_bytes(32))
        flow = {
            "state": _b64url(secrets.token_bytes(16)),
            "nonce": _b64url(secrets.token_bytes(16)),
            "verifier": verifier,
            "returnTo": _safe_path(_first(_query(url), "return_to"))
            or (self.after_sign_in if self.after_sign_in is not None else "/"),
            "exp": self._now() + 600,
        }
        endpoint = urlsplit(str(discovery["authorization_endpoint"]))
        search = _form(
            {
                "response_type": "code",
                "client_id": self.client_id,
                "redirect_uri": self.redirect_uri,
                "scope": "openid email",
                "state": flow["state"],
                "nonce": flow["nonce"],
                "code_challenge": _b64url(hashlib.sha256(verifier.encode("ascii")).digest()),
                "code_challenge_method": "S256",
            }
        )
        location = endpoint._replace(query=search, fragment=endpoint.fragment).geturl()
        return SignInResponse(
            302,
            [("location", location), ("set-cookie", self._cookie(FLOW_COOKIE, self._seal(flow, "flow"), 600))],
        )

    def _callback(self, headers: Mapping[str, str], url: str) -> SignInResponse:
        flow = self._unseal(_cookies(headers).get(FLOW_COOKIE), "flow")
        query = _query(url)
        if (
            not isinstance(flow, dict)
            or not _is_number(flow.get("exp"))
            or flow["exp"] <= self._now()
            or _first(query, "state") != flow.get("state")
        ):
            raise SignInRefused("invalid_request", "That sign-in is not one this site started. Start again.")
        iss = _first(query, "iss")
        if iss and re.sub(r"/$", "", iss) != self.issuer:
            raise SignInRefused("invalid_request", "That answer came from another issuer.")
        error = _first(query, "error")
        if error:
            back = urlsplit(urljoin(self._origin + "/", flow["returnTo"]))
            params = [(k, v) for k, v in parse_qsl(back.query, keep_blank_values=True) if k != "pidgeon_error"]
            params.append(("pidgeon_error", error))
            return SignInResponse(
                302,
                [
                    ("location", f"{back.path or '/'}?{_form_pairs(params)}"),
                    ("set-cookie", self._cookie(FLOW_COOKIE, "", 0)),
                ],
            )

        discovery = self._discover(self.issuer)
        response = self._http.post(
            str(discovery["token_endpoint"]),
            headers={"content-type": "application/x-www-form-urlencoded"},
            content=_form(
                {
                    "grant_type": "authorization_code",
                    "code": _first(query, "code") or "",
                    "code_verifier": flow["verifier"],
                    "client_id": self.client_id,
                    "redirect_uri": self.redirect_uri,
                }
            ),
        )
        try:
            tokens = response.json()
        except ValueError:
            tokens = {}
        if not isinstance(tokens, dict):
            tokens = {}
        if not response.is_success or not _truthy(tokens.get("id_token")):
            described = tokens.get("error_description")
            raise SignInRefused(
                "invalid_grant", _js_string(described) if described is not None else "Pidgeon did not sign you in."
            )
        claims = self.verify_id_token(str(tokens["id_token"]), nonce=flow["nonce"])

        if self.on_sign_in is not None:
            self.on_sign_in(claims)
        return SignInResponse(
            302,
            [
                ("location", flow["returnTo"]),
                ("set-cookie", self._cookie(FLOW_COOKIE, "", 0)),
                (
                    "set-cookie",
                    self._cookie(
                        SESSION_COOKIE, self._seal(self._new_session(claims), "session"), self.session_seconds
                    ),
                ),
            ],
        )

    def _logout(self) -> SignInResponse:
        return SignInResponse(
            302,
            [
                ("location", self.after_sign_in if self.after_sign_in is not None else "/"),
                ("set-cookie", self._cookie(SESSION_COOKIE, "", 0)),
            ],
        )

    # --- The ID token -------------------------------------------------------------

    def verify_id_token(self, token: str, nonce: str | None = None) -> dict[str, Any]:
        """An ID token from Pidgeon, checked: from an issuer this site lists (a person's, from
        ``issuer`` only), signed by a key in that issuer's JWKS (EdDSA), for this site, current,
        and with ``nonce`` when one is given."""
        parts = token.split(".")
        if len(parts) != 3:
            raise SignInRefused("invalid_grant", "That is not an ID token.")
        try:
            header = _json_parse(_from_b64url(parts[0]))
            claims = _json_parse(_from_b64url(parts[1]))
        except ValueError as cause:
            raise SignInRefused("invalid_grant", "That is not an ID token.") from cause
        if not isinstance(claims, dict):
            raise SignInRefused("invalid_grant", "That is not an ID token.")
        if not isinstance(header, dict) or header.get("alg") != "EdDSA" or not _truthy(header.get("kid")):
            raise SignInRefused("invalid_grant", "The ID token is not signed the way Pidgeon signs.")
        # The issuer is chosen from the list before any key is looked for, so an
        # unlisted one is never contacted. A browser's answer comes from ``issuer`` only.
        iss = re.sub(r"/$", "", claims["iss"]) if isinstance(claims.get("iss"), str) else ""
        accepted = [self.issuer] if nonce is not None else self.issuers
        if iss not in accepted:
            raise SignInRefused("invalid_grant", "The ID token is from another issuer.")
        x = self._key(iss, header["kid"])
        signed = False
        if x:
            try:
                signed = _verify_ed25519(_from_b64url(x), f"{parts[0]}.{parts[1]}".encode(), _from_b64url(parts[2]))
            except ValueError:
                signed = False
        if not signed:
            raise SignInRefused("invalid_grant", "The ID token’s signature does not hold.")

        now = self._now()
        aud = claims.get("aud")
        if not (aud == self.client_id or (isinstance(aud, list) and self.client_id in aud)):
            raise SignInRefused("invalid_grant", "The ID token is for another site.")
        exp = claims.get("exp")
        if not _is_number(exp) or exp + SKEW <= now:
            raise SignInRefused("invalid_grant", "The ID token has expired.")
        iat = claims.get("iat")
        if _is_number(iat) and iat > now + SKEW:
            raise SignInRefused("invalid_grant", "The ID token is from the future.")
        if nonce is not None and claims.get("nonce") != nonce:
            raise SignInRefused("invalid_grant", "The ID token is for another sign-in.")
        if not isinstance(claims.get("sub"), str) or not _truthy(claims.get("kind")):
            raise SignInRefused("invalid_grant", "The ID token says nothing about who signed in.")
        return claims

    def _discover(self, issuer: str) -> dict[str, Any]:
        """An issuer's configuration. It must name the issuer it was fetched from (OpenID
        Connect Discovery §4.3) and keep its keys on that issuer's origin, so a host that copies
        another issuer's document cannot point a site at keys of its own."""
        held = self._discovery.get(issuer)
        if held is not None and held[0] > self._now() - 300:
            return held[1]
        response = self._http.get(f"{issuer}/.well-known/openid-configuration")
        if not response.is_success:
            raise RuntimeError(f"{issuer} answered {response.status_code} for its configuration.")
        value = response.json()
        named = value.get("issuer") if isinstance(value, dict) else None
        if not isinstance(named, str) or re.sub(r"/$", "", named) != issuer:
            raise SignInRefused("invalid_grant", f"{issuer}'s configuration names another issuer.")
        if not _same_origin(value.get("jwks_uri"), issuer):
            raise SignInRefused("invalid_grant", f"{issuer}'s keys are not on its own host.")
        self._discovery[issuer] = (self._now(), value)
        return value

    def _key(self, issuer: str, kid: Any) -> str | None:
        """A key from the issuer's JWKS by ``kid``, fetched again once when the ``kid`` is new (a rotation)."""
        now = self._now()
        held = self._keys.get(issuer)
        fresh = held is not None and held[0] > now - 300
        try:
            known = held is not None and kid in held[1]
        except TypeError:  # an unhashable kid
            return None
        if not fresh or not known:
            if fresh and held[0] > now - 10:  # type: ignore[index]
                return None
            discovery = self._discover(issuer)
            response = self._http.get(str(discovery["jwks_uri"]))
            try:
                jwks = response.json()
            except ValueError:
                jwks = {"keys": []}
            listed = jwks.get("keys") if isinstance(jwks, dict) else None
            value: dict[str, str] = {}
            for entry in listed if isinstance(listed, list) else []:
                if (
                    isinstance(entry, dict)
                    and _truthy(entry.get("kid"))
                    and isinstance(entry.get("x"), str)
                    and entry.get("x")
                    and entry.get("kty") == "OKP"
                    and entry.get("crv") == "Ed25519"
                ):
                    value[entry["kid"]] = entry["x"]
            self._keys[issuer] = (self._now(), value)
        return self._keys[issuer][1].get(kid)

    # --- Sessions -----------------------------------------------------------------

    def _new_session(self, claims: dict[str, Any]) -> dict[str, Any]:
        return {"claims": claims, "exp": self._now() + self.session_seconds}

    def _seal(self, value: Any, purpose: str) -> str:
        payload = _b64url(_json_dumps(value))
        return f"{payload}.{self._mac(purpose, payload)}"

    def _unseal(self, token: str | None, purpose: str) -> Any:
        if not token:
            return None
        parts = token.split(".")
        payload = parts[0]
        mac = parts[1] if len(parts) > 1 else ""
        if not payload or not mac:
            return None
        if not hmac.compare_digest(self._mac(purpose, payload).encode("utf-8"), mac.encode("utf-8")):
            return None
        try:
            return _json_parse(_from_b64url(payload))
        except ValueError:
            return None

    def _mac(self, purpose: str, payload: str) -> str:
        digest = hmac.new(self.secret.encode("utf-8"), f"{purpose}.{payload}".encode(), hashlib.sha256).digest()
        return _b64url(digest)

    def _cookie(self, name: str, value: str, max_age: int) -> str:
        secure = "; Secure" if self._origin.startswith("https:") else ""
        path = self.base_path if name == FLOW_COOKIE else "/"
        return f"{name}={_encode_uri_component(value)}; Path={path}; Max-Age={max_age}; HttpOnly; SameSite=Lax{secure}"


def _form_pairs(pairs: list[tuple[str, str]]) -> str:
    return urlencode(pairs, quote_via=quote_plus, safe="*-._")


def pidgeon_sign_in(**options: Any) -> PidgeonSignIn:
    """``PidgeonSignIn(**options)``."""
    return PidgeonSignIn(**options)
