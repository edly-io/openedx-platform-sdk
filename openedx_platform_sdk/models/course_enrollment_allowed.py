from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from .. import types
from ..types import UNSET, Unset

T = TypeVar("T", bound="CourseEnrollmentAllowed")


@_attrs_define
class CourseEnrollmentAllowed:
    """Serializes CourseEnrollmentAllowed model

    Aggregates all data from the CourseEnrollmentAllowed table, and pulls in the serialization
    to give a complete representation of course enrollment allowed.

        Attributes:
            email (str):
            course_id (str):
            created (datetime.datetime | None):
            auto_enroll (bool | Unset):
            user (int | None | Unset): First user which enrolled in the specified course through the specified e-mail. Once
                set, it won't change.
    """

    email: str
    course_id: str
    created: datetime.datetime | None
    auto_enroll: bool | Unset = UNSET
    user: int | None | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        email = self.email

        course_id = self.course_id

        created: None | str
        if isinstance(self.created, datetime.datetime):
            created = self.created.isoformat()
        else:
            created = self.created

        auto_enroll = self.auto_enroll

        user: int | None | Unset
        if isinstance(self.user, Unset):
            user = UNSET
        else:
            user = self.user

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "email": email,
                "course_id": course_id,
                "created": created,
            }
        )
        if auto_enroll is not UNSET:
            field_dict["auto_enroll"] = auto_enroll
        if user is not UNSET:
            field_dict["user"] = user

        return field_dict

    def to_multipart(self) -> types.RequestFiles:
        files: types.RequestFiles = []

        files.append(("email", (None, str(self.email).encode(), "text/plain")))

        files.append(("course_id", (None, str(self.course_id).encode(), "text/plain")))

        if isinstance(self.created, datetime.datetime):
            files.append(("created", (None, self.created.isoformat().encode(), "text/plain")))
        else:
            files.append(("created", (None, str(self.created).encode(), "text/plain")))

        if not isinstance(self.auto_enroll, Unset):
            files.append(("auto_enroll", (None, str(self.auto_enroll).encode(), "text/plain")))

        if not isinstance(self.user, Unset):
            if isinstance(self.user, int):
                files.append(("user", (None, str(self.user).encode(), "text/plain")))
            else:
                files.append(("user", (None, str(self.user).encode(), "text/plain")))

        for prop_name, prop in self.additional_properties.items():
            files.append((prop_name, (None, str(prop).encode(), "text/plain")))

        return files

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        email = d.pop("email")

        course_id = d.pop("course_id")

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

        auto_enroll = d.pop("auto_enroll", UNSET)

        def _parse_user(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        user = _parse_user(d.pop("user", UNSET))

        course_enrollment_allowed = cls(
            email=email,
            course_id=course_id,
            created=created,
            auto_enroll=auto_enroll,
            user=user,
        )

        course_enrollment_allowed.additional_properties = d
        return course_enrollment_allowed

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
