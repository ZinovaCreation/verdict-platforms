# Contributing

This document specifies how to add or update a platform evaluation. The evaluation itself is produced by following `verdict-engine/ENGINE.md`; this document covers how the resulting record is stored in this repository.

## Governance

This repository is a transparency publication, not a community project. External pull requests are not accepted. The evaluation engine and dataset are maintained solely by VERDICT / ZinovaCreation to preserve single-source methodology governance as a condition of editorial independence.

Factual corrections to published evaluations can be sent to vendor@getverdict.fyi with supporting documentation.

## Adding a new platform

1. Produce the evaluation using the engine — load `verdict-engine/ENGINE.md`, `QA.md`, and `KNOWN_FACTS.md` into the session, run the relevant prompt from `verdict-engine/prompts/`, and pass QA review.
2. Copy [`platforms/_template.md`](./platforms/_template.md) to `platforms/<slug>.md`.
3. Populate the front matter and the report body.
4. Run local validation: `python scripts/validate.py platforms/<slug>.md`
5. Run the indexer: `python scripts/build_index.py`
6. Commit the platform file _and_ the regenerated `rankings/` and `data/platforms.json`.

CI re-runs the indexer and blocks merges if generated artifacts are stale.

## Slug convention

- Lowercase ASCII only
- Hyphen-separated
- Must match `^[a-z0-9][a-z0-9-]*[a-z0-9]$`
- Filename must equal `<slug>.md`
- Slugs are **permanent**. Never rename after publication.

## Front matter schema

Authoritative schema: [`data/schema.json`](./data/schema.json).

```yaml
---
# Identity
name: "Aider"
slug: aider
operator: "Paul Gauthier (individual maintainer)"
independence: independent             # independent | parent | subsidiary
parent_entity: null                   # required non-null if subsidiary
category: "AI Coding Agent"
homepage: "https://aider.chat/"
github: "https://github.com/Aider-AI/aider"

# Evaluation metadata
evaluation_number: 57
evaluation_type: initial              # initial | update
evaluated_at: 2026-04-24
evaluator_model: "claude-opus-4-7"
framework_version: "v0.3.1-final"
layer: "0"                            # "0" | "1" | "C"
target_version: "0.68.0"
previous_evaluation_date: null
previous_score: null

# Scoring (Layer 0: /85; Layer 1: /100)
score: 0
max_score: 85
tier: null                            # auto-assigned by build_index.py

verdict:
  v: { score: 0, rating: null, note: "" }   # 0–20
  r: { score: 0, rating: null, note: "" }   # 0–20
  d: { score: 0, rating: null, note: "" }   # 0–15
  i: { score: 0, rating: null, note: "" }   # 0–10
  c: { score: 0, rating: null, note: "" }   # 0–10
  t: { score: 0, rating: null, note: "" }   # 0–10
  e: { score: null, rating: null, note: null }  # Layer 0: null; Layer 1+: 0–15

# CISA KEV
cisa_kev:
  present: false
  entries: []
  # Example entry:
  #   - cve_id: "CVE-2025-3248"
  #     kev_added_date: 2025-05-05
  #     fcec_deadline: 2025-05-26
  #     elapsed_days: 21

# Incident summary (trailing 12 months)
cve_count_12mo: 0
max_cvss_12mo: null
supply_chain_compromise_12mo: false

# Known facts applied
known_facts_applied: []               # entity keys from KNOWN_FACTS.md

# QA record
qa:
  factual: pass
  legal: pass
  quality: pass
  revision_cycles: 0
  flagged: false

# Differential — null for initial, required object for update
differential: null

# Review cadence
next_review_due: 2026-07-23           # evaluated_at + 90 days (auto)

# Tags
tags: [oss, cli]

# Auto-managed — do not hand-edit
rank: null
---
```

## Field rules

| Field | Rule |
|---|---|
| `name` | Display form. |
| `slug` | Matches regex; matches filename. Never rename after publication. |
| `operator` | Legal entity name + jurisdiction or maintainer identity. |
| `independence` | `independent` for standalone; `parent` when operator is itself a parent; `subsidiary` when owned. |
| `parent_entity` | Required non-null if `independence = subsidiary`. |
| `category` | Free-text consistent across the dataset. |
| `evaluation_number` | VERDICT-internal sequential number. |
| `evaluation_type` | `initial` for first evaluation; `update` for subsequent. |
| `framework_version` | Must match `verdict-engine/ENGINE.md` version in use. |
| `layer` | `0` for public documentation; `1` for behavioral testing; `C` for continuous. |
| `score` | Must equal layer composite (see below). |
| `max_score` | 85 at Layer 0, 100 at Layer 1. |
| `verdict.e.score` | Must be `null` at Layer 0; integer at Layer 1+. |
| `verdict.*.rating` | Optional on write; auto-set by indexer (70%+ High, 40–69% Mid, 0–39% Low). |
| `verdict.*.note` | ≤ 80 characters. Single most informative fact. |
| `cisa_kev.present` | `true` ⇒ `entries` non-empty AND body mentions KEV in all four required sections. |
| `cisa_kev.entries[].cve_id` | Matches `^CVE-\d{4}-\d{4,7}$`. |
| `known_facts_applied` | Entity keys from `KNOWN_FACTS.md`. Empty array if none applicable. |
| `qa.factual/legal/quality` | `pass` / `fail` / `unresolved`. |
| `qa.revision_cycles` | 0–2 per QA protocol. |
| `qa.flagged` | `true` if UNRESOLVED — HUMAN REVIEW REQUIRED. |
| `differential` | Null for `initial`; object with re-evaluated / carried-forward state per axis for `update`. |
| `next_review_due` | `evaluated_at + 90 days` (validator enforces). |
| `rank` | Never hand-edit; owned by indexer. |

## Composite formulas

- **Layer 0:** `score = V + R + D + I + C + T` (max 85). E is excluded.
- **Layer 1:** `score = V + E + R + D + I + C + T` (max 100).

The validator rejects any mismatch.

## Body structure (required sections)

Every platform file's body must contain, in order:

1. **Executive Summary** (`## Executive Summary`) — 3–5 sentences.
2. **Scorecard** (`## Scorecard`) — per-dimension table with rating and CISA KEV line.
3. **Dimension Detail** (`## Dimension Detail`) — six (or seven at Layer 1+) dimension subsections, each with a criterion table plus Positive findings / Recorded concerns.
4. **Incident Timeline** (`## Incident Timeline`) — CVE table or statement of none in trailing 12 months.
5. **Contextual Analysis** (`## Contextual Analysis`) — qualitative observations.
6. **Economic Risk (P dimension)** — include only if an issue is found.
7. **VERDICT Record** (`## VERDICT Record`) — Summary, Risk Factor Summary by Use Case (4 rows), Reference Information (≤3 options), **Bias Disclosure** (verbatim from ENGINE.md).
8. **Future Evaluation Plan** (`## Future Evaluation Plan`) — Layer 1 timing and Layer C monitoring cadence.
9. **Japanese Summary** — in a `japanese-summary` code block.

The validator checks for CISA KEV coverage in four locations (Scorecard, Incident Timeline, Executive Summary, Contextual Analysis) when `cisa_kev.present = true`, and for the verbatim bias-disclosure text in every file.

## Updating an existing evaluation

Update the file in place:

- Bump `evaluated_at` and `target_version` as appropriate.
- Set `evaluation_type: update`.
- Populate `previous_evaluation_date` and `previous_score`.
- Populate `differential` with `re-evaluated` or `carried-forward` for each axis.
- Per ENGINE.md differential rules: R is always re-evaluated; D / I / C typically carry forward unless new evidence exists.
- If total score changes by ≥3, flag for full re-review.

Git history is the audit trail.

## Validation checklist

Before opening a PR:

- [ ] `python scripts/validate.py platforms/<slug>.md` passes
- [ ] `python scripts/build_index.py` committed with up-to-date `rankings/` and `data/platforms.json`
- [ ] `score` matches the layer composite formula
- [ ] `verdict.e` correctly null (Layer 0) or integer (Layer 1+)
- [ ] All axis `note` fields ≤ 80 chars
- [ ] Bias Disclosure verbatim present
- [ ] CISA KEV entries recorded in all four required body sections if present
- [ ] `next_review_due` = `evaluated_at + 90 days`
