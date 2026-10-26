from typing import Any

from dify_plugin import ToolProvider
from dify_plugin.errors.tool import ToolProviderCredentialValidationError
from pidgeon.api.me import me_get
from pidgeon.errors import PidgeonError

from tools.common import call, describe


class PidgeonProvider(ToolProvider):
    def _validate_credentials(self, credentials: dict[str, Any]) -> None:
        if not str(credentials.get("api_key") or "").strip():
            raise ToolProviderCredentialValidationError("Paste a Pidgeon API key.")
        try:
            call(me_get, credentials)
        except PidgeonError as error:
            raise ToolProviderCredentialValidationError(describe(error)) from error
