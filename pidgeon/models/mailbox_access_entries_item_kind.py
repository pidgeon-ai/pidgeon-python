from enum import StrEnum


class MailboxAccessEntriesItemKind(StrEnum):
    EVERYONE = "everyone"
    KEY = "key"
    MEMBER = "member"

    def __str__(self) -> str:
        return str(self.value)
