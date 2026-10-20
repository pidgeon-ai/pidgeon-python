from enum import StrEnum


class AttachmentTextFirewallType0SignalsItemKind(StrEnum):
    ASSISTANT_DIRECTIVE = "assistant_directive"
    DISPLAY_NAME_SPOOF = "display_name_spoof"
    EXFILTRATION_REQUEST = "exfiltration_request"
    HIDDEN_TEXT = "hidden_text"
    INVISIBLE_CHARACTERS = "invisible_characters"
    LOOKALIKE_SENDER = "lookalike_sender"
    QUOTED_DIRECTIVE = "quoted_directive"
    ROLE_SPOOF = "role_spoof"
    UNAUTHENTICATED_WITH_DIRECTIVE = "unauthenticated_with_directive"

    def __str__(self) -> str:
        return str(self.value)
