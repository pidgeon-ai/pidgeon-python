from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define

if TYPE_CHECKING:
    from ..models.event_data import EventData


T = TypeVar("T", bound="Event")


@_attrs_define
class Event:
    """
    Attributes:
        id (str):
        type_ (str):
        identity (None | str):
        message_id (None | str):
        thread_id (None | str):
        data (EventData):
        created_at (str): ISO-8601, UTC.
    """

    id: str
    type_: str
    identity: None | str
    message_id: None | str
    thread_id: None | str
    data: EventData
    created_at: str

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        type_ = self.type_

        identity: None | str
        identity = self.identity

        message_id: None | str
        message_id = self.message_id

        thread_id: None | str
        thread_id = self.thread_id

        data = self.data.to_dict()

        created_at = self.created_at

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "id": id,
                "type": type_,
                "identity": identity,
                "message_id": message_id,
                "thread_id": thread_id,
                "data": data,
                "created_at": created_at,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.event_data import EventData  # noqa: PLC0415

        d = dict(src_dict)
        id = d.pop("id")

        type_ = d.pop("type")

        def _parse_identity(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        identity = _parse_identity(d.pop("identity"))

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

        data = EventData.from_dict(d.pop("data"))

        created_at = d.pop("created_at")

        event = cls(
            id=id,
            type_=type_,
            identity=identity,
            message_id=message_id,
            thread_id=thread_id,
            data=data,
            created_at=created_at,
        )

        return event
