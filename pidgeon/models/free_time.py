from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define

if TYPE_CHECKING:
    from ..models.free_time_busy_item import FreeTimeBusyItem
    from ..models.free_time_slots_item import FreeTimeSlotsItem


T = TypeVar("T", bound="FreeTime")


@_attrs_define
class FreeTime:
    """
    Attributes:
        timezone (str): The zone `local_start` and `local_end` are in.
        duration_minutes (int):
        slots (list[FreeTimeSlotsItem]): Every stretch at least `duration_minutes` long when all of them are free, in
            order. Whole stretches, not cut into meetings.
        busy (list[FreeTimeBusyItem]): What each address has on in the window, merged; no titles.
    """

    timezone: str
    duration_minutes: int
    slots: list[FreeTimeSlotsItem]
    busy: list[FreeTimeBusyItem]

    def to_dict(self) -> dict[str, Any]:
        timezone = self.timezone

        duration_minutes = self.duration_minutes

        slots = []
        for slots_item_data in self.slots:
            slots_item = slots_item_data.to_dict()
            slots.append(slots_item)

        busy = []
        for busy_item_data in self.busy:
            busy_item = busy_item_data.to_dict()
            busy.append(busy_item)

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "timezone": timezone,
                "duration_minutes": duration_minutes,
                "slots": slots,
                "busy": busy,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.free_time_busy_item import FreeTimeBusyItem  # noqa: PLC0415
        from ..models.free_time_slots_item import FreeTimeSlotsItem  # noqa: PLC0415

        d = dict(src_dict)
        timezone = d.pop("timezone")

        duration_minutes = d.pop("duration_minutes")

        slots = []
        _slots = d.pop("slots")
        for slots_item_data in _slots:
            slots_item = FreeTimeSlotsItem.from_dict(slots_item_data)

            slots.append(slots_item)

        busy = []
        _busy = d.pop("busy")
        for busy_item_data in _busy:
            busy_item = FreeTimeBusyItem.from_dict(busy_item_data)

            busy.append(busy_item)

        free_time = cls(
            timezone=timezone,
            duration_minutes=duration_minutes,
            slots=slots,
            busy=busy,
        )

        return free_time
