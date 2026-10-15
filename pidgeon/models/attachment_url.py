from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define

T = TypeVar("T", bound="AttachmentUrl")


@_attrs_define
class AttachmentUrl:
    """
    Attributes:
        id (str):
        url (str): Short-lived and signed. It expires; do not store it.
    """

    id: str
    url: str

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        url = self.url

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "id": id,
                "url": url,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        id = d.pop("id")

        url = d.pop("url")

        attachment_url = cls(
            id=id,
            url=url,
        )

        return attachment_url
