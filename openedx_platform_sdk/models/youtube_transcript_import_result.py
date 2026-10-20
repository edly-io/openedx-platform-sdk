from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="YoutubeTranscriptImportResult")


@_attrs_define
class YoutubeTranscriptImportResult:
    """Outcome of importing a YouTube transcript into a video block.

    Attributes:
        edx_video_id (None | str): Video pipeline identifier the transcript was attached to. Null when the block lives
            in a content library, where transcripts are stored on the block itself.
        status (str): Outcome of the import: "Success" when the transcript was stored.
    """

    edx_video_id: None | str
    status: str
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        edx_video_id: None | str
        edx_video_id = self.edx_video_id

        status = self.status

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "edx_video_id": edx_video_id,
                "status": status,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)

        def _parse_edx_video_id(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        edx_video_id = _parse_edx_video_id(d.pop("edx_video_id"))

        status = d.pop("status")

        youtube_transcript_import_result = cls(
            edx_video_id=edx_video_id,
            status=status,
        )

        youtube_transcript_import_result.additional_properties = d
        return youtube_transcript_import_result

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
