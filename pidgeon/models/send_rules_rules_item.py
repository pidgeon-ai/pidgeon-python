from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define

from ..models.send_rules_rules_item_match_type import SendRulesRulesItemMatchType

T = TypeVar("T", bound="SendRulesRulesItem")


@_attrs_define
class SendRulesRulesItem:
    """
    Attributes:
        id (str):
        effect (str): allow or block. A block refuses under every policy.
        match_type (SendRulesRulesItemMatchType):
        match_value (str):
        created_at (str): ISO-8601, UTC.
    """

    id: str
    effect: str
    match_type: SendRulesRulesItemMatchType
    match_value: str
    created_at: str

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        effect = self.effect

        match_type = self.match_type.value

        match_value = self.match_value

        created_at = self.created_at

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "id": id,
                "effect": effect,
                "match_type": match_type,
                "match_value": match_value,
                "created_at": created_at,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        id = d.pop("id")

        effect = d.pop("effect")

        match_type = SendRulesRulesItemMatchType(d.pop("match_type"))

        match_value = d.pop("match_value")

        created_at = d.pop("created_at")

        send_rules_rules_item = cls(
            id=id,
            effect=effect,
            match_type=match_type,
            match_value=match_value,
            created_at=created_at,
        )

        return send_rules_rules_item
