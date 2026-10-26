from collections.abc import Generator
from typing import Any

from dify_plugin import Tool
from dify_plugin.entities.tool import ToolInvokeMessage
from pidgeon.api.messages import messages_reply
from pidgeon.errors import PidgeonError
from pidgeon.models import MessagesReplyBody

from tools.common import call, describe, text


class ReplyToEmailTool(Tool):
    def _invoke(self, tool_parameters: dict[str, Any]) -> Generator[ToolInvokeMessage, None, None]:
        message_id = text(tool_parameters.get("message_id"))
        if not message_id:
            yield self.create_text_message("Give the message_id of the message to answer.")
            return
        try:
            sent = call(
                messages_reply,
                self.runtime.credentials,
                id=message_id,
                body=MessagesReplyBody(text=str(tool_parameters.get("text") or "")),
            )
        except PidgeonError as error:
            yield self.create_text_message(describe(error))
            return
        data = sent["data"]
        yield self.create_json_message(data)
        yield self.create_text_message(f"Replied in thread {data.get('thread_id')} (message {data.get('id')}).")
