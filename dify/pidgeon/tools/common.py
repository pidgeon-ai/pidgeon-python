"""What every Pidgeon tool shares: the client, the error text, and the shapes."""

from types import ModuleType
from typing import Any

import httpx
from pidgeon import AuthenticatedClient
from pidgeon.errors import PidgeonError
from pidgeon.types import UNSET

API = "https://pidgeon.ai/api/v1"
USER_AGENT = "pidgeon-dify/0.0.1"


def client(credentials: dict[str, Any], timeout: float = 60) -> AuthenticatedClient:
    """Our Python client, on the key the person connected."""
    return AuthenticatedClient(
        base_url=API,
        token=str(credentials["api_key"]).strip(),
        headers={"User-Agent": USER_AGENT},
        timeout=httpx.Timeout(timeout, connect=10),
    )


def call(
    operation: ModuleType,
    credentials: dict[str, Any],
    *,
    request_timeout: float = 60,
    **arguments: Any,
) -> dict[str, Any]:
    """
    One operation of our Python client, answered as the JSON on the wire.

    The request is the client's own (`_get_kwargs` builds it from the typed
    body), and so is the error: a refusal raises `PidgeonError`. The answer
    is not parsed into the client's models, because a plugin pins one client
    version and a model that meets a field or a value added to the API since
    refuses the whole answer. The JSON passes through as Pidgeon sent it.
    """
    http = client(credentials, request_timeout).get_httpx_client()
    response = http.request(**operation._get_kwargs(**arguments))
    if response.status_code >= 400:
        raise PidgeonError.from_response(response)
    return response.json() if response.content else {}


def describe(error: PidgeonError) -> str:
    """Pidgeon's own message, which already says what to do, and its code."""
    code = f" ({error.code}{', ' + error.field if error.field else ''})" if error.code else ""
    return f"Pidgeon answered {error.status_code}: {error.message}{code}"


def text(value: Any) -> str:
    return str(value).strip() if value is not None else ""


def optional(value: Any) -> Any:
    """An empty field is a field left out, not an empty string sent."""
    cleaned = text(value)
    return cleaned if cleaned else UNSET


def address_list(value: Any) -> list[str]:
    """One address, or several separated by commas, semicolons or new lines."""
    if isinstance(value, list):
        entries = [str(entry) for entry in value]
    else:
        entries = text(value).replace(";", ",").replace("\n", ",").split(",")
    return [entry.strip() for entry in entries if entry.strip()]


def flat_message(message: dict[str, Any]) -> dict[str, Any]:
    """
    One message as a workflow variable: flat, so an IF/ELSE node reaches
    `auth_dmarc` or `firewall_verdict` by name with no model in between.
    """
    sender = message.get("from") or {}
    to = [person.get("email") for person in message.get("to") or []]
    cc = [person.get("email") for person in message.get("cc") or []]
    firewall = message.get("firewall") or {}
    auth = message.get("authentication") or {}
    extracted = message.get("extracted") or {}
    delivered_to = message.get("delivered_to") or message.get("identity")
    return {
        "message_id": message.get("id"),
        "thread_id": message.get("thread_id"),
        "address": message.get("identity"),
        "from": sender.get("email"),
        "from_name": sender.get("name"),
        "to": to,
        "cc": cc,
        "subject": message.get("subject"),
        "received_at": message.get("created_at"),
        "spam": bool(message.get("is_spam", False)),
        "bcc_to_this_address": bool(delivered_to)
        and delivered_to.lower() not in [entry.lower() for entry in to + cc if entry],
        "firewall_verdict": firewall.get("verdict"),
        "auth_dmarc": auth.get("dmarc"),
        "text": message.get("text"),
        "codes": [code.get("value") for code in extracted.get("codes") or []],
        "links": extracted.get("links") or [],
        "attachments": message.get("attachments") or [],
        "test": bool(message.get("test", False)),
    }
