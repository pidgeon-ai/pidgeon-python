from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define

T = TypeVar("T", bound="AgentSignup")


@_attrs_define
class AgentSignup:
    """
    Attributes:
        signup_id (str):
        address (str):
        identity_id (str):
        can_send (bool):
        code_expires_at (None | str):
    """

    signup_id: str
    address: str
    identity_id: str
    can_send: bool
    code_expires_at: None | str

    def to_dict(self) -> dict[str, Any]:
        signup_id = self.signup_id

        address = self.address

        identity_id = self.identity_id

        can_send = self.can_send

        code_expires_at: None | str
        code_expires_at = self.code_expires_at

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "signup_id": signup_id,
                "address": address,
                "identity_id": identity_id,
                "can_send": can_send,
                "code_expires_at": code_expires_at,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        signup_id = d.pop("signup_id")

        address = d.pop("address")

        identity_id = d.pop("identity_id")

        can_send = d.pop("can_send")

        def _parse_code_expires_at(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        code_expires_at = _parse_code_expires_at(d.pop("code_expires_at"))

        agent_signup = cls(
            signup_id=signup_id,
            address=address,
            identity_id=identity_id,
            can_send=can_send,
            code_expires_at=code_expires_at,
        )

        return agent_signup
