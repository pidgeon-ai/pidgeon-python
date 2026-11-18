"""LangChain's own standard tests for a tool (``langchain-tests``), for each one."""

from __future__ import annotations

from typing import Any

from langchain_core.tools import BaseTool
from langchain_tests.unit_tests import ToolsUnitTests

from langchain_pidgeon import (
    AwaitMessage,
    GetMessage,
    GetReputation,
    GetThread,
    ListInboxes,
    ListThreads,
    RegisterAgent,
    ReplyToMessage,
    SendMessage,
    VerifyRequest,
)

KEY = "pgn_test_key"
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


class TestListInboxes(Standard):
    tool_class = ListInboxes


class TestSendMessage(Standard):
    tool_class = SendMessage
    example = {"inbox_id": ID, "to": ["ops@example.com"], "subject": "Hi", "text": "Hello"}


class TestReplyToMessage(Standard):
    tool_class = ReplyToMessage
    example = {"message_id": ID, "text": "Thanks."}


class TestListThreads(Standard):
    tool_class = ListThreads
    example = {"folder": "inbox"}


class TestGetThread(Standard):
    tool_class = GetThread
    example = {"thread_id": ID}


class TestGetMessage(Standard):
    tool_class = GetMessage
    example = {"message_id": ID}


class TestAwaitMessage(Standard):
    tool_class = AwaitMessage
    example = {"inbox_id": ID, "timeout": 10}


class TestRegisterAgent(Standard):
    tool_class = RegisterAgent
    example = {"name": "Scout", "purpose": "Books travel."}


class TestGetReputation(Standard):
    tool_class = GetReputation
    example = {"agent_id": ID}


class TestVerifyRequest(Standard):
    tool_class = VerifyRequest
    example = {"method": "GET", "url": "https://shop.example/", "headers": {"signature": "x"}}
