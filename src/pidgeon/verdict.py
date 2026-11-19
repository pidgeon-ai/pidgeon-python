"""
Pidgeon verdicts, for a sign-up hook that cannot see the agent's request
(Supabase's Before User Created, an Auth0 Action, WorkOS Actions).

1. The website's proxy verifies the agent (``Pidgeon(api_key).verify(...)``)
   and gets ``verdict``: what Pidgeon found, signed, for five minutes.
2. The app passes it to the sign-up (Supabase ``options.data``, a hidden
   field, a header).
3. The hook checks it: offline here with ``verify_verdict``, against
   Pidgeon's published keys, or with Pidgeon (``Pidgeon(api_key).check_verdict``),
   which also holds it to your account, spends it once and sees a revocation since.
"""

from __future__ import annotations

import ipaddress
import json
import time
from collections.abc import Mapping
from typing import Any
from urllib.parse import urlsplit

import httpx
from cryptography.exceptions import InvalidSignature
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.asymmetric import padding
from cryptography.hazmat.primitives.asymmetric.rsa import RSAPublicNumbers

from .auth import DEFAULT_ISSUER, _b64url_decode, _int, _jwks, _trim

#: The ``typ`` a verdict carries, and an ID token never does.
VERDICT_TYP = "pidgeon-verdict+jwt"

#: The header a proxy hands the verdict on in, to the app behind it.
VERDICT_HEADER = "pidgeon-verdict"

#: How long a verdict lasts after Pidgeon signs it.
VERDICT_LIFETIME_SECONDS = 300

#: How far clocks between Pidgeon and the hook may disagree.
LEEWAY_SECONDS = 30


class VerdictError(Exception):
    """
    A verdict was not accepted. ``reason``: ``invalid``, ``expired``,
    ``wrong_site``, ``wrong_account``, ``wrong_ip``.
    """

    def __init__(self, reason: str, message: str):
        super().__init__(message)
        self.reason = reason


def canonical_ip(raw: str | None) -> str | None:
    """An address as one form: IPv6 compressed, ``::ffff:1.2.3.4`` as ``1.2.3.4``. None when not one."""
    try:
        address = ipaddress.ip_address((raw or "").strip())
    except ValueError:
        return None
    if isinstance(address, ipaddress.IPv6Address) and address.ipv4_mapped:
        return str(address.ipv4_mapped)
    return address.compressed


def _origin(url: str) -> str:
    parts = urlsplit(url)
    if parts.scheme not in ("http", "https") or not parts.hostname:
        raise ValueError(f"{url!r} is not a site's address.")
    port = parts.port
    default = {"http": 80, "https": 443}[parts.scheme]
    host = parts.hostname if ":" not in parts.hostname else f"[{parts.hostname}]"
    return f"{parts.scheme}://{host}" + (f":{port}" if port and port != default else "")


def verify_verdict(
    token: str,
    origin: str,
    account: str | None = None,
    ip: str | None = None,
    issuer: str = DEFAULT_ISSUER,
    jwks: Mapping[str, Any] | None = None,
    client: httpx.Client | None = None,
) -> dict[str, Any]:
    """
    Check a verdict offline: RS256 with Pidgeon's published key under the
    verdict ``typ``, issued by Pidgeon, for ``origin`` (your site), not
    expired, and, when it names an address and you pass ``ip``, for that
    address. With ``account`` (recommended), also issued to your Pidgeon
    account. Answers the claims; raises ``VerdictError`` otherwise.

    Offline means it cannot be spent: within its five minutes it verifies
    each time it is shown. Where one sign-up per verdict matters, use
    ``Pidgeon(api_key).check_verdict`` instead.
    """
    try:
        header_b64, payload_b64, signature_b64 = token.split(".")
        header = json.loads(_b64url_decode(header_b64))
        claims = json.loads(_b64url_decode(payload_b64))
    except ValueError as error:
        raise VerdictError("invalid", "That is not a verdict.") from error
    if not isinstance(header, dict) or not isinstance(claims, dict):
        raise VerdictError("invalid", "That is not a verdict.")
    if header.get("alg") != "RS256":
        raise VerdictError("invalid", "Verdicts from Pidgeon are RS256.")
    # An ID token shares the key and the issuer; it is never a verdict.
    if header.get("typ") != VERDICT_TYP:
        raise VerdictError("invalid", "That is not a verdict.")
    keys = (jwks or _jwks(issuer, client)).get("keys", [])
    key = next(
        (k for k in keys if k.get("kid") == header.get("kid") and k.get("kty") == "RSA"), None
    )
    if key is None:
        raise VerdictError("invalid", "No published key matches the verdict's kid.")
    public = RSAPublicNumbers(_int(key["e"]), _int(key["n"])).public_key()
    try:
        public.verify(
            _b64url_decode(signature_b64),
            f"{header_b64}.{payload_b64}".encode(),
            padding.PKCS1v15(),
            hashes.SHA256(),
        )
    except InvalidSignature as error:
        raise VerdictError("invalid", "The signature does not hold.") from error
    if claims.get("iss") != _trim(issuer):
        raise VerdictError("invalid", "The verdict is not from this issuer.")
    if not isinstance(claims.get("jti"), str):
        raise VerdictError("invalid", "The verdict names no check.")
    exp = claims.get("exp")
    if not isinstance(exp, (int, float)) or exp + LEEWAY_SECONDS < time.time():
        raise VerdictError("expired", "The verdict has expired.")
    if claims.get("aud") != _origin(origin):
        raise VerdictError("wrong_site", "The verdict is for another site.")
    if account is not None and claims.get("receiver") != account:
        raise VerdictError("wrong_account", "The verdict was issued to another Pidgeon account.")
    if claims.get("ip") and ip and canonical_ip(ip) != claims["ip"]:
        raise VerdictError("wrong_ip", "The verdict is for another address.")
    return claims
