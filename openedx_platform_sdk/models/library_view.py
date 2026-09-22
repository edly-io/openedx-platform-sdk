from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="LibraryView")


@_attrs_define
class LibraryView:
    """Serializer for library view

    Attributes:
        display_name (str):
        library_key (str):
        url (str):
        org (str):
        number (str):
        can_edit (bool):
        is_migrated (bool):
        migrated_to_title (str | Unset):
        migrated_to_key (str | Unset):
        migrated_to_collection_key (str | Unset):
        migrated_to_collection_title (str | Unset):
    """

    display_name: str
    library_key: str
    url: str
    org: str
    number: str
    can_edit: bool
    is_migrated: bool
    migrated_to_title: str | Unset = UNSET
    migrated_to_key: str | Unset = UNSET
    migrated_to_collection_key: str | Unset = UNSET
    migrated_to_collection_title: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        display_name = self.display_name

        library_key = self.library_key

        url = self.url

        org = self.org

        number = self.number

        can_edit = self.can_edit

        is_migrated = self.is_migrated

        migrated_to_title = self.migrated_to_title

        migrated_to_key = self.migrated_to_key

        migrated_to_collection_key = self.migrated_to_collection_key

        migrated_to_collection_title = self.migrated_to_collection_title

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "display_name": display_name,
                "library_key": library_key,
                "url": url,
                "org": org,
                "number": number,
                "can_edit": can_edit,
                "is_migrated": is_migrated,
            }
        )
        if migrated_to_title is not UNSET:
            field_dict["migrated_to_title"] = migrated_to_title
        if migrated_to_key is not UNSET:
            field_dict["migrated_to_key"] = migrated_to_key
        if migrated_to_collection_key is not UNSET:
            field_dict["migrated_to_collection_key"] = migrated_to_collection_key
        if migrated_to_collection_title is not UNSET:
            field_dict["migrated_to_collection_title"] = migrated_to_collection_title

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        display_name = d.pop("display_name")

        library_key = d.pop("library_key")

        url = d.pop("url")

        org = d.pop("org")

        number = d.pop("number")

        can_edit = d.pop("can_edit")

        is_migrated = d.pop("is_migrated")

        migrated_to_title = d.pop("migrated_to_title", UNSET)

        migrated_to_key = d.pop("migrated_to_key", UNSET)

        migrated_to_collection_key = d.pop("migrated_to_collection_key", UNSET)

        migrated_to_collection_title = d.pop("migrated_to_collection_title", UNSET)

        library_view = cls(
            display_name=display_name,
            library_key=library_key,
            url=url,
            org=org,
            number=number,
            can_edit=can_edit,
            is_migrated=is_migrated,
            migrated_to_title=migrated_to_title,
            migrated_to_key=migrated_to_key,
            migrated_to_collection_key=migrated_to_collection_key,
            migrated_to_collection_title=migrated_to_collection_title,
        )

        library_view.additional_properties = d
        return library_view

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
