"""
The Pidgeon API client, and httpx clients that sign as an agent.
"""

from __future__ import annotations

import json
import mimetypes
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
InboxKind = Literal["agent", "events"]
Body = Literal["original", "clean"]
Folder = Literal["inbox", "archive", "spam", "trash"]
ThreadStatus = Literal["open", "waiting", "resolved", "human_review"]
Owner = Literal["agent", "human", "automation"]
FileInput = Union[bytes, bytearray, str, "os.PathLike[str]"]


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


class _Unset:
    def __repr__(self) -> str:
        return "UNSET"


# A field left out of a PATCH, where ``None`` means "clear it".
UNSET: Any = _Unset()


def _drop_none(body: Mapping[str, Any]) -> Json:
    return {name: value for name, value in body.items() if value is not None}


def _given(body: Mapping[str, Any]) -> Json:
    return {name: value for name, value in body.items() if value is not UNSET}


def _read_file(
    file: FileInput, filename: Optional[str], content_type: Optional[str]
) -> tuple[bytes, str, str]:
    if isinstance(file, (bytes, bytearray)):
        content = bytes(file)
        if not filename:
            raise ValueError("Name the file: pass `filename` with bytes.")
    else:
        with open(file, "rb") as handle:
            content = handle.read()
        filename = filename or os.path.basename(os.fspath(file))
    kind = content_type or mimetypes.guess_type(filename)[0] or "application/octet-stream"
    return content, filename, kind


def _message(
    to: list[str],
    subject: Optional[str],
    text: Optional[str],
    html: Optional[str],
    cc: Optional[list[str]],
    bcc: Optional[list[str]],
    reply_to: Optional[str],
    attachment_ids: Optional[list[str]] = None,
) -> Json:
    return _drop_none(
        {"to": to, "cc": cc, "bcc": bcc, "subject": subject, "text": text, "html": html,
         "reply_to": reply_to, "attachment_ids": attachment_ids}
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

    The products' calls are grouped: ``agents`` (Passport), ``email`` (inboxes,
    messages, threads, labels, contacts, attachments, domains, the calendar
    and more), ``sites`` and ``mandates`` (Auth), ``events``, ``webhooks`` and
    ``pods`` (the account); ``verify`` and ``report`` are Bouncer's. Email's
    first groups are also on the client itself (``inboxes``, ``messages``,
    ``drafts``, ``rules``, ``suppressions``), as in 2.0.
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
        self.webhooks = _Webhooks(self)
        self.pods = _Pods(self)
        self.email = _Email(self)

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
        files: Optional[Mapping[str, Any]] = None,
        timeout: Optional[float] = None,
    ) -> Any:
        """
        Any ``/v1`` call: the methods are this with the path and body filled in.
        ``files`` sends ``multipart/form-data`` instead of JSON (httpx's form);
        ``timeout`` overrides the client's for this call.
        """
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
            files=files,
            params={k: v for k, v in (query or {}).items() if v is not None} or None,
            timeout=httpx.USE_CLIENT_DEFAULT if timeout is None else timeout,
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

    def update(
        self, agent_id: str, *, name: Optional[str] = None, purpose: Optional[str] = None
    ) -> Json:
        """Rename the agent, or change what it does: what websites see when it arrives."""
        return self._c.request(
            "PATCH", f"/v1/agents/{_seg(agent_id)}", _drop_none({"name": name, "purpose": purpose})
        )

    def revoke(self, agent_id: str) -> None:
        """Revoke the agent and every key it has. None verifies again; it cannot be undone."""
        self._c.request("DELETE", f"/v1/agents/{_seg(agent_id)}")

    def revoke_key(self, agent_id: str, kid: str) -> None:
        """Revoke one of the agent's keys, by its ``kid``. Its other keys stay."""
        self._c.request("DELETE", f"/v1/agents/{_seg(agent_id)}/keys/{_seg(kid)}")

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
        domain: Optional[str] = None,
    ) -> Json:
        """
        ``name`` is the part before the @; ``domain`` one of the account's
        mail domains (left out, the account's address on Pidgeon). Bind an
        agent's inbox to it with ``agent_id``.
        """
        return self._c.request(
            "POST",
            "/v1/email/inboxes",
            _drop_none(
                {"name": name, "kind": kind, "display_name": display_name,
                 "agent_id": agent_id, "pod_id": pod_id, "domain": domain}
            ),
        )

    def update(self, inbox_id: str, *, hold_suspicious: Literal[True] = True) -> Json:
        """
        ``hold_suspicious=True`` holds mail the Firewall calls suspicious for a
        person. A key turns it on, never off: a person of the account does that.
        """
        return self._c.request(
            "PATCH", f"/v1/email/inboxes/{_seg(inbox_id)}", {"hold_suspicious": hold_suspicious}
        )

    def remove(self, inbox_id: str) -> None:
        """Remove an inbox. Its address is retired, never given to anyone again."""
        self._c.request("DELETE", f"/v1/email/inboxes/{_seg(inbox_id)}")


class _Messages(_Group):
    def list(
        self,
        inbox_id: str,
        *,
        limit: Optional[int] = None,
        cursor: Optional[str] = None,
        body: Optional[Body] = None,
    ) -> Json:
        """The inbox's mail, newest first. ``body="clean"`` serves the Firewall's cleaned text."""
        return self._c.request(
            "GET",
            f"/v1/email/inboxes/{_seg(inbox_id)}/messages",
            query={"limit": limit, "cursor": cursor, "body": body},
        )

    def wait(
        self,
        inbox_id: str,
        *,
        since: Optional[str] = None,
        timeout: Optional[int] = None,
        body: Optional[Body] = None,
    ) -> Json:
        """
        Wait for mail: answers as soon as mail newer than ``since`` (a time or a
        message id; left out, now) is there, or after ``timeout`` seconds
        (default 25, at most 50) with none. Pass ``next_since`` back to wait
        for the next. ``GET …/messages/await``; ``await`` is Python's.
        """
        return self._c.request(
            "GET",
            f"/v1/email/inboxes/{_seg(inbox_id)}/messages/await",
            query={"since": since, "timeout": timeout, "body": body},
            timeout=(25 if timeout is None else timeout) + 10,
        )

    def get(self, message_id: str, *, body: Optional[Body] = None) -> Json:
        """One message, with the Firewall's verdict. A held one raises ``403 held``."""
        return self._c.request(
            "GET", f"/v1/email/messages/{_seg(message_id)}", query={"body": body}
        )

    def update(self, message_id: str, *, seen: bool) -> Json:
        """Mark a received message read (``seen=True``) or unread."""
        return self._c.request("PATCH", f"/v1/email/messages/{_seg(message_id)}", {"seen": seen})

    def send(
        self,
        inbox_id: str,
        *,
        to: list[str],
        subject: Optional[str] = None,
        text: Optional[str] = None,
        html: Optional[str] = None,
        cc: Optional[list[str]] = None,
        bcc: Optional[list[str]] = None,
        reply_to: Optional[str] = None,
        attachment_ids: Optional[list[str]] = None,
    ) -> Json:
        """
        Send from an inbox: ``status`` is ``sent``, or ``held`` while a person
        approves it. ``attachment_ids`` are files from ``email.attachments``.
        """
        return self._c.request(
            "POST",
            f"/v1/email/inboxes/{_seg(inbox_id)}/messages",
            _message(to, subject, text, html, cc, bcc, reply_to, attachment_ids),
        )


class _Drafts(_Group):
    def create(
        self,
        inbox_id: str,
        *,
        to: list[str],
        subject: Optional[str] = None,
        text: Optional[str] = None,
        html: Optional[str] = None,
        cc: Optional[list[str]] = None,
        bcc: Optional[list[str]] = None,
        reply_to: Optional[str] = None,
        attachment_ids: Optional[list[str]] = None,
    ) -> Json:
        return self._c.request(
            "POST",
            f"/v1/email/inboxes/{_seg(inbox_id)}/drafts",
            _message(to, subject, text, html, cc, bcc, reply_to, attachment_ids),
        )

    def get(self, draft_id: str) -> Json:
        return self._c.request("GET", f"/v1/email/drafts/{_seg(draft_id)}")

    def update(
        self,
        draft_id: str,
        *,
        to: list[str],
        subject: Optional[str] = None,
        text: Optional[str] = None,
        html: Optional[str] = None,
        cc: Optional[list[str]] = None,
        bcc: Optional[list[str]] = None,
        attachment_ids: Optional[list[str]] = None,
    ) -> Json:
        """Replace a draft's addresses, body and files. Its thread stays: no ``reply_to``."""
        return self._c.request(
            "PATCH",
            f"/v1/email/drafts/{_seg(draft_id)}",
            _message(to, subject, text, html, cc, bcc, None, attachment_ids),
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

    def remove(self, pod_id: str) -> None:
        """Remove an empty pod: not the default one, nor one with agents, domains or endpoints."""
        self._c.request("DELETE", f"/v1/pods/{_seg(pod_id)}")


class _Webhooks(_Group):
    """Endpoints that hear about the whole account or listed inboxes; they take a key of the whole account."""

    def list(self) -> Json:
        return self._c.request("GET", "/v1/webhooks")

    def create(self, url: str, events: _Strings, inbox_ids: Optional[_Strings] = None) -> Json:
        """``url`` is https; ``events`` the event types to send; ``inbox_ids``, if given,
        the only inboxes it hears (otherwise the whole account). Answers the secret once."""
        body: dict[str, Any] = {"url": url, "events": events}
        if inbox_ids is not None:
            body["inbox_ids"] = inbox_ids
        return self._c.request("POST", "/v1/webhooks", body)

    def remove(self, webhook_id: str) -> None:
        self._c.request("DELETE", f"/v1/webhooks/{_seg(webhook_id)}")


class _Threads(_Group):
    """Conversations, across the account's inboxes."""

    def list(
        self,
        *,
        inbox_id: Optional[str] = None,
        folder: Optional[Folder] = None,
        label_id: Optional[str] = None,
        status: Optional[ThreadStatus] = None,
        starred: Optional[bool] = None,
        limit: Optional[int] = None,
        cursor: Optional[str] = None,
    ) -> Json:
        """Newest first. ``starred=True`` keeps the starred ones."""
        return self._c.request(
            "GET",
            "/v1/email/threads",
            query={"inbox_id": inbox_id, "folder": folder, "label_id": label_id,
                   "status": status, "starred": starred, "limit": limit, "cursor": cursor},
        )

    def get(
        self,
        thread_id: str,
        *,
        limit: Optional[int] = None,
        cursor: Optional[str] = None,
        body: Optional[Body] = None,
    ) -> Json:
        """One conversation and its messages, oldest first (``limit`` up to 200)."""
        return self._c.request(
            "GET",
            f"/v1/email/threads/{_seg(thread_id)}",
            query={"limit": limit, "cursor": cursor, "body": body},
        )

    def update(
        self,
        thread_id: str,
        *,
        folder: Optional[Folder] = None,
        starred: Optional[bool] = None,
        status: Optional[ThreadStatus] = None,
        owner_type: Optional[Owner] = None,
        assignee_id: Optional[str] = UNSET,
    ) -> Json:
        """
        Change what you pass. Hand a conversation to a person with
        ``owner_type="human", status="human_review"``; ``assignee_id=None`` unassigns.
        """
        change = _drop_none(
            {"folder": folder, "starred": starred, "status": status, "owner_type": owner_type}
        )
        return self._c.request(
            "PATCH",
            f"/v1/email/threads/{_seg(thread_id)}",
            {**change, **_given({"assignee_id": assignee_id})},
        )

    def remove(self, thread_id: str) -> None:
        """Delete the conversation, its messages and files, for good."""
        self._c.request("DELETE", f"/v1/email/threads/{_seg(thread_id)}")

    def add_label(self, thread_id: str, label_id: str) -> Json:
        """Answers the conversation."""
        return self._c.request(
            "POST", f"/v1/email/threads/{_seg(thread_id)}/labels", {"label_id": label_id}
        )

    def remove_label(self, thread_id: str, label_id: str) -> Json:
        """Answers the conversation."""
        return self._c.request(
            "DELETE", f"/v1/email/threads/{_seg(thread_id)}/labels/{_seg(label_id)}"
        )


class _Labels(_Group):
    """An inbox's labels, put on its conversations with ``threads.add_label``."""

    def list(self, inbox_id: str) -> Json:
        return self._c.request("GET", f"/v1/email/inboxes/{_seg(inbox_id)}/labels")

    def create(self, inbox_id: str, name: str, *, colour: Optional[str] = None) -> Json:
        """``colour`` is a palette name such as slate (the default), red or green."""
        return self._c.request(
            "POST",
            f"/v1/email/inboxes/{_seg(inbox_id)}/labels",
            _drop_none({"name": name, "colour": colour}),
        )

    def update(
        self, label_id: str, *, name: Optional[str] = None, colour: Optional[str] = None
    ) -> Json:
        return self._c.request(
            "PATCH",
            f"/v1/email/labels/{_seg(label_id)}",
            _drop_none({"name": name, "colour": colour}),
        )

    def remove(self, label_id: str) -> None:
        """The label goes; its conversations stay."""
        self._c.request("DELETE", f"/v1/email/labels/{_seg(label_id)}")


class _Contacts(_Group):
    """Who the account's inboxes correspond with."""

    def list(
        self,
        *,
        inbox_id: Optional[str] = None,
        search: Optional[str] = None,
        limit: Optional[int] = None,
        cursor: Optional[str] = None,
    ) -> Json:
        """Most recently seen first. ``search`` is part of an address or name."""
        return self._c.request(
            "GET",
            "/v1/email/contacts",
            query={"inbox_id": inbox_id, "search": search, "limit": limit, "cursor": cursor},
        )

    def get(self, contact_id: str) -> Json:
        return self._c.request("GET", f"/v1/email/contacts/{_seg(contact_id)}")

    def update(
        self, contact_id: str, *, name: Optional[str] = UNSET, notes: Optional[str] = UNSET
    ) -> Json:
        """Change what you pass; ``None`` clears it. From then on mail no longer renames it."""
        return self._c.request(
            "PATCH",
            f"/v1/email/contacts/{_seg(contact_id)}",
            _given({"name": name, "notes": notes}),
        )

    def remove(self, contact_id: str) -> None:
        """Forget it. New mail notes it again."""
        self._c.request("DELETE", f"/v1/email/contacts/{_seg(contact_id)}")


class _Attachments(_Group):
    """Files to send: upload one, then name its id in ``attachment_ids``."""

    def upload(
        self,
        inbox_id: str,
        file: FileInput,
        *,
        filename: Optional[str] = None,
        content_type: Optional[str] = None,
    ) -> Json:
        """
        Upload a file of up to 4 MB: bytes (with ``filename``) or a path. The
        content type is guessed from the name when left out.
        """
        content, name, kind = _read_file(file, filename, content_type)
        return self._c.request(
            "POST",
            f"/v1/email/inboxes/{_seg(inbox_id)}/attachments",
            files={"file": (name, content, kind)},
        )

    def upload_large(
        self,
        inbox_id: str,
        file: FileInput,
        *,
        filename: Optional[str] = None,
        content_type: Optional[str] = None,
    ) -> Json:
        """
        Upload a file of up to 25 MB in three steps: describe it, put the bytes
        at the upload link, and complete it. Answers the file, now sendable.
        """
        content, name, kind = _read_file(file, filename, content_type)
        made = self._c.request(
            "POST",
            f"/v1/email/inboxes/{_seg(inbox_id)}/attachments/uploads",
            {"filename": name, "content_type": kind, "size": len(content)},
        )
        upload = made["upload"]
        # The link is signed for storage: it carries no API key.
        put = self._c._client.request(
            upload.get("method", "PUT"),
            upload["url"],
            content=content,
            headers={"content-type": kind},
        )
        if not put.is_success:
            raise PidgeonError(
                put.status_code,
                "upload_failed",
                f"Putting the file at the upload link answered {put.status_code}.",
            )
        return self._c.request("POST", f"/v1/email/attachments/{_seg(made['id'])}/complete")

    def get(self, attachment_id: str) -> Json:
        """The file's details and a link to its bytes that lasts five minutes."""
        return self._c.request("GET", f"/v1/email/attachments/{_seg(attachment_id)}")


class _Domains(_Group):
    """The account's proved domains and the mail on each (a key of the whole account)."""

    def list(self) -> Json:
        return self._c.request("GET", "/v1/email/domains")

    def get(self, domain_id: str) -> Json:
        """One domain, its mail status and the records to set."""
        return self._c.request("GET", f"/v1/email/domains/{_seg(domain_id)}")

    def enable_mail(self, domain_id: str) -> Json:
        """Turn mail on for a proved domain; answers the records to set."""
        return self._c.request("POST", f"/v1/email/domains/{_seg(domain_id)}/mail")

    def disable_mail(self, domain_id: str) -> None:
        """Turn mail off; the domain must have no inboxes left."""
        self._c.request("DELETE", f"/v1/email/domains/{_seg(domain_id)}/mail")

    def check(self, domain_id: str) -> Json:
        """Ask SES and DNS where the domain stands now."""
        return self._c.request("POST", f"/v1/email/domains/{_seg(domain_id)}/check")


class _AppPasswords(_Group):
    """Passwords for mail apps (IMAP and SMTP) on one inbox."""

    def list(self, inbox_id: str) -> Json:
        """Never their secrets."""
        return self._c.request("GET", f"/v1/email/inboxes/{_seg(inbox_id)}/app-passwords")

    def create(self, inbox_id: str, name: str) -> Json:
        """``name`` says where it is used. The password is in the answer once."""
        return self._c.request(
            "POST", f"/v1/email/inboxes/{_seg(inbox_id)}/app-passwords", {"name": name}
        )

    def revoke(self, app_password_id: str) -> None:
        """Its mail apps are refused from their next request."""
        self._c.request("DELETE", f"/v1/email/app-passwords/{_seg(app_password_id)}")


class _CalendarEvents(_Group):
    def list(
        self,
        inbox_id: str,
        *,
        after: Optional[str] = None,
        before: Optional[str] = None,
        limit: Optional[int] = None,
        cursor: Optional[str] = None,
    ) -> Json:
        """In start order; ``after`` and ``before`` keep the events overlapping that window."""
        return self._c.request(
            "GET",
            f"/v1/email/inboxes/{_seg(inbox_id)}/events",
            query={"after": after, "before": before, "limit": limit, "cursor": cursor},
        )

    def create(
        self,
        inbox_id: str,
        *,
        title: str,
        start: str,
        end: Optional[str] = None,
        all_day: Optional[bool] = None,
        description: Optional[str] = None,
        location: Optional[str] = None,
        attendees: Optional[_Strings] = None,
        send_invites: Optional[bool] = None,
    ) -> Json:
        """
        ``start`` and ``end`` are ISO 8601 times, and ``end`` is required; with
        ``all_day=True`` they are dates, and ``end`` defaults to ``start``.
        ``attendees`` lists who is on it (writing it sends nothing);
        ``send_invites=True`` invites them, with a key that has ``send`` access.
        """
        return self._c.request(
            "POST",
            f"/v1/email/inboxes/{_seg(inbox_id)}/events",
            _drop_none({"title": title, "start": start, "end": end, "all_day": all_day,
                        "description": description, "location": location,
                        "attendees": list(attendees) if attendees is not None else None,
                        "send_invites": send_invites}),
        )

    def get(self, event_id: str) -> Json:
        return self._c.request("GET", f"/v1/email/events/{_seg(event_id)}")

    def update(
        self,
        event_id: str,
        *,
        title: str = UNSET,
        start: str = UNSET,
        end: str = UNSET,
        all_day: bool = UNSET,
        description: Optional[str] = UNSET,
        location: Optional[str] = UNSET,
        attendees: _Strings = UNSET,
        send_invites: bool = UNSET,
    ) -> Json:
        """
        Change what you pass; ``description=None`` or ``location=None`` clears it.
        ``send_invites=True`` sends the attendees the updated invitation.
        """
        return self._c.request(
            "PATCH",
            f"/v1/email/events/{_seg(event_id)}",
            _given({"title": title, "start": start, "end": end, "all_day": all_day,
                    "description": description, "location": location,
                    "attendees": list(attendees) if attendees is not UNSET else UNSET,
                    "send_invites": send_invites}),
        )

    def remove(self, event_id: str, *, send_invites: bool = False) -> Optional[Json]:
        """Gone, and from calendar apps at their next sync; ``send_invites=True`` cancels with the attendees first."""
        return self._c.request(
            "DELETE",
            f"/v1/email/events/{_seg(event_id)}",
            query={"send_invites": "true"} if send_invites else None,
        )


class _Calendar(_Group):
    """Each inbox's calendar, which calendar apps sync over CalDAV."""

    def __init__(self, client: Pidgeon) -> None:
        super().__init__(client)
        self.events = _CalendarEvents(client)


class _Email(_Group):
    """Email: inboxes, their mail, conversations, files, domains and calendars."""

    def __init__(self, client: Pidgeon) -> None:
        super().__init__(client)
        self.inboxes: _Inboxes = client.inboxes
        self.messages: _Messages = client.messages
        self.drafts: _Drafts = client.drafts
        self.rules: _Rules = client.rules
        self.suppressions: _Suppressions = client.suppressions
        self.threads = _Threads(client)
        self.labels = _Labels(client)
        self.contacts = _Contacts(client)
        self.attachments = _Attachments(client)
        self.domains = _Domains(client)
        self.app_passwords = _AppPasswords(client)
        self.calendar = _Calendar(client)

    def search(
        self,
        q: str,
        *,
        inbox_id: Optional[str] = None,
        limit: Optional[int] = None,
        cursor: Optional[str] = None,
        body: Optional[Body] = None,
    ) -> Json:
        """
        Messages whose subject, sender or text match ``q``, newest first. Held
        mail is not found. ``body="clean"`` serves the Firewall's text, as a read does.
        """
        return self._c.request(
            "GET",
            "/v1/email/search",
            query={"q": q, "inbox_id": inbox_id, "limit": limit, "cursor": cursor, "body": body},
        )

    def storage(self) -> Json:
        """``used_bytes`` of the account's ``limit_bytes``, for its mail and files."""
        return self._c.request("GET", "/v1/email/storage")

    def test_inbound(
        self,
        inbox_id: str,
        *,
        from_: str,
        subject: Optional[str] = None,
        text: Optional[str] = None,
        html: Optional[str] = None,
        from_name: Optional[str] = None,
        in_reply_to: Optional[str] = None,
    ) -> Json:
        """
        With a test key: deliver a message to one of your inboxes as if
        ``from_`` sent it, through the real receiving pipeline, marked test.
        ``in_reply_to`` is a Message-ID, to answer something the inbox sent.
        """
        return self._c.request(
            "POST",
            "/v1/email/test/inbound",
            _drop_none({"inbox_id": inbox_id, "from": from_, "from_name": from_name,
                        "subject": subject, "text": text, "html": html,
                        "in_reply_to": in_reply_to}),
        )


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
