from enum import StrEnum


class IdentitiesCreateBodyMode(StrEnum):
    AUTOMATED = "automated"
    HUMAN = "human"
    HYBRID = "hybrid"

    def __str__(self) -> str:
        return str(self.value)
