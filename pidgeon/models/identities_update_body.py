from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define

from ..models.identities_update_body_mode import IdentitiesUpdateBodyMode
from ..models.identities_update_body_send_policy import IdentitiesUpdateBodySendPolicy
from ..models.identities_update_body_status import IdentitiesUpdateBodyStatus
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.identities_update_body_capabilities import IdentitiesUpdateBodyCapabilities


T = TypeVar("T", bound="IdentitiesUpdateBody")


@_attrs_define
class IdentitiesUpdateBody:
    """
    Attributes:
        display_name (None | str | Unset): The name a recipient sees beside the address.
        mode (IdentitiesUpdateBodyMode | Unset): Who answers: a person, software, or both.
        capabilities (IdentitiesUpdateBodyCapabilities | Unset):
        status (IdentitiesUpdateBodyStatus | Unset):
        expires_at (datetime.datetime | None | Unset): When it stops accepting mail. Expiry suspends; it never deletes,
            so the correspondence survives.
        send_policy (IdentitiesUpdateBodySendPolicy | Unset): Who it may write to. `reply_only` makes an address
            structurally unable to start a conversation with a stranger.
        tenant_id (None | str | Unset): Your own opaque grouping — a customer id, whatever your side calls it. Never
            parsed here.
    """

    display_name: None | str | Unset = UNSET
    mode: IdentitiesUpdateBodyMode | Unset = UNSET
    capabilities: IdentitiesUpdateBodyCapabilities | Unset = UNSET
    status: IdentitiesUpdateBodyStatus | Unset = UNSET
    expires_at: datetime.datetime | None | Unset = UNSET
    send_policy: IdentitiesUpdateBodySendPolicy | Unset = UNSET
    tenant_id: None | str | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        display_name: None | str | Unset
        if isinstance(self.display_name, Unset):
            display_name = UNSET
        else:
            display_name = self.display_name

        mode: str | Unset = UNSET
        if not isinstance(self.mode, Unset):
            mode = self.mode.value

        capabilities: dict[str, Any] | Unset = UNSET
        if not isinstance(self.capabilities, Unset):
            capabilities = self.capabilities.to_dict()

        status: str | Unset = UNSET
        if not isinstance(self.status, Unset):
            status = self.status.value

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
        if display_name is not UNSET:
            field_dict["display_name"] = display_name
        if mode is not UNSET:
            field_dict["mode"] = mode
        if capabilities is not UNSET:
            field_dict["capabilities"] = capabilities
        if status is not UNSET:
            field_dict["status"] = status
        if expires_at is not UNSET:
            field_dict["expires_at"] = expires_at
        if send_policy is not UNSET:
            field_dict["send_policy"] = send_policy
        if tenant_id is not UNSET:
            field_dict["tenant_id"] = tenant_id

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.identities_update_body_capabilities import IdentitiesUpdateBodyCapabilities  # noqa: PLC0415

        d = dict(src_dict)

        def _parse_display_name(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        display_name = _parse_display_name(d.pop("display_name", UNSET))

        _mode = d.pop("mode", UNSET)
        mode: IdentitiesUpdateBodyMode | Unset
        if isinstance(_mode, Unset):
            mode = UNSET
        else:
            mode = IdentitiesUpdateBodyMode(_mode)

        _capabilities = d.pop("capabilities", UNSET)
        capabilities: IdentitiesUpdateBodyCapabilities | Unset
        if isinstance(_capabilities, Unset):
            capabilities = UNSET
        else:
            capabilities = IdentitiesUpdateBodyCapabilities.from_dict(_capabilities)

        _status = d.pop("status", UNSET)
        status: IdentitiesUpdateBodyStatus | Unset
        if isinstance(_status, Unset):
            status = UNSET
        else:
            status = IdentitiesUpdateBodyStatus(_status)

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
        send_policy: IdentitiesUpdateBodySendPolicy | Unset
        if isinstance(_send_policy, Unset):
            send_policy = UNSET
        else:
            send_policy = IdentitiesUpdateBodySendPolicy(_send_policy)

        def _parse_tenant_id(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        tenant_id = _parse_tenant_id(d.pop("tenant_id", UNSET))

        identities_update_body = cls(
            display_name=display_name,
            mode=mode,
            capabilities=capabilities,
            status=status,
            expires_at=expires_at,
            send_policy=send_policy,
            tenant_id=tenant_id,
        )

        return identities_update_body
