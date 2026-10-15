from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define

from ..models.mailbox_access_entries_item_access import MailboxAccessEntriesItemAccess
from ..models.mailbox_access_entries_item_kind import MailboxAccessEntriesItemKind

T = TypeVar("T", bound="MailboxAccessEntriesItem")


@_attrs_define
class MailboxAccessEntriesItem:
    """
    Attributes:
        id (str): The grant’s own id. What `DELETE ?grant_id=` takes.
        kind (MailboxAccessEntriesItemKind):
        principal_id (None | str): The person or key. Null for `everyone`, which names nobody.
        label (str): For showing a person. A renamed key changes it; never match on it.
        access (MailboxAccessEntriesItemAccess):
    """

    id: str
    kind: MailboxAccessEntriesItemKind
    principal_id: None | str
    label: str
    access: MailboxAccessEntriesItemAccess

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        kind = self.kind.value

        principal_id: None | str
        principal_id = self.principal_id

        label = self.label

        access = self.access.value

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "id": id,
                "kind": kind,
                "principal_id": principal_id,
                "label": label,
                "access": access,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        id = d.pop("id")

        kind = MailboxAccessEntriesItemKind(d.pop("kind"))

        def _parse_principal_id(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        principal_id = _parse_principal_id(d.pop("principal_id"))

        label = d.pop("label")

        access = MailboxAccessEntriesItemAccess(d.pop("access"))

        mailbox_access_entries_item = cls(
            id=id,
            kind=kind,
            principal_id=principal_id,
            label=label,
            access=access,
        )

        return mailbox_access_entries_item
