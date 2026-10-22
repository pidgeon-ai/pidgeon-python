"""PidgeonToolSpec, against the SDK functions it calls and the API's refusals.

The calls are replaced one level down, at the generated SDK function, so these
tests hold what reaches the API: which operation, with which arguments. The
live test at the end runs every read against a real Pidgeon when
PIDGEON_API_KEY is set.
"""

import json
import os
from types import SimpleNamespace
from typing import Any, Dict, List, Tuple

import httpx
import pytest
from llama_index.core.tools.tool_spec.base import BaseToolSpec
from llama_index.tools.pidgeon import PidgeonToolSpec
from llama_index.tools.pidgeon import base
from pidgeon import AuthenticatedClient
from pidgeon.types import UNSET

ADDRESS = "0b6c7c1e-8a52-4d77-9a1e-0c1b2a3d4e5f"
MESSAGE = "7d1f0a2b-3c4d-4e5f-8a9b-0c1d2e3f4a5b"


class Recorder:
    """Stands in for one generated module: records each `sync` call."""

    def __init__(self) -> None:
        self.calls: List[Tuple[Tuple[Any, ...], Dict[str, Any]]] = []

    def sync(self, *args: Any, **kwargs: Any) -> Any:
        self.calls.append((args, kwargs))
        return SimpleNamespace(to_dict=lambda: {"data": "ok"})


@pytest.fixture
def spec() -> PidgeonToolSpec:
    return PidgeonToolSpec(api_key="pgn_live_test")


def record(monkeypatch: pytest.MonkeyPatch, name: str) -> Recorder:
    recorder = Recorder()
    monkeypatch.setattr(base, name, recorder)
    return recorder


def test_class() -> None:
    names_of_base_classes = [b.__name__ for b in PidgeonToolSpec.__mro__]
    assert BaseToolSpec.__name__ in names_of_base_classes


def test_every_spec_function_becomes_a_tool(spec: PidgeonToolSpec) -> None:
    tools = spec.to_tool_list()
    assert [tool.metadata.name for tool in tools] == PidgeonToolSpec.spec_functions
    for tool in tools:
        assert tool.metadata.description.strip(), tool.metadata.name


def test_the_key_comes_from_the_environment(monkeypatch: pytest.MonkeyPatch) -> None:
    monkeypatch.setenv("PIDGEON_API_KEY", "pgn_live_from_env")
    assert PidgeonToolSpec().client.token == "pgn_live_from_env"


def test_no_key_is_a_clear_error(monkeypatch: pytest.MonkeyPatch) -> None:
    monkeypatch.delenv("PIDGEON_API_KEY", raising=False)
    with pytest.raises(ValueError, match="PIDGEON_API_KEY"):
        PidgeonToolSpec()


def test_a_held_open_wait_outlasts_the_http_default(spec: PidgeonToolSpec) -> None:
    # httpx reads for 5 seconds by default; await_message waits up to 280.
    assert spec.client.get_httpx_client().timeout.read >= 280


def test_bodies_are_cleaned_unless_asked(
    spec: PidgeonToolSpec, monkeypatch: pytest.MonkeyPatch
) -> None:
    # The SDK's own default is "original"; the model's is "clean".
    get = record(monkeypatch, "messages_get")
    listing = record(monkeypatch, "messages_list_in_thread")
    awaited = record(monkeypatch, "messages_await")

    spec.get_message(MESSAGE)
    spec.list_messages("thread")
    spec.await_message(ADDRESS)
    spec.get_message(MESSAGE, body="original")

    assert str(get.calls[0][1]["body"]) == "clean"
    assert str(listing.calls[0][1]["body"]) == "clean"
    assert str(awaited.calls[0][1]["body"]) == "clean"
    assert str(get.calls[1][1]["body"]) == "original"


def test_a_new_address_is_reply_only_by_default(
    spec: PidgeonToolSpec, monkeypatch: pytest.MonkeyPatch
) -> None:
    create = record(monkeypatch, "identities_create")

    spec.create_address(address="scout@pidgeon.email")
    spec.create_address(address="open@pidgeon.email", reply_only=False)

    first = create.calls[0][1]["body"].to_dict()
    assert first == {
        "address": "scout@pidgeon.email",
        "type": "agent",
        "send_policy": "reply_only",
    }
    assert create.calls[1][1]["body"].to_dict()["send_policy"] == "open"


def test_a_reply_brings_only_the_words(
    spec: PidgeonToolSpec, monkeypatch: pytest.MonkeyPatch
) -> None:
    reply = record(monkeypatch, "messages_reply")

    spec.reply_to_message(MESSAGE, "Thanks, that worked.")

    args, kwargs = reply.calls[0]
    assert args == (MESSAGE,)
    assert kwargs["body"].to_dict() == {"text": "Thanks, that worked."}


def test_send_says_who_from(spec: PidgeonToolSpec, monkeypatch: pytest.MonkeyPatch) -> None:
    send = record(monkeypatch, "messages_send")

    spec.send_message("scout@pidgeon.email", ["ops@example.com"], "Access", "Could you?")

    assert send.calls[0][1]["body"].to_dict() == {
        "from": "scout@pidgeon.email",
        "to": ["ops@example.com"],
        "subject": "Access",
        "text": "Could you?",
    }


def test_a_draft_answers_the_message_it_names(
    spec: PidgeonToolSpec, monkeypatch: pytest.MonkeyPatch
) -> None:
    draft = record(monkeypatch, "drafts_create")

    spec.create_draft(ADDRESS, "Proposed answer", in_reply_to_message_id=MESSAGE)

    assert draft.calls[0][1]["body"].to_dict() == {
        "identity_id": ADDRESS,
        "text": "Proposed answer",
        "in_reply_to": MESSAGE,
    }


def test_a_wait_narrows_and_resumes(
    spec: PidgeonToolSpec, monkeypatch: pytest.MonkeyPatch
) -> None:
    awaited = record(monkeypatch, "messages_await")

    spec.await_message(ADDRESS, from_address="example.com", has_code=True, timeout=30)
    spec.await_message(ADDRESS, after="2026-10-22T10:00:00.000Z")

    first = awaited.calls[0][1]
    assert first["identity_id"] == ADDRESS
    assert first["from_"] == "example.com"
    assert str(first["has_code"]) == "true"
    assert first["timeout"] == 30
    assert first["after"] is UNSET
    assert awaited.calls[1][1]["after"].isoformat() == "2026-10-22T10:00:00+00:00"


def test_unset_filters_are_left_out(
    spec: PidgeonToolSpec, monkeypatch: pytest.MonkeyPatch
) -> None:
    threads = record(monkeypatch, "threads_list")
    search = record(monkeypatch, "messages_search")

    spec.list_threads()
    spec.search_messages(q="invoice")

    assert threads.calls[0][1]["identity_id"] is UNSET
    assert threads.calls[0][1]["status"] is UNSET
    assert search.calls[0][1]["q"] == "invoice"
    assert search.calls[0][1]["from_"] is UNSET


def test_a_refusal_reaches_the_model_with_the_apis_sentence() -> None:
    """A refused send is a value the agent reads, not an exception that ends the run."""

    def refuse(request: httpx.Request) -> httpx.Response:
        assert request.headers["Authorization"] == "Bearer pgn_live_test"
        return httpx.Response(
            403,
            headers={"Retry-After": "30"},
            json={
                "error": {
                    "code": "insufficient_access",
                    "message": "This key can read this address but not send from it.",
                    "field": "from",
                }
            },
        )

    client = AuthenticatedClient(
        base_url="https://pidgeon.ai/api/v1",
        token="pgn_live_test",
        httpx_args={"transport": httpx.MockTransport(refuse)},
    )
    result = PidgeonToolSpec(client=client).send_message(
        "scout@pidgeon.email", ["ops@example.com"], "Hi", "Hello"
    )

    assert result == {
        "error": {
            "code": "insufficient_access",
            "message": "This key can read this address but not send from it.",
            "field": "from",
            "retry_after": 30,
        }
    }


@pytest.mark.skipif(not os.environ.get("PIDGEON_API_KEY"), reason="needs PIDGEON_API_KEY")
def test_live_reads() -> None:
    """Every read function, against a real Pidgeon."""
    spec = PidgeonToolSpec(base_url=os.environ.get("PIDGEON_BASE_URL", base.BASE_URL))

    addresses = spec.list_addresses(limit=5)
    assert "error" not in addresses, addresses
    assert addresses["data"], "the key reaches no address"
    identity = addresses["data"][0]["id"]

    threads = spec.list_threads(identity_id=identity, limit=1)
    assert "error" not in threads, threads
    if threads["data"]:
        messages = spec.list_messages(threads["data"][0]["id"], limit=1)
        assert "error" not in messages, messages
        if messages["data"]:
            message = spec.get_message(messages["data"][0]["id"])
            assert "error" not in message, message

    found = spec.search_messages(identity_id=identity, q="the", limit=1)
    assert "error" not in found, found

    awaited = spec.await_message(identity, timeout=1)
    assert "error" not in awaited, awaited
    assert json.dumps(awaited)
