from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar
from uuid import UUID

from attrs import define as _attrs_define

T = TypeVar("T", bound="AppPasswordsCreateBody")


@_attrs_define
class AppPasswordsCreateBody:
    """
    Attributes:
        identity_id (UUID): The address this belongs to.
        name (str):
    """

    identity_id: UUID
    name: str

    def to_dict(self) -> dict[str, Any]:
        identity_id = str(self.identity_id)

        name = self.name

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "identity_id": identity_id,
                "name": name,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        identity_id = UUID(d.pop("identity_id"))

        name = d.pop("name")

        app_passwords_create_body = cls(
            identity_id=identity_id,
            name=name,
        )

        return app_passwords_create_body
