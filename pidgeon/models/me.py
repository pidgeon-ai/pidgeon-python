from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, Literal, TypeVar, cast

from attrs import define as _attrs_define

if TYPE_CHECKING:
    from ..models.me_key_type_0 import MeKeyType0
    from ..models.me_workspace import MeWorkspace


T = TypeVar("T", bound="Me")


@_attrs_define
class Me:
    """
    Attributes:
        kind (Literal['key']): What is calling. Only API keys reach this API.
        key (MeKeyType0 | None): Null only if the key was deleted between authenticating and this read.
        workspace (MeWorkspace):
        reaches (int): How many addresses this key can read. `GET /identities` lists them; this is the count, which is
            what tells a key that reaches nothing apart from one that is misconfigured.
    """

    kind: Literal["key"]
    key: MeKeyType0 | None
    workspace: MeWorkspace
    reaches: int

    def to_dict(self) -> dict[str, Any]:
        from ..models.me_key_type_0 import MeKeyType0  # noqa: PLC0415

        kind = self.kind

        key: dict[str, Any] | None
        if isinstance(self.key, MeKeyType0):
            key = self.key.to_dict()
        else:
            key = self.key

        workspace = self.workspace.to_dict()

        reaches = self.reaches

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "kind": kind,
                "key": key,
                "workspace": workspace,
                "reaches": reaches,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.me_key_type_0 import MeKeyType0  # noqa: PLC0415
        from ..models.me_workspace import MeWorkspace  # noqa: PLC0415

        d = dict(src_dict)
        kind = cast(Literal["key"], d.pop("kind"))
        if kind != "key":
            raise ValueError(f"kind must match const 'key', got '{kind}'")

        def _parse_key(data: object) -> MeKeyType0 | None:
            if data is None:
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                key_type_0 = MeKeyType0.from_dict(data)

                return key_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(MeKeyType0 | None, data)

        key = _parse_key(d.pop("key"))

        workspace = MeWorkspace.from_dict(d.pop("workspace"))

        reaches = d.pop("reaches")

        me = cls(
            kind=kind,
            key=key,
            workspace=workspace,
            reaches=reaches,
        )

        return me
