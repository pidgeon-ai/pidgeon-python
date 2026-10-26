from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define

T = TypeVar("T", bound="MessageDeliveryType0RecipientsItem")


@_attrs_define
class MessageDeliveryType0RecipientsItem:
    """
    Attributes:
        address (str):
        state (str):
        bounce_type (None | str):
        diagnostic (None | str):
    """

    address: str
    state: str
    bounce_type: None | str
    diagnostic: None | str

    def to_dict(self) -> dict[str, Any]:
        address = self.address

        state = self.state

        bounce_type: None | str
        bounce_type = self.bounce_type

        diagnostic: None | str
        diagnostic = self.diagnostic

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "address": address,
                "state": state,
                "bounce_type": bounce_type,
                "diagnostic": diagnostic,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        address = d.pop("address")

        state = d.pop("state")

        def _parse_bounce_type(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        bounce_type = _parse_bounce_type(d.pop("bounce_type"))

        def _parse_diagnostic(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        diagnostic = _parse_diagnostic(d.pop("diagnostic"))

        message_delivery_type_0_recipients_item = cls(
            address=address,
            state=state,
            bounce_type=bounce_type,
            diagnostic=diagnostic,
        )

        return message_delivery_type_0_recipients_item
