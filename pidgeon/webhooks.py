"""Verifying a delivery.

The only part of this package with a security contract: it is what a customer
runs to decide whether a request claiming a message arrived actually came from
us. Everything else here is a generated, typed ``httpx`` call.

**Hand-written, and it stays through regeneration.** ``openapi-python-client``
rewrites the modules it owns — ``api/``, ``models/``, ``client.py`` — and
leaves anything else in the package alone, which was checked rather than
assumed before this file was added.

It exists because it did not. The TypeScript client has shipped
``verifyWebhook`` since it had webhooks at all, and a Python receiver had to
reimplement HMAC over ``timestamp.body`` by reading our TypeScript — a
security-critical routine, rewritten by every customer, from a source that is
not documentation. A window building a real project against production
reported it on 13 October.

Kept deliberately close to ``packages/sdk/src/webhooks.ts``: same header
names, same ``v1=`` prefix, same five-minute tolerance, same order of checks.
Two implementations of one scheme that drift are worse than one, so the thing
that keeps them together is that both are tested against payloads signed by
the *server's* implementation rather than against each other.
"""

from __future__ import annotations

import hashlib
import hmac
import time
from collections.abc import Mapping
from typing import Any

__all__ = [
    "SIGNATURE_HEADER",
    "TIMESTAMP_HEADER",
    "WebhookVerificationError",
    "verify_webhook",
]

SIGNATURE_HEADER = "x-pidgeon-signature"
TIMESTAMP_HEADER = "x-pidgeon-timestamp"

DEFAULT_TOLERANCE_SECONDS = 300


class WebhookVerificationError(Exception):
    """A delivery that could not be trusted.

    Raised rather than returning ``False``, for the reason the TypeScript one
    gives: the failure mode of a boolean is a caller who forgets to check it,
    and the cost of that here is accepting an unauthenticated POST as a
    message from us.

    It is deliberately *not* an ``Error`` from ``pidgeon.models``. That type is
    a response the API sent; this is a request we refused to believe.
    """


def verify_webhook(
    *,
    raw_body: str | bytes,
    headers: Mapping[str, Any],
    secret: str,
    tolerance_seconds: int = DEFAULT_TOLERANCE_SECONDS,
    now: float | None = None,
) -> dict[str, Any]:
    """Verify a delivery and return its payload.

    ``raw_body`` must be the exact bytes we sent. Re-serialising parsed JSON
    changes key order and whitespace and the signature will not match — read
    the body before you parse it. A ``str`` is encoded as UTF-8, which is what
    the server signed.

    ``headers`` is anything that maps a name to a value: a ``dict``, Django's
    ``request.headers``, Flask's, Starlette's. Matched case-insensitively,
    because HTTP header names are and half of these are not.

    Returns the decoded envelope — ``id``, ``type``, ``created_at``, ``data``.
    Raises :class:`WebhookVerificationError` for anything else.
    """
    import json

    timestamp = _header(headers, TIMESTAMP_HEADER)
    signature = _header(headers, SIGNATURE_HEADER)

    if not timestamp or not signature:
        raise WebhookVerificationError("This request is not signed.")

    try:
        seconds = int(float(timestamp))
    except (TypeError, ValueError) as cause:
        raise WebhookVerificationError("The signature timestamp is not a number.") from cause

    #
    # The clock first, and before any hashing.
    #
    # A replay carries a signature that verifies — it was ours — so the age is
    # the only thing that refuses it, and checking it first means a flood of
    # old deliveries costs no HMAC work.
    #
    current = int(now if now is not None else time.time())
    if abs(current - seconds) > tolerance_seconds:
        raise WebhookVerificationError("This request is too old to trust. It may be a replay.")

    body = raw_body.encode("utf-8") if isinstance(raw_body, str) else raw_body
    signed = f"{seconds}.".encode() + body

    mac = hmac.new(secret.encode("utf-8"), signed, hashlib.sha256).hexdigest()
    expected = f"v1={mac}"

    # `compare_digest`, not `==`: the comparison is the one place a timing
    # difference leaks the signature a byte at a time.
    if not hmac.compare_digest(expected, signature):
        raise WebhookVerificationError("The signature does not match.")

    try:
        return json.loads(body)
    except ValueError as cause:
        raise WebhookVerificationError("The payload is signed but is not JSON.") from cause


def _header(headers: Mapping[str, Any], name: str) -> str | None:
    """One header, however the framework spells it.

    Tried verbatim first because most mappings are already lower-cased and a
    full scan of every header to find one is work for nothing.
    """
    for key in (name, name.lower(), name.upper(), name.replace("-", "_").upper()):
        value = headers.get(key)
        if value is not None:
            return str(value)

    lowered = name.lower()
    for key, value in headers.items():
        if str(key).lower().replace("_", "-") == lowered:
            return str(value)

    return None
