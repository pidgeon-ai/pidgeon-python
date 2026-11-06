"""Signing an agent's email: the ``Post-Envelope`` header.

Post's signed envelope (``docs/spec/`` §"The Signed Envelope"): Ed25519 by the
From domain over the message as JSON. It works through any provider that lets
you set a header — SES, Gmail's API, Resend, Postmark, ``smtplib`` — because
the signature travels in the message, not in the transport.

A receiver checks it against the key ``post.<domain>/.well-known/post.json``
publishes (anyone, offline) or by sending the message to Pidgeon's verifier
(``POST /v1/verify``). What the verifier compares, and so what must be sent
exactly as signed: the From address, the subject, To and Cc, the plain-text
body (line endings and trailing whitespace aside) and the attachments'
SHA-256. Send the same ``text`` as the message's text/plain part; an HTML part
beside it is not covered.

The twin of ``packages/id/src/email.ts``. **The signed bytes are the
receiver's, not ours to re-spell**: the server verifies the bytes it decodes
from ``m=``, then compares them with the MIME, so the JSON is written exactly
as ``JSON.stringify`` writes it (``_js.js_stringify``), in the order
``src/lib/mail/envelope.ts`` ``messageBytes`` writes it.
"""

from __future__ import annotations

import re
import uuid
from collections.abc import Mapping, Sequence
from dataclasses import dataclass
from datetime import UTC, datetime
from hashlib import sha256
from typing import Any, Literal

from ._js import b64url, js_stringify
from .keys import Identity

__all__ = ["ENVELOPE_VERSION", "SignedEmail", "sign_email"]

ENVELOPE_VERSION = "post0"


@dataclass(frozen=True)
class SignedEmail:
    """What ``sign_email`` gives back."""

    headers: dict[str, str]
    """The header to add: ``Post-Envelope``."""
    grant_headers: list[tuple[str, str]]
    """One ``Post-Grant`` field per grant, in order: add each as its own header line."""
    message: bytes
    """The exact bytes signed, for a test or a log."""


def _runs(text: str) -> str:
    """76-character runs, separated by spaces, which any mailer folds onto continuation lines."""
    return " ".join(text[i : i + 76] for i in range(0, len(text), 76))


def _iso(moment: datetime) -> str:
    """``Date.toISOString()`` without its milliseconds. A naive datetime is taken as UTC."""
    if moment.tzinfo is None:
        moment = moment.replace(tzinfo=UTC)
    return moment.astimezone(UTC).strftime("%Y-%m-%dT%H:%M:%SZ")


def sign_email(
    identity: Identity,
    *,
    from_: str,
    to: Sequence[str],
    subject: str,
    text: str,
    cc: Sequence[str] | None = None,
    kind: Literal["agent", "service"] | None = None,
    on_behalf_of: str | None = None,
    id: str | None = None,
    thread: Mapping[str, str | None] | None = None,
    data: Mapping[str, Any] | None = None,
    attachments: Sequence[Mapping[str, Any]] | None = None,
    created_at: datetime | None = None,
    grants: Sequence[str] | None = None,
) -> SignedEmail:
    """The ``Post-Envelope`` header for one message.

    ``from_`` is the agent's address (its domain must be the identity's);
    ``text`` the text/plain body exactly as sent. ``id`` is stable per message,
    a new UUID when omitted; ``thread`` is ``{"id": ..., "parent": ...}``.
    ``data`` is ``{"schema": ..., "body": ...}``, typed data carried beside the
    text. Each attachment is ``{"content_type", "filename", "content"}`` with
    ``content`` the bytes. ``grants`` are compact JWS the agent was given, each
    becoming a ``Post-Grant`` field: a grant holds only beside a signature
    from the agent it names, which this envelope is.
    """
    sender = from_.strip().lower()
    if sender[sender.rfind("@") + 1 :] != identity.domain:
        raise ValueError(f"{sender} is not an address at {identity.domain}, whose key this is.")

    message_id = id if id is not None else str(uuid.uuid4())
    thread = thread if thread is not None else {"id": message_id}
    signed_thread: dict[str, Any] = {"id": thread["id"]}
    if thread.get("parent"):
        signed_thread["parent"] = thread["parent"]
    signed_sender: dict[str, Any] = {"address": sender, "kind": kind if kind is not None else "agent"}
    if on_behalf_of:
        signed_sender["on_behalf_of"] = on_behalf_of

    parts: list[dict[str, Any]] = [{"role": "text", "type": "text/plain", "body": text}]
    if data:
        parts.append({"role": "data", "schema": data["schema"], "body": data["body"]})
    for file in attachments or []:
        content = bytes(file["content"])
        parts.append(
            {
                "role": "attachment",
                "type": file["content_type"],
                "name": file["filename"],
                "sha256": sha256(content).hexdigest(),
                "size": len(content),
            }
        )

    message = {
        "v": ENVELOPE_VERSION,
        "id": message_id,
        "thread": signed_thread,
        "sender": signed_sender,
        "to": list(to),
        "cc": list(cc) if cc is not None else [],
        "created_at": _iso(created_at if created_at is not None else datetime.now(UTC)),
        "subject": subject,
        "parts": parts,
    }

    data_bytes = js_stringify(message).encode("utf-8")
    signature = identity.sign(data_bytes)
    header = "; ".join(
        [
            f"v={ENVELOPE_VERSION}",
            f"d={identity.domain}",
            f"k={identity.kid}",
            f"s={_runs(b64url(signature))}",
            f"m={_runs(b64url(data_bytes))}",
        ]
    )
    return SignedEmail(
        headers={"Post-Envelope": header},
        grant_headers=[("Post-Grant", _runs(re.sub(r"\s+", "", jws))) for jws in grants or []],
        message=data_bytes,
    )
