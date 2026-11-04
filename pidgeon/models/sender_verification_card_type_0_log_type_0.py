from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define

T = TypeVar("T", bound="SenderVerificationCardType0LogType0")


@_attrs_define
class SenderVerificationCardType0LogType0:
    """
    Attributes:
        index (int): The entry’s index in the card log.
        tree_size (int): The size of the tree the proof is against.
        leaf_hash (str): SHA-256 of 0x00 and `data`, base64.
        proof (list[str]): The audit path, RFC 9162 §2.1.3, base64.
        data (str): The entry’s exact bytes: canonical JSON (RFC 8785).
        checkpoint (str): The signed tree head the proof is against: a C2SP checkpoint (signed note).
        verifier_key (str): The log’s key, `<origin>+<key id>+<base64 key>`, to check `checkpoint`.
    """

    index: int
    tree_size: int
    leaf_hash: str
    proof: list[str]
    data: str
    checkpoint: str
    verifier_key: str

    def to_dict(self) -> dict[str, Any]:
        index = self.index

        tree_size = self.tree_size

        leaf_hash = self.leaf_hash

        proof = self.proof

        data = self.data

        checkpoint = self.checkpoint

        verifier_key = self.verifier_key

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "index": index,
                "tree_size": tree_size,
                "leaf_hash": leaf_hash,
                "proof": proof,
                "data": data,
                "checkpoint": checkpoint,
                "verifier_key": verifier_key,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        index = d.pop("index")

        tree_size = d.pop("tree_size")

        leaf_hash = d.pop("leaf_hash")

        proof = cast(list[str], d.pop("proof"))

        data = d.pop("data")

        checkpoint = d.pop("checkpoint")

        verifier_key = d.pop("verifier_key")

        sender_verification_card_type_0_log_type_0 = cls(
            index=index,
            tree_size=tree_size,
            leaf_hash=leaf_hash,
            proof=proof,
            data=data,
            checkpoint=checkpoint,
            verifier_key=verifier_key,
        )

        return sender_verification_card_type_0_log_type_0
