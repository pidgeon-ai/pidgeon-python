from __future__ import annotations

from collections.abc import Mapping
from typing import Any, Literal, TypeVar, cast

from attrs import define as _attrs_define

T = TypeVar("T", bound="GrantGrantorType1")


@_attrs_define
class GrantGrantorType1:
    """
    Attributes:
        type_ (Literal['organisation']):
        domain (str):
    """

    type_: Literal["organisation"]
    domain: str

    def to_dict(self) -> dict[str, Any]:
        type_ = self.type_

        domain = self.domain

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "type": type_,
                "domain": domain,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        type_ = cast(Literal["organisation"], d.pop("type"))
        if type_ != "organisation":
            raise ValueError(f"type must match const 'organisation', got '{type_}'")

        domain = d.pop("domain")

        grant_grantor_type_1 = cls(
            type_=type_,
            domain=domain,
        )

        return grant_grantor_type_1
