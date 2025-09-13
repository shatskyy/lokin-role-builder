def test_ingestion_minimal_counts_present():
    """Given a small sample raw dataset and a temporary SQLite DB,
    when we run the ingestion CLI, then base tables should have > 0 rows.
    Fixtures: tmp_path for raw files; temporary DB URL.
    """
    pass


def test_idempotent_upsert_no_duplicates():
    """Given the same dataset ingested twice,
    when we re-run ingestion, then no duplicate rows should be created.
    Fixtures: temporary DB pre-seeded with first pass.
    """
    pass


def test_versions_recorded():
    """Given a version string passed to the CLI,
    when ingestion completes, then a versions row should be recorded.
    Fixtures: temporary DB and mocked clock if needed.
    """
    pass
