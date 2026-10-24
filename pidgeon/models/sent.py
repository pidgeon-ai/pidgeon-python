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
        test (bool): True when this was a test-mode send: nothing was handed to the mail provider, and only this
            account’s own addresses received it.
    """

    id: str
    thread_id: str
    rejected: list[SentRejectedItem]
    test: bool

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        thread_id = self.thread_id

        rejected = []
        for rejected_item_data in self.rejected:
            rejected_item = rejected_item_data.to_dict()
            rejected.append(rejected_item)

        test = self.test

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "id": id,
                "thread_id": thread_id,
                "rejected": rejected,
                "test": test,
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

        test = d.pop("test")

        sent = cls(
            id=id,
            thread_id=thread_id,
            rejected=rejected,
            test=test,
        )

        return sent
