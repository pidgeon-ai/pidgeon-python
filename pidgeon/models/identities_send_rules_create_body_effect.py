from enum import StrEnum


class IdentitiesSendRulesCreateBodyEffect(StrEnum):
    ALLOW = "allow"
    BLOCK = "block"

    def __str__(self) -> str:
        return str(self.value)
