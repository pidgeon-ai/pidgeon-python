from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define

if TYPE_CHECKING:
    from ..models.signed_upload_upload import SignedUploadUpload


T = TypeVar("T", bound="SignedUpload")


@_attrs_define
class SignedUpload:
    """
    Attributes:
        id (str):
        filename (str):
        content_type (str):
        size (int):
        upload (SignedUploadUpload):
    """

    id: str
    filename: str
    content_type: str
    size: int
    upload: SignedUploadUpload

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        filename = self.filename

        content_type = self.content_type

        size = self.size

        upload = self.upload.to_dict()

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "id": id,
                "filename": filename,
                "content_type": content_type,
                "size": size,
                "upload": upload,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.signed_upload_upload import SignedUploadUpload  # noqa: PLC0415

        d = dict(src_dict)
        id = d.pop("id")

        filename = d.pop("filename")

        content_type = d.pop("content_type")

        size = d.pop("size")

        upload = SignedUploadUpload.from_dict(d.pop("upload"))

        signed_upload = cls(
            id=id,
            filename=filename,
            content_type=content_type,
            size=size,
            upload=upload,
        )

        return signed_upload
