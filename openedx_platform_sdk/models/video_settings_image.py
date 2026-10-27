from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.video_settings_image_supported_file_formats import VideoSettingsImageSupportedFileFormats


T = TypeVar("T", bound="VideoSettingsImage")


@_attrs_define
class VideoSettingsImage:
    """Limits that apply to video thumbnail images uploaded to the course.

    Attributes:
        video_image_upload_enabled (bool): Whether thumbnail images may be uploaded for the course's videos.
        max_size (int): Largest accepted image, in bytes.
        min_size (int): Smallest accepted image, in bytes.
        max_width (int): Largest accepted image width, in pixels.
        max_height (int): Largest accepted image height, in pixels.
        supported_file_formats (VideoSettingsImageSupportedFileFormats): Accepted image file extensions, each mapped to
            its MIME type.
    """

    video_image_upload_enabled: bool
    max_size: int
    min_size: int
    max_width: int
    max_height: int
    supported_file_formats: VideoSettingsImageSupportedFileFormats
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        video_image_upload_enabled = self.video_image_upload_enabled

        max_size = self.max_size

        min_size = self.min_size

        max_width = self.max_width

        max_height = self.max_height

        supported_file_formats = self.supported_file_formats.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "video_image_upload_enabled": video_image_upload_enabled,
                "max_size": max_size,
                "min_size": min_size,
                "max_width": max_width,
                "max_height": max_height,
                "supported_file_formats": supported_file_formats,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.video_settings_image_supported_file_formats import VideoSettingsImageSupportedFileFormats

        d = dict(src_dict)
        video_image_upload_enabled = d.pop("video_image_upload_enabled")

        max_size = d.pop("max_size")

        min_size = d.pop("min_size")

        max_width = d.pop("max_width")

        max_height = d.pop("max_height")

        supported_file_formats = VideoSettingsImageSupportedFileFormats.from_dict(d.pop("supported_file_formats"))

        video_settings_image = cls(
            video_image_upload_enabled=video_image_upload_enabled,
            max_size=max_size,
            min_size=min_size,
            max_width=max_width,
            max_height=max_height,
            supported_file_formats=supported_file_formats,
        )

        video_settings_image.additional_properties = d
        return video_settings_image

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
