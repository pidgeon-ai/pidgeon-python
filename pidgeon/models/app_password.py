from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define

T = TypeVar("T", bound="AppPassword")


@_attrs_define
class AppPassword:
    """
    Attributes:
        id (str):
        name (str):
        prefix (str):
        last_used_at (None | str):
        revoked_at (None | str):
        created_at (str): ISO-8601, UTC.
    """

    id: str
    name: str
    prefix: str
    last_used_at: None | str
    revoked_at: None | str
    created_at: str

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        name = self.name

        prefix = self.prefix

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

        app_password = cls(
            id=id,
            name=name,
            prefix=prefix,
            last_used_at=last_used_at,
            revoked_at=revoked_at,
            created_at=created_at,
        )

        return app_password
