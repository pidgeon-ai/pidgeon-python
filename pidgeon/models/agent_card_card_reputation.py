from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define

from ..models.agent_card_card_reputation_standing import AgentCardCardReputationStanding

T = TypeVar("T", bound="AgentCardCardReputation")


@_attrs_define
class AgentCardCardReputation:
    """
    Attributes:
        standing (AgentCardCardReputationStanding):
        since (str): The month the address was made, `YYYY-MM`.
    """

    standing: AgentCardCardReputationStanding
    since: str

    def to_dict(self) -> dict[str, Any]:
        standing = self.standing.value

        since = self.since

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "standing": standing,
                "since": since,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        standing = AgentCardCardReputationStanding(d.pop("standing"))

        since = d.pop("since")

        agent_card_card_reputation = cls(
            standing=standing,
            since=since,
        )

        return agent_card_card_reputation
