from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar
from uuid import UUID

from attrs import define as _attrs_define

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.undo_undo_item_rows_item import UndoUndoItemRowsItem


T = TypeVar("T", bound="UndoUndoItem")


@_attrs_define
class UndoUndoItem:
    """
    Attributes:
        message_id (UUID):
        rows (list[UndoUndoItemRowsItem]):
        read (list[UUID] | Unset):
    """

    message_id: UUID
    rows: list[UndoUndoItemRowsItem]
    read: list[UUID] | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        message_id = str(self.message_id)

        rows = []
        for rows_item_data in self.rows:
            rows_item = rows_item_data.to_dict()
            rows.append(rows_item)

        read: list[str] | Unset = UNSET
        if not isinstance(self.read, Unset):
            read = []
            for read_item_data in self.read:
                read_item = str(read_item_data)
                read.append(read_item)

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "messageId": message_id,
                "rows": rows,
            }
        )
        if read is not UNSET:
            field_dict["read"] = read

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.undo_undo_item_rows_item import UndoUndoItemRowsItem  # noqa: PLC0415

        d = dict(src_dict)
        message_id = UUID(d.pop("messageId"))

        rows = []
        _rows = d.pop("rows")
        for rows_item_data in _rows:
            rows_item = UndoUndoItemRowsItem.from_dict(rows_item_data)

            rows.append(rows_item)

        _read = d.pop("read", UNSET)
        read: list[UUID] | Unset = UNSET
        if _read is not UNSET:
            read = []
            for read_item_data in _read:
                read_item = UUID(read_item_data)

                read.append(read_item)

        undo_undo_item = cls(
            message_id=message_id,
            rows=rows,
            read=read,
        )

        return undo_undo_item
