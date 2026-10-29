from enum import StrEnum


class WebhooksCreateBodyEventTypesItem(StrEnum):
    CALENDAR_EVENT_CREATED = "calendar.event.created"
    CALENDAR_EVENT_DELETED = "calendar.event.deleted"
    CALENDAR_EVENT_ENDING = "calendar.event.ending"
    CALENDAR_EVENT_RESPONDED = "calendar.event.responded"
    CALENDAR_EVENT_STARTING = "calendar.event.starting"
    CALENDAR_EVENT_UPDATED = "calendar.event.updated"
    DOMAIN_VERIFIED = "domain.verified"
    DRAFT_APPROVAL_REQUESTED = "draft.approval_requested"
    DRAFT_APPROVED = "draft.approved"
    DRAFT_EXPIRED = "draft.expired"
    DRAFT_REJECTED = "draft.rejected"
    IDENTITY_CREATED = "identity.created"
    IDENTITY_SUSPENDED = "identity.suspended"
    IDENTITY_TRANSFERRED = "identity.transferred"
    IDENTITY_UPDATED = "identity.updated"
    MESSAGE_ARCHIVED = "message.archived"
    MESSAGE_BOUNCED = "message.bounced"
    MESSAGE_COMPLAINED = "message.complained"
    MESSAGE_DELETED = "message.deleted"
    MESSAGE_DELIVERED = "message.delivered"
    MESSAGE_HANDED_OFF = "message.handed_off"
    MESSAGE_HELD = "message.held"
    MESSAGE_INVITATION = "message.invitation"
    MESSAGE_READ = "message.read"
    MESSAGE_RECEIVED = "message.received"
    MESSAGE_REJECTED = "message.rejected"
    MESSAGE_RELEASED = "message.released"
    MESSAGE_SENT = "message.sent"
    MESSAGE_SPAM = "message.spam"
    THREAD_ASSIGNED = "thread.assigned"
    THREAD_CREATED = "thread.created"
    THREAD_UNASSIGNED = "thread.unassigned"
    THREAD_UPDATED = "thread.updated"

    @classmethod
    def _missing_(cls, value: object) -> "WebhooksCreateBodyEventTypesItem | None":
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
