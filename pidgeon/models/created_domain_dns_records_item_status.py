from enum import StrEnum


class CreatedDomainDnsRecordsItemStatus(StrEnum):
    CONNECTED = "connected"
    INCORRECT = "incorrect"
    NOT_REQUIRED = "not_required"
    WAITING = "waiting"

    def __str__(self) -> str:
        return str(self.value)
