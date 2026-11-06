"""Sign in with Pidgeon, from the agent's side: no browser, no password, no person present.

1. **At Pidgeon**, an RFC 8693 token exchange signed with the agent's key:
   its card as the subject token, the site's ``client_id`` as the audience,
   and its grant, when it acts under one, in ``Post-Grant``. Out comes an ID
   token for that site, bound to this key.
2. **At the site**, the ID token as an RFC 7523 JWT-bearer grant, signed
   again with the same key, so a copy of the token is no use to anyone else.
   The site answers with its own session.

The site says where both are: ``GET`` on its token endpoint answers its
issuer and ``client_id`` (``@pidgeon-ai/sign-in`` and ``pidgeon.sign_in``
serve it).

An agent whose address is in a Pidgeon account holds no signing key of its
own: we sign its mail. It signs in with ``sign_in_with_api_key`` instead,
sending an API key that can send as the address. **That key goes only to the
issuer the agent names, never to one a site names**, and the ID token is
bound to a key made for this one sign-in, shown to Pidgeon with a DPoP proof
(RFC 9449).

The twin of ``packages/id/src/sign-in.ts``, step for step and check for
check. ``tests/integration/python-sign-in-with-pidgeon.test.ts`` runs it
against the real token endpoint and the real site library.
"""

from __future__ import annotations

import contextlib
import os
import re
import time
from collections.abc import Callable, Iterator, Mapping
from dataclasses import dataclass
from typing import Any
from urllib.parse import quote, quote_plus

import httpx

from ._js import b64url, js_stringify, url_parts
from .http import sign_request
from .keys import Identity, generate_identity

__all__ = [
    "JWT_BEARER",
    "PIDGEON_ISSUER",
    "TOKEN_EXCHANGE",
    "PidgeonSignIn",
    "SignInError",
    "dpop_proof",
    "fetch_card",
    "sign_in_with_api_key",
    "sign_in_with_pidgeon",
    "site_metadata",
]

PIDGEON_ISSUER = "https://post.pidgeon.email"
"""Pidgeon's issuer, the only one an API key is sent to unless the agent says otherwise."""

TOKEN_EXCHANGE = "urn:ietf:params:oauth:grant-type:token-exchange"
JWT_BEARER = "urn:ietf:params:oauth:grant-type:jwt-bearer"
_TOKEN_TYPE_JWT = "urn:ietf:params:oauth:token-type:jwt"


@dataclass(frozen=True)
class PidgeonSignIn:
    """A sign-in that worked."""

    site: dict[str, Any]
    """What the site answered: its session, and what it learned."""
    id_token: str
    """The ID token Pidgeon issued, for reading; the site checked it."""
    access_token: str
    """Pidgeon's userinfo token, for as long as the grant lasts and ten minutes at most."""


class SignInError(Exception):
    """A step that refused: ``site``, ``card`` or ``pidgeon``, with its status and OAuth error code."""

    def __init__(self, step: str, status: int, code: str | None, message: str) -> None:
        super().__init__(message)
        self.step = step
        self.status = status
        self.code = code
        self.message = message


@contextlib.contextmanager
def _http(client: httpx.Client | None) -> Iterator[httpx.Client]:
    """The caller's client, or one of our own that follows redirects, as ``fetch`` does."""
    if client is not None:
        yield client
        return
    with httpx.Client(follow_redirects=True) as own:
        yield own


def _json(response: httpx.Response) -> dict[str, Any]:
    try:
        body = response.json()
    except ValueError:
        return {}
    return body if isinstance(body, dict) else {}


def _form(values: Mapping[str, str]) -> str:
    """``URLSearchParams.toString()``: ``*-._`` and alphanumerics bare, spaces as ``+``."""
    return "&".join(
        f"{quote_plus(name, safe='*').replace('~', '%7E')}={quote_plus(value, safe='*').replace('~', '%7E')}"
        for name, value in values.items()
    )


def _component(value: str) -> str:
    """``encodeURIComponent``."""
    return quote(value, safe="-_.!~*'()")


def _string(value: Any) -> str | None:
    return value if isinstance(value, str) else None


def site_metadata(site: str, client: httpx.Client | None = None) -> dict[str, str]:
    """The site's ``issuer`` and ``client_id``, from ``GET`` on its token endpoint."""
    with _http(client) as http:
        response = http.get(site, headers={"accept": "application/json"})
    body = _json(response)
    if not response.is_success or not isinstance(body.get("issuer"), str) or not isinstance(body.get("client_id"), str):
        raise SignInError("site", response.status_code, None, f"{site} does not offer Sign in with Pidgeon.")
    return {"issuer": body["issuer"], "client_id": body["client_id"], "token_endpoint": site}


def _default_post_host(domain: str) -> str:
    return f"https://post.{domain}"


def fetch_card(agent: str, client: httpx.Client | None = None, post_host: Callable[[str], str] | None = None) -> str:
    """The agent's card (its compact JWS), from its domain's protocol host."""
    parts = agent.split("@")
    domain = parts[1] if len(parts) > 1 else ""
    host = (post_host or _default_post_host)(domain)
    with _http(client) as http:
        response = http.get(f"{host}/.well-known/post/card?address={_component(agent)}")
    body = _json(response)
    if not response.is_success or not isinstance(body.get("jws"), str):
        raise SignInError("card", response.status_code, None, f"{agent} has no card to sign in with.")
    return body["jws"]


def dpop_proof(identity: Identity, method: str, url: str) -> str:
    """RFC 9449 §4.2: a proof that this request comes from whoever holds ``identity``'s key."""
    target = url_parts(url)

    def encode(value: Any) -> str:
        return b64url(js_stringify(value).encode("utf-8"))

    header = encode(
        {"typ": "dpop+jwt", "alg": "EdDSA", "jwk": {"kty": "OKP", "crv": "Ed25519", "x": b64url(identity.public_key)}}
    )
    payload = encode(
        {
            "jti": b64url(os.urandom(16)),
            "htm": method.upper(),
            "htu": f"{target.origin}{target.pathname}",
            "iat": int(time.time()),
        }
    )
    signature = identity.sign(f"{header}.{payload}".encode("ascii"))
    return f"{header}.{payload}.{b64url(signature)}"


# The headers that show Pidgeon who is asking, given the request it will see.
_Authenticate = Callable[[str, str, dict[str, str], str, dict[str, str]], dict[str, str]]


def sign_in_with_pidgeon(
    identity: Identity,
    *,
    agent: str,
    site: str,
    grant: str | None = None,
    card: str | None = None,
    post_host: Callable[[str], str] | None = None,
    delegation: bool = False,
    client: httpx.Client | None = None,
) -> PidgeonSignIn:
    """Signs in to ``site`` (its token endpoint for agents) as ``agent``, with its own key.

    ``grant`` is a grant the agent acts under (its JWS), when it has one for
    this site. ``card`` is the card's compact JWS, fetched from
    ``post.<domain>`` when not given (``post_host`` says where a domain's
    protocol host answers, when not there). ``delegation`` asks for the
    access token as a JWT that says the agent acts for its grantor (RFC 8693
    §4.1: ``sub`` the grantor, ``act`` the agent), for an API to read; it
    needs ``grant``.
    """

    def authenticate(
        token_endpoint: str, exchange: str, headers: dict[str, str], signer: str, _site: dict[str, str]
    ) -> dict[str, str]:
        return sign_request(
            identity,
            method="POST",
            url=token_endpoint,
            headers=headers,
            body=exchange,
            agent=signer,
            grants=[grant] if grant else None,
        )

    return _sign_in(identity, agent, site, grant, card, post_host, delegation, client, authenticate)


def sign_in_with_api_key(
    *,
    agent: str,
    api_key: str,
    site: str,
    issuer: str | None = None,
    grant: str | None = None,
    card: str | None = None,
    post_host: Callable[[str], str] | None = None,
    delegation: bool = False,
    client: httpx.Client | None = None,
) -> PidgeonSignIn:
    """Signs in to ``site`` as an address in a Pidgeon account, with an API key that can send as it.

    The key is sent to ``issuer`` (default ``PIDGEON_ISSUER``) and nowhere
    else: a site that names another issuer is refused before anything is
    sent to it.
    """
    signer = agent.strip().lower()
    parts = signer.split("@")
    # A key for this sign-in only. It never leaves this process.
    ephemeral = generate_identity(parts[1] if len(parts) > 1 else "")
    trusted = re.sub(r"/$", "", issuer if issuer is not None else PIDGEON_ISSUER)

    def authenticate(
        token_endpoint: str, _exchange: str, _headers: dict[str, str], _signer: str, metadata: dict[str, str]
    ) -> dict[str, str]:
        if (
            re.sub(r"/$", "", metadata["issuer"]) != trusted
            or url_parts(token_endpoint).origin != url_parts(trusted).origin
        ):
            raise SignInError(
                "site",
                0,
                "unknown_issuer",
                f"{metadata['token_endpoint']} signs in with {metadata['issuer']}, not {trusted}, "
                "so your API key is not sent there.",
            )
        headers = {"authorization": f"Bearer {api_key}", "dpop": dpop_proof(ephemeral, "POST", token_endpoint)}
        if grant:
            headers["post-grant"] = re.sub(r"\s+", "", grant)
        return headers

    def admit(metadata: dict[str, str]) -> None:
        # Before anything is fetched from it: an issuer the site names is not
        # contacted at all unless it is ours, as the TypeScript does.
        if re.sub(r"/$", "", metadata["issuer"]) != trusted:
            raise SignInError(
                "site",
                0,
                "unknown_issuer",
                f"{metadata['token_endpoint']} signs in with {metadata['issuer']}, not {trusted}, "
                "so your API key is not sent there.",
            )

    return _sign_in(ephemeral, agent, site, grant, card, post_host, delegation, client, authenticate, admit)


def _sign_in(
    identity: Identity,
    agent: str,
    site_url: str,
    grant: str | None,
    card: str | None,
    post_host: Callable[[str], str] | None,
    delegation: bool,
    client: httpx.Client | None,
    authenticate: _Authenticate,
    admit: Callable[[dict[str, str]], None] | None = None,
) -> PidgeonSignIn:
    del grant  # Carried by `authenticate`, which knows how this agent shows it.
    signer = agent.strip().lower()
    with _http(client) as http:
        site = site_metadata(site_url, http)
        if admit is not None:
            admit(site)
        subject_token = card if card is not None else fetch_card(signer, http, post_host)

        # 1. Pidgeon: the card and the grant, for this site, from whoever can show they are the agent.
        discovery = _json(http.get(f"{re.sub(r'/$', '', site['issuer'])}/.well-known/openid-configuration"))
        token_endpoint = discovery.get("token_endpoint")
        if not isinstance(token_endpoint, str):
            raise SignInError("pidgeon", 0, None, f"{site['issuer']} has no token endpoint.")
        values = {
            "grant_type": TOKEN_EXCHANGE,
            "subject_token": subject_token,
            "subject_token_type": _TOKEN_TYPE_JWT,
            "audience": site["client_id"],
        }
        if delegation:
            values["requested_token_type"] = _TOKEN_TYPE_JWT
        exchange = _form(values)
        headers = {"content-type": "application/x-www-form-urlencoded"}
        issued = http.post(
            token_endpoint,
            headers={**headers, **authenticate(token_endpoint, exchange, headers, signer, site)},
            content=exchange.encode("utf-8"),
        )
        tokens = _json(issued)
        if not issued.is_success or not isinstance(tokens.get("id_token"), str):
            description = _string(tokens.get("error_description"))
            raise SignInError(
                "pidgeon",
                issued.status_code,
                _string(tokens.get("error")),
                description if description is not None else f"Pidgeon answered {issued.status_code}.",
            )

        # 2. The site: the ID token as a JWT-bearer grant, signed with the same key.
        bearer = _form({"grant_type": JWT_BEARER, "assertion": tokens["id_token"]})
        answered = http.post(
            site["token_endpoint"],
            headers={
                **headers,
                **sign_request(
                    identity, method="POST", url=site["token_endpoint"], headers=headers, body=bearer, agent=signer
                ),
            },
            content=bearer.encode("utf-8"),
        )
        session = _json(answered)
        if not answered.is_success:
            description = _string(session.get("error_description"))
            raise SignInError(
                "site",
                answered.status_code,
                _string(session.get("error")),
                description if description is not None else f"The site answered {answered.status_code}.",
            )
        return PidgeonSignIn(site=session, id_token=tokens["id_token"], access_token=tokens.get("access_token"))
