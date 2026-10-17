from enum import StrEnum


class MetricsReputationType0Sending(StrEnum):
    ENABLED = "enabled"
    PAUSED = "paused"
    UNKNOWN = "unknown"

    def __str__(self) -> str:
        return str(self.value)
