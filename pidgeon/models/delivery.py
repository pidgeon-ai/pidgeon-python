from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define

T = TypeVar("T", bound="Delivery")


@_attrs_define
class Delivery:
    """
    Attributes:
        id (str):
        event_id (str):
        event_type (str):
        status (str):
        attempts (int):
        response_status (int | None):
        error (None | str):
        created_at (str): ISO-8601, UTC.
        delivered_at (None | str):
        duration_ms (int | None): Round trip of the last attempt. Null before one, and for a refusal.
        next_attempt_at (None | str): When it will be tried again. Null unless it is pending with an attempt behind it.
    """

    id: str
    event_id: str
    event_type: str
    status: str
    attempts: int
    response_status: int | None
    error: None | str
    created_at: str
    delivered_at: None | str
    duration_ms: int | None
    next_attempt_at: None | str

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        event_id = self.event_id

        event_type = self.event_type

        status = self.status

        attempts = self.attempts

        response_status: int | None
        response_status = self.response_status

        error: None | str
        error = self.error

        created_at = self.created_at

        delivered_at: None | str
        delivered_at = self.delivered_at

        duration_ms: int | None
        duration_ms = self.duration_ms

        next_attempt_at: None | str
        next_attempt_at = self.next_attempt_at

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "id": id,
                "event_id": event_id,
                "event_type": event_type,
                "status": status,
                "attempts": attempts,
                "response_status": response_status,
                "error": error,
                "created_at": created_at,
                "delivered_at": delivered_at,
                "duration_ms": duration_ms,
                "next_attempt_at": next_attempt_at,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        id = d.pop("id")

        event_id = d.pop("event_id")

        event_type = d.pop("event_type")

        status = d.pop("status")

        attempts = d.pop("attempts")

        def _parse_response_status(data: object) -> int | None:
            if data is None:
                return data
            return cast(int | None, data)

        response_status = _parse_response_status(d.pop("response_status"))

        def _parse_error(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        error = _parse_error(d.pop("error"))

        created_at = d.pop("created_at")

        def _parse_delivered_at(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        delivered_at = _parse_delivered_at(d.pop("delivered_at"))

        def _parse_duration_ms(data: object) -> int | None:
            if data is None:
                return data
            return cast(int | None, data)

        duration_ms = _parse_duration_ms(d.pop("duration_ms"))

        def _parse_next_attempt_at(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        next_attempt_at = _parse_next_attempt_at(d.pop("next_attempt_at"))

        delivery = cls(
            id=id,
            event_id=event_id,
            event_type=event_type,
            status=status,
            attempts=attempts,
            response_status=response_status,
            error=error,
            created_at=created_at,
            delivered_at=delivered_at,
            duration_ms=duration_ms,
            next_attempt_at=next_attempt_at,
        )

        return delivery
