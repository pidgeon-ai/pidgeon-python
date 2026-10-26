from collections.abc import Generator
from typing import Any
from uuid import UUID

from dify_plugin import Tool
from dify_plugin.entities.tool import ToolInvokeMessage
from pidgeon.api.messages import messages_search
from pidgeon.errors import PidgeonError
from pidgeon.models import MessagesSearchIn
from pidgeon.types import UNSET

from tools.common import call, describe, optional, text


class SearchEmailsTool(Tool):
    def _invoke(self, tool_parameters: dict[str, Any]) -> Generator[ToolInvokeMessage, None, None]:
        address_id = text(tool_parameters.get("address_id"))
        folder = text(tool_parameters.get("folder"))
        try:
            limit = min(max(int(tool_parameters.get("limit") or 20), 1), 100)
            found = call(
                messages_search,
                self.runtime.credentials,
                q=optional(tool_parameters.get("query")),
                identity_id=UUID(address_id) if address_id else UNSET,
                from_=optional(tool_parameters.get("from")),
                in_=MessagesSearchIn(folder) if folder else UNSET,
                limit=limit,
            )
        except ValueError:
            yield self.create_text_message("Address ID is an id such as 3f9c…, not an email address.")
            return
        except PidgeonError as error:
            yield self.create_text_message(describe(error))
            return
        messages = found.get("data") or []
        yield self.create_json_message({"messages": messages, "has_more": bool(found.get("has_more"))})
        yield self.create_text_message(f"Found {len(messages)} message{'s' if len(messages) != 1 else ''}.")
