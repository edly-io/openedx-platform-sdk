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
                            that a date the API returns as null doesn't raise
                            TypeError.
5. fix_unenroll_body_union — drops the non-JSON body types from the unenroll
                             endpoint, which fix 2 leaves accepted but
                             unserialised (a silent empty POST to a
                             destructive endpoint).

Fix 4 works around a platform schema bug rather than a generator bug: Studio's
``CourseDetails`` declares its dates required and non-null, but the API returns
null for a course with no dates set. The LMS half of the same bug, on
``EnrollmentCourse``, was fixed upstream by
https://github.com/openedx/openedx-platform/pull/39120, as was the bare-list
``enrollment_allowed`` response a former fix patched.

It then restores the hand-written ``auth`` exports to ``__init__.py``, which
the generator rewrites without them.

Every step reports how many sites it patched, and the script exits non-zero if
any of them patches nothing. A regeneration that suddenly needs no patches
means the generator's output shape has changed, which needs a human to look
rather than silently producing a client with the original bugs back in it.
"""

import glob
import os
import re
import sys

# The unenroll endpoint's URL as the generator writes it into ``_get_kwargs``,
# with or without the service's API prefix.
UNENROLL_URL_PATTERN = re.compile(r'"url": "[^"]*/v2/enrollment/unenroll/"')

# ---------------------------------------------------------------------------
# Bug 1
# ---------------------------------------------------------------------------

def fix_unset_import(api_dir: str) -> int:
    """Add the missing ``Unset`` name to ``from ...types import`` lines.

    Some generated API files use ``Unset`` in type annotations (e.g.
    ``Union[Unset, str]``) but only import ``UNSET`` (the sentinel value).
    This causes a ``NameError`` at runtime.  The fix appends ``, Unset`` to
    every matching import line.
    """
    patched = 0
    for path in _glob_py(api_dir):
        text = open(path).read()
        old = "from ...types import UNSET, Response"
        new = "from ...types import UNSET, Response, Unset"
        if new in text:
            patched += 1  # already in the fixed state
        elif old in text:
            open(path, "w").write(text.replace(old, new))
            patched += 1
            print(f"  Fixed missing Unset import in {os.path.basename(path)}")
    return patched


# ---------------------------------------------------------------------------
# Bug 2
# ---------------------------------------------------------------------------

def fix_multipart_bug(api_dir: str) -> int:
    """Remove duplicate ``isinstance(body, X)`` blocks from ``_get_kwargs``.

    The generator emits three identical ``if isinstance(body, ...)`` blocks
    for JSON, form-encoded, and multipart bodies.  Because the multipart block
    is last it always wins, which silently breaks nested-dict JSON payloads
    (the body ends up in ``_kwargs["files"]`` instead of ``_kwargs["json"]``).

    Fix: keep only the JSON block — drop any block that populates
    ``_kwargs["data"]`` or ``_kwargs["files"]``.
    """
    patched = 0
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
            patched += 1
            print(f"  Fixed multipart bug in {os.path.basename(path)}")
        elif "".join(lines).count("if isinstance(body,") == 1:
            # Exactly one isinstance(body, ...) block means this file is
            # already in the fixed state rather than never having had the bug.
            patched += 1
    return patched


# ---------------------------------------------------------------------------
# Bug 3
# ---------------------------------------------------------------------------

def fix_dict_safe_to_dict(models_dir: str) -> int:
    """Make ``to_dict()`` calls on DictField wrapper models dict-safe.

    The generator emits ``X = self.X.to_dict()`` unconditionally, but callers
    may pass plain Python dicts.  Fix: replace the call with
    ``X = self.X.to_dict() if not isinstance(self.X, dict) else dict(self.X)``
    whenever the preceding line is ``if not isinstance(self.X, Unset):``.
    """
    patched = 0
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
            patched += 1
            print(f"  Fixed dict-safe to_dict() in {os.path.basename(path)}")
        elif "else dict(self." in "".join(lines):
            patched += 1  # already in the fixed state
    return patched


# ---------------------------------------------------------------------------
# Bug 4
# ---------------------------------------------------------------------------

def fix_null_safe_datetime(models_dir: str) -> int:
    """Replace bare ``datetime.fromisoformat(d.pop(...))`` with a null-safe form.

    Studio's ``CourseDetails`` datetime fields are marked required and
    non-null in the schema, but the API returns ``null`` for courses that have
    no dates set.  The bare ``fromisoformat`` call raises ``TypeError`` on
    ``None``.

    Platform schema bug, not a generator bug. The LMS ``EnrollmentCourse``
    fields had the same bug and were fixed upstream by
    https://github.com/openedx/openedx-platform/pull/39120; delete this step
    once ``CourseDetails`` is fixed the same way.

    Fix: split into a ``_raw_<var> = d.pop(...)`` step and a conditional
    ``fromisoformat`` that yields ``None`` when the raw value is not a string.
    Only lines inside ``from_dict()`` method bodies are touched.
    """
    DT_PATTERN = re.compile(
        r"^(\s+)(\w+) = datetime\.datetime\.fromisoformat\(d\.pop\(\"(\w+)\"\)\)\s*$"
    )
    patched = 0
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
            patched += 1
            print(f"  Fixed null-safe datetime parsing in {os.path.basename(path)}")
        elif "_raw_" in "".join(lines):
            patched += 1  # already in the fixed state
    return patched


# ---------------------------------------------------------------------------
# Bug 5
# ---------------------------------------------------------------------------

def fix_unenroll_body_union(package_dir: str) -> int:
    """Drop the non-JSON body types from the unenroll endpoint.

    The platform schema declares three content types for ``POST
    /api/enrollment/v2/enrollment/unenroll/`` whose payloads are identical
    (``username: str``), so the generator emits ``JsonBody``, ``DataBody`` and
    ``FilesBody`` and accepts all three in the signature.

    Bug 2 above keeps only the JSON branch in ``_get_kwargs``, which leaves the
    other two types accepted but unserialised: passing either sends a POST with
    no body and no ``Content-Type`` to a destructive endpoint, with no error.
    Since the generated signature is what callers type against, the types are
    removed rather than left as a silent trap.

    The module is found by the URL it calls rather than by name, because the
    name follows the schema's operationId, which changes whenever the platform
    changes how it publishes the path.
    """
    api_dir = os.path.join(package_dir, "api", "openedx_platform_sdk")
    models_init = os.path.join(package_dir, "models", "__init__.py")
    matches = [
        path for path in _glob_py(api_dir)
        if UNENROLL_URL_PATTERN.search(open(path).read())
    ]
    if len(matches) != 1:
        print(
            f"  ERROR: expected one API module calling the unenroll URL, found {len(matches)}"
            + (f": {', '.join(sorted(os.path.basename(m) for m in matches))}" if matches else "")
            + ".",
            file=sys.stderr,
        )
        return 0
    api_path = matches[0]
    stem = os.path.splitext(os.path.basename(api_path))[0]
    camel = "".join(part.capitalize() for part in stem.split("_"))
    dead = [f"{camel}{kind}Body" for kind in ("Data", "Files")]

    # Each of the three halves must independently end up clean. They are tracked
    # separately rather than through a shared counter: a shared one lets a half
    # that silently matched nothing be covered by a half that succeeded, which
    # ships a package whose ``__all__`` names modules that were deleted.
    init_clean = False

    text = open(api_path).read()
    original = text
    for name in dead:
        snake = re.sub(r"(?<!^)(?=[A-Z])", "_", name).lower()
        # Single-line, or wrapped in parentheses once the name is long enough.
        text = re.sub(
            rf"from \.\.\.models\.{snake} import (?:{name}|\(\s*{name},?\s*\))\n", "", text
        )
        text = text.replace(f"    | {name}\n", "")
        text = text.replace(f"        body ({name} | Unset):\n", "")
    if text != original:
        open(api_path, "w").write(text)
        print(f"  Removed non-JSON unenroll body types from {os.path.basename(api_path)}")
    # True whether this run removed them or an earlier run already did.
    api_clean = not any(_mentions(text, name) for name in dead)
    if not api_clean:
        remaining = sorted(name for name in dead if _mentions(text, name))
        print(
            f"  ERROR: {os.path.basename(api_path)} still references {', '.join(remaining)} "
            "— the generator's output shape changed and the patterns above no longer match.",
            file=sys.stderr,
        )

    if os.path.isfile(models_init):
        text = open(models_init).read()
        original = text
        for name in dead:
            snake = re.sub(r"(?<!^)(?=[A-Z])", "_", name).lower()
            text = text.replace(f"from .{snake} import {name}\n", "")
            text = text.replace(f'    "{name}",\n', "")
        if text != original:
            open(models_init, "w").write(text)
            print("  Removed non-JSON unenroll body exports from models/__init__.py")
        init_clean = not any(_mentions(text, name) for name in dead)
        if not init_clean:
            remaining = sorted(name for name in dead if _mentions(text, name))
            print(
                f"  ERROR: models/__init__.py still references {', '.join(remaining)} "
                "— check the import and __all__ formatting the generator emits.",
                file=sys.stderr,
            )
    else:
        print(f"  ERROR: {models_init} is missing.", file=sys.stderr)

    # Only unreferenced modules may be deleted. Deleting them while either half
    # above still names them produces a package that fails on import, so the
    # deletion is gated on both halves being clean.
    if not (api_clean and init_clean):
        return 0

    models_removed = 0
    for kind in ("data", "files"):
        path = os.path.join(package_dir, "models", f"{stem}_{kind}_body.py")
        if os.path.isfile(path):
            os.remove(path)
            print(f"  Deleted unused model {os.path.basename(path)}")
            models_removed += 1
        else:
            # Already gone from an earlier run — the end state is what matters.
            models_removed += 1

    return 1 if models_removed == 2 else 0


# ---------------------------------------------------------------------------
# Hand-written auth exports
# ---------------------------------------------------------------------------

def restore_auth_exports(package_dir: str) -> int:
    """Re-add the hand-written ``auth`` exports to the generated ``__init__.py``.

    ``auth.py`` is preserved across regeneration by ``regen_sdk.sh``, but the
    generator rewrites ``__init__.py`` from the schema and so drops both the
    import and the ``__all__`` entry for it.
    """
    path = os.path.join(package_dir, "__init__.py")
    if not os.path.isfile(path):
        print(f"  WARNING: {path} not found; skipping auth export restore")
        return 0

    text = open(path).read()
    patched = 0

    import_line = "from .auth import OAuth2ClientCredentials\n"
    if import_line not in text:
        if "from .client import" not in text:
            print("  WARNING: no 'from .client import' in __init__.py; cannot place auth import")
            return 0
        text = text.replace("from .client import", import_line + "from .client import", 1)
        patched += 1

    if '"OAuth2ClientCredentials",' not in text:
        if '"AuthenticatedClient",' not in text:
            print('  WARNING: no "AuthenticatedClient" in __init__.py __all__; cannot add export')
            return patched
        text = text.replace(
            '"AuthenticatedClient",',
            '"AuthenticatedClient",\n    "OAuth2ClientCredentials",',
            1,
        )
        patched += 1

    if patched:
        open(path, "w").write(text)
        print("  Restored auth exports in __init__.py")
    else:
        patched = 2  # already present; re-running is a no-op

    return patched


# ---------------------------------------------------------------------------
# Helpers
# ---------------------------------------------------------------------------

def _glob_py(directory: str) -> list[str]:
    return glob.glob(os.path.join(directory, "*.py"))


def _mentions(text: str, name: str) -> bool:
    """Whether ``name`` appears as a whole identifier, not inside a longer one."""
    return re.search(rf"\b{re.escape(name)}\b", text) is not None


# ---------------------------------------------------------------------------
# Entry point
# ---------------------------------------------------------------------------

def main() -> None:
    if len(sys.argv) < 2:
        print(f"Usage: {sys.argv[0]} <sdk_root>", file=sys.stderr)
        sys.exit(1)

    sdk_root = sys.argv[1]
    package_dir = os.path.join(sdk_root, "openedx_platform_sdk")
    api_dir = os.path.join(package_dir, "api", "openedx_platform_sdk")
    models_dir = os.path.join(package_dir, "models")

    results = [
        ("fix_unset_import", fix_unset_import(api_dir)),
        ("fix_multipart_bug", fix_multipart_bug(api_dir)),
        ("fix_dict_safe_to_dict", fix_dict_safe_to_dict(models_dir)),
        ("fix_null_safe_datetime", fix_null_safe_datetime(models_dir)),
        ("fix_unenroll_body_union", fix_unenroll_body_union(package_dir)),
        ("restore_auth_exports", restore_auth_exports(package_dir)),
    ]

    unapplied = [name for name, count in results if count == 0]
    if unapplied:
        print(
            "\nERROR: the following post-processing steps patched nothing:\n"
            + "\n".join(f"  - {name}" for name in unapplied)
            + "\n\nThe generator's output shape has probably changed. Check whether"
            "\nthe underlying bug is fixed upstream (in which case delete the step)"
            "\nor whether it now needs a different pattern — do not ship the client"
            "\nwithout resolving this.",
            file=sys.stderr,
        )
        sys.exit(1)

    print("\n  All post-processing steps applied.")


if __name__ == "__main__":
    main()
