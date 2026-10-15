from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define

from ..models.label_colour import LabelColour

T = TypeVar("T", bound="Label")


@_attrs_define
class Label:
    """
    Attributes:
        id (str):
        identity_id (str):
        name (str):
        colour (LabelColour):
        created_at (str): ISO-8601, UTC.
    """

    id: str
    identity_id: str
    name: str
    colour: LabelColour
    created_at: str

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        identity_id = self.identity_id

        name = self.name

        colour = self.colour.value

        created_at = self.created_at

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "id": id,
                "identity_id": identity_id,
                "name": name,
                "colour": colour,
                "created_at": created_at,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        id = d.pop("id")

        identity_id = d.pop("identity_id")

        name = d.pop("name")

        colour = LabelColour(d.pop("colour"))

        created_at = d.pop("created_at")

        label = cls(
            id=id,
            identity_id=identity_id,
            name=name,
            colour=colour,
            created_at=created_at,
        )

        return label
