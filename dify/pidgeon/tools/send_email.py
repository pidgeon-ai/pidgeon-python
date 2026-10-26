from collections.abc import Generator
from typing import Any

from dify_plugin import Tool
from dify_plugin.entities.tool import ToolInvokeMessage
from pidgeon.api.messages import messages_send
from pidgeon.errors import PidgeonError
from pidgeon.models import MessagesSendBody
from pidgeon.types import UNSET

from tools.common import address_list, call, describe, text


class SendEmailTool(Tool):
    def _invoke(self, tool_parameters: dict[str, Any]) -> Generator[ToolInvokeMessage, None, None]:
        to = address_list(tool_parameters.get("to"))
        if not to:
            yield self.create_text_message("Name somebody to send to.")
            return
        cc = address_list(tool_parameters.get("cc"))
        body = MessagesSendBody(
            from_=text(tool_parameters.get("from")),
            to=to,
            cc=cc or UNSET,
            subject=text(tool_parameters.get("subject")),
            text=str(tool_parameters.get("text") or ""),
        )
        try:
            sent = call(messages_send, self.runtime.credentials, body=body)
        except PidgeonError as error:
            yield self.create_text_message(describe(error))
            return
        data = sent["data"]
        yield self.create_json_message(data)
        yield self.create_text_message(f"Sent to {', '.join(to)} (message {data.get('id')}).")
