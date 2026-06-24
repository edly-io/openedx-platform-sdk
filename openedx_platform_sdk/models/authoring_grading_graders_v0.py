from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="AuthoringGradingGradersV0")


@_attrs_define
class AuthoringGradingGradersV0:
    """Serializer for graders

    Attributes:
        type_ (str):
        min_count (int):
        drop_count (int):
        weight (int):
        id (int):
        short_label (None | str | Unset):
    """

    type_: str
    min_count: int
    drop_count: int
    weight: int
    id: int
    short_label: None | str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        type_ = self.type_

        min_count = self.min_count

        drop_count = self.drop_count

        weight = self.weight

        id = self.id

        short_label: None | str | Unset
        if isinstance(self.short_label, Unset):
            short_label = UNSET
        else:
            short_label = self.short_label

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "type": type_,
                "min_count": min_count,
                "drop_count": drop_count,
                "weight": weight,
                "id": id,
            }
        )
        if short_label is not UNSET:
            field_dict["short_label"] = short_label

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        type_ = d.pop("type")

        min_count = d.pop("min_count")

        drop_count = d.pop("drop_count")

        weight = d.pop("weight")

        id = d.pop("id")

        def _parse_short_label(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        short_label = _parse_short_label(d.pop("short_label", UNSET))

        authoring_grading_graders_v0 = cls(
            type_=type_,
            min_count=min_count,
            drop_count=drop_count,
            weight=weight,
            id=id,
            short_label=short_label,
        )

        authoring_grading_graders_v0.additional_properties = d
        return authoring_grading_graders_v0

    @property
    def additional_keys(self) -> list[str]:
        return list(self.additional_properties.keys())

    def __getitem__(self, key: str) -> Any:
        return self.additional_properties[key]

    def __setitem__(self, key: str, value: Any) -> None:
        self.additional_properties[key] = value

    def __delitem__(self, key: str) -> None:
        del self.additional_properties[key]

    def __contains__(self, key: str) -> bool:
        return key in self.additional_properties
