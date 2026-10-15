from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define

if TYPE_CHECKING:
    from ..models.webhook_headers_headers import WebhookHeadersHeaders


T = TypeVar("T", bound="WebhookHeaders")


@_attrs_define
class WebhookHeaders:
    """
    Attributes:
        headers (WebhookHeadersHeaders):
    """

    headers: WebhookHeadersHeaders

    def to_dict(self) -> dict[str, Any]:
        headers = self.headers.to_dict()

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "headers": headers,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.webhook_headers_headers import WebhookHeadersHeaders  # noqa: PLC0415

        d = dict(src_dict)
        headers = WebhookHeadersHeaders.from_dict(d.pop("headers"))

        webhook_headers = cls(
            headers=headers,
        )

        return webhook_headers
