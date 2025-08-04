# FastAPI + Vue Template

This repository provides a minimal template for a FastAPI backend with a Vue frontend.

## Backend
- FastAPI application configured via [pydantic-settings](https://pydantic-docs.helpmanual.io/usage/settings/).
- Built-in middlewares: CORS and gzip compression.
- Static assets served from `app/static`.
- All API endpoints, including docs, доступны по префиксу `/api`.
- Settings читаются из переменных окружения `app/.env` (см. `app/.env.example`).
- Списки значений в переменных окружения задаются через запятую или в JSON-формате.

## Frontend
- Vue 3 application bootstrapped with Vite.
- Build the static assets via `./scripts/build_frontend.sh`.

## Scripts
- `scripts/build_frontend.sh` – install dependencies, build the Vue frontend and copy assets to the backend.
- `scripts/setup.sh` – install system packages on a fresh Ubuntu server.

## Docker
- `Dockerfile` for the FastAPI backend.
- `docker-compose.yml` to run backend and nginx that serves static files and proxies API requests.

## Development
1. Copy `app/.env.example` to `app/.env` and adjust values.
2. Install Python dependencies: `pip install -r requirements.txt`.
3. Build frontend assets: `./scripts/build_frontend.sh`.
4. Run with Docker: `docker-compose up --build`.
