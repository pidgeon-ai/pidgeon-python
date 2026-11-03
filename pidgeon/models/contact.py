from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define

from ..models.contact_blocked_type_0 import ContactBlockedType0
from ..models.contact_kind import ContactKind

T = TypeVar("T", bound="Contact")


@_attrs_define
class Contact:
    """
    Attributes:
        id (str):
        identity_id (str): The address this is a contact of.
        inbox (str): That address, as an email.
        email (str):
        name (None | str):
        avatar_url (None | str):
        kind (ContactKind):
        notes (None | str):
        snoozed_until (None | str): While muted: until when their new mail arrives snoozed. Null otherwise.
        blocked (ContactBlockedType0 | None): Null when their mail reaches the inbox. `contact`: blocked here, and
            unblocking undoes it. `rule`: a wider rule on the domain or the workspace blocks them.
        last_seen_at (None | str): The last mail between them and this address.
        created_at (str): ISO-8601, UTC.
    """

    id: str
    identity_id: str
    inbox: str
    email: str
    name: None | str
    avatar_url: None | str
    kind: ContactKind
    notes: None | str
    snoozed_until: None | str
    blocked: ContactBlockedType0 | None
    last_seen_at: None | str
    created_at: str

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        identity_id = self.identity_id

        inbox = self.inbox

        email = self.email

        name: None | str
        name = self.name

        avatar_url: None | str
        avatar_url = self.avatar_url

        kind = self.kind.value

        notes: None | str
        notes = self.notes

        snoozed_until: None | str
        snoozed_until = self.snoozed_until

        blocked: None | str
        if isinstance(self.blocked, ContactBlockedType0):
            blocked = self.blocked.value
        else:
            blocked = self.blocked

        last_seen_at: None | str
        last_seen_at = self.last_seen_at

        created_at = self.created_at

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "id": id,
                "identity_id": identity_id,
                "inbox": inbox,
                "email": email,
                "name": name,
                "avatar_url": avatar_url,
                "kind": kind,
                "notes": notes,
                "snoozed_until": snoozed_until,
                "blocked": blocked,
                "last_seen_at": last_seen_at,
                "created_at": created_at,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        id = d.pop("id")

        identity_id = d.pop("identity_id")

        inbox = d.pop("inbox")

        email = d.pop("email")

        def _parse_name(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        name = _parse_name(d.pop("name"))

        def _parse_avatar_url(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        avatar_url = _parse_avatar_url(d.pop("avatar_url"))

        kind = ContactKind(d.pop("kind"))

        def _parse_notes(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        notes = _parse_notes(d.pop("notes"))

        def _parse_snoozed_until(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        snoozed_until = _parse_snoozed_until(d.pop("snoozed_until"))

        def _parse_blocked(data: object) -> ContactBlockedType0 | None:
            if data is None:
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                blocked_type_0 = ContactBlockedType0(data)

                return blocked_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(ContactBlockedType0 | None, data)

        blocked = _parse_blocked(d.pop("blocked"))

        def _parse_last_seen_at(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        last_seen_at = _parse_last_seen_at(d.pop("last_seen_at"))

        created_at = d.pop("created_at")

        contact = cls(
            id=id,
            identity_id=identity_id,
            inbox=inbox,
            email=email,
            name=name,
            avatar_url=avatar_url,
            kind=kind,
            notes=notes,
            snoozed_until=snoozed_until,
            blocked=blocked,
            last_seen_at=last_seen_at,
            created_at=created_at,
        )

        return contact
