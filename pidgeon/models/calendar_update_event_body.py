from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.calendar_update_event_body_status import CalendarUpdateEventBodyStatus
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.calendar_update_event_body_attendees_item import CalendarUpdateEventBodyAttendeesItem
    from ..models.calendar_update_event_body_recurrence_type_0 import CalendarUpdateEventBodyRecurrenceType0


T = TypeVar("T", bound="CalendarUpdateEventBody")


@_attrs_define
class CalendarUpdateEventBody:
    """
    Attributes:
        title (str | Unset):
        start (str | Unset):
        end (str | Unset):
        timezone (str | Unset): An IANA name, like `Europe/Lisbon`. The times above are read in it.
        all_day (bool | Unset):
        description (None | str | Unset):
        location (None | str | Unset):
        status (CalendarUpdateEventBodyStatus | Unset):
        metadata (Any | Unset):
        attendees (list[CalendarUpdateEventBodyAttendeesItem] | Unset):
        recurrence (CalendarUpdateEventBodyRecurrenceType0 | None | Unset):
        send_invites (bool | Unset):
    """

    title: str | Unset = UNSET
    start: str | Unset = UNSET
    end: str | Unset = UNSET
    timezone: str | Unset = UNSET
    all_day: bool | Unset = UNSET
    description: None | str | Unset = UNSET
    location: None | str | Unset = UNSET
    status: CalendarUpdateEventBodyStatus | Unset = UNSET
    metadata: Any | Unset = UNSET
    attendees: list[CalendarUpdateEventBodyAttendeesItem] | Unset = UNSET
    recurrence: CalendarUpdateEventBodyRecurrenceType0 | None | Unset = UNSET
    send_invites: bool | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.calendar_update_event_body_recurrence_type_0 import CalendarUpdateEventBodyRecurrenceType0  # noqa: PLC0415

        title = self.title

        start = self.start

        end = self.end

        timezone = self.timezone

        all_day = self.all_day

        description: None | str | Unset
        if isinstance(self.description, Unset):
            description = UNSET
        else:
            description = self.description

        location: None | str | Unset
        if isinstance(self.location, Unset):
            location = UNSET
        else:
            location = self.location

        status: str | Unset = UNSET
        if not isinstance(self.status, Unset):
            status = self.status.value

        metadata = self.metadata

        attendees: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.attendees, Unset):
            attendees = []
            for attendees_item_data in self.attendees:
                attendees_item = attendees_item_data.to_dict()
                attendees.append(attendees_item)

        recurrence: dict[str, Any] | None | Unset
        if isinstance(self.recurrence, Unset):
            recurrence = UNSET
        elif isinstance(self.recurrence, CalendarUpdateEventBodyRecurrenceType0):
            recurrence = self.recurrence.to_dict()
        else:
            recurrence = self.recurrence

        send_invites = self.send_invites

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if title is not UNSET:
            field_dict["title"] = title
        if start is not UNSET:
            field_dict["start"] = start
        if end is not UNSET:
            field_dict["end"] = end
        if timezone is not UNSET:
            field_dict["timezone"] = timezone
        if all_day is not UNSET:
            field_dict["all_day"] = all_day
        if description is not UNSET:
            field_dict["description"] = description
        if location is not UNSET:
            field_dict["location"] = location
        if status is not UNSET:
            field_dict["status"] = status
        if metadata is not UNSET:
            field_dict["metadata"] = metadata
        if attendees is not UNSET:
            field_dict["attendees"] = attendees
        if recurrence is not UNSET:
            field_dict["recurrence"] = recurrence
        if send_invites is not UNSET:
            field_dict["send_invites"] = send_invites

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.calendar_update_event_body_attendees_item import CalendarUpdateEventBodyAttendeesItem  # noqa: PLC0415
        from ..models.calendar_update_event_body_recurrence_type_0 import CalendarUpdateEventBodyRecurrenceType0  # noqa: PLC0415

        d = dict(src_dict)
        title = d.pop("title", UNSET)

        start = d.pop("start", UNSET)

        end = d.pop("end", UNSET)

        timezone = d.pop("timezone", UNSET)

        all_day = d.pop("all_day", UNSET)

        def _parse_description(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        description = _parse_description(d.pop("description", UNSET))

        def _parse_location(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        location = _parse_location(d.pop("location", UNSET))

        _status = d.pop("status", UNSET)
        status: CalendarUpdateEventBodyStatus | Unset
        if isinstance(_status, Unset):
            status = UNSET
        else:
            status = CalendarUpdateEventBodyStatus(_status)

        metadata = d.pop("metadata", UNSET)

        _attendees = d.pop("attendees", UNSET)
        attendees: list[CalendarUpdateEventBodyAttendeesItem] | Unset = UNSET
        if _attendees is not UNSET:
            attendees = []
            for attendees_item_data in _attendees:
                attendees_item = CalendarUpdateEventBodyAttendeesItem.from_dict(attendees_item_data)

                attendees.append(attendees_item)

        def _parse_recurrence(data: object) -> CalendarUpdateEventBodyRecurrenceType0 | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                recurrence_type_0 = CalendarUpdateEventBodyRecurrenceType0.from_dict(data)

                return recurrence_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(CalendarUpdateEventBodyRecurrenceType0 | None | Unset, data)

        recurrence = _parse_recurrence(d.pop("recurrence", UNSET))

        send_invites = d.pop("send_invites", UNSET)

        calendar_update_event_body = cls(
            title=title,
            start=start,
            end=end,
            timezone=timezone,
            all_day=all_day,
            description=description,
            location=location,
            status=status,
            metadata=metadata,
            attendees=attendees,
            recurrence=recurrence,
            send_invites=send_invites,
        )

        calendar_update_event_body.additional_properties = d
        return calendar_update_event_body

    @property
    def additional_keys(self) -> list[str]:
        return list(self.additional_properties.keys())

    def __getitem__(self, key: str) -> Any:
        return self.additional_properties[key]

    def __setitem__(self, key: str, value: Any) -> None:
        self.additional_properties[key] = value

    def __delitem__(self, key: str) -> None:
        del self.additional_properties[key]

    def __contains__(self, key: str) -> bool:
        return key in self.additional_properties
