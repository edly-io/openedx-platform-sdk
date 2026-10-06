from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.course_common import CourseCommon
    from ..models.unsucceeded_course import UnsucceededCourse


T = TypeVar("T", bound="CourseHomeTab")


@_attrs_define
class CourseHomeTab:
    """Serializer for the courses tab of the Studio home page.

    Attributes:
        courses (list[CourseCommon] | Unset):
        archived_courses (list[CourseCommon] | Unset):
        in_process_course_actions (list[UnsucceededCourse] | None | Unset):
    """

    courses: list[CourseCommon] | Unset = UNSET
    archived_courses: list[CourseCommon] | Unset = UNSET
    in_process_course_actions: list[UnsucceededCourse] | None | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        courses: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.courses, Unset):
            courses = []
            for courses_item_data in self.courses:
                courses_item = courses_item_data.to_dict()
                courses.append(courses_item)

        archived_courses: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.archived_courses, Unset):
            archived_courses = []
            for archived_courses_item_data in self.archived_courses:
                archived_courses_item = archived_courses_item_data.to_dict()
                archived_courses.append(archived_courses_item)

        in_process_course_actions: list[dict[str, Any]] | None | Unset
        if isinstance(self.in_process_course_actions, Unset):
            in_process_course_actions = UNSET
        elif isinstance(self.in_process_course_actions, list):
            in_process_course_actions = []
            for in_process_course_actions_type_0_item_data in self.in_process_course_actions:
                in_process_course_actions_type_0_item = in_process_course_actions_type_0_item_data.to_dict()
                in_process_course_actions.append(in_process_course_actions_type_0_item)

        else:
            in_process_course_actions = self.in_process_course_actions

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if courses is not UNSET:
            field_dict["courses"] = courses
        if archived_courses is not UNSET:
            field_dict["archived_courses"] = archived_courses
        if in_process_course_actions is not UNSET:
            field_dict["in_process_course_actions"] = in_process_course_actions

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.course_common import CourseCommon
        from ..models.unsucceeded_course import UnsucceededCourse

        d = dict(src_dict)
        _courses = d.pop("courses", UNSET)
        courses: list[CourseCommon] | Unset = UNSET
        if _courses is not UNSET:
            courses = []
            for courses_item_data in _courses:
                courses_item = CourseCommon.from_dict(courses_item_data)

                courses.append(courses_item)

        _archived_courses = d.pop("archived_courses", UNSET)
        archived_courses: list[CourseCommon] | Unset = UNSET
        if _archived_courses is not UNSET:
            archived_courses = []
            for archived_courses_item_data in _archived_courses:
                archived_courses_item = CourseCommon.from_dict(archived_courses_item_data)

                archived_courses.append(archived_courses_item)

        def _parse_in_process_course_actions(data: object) -> list[UnsucceededCourse] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                in_process_course_actions_type_0 = []
                _in_process_course_actions_type_0 = data
                for in_process_course_actions_type_0_item_data in _in_process_course_actions_type_0:
                    in_process_course_actions_type_0_item = UnsucceededCourse.from_dict(
                        in_process_course_actions_type_0_item_data
                    )

                    in_process_course_actions_type_0.append(in_process_course_actions_type_0_item)

                return in_process_course_actions_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[UnsucceededCourse] | None | Unset, data)

        in_process_course_actions = _parse_in_process_course_actions(d.pop("in_process_course_actions", UNSET))

        course_home_tab = cls(
            courses=courses,
            archived_courses=archived_courses,
            in_process_course_actions=in_process_course_actions,
        )

        course_home_tab.additional_properties = d
        return course_home_tab

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
