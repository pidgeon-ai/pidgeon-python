from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define

if TYPE_CHECKING:
    from ..models.sender_verification_card_type_0_log_type_0 import SenderVerificationCardType0LogType0


T = TypeVar("T", bound="SenderVerificationCardType0")


@_attrs_define
class SenderVerificationCardType0:
    """
    Attributes:
        url (str):
        standing (str):
        since (str):
        log (None | SenderVerificationCardType0LogType0): The card’s latest entry in the public card log and its
            inclusion proof. Null until the log’s next pass (at most five minutes) has seen it.
    """

    url: str
    standing: str
    since: str
    log: None | SenderVerificationCardType0LogType0

    def to_dict(self) -> dict[str, Any]:
        from ..models.sender_verification_card_type_0_log_type_0 import SenderVerificationCardType0LogType0  # noqa: PLC0415

        url = self.url

        standing = self.standing

        since = self.since

        log: dict[str, Any] | None
        if isinstance(self.log, SenderVerificationCardType0LogType0):
            log = self.log.to_dict()
        else:
            log = self.log

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "url": url,
                "standing": standing,
                "since": since,
                "log": log,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.sender_verification_card_type_0_log_type_0 import SenderVerificationCardType0LogType0  # noqa: PLC0415

        d = dict(src_dict)
        url = d.pop("url")

        standing = d.pop("standing")

        since = d.pop("since")

        def _parse_log(data: object) -> None | SenderVerificationCardType0LogType0:
            if data is None:
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                log_type_0 = SenderVerificationCardType0LogType0.from_dict(data)

                return log_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | SenderVerificationCardType0LogType0, data)

        log = _parse_log(d.pop("log"))

        sender_verification_card_type_0 = cls(
            url=url,
            standing=standing,
            since=since,
            log=log,
        )

        return sender_verification_card_type_0
