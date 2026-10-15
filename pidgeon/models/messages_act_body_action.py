from enum import StrEnum


class MessagesActBodyAction(StrEnum):
    ARCHIVE = "archive"
    DELETE = "delete"
    DELETE_FOREVER = "delete_forever"
    NOT_SPAM = "not_spam"
    READ = "read"
    RESTORE = "restore"
    SPAM = "spam"
    STAR = "star"
    UNARCHIVE = "unarchive"
    UNREAD = "unread"
    UNSTAR = "unstar"

    def __str__(self) -> str:
        return str(self.value)
