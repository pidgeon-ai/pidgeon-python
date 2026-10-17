from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import Any, TypeVar, cast
from uuid import UUID

from attrs import define as _attrs_define

from ..models.identities_create_body_mode import IdentitiesCreateBodyMode
from ..models.identities_create_body_send_policy import IdentitiesCreateBodySendPolicy
from ..models.identities_create_body_type import IdentitiesCreateBodyType
from ..types import UNSET, Unset

T = TypeVar("T", bound="IdentitiesCreateBody")


@_attrs_define
class IdentitiesCreateBody:
    """
    Attributes:
        domain_id (UUID | Unset): From `GET /domains`, or the `domain_id` on any address you already have.
        domain (str | Unset): A domain name you own, or the shared one. An alternative to `domain_id`.
        address (str | Unset): A whole address — the local part and the domain in one. An alternative to the other two.
        local_part (str | Unset): Everything before the `@`.
        display_name (None | str | Unset): The name a recipient sees beside the address.
        inbox (bool | Unset): Whether it keeps mail. With an inbox what arrives is stored and a person can open it;
            without one it becomes an event and your webhook fires. Defaults from `type`.
        type_ (IdentitiesCreateBodyType | Unset): A label for what this address is for. It does not change what the
            address can do — that is `inbox`. Default: IdentitiesCreateBodyType.APPLICATION.
        mode (IdentitiesCreateBodyMode | Unset): Who answers: a person, software, or both.
        expires_at (datetime.datetime | None | Unset): When it stops accepting mail. Expiry suspends; it never deletes,
            so the correspondence survives.
        send_policy (IdentitiesCreateBodySendPolicy | Unset): Who it may write to. `reply_only` makes an address
            structurally unable to start a conversation with a stranger.
        tenant_id (None | str | Unset): Your own opaque grouping — a customer id, whatever your side calls it. Never
            parsed here.
        pod_id (None | Unset | UUID): The pod this belongs to — your account’s default when you name none. A pod is a
            sending boundary: mail from it lands on its own reputation, so one of your customers cannot damage another’s
            delivery. It does not change what an address can do, and no key is scoped to one.
    """

    domain_id: UUID | Unset = UNSET
    domain: str | Unset = UNSET
    address: str | Unset = UNSET
    local_part: str | Unset = UNSET
    display_name: None | str | Unset = UNSET
    inbox: bool | Unset = UNSET
    type_: IdentitiesCreateBodyType | Unset = IdentitiesCreateBodyType.APPLICATION
    mode: IdentitiesCreateBodyMode | Unset = UNSET
    expires_at: datetime.datetime | None | Unset = UNSET
    send_policy: IdentitiesCreateBodySendPolicy | Unset = UNSET
    tenant_id: None | str | Unset = UNSET
    pod_id: None | Unset | UUID = UNSET

    def to_dict(self) -> dict[str, Any]:
        domain_id: str | Unset = UNSET
        if not isinstance(self.domain_id, Unset):
            domain_id = str(self.domain_id)

        domain = self.domain

        address = self.address

        local_part = self.local_part

        display_name: None | str | Unset
        if isinstance(self.display_name, Unset):
            display_name = UNSET
        else:
            display_name = self.display_name

        inbox = self.inbox

        type_: str | Unset = UNSET
        if not isinstance(self.type_, Unset):
            type_ = self.type_.value

        mode: str | Unset = UNSET
        if not isinstance(self.mode, Unset):
            mode = self.mode.value

        expires_at: None | str | Unset
        if isinstance(self.expires_at, Unset):
            expires_at = UNSET
        elif isinstance(self.expires_at, datetime.datetime):
            expires_at = self.expires_at.isoformat()
        else:
            expires_at = self.expires_at

        send_policy: str | Unset = UNSET
        if not isinstance(self.send_policy, Unset):
            send_policy = self.send_policy.value

        tenant_id: None | str | Unset
        if isinstance(self.tenant_id, Unset):
            tenant_id = UNSET
        else:
            tenant_id = self.tenant_id

        pod_id: None | str | Unset
        if isinstance(self.pod_id, Unset):
            pod_id = UNSET
        elif isinstance(self.pod_id, UUID):
            pod_id = str(self.pod_id)
        else:
            pod_id = self.pod_id

        field_dict: dict[str, Any] = {}

        field_dict.update({})
        if domain_id is not UNSET:
            field_dict["domain_id"] = domain_id
        if domain is not UNSET:
            field_dict["domain"] = domain
        if address is not UNSET:
            field_dict["address"] = address
        if local_part is not UNSET:
            field_dict["local_part"] = local_part
        if display_name is not UNSET:
            field_dict["display_name"] = display_name
        if inbox is not UNSET:
            field_dict["inbox"] = inbox
        if type_ is not UNSET:
            field_dict["type"] = type_
        if mode is not UNSET:
            field_dict["mode"] = mode
        if expires_at is not UNSET:
            field_dict["expires_at"] = expires_at
        if send_policy is not UNSET:
            field_dict["send_policy"] = send_policy
        if tenant_id is not UNSET:
            field_dict["tenant_id"] = tenant_id
        if pod_id is not UNSET:
            field_dict["pod_id"] = pod_id

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        _domain_id = d.pop("domain_id", UNSET)
        domain_id: UUID | Unset
        if isinstance(_domain_id, Unset):
            domain_id = UNSET
        else:
            domain_id = UUID(_domain_id)

        domain = d.pop("domain", UNSET)

        address = d.pop("address", UNSET)

        local_part = d.pop("local_part", UNSET)

        def _parse_display_name(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        display_name = _parse_display_name(d.pop("display_name", UNSET))

        inbox = d.pop("inbox", UNSET)

        _type_ = d.pop("type", UNSET)
        type_: IdentitiesCreateBodyType | Unset
        if isinstance(_type_, Unset):
            type_ = UNSET
        else:
            type_ = IdentitiesCreateBodyType(_type_)

        _mode = d.pop("mode", UNSET)
        mode: IdentitiesCreateBodyMode | Unset
        if isinstance(_mode, Unset):
            mode = UNSET
        else:
            mode = IdentitiesCreateBodyMode(_mode)

        def _parse_expires_at(data: object) -> datetime.datetime | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                expires_at_type_0 = datetime.datetime.fromisoformat(data)

                return expires_at_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(datetime.datetime | None | Unset, data)

        expires_at = _parse_expires_at(d.pop("expires_at", UNSET))

        _send_policy = d.pop("send_policy", UNSET)
        send_policy: IdentitiesCreateBodySendPolicy | Unset
        if isinstance(_send_policy, Unset):
            send_policy = UNSET
        else:
            send_policy = IdentitiesCreateBodySendPolicy(_send_policy)

        def _parse_tenant_id(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        tenant_id = _parse_tenant_id(d.pop("tenant_id", UNSET))

        def _parse_pod_id(data: object) -> None | Unset | UUID:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                pod_id_type_0 = UUID(data)

                return pod_id_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | Unset | UUID, data)

        pod_id = _parse_pod_id(d.pop("pod_id", UNSET))

        identities_create_body = cls(
            domain_id=domain_id,
            domain=domain,
            address=address,
            local_part=local_part,
            display_name=display_name,
            inbox=inbox,
            type_=type_,
            mode=mode,
            expires_at=expires_at,
            send_policy=send_policy,
            tenant_id=tenant_id,
            pod_id=pod_id,
        )

        return identities_create_body
