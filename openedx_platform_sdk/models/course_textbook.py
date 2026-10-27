from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.textbook_chapter import TextbookChapter


T = TypeVar("T", bound="CourseTextbook")


@_attrs_define
class CourseTextbook:
    """One PDF textbook of a course, as stored in the course's settings.

    A stored textbook can lack ``id``, ``chapters`` or ``tab_title``: imported
    courses may carry textbooks written by other tools, such as the single-file
    form that has a ``url`` and no chapters. Such a textbook is returned with
    ``null`` for the missing scalar and an empty chapter list, rather than
    failing the whole page. A stored ``null`` chapter list is returned empty
    too. Stored keys not declared here are not returned.

        Attributes:
            id (None | str | Unset): Identifier of the textbook, unique within its course. Null when the stored textbook has
                none.
            chapters (list[TextbookChapter] | Unset): Chapters in reading order. Empty when the stored textbook has no
                chapter list.
            tab_title (None | str | Unset): Title of the course tab that opens the textbook. Null when the stored textbook
                has none.
    """

    id: None | str | Unset = UNSET
    chapters: list[TextbookChapter] | Unset = UNSET
    tab_title: None | str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id: None | str | Unset
        if isinstance(self.id, Unset):
            id = UNSET
        else:
            id = self.id

        chapters: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.chapters, Unset):
            chapters = []
            for chapters_item_data in self.chapters:
                chapters_item = chapters_item_data.to_dict()
                chapters.append(chapters_item)

        tab_title: None | str | Unset
        if isinstance(self.tab_title, Unset):
            tab_title = UNSET
        else:
            tab_title = self.tab_title

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if id is not UNSET:
            field_dict["id"] = id
        if chapters is not UNSET:
            field_dict["chapters"] = chapters
        if tab_title is not UNSET:
            field_dict["tab_title"] = tab_title

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.textbook_chapter import TextbookChapter

        d = dict(src_dict)

        def _parse_id(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        id = _parse_id(d.pop("id", UNSET))

        _chapters = d.pop("chapters", UNSET)
        chapters: list[TextbookChapter] | Unset = UNSET
        if _chapters is not UNSET:
            chapters = []
            for chapters_item_data in _chapters:
                chapters_item = TextbookChapter.from_dict(chapters_item_data)

                chapters.append(chapters_item)

        def _parse_tab_title(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        tab_title = _parse_tab_title(d.pop("tab_title", UNSET))

        course_textbook = cls(
            id=id,
            chapters=chapters,
            tab_title=tab_title,
        )

        course_textbook.additional_properties = d
        return course_textbook

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
