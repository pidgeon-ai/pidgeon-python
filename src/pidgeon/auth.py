"""
Pidgeon Auth: Sign in with Pidgeon (https://pidgeon.ai).

People sign in to your site with any OpenID Connect library pointed at the
issuer ``https://pidgeon.ai``; check the ID token with ``verify_id_token``.

Agents sign in with no person present: ``sign_in_as_agent`` exchanges a
request signed with the agent's Pidgeon key for an ID token for one site.
The agent sends that token with every request it signs
(``Authorization: Bearer <id_token>``), and ``verify_agent_sign_in`` checks
both: the token is Pidgeon's and for you, and the request is signed with the
key the token names (``cnf``), so a copied token is useless on its own.
"""

from __future__ import annotations

import base64
import json
import time
from collections.abc import Mapping
from dataclasses import dataclass
from typing import Any
from urllib.parse import urlencode

import httpx
from cryptography.exceptions import InvalidSignature
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.asymmetric import padding
from cryptography.hazmat.primitives.asymmetric.rsa import RSAPublicNumbers

from .credential import Headers, key_id_of, sign_request, verify_agent_request

DEFAULT_ISSUER = "https://pidgeon.ai"
TOKEN_EXCHANGE = "urn:ietf:params:oauth:grant-type:token-exchange"
AGENT_KEY_TOKEN = "urn:pidgeon:params:oauth:token-type:agent-key"
ID_TOKEN = "urn:ietf:params:oauth:token-type:id_token"
ID_JAG = "urn:ietf:params:oauth:token-type:id-jag"

#: How far clocks may disagree when checking ``exp`` and ``iat``.
LEEWAY_SECONDS = 60


class SignInError(Exception):
    """A sign-in was not accepted. ``reason``: refused, invalid_token, not_an_agent, unsigned or wrong_key."""

    def __init__(self, reason: str, message: str) -> None:
        super().__init__(message)
        self.reason = reason


@dataclass(frozen=True)
class AgentSignIn:
    id_token: str
    expires_in: int


def _trim(issuer: str) -> str:
    return issuer.rstrip("/")


def agent_sign_in_request(
    site: str, private_jwk: Mapping[str, Any], directory: str, issuer: str = DEFAULT_ISSUER
) -> tuple[str, dict[str, str], str]:
    """The agent's token request, signed and ready to send: ``(url, headers, body)``."""
    url = f"{_trim(issuer)}/oauth/token"
    headers = dict(sign_request("POST", url, None, private_jwk, directory))
    headers["content-type"] = "application/x-www-form-urlencoded"
    body = urlencode(
        {
            "grant_type": TOKEN_EXCHANGE,
            "subject_token": key_id_of(private_jwk),
            "subject_token_type": AGENT_KEY_TOKEN,
            "audience": site,
        }
    )
    return url, headers, body


def sign_in_as_agent(
    site: str,
    private_jwk: Mapping[str, Any],
    directory: str,
    issuer: str = DEFAULT_ISSUER,
    client: httpx.Client | None = None,
) -> AgentSignIn:
    """The agent's side: an ID token for one site (its client id), for ten minutes."""
    url, headers, body = agent_sign_in_request(site, private_jwk, directory, issuer)
    http = client or httpx.Client()
    try:
        response = http.post(url, headers=headers, content=body)
    finally:
        if client is None:
            http.close()
    try:
        answer = response.json()
    except ValueError:
        answer = {}
    if response.status_code != 200 or "access_token" not in answer:
        raise SignInError(
            "refused",
            answer.get("error_description") or answer.get("error") or f"HTTP {response.status_code}",
        )
    return AgentSignIn(id_token=answer["access_token"], expires_in=int(answer.get("expires_in", 600)))


def id_jag_request(
    audience: str,
    client_id: str,
    private_jwk: Mapping[str, Any],
    directory: str,
    resource: str | None = None,
    scope: str | None = None,
    issuer: str = DEFAULT_ISSUER,
) -> tuple[str, dict[str, str], str]:
    """The agent's ID-JAG request, signed and ready to send: ``(url, headers, body)``."""
    url = f"{_trim(issuer)}/oauth/token"
    headers = dict(sign_request("POST", url, None, private_jwk, directory))
    headers["content-type"] = "application/x-www-form-urlencoded"
    fields = {
        "grant_type": TOKEN_EXCHANGE,
        "requested_token_type": ID_JAG,
        "subject_token": key_id_of(private_jwk),
        "subject_token_type": AGENT_KEY_TOKEN,
        "audience": audience,
        "client_id": client_id,
    }
    if resource:
        fields["resource"] = resource
    if scope:
        fields["scope"] = scope
    return url, headers, urlencode(fields)


def request_id_jag(
    audience: str,
    client_id: str,
    private_jwk: Mapping[str, Any],
    directory: str,
    resource: str | None = None,
    scope: str | None = None,
    issuer: str = DEFAULT_ISSUER,
    client: httpx.Client | None = None,
) -> str:
    """
    The agent's side, for an MCP server whose authorization server trusts
    Pidgeon: an ID-JAG (five minutes) to present there as a JWT bearer grant.
    """
    url, headers, body = id_jag_request(
        audience, client_id, private_jwk, directory, resource, scope, issuer
    )
    http = client or httpx.Client()
    try:
        response = http.post(url, headers=headers, content=body)
    finally:
        if client is None:
            http.close()
    try:
        answer = response.json()
    except ValueError:
        answer = {}
    if response.status_code != 200 or "access_token" not in answer:
        raise SignInError(
            "refused",
            answer.get("error_description") or answer.get("error") or f"HTTP {response.status_code}",
        )
    return answer["access_token"]


def _b64url_decode(text: str) -> bytes:
    return base64.urlsafe_b64decode(text + "=" * (-len(text) % 4))


def _int(text: str) -> int:
    return int.from_bytes(_b64url_decode(text), "big")


def _jwks(issuer: str, client: httpx.Client | None) -> Mapping[str, Any]:
    http = client or httpx.Client()
    try:
        return http.get(f"{_trim(issuer)}/.well-known/jwks.json").json()
    finally:
        if client is None:
            http.close()


def verify_id_token(
    id_token: str,
    client_id: str,
    issuer: str = DEFAULT_ISSUER,
    nonce: str | None = None,
    jwks: Mapping[str, Any] | None = None,
    client: httpx.Client | None = None,
) -> dict[str, Any]:
    """
    The site's side, for any ID token from Pidgeon: RS256 with Pidgeon's
    published key, issued by Pidgeon, for your client id, not expired, and
    with your ``nonce`` if you sent one. Answers the claims.
    """
    try:
        header_b64, payload_b64, signature_b64 = id_token.split(".")
        header = json.loads(_b64url_decode(header_b64))
        claims = json.loads(_b64url_decode(payload_b64))
    except ValueError as error:
        raise SignInError("invalid_token", "That is not a JWT.") from error
    if header.get("alg") != "RS256":
        raise SignInError("invalid_token", "ID tokens from Pidgeon are RS256.")
    # An ID-JAG (typ oauth-id-jag+jwt) shares the key and the issuer; it is never a sign-in.
    if header.get("typ") != "JWT":
        raise SignInError("invalid_token", "That is not an ID token.")
    keys = (jwks or _jwks(issuer, client)).get("keys", [])
    key = next((k for k in keys if k.get("kid") == header.get("kid") and k.get("kty") == "RSA"), None)
    if key is None:
        raise SignInError("invalid_token", "No published key matches the token's kid.")
    public = RSAPublicNumbers(_int(key["e"]), _int(key["n"])).public_key()
    try:
        public.verify(
            _b64url_decode(signature_b64),
            f"{header_b64}.{payload_b64}".encode(),
            padding.PKCS1v15(),
            hashes.SHA256(),
        )
    except InvalidSignature as error:
        raise SignInError("invalid_token", "The signature does not hold.") from error
    now = time.time()
    audience = claims.get("aud")
    audiences = audience if isinstance(audience, list) else [audience]
    if claims.get("iss") != _trim(issuer):
        raise SignInError("invalid_token", "The token is not from this issuer.")
    if client_id not in audiences:
        raise SignInError("invalid_token", "The token is for another site.")
    if not isinstance(claims.get("exp"), (int, float)) or claims["exp"] + LEEWAY_SECONDS < now:
        raise SignInError("invalid_token", "The token has expired.")
    if nonce is not None and claims.get("nonce") != nonce:
        raise SignInError("invalid_token", "The nonce does not match.")
    return claims


def verify_agent_sign_in(
    method: str,
    url: str | httpx.URL,
    headers: Headers,
    client_id: str,
    issuer: str = DEFAULT_ISSUER,
    jwks: Mapping[str, Any] | None = None,
    client: httpx.Client | None = None,
) -> dict[str, Any]:
    """
    The site's side, for an agent's request: the ID token in
    ``Authorization: Bearer``, and the request signed with the key that
    token names. Answers who the agent is and who stands behind it.
    """
    fields = {k.lower(): v for k, v in (headers.items() if hasattr(headers, "items") else headers)}
    authorization = fields.get("authorization", "")
    if not authorization.lower().startswith("bearer "):
        raise SignInError("unsigned", "Send the ID token as `Authorization: Bearer`.")
    claims = verify_id_token(authorization[7:].strip(), client_id, issuer, jwks=jwks, client=client)
    bound = (claims.get("cnf") or {}).get("jwk")
    if claims.get("kind") != "agent" or not bound:
        raise SignInError("not_an_agent", "This token is not an agent's.")
    bound_kid = key_id_of(bound)
    proof = verify_agent_request(method, url, headers, lambda kid: bound if kid == bound_kid else None)
    if not proof.ok:
        raise SignInError(
            "unsigned" if proof.reason == "unsigned" else "wrong_key",
            "The request must be signed with the key the token was issued to.",
        )
    return claims
