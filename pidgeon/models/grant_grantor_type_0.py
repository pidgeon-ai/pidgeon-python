from __future__ import annotations

from collections.abc import Mapping
from typing import Any, Literal, TypeVar, cast

from attrs import define as _attrs_define

T = TypeVar("T", bound="GrantGrantorType0")


@_attrs_define
class GrantGrantorType0:
    """
    Attributes:
        type_ (Literal['person']):
        email (str):
    """

    type_: Literal["person"]
    email: str

    def to_dict(self) -> dict[str, Any]:
        type_ = self.type_

        email = self.email

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "type": type_,
                "email": email,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        type_ = cast(Literal["person"], d.pop("type"))
        if type_ != "person":
            raise ValueError(f"type must match const 'person', got '{type_}'")

        email = d.pop("email")

        grant_grantor_type_0 = cls(
            type_=type_,
            email=email,
        )

        return grant_grantor_type_0
