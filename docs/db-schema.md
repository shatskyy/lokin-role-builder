# DB Schema (v1)

- onet_occupations (1) → (many)
  - onet_alt_titles
  - onet_tasks
  - onet_skills
  - onet_knowledge
  - onet_abilities
  - onet_work_styles
  - onet_tech_skills (optional)

## Index notes

- Foreign key indexes on child tables: onet_code
- FTS tables (SQLite FTS5): fts_occupations, fts_alt_titles, fts_tasks
- Future Postgres: use tsvector columns + GIN indexes

## Versioning

- versions table records O\*NET package version and loaded_at timestamp
- Future: store version in outputs/generation tables to track provenance
