from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, Literal, TypeVar, cast

from attrs import define as _attrs_define

if TYPE_CHECKING:
    from ..models.signed_upload_upload_headers import SignedUploadUploadHeaders


T = TypeVar("T", bound="SignedUploadUpload")


@_attrs_define
class SignedUploadUpload:
    """
    Attributes:
        method (Literal['PUT']):
        url (str):
        headers (SignedUploadUploadHeaders):
        expires_at (str): ISO-8601, UTC.
    """

    method: Literal["PUT"]
    url: str
    headers: SignedUploadUploadHeaders
    expires_at: str

    def to_dict(self) -> dict[str, Any]:
        method = self.method

        url = self.url

        headers = self.headers.to_dict()

        expires_at = self.expires_at

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "method": method,
                "url": url,
                "headers": headers,
                "expires_at": expires_at,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.signed_upload_upload_headers import SignedUploadUploadHeaders  # noqa: PLC0415

        d = dict(src_dict)
        method = cast(Literal["PUT"], d.pop("method"))
        if method != "PUT":
            raise ValueError(f"method must match const 'PUT', got '{method}'")

        url = d.pop("url")

        headers = SignedUploadUploadHeaders.from_dict(d.pop("headers"))

        expires_at = d.pop("expires_at")

        signed_upload_upload = cls(
            method=method,
            url=url,
            headers=headers,
            expires_at=expires_at,
        )

        return signed_upload_upload
