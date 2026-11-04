from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define

from ..models.sender_verification_grants_item_reason_type_0 import SenderVerificationGrantsItemReasonType0

if TYPE_CHECKING:
    from ..models.sender_verification_grants_item_grantor_type_0_type_0 import (
        SenderVerificationGrantsItemGrantorType0Type0,
    )
    from ..models.sender_verification_grants_item_grantor_type_0_type_1 import (
        SenderVerificationGrantsItemGrantorType0Type1,
    )
    from ..models.sender_verification_grants_item_scope_type_0 import SenderVerificationGrantsItemScopeType0
    from ..models.sender_verification_grants_item_subject_type_0 import SenderVerificationGrantsItemSubjectType0


T = TypeVar("T", bound="SenderVerificationGrantsItem")


@_attrs_define
class SenderVerificationGrantsItem:
    """
    Attributes:
        valid (bool): True when the grant is ours, signed, in force, held by the sender a signature verified, and for
            here and this subject.
        reason (None | SenderVerificationGrantsItemReasonType0): Why it does not hold: the first thing wrong. Null when
            `valid`.
        id (None | str): Null unless the signature holds.
        agent (None | str):
        grantor (None | SenderVerificationGrantsItemGrantorType0Type0 | SenderVerificationGrantsItemGrantorType0Type1):
        scope (None | SenderVerificationGrantsItemScopeType0):
        audience (None | str): The domain it is for acting with. Null: anywhere.
        subject (None | SenderVerificationGrantsItemSubjectType0):
        expires_at (None | str):
    """

    valid: bool
    reason: None | SenderVerificationGrantsItemReasonType0
    id: None | str
    agent: None | str
    grantor: None | SenderVerificationGrantsItemGrantorType0Type0 | SenderVerificationGrantsItemGrantorType0Type1
    scope: None | SenderVerificationGrantsItemScopeType0
    audience: None | str
    subject: None | SenderVerificationGrantsItemSubjectType0
    expires_at: None | str

    def to_dict(self) -> dict[str, Any]:
        from ..models.sender_verification_grants_item_grantor_type_0_type_0 import (
            SenderVerificationGrantsItemGrantorType0Type0,  # noqa: PLC0415
        )
        from ..models.sender_verification_grants_item_grantor_type_0_type_1 import (
            SenderVerificationGrantsItemGrantorType0Type1,  # noqa: PLC0415
        )
        from ..models.sender_verification_grants_item_scope_type_0 import SenderVerificationGrantsItemScopeType0  # noqa: PLC0415
        from ..models.sender_verification_grants_item_subject_type_0 import SenderVerificationGrantsItemSubjectType0  # noqa: PLC0415

        valid = self.valid

        reason: None | str
        if isinstance(self.reason, SenderVerificationGrantsItemReasonType0):
            reason = self.reason.value
        else:
            reason = self.reason

        id: None | str
        id = self.id

        agent: None | str
        agent = self.agent

        grantor: dict[str, Any] | None
        if isinstance(self.grantor, SenderVerificationGrantsItemGrantorType0Type0):
            grantor = self.grantor.to_dict()
        elif isinstance(self.grantor, SenderVerificationGrantsItemGrantorType0Type1):
            grantor = self.grantor.to_dict()
        else:
            grantor = self.grantor

        scope: dict[str, Any] | None
        if isinstance(self.scope, SenderVerificationGrantsItemScopeType0):
            scope = self.scope.to_dict()
        else:
            scope = self.scope

        audience: None | str
        audience = self.audience

        subject: dict[str, Any] | None
        if isinstance(self.subject, SenderVerificationGrantsItemSubjectType0):
            subject = self.subject.to_dict()
        else:
            subject = self.subject

        expires_at: None | str
        expires_at = self.expires_at

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "valid": valid,
                "reason": reason,
                "id": id,
                "agent": agent,
                "grantor": grantor,
                "scope": scope,
                "audience": audience,
                "subject": subject,
                "expires_at": expires_at,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.sender_verification_grants_item_grantor_type_0_type_0 import (
            SenderVerificationGrantsItemGrantorType0Type0,  # noqa: PLC0415
        )
        from ..models.sender_verification_grants_item_grantor_type_0_type_1 import (
            SenderVerificationGrantsItemGrantorType0Type1,  # noqa: PLC0415
        )
        from ..models.sender_verification_grants_item_scope_type_0 import SenderVerificationGrantsItemScopeType0  # noqa: PLC0415
        from ..models.sender_verification_grants_item_subject_type_0 import SenderVerificationGrantsItemSubjectType0  # noqa: PLC0415

        d = dict(src_dict)
        valid = d.pop("valid")

        def _parse_reason(data: object) -> None | SenderVerificationGrantsItemReasonType0:
            if data is None:
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                reason_type_0 = SenderVerificationGrantsItemReasonType0(data)

                return reason_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | SenderVerificationGrantsItemReasonType0, data)

        reason = _parse_reason(d.pop("reason"))

        def _parse_id(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        id = _parse_id(d.pop("id"))

        def _parse_agent(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        agent = _parse_agent(d.pop("agent"))

        def _parse_grantor(
            data: object,
        ) -> None | SenderVerificationGrantsItemGrantorType0Type0 | SenderVerificationGrantsItemGrantorType0Type1:
            if data is None:
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                grantor_type_0_type_0 = SenderVerificationGrantsItemGrantorType0Type0.from_dict(data)

                return grantor_type_0_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                grantor_type_0_type_1 = SenderVerificationGrantsItemGrantorType0Type1.from_dict(data)

                return grantor_type_0_type_1
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(
                None | SenderVerificationGrantsItemGrantorType0Type0 | SenderVerificationGrantsItemGrantorType0Type1,
                data,
            )

        grantor = _parse_grantor(d.pop("grantor"))

        def _parse_scope(data: object) -> None | SenderVerificationGrantsItemScopeType0:
            if data is None:
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                scope_type_0 = SenderVerificationGrantsItemScopeType0.from_dict(data)

                return scope_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | SenderVerificationGrantsItemScopeType0, data)

        scope = _parse_scope(d.pop("scope"))

        def _parse_audience(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        audience = _parse_audience(d.pop("audience"))

        def _parse_subject(data: object) -> None | SenderVerificationGrantsItemSubjectType0:
            if data is None:
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                subject_type_0 = SenderVerificationGrantsItemSubjectType0.from_dict(data)

                return subject_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | SenderVerificationGrantsItemSubjectType0, data)

        subject = _parse_subject(d.pop("subject"))

        def _parse_expires_at(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        expires_at = _parse_expires_at(d.pop("expires_at"))

        sender_verification_grants_item = cls(
            valid=valid,
            reason=reason,
            id=id,
            agent=agent,
            grantor=grantor,
            scope=scope,
            audience=audience,
            subject=subject,
            expires_at=expires_at,
        )

        return sender_verification_grants_item
