from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.messages_undo_body_undo_item_rows_item import MessagesUndoBodyUndoItemRowsItem


T = TypeVar("T", bound="MessagesUndoBodyUndoItem")


@_attrs_define
class MessagesUndoBodyUndoItem:
    """
    Attributes:
        message_id (UUID):
        rows (list[MessagesUndoBodyUndoItemRowsItem]):
        read (list[UUID] | Unset):
    """

    message_id: UUID
    rows: list[MessagesUndoBodyUndoItemRowsItem]
    read: list[UUID] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

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
        field_dict.update(self.additional_properties)
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
        from ..models.messages_undo_body_undo_item_rows_item import MessagesUndoBodyUndoItemRowsItem  # noqa: PLC0415

        d = dict(src_dict)
        message_id = UUID(d.pop("messageId"))

        rows = []
        _rows = d.pop("rows")
        for rows_item_data in _rows:
            rows_item = MessagesUndoBodyUndoItemRowsItem.from_dict(rows_item_data)

            rows.append(rows_item)

        _read = d.pop("read", UNSET)
        read: list[UUID] | Unset = UNSET
        if _read is not UNSET:
            read = []
            for read_item_data in _read:
                read_item = UUID(read_item_data)

                read.append(read_item)

        messages_undo_body_undo_item = cls(
            message_id=message_id,
            rows=rows,
            read=read,
        )

        messages_undo_body_undo_item.additional_properties = d
        return messages_undo_body_undo_item

    @property
    def additional_keys(self) -> list[str]:
        return list(self.additional_properties.keys())

    def __getitem__(self, key: str) -> Any:
        return self.additional_properties[key]

    def __setitem__(self, key: str, value: Any) -> None:
        self.additional_properties[key] = value

    def __delitem__(self, key: str) -> None:
        del self.additional_properties[key]

    def __contains__(self, key: str) -> bool:
        return key in self.additional_properties
