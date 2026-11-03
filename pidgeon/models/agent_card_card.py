from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, Literal, TypeVar, cast

from attrs import define as _attrs_define

from ..models.agent_card_card_kind import AgentCardCardKind
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.agent_card_card_keys_item import AgentCardCardKeysItem
    from ..models.agent_card_card_operator import AgentCardCardOperator
    from ..models.agent_card_card_reputation import AgentCardCardReputation


T = TypeVar("T", bound="AgentCardCard")


@_attrs_define
class AgentCardCard:
    """
    Attributes:
        iss (str): `https://post.<domain>`: the domain that signed it.
        sub (str): The address’s id. Never reassigned, unlike the address.
        iat (int):
        exp (int): A day after `iat`. Refetch after it.
        v (Literal['post0']):
        address (str):
        kind (AgentCardCardKind):
        created_at (str): ISO-8601, UTC.
        keys (list[AgentCardCardKeysItem]): What signs this address’s mail.
        reputation (AgentCardCardReputation):
        url (str):
        on_behalf_of (str | Unset):
        operator (AgentCardCardOperator | Unset):
    """

    iss: str
    sub: str
    iat: int
    exp: int
    v: Literal["post0"]
    address: str
    kind: AgentCardCardKind
    created_at: str
    keys: list[AgentCardCardKeysItem]
    reputation: AgentCardCardReputation
    url: str
    on_behalf_of: str | Unset = UNSET
    operator: AgentCardCardOperator | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        iss = self.iss

        sub = self.sub

        iat = self.iat

        exp = self.exp

        v = self.v

        address = self.address

        kind = self.kind.value

        created_at = self.created_at

        keys = []
        for keys_item_data in self.keys:
            keys_item = keys_item_data.to_dict()
            keys.append(keys_item)

        reputation = self.reputation.to_dict()

        url = self.url

        on_behalf_of = self.on_behalf_of

        operator: dict[str, Any] | Unset = UNSET
        if not isinstance(self.operator, Unset):
            operator = self.operator.to_dict()

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "iss": iss,
                "sub": sub,
                "iat": iat,
                "exp": exp,
                "v": v,
                "address": address,
                "kind": kind,
                "created_at": created_at,
                "keys": keys,
                "reputation": reputation,
                "url": url,
            }
        )
        if on_behalf_of is not UNSET:
            field_dict["on_behalf_of"] = on_behalf_of
        if operator is not UNSET:
            field_dict["operator"] = operator

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.agent_card_card_keys_item import AgentCardCardKeysItem  # noqa: PLC0415
        from ..models.agent_card_card_operator import AgentCardCardOperator  # noqa: PLC0415
        from ..models.agent_card_card_reputation import AgentCardCardReputation  # noqa: PLC0415

        d = dict(src_dict)
        iss = d.pop("iss")

        sub = d.pop("sub")

        iat = d.pop("iat")

        exp = d.pop("exp")

        v = cast(Literal["post0"], d.pop("v"))
        if v != "post0":
            raise ValueError(f"v must match const 'post0', got '{v}'")

        address = d.pop("address")

        kind = AgentCardCardKind(d.pop("kind"))

        created_at = d.pop("created_at")

        keys = []
        _keys = d.pop("keys")
        for keys_item_data in _keys:
            keys_item = AgentCardCardKeysItem.from_dict(keys_item_data)

            keys.append(keys_item)

        reputation = AgentCardCardReputation.from_dict(d.pop("reputation"))

        url = d.pop("url")

        on_behalf_of = d.pop("on_behalf_of", UNSET)

        _operator = d.pop("operator", UNSET)
        operator: AgentCardCardOperator | Unset
        if isinstance(_operator, Unset):
            operator = UNSET
        else:
            operator = AgentCardCardOperator.from_dict(_operator)

        agent_card_card = cls(
            iss=iss,
            sub=sub,
            iat=iat,
            exp=exp,
            v=v,
            address=address,
            kind=kind,
            created_at=created_at,
            keys=keys,
            reputation=reputation,
            url=url,
            on_behalf_of=on_behalf_of,
            operator=operator,
        )

        return agent_card_card
