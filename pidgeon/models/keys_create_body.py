from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import Any, TypeVar, cast
from uuid import UUID

from attrs import define as _attrs_define

from ..models.keys_create_body_access import KeysCreateBodyAccess
from ..types import UNSET, Unset

T = TypeVar("T", bound="KeysCreateBody")


@_attrs_define
class KeysCreateBody:
    """
    Attributes:
        name (str):
        identity_ids (list[UUID]):
        access (KeysCreateBodyAccess | Unset): What a key may do. Give an agent the narrowest one that works.
        expires_at (datetime.datetime | None | Unset): When it stops accepting mail. Expiry suspends; it never deletes,
            so the correspondence survives.
    """

    name: str
    identity_ids: list[UUID]
    access: KeysCreateBodyAccess | Unset = UNSET
    expires_at: datetime.datetime | None | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        name = self.name

        identity_ids = []
        for identity_ids_item_data in self.identity_ids:
            identity_ids_item = str(identity_ids_item_data)
            identity_ids.append(identity_ids_item)

        access: str | Unset = UNSET
        if not isinstance(self.access, Unset):
            access = self.access.value

        expires_at: None | str | Unset
        if isinstance(self.expires_at, Unset):
            expires_at = UNSET
        elif isinstance(self.expires_at, datetime.datetime):
            expires_at = self.expires_at.isoformat()
        else:
            expires_at = self.expires_at

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "name": name,
                "identity_ids": identity_ids,
            }
        )
        if access is not UNSET:
            field_dict["access"] = access
        if expires_at is not UNSET:
            field_dict["expires_at"] = expires_at

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        name = d.pop("name")

        identity_ids = []
        _identity_ids = d.pop("identity_ids")
        for identity_ids_item_data in _identity_ids:
            identity_ids_item = UUID(identity_ids_item_data)

            identity_ids.append(identity_ids_item)

        _access = d.pop("access", UNSET)
        access: KeysCreateBodyAccess | Unset
        if isinstance(_access, Unset):
            access = UNSET
        else:
            access = KeysCreateBodyAccess(_access)

        def _parse_expires_at(data: object) -> datetime.datetime | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                expires_at_type_0 = datetime.datetime.fromisoformat(data)

                return expires_at_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(datetime.datetime | None | Unset, data)

        expires_at = _parse_expires_at(d.pop("expires_at", UNSET))

        keys_create_body = cls(
            name=name,
            identity_ids=identity_ids,
            access=access,
            expires_at=expires_at,
        )

        return keys_create_body
