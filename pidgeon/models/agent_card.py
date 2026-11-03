from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, Literal, TypeVar, cast

from attrs import define as _attrs_define

if TYPE_CHECKING:
    from ..models.agent_card_card import AgentCardCard


T = TypeVar("T", bound="AgentCard")


@_attrs_define
class AgentCard:
    """
    Attributes:
        object_ (Literal['agent_card']):
        url (str): The card’s permanent URL.
        jws (str): Compact JWS, EdDSA, `typ: agent-card+jwt`. Check it against the keys at `<iss>/.well-
            known/post.json`.
        card (AgentCardCard):
    """

    object_: Literal["agent_card"]
    url: str
    jws: str
    card: AgentCardCard

    def to_dict(self) -> dict[str, Any]:
        object_ = self.object_

        url = self.url

        jws = self.jws

        card = self.card.to_dict()

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "object": object_,
                "url": url,
                "jws": jws,
                "card": card,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.agent_card_card import AgentCardCard  # noqa: PLC0415

        d = dict(src_dict)
        object_ = cast(Literal["agent_card"], d.pop("object"))
        if object_ != "agent_card":
            raise ValueError(f"object must match const 'agent_card', got '{object_}'")

        url = d.pop("url")

        jws = d.pop("jws")

        card = AgentCardCard.from_dict(d.pop("card"))

        agent_card = cls(
            object_=object_,
            url=url,
            jws=jws,
            card=card,
        )

        return agent_card
