"""The agent's identity: ``@pidgeon-ai/id``, in Python.

A signed identity for an AI agent on its operator's own domain, and the open
library it signs with:

- ``sign_email``: the ``Post-Envelope`` header, for mail sent through any provider.
- ``sign_request`` / ``signed_request`` / ``SigningAuth``: HTTP Message
  Signatures (RFC 9421) in Web Bot Auth's profile, for HTTP requests and for
  MCP over Streamable HTTP.
- ``verify_request``: the receiving side, for an MCP server or an API.
- ``sign_in_with_pidgeon`` / ``sign_in_with_api_key``: sign in to a website
  as the agent, with its card and grant.
- ``sign_a2a_card`` / ``verify_a2a_card``: the same identity inside an A2A
  Agent Card.
- ``IdClient``: issuance, as ``pidgeon id`` drives it.

**Hand-written, and it stays through regeneration**, like ``webhooks.py``:
``openapi-python-client`` rewrites only the modules it owns. Each module
mirrors a file in ``packages/id/src/`` and says which. The two languages
have the same capabilities by rule (``tests/unit/sdk-parity.test.ts`` names
every TypeScript export's Python twin here) and the same wire formats by
test (``tests/unit/python-identity.test.ts`` runs this package against the
TypeScript and against the server's own verifiers). The ``pidgeon id``
command-line tool is not ported: it is one binary for every language.

Synchronous, over ``httpx``; every call that sends takes an optional
``httpx.Client``, where the TypeScript takes a ``fetch``.
"""

from .a2a import (
    POST_A2A_EXTENSION,
    a2a_signing_payload,
    canonical_json,
    post_identity_extension,
    sign_a2a_card,
    verify_a2a_card,
)
from .api import IdApiError, IdClient, rotation_statement
from .email import SignedEmail, sign_email
from .http import SigningAuth, content_digest, sign_request, signed_request, verify_request
from .keys import (
    Identity,
    PreviousKey,
    StoredIdentity,
    generate_identity,
    identity_from_seed,
    jwk_thumbprint,
    load_identity,
    save_identity,
)
from .sign_in import (
    JWT_BEARER,
    PIDGEON_ISSUER,
    TOKEN_EXCHANGE,
    PidgeonSignIn,
    SignInError,
    dpop_proof,
    fetch_card,
    sign_in_with_api_key,
    sign_in_with_pidgeon,
    site_metadata,
)

__all__ = [
    "JWT_BEARER",
    "PIDGEON_ISSUER",
    "POST_A2A_EXTENSION",
    "TOKEN_EXCHANGE",
    "IdApiError",
    "IdClient",
    "Identity",
    "PidgeonSignIn",
    "PreviousKey",
    "SignInError",
    "SignedEmail",
    "SigningAuth",
    "StoredIdentity",
    "a2a_signing_payload",
    "canonical_json",
    "content_digest",
    "dpop_proof",
    "fetch_card",
    "generate_identity",
    "identity_from_seed",
    "jwk_thumbprint",
    "load_identity",
    "post_identity_extension",
    "rotation_statement",
    "save_identity",
    "sign_a2a_card",
    "sign_email",
    "sign_in_with_api_key",
    "sign_in_with_pidgeon",
    "sign_request",
    "signed_request",
    "site_metadata",
    "verify_a2a_card",
    "verify_request",
]
