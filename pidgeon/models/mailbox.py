from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define

from ..models.mailbox_folder import MailboxFolder

T = TypeVar("T", bound="Mailbox")


@_attrs_define
class Mailbox:
    """
    Attributes:
        folder (MailboxFolder):
        total (int | None): Null where the product does not count that folder. Not zero — zero is a claim.
        unread (int | None):
    """

    folder: MailboxFolder
    total: int | None
    unread: int | None

    def to_dict(self) -> dict[str, Any]:
        folder = self.folder.value

        total: int | None
        total = self.total

        unread: int | None
        unread = self.unread

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "folder": folder,
                "total": total,
                "unread": unread,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        folder = MailboxFolder(d.pop("folder"))

        def _parse_total(data: object) -> int | None:
            if data is None:
                return data
            return cast(int | None, data)

        total = _parse_total(d.pop("total"))

        def _parse_unread(data: object) -> int | None:
            if data is None:
                return data
            return cast(int | None, data)

        unread = _parse_unread(d.pop("unread"))

        mailbox = cls(
            folder=folder,
            total=total,
            unread=unread,
        )

        return mailbox
