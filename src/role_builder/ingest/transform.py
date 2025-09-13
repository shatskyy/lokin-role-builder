"""Light transforms for O*NET rows.

Functions accept row dicts from reader.py and return normalized dicts
matching destination table schemas. Implement trimming, type casting,
and defaulting behaviors in coding phase.
"""

from typing import Dict


def normalize_occupation(row: Dict) -> Dict:
    """Normalize occupation row.

    Input keys: {"onet_code", "title", "description", "job_zone"}
    Output keys: {"onet_code", "title", "description", "job_zone"}
    """
    # TODO: implement normalization
    return row


def normalize_alt_title(row: Dict) -> Dict:
    """Normalize alternate title row.

    Input keys: {"onet_code", "alt_title"}
    Output keys: {"onet_code", "alt_title"}
    """
    # TODO: implement normalization
    return row


def normalize_task(row: Dict) -> Dict:
    """Normalize task row.

    Input keys: {"onet_code", "task", "importance", "frequency"}
    Output keys: {"onet_code", "task", "importance", "frequency"}
    """
    # TODO: implement normalization
    return row


def normalize_skill(row: Dict) -> Dict:
    """Normalize skill row.

    Input keys: {"onet_code", "name", "importance", "level"}
    Output keys: {"onet_code", "name", "importance", "level"}
    """
    # TODO: implement normalization
    return row


def normalize_knowledge(row: Dict) -> Dict:
    """Normalize knowledge row.

    Input keys: {"onet_code", "name", "importance", "level"}
    Output keys: {"onet_code", "name", "importance", "level"}
    """
    # TODO: implement normalization
    return row


def normalize_ability(row: Dict) -> Dict:
    """Normalize ability row.

    Input keys: {"onet_code", "name", "importance", "level"}
    Output keys: {"onet_code", "name", "importance", "level"}
    """
    # TODO: implement normalization
    return row


def normalize_work_style(row: Dict) -> Dict:
    """Normalize work style row.

    Input keys: {"onet_code", "name", "importance"}
    Output keys: {"onet_code", "name", "importance"}
    """
    # TODO: implement normalization
    return row


def normalize_tech_skill(row: Dict) -> Dict:
    """Normalize technology skill row.

    Input keys: {"onet_code", "tech_name", "hot_flag"}
    Output keys: {"onet_code", "tech_name", "hot_flag"}
    """
    # TODO: implement normalization
    return row
