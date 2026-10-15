from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar
from uuid import UUID

from attrs import define as _attrs_define

from ..models.identities_access_create_body_access import IdentitiesAccessCreateBodyAccess
from ..types import UNSET, Unset

T = TypeVar("T", bound="IdentitiesAccessCreateBody")


@_attrs_define
class IdentitiesAccessCreateBody:
    """
    Attributes:
        access (IdentitiesAccessCreateBodyAccess): What a key may do. Give an agent the narrowest one that works.
        user_id (UUID | Unset):
        api_key_id (UUID | Unset):
        everyone (bool | Unset):
    """

    access: IdentitiesAccessCreateBodyAccess
    user_id: UUID | Unset = UNSET
    api_key_id: UUID | Unset = UNSET
    everyone: bool | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        access = self.access.value

        user_id: str | Unset = UNSET
        if not isinstance(self.user_id, Unset):
            user_id = str(self.user_id)

        api_key_id: str | Unset = UNSET
        if not isinstance(self.api_key_id, Unset):
            api_key_id = str(self.api_key_id)

        everyone = self.everyone

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "access": access,
            }
        )
        if user_id is not UNSET:
            field_dict["user_id"] = user_id
        if api_key_id is not UNSET:
            field_dict["api_key_id"] = api_key_id
        if everyone is not UNSET:
            field_dict["everyone"] = everyone

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        access = IdentitiesAccessCreateBodyAccess(d.pop("access"))

        _user_id = d.pop("user_id", UNSET)
        user_id: UUID | Unset
        if isinstance(_user_id, Unset):
            user_id = UNSET
        else:
            user_id = UUID(_user_id)

        _api_key_id = d.pop("api_key_id", UNSET)
        api_key_id: UUID | Unset
        if isinstance(_api_key_id, Unset):
            api_key_id = UNSET
        else:
            api_key_id = UUID(_api_key_id)

        everyone = d.pop("everyone", UNSET)

        identities_access_create_body = cls(
            access=access,
            user_id=user_id,
            api_key_id=api_key_id,
            everyone=everyone,
        )

        return identities_access_create_body
