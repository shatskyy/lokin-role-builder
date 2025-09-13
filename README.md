# lokin-role-builder

FastAPI service scaffold with embeddings utilities and data ingestion tooling.

## Setup

- Create and activate a virtual environment
```bash
python3 -m venv .venv
source .venv/bin/activate
```

- Install dependencies
```bash
pip install -e .[dev]
```

- Environment
Copy `.env.example` to `.env` and adjust values. Default `DATABASE_URL` is `sqlite:///./dev.db`.

## Run app
```bash
uvicorn app.main:app --reload
```

## Database
SQLAlchemy models live under `src/role_builder/models`. Alembic reads `DATABASE_URL` from env via `role_builder.config.get_settings()`.

### Alembic migrations
- Generate a new revision (autogenerate):
```bash
alembic revision --autogenerate -m "your message"
```
- Apply migrations:
```bash
alembic upgrade head
```
- Downgrade one step:
```bash
alembic downgrade -1
```

Initial revision is at `alembic/versions/20250913_000001_init.py`.

## Testing
```bash
pytest -q
```

## Linting
```bash
ruff check .
ruff format .
mypy .
```

