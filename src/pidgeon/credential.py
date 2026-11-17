"""
The agent credential: Web Bot Auth, unchanged.

An agent signs each request with its Ed25519 key under HTTP Message
Signatures (RFC 9421), tagged ``web-bot-auth``, covering the request's
authority, method, path and query and the ``Signature-Agent`` header, which points at
its operator's directory on Pidgeon. This module produces exactly what the
TypeScript SDK (Cloudflare's ``web-bot-auth``) produces, byte for byte: the
same key id, the same Signature-Input, and, Ed25519 being deterministic, the
same signature for the same key, request and time.

Choices, each the TypeScript SDK's:

- Ed25519 only, because Cloudflare accepts nothing else.
- ``Signature-Agent`` in the string form (``"https://…"``), which Cloudflare
  requires today; the verifier accepts the working group's dictionary form
  too.
- A minute's lifetime by default, so a captured request is useless soon.
- A fresh nonce in every signature, so a verifier that remembers them accepts
  each signature once.
"""

from __future__ import annotations

import base64
import hashlib
import json
import math
import os
import re
import time
from collections.abc import Callable, Iterable, Mapping
from dataclasses import dataclass
from datetime import datetime, timezone
from typing import Any, Literal, Optional, Union

import httpx
from cryptography.exceptions import InvalidSignature
from cryptography.hazmat.primitives import serialization
from cryptography.hazmat.primitives.asymmetric.ed25519 import Ed25519PrivateKey, Ed25519PublicKey

from . import _sf

__all__ = [
    "DEFAULT_LIFETIME_SECONDS",
    "MAX_LIFETIME_SECONDS",
    "AgentKey",
    "Verification",
    "directory_url",
    "generate_agent_key",
    "is_public_jwk",
    "key_id_of",
    "new_nonce",
    "sign_request",
    "verify_agent_request",
]

#: How long a signature lasts unless the agent asks for less.
DEFAULT_LIFETIME_SECONDS = 60

#: The longest a signature lasts, whatever the signer asks, and the oldest a
#: verifier accepts, whatever its ``expires`` says: five minutes, so a captured
#: request is soon useless. (The draft's own ceiling, a day, left a copied
#: request replayable at the same site all day.)
MAX_LIFETIME_SECONDS = 5 * 60

#: How far an agent's clock may run ahead of the verifier's.
CLOCK_SKEW_SECONDS = 30

TAG = "web-bot-auth"
LABEL = "sig1"

#: What the signature covers, in order: the authority, the Signature-Agent, then ours.
#: The query is covered when the URL has none too (its value is then ``?``), so
#: one cannot be added in transit.
COVERED = ("@authority", "signature-agent", "@method", "@path", "@query")

#: A nonce is 64 random bytes (Web Bot Auth §4.2.2).
NONCE_BYTES = 64

Headers = Union[Mapping[str, Any], Iterable[tuple[str, str]], httpx.Headers, None]
Now = Union[datetime, float, int, None]


def _b64url(data: bytes) -> str:
    return base64.urlsafe_b64encode(data).rstrip(b"=").decode("ascii")


def _b64url_decode(text: str) -> bytes:
    return base64.urlsafe_b64decode(text + "=" * (-len(text) % 4))


def directory_url(slug: str, host: str = "agents.pidgeon.ai") -> str:
    """An operator's directory: where its agents' public keys are published."""
    return f"https://{slug}.{host}"


def key_id_of(jwk: Mapping[str, Any]) -> str:
    """A key's id: its JWK SHA-256 thumbprint (RFC 7638), Web Bot Auth's ``keyid``."""
    required = {"crv": jwk["crv"], "kty": jwk["kty"], "x": jwk["x"]}
    canonical = json.dumps(required, separators=(",", ":"), sort_keys=True, ensure_ascii=False)
    return _b64url(hashlib.sha256(canonical.encode("utf-8")).digest())


_X = re.compile(r"^[A-Za-z0-9_-]{43}$")


def is_public_jwk(value: Any) -> bool:
    """Whether something is an Ed25519 public key, and only that: no private part."""
    return (
        isinstance(value, Mapping)
        and value.get("kty") == "OKP"
        and value.get("crv") == "Ed25519"
        and isinstance(value.get("x"), str)
        and bool(_X.match(value["x"]))
        and "d" not in value
    )


@dataclass(frozen=True)
class AgentKey:
    """Both halves of an agent's key. The private half never reaches Pidgeon."""

    kid: str
    public_jwk: dict[str, str]
    private_jwk: dict[str, str]


def generate_agent_key() -> AgentKey:
    """A new key pair, for an agent. Run it where the agent runs."""
    private = Ed25519PrivateKey.generate()
    d = private.private_bytes(
        serialization.Encoding.Raw, serialization.PrivateFormat.Raw, serialization.NoEncryption()
    )
    x = private.public_key().public_bytes(
        serialization.Encoding.Raw, serialization.PublicFormat.Raw
    )
    public_jwk = {"kty": "OKP", "crv": "Ed25519", "x": _b64url(x)}
    # No "alg": Web Bot Auth wants an Ed25519 JWK's alg to be EdDSA or absent.
    private_jwk = {**public_jwk, "d": _b64url(d)}
    return AgentKey(kid=key_id_of(public_jwk), public_jwk=public_jwk, private_jwk=private_jwk)


def _private_key(jwk: Mapping[str, Any]) -> Ed25519PrivateKey:
    if jwk.get("kty") != "OKP" or jwk.get("crv") != "Ed25519":
        raise ValueError("The agent key must be an Ed25519 JWK (kty OKP, crv Ed25519).")
    if jwk.get("alg") not in (None, "EdDSA"):
        raise ValueError("An Ed25519 JWK's alg must be EdDSA when present.")
    if not isinstance(jwk.get("d"), str) or not isinstance(jwk.get("x"), str):
        raise ValueError("The agent key must be a private JWK, with both x and d.")
    key = Ed25519PrivateKey.from_private_bytes(_b64url_decode(jwk["d"]))
    x = key.public_key().public_bytes(serialization.Encoding.Raw, serialization.PublicFormat.Raw)
    if _b64url(x) != jwk["x"]:
        raise ValueError("The agent key's x is not the public half of its d.")
    return key


def _public_key(jwk: Mapping[str, Any]) -> Ed25519PublicKey:
    if jwk.get("kty") != "OKP" or jwk.get("crv") != "Ed25519" or not isinstance(jwk.get("x"), str):
        raise ValueError("Not an Ed25519 public JWK.")
    if jwk.get("alg") not in (None, "EdDSA"):
        raise ValueError("An Ed25519 JWK's alg must be EdDSA when present.")
    return Ed25519PublicKey.from_public_bytes(_b64url_decode(jwk["x"]))


def _seconds(now: Now) -> float:
    if now is None:
        return time.time()
    if isinstance(now, datetime):
        if now.tzinfo is None:
            now = now.replace(tzinfo=timezone.utc)
        return now.timestamp()
    return float(now)


def _header_map(headers: Headers) -> dict[str, str]:
    """Lower-case names; repeated fields joined with ", ", as RFC 9421 reads them."""
    out: dict[str, list[str]] = {}
    if headers is None:
        return {}
    if isinstance(headers, httpx.Headers):
        pairs: Iterable[tuple[str, Any]] = headers.multi_items()
    elif isinstance(headers, Mapping):
        pairs = headers.items()
    else:
        pairs = headers
    for name, value in pairs:
        if value is None:
            continue
        values = value if isinstance(value, (list, tuple)) else [value]
        for one in values:
            out.setdefault(name.lower(), []).append(str(one).strip())
    return {name: ", ".join(values) for name, values in out.items()}


@dataclass(frozen=True)
class _Target:
    method: str
    authority: str
    scheme: str
    path: str
    query: str
    target_uri: str


def _target(method: str, url: Union[str, httpx.URL]) -> _Target:
    """The derived components of a request, as a WHATWG URL gives them to the TypeScript signer."""
    parsed = url if isinstance(url, httpx.URL) else httpx.URL(str(url))
    if not parsed.scheme or not parsed.host:
        raise ValueError(f"{url} is not an absolute URL.")
    host = parsed.raw_host.decode("ascii").lower()
    if ":" in host:
        host = f"[{host}]"
    authority = host if parsed.port is None else f"{host}:{parsed.port}"
    raw = parsed.raw_path.decode("ascii")
    path, _, query = raw.partition("?")
    return _Target(
        method=method.upper(),
        authority=authority,
        scheme=parsed.scheme,
        path=path or "/",
        query=f"?{query}",
        target_uri=str(parsed.copy_with(fragment=None)),
    )


def _component_value(target: _Target, headers: dict[str, str], item: _sf.Item) -> str:
    name = item.value
    if not isinstance(name, str) or isinstance(name, _sf.Token):
        raise ValueError("Component identifiers must be strings.")
    if name.startswith("@"):
        if item.params:
            raise ValueError(f"Parameters on {name} are not supported.")
        derived = {
            "@method": target.method,
            "@authority": target.authority,
            "@scheme": target.scheme,
            "@path": target.path,
            "@query": target.query,
            "@target-uri": target.target_uri,
        }
        if name not in derived:
            raise ValueError(f"Unsupported derived component {name}.")
        return derived[name]
    if name not in headers:
        raise ValueError(f"Missing field {name}.")
    value = headers[name]
    if not item.params:
        return value
    if set(item.params) != {"key"} or not isinstance(item.params["key"], str):
        raise ValueError(f"Unsupported parameters on {name}.")
    member = _sf.parse_dictionary(value).get(item.params["key"])
    if member is None:
        raise ValueError(f"Field {name} has no member {item.params['key']}.")
    return _sf.serialize_member(member)


def _signature_base(target: _Target, headers: dict[str, str], inner: _sf.InnerList) -> bytes:
    lines = [
        f"{_sf.serialize_item(_sf.Item(item.value, item.params))}: "
        f"{_component_value(target, headers, item)}"
        for item in inner.items
    ]
    lines.append(f'"@signature-params": {_sf.serialize_inner_list(inner)}')
    return "\n".join(lines).encode("ascii")


def new_nonce() -> str:
    """A fresh nonce: 64 random bytes, base64url."""
    return _b64url(os.urandom(NONCE_BYTES))


def _valid_nonce(nonce: object) -> bool:
    """64 bytes, in canonical base64 or unpadded base64url, as the verifier Pidgeon runs accepts."""
    if not isinstance(nonce, str) or isinstance(nonce, _sf.Token):
        return False
    normalized = nonce.replace("-", "+").replace("_", "/")
    try:
        raw = base64.b64decode(normalized + "=" * (-len(normalized) % 4), validate=True)
    except (ValueError, TypeError):
        return False
    return len(raw) == NONCE_BYTES and nonce in (_b64url(raw), base64.b64encode(raw).decode("ascii"))


def sign_request(
    method: str,
    url: Union[str, httpx.URL],
    headers: Headers,
    private_jwk: Mapping[str, Any],
    directory: str,
    lifetime_seconds: float = DEFAULT_LIFETIME_SECONDS,
    now: Now = None,
    nonce: Optional[str] = None,
) -> dict[str, str]:
    """
    Sign a request as an agent: returns the headers to add (``signature-agent``,
    ``signature-input``, ``signature``). Any Signature-Agent the request carries
    is replaced by this one. No other header is covered, so ``headers`` does not
    change the signature. Every signature has a fresh nonce, so sign again for
    each send, retries included; ``nonce`` is for tests that need the same
    bytes twice.
    """
    key = _private_key(private_jwk)
    created_at = _seconds(now)
    lifetime = min(lifetime_seconds, MAX_LIFETIME_SECONDS)
    created = math.floor(created_at)
    expires = math.floor(created_at + lifetime)
    if created > expires:
        raise ValueError("lifetime_seconds must not be negative.")
    if nonce is not None and not _valid_nonce(nonce):
        raise ValueError("nonce must be 64 bytes, base64url or base64.")

    signature_agent = _sf.serialize_bare_item(directory)
    fields = _header_map(headers)
    fields["signature-agent"] = signature_agent

    inner = _sf.InnerList(
        [_sf.Item(name) for name in COVERED],
        {
            "created": created,
            "keyid": key_id_of(private_jwk),
            "alg": "ed25519",
            "expires": expires,
            "nonce": new_nonce() if nonce is None else nonce,
            "tag": TAG,
        },
    )
    base = _signature_base(_target(method, url), fields, inner)
    signature = key.sign(base)
    return {
        "signature-agent": signature_agent,
        "signature-input": _sf.serialize_dictionary({LABEL: inner}),
        "signature": _sf.serialize_dictionary({LABEL: _sf.Item(signature)}),
    }


Rejection = Literal["unsigned", "invalid", "unknown_key", "expired"]


@dataclass(frozen=True)
class Verification:
    """Whether a request's agent signature holds. On ``ok``, ``kid`` is the key that signed it."""

    ok: bool
    reason: Optional[Rejection] = None
    kid: Optional[str] = None
    directory: Optional[str] = None
    created: Optional[datetime] = None
    expires: Optional[datetime] = None
    #: The signature's nonce, when it has one: remember it to refuse the same signature twice.
    nonce: Optional[str] = None
    detail: str = ""


class _Rejected(Exception):
    def __init__(self, reason: Rejection, detail: str) -> None:
        super().__init__(detail)
        self.reason = reason


def _signature_agent(headers: dict[str, str], components: list[_sf.Item]) -> Optional[str]:
    """The directory the signature vouches for, if the request names one."""
    header = headers.get("signature-agent")
    if header is None:
        return None
    try:
        entries = _sf.parse_dictionary(header)
        uris = {
            label: member.value
            for label, member in entries.items()
            if isinstance(member, _sf.Item) and isinstance(member.value, str)
            and not isinstance(member.value, _sf.Token)
        }
        if not entries or len(uris) != len(entries):
            raise _sf.ParseError("not a dictionary of strings")
    except _sf.ParseError:
        item = _sf.parse_item(header)
        if not isinstance(item.value, str) or isinstance(item.value, _sf.Token):
            raise _Rejected("invalid", "Signature-Agent must be a string.")
        if not any(c.value == "signature-agent" and not c.params for c in components):
            raise _Rejected("invalid", "The signature must cover signature-agent.")
        return item.value
    keys = [
        c.params["key"]
        for c in components
        if c.value == "signature-agent" and set(c.params) == {"key"}
        and isinstance(c.params["key"], str)
    ]
    if len(keys) != 1 or keys[0] not in uris:
        raise _Rejected("invalid", "The signature must cover exactly one signature-agent member.")
    return str(uris[keys[0]])


def verify_agent_request(
    method: str,
    url: Union[str, httpx.URL],
    headers: Headers,
    find_key: Callable[[str], Optional[Mapping[str, Any]]],
    *,
    now: Now = None,
) -> Verification:
    """
    Check a request's agent signature. ``find_key`` turns a key id into the
    public JWK published for it, or None; whether that key is revoked, and the
    operator's reputation, are the caller's next questions (``Pidgeon.verify``
    answers both).
    """
    fields = _header_map(headers)
    if "signature" not in fields or "signature-input" not in fields:
        return Verification(ok=False, reason="unsigned", detail="The request carries no agent signature.")

    kid: Optional[str] = None
    try:
        try:
            inputs = _sf.parse_dictionary(fields["signature-input"])
            signatures = _sf.parse_dictionary(fields["signature"])
        except _sf.ParseError as error:
            raise _Rejected("invalid", f"Malformed signature fields: {error}")
        if set(inputs) != set(signatures):
            raise _Rejected("invalid", "Signature and Signature-Input label sets differ.")
        # A proxy may add its own signature (RFC 9421 §4.3): check the web-bot-auth one.
        if len(inputs) == 1:
            label = next(iter(inputs))
        else:
            tagged = [
                name
                for name, member in inputs.items()
                if isinstance(member, _sf.InnerList) and member.params.get("tag") == TAG
            ]
            if not tagged:
                raise _Rejected("invalid", "No signature is tagged web-bot-auth.")
            label = tagged[0]
        inner, signed = inputs[label], signatures[label]
        if not isinstance(inner, _sf.InnerList):
            raise _Rejected("invalid", "Signature-Input members must be inner lists.")
        if not isinstance(signed, _sf.Item) or not isinstance(signed.value, bytes) or signed.params:
            raise _Rejected("invalid", "Signature members must be byte sequences.")
        for component in inner.items:
            name = component.value
            if not isinstance(name, str) or isinstance(name, _sf.Token) or name != name.lower():
                raise _Rejected("invalid", "Component identifiers must be lower-case strings.")

        params = inner.params
        # alg and nonce are optional (draft-ietf-webbotauth-httpsig-protocol-01 §5.2, RFC 9421 §2.3).
        for required in ("created", "expires", "keyid", "tag"):
            if required not in params:
                raise _Rejected("invalid", f"Required parameter {required} is absent.")
        created, expires = params["created"], params["expires"]
        if not all(isinstance(v, int) and not isinstance(v, bool) for v in (created, expires)):
            raise _Rejected("invalid", "created and expires must be integers.")
        assert isinstance(created, int) and isinstance(expires, int)
        at = math.floor(_seconds(now))
        if created > at + CLOCK_SKEW_SECONDS:
            raise _Rejected("expired", "Signature was created in the future.")
        if expires < at - CLOCK_SKEW_SECONDS:
            raise _Rejected("expired", "Signature has expired.")
        if at - created > MAX_LIFETIME_SECONDS + CLOCK_SKEW_SECONDS:
            raise _Rejected("expired", "Signature is too old.")
        if "alg" in params and params["alg"] != "ed25519":
            raise _Rejected("invalid", "Only ed25519 is accepted.")
        if params["tag"] != TAG:
            raise _Rejected("invalid", f"tag must be '{TAG}'.")
        if created > expires:
            raise _Rejected("invalid", "created must not be after expires.")
        if "nonce" in params and (
            not isinstance(params["nonce"], str) or isinstance(params["nonce"], _sf.Token)
        ):
            raise _Rejected("invalid", "nonce must be a string.")
        candidate = params["keyid"]
        if not isinstance(candidate, str) or isinstance(candidate, _sf.Token) or not candidate:
            raise _Rejected("invalid", "keyid must be a non-empty string.")
        kid = candidate
        if not any(c.value in ("@authority", "@target-uri") and not c.params for c in inner.items):
            raise _Rejected("invalid", "The signature must cover bare @authority or @target-uri.")
        directory = _signature_agent(fields, inner.items)

        jwk = find_key(kid)
        if jwk is None:
            raise _Rejected("unknown_key", f"No published key {kid}.")
        if key_id_of(jwk) != kid:
            raise _Rejected("invalid", "The published key's id does not match the signed keyid.")
        try:
            base = _signature_base(_target(method, url), fields, inner)
        except ValueError as error:
            raise _Rejected("invalid", str(error))
        try:
            _public_key(jwk).verify(signed.value, base)
        except (InvalidSignature, ValueError):
            raise _Rejected("invalid", "Signature verification failed.")
        return Verification(
            ok=True,
            kid=kid,
            directory=directory,
            created=datetime.fromtimestamp(created, timezone.utc),
            expires=datetime.fromtimestamp(expires, timezone.utc),
            nonce=params.get("nonce") if isinstance(params.get("nonce"), str) else None,
        )
    except _Rejected as rejected:
        return Verification(
            ok=False,
            reason=rejected.reason,
            kid=kid if rejected.reason == "unknown_key" else None,
            detail=str(rejected),
        )
