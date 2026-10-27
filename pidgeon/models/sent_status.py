from enum import StrEnum


class SentStatus(StrEnum):
    PENDING_APPROVAL = "pending_approval"
    SENT = "sent"

    def __str__(self) -> str:
        return str(self.value)
