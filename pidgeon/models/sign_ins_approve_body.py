from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define

from ..types import UNSET, Unset

T = TypeVar("T", bound="SignInsApproveBody")


@_attrs_define
class SignInsApproveBody:
    """
    Attributes:
        url (str): Where we POST. HTTPS, and it has to answer within a few seconds.
        address (str | Unset): A whole address — the local part and the domain in one. An alternative to the other two.
    """

    url: str
    address: str | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        url = self.url

        address = self.address

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "url": url,
            }
        )
        if address is not UNSET:
            field_dict["address"] = address

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        url = d.pop("url")

        address = d.pop("address", UNSET)

        sign_ins_approve_body = cls(
            url=url,
            address=address,
        )

        return sign_ins_approve_body
