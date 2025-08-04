#!/usr/bin/env bash
set -euo pipefail

# Basic development dependencies for Ubuntu
sudo apt update
sudo apt install -y \
  python3 python3-venv python3-pip \
  nodejs npm \
  git curl \
  docker.io docker-compose-plugin \
  nginx
