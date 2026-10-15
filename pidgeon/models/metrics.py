from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define

if TYPE_CHECKING:
    from ..models.metrics_inbound import MetricsInbound
    from ..models.metrics_outbound import MetricsOutbound


T = TypeVar("T", bound="Metrics")


@_attrs_define
class Metrics:
    """
    Attributes:
        since (str):
        until (str):
        days (float):
        identity (None | str):
        outbound (MetricsOutbound):
        inbound (MetricsInbound):
    """

    since: str
    until: str
    days: float
    identity: None | str
    outbound: MetricsOutbound
    inbound: MetricsInbound

    def to_dict(self) -> dict[str, Any]:
        since = self.since

        until = self.until

        days = self.days

        identity: None | str
        identity = self.identity

        outbound = self.outbound.to_dict()

        inbound = self.inbound.to_dict()

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "since": since,
                "until": until,
                "days": days,
                "identity": identity,
                "outbound": outbound,
                "inbound": inbound,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.metrics_inbound import MetricsInbound  # noqa: PLC0415
        from ..models.metrics_outbound import MetricsOutbound  # noqa: PLC0415

        d = dict(src_dict)
        since = d.pop("since")

        until = d.pop("until")

        days = d.pop("days")

        def _parse_identity(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        identity = _parse_identity(d.pop("identity"))

        outbound = MetricsOutbound.from_dict(d.pop("outbound"))

        inbound = MetricsInbound.from_dict(d.pop("inbound"))

        metrics = cls(
            since=since,
            until=until,
            days=days,
            identity=identity,
            outbound=outbound,
            inbound=inbound,
        )

        return metrics
