from enum import StrEnum


class CalendarUpdateEventBodyStatus(StrEnum):
    CANCELLED = "cancelled"
    CONFIRMED = "confirmed"
    TENTATIVE = "tentative"

    def __str__(self) -> str:
        return str(self.value)
