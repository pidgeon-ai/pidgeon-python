from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define

if TYPE_CHECKING:
    from ..models.mailbox_access_entries_item import MailboxAccessEntriesItem
    from ..models.mailbox_access_owner_type_0 import MailboxAccessOwnerType0


T = TypeVar("T", bound="MailboxAccess")


@_attrs_define
class MailboxAccess:
    """
    Attributes:
        identity_id (str):
        owner (MailboxAccessOwnerType0 | None): The person the address is. Null for a shared or programmable one.
        entries (list[MailboxAccessEntriesItem]):
        can_manage (bool): Whether this credential may change any of the above.
    """

    identity_id: str
    owner: MailboxAccessOwnerType0 | None
    entries: list[MailboxAccessEntriesItem]
    can_manage: bool

    def to_dict(self) -> dict[str, Any]:
        from ..models.mailbox_access_owner_type_0 import MailboxAccessOwnerType0  # noqa: PLC0415

        identity_id = self.identity_id

        owner: dict[str, Any] | None
        if isinstance(self.owner, MailboxAccessOwnerType0):
            owner = self.owner.to_dict()
        else:
            owner = self.owner

        entries = []
        for entries_item_data in self.entries:
            entries_item = entries_item_data.to_dict()
            entries.append(entries_item)

        can_manage = self.can_manage

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "identity_id": identity_id,
                "owner": owner,
                "entries": entries,
                "can_manage": can_manage,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.mailbox_access_entries_item import MailboxAccessEntriesItem  # noqa: PLC0415
        from ..models.mailbox_access_owner_type_0 import MailboxAccessOwnerType0  # noqa: PLC0415

        d = dict(src_dict)
        identity_id = d.pop("identity_id")

        def _parse_owner(data: object) -> MailboxAccessOwnerType0 | None:
            if data is None:
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                owner_type_0 = MailboxAccessOwnerType0.from_dict(data)

                return owner_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(MailboxAccessOwnerType0 | None, data)

        owner = _parse_owner(d.pop("owner"))

        entries = []
        _entries = d.pop("entries")
        for entries_item_data in _entries:
            entries_item = MailboxAccessEntriesItem.from_dict(entries_item_data)

            entries.append(entries_item)

        can_manage = d.pop("can_manage")

        mailbox_access = cls(
            identity_id=identity_id,
            owner=owner,
            entries=entries,
            can_manage=can_manage,
        )

        return mailbox_access
