#!/usr/bin/env python3
"""Post-process the auto-generated openedx-platform-sdk to fix known generator bugs.

Usage:
    python postprocess_sdk.py <sdk_root>

Where <sdk_root> is the directory that contains the ``openedx_platform_sdk``
package (i.e. the directory where ``regen_sdk.sh`` lives).

The script applies five targeted fixes in order:

1. fix_unset_import    — adds the missing ``Unset`` name to ``from ...types``
                         imports in API files that use it in type annotations.
2. fix_multipart_bug   — removes duplicate ``isinstance(body, X)`` blocks that
                         set ``_kwargs["data"]`` or ``_kwargs["files"]`` inside
                         ``_get_kwargs``; the multipart block always wins and
                         breaks nested-dict JSON payloads.
3. fix_dict_safe_to_dict — makes ``to_dict()`` calls on DictField wrapper
                           models tolerate plain Python dicts in addition to
                           model instances.
4. fix_null_safe_datetime — replaces bare ``datetime.datetime.fromisoformat(
                            d.pop("field"))`` calls with a null-safe version so
                            that courses with no dates set (API returns null)
                            don't raise TypeError.
5. fix_plain_list_enrollment_allowed — guards the ``from_dict()`` of
                                       ``PaginatedCourseEnrollmentAllowedList``
                                       against the endpoint returning a bare
                                       JSON array instead of the expected
                                       paginated envelope.
"""

import glob
import os
import re
import sys


# ---------------------------------------------------------------------------
# Bug 1
# ---------------------------------------------------------------------------

def fix_unset_import(api_dir: str) -> None:
    """Add the missing ``Unset`` name to ``from ...types import`` lines.

    Some generated API files use ``Unset`` in type annotations (e.g.
    ``Union[Unset, str]``) but only import ``UNSET`` (the sentinel value).
    This causes a ``NameError`` at runtime.  The fix appends ``, Unset`` to
    every matching import line.
    """
    for path in _glob_py(api_dir):
        text = open(path).read()
        old = "from ...types import UNSET, Response"
        new = "from ...types import UNSET, Response, Unset"
        if old in text and new not in text:
            open(path, "w").write(text.replace(old, new))
            print(f"  Fixed missing Unset import in {os.path.basename(path)}")


# ---------------------------------------------------------------------------
# Bug 2
# ---------------------------------------------------------------------------

def fix_multipart_bug(api_dir: str) -> None:
    """Remove duplicate ``isinstance(body, X)`` blocks from ``_get_kwargs``.

    The generator emits three identical ``if isinstance(body, ...)`` blocks
    for JSON, form-encoded, and multipart bodies.  Because the multipart block
    is last it always wins, which silently breaks nested-dict JSON payloads
    (the body ends up in ``_kwargs["files"]`` instead of ``_kwargs["json"]``).

    Fix: keep only the JSON block — drop any block that populates
    ``_kwargs["data"]`` or ``_kwargs["files"]``.
    """
    for path in _glob_py(api_dir):
        lines = open(path).readlines()
        in_get_kwargs = False
        new_lines: list[str] = []
        i = 0
        changed = False
        while i < len(lines):
            line = lines[i]
            if "def _get_kwargs(" in line:
                in_get_kwargs = True
            if in_get_kwargs and line.strip() == "return _kwargs":
                in_get_kwargs = False
            # Inside _get_kwargs, skip any isinstance(body, ...) block that
            # sets _kwargs["data"] or _kwargs["files"] (non-JSON blocks).
            if in_get_kwargs and line.startswith("    if isinstance(body,"):
                j = i + 1
                while j < len(lines) and (
                    lines[j].strip() == "" or lines[j].startswith("        ")
                ):
                    j += 1
                block_content = "".join(lines[i:j])
                if '_kwargs["json"]' not in block_content and (
                    '_kwargs["data"]' in block_content
                    or '_kwargs["files"]' in block_content
                ):
                    changed = True
                    i = j
                    continue
            new_lines.append(line)
            i += 1
        if changed:
            open(path, "w").writelines(new_lines)
            print(f"  Fixed multipart bug in {os.path.basename(path)}")


# ---------------------------------------------------------------------------
# Bug 3
# ---------------------------------------------------------------------------

def fix_dict_safe_to_dict(models_dir: str) -> None:
    """Make ``to_dict()`` calls on DictField wrapper models dict-safe.

    The generator emits ``X = self.X.to_dict()`` unconditionally, but callers
    may pass plain Python dicts.  Fix: replace the call with
    ``X = self.X.to_dict() if not isinstance(self.X, dict) else dict(self.X)``
    whenever the preceding line is ``if not isinstance(self.X, Unset):``.
    """
    for path in _glob_py(models_dir):
        lines = open(path).readlines()
        new_lines: list[str] = []
        changed = False
        i = 0
        while i < len(lines):
            line = lines[i]
            m = re.match(r"^(\s+)if not isinstance\(self\.(\w+), Unset\):\s*$", line)
            if m and i + 1 < len(lines):
                field = m.group(2)
                next_line = lines[i + 1]
                nm = re.match(
                    r"^(\s+)"
                    + re.escape(field)
                    + r" = self\."
                    + re.escape(field)
                    + r"\.to_dict\(\)\s*$",
                    next_line,
                )
                if nm:
                    inner_indent = nm.group(1)
                    new_lines.append(line)
                    new_lines.append(
                        f"{inner_indent}{field} = self.{field}.to_dict() "
                        f"if not isinstance(self.{field}, dict) else dict(self.{field})\n"
                    )
                    changed = True
                    i += 2
                    continue
            new_lines.append(line)
            i += 1
        if changed:
            open(path, "w").writelines(new_lines)
            print(f"  Fixed dict-safe to_dict() in {os.path.basename(path)}")


# ---------------------------------------------------------------------------
# Bug 4
# ---------------------------------------------------------------------------

def fix_null_safe_datetime(models_dir: str) -> None:
    """Replace bare ``datetime.fromisoformat(d.pop(...))`` with a null-safe form.

    ``EnrollmentCourse`` datetime fields (``enrollment_start``,
    ``enrollment_end``, ``course_start``, ``course_end``) are marked required
    in the schema, but the API returns ``null`` for courses that have no dates
    set.  The bare ``fromisoformat`` call raises ``TypeError`` on ``None``.

    Fix: split into a ``_raw_<var> = d.pop(...)`` step and a conditional
    ``fromisoformat`` that yields ``None`` when the raw value is not a string.
    Only lines inside ``from_dict()`` method bodies are touched.
    """
    DT_PATTERN = re.compile(
        r"^(\s+)(\w+) = datetime\.datetime\.fromisoformat\(d\.pop\(\"(\w+)\"\)\)\s*$"
    )
    for path in _glob_py(models_dir):
        lines = open(path).readlines()
        new_lines: list[str] = []
        changed = False
        in_from_dict = False

        for line in lines:
            if "def from_dict(" in line:
                in_from_dict = True
            elif in_from_dict and re.match(r"^    def ", line) and "from_dict" not in line:
                in_from_dict = False

            if in_from_dict:
                m = DT_PATTERN.match(line)
                if m:
                    indent, var, key = m.group(1), m.group(2), m.group(3)
                    new_lines.append(f'{indent}_raw_{var} = d.pop("{key}")\n')
                    new_lines.append(
                        f"{indent}{var} = datetime.datetime.fromisoformat(_raw_{var}) "
                        f"if isinstance(_raw_{var}, str) else None\n"
                    )
                    changed = True
                    continue
            new_lines.append(line)

        if changed:
            open(path, "w").writelines(new_lines)
            print(f"  Fixed null-safe datetime parsing in {os.path.basename(path)}")


# ---------------------------------------------------------------------------
# Bug 5
# ---------------------------------------------------------------------------

def fix_plain_list_enrollment_allowed(models_dir: str) -> None:
    """Normalise a bare-list response from the enrollment-allowed endpoint.

    ``GET /v2/enrollment/enrollment_allowed/`` returns a plain JSON array
    instead of the expected paginated envelope ``{"count": N, "results": [...]}``.
    Fix: insert an ``isinstance(src_dict, list)`` guard at the top of
    ``PaginatedCourseEnrollmentAllowedList.from_dict()`` that converts the bare
    list into the envelope shape before the regular parsing runs.
    """
    TARGET = "paginated_course_enrollment_allowed_list.py"
    MARKER = "        d = dict(src_dict)"
    INSERT = (
        "        if isinstance(src_dict, list):\n"
        "            src_dict = {\"count\": len(src_dict), \"results\": src_dict}\n"
    )

    for path in _glob_py(models_dir):
        if os.path.basename(path) != TARGET:
            continue
        text = open(path).read()
        if INSERT in text:
            break  # already patched
        if MARKER not in text:
            print(f"  WARNING: could not find marker in {TARGET}; skipping Bug 5 fix")
            break
        text = text.replace(MARKER, INSERT + MARKER, 1)
        open(path, "w").write(text)
        print(f"  Fixed plain-list response in {TARGET}")
        break


# ---------------------------------------------------------------------------
# Helpers
# ---------------------------------------------------------------------------

def _glob_py(directory: str) -> list[str]:
    return glob.glob(os.path.join(directory, "*.py"))


# ---------------------------------------------------------------------------
# Entry point
# ---------------------------------------------------------------------------

def main() -> None:
    if len(sys.argv) < 2:
        print(f"Usage: {sys.argv[0]} <sdk_root>", file=sys.stderr)
        sys.exit(1)

    sdk_root = sys.argv[1]
    api_dir = os.path.join(sdk_root, "openedx_platform_sdk", "api", "openedx_platform_sdk")
    models_dir = os.path.join(sdk_root, "openedx_platform_sdk", "models")

    fix_unset_import(api_dir)
    fix_multipart_bug(api_dir)
    fix_dict_safe_to_dict(models_dir)
    fix_null_safe_datetime(models_dir)
    fix_plain_list_enrollment_allowed(models_dir)


if __name__ == "__main__":
    main()
