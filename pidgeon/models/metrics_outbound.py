from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define

T = TypeVar("T", bound="MetricsOutbound")


@_attrs_define
class MetricsOutbound:
    """
    Attributes:
        sent (float):
        delivered (float):
        bounced (float):
        rejected (float):
        complained (float):
        delivery_rate (float | None):
    """

    sent: float
    delivered: float
    bounced: float
    rejected: float
    complained: float
    delivery_rate: float | None

    def to_dict(self) -> dict[str, Any]:
        sent = self.sent

        delivered = self.delivered

        bounced = self.bounced

        rejected = self.rejected

        complained = self.complained

        delivery_rate: float | None
        delivery_rate = self.delivery_rate

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "sent": sent,
                "delivered": delivered,
                "bounced": bounced,
                "rejected": rejected,
                "complained": complained,
                "delivery_rate": delivery_rate,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        sent = d.pop("sent")

        delivered = d.pop("delivered")

        bounced = d.pop("bounced")

        rejected = d.pop("rejected")

        complained = d.pop("complained")

        def _parse_delivery_rate(data: object) -> float | None:
            if data is None:
                return data
            return cast(float | None, data)

        delivery_rate = _parse_delivery_rate(d.pop("delivery_rate"))

        metrics_outbound = cls(
            sent=sent,
            delivered=delivered,
            bounced=bounced,
            rejected=rejected,
            complained=complained,
            delivery_rate=delivery_rate,
        )

        return metrics_outbound
