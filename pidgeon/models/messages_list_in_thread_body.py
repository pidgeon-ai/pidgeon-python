from enum import StrEnum


class MessagesListInThreadBody(StrEnum):
    CLEAN = "clean"
    ORIGINAL = "original"

    def __str__(self) -> str:
        return str(self.value)
