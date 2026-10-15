from enum import StrEnum


class DomainDetailDnsRecordsItemStatus(StrEnum):
    CONNECTED = "connected"
    INCORRECT = "incorrect"
    NOT_REQUIRED = "not_required"
    WAITING = "waiting"

    def __str__(self) -> str:
        return str(self.value)
