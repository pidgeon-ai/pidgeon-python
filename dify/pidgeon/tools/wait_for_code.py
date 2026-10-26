from collections.abc import Generator
from typing import Any
from uuid import UUID

from dify_plugin import Tool
from dify_plugin.entities.tool import ToolInvokeMessage
from pidgeon.api.messages import messages_await
from pidgeon.errors import PidgeonError
from pidgeon.models import MessagesAwaitBody, MessagesAwaitHasCode

from tools.common import call, describe, flat_message, optional, text


class WaitForCodeTool(Tool):
    def _invoke(self, tool_parameters: dict[str, Any]) -> Generator[ToolInvokeMessage, None, None]:
        try:
            address_id = UUID(text(tool_parameters.get("address_id")))
        except ValueError:
            yield self.create_text_message("Address ID is an id such as 3f9c…, not an email address.")
            return
        timeout = min(max(int(tool_parameters.get("timeout") or 60), 1), 280)
        try:
            # Pidgeon holds the request open until mail arrives, so it outlives the wait.
            awaited = call(
                messages_await,
                self.runtime.credentials,
                request_timeout=timeout + 30,
                identity_id=address_id,
                body=MessagesAwaitBody.CLEAN,
                has_code=MessagesAwaitHasCode.TRUE,
                from_=optional(tool_parameters.get("from")),
                timeout=timeout,
            )
        except PidgeonError as error:
            yield self.create_text_message(describe(error))
            return
        result = awaited.get("data") or {}
        message = result.get("message")
        item = flat_message(message) if message else {}
        code = (item.get("codes") or [None])[0]
        yield self.create_json_message(
            {
                "code": code,
                **item,
                "timed_out": bool(result.get("timed_out", message is None)),
                "cursor": result.get("cursor"),
            }
        )
        yield self.create_text_message(
            f"The code is {code}." if code else f"No code arrived in {timeout} seconds."
        )
