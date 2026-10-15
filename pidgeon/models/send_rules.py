from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define

if TYPE_CHECKING:
    from ..models.send_rules_rules_item import SendRulesRulesItem


T = TypeVar("T", bound="SendRules")


@_attrs_define
class SendRules:
    """
    Attributes:
        identity_id (str):
        send_policy (str):
        rules (list[SendRulesRulesItem]):
    """

    identity_id: str
    send_policy: str
    rules: list[SendRulesRulesItem]

    def to_dict(self) -> dict[str, Any]:
        identity_id = self.identity_id

        send_policy = self.send_policy

        rules = []
        for rules_item_data in self.rules:
            rules_item = rules_item_data.to_dict()
            rules.append(rules_item)

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "identity_id": identity_id,
                "send_policy": send_policy,
                "rules": rules,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.send_rules_rules_item import SendRulesRulesItem  # noqa: PLC0415

        d = dict(src_dict)
        identity_id = d.pop("identity_id")

        send_policy = d.pop("send_policy")

        rules = []
        _rules = d.pop("rules")
        for rules_item_data in _rules:
            rules_item = SendRulesRulesItem.from_dict(rules_item_data)

            rules.append(rules_item)

        send_rules = cls(
            identity_id=identity_id,
            send_policy=send_policy,
            rules=rules,
        )

        return send_rules
