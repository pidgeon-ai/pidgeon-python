from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define

T = TypeVar("T", bound="MeWorkspace")


@_attrs_define
class MeWorkspace:
    """
    Attributes:
        id (str):
        plan (str): Which entitlements apply. See /docs/limits.
    """

    id: str
    plan: str

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        plan = self.plan

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "id": id,
                "plan": plan,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        id = d.pop("id")

        plan = d.pop("plan")

        me_workspace = cls(
            id=id,
            plan=plan,
        )

        return me_workspace
