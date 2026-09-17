#!/usr/bin/env bash
# Regenerate the javascript SDK from Studio (CMS) and LMS OpenAPI schemas.
#
# Usage mirrors regen_sdk.sh:
#
#   A) CI: pass schema file paths directly
#        CMS_SCHEMA_FILE=platform/cms_schema.yml \
#        LMS_SCHEMA_FILE=platform/lms_schema.yml \
#        ./regen_sdk_js.sh
#
#   B) Local dev with a platform checkout
#        PLATFORM_DIR=/path/to/openedx-platform ./regen_sdk_js.sh
#
#   C) Local dev with a running Studio + LMS instance
#        STUDIO_URL=http://studio.local.openedx.io:8001 \
#        LMS_URL=http://local.openedx.io:8000 \
#        ./regen_sdk_js.sh
#
# Requirements:
#   pip install pyyaml
#   npm install (inside javascript/)

set -euo pipefail

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
FILTERED_SCHEMA_FILE="$SCRIPT_DIR/filtered_schema.yml"
FILTER_SCRIPT="$SCRIPT_DIR/filter_schema.py"
JS_DIR="$SCRIPT_DIR/javascript"
SDK_TAG="openedx-platform-sdk"

CMS_SCHEMA_FILE="${CMS_SCHEMA_FILE:-}"
LMS_SCHEMA_FILE="${LMS_SCHEMA_FILE:-}"

# ── 1. Resolve schema files ───────────────────────────────────────────────────
if [[ -n "${PLATFORM_DIR:-}" ]]; then
    echo "→ Copying schemas from PLATFORM_DIR=$PLATFORM_DIR ..."
    CMS_SCHEMA_FILE="$SCRIPT_DIR/cms_schema.yml"
    LMS_SCHEMA_FILE="$SCRIPT_DIR/lms_schema.yml"
    cp "$PLATFORM_DIR/cms_schema.yml" "$CMS_SCHEMA_FILE"
    cp "$PLATFORM_DIR/lms_schema.yml" "$LMS_SCHEMA_FILE"

elif [[ -n "${STUDIO_URL:-}" && -n "${LMS_URL:-}" ]]; then
    echo "→ Downloading Studio schema from $STUDIO_URL ..."
    CMS_SCHEMA_FILE="$SCRIPT_DIR/cms_schema.yml"
    if ! curl -sf "$STUDIO_URL/authoring-api/schema/" -o "$CMS_SCHEMA_FILE"; then
        echo "Error: Could not reach $STUDIO_URL/authoring-api/schema/"
        exit 1
    fi

    echo "→ Downloading LMS schema from $LMS_URL ..."
    LMS_SCHEMA_FILE="$SCRIPT_DIR/lms_schema.yml"
    if ! curl -sf "$LMS_URL/lms-api/schema/" -o "$LMS_SCHEMA_FILE"; then
        echo "Error: Could not reach $LMS_URL/lms-api/schema/"
        exit 1
    fi

elif [[ -n "$CMS_SCHEMA_FILE" && -n "$LMS_SCHEMA_FILE" ]]; then
    echo "→ Using provided schema files:"
    echo "  CMS schema : $CMS_SCHEMA_FILE"
    echo "  LMS schema : $LMS_SCHEMA_FILE"

else
    echo "Error: No schema source provided."
    echo ""
    echo "Provide one of:"
    echo "  A) CMS_SCHEMA_FILE=... LMS_SCHEMA_FILE=... ./regen_sdk_js.sh"
    echo "  B) PLATFORM_DIR=/path/to/openedx-platform ./regen_sdk_js.sh"
    echo "  C) STUDIO_URL=... LMS_URL=... ./regen_sdk_js.sh"
    exit 1
fi

if [[ ! -f "$CMS_SCHEMA_FILE" ]]; then
    echo "Error: CMS schema file not found: $CMS_SCHEMA_FILE"
    exit 1
fi
if [[ ! -f "$LMS_SCHEMA_FILE" ]]; then
    echo "Error: LMS schema file not found: $LMS_SCHEMA_FILE"
    exit 1
fi

# ── 2. Filter and merge both schemas (same filter the python SDK uses) ────────
echo "→ Filtering and merging schemas for tag '$SDK_TAG'..."
python "$FILTER_SCRIPT" "$CMS_SCHEMA_FILE" "$FILTERED_SCHEMA_FILE" "$SDK_TAG" --merge "$LMS_SCHEMA_FILE"

# ── 3. Regenerate the client ──────────────────────────────────────────────────
echo "→ Regenerating javascript client..."
cd "$JS_DIR"

if [[ ! -d node_modules ]]; then
    echo "→ Installing javascript dependencies..."
    npm ci
fi

# auth.ts and index.ts are hand-written and live outside src/generated,
# so the generator only ever replaces src/generated.
rm -rf src/generated
npm run generate

echo ""
echo "✓ Javascript SDK regenerated successfully."
echo "  Package : javascript"
echo "  Schema  : $FILTERED_SCHEMA_FILE"
