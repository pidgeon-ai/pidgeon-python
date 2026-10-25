from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define

T = TypeVar("T", bound="AppPasswordCreated")


@_attrs_define
class AppPasswordCreated:
    """
    Attributes:
        id (str):
        name (str):
        prefix (str):
        last_used_at (None | str):
        revoked_at (None | str):
        created_at (str): ISO-8601, UTC.
        username (str): The address, as a mail client wants it.
        password (None | str): Shown once, here, and never again. Null on an `Idempotency-Key` replay (`Idempotent-
            Replay: true`): the password is never stored, so revoke it and issue another.
    """

    id: str
    name: str
    prefix: str
    last_used_at: None | str
    revoked_at: None | str
    created_at: str
    username: str
    password: None | str

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        name = self.name

        prefix = self.prefix

        last_used_at: None | str
        last_used_at = self.last_used_at

        revoked_at: None | str
        revoked_at = self.revoked_at

        created_at = self.created_at

        username = self.username

        password: None | str
        password = self.password

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "id": id,
                "name": name,
                "prefix": prefix,
                "last_used_at": last_used_at,
                "revoked_at": revoked_at,
                "created_at": created_at,
                "username": username,
                "password": password,
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

        username = d.pop("username")

        def _parse_password(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        password = _parse_password(d.pop("password"))

        app_password_created = cls(
            id=id,
            name=name,
            prefix=prefix,
            last_used_at=last_used_at,
            revoked_at=revoked_at,
            created_at=created_at,
            username=username,
            password=password,
        )

        return app_password_created
