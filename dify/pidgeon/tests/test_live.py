"""
The plugin against production Pidgeon, each tool as Dify invokes it.
Skipped without `PIDGEON_ADMIN_KEY`.

The admin key creates the address (through Create Address) and a test key
for it; everything after runs on the test key, so nothing sent leaves
Pidgeon. Both are deleted at the end.
"""

import os
import secrets
import threading
import time
from datetime import UTC, datetime, timedelta

import httpx
import pytest

from provider.pidgeon import PidgeonProvider
from tools.create_address import CreateAddressTool
from tools.reply_to_email import ReplyToEmailTool
from tools.search_emails import SearchEmailsTool
from tools.update_thread import UpdateThreadTool
from tools.wait_for_code import WaitForCodeTool

API = "https://pidgeon.ai/api/v1"
ADMIN = os.environ.get("PIDGEON_ADMIN_KEY")
MARKER = secrets.token_hex(3)

pytestmark = pytest.mark.skipif(not ADMIN, reason="PIDGEON_ADMIN_KEY is not set")


def pidgeon(key: str, method: str, path: str, body: dict | None = None) -> dict:
    response = httpx.request(
        method, f"{API}{path}", headers={"Authorization": f"Bearer {key}"}, json=body, timeout=60
    )
    assert response.status_code < 400, f"{method} {path} → {response.status_code} {response.text}"
    return response.json() if response.content else {}


def run(tool_class, key: str, parameters: dict):
    messages = list(tool_class.from_credentials({"api_key": key}).invoke(parameters))
    data = next((m.message.json_object for m in messages if m.type.value == "json"), None)
    text = next((m.message.text for m in messages if m.type.value == "text"), None)
    return data, text


@pytest.fixture(scope="module")
def fixture():
    # Old runs that died before their cleanup.
    for stale in pidgeon(ADMIN, "GET", "/identities?limit=200")["data"]:
        if str(stale["email"]).startswith("dify-e2e-"):
            created = datetime.fromisoformat(stale["created_at"].replace("Z", "+00:00"))
            if datetime.now(UTC) - created > timedelta(hours=1):
                httpx.delete(f"{API}/identities/{stale['id']}", headers={"Authorization": f"Bearer {ADMIN}"})

    address, summary = run(CreateAddressTool, ADMIN, {"address": f"dify-e2e-{MARKER}@pidgeon.email"})
    assert address, summary
    key = pidgeon(
        ADMIN,
        "POST",
        "/api-keys",
        {"name": "Dify e2e", "access": "send", "identity_ids": [address["id"]], "test": True},
    )["data"]
    yield {"address": address, "key": key["token"]}
    httpx.delete(f"{API}/api-keys/{key['id']}", headers={"Authorization": f"Bearer {ADMIN}"})
    httpx.delete(f"{API}/identities/{address['id']}", headers={"Authorization": f"Bearer {ADMIN}"})


def test_the_connection_accepts_the_test_key(fixture):
    PidgeonProvider()._validate_credentials({"api_key": fixture["key"]})


def test_mail_in_code_read_reply_hand_off_search(fixture):
    key, address = fixture["key"], fixture["address"]

    # Waiting first, as a sign-up does: the code arrives while the tool holds.
    waited: dict = {}
    waiter = threading.Thread(
        target=lambda: waited.update(
            zip(("data", "text"), run(WaitForCodeTool, key, {"address_id": address["id"], "timeout": 60}))
        )
    )
    waiter.start()
    time.sleep(2)
    delivered = pidgeon(
        key,
        "POST",
        "/test/inbound",
        {
            "to": address["email"],
            "from": "priya@supplier.example",
            "from_name": "Priya Raman",
            "subject": f"Angebot {MARKER}",
            "text": "Guten Tag, anbei unser Angebot. Ihr Code: 482910.",
        },
    )["data"]
    waiter.join(90)

    assert waited["data"]["timed_out"] is False, waited
    assert waited["data"]["code"] == "482910"
    assert waited["data"]["message_id"] == delivered["message_id"]
    assert waited["data"]["test"] is True

    reply, summary = run(ReplyToEmailTool, key, {"message_id": delivered["message_id"], "text": f"Danke {MARKER}"})
    assert reply and reply["id"], summary

    thread, summary = run(
        UpdateThreadTool,
        key,
        {"thread_id": waited["data"]["thread_id"], "owner": "human", "reason": "Needs a price"},
    )
    assert thread and thread["owner_type"] == "human", summary

    found, summary = run(SearchEmailsTool, key, {"query": MARKER, "address_id": address["id"], "limit": 10})
    assert any(message["id"] == delivered["message_id"] for message in found["messages"]), summary
