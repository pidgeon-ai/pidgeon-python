from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define

if TYPE_CHECKING:
    from ..models.identity_capabilities import IdentityCapabilities


T = TypeVar("T", bound="Identity")


@_attrs_define
class Identity:
    """
    Attributes:
        id (str):
        email (str):
        local_part (str):
        domain (str):
        domain_id (str): Pass this to POST /identities to add another address here.
        display_name (None | str):
        type_ (str): human, team, application, workflow or agent.
        mode (str): Who answers: human, automated or hybrid.
        status (str):
        capabilities (IdentityCapabilities):
        has_inbox (bool): False for an address that turns mail into events and stores nothing.
        routed_address_count (int):
        created_at (str): ISO-8601, UTC.
        expires_at (None | str): When it stops accepting mail. Expiry suspends the address; it never deletes it.
        send_policy (str): Who it may write to: open, reply_only (somebody who wrote to it first), or list.
        receive_policy (str): Who may write to it: open, or list (only senders with an inbox rule, on mail that passes
            DMARC).
        tenant_id (None | str): Your own opaque grouping for this address. Never parsed here.
        pod_id (str): The pod this address is in. Every workspace has one to start with and every address is in one, so
            this is never null.
    """

    id: str
    email: str
    local_part: str
    domain: str
    domain_id: str
    display_name: None | str
    type_: str
    mode: str
    status: str
    capabilities: IdentityCapabilities
    has_inbox: bool
    routed_address_count: int
    created_at: str
    expires_at: None | str
    send_policy: str
    receive_policy: str
    tenant_id: None | str
    pod_id: str

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        email = self.email

        local_part = self.local_part

        domain = self.domain

        domain_id = self.domain_id

        display_name: None | str
        display_name = self.display_name

        type_ = self.type_

        mode = self.mode

        status = self.status

        capabilities = self.capabilities.to_dict()

        has_inbox = self.has_inbox

        routed_address_count = self.routed_address_count

        created_at = self.created_at

        expires_at: None | str
        expires_at = self.expires_at

        send_policy = self.send_policy

        receive_policy = self.receive_policy

        tenant_id: None | str
        tenant_id = self.tenant_id

        pod_id = self.pod_id

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "id": id,
                "email": email,
                "local_part": local_part,
                "domain": domain,
                "domain_id": domain_id,
                "display_name": display_name,
                "type": type_,
                "mode": mode,
                "status": status,
                "capabilities": capabilities,
                "has_inbox": has_inbox,
                "routed_address_count": routed_address_count,
                "created_at": created_at,
                "expires_at": expires_at,
                "send_policy": send_policy,
                "receive_policy": receive_policy,
                "tenant_id": tenant_id,
                "pod_id": pod_id,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.identity_capabilities import IdentityCapabilities  # noqa: PLC0415

        d = dict(src_dict)
        id = d.pop("id")

        email = d.pop("email")

        local_part = d.pop("local_part")

        domain = d.pop("domain")

        domain_id = d.pop("domain_id")

        def _parse_display_name(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        display_name = _parse_display_name(d.pop("display_name"))

        type_ = d.pop("type")

        mode = d.pop("mode")

        status = d.pop("status")

        capabilities = IdentityCapabilities.from_dict(d.pop("capabilities"))

        has_inbox = d.pop("has_inbox")

        routed_address_count = d.pop("routed_address_count")

        created_at = d.pop("created_at")

        def _parse_expires_at(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        expires_at = _parse_expires_at(d.pop("expires_at"))

        send_policy = d.pop("send_policy")

        receive_policy = d.pop("receive_policy")

        def _parse_tenant_id(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        tenant_id = _parse_tenant_id(d.pop("tenant_id"))

        pod_id = d.pop("pod_id")

        identity = cls(
            id=id,
            email=email,
            local_part=local_part,
            domain=domain,
            domain_id=domain_id,
            display_name=display_name,
            type_=type_,
            mode=mode,
            status=status,
            capabilities=capabilities,
            has_inbox=has_inbox,
            routed_address_count=routed_address_count,
            created_at=created_at,
            expires_at=expires_at,
            send_policy=send_policy,
            receive_policy=receive_policy,
            tenant_id=tenant_id,
            pod_id=pod_id,
        )

        return identity
