from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar
from uuid import UUID

from attrs import define as _attrs_define

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.grants_create_body_grantor_type_0 import GrantsCreateBodyGrantorType0
    from ..models.grants_create_body_grantor_type_1 import GrantsCreateBodyGrantorType1


T = TypeVar("T", bound="GrantsCreateBody")


@_attrs_define
class GrantsCreateBody:
    """
    Attributes:
        identity_id (UUID): The agent’s address.
        template (str): A template’s `name` or `id`.
        grantor (GrantsCreateBodyGrantorType0 | GrantsCreateBodyGrantorType1): `{ email }` asks that person on a consent
            page, and the answer carries `consent_url` to send them to. `{ organisation: true }` grants at once as this
            account’s verified domain, and needs a key with admin on the account.
        subject_id (str): The customer, account or order it is for, in the recipient’s own terms.
        expires_at (datetime.datetime | Unset): When it ends. The template’s `max_days` from now when omitted, and at
            most that.
    """

    identity_id: UUID
    template: str
    grantor: GrantsCreateBodyGrantorType0 | GrantsCreateBodyGrantorType1
    subject_id: str
    expires_at: datetime.datetime | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        from ..models.grants_create_body_grantor_type_0 import GrantsCreateBodyGrantorType0  # noqa: PLC0415

        identity_id = str(self.identity_id)

        template = self.template

        grantor: dict[str, Any]
        if isinstance(self.grantor, GrantsCreateBodyGrantorType0):
            grantor = self.grantor.to_dict()
        else:
            grantor = self.grantor.to_dict()

        subject_id = self.subject_id

        expires_at: str | Unset = UNSET
        if not isinstance(self.expires_at, Unset):
            expires_at = self.expires_at.isoformat()

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "identity_id": identity_id,
                "template": template,
                "grantor": grantor,
                "subject_id": subject_id,
            }
        )
        if expires_at is not UNSET:
            field_dict["expires_at"] = expires_at

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.grants_create_body_grantor_type_0 import GrantsCreateBodyGrantorType0  # noqa: PLC0415
        from ..models.grants_create_body_grantor_type_1 import GrantsCreateBodyGrantorType1  # noqa: PLC0415

        d = dict(src_dict)
        identity_id = UUID(d.pop("identity_id"))

        template = d.pop("template")

        def _parse_grantor(data: object) -> GrantsCreateBodyGrantorType0 | GrantsCreateBodyGrantorType1:
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                grantor_type_0 = GrantsCreateBodyGrantorType0.from_dict(data)

                return grantor_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            if not isinstance(data, dict):
                raise TypeError()
            grantor_type_1 = GrantsCreateBodyGrantorType1.from_dict(data)

            return grantor_type_1

        grantor = _parse_grantor(d.pop("grantor"))

        subject_id = d.pop("subject_id")

        _expires_at = d.pop("expires_at", UNSET)
        expires_at: datetime.datetime | Unset
        if isinstance(_expires_at, Unset):
            expires_at = UNSET
        else:
            expires_at = datetime.datetime.fromisoformat(_expires_at)

        grants_create_body = cls(
            identity_id=identity_id,
            template=template,
            grantor=grantor,
            subject_id=subject_id,
            expires_at=expires_at,
        )

        return grants_create_body
