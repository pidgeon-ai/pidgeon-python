from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.calendar_update_event_body_attendees_item_status import CalendarUpdateEventBodyAttendeesItemStatus
from ..types import UNSET, Unset

T = TypeVar("T", bound="CalendarUpdateEventBodyAttendeesItem")


@_attrs_define
class CalendarUpdateEventBodyAttendeesItem:
    """
    Attributes:
        email (str):
        name (None | str | Unset):
        status (CalendarUpdateEventBodyAttendeesItemStatus | Unset):  Default:
            CalendarUpdateEventBodyAttendeesItemStatus.NEEDS_ACTION.
        optional (bool | Unset):  Default: False.
    """

    email: str
    name: None | str | Unset = UNSET
    status: CalendarUpdateEventBodyAttendeesItemStatus | Unset = CalendarUpdateEventBodyAttendeesItemStatus.NEEDS_ACTION
    optional: bool | Unset = False
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        email = self.email

        name: None | str | Unset
        if isinstance(self.name, Unset):
            name = UNSET
        else:
            name = self.name

        status: str | Unset = UNSET
        if not isinstance(self.status, Unset):
            status = self.status.value

        optional = self.optional

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "email": email,
            }
        )
        if name is not UNSET:
            field_dict["name"] = name
        if status is not UNSET:
            field_dict["status"] = status
        if optional is not UNSET:
            field_dict["optional"] = optional

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        email = d.pop("email")

        def _parse_name(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        name = _parse_name(d.pop("name", UNSET))

        _status = d.pop("status", UNSET)
        status: CalendarUpdateEventBodyAttendeesItemStatus | Unset
        if isinstance(_status, Unset):
            status = UNSET
        else:
            status = CalendarUpdateEventBodyAttendeesItemStatus(_status)

        optional = d.pop("optional", UNSET)

        calendar_update_event_body_attendees_item = cls(
            email=email,
            name=name,
            status=status,
            optional=optional,
        )

        calendar_update_event_body_attendees_item.additional_properties = d
        return calendar_update_event_body_attendees_item

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
