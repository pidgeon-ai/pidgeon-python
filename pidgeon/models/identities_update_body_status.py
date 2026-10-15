from enum import StrEnum


class IdentitiesUpdateBodyStatus(StrEnum):
    ACTIVE = "active"
    ARCHIVED = "archived"
    SUSPENDED = "suspended"

    def __str__(self) -> str:
        return str(self.value)
