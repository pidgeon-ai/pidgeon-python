from enum import StrEnum


class CalendarEventDurationMode(StrEnum):
    EXACT = "exact"
    NOMINAL = "nominal"

    def __str__(self) -> str:
        return str(self.value)
