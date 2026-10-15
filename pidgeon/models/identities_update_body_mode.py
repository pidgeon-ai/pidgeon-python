from enum import StrEnum


class IdentitiesUpdateBodyMode(StrEnum):
    AUTOMATED = "automated"
    HUMAN = "human"
    HYBRID = "hybrid"

    def __str__(self) -> str:
        return str(self.value)
