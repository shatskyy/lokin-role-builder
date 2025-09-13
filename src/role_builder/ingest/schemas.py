"""SQLAlchemy schema definitions for O*NET subset used in v1.

Tables:
- onet_occupations: core occupation index
- onet_alt_titles: alternate titles for matching
- onet_tasks: task statements and ratings (importance/frequency)
- onet_skills, onet_knowledge, onet_abilities: descriptor domains with importance/level
- onet_work_styles: soft skills importance
- onet_tech_skills: technology skills (optional in v1)
- versions: ingestion version tracking

Indices:
- Btree indexes on foreign keys (onet_code) in child tables.

Docstrings on each model describe fields and notes.
"""

# TODO: from sqlalchemy.orm import declarative_base
# Base = declarative_base()


class OnetOccupation:
    """onet_occupations

    Fields:
    - onet_code (PK, string)
    - title (string)
    - description (text, nullable)
    - job_zone (integer or string, nullable)
    """
    # TODO: Implement SQLAlchemy model
    pass


class OnetAltTitle:
    """onet_alt_titles

    Fields:
    - id (PK, integer autoincrement)
    - onet_code (FK → onet_occupations.onet_code)
    - alt_title (string)
    """
    # TODO: Implement SQLAlchemy model
    pass


class OnetTask:
    """onet_tasks

    Fields:
    - id (PK, integer autoincrement)
    - onet_code (FK)
    - task (text)
    - importance (float, nullable)
    - frequency (float, nullable)
    """
    # TODO: Implement SQLAlchemy model
    pass


class OnetSkill:
    """onet_skills

    Fields:
    - id (PK)
    - onet_code (FK)
    - name (string)
    - importance (float, nullable)
    - level (float, nullable)
    """
    # TODO: Implement SQLAlchemy model
    pass


class OnetKnowledge:
    """onet_knowledge

    Fields:
    - id (PK)
    - onet_code (FK)
    - name (string)
    - importance (float, nullable)
    - level (float, nullable)
    """
    # TODO: Implement SQLAlchemy model
    pass


class OnetAbility:
    """onet_abilities

    Fields:
    - id (PK)
    - onet_code (FK)
    - name (string)
    - importance (float, nullable)
    - level (float, nullable)
    """
    # TODO: Implement SQLAlchemy model
    pass


class OnetWorkStyle:
    """onet_work_styles

    Fields:
    - id (PK)
    - onet_code (FK)
    - name (string)
    - importance (float, nullable)
    """
    # TODO: Implement SQLAlchemy model
    pass


class OnetTechSkill:
    """onet_tech_skills (optional)

    Fields:
    - id (PK)
    - onet_code (FK)
    - tech_name (string)
    - hot_flag (boolean default false)
    """
    # TODO: Implement SQLAlchemy model
    pass


class VersionRecord:
    """versions

    Fields:
    - id (PK)
    - onet_version (string)
    - loaded_at (datetime)
    """
    # TODO: Implement SQLAlchemy model
    pass
