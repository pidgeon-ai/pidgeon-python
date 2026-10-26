from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define

from ..models.warning_code import WarningCode

T = TypeVar("T", bound="Warning_")


@_attrs_define
class Warning_:
    """
    Attributes:
        code (WarningCode):
        fields (list[str]): What the request left out, as the wire spells it: `access`, `key.access`.
        message (str):
        sunset (datetime.datetime): When leaving them out becomes a 400.
    """

    code: WarningCode
    fields: list[str]
    message: str
    sunset: datetime.datetime

    def to_dict(self) -> dict[str, Any]:
        code = self.code.value

        fields = self.fields

        message = self.message

        sunset = self.sunset.isoformat()

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "code": code,
                "fields": fields,
                "message": message,
                "sunset": sunset,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        code = WarningCode(d.pop("code"))

        fields = cast(list[str], d.pop("fields"))

        message = d.pop("message")

        sunset = datetime.datetime.fromisoformat(d.pop("sunset"))

        warning = cls(
            code=code,
            fields=fields,
            message=message,
            sunset=sunset,
        )

        return warning
