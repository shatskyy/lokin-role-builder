"""Configuration for role_builder.

Environment variables (read via python-dotenv if present):

- DB_URL: Database URL. Default: sqlite:///./data/role_builder.sqlite
- USE_EMBEDDINGS: Whether to enable embeddings flows. Default: false
- RAW_ONET_DIR: Path to raw O*NET files. Default: ./data/raw/onet_30_0

Use get_settings() to obtain a simple settings object for the app.
"""

from typing import Any, Dict


def get_settings() -> Dict[str, Any]:
    """Return settings dict.

    This function will read environment variables (optionally via python-dotenv)
    and provide defaults when not set. It intentionally does not perform any I/O
    at import time. Implementation to be added in Phase 2 coding step.
    """
    # TODO: Implement reading .env (python-dotenv) and environment with defaults
    return {}
