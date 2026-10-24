from enum import StrEnum


class PodsCreateBodyAddressMode(StrEnum):
    AUTOMATED = "automated"
    HUMAN = "human"
    HYBRID = "hybrid"

    def __str__(self) -> str:
        return str(self.value)
