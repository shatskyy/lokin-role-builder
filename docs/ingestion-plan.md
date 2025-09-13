# Ingestion Plan (v1 specifics)

## Source → Destination mapping

- Occupation Data.txt → onet_occupations (onet_code, title, description, job_zone)
- Job Zones.txt, Job Zone Reference.txt → join to populate job_zone
- Alternate Titles.txt, Sample of Reported Titles.txt → onet_alt_titles (onet_code, alt_title)
- Task Statements.txt, Task Ratings.txt, Task Categories.txt → onet_tasks (onet_code, task, importance, frequency)
- Skills.txt → onet_skills (onet_code, name, importance, level)
- Knowledge.txt → onet_knowledge (onet_code, name, importance, level)
- Abilities.txt → onet_abilities (onet_code, name, importance, level)
- Work Styles.txt → onet_work_styles (onet_code, name, importance)
- Technology Skills.txt → onet_tech_skills (onet_code, tech_name, hot_flag)

## Key fields & idempotency

- Natural keys:
  - onet_occupations: onet_code
  - onet_alt_titles: (onet_code, alt_title)
  - onet_tasks: (onet_code, task)
  - descriptors (skills/knowledge/abilities/work_styles): (onet_code, name)
  - tech skills: (onet_code, tech_name)
- Idempotency: upserts by natural keys; re-runs update changed values

## Expected counts (high level)

- Occupations ≈ 1,000 rows
- Alt titles: multiple per occupation
- Tasks: multiple per occupation

## Notes

- Readers should be resilient to minor format changes and skip bad rows with warnings.
- Store raw package under data/raw/onet_30_0/.
