def test_fts_occupations_basic_query():
    """Given a small ingested dataset and rebuilt FTS,
    when we query for a simple keyword, then occupation rows should be found.
    Fixtures: temporary DB, sample data, FTS rebuild call.
    """
    pass


def test_fts_alt_titles_basic_query():
    """Given alternate titles ingested and FTS rebuilt,
    when we query using an alias title, then results should include matching onet_code.
    Fixtures: temporary DB, sample alt titles.
    """
    pass


def test_fts_tasks_basic_query():
    """Given tasks ingested and FTS rebuilt,
    when we query for a task keyword, then task rows should be found.
    Fixtures: temporary DB, sample tasks.
    """
    pass
