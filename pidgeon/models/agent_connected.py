from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define

T = TypeVar("T", bound="AgentConnected")


@_attrs_define
class AgentConnected:
    """
    Attributes:
        address (str):
        identity_id (str):
        api_key (str):
        api_key_id (str):
    """

    address: str
    identity_id: str
    api_key: str
    api_key_id: str

    def to_dict(self) -> dict[str, Any]:
        address = self.address

        identity_id = self.identity_id

        api_key = self.api_key

        api_key_id = self.api_key_id

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "address": address,
                "identity_id": identity_id,
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

        api_key = d.pop("api_key")

        api_key_id = d.pop("api_key_id")

        agent_connected = cls(
            address=address,
            identity_id=identity_id,
            api_key=api_key,
            api_key_id=api_key_id,
        )

        return agent_connected
