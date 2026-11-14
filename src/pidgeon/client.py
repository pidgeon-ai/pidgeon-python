"""
The Pidgeon API client, and httpx clients that sign as an agent.
"""

from __future__ import annotations

import json
import os
from collections.abc import Generator, Mapping
from dataclasses import dataclass
from typing import Any, Literal, Optional, Union
from urllib.parse import quote

import httpx

from .credential import (
    DEFAULT_LIFETIME_SECONDS,
    AgentKey,
    Headers,
    _header_map,
    generate_agent_key,
    sign_request,
)

DEFAULT_BASE_URL = "https://pidgeon.ai"

Band = Literal["unverified", "new", "good", "flagged", "suspended"]
ReportCategory = Literal["fraud", "abuse", "scraping", "spam", "fake_signups", "other"]
InboxKind = Literal["person", "shared", "agent", "events"]


class PidgeonError(Exception):
    """The API refused: ``status`` is the HTTP status, ``code`` the API's error code."""

    def __init__(self, status: int, code: str, message: str) -> None:
        super().__init__(message)
        self.status = status
        self.code = code
        self.message = message

    def __repr__(self) -> str:
        return f"PidgeonError(status={self.status!r}, code={self.code!r}, message={self.message!r})"


Json = dict[str, Any]
# Spelled out once: inside a class with a ``list`` method, ``list[str]`` names the method.
_Strings = list[str]


def _drop_none(body: Mapping[str, Any]) -> Json:
    return {name: value for name, value in body.items() if value is not None}


def _message(
    to: list[str],
    subject: str,
    text: Optional[str],
    html: Optional[str],
    cc: Optional[list[str]],
    bcc: Optional[list[str]],
    reply_to: Optional[str],
) -> Json:
    return _drop_none(
        {"to": to, "cc": cc, "bcc": bcc, "subject": subject, "text": text, "html": html,
         "reply_to": reply_to}
    )


def _seg(value: str) -> str:
    return quote(value, safe="")


class Pidgeon:
    """
    The client for Pidgeon's API: the website's, the operator's, and a coding
    agent's. Keep the API key on a server.

    ``api_key`` is an API key (``pgn_…``) or an OAuth access token. ``client``
    is an optional ``httpx.Client`` to send through (for proxies, timeouts or
    tests); the Pidgeon client closes only one it made itself.

    The products' calls are grouped: ``agents`` (Passport), ``inboxes``,
    ``messages``, ``drafts``, ``rules`` and ``suppressions`` (Email), ``sites`` and ``mandates`` (Auth),
    ``events`` and ``pods`` (the account); ``verify`` and ``report`` are
    Bouncer's.
    """

    def __init__(
        self,
        api_key: str,
        base_url: str = DEFAULT_BASE_URL,
        *,
        client: Optional[httpx.Client] = None,
        timeout: float = 10.0,
    ) -> None:
        if not api_key:
            raise ValueError("Pidgeon needs an API key (Settings → API keys).")
        self._api_key = api_key
        self._base_url = base_url.rstrip("/")
        self._owns_client = client is None
        self._client = client or httpx.Client(timeout=timeout)
        self.agents = _Agents(self)
        self.inboxes = _Inboxes(self)
        self.messages = _Messages(self)
        self.drafts = _Drafts(self)
        self.rules = _Rules(self)
        self.suppressions = _Suppressions(self)
        self.sites = _Sites(self)
        self.mandates = _Mandates(self)
        self.events = _Events(self)
        self.pods = _Pods(self)

    @property
    def base_url(self) -> str:
        return self._base_url

    def close(self) -> None:
        if self._owns_client:
            self._client.close()

    def __enter__(self) -> "Pidgeon":
        return self

    def __exit__(self, *_: object) -> None:
        self.close()

    def request(
        self,
        method: str,
        path: str,
        body: Any = None,
        *,
        query: Optional[Mapping[str, Any]] = None,
        headers: Optional[Mapping[str, str]] = None,
    ) -> Any:
        """Any ``/v1`` call: the methods are this with the path and body filled in."""
        sent = {"authorization": f"Bearer {self._api_key}", **(headers or {})}
        content = None
        if body is not None:
            sent["content-type"] = "application/json"
            content = json.dumps(body).encode("utf-8")
        response = self._client.request(
            method,
            f"{self._base_url}{path}",
            headers=sent,
            content=content,
            params={k: v for k, v in (query or {}).items() if v is not None} or None,
        )
        if response.status_code == 204:
            return None
        try:
            data = response.json()
        except ValueError:
            data = None
        if not response.is_success:
            error = data.get("error") if isinstance(data, dict) else None
            error = error if isinstance(error, dict) else {}
            raise PidgeonError(
                response.status_code,
                error.get("code") or "error",
                error.get("message") or f"Pidgeon answered {response.status_code}.",
            )
        return data

    def _call(self, path: str, body: Any, extra: Optional[Mapping[str, str]] = None) -> Any:
        return self.request("POST", path, body, headers=extra)

    # Bouncer

    def verify(self, method: str, url: str, headers: Headers) -> Json:
        """Who stands behind an agent's request, and how they stand. Forward it as you received it."""
        return self._call(
            "/v1/verify",
            {"request": {"method": method, "url": str(url), "headers": _header_map(headers)}},
        )

    def report(self, verification_id: str, category: ReportCategory, evidence: str) -> Json:
        """Report an agent from one of your verifications: what it did, in your words."""
        return self._call(
            "/v1/reports",
            {"verification_id": verification_id, "category": category, "evidence": evidence},
        )

    # Passport

    def publish_key(self, agent_id: str, key: AgentKey, directory: str) -> Json:
        """
        Publish an agent's public key. The request is signed with the key itself,
        which is how Pidgeon knows you hold it; the private half never leaves you.
        """
        path = f"/v1/agents/{_seg(agent_id)}/keys"
        signature = sign_request("POST", f"{self._base_url}{path}", None, key.private_jwk, directory)
        return self._call(path, {"public_jwk": dict(key.public_jwk)}, signature)


class _Group:
    def __init__(self, client: Pidgeon) -> None:
        self._c = client


class _Agents(_Group):
    def list(self, *, limit: Optional[int] = None, cursor: Optional[str] = None) -> Json:
        return self._c.request("GET", "/v1/agents", query={"limit": limit, "cursor": cursor})

    def create(self, name: str, purpose: str = "", *, pod_id: Optional[str] = None) -> Json:
        """Register an agent. It has no key until you make one where it runs and publish it."""
        return self._c.request(
            "POST", "/v1/agents", _drop_none({"name": name, "purpose": purpose, "pod_id": pod_id})
        )

    def get(self, agent_id: str) -> Json:
        """The agent, its keys, its directory and its operator's reputation."""
        return self._c.request("GET", f"/v1/agents/{_seg(agent_id)}")

    def set_up(self, name: str, purpose: str = "", *, pod_id: Optional[str] = None) -> "AgentSetUp":
        """
        Register an agent, make its key here, and publish the public half signed
        with it. Keep ``key.private_jwk`` where the agent runs: Pidgeon never sees it.
        """
        agent = self.create(name, purpose, pod_id=pod_id)
        key = generate_agent_key()
        published = self._c.publish_key(agent["id"], key, agent["directory"])
        return AgentSetUp(agent=agent, key=key, kid=published["kid"])


@dataclass(frozen=True)
class AgentSetUp:
    """What ``agents.set_up`` answers: the agent, its key (both halves) and the key's id."""

    agent: Json
    key: AgentKey
    kid: str


class _Inboxes(_Group):
    def list(self, *, limit: Optional[int] = None, cursor: Optional[str] = None) -> Json:
        return self._c.request(
            "GET", "/v1/email/inboxes", query={"limit": limit, "cursor": cursor}
        )

    def get(self, inbox_id: str) -> Json:
        return self._c.request("GET", f"/v1/email/inboxes/{_seg(inbox_id)}")

    def create(
        self,
        name: str,
        kind: InboxKind = "agent",
        *,
        display_name: Optional[str] = None,
        agent_id: Optional[str] = None,
        pod_id: Optional[str] = None,
    ) -> Json:
        """``name`` is the part before the @. Bind an agent's inbox to it with ``agent_id``."""
        return self._c.request(
            "POST",
            "/v1/email/inboxes",
            _drop_none(
                {"name": name, "kind": kind, "display_name": display_name,
                 "agent_id": agent_id, "pod_id": pod_id}
            ),
        )

    def remove(self, inbox_id: str) -> None:
        """Remove an inbox. Its address is retired, never given to anyone again."""
        self._c.request("DELETE", f"/v1/email/inboxes/{_seg(inbox_id)}")


class _Messages(_Group):
    def send(
        self,
        inbox_id: str,
        *,
        to: list[str],
        subject: str,
        text: Optional[str] = None,
        html: Optional[str] = None,
        cc: Optional[list[str]] = None,
        bcc: Optional[list[str]] = None,
        reply_to: Optional[str] = None,
    ) -> Json:
        """Send from an inbox: ``status`` is ``sent``, or ``held`` while a person approves it."""
        return self._c.request(
            "POST",
            f"/v1/email/inboxes/{_seg(inbox_id)}/messages",
            _message(to, subject, text, html, cc, bcc, reply_to),
        )


class _Drafts(_Group):
    def create(
        self,
        inbox_id: str,
        *,
        to: list[str],
        subject: str,
        text: Optional[str] = None,
        html: Optional[str] = None,
        cc: Optional[list[str]] = None,
        bcc: Optional[list[str]] = None,
        reply_to: Optional[str] = None,
    ) -> Json:
        return self._c.request(
            "POST",
            f"/v1/email/inboxes/{_seg(inbox_id)}/drafts",
            _message(to, subject, text, html, cc, bcc, reply_to),
        )

    def get(self, draft_id: str) -> Json:
        return self._c.request("GET", f"/v1/email/drafts/{_seg(draft_id)}")

    def update(
        self,
        draft_id: str,
        *,
        to: list[str],
        subject: str,
        text: Optional[str] = None,
        html: Optional[str] = None,
        cc: Optional[list[str]] = None,
        bcc: Optional[list[str]] = None,
        reply_to: Optional[str] = None,
    ) -> Json:
        """Replace a draft's addresses and body."""
        return self._c.request(
            "PATCH",
            f"/v1/email/drafts/{_seg(draft_id)}",
            _message(to, subject, text, html, cc, bcc, reply_to),
        )

    def remove(self, draft_id: str) -> None:
        self._c.request("DELETE", f"/v1/email/drafts/{_seg(draft_id)}")

    def send(self, draft_id: str, *, send_at: Optional[str] = None) -> Json:
        """Send now, or at ``send_at`` (ISO 8601, up to 90 days ahead)."""
        return self._c.request(
            "POST", f"/v1/email/drafts/{_seg(draft_id)}/send", _drop_none({"send_at": send_at})
        )

    def request_approval(self, draft_id: str) -> Json:
        """Hold it for a person of the account to send or reject."""
        return self._c.request("POST", f"/v1/email/drafts/{_seg(draft_id)}/approval", {})


class _Rules(_Group):
    """Send and receive rules, for one inbox or (``inbox_id`` left out) every inbox."""

    def list(self) -> Json:
        return self._c.request("GET", "/v1/email/rules")

    def create(
        self,
        direction: Literal["send", "receive"],
        action: Literal["allow", "block"],
        pattern: str,
        *,
        inbox_id: Optional[str] = None,
    ) -> Json:
        return self._c.request(
            "POST",
            "/v1/email/rules",
            {"direction": direction, "action": action, "pattern": pattern, "inbox_id": inbox_id},
        )

    def remove(self, rule_id: str) -> None:
        self._c.request("DELETE", f"/v1/email/rules/{_seg(rule_id)}")


class _Suppressions(_Group):
    """The do-not-send list: bounces and complaints put addresses on it; you can too."""

    def list(self) -> Json:
        return self._c.request("GET", "/v1/email/suppressions")

    def add(self, address: str) -> Json:
        return self._c.request("POST", "/v1/email/suppressions", {"address": address})

    def remove(self, address: str) -> None:
        self._c.request("DELETE", "/v1/email/suppressions", query={"address": address})


class _Sites(_Group):
    """Sites registered for Sign in with Pidgeon."""

    def list(self) -> Json:
        return self._c.request("GET", "/v1/auth/clients")

    def create(self, name: str, redirect_uris: _Strings, *, pod_id: Optional[str] = None) -> Json:
        """Answers ``client_secret`` once: keep it on the site's server."""
        return self._c.request(
            "POST",
            "/v1/auth/clients",
            _drop_none({"name": name, "redirect_uris": redirect_uris, "pod_id": pod_id}),
        )

    def remove(self, client_id: str) -> None:
        self._c.request("DELETE", f"/v1/auth/clients/{_seg(client_id)}")


class _Mandates(_Group):
    """A person's permission for one of your agents to act for them at one site."""

    def list(self) -> Json:
        return self._c.request("GET", "/v1/auth/mandates")

    def create(
        self, agent_id: str, client_id: str, scope: str, description: str, *, days: int = 30
    ) -> Json:
        """Answers ``consent_url``: send it to the person, who allows or declines."""
        return self._c.request(
            "POST",
            "/v1/auth/mandates",
            {"agent_id": agent_id, "client_id": client_id, "scope": scope,
             "description": description, "days": days},
        )

    def revoke(self, mandate_id: str) -> None:
        self._c.request("DELETE", f"/v1/auth/mandates/{_seg(mandate_id)}")


class _Events(_Group):
    def list(
        self,
        *,
        limit: Optional[int] = None,
        cursor: Optional[str] = None,
        type: Optional[str] = None,
    ) -> Json:
        """The account's event log, newest first."""
        return self._c.request(
            "GET", "/v1/events", query={"limit": limit, "cursor": cursor, "type": type}
        )


class _Pods(_Group):
    def list(self) -> Json:
        return self._c.request("GET", "/v1/pods")

    def create(self, name: str) -> Json:
        return self._c.request("POST", "/v1/pods", {"name": name})


class AgentAuth(httpx.Auth):
    """An httpx auth that signs every request as the agent (works for sync and async clients)."""

    def __init__(
        self,
        private_jwk: Mapping[str, Any],
        directory: str,
        lifetime_seconds: float = DEFAULT_LIFETIME_SECONDS,
    ) -> None:
        self.private_jwk = dict(private_jwk)
        self.directory = directory
        self.lifetime_seconds = lifetime_seconds

    def auth_flow(self, request: httpx.Request) -> Generator[httpx.Request, httpx.Response, None]:
        signature = sign_request(
            request.method,
            request.url,
            request.headers,
            self.private_jwk,
            self.directory,
            lifetime_seconds=self.lifetime_seconds,
        )
        for name, value in signature.items():
            request.headers[name] = value
        yield request


def signed_client(private_jwk: Mapping[str, Any], directory: str, **kwargs: Any) -> httpx.Client:
    """An ``httpx.Client`` whose every request carries the agent's Web Bot Auth signature."""
    return httpx.Client(auth=AgentAuth(private_jwk, directory), **kwargs)


def signed_async_client(
    private_jwk: Mapping[str, Any], directory: str, **kwargs: Any
) -> httpx.AsyncClient:
    """The same, for asyncio."""
    return httpx.AsyncClient(auth=AgentAuth(private_jwk, directory), **kwargs)


@dataclass(frozen=True)
class Agent:
    """Your agent: its private key and its operator's directory."""

    private_jwk: dict[str, Any]
    directory: str

    @property
    def auth(self) -> AgentAuth:
        return AgentAuth(self.private_jwk, self.directory)

    def sign(self, method: str, url: str, headers: Headers = None) -> dict[str, str]:
        return sign_request(method, url, headers, self.private_jwk, self.directory)

    def client(self, **kwargs: Any) -> httpx.Client:
        return signed_client(self.private_jwk, self.directory, **kwargs)

    def async_client(self, **kwargs: Any) -> httpx.AsyncClient:
        return signed_async_client(self.private_jwk, self.directory, **kwargs)


def agent_from_env(env: Optional[Mapping[str, str]] = None) -> Agent:
    """Your agent, from ``PIDGEON_AGENT_KEY`` and ``PIDGEON_DIRECTORY`` (the dashboard gives both)."""
    source: Mapping[str, Union[str, None]] = os.environ if env is None else env
    key = source.get("PIDGEON_AGENT_KEY")
    directory = source.get("PIDGEON_DIRECTORY")
    if not key or not directory:
        raise RuntimeError(
            "Set PIDGEON_AGENT_KEY and PIDGEON_DIRECTORY: your agent’s page on pidgeon.ai has both."
        )
    return Agent(private_jwk=json.loads(key), directory=directory)
