from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define

T = TypeVar("T", bound="CardLogMonitor")


@_attrs_define
class CardLogMonitor:
    """
    Attributes:
        id (str):
        term (str): The name or domain watched for.
        email (bool): Whether a match is emailed to the workspace’s owners.
        next_index (int): The first log entry it has not matched yet.
        created_at (str): ISO-8601, UTC.
    """

    id: str
    term: str
    email: bool
    next_index: int
    created_at: str

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        term = self.term

        email = self.email

        next_index = self.next_index

        created_at = self.created_at

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "id": id,
                "term": term,
                "email": email,
                "next_index": next_index,
                "created_at": created_at,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        id = d.pop("id")

        term = d.pop("term")

        email = d.pop("email")

        next_index = d.pop("next_index")

        created_at = d.pop("created_at")

        card_log_monitor = cls(
            id=id,
            term=term,
            email=email,
            next_index=next_index,
            created_at=created_at,
        )

        return card_log_monitor
