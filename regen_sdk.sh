#!/usr/bin/env bash
# Regenerate openedx-platform-sdk from the openedx-platform OpenAPI schema.
#
# Usage:
#   ./regen_sdk.sh                                    # regenerate from running Studio (no platform repo needed)
#   ./regen_sdk.sh feat/axim-api_improvements         # checkout branch first, then regenerate
#
# Environment variables:
#   STUDIO_URL       Base URL of running Studio  (default: http://studio.local.openedx.io:8001)
#   PLATFORM_DIR     Path to local openedx-platform repo (default: ../openedx-platform)
#                    Only needed when passing a branch argument.
#
# Requirements:
#   pip install openapi-python-client pyyaml

set -euo pipefail

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
SCHEMA_FILE="$SCRIPT_DIR/schema.yml"
FILTERED_SCHEMA_FILE="$SCRIPT_DIR/filtered_schema.yml"
FILTER_SCRIPT="$SCRIPT_DIR/filter_schema.py"
CONFIG_FILE="$SCRIPT_DIR/config.yml"
STUDIO_URL="${STUDIO_URL:-http://studio.local.openedx.io:8001}"
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

# ── 2. Download schema from running Studio ────────────────────────────────────
echo "→ Downloading OpenAPI schema from $STUDIO_URL ..."
if ! curl -sf "$STUDIO_URL/authoring-api/schema/" -o "$SCHEMA_FILE"; then
    echo "Error: Could not reach $STUDIO_URL/authoring-api/schema/"
    echo "Make sure Studio is running. Override the URL with:"
    echo "  STUDIO_URL=http://your-studio-url:port ./regen_sdk.sh"
    exit 1
fi
echo "  Schema written to: $SCHEMA_FILE"

# ── 3. Filter schema to SDK-tagged paths only ─────────────────────────────────
echo "→ Filtering schema to tag '$SDK_TAG'..."
python "$FILTER_SCRIPT" "$SCHEMA_FILE" "$FILTERED_SCHEMA_FILE" "$SDK_TAG"

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

echo ""
echo "✓ SDK regenerated successfully."
echo "  Package : openedx_platform_sdk"
echo "  Schema  : $FILTERED_SCHEMA_FILE"
[[ -n "$BRANCH" ]] && echo "  Branch  : $BRANCH"
