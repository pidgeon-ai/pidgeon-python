from enum import StrEnum


class MessageExtractedLinksItemKind(StrEnum):
    OTHER = "other"
    VERIFICATION = "verification"

    def __str__(self) -> str:
        return str(self.value)
