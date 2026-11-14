"""Checking the webhooks Pidgeon sends (``Pidgeon-Signature``), as the TypeScript ``verifyWebhook`` does."""

from __future__ import annotations

import hashlib
import hmac
import json
import time
from typing import Any, Optional, Union

from .client import PidgeonError


def sign_webhook(secret: str, body: Union[str, bytes], timestamp: int) -> str:
    """The header Pidgeon sends: ``t=<unix seconds>,v1=<hex HMAC-SHA256 of "<t>.<body>">``."""
    raw = body.encode() if isinstance(body, str) else body
    mac = hmac.new(secret.encode(), str(timestamp).encode() + b"." + raw, hashlib.sha256)
    return f"t={timestamp},v1={mac.hexdigest()}"


def verify_webhook(
    secret: str,
    raw_body: Union[str, bytes],
    signature_header: Optional[str],
    tolerance_seconds: int = 300,
    now: Optional[float] = None,
) -> dict[str, Any]:
    """
    Check a webhook's signature against your endpoint's secret and return the
    event, or raise ``PidgeonError``. Pass the raw body as received. Signatures
    older than ``tolerance_seconds`` are refused, so a captured delivery cannot
    be replayed later.
    """
    parts = dict(
        part.strip().split("=", 1) for part in (signature_header or "").split(",") if "=" in part
    )
    try:
        timestamp = int(parts["t"])
        given = parts["v1"]
    except (KeyError, ValueError):
        raise PidgeonError(400, "invalid_signature", "The Pidgeon-Signature header is missing or malformed.")
    if abs(int(now if now is not None else time.time()) - timestamp) > tolerance_seconds:
        raise PidgeonError(400, "stale_signature", "The webhook was signed too long ago.")
    expected = sign_webhook(secret, raw_body, timestamp).split("v1=", 1)[1]
    if not hmac.compare_digest(expected, given):
        raise PidgeonError(400, "invalid_signature", "The webhook signature does not match.")
    return json.loads(raw_body)
