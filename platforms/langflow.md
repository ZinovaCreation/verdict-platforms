---
name: Langflow
slug: langflow
operator: IBM (DataStax Acquisition)
independence: unrecorded
parent_entity: null
category: Visual AI Agent Builder · Open Source
homepage: null
github: null
evaluation_number: 8
evaluation_type: update
evaluated_at: '2026-03-24'
evaluator_model: unrecorded
framework_version: v0.3.1
layer: '0'
target_version: null
previous_evaluation_date: '2026-03-13'
previous_score: 33
score: 30
max_score: 85
tier: D
verdict:
  v:
    score: 5
    note: ''
  e:
    score: null
    note: null
  r:
    score: 4
    note: ''
  d:
    score: 4
    note: ''
  i:
    score: 5
    note: ''
  c:
    score: 4
    note: ''
  t:
    score: 6
    note: ''
cisa_kev:
  present: true
  entries:
  - cve_id: CVE-2025-3248
    kev_added_date: '2025-05-05'
    fcec_deadline: null
cve_count_12mo: null
cve_count_basis: conflicting
max_cvss_12mo: null
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
rank: null
sources: []
og_description: 'Independent security evaluation of Langflow. Score: 30/85 — lowest in the VERDICT index. CISA KEV listed (CVE-2025-3248, CVSS 9.8). Flodrix botnet exploitation. IBM acquired. Framework v0.3.1.'
category_line: Visual AI Agent Builder · Open Source
display_tags: &id001
- text: CISA KEV · CVE-2025-3248
  color: red
- text: 6 CVEs · Mar 2026
  color: red
- text: IBM Acquired · Aug 2025
  color: dim
finding: 'CVE-2025-3248 (CVSS 9.8) added to CISA KEV May 2025 after Flodrix botnet infections across 1,000+ instances. ~12 months from first report to patch. Triple ownership: Logspace → DataStax → IBM.'
meta_description: 'Independent security evaluation of Langflow. Score: 30/85 — lowest in the VERDICT index. CISA KEV listed (CVE-2025-3248, CVSS 9.8). Flodrix botnet exploitation. IBM acquired. Framework v0.3.1.'
key_finding: CISA KEV listed (CVE-2025-3248). IBM acquired via DataStax. 6 CVEs in March 2026 cluster. Auth not enforced across critical endpoints.
card_owner: IBM (DataStax Acquisition)
card_category: Visual AI Agent Builder · Open Source
card_tags: *id001
updated_at: '2026-03-24'
score_basis: published_inconsistent
---
# Langflow

CISA KEV listed (CVE-2025-3248). IBM acquired via DataStax. 6 CVEs in March 2026 cluster. Auth not enforced across critical endpoints.

## Layer 0 Score: 30/85 (Tier D)

**V** 5/20 · **R** 4/20 · **D** 4/15 · **I** 5/10 · **C** 4/10 · **T** 6/10

## CISA KEV

Listed — CVE-2025-3248 appears in the CISA Known Exploited Vulnerabilities catalog (captured from the published evaluation).

## Scorecard

The Scorecard of the original evaluation contains no KEV language (captured as-published; not synthesized in migration).

## Incident Timeline

KEV May 2025) | | | Python code passed to exec() | KEV

## Executive Summary

CVE-2025-3248 (CVSS 9.8, CISA KEV), confirming the structural issues criterion

## Contextual Analysis

exploitation of both. CVE-2025-3248 is in the CISA KEV catalog. CVE-2026-33017

## Source Divergence (recorded as-published, not reconciled)

Published live card: score 30/85; card dimension scores V 5 / R 4 / D 4 / I 5 / C 4 / T 6 (sum 28). Published evaluation record (Notion v2, 2026-03-24 revision): Scorecard V 8 / R 8 / D 3 / I 5 / C 2 / T 4 (sum 30), Total 30/85. The migration captures the live card values (the §4 capture-fidelity SSOT) and records the divergence; which dimension set is current is not decided here (a v1-era origin for the card dims is a hypothesis, unconfirmed and not asserted). Resolution is a re-evaluation. The CVE count is likewise recorded as conflicting (criterion table 2 vs card 6).

## Bias Disclosure

This evaluation uses Claude (Anthropic) as its tooling. Anthropic operates in the AI agent market and may compete with some evaluated vendors. VERDICT discloses this relationship in every report and applies identical evaluation criteria to all platforms regardless of their relationship to Anthropic.

## Full Evaluation

See evaluations/ for the complete Layer 0 report.