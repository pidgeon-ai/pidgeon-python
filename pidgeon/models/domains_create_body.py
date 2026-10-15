from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define

from ..types import UNSET, Unset

T = TypeVar("T", bound="DomainsCreateBody")


@_attrs_define
class DomainsCreateBody:
    """
    Attributes:
        domain (str): A domain name you own, or the shared one. An alternative to `domain_id`.
        inbound_enabled (bool | Unset):
    """

    domain: str
    inbound_enabled: bool | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        domain = self.domain

        inbound_enabled = self.inbound_enabled

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "domain": domain,
            }
        )
        if inbound_enabled is not UNSET:
            field_dict["inbound_enabled"] = inbound_enabled

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        domain = d.pop("domain")

        inbound_enabled = d.pop("inbound_enabled", UNSET)

        domains_create_body = cls(
            domain=domain,
            inbound_enabled=inbound_enabled,
        )

        return domains_create_body
