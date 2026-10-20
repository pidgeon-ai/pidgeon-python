from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define

T = TypeVar("T", bound="AwaitedMessageHeldBack")


@_attrs_define
class AwaitedMessageHeldBack:
    """What matched and was not returned. A wait that times out with `spam` above zero did not miss the message: it was
    filed as spam.

        Attributes:
            spam (int): Matching messages that arrived and were filed as spam.
            message_ids (list[str]): Their ids, for `GET /messages/{id}`.
            how_to_include (None | str): What to do about them, in a sentence. Null when nothing was held back.
    """

    spam: int
    message_ids: list[str]
    how_to_include: None | str

    def to_dict(self) -> dict[str, Any]:
        spam = self.spam

        message_ids = self.message_ids

        how_to_include: None | str
        how_to_include = self.how_to_include

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "spam": spam,
                "message_ids": message_ids,
                "how_to_include": how_to_include,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        spam = d.pop("spam")

        message_ids = cast(list[str], d.pop("message_ids"))

        def _parse_how_to_include(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        how_to_include = _parse_how_to_include(d.pop("how_to_include"))

        awaited_message_held_back = cls(
            spam=spam,
            message_ids=message_ids,
            how_to_include=how_to_include,
        )

        return awaited_message_held_back
