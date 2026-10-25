from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.undo_undo_item import UndoUndoItem


T = TypeVar("T", bound="Undo")


@_attrs_define
class Undo:
    """
    Attributes:
        undo (list[UndoUndoItem]):
        id (str | Unset):
        applied (int | Unset):
    """

    undo: list[UndoUndoItem]
    id: str | Unset = UNSET
    applied: int | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        undo = []
        for undo_item_data in self.undo:
            undo_item = undo_item_data.to_dict()
            undo.append(undo_item)

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
        from ..models.undo_undo_item import UndoUndoItem  # noqa: PLC0415

        d = dict(src_dict)
        undo = []
        _undo = d.pop("undo")
        for undo_item_data in _undo:
            undo_item = UndoUndoItem.from_dict(undo_item_data)

            undo.append(undo_item)

        id = d.pop("id", UNSET)

        applied = d.pop("applied", UNSET)

        undo = cls(
            undo=undo,
            id=id,
            applied=applied,
        )

        return undo
