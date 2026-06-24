from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="CourseCommonSerializerV2")


@_attrs_define
class CourseCommonSerializerV2:
    """Serializer for course common fields V2.

    Attributes:
        course_key (str):
        display_name (str):
        lms_link (str):
        cms_link (str):
        number (str):
        org (str):
        rerun_link (str):
        run (str):
        url (str):
        is_active (str):
    """

    course_key: str
    display_name: str
    lms_link: str
    cms_link: str
    number: str
    org: str
    rerun_link: str
    run: str
    url: str
    is_active: str
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        course_key = self.course_key

        display_name = self.display_name

        lms_link = self.lms_link

        cms_link = self.cms_link

        number = self.number

        org = self.org

        rerun_link = self.rerun_link

        run = self.run

        url = self.url

        is_active = self.is_active

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "course_key": course_key,
                "display_name": display_name,
                "lms_link": lms_link,
                "cms_link": cms_link,
                "number": number,
                "org": org,
                "rerun_link": rerun_link,
                "run": run,
                "url": url,
                "is_active": is_active,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        course_key = d.pop("course_key")

        display_name = d.pop("display_name")

        lms_link = d.pop("lms_link")

        cms_link = d.pop("cms_link")

        number = d.pop("number")

        org = d.pop("org")

        rerun_link = d.pop("rerun_link")

        run = d.pop("run")

        url = d.pop("url")

        is_active = d.pop("is_active")

        course_common_serializer_v2 = cls(
            course_key=course_key,
            display_name=display_name,
            lms_link=lms_link,
            cms_link=cms_link,
            number=number,
            org=org,
            rerun_link=rerun_link,
            run=run,
            url=url,
            is_active=is_active,
        )

        course_common_serializer_v2.additional_properties = d
        return course_common_serializer_v2

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
