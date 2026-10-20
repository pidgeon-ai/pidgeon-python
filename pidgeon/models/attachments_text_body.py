from enum import StrEnum


class AttachmentsTextBody(StrEnum):
    CLEAN = "clean"
    ORIGINAL = "original"

    def __str__(self) -> str:
        return str(self.value)
