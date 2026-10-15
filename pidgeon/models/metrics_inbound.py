from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define

T = TypeVar("T", bound="MetricsInbound")


@_attrs_define
class MetricsInbound:
    """
    Attributes:
        received (float):
        spam (float):
    """

    received: float
    spam: float

    def to_dict(self) -> dict[str, Any]:
        received = self.received

        spam = self.spam

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "received": received,
                "spam": spam,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        received = d.pop("received")

        spam = d.pop("spam")

        metrics_inbound = cls(
            received=received,
            spam=spam,
        )

        return metrics_inbound
