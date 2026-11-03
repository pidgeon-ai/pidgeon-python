from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast
from uuid import UUID

from attrs import define as _attrs_define

from ..models.contacts_create_body_kind import ContactsCreateBodyKind
from ..types import UNSET, Unset

T = TypeVar("T", bound="ContactsCreateBody")


@_attrs_define
class ContactsCreateBody:
    """
    Attributes:
        identity_id (UUID): The address whose contact this is.
        email (str):
        name (None | str | Unset):
        kind (ContactsCreateBodyKind | Unset): A person, or another agent.
        notes (None | str | Unset): Anything worth remembering about them. Up to 5,000 characters.
    """

    identity_id: UUID
    email: str
    name: None | str | Unset = UNSET
    kind: ContactsCreateBodyKind | Unset = UNSET
    notes: None | str | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        identity_id = str(self.identity_id)

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

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "identity_id": identity_id,
                "email": email,
            }
        )
        if name is not UNSET:
            field_dict["name"] = name
        if kind is not UNSET:
            field_dict["kind"] = kind
        if notes is not UNSET:
            field_dict["notes"] = notes

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        identity_id = UUID(d.pop("identity_id"))

        email = d.pop("email")

        def _parse_name(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        name = _parse_name(d.pop("name", UNSET))

        _kind = d.pop("kind", UNSET)
        kind: ContactsCreateBodyKind | Unset
        if isinstance(_kind, Unset):
            kind = UNSET
        else:
            kind = ContactsCreateBodyKind(_kind)

        def _parse_notes(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        notes = _parse_notes(d.pop("notes", UNSET))

        contacts_create_body = cls(
            identity_id=identity_id,
            email=email,
            name=name,
            kind=kind,
            notes=notes,
        )

        return contacts_create_body
