from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define

from ..types import UNSET, Unset

T = TypeVar("T", bound="Undo")


@_attrs_define
class Undo:
    """
    Attributes:
        undo (list[Any]):
        id (str | Unset):
        applied (int | Unset):
    """

    undo: list[Any]
    id: str | Unset = UNSET
    applied: int | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        undo = self.undo

        id = self.id

        applied = self.applied

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "undo": undo,
            }
        )
        if id is not UNSET:
            field_dict["id"] = id
        if applied is not UNSET:
            field_dict["applied"] = applied

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        undo = cast(list[Any], d.pop("undo"))

        id = d.pop("id", UNSET)

        applied = d.pop("applied", UNSET)

        undo = cls(
            undo=undo,
            id=id,
            applied=applied,
        )

        return undo
