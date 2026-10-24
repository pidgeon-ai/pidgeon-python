from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define

T = TypeVar("T", bound="PodDeleted")


@_attrs_define
class PodDeleted:
    """
    Attributes:
        id (str):
        deleted (bool):
        addresses_deleted (int): Addresses deleted with the pod, each with all of its mail.
        keys_revoked (int): Keys revoked: the pod’s own, and every key those had minted.
    """

    id: str
    deleted: bool
    addresses_deleted: int
    keys_revoked: int

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        deleted = self.deleted

        addresses_deleted = self.addresses_deleted

        keys_revoked = self.keys_revoked

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "id": id,
                "deleted": deleted,
                "addresses_deleted": addresses_deleted,
                "keys_revoked": keys_revoked,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        id = d.pop("id")

        deleted = d.pop("deleted")

        addresses_deleted = d.pop("addresses_deleted")

        keys_revoked = d.pop("keys_revoked")

        pod_deleted = cls(
            id=id,
            deleted=deleted,
            addresses_deleted=addresses_deleted,
            keys_revoked=keys_revoked,
        )

        return pod_deleted
