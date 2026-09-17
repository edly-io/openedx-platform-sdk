from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="CourseCommon")


@_attrs_define
class CourseCommon:
    """Serializer for course renders

    Attributes:
        course_key (str):
        display_name (str):
        lms_link (str):
        number (str):
        org (str):
        rerun_link (str):
        run (str):
        url (str):
    """

    course_key: str
    display_name: str
    lms_link: str
    number: str
    org: str
    rerun_link: str
    run: str
    url: str
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        course_key = self.course_key

        display_name = self.display_name

        lms_link = self.lms_link

        number = self.number

        org = self.org

        rerun_link = self.rerun_link

        run = self.run

        url = self.url

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "course_key": course_key,
                "display_name": display_name,
                "lms_link": lms_link,
                "number": number,
                "org": org,
                "rerun_link": rerun_link,
                "run": run,
                "url": url,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        course_key = d.pop("course_key")

        display_name = d.pop("display_name")

        lms_link = d.pop("lms_link")

        number = d.pop("number")

        org = d.pop("org")

        rerun_link = d.pop("rerun_link")

        run = d.pop("run")

        url = d.pop("url")

        course_common = cls(
            course_key=course_key,
            display_name=display_name,
            lms_link=lms_link,
            number=number,
            org=org,
            rerun_link=rerun_link,
            run=run,
            url=url,
        )

        course_common.additional_properties = d
        return course_common

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
