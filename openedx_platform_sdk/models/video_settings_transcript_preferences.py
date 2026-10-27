from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="VideoSettingsTranscriptPreferences")


@_attrs_define
class VideoSettingsTranscriptPreferences:
    """The course's saved preferences for third-party transcription.

    Attributes:
        course_id (str): Key of the course the preferences belong to.
        provider (str): Transcription provider.
        cielo24_fidelity (None | str): Cielo24 fidelity level, when Cielo24 is used.
        cielo24_turnaround (None | str): Cielo24 turnaround, when Cielo24 is used.
        three_play_turnaround (None | str): 3Play Media turnaround, when 3Play Media is used.
        preferred_languages (list[str]): Language codes transcripts are requested in.
        video_source_language (None | str): Language code of the videos' spoken language.
        modified (str): When the preferences were last changed.
    """

    course_id: str
    provider: str
    cielo24_fidelity: None | str
    cielo24_turnaround: None | str
    three_play_turnaround: None | str
    preferred_languages: list[str]
    video_source_language: None | str
    modified: str
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        course_id = self.course_id

        provider = self.provider

        cielo24_fidelity: None | str
        cielo24_fidelity = self.cielo24_fidelity

        cielo24_turnaround: None | str
        cielo24_turnaround = self.cielo24_turnaround

        three_play_turnaround: None | str
        three_play_turnaround = self.three_play_turnaround

        preferred_languages = self.preferred_languages

        video_source_language: None | str
        video_source_language = self.video_source_language

        modified = self.modified

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "course_id": course_id,
                "provider": provider,
                "cielo24_fidelity": cielo24_fidelity,
                "cielo24_turnaround": cielo24_turnaround,
                "three_play_turnaround": three_play_turnaround,
                "preferred_languages": preferred_languages,
                "video_source_language": video_source_language,
                "modified": modified,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        course_id = d.pop("course_id")

        provider = d.pop("provider")

        def _parse_cielo24_fidelity(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        cielo24_fidelity = _parse_cielo24_fidelity(d.pop("cielo24_fidelity"))

        def _parse_cielo24_turnaround(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        cielo24_turnaround = _parse_cielo24_turnaround(d.pop("cielo24_turnaround"))

        def _parse_three_play_turnaround(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        three_play_turnaround = _parse_three_play_turnaround(d.pop("three_play_turnaround"))

        preferred_languages = cast(list[str], d.pop("preferred_languages"))

        def _parse_video_source_language(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        video_source_language = _parse_video_source_language(d.pop("video_source_language"))

        modified = d.pop("modified")

        video_settings_transcript_preferences = cls(
            course_id=course_id,
            provider=provider,
            cielo24_fidelity=cielo24_fidelity,
            cielo24_turnaround=cielo24_turnaround,
            three_play_turnaround=three_play_turnaround,
            preferred_languages=preferred_languages,
            video_source_language=video_source_language,
            modified=modified,
        )

        video_settings_transcript_preferences.additional_properties = d
        return video_settings_transcript_preferences

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
