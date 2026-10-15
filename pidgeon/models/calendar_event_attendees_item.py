from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define

T = TypeVar("T", bound="CalendarEventAttendeesItem")


@_attrs_define
class CalendarEventAttendeesItem:
    """
    Attributes:
        email (str):
        name (None | str):
        status (str):
        optional (bool):
    """

    email: str
    name: None | str
    status: str
    optional: bool

    def to_dict(self) -> dict[str, Any]:
        email = self.email

        name: None | str
        name = self.name

        status = self.status

        optional = self.optional

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "email": email,
                "name": name,
                "status": status,
                "optional": optional,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        email = d.pop("email")

        def _parse_name(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        name = _parse_name(d.pop("name"))

        status = d.pop("status")

        optional = d.pop("optional")

        calendar_event_attendees_item = cls(
            email=email,
            name=name,
            status=status,
            optional=optional,
        )

        return calendar_event_attendees_item
