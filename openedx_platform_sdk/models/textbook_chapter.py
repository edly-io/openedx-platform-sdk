from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="TextbookChapter")


@_attrs_define
class TextbookChapter:
    """One chapter of a course PDF textbook.

    A stored chapter missing ``title`` or ``url``, or holding null for either,
    is returned with an empty string in its place rather than failing the page.

        Attributes:
            title (str | Unset): Chapter title shown in the textbook's table of contents. Empty when the stored chapter has
                none. Default: ''.
            url (str | Unset): Address of the chapter's PDF file, usually a course asset path. Empty when the stored chapter
                has none. Default: ''.
    """

    title: str | Unset = ""
    url: str | Unset = ""
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        title = self.title

        url = self.url

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if title is not UNSET:
            field_dict["title"] = title
        if url is not UNSET:
            field_dict["url"] = url

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        title = d.pop("title", UNSET)

        url = d.pop("url", UNSET)

        textbook_chapter = cls(
            title=title,
            url=url,
        )

        textbook_chapter.additional_properties = d
        return textbook_chapter

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
