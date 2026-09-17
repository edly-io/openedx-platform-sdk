from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="EnrollmentCourse")


@_attrs_define
class EnrollmentCourse:
    """Serialize a course block and related information.

    Attributes:
        course_id (str):
        course_name (str):
        enrollment_start (datetime.datetime):
        enrollment_end (datetime.datetime):
        course_start (datetime.datetime):
        course_end (datetime.datetime):
        invite_only (bool):
        course_modes (str):
        pacing_type (str):
    """

    course_id: str
    course_name: str
    enrollment_start: datetime.datetime
    enrollment_end: datetime.datetime
    course_start: datetime.datetime
    course_end: datetime.datetime
    invite_only: bool
    course_modes: str
    pacing_type: str
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        course_id = self.course_id

        course_name = self.course_name

        enrollment_start = self.enrollment_start.isoformat()

        enrollment_end = self.enrollment_end.isoformat()

        course_start = self.course_start.isoformat()

        course_end = self.course_end.isoformat()

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

        _raw_enrollment_start = d.pop("enrollment_start")
        enrollment_start = datetime.datetime.fromisoformat(_raw_enrollment_start) if isinstance(_raw_enrollment_start, str) else None

        _raw_enrollment_end = d.pop("enrollment_end")
        enrollment_end = datetime.datetime.fromisoformat(_raw_enrollment_end) if isinstance(_raw_enrollment_end, str) else None

        _raw_course_start = d.pop("course_start")
        course_start = datetime.datetime.fromisoformat(_raw_course_start) if isinstance(_raw_course_start, str) else None

        _raw_course_end = d.pop("course_end")
        course_end = datetime.datetime.fromisoformat(_raw_course_end) if isinstance(_raw_course_end, str) else None

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
