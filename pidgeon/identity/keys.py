"""An operator's signing key for one domain.

Ed25519, made on this machine and never sent anywhere: Pidgeon holds only the
public half. ``kid`` is the key's RFC 8037 JWK thumbprint, which is what Web
Bot Auth calls a ``keyid`` and what the domain's ``post.json`` lists, so one
name finds the key from an email, an HTTP request and the policy alike.

The twin of ``packages/id/src/keys.ts``. The TypeScript signs through
``post-core``, the protocol's Rust core compiled to WebAssembly; this signs
through OpenSSL (``cryptography``). Ed25519 is deterministic, so the same seed
gives the same public key and the same signature in both, and
``tests/unit/python-identity.test.ts`` checks that it does.

**The identity file is shared with the TypeScript library and the ``pidgeon
id`` command-line tool**: same directory (``$PIDGEON_ID_DIR``, else
``$XDG_CONFIG_HOME/pidgeon/id``, else ``~/.config/pidgeon/id``), one
``<domain>.json`` per domain, mode 0600, the same JSON to the byte. A key
made with ``pidgeon id init`` signs from Python without a conversion, and the
other way round.
"""

from __future__ import annotations

import json
import os
from collections.abc import Mapping
from dataclasses import dataclass, field
from hashlib import sha256
from typing import Protocol

from cryptography.exceptions import InvalidSignature
from cryptography.hazmat.primitives.asymmetric.ed25519 import Ed25519PrivateKey, Ed25519PublicKey

from ._js import b64url, from_b64url

__all__ = [
    "Identity",
    "PreviousKey",
    "StoredIdentity",
    "generate_identity",
    "identity_dir",
    "identity_from_seed",
    "jwk_thumbprint",
    "list_identities",
    "load_identity",
    "save_identity",
    "verify_bytes",
]


class Identity(Protocol):
    """What signs: a domain, its key's ``kid`` and public half, and Ed25519 over exact bytes."""

    domain: str
    kid: str
    public_key: bytes

    def sign(self, message: bytes) -> bytes: ...


@dataclass(frozen=True)
class PreviousKey:
    """The key an identity replaced, while receivers may still hold it."""

    kid: str
    public_key: bytes


@dataclass
class StoredIdentity:
    """An identity with its private key: the seed, kept in the identity file and nowhere else."""

    domain: str
    kid: str
    public_key: bytes
    seed: bytes = field(repr=False)
    previous: PreviousKey | None = None

    def sign(self, message: bytes) -> bytes:
        """Ed25519 over exactly these bytes."""
        return Ed25519PrivateKey.from_private_bytes(self.seed).sign(bytes(message))


def jwk_thumbprint(public_key: bytes) -> str:
    """RFC 8037 §A.3."""
    jwk = f'{{"crv":"Ed25519","kty":"OKP","x":"{b64url(public_key)}"}}'
    return b64url(sha256(jwk.encode("ascii")).digest())


def verify_bytes(public_key: bytes, message: bytes, signature: bytes) -> bool:
    """Whether ``signature`` is ``public_key``'s over ``message``. Never raises."""
    try:
        Ed25519PublicKey.from_public_bytes(bytes(public_key)).verify(bytes(signature), bytes(message))
        return True
    except (InvalidSignature, ValueError, TypeError):
        return False


def identity_from_seed(domain: str, seed: bytes) -> StoredIdentity:
    """The identity a 32-byte seed makes, for ``domain``."""
    seed = bytes(seed)
    public_key = Ed25519PrivateKey.from_private_bytes(seed).public_key().public_bytes_raw()
    return StoredIdentity(domain=domain.lower(), kid=jwk_thumbprint(public_key), public_key=public_key, seed=seed)


def generate_identity(domain: str) -> StoredIdentity:
    """A new key for ``domain``, from the operating system's randomness."""
    return identity_from_seed(domain, os.urandom(32))


# --- On disk ------------------------------------------------------------------


def identity_dir(env: Mapping[str, str] | None = None) -> str:
    """``$PIDGEON_ID_DIR``, else ``~/.config/pidgeon/id``. One file per domain."""
    env = os.environ if env is None else env
    config = env.get("XDG_CONFIG_HOME") or os.path.join(os.path.expanduser("~"), ".config")
    return env.get("PIDGEON_ID_DIR") or os.path.join(config, "pidgeon", "id")


def save_identity(identity: StoredIdentity, dir: str | None = None) -> str:
    """Writes ``<dir>/<domain>.json``, mode 0600, and returns its path."""
    dir = identity_dir() if dir is None else dir
    os.makedirs(dir, mode=0o700, exist_ok=True)
    path = os.path.join(dir, f"{identity.domain}.json")
    file = {
        "v": 1,
        "domain": identity.domain,
        "kid": identity.kid,
        "seed": b64url(identity.seed),
        "previous": (
            {"kid": identity.previous.kid, "public_key": b64url(identity.previous.public_key)}
            if identity.previous
            else None
        ),
    }
    # `JSON.stringify(file, null, 2)` and a newline, which `json.dumps` writes identically.
    text = json.dumps(file, indent=2, ensure_ascii=False) + "\n"
    descriptor = os.open(path, os.O_WRONLY | os.O_CREAT | os.O_TRUNC, 0o600)
    with os.fdopen(descriptor, "w", encoding="utf-8") as handle:
        handle.write(text)
    os.chmod(path, 0o600)
    return path


def load_identity(domain: str, *, dir: str | None = None, env: Mapping[str, str] | None = None) -> StoredIdentity:
    """The identity for ``domain``.

    From ``PIDGEON_ID_KEY`` (``<domain>:<seed>``, for a server the operator
    deploys to) when it names this domain, else from the identity file.
    """
    env = os.environ if env is None else env
    name = domain.lower()
    from_env = env.get("PIDGEON_ID_KEY")
    if from_env is not None:
        parts = from_env.split(":")
        if len(parts) == 2 and parts[0].lower() == name:
            return identity_from_seed(name, from_b64url(parts[1]))

    path = os.path.join(identity_dir(env) if dir is None else dir, f"{name}.json")
    try:
        with open(path, encoding="utf-8") as handle:
            file = json.load(handle)
    except (OSError, ValueError):
        raise FileNotFoundError(
            f"No identity for {name} on this machine. Run `pidgeon id init {name}` first."
        ) from None

    identity = identity_from_seed(file["domain"], from_b64url(file["seed"]))
    if identity.kid != file["kid"]:
        raise ValueError(f"{path} is damaged: its key does not match its kid.")
    previous = file.get("previous")
    identity.previous = (
        PreviousKey(kid=previous["kid"], public_key=from_b64url(previous["public_key"])) if previous else None
    )
    return identity


def list_identities(dir: str | None = None) -> list[str]:
    """The domains with an identity file here."""
    try:
        names = os.listdir(identity_dir() if dir is None else dir)
    except OSError:
        return []
    return [name[:-5] for name in names if name.endswith(".json")]
