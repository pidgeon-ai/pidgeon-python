from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define

if TYPE_CHECKING:
    from ..models.receive_rules_rules_item import ReceiveRulesRulesItem


T = TypeVar("T", bound="ReceiveRules")


@_attrs_define
class ReceiveRules:
    """
    Attributes:
        identity_id (str):
        receive_policy (str): open, or list: only senders with an inbox rule, on mail that passes DMARC.
        rules (list[ReceiveRulesRulesItem]):
    """

    identity_id: str
    receive_policy: str
    rules: list[ReceiveRulesRulesItem]

    def to_dict(self) -> dict[str, Any]:
        identity_id = self.identity_id

        receive_policy = self.receive_policy

        rules = []
        for rules_item_data in self.rules:
            rules_item = rules_item_data.to_dict()
            rules.append(rules_item)

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "identity_id": identity_id,
                "receive_policy": receive_policy,
                "rules": rules,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.receive_rules_rules_item import ReceiveRulesRulesItem  # noqa: PLC0415

        d = dict(src_dict)
        identity_id = d.pop("identity_id")

        receive_policy = d.pop("receive_policy")

        rules = []
        _rules = d.pop("rules")
        for rules_item_data in _rules:
            rules_item = ReceiveRulesRulesItem.from_dict(rules_item_data)

            rules.append(rules_item)

        receive_rules = cls(
            identity_id=identity_id,
            receive_policy=receive_policy,
            rules=rules,
        )

        return receive_rules
