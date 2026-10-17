from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define

if TYPE_CHECKING:
    from ..models.metrics_inbound import MetricsInbound
    from ..models.metrics_outbound import MetricsOutbound
    from ..models.metrics_pod_type_0 import MetricsPodType0
    from ..models.metrics_reputation_type_0 import MetricsReputationType0


T = TypeVar("T", bound="Metrics")


@_attrs_define
class Metrics:
    """
    Attributes:
        since (str):
        until (str):
        days (float):
        identity (None | str):
        pod (MetricsPodType0 | None):
        reputation (MetricsReputationType0 | None):
        outbound (MetricsOutbound):
        inbound (MetricsInbound):
    """

    since: str
    until: str
    days: float
    identity: None | str
    pod: MetricsPodType0 | None
    reputation: MetricsReputationType0 | None
    outbound: MetricsOutbound
    inbound: MetricsInbound

    def to_dict(self) -> dict[str, Any]:
        from ..models.metrics_pod_type_0 import MetricsPodType0  # noqa: PLC0415
        from ..models.metrics_reputation_type_0 import MetricsReputationType0  # noqa: PLC0415

        since = self.since

        until = self.until

        days = self.days

        identity: None | str
        identity = self.identity

        pod: dict[str, Any] | None
        if isinstance(self.pod, MetricsPodType0):
            pod = self.pod.to_dict()
        else:
            pod = self.pod

        reputation: dict[str, Any] | None
        if isinstance(self.reputation, MetricsReputationType0):
            reputation = self.reputation.to_dict()
        else:
            reputation = self.reputation

        outbound = self.outbound.to_dict()

        inbound = self.inbound.to_dict()

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "since": since,
                "until": until,
                "days": days,
                "identity": identity,
                "pod": pod,
                "reputation": reputation,
                "outbound": outbound,
                "inbound": inbound,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.metrics_inbound import MetricsInbound  # noqa: PLC0415
        from ..models.metrics_outbound import MetricsOutbound  # noqa: PLC0415
        from ..models.metrics_pod_type_0 import MetricsPodType0  # noqa: PLC0415
        from ..models.metrics_reputation_type_0 import MetricsReputationType0  # noqa: PLC0415

        d = dict(src_dict)
        since = d.pop("since")

        until = d.pop("until")

        days = d.pop("days")

        def _parse_identity(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        identity = _parse_identity(d.pop("identity"))

        def _parse_pod(data: object) -> MetricsPodType0 | None:
            if data is None:
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                pod_type_0 = MetricsPodType0.from_dict(data)

                return pod_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(MetricsPodType0 | None, data)

        pod = _parse_pod(d.pop("pod"))

        def _parse_reputation(data: object) -> MetricsReputationType0 | None:
            if data is None:
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                reputation_type_0 = MetricsReputationType0.from_dict(data)

                return reputation_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(MetricsReputationType0 | None, data)

        reputation = _parse_reputation(d.pop("reputation"))

        outbound = MetricsOutbound.from_dict(d.pop("outbound"))

        inbound = MetricsInbound.from_dict(d.pop("inbound"))

        metrics = cls(
            since=since,
            until=until,
            days=days,
            identity=identity,
            pod=pod,
            reputation=reputation,
            outbound=outbound,
            inbound=inbound,
        )

        return metrics
