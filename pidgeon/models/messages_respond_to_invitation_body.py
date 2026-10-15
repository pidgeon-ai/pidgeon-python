from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.messages_respond_to_invitation_body_status import MessagesRespondToInvitationBodyStatus
from ..types import UNSET, Unset

T = TypeVar("T", bound="MessagesRespondToInvitationBody")


@_attrs_define
class MessagesRespondToInvitationBody:
    """
    Attributes:
        status (MessagesRespondToInvitationBodyStatus):
        comment (str | Unset):
    """

    status: MessagesRespondToInvitationBodyStatus
    comment: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        status = self.status.value

        comment = self.comment

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "status": status,
            }
        )
        if comment is not UNSET:
            field_dict["comment"] = comment

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        status = MessagesRespondToInvitationBodyStatus(d.pop("status"))

        comment = d.pop("comment", UNSET)

        messages_respond_to_invitation_body = cls(
            status=status,
            comment=comment,
        )

        messages_respond_to_invitation_body.additional_properties = d
        return messages_respond_to_invitation_body

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
