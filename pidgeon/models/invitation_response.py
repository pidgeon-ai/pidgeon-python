from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define

T = TypeVar("T", bound="InvitationResponse")


@_attrs_define
class InvitationResponse:
    """
    Attributes:
        status (str):
        attendee (str): Which of the mailbox’s addresses answered.
        already_sent (bool): True when this answer had already gone out. Not an error — a retry.
        message_id (None | str):
        thread_id (None | str):
    """

    status: str
    attendee: str
    already_sent: bool
    message_id: None | str
    thread_id: None | str

    def to_dict(self) -> dict[str, Any]:
        status = self.status

        attendee = self.attendee

        already_sent = self.already_sent

        message_id: None | str
        message_id = self.message_id

        thread_id: None | str
        thread_id = self.thread_id

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "status": status,
                "attendee": attendee,
                "already_sent": already_sent,
                "message_id": message_id,
                "thread_id": thread_id,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        status = d.pop("status")

        attendee = d.pop("attendee")

        already_sent = d.pop("already_sent")

        def _parse_message_id(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        message_id = _parse_message_id(d.pop("message_id"))

        def _parse_thread_id(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        thread_id = _parse_thread_id(d.pop("thread_id"))

        invitation_response = cls(
            status=status,
            attendee=attendee,
            already_sent=already_sent,
            message_id=message_id,
            thread_id=thread_id,
        )

        return invitation_response
