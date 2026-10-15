from enum import StrEnum


class EventResponseEventSource(StrEnum):
    API = "api"
    EMAIL = "email"

    def __str__(self) -> str:
        return str(self.value)
