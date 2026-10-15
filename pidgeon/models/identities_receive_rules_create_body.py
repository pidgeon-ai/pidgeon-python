from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define

from ..models.identities_receive_rules_create_body_action import IdentitiesReceiveRulesCreateBodyAction

T = TypeVar("T", bound="IdentitiesReceiveRulesCreateBody")


@_attrs_define
class IdentitiesReceiveRulesCreateBody:
    """
    Attributes:
        action (IdentitiesReceiveRulesCreateBodyAction):
        value (str):
    """

    action: IdentitiesReceiveRulesCreateBodyAction
    value: str

    def to_dict(self) -> dict[str, Any]:
        action = self.action.value

        value = self.value

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "action": action,
                "value": value,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        action = IdentitiesReceiveRulesCreateBodyAction(d.pop("action"))

        value = d.pop("value")

        identities_receive_rules_create_body = cls(
            action=action,
            value=value,
        )

        return identities_receive_rules_create_body
