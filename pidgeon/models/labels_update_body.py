from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define

from ..types import UNSET, Unset

T = TypeVar("T", bound="LabelsUpdateBody")


@_attrs_define
class LabelsUpdateBody:
    """
    Attributes:
        name (str | Unset):
        colour (str | Unset):
    """

    name: str | Unset = UNSET
    colour: str | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        name = self.name

        colour = self.colour

        field_dict: dict[str, Any] = {}

        field_dict.update({})
        if name is not UNSET:
            field_dict["name"] = name
        if colour is not UNSET:
            field_dict["colour"] = colour

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        name = d.pop("name", UNSET)

        colour = d.pop("colour", UNSET)

        labels_update_body = cls(
            name=name,
            colour=colour,
        )

        return labels_update_body
