from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar
from uuid import UUID

from attrs import define as _attrs_define

T = TypeVar("T", bound="AttachmentsCreateUploadBody")


@_attrs_define
class AttachmentsCreateUploadBody:
    """
    Attributes:
        identity_id (UUID): The address this belongs to.
        filename (str):
        content_type (str):
        size (int):
    """

    identity_id: UUID
    filename: str
    content_type: str
    size: int

    def to_dict(self) -> dict[str, Any]:
        identity_id = str(self.identity_id)

        filename = self.filename

        content_type = self.content_type

        size = self.size

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "identity_id": identity_id,
                "filename": filename,
                "content_type": content_type,
                "size": size,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        identity_id = UUID(d.pop("identity_id"))

        filename = d.pop("filename")

        content_type = d.pop("content_type")

        size = d.pop("size")

        attachments_create_upload_body = cls(
            identity_id=identity_id,
            filename=filename,
            content_type=content_type,
            size=size,
        )

        return attachments_create_upload_body
