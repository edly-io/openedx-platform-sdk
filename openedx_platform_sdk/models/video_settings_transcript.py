from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.video_settings_transcript_transcription_plans_type_0 import (
        VideoSettingsTranscriptTranscriptionPlansType0,
    )


T = TypeVar("T", bound="VideoSettingsTranscript")


@_attrs_define
class VideoSettingsTranscript:
    """Studio handler addresses and options for the course's video transcripts.

    Attributes:
        transcript_download_handler_url (str): Studio address that downloads a transcript.
        transcript_upload_handler_url (str): Studio address that uploads a transcript.
        transcript_delete_handler_url (str): Studio address that deletes a transcript of this course.
        transcript_download_file_format (str): File format transcripts are downloaded in.
        transcript_preferences_handler_url (None | str): Studio address that saves the course's transcript preferences.
            Null when transcripts are disabled.
        transcript_credentials_handler_url (None | str): Studio address that saves transcript provider credentials. Null
            when transcripts are disabled.
        transcription_plans (None | VideoSettingsTranscriptTranscriptionPlansType0): Third-party transcription plans,
            keyed by provider name, with each plan's options as the provider defines them. Null when transcripts are
            disabled.
    """

    transcript_download_handler_url: str
    transcript_upload_handler_url: str
    transcript_delete_handler_url: str
    transcript_download_file_format: str
    transcript_preferences_handler_url: None | str
    transcript_credentials_handler_url: None | str
    transcription_plans: None | VideoSettingsTranscriptTranscriptionPlansType0
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.video_settings_transcript_transcription_plans_type_0 import (
            VideoSettingsTranscriptTranscriptionPlansType0,
        )

        transcript_download_handler_url = self.transcript_download_handler_url

        transcript_upload_handler_url = self.transcript_upload_handler_url

        transcript_delete_handler_url = self.transcript_delete_handler_url

        transcript_download_file_format = self.transcript_download_file_format

        transcript_preferences_handler_url: None | str
        transcript_preferences_handler_url = self.transcript_preferences_handler_url

        transcript_credentials_handler_url: None | str
        transcript_credentials_handler_url = self.transcript_credentials_handler_url

        transcription_plans: dict[str, Any] | None
        if isinstance(self.transcription_plans, VideoSettingsTranscriptTranscriptionPlansType0):
            transcription_plans = self.transcription_plans.to_dict()
        else:
            transcription_plans = self.transcription_plans

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "transcript_download_handler_url": transcript_download_handler_url,
                "transcript_upload_handler_url": transcript_upload_handler_url,
                "transcript_delete_handler_url": transcript_delete_handler_url,
                "transcript_download_file_format": transcript_download_file_format,
                "transcript_preferences_handler_url": transcript_preferences_handler_url,
                "transcript_credentials_handler_url": transcript_credentials_handler_url,
                "transcription_plans": transcription_plans,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.video_settings_transcript_transcription_plans_type_0 import (
            VideoSettingsTranscriptTranscriptionPlansType0,
        )

        d = dict(src_dict)
        transcript_download_handler_url = d.pop("transcript_download_handler_url")

        transcript_upload_handler_url = d.pop("transcript_upload_handler_url")

        transcript_delete_handler_url = d.pop("transcript_delete_handler_url")

        transcript_download_file_format = d.pop("transcript_download_file_format")

        def _parse_transcript_preferences_handler_url(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        transcript_preferences_handler_url = _parse_transcript_preferences_handler_url(
            d.pop("transcript_preferences_handler_url")
        )

        def _parse_transcript_credentials_handler_url(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        transcript_credentials_handler_url = _parse_transcript_credentials_handler_url(
            d.pop("transcript_credentials_handler_url")
        )

        def _parse_transcription_plans(data: object) -> None | VideoSettingsTranscriptTranscriptionPlansType0:
            if data is None:
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                transcription_plans_type_0 = VideoSettingsTranscriptTranscriptionPlansType0.from_dict(data)

                return transcription_plans_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | VideoSettingsTranscriptTranscriptionPlansType0, data)

        transcription_plans = _parse_transcription_plans(d.pop("transcription_plans"))

        video_settings_transcript = cls(
            transcript_download_handler_url=transcript_download_handler_url,
            transcript_upload_handler_url=transcript_upload_handler_url,
            transcript_delete_handler_url=transcript_delete_handler_url,
            transcript_download_file_format=transcript_download_file_format,
            transcript_preferences_handler_url=transcript_preferences_handler_url,
            transcript_credentials_handler_url=transcript_credentials_handler_url,
            transcription_plans=transcription_plans,
        )

        video_settings_transcript.additional_properties = d
        return video_settings_transcript

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
