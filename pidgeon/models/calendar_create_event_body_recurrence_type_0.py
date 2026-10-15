from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="CalendarCreateEventBodyRecurrenceType0")


@_attrs_define
class CalendarCreateEventBodyRecurrenceType0:
    """
    Attributes:
        rule (str):
        exdates (list[str] | Unset):
        rdates (list[str] | Unset):
    """

    rule: str
    exdates: list[str] | Unset = UNSET
    rdates: list[str] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        rule = self.rule

        exdates: list[str] | Unset = UNSET
        if not isinstance(self.exdates, Unset):
            exdates = self.exdates

        rdates: list[str] | Unset = UNSET
        if not isinstance(self.rdates, Unset):
            rdates = self.rdates

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "rule": rule,
            }
        )
        if exdates is not UNSET:
            field_dict["exdates"] = exdates
        if rdates is not UNSET:
            field_dict["rdates"] = rdates

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        rule = d.pop("rule")

        exdates = cast(list[str], d.pop("exdates", UNSET))

        rdates = cast(list[str], d.pop("rdates", UNSET))

        calendar_create_event_body_recurrence_type_0 = cls(
            rule=rule,
            exdates=exdates,
            rdates=rdates,
        )

        calendar_create_event_body_recurrence_type_0.additional_properties = d
        return calendar_create_event_body_recurrence_type_0

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
