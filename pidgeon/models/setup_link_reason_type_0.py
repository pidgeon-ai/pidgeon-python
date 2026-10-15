from enum import StrEnum


class SetupLinkReasonType0(StrEnum):
    PROVIDER = "provider"
    UNCONFIGURED = "unconfigured"

    def __str__(self) -> str:
        return str(self.value)
