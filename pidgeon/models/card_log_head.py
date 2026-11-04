from __future__ import annotations

from collections.abc import Mapping
from typing import Any, Literal, TypeVar, cast

from attrs import define as _attrs_define

T = TypeVar("T", bound="CardLogHead")


@_attrs_define
class CardLogHead:
    """
    Attributes:
        object_ (Literal['card_log_head']):
        origin (str): The log’s name: the checkpoint’s first line and its key’s name.
        size (int): How many entries the log has.
        root_hash (str): The RFC 9162 Merkle root at `size`, base64.
        checkpoint (str): The signed tree head, a C2SP checkpoint (signed note, Ed25519). The authority: the fields
            beside it are read from it.
        verifier_key (str): The log’s key as a signed-note verifier key, `<origin>+<key id>+<base64 key>`. Pin it.
        created_at (str): ISO-8601, UTC.
    """

    object_: Literal["card_log_head"]
    origin: str
    size: int
    root_hash: str
    checkpoint: str
    verifier_key: str
    created_at: str

    def to_dict(self) -> dict[str, Any]:
        object_ = self.object_

        origin = self.origin

        size = self.size

        root_hash = self.root_hash

        checkpoint = self.checkpoint

        verifier_key = self.verifier_key

        created_at = self.created_at

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "object": object_,
                "origin": origin,
                "size": size,
                "root_hash": root_hash,
                "checkpoint": checkpoint,
                "verifier_key": verifier_key,
                "created_at": created_at,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        object_ = cast(Literal["card_log_head"], d.pop("object"))
        if object_ != "card_log_head":
            raise ValueError(f"object must match const 'card_log_head', got '{object_}'")

        origin = d.pop("origin")

        size = d.pop("size")

        root_hash = d.pop("root_hash")

        checkpoint = d.pop("checkpoint")

        verifier_key = d.pop("verifier_key")

        created_at = d.pop("created_at")

        card_log_head = cls(
            object_=object_,
            origin=origin,
            size=size,
            root_hash=root_hash,
            checkpoint=checkpoint,
            verifier_key=verifier_key,
            created_at=created_at,
        )

        return card_log_head
