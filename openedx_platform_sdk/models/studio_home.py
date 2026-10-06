from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.course_common import CourseCommon
    from ..models.library_view import LibraryView
    from ..models.unsucceeded_course import UnsucceededCourse


T = TypeVar("T", bound="StudioHome")


@_attrs_define
class StudioHome:
    """Serializer for Studio home

    Attributes:
        allow_course_reruns (bool):
        allow_to_create_new_org (bool):
        allow_unicode_course_id (bool):
        allowed_organizations (list[str]):
        allowed_organizations_for_libraries (list[str]):
        can_access_advanced_settings (bool):
        can_create_organizations (bool):
        course_creator_status (str):
        libraries_enabled (bool):
        libraries_v1_enabled (bool):
        libraries_v2_enabled (bool):
        taxonomies_enabled (bool):
        taxonomy_list_mfe_url (str):
        request_course_creator_url (str):
        rerun_creator_status (bool):
        show_new_library_button (bool):
        show_new_library_v2_button (bool):
        split_studio_home (bool):
        studio_name (str):
        studio_short_name (str):
        studio_request_email (str):
        tech_support_email (str):
        platform_name (str):
        user_is_active (bool):
        archived_courses (list[CourseCommon] | Unset):
        courses (list[CourseCommon] | Unset):
        in_process_course_actions (list[UnsucceededCourse] | None | Unset):
        libraries (list[LibraryView] | None | Unset):
    """

    allow_course_reruns: bool
    allow_to_create_new_org: bool
    allow_unicode_course_id: bool
    allowed_organizations: list[str]
    allowed_organizations_for_libraries: list[str]
    can_access_advanced_settings: bool
    can_create_organizations: bool
    course_creator_status: str
    libraries_enabled: bool
    libraries_v1_enabled: bool
    libraries_v2_enabled: bool
    taxonomies_enabled: bool
    taxonomy_list_mfe_url: str
    request_course_creator_url: str
    rerun_creator_status: bool
    show_new_library_button: bool
    show_new_library_v2_button: bool
    split_studio_home: bool
    studio_name: str
    studio_short_name: str
    studio_request_email: str
    tech_support_email: str
    platform_name: str
    user_is_active: bool
    archived_courses: list[CourseCommon] | Unset = UNSET
    courses: list[CourseCommon] | Unset = UNSET
    in_process_course_actions: list[UnsucceededCourse] | None | Unset = UNSET
    libraries: list[LibraryView] | None | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        allow_course_reruns = self.allow_course_reruns

        allow_to_create_new_org = self.allow_to_create_new_org

        allow_unicode_course_id = self.allow_unicode_course_id

        allowed_organizations = self.allowed_organizations

        allowed_organizations_for_libraries = self.allowed_organizations_for_libraries

        can_access_advanced_settings = self.can_access_advanced_settings

        can_create_organizations = self.can_create_organizations

        course_creator_status = self.course_creator_status

        libraries_enabled = self.libraries_enabled

        libraries_v1_enabled = self.libraries_v1_enabled

        libraries_v2_enabled = self.libraries_v2_enabled

        taxonomies_enabled = self.taxonomies_enabled

        taxonomy_list_mfe_url = self.taxonomy_list_mfe_url

        request_course_creator_url = self.request_course_creator_url

        rerun_creator_status = self.rerun_creator_status

        show_new_library_button = self.show_new_library_button

        show_new_library_v2_button = self.show_new_library_v2_button

        split_studio_home = self.split_studio_home

        studio_name = self.studio_name

        studio_short_name = self.studio_short_name

        studio_request_email = self.studio_request_email

        tech_support_email = self.tech_support_email

        platform_name = self.platform_name

        user_is_active = self.user_is_active

        archived_courses: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.archived_courses, Unset):
            archived_courses = []
            for archived_courses_item_data in self.archived_courses:
                archived_courses_item = archived_courses_item_data.to_dict()
                archived_courses.append(archived_courses_item)

        courses: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.courses, Unset):
            courses = []
            for courses_item_data in self.courses:
                courses_item = courses_item_data.to_dict()
                courses.append(courses_item)

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

        libraries: list[dict[str, Any]] | None | Unset
        if isinstance(self.libraries, Unset):
            libraries = UNSET
        elif isinstance(self.libraries, list):
            libraries = []
            for libraries_type_0_item_data in self.libraries:
                libraries_type_0_item = libraries_type_0_item_data.to_dict()
                libraries.append(libraries_type_0_item)

        else:
            libraries = self.libraries

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "allow_course_reruns": allow_course_reruns,
                "allow_to_create_new_org": allow_to_create_new_org,
                "allow_unicode_course_id": allow_unicode_course_id,
                "allowed_organizations": allowed_organizations,
                "allowed_organizations_for_libraries": allowed_organizations_for_libraries,
                "can_access_advanced_settings": can_access_advanced_settings,
                "can_create_organizations": can_create_organizations,
                "course_creator_status": course_creator_status,
                "libraries_enabled": libraries_enabled,
                "libraries_v1_enabled": libraries_v1_enabled,
                "libraries_v2_enabled": libraries_v2_enabled,
                "taxonomies_enabled": taxonomies_enabled,
                "taxonomy_list_mfe_url": taxonomy_list_mfe_url,
                "request_course_creator_url": request_course_creator_url,
                "rerun_creator_status": rerun_creator_status,
                "show_new_library_button": show_new_library_button,
                "show_new_library_v2_button": show_new_library_v2_button,
                "split_studio_home": split_studio_home,
                "studio_name": studio_name,
                "studio_short_name": studio_short_name,
                "studio_request_email": studio_request_email,
                "tech_support_email": tech_support_email,
                "platform_name": platform_name,
                "user_is_active": user_is_active,
            }
        )
        if archived_courses is not UNSET:
            field_dict["archived_courses"] = archived_courses
        if courses is not UNSET:
            field_dict["courses"] = courses
        if in_process_course_actions is not UNSET:
            field_dict["in_process_course_actions"] = in_process_course_actions
        if libraries is not UNSET:
            field_dict["libraries"] = libraries

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.course_common import CourseCommon
        from ..models.library_view import LibraryView
        from ..models.unsucceeded_course import UnsucceededCourse

        d = dict(src_dict)
        allow_course_reruns = d.pop("allow_course_reruns")

        allow_to_create_new_org = d.pop("allow_to_create_new_org")

        allow_unicode_course_id = d.pop("allow_unicode_course_id")

        allowed_organizations = cast(list[str], d.pop("allowed_organizations"))

        allowed_organizations_for_libraries = cast(list[str], d.pop("allowed_organizations_for_libraries"))

        can_access_advanced_settings = d.pop("can_access_advanced_settings")

        can_create_organizations = d.pop("can_create_organizations")

        course_creator_status = d.pop("course_creator_status")

        libraries_enabled = d.pop("libraries_enabled")

        libraries_v1_enabled = d.pop("libraries_v1_enabled")

        libraries_v2_enabled = d.pop("libraries_v2_enabled")

        taxonomies_enabled = d.pop("taxonomies_enabled")

        taxonomy_list_mfe_url = d.pop("taxonomy_list_mfe_url")

        request_course_creator_url = d.pop("request_course_creator_url")

        rerun_creator_status = d.pop("rerun_creator_status")

        show_new_library_button = d.pop("show_new_library_button")

        show_new_library_v2_button = d.pop("show_new_library_v2_button")

        split_studio_home = d.pop("split_studio_home")

        studio_name = d.pop("studio_name")

        studio_short_name = d.pop("studio_short_name")

        studio_request_email = d.pop("studio_request_email")

        tech_support_email = d.pop("tech_support_email")

        platform_name = d.pop("platform_name")

        user_is_active = d.pop("user_is_active")

        _archived_courses = d.pop("archived_courses", UNSET)
        archived_courses: list[CourseCommon] | Unset = UNSET
        if _archived_courses is not UNSET:
            archived_courses = []
            for archived_courses_item_data in _archived_courses:
                archived_courses_item = CourseCommon.from_dict(archived_courses_item_data)

                archived_courses.append(archived_courses_item)

        _courses = d.pop("courses", UNSET)
        courses: list[CourseCommon] | Unset = UNSET
        if _courses is not UNSET:
            courses = []
            for courses_item_data in _courses:
                courses_item = CourseCommon.from_dict(courses_item_data)

                courses.append(courses_item)

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

        def _parse_libraries(data: object) -> list[LibraryView] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                libraries_type_0 = []
                _libraries_type_0 = data
                for libraries_type_0_item_data in _libraries_type_0:
                    libraries_type_0_item = LibraryView.from_dict(libraries_type_0_item_data)

                    libraries_type_0.append(libraries_type_0_item)

                return libraries_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[LibraryView] | None | Unset, data)

        libraries = _parse_libraries(d.pop("libraries", UNSET))

        studio_home = cls(
            allow_course_reruns=allow_course_reruns,
            allow_to_create_new_org=allow_to_create_new_org,
            allow_unicode_course_id=allow_unicode_course_id,
            allowed_organizations=allowed_organizations,
            allowed_organizations_for_libraries=allowed_organizations_for_libraries,
            can_access_advanced_settings=can_access_advanced_settings,
            can_create_organizations=can_create_organizations,
            course_creator_status=course_creator_status,
            libraries_enabled=libraries_enabled,
            libraries_v1_enabled=libraries_v1_enabled,
            libraries_v2_enabled=libraries_v2_enabled,
            taxonomies_enabled=taxonomies_enabled,
            taxonomy_list_mfe_url=taxonomy_list_mfe_url,
            request_course_creator_url=request_course_creator_url,
            rerun_creator_status=rerun_creator_status,
            show_new_library_button=show_new_library_button,
            show_new_library_v2_button=show_new_library_v2_button,
            split_studio_home=split_studio_home,
            studio_name=studio_name,
            studio_short_name=studio_short_name,
            studio_request_email=studio_request_email,
            tech_support_email=tech_support_email,
            platform_name=platform_name,
            user_is_active=user_is_active,
            archived_courses=archived_courses,
            courses=courses,
            in_process_course_actions=in_process_course_actions,
            libraries=libraries,
        )

        studio_home.additional_properties = d
        return studio_home

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
