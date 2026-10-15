from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define

from ..models.api_key_access import ApiKeyAccess

T = TypeVar("T", bound="ApiKey")


@_attrs_define
class ApiKey:
    """
    Attributes:
        id (str):
        name (str):
        prefix (str):
        identity_ids (list[str]):
        access (ApiKeyAccess): The highest rung on any address. Composed with the grant; lower wins.
        created_by_key_id (None | str):
        last_used_at (None | str):
        revoked_at (None | str):
        created_at (str): ISO-8601, UTC.
    """

    id: str
    name: str
    prefix: str
    identity_ids: list[str]
    access: ApiKeyAccess
    created_by_key_id: None | str
    last_used_at: None | str
    revoked_at: None | str
    created_at: str

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        name = self.name

        prefix = self.prefix

        identity_ids = self.identity_ids

        access = self.access.value

        created_by_key_id: None | str
        created_by_key_id = self.created_by_key_id

        last_used_at: None | str
        last_used_at = self.last_used_at

        revoked_at: None | str
        revoked_at = self.revoked_at

        created_at = self.created_at

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "id": id,
                "name": name,
                "prefix": prefix,
                "identity_ids": identity_ids,
                "access": access,
                "created_by_key_id": created_by_key_id,
                "last_used_at": last_used_at,
                "revoked_at": revoked_at,
                "created_at": created_at,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        id = d.pop("id")

        name = d.pop("name")

        prefix = d.pop("prefix")

        identity_ids = cast(list[str], d.pop("identity_ids"))

        access = ApiKeyAccess(d.pop("access"))

        def _parse_created_by_key_id(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        created_by_key_id = _parse_created_by_key_id(d.pop("created_by_key_id"))

        def _parse_last_used_at(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        last_used_at = _parse_last_used_at(d.pop("last_used_at"))

        def _parse_revoked_at(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        revoked_at = _parse_revoked_at(d.pop("revoked_at"))

        created_at = d.pop("created_at")

        api_key = cls(
            id=id,
            name=name,
            prefix=prefix,
            identity_ids=identity_ids,
            access=access,
            created_by_key_id=created_by_key_id,
            last_used_at=last_used_at,
            revoked_at=revoked_at,
            created_at=created_at,
        )

        return api_key
