from enum import StrEnum


class MessageExtractedCodesItemKind(StrEnum):
    ALPHANUMERIC = "alphanumeric"
    NUMERIC = "numeric"

    def __str__(self) -> str:
        return str(self.value)
