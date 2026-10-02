from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="UnsucceededCourse")


@_attrs_define
class UnsucceededCourse:
    """Serializer for unsucceeded course

    Attributes:
        display_name (str):
        course_key (str):
        org (str):
        number (str):
        run (str):
        is_failed (bool):
        is_in_progress (bool):
        dismiss_link (str):
    """

    display_name: str
    course_key: str
    org: str
    number: str
    run: str
    is_failed: bool
    is_in_progress: bool
    dismiss_link: str
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        display_name = self.display_name

        course_key = self.course_key

        org = self.org

        number = self.number

        run = self.run

        is_failed = self.is_failed

        is_in_progress = self.is_in_progress

        dismiss_link = self.dismiss_link

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "display_name": display_name,
                "course_key": course_key,
                "org": org,
                "number": number,
                "run": run,
                "is_failed": is_failed,
                "is_in_progress": is_in_progress,
                "dismiss_link": dismiss_link,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        display_name = d.pop("display_name")

        course_key = d.pop("course_key")

        org = d.pop("org")

        number = d.pop("number")

        run = d.pop("run")

        is_failed = d.pop("is_failed")

        is_in_progress = d.pop("is_in_progress")

        dismiss_link = d.pop("dismiss_link")

        unsucceeded_course = cls(
            display_name=display_name,
            course_key=course_key,
            org=org,
            number=number,
            run=run,
            is_failed=is_failed,
            is_in_progress=is_in_progress,
            dismiss_link=dismiss_link,
        )

        unsucceeded_course.additional_properties = d
        return unsucceeded_course

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
