# VERDICT population census, 2026-09

Dataset behind VERDICT Population Definition v1 (version date 2026-09-19). Every figure in that document is derived from the files here, and every source was retrieved on the same day.

## Files

- `census_v1_2026-09-19.csv` - one row per population candidate: 30 entries of the MIT AI Agent Index (2025 edition), 50 entries of the Forbes AI 50 (2026), 5 products named in the a16z Top 100 Gen AI Consumer Apps report (6th edition), and 858 GitHub repositories returned by the three topic queries, of which 832 pass the AI-relevance filter (`eligible` = 1).
- `mit_2025_entries.json` - the 30 entry identifiers of the MIT AI Agent Index, 2025 edition. Source: https://aiagentindex.mit.edu/ (CC-BY 4.0). Redistributed with attribution; VERDICT adds nothing to the data.
- `repo_status.json` - repository-level check of the 41 VERDICT evaluations whose subject is an open-source repository: current name, stars, last push, topics, language, population status and reason.
- `corpus_population_status.json` - population status of all 69 VERDICT evaluations on the version date, with the reason for each entry outside the population.
- `sha256sums.txt` - digests of every retrieved source file and of the CSV. Source snapshots marked "local archive only" are retained by VERDICT and are not redistributed.
- `github_query_log.txt` - the three GitHub search queries and their result counts.
- `nonplatform_vocab_v2.txt` - vocabulary used as an ordering aid for the star-descending evaluation queue. It is not part of the population definition and is not applied to the denominator or to any coverage figure.

## CSV columns

`name`, `source_list`, `list_version`, `retrieved_at`, `url`, `stars`, `pushed_at`, `language`, `topics_matched`, `stack_layer_heuristic`, `in_corpus`, `in_corpus_via`, `nonplatform_flag_queue_only`, `eligible`.

## Non-canonical fields

`stack_layer_heuristic`, `nonplatform_flag_queue_only`, and the `in_corpus` mapping are operational aids produced by keyword rules and an Operations-maintained repository table. They are outside the VERDICT schema, carry no evaluative meaning, and will be replaced when the Engine-ratified category-to-stack_layer map is published.

## Scope

Nothing in this dataset is an assessment of any platform. Inclusion means only that a third-party list or a mechanical GitHub condition placed the entry in the field VERDICT measures itself against. Method, adoption tests and known limitations: `docs/selection/population_definition.md` in verdict-engine.
