from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.pods_create_body_address import PodsCreateBodyAddress
    from ..models.pods_create_body_key import PodsCreateBodyKey


T = TypeVar("T", bound="PodsCreateBody")


@_attrs_define
class PodsCreateBody:
    """
    Attributes:
        name (str):
        client_id (None | str | Unset): Your own id for this pod. Carried and returned, never parsed.
        address (PodsCreateBodyAddress | Unset): An address to create in the new pod. The same fields as `POST
            /identities`.
        key (PodsCreateBodyKey | Unset): A key for the new pod, reaching its addresses and nothing else. Its token is in
            this response once; a replay returns the key with `token: null`.
    """

    name: str
    client_id: None | str | Unset = UNSET
    address: PodsCreateBodyAddress | Unset = UNSET
    key: PodsCreateBodyKey | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        name = self.name

        client_id: None | str | Unset
        if isinstance(self.client_id, Unset):
            client_id = UNSET
        else:
            client_id = self.client_id

        address: dict[str, Any] | Unset = UNSET
        if not isinstance(self.address, Unset):
            address = self.address.to_dict()

        key: dict[str, Any] | Unset = UNSET
        if not isinstance(self.key, Unset):
            key = self.key.to_dict()

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "name": name,
            }
        )
        if client_id is not UNSET:
            field_dict["client_id"] = client_id
        if address is not UNSET:
            field_dict["address"] = address
        if key is not UNSET:
            field_dict["key"] = key

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.pods_create_body_address import PodsCreateBodyAddress  # noqa: PLC0415
        from ..models.pods_create_body_key import PodsCreateBodyKey  # noqa: PLC0415

        d = dict(src_dict)
        name = d.pop("name")

        def _parse_client_id(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        client_id = _parse_client_id(d.pop("client_id", UNSET))

        _address = d.pop("address", UNSET)
        address: PodsCreateBodyAddress | Unset
        if isinstance(_address, Unset):
            address = UNSET
        else:
            address = PodsCreateBodyAddress.from_dict(_address)

        _key = d.pop("key", UNSET)
        key: PodsCreateBodyKey | Unset
        if isinstance(_key, Unset):
            key = UNSET
        else:
            key = PodsCreateBodyKey.from_dict(_key)

        pods_create_body = cls(
            name=name,
            client_id=client_id,
            address=address,
            key=key,
        )

        return pods_create_body
