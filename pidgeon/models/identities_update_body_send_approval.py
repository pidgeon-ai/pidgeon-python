from enum import StrEnum


class IdentitiesUpdateBodySendApproval(StrEnum):
    FIRST_CONTACT = "first_contact"
    NONE = "none"

    def __str__(self) -> str:
        return str(self.value)
