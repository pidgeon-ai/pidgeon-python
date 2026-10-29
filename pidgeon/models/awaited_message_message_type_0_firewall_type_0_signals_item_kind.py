from enum import StrEnum


class AwaitedMessageMessageType0FirewallType0SignalsItemKind(StrEnum):
    ASSISTANT_DIRECTIVE = "assistant_directive"
    DISPLAY_NAME_SPOOF = "display_name_spoof"
    EXFILTRATION_REQUEST = "exfiltration_request"
    HIDDEN_TEXT = "hidden_text"
    INVISIBLE_CHARACTERS = "invisible_characters"
    LOOKALIKE_SENDER = "lookalike_sender"
    QUOTED_DIRECTIVE = "quoted_directive"
    ROLE_SPOOF = "role_spoof"
    UNAUTHENTICATED_WITH_DIRECTIVE = "unauthenticated_with_directive"

    @classmethod
    def _missing_(cls, value: object) -> "AwaitedMessageMessageType0FirewallType0SignalsItemKind | None":
        # A value the API added after this client was published (a new
        # Firewall signal kind, say) is kept as itself rather than raising:
        # an additive change to the API must not break a published client.
        # `docs/email.md` → Pidgeon Firewall, firewall.md §6.
        if not isinstance(value, str):
            return None
        member = str.__new__(cls, value)
        member._name_ = value.upper()
        member._value_ = value
        return member

    def __str__(self) -> str:
        return str(self.value)
