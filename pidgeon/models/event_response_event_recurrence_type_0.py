from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define

T = TypeVar("T", bound="EventResponseEventRecurrenceType0")


@_attrs_define
class EventResponseEventRecurrenceType0:
    """
    Attributes:
        rule (str): Normalised, so it may differ from what you sent.
        exdates (list[str]):
        rdates (list[str]):
        truncate_before (None | str):
    """

    rule: str
    exdates: list[str]
    rdates: list[str]
    truncate_before: None | str

    def to_dict(self) -> dict[str, Any]:
        rule = self.rule

        exdates = self.exdates

        rdates = self.rdates

        truncate_before: None | str
        truncate_before = self.truncate_before

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "rule": rule,
                "exdates": exdates,
                "rdates": rdates,
                "truncate_before": truncate_before,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        rule = d.pop("rule")

        exdates = cast(list[str], d.pop("exdates"))

        rdates = cast(list[str], d.pop("rdates"))

        def _parse_truncate_before(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        truncate_before = _parse_truncate_before(d.pop("truncate_before"))

        event_response_event_recurrence_type_0 = cls(
            rule=rule,
            exdates=exdates,
            rdates=rdates,
            truncate_before=truncate_before,
        )

        return event_response_event_recurrence_type_0
