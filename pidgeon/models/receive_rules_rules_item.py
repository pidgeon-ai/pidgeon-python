from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define

from ..models.receive_rules_rules_item_match_type import ReceiveRulesRulesItemMatchType

T = TypeVar("T", bound="ReceiveRulesRulesItem")


@_attrs_define
class ReceiveRulesRulesItem:
    """
    Attributes:
        id (str):
        action (str): reject refuses before the message is stored. spam, trash and archive file it. inbox means never
            classify this sender as spam.
        match_type (ReceiveRulesRulesItemMatchType):
        match_value (str):
        created_at (str): ISO-8601, UTC.
    """

    id: str
    action: str
    match_type: ReceiveRulesRulesItemMatchType
    match_value: str
    created_at: str

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        action = self.action

        match_type = self.match_type.value

        match_value = self.match_value

        created_at = self.created_at

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "id": id,
                "action": action,
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

        action = d.pop("action")

        match_type = ReceiveRulesRulesItemMatchType(d.pop("match_type"))

        match_value = d.pop("match_value")

        created_at = d.pop("created_at")

        receive_rules_rules_item = cls(
            id=id,
            action=action,
            match_type=match_type,
            match_value=match_value,
            created_at=created_at,
        )

        return receive_rules_rules_item
