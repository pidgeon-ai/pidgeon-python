from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define

T = TypeVar("T", bound="WebhookCreated")


@_attrs_define
class WebhookCreated:
    """
    Attributes:
        id (str):
        url (str):
        identity (None | str):
        event_types (list[str]):
        status (str):
        consecutive_failures (int):
        last_delivered_at (None | str):
        last_failed_at (None | str):
        created_at (str): ISO-8601, UTC.
        secret (str): Shown once, here, and never again.
    """

    id: str
    url: str
    identity: None | str
    event_types: list[str]
    status: str
    consecutive_failures: int
    last_delivered_at: None | str
    last_failed_at: None | str
    created_at: str
    secret: str

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        url = self.url

        identity: None | str
        identity = self.identity

        event_types = self.event_types

        status = self.status

        consecutive_failures = self.consecutive_failures

        last_delivered_at: None | str
        last_delivered_at = self.last_delivered_at

        last_failed_at: None | str
        last_failed_at = self.last_failed_at

        created_at = self.created_at

        secret = self.secret

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "id": id,
                "url": url,
                "identity": identity,
                "event_types": event_types,
                "status": status,
                "consecutive_failures": consecutive_failures,
                "last_delivered_at": last_delivered_at,
                "last_failed_at": last_failed_at,
                "created_at": created_at,
                "secret": secret,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        id = d.pop("id")

        url = d.pop("url")

        def _parse_identity(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        identity = _parse_identity(d.pop("identity"))

        event_types = cast(list[str], d.pop("event_types"))

        status = d.pop("status")

        consecutive_failures = d.pop("consecutive_failures")

        def _parse_last_delivered_at(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        last_delivered_at = _parse_last_delivered_at(d.pop("last_delivered_at"))

        def _parse_last_failed_at(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        last_failed_at = _parse_last_failed_at(d.pop("last_failed_at"))

        created_at = d.pop("created_at")

        secret = d.pop("secret")

        webhook_created = cls(
            id=id,
            url=url,
            identity=identity,
            event_types=event_types,
            status=status,
            consecutive_failures=consecutive_failures,
            last_delivered_at=last_delivered_at,
            last_failed_at=last_failed_at,
            created_at=created_at,
            secret=secret,
        )

        return webhook_created
