from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define

from ..models.agent_card_card_keys_item_type import AgentCardCardKeysItemType
from ..types import UNSET, Unset

T = TypeVar("T", bound="AgentCardCardKeysItem")


@_attrs_define
class AgentCardCardKeysItem:
    """
    Attributes:
        type_ (AgentCardCardKeysItemType):
        domain (str):
        kid (str | Unset):
        selector (str | Unset):
    """

    type_: AgentCardCardKeysItemType
    domain: str
    kid: str | Unset = UNSET
    selector: str | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        type_ = self.type_.value

        domain = self.domain

        kid = self.kid

        selector = self.selector

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "type": type_,
                "domain": domain,
            }
        )
        if kid is not UNSET:
            field_dict["kid"] = kid
        if selector is not UNSET:
            field_dict["selector"] = selector

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        type_ = AgentCardCardKeysItemType(d.pop("type"))

        domain = d.pop("domain")

        kid = d.pop("kid", UNSET)

        selector = d.pop("selector", UNSET)

        agent_card_card_keys_item = cls(
            type_=type_,
            domain=domain,
            kid=kid,
            selector=selector,
        )

        return agent_card_card_keys_item
