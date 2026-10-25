from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar
from uuid import UUID

from attrs import define as _attrs_define

T = TypeVar("T", bound="UndoUndoItemRowsItem")


@_attrs_define
class UndoUndoItemRowsItem:
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

    def to_dict(self) -> dict[str, Any]:
        id = str(self.id)

        is_starred = self.is_starred

        is_archived = self.is_archived

        is_deleted = self.is_deleted

        is_spam = self.is_spam

        field_dict: dict[str, Any] = {}

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

        undo_undo_item_rows_item = cls(
            id=id,
            is_starred=is_starred,
            is_archived=is_archived,
            is_deleted=is_deleted,
            is_spam=is_spam,
        )

        return undo_undo_item_rows_item
