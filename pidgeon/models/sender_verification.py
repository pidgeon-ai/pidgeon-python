from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, Literal, TypeVar, cast

from attrs import define as _attrs_define

from ..models.sender_verification_body import SenderVerificationBody
from ..models.sender_verification_verdict import SenderVerificationVerdict

if TYPE_CHECKING:
    from ..models.sender_verification_card_type_0 import SenderVerificationCardType0
    from ..models.sender_verification_operator_type_0 import SenderVerificationOperatorType0
    from ..models.sender_verification_sender_type_0 import SenderVerificationSenderType0
    from ..models.sender_verification_signatures import SenderVerificationSignatures
    from ..models.sender_verification_warnings_item import SenderVerificationWarningsItem


T = TypeVar("T", bound="SenderVerification")


@_attrs_define
class SenderVerification:
    """
    Attributes:
        object_ (Literal['sender_verification']):
        verdict (SenderVerificationVerdict): `verified`: a signature holds and nothing is wrong. `caution`: it holds,
            with `warnings`. `failed`: a signature does not verify, or the body changed. `unsigned`: nothing to check.
        advice (str): One sentence to act on.
        sender (None | SenderVerificationSenderType0): Null unless a signature covers it.
        is_agent (bool | None):
        operator (None | SenderVerificationOperatorType0):
        ai_disclosure (None | str):
        signed_at (None | str):
        body (SenderVerificationBody):
        signatures (SenderVerificationSignatures):
        card (None | SenderVerificationCardType0): The sender’s agent card, when we issue it.
        warnings (list[SenderVerificationWarningsItem]):
    """

    object_: Literal["sender_verification"]
    verdict: SenderVerificationVerdict
    advice: str
    sender: None | SenderVerificationSenderType0
    is_agent: bool | None
    operator: None | SenderVerificationOperatorType0
    ai_disclosure: None | str
    signed_at: None | str
    body: SenderVerificationBody
    signatures: SenderVerificationSignatures
    card: None | SenderVerificationCardType0
    warnings: list[SenderVerificationWarningsItem]

    def to_dict(self) -> dict[str, Any]:
        from ..models.sender_verification_card_type_0 import SenderVerificationCardType0  # noqa: PLC0415
        from ..models.sender_verification_operator_type_0 import SenderVerificationOperatorType0  # noqa: PLC0415
        from ..models.sender_verification_sender_type_0 import SenderVerificationSenderType0  # noqa: PLC0415

        object_ = self.object_

        verdict = self.verdict.value

        advice = self.advice

        sender: dict[str, Any] | None
        if isinstance(self.sender, SenderVerificationSenderType0):
            sender = self.sender.to_dict()
        else:
            sender = self.sender

        is_agent: bool | None
        is_agent = self.is_agent

        operator: dict[str, Any] | None
        if isinstance(self.operator, SenderVerificationOperatorType0):
            operator = self.operator.to_dict()
        else:
            operator = self.operator

        ai_disclosure: None | str
        ai_disclosure = self.ai_disclosure

        signed_at: None | str
        signed_at = self.signed_at

        body = self.body.value

        signatures = self.signatures.to_dict()

        card: dict[str, Any] | None
        if isinstance(self.card, SenderVerificationCardType0):
            card = self.card.to_dict()
        else:
            card = self.card

        warnings = []
        for warnings_item_data in self.warnings:
            warnings_item = warnings_item_data.to_dict()
            warnings.append(warnings_item)

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "object": object_,
                "verdict": verdict,
                "advice": advice,
                "sender": sender,
                "is_agent": is_agent,
                "operator": operator,
                "ai_disclosure": ai_disclosure,
                "signed_at": signed_at,
                "body": body,
                "signatures": signatures,
                "card": card,
                "warnings": warnings,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.sender_verification_card_type_0 import SenderVerificationCardType0  # noqa: PLC0415
        from ..models.sender_verification_operator_type_0 import SenderVerificationOperatorType0  # noqa: PLC0415
        from ..models.sender_verification_sender_type_0 import SenderVerificationSenderType0  # noqa: PLC0415
        from ..models.sender_verification_signatures import SenderVerificationSignatures  # noqa: PLC0415
        from ..models.sender_verification_warnings_item import SenderVerificationWarningsItem  # noqa: PLC0415

        d = dict(src_dict)
        object_ = cast(Literal["sender_verification"], d.pop("object"))
        if object_ != "sender_verification":
            raise ValueError(f"object must match const 'sender_verification', got '{object_}'")

        verdict = SenderVerificationVerdict(d.pop("verdict"))

        advice = d.pop("advice")

        def _parse_sender(data: object) -> None | SenderVerificationSenderType0:
            if data is None:
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                sender_type_0 = SenderVerificationSenderType0.from_dict(data)

                return sender_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | SenderVerificationSenderType0, data)

        sender = _parse_sender(d.pop("sender"))

        def _parse_is_agent(data: object) -> bool | None:
            if data is None:
                return data
            return cast(bool | None, data)

        is_agent = _parse_is_agent(d.pop("is_agent"))

        def _parse_operator(data: object) -> None | SenderVerificationOperatorType0:
            if data is None:
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                operator_type_0 = SenderVerificationOperatorType0.from_dict(data)

                return operator_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | SenderVerificationOperatorType0, data)

        operator = _parse_operator(d.pop("operator"))

        def _parse_ai_disclosure(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        ai_disclosure = _parse_ai_disclosure(d.pop("ai_disclosure"))

        def _parse_signed_at(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        signed_at = _parse_signed_at(d.pop("signed_at"))

        body = SenderVerificationBody(d.pop("body"))

        signatures = SenderVerificationSignatures.from_dict(d.pop("signatures"))

        def _parse_card(data: object) -> None | SenderVerificationCardType0:
            if data is None:
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                card_type_0 = SenderVerificationCardType0.from_dict(data)

                return card_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | SenderVerificationCardType0, data)

        card = _parse_card(d.pop("card"))

        warnings = []
        _warnings = d.pop("warnings")
        for warnings_item_data in _warnings:
            warnings_item = SenderVerificationWarningsItem.from_dict(warnings_item_data)

            warnings.append(warnings_item)

        sender_verification = cls(
            object_=object_,
            verdict=verdict,
            advice=advice,
            sender=sender,
            is_agent=is_agent,
            operator=operator,
            ai_disclosure=ai_disclosure,
            signed_at=signed_at,
            body=body,
            signatures=signatures,
            card=card,
            warnings=warnings,
        )

        return sender_verification
