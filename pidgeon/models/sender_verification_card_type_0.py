from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define

T = TypeVar("T", bound="SenderVerificationCardType0")


@_attrs_define
class SenderVerificationCardType0:
    """
    Attributes:
        url (str):
        standing (str):
        since (str):
    """

    url: str
    standing: str
    since: str

    def to_dict(self) -> dict[str, Any]:
        url = self.url

        standing = self.standing

        since = self.since

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "url": url,
                "standing": standing,
                "since": since,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        url = d.pop("url")

        standing = d.pop("standing")

        since = d.pop("since")

        sender_verification_card_type_0 = cls(
            url=url,
            standing=standing,
            since=since,
        )

        return sender_verification_card_type_0
