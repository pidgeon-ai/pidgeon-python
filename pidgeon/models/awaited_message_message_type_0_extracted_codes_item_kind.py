from enum import StrEnum


class AwaitedMessageMessageType0ExtractedCodesItemKind(StrEnum):
    ALPHANUMERIC = "alphanumeric"
    NUMERIC = "numeric"

    def __str__(self) -> str:
        return str(self.value)
