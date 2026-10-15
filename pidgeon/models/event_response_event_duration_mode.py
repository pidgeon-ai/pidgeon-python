from enum import StrEnum


class EventResponseEventDurationMode(StrEnum):
    EXACT = "exact"
    NOMINAL = "nominal"

    def __str__(self) -> str:
        return str(self.value)
