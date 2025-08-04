#!/bin/bash
set -euo pipefail

# Build Vue frontend
cd /app/frontend

npm ci
npm run build

# Copy built assets to backend static directory
TARGET_DIR="/app/app/static"
rm -rf "$TARGET_DIR"
mkdir -p "$TARGET_DIR"
cp -r dist/* "$TARGET_DIR/"
