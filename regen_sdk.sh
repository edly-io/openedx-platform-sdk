#!/usr/bin/env bash
# Regenerate openedx-platform-sdk from the openedx-platform schema.
#
# Usage:
#   ./regen_sdk.sh                              # uses current branch in openedx-platform
#   ./regen_sdk.sh feat/axim-api_improvements   # checkout branch first, then regenerate
#
# Requirements:
#   pip install openapi-python-client pyyaml
#   Studio running at $STUDIO_URL (default: http://studio.local.openedx.io:8001)

set -euo pipefail

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
PLATFORM_DIR="$(dirname "$SCRIPT_DIR")/openedx-platform"
SCHEMA_FILE="$SCRIPT_DIR/schema.yml"
FILTERED_SCHEMA_FILE="$SCRIPT_DIR/filtered_schema.yml"
FILTER_SCRIPT="$SCRIPT_DIR/filter_schema.py"
CONFIG_FILE="$SCRIPT_DIR/config.yml"
STUDIO_URL="${STUDIO_URL:-http://studio.local.openedx.io:8001}"
SDK_TAG="openedx-platform-sdk"

# ── 1. Optional branch checkout ───────────────────────────────────────────────
BRANCH="${1:-}"
if [[ -n "$BRANCH" ]]; then
    echo "→ Checking out branch '$BRANCH' in openedx-platform..."
    git -C "$PLATFORM_DIR" fetch origin
    git -C "$PLATFORM_DIR" checkout "$BRANCH"
    echo "  Current branch: $(git -C "$PLATFORM_DIR" branch --show-current)"
fi

# ── 2. Download schema from running Studio ────────────────────────────────────
echo "→ Downloading OpenAPI schema from $STUDIO_URL ..."
curl -sf "$STUDIO_URL/authoring-api/schema/" -o "$SCHEMA_FILE"
echo "  Schema written to: $SCHEMA_FILE"

# ── 3. Filter schema to SDK-tagged paths only ─────────────────────────────────
echo "→ Filtering schema to tag '$SDK_TAG'..."
python "$FILTER_SCRIPT" "$SCHEMA_FILE" "$FILTERED_SCHEMA_FILE" "$SDK_TAG"

# ── 4. Regenerate the SDK ─────────────────────────────────────────────────────
echo "→ Regenerating SDK..."
cd "$SCRIPT_DIR"

if [[ -d "$SCRIPT_DIR/openedx_platform_sdk" ]]; then
    openapi-python-client update \
        --path "$FILTERED_SCHEMA_FILE" \
        --config "$CONFIG_FILE"
else
    openapi-python-client generate \
        --path "$FILTERED_SCHEMA_FILE" \
        --config "$CONFIG_FILE"
fi

echo ""
echo "✓ SDK regenerated successfully."
echo "  Package : openedx_platform_sdk"
echo "  Schema  : $FILTERED_SCHEMA_FILE"
[[ -n "$BRANCH" ]] && echo "  Branch  : $BRANCH"
