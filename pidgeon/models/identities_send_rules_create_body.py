from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define

from ..models.identities_send_rules_create_body_effect import IdentitiesSendRulesCreateBodyEffect

T = TypeVar("T", bound="IdentitiesSendRulesCreateBody")


@_attrs_define
class IdentitiesSendRulesCreateBody:
    """
    Attributes:
        effect (IdentitiesSendRulesCreateBodyEffect):
        value (str):
    """

    effect: IdentitiesSendRulesCreateBodyEffect
    value: str

    def to_dict(self) -> dict[str, Any]:
        effect = self.effect.value

        value = self.value

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "effect": effect,
                "value": value,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        effect = IdentitiesSendRulesCreateBodyEffect(d.pop("effect"))

        value = d.pop("value")

        identities_send_rules_create_body = cls(
            effect=effect,
            value=value,
        )

        return identities_send_rules_create_body
