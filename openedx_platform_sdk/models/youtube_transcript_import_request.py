from __future__ import annotations

import json
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from .. import types

if TYPE_CHECKING:
    from ..models.youtube_transcript_video import YoutubeTranscriptVideo


T = TypeVar("T", bound="YoutubeTranscriptImportRequest")


@_attrs_define
class YoutubeTranscriptImportRequest:
    """Input identifying the video block to import a YouTube transcript into.

    Attributes:
        locator (str): Usage key of the video block to import the transcript into.
        videos (list[YoutubeTranscriptVideo]): Video sources declared on the block. An entry of type "youtube" is
            required.
    """

    locator: str
    videos: list[YoutubeTranscriptVideo]
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        locator = self.locator

        videos = []
        for videos_item_data in self.videos:
            videos_item = videos_item_data.to_dict()
            videos.append(videos_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "locator": locator,
                "videos": videos,
            }
        )

        return field_dict

    def to_multipart(self) -> types.RequestFiles:
        files: types.RequestFiles = []

        files.append(("locator", (None, str(self.locator).encode(), "text/plain")))

        for videos_item_element in self.videos:
            files.append(("videos", (None, json.dumps(videos_item_element.to_dict()).encode(), "application/json")))

        for prop_name, prop in self.additional_properties.items():
            files.append((prop_name, (None, str(prop).encode(), "text/plain")))

        return files

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.youtube_transcript_video import YoutubeTranscriptVideo

        d = dict(src_dict)
        locator = d.pop("locator")

        videos = []
        _videos = d.pop("videos")
        for videos_item_data in _videos:
            videos_item = YoutubeTranscriptVideo.from_dict(videos_item_data)

            videos.append(videos_item)

        youtube_transcript_import_request = cls(
            locator=locator,
            videos=videos,
        )

        youtube_transcript_import_request.additional_properties = d
        return youtube_transcript_import_request

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
