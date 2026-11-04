from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.grant_scope_limit import GrantScopeLimit


T = TypeVar("T", bound="GrantScope")


@_attrs_define
class GrantScope:
    """
    Attributes:
        name (str): Stable, for software: `bookings.change`.
        label (str): For people: "manage your bookings".
        limit (GrantScopeLimit | Unset):
    """

    name: str
    label: str
    limit: GrantScopeLimit | Unset = UNSET

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
        from ..models.grant_scope_limit import GrantScopeLimit  # noqa: PLC0415

        d = dict(src_dict)
        name = d.pop("name")

        label = d.pop("label")

        _limit = d.pop("limit", UNSET)
        limit: GrantScopeLimit | Unset
        if isinstance(_limit, Unset):
            limit = UNSET
        else:
            limit = GrantScopeLimit.from_dict(_limit)

        grant_scope = cls(
            name=name,
            label=label,
            limit=limit,
        )

        return grant_scope
