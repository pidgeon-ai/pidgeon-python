from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.sender_verification_grants_item_scope_type_0_limit import SenderVerificationGrantsItemScopeType0Limit


T = TypeVar("T", bound="SenderVerificationGrantsItemScopeType0")


@_attrs_define
class SenderVerificationGrantsItemScopeType0:
    """
    Attributes:
        name (str): Stable, for software: `bookings.change`.
        label (str): For people: "manage your bookings".
        limit (SenderVerificationGrantsItemScopeType0Limit | Unset):
    """

    name: str
    label: str
    limit: SenderVerificationGrantsItemScopeType0Limit | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        name = self.name

        label = self.label

        limit: dict[str, Any] | Unset = UNSET
        if not isinstance(self.limit, Unset):
            limit = self.limit.to_dict()

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "name": name,
                "label": label,
            }
        )
        if limit is not UNSET:
            field_dict["limit"] = limit

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.sender_verification_grants_item_scope_type_0_limit import (
            SenderVerificationGrantsItemScopeType0Limit,  # noqa: PLC0415
        )

        d = dict(src_dict)
        name = d.pop("name")

        label = d.pop("label")

        _limit = d.pop("limit", UNSET)
        limit: SenderVerificationGrantsItemScopeType0Limit | Unset
        if isinstance(_limit, Unset):
            limit = UNSET
        else:
            limit = SenderVerificationGrantsItemScopeType0Limit.from_dict(_limit)

        sender_verification_grants_item_scope_type_0 = cls(
            name=name,
            label=label,
            limit=limit,
        )

        return sender_verification_grants_item_scope_type_0
