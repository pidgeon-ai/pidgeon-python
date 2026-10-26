from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define

if TYPE_CHECKING:
    from ..models.message_delivery_type_0_recipients_item import MessageDeliveryType0RecipientsItem


T = TypeVar("T", bound="MessageDeliveryType0")


@_attrs_define
class MessageDeliveryType0:
    """
    Attributes:
        state (str): `queued`, `sent`, `delivered`, `deferred`, `rejected`, `bounced` or `complained`: the worst any
            recipient has reached, so one bounce shows through a delivery.
        delivered_at (None | str):
        recipients (list[MessageDeliveryType0RecipientsItem]):
    """

    state: str
    delivered_at: None | str
    recipients: list[MessageDeliveryType0RecipientsItem]

    def to_dict(self) -> dict[str, Any]:
        state = self.state

        delivered_at: None | str
        delivered_at = self.delivered_at

        recipients = []
        for recipients_item_data in self.recipients:
            recipients_item = recipients_item_data.to_dict()
            recipients.append(recipients_item)

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "state": state,
                "delivered_at": delivered_at,
                "recipients": recipients,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.message_delivery_type_0_recipients_item import MessageDeliveryType0RecipientsItem  # noqa: PLC0415

        d = dict(src_dict)
        state = d.pop("state")

        def _parse_delivered_at(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        delivered_at = _parse_delivered_at(d.pop("delivered_at"))

        recipients = []
        _recipients = d.pop("recipients")
        for recipients_item_data in _recipients:
            recipients_item = MessageDeliveryType0RecipientsItem.from_dict(recipients_item_data)

            recipients.append(recipients_item)

        message_delivery_type_0 = cls(
            state=state,
            delivered_at=delivered_at,
            recipients=recipients,
        )

        return message_delivery_type_0
