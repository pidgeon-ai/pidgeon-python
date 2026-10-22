"""Every Pidgeon tool, sharing one client."""

from __future__ import annotations

from langchain_core.tools import BaseTool, BaseToolkit
from pidgeon import AuthenticatedClient
from pydantic import ConfigDict, Field, SecretStr, model_validator

from langchain_pidgeon.tools import TOOLS, client_from_env


class PidgeonToolkit(BaseToolkit):
    """Pidgeon's tools for one key: addresses, reading, waiting, sending, handing over.

    The key is the whole of the access control. It decides which addresses a
    tool can reach and whether it may send, on the server, whatever the
    prompt says, so give an agent the narrowest one its job needs.

    Each tool's `metadata` carries the hosted MCP server's hints
    (`readOnlyHint`, `destructiveHint`, `idempotentHint`, `openWorldHint`),
    which is how to choose the calls a person approves first:

        toolkit = PidgeonToolkit()
        asks_first = [t.name for t in toolkit.get_tools() if not t.metadata["readOnlyHint"]]
    """

    model_config = ConfigDict(arbitrary_types_allowed=True)

    client: AuthenticatedClient | None = Field(default=None, exclude=True)
    api_key: SecretStr | None = Field(default=None, exclude=True)
    base_url: str | None = Field(default=None, exclude=True)

    @model_validator(mode="after")
    def _connect(self) -> PidgeonToolkit:
        if self.client is None:
            self.client = client_from_env(
                self.api_key.get_secret_value() if self.api_key else None,
                self.base_url,
            )
        return self

    def get_tools(self) -> list[BaseTool]:
        return [tool(client=self.client) for tool in TOOLS]
