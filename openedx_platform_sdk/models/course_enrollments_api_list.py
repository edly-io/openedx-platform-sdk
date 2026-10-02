from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="CourseEnrollmentsApiList")


@_attrs_define
class CourseEnrollmentsApiList:
    """Serializes CourseEnrollment model and returns a subset of fields returned
    by the CourseEnrollmentSerializer.

        Attributes:
            created (datetime.datetime | None):
            user (str):
            course_id (str):
            mode (str | Unset):
            is_active (bool | Unset):
    """

    created: datetime.datetime | None
    user: str
    course_id: str
    mode: str | Unset = UNSET
    is_active: bool | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        created: None | str
        if isinstance(self.created, datetime.datetime):
            created = self.created.isoformat()
        else:
            created = self.created

        user = self.user

        course_id = self.course_id

        mode = self.mode

        is_active = self.is_active

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "created": created,
                "user": user,
                "course_id": course_id,
            }
        )
        if mode is not UNSET:
            field_dict["mode"] = mode
        if is_active is not UNSET:
            field_dict["is_active"] = is_active

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
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

        user = d.pop("user")

        course_id = d.pop("course_id")

        mode = d.pop("mode", UNSET)

        is_active = d.pop("is_active", UNSET)

        course_enrollments_api_list = cls(
            created=created,
            user=user,
            course_id=course_id,
            mode=mode,
            is_active=is_active,
        )

        course_enrollments_api_list.additional_properties = d
        return course_enrollments_api_list

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
