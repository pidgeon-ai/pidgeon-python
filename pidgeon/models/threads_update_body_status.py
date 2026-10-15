from enum import StrEnum


class ThreadsUpdateBodyStatus(StrEnum):
    HUMAN_REVIEW = "human_review"
    OPEN = "open"
    RESOLVED = "resolved"
    WAITING = "waiting"

    def __str__(self) -> str:
        return str(self.value)
