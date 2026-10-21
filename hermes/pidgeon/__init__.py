"""Pidgeon for Hermes Agent: email to your agent's address starts a conversation."""


def register(ctx) -> None:
    # Imported here so `pidgeon.core` loads without Hermes, for its tests.
    from .adapter import register as register_platform

    register_platform(ctx)
