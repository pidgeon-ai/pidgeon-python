from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define

from ..types import UNSET, Unset

T = TypeVar("T", bound="AwaitedMessageHeldBack")


@_attrs_define
class AwaitedMessageHeldBack:
    """What matched and was not returned. A wait that times out with `spam`, `unauthenticated` or `held` above zero did not
    miss the message: it was held back.

        Attributes:
            spam (int): Matching messages that arrived and were filed as spam.
            unauthenticated (int): Messages that matched `from` but did not pass DMARC, so their From may be forged.
            message_ids (list[str]): Their ids, spam first, for `GET /messages/{id}`.
            how_to_include (None | str): What to do about them, in a sentence. Null when nothing was held back.
            held (int | Unset): Messages Pidgeon Firewall held for a person. Matched on `from` alone; returned by a later
                wait once a person releases them. Absent before 1.42.0.
    """

    spam: int
    unauthenticated: int
    message_ids: list[str]
    how_to_include: None | str
    held: int | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        spam = self.spam

        unauthenticated = self.unauthenticated

        message_ids = self.message_ids

        how_to_include: None | str
        how_to_include = self.how_to_include

        held = self.held

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "spam": spam,
                "unauthenticated": unauthenticated,
                "message_ids": message_ids,
                "how_to_include": how_to_include,
            }
        )
        if held is not UNSET:
            field_dict["held"] = held

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        spam = d.pop("spam")

        unauthenticated = d.pop("unauthenticated")

        message_ids = cast(list[str], d.pop("message_ids"))

        def _parse_how_to_include(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        how_to_include = _parse_how_to_include(d.pop("how_to_include"))

        held = d.pop("held", UNSET)

        awaited_message_held_back = cls(
            spam=spam,
            unauthenticated=unauthenticated,
            message_ids=message_ids,
            how_to_include=how_to_include,
            held=held,
        )

        return awaited_message_held_back
