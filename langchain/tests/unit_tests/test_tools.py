"""The tools against a mocked API.

The SDK runs for real and only the network is fake (`httpx.MockTransport`),
so these check the request each tool makes — method, path, query, body,
key — rather than which SDK function it called.
"""

from __future__ import annotations

import json
import re
from pathlib import Path
from typing import Any

import httpx
import pytest
from langchain_core.messages import ToolMessage
from pidgeon import AuthenticatedClient
from pidgeon.api.identities import identities_create
from pidgeon.api.messages import messages_get
from pidgeon.api.threads import threads_update

from langchain_pidgeon import (
    AwaitMessage,
    CreateAddress,
    GetMessage,
    ListAddresses,
    ListMessages,
    PidgeonToolkit,
    ReplyToMessage,
    SearchMessages,
    SendMessage,
    UpdateThread,
)
from langchain_pidgeon.tools import TOOLS

KEY = "pgn_live_test"
ID = "0b5d1c1e-6a3f-4c55-9a8e-1f2d3c4b5a69"
PAGE = {"data": [], "has_more": False, "next_cursor": None}
SENT = {"data": {"id": ID, "thread_id": ID, "rejected": [], "test": False}}
TIMED_OUT = {
    "data": {
        "message": None,
        "timed_out": True,
        "cursor": "2026-10-22T10:00:00.000Z",
        "held_back": {
            "spam": 0,
            "unauthenticated": 0,
            "message_ids": [],
            "how_to_include": None,
        },
    }
}


class Api:
    """Answers each request with the next canned response and keeps the request."""

    def __init__(self, *responses: tuple[int, Any]):
        self.responses = list(responses)
        self.requests: list[httpx.Request] = []

    def __call__(self, request: httpx.Request) -> httpx.Response:
        self.requests.append(request)
        status, payload = self.responses.pop(0)
        return httpx.Response(status, json=payload)

    @property
    def last(self) -> httpx.Request:
        return self.requests[-1]

    def body(self) -> dict[str, Any]:
        return json.loads(self.last.content)

    def query(self) -> dict[str, str]:
        return dict(self.last.url.params)


def client(api: Api) -> AuthenticatedClient:
    pidgeon = AuthenticatedClient(base_url="https://pidgeon.test/api/v1", token=KEY)
    pidgeon.set_httpx_client(
        httpx.Client(
            base_url="https://pidgeon.test/api/v1",
            headers={"Authorization": f"Bearer {KEY}"},
            transport=httpx.MockTransport(api),
        )
    )
    pidgeon.set_async_httpx_client(
        httpx.AsyncClient(
            base_url="https://pidgeon.test/api/v1",
            headers={"Authorization": f"Bearer {KEY}"},
            transport=httpx.MockTransport(api),
        )
    )
    return pidgeon


class Parsed:
    """For an answer whose model has two dozen required fields: what came back."""

    def __init__(self, payload: dict[str, Any]):
        self.payload = payload

    @classmethod
    def from_dict(cls, payload: dict[str, Any]) -> Parsed:
        return cls(payload)

    def to_dict(self) -> dict[str, Any]:
        return self.payload


# ------------------------------------------------------------ requests


def test_list_addresses_reads_identities() -> None:
    api = Api((200, PAGE))
    answer = ListAddresses(client=client(api)).invoke({"limit": 10})

    assert api.last.method == "GET"
    assert api.last.url.path == "/api/v1/identities"
    assert api.query() == {"limit": "10"}
    assert api.last.headers["authorization"] == f"Bearer {KEY}"
    assert json.loads(answer) == PAGE


def test_create_address_posts_the_body(monkeypatch: pytest.MonkeyPatch) -> None:
    monkeypatch.setattr(identities_create, "IdentitiesCreateResponse201", Parsed)
    api = Api((201, {"data": {"id": ID, "email": "scout@pidgeon.email"}}))
    answer = CreateAddress(client=client(api)).invoke(
        {"address": "scout@pidgeon.email", "type": "agent", "send_policy": "reply_only"}
    )

    assert (api.last.method, api.last.url.path) == ("POST", "/api/v1/identities")
    assert api.body() == {
        "address": "scout@pidgeon.email",
        "type": "agent",
        "send_policy": "reply_only",
    }
    assert json.loads(answer)["data"]["email"] == "scout@pidgeon.email"


def test_list_messages_is_clean_by_default() -> None:
    api = Api((200, PAGE))
    ListMessages(client=client(api)).invoke({"thread_id": ID})

    assert api.last.url.path == "/api/v1/messages"
    assert api.query() == {"thread_id": ID, "body": "clean", "limit": "50"}


def test_search_messages_spells_from_and_in_as_the_api_does() -> None:
    api = Api((200, PAGE))
    SearchMessages(client=client(api)).invoke(
        {"q": "invoice", "from_": "acme.com", "in_": "spam", "is_unread": True}
    )

    assert api.last.url.path == "/api/v1/messages/search"
    query = api.query()
    assert query["q"] == "invoice"
    assert query["from"] == "acme.com"
    assert query["in"] == "spam"
    assert query["is_unread"] == "true"


def test_get_message_is_clean_by_default(monkeypatch: pytest.MonkeyPatch) -> None:
    monkeypatch.setattr(messages_get, "MessagesGetResponse200", Parsed)
    api = Api((200, {"data": {"id": ID}}), (200, {"data": {"id": ID}}))
    tool = GetMessage(client=client(api))

    tool.invoke({"id": ID})
    assert api.last.url.path == f"/api/v1/messages/{ID}"
    assert api.query() == {"body": "clean"}

    tool.invoke({"id": ID, "body": "original"})
    assert api.query() == {"body": "original"}


def test_await_message_waits_for_a_code() -> None:
    api = Api((200, TIMED_OUT))
    answer = AwaitMessage(client=client(api)).invoke(
        {"identity_id": ID, "has_code": True, "timeout": 30, "from_": "github.com"}
    )

    assert api.last.url.path == "/api/v1/messages/await"
    assert api.query() == {
        "identity_id": ID,
        "body": "clean",
        "from": "github.com",
        "has_code": "true",
        "timeout": "30",
    }
    assert json.loads(answer)["data"]["timed_out"] is True


def test_await_message_takes_the_cursor_back() -> None:
    api = Api((200, TIMED_OUT))
    AwaitMessage(client=client(api)).invoke(
        {"identity_id": ID, "after": TIMED_OUT["data"]["cursor"]}
    )

    assert api.query()["after"].startswith("2026-10-22T10:00:00")


def test_the_client_waits_longer_than_await_can() -> None:
    pidgeon = PidgeonToolkit(api_key=KEY).client
    assert pidgeon.get_httpx_client().timeout.read >= 280 + 10


def test_send_message_sends_from() -> None:
    api = Api((202, SENT))
    SendMessage(client=client(api)).invoke(
        {"from_": "scout@pidgeon.email", "to": "ops@example.com", "subject": "Hi", "text": "Hello"}
    )

    assert (api.last.method, api.last.url.path) == ("POST", "/api/v1/messages")
    assert api.body() == {
        "from": "scout@pidgeon.email",
        "to": "ops@example.com",
        "subject": "Hi",
        "text": "Hello",
    }


def test_reply_puts_the_id_in_the_path() -> None:
    api = Api((202, SENT))
    ReplyToMessage(client=client(api)).invoke({"id": ID, "text": "Thanks."})

    assert (api.last.method, api.last.url.path) == ("POST", f"/api/v1/messages/{ID}/reply")
    assert api.body() == {"text": "Thanks."}


def test_update_thread_hands_it_to_a_person(monkeypatch: pytest.MonkeyPatch) -> None:
    monkeypatch.setattr(threads_update, "ThreadsUpdateResponse200", Parsed)
    api = Api((200, {"data": {"id": ID}}))
    UpdateThread(client=client(api)).invoke(
        {"id": ID, "owner_type": "human", "status": "human_review", "reason": "Asks for a refund."}
    )

    assert (api.last.method, api.last.url.path) == ("PATCH", f"/api/v1/threads/{ID}")
    assert api.body() == {
        "owner_type": "human",
        "status": "human_review",
        "reason": "Asks for a refund.",
    }


async def test_tools_work_async() -> None:
    api = Api((200, TIMED_OUT))
    answer = await AwaitMessage(client=client(api)).ainvoke({"identity_id": ID})

    assert api.last.url.path == "/api/v1/messages/await"
    assert json.loads(answer)["data"]["timed_out"] is True


# ------------------------------------------------------------ refusals


def test_a_refusal_reaches_the_model_as_the_apis_sentence() -> None:
    refusal = {
        "error": {"code": "forbidden", "message": "This key cannot send as scout@pidgeon.email."}
    }
    api = Api((403, refusal))
    answer = SendMessage(client=client(api)).invoke(
        {
            "name": "send_message",
            "args": {"from_": "scout@pidgeon.email", "to": "ops@example.com", "text": "Hi"},
            "id": "call_1",
            "type": "tool_call",
        }
    )

    assert isinstance(answer, ToolMessage)
    assert answer.status == "error"
    assert answer.content == "This key cannot send as scout@pidgeon.email."


def test_a_refusal_raises_when_asked_to() -> None:
    api = Api((404, {"error": {"code": "not_found", "message": "No such message."}}))
    tool = GetMessage(client=client(api), handle_tool_error=False)

    with pytest.raises(Exception, match="No such message."):
        tool.invoke({"id": ID})


# ------------------------------------------------------------ the key


def test_the_key_comes_from_the_environment(monkeypatch: pytest.MonkeyPatch) -> None:
    monkeypatch.setenv("PIDGEON_API_KEY", KEY)
    monkeypatch.delenv("PIDGEON_BASE_URL", raising=False)
    pidgeon = PidgeonToolkit().client

    assert pidgeon.token == KEY
    assert pidgeon._base_url == "https://pidgeon.ai/api/v1"


def test_no_key_is_a_sentence_saying_where_to_get_one(monkeypatch: pytest.MonkeyPatch) -> None:
    monkeypatch.delenv("PIDGEON_API_KEY", raising=False)

    with pytest.raises(ValueError, match="PIDGEON_API_KEY"):
        PidgeonToolkit()


def test_the_toolkit_shares_one_client() -> None:
    toolkit = PidgeonToolkit(api_key=KEY)
    tools = toolkit.get_tools()

    assert [tool.name for tool in tools] == [tool.model_fields["name"].default for tool in TOOLS]
    assert all(tool.client is toolkit.client for tool in tools)


# ------------------------------------------------------------ the MCP server's

MCP_TOOLS = Path(__file__).parents[3] / "mcp" / "src" / "tools.ts"


def mcp_hints() -> dict[str, dict[str, bool]]:
    """Each tool's four hints, read out of `packages/mcp/src/tools.ts`."""
    source = MCP_TOOLS.read_text()
    kinds = {
        name: {
            hint: value == "true" for hint, value in re.findall(r"(\w+Hint): (true|false)", body)
        }
        for name, body in re.findall(r"const (\w+): ToolAnnotations = \{([^}]*)\}", source)
    }
    return {
        name: kinds[kind]
        for name, kind in re.findall(r"name: '(\w+)',[\s\S]*?annotations: (\w+),", source)
    }


@pytest.mark.skipif(not MCP_TOOLS.exists(), reason="the MCP server's source is not beside this")
@pytest.mark.parametrize("tool", TOOLS, ids=lambda tool: tool.model_fields["name"].default)
def test_each_tool_is_an_mcp_tool_and_says_what_the_server_says(tool: type) -> None:
    name = tool.model_fields["name"].default
    hints = mcp_hints()

    assert name in hints, f"{name} is not a tool of the MCP server"
    assert tool.hints == hints[name]


@pytest.mark.parametrize("tool", TOOLS, ids=lambda tool: tool.model_fields["name"].default)
def test_the_description_opens_with_what_the_tool_does_to_the_world(tool: type) -> None:
    description = tool.model_fields["description"].default
    instance = tool(api_key=KEY)

    assert instance.metadata == tool.hints
    if tool.hints["readOnlyHint"]:
        assert description.startswith("Read-only")
    if tool.hints["destructiveHint"]:
        assert "cannot be unsent" in description
