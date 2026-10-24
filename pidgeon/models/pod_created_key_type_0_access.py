from enum import StrEnum


class PodCreatedKeyType0Access(StrEnum):
    ADMIN = "admin"
    READ = "read"
    SEND = "send"

    def __str__(self) -> str:
        return str(self.value)
