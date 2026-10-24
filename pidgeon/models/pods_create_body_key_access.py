from enum import StrEnum


class PodsCreateBodyKeyAccess(StrEnum):
    ADMIN = "admin"
    READ = "read"
    SEND = "send"

    def __str__(self) -> str:
        return str(self.value)
