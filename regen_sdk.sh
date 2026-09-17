#!/usr/bin/env bash
# Regenerate openedx-platform-sdk from Studio (CMS) and LMS OpenAPI schemas.
#
# Usage:
#   ./regen_sdk.sh
#
# Schema source (pick one — CI uses option A, local dev uses B or C):
#
#   A) CI: pass schema file paths directly (used by regenerate_sdk.yml):
#        CMS_SCHEMA_FILE=platform/cms_schema.yml \
#        LMS_SCHEMA_FILE=platform/lms_schema.yml \
#        ./regen_sdk.sh
#
#   B) Local dev with a platform checkout (copies schemas from it):
#        PLATFORM_DIR=/path/to/openedx-platform ./regen_sdk.sh
#
#   C) Local dev with a running Studio + LMS instance:
#        STUDIO_URL=http://studio.local.openedx.io:8001 \
#        LMS_URL=http://local.openedx.io:8000 \
#        ./regen_sdk.sh
#
# Requirements:
#   pip install openapi-python-client pyyaml

set -euo pipefail

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
FILTERED_SCHEMA_FILE="$SCRIPT_DIR/filtered_schema.yml"
FILTER_SCRIPT="$SCRIPT_DIR/filter_schema.py"
CONFIG_FILE="$SCRIPT_DIR/config.yml"
SDK_TAG="openedx-platform-sdk"

# Schema file paths — override via env vars or derived below.
CMS_SCHEMA_FILE="${CMS_SCHEMA_FILE:-}"
LMS_SCHEMA_FILE="${LMS_SCHEMA_FILE:-}"

# ── 1. Resolve schema files ───────────────────────────────────────────────────
if [[ -n "${PLATFORM_DIR:-}" ]]; then
    # Copy schemas from a local platform checkout (for testing unreleased changes).
    echo "→ Copying schemas from PLATFORM_DIR=$PLATFORM_DIR ..."
    CMS_SCHEMA_FILE="$SCRIPT_DIR/cms_schema.yml"
    LMS_SCHEMA_FILE="$SCRIPT_DIR/lms_schema.yml"
    cp "$PLATFORM_DIR/cms_schema.yml" "$CMS_SCHEMA_FILE"
    cp "$PLATFORM_DIR/lms_schema.yml" "$LMS_SCHEMA_FILE"
    echo "  CMS schema : $CMS_SCHEMA_FILE"
    echo "  LMS schema : $LMS_SCHEMA_FILE"

elif [[ -n "${STUDIO_URL:-}" && -n "${LMS_URL:-}" ]]; then
    # Download live schemas from running Studio and LMS instances.
    echo "→ Downloading Studio schema from $STUDIO_URL ..."
    CMS_SCHEMA_FILE="$SCRIPT_DIR/cms_schema.yml"
    if ! curl -sf "$STUDIO_URL/authoring-api/schema/" -o "$CMS_SCHEMA_FILE"; then
        echo "Error: Could not reach $STUDIO_URL/authoring-api/schema/"
        exit 1
    fi
    echo "  CMS schema written to: $CMS_SCHEMA_FILE"

    echo "→ Downloading LMS schema from $LMS_URL ..."
    LMS_SCHEMA_FILE="$SCRIPT_DIR/lms_schema.yml"
    if ! curl -sf "$LMS_URL/lms-api/schema/" -o "$LMS_SCHEMA_FILE"; then
        echo "Error: Could not reach $LMS_URL/lms-api/schema/"
        exit 1
    fi
    echo "  LMS schema written to: $LMS_SCHEMA_FILE"

elif [[ -n "$CMS_SCHEMA_FILE" && -n "$LMS_SCHEMA_FILE" ]]; then
    # Use explicitly provided schema file paths — no download needed.
    echo "→ Using provided schema files:"
    echo "  CMS schema : $CMS_SCHEMA_FILE"
    echo "  LMS schema : $LMS_SCHEMA_FILE"

else
    echo "Error: No schema source provided."
    echo ""
    echo "Provide one of:"
    echo "  A) Schema file paths:"
    echo "       CMS_SCHEMA_FILE=/path/to/cms_schema.yml LMS_SCHEMA_FILE=/path/to/lms_schema.yml ./regen_sdk.sh"
    echo "  B) Running instance URLs:"
    echo "       STUDIO_URL=http://studio.local.openedx.io:8001 LMS_URL=http://local.openedx.io:8000 ./regen_sdk.sh"
    echo "  C) Local platform checkout:"
    echo "       PLATFORM_DIR=/path/to/openedx-platform ./regen_sdk.sh"
    exit 1
fi

# Verify the resolved schema files exist.
if [[ ! -f "$CMS_SCHEMA_FILE" ]]; then
    echo "Error: CMS schema file not found: $CMS_SCHEMA_FILE"
    exit 1
fi
if [[ ! -f "$LMS_SCHEMA_FILE" ]]; then
    echo "Error: LMS schema file not found: $LMS_SCHEMA_FILE"
    exit 1
fi

# ── 2. Filter and merge both schemas ──────────────────────────────────────────
echo "→ Filtering and merging schemas for tag '$SDK_TAG'..."
python "$FILTER_SCRIPT" "$CMS_SCHEMA_FILE" "$FILTERED_SCHEMA_FILE" "$SDK_TAG" --merge "$LMS_SCHEMA_FILE"

# ── 3. Regenerate the SDK ─────────────────────────────────────────────────────
echo "→ Regenerating SDK..."

# Everything below works out of a single scratch directory that is removed on
# exit, however the script terminates.
work_dir="$(mktemp -d)"
trap 'rm -rf "$work_dir"' EXIT

# Preserve hand-written files before wiping the package directory.
cp "$SCRIPT_DIR/openedx_platform_sdk/auth.py" "$work_dir/auth.py" 2>/dev/null || true

# Generate into the scratch directory; openapi-python-client always creates a
# new project folder — we only want the inner package directory.
gen_dir="$work_dir/generated"
openapi-python-client generate \
    --path "$FILTERED_SCHEMA_FILE" \
    --config "$CONFIG_FILE" \
    --output-path "$gen_dir" \
    --overwrite

# Replace only the auto-generated package directory.
rm -rf "$SCRIPT_DIR/openedx_platform_sdk"
mv "$gen_dir/openedx_platform_sdk" "$SCRIPT_DIR/openedx_platform_sdk"

# Restore hand-written files. postprocess_sdk.py re-adds the auth exports to
# __init__.py, which the generator rewrites without them.
if [[ -f "$work_dir/auth.py" ]]; then
    cp "$work_dir/auth.py" "$SCRIPT_DIR/openedx_platform_sdk/auth.py"
fi

# Apply all five generator-bug fixes and restore the auth exports
# (see postprocess_sdk.py for details).
python "$SCRIPT_DIR/postprocess_sdk.py" "$SCRIPT_DIR"

echo ""
echo "✓ SDK regenerated successfully."
echo "  Package : openedx_platform_sdk"
echo "  Schema  : $FILTERED_SCHEMA_FILE"
