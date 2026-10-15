from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define

if TYPE_CHECKING:
    from ..models.event_response_event import EventResponseEvent


T = TypeVar("T", bound="EventResponse")


@_attrs_define
class EventResponse:
    """
    Attributes:
        event (EventResponseEvent):
        attendee (str): Which of the mailbox’s addresses answered.
        status (str):
        reply_sent (bool): Whether an iCalendar REPLY actually went to an organiser. False when the meeting has none to
            tell, when `send_reply` was false, and when this answer had already gone out.
    """

    event: EventResponseEvent
    attendee: str
    status: str
    reply_sent: bool

    def to_dict(self) -> dict[str, Any]:
        event = self.event.to_dict()

        attendee = self.attendee

        status = self.status

        reply_sent = self.reply_sent

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "event": event,
                "attendee": attendee,
                "status": status,
                "reply_sent": reply_sent,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.event_response_event import EventResponseEvent  # noqa: PLC0415

        d = dict(src_dict)
        event = EventResponseEvent.from_dict(d.pop("event"))

        attendee = d.pop("attendee")

        status = d.pop("status")

        reply_sent = d.pop("reply_sent")

        event_response = cls(
            event=event,
            attendee=attendee,
            status=status,
            reply_sent=reply_sent,
        )

        return event_response
