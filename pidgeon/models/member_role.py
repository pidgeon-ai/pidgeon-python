from enum import StrEnum


class MemberRole(StrEnum):
    MEMBER = "member"
    OWNER = "owner"

    def __str__(self) -> str:
        return str(self.value)
