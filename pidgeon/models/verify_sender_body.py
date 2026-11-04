from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.verify_sender_body_request import VerifySenderBodyRequest


T = TypeVar("T", bound="VerifySenderBody")


@_attrs_define
class VerifySenderBody:
    """
    Attributes:
        message (str | Unset): The raw message, or its headers. Send this or `request`.
        request (VerifySenderBodyRequest | Unset): An HTTP request an agent signed (HTTP Message Signatures, Web Bot
            Auth), as received. Send this or `message`.
        recipient (str | Unset):
    """

    message: str | Unset = UNSET
    request: VerifySenderBodyRequest | Unset = UNSET
    recipient: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        message = self.message

        request: dict[str, Any] | Unset = UNSET
        if not isinstance(self.request, Unset):
            request = self.request.to_dict()

        recipient = self.recipient

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if message is not UNSET:
            field_dict["message"] = message
        if request is not UNSET:
            field_dict["request"] = request
        if recipient is not UNSET:
            field_dict["recipient"] = recipient

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.verify_sender_body_request import VerifySenderBodyRequest  # noqa: PLC0415

        d = dict(src_dict)
        message = d.pop("message", UNSET)

        _request = d.pop("request", UNSET)
        request: VerifySenderBodyRequest | Unset
        if isinstance(_request, Unset):
            request = UNSET
        else:
            request = VerifySenderBodyRequest.from_dict(_request)

        recipient = d.pop("recipient", UNSET)

        verify_sender_body = cls(
            message=message,
            request=request,
            recipient=recipient,
        )

        verify_sender_body.additional_properties = d
        return verify_sender_body

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
