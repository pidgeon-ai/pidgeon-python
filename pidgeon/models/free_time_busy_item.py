from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define

T = TypeVar("T", bound="FreeTimeBusyItem")


@_attrs_define
class FreeTimeBusyItem:
    """
    Attributes:
        identity_id (str):
        start (str): ISO-8601, UTC.
        end (str): ISO-8601, UTC.
    """

    identity_id: str
    start: str
    end: str

    def to_dict(self) -> dict[str, Any]:
        identity_id = self.identity_id

        start = self.start

        end = self.end

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "identity_id": identity_id,
                "start": start,
                "end": end,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        identity_id = d.pop("identity_id")

        start = d.pop("start")

        end = d.pop("end")

        free_time_busy_item = cls(
            identity_id=identity_id,
            start=start,
            end=end,
        )

        return free_time_busy_item
