#!/usr/bin/env bash
set -euo pipefail

# Build Vue frontend
SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
cd "$SCRIPT_DIR/../frontend"

npm ci
npm run build

# Copy built assets to backend static directory
TARGET_DIR="$SCRIPT_DIR/../app/static"
rm -rf "$TARGET_DIR"
mkdir -p "$TARGET_DIR"
cp -r dist/* "$TARGET_DIR/"
