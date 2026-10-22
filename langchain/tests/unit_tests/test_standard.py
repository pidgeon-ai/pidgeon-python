"""LangChain's own standard tests for a tool (`langchain-tests`), for each one."""

from __future__ import annotations

from typing import Any

from langchain_core.tools import BaseTool
from langchain_tests.unit_tests import ToolsUnitTests

from langchain_pidgeon import (
    AwaitMessage,
    CreateAddress,
    GetMessage,
    ListAddresses,
    ListMessages,
    ReplyToMessage,
    SearchMessages,
    SendMessage,
    UpdateThread,
)

KEY = "pgn_live_test"
ID = "0b5d1c1e-6a3f-4c55-9a8e-1f2d3c4b5a69"


class Standard(ToolsUnitTests):
    tool_class: type[BaseTool]
    example: dict[str, Any] = {}

    @property
    def tool_constructor(self) -> type[BaseTool]:
        return self.tool_class

    @property
    def tool_constructor_params(self) -> dict[str, Any]:
        return {"api_key": KEY}

    @property
    def tool_invoke_params_example(self) -> dict[str, Any]:
        return self.example

    @property
    def init_from_env_params(self) -> tuple[dict[str, str], dict[str, Any], dict[str, Any]]:
        return {"PIDGEON_API_KEY": KEY}, {}, {"handle_tool_error": True}


class TestListAddresses(Standard):
    tool_class = ListAddresses
    example = {"limit": 10}


class TestCreateAddress(Standard):
    tool_class = CreateAddress
    example = {"address": "scout@pidgeon.email", "send_policy": "reply_only"}


class TestListMessages(Standard):
    tool_class = ListMessages
    example = {"thread_id": ID}


class TestSearchMessages(Standard):
    tool_class = SearchMessages
    example = {"q": "invoice"}


class TestGetMessage(Standard):
    tool_class = GetMessage
    example = {"id": ID}


class TestAwaitMessage(Standard):
    tool_class = AwaitMessage
    example = {"identity_id": ID, "has_code": True}


class TestSendMessage(Standard):
    tool_class = SendMessage
    example = {"from_": "scout@pidgeon.email", "to": "ops@example.com", "text": "Hello"}


class TestReplyToMessage(Standard):
    tool_class = ReplyToMessage
    example = {"id": ID, "text": "Thanks."}


class TestUpdateThread(Standard):
    tool_class = UpdateThread
    example = {"id": ID, "owner_type": "human", "status": "human_review"}
