from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="InstructorInfo")


@_attrs_define
class InstructorInfo:
    """Serializer for instructor info

    Attributes:
        title (str):
        name (str | Unset):
        organization (str | Unset):
        image (str | Unset):
        bio (str | Unset):
    """

    title: str
    name: str | Unset = UNSET
    organization: str | Unset = UNSET
    image: str | Unset = UNSET
    bio: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        title = self.title

        name = self.name

        organization = self.organization

        image = self.image

        bio = self.bio

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "title": title,
            }
        )
        if name is not UNSET:
            field_dict["name"] = name
        if organization is not UNSET:
            field_dict["organization"] = organization
        if image is not UNSET:
            field_dict["image"] = image
        if bio is not UNSET:
            field_dict["bio"] = bio

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        title = d.pop("title")

        name = d.pop("name", UNSET)

        organization = d.pop("organization", UNSET)

        image = d.pop("image", UNSET)

        bio = d.pop("bio", UNSET)

        instructor_info = cls(
            title=title,
            name=name,
            organization=organization,
            image=image,
            bio=bio,
        )

        instructor_info.additional_properties = d
        return instructor_info

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
