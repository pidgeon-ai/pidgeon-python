from enum import StrEnum


class MessagesAwaitBody(StrEnum):
    CLEAN = "clean"
    ORIGINAL = "original"

    def __str__(self) -> str:
        return str(self.value)
