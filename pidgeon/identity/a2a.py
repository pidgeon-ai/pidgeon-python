"""A Post identity inside an A2A Agent Card.

A2A 1.0.0 (``a2a-protocol.org/latest/specification`` §4.4.1 and §8.4, and
``specification/a2a.proto``, read 4 November). Two pieces, both A2A's own
mechanisms:

- **An extension** (``capabilities.extensions[]``, A2A's ``AgentExtension``),
  ``uri`` ``POST_A2A_EXTENSION``, whose ``params`` carry the agent's Post
  card: its address, kind, ``on_behalf_of``, the proved operator domain, the
  card URL and the card's JWS. A client that knows Post checks the JWS; one
  that does not ignores it, because ``required`` is false.
- **A signature** (``signatures[]``, A2A's ``AgentCardSignature``): JWS JSON
  form with the payload left out, over the RFC 8785 canonical form of the
  card without ``signatures``, by the operator's key. ``alg`` ``EdDSA``,
  ``kid`` the key's JWK thumbprint, ``jku`` the domain's Web Bot Auth key
  directory (``https://post.<domain>/.well-known/http-message-signatures-directory``),
  which is a JWKS. So the key that signs the agent's mail, its HTTP requests
  and its A2A card is one key, published once.

A2A's canonicalisation also drops proto default values. This drops
``signatures`` and empty arrays, as the spec's example does, and leaves every
other field as given: a card built by hand round-trips; a card re-serialised
by a proto library that drops ``false`` may not.

The twin of ``packages/id/src/a2a.ts``. RFC 8785 is the reason this file
exists in two languages without drifting: the canonical form is defined
byte for byte (keys sorted by UTF-16 code unit, ECMAScript number
spelling), so a card signed here verifies there and back, which
``tests/unit/python-identity.test.ts`` checks.
"""

from __future__ import annotations

import json
import math
from collections.abc import Callable, Mapping
from typing import Any

from ._js import b64url, from_b64url, js_number, js_string, js_stringify
from .keys import Identity, verify_bytes

__all__ = [
    "POST_A2A_EXTENSION",
    "a2a_signing_payload",
    "canonical_json",
    "post_identity_extension",
    "sign_a2a_card",
    "verify_a2a_card",
]

POST_A2A_EXTENSION = "https://pidgeon.ai/post/a2a/v0"


def post_identity_extension(card: Mapping[str, Any]) -> dict[str, Any]:
    """The ``AgentExtension`` that carries a Post card (the document ``pidgeon id issue`` returns)."""
    inner = card["card"]
    params: dict[str, Any] = {"address": inner["address"], "kind": inner["kind"]}
    if inner.get("on_behalf_of"):
        params["on_behalf_of"] = inner["on_behalf_of"]
    if inner.get("operator"):
        params["operator"] = inner["operator"]["domain"]
    params["card_url"] = card["url"]
    params["card_jws"] = card["jws"]
    return {
        "uri": POST_A2A_EXTENSION,
        "description": "Post agent identity: a signed card for this agent’s address and operator.",
        "required": False,
        "params": params,
    }


def canonical_json(value: Any) -> str:
    """RFC 8785 for JSON values: sorted keys (UTF-16 order), no whitespace, ECMAScript numbers."""
    if value is None or isinstance(value, (bool, str)):
        return js_stringify(value)
    if isinstance(value, (int, float)):
        if isinstance(value, float) and not math.isfinite(value):
            raise ValueError("JCS has no NaN or Infinity.")
        return js_number(value)
    if isinstance(value, (list, tuple)):
        return "[" + ",".join(canonical_json(item) for item in value) + "]"
    if isinstance(value, Mapping):
        entries = sorted(
            ((str(key), member) for key, member in value.items()), key=lambda entry: entry[0].encode("utf-16-be")
        )
        return "{" + ",".join(f"{js_string(key)}:{canonical_json(member)}" for key, member in entries) + "}"
    raise TypeError(f"{type(value).__name__} is not JSON.")


def _strip(value: Any) -> Any:
    if isinstance(value, (list, tuple)):
        return [_strip(item) for item in value]
    if isinstance(value, Mapping):
        return {
            key: _strip(member)
            for key, member in value.items()
            if not (isinstance(member, (list, tuple)) and len(member) == 0)
        }
    return value


def a2a_signing_payload(card: Mapping[str, Any]) -> str:
    """What A2A signs: the card without ``signatures``, empty arrays dropped, canonical."""
    rest = {key: member for key, member in card.items() if key != "signatures"}
    return canonical_json(_strip(rest))


def sign_a2a_card(identity: Identity, card: Mapping[str, Any], post: Mapping[str, Any] | None = None) -> dict[str, Any]:
    """The card with the Post extension added (replacing an older one) and signed by the operator's key.

    Any signature it already had is dropped: it was over a card without the extension.
    """
    capabilities = card["capabilities"]
    extensions = [
        extension for extension in capabilities.get("extensions") or [] if extension.get("uri") != POST_A2A_EXTENSION
    ]
    with_identity = {
        **card,
        "capabilities": {
            **capabilities,
            "extensions": [*extensions, post_identity_extension(post)] if post else extensions,
        },
    }
    with_identity.pop("signatures", None)

    header = {
        "alg": "EdDSA",
        "typ": "JOSE",
        "kid": identity.kid,
        "jku": f"https://post.{identity.domain}/.well-known/http-message-signatures-directory",
    }
    protected = b64url(js_stringify(header).encode("utf-8"))
    payload = b64url(a2a_signing_payload(with_identity).encode("utf-8"))
    signature = identity.sign(f"{protected}.{payload}".encode("ascii"))
    return {**with_identity, "signatures": [{"protected": protected, "signature": b64url(signature)}]}


def verify_a2a_card(card: Mapping[str, Any], key: Callable[[str, str | None], bytes | None]) -> dict[str, Any]:
    """Whether one of the card's signatures holds under the key ``key(kid, jku)`` finds.

    Fetch the JWKS at ``jku`` only from a host you trust for the operator's
    domain, such as ``post.<domain>``. Only ``EdDSA`` here. The answer is the
    TypeScript twin's: ``{"ok": True, "kid", "jku", "identity"}`` (the Post
    extension's ``params``, or ``None``), or ``{"ok": False, "reason"}``.
    """
    payload = b64url(a2a_signing_payload(card).encode("utf-8"))
    signatures = card.get("signatures") or []
    for entry in signatures:
        try:
            header = json.loads(from_b64url(entry["protected"]).decode("utf-8"))
        except (KeyError, TypeError, ValueError):
            continue
        if not isinstance(header, dict) or header.get("alg") != "EdDSA" or not isinstance(header.get("kid"), str):
            continue
        jku = header.get("jku")
        public_key = key(header["kid"], jku)
        if not public_key:
            continue
        try:
            signature = from_b64url(entry["signature"])
        except (KeyError, TypeError, ValueError):
            continue
        if verify_bytes(public_key, f"{entry['protected']}.{payload}".encode(), signature):
            extension = next(
                (
                    candidate
                    for candidate in (card.get("capabilities") or {}).get("extensions") or []
                    if candidate.get("uri") == POST_A2A_EXTENSION
                ),
                None,
            )
            return {
                "ok": True,
                "kid": header["kid"],
                "jku": jku,
                "identity": extension.get("params") if extension else None,
            }
    return {"ok": False, "reason": "no_signature_verifies" if signatures else "unsigned"}
