from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define

T = TypeVar("T", bound="LabelRemoved")


@_attrs_define
class LabelRemoved:
    """
    Attributes:
        thread_id (str):
        label_id (str):
        removed (bool):
    """

    thread_id: str
    label_id: str
    removed: bool

    def to_dict(self) -> dict[str, Any]:
        thread_id = self.thread_id

        label_id = self.label_id

        removed = self.removed

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "thread_id": thread_id,
                "label_id": label_id,
                "removed": removed,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        thread_id = d.pop("thread_id")

        label_id = d.pop("label_id")

        removed = d.pop("removed")

        label_removed = cls(
            thread_id=thread_id,
            label_id=label_id,
            removed=removed,
        )

        return label_removed
