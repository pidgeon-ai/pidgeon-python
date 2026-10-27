from enum import StrEnum


class SentApprovalType0Reason(StrEnum):
    FIRST_CONTACT = "first_contact"
    RISKY_THREAD = "risky_thread"

    def __str__(self) -> str:
        return str(self.value)
