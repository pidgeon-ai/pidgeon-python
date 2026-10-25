from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define

from ..models.created_domain_existing_mail_type_0_provider import CreatedDomainExistingMailType0Provider

T = TypeVar("T", bound="CreatedDomainExistingMailType0")


@_attrs_define
class CreatedDomainExistingMailType0:
    """
    Attributes:
        provider (CreatedDomainExistingMailType0Provider):
        name (str):
        hosts (list[str]):
    """

    provider: CreatedDomainExistingMailType0Provider
    name: str
    hosts: list[str]

    def to_dict(self) -> dict[str, Any]:
        provider = self.provider.value

        name = self.name

        hosts = self.hosts

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "provider": provider,
                "name": name,
                "hosts": hosts,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        provider = CreatedDomainExistingMailType0Provider(d.pop("provider"))

        name = d.pop("name")

        hosts = cast(list[str], d.pop("hosts"))

        created_domain_existing_mail_type_0 = cls(
            provider=provider,
            name=name,
            hosts=hosts,
        )

        return created_domain_existing_mail_type_0
