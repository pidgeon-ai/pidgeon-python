from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define

if TYPE_CHECKING:
    from ..models.awaited_message_held_back import AwaitedMessageHeldBack
    from ..models.awaited_message_message_type_0 import AwaitedMessageMessageType0


T = TypeVar("T", bound="AwaitedMessage")


@_attrs_define
class AwaitedMessage:
    """
    Attributes:
        message (AwaitedMessageMessageType0 | None): The first matching message to arrive, or null when `timeout` passed
            first.
        timed_out (bool):
        cursor (str): Pass as `after` on the next call, so a message arriving between two calls is not missed.
        held_back (AwaitedMessageHeldBack): What matched and was not returned. A wait that times out with `spam` or
            `unauthenticated` above zero did not miss the message: it was held back.
    """

    message: AwaitedMessageMessageType0 | None
    timed_out: bool
    cursor: str
    held_back: AwaitedMessageHeldBack

    def to_dict(self) -> dict[str, Any]:
        from ..models.awaited_message_message_type_0 import AwaitedMessageMessageType0  # noqa: PLC0415

        message: dict[str, Any] | None
        if isinstance(self.message, AwaitedMessageMessageType0):
            message = self.message.to_dict()
        else:
            message = self.message

        timed_out = self.timed_out

        cursor = self.cursor

        held_back = self.held_back.to_dict()

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "message": message,
                "timed_out": timed_out,
                "cursor": cursor,
                "held_back": held_back,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.awaited_message_held_back import AwaitedMessageHeldBack  # noqa: PLC0415
        from ..models.awaited_message_message_type_0 import AwaitedMessageMessageType0  # noqa: PLC0415

        d = dict(src_dict)

        def _parse_message(data: object) -> AwaitedMessageMessageType0 | None:
            if data is None:
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                message_type_0 = AwaitedMessageMessageType0.from_dict(data)

                return message_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(AwaitedMessageMessageType0 | None, data)

        message = _parse_message(d.pop("message"))

        timed_out = d.pop("timed_out")

        cursor = d.pop("cursor")

        held_back = AwaitedMessageHeldBack.from_dict(d.pop("held_back"))

        awaited_message = cls(
            message=message,
            timed_out=timed_out,
            cursor=cursor,
            held_back=held_back,
        )

        return awaited_message
