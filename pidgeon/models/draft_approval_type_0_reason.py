from enum import StrEnum


class DraftApprovalType0Reason(StrEnum):
    FIRST_CONTACT = "first_contact"
    RISKY_THREAD = "risky_thread"

    def __str__(self) -> str:
        return str(self.value)
