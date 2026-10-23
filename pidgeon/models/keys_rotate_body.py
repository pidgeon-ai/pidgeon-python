from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define

from ..types import UNSET, Unset

T = TypeVar("T", bound="KeysRotateBody")


@_attrs_define
class KeysRotateBody:
    """
    Attributes:
        grace_period_seconds (int | Unset):
    """

    grace_period_seconds: int | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        grace_period_seconds = self.grace_period_seconds

        field_dict: dict[str, Any] = {}

        field_dict.update({})
        if grace_period_seconds is not UNSET:
            field_dict["grace_period_seconds"] = grace_period_seconds

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        grace_period_seconds = d.pop("grace_period_seconds", UNSET)

        keys_rotate_body = cls(
            grace_period_seconds=grace_period_seconds,
        )

        return keys_rotate_body
