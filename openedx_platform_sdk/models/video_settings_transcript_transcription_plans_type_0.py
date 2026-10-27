from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.video_settings_transcript_transcription_plans_type_0_additional_property import (
        VideoSettingsTranscriptTranscriptionPlansType0AdditionalProperty,
    )


T = TypeVar("T", bound="VideoSettingsTranscriptTranscriptionPlansType0")


@_attrs_define
class VideoSettingsTranscriptTranscriptionPlansType0:
    """Third-party transcription plans, keyed by provider name, with each plan's options as the provider defines them. Null
    when transcripts are disabled.

    """

    additional_properties: dict[str, VideoSettingsTranscriptTranscriptionPlansType0AdditionalProperty] = _attrs_field(
        init=False, factory=dict
    )

    def to_dict(self) -> dict[str, Any]:

        field_dict: dict[str, Any] = {}
        for prop_name, prop in self.additional_properties.items():
            field_dict[prop_name] = prop.to_dict()

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.video_settings_transcript_transcription_plans_type_0_additional_property import (
            VideoSettingsTranscriptTranscriptionPlansType0AdditionalProperty,
        )

        d = dict(src_dict)
        video_settings_transcript_transcription_plans_type_0 = cls()

        additional_properties = {}
        for prop_name, prop_dict in d.items():
            additional_property = VideoSettingsTranscriptTranscriptionPlansType0AdditionalProperty.from_dict(prop_dict)

            additional_properties[prop_name] = additional_property

        video_settings_transcript_transcription_plans_type_0.additional_properties = additional_properties
        return video_settings_transcript_transcription_plans_type_0

    @property
    def additional_keys(self) -> list[str]:
        return list(self.additional_properties.keys())

    def __getitem__(self, key: str) -> VideoSettingsTranscriptTranscriptionPlansType0AdditionalProperty:
        return self.additional_properties[key]

    def __setitem__(self, key: str, value: VideoSettingsTranscriptTranscriptionPlansType0AdditionalProperty) -> None:
        self.additional_properties[key] = value

    def __delitem__(self, key: str) -> None:
        del self.additional_properties[key]

    def __contains__(self, key: str) -> bool:
        return key in self.additional_properties
