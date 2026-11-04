from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define

T = TypeVar("T", bound="GrantsCreateBodyGrantorType1")


@_attrs_define
class GrantsCreateBodyGrantorType1:
    """
    Attributes:
        organisation (bool):
    """

    organisation: bool

    def to_dict(self) -> dict[str, Any]:
        organisation = self.organisation

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "organisation": organisation,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        organisation = d.pop("organisation")

        grants_create_body_grantor_type_1 = cls(
            organisation=organisation,
        )

        return grants_create_body_grantor_type_1
