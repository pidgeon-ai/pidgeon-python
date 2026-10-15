from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define

from ..models.event_response_event_duration_mode import EventResponseEventDurationMode
from ..models.event_response_event_kind import EventResponseEventKind
from ..models.event_response_event_source import EventResponseEventSource
from ..models.event_response_event_status import EventResponseEventStatus

if TYPE_CHECKING:
    from ..models.event_response_event_attendees_item import EventResponseEventAttendeesItem
    from ..models.event_response_event_recurrence_type_0 import EventResponseEventRecurrenceType0


T = TypeVar("T", bound="EventResponseEvent")


@_attrs_define
class EventResponseEvent:
    """
    Attributes:
        id (str):
        identity_id (str):
        kind (EventResponseEventKind):
        series_id (None | str):
        original_start (None | str):
        source (EventResponseEventSource):
        uid (str):
        sequence (float):
        status (EventResponseEventStatus):
        title (str):
        description (None | str):
        location (None | str):
        metadata (Any):
        all_day (bool):
        start (str): Local wall time in `timezone`. This is the truth.
        end (str): For an all-day event, the last day, inclusive.
        timezone (str):
        starts_at (str): The same moment as an instant, derived from `start`.
        ends_at (str): ISO-8601, UTC.
        duration_mode (EventResponseEventDurationMode):
        duration_value (float):
        recurrence (EventResponseEventRecurrenceType0 | None):
        attendees (list[EventResponseEventAttendeesItem]):
        attendee_count (float):
        organizer_email (None | str):
        origin_message_id (None | str):
        etag (str): Send it back in `If-Match` to make a write conditional.
        created_at (str): ISO-8601, UTC.
        updated_at (str): ISO-8601, UTC.
    """

    id: str
    identity_id: str
    kind: EventResponseEventKind
    series_id: None | str
    original_start: None | str
    source: EventResponseEventSource
    uid: str
    sequence: float
    status: EventResponseEventStatus
    title: str
    description: None | str
    location: None | str
    metadata: Any
    all_day: bool
    start: str
    end: str
    timezone: str
    starts_at: str
    ends_at: str
    duration_mode: EventResponseEventDurationMode
    duration_value: float
    recurrence: EventResponseEventRecurrenceType0 | None
    attendees: list[EventResponseEventAttendeesItem]
    attendee_count: float
    organizer_email: None | str
    origin_message_id: None | str
    etag: str
    created_at: str
    updated_at: str

    def to_dict(self) -> dict[str, Any]:
        from ..models.event_response_event_recurrence_type_0 import EventResponseEventRecurrenceType0  # noqa: PLC0415

        id = self.id

        identity_id = self.identity_id

        kind = self.kind.value

        series_id: None | str
        series_id = self.series_id

        original_start: None | str
        original_start = self.original_start

        source = self.source.value

        uid = self.uid

        sequence = self.sequence

        status = self.status.value

        title = self.title

        description: None | str
        description = self.description

        location: None | str
        location = self.location

        metadata = self.metadata

        all_day = self.all_day

        start = self.start

        end = self.end

        timezone = self.timezone

        starts_at = self.starts_at

        ends_at = self.ends_at

        duration_mode = self.duration_mode.value

        duration_value = self.duration_value

        recurrence: dict[str, Any] | None
        if isinstance(self.recurrence, EventResponseEventRecurrenceType0):
            recurrence = self.recurrence.to_dict()
        else:
            recurrence = self.recurrence

        attendees = []
        for attendees_item_data in self.attendees:
            attendees_item = attendees_item_data.to_dict()
            attendees.append(attendees_item)

        attendee_count = self.attendee_count

        organizer_email: None | str
        organizer_email = self.organizer_email

        origin_message_id: None | str
        origin_message_id = self.origin_message_id

        etag = self.etag

        created_at = self.created_at

        updated_at = self.updated_at

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "id": id,
                "identity_id": identity_id,
                "kind": kind,
                "series_id": series_id,
                "original_start": original_start,
                "source": source,
                "uid": uid,
                "sequence": sequence,
                "status": status,
                "title": title,
                "description": description,
                "location": location,
                "metadata": metadata,
                "all_day": all_day,
                "start": start,
                "end": end,
                "timezone": timezone,
                "starts_at": starts_at,
                "ends_at": ends_at,
                "duration_mode": duration_mode,
                "duration_value": duration_value,
                "recurrence": recurrence,
                "attendees": attendees,
                "attendee_count": attendee_count,
                "organizer_email": organizer_email,
                "origin_message_id": origin_message_id,
                "etag": etag,
                "created_at": created_at,
                "updated_at": updated_at,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.event_response_event_attendees_item import EventResponseEventAttendeesItem  # noqa: PLC0415
        from ..models.event_response_event_recurrence_type_0 import EventResponseEventRecurrenceType0  # noqa: PLC0415

        d = dict(src_dict)
        id = d.pop("id")

        identity_id = d.pop("identity_id")

        kind = EventResponseEventKind(d.pop("kind"))

        def _parse_series_id(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        series_id = _parse_series_id(d.pop("series_id"))

        def _parse_original_start(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        original_start = _parse_original_start(d.pop("original_start"))

        source = EventResponseEventSource(d.pop("source"))

        uid = d.pop("uid")

        sequence = d.pop("sequence")

        status = EventResponseEventStatus(d.pop("status"))

        title = d.pop("title")

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

        metadata = d.pop("metadata")

        all_day = d.pop("all_day")

        start = d.pop("start")

        end = d.pop("end")

        timezone = d.pop("timezone")

        starts_at = d.pop("starts_at")

        ends_at = d.pop("ends_at")

        duration_mode = EventResponseEventDurationMode(d.pop("duration_mode"))

        duration_value = d.pop("duration_value")

        def _parse_recurrence(data: object) -> EventResponseEventRecurrenceType0 | None:
            if data is None:
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                recurrence_type_0 = EventResponseEventRecurrenceType0.from_dict(data)

                return recurrence_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(EventResponseEventRecurrenceType0 | None, data)

        recurrence = _parse_recurrence(d.pop("recurrence"))

        attendees = []
        _attendees = d.pop("attendees")
        for attendees_item_data in _attendees:
            attendees_item = EventResponseEventAttendeesItem.from_dict(attendees_item_data)

            attendees.append(attendees_item)

        attendee_count = d.pop("attendee_count")

        def _parse_organizer_email(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        organizer_email = _parse_organizer_email(d.pop("organizer_email"))

        def _parse_origin_message_id(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        origin_message_id = _parse_origin_message_id(d.pop("origin_message_id"))

        etag = d.pop("etag")

        created_at = d.pop("created_at")

        updated_at = d.pop("updated_at")

        event_response_event = cls(
            id=id,
            identity_id=identity_id,
            kind=kind,
            series_id=series_id,
            original_start=original_start,
            source=source,
            uid=uid,
            sequence=sequence,
            status=status,
            title=title,
            description=description,
            location=location,
            metadata=metadata,
            all_day=all_day,
            start=start,
            end=end,
            timezone=timezone,
            starts_at=starts_at,
            ends_at=ends_at,
            duration_mode=duration_mode,
            duration_value=duration_value,
            recurrence=recurrence,
            attendees=attendees,
            attendee_count=attendee_count,
            organizer_email=organizer_email,
            origin_message_id=origin_message_id,
            etag=etag,
            created_at=created_at,
            updated_at=updated_at,
        )

        return event_response_event
