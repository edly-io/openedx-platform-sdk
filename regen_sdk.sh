#!/usr/bin/env bash
# Regenerate openedx-platform-sdk from Studio (CMS) and LMS OpenAPI schemas.
#
# Usage:
#   ./regen_sdk.sh                                    # regenerate from running devstack
#   ./regen_sdk.sh feat/axim-api_improvements         # checkout branch first, then regenerate
#
# Environment variables:
#   STUDIO_URL       Base URL of running Studio  (default: http://studio.local.openedx.io:8001)
#   LMS_URL          Base URL of running LMS      (default: http://local.openedx.io:8000)
#   PLATFORM_DIR     Path to local openedx-platform repo (default: ../openedx-platform)
#                    Only needed when passing a branch argument.
#
# Requirements:
#   pip install openapi-python-client pyyaml

set -euo pipefail

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
SCHEMA_FILE="$SCRIPT_DIR/schema.yml"
LMS_SCHEMA_FILE="$SCRIPT_DIR/lms_schema.yml"
FILTERED_SCHEMA_FILE="$SCRIPT_DIR/filtered_schema.yml"
FILTER_SCRIPT="$SCRIPT_DIR/filter_schema.py"
CONFIG_FILE="$SCRIPT_DIR/config.yml"
STUDIO_URL="${STUDIO_URL:-http://studio.local.openedx.io:8001}"
LMS_URL="${LMS_URL:-http://local.openedx.io:8000}"
PLATFORM_DIR="${PLATFORM_DIR:-$(dirname "$SCRIPT_DIR")/openedx-platform}"
SDK_TAG="openedx-platform-sdk"

# ── 1. Optional branch checkout ───────────────────────────────────────────────
BRANCH="${1:-}"
if [[ -n "$BRANCH" ]]; then
    if [[ ! -d "$PLATFORM_DIR/.git" ]]; then
        echo "Error: PLATFORM_DIR='$PLATFORM_DIR' is not a git repository."
        echo "Set the PLATFORM_DIR env var to your local openedx-platform checkout:"
        echo "  PLATFORM_DIR=/path/to/openedx-platform ./regen_sdk.sh $BRANCH"
        exit 1
    fi
    echo "→ Checking out branch '$BRANCH' in $PLATFORM_DIR ..."
    git -C "$PLATFORM_DIR" fetch origin
    git -C "$PLATFORM_DIR" checkout "$BRANCH"
    echo "  Current branch: $(git -C "$PLATFORM_DIR" branch --show-current)"
fi

# ── 2. Download schemas from Studio and LMS ───────────────────────────────────
echo "→ Downloading Studio schema from $STUDIO_URL ..."
if ! curl -sf "$STUDIO_URL/authoring-api/schema/" -o "$SCHEMA_FILE"; then
    echo "Error: Could not reach $STUDIO_URL/authoring-api/schema/"
    echo "Make sure Studio is running. Override with: STUDIO_URL=http://... ./regen_sdk.sh"
    exit 1
fi
echo "  Studio schema written to: $SCHEMA_FILE"

echo "→ Downloading LMS schema from $LMS_URL ..."
if ! curl -sf "$LMS_URL/lms-api/schema/" -o "$LMS_SCHEMA_FILE"; then
    echo "Error: Could not reach $LMS_URL/lms-api/schema/"
    echo "Make sure LMS is running. Override with: LMS_URL=http://... ./regen_sdk.sh"
    exit 1
fi
echo "  LMS schema written to: $LMS_SCHEMA_FILE"

# ── 3. Filter and merge both schemas ─────────────────────────────────────────
echo "→ Filtering and merging schemas for tag '$SDK_TAG'..."
python "$FILTER_SCRIPT" "$SCHEMA_FILE" "$FILTERED_SCHEMA_FILE" "$SDK_TAG" --merge "$LMS_SCHEMA_FILE"

# ── 4. Regenerate the SDK ─────────────────────────────────────────────────────
echo "→ Regenerating SDK..."

# Preserve hand-written files before wiping the package directory.
cp "$SCRIPT_DIR/openedx_platform_sdk/auth.py" /tmp/_sdk_auth.py 2>/dev/null || true

# Generate into a temp directory; openapi-python-client always creates a new
# project folder — we only want the inner package directory.
TMPDIR="$(mktemp -d)"
openapi-python-client generate \
    --path "$FILTERED_SCHEMA_FILE" \
    --config "$CONFIG_FILE" \
    --output-path "$TMPDIR" \
    --overwrite

# Replace only the auto-generated package directory
rm -rf "$SCRIPT_DIR/openedx_platform_sdk"
mv "$TMPDIR/openedx_platform_sdk" "$SCRIPT_DIR/openedx_platform_sdk"
rm -rf "$TMPDIR"

# Restore hand-written files
if [[ -f /tmp/_sdk_auth.py ]]; then
    cp /tmp/_sdk_auth.py "$SCRIPT_DIR/openedx_platform_sdk/auth.py"
    # Re-add the auth export to __init__.py (openapi-python-client regenerates it without it)
    sed -i '' 's/^from \.client import/from .auth import OAuth2ClientCredentials\nfrom .client import/' \
        "$SCRIPT_DIR/openedx_platform_sdk/__init__.py"
    sed -i '' 's/"AuthenticatedClient",/"AuthenticatedClient",\n    "OAuth2ClientCredentials",/' \
        "$SCRIPT_DIR/openedx_platform_sdk/__init__.py"
fi

# Fix generator bugs in API modules that have nested-object bodies.
API_DIR="$SCRIPT_DIR/openedx_platform_sdk/api/openedx_platform_sdk"

# Bug 1: Some generated files use Unset in type annotations but import only UNSET.
# Apply the fix to every API file that has this pattern.
grep -rl 'from \.\.\.types import UNSET, Response$' "$API_DIR" | while read -r f; do
    sed -i '' 's/from \.\.\.types import UNSET, Response$/from ...types import UNSET, Response, Unset/' "$f"
    echo "  Fixed missing Unset import in $(basename "$f")"
done

# Bug 2: _get_kwargs has three identical isinstance(body, X) blocks for json/form/multipart.
# The multipart block always wins and breaks nested-dict payloads. Keep only JSON block.
python3 - "$API_DIR" <<'PYEOF'
import sys, os, glob

api_dir = sys.argv[1]

for path in glob.glob(os.path.join(api_dir, "*.py")):
    lines = open(path).readlines()
    # Find the _get_kwargs function boundaries
    in_get_kwargs = False
    new_lines = []
    i = 0
    changed = False
    while i < len(lines):
        line = lines[i]
        if "def _get_kwargs(" in line:
            in_get_kwargs = True
        if in_get_kwargs and line.strip() == "return _kwargs":
            in_get_kwargs = False
        # Inside _get_kwargs, when we see the second "if isinstance(body" block,
        # skip until we see "    _kwargs["headers"] = headers" (un-indented in func)
        if in_get_kwargs and line.startswith("    if isinstance(body,"):
            # Check if the next non-blank, non-comment line sets _kwargs["json"]
            # by looking at what comes after this block
            block_start = i
            # Look ahead to see if the following line (possibly with inner if) sets json
            j = i + 1
            while j < len(lines) and (lines[j].strip() == "" or lines[j].startswith("        ")):
                j += 1
            # j now points past this if-block. If j points to another "if isinstance(body",
            # this is a duplicate block — skip it if it contains "data" or "files"
            block_content = "".join(lines[i:j])
            if '_kwargs["json"]' not in block_content and (
                '_kwargs["data"]' in block_content or '_kwargs["files"]' in block_content
            ):
                changed = True
                i = j
                continue
        new_lines.append(line)
        i += 1
    if changed:
        open(path, 'w').writelines(new_lines)
        print(f"  Fixed multipart bug in {os.path.basename(path)}")
PYEOF

# Bug 3: DictField wrapper models — to_dict() calls .to_dict() on the field unconditionally,
# but users pass plain Python dicts. Fix: make the call dict-safe.
# Pattern: `if not isinstance(self.X, Unset):` followed by `X = self.X.to_dict()`
MODELS_DIR="$SCRIPT_DIR/openedx_platform_sdk/models"
python3 - "$MODELS_DIR" <<'PYEOF'
import sys, os, glob, re

models_dir = sys.argv[1]
for path in glob.glob(os.path.join(models_dir, "*.py")):
    lines = open(path).readlines()
    new_lines = []
    changed = False
    i = 0
    while i < len(lines):
        line = lines[i]
        m = re.match(r'^(\s+)if not isinstance\(self\.(\w+), Unset\):\s*$', line)
        if m and i + 1 < len(lines):
            field = m.group(2)
            next_line = lines[i + 1]
            nm = re.match(
                r'^(\s+)' + re.escape(field) + r' = self\.' + re.escape(field) + r'\.to_dict\(\)\s*$',
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
        open(path, 'w').writelines(new_lines)
        print(f"  Fixed dict-safe to_dict() in {os.path.basename(path)}")
PYEOF

# Bug 4: EnrollmentCourse datetime fields (enrollment_start, enrollment_end, course_start,
# course_end) are marked required in the schema but the API returns null for courses with no
# dates set. Fix: replace datetime.datetime.fromisoformat(d.pop(field)) calls with a
# null-safe helper inside from_dict() for affected models.
python3 - "$MODELS_DIR" <<'PYEOF'
import sys, os, glob, re

models_dir = sys.argv[1]
# Pattern: bare `datetime.datetime.fromisoformat(d.pop("field"))` inside from_dict
DT_PATTERN = re.compile(
    r'^(\s+)(\w+) = datetime\.datetime\.fromisoformat\(d\.pop\("(\w+)"\)\)\s*$'
)

for path in glob.glob(os.path.join(models_dir, "*.py")):
    lines = open(path).readlines()
    new_lines = []
    changed = False
    in_from_dict = False

    for line in lines:
        if "def from_dict(" in line:
            in_from_dict = True
        elif in_from_dict and re.match(r'^    def ', line) and "from_dict" not in line:
            in_from_dict = False

        if in_from_dict:
            m = DT_PATTERN.match(line)
            if m:
                indent, var, key = m.group(1), m.group(2), m.group(3)
                # Emit a null-safe helper on first match in this file
                if not changed:
                    # Insert helper before first occurrence — handled inline below
                    pass
                new_lines.append(
                    f"{indent}_raw_{var} = d.pop(\"{key}\")\n"
                    f"{indent}{var} = datetime.datetime.fromisoformat(_raw_{var}) "
                    f"if isinstance(_raw_{var}, str) else None\n"
                )
                changed = True
                continue
        new_lines.append(line)

    if changed:
        open(path, 'w').writelines(new_lines)
        print(f"  Fixed null-safe datetime parsing in {os.path.basename(path)}")
PYEOF

# Bug 5: The GET /v2/enrollment/enrollment_allowed/ endpoint returns a plain JSON array
# instead of the expected paginated envelope {"count":N,"results":[...]}.
# Fix: add an isinstance(src_dict, list) guard in from_dict() so a bare list is
# normalised into the envelope shape before the regular parsing runs.
python3 - "$MODELS_DIR" <<'PYEOF'
import sys, os, glob

models_dir = sys.argv[1]
TARGET = "paginated_course_enrollment_allowed_list.py"
# Include the leading 8 spaces so str.replace matches the full line, not just a substring.
MARKER = "        d = dict(src_dict)"
INSERT = (
    "        if isinstance(src_dict, list):\n"
    "            src_dict = {\"count\": len(src_dict), \"results\": src_dict}\n"
)

for path in glob.glob(os.path.join(models_dir, "*.py")):
    if os.path.basename(path) != TARGET:
        continue
    text = open(path).read()
    if INSERT in text:
        break  # already patched
    if MARKER not in text:
        print(f"  WARNING: could not find marker in {TARGET}; skipping Bug 5 fix")
        break
    text = text.replace(MARKER, INSERT + MARKER, 1)
    open(path, 'w').write(text)
    print(f"  Fixed plain-list response in {TARGET}")
PYEOF

echo ""
echo "✓ SDK regenerated successfully."
echo "  Package : openedx_platform_sdk"
echo "  Schema  : $FILTERED_SCHEMA_FILE"
[[ -n "$BRANCH" ]] && echo "  Branch  : $BRANCH"
