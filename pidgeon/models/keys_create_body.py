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
        identity_ids (list[UUID] | Unset):
        pod_id (UUID | Unset): The pod this belongs to — your account’s default when you name none. A pod is a sending
            boundary: mail from it lands on its own reputation, so one of your customers cannot damage another’s delivery.
            It does not change what an address can do, and no key is scoped to one.
        access (KeysCreateBodyAccess | Unset): What a key may do. Give an agent the narrowest one that works.
        expires_at (datetime.datetime | None | Unset): When it stops accepting mail. Expiry suspends; it never deletes,
            so the correspondence survives.
        test (bool | Unset): A test-mode key (`pgn_test_`): everything works, nothing is sent outside Pidgeon, and
            nothing counts against the plan. A test key mints only test keys.
    """

    name: str
    identity_ids: list[UUID] | Unset = UNSET
    pod_id: UUID | Unset = UNSET
    access: KeysCreateBodyAccess | Unset = UNSET
    expires_at: datetime.datetime | None | Unset = UNSET
    test: bool | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        name = self.name

        identity_ids: list[str] | Unset = UNSET
        if not isinstance(self.identity_ids, Unset):
            identity_ids = []
            for identity_ids_item_data in self.identity_ids:
                identity_ids_item = str(identity_ids_item_data)
                identity_ids.append(identity_ids_item)

        pod_id: str | Unset = UNSET
        if not isinstance(self.pod_id, Unset):
            pod_id = str(self.pod_id)

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

        test = self.test

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "name": name,
            }
        )
        if identity_ids is not UNSET:
            field_dict["identity_ids"] = identity_ids
        if pod_id is not UNSET:
            field_dict["pod_id"] = pod_id
        if access is not UNSET:
            field_dict["access"] = access
        if expires_at is not UNSET:
            field_dict["expires_at"] = expires_at
        if test is not UNSET:
            field_dict["test"] = test

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        name = d.pop("name")

        _identity_ids = d.pop("identity_ids", UNSET)
        identity_ids: list[UUID] | Unset = UNSET
        if _identity_ids is not UNSET:
            identity_ids = []
            for identity_ids_item_data in _identity_ids:
                identity_ids_item = UUID(identity_ids_item_data)

                identity_ids.append(identity_ids_item)

        _pod_id = d.pop("pod_id", UNSET)
        pod_id: UUID | Unset
        if isinstance(_pod_id, Unset):
            pod_id = UNSET
        else:
            pod_id = UUID(_pod_id)

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

        test = d.pop("test", UNSET)

        keys_create_body = cls(
            name=name,
            identity_ids=identity_ids,
            pod_id=pod_id,
            access=access,
            expires_at=expires_at,
            test=test,
        )

        return keys_create_body
