from enum import StrEnum


class ApiKeyAccess(StrEnum):
    ADMIN = "admin"
    DRAFT = "draft"
    READ = "read"
    SEND = "send"

    def __str__(self) -> str:
        return str(self.value)
