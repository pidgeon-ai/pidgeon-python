from enum import StrEnum


class IdentitiesReceiveRulesCreateBodyAction(StrEnum):
    ARCHIVE = "archive"
    INBOX = "inbox"
    REJECT = "reject"
    SPAM = "spam"
    TRASH = "trash"

    def __str__(self) -> str:
        return str(self.value)
