"""Readers for O*NET raw files.

Each function yields normalized dict rows expected by downstream transforms/loaders.
Skip bad rows and log warnings (to be implemented in coding phase).

Expected filenames under RAW_ONET_DIR (see docs/ingestion-plan.md for exact names):
- Occupation Data.txt
- Alternate Titles.txt (+ Sample of Reported Titles.txt)
- Task Statements.txt, Task Ratings.txt, Task Categories.txt
- Skills.txt, Knowledge.txt, Abilities.txt
- Work Styles.txt
- Technology Skills.txt (optional)
"""

from typing import Dict, Iterable


def read_occupations(raw_dir: str) -> Iterable[Dict]:
    """Yield occupation rows.

    Expected input files: Occupation Data.txt, Job Zones.txt (for job_zone).
    Output schema keys: {"onet_code", "title", "description", "job_zone"}.
    """
    # TODO: Implement parsing
    yield from ()


def read_alt_titles(raw_dir: str) -> Iterable[Dict]:
    """Yield alternate title rows.

    Expected input files: Alternate Titles.txt (and optionally Sample of Reported Titles.txt).
    Output schema keys: {"onet_code", "alt_title"}.
    """
    # TODO: Implement parsing
    yield from ()


def read_tasks(raw_dir: str) -> Iterable[Dict]:
    """Yield task rows with importance/frequency.

    Expected input files: Task Statements.txt, Task Ratings.txt, Task Categories.txt.
    Output schema keys: {"onet_code", "task", "importance", "frequency"}.
    """
    # TODO: Implement parsing
    yield from ()


def read_skills(raw_dir: str) -> Iterable[Dict]:
    """Yield skill rows.

    Expected input files: Skills.txt.
    Output schema keys: {"onet_code", "name", "importance", "level"}.
    """
    # TODO: Implement parsing
    yield from ()


def read_knowledge(raw_dir: str) -> Iterable[Dict]:
    """Yield knowledge rows.

    Expected input files: Knowledge.txt.
    Output schema keys: {"onet_code", "name", "importance", "level"}.
    """
    # TODO: Implement parsing
    yield from ()


def read_abilities(raw_dir: str) -> Iterable[Dict]:
    """Yield ability rows.

    Expected input files: Abilities.txt.
    Output schema keys: {"onet_code", "name", "importance", "level"}.
    """
    # TODO: Implement parsing
    yield from ()


def read_work_styles(raw_dir: str) -> Iterable[Dict]:
    """Yield work style rows.

    Expected input files: Work Styles.txt.
    Output schema keys: {"onet_code", "name", "importance"}.
    """
    # TODO: Implement parsing
    yield from ()


def read_tech_skills(raw_dir: str) -> Iterable[Dict]:
    """Yield technology skill rows (optional for v1).

    Expected input files: Technology Skills.txt.
    Output schema keys: {"onet_code", "tech_name", "hot_flag"}.
    """
    # TODO: Implement parsing
    yield from ()
