from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define

from ..models.routing_rule_destination_type import RoutingRuleDestinationType
from ..models.routing_rule_match_type import RoutingRuleMatchType
from ..models.routing_rule_status import RoutingRuleStatus

T = TypeVar("T", bound="RoutingRule")


@_attrs_define
class RoutingRule:
    """
    Attributes:
        id (str):
        match (str):
        match_type (RoutingRuleMatchType):
        destination_type (RoutingRuleDestinationType):
        destination (str):
        destination_id (None | str):
        status (RoutingRuleStatus):
        domain (str):
        domain_id (str):
        created_at (str): ISO-8601, UTC.
    """

    id: str
    match: str
    match_type: RoutingRuleMatchType
    destination_type: RoutingRuleDestinationType
    destination: str
    destination_id: None | str
    status: RoutingRuleStatus
    domain: str
    domain_id: str
    created_at: str

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        match = self.match

        match_type = self.match_type.value

        destination_type = self.destination_type.value

        destination = self.destination

        destination_id: None | str
        destination_id = self.destination_id

        status = self.status.value

        domain = self.domain

        domain_id = self.domain_id

        created_at = self.created_at

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "id": id,
                "match": match,
                "match_type": match_type,
                "destination_type": destination_type,
                "destination": destination,
                "destination_id": destination_id,
                "status": status,
                "domain": domain,
                "domain_id": domain_id,
                "created_at": created_at,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        id = d.pop("id")

        match = d.pop("match")

        match_type = RoutingRuleMatchType(d.pop("match_type"))

        destination_type = RoutingRuleDestinationType(d.pop("destination_type"))

        destination = d.pop("destination")

        def _parse_destination_id(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        destination_id = _parse_destination_id(d.pop("destination_id"))

        status = RoutingRuleStatus(d.pop("status"))

        domain = d.pop("domain")

        domain_id = d.pop("domain_id")

        created_at = d.pop("created_at")

        routing_rule = cls(
            id=id,
            match=match,
            match_type=match_type,
            destination_type=destination_type,
            destination=destination,
            destination_id=destination_id,
            status=status,
            domain=domain,
            domain_id=domain_id,
            created_at=created_at,
        )

        return routing_rule
