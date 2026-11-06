"""Pidgeon's issuance API (``/api/id``), for an operator with no account.

**The key is the account.** Every request is signed with the operator's key —
HTTP Message Signatures with the tag ``pidgeon-id``, never ``web-bot-auth``,
so a signature an agent made for somebody's API is never one the issuance
API accepts — and the server finds the domain from the ``keyid``. Nothing to
sign up for and no token to leak.

The twin of ``packages/id/src/api.ts``: the same calls, the same bodies to
the byte (they are signed, through ``content-digest``), the same error.
Answers are the API's JSON ``data`` as dictionaries.
"""

from __future__ import annotations

from typing import Any, Literal
from urllib.parse import quote

import httpx

from ._js import b64url, js_stringify
from .http import sign_request
from .keys import Identity

__all__ = ["DEFAULT_ID_URL", "ISSUANCE_TAG", "IdApiError", "IdClient", "rotation_statement"]

ISSUANCE_TAG = "pidgeon-id"
DEFAULT_ID_URL = "https://pidgeon.ai/api/id"


class IdApiError(Exception):
    """An answer from the issuance API that was not a success: its HTTP status, error code and message."""

    def __init__(self, status: int, code: str | None, message: str) -> None:
        super().__init__(message)
        self.status = status
        self.code = code
        self.message = message


def _component(value: str) -> str:
    """``encodeURIComponent``."""
    return quote(value, safe="-_.!~*'()")


class IdClient:
    """Issuance for one domain, signed with its key. ``client`` is the ``httpx.Client`` to send with."""

    def __init__(self, identity: Identity, base_url: str = DEFAULT_ID_URL, client: httpx.Client | None = None) -> None:
        self.identity = identity
        self.base_url = base_url
        self.client = client

    def _call(self, method: str, path: str, body: Any = None) -> Any:
        base = self.base_url[:-1] if self.base_url.endswith("/") else self.base_url
        url = f"{base}{path}"
        text = None if body is None else js_stringify(body)
        headers: dict[str, str] = {"content-type": "application/json"} if text else {}
        headers.update(sign_request(self.identity, method=method, url=url, body=text, tag=ISSUANCE_TAG))

        content = text.encode("utf-8") if text is not None else None
        if self.client is not None:
            response = self.client.request(method, url, headers=headers, content=content)
        else:
            with httpx.Client(follow_redirects=True) as client:
                response = client.request(method, url, headers=headers, content=content)
        try:
            answer = response.json()
        except ValueError:
            answer = None
        if not response.is_success or not isinstance(answer, dict) or "data" not in answer:
            error = answer.get("error") if isinstance(answer, dict) else None
            error = error if isinstance(error, dict) else {}
            raise IdApiError(
                response.status_code,
                error.get("code"),
                message
                if isinstance(message := error.get("message"), str)
                else f"Pidgeon answered {response.status_code}.",
            )
        return answer["data"]

    def claim(self) -> dict[str, Any]:
        """Claim the domain with this key. Idempotent: a second call returns the same records."""
        return self._call(
            "POST", "/domains", {"domain": self.identity.domain, "public_key": b64url(self.identity.public_key)}
        )

    def check(self) -> dict[str, Any]:
        """Look at DNS now; ``verified`` once ``_post`` says this key's id."""
        return self._call("POST", "/domains/check", {"domain": self.identity.domain})

    def issue(
        self, name: str, *, kind: Literal["agent", "service"] | None = None, on_behalf_of: str | None = None
    ) -> dict[str, Any]:
        """An agent card for ``<name>@<domain>``."""
        body: dict[str, Any] = {"name": name}
        if kind is not None:
            body["kind"] = kind
        if on_behalf_of is not None:
            body["on_behalf_of"] = on_behalf_of
        return self._call("POST", "/agents", body)

    def list(self) -> list[dict[str, Any]]:
        return self._call("GET", "/agents")

    def revoke(self, name: str) -> dict[str, Any]:
        return self._call("DELETE", f"/agents/{_component(name)}")

    def grant(
        self,
        *,
        agent: str,
        scope: dict[str, Any],
        subject: dict[str, str],
        audience: str | None = None,
        expires_at: str | None = None,
        grantor: dict[str, str] | None = None,
    ) -> dict[str, Any]:
        """The domain grants one of its own agents, at once.

        What it may do (``scope``), for which customer, account or order
        (``subject``), where (``audience``), until when (``expires_at``, at most
        90 days). With ``grantor={"email": ...}`` a person is asked instead of
        granting as the domain: the answer has a ``consent_url`` for them.
        """
        body: dict[str, Any] = {"agent": agent, "scope": scope, "subject": subject}
        for name, value in (("audience", audience), ("expires_at", expires_at), ("grantor", grantor)):
            if value is not None:
                body[name] = value
        return self._call("POST", "/grants", body)

    def revoke_sign_ins(self, name: str) -> dict[str, Any]:
        """Every token Sign in with Pidgeon issued ``name``, taken back; its card and grants stand."""
        return self._call("DELETE", f"/agents/{_component(name)}/sign-ins")

    def revoke_grant(self, id: str) -> dict[str, Any]:
        return self._call("DELETE", f"/grants/{_component(id)}")

    def rotate(self, next: Identity) -> dict[str, Any]:
        """Publish ``next`` as the domain's key, signed by the current one.

        ``proof`` is ``next``'s own signature over the rotation, so nobody can
        rotate a domain onto a key they do not hold.
        """
        statement = rotation_statement(self.identity.domain, self.identity.kid, next.kid)
        return self._call(
            "POST",
            "/keys",
            {"public_key": b64url(next.public_key), "proof": b64url(next.sign(statement.encode("utf-8")))},
        )


def rotation_statement(domain: str, from_: str, to: str) -> str:
    """What a new key signs to show it is held by whoever asks for it. The server builds the same."""
    return f"pidgeon id rotate\n{domain}\n{from_}\n{to}"
