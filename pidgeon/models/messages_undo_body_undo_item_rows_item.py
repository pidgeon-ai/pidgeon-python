from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="MessagesUndoBodyUndoItemRowsItem")


@_attrs_define
class MessagesUndoBodyUndoItemRowsItem:
    """
    Attributes:
        id (UUID):
        is_starred (bool):
        is_archived (bool):
        is_deleted (bool):
        is_spam (bool):
    """

    id: UUID
    is_starred: bool
    is_archived: bool
    is_deleted: bool
    is_spam: bool
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = str(self.id)

        is_starred = self.is_starred

        is_archived = self.is_archived

        is_deleted = self.is_deleted

        is_spam = self.is_spam

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "is_starred": is_starred,
                "is_archived": is_archived,
                "is_deleted": is_deleted,
                "is_spam": is_spam,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        id = UUID(d.pop("id"))

        is_starred = d.pop("is_starred")

        is_archived = d.pop("is_archived")

        is_deleted = d.pop("is_deleted")

        is_spam = d.pop("is_spam")

        messages_undo_body_undo_item_rows_item = cls(
            id=id,
            is_starred=is_starred,
            is_archived=is_archived,
            is_deleted=is_deleted,
            is_spam=is_spam,
        )

        messages_undo_body_undo_item_rows_item.additional_properties = d
        return messages_undo_body_undo_item_rows_item

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
