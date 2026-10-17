from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define

from ..models.metrics_reputation_type_0_sending import MetricsReputationType0Sending

T = TypeVar("T", bound="MetricsReputationType0")


@_attrs_define
class MetricsReputationType0:
    """
    Attributes:
        sending (MetricsReputationType0Sending):
    """

    sending: MetricsReputationType0Sending

    def to_dict(self) -> dict[str, Any]:
        sending = self.sending.value

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "sending": sending,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        sending = MetricsReputationType0Sending(d.pop("sending"))

        metrics_reputation_type_0 = cls(
            sending=sending,
        )

        return metrics_reputation_type_0
