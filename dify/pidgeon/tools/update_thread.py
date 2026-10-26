from collections.abc import Generator
from typing import Any

from dify_plugin import Tool
from dify_plugin.entities.tool import ToolInvokeMessage
from pidgeon.api.threads import threads_update
from pidgeon.errors import PidgeonError
from pidgeon.models import ThreadsUpdateBody, ThreadsUpdateBodyOwnerType, ThreadsUpdateBodyStatus
from pidgeon.types import UNSET

from tools.common import call, describe, optional, text


class UpdateThreadTool(Tool):
    def _invoke(self, tool_parameters: dict[str, Any]) -> Generator[ToolInvokeMessage, None, None]:
        thread_id = text(tool_parameters.get("thread_id"))
        owner = text(tool_parameters.get("owner"))
        status = text(tool_parameters.get("status"))
        if not thread_id:
            yield self.create_text_message("Give the thread_id of the thread to change.")
            return
        if not owner and not status:
            yield self.create_text_message("Choose an owner or a status to change.")
            return
        try:
            body = ThreadsUpdateBody(
                owner_type=ThreadsUpdateBodyOwnerType(owner) if owner else UNSET,
                status=ThreadsUpdateBodyStatus(status) if status else UNSET,
                reason=optional(tool_parameters.get("reason")),
            )
        except ValueError:
            yield self.create_text_message(
                "Owner is human or agent; status is open, waiting, resolved or human_review."
            )
            return
        try:
            updated = call(threads_update, self.runtime.credentials, id=thread_id, body=body)
        except PidgeonError as error:
            yield self.create_text_message(describe(error))
            return
        data = updated["data"]
        yield self.create_json_message(data)
        yield self.create_text_message(
            f"Thread {thread_id}: owner {data.get('owner_type')}, status {data.get('status')}."
        )
