from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.course_textbook import CourseTextbook


T = TypeVar("T", bound="PaginatedCourseTextbookList")


@_attrs_define
class PaginatedCourseTextbookList:
    """
    Attributes:
        count (int): Total number of items.
        num_pages (int): Total number of pages.
        current_page (int): Number of this page, starting at 1.
        start (int): Zero-based index of the first item on this page.
        next_ (None | str): Address of the next page, or null on the last page.
        previous (None | str): Address of the previous page, or null on the first page.
        results (list[CourseTextbook]):
    """

    count: int
    num_pages: int
    current_page: int
    start: int
    next_: None | str
    previous: None | str
    results: list[CourseTextbook]
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        count = self.count

        num_pages = self.num_pages

        current_page = self.current_page

        start = self.start

        next_: None | str
        next_ = self.next_

        previous: None | str
        previous = self.previous

        results = []
        for results_item_data in self.results:
            results_item = results_item_data.to_dict()
            results.append(results_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "count": count,
                "num_pages": num_pages,
                "current_page": current_page,
                "start": start,
                "next": next_,
                "previous": previous,
                "results": results,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.course_textbook import CourseTextbook

        d = dict(src_dict)
        count = d.pop("count")

        num_pages = d.pop("num_pages")

        current_page = d.pop("current_page")

        start = d.pop("start")

        def _parse_next_(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        next_ = _parse_next_(d.pop("next"))

        def _parse_previous(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        previous = _parse_previous(d.pop("previous"))

        results = []
        _results = d.pop("results")
        for results_item_data in _results:
            results_item = CourseTextbook.from_dict(results_item_data)

            results.append(results_item)

        paginated_course_textbook_list = cls(
            count=count,
            num_pages=num_pages,
            current_page=current_page,
            start=start,
            next_=next_,
            previous=previous,
            results=results,
        )

        paginated_course_textbook_list.additional_properties = d
        return paginated_course_textbook_list

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
