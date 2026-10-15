from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define

from ..types import UNSET, Unset

T = TypeVar("T", bound="MailboxChange")


@_attrs_define
class MailboxChange:
    """
    Attributes:
        id (str):
        changed_at (str): ISO-8601, UTC.
        deleted (bool):
        folder (None | str | Unset):
    """

    id: str
    changed_at: str
    deleted: bool
    folder: None | str | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        changed_at = self.changed_at

        deleted = self.deleted

        folder: None | str | Unset
        if isinstance(self.folder, Unset):
            folder = UNSET
        else:
            folder = self.folder

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "id": id,
                "changed_at": changed_at,
                "deleted": deleted,
            }
        )
        if folder is not UNSET:
            field_dict["folder"] = folder

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        id = d.pop("id")

        changed_at = d.pop("changed_at")

        deleted = d.pop("deleted")

        def _parse_folder(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        folder = _parse_folder(d.pop("folder", UNSET))

        mailbox_change = cls(
            id=id,
            changed_at=changed_at,
            deleted=deleted,
            folder=folder,
        )

        return mailbox_change
