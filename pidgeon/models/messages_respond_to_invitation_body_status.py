from enum import StrEnum


class MessagesRespondToInvitationBodyStatus(StrEnum):
    ACCEPTED = "accepted"
    DECLINED = "declined"
    TENTATIVE = "tentative"

    def __str__(self) -> str:
        return str(self.value)
