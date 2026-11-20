"""
Pidgeon's Python SDK: email inboxes for AI agents.

``Pidgeon(api_key).email`` is Email: inboxes on @pidgeon.email or your own
domain, messages, waiting for mail, threads, labels, contacts, attachments,
domains and calendars. For a platform, ``.pods`` gives each of your users
inboxes of their own; ``.keys``, ``.webhooks`` and ``.events`` are the account.

Sign in with Pidgeon: ``.agents.set_up()`` registers an agent, makes its key
here and publishes the public half; ``signed_client`` or
``agent_from_env().client()`` signs its requests; ``pidgeon.auth`` has
``sign_in_as_agent`` for an agent, and ``verify_id_token`` and
``verify_agent_sign_in`` for a site. ``.sites`` and ``.mandates`` register
sites and ask people's permission.
"""

from . import auth, verdict
from .client import (
    DEFAULT_BASE_URL,
    Agent,
    AgentAuth,
    AgentSetUp,
    Pidgeon,
    PidgeonError,
    UNSET,
    agent_from_env,
    signed_async_client,
    signed_client,
)
from .credential import (
    DEFAULT_LIFETIME_SECONDS,
    MAX_LIFETIME_SECONDS,
    AgentKey,
    Verification,
    directory_url,
    generate_agent_key,
    is_public_jwk,
    key_id_of,
    new_nonce,
    sign_request,
    verify_agent_request,
)

__version__ = "2.12.0"

from .webhooks import sign_webhook, verify_webhook

__all__ = [
    "auth",
    "verdict",
    "sign_webhook",
    "verify_webhook",
    "DEFAULT_BASE_URL",
    "DEFAULT_LIFETIME_SECONDS",
    "MAX_LIFETIME_SECONDS",
    "Agent",
    "AgentAuth",
    "AgentSetUp",
    "AgentKey",
    "Pidgeon",
    "PidgeonError",
    "UNSET",
    "Verification",
    "agent_from_env",
    "directory_url",
    "generate_agent_key",
    "is_public_jwk",
    "key_id_of",
    "new_nonce",
    "sign_request",
    "signed_async_client",
    "signed_client",
    "verify_agent_request",
]
