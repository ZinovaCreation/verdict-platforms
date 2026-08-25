---
name: Flowise
slug: flowise
operator: Acquired by Workday (Aug 2025)
independence: unrecorded
parent_entity: null
category: LLM Agent Builder · Open Source
homepage: null
github: null
evaluation_number: 7
evaluation_type: update
evaluated_at: '2026-03-24'
evaluator_model: unrecorded
framework_version: v0.3.1
layer: '0'
target_version: null
previous_evaluation_date: '2026-03-13'
previous_score: 37
score: 33
max_score: 85
tier: D
verdict:
  v:
    score: 10
    rating: Mid
    note: ''
  e:
    score: null
    rating: null
    note: null
  r:
    score: 4
    rating: Low
    note: ''
  d:
    score: 4
    rating: Low
    note: ''
  i:
    score: 5
    rating: Mid
    note: ''
  c:
    score: 4
    rating: Mid
    note: ''
  t:
    score: 6
    rating: Mid
    note: ''
cisa_kev:
  present: false
  entries: []
cve_count_12mo: 12
cve_count_basis: lower_bound
max_cvss_12mo: 9.8
supply_chain_compromise_12mo: false
known_facts_applied: []
qa:
  factual: unresolved
  legal: unresolved
  quality: unresolved
  revision_cycles: 0
  flagged: false
differential:
  v: null
  r: re-evaluated
  d: null
  i: null
  c: null
  t: null
  e: null
next_review_due: '2026-06-22'
tags: []
rank: 64
sources: []
og_description: 'Independent security evaluation of Flowise. Score: 33/85. Six CVEs in March 2026 cluster including two CVSS 9.8. Authentication not enforced by default. Acquired by Workday. Framework v0.3.1.'
category_line: LLM Agent Builder · Open Source
display_tags: &id001
- text: 6 CVEs · Mar 2026 Cluster
  color: red
- text: 2× CVSS 9.8 · Auth Not Enforced
  color: red
- text: Acquired by Workday (Aug 2025)
  color: warn
finding: 'March 2026 cluster: 6 CVEs patched in v3.0.13, including CVE-2025-55346 and CVE-2025-58434 (both CVSS 9.8). Structural pattern: authentication not enforced for critical functions across 4+ endpoints.'
meta_description: 'Independent security evaluation of Flowise. Score: 33/85. Six CVEs in March 2026 cluster including two CVSS 9.8. Authentication not enforced by default. Acquired by Workday. Framework v0.3.1.'
key_finding: 'March 2026 cluster: 6 CVEs patched in v3.0.13, including CVE-2025-55346 and CVE-2025-58434 (both CVSS 9.8). Structural pattern confirmed: authentication not enforced for critical functions across 4+ independent endpoints. No CISA KEV.'
card_owner: Acquired by Workday (Aug 2025)
card_category: LLM Agent Builder · Open Source
card_tags: *id001
updated_at: '2026-03-24'
---
# Flowise

March 2026 cluster: 6 CVEs patched in v3.0.13, including CVE-2025-55346 and CVE-2025-58434 (both CVSS 9.8). Structural pattern confirmed: authentication not enforced for critical functions across 4+ independent endpoints. No CISA KEV.

## Layer 0 Score: 33/85 (Tier D)

**V** 10/20 · **R** 4/20 · **D** 4/15 · **I** 5/10 · **C** 4/10 · **T** 6/10

## CISA KEV

該当なし — no Flowise packages appear in the CISA Known Exploited Vulnerabilities catalog. At least 12 published CVEs in the trailing 12 months (published as a bound; basis: lower_bound).

## Bias Disclosure

This evaluation uses Claude (Anthropic) as its tooling. Anthropic operates in the AI agent market and may compete with some evaluated vendors. VERDICT discloses this relationship in every report and applies identical evaluation criteria to all platforms regardless of their relationship to Anthropic.

## Full Evaluation

See evaluations/ for the complete Layer 0 report.