"""Configuration for role_builder.

Environment variables (read via python-dotenv if present):

- DATABASE_URL: Database URL. Default: sqlite:///./dev.db
- USE_EMBEDDINGS: Whether to enable embeddings flows. Default: false
- RAW_ONET_DIR: Path to raw O*NET files. Default: ./data/raw/onet_30_0

Use get_settings() to obtain a simple settings object for the app.
"""

from __future__ import annotations

import os
from typing import Any, Dict

from dotenv import load_dotenv


def get_settings() -> Dict[str, Any]:
    """Return settings dict using env vars and sane defaults.

    Loads variables from a local .env if present and then overlays process env.
    """
    # Load variables from .env if present (no error if missing)
    load_dotenv(override=False)

    database_url = os.getenv("DATABASE_URL", "sqlite:///./dev.db")
    use_embeddings_env = os.getenv("USE_EMBEDDINGS", "false").lower()
    use_embeddings = use_embeddings_env in {"1", "true", "yes", "y"}
    raw_onet_dir = os.getenv("RAW_ONET_DIR", "./data/raw/onet_30_0")

    return {
        "DATABASE_URL": database_url,
        "USE_EMBEDDINGS": use_embeddings,
        "RAW_ONET_DIR": raw_onet_dir,
    }
