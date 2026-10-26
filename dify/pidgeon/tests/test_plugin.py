"""
The plugin offline: each tool through the SDK's own `Tool.from_credentials`,
with HTTP answered at the transport, so our Python client runs as it would.
"""

import json
from pathlib import Path

import httpx
import pytest
import yaml
from dify_plugin.core.entities.plugin.setup import PluginConfiguration
from dify_plugin.entities.tool import ToolConfiguration, ToolProviderConfiguration
from dify_plugin.errors.tool import ToolProviderCredentialValidationError

from provider.pidgeon import PidgeonProvider
from tools.create_address import CreateAddressTool
from tools.reply_to_email import ReplyToEmailTool
from tools.search_emails import SearchEmailsTool
from tools.send_email import SendEmailTool
from tools.update_thread import UpdateThreadTool
from tools.wait_for_code import WaitForCodeTool

ROOT = Path(__file__).resolve().parents[1]
CREDENTIALS = {"api_key": "pgn_test_abc"}
IDENTITY = "3f9c2b1d-8c3e-4f1a-b2d4-6e9f0a1b2c3d"


@pytest.fixture
def api(monkeypatch):
    """Every request the client makes, and the answer to give it."""
    state = {"requests": [], "answer": lambda request: (200, {"data": {}})}

    def handle(self, request: httpx.Request) -> httpx.Response:
        state["requests"].append(request)
        status, body = state["answer"](request)
        return httpx.Response(status, json=body, request=request)

    monkeypatch.setattr(httpx.HTTPTransport, "handle_request", handle)
    return state


def run(tool_class, parameters):
    tool = tool_class.from_credentials(CREDENTIALS)
    messages = list(tool.invoke(parameters))
    json_message = next((m.message.json_object for m in messages if m.type.value == "json"), None)
    text_message = next((m.message.text for m in messages if m.type.value == "text"), None)
    return json_message, text_message


def body_of(request: httpx.Request) -> dict:
    return json.loads(request.content)


# The files Dify reads.


def test_the_manifest_and_every_yaml_load_as_dify_reads_them():
    manifest = yaml.safe_load((ROOT / "manifest.yaml").read_text())
    PluginConfiguration(**manifest)
    assert manifest["author"] == "pidgeon"
    for field in ("repo", "contact", "privacy"):
        assert manifest[field], f"the Marketplace requires {field}"
    assert (ROOT / "PRIVACY.md").read_text().strip()
    assert (ROOT / "_assets" / manifest["icon"]).exists()

    provider = yaml.safe_load((ROOT / "provider" / "pidgeon.yaml").read_text())
    assert provider["identity"]["author"] == manifest["author"]
    ToolProviderConfiguration(**{**provider, "tools": []})
    for tool_file in provider["tools"]:
        tool = yaml.safe_load((ROOT / tool_file).read_text())
        ToolConfiguration(**tool)
        assert tool["identity"]["author"] == manifest["author"]
        assert (ROOT / tool["extra"]["python"]["source"]).exists()


def test_tests_and_secrets_stay_out_of_the_package():
    ignored = (ROOT / ".difyignore").read_text().split()
    assert {"tests/", ".env", ".venv/"} <= set(ignored)


# The connection.


def test_the_key_is_checked_against_me(api):
    PidgeonProvider()._validate_credentials(CREDENTIALS)
    request = api["requests"][0]
    assert request.method == "GET"
    assert str(request.url) == "https://pidgeon.ai/api/v1/me"
    assert request.headers["authorization"] == "Bearer pgn_test_abc"


def test_a_refused_key_says_what_pidgeon_said(api):
    api["answer"] = lambda request: (
        401,
        {"error": {"code": "invalid_key", "message": "This key has been revoked."}},
    )
    with pytest.raises(ToolProviderCredentialValidationError, match="This key has been revoked"):
        PidgeonProvider()._validate_credentials(CREDENTIALS)


def test_an_empty_key_is_refused_before_any_request(api):
    with pytest.raises(ToolProviderCredentialValidationError, match="Paste a Pidgeon API key"):
        PidgeonProvider()._validate_credentials({"api_key": " "})
    assert api["requests"] == []


# The tools.


def test_send_posts_one_message_with_a_list_of_recipients(api):
    api["answer"] = lambda request: (202, {"data": {"id": "m1", "thread_id": "t1", "rejected": []}})
    data, summary = run(
        SendEmailTool,
        {
            "from": "quotes@acme.pidgeon.email",
            "to": "priya@supplier.de; ops@acme.com",
            "subject": "Angebot 4471",
            "text": "Danke.",
        },
    )
    request = api["requests"][0]
    assert (request.method, request.url.path) == ("POST", "/api/v1/messages")
    assert body_of(request) == {
        "from": "quotes@acme.pidgeon.email",
        "to": ["priya@supplier.de", "ops@acme.com"],
        "subject": "Angebot 4471",
        "text": "Danke.",
    }
    assert data["id"] == "m1"
    assert summary == "Sent to priya@supplier.de, ops@acme.com (message m1)."


def test_send_to_nobody_sends_nothing(api):
    _, summary = run(SendEmailTool, {"from": "a@b.c", "to": " , ", "subject": "x", "text": "y"})
    assert summary == "Name somebody to send to."
    assert api["requests"] == []


def test_a_refusal_comes_back_as_text_the_model_can_act_on(api):
    api["answer"] = lambda request: (
        403,
        {"error": {"code": "not_permitted", "message": "This address can only answer people who wrote first."}},
    )
    data, summary = run(SendEmailTool, {"from": "a@b.c", "to": "x@y.z", "subject": "s", "text": "t"})
    assert data is None
    assert summary == (
        "Pidgeon answered 403: This address can only answer people who wrote first. (not_permitted)"
    )


def test_reply_answers_by_message_id(api):
    api["answer"] = lambda request: (202, {"data": {"id": "m2", "thread_id": "t1", "rejected": []}})
    _, summary = run(ReplyToEmailTool, {"message_id": " m1 ", "text": "Danke!"})
    request = api["requests"][0]
    assert (request.method, request.url.path) == ("POST", "/api/v1/messages/m1/reply")
    assert body_of(request) == {"text": "Danke!"}
    assert summary == "Replied in thread t1 (message m2)."


def test_create_address_is_reply_only_unless_asked(api):
    api["answer"] = lambda request: (201, {"data": {"id": IDENTITY, "email": "quotes@acme.pidgeon.email"}})
    _, summary = run(CreateAddressTool, {"address": "quotes@acme.pidgeon.email"})
    body = body_of(api["requests"][0])
    assert body["address"] == "quotes@acme.pidgeon.email"
    assert body["send_policy"] == "reply_only"
    assert "display_name" not in body
    assert summary == f"Created quotes@acme.pidgeon.email (id {IDENTITY})."


def test_search_passes_the_folder_and_caps_the_limit(api):
    api["answer"] = lambda request: (200, {"data": [], "has_more": False, "next_cursor": None})
    data, summary = run(SearchEmailsTool, {"query": "Angebot", "folder": "inbox", "limit": 500, "address_id": IDENTITY})
    params = dict(api["requests"][0].url.params)
    assert params == {"q": "Angebot", "in": "inbox", "limit": "100", "identity_id": IDENTITY}
    assert data == {"messages": [], "has_more": False}
    assert summary == "Found 0 messages."


def test_search_refuses_an_email_where_an_id_goes(api):
    _, summary = run(SearchEmailsTool, {"address_id": "quotes@acme.pidgeon.email"})
    assert "not an email address" in summary
    assert api["requests"] == []


def test_wait_for_code_returns_the_code_and_outlives_the_wait(api, monkeypatch):
    api["answer"] = lambda request: (
        200,
        {
            "data": {
                "message": {
                    "id": "m1",
                    "thread_id": "t1",
                    "identity": "signup@acme.pidgeon.email",
                    "from": {"email": "no-reply@github.com", "name": "GitHub"},
                    "to": [{"email": "signup@acme.pidgeon.email"}],
                    "subject": "Your code",
                    "extracted": {"codes": [{"value": "482910"}], "links": []},
                    "authentication": {"dmarc": "pass"},
                },
                "timed_out": False,
                "cursor": "c1",
            }
        },
    )
    data, summary = run(WaitForCodeTool, {"address_id": IDENTITY, "from": "no-reply@github.com", "timeout": 999})
    request = api["requests"][0]
    assert request.url.path == "/api/v1/messages/await"
    assert dict(request.url.params) == {
        "identity_id": IDENTITY,
        "body": "clean",
        "from": "no-reply@github.com",
        "has_code": "true",
        "timeout": "280",
    }
    assert request.extensions["timeout"]["read"] == 310
    assert data["code"] == "482910"
    assert data["from"] == "no-reply@github.com"
    assert data["auth_dmarc"] == "pass"
    assert data["timed_out"] is False
    assert summary == "The code is 482910."


def test_nothing_arriving_is_an_answer(api):
    api["answer"] = lambda request: (200, {"data": {"message": None, "timed_out": True, "cursor": "c2"}})
    data, summary = run(WaitForCodeTool, {"address_id": IDENTITY, "timeout": 5})
    assert data == {"code": None, "timed_out": True, "cursor": "c2"}
    assert summary == "No code arrived in 5 seconds."


def test_update_thread_hands_it_to_a_person(api):
    api["answer"] = lambda request: (200, {"data": {"id": "t1", "owner_type": "human", "status": "open"}})
    _, summary = run(UpdateThreadTool, {"thread_id": "t1", "owner": "human", "reason": "Needs a price"})
    request = api["requests"][0]
    assert (request.method, request.url.path) == ("PATCH", "/api/v1/threads/t1")
    assert body_of(request) == {"owner_type": "human", "reason": "Needs a price"}
    assert summary == "Thread t1: owner human, status open."


def test_update_thread_that_changes_nothing_sends_nothing(api):
    _, summary = run(UpdateThreadTool, {"thread_id": "t1"})
    assert summary == "Choose an owner or a status to change."
    assert api["requests"] == []
