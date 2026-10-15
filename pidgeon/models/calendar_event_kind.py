from enum import StrEnum


class CalendarEventKind(StrEnum):
    INSTANCE = "instance"
    SERIES = "series"
    SINGLE = "single"

    def __str__(self) -> str:
        return str(self.value)
