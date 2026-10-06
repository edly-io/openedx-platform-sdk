from __future__ import annotations

import datetime
import json
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from .. import types

if TYPE_CHECKING:
    from ..models.instructors import Instructors


T = TypeVar("T", bound="CourseDetails")


@_attrs_define
class CourseDetails:
    """Serializer for course details

    Attributes:
        about_sidebar_html (None | str):
        banner_image_name (str):
        banner_image_asset_path (str):
        certificate_available_date (datetime.datetime | None):
        certificates_display_behavior (None | str):
        course_id (str):
        course_image_asset_path (str):
        course_image_name (str):
        description (str):
        duration (str):
        effort (None | str):
        end_date (datetime.datetime | None):
        enrollment_end (datetime.datetime | None):
        enrollment_start (datetime.datetime | None):
        entrance_exam_enabled (str):
        entrance_exam_id (str):
        entrance_exam_minimum_score_pct (str):
        instructor_info (Instructors): Serializer for instructors
        intro_video (None | str):
        language (None | str):
        learning_info (list[str]):
        license_ (None | str):
        org (str):
        overview (str):
        pre_requisite_courses (list[str]):
        run (str):
        self_paced (bool):
        has_changes (bool):
        short_description (str):
        start_date (datetime.datetime):
        subtitle (str):
        syllabus (None | str):
        title (str):
        video_thumbnail_image_asset_path (str):
        video_thumbnail_image_name (str):
    """

    about_sidebar_html: None | str
    banner_image_name: str
    banner_image_asset_path: str
    certificate_available_date: datetime.datetime | None
    certificates_display_behavior: None | str
    course_id: str
    course_image_asset_path: str
    course_image_name: str
    description: str
    duration: str
    effort: None | str
    end_date: datetime.datetime | None
    enrollment_end: datetime.datetime | None
    enrollment_start: datetime.datetime | None
    entrance_exam_enabled: str
    entrance_exam_id: str
    entrance_exam_minimum_score_pct: str
    instructor_info: Instructors
    intro_video: None | str
    language: None | str
    learning_info: list[str]
    license_: None | str
    org: str
    overview: str
    pre_requisite_courses: list[str]
    run: str
    self_paced: bool
    has_changes: bool
    short_description: str
    start_date: datetime.datetime
    subtitle: str
    syllabus: None | str
    title: str
    video_thumbnail_image_asset_path: str
    video_thumbnail_image_name: str
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        about_sidebar_html: None | str
        about_sidebar_html = self.about_sidebar_html

        banner_image_name = self.banner_image_name

        banner_image_asset_path = self.banner_image_asset_path

        certificate_available_date: None | str
        if isinstance(self.certificate_available_date, datetime.datetime):
            certificate_available_date = self.certificate_available_date.isoformat()
        else:
            certificate_available_date = self.certificate_available_date

        certificates_display_behavior: None | str
        certificates_display_behavior = self.certificates_display_behavior

        course_id = self.course_id

        course_image_asset_path = self.course_image_asset_path

        course_image_name = self.course_image_name

        description = self.description

        duration = self.duration

        effort: None | str
        effort = self.effort

        end_date: None | str
        if isinstance(self.end_date, datetime.datetime):
            end_date = self.end_date.isoformat()
        else:
            end_date = self.end_date

        enrollment_end: None | str
        if isinstance(self.enrollment_end, datetime.datetime):
            enrollment_end = self.enrollment_end.isoformat()
        else:
            enrollment_end = self.enrollment_end

        enrollment_start: None | str
        if isinstance(self.enrollment_start, datetime.datetime):
            enrollment_start = self.enrollment_start.isoformat()
        else:
            enrollment_start = self.enrollment_start

        entrance_exam_enabled = self.entrance_exam_enabled

        entrance_exam_id = self.entrance_exam_id

        entrance_exam_minimum_score_pct = self.entrance_exam_minimum_score_pct

        instructor_info = self.instructor_info.to_dict()

        intro_video: None | str
        intro_video = self.intro_video

        language: None | str
        language = self.language

        learning_info = self.learning_info

        license_: None | str
        license_ = self.license_

        org = self.org

        overview = self.overview

        pre_requisite_courses = self.pre_requisite_courses

        run = self.run

        self_paced = self.self_paced

        has_changes = self.has_changes

        short_description = self.short_description

        start_date = self.start_date.isoformat()

        subtitle = self.subtitle

        syllabus: None | str
        syllabus = self.syllabus

        title = self.title

        video_thumbnail_image_asset_path = self.video_thumbnail_image_asset_path

        video_thumbnail_image_name = self.video_thumbnail_image_name

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "about_sidebar_html": about_sidebar_html,
                "banner_image_name": banner_image_name,
                "banner_image_asset_path": banner_image_asset_path,
                "certificate_available_date": certificate_available_date,
                "certificates_display_behavior": certificates_display_behavior,
                "course_id": course_id,
                "course_image_asset_path": course_image_asset_path,
                "course_image_name": course_image_name,
                "description": description,
                "duration": duration,
                "effort": effort,
                "end_date": end_date,
                "enrollment_end": enrollment_end,
                "enrollment_start": enrollment_start,
                "entrance_exam_enabled": entrance_exam_enabled,
                "entrance_exam_id": entrance_exam_id,
                "entrance_exam_minimum_score_pct": entrance_exam_minimum_score_pct,
                "instructor_info": instructor_info,
                "intro_video": intro_video,
                "language": language,
                "learning_info": learning_info,
                "license": license_,
                "org": org,
                "overview": overview,
                "pre_requisite_courses": pre_requisite_courses,
                "run": run,
                "self_paced": self_paced,
                "has_changes": has_changes,
                "short_description": short_description,
                "start_date": start_date,
                "subtitle": subtitle,
                "syllabus": syllabus,
                "title": title,
                "video_thumbnail_image_asset_path": video_thumbnail_image_asset_path,
                "video_thumbnail_image_name": video_thumbnail_image_name,
            }
        )

        return field_dict

    def to_multipart(self) -> types.RequestFiles:
        files: types.RequestFiles = []

        if isinstance(self.about_sidebar_html, str):
            files.append(("about_sidebar_html", (None, str(self.about_sidebar_html).encode(), "text/plain")))
        else:
            files.append(("about_sidebar_html", (None, str(self.about_sidebar_html).encode(), "text/plain")))

        files.append(("banner_image_name", (None, str(self.banner_image_name).encode(), "text/plain")))

        files.append(("banner_image_asset_path", (None, str(self.banner_image_asset_path).encode(), "text/plain")))

        if isinstance(self.certificate_available_date, datetime.datetime):
            files.append(
                (
                    "certificate_available_date",
                    (None, self.certificate_available_date.isoformat().encode(), "text/plain"),
                )
            )
        else:
            files.append(
                ("certificate_available_date", (None, str(self.certificate_available_date).encode(), "text/plain"))
            )

        if isinstance(self.certificates_display_behavior, str):
            files.append(
                (
                    "certificates_display_behavior",
                    (None, str(self.certificates_display_behavior).encode(), "text/plain"),
                )
            )
        else:
            files.append(
                (
                    "certificates_display_behavior",
                    (None, str(self.certificates_display_behavior).encode(), "text/plain"),
                )
            )

        files.append(("course_id", (None, str(self.course_id).encode(), "text/plain")))

        files.append(("course_image_asset_path", (None, str(self.course_image_asset_path).encode(), "text/plain")))

        files.append(("course_image_name", (None, str(self.course_image_name).encode(), "text/plain")))

        files.append(("description", (None, str(self.description).encode(), "text/plain")))

        files.append(("duration", (None, str(self.duration).encode(), "text/plain")))

        if isinstance(self.effort, str):
            files.append(("effort", (None, str(self.effort).encode(), "text/plain")))
        else:
            files.append(("effort", (None, str(self.effort).encode(), "text/plain")))

        if isinstance(self.end_date, datetime.datetime):
            files.append(("end_date", (None, self.end_date.isoformat().encode(), "text/plain")))
        else:
            files.append(("end_date", (None, str(self.end_date).encode(), "text/plain")))

        if isinstance(self.enrollment_end, datetime.datetime):
            files.append(("enrollment_end", (None, self.enrollment_end.isoformat().encode(), "text/plain")))
        else:
            files.append(("enrollment_end", (None, str(self.enrollment_end).encode(), "text/plain")))

        if isinstance(self.enrollment_start, datetime.datetime):
            files.append(("enrollment_start", (None, self.enrollment_start.isoformat().encode(), "text/plain")))
        else:
            files.append(("enrollment_start", (None, str(self.enrollment_start).encode(), "text/plain")))

        files.append(("entrance_exam_enabled", (None, str(self.entrance_exam_enabled).encode(), "text/plain")))

        files.append(("entrance_exam_id", (None, str(self.entrance_exam_id).encode(), "text/plain")))

        files.append(
            (
                "entrance_exam_minimum_score_pct",
                (None, str(self.entrance_exam_minimum_score_pct).encode(), "text/plain"),
            )
        )

        files.append(
            ("instructor_info", (None, json.dumps(self.instructor_info.to_dict()).encode(), "application/json"))
        )

        if isinstance(self.intro_video, str):
            files.append(("intro_video", (None, str(self.intro_video).encode(), "text/plain")))
        else:
            files.append(("intro_video", (None, str(self.intro_video).encode(), "text/plain")))

        if isinstance(self.language, str):
            files.append(("language", (None, str(self.language).encode(), "text/plain")))
        else:
            files.append(("language", (None, str(self.language).encode(), "text/plain")))

        for learning_info_item_element in self.learning_info:
            files.append(("learning_info", (None, str(learning_info_item_element).encode(), "text/plain")))

        if isinstance(self.license_, str):
            files.append(("license", (None, str(self.license_).encode(), "text/plain")))
        else:
            files.append(("license", (None, str(self.license_).encode(), "text/plain")))

        files.append(("org", (None, str(self.org).encode(), "text/plain")))

        files.append(("overview", (None, str(self.overview).encode(), "text/plain")))

        for pre_requisite_courses_item_element in self.pre_requisite_courses:
            files.append(
                ("pre_requisite_courses", (None, str(pre_requisite_courses_item_element).encode(), "text/plain"))
            )

        files.append(("run", (None, str(self.run).encode(), "text/plain")))

        files.append(("self_paced", (None, str(self.self_paced).encode(), "text/plain")))

        files.append(("has_changes", (None, str(self.has_changes).encode(), "text/plain")))

        files.append(("short_description", (None, str(self.short_description).encode(), "text/plain")))

        files.append(("start_date", (None, self.start_date.isoformat().encode(), "text/plain")))

        files.append(("subtitle", (None, str(self.subtitle).encode(), "text/plain")))

        if isinstance(self.syllabus, str):
            files.append(("syllabus", (None, str(self.syllabus).encode(), "text/plain")))
        else:
            files.append(("syllabus", (None, str(self.syllabus).encode(), "text/plain")))

        files.append(("title", (None, str(self.title).encode(), "text/plain")))

        files.append(
            (
                "video_thumbnail_image_asset_path",
                (None, str(self.video_thumbnail_image_asset_path).encode(), "text/plain"),
            )
        )

        files.append(
            ("video_thumbnail_image_name", (None, str(self.video_thumbnail_image_name).encode(), "text/plain"))
        )

        for prop_name, prop in self.additional_properties.items():
            files.append((prop_name, (None, str(prop).encode(), "text/plain")))

        return files

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.instructors import Instructors

        d = dict(src_dict)

        def _parse_about_sidebar_html(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        about_sidebar_html = _parse_about_sidebar_html(d.pop("about_sidebar_html"))

        banner_image_name = d.pop("banner_image_name")

        banner_image_asset_path = d.pop("banner_image_asset_path")

        def _parse_certificate_available_date(data: object) -> datetime.datetime | None:
            if data is None:
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                certificate_available_date_type_0 = datetime.datetime.fromisoformat(data)

                return certificate_available_date_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(datetime.datetime | None, data)

        certificate_available_date = _parse_certificate_available_date(d.pop("certificate_available_date"))

        def _parse_certificates_display_behavior(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        certificates_display_behavior = _parse_certificates_display_behavior(d.pop("certificates_display_behavior"))

        course_id = d.pop("course_id")

        course_image_asset_path = d.pop("course_image_asset_path")

        course_image_name = d.pop("course_image_name")

        description = d.pop("description")

        duration = d.pop("duration")

        def _parse_effort(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        effort = _parse_effort(d.pop("effort"))

        def _parse_end_date(data: object) -> datetime.datetime | None:
            if data is None:
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                end_date_type_0 = datetime.datetime.fromisoformat(data)

                return end_date_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(datetime.datetime | None, data)

        end_date = _parse_end_date(d.pop("end_date"))

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

        entrance_exam_enabled = d.pop("entrance_exam_enabled")

        entrance_exam_id = d.pop("entrance_exam_id")

        entrance_exam_minimum_score_pct = d.pop("entrance_exam_minimum_score_pct")

        instructor_info = Instructors.from_dict(d.pop("instructor_info"))

        def _parse_intro_video(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        intro_video = _parse_intro_video(d.pop("intro_video"))

        def _parse_language(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        language = _parse_language(d.pop("language"))

        learning_info = cast(list[str], d.pop("learning_info"))

        def _parse_license_(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        license_ = _parse_license_(d.pop("license"))

        org = d.pop("org")

        overview = d.pop("overview")

        pre_requisite_courses = cast(list[str], d.pop("pre_requisite_courses"))

        run = d.pop("run")

        self_paced = d.pop("self_paced")

        has_changes = d.pop("has_changes")

        short_description = d.pop("short_description")

        _raw_start_date = d.pop("start_date")
        start_date = datetime.datetime.fromisoformat(_raw_start_date) if isinstance(_raw_start_date, str) else None

        subtitle = d.pop("subtitle")

        def _parse_syllabus(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        syllabus = _parse_syllabus(d.pop("syllabus"))

        title = d.pop("title")

        video_thumbnail_image_asset_path = d.pop("video_thumbnail_image_asset_path")

        video_thumbnail_image_name = d.pop("video_thumbnail_image_name")

        course_details = cls(
            about_sidebar_html=about_sidebar_html,
            banner_image_name=banner_image_name,
            banner_image_asset_path=banner_image_asset_path,
            certificate_available_date=certificate_available_date,
            certificates_display_behavior=certificates_display_behavior,
            course_id=course_id,
            course_image_asset_path=course_image_asset_path,
            course_image_name=course_image_name,
            description=description,
            duration=duration,
            effort=effort,
            end_date=end_date,
            enrollment_end=enrollment_end,
            enrollment_start=enrollment_start,
            entrance_exam_enabled=entrance_exam_enabled,
            entrance_exam_id=entrance_exam_id,
            entrance_exam_minimum_score_pct=entrance_exam_minimum_score_pct,
            instructor_info=instructor_info,
            intro_video=intro_video,
            language=language,
            learning_info=learning_info,
            license_=license_,
            org=org,
            overview=overview,
            pre_requisite_courses=pre_requisite_courses,
            run=run,
            self_paced=self_paced,
            has_changes=has_changes,
            short_description=short_description,
            start_date=start_date,
            subtitle=subtitle,
            syllabus=syllabus,
            title=title,
            video_thumbnail_image_asset_path=video_thumbnail_image_asset_path,
            video_thumbnail_image_name=video_thumbnail_image_name,
        )

        course_details.additional_properties = d
        return course_details

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
