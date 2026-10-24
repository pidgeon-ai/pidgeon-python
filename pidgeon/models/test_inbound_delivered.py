from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define

from ..models.test_inbound_delivered_status import TestInboundDeliveredStatus

T = TypeVar("T", bound="TestInboundDelivered")


@_attrs_define
class TestInboundDelivered:
    """
    Attributes:
        status (TestInboundDeliveredStatus): `delivered` in the normal case; `rejected` when a sender rule on the
            address refuses it, as it would refuse the real thing.
        message_id (None | str):
        thread_id (None | str):
        identity_id (str):
        spam (bool): Whether the spam filter filed it as spam.
    """

    status: TestInboundDeliveredStatus
    message_id: None | str
    thread_id: None | str
    identity_id: str
    spam: bool

    def to_dict(self) -> dict[str, Any]:
        status = self.status.value

        message_id: None | str
        message_id = self.message_id

        thread_id: None | str
        thread_id = self.thread_id

        identity_id = self.identity_id

        spam = self.spam

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "status": status,
                "message_id": message_id,
                "thread_id": thread_id,
                "identity_id": identity_id,
                "spam": spam,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        status = TestInboundDeliveredStatus(d.pop("status"))

        def _parse_message_id(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        message_id = _parse_message_id(d.pop("message_id"))

        def _parse_thread_id(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        thread_id = _parse_thread_id(d.pop("thread_id"))

        identity_id = d.pop("identity_id")

        spam = d.pop("spam")

        test_inbound_delivered = cls(
            status=status,
            message_id=message_id,
            thread_id=thread_id,
            identity_id=identity_id,
            spam=spam,
        )

        return test_inbound_delivered
