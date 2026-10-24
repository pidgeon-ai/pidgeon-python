from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import Any, TypeVar, cast
from uuid import UUID

from attrs import define as _attrs_define

from ..models.pods_create_body_address_mode import PodsCreateBodyAddressMode
from ..models.pods_create_body_address_send_policy import PodsCreateBodyAddressSendPolicy
from ..models.pods_create_body_address_type import PodsCreateBodyAddressType
from ..types import UNSET, Unset

T = TypeVar("T", bound="PodsCreateBodyAddress")


@_attrs_define
class PodsCreateBodyAddress:
    """An address to create in the new pod. The same fields as `POST /identities`.

    Attributes:
        domain_id (UUID | Unset):
        domain (str | Unset):
        address (str | Unset):
        local_part (str | Unset):
        display_name (None | str | Unset):
        inbox (bool | Unset):
        type_ (PodsCreateBodyAddressType | Unset):  Default: PodsCreateBodyAddressType.APPLICATION.
        mode (PodsCreateBodyAddressMode | Unset):
        expires_at (datetime.datetime | None | Unset):
        send_policy (PodsCreateBodyAddressSendPolicy | Unset):
        tenant_id (None | str | Unset):
    """

    domain_id: UUID | Unset = UNSET
    domain: str | Unset = UNSET
    address: str | Unset = UNSET
    local_part: str | Unset = UNSET
    display_name: None | str | Unset = UNSET
    inbox: bool | Unset = UNSET
    type_: PodsCreateBodyAddressType | Unset = PodsCreateBodyAddressType.APPLICATION
    mode: PodsCreateBodyAddressMode | Unset = UNSET
    expires_at: datetime.datetime | None | Unset = UNSET
    send_policy: PodsCreateBodyAddressSendPolicy | Unset = UNSET
    tenant_id: None | str | Unset = UNSET

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
        type_: PodsCreateBodyAddressType | Unset
        if isinstance(_type_, Unset):
            type_ = UNSET
        else:
            type_ = PodsCreateBodyAddressType(_type_)

        _mode = d.pop("mode", UNSET)
        mode: PodsCreateBodyAddressMode | Unset
        if isinstance(_mode, Unset):
            mode = UNSET
        else:
            mode = PodsCreateBodyAddressMode(_mode)

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
        send_policy: PodsCreateBodyAddressSendPolicy | Unset
        if isinstance(_send_policy, Unset):
            send_policy = UNSET
        else:
            send_policy = PodsCreateBodyAddressSendPolicy(_send_policy)

        def _parse_tenant_id(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        tenant_id = _parse_tenant_id(d.pop("tenant_id", UNSET))

        pods_create_body_address = cls(
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
        )

        return pods_create_body_address
