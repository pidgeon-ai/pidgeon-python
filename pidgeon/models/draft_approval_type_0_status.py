from enum import StrEnum


class DraftApprovalType0Status(StrEnum):
    APPROVED = "approved"
    EXPIRED = "expired"
    PENDING = "pending"
    REJECTED = "rejected"

    def __str__(self) -> str:
        return str(self.value)
