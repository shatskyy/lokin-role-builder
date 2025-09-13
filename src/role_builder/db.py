"""Database helpers for role_builder.

Responsibilities:
- Build SQLAlchemy engine from DB_URL
- Provide session factory/context manager
- Expose init_db() to create tables from schemas metadata

Note: Designed to later swap to Postgres with minimal changes.
"""

from typing import Any


# TODO: from .ingest.schemas import Base (SQLAlchemy metadata)


def get_engine() -> Any:
    """Return a SQLAlchemy engine built from configuration.

    Implementation to be added in Phase 2 coding step.
    """
    # TODO: create_engine using DB_URL from config
    return None


def get_session() -> Any:
    """Return a session factory/context manager.

    Implementation to be added in Phase 2 coding step.
    """
    # TODO: sessionmaker(bind=engine)
    return None


def init_db() -> None:
    """Create all tables if missing using metadata from schemas.py.

    Implementation to be added in Phase 2 coding step.
    """
    # TODO: Base.metadata.create_all(engine)
    return None
