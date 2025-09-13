# names only; fill later

dev:
	@# TODO: start local dev env or REPL later

test:
	pytest -q || true

sync-onet:
	python -m role_builder.ingest.cli ingest onet --raw-dir $${RAW_ONET_DIR:-./data/raw/onet_30_0} --version 30.0 || true
	python -m role_builder.ingest.cli ingest fts-rebuild || true
	python -m role_builder.ingest.cli ingest verify || true
