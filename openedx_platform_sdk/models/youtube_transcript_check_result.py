from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="YoutubeTranscriptCheckResult")


@_attrs_define
class YoutubeTranscriptCheckResult:
    """Transcript availability of one video block, across its declared sources.

    Attributes:
        html5_local (list[str]): Identifiers of the HTML5 sources that already have a transcript stored for this course.
        html5_equal (bool): Whether exactly two HTML5 sources were found and their stored transcripts are identical.
        is_youtube_mode (bool): Whether the block declares a YouTube source, which takes priority over HTML5 sources.
        youtube_local (bool): Whether a transcript for the YouTube source is already stored for this course.
        youtube_server (bool): Whether YouTube is currently serving a transcript for the video.
        youtube_diff (bool): Whether the transcript on YouTube differs from the stored one.
        status (str): Outcome of the check: "Success" when the block could be inspected.
        command (str): Action the caller should take next: replace, found, import, choose, use_existing, or not_found.
        current_item_subs (None | str | Unset): Name of the transcript currently attached to the block, or null when
            none is attached.
    """

    html5_local: list[str]
    html5_equal: bool
    is_youtube_mode: bool
    youtube_local: bool
    youtube_server: bool
    youtube_diff: bool
    status: str
    command: str
    current_item_subs: None | str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        html5_local = self.html5_local

        html5_equal = self.html5_equal

        is_youtube_mode = self.is_youtube_mode

        youtube_local = self.youtube_local

        youtube_server = self.youtube_server

        youtube_diff = self.youtube_diff

        status = self.status

        command = self.command

        current_item_subs: None | str | Unset
        if isinstance(self.current_item_subs, Unset):
            current_item_subs = UNSET
        else:
            current_item_subs = self.current_item_subs

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "html5_local": html5_local,
                "html5_equal": html5_equal,
                "is_youtube_mode": is_youtube_mode,
                "youtube_local": youtube_local,
                "youtube_server": youtube_server,
                "youtube_diff": youtube_diff,
                "status": status,
                "command": command,
            }
        )
        if current_item_subs is not UNSET:
            field_dict["current_item_subs"] = current_item_subs

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        html5_local = cast(list[str], d.pop("html5_local"))

        html5_equal = d.pop("html5_equal")

        is_youtube_mode = d.pop("is_youtube_mode")

        youtube_local = d.pop("youtube_local")

        youtube_server = d.pop("youtube_server")

        youtube_diff = d.pop("youtube_diff")

        status = d.pop("status")

        command = d.pop("command")

        def _parse_current_item_subs(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        current_item_subs = _parse_current_item_subs(d.pop("current_item_subs", UNSET))

        youtube_transcript_check_result = cls(
            html5_local=html5_local,
            html5_equal=html5_equal,
            is_youtube_mode=is_youtube_mode,
            youtube_local=youtube_local,
            youtube_server=youtube_server,
            youtube_diff=youtube_diff,
            status=status,
            command=command,
            current_item_subs=current_item_subs,
        )

        youtube_transcript_check_result.additional_properties = d
        return youtube_transcript_check_result

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
