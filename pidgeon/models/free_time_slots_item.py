from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define

T = TypeVar("T", bound="FreeTimeSlotsItem")


@_attrs_define
class FreeTimeSlotsItem:
    """
    Attributes:
        start (str): ISO-8601, UTC.
        end (str): ISO-8601, UTC.
        local_start (str): `start` as a wall time in `timezone`, no offset.
        local_end (str): `end` as a wall time in `timezone`, no offset.
    """

    start: str
    end: str
    local_start: str
    local_end: str

    def to_dict(self) -> dict[str, Any]:
        start = self.start

        end = self.end

        local_start = self.local_start

        local_end = self.local_end

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "start": start,
                "end": end,
                "local_start": local_start,
                "local_end": local_end,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        start = d.pop("start")

        end = d.pop("end")

        local_start = d.pop("local_start")

        local_end = d.pop("local_end")

        free_time_slots_item = cls(
            start=start,
            end=end,
            local_start=local_start,
            local_end=local_end,
        )

        return free_time_slots_item
