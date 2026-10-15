from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="AgentAttachHumanBody")


@_attrs_define
class AgentAttachHumanBody:
    """
    Attributes:
        signup_id (UUID): From the signup this is finishing.
        human_email (str): A person who can be reached. They receive the code that finishes the signup.
    """

    signup_id: UUID
    human_email: str
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        signup_id = str(self.signup_id)

        human_email = self.human_email

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "signup_id": signup_id,
                "human_email": human_email,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        signup_id = UUID(d.pop("signup_id"))

        human_email = d.pop("human_email")

        agent_attach_human_body = cls(
            signup_id=signup_id,
            human_email=human_email,
        )

        agent_attach_human_body.additional_properties = d
        return agent_attach_human_body

    @property
    def additional_keys(self) -> list[str]:
        return list(self.additional_properties.keys())

    def __getitem__(self, key: str) -> Any:
        return self.additional_properties[key]

    def __setitem__(self, key: str, value: Any) -> None:
        self.additional_properties[key] = value

    def __delitem__(self, key: str) -> None:
        del self.additional_properties[key]

    def __contains__(self, key: str) -> bool:
        return key in self.additional_properties
