"""CLI entrypoints for ingestion and FTS operations.

Commands:
- ingest onet --raw-dir <path> --version <string>
- ingest fts-rebuild
- ingest verify

Parameters default to environment (RAW_ONET_DIR). Implement behavior in coding phase.
"""

# Placeholder for Typer or argparse-based CLI

def main() -> int:
    """CLI main.

    Should parse subcommands and options, then dispatch to ingestion/FTS/verify
    routines. Returns process exit code (0 on success, non-zero on failure).
    """
    # TODO: Implement CLI in coding phase
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
