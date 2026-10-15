from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar
from uuid import UUID

from attrs import define as _attrs_define

T = TypeVar("T", bound="ThreadsLabelsCreateBody")


@_attrs_define
class ThreadsLabelsCreateBody:
    """
    Attributes:
        label_id (UUID):
    """

    label_id: UUID

    def to_dict(self) -> dict[str, Any]:
        label_id = str(self.label_id)

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "label_id": label_id,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        label_id = UUID(d.pop("label_id"))

        threads_labels_create_body = cls(
            label_id=label_id,
        )

        return threads_labels_create_body
