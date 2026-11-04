from enum import StrEnum


class SenderVerificationGrantsItemReasonType0(StrEnum):
    BAD_SIGNATURE = "bad_signature"
    EXPIRED = "expired"
    MALFORMED = "malformed"
    NOT_FOUND = "not_found"
    REVOKED = "revoked"
    SENDER_UNVERIFIED = "sender_unverified"
    UNKNOWN_ISSUER = "unknown_issuer"
    WRONG_AGENT = "wrong_agent"
    WRONG_AUDIENCE = "wrong_audience"
    WRONG_SUBJECT = "wrong_subject"

    @classmethod
    def _missing_(cls, value: object) -> "SenderVerificationGrantsItemReasonType0 | None":
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
