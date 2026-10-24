from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define

if TYPE_CHECKING:
    from ..models.pod_created_address_type_0 import PodCreatedAddressType0
    from ..models.pod_created_key_type_0 import PodCreatedKeyType0


T = TypeVar("T", bound="PodCreated")


@_attrs_define
class PodCreated:
    """
    Attributes:
        id (str):
        name (str):
        client_id (None | str): Your own id for this pod — a customer id, whatever your side calls it.
        is_default (bool): Where an address lands when a create call names no pod. Exactly one per account.
        identity_count (int): Addresses in it.
        created_at (str): ISO-8601, UTC.
        address (None | PodCreatedAddressType0): The address created in the pod, or null when the call asked for none.
        key (None | PodCreatedKeyType0): A pod key for it, or null when the call asked for none.
    """

    id: str
    name: str
    client_id: None | str
    is_default: bool
    identity_count: int
    created_at: str
    address: None | PodCreatedAddressType0
    key: None | PodCreatedKeyType0

    def to_dict(self) -> dict[str, Any]:
        from ..models.pod_created_address_type_0 import PodCreatedAddressType0  # noqa: PLC0415
        from ..models.pod_created_key_type_0 import PodCreatedKeyType0  # noqa: PLC0415

        id = self.id

        name = self.name

        client_id: None | str
        client_id = self.client_id

        is_default = self.is_default

        identity_count = self.identity_count

        created_at = self.created_at

        address: dict[str, Any] | None
        if isinstance(self.address, PodCreatedAddressType0):
            address = self.address.to_dict()
        else:
            address = self.address

        key: dict[str, Any] | None
        if isinstance(self.key, PodCreatedKeyType0):
            key = self.key.to_dict()
        else:
            key = self.key

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "id": id,
                "name": name,
                "client_id": client_id,
                "is_default": is_default,
                "identity_count": identity_count,
                "created_at": created_at,
                "address": address,
                "key": key,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.pod_created_address_type_0 import PodCreatedAddressType0  # noqa: PLC0415
        from ..models.pod_created_key_type_0 import PodCreatedKeyType0  # noqa: PLC0415

        d = dict(src_dict)
        id = d.pop("id")

        name = d.pop("name")

        def _parse_client_id(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        client_id = _parse_client_id(d.pop("client_id"))

        is_default = d.pop("is_default")

        identity_count = d.pop("identity_count")

        created_at = d.pop("created_at")

        def _parse_address(data: object) -> None | PodCreatedAddressType0:
            if data is None:
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                address_type_0 = PodCreatedAddressType0.from_dict(data)

                return address_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | PodCreatedAddressType0, data)

        address = _parse_address(d.pop("address"))

        def _parse_key(data: object) -> None | PodCreatedKeyType0:
            if data is None:
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                key_type_0 = PodCreatedKeyType0.from_dict(data)

                return key_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | PodCreatedKeyType0, data)

        key = _parse_key(d.pop("key"))

        pod_created = cls(
            id=id,
            name=name,
            client_id=client_id,
            is_default=is_default,
            identity_count=identity_count,
            created_at=created_at,
            address=address,
            key=key,
        )

        return pod_created
