from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define

T = TypeVar("T", bound="Emptied")


@_attrs_define
class Emptied:
    """
    Attributes:
        folder (str):
        deleted (int):
    """

    folder: str
    deleted: int

    def to_dict(self) -> dict[str, Any]:
        folder = self.folder

        deleted = self.deleted

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "folder": folder,
                "deleted": deleted,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        folder = d.pop("folder")

        deleted = d.pop("deleted")

        emptied = cls(
            folder=folder,
            deleted=deleted,
        )

        return emptied
