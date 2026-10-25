from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define

if TYPE_CHECKING:
    from ..models.messages_undo_body_undo_item import MessagesUndoBodyUndoItem


T = TypeVar("T", bound="MessagesUndoBody")


@_attrs_define
class MessagesUndoBody:
    """
    Attributes:
        undo (list[MessagesUndoBodyUndoItem]):
    """

    undo: list[MessagesUndoBodyUndoItem]

    def to_dict(self) -> dict[str, Any]:
        undo = []
        for undo_item_data in self.undo:
            undo_item = undo_item_data.to_dict()
            undo.append(undo_item)

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "undo": undo,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.messages_undo_body_undo_item import MessagesUndoBodyUndoItem  # noqa: PLC0415

        d = dict(src_dict)
        undo = []
        _undo = d.pop("undo")
        for undo_item_data in _undo:
            undo_item = MessagesUndoBodyUndoItem.from_dict(undo_item_data)

            undo.append(undo_item)

        messages_undo_body = cls(
            undo=undo,
        )

        return messages_undo_body
