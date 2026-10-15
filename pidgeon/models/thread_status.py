from enum import StrEnum


class ThreadStatus(StrEnum):
    HUMAN_REVIEW = "human_review"
    OPEN = "open"
    RESOLVED = "resolved"
    WAITING = "waiting"

    def __str__(self) -> str:
        return str(self.value)
