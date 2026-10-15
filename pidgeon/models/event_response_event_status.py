from enum import StrEnum


class EventResponseEventStatus(StrEnum):
    CANCELLED = "cancelled"
    CONFIRMED = "confirmed"
    TENTATIVE = "tentative"

    def __str__(self) -> str:
        return str(self.value)
