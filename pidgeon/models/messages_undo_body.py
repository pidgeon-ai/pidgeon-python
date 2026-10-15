from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define

T = TypeVar("T", bound="MessagesUndoBody")


@_attrs_define
class MessagesUndoBody:
    """
    Attributes:
        undo (list[Any]):
    """

    undo: list[Any]

    def to_dict(self) -> dict[str, Any]:
        undo = self.undo

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "undo": undo,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        undo = cast(list[Any], d.pop("undo"))

        messages_undo_body = cls(
            undo=undo,
        )

        return messages_undo_body
