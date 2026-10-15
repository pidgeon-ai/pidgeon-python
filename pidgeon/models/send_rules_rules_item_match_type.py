from enum import StrEnum


class SendRulesRulesItemMatchType(StrEnum):
    ADDRESS = "address"
    DOMAIN = "domain"

    def __str__(self) -> str:
        return str(self.value)
