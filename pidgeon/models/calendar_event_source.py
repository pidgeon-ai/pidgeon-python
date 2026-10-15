from enum import StrEnum


class CalendarEventSource(StrEnum):
    API = "api"
    EMAIL = "email"

    def __str__(self) -> str:
        return str(self.value)
