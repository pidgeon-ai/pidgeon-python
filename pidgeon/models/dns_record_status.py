from enum import StrEnum


class DnsRecordStatus(StrEnum):
    CONNECTED = "connected"
    INCORRECT = "incorrect"
    NOT_REQUIRED = "not_required"
    WAITING = "waiting"

    def __str__(self) -> str:
        return str(self.value)
