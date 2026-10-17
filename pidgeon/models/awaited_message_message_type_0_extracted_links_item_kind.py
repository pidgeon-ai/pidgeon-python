from enum import StrEnum


class AwaitedMessageMessageType0ExtractedLinksItemKind(StrEnum):
    OTHER = "other"
    VERIFICATION = "verification"

    def __str__(self) -> str:
        return str(self.value)
