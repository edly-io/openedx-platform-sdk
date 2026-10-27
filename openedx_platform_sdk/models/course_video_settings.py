from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.course_video_settings_transcript_credentials_type_0 import (
        CourseVideoSettingsTranscriptCredentialsType0,
    )
    from ..models.transcript_language import TranscriptLanguage
    from ..models.video_settings_image import VideoSettingsImage
    from ..models.video_settings_transcript import VideoSettingsTranscript
    from ..models.video_settings_transcript_preferences import VideoSettingsTranscriptPreferences


T = TypeVar("T", bound="CourseVideoSettings")


@_attrs_define
class CourseVideoSettings:
    """The course's video upload and transcript settings.

    Attributes:
        image_upload_url (str): Studio address that uploads a video's thumbnail image.
        video_handler_url (str): Studio address that manages the course's video uploads.
        encodings_download_url (str): Studio address that downloads the course's video encodings as CSV.
        default_video_image_url (str): Address of the image shown for videos without one.
        concurrent_upload_limit (int): How many videos a client may upload at the same time.
        video_supported_file_formats (list[str]): Accepted video file extensions.
        video_upload_max_file_size (int): Largest accepted video file, in gigabytes.
        video_image_settings (VideoSettingsImage): Limits that apply to video thumbnail images uploaded to the course.
        is_video_transcript_enabled (bool): Whether third-party transcription is enabled for the course.
        is_ai_translations_enabled (bool): Whether AI translation of transcripts is enabled for the course.
        active_transcript_preferences (None | VideoSettingsTranscriptPreferences): The course's transcription
            preferences. Null when transcripts are disabled or none are saved.
        transcript_credentials (CourseVideoSettingsTranscriptCredentialsType0 | None): Whether the course's organization
            has credentials for each transcription provider, keyed by provider name. Null when transcripts are disabled.
        transcript_available_languages (list[TranscriptLanguage]): Every language a transcript may be written in,
            ordered by display name.
        video_transcript_settings (VideoSettingsTranscript): Studio handler addresses and options for the course's video
            transcripts.
    """

    image_upload_url: str
    video_handler_url: str
    encodings_download_url: str
    default_video_image_url: str
    concurrent_upload_limit: int
    video_supported_file_formats: list[str]
    video_upload_max_file_size: int
    video_image_settings: VideoSettingsImage
    is_video_transcript_enabled: bool
    is_ai_translations_enabled: bool
    active_transcript_preferences: None | VideoSettingsTranscriptPreferences
    transcript_credentials: CourseVideoSettingsTranscriptCredentialsType0 | None
    transcript_available_languages: list[TranscriptLanguage]
    video_transcript_settings: VideoSettingsTranscript
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.course_video_settings_transcript_credentials_type_0 import (
            CourseVideoSettingsTranscriptCredentialsType0,
        )
        from ..models.video_settings_transcript_preferences import VideoSettingsTranscriptPreferences

        image_upload_url = self.image_upload_url

        video_handler_url = self.video_handler_url

        encodings_download_url = self.encodings_download_url

        default_video_image_url = self.default_video_image_url

        concurrent_upload_limit = self.concurrent_upload_limit

        video_supported_file_formats = self.video_supported_file_formats

        video_upload_max_file_size = self.video_upload_max_file_size

        video_image_settings = self.video_image_settings.to_dict()

        is_video_transcript_enabled = self.is_video_transcript_enabled

        is_ai_translations_enabled = self.is_ai_translations_enabled

        active_transcript_preferences: dict[str, Any] | None
        if isinstance(self.active_transcript_preferences, VideoSettingsTranscriptPreferences):
            active_transcript_preferences = self.active_transcript_preferences.to_dict()
        else:
            active_transcript_preferences = self.active_transcript_preferences

        transcript_credentials: dict[str, Any] | None
        if isinstance(self.transcript_credentials, CourseVideoSettingsTranscriptCredentialsType0):
            transcript_credentials = self.transcript_credentials.to_dict()
        else:
            transcript_credentials = self.transcript_credentials

        transcript_available_languages = []
        for transcript_available_languages_item_data in self.transcript_available_languages:
            transcript_available_languages_item = transcript_available_languages_item_data.to_dict()
            transcript_available_languages.append(transcript_available_languages_item)

        video_transcript_settings = self.video_transcript_settings.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "image_upload_url": image_upload_url,
                "video_handler_url": video_handler_url,
                "encodings_download_url": encodings_download_url,
                "default_video_image_url": default_video_image_url,
                "concurrent_upload_limit": concurrent_upload_limit,
                "video_supported_file_formats": video_supported_file_formats,
                "video_upload_max_file_size": video_upload_max_file_size,
                "video_image_settings": video_image_settings,
                "is_video_transcript_enabled": is_video_transcript_enabled,
                "is_ai_translations_enabled": is_ai_translations_enabled,
                "active_transcript_preferences": active_transcript_preferences,
                "transcript_credentials": transcript_credentials,
                "transcript_available_languages": transcript_available_languages,
                "video_transcript_settings": video_transcript_settings,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.course_video_settings_transcript_credentials_type_0 import (
            CourseVideoSettingsTranscriptCredentialsType0,
        )
        from ..models.transcript_language import TranscriptLanguage
        from ..models.video_settings_image import VideoSettingsImage
        from ..models.video_settings_transcript import VideoSettingsTranscript
        from ..models.video_settings_transcript_preferences import VideoSettingsTranscriptPreferences

        d = dict(src_dict)
        image_upload_url = d.pop("image_upload_url")

        video_handler_url = d.pop("video_handler_url")

        encodings_download_url = d.pop("encodings_download_url")

        default_video_image_url = d.pop("default_video_image_url")

        concurrent_upload_limit = d.pop("concurrent_upload_limit")

        video_supported_file_formats = cast(list[str], d.pop("video_supported_file_formats"))

        video_upload_max_file_size = d.pop("video_upload_max_file_size")

        video_image_settings = VideoSettingsImage.from_dict(d.pop("video_image_settings"))

        is_video_transcript_enabled = d.pop("is_video_transcript_enabled")

        is_ai_translations_enabled = d.pop("is_ai_translations_enabled")

        def _parse_active_transcript_preferences(data: object) -> None | VideoSettingsTranscriptPreferences:
            if data is None:
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                active_transcript_preferences_type_1 = VideoSettingsTranscriptPreferences.from_dict(data)

                return active_transcript_preferences_type_1
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | VideoSettingsTranscriptPreferences, data)

        active_transcript_preferences = _parse_active_transcript_preferences(d.pop("active_transcript_preferences"))

        def _parse_transcript_credentials(data: object) -> CourseVideoSettingsTranscriptCredentialsType0 | None:
            if data is None:
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                transcript_credentials_type_0 = CourseVideoSettingsTranscriptCredentialsType0.from_dict(data)

                return transcript_credentials_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(CourseVideoSettingsTranscriptCredentialsType0 | None, data)

        transcript_credentials = _parse_transcript_credentials(d.pop("transcript_credentials"))

        transcript_available_languages = []
        _transcript_available_languages = d.pop("transcript_available_languages")
        for transcript_available_languages_item_data in _transcript_available_languages:
            transcript_available_languages_item = TranscriptLanguage.from_dict(transcript_available_languages_item_data)

            transcript_available_languages.append(transcript_available_languages_item)

        video_transcript_settings = VideoSettingsTranscript.from_dict(d.pop("video_transcript_settings"))

        course_video_settings = cls(
            image_upload_url=image_upload_url,
            video_handler_url=video_handler_url,
            encodings_download_url=encodings_download_url,
            default_video_image_url=default_video_image_url,
            concurrent_upload_limit=concurrent_upload_limit,
            video_supported_file_formats=video_supported_file_formats,
            video_upload_max_file_size=video_upload_max_file_size,
            video_image_settings=video_image_settings,
            is_video_transcript_enabled=is_video_transcript_enabled,
            is_ai_translations_enabled=is_ai_translations_enabled,
            active_transcript_preferences=active_transcript_preferences,
            transcript_credentials=transcript_credentials,
            transcript_available_languages=transcript_available_languages,
            video_transcript_settings=video_transcript_settings,
        )

        course_video_settings.additional_properties = d
        return course_video_settings

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
