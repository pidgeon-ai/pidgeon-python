from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define

T = TypeVar("T", bound="GrantTemplateLimitType0")


@_attrs_define
class GrantTemplateLimitType0:
    """
    Attributes:
        amount (int): Minor units: 10000 is $100.00.
        currency (str): ISO 4217.
    """

    amount: int
    currency: str

    def to_dict(self) -> dict[str, Any]:
        amount = self.amount

        currency = self.currency

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "amount": amount,
                "currency": currency,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        amount = d.pop("amount")

        currency = d.pop("currency")

        grant_template_limit_type_0 = cls(
            amount=amount,
            currency=currency,
        )

        return grant_template_limit_type_0
