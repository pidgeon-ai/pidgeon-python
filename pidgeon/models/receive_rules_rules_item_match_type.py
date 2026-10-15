from enum import StrEnum


class ReceiveRulesRulesItemMatchType(StrEnum):
    ADDRESS = "address"
    DOMAIN = "domain"

    def __str__(self) -> str:
        return str(self.value)
