from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define

T = TypeVar("T", bound="ReceiveRuleRemoved")


@_attrs_define
class ReceiveRuleRemoved:
    """
    Attributes:
        identity_id (str):
        rule_id (str):
        removed (bool):
    """

    identity_id: str
    rule_id: str
    removed: bool

    def to_dict(self) -> dict[str, Any]:
        identity_id = self.identity_id

        rule_id = self.rule_id

        removed = self.removed

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "identity_id": identity_id,
                "rule_id": rule_id,
                "removed": removed,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        identity_id = d.pop("identity_id")

        rule_id = d.pop("rule_id")

        removed = d.pop("removed")

        receive_rule_removed = cls(
            identity_id=identity_id,
            rule_id=rule_id,
            removed=removed,
        )

        return receive_rule_removed
