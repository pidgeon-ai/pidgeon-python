from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define

T = TypeVar("T", bound="TenantSuspended")


@_attrs_define
class TenantSuspended:
    """
    Attributes:
        tenant_id (str):
        suspended (int): How many addresses this call changed.
    """

    tenant_id: str
    suspended: int

    def to_dict(self) -> dict[str, Any]:
        tenant_id = self.tenant_id

        suspended = self.suspended

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "tenant_id": tenant_id,
                "suspended": suspended,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        tenant_id = d.pop("tenant_id")

        suspended = d.pop("suspended")

        tenant_suspended = cls(
            tenant_id=tenant_id,
            suspended=suspended,
        )

        return tenant_suspended
