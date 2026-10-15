from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define

T = TypeVar("T", bound="AgentVerified")


@_attrs_define
class AgentVerified:
    """
    Attributes:
        address (str):
        identity_id (str):
        sign_in_url (str):
        api_key (str):
        api_key_id (str):
    """

    address: str
    identity_id: str
    sign_in_url: str
    api_key: str
    api_key_id: str

    def to_dict(self) -> dict[str, Any]:
        address = self.address

        identity_id = self.identity_id

        sign_in_url = self.sign_in_url

        api_key = self.api_key

        api_key_id = self.api_key_id

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "address": address,
                "identity_id": identity_id,
                "sign_in_url": sign_in_url,
                "api_key": api_key,
                "api_key_id": api_key_id,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        address = d.pop("address")

        identity_id = d.pop("identity_id")

        sign_in_url = d.pop("sign_in_url")

        api_key = d.pop("api_key")

        api_key_id = d.pop("api_key_id")

        agent_verified = cls(
            address=address,
            identity_id=identity_id,
            sign_in_url=sign_in_url,
            api_key=api_key,
            api_key_id=api_key_id,
        )

        return agent_verified
