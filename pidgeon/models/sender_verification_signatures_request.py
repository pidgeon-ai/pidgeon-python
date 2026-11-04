from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define

from ..models.sender_verification_signatures_request_result import SenderVerificationSignaturesRequestResult

T = TypeVar("T", bound="SenderVerificationSignaturesRequest")


@_attrs_define
class SenderVerificationSignaturesRequest:
    """An HTTP request’s signature (RFC 9421, Web Bot Auth), when `request` was sent. `none` for a message.

    Attributes:
        result (SenderVerificationSignaturesRequestResult):
        domain (None | str):
        keyid (None | str):
        reason (None | str):
    """

    result: SenderVerificationSignaturesRequestResult
    domain: None | str
    keyid: None | str
    reason: None | str

    def to_dict(self) -> dict[str, Any]:
        result = self.result.value

        domain: None | str
        domain = self.domain

        keyid: None | str
        keyid = self.keyid

        reason: None | str
        reason = self.reason

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "result": result,
                "domain": domain,
                "keyid": keyid,
                "reason": reason,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        result = SenderVerificationSignaturesRequestResult(d.pop("result"))

        def _parse_domain(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        domain = _parse_domain(d.pop("domain"))

        def _parse_keyid(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        keyid = _parse_keyid(d.pop("keyid"))

        def _parse_reason(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        reason = _parse_reason(d.pop("reason"))

        sender_verification_signatures_request = cls(
            result=result,
            domain=domain,
            keyid=keyid,
            reason=reason,
        )

        return sender_verification_signatures_request
