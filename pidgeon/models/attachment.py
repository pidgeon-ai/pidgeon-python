from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define

T = TypeVar("T", bound="Attachment")


@_attrs_define
class Attachment:
    """
    Attributes:
        id (str):
        filename (str):
        content_type (str):
        size (int):
        downloadable (bool): False when there is metadata but no object store behind it.
    """

    id: str
    filename: str
    content_type: str
    size: int
    downloadable: bool

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        filename = self.filename

        content_type = self.content_type

        size = self.size

        downloadable = self.downloadable

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "id": id,
                "filename": filename,
                "content_type": content_type,
                "size": size,
                "downloadable": downloadable,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        id = d.pop("id")

        filename = d.pop("filename")

        content_type = d.pop("content_type")

        size = d.pop("size")

        downloadable = d.pop("downloadable")

        attachment = cls(
            id=id,
            filename=filename,
            content_type=content_type,
            size=size,
            downloadable=downloadable,
        )

        return attachment
