from __future__ import annotations

from collections.abc import Mapping
from typing import Any, Literal, TypeVar, cast

from attrs import define as _attrs_define

T = TypeVar("T", bound="Replayed")


@_attrs_define
class Replayed:
    """
    Attributes:
        id (str):
        status (Literal['pending']):
    """

    id: str
    status: Literal["pending"]

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        status = self.status

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "id": id,
                "status": status,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        id = d.pop("id")

        status = cast(Literal["pending"], d.pop("status"))
        if status != "pending":
            raise ValueError(f"status must match const 'pending', got '{status}'")

        replayed = cls(
            id=id,
            status=status,
        )

        return replayed
