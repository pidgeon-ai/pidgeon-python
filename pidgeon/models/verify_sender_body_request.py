from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.verify_sender_body_request_headers import VerifySenderBodyRequestHeaders


T = TypeVar("T", bound="VerifySenderBodyRequest")


@_attrs_define
class VerifySenderBodyRequest:
    """An HTTP request an agent signed (HTTP Message Signatures, Web Bot Auth), as received. Send this or `message`.

    Attributes:
        method (str):
        url (str): The URL the request was sent to.
        headers (VerifySenderBodyRequestHeaders): The request’s headers as received, `Signature-Input` and `Signature`
            among them.
        body (str | Unset): The body as UTF-8, to check against a covered `Content-Digest`.
    """

    method: str
    url: str
    headers: VerifySenderBodyRequestHeaders
    body: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        method = self.method

        url = self.url

        headers = self.headers.to_dict()

        body = self.body

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "method": method,
                "url": url,
                "headers": headers,
            }
        )
        if body is not UNSET:
            field_dict["body"] = body

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.verify_sender_body_request_headers import VerifySenderBodyRequestHeaders  # noqa: PLC0415

        d = dict(src_dict)
        method = d.pop("method")

        url = d.pop("url")

        headers = VerifySenderBodyRequestHeaders.from_dict(d.pop("headers"))

        body = d.pop("body", UNSET)

        verify_sender_body_request = cls(
            method=method,
            url=url,
            headers=headers,
            body=body,
        )

        verify_sender_body_request.additional_properties = d
        return verify_sender_body_request

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
