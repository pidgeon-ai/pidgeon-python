from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define

from ..models.labels_update_body_colour import LabelsUpdateBodyColour
from ..types import UNSET, Unset

T = TypeVar("T", bound="LabelsUpdateBody")


@_attrs_define
class LabelsUpdateBody:
    """
    Attributes:
        name (str | Unset):
        colour (LabelsUpdateBodyColour | Unset):
    """

    name: str | Unset = UNSET
    colour: LabelsUpdateBodyColour | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        name = self.name

        colour: str | Unset = UNSET
        if not isinstance(self.colour, Unset):
            colour = self.colour.value

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

        _colour = d.pop("colour", UNSET)
        colour: LabelsUpdateBodyColour | Unset
        if isinstance(_colour, Unset):
            colour = UNSET
        else:
            colour = LabelsUpdateBodyColour(_colour)

        labels_update_body = cls(
            name=name,
            colour=colour,
        )

        return labels_update_body
