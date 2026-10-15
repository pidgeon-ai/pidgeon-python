from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define

from ..models.webhooks_update_body_status import WebhooksUpdateBodyStatus

T = TypeVar("T", bound="WebhooksUpdateBody")


@_attrs_define
class WebhooksUpdateBody:
    """
    Attributes:
        status (WebhooksUpdateBodyStatus):
    """

    status: WebhooksUpdateBodyStatus

    def to_dict(self) -> dict[str, Any]:
        status = self.status.value

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "status": status,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        status = WebhooksUpdateBodyStatus(d.pop("status"))

        webhooks_update_body = cls(
            status=status,
        )

        return webhooks_update_body
