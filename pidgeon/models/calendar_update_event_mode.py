from enum import StrEnum


class CalendarUpdateEventMode(StrEnum):
    FUTURE = "future"
    SINGLE = "single"

    def __str__(self) -> str:
        return str(self.value)
