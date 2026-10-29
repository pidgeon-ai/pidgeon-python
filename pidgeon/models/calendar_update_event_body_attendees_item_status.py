from enum import StrEnum


class CalendarUpdateEventBodyAttendeesItemStatus(StrEnum):
    ACCEPTED = "accepted"
    DECLINED = "declined"
    NEEDS_ACTION = "needs_action"
    TENTATIVE = "tentative"

    @classmethod
    def _missing_(cls, value: object) -> "CalendarUpdateEventBodyAttendeesItemStatus | None":
        # A value the API added after this client was published (a new
        # Firewall signal kind, say) is kept as itself rather than raising:
        # an additive change to the API must not break a published client.
        # `docs/email.md` → Pidgeon Firewall, firewall.md §6.
        if not isinstance(value, str):
            return None
        member = str.__new__(cls, value)
        member._name_ = value.upper()
        member._value_ = value
        return member

    def __str__(self) -> str:
        return str(self.value)
