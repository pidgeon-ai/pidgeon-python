from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar
from uuid import UUID

from attrs import define as _attrs_define

from ..models.labels_create_body_colour import LabelsCreateBodyColour
from ..types import UNSET, Unset

T = TypeVar("T", bound="LabelsCreateBody")


@_attrs_define
class LabelsCreateBody:
    """
    Attributes:
        identity_id (UUID): The address this belongs to.
        name (str):
        colour (LabelsCreateBodyColour | Unset):
    """

    identity_id: UUID
    name: str
    colour: LabelsCreateBodyColour | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        identity_id = str(self.identity_id)

        name = self.name

        colour: str | Unset = UNSET
        if not isinstance(self.colour, Unset):
            colour = self.colour.value

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "identity_id": identity_id,
                "name": name,
            }
        )
        if colour is not UNSET:
            field_dict["colour"] = colour

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        identity_id = UUID(d.pop("identity_id"))

        name = d.pop("name")

        _colour = d.pop("colour", UNSET)
        colour: LabelsCreateBodyColour | Unset
        if isinstance(_colour, Unset):
            colour = UNSET
        else:
            colour = LabelsCreateBodyColour(_colour)

        labels_create_body = cls(
            identity_id=identity_id,
            name=name,
            colour=colour,
        )

        return labels_create_body
