from __future__ import annotations

from collections.abc import Mapping
from typing import Any, Literal, TypeVar, cast

from attrs import define as _attrs_define

T = TypeVar("T", bound="CardLogConsistency")


@_attrs_define
class CardLogConsistency:
    """
    Attributes:
        object_ (Literal['card_log_consistency']):
        first (int):
        second (int):
        proof (list[str]): RFC 9162 §2.1.4, base64.
    """

    object_: Literal["card_log_consistency"]
    first: int
    second: int
    proof: list[str]

    def to_dict(self) -> dict[str, Any]:
        object_ = self.object_

        first = self.first

        second = self.second

        proof = self.proof

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "object": object_,
                "first": first,
                "second": second,
                "proof": proof,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        object_ = cast(Literal["card_log_consistency"], d.pop("object"))
        if object_ != "card_log_consistency":
            raise ValueError(f"object must match const 'card_log_consistency', got '{object_}'")

        first = d.pop("first")

        second = d.pop("second")

        proof = cast(list[str], d.pop("proof"))

        card_log_consistency = cls(
            object_=object_,
            first=first,
            second=second,
            proof=proof,
        )

        return card_log_consistency
