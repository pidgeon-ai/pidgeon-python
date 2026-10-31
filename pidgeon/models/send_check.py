from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define

from ..models.send_check_status import SendCheckStatus

if TYPE_CHECKING:
    from ..models.send_check_approval_type_0 import SendCheckApprovalType0


T = TypeVar("T", bound="SendCheck")


@_attrs_define
class SendCheck:
    """
    Attributes:
        dry_run (bool): Always true: nothing was sent, written or counted.
        would_send (bool): True when the real send would go now. False when it would wait for a person (`status:
            "pending_approval"`).
        status (SendCheckStatus): The `status` the real send would answer.
        from_ (str):
        to (list[str]):
        cc (list[str]):
        bcc (list[str]):
        thread_id (None | str): The conversation it would go in. Null for a new message, which starts one.
        test (bool): True when the real send would be a test-mode send.
        approval (None | SendCheckApprovalType0): Why it would wait, when `status` is `pending_approval`. Null
            otherwise.
    """

    dry_run: bool
    would_send: bool
    status: SendCheckStatus
    from_: str
    to: list[str]
    cc: list[str]
    bcc: list[str]
    thread_id: None | str
    test: bool
    approval: None | SendCheckApprovalType0

    def to_dict(self) -> dict[str, Any]:
        from ..models.send_check_approval_type_0 import SendCheckApprovalType0  # noqa: PLC0415

        dry_run = self.dry_run

        would_send = self.would_send

        status = self.status.value

        from_ = self.from_

        to = self.to

        cc = self.cc

        bcc = self.bcc

        thread_id: None | str
        thread_id = self.thread_id

        test = self.test

        approval: dict[str, Any] | None
        if isinstance(self.approval, SendCheckApprovalType0):
            approval = self.approval.to_dict()
        else:
            approval = self.approval

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "dry_run": dry_run,
                "would_send": would_send,
                "status": status,
                "from": from_,
                "to": to,
                "cc": cc,
                "bcc": bcc,
                "thread_id": thread_id,
                "test": test,
                "approval": approval,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.send_check_approval_type_0 import SendCheckApprovalType0  # noqa: PLC0415

        d = dict(src_dict)
        dry_run = d.pop("dry_run")

        would_send = d.pop("would_send")

        status = SendCheckStatus(d.pop("status"))

        from_ = d.pop("from")

        to = cast(list[str], d.pop("to"))

        cc = cast(list[str], d.pop("cc"))

        bcc = cast(list[str], d.pop("bcc"))

        def _parse_thread_id(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        thread_id = _parse_thread_id(d.pop("thread_id"))

        test = d.pop("test")

        def _parse_approval(data: object) -> None | SendCheckApprovalType0:
            if data is None:
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                approval_type_0 = SendCheckApprovalType0.from_dict(data)

                return approval_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | SendCheckApprovalType0, data)

        approval = _parse_approval(d.pop("approval"))

        send_check = cls(
            dry_run=dry_run,
            would_send=would_send,
            status=status,
            from_=from_,
            to=to,
            cc=cc,
            bcc=bcc,
            thread_id=thread_id,
            test=test,
            approval=approval,
        )

        return send_check
