from collections.abc import Generator
from typing import Any

from dify_plugin import Tool
from dify_plugin.entities.tool import ToolInvokeMessage
from pidgeon.api.identities import identities_create
from pidgeon.errors import PidgeonError
from pidgeon.models import (
    IdentitiesCreateBody,
    IdentitiesCreateBodySendPolicy,
    IdentitiesCreateBodyType,
)

from tools.common import call, describe, optional, text


class CreateAddressTool(Tool):
    def _invoke(self, tool_parameters: dict[str, Any]) -> Generator[ToolInvokeMessage, None, None]:
        address = text(tool_parameters.get("address"))
        if "@" not in address:
            yield self.create_text_message("Give the whole address, such as quotes@acme.pidgeon.email.")
            return
        body = IdentitiesCreateBody(
            address=address,
            display_name=optional(tool_parameters.get("display_name")),
            type_=IdentitiesCreateBodyType.AGENT,
            send_policy=IdentitiesCreateBodySendPolicy(
                text(tool_parameters.get("send_policy")) or "reply_only"
            ),
        )
        try:
            created = call(identities_create, self.runtime.credentials, body=body)
        except PidgeonError as error:
            yield self.create_text_message(describe(error))
            return
        data = created["data"]
        yield self.create_json_message(data)
        yield self.create_text_message(f"Created {data.get('email')} (id {data.get('id')}).")
