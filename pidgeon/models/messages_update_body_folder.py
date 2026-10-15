from enum import StrEnum


class MessagesUpdateBodyFolder(StrEnum):
    ARCHIVE = "archive"
    INBOX = "inbox"
    SPAM = "spam"
    TRASH = "trash"

    def __str__(self) -> str:
        return str(self.value)
