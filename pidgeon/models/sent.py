from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define

if TYPE_CHECKING:
    from ..models.sent_rejected_item import SentRejectedItem


T = TypeVar("T", bound="Sent")


@_attrs_define
class Sent:
    """
    Attributes:
        id (str):
        thread_id (str):
        rejected (list[SentRejectedItem]):
    """

    id: str
    thread_id: str
    rejected: list[SentRejectedItem]

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        thread_id = self.thread_id

        rejected = []
        for rejected_item_data in self.rejected:
            rejected_item = rejected_item_data.to_dict()
            rejected.append(rejected_item)

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "id": id,
                "thread_id": thread_id,
                "rejected": rejected,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.sent_rejected_item import SentRejectedItem  # noqa: PLC0415

        d = dict(src_dict)
        id = d.pop("id")

        thread_id = d.pop("thread_id")

        rejected = []
        _rejected = d.pop("rejected")
        for rejected_item_data in _rejected:
            rejected_item = SentRejectedItem.from_dict(rejected_item_data)

            rejected.append(rejected_item)

        sent = cls(
            id=id,
            thread_id=thread_id,
            rejected=rejected,
        )

        return sent
