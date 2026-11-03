from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define

from ..models.contacts_update_body_kind import ContactsUpdateBodyKind
from ..types import UNSET, Unset

T = TypeVar("T", bound="ContactsUpdateBody")


@_attrs_define
class ContactsUpdateBody:
    """
    Attributes:
        email (str | Unset):
        name (None | str | Unset):
        kind (ContactsUpdateBodyKind | Unset): A person, or another agent.
        notes (None | str | Unset): Anything worth remembering about them. Up to 5,000 characters.
        snoozed_until (datetime.datetime | None | Unset): Until when their new mail arrives snoozed, ISO 8601, a year
            ahead at most. `null` unmutes.
    """

    email: str | Unset = UNSET
    name: None | str | Unset = UNSET
    kind: ContactsUpdateBodyKind | Unset = UNSET
    notes: None | str | Unset = UNSET
    snoozed_until: datetime.datetime | None | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        email = self.email

        name: None | str | Unset
        if isinstance(self.name, Unset):
            name = UNSET
        else:
            name = self.name

        kind: str | Unset = UNSET
        if not isinstance(self.kind, Unset):
            kind = self.kind.value

        notes: None | str | Unset
        if isinstance(self.notes, Unset):
            notes = UNSET
        else:
            notes = self.notes

        snoozed_until: None | str | Unset
        if isinstance(self.snoozed_until, Unset):
            snoozed_until = UNSET
        elif isinstance(self.snoozed_until, datetime.datetime):
            snoozed_until = self.snoozed_until.isoformat()
        else:
            snoozed_until = self.snoozed_until

        field_dict: dict[str, Any] = {}

        field_dict.update({})
        if email is not UNSET:
            field_dict["email"] = email
        if name is not UNSET:
            field_dict["name"] = name
        if kind is not UNSET:
            field_dict["kind"] = kind
        if notes is not UNSET:
            field_dict["notes"] = notes
        if snoozed_until is not UNSET:
            field_dict["snoozed_until"] = snoozed_until

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        email = d.pop("email", UNSET)

        def _parse_name(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        name = _parse_name(d.pop("name", UNSET))

        _kind = d.pop("kind", UNSET)
        kind: ContactsUpdateBodyKind | Unset
        if isinstance(_kind, Unset):
            kind = UNSET
        else:
            kind = ContactsUpdateBodyKind(_kind)

        def _parse_notes(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        notes = _parse_notes(d.pop("notes", UNSET))

        def _parse_snoozed_until(data: object) -> datetime.datetime | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                snoozed_until_type_0 = datetime.datetime.fromisoformat(data)

                return snoozed_until_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(datetime.datetime | None | Unset, data)

        snoozed_until = _parse_snoozed_until(d.pop("snoozed_until", UNSET))

        contacts_update_body = cls(
            email=email,
            name=name,
            kind=kind,
            notes=notes,
            snoozed_until=snoozed_until,
        )

        return contacts_update_body
