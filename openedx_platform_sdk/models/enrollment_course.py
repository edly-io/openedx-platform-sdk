from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="EnrollmentCourse")


@_attrs_define
class EnrollmentCourse:
    """Serialize a course block and related information.

    Attributes:
        course_id (str):
        course_name (str):
        enrollment_start (datetime.datetime | None):
        enrollment_end (datetime.datetime | None):
        course_start (datetime.datetime | None):
        course_end (datetime.datetime | None):
        invite_only (bool):
        course_modes (str):
        pacing_type (str):
    """

    course_id: str
    course_name: str
    enrollment_start: datetime.datetime | None
    enrollment_end: datetime.datetime | None
    course_start: datetime.datetime | None
    course_end: datetime.datetime | None
    invite_only: bool
    course_modes: str
    pacing_type: str
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        course_id = self.course_id

        course_name = self.course_name

        enrollment_start: None | str
        if isinstance(self.enrollment_start, datetime.datetime):
            enrollment_start = self.enrollment_start.isoformat()
        else:
            enrollment_start = self.enrollment_start

        enrollment_end: None | str
        if isinstance(self.enrollment_end, datetime.datetime):
            enrollment_end = self.enrollment_end.isoformat()
        else:
            enrollment_end = self.enrollment_end

        course_start: None | str
        if isinstance(self.course_start, datetime.datetime):
            course_start = self.course_start.isoformat()
        else:
            course_start = self.course_start

        course_end: None | str
        if isinstance(self.course_end, datetime.datetime):
            course_end = self.course_end.isoformat()
        else:
            course_end = self.course_end

        invite_only = self.invite_only

        course_modes = self.course_modes

        pacing_type = self.pacing_type

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "course_id": course_id,
                "course_name": course_name,
                "enrollment_start": enrollment_start,
                "enrollment_end": enrollment_end,
                "course_start": course_start,
                "course_end": course_end,
                "invite_only": invite_only,
                "course_modes": course_modes,
                "pacing_type": pacing_type,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        course_id = d.pop("course_id")

        course_name = d.pop("course_name")

        def _parse_enrollment_start(data: object) -> datetime.datetime | None:
            if data is None:
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                enrollment_start_type_0 = datetime.datetime.fromisoformat(data)

                return enrollment_start_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(datetime.datetime | None, data)

        enrollment_start = _parse_enrollment_start(d.pop("enrollment_start"))

        def _parse_enrollment_end(data: object) -> datetime.datetime | None:
            if data is None:
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                enrollment_end_type_0 = datetime.datetime.fromisoformat(data)

                return enrollment_end_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(datetime.datetime | None, data)

        enrollment_end = _parse_enrollment_end(d.pop("enrollment_end"))

        def _parse_course_start(data: object) -> datetime.datetime | None:
            if data is None:
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                course_start_type_0 = datetime.datetime.fromisoformat(data)

                return course_start_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(datetime.datetime | None, data)

        course_start = _parse_course_start(d.pop("course_start"))

        def _parse_course_end(data: object) -> datetime.datetime | None:
            if data is None:
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                course_end_type_0 = datetime.datetime.fromisoformat(data)

                return course_end_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(datetime.datetime | None, data)

        course_end = _parse_course_end(d.pop("course_end"))

        invite_only = d.pop("invite_only")

        course_modes = d.pop("course_modes")

        pacing_type = d.pop("pacing_type")

        enrollment_course = cls(
            course_id=course_id,
            course_name=course_name,
            enrollment_start=enrollment_start,
            enrollment_end=enrollment_end,
            course_start=course_start,
            course_end=course_end,
            invite_only=invite_only,
            course_modes=course_modes,
            pacing_type=pacing_type,
        )

        enrollment_course.additional_properties = d
        return enrollment_course

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
