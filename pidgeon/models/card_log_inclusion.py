from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, Literal, TypeVar, cast

from attrs import define as _attrs_define

if TYPE_CHECKING:
    from ..models.card_log_inclusion_entry import CardLogInclusionEntry
    from ..models.card_log_inclusion_head import CardLogInclusionHead


T = TypeVar("T", bound="CardLogInclusion")


@_attrs_define
class CardLogInclusion:
    """
    Attributes:
        object_ (Literal['card_log_inclusion']):
        index (int):
        tree_size (int):
        leaf_hash (str):
        proof (list[str]): The audit path, RFC 9162 §2.1.3, base64.
        entry (CardLogInclusionEntry):
        head (CardLogInclusionHead): The signed head at `tree_size`.
    """

    object_: Literal["card_log_inclusion"]
    index: int
    tree_size: int
    leaf_hash: str
    proof: list[str]
    entry: CardLogInclusionEntry
    head: CardLogInclusionHead

    def to_dict(self) -> dict[str, Any]:
        object_ = self.object_

        index = self.index

        tree_size = self.tree_size

        leaf_hash = self.leaf_hash

        proof = self.proof

        entry = self.entry.to_dict()

        head = self.head.to_dict()

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "object": object_,
                "index": index,
                "tree_size": tree_size,
                "leaf_hash": leaf_hash,
                "proof": proof,
                "entry": entry,
                "head": head,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.card_log_inclusion_entry import CardLogInclusionEntry  # noqa: PLC0415
        from ..models.card_log_inclusion_head import CardLogInclusionHead  # noqa: PLC0415

        d = dict(src_dict)
        object_ = cast(Literal["card_log_inclusion"], d.pop("object"))
        if object_ != "card_log_inclusion":
            raise ValueError(f"object must match const 'card_log_inclusion', got '{object_}'")

        index = d.pop("index")

        tree_size = d.pop("tree_size")

        leaf_hash = d.pop("leaf_hash")

        proof = cast(list[str], d.pop("proof"))

        entry = CardLogInclusionEntry.from_dict(d.pop("entry"))

        head = CardLogInclusionHead.from_dict(d.pop("head"))

        card_log_inclusion = cls(
            object_=object_,
            index=index,
            tree_size=tree_size,
            leaf_hash=leaf_hash,
            proof=proof,
            entry=entry,
            head=head,
        )

        return card_log_inclusion
