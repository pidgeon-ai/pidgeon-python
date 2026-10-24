from enum import StrEnum


class DnsRecordStateType0(StrEnum):
    CONNECTED = "connected"
    MISSING = "missing"
    NOT_REQUIRED = "not_required"
    PUBLISHED = "published"
    WRONG_NAME = "wrong_name"
    WRONG_VALUE = "wrong_value"

    def __str__(self) -> str:
        return str(self.value)
