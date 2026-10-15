from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define

T = TypeVar("T", bound="Restored")


@_attrs_define
class Restored:
    """
    Attributes:
        restored (int):
    """

    restored: int

    def to_dict(self) -> dict[str, Any]:
        restored = self.restored

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "restored": restored,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        restored = d.pop("restored")

        restored = cls(
            restored=restored,
        )

        return restored
