from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define

T = TypeVar("T", bound="Calendar")


@_attrs_define
class Calendar:
    """
    Attributes:
        identity_id (str):
        identity (str):
        timezone (str):
        event_count (float):
        etag (str):
        created_at (str): ISO-8601, UTC.
        updated_at (str): ISO-8601, UTC.
    """

    identity_id: str
    identity: str
    timezone: str
    event_count: float
    etag: str
    created_at: str
    updated_at: str

    def to_dict(self) -> dict[str, Any]:
        identity_id = self.identity_id

        identity = self.identity

        timezone = self.timezone

        event_count = self.event_count

        etag = self.etag

        created_at = self.created_at

        updated_at = self.updated_at

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "identity_id": identity_id,
                "identity": identity,
                "timezone": timezone,
                "event_count": event_count,
                "etag": etag,
                "created_at": created_at,
                "updated_at": updated_at,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        identity_id = d.pop("identity_id")

        identity = d.pop("identity")

        timezone = d.pop("timezone")

        event_count = d.pop("event_count")

        etag = d.pop("etag")

        created_at = d.pop("created_at")

        updated_at = d.pop("updated_at")

        calendar = cls(
            identity_id=identity_id,
            identity=identity,
            timezone=timezone,
            event_count=event_count,
            etag=etag,
            created_at=created_at,
            updated_at=updated_at,
        )

        return calendar
