from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define

T = TypeVar("T", bound="Pod")


@_attrs_define
class Pod:
    """
    Attributes:
        id (str):
        name (str):
        client_id (None | str): Your own id for this pod — a customer id, whatever your side calls it.
        is_default (bool): Where an address lands when a create call names no pod. Exactly one per account.
        identity_count (int): Addresses in it.
        created_at (str): ISO-8601, UTC.
    """

    id: str
    name: str
    client_id: None | str
    is_default: bool
    identity_count: int
    created_at: str

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        name = self.name

        client_id: None | str
        client_id = self.client_id

        is_default = self.is_default

        identity_count = self.identity_count

        created_at = self.created_at

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "id": id,
                "name": name,
                "client_id": client_id,
                "is_default": is_default,
                "identity_count": identity_count,
                "created_at": created_at,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        id = d.pop("id")

        name = d.pop("name")

        def _parse_client_id(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        client_id = _parse_client_id(d.pop("client_id"))

        is_default = d.pop("is_default")

        identity_count = d.pop("identity_count")

        created_at = d.pop("created_at")

        pod = cls(
            id=id,
            name=name,
            client_id=client_id,
            is_default=is_default,
            identity_count=identity_count,
            created_at=created_at,
        )

        return pod
