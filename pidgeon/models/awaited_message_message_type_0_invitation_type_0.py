from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define

if TYPE_CHECKING:
    from ..models.awaited_message_message_type_0_invitation_type_0_attendees_item import (
        AwaitedMessageMessageType0InvitationType0AttendeesItem,
    )


T = TypeVar("T", bound="AwaitedMessageMessageType0InvitationType0")


@_attrs_define
class AwaitedMessageMessageType0InvitationType0:
    """
    Attributes:
        method (None | str):
        uid (str):
        sequence (float):
        status (None | str):
        summary (None | str):
        description (None | str):
        location (None | str):
        start (None | str): The local wall time the sender wrote. This and `timezone` are the truth.
        end (None | str):
        starts_at (None | str): The same moment as a UTC instant.
        ends_at (None | str):
        all_day (bool):
        timezone (None | str):
        organizer_email (None | str):
        organizer_name (None | str):
        attendees (list[AwaitedMessageMessageType0InvitationType0AttendeesItem]):
        recurrence_rule (None | str):
        is_instance (bool):
    """

    method: None | str
    uid: str
    sequence: float
    status: None | str
    summary: None | str
    description: None | str
    location: None | str
    start: None | str
    end: None | str
    starts_at: None | str
    ends_at: None | str
    all_day: bool
    timezone: None | str
    organizer_email: None | str
    organizer_name: None | str
    attendees: list[AwaitedMessageMessageType0InvitationType0AttendeesItem]
    recurrence_rule: None | str
    is_instance: bool

    def to_dict(self) -> dict[str, Any]:
        method: None | str
        method = self.method

        uid = self.uid

        sequence = self.sequence

        status: None | str
        status = self.status

        summary: None | str
        summary = self.summary

        description: None | str
        description = self.description

        location: None | str
        location = self.location

        start: None | str
        start = self.start

        end: None | str
        end = self.end

        starts_at: None | str
        starts_at = self.starts_at

        ends_at: None | str
        ends_at = self.ends_at

        all_day = self.all_day

        timezone: None | str
        timezone = self.timezone

        organizer_email: None | str
        organizer_email = self.organizer_email

        organizer_name: None | str
        organizer_name = self.organizer_name

        attendees = []
        for attendees_item_data in self.attendees:
            attendees_item = attendees_item_data.to_dict()
            attendees.append(attendees_item)

        recurrence_rule: None | str
        recurrence_rule = self.recurrence_rule

        is_instance = self.is_instance

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "method": method,
                "uid": uid,
                "sequence": sequence,
                "status": status,
                "summary": summary,
                "description": description,
                "location": location,
                "start": start,
                "end": end,
                "starts_at": starts_at,
                "ends_at": ends_at,
                "all_day": all_day,
                "timezone": timezone,
                "organizer_email": organizer_email,
                "organizer_name": organizer_name,
                "attendees": attendees,
                "recurrence_rule": recurrence_rule,
                "is_instance": is_instance,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.awaited_message_message_type_0_invitation_type_0_attendees_item import (
            AwaitedMessageMessageType0InvitationType0AttendeesItem,  # noqa: PLC0415
        )

        d = dict(src_dict)

        def _parse_method(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        method = _parse_method(d.pop("method"))

        uid = d.pop("uid")

        sequence = d.pop("sequence")

        def _parse_status(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        status = _parse_status(d.pop("status"))

        def _parse_summary(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        summary = _parse_summary(d.pop("summary"))

        def _parse_description(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        description = _parse_description(d.pop("description"))

        def _parse_location(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        location = _parse_location(d.pop("location"))

        def _parse_start(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        start = _parse_start(d.pop("start"))

        def _parse_end(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        end = _parse_end(d.pop("end"))

        def _parse_starts_at(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        starts_at = _parse_starts_at(d.pop("starts_at"))

        def _parse_ends_at(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        ends_at = _parse_ends_at(d.pop("ends_at"))

        all_day = d.pop("all_day")

        def _parse_timezone(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        timezone = _parse_timezone(d.pop("timezone"))

        def _parse_organizer_email(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        organizer_email = _parse_organizer_email(d.pop("organizer_email"))

        def _parse_organizer_name(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        organizer_name = _parse_organizer_name(d.pop("organizer_name"))

        attendees = []
        _attendees = d.pop("attendees")
        for attendees_item_data in _attendees:
            attendees_item = AwaitedMessageMessageType0InvitationType0AttendeesItem.from_dict(attendees_item_data)

            attendees.append(attendees_item)

        def _parse_recurrence_rule(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        recurrence_rule = _parse_recurrence_rule(d.pop("recurrence_rule"))

        is_instance = d.pop("is_instance")

        awaited_message_message_type_0_invitation_type_0 = cls(
            method=method,
            uid=uid,
            sequence=sequence,
            status=status,
            summary=summary,
            description=description,
            location=location,
            start=start,
            end=end,
            starts_at=starts_at,
            ends_at=ends_at,
            all_day=all_day,
            timezone=timezone,
            organizer_email=organizer_email,
            organizer_name=organizer_name,
            attendees=attendees,
            recurrence_rule=recurrence_rule,
            is_instance=is_instance,
        )

        return awaited_message_message_type_0_invitation_type_0
