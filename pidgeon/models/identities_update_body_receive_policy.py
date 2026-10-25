from enum import StrEnum


class IdentitiesUpdateBodyReceivePolicy(StrEnum):
    LIST = "list"
    OPEN = "open"

    def __str__(self) -> str:
        return str(self.value)
