from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, Literal, TypeVar, cast

from attrs import define as _attrs_define

from ..models.grant_status import GrantStatus
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.grant_grantor_type_0 import GrantGrantorType0
    from ..models.grant_grantor_type_1 import GrantGrantorType1
    from ..models.grant_scope import GrantScope
    from ..models.grant_subject import GrantSubject


T = TypeVar("T", bound="Grant")


@_attrs_define
class Grant:
    """
    Attributes:
        object_ (Literal['grant']):
        id (str):
        status (GrantStatus): `pending` until the grantor answers on the consent page.
        identity_id (None | str): The agent’s address, the card’s `sub`.
        agent (str):
        grantor (GrantGrantorType0 | GrantGrantorType1):
        scope (GrantScope):
        audience (None | str):
        subject (GrantSubject):
        expires_at (str): ISO-8601, UTC.
        created_at (str): ISO-8601, UTC.
        decided_at (None | str):
        revoked_at (None | str):
        jws (None | str): The signed grant (compact JWS, EdDSA, `typ: agent-grant+jwt`) while it is active: what the
            agent carries in `Post-Grant`.
        consent_url (str | Unset): Send the grantor here. Only on the answer that asked for it; it is not shown again.
    """

    object_: Literal["grant"]
    id: str
    status: GrantStatus
    identity_id: None | str
    agent: str
    grantor: GrantGrantorType0 | GrantGrantorType1
    scope: GrantScope
    audience: None | str
    subject: GrantSubject
    expires_at: str
    created_at: str
    decided_at: None | str
    revoked_at: None | str
    jws: None | str
    consent_url: str | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        from ..models.grant_grantor_type_0 import GrantGrantorType0  # noqa: PLC0415

        object_ = self.object_

        id = self.id

        status = self.status.value

        identity_id: None | str
        identity_id = self.identity_id

        agent = self.agent

        grantor: dict[str, Any]
        if isinstance(self.grantor, GrantGrantorType0):
            grantor = self.grantor.to_dict()
        else:
            grantor = self.grantor.to_dict()

        scope = self.scope.to_dict()

        audience: None | str
        audience = self.audience

        subject = self.subject.to_dict()

        expires_at = self.expires_at

        created_at = self.created_at

        decided_at: None | str
        decided_at = self.decided_at

        revoked_at: None | str
        revoked_at = self.revoked_at

        jws: None | str
        jws = self.jws

        consent_url = self.consent_url

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "object": object_,
                "id": id,
                "status": status,
                "identity_id": identity_id,
                "agent": agent,
                "grantor": grantor,
                "scope": scope,
                "audience": audience,
                "subject": subject,
                "expires_at": expires_at,
                "created_at": created_at,
                "decided_at": decided_at,
                "revoked_at": revoked_at,
                "jws": jws,
            }
        )
        if consent_url is not UNSET:
            field_dict["consent_url"] = consent_url

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.grant_grantor_type_0 import GrantGrantorType0  # noqa: PLC0415
        from ..models.grant_grantor_type_1 import GrantGrantorType1  # noqa: PLC0415
        from ..models.grant_scope import GrantScope  # noqa: PLC0415
        from ..models.grant_subject import GrantSubject  # noqa: PLC0415

        d = dict(src_dict)
        object_ = cast(Literal["grant"], d.pop("object"))
        if object_ != "grant":
            raise ValueError(f"object must match const 'grant', got '{object_}'")

        id = d.pop("id")

        status = GrantStatus(d.pop("status"))

        def _parse_identity_id(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        identity_id = _parse_identity_id(d.pop("identity_id"))

        agent = d.pop("agent")

        def _parse_grantor(data: object) -> GrantGrantorType0 | GrantGrantorType1:
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                grantor_type_0 = GrantGrantorType0.from_dict(data)

                return grantor_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            if not isinstance(data, dict):
                raise TypeError()
            grantor_type_1 = GrantGrantorType1.from_dict(data)

            return grantor_type_1

        grantor = _parse_grantor(d.pop("grantor"))

        scope = GrantScope.from_dict(d.pop("scope"))

        def _parse_audience(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        audience = _parse_audience(d.pop("audience"))

        subject = GrantSubject.from_dict(d.pop("subject"))

        expires_at = d.pop("expires_at")

        created_at = d.pop("created_at")

        def _parse_decided_at(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        decided_at = _parse_decided_at(d.pop("decided_at"))

        def _parse_revoked_at(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        revoked_at = _parse_revoked_at(d.pop("revoked_at"))

        def _parse_jws(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        jws = _parse_jws(d.pop("jws"))

        consent_url = d.pop("consent_url", UNSET)

        grant = cls(
            object_=object_,
            id=id,
            status=status,
            identity_id=identity_id,
            agent=agent,
            grantor=grantor,
            scope=scope,
            audience=audience,
            subject=subject,
            expires_at=expires_at,
            created_at=created_at,
            decided_at=decided_at,
            revoked_at=revoked_at,
            jws=jws,
            consent_url=consent_url,
        )

        return grant
