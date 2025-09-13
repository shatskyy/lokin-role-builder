"""Database helpers for role_builder.

Responsibilities:
- Build SQLAlchemy engine from DATABASE_URL
- Provide session factory/context manager
- Expose init_db() to create tables from models Base metadata

Note: Designed to later swap to Postgres with minimal changes.
"""

from __future__ import annotations

from contextlib import contextmanager
from typing import Generator

from sqlalchemy import create_engine
from sqlalchemy.engine import Engine
from sqlalchemy.orm import Session, sessionmaker

from .config import get_settings
from .models import Base


_ENGINE: Engine | None = None
_SessionFactory: sessionmaker[Session] | None = None


def get_engine() -> Engine:
    """Return a SQLAlchemy engine built from configuration with sqlite pragmas."""
    global _ENGINE
    if _ENGINE is not None:
        return _ENGINE

    settings = get_settings()
    database_url = settings.get("DATABASE_URL", "sqlite:///./dev.db")

    connect_args = {}
    if database_url.startswith("sqlite"):
        connect_args = {"check_same_thread": False}

    _ENGINE = create_engine(database_url, future=True, echo=False, connect_args=connect_args)
    return _ENGINE


def get_session_factory() -> sessionmaker[Session]:
    """Return a configured sessionmaker bound to the engine."""
    global _SessionFactory
    if _SessionFactory is None:
        _SessionFactory = sessionmaker(bind=get_engine(), autoflush=False, autocommit=False, future=True)
    return _SessionFactory


@contextmanager
def get_session() -> Generator[Session, None, None]:
    """Yield a session with commit/rollback handling."""
    session = get_session_factory()()
    try:
        yield session
        session.commit()
    except Exception:
        session.rollback()
        raise
    finally:
        session.close()


def init_db() -> None:
    """Create all tables if missing using metadata from models Base."""
    engine = get_engine()
    Base.metadata.create_all(bind=engine)
