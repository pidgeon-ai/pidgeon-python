from enum import StrEnum


class SearchHitFolder(StrEnum):
    ARCHIVE = "archive"
    DRAFTS = "drafts"
    INBOX = "inbox"
    SCHEDULED = "scheduled"
    SENT = "sent"
    SNOOZED = "snoozed"
    SPAM = "spam"
    STARRED = "starred"
    TRASH = "trash"
    UNAUTHENTICATED = "unauthenticated"

    def __str__(self) -> str:
        return str(self.value)
