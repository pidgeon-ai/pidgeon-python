from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define

from ..models.sender_verification_grants_item_subject_type_0_type import SenderVerificationGrantsItemSubjectType0Type

T = TypeVar("T", bound="SenderVerificationGrantsItemSubjectType0")


@_attrs_define
class SenderVerificationGrantsItemSubjectType0:
    """
    Attributes:
        type_ (SenderVerificationGrantsItemSubjectType0Type):
        id (str):
    """

    type_: SenderVerificationGrantsItemSubjectType0Type
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
        type_ = SenderVerificationGrantsItemSubjectType0Type(d.pop("type"))

        id = d.pop("id")

        sender_verification_grants_item_subject_type_0 = cls(
            type_=type_,
            id=id,
        )

        return sender_verification_grants_item_subject_type_0
