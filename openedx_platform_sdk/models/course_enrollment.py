from __future__ import annotations

import datetime
import json
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from .. import types
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.enrollment_course import EnrollmentCourse


T = TypeVar("T", bound="CourseEnrollment")


@_attrs_define
class CourseEnrollment:
    """Serializes CourseEnrollment models

    Aggregates all data from the Course Enrollment table, and pulls in the serialization for
    the Course block and course modes, to give a complete representation of course enrollment.

        Attributes:
            created (datetime.datetime | None):
            course_details (EnrollmentCourse): Serialize a course block and related information.
            user (str):
            mode (str | Unset):
            is_active (bool | Unset):
    """

    created: datetime.datetime | None
    course_details: EnrollmentCourse
    user: str
    mode: str | Unset = UNSET
    is_active: bool | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        created: None | str
        if isinstance(self.created, datetime.datetime):
            created = self.created.isoformat()
        else:
            created = self.created

        course_details = self.course_details.to_dict()

        user = self.user

        mode = self.mode

        is_active = self.is_active

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "created": created,
                "course_details": course_details,
                "user": user,
            }
        )
        if mode is not UNSET:
            field_dict["mode"] = mode
        if is_active is not UNSET:
            field_dict["is_active"] = is_active

        return field_dict

    def to_multipart(self) -> types.RequestFiles:
        files: types.RequestFiles = []

        if isinstance(self.created, datetime.datetime):
            files.append(("created", (None, self.created.isoformat().encode(), "text/plain")))
        else:
            files.append(("created", (None, str(self.created).encode(), "text/plain")))

        files.append(("course_details", (None, json.dumps(self.course_details.to_dict()).encode(), "application/json")))

        files.append(("user", (None, str(self.user).encode(), "text/plain")))

        if not isinstance(self.mode, Unset):
            files.append(("mode", (None, str(self.mode).encode(), "text/plain")))

        if not isinstance(self.is_active, Unset):
            files.append(("is_active", (None, str(self.is_active).encode(), "text/plain")))

        for prop_name, prop in self.additional_properties.items():
            files.append((prop_name, (None, str(prop).encode(), "text/plain")))

        return files

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.enrollment_course import EnrollmentCourse

        d = dict(src_dict)

        def _parse_created(data: object) -> datetime.datetime | None:
            if data is None:
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                created_type_0 = datetime.datetime.fromisoformat(data)

                return created_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(datetime.datetime | None, data)

        created = _parse_created(d.pop("created"))

        course_details = EnrollmentCourse.from_dict(d.pop("course_details"))

        user = d.pop("user")

        mode = d.pop("mode", UNSET)

        is_active = d.pop("is_active", UNSET)

        course_enrollment = cls(
            created=created,
            course_details=course_details,
            user=user,
            mode=mode,
            is_active=is_active,
        )

        course_enrollment.additional_properties = d
        return course_enrollment

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
