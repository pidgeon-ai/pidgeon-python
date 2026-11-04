from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define

from ..models.card_log_entry_entry_keys_item_type import CardLogEntryEntryKeysItemType
from ..types import UNSET, Unset

T = TypeVar("T", bound="CardLogEntryEntryKeysItem")


@_attrs_define
class CardLogEntryEntryKeysItem:
    """
    Attributes:
        type_ (CardLogEntryEntryKeysItemType):
        domain (str):
        kid (str | Unset):
        pub (str | Unset): For `post`: the Ed25519 public key, base64url.
        selector (str | Unset):
    """

    type_: CardLogEntryEntryKeysItemType
    domain: str
    kid: str | Unset = UNSET
    pub: str | Unset = UNSET
    selector: str | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        type_ = self.type_.value

        domain = self.domain

        kid = self.kid

        pub = self.pub

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
        if pub is not UNSET:
            field_dict["pub"] = pub
        if selector is not UNSET:
            field_dict["selector"] = selector

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        type_ = CardLogEntryEntryKeysItemType(d.pop("type"))

        domain = d.pop("domain")

        kid = d.pop("kid", UNSET)

        pub = d.pop("pub", UNSET)

        selector = d.pop("selector", UNSET)

        card_log_entry_entry_keys_item = cls(
            type_=type_,
            domain=domain,
            kid=kid,
            pub=pub,
            selector=selector,
        )

        return card_log_entry_entry_keys_item
