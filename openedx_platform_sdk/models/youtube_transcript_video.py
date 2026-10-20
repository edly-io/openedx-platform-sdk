from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="YoutubeTranscriptVideo")


@_attrs_define
class YoutubeTranscriptVideo:
    """One entry of the video list identifying a source to inspect or import from.

    Attributes:
        type_ (str): Source kind. "youtube" names a YouTube video id, "edx_video_id" names a video in the video
            pipeline, and any other value is treated as an HTML5 source.
        video (str): Identifier of the source, interpreted according to the type field.
        mode (str | Unset): Playback mode of an HTML5 source, such as "mp4" or "webm".
    """

    type_: str
    video: str
    mode: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        type_ = self.type_

        video = self.video

        mode = self.mode

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "type": type_,
                "video": video,
            }
        )
        if mode is not UNSET:
            field_dict["mode"] = mode

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        type_ = d.pop("type")

        video = d.pop("video")

        mode = d.pop("mode", UNSET)

        youtube_transcript_video = cls(
            type_=type_,
            video=video,
            mode=mode,
        )

        youtube_transcript_video.additional_properties = d
        return youtube_transcript_video

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
