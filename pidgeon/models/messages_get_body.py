from enum import StrEnum


class MessagesGetBody(StrEnum):
    CLEAN = "clean"
    ORIGINAL = "original"

    def __str__(self) -> str:
        return str(self.value)
