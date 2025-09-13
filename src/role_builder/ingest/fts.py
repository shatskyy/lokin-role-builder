"""SQLite FTS5 helpers for occupations, alt titles, and tasks.

Functions create/populate virtual FTS tables mirroring base tables.
No triggers in v1; callers should explicitly rebuild after ingestion.
Postgres migration note: use tsvector columns and GIN indexes with to_tsvector().
"""

from typing import Dict, Any


def create_fts_indexes(engine: Any) -> None:
    """Create FTS virtual tables if missing.

    Tables:
    - fts_occupations(title, description, onet_code)
    - fts_alt_titles(alt_title, onet_code)
    - fts_tasks(task, onet_code)
    """
    # TODO: Implement
    return None


def populate_fts_indexes(engine: Any) -> Dict[str, int]:
    """Populate FTS tables from base tables.

    Returns a dict of table_name → rows inserted.
    """
    # TODO: Implement
    return {}


def rebuild_fts(engine: Any) -> Dict[str, int]:
    """Drop, recreate, and repopulate all FTS tables.

    Returns a dict of table_name → rows inserted.
    """
    # TODO: Implement
    return {}
