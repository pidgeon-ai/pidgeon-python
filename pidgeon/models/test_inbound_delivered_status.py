from enum import StrEnum


class TestInboundDeliveredStatus(StrEnum):
    DELIVERED = "delivered"
    DUPLICATE = "duplicate"
    FORWARDED = "forwarded"
    NO_SUCH_ADDRESS = "no_such_address"
    REJECTED = "rejected"

    def __str__(self) -> str:
        return str(self.value)
