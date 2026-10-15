from enum import StrEnum


class IdentitiesCreateBodySendPolicy(StrEnum):
    LIST = "list"
    OPEN = "open"
    REPLY_ONLY = "reply_only"

    def __str__(self) -> str:
        return str(self.value)
