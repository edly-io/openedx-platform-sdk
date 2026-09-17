from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.course_home_tab_serializer_v2 import CourseHomeTabSerializerV2


T = TypeVar("T", bound="PaginatedV4HomeCoursesResponse")


@_attrs_define
class PaginatedV4HomeCoursesResponse:
    """
    Attributes:
        count (int): Total number of courses.
        num_pages (int): Total number of pages.
        current_page (int): Current page number.
        start (int): Zero-based index of the first item on this page.
        next_ (None | str): URL for the next page, or null.
        previous (None | str): URL for the previous page, or null.
        results (CourseHomeTabSerializerV2): Serializer for course home tab V2 with unsucceeded courses and in process
            course actions.
    """

    count: int
    num_pages: int
    current_page: int
    start: int
    next_: None | str
    previous: None | str
    results: CourseHomeTabSerializerV2
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

        results = self.results.to_dict()

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
        from ..models.course_home_tab_serializer_v2 import CourseHomeTabSerializerV2

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

        results = CourseHomeTabSerializerV2.from_dict(d.pop("results"))

        paginated_v4_home_courses_response = cls(
            count=count,
            num_pages=num_pages,
            current_page=current_page,
            start=start,
            next_=next_,
            previous=previous,
            results=results,
        )

        paginated_v4_home_courses_response.additional_properties = d
        return paginated_v4_home_courses_response

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
