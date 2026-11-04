from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define

from ..models.grant_subject_type import GrantSubjectType

T = TypeVar("T", bound="GrantSubject")


@_attrs_define
class GrantSubject:
    """
    Attributes:
        type_ (GrantSubjectType):
        id (str):
    """

    type_: GrantSubjectType
    id: str

    def to_dict(self) -> dict[str, Any]:
        type_ = self.type_.value

        id = self.id

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "type": type_,
                "id": id,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        type_ = GrantSubjectType(d.pop("type"))

        id = d.pop("id")

        grant_subject = cls(
            type_=type_,
            id=id,
        )

        return grant_subject
