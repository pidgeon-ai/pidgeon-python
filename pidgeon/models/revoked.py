from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define

T = TypeVar("T", bound="Revoked")


@_attrs_define
class Revoked:
    """
    Attributes:
        identity_id (str):
        grant_id (str):
        revoked (bool):
    """

    identity_id: str
    grant_id: str
    revoked: bool

    def to_dict(self) -> dict[str, Any]:
        identity_id = self.identity_id

        grant_id = self.grant_id

        revoked = self.revoked

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "identity_id": identity_id,
                "grant_id": grant_id,
                "revoked": revoked,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        identity_id = d.pop("identity_id")

        grant_id = d.pop("grant_id")

        revoked = d.pop("revoked")

        revoked = cls(
            identity_id=identity_id,
            grant_id=grant_id,
            revoked=revoked,
        )

        return revoked
