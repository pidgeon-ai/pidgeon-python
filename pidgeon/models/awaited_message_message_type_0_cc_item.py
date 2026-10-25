from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define

from ..types import UNSET, Unset

T = TypeVar("T", bound="AwaitedMessageMessageType0CcItem")


@_attrs_define
class AwaitedMessageMessageType0CcItem:
    """An address, with the display name when one was given.

    Attributes:
        email (str):
        name (None | str | Unset):
    """

    email: str
    name: None | str | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        email = self.email

        name: None | str | Unset
        if isinstance(self.name, Unset):
            name = UNSET
        else:
            name = self.name

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "email": email,
            }
        )
        if name is not UNSET:
            field_dict["name"] = name

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        email = d.pop("email")

        def _parse_name(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        name = _parse_name(d.pop("name", UNSET))

        awaited_message_message_type_0_cc_item = cls(
            email=email,
            name=name,
        )

        return awaited_message_message_type_0_cc_item
