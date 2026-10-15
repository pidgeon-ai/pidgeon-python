from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define

T = TypeVar("T", bound="Workspace")


@_attrs_define
class Workspace:
    """
    Attributes:
        id (str):
        name (str):
        plan (str):
        status (str):
    """

    id: str
    name: str
    plan: str
    status: str

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        name = self.name

        plan = self.plan

        status = self.status

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "id": id,
                "name": name,
                "plan": plan,
                "status": status,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        id = d.pop("id")

        name = d.pop("name")

        plan = d.pop("plan")

        status = d.pop("status")

        workspace = cls(
            id=id,
            name=name,
            plan=plan,
            status=status,
        )

        return workspace
