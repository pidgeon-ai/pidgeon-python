"""Every Pidgeon tool, sharing one client."""

from __future__ import annotations

from pathlib import Path

from langchain_core.tools import BaseTool, BaseToolkit
from pidgeon import Pidgeon
from pydantic import ConfigDict, Field, SecretStr, model_validator

from langchain_pidgeon.tools import TOOLS, RegisterAgent, client_from_env


class PidgeonToolkit(BaseToolkit):
    """Pidgeon's tools for one API key: the agent's email inbox, and its Sign in with Pidgeon key.

    The key is the access control: it decides, on Pidgeon's side, which
    inboxes a tool reaches and whether it may send, whatever the prompt says.
    Give an agent the narrowest key its job needs.

    Each tool's ``metadata`` carries ``readOnlyHint``, ``destructiveHint`` and
    ``openWorldHint``, to choose the calls a person approves first::

        tools = PidgeonToolkit().get_tools()
        ask_first = [t.name for t in tools if not t.metadata["readOnlyHint"]]
    """

    model_config = ConfigDict(arbitrary_types_allowed=True)

    client: Pidgeon | None = Field(default=None, exclude=True)
    api_key: SecretStr | None = Field(default=None, exclude=True)
    base_url: str | None = Field(default=None, exclude=True)
    key_dir: Path | None = Field(default=None, exclude=True)

    @model_validator(mode="after")
    def _connect(self) -> PidgeonToolkit:
        if self.client is None:
            self.client = client_from_env(
                self.api_key.get_secret_value() if self.api_key else None, self.base_url
            )
        return self

    def get_tools(self) -> list[BaseTool]:
        return [
            tool(client=self.client, key_dir=self.key_dir)
            if tool is RegisterAgent
            else tool(client=self.client)
            for tool in TOOLS
        ]
