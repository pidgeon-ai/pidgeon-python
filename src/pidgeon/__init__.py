"""
Pidgeon's Python SDK.

For an agent: ``signed_client`` or ``agent_from_env().client()`` signs every
request with the agent's key, so a website that checks can tell who stands
behind it.

For a website: ``Pidgeon(api_key).verify(method, url, headers)`` asks Pidgeon
who stands behind an agent's request and how they stand; ``.report()``
reports one that misbehaved.

Sign in with Pidgeon (``pidgeon.auth``): ``sign_in_as_agent`` for an agent,
``verify_id_token`` and ``verify_agent_sign_in`` for a site.

Verdicts at sign-up (``pidgeon.verdict``): ``verify_verdict`` checks the
verdict ``verify`` answered, offline, in a hook that cannot see the request.

For an operator's tooling and coding agents: ``.agents.set_up()`` registers
an agent, makes its key here and publishes the public half; ``.email`` is
Email (inboxes, messages, threads, labels, contacts, attachments, domains,
calendars); ``.sites`` and ``.mandates`` are Auth; ``.events``, ``.webhooks``
and ``.pods`` are the account.
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

__version__ = "2.10.0"

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
