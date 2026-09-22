from __future__ import annotations

import json
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from .. import types
from ..models.publish_enum import PublishEnum
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.patched_xblock_actions_type_0 import PatchedXblockActionsType0
    from ..models.patched_xblock_fields_type_0 import PatchedXblockFieldsType0
    from ..models.patched_xblock_group_access_type_0 import PatchedXblockGroupAccessType0
    from ..models.patched_xblock_metadata_type_0 import PatchedXblockMetadataType0
    from ..models.patched_xblock_user_partition_info_type_0 import PatchedXblockUserPartitionInfoType0


T = TypeVar("T", bound="PatchedXblock")


@_attrs_define
class PatchedXblock:
    """A serializer for xblocks that enforces strict validation.

    The serializer ensures:
    1. All top-level fields have the expected data types.
    2. No unexpected fields are passed in.

    Note: The current list of fields is not exhaustive. It is primarily designed
    to support the CMS API demo. While optional fields have been added, they were
    chosen based on ease of discovery, not comprehensiveness.

        Attributes:
            id (None | str | Unset):
            parent_locator (None | str | Unset):
            display_name (None | str | Unset):
            category (None | str | Unset):
            data (None | str | Unset):
            metadata (None | PatchedXblockMetadataType0 | Unset):
            has_changes (bool | None | Unset):
            children (list[Any] | None | Unset):
            fields (None | PatchedXblockFieldsType0 | Unset):
            has_children (bool | None | Unset):
            video_sharing_enabled (bool | None | Unset):
            video_sharing_options (None | str | Unset):
            video_sharing_doc_url (None | str | Unset):
            edited_on (None | str | Unset):
            published (bool | None | Unset):
            published_on (Any | Unset):
            studio_url (None | str | Unset):
            released_to_students (bool | None | Unset):
            release_date (Any | Unset):
            nullout (Any | Unset):
            grader_type (Any | Unset):
            visibility_state (None | str | Unset):
            has_explicit_staff_lock (bool | None | Unset):
            start (None | str | Unset):
            graded (bool | None | Unset):
            due_date (None | str | Unset):
            due (Any | Unset):
            relative_weeks_due (Any | Unset):
            format_ (Any | Unset):
            course_graders (list[Any] | None | Unset):
            actions (None | PatchedXblockActionsType0 | Unset):
            explanatory_message (None | str | Unset):
            group_access (None | PatchedXblockGroupAccessType0 | Unset):
            user_partitions (list[Any] | None | Unset):
            show_correctness (None | str | Unset):
            discussion_enabled (bool | None | Unset):
            ancestor_has_staff_lock (bool | None | Unset):
            user_partition_info (None | PatchedXblockUserPartitionInfoType0 | Unset):
            summary_configuration_enabled (Any | Unset):
            is_prereq (bool | None | Unset):
            prereq_usage_key (None | str | Unset):
            prereq_min_score (int | None | Unset):
            prereq_min_completion (int | None | Unset):
            publish (None | PublishEnum | Unset):
            duplicate_source_locator (None | str | Unset):
            move_source_locator (None | str | Unset):
            target_index (int | None | Unset):
            boilerplate (Any | Unset):
            staged_content (None | str | Unset):
            hide_from_toc (bool | None | Unset):
    """

    id: None | str | Unset = UNSET
    parent_locator: None | str | Unset = UNSET
    display_name: None | str | Unset = UNSET
    category: None | str | Unset = UNSET
    data: None | str | Unset = UNSET
    metadata: None | PatchedXblockMetadataType0 | Unset = UNSET
    has_changes: bool | None | Unset = UNSET
    children: list[Any] | None | Unset = UNSET
    fields: None | PatchedXblockFieldsType0 | Unset = UNSET
    has_children: bool | None | Unset = UNSET
    video_sharing_enabled: bool | None | Unset = UNSET
    video_sharing_options: None | str | Unset = UNSET
    video_sharing_doc_url: None | str | Unset = UNSET
    edited_on: None | str | Unset = UNSET
    published: bool | None | Unset = UNSET
    published_on: Any | Unset = UNSET
    studio_url: None | str | Unset = UNSET
    released_to_students: bool | None | Unset = UNSET
    release_date: Any | Unset = UNSET
    nullout: Any | Unset = UNSET
    grader_type: Any | Unset = UNSET
    visibility_state: None | str | Unset = UNSET
    has_explicit_staff_lock: bool | None | Unset = UNSET
    start: None | str | Unset = UNSET
    graded: bool | None | Unset = UNSET
    due_date: None | str | Unset = UNSET
    due: Any | Unset = UNSET
    relative_weeks_due: Any | Unset = UNSET
    format_: Any | Unset = UNSET
    course_graders: list[Any] | None | Unset = UNSET
    actions: None | PatchedXblockActionsType0 | Unset = UNSET
    explanatory_message: None | str | Unset = UNSET
    group_access: None | PatchedXblockGroupAccessType0 | Unset = UNSET
    user_partitions: list[Any] | None | Unset = UNSET
    show_correctness: None | str | Unset = UNSET
    discussion_enabled: bool | None | Unset = UNSET
    ancestor_has_staff_lock: bool | None | Unset = UNSET
    user_partition_info: None | PatchedXblockUserPartitionInfoType0 | Unset = UNSET
    summary_configuration_enabled: Any | Unset = UNSET
    is_prereq: bool | None | Unset = UNSET
    prereq_usage_key: None | str | Unset = UNSET
    prereq_min_score: int | None | Unset = UNSET
    prereq_min_completion: int | None | Unset = UNSET
    publish: None | PublishEnum | Unset = UNSET
    duplicate_source_locator: None | str | Unset = UNSET
    move_source_locator: None | str | Unset = UNSET
    target_index: int | None | Unset = UNSET
    boilerplate: Any | Unset = UNSET
    staged_content: None | str | Unset = UNSET
    hide_from_toc: bool | None | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.patched_xblock_actions_type_0 import PatchedXblockActionsType0
        from ..models.patched_xblock_fields_type_0 import PatchedXblockFieldsType0
        from ..models.patched_xblock_group_access_type_0 import PatchedXblockGroupAccessType0
        from ..models.patched_xblock_metadata_type_0 import PatchedXblockMetadataType0
        from ..models.patched_xblock_user_partition_info_type_0 import PatchedXblockUserPartitionInfoType0

        id: None | str | Unset
        if isinstance(self.id, Unset):
            id = UNSET
        else:
            id = self.id

        parent_locator: None | str | Unset
        if isinstance(self.parent_locator, Unset):
            parent_locator = UNSET
        else:
            parent_locator = self.parent_locator

        display_name: None | str | Unset
        if isinstance(self.display_name, Unset):
            display_name = UNSET
        else:
            display_name = self.display_name

        category: None | str | Unset
        if isinstance(self.category, Unset):
            category = UNSET
        else:
            category = self.category

        data: None | str | Unset
        if isinstance(self.data, Unset):
            data = UNSET
        else:
            data = self.data

        metadata: dict[str, Any] | None | Unset
        if isinstance(self.metadata, Unset):
            metadata = UNSET
        elif isinstance(self.metadata, PatchedXblockMetadataType0):
            metadata = self.metadata.to_dict()
        else:
            metadata = self.metadata

        has_changes: bool | None | Unset
        if isinstance(self.has_changes, Unset):
            has_changes = UNSET
        else:
            has_changes = self.has_changes

        children: list[Any] | None | Unset
        if isinstance(self.children, Unset):
            children = UNSET
        elif isinstance(self.children, list):
            children = self.children

        else:
            children = self.children

        fields: dict[str, Any] | None | Unset
        if isinstance(self.fields, Unset):
            fields = UNSET
        elif isinstance(self.fields, PatchedXblockFieldsType0):
            fields = self.fields.to_dict()
        else:
            fields = self.fields

        has_children: bool | None | Unset
        if isinstance(self.has_children, Unset):
            has_children = UNSET
        else:
            has_children = self.has_children

        video_sharing_enabled: bool | None | Unset
        if isinstance(self.video_sharing_enabled, Unset):
            video_sharing_enabled = UNSET
        else:
            video_sharing_enabled = self.video_sharing_enabled

        video_sharing_options: None | str | Unset
        if isinstance(self.video_sharing_options, Unset):
            video_sharing_options = UNSET
        else:
            video_sharing_options = self.video_sharing_options

        video_sharing_doc_url: None | str | Unset
        if isinstance(self.video_sharing_doc_url, Unset):
            video_sharing_doc_url = UNSET
        else:
            video_sharing_doc_url = self.video_sharing_doc_url

        edited_on: None | str | Unset
        if isinstance(self.edited_on, Unset):
            edited_on = UNSET
        else:
            edited_on = self.edited_on

        published: bool | None | Unset
        if isinstance(self.published, Unset):
            published = UNSET
        else:
            published = self.published

        published_on = self.published_on

        studio_url: None | str | Unset
        if isinstance(self.studio_url, Unset):
            studio_url = UNSET
        else:
            studio_url = self.studio_url

        released_to_students: bool | None | Unset
        if isinstance(self.released_to_students, Unset):
            released_to_students = UNSET
        else:
            released_to_students = self.released_to_students

        release_date = self.release_date

        nullout = self.nullout

        grader_type = self.grader_type

        visibility_state: None | str | Unset
        if isinstance(self.visibility_state, Unset):
            visibility_state = UNSET
        else:
            visibility_state = self.visibility_state

        has_explicit_staff_lock: bool | None | Unset
        if isinstance(self.has_explicit_staff_lock, Unset):
            has_explicit_staff_lock = UNSET
        else:
            has_explicit_staff_lock = self.has_explicit_staff_lock

        start: None | str | Unset
        if isinstance(self.start, Unset):
            start = UNSET
        else:
            start = self.start

        graded: bool | None | Unset
        if isinstance(self.graded, Unset):
            graded = UNSET
        else:
            graded = self.graded

        due_date: None | str | Unset
        if isinstance(self.due_date, Unset):
            due_date = UNSET
        else:
            due_date = self.due_date

        due = self.due

        relative_weeks_due = self.relative_weeks_due

        format_ = self.format_

        course_graders: list[Any] | None | Unset
        if isinstance(self.course_graders, Unset):
            course_graders = UNSET
        elif isinstance(self.course_graders, list):
            course_graders = self.course_graders

        else:
            course_graders = self.course_graders

        actions: dict[str, Any] | None | Unset
        if isinstance(self.actions, Unset):
            actions = UNSET
        elif isinstance(self.actions, PatchedXblockActionsType0):
            actions = self.actions.to_dict()
        else:
            actions = self.actions

        explanatory_message: None | str | Unset
        if isinstance(self.explanatory_message, Unset):
            explanatory_message = UNSET
        else:
            explanatory_message = self.explanatory_message

        group_access: dict[str, Any] | None | Unset
        if isinstance(self.group_access, Unset):
            group_access = UNSET
        elif isinstance(self.group_access, PatchedXblockGroupAccessType0):
            group_access = self.group_access.to_dict()
        else:
            group_access = self.group_access

        user_partitions: list[Any] | None | Unset
        if isinstance(self.user_partitions, Unset):
            user_partitions = UNSET
        elif isinstance(self.user_partitions, list):
            user_partitions = self.user_partitions

        else:
            user_partitions = self.user_partitions

        show_correctness: None | str | Unset
        if isinstance(self.show_correctness, Unset):
            show_correctness = UNSET
        else:
            show_correctness = self.show_correctness

        discussion_enabled: bool | None | Unset
        if isinstance(self.discussion_enabled, Unset):
            discussion_enabled = UNSET
        else:
            discussion_enabled = self.discussion_enabled

        ancestor_has_staff_lock: bool | None | Unset
        if isinstance(self.ancestor_has_staff_lock, Unset):
            ancestor_has_staff_lock = UNSET
        else:
            ancestor_has_staff_lock = self.ancestor_has_staff_lock

        user_partition_info: dict[str, Any] | None | Unset
        if isinstance(self.user_partition_info, Unset):
            user_partition_info = UNSET
        elif isinstance(self.user_partition_info, PatchedXblockUserPartitionInfoType0):
            user_partition_info = self.user_partition_info.to_dict()
        else:
            user_partition_info = self.user_partition_info

        summary_configuration_enabled = self.summary_configuration_enabled

        is_prereq: bool | None | Unset
        if isinstance(self.is_prereq, Unset):
            is_prereq = UNSET
        else:
            is_prereq = self.is_prereq

        prereq_usage_key: None | str | Unset
        if isinstance(self.prereq_usage_key, Unset):
            prereq_usage_key = UNSET
        else:
            prereq_usage_key = self.prereq_usage_key

        prereq_min_score: int | None | Unset
        if isinstance(self.prereq_min_score, Unset):
            prereq_min_score = UNSET
        else:
            prereq_min_score = self.prereq_min_score

        prereq_min_completion: int | None | Unset
        if isinstance(self.prereq_min_completion, Unset):
            prereq_min_completion = UNSET
        else:
            prereq_min_completion = self.prereq_min_completion

        publish: None | str | Unset
        if isinstance(self.publish, Unset):
            publish = UNSET
        elif isinstance(self.publish, PublishEnum):
            publish = self.publish.value
        else:
            publish = self.publish

        duplicate_source_locator: None | str | Unset
        if isinstance(self.duplicate_source_locator, Unset):
            duplicate_source_locator = UNSET
        else:
            duplicate_source_locator = self.duplicate_source_locator

        move_source_locator: None | str | Unset
        if isinstance(self.move_source_locator, Unset):
            move_source_locator = UNSET
        else:
            move_source_locator = self.move_source_locator

        target_index: int | None | Unset
        if isinstance(self.target_index, Unset):
            target_index = UNSET
        else:
            target_index = self.target_index

        boilerplate = self.boilerplate

        staged_content: None | str | Unset
        if isinstance(self.staged_content, Unset):
            staged_content = UNSET
        else:
            staged_content = self.staged_content

        hide_from_toc: bool | None | Unset
        if isinstance(self.hide_from_toc, Unset):
            hide_from_toc = UNSET
        else:
            hide_from_toc = self.hide_from_toc

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if id is not UNSET:
            field_dict["id"] = id
        if parent_locator is not UNSET:
            field_dict["parent_locator"] = parent_locator
        if display_name is not UNSET:
            field_dict["display_name"] = display_name
        if category is not UNSET:
            field_dict["category"] = category
        if data is not UNSET:
            field_dict["data"] = data
        if metadata is not UNSET:
            field_dict["metadata"] = metadata
        if has_changes is not UNSET:
            field_dict["has_changes"] = has_changes
        if children is not UNSET:
            field_dict["children"] = children
        if fields is not UNSET:
            field_dict["fields"] = fields
        if has_children is not UNSET:
            field_dict["has_children"] = has_children
        if video_sharing_enabled is not UNSET:
            field_dict["video_sharing_enabled"] = video_sharing_enabled
        if video_sharing_options is not UNSET:
            field_dict["video_sharing_options"] = video_sharing_options
        if video_sharing_doc_url is not UNSET:
            field_dict["video_sharing_doc_url"] = video_sharing_doc_url
        if edited_on is not UNSET:
            field_dict["edited_on"] = edited_on
        if published is not UNSET:
            field_dict["published"] = published
        if published_on is not UNSET:
            field_dict["published_on"] = published_on
        if studio_url is not UNSET:
            field_dict["studio_url"] = studio_url
        if released_to_students is not UNSET:
            field_dict["released_to_students"] = released_to_students
        if release_date is not UNSET:
            field_dict["release_date"] = release_date
        if nullout is not UNSET:
            field_dict["nullout"] = nullout
        if grader_type is not UNSET:
            field_dict["graderType"] = grader_type
        if visibility_state is not UNSET:
            field_dict["visibility_state"] = visibility_state
        if has_explicit_staff_lock is not UNSET:
            field_dict["has_explicit_staff_lock"] = has_explicit_staff_lock
        if start is not UNSET:
            field_dict["start"] = start
        if graded is not UNSET:
            field_dict["graded"] = graded
        if due_date is not UNSET:
            field_dict["due_date"] = due_date
        if due is not UNSET:
            field_dict["due"] = due
        if relative_weeks_due is not UNSET:
            field_dict["relative_weeks_due"] = relative_weeks_due
        if format_ is not UNSET:
            field_dict["format"] = format_
        if course_graders is not UNSET:
            field_dict["course_graders"] = course_graders
        if actions is not UNSET:
            field_dict["actions"] = actions
        if explanatory_message is not UNSET:
            field_dict["explanatory_message"] = explanatory_message
        if group_access is not UNSET:
            field_dict["group_access"] = group_access
        if user_partitions is not UNSET:
            field_dict["user_partitions"] = user_partitions
        if show_correctness is not UNSET:
            field_dict["show_correctness"] = show_correctness
        if discussion_enabled is not UNSET:
            field_dict["discussion_enabled"] = discussion_enabled
        if ancestor_has_staff_lock is not UNSET:
            field_dict["ancestor_has_staff_lock"] = ancestor_has_staff_lock
        if user_partition_info is not UNSET:
            field_dict["user_partition_info"] = user_partition_info
        if summary_configuration_enabled is not UNSET:
            field_dict["summary_configuration_enabled"] = summary_configuration_enabled
        if is_prereq is not UNSET:
            field_dict["isPrereq"] = is_prereq
        if prereq_usage_key is not UNSET:
            field_dict["prereqUsageKey"] = prereq_usage_key
        if prereq_min_score is not UNSET:
            field_dict["prereqMinScore"] = prereq_min_score
        if prereq_min_completion is not UNSET:
            field_dict["prereqMinCompletion"] = prereq_min_completion
        if publish is not UNSET:
            field_dict["publish"] = publish
        if duplicate_source_locator is not UNSET:
            field_dict["duplicate_source_locator"] = duplicate_source_locator
        if move_source_locator is not UNSET:
            field_dict["move_source_locator"] = move_source_locator
        if target_index is not UNSET:
            field_dict["target_index"] = target_index
        if boilerplate is not UNSET:
            field_dict["boilerplate"] = boilerplate
        if staged_content is not UNSET:
            field_dict["staged_content"] = staged_content
        if hide_from_toc is not UNSET:
            field_dict["hide_from_toc"] = hide_from_toc

        return field_dict

    def to_multipart(self) -> types.RequestFiles:
        from ..models.patched_xblock_actions_type_0 import PatchedXblockActionsType0
        from ..models.patched_xblock_fields_type_0 import PatchedXblockFieldsType0
        from ..models.patched_xblock_group_access_type_0 import PatchedXblockGroupAccessType0
        from ..models.patched_xblock_metadata_type_0 import PatchedXblockMetadataType0
        from ..models.patched_xblock_user_partition_info_type_0 import PatchedXblockUserPartitionInfoType0

        files: types.RequestFiles = []

        if not isinstance(self.id, Unset):
            if isinstance(self.id, str):
                files.append(("id", (None, str(self.id).encode(), "text/plain")))
            else:
                files.append(("id", (None, str(self.id).encode(), "text/plain")))

        if not isinstance(self.parent_locator, Unset):
            if isinstance(self.parent_locator, str):
                files.append(("parent_locator", (None, str(self.parent_locator).encode(), "text/plain")))
            else:
                files.append(("parent_locator", (None, str(self.parent_locator).encode(), "text/plain")))

        if not isinstance(self.display_name, Unset):
            if isinstance(self.display_name, str):
                files.append(("display_name", (None, str(self.display_name).encode(), "text/plain")))
            else:
                files.append(("display_name", (None, str(self.display_name).encode(), "text/plain")))

        if not isinstance(self.category, Unset):
            if isinstance(self.category, str):
                files.append(("category", (None, str(self.category).encode(), "text/plain")))
            else:
                files.append(("category", (None, str(self.category).encode(), "text/plain")))

        if not isinstance(self.data, Unset):
            if isinstance(self.data, str):
                files.append(("data", (None, str(self.data).encode(), "text/plain")))
            else:
                files.append(("data", (None, str(self.data).encode(), "text/plain")))

        if not isinstance(self.metadata, Unset):
            if isinstance(self.metadata, PatchedXblockMetadataType0):
                files.append(("metadata", (None, json.dumps(self.metadata.to_dict()).encode(), "application/json")))
            else:
                files.append(("metadata", (None, str(self.metadata).encode(), "text/plain")))

        if not isinstance(self.has_changes, Unset):
            if isinstance(self.has_changes, bool):
                files.append(("has_changes", (None, str(self.has_changes).encode(), "text/plain")))
            else:
                files.append(("has_changes", (None, str(self.has_changes).encode(), "text/plain")))

        if not isinstance(self.children, Unset):
            if isinstance(self.children, list):
                for children_type_0_item_element in self.children:
                    files.append(("children", (None, str(children_type_0_item_element).encode(), "text/plain")))
            else:
                files.append(("children", (None, str(self.children).encode(), "text/plain")))

        if not isinstance(self.fields, Unset):
            if isinstance(self.fields, PatchedXblockFieldsType0):
                files.append(("fields", (None, json.dumps(self.fields.to_dict()).encode(), "application/json")))
            else:
                files.append(("fields", (None, str(self.fields).encode(), "text/plain")))

        if not isinstance(self.has_children, Unset):
            if isinstance(self.has_children, bool):
                files.append(("has_children", (None, str(self.has_children).encode(), "text/plain")))
            else:
                files.append(("has_children", (None, str(self.has_children).encode(), "text/plain")))

        if not isinstance(self.video_sharing_enabled, Unset):
            if isinstance(self.video_sharing_enabled, bool):
                files.append(("video_sharing_enabled", (None, str(self.video_sharing_enabled).encode(), "text/plain")))
            else:
                files.append(("video_sharing_enabled", (None, str(self.video_sharing_enabled).encode(), "text/plain")))

        if not isinstance(self.video_sharing_options, Unset):
            if isinstance(self.video_sharing_options, str):
                files.append(("video_sharing_options", (None, str(self.video_sharing_options).encode(), "text/plain")))
            else:
                files.append(("video_sharing_options", (None, str(self.video_sharing_options).encode(), "text/plain")))

        if not isinstance(self.video_sharing_doc_url, Unset):
            if isinstance(self.video_sharing_doc_url, str):
                files.append(("video_sharing_doc_url", (None, str(self.video_sharing_doc_url).encode(), "text/plain")))
            else:
                files.append(("video_sharing_doc_url", (None, str(self.video_sharing_doc_url).encode(), "text/plain")))

        if not isinstance(self.edited_on, Unset):
            if isinstance(self.edited_on, str):
                files.append(("edited_on", (None, str(self.edited_on).encode(), "text/plain")))
            else:
                files.append(("edited_on", (None, str(self.edited_on).encode(), "text/plain")))

        if not isinstance(self.published, Unset):
            if isinstance(self.published, bool):
                files.append(("published", (None, str(self.published).encode(), "text/plain")))
            else:
                files.append(("published", (None, str(self.published).encode(), "text/plain")))

        if not isinstance(self.published_on, Unset):
            files.append(("published_on", (None, str(self.published_on).encode(), "text/plain")))

        if not isinstance(self.studio_url, Unset):
            if isinstance(self.studio_url, str):
                files.append(("studio_url", (None, str(self.studio_url).encode(), "text/plain")))
            else:
                files.append(("studio_url", (None, str(self.studio_url).encode(), "text/plain")))

        if not isinstance(self.released_to_students, Unset):
            if isinstance(self.released_to_students, bool):
                files.append(("released_to_students", (None, str(self.released_to_students).encode(), "text/plain")))
            else:
                files.append(("released_to_students", (None, str(self.released_to_students).encode(), "text/plain")))

        if not isinstance(self.release_date, Unset):
            files.append(("release_date", (None, str(self.release_date).encode(), "text/plain")))

        if not isinstance(self.nullout, Unset):
            files.append(("nullout", (None, str(self.nullout).encode(), "text/plain")))

        if not isinstance(self.grader_type, Unset):
            files.append(("graderType", (None, str(self.grader_type).encode(), "text/plain")))

        if not isinstance(self.visibility_state, Unset):
            if isinstance(self.visibility_state, str):
                files.append(("visibility_state", (None, str(self.visibility_state).encode(), "text/plain")))
            else:
                files.append(("visibility_state", (None, str(self.visibility_state).encode(), "text/plain")))

        if not isinstance(self.has_explicit_staff_lock, Unset):
            if isinstance(self.has_explicit_staff_lock, bool):
                files.append(
                    ("has_explicit_staff_lock", (None, str(self.has_explicit_staff_lock).encode(), "text/plain"))
                )
            else:
                files.append(
                    ("has_explicit_staff_lock", (None, str(self.has_explicit_staff_lock).encode(), "text/plain"))
                )

        if not isinstance(self.start, Unset):
            if isinstance(self.start, str):
                files.append(("start", (None, str(self.start).encode(), "text/plain")))
            else:
                files.append(("start", (None, str(self.start).encode(), "text/plain")))

        if not isinstance(self.graded, Unset):
            if isinstance(self.graded, bool):
                files.append(("graded", (None, str(self.graded).encode(), "text/plain")))
            else:
                files.append(("graded", (None, str(self.graded).encode(), "text/plain")))

        if not isinstance(self.due_date, Unset):
            if isinstance(self.due_date, str):
                files.append(("due_date", (None, str(self.due_date).encode(), "text/plain")))
            else:
                files.append(("due_date", (None, str(self.due_date).encode(), "text/plain")))

        if not isinstance(self.due, Unset):
            files.append(("due", (None, str(self.due).encode(), "text/plain")))

        if not isinstance(self.relative_weeks_due, Unset):
            files.append(("relative_weeks_due", (None, str(self.relative_weeks_due).encode(), "text/plain")))

        if not isinstance(self.format_, Unset):
            files.append(("format", (None, str(self.format_).encode(), "text/plain")))

        if not isinstance(self.course_graders, Unset):
            if isinstance(self.course_graders, list):
                for course_graders_type_0_item_element in self.course_graders:
                    files.append(
                        ("course_graders", (None, str(course_graders_type_0_item_element).encode(), "text/plain"))
                    )
            else:
                files.append(("course_graders", (None, str(self.course_graders).encode(), "text/plain")))

        if not isinstance(self.actions, Unset):
            if isinstance(self.actions, PatchedXblockActionsType0):
                files.append(("actions", (None, json.dumps(self.actions.to_dict()).encode(), "application/json")))
            else:
                files.append(("actions", (None, str(self.actions).encode(), "text/plain")))

        if not isinstance(self.explanatory_message, Unset):
            if isinstance(self.explanatory_message, str):
                files.append(("explanatory_message", (None, str(self.explanatory_message).encode(), "text/plain")))
            else:
                files.append(("explanatory_message", (None, str(self.explanatory_message).encode(), "text/plain")))

        if not isinstance(self.group_access, Unset):
            if isinstance(self.group_access, PatchedXblockGroupAccessType0):
                files.append(
                    ("group_access", (None, json.dumps(self.group_access.to_dict()).encode(), "application/json"))
                )
            else:
                files.append(("group_access", (None, str(self.group_access).encode(), "text/plain")))

        if not isinstance(self.user_partitions, Unset):
            if isinstance(self.user_partitions, list):
                for user_partitions_type_0_item_element in self.user_partitions:
                    files.append(
                        ("user_partitions", (None, str(user_partitions_type_0_item_element).encode(), "text/plain"))
                    )
            else:
                files.append(("user_partitions", (None, str(self.user_partitions).encode(), "text/plain")))

        if not isinstance(self.show_correctness, Unset):
            if isinstance(self.show_correctness, str):
                files.append(("show_correctness", (None, str(self.show_correctness).encode(), "text/plain")))
            else:
                files.append(("show_correctness", (None, str(self.show_correctness).encode(), "text/plain")))

        if not isinstance(self.discussion_enabled, Unset):
            if isinstance(self.discussion_enabled, bool):
                files.append(("discussion_enabled", (None, str(self.discussion_enabled).encode(), "text/plain")))
            else:
                files.append(("discussion_enabled", (None, str(self.discussion_enabled).encode(), "text/plain")))

        if not isinstance(self.ancestor_has_staff_lock, Unset):
            if isinstance(self.ancestor_has_staff_lock, bool):
                files.append(
                    ("ancestor_has_staff_lock", (None, str(self.ancestor_has_staff_lock).encode(), "text/plain"))
                )
            else:
                files.append(
                    ("ancestor_has_staff_lock", (None, str(self.ancestor_has_staff_lock).encode(), "text/plain"))
                )

        if not isinstance(self.user_partition_info, Unset):
            if isinstance(self.user_partition_info, PatchedXblockUserPartitionInfoType0):
                files.append(
                    (
                        "user_partition_info",
                        (None, json.dumps(self.user_partition_info.to_dict()).encode(), "application/json"),
                    )
                )
            else:
                files.append(("user_partition_info", (None, str(self.user_partition_info).encode(), "text/plain")))

        if not isinstance(self.summary_configuration_enabled, Unset):
            files.append(
                (
                    "summary_configuration_enabled",
                    (None, str(self.summary_configuration_enabled).encode(), "text/plain"),
                )
            )

        if not isinstance(self.is_prereq, Unset):
            if isinstance(self.is_prereq, bool):
                files.append(("isPrereq", (None, str(self.is_prereq).encode(), "text/plain")))
            else:
                files.append(("isPrereq", (None, str(self.is_prereq).encode(), "text/plain")))

        if not isinstance(self.prereq_usage_key, Unset):
            if isinstance(self.prereq_usage_key, str):
                files.append(("prereqUsageKey", (None, str(self.prereq_usage_key).encode(), "text/plain")))
            else:
                files.append(("prereqUsageKey", (None, str(self.prereq_usage_key).encode(), "text/plain")))

        if not isinstance(self.prereq_min_score, Unset):
            if isinstance(self.prereq_min_score, int):
                files.append(("prereqMinScore", (None, str(self.prereq_min_score).encode(), "text/plain")))
            else:
                files.append(("prereqMinScore", (None, str(self.prereq_min_score).encode(), "text/plain")))

        if not isinstance(self.prereq_min_completion, Unset):
            if isinstance(self.prereq_min_completion, int):
                files.append(("prereqMinCompletion", (None, str(self.prereq_min_completion).encode(), "text/plain")))
            else:
                files.append(("prereqMinCompletion", (None, str(self.prereq_min_completion).encode(), "text/plain")))

        if not isinstance(self.publish, Unset):
            if isinstance(self.publish, PublishEnum):
                files.append(("publish", (None, str(self.publish.value).encode(), "text/plain")))
            else:
                files.append(("publish", (None, str(self.publish).encode(), "text/plain")))

        if not isinstance(self.duplicate_source_locator, Unset):
            if isinstance(self.duplicate_source_locator, str):
                files.append(
                    ("duplicate_source_locator", (None, str(self.duplicate_source_locator).encode(), "text/plain"))
                )
            else:
                files.append(
                    ("duplicate_source_locator", (None, str(self.duplicate_source_locator).encode(), "text/plain"))
                )

        if not isinstance(self.move_source_locator, Unset):
            if isinstance(self.move_source_locator, str):
                files.append(("move_source_locator", (None, str(self.move_source_locator).encode(), "text/plain")))
            else:
                files.append(("move_source_locator", (None, str(self.move_source_locator).encode(), "text/plain")))

        if not isinstance(self.target_index, Unset):
            if isinstance(self.target_index, int):
                files.append(("target_index", (None, str(self.target_index).encode(), "text/plain")))
            else:
                files.append(("target_index", (None, str(self.target_index).encode(), "text/plain")))

        if not isinstance(self.boilerplate, Unset):
            files.append(("boilerplate", (None, str(self.boilerplate).encode(), "text/plain")))

        if not isinstance(self.staged_content, Unset):
            if isinstance(self.staged_content, str):
                files.append(("staged_content", (None, str(self.staged_content).encode(), "text/plain")))
            else:
                files.append(("staged_content", (None, str(self.staged_content).encode(), "text/plain")))

        if not isinstance(self.hide_from_toc, Unset):
            if isinstance(self.hide_from_toc, bool):
                files.append(("hide_from_toc", (None, str(self.hide_from_toc).encode(), "text/plain")))
            else:
                files.append(("hide_from_toc", (None, str(self.hide_from_toc).encode(), "text/plain")))

        for prop_name, prop in self.additional_properties.items():
            files.append((prop_name, (None, str(prop).encode(), "text/plain")))

        return files

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.patched_xblock_actions_type_0 import PatchedXblockActionsType0
        from ..models.patched_xblock_fields_type_0 import PatchedXblockFieldsType0
        from ..models.patched_xblock_group_access_type_0 import PatchedXblockGroupAccessType0
        from ..models.patched_xblock_metadata_type_0 import PatchedXblockMetadataType0
        from ..models.patched_xblock_user_partition_info_type_0 import PatchedXblockUserPartitionInfoType0

        d = dict(src_dict)

        def _parse_id(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        id = _parse_id(d.pop("id", UNSET))

        def _parse_parent_locator(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        parent_locator = _parse_parent_locator(d.pop("parent_locator", UNSET))

        def _parse_display_name(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        display_name = _parse_display_name(d.pop("display_name", UNSET))

        def _parse_category(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        category = _parse_category(d.pop("category", UNSET))

        def _parse_data(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        data = _parse_data(d.pop("data", UNSET))

        def _parse_metadata(data: object) -> None | PatchedXblockMetadataType0 | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                metadata_type_0 = PatchedXblockMetadataType0.from_dict(data)

                return metadata_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | PatchedXblockMetadataType0 | Unset, data)

        metadata = _parse_metadata(d.pop("metadata", UNSET))

        def _parse_has_changes(data: object) -> bool | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(bool | None | Unset, data)

        has_changes = _parse_has_changes(d.pop("has_changes", UNSET))

        def _parse_children(data: object) -> list[Any] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                children_type_0 = cast(list[Any], data)

                return children_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[Any] | None | Unset, data)

        children = _parse_children(d.pop("children", UNSET))

        def _parse_fields(data: object) -> None | PatchedXblockFieldsType0 | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                fields_type_0 = PatchedXblockFieldsType0.from_dict(data)

                return fields_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | PatchedXblockFieldsType0 | Unset, data)

        fields = _parse_fields(d.pop("fields", UNSET))

        def _parse_has_children(data: object) -> bool | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(bool | None | Unset, data)

        has_children = _parse_has_children(d.pop("has_children", UNSET))

        def _parse_video_sharing_enabled(data: object) -> bool | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(bool | None | Unset, data)

        video_sharing_enabled = _parse_video_sharing_enabled(d.pop("video_sharing_enabled", UNSET))

        def _parse_video_sharing_options(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        video_sharing_options = _parse_video_sharing_options(d.pop("video_sharing_options", UNSET))

        def _parse_video_sharing_doc_url(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        video_sharing_doc_url = _parse_video_sharing_doc_url(d.pop("video_sharing_doc_url", UNSET))

        def _parse_edited_on(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        edited_on = _parse_edited_on(d.pop("edited_on", UNSET))

        def _parse_published(data: object) -> bool | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(bool | None | Unset, data)

        published = _parse_published(d.pop("published", UNSET))

        published_on = d.pop("published_on", UNSET)

        def _parse_studio_url(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        studio_url = _parse_studio_url(d.pop("studio_url", UNSET))

        def _parse_released_to_students(data: object) -> bool | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(bool | None | Unset, data)

        released_to_students = _parse_released_to_students(d.pop("released_to_students", UNSET))

        release_date = d.pop("release_date", UNSET)

        nullout = d.pop("nullout", UNSET)

        grader_type = d.pop("graderType", UNSET)

        def _parse_visibility_state(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        visibility_state = _parse_visibility_state(d.pop("visibility_state", UNSET))

        def _parse_has_explicit_staff_lock(data: object) -> bool | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(bool | None | Unset, data)

        has_explicit_staff_lock = _parse_has_explicit_staff_lock(d.pop("has_explicit_staff_lock", UNSET))

        def _parse_start(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        start = _parse_start(d.pop("start", UNSET))

        def _parse_graded(data: object) -> bool | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(bool | None | Unset, data)

        graded = _parse_graded(d.pop("graded", UNSET))

        def _parse_due_date(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        due_date = _parse_due_date(d.pop("due_date", UNSET))

        due = d.pop("due", UNSET)

        relative_weeks_due = d.pop("relative_weeks_due", UNSET)

        format_ = d.pop("format", UNSET)

        def _parse_course_graders(data: object) -> list[Any] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                course_graders_type_0 = cast(list[Any], data)

                return course_graders_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[Any] | None | Unset, data)

        course_graders = _parse_course_graders(d.pop("course_graders", UNSET))

        def _parse_actions(data: object) -> None | PatchedXblockActionsType0 | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                actions_type_0 = PatchedXblockActionsType0.from_dict(data)

                return actions_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | PatchedXblockActionsType0 | Unset, data)

        actions = _parse_actions(d.pop("actions", UNSET))

        def _parse_explanatory_message(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        explanatory_message = _parse_explanatory_message(d.pop("explanatory_message", UNSET))

        def _parse_group_access(data: object) -> None | PatchedXblockGroupAccessType0 | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                group_access_type_0 = PatchedXblockGroupAccessType0.from_dict(data)

                return group_access_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | PatchedXblockGroupAccessType0 | Unset, data)

        group_access = _parse_group_access(d.pop("group_access", UNSET))

        def _parse_user_partitions(data: object) -> list[Any] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                user_partitions_type_0 = cast(list[Any], data)

                return user_partitions_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[Any] | None | Unset, data)

        user_partitions = _parse_user_partitions(d.pop("user_partitions", UNSET))

        def _parse_show_correctness(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        show_correctness = _parse_show_correctness(d.pop("show_correctness", UNSET))

        def _parse_discussion_enabled(data: object) -> bool | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(bool | None | Unset, data)

        discussion_enabled = _parse_discussion_enabled(d.pop("discussion_enabled", UNSET))

        def _parse_ancestor_has_staff_lock(data: object) -> bool | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(bool | None | Unset, data)

        ancestor_has_staff_lock = _parse_ancestor_has_staff_lock(d.pop("ancestor_has_staff_lock", UNSET))

        def _parse_user_partition_info(data: object) -> None | PatchedXblockUserPartitionInfoType0 | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                user_partition_info_type_0 = PatchedXblockUserPartitionInfoType0.from_dict(data)

                return user_partition_info_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | PatchedXblockUserPartitionInfoType0 | Unset, data)

        user_partition_info = _parse_user_partition_info(d.pop("user_partition_info", UNSET))

        summary_configuration_enabled = d.pop("summary_configuration_enabled", UNSET)

        def _parse_is_prereq(data: object) -> bool | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(bool | None | Unset, data)

        is_prereq = _parse_is_prereq(d.pop("isPrereq", UNSET))

        def _parse_prereq_usage_key(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        prereq_usage_key = _parse_prereq_usage_key(d.pop("prereqUsageKey", UNSET))

        def _parse_prereq_min_score(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        prereq_min_score = _parse_prereq_min_score(d.pop("prereqMinScore", UNSET))

        def _parse_prereq_min_completion(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        prereq_min_completion = _parse_prereq_min_completion(d.pop("prereqMinCompletion", UNSET))

        def _parse_publish(data: object) -> None | PublishEnum | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                publish_type_0 = PublishEnum(data)

                return publish_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | PublishEnum | Unset, data)

        publish = _parse_publish(d.pop("publish", UNSET))

        def _parse_duplicate_source_locator(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        duplicate_source_locator = _parse_duplicate_source_locator(d.pop("duplicate_source_locator", UNSET))

        def _parse_move_source_locator(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        move_source_locator = _parse_move_source_locator(d.pop("move_source_locator", UNSET))

        def _parse_target_index(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        target_index = _parse_target_index(d.pop("target_index", UNSET))

        boilerplate = d.pop("boilerplate", UNSET)

        def _parse_staged_content(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        staged_content = _parse_staged_content(d.pop("staged_content", UNSET))

        def _parse_hide_from_toc(data: object) -> bool | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(bool | None | Unset, data)

        hide_from_toc = _parse_hide_from_toc(d.pop("hide_from_toc", UNSET))

        patched_xblock = cls(
            id=id,
            parent_locator=parent_locator,
            display_name=display_name,
            category=category,
            data=data,
            metadata=metadata,
            has_changes=has_changes,
            children=children,
            fields=fields,
            has_children=has_children,
            video_sharing_enabled=video_sharing_enabled,
            video_sharing_options=video_sharing_options,
            video_sharing_doc_url=video_sharing_doc_url,
            edited_on=edited_on,
            published=published,
            published_on=published_on,
            studio_url=studio_url,
            released_to_students=released_to_students,
            release_date=release_date,
            nullout=nullout,
            grader_type=grader_type,
            visibility_state=visibility_state,
            has_explicit_staff_lock=has_explicit_staff_lock,
            start=start,
            graded=graded,
            due_date=due_date,
            due=due,
            relative_weeks_due=relative_weeks_due,
            format_=format_,
            course_graders=course_graders,
            actions=actions,
            explanatory_message=explanatory_message,
            group_access=group_access,
            user_partitions=user_partitions,
            show_correctness=show_correctness,
            discussion_enabled=discussion_enabled,
            ancestor_has_staff_lock=ancestor_has_staff_lock,
            user_partition_info=user_partition_info,
            summary_configuration_enabled=summary_configuration_enabled,
            is_prereq=is_prereq,
            prereq_usage_key=prereq_usage_key,
            prereq_min_score=prereq_min_score,
            prereq_min_completion=prereq_min_completion,
            publish=publish,
            duplicate_source_locator=duplicate_source_locator,
            move_source_locator=move_source_locator,
            target_index=target_index,
            boilerplate=boilerplate,
            staged_content=staged_content,
            hide_from_toc=hide_from_toc,
        )

        patched_xblock.additional_properties = d
        return patched_xblock

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
