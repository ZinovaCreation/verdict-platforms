---
name: n8n
slug: n8n
operator: Independent · n8n GmbH (Berlin)
independence: unrecorded
parent_entity: null
category: Workflow Automation · Open Source
homepage: null
github: null
evaluation_number: 1
evaluation_type: update
evaluated_at: '2026-03-24'
evaluator_model: unrecorded
framework_version: v0.3.1
layer: '0'
target_version: null
previous_evaluation_date: '2026-03-13'
previous_score: 40
score: 35
max_score: 85
tier: C
verdict:
  v:
    score: 12
    note: ''
  e:
    score: null
    note: null
  r:
    score: 5
    note: ''
  d:
    score: 3
    note: ''
  i:
    score: 6
    note: ''
  c:
    score: 3
    note: ''
  t:
    score: 6
    note: ''
cisa_kev:
  present: true
  entries:
  - cve_id: CVE-2025-68613
    kev_added_date: '2026-03-11'
    fcec_deadline: '2026-03-25'
cve_count_12mo: 12
cve_count_basis: lower_bound
max_cvss_12mo: 10.0
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
og_description: 'Independent security evaluation of n8n. Score: 35/85. CISA KEV listed (CVE-2025-68613, CVSS 9.9). 12+ CVEs in trailing 12 months. Structural sandbox bypass pattern across 5+ CVEs. Framework v0.3.1.'
category_line: Workflow Automation · Open Source
display_tags: &id001
- text: CISA KEV · CVE-2025-68613
  color: red
- text: 12+ CVEs · 2× CVSS 10.0
  color: red
- text: Structural Sandbox Bypass · 5+ CVEs
  color: red
finding: 12+ CVEs in trailing 12 months. Two CVSS 10.0 vulnerabilities confirmed (CVE-2026-21858, CVE-2026-21877). CVE-2025-68613 added to CISA KEV catalog March 2026. Blocklist-based sandbox bypass confirmed across 5+ independent CVEs.
meta_description: 'Independent security evaluation of n8n. Score: 35/85. CISA KEV listed (CVE-2025-68613, CVSS 9.9). 12+ CVEs in trailing 12 months. Structural sandbox bypass pattern across 5+ CVEs. Framework v0.3.1.'
key_finding: 12+ CVEs in trailing 12 months. Two CVSS 10.0 vulnerabilities confirmed (CVE-2026-21858, CVE-2026-21877). CVE-2025-68613 added to CISA KEV catalog March 2026 — FCEB patch deadline March 25, 2026. Blocklist-based sandbox bypass confirmed across 5+ independent CVEs.
card_owner: Independent · n8n GmbH (Berlin)
card_category: Workflow Automation · Open Source
card_tags: *id001
updated_at: '2026-03-24'
---
# n8n

12+ CVEs in trailing 12 months. Two CVSS 10.0 vulnerabilities confirmed (CVE-2026-21858, CVE-2026-21877). CVE-2025-68613 added to CISA KEV catalog March 2026 — FCEB patch deadline March 25, 2026. Blocklist-based sandbox bypass confirmed across 5+ independent CVEs.

## Layer 0 Score: 35/85 (Tier C)

**V** 12/20 · **R** 5/20 · **D** 3/15 · **I** 6/10 · **C** 3/10 · **T** 6/10

## CISA KEV

Listed — CVE-2025-68613 appears in the CISA Known Exploited Vulnerabilities catalog (captured from the published evaluation).

## Scorecard

12-month CVE record including CISA KEV confirmation and structural issues

## Incident Timeline

| | | ⚠️ CISA KEV: Added 2026.03.11 | v1.122.0

## Executive Summary

The Executive Summary of the original evaluation contains no KEV language (captured as-published; not synthesized in migration).

## Contextual Analysis

CISA's March 11, 2026 KEV designation for CVE-2025-68613 carries operational

## Bias Disclosure

This evaluation uses Claude (Anthropic) as its tooling. Anthropic operates in the AI agent market and may compete with some evaluated vendors. VERDICT discloses this relationship in every report and applies identical evaluation criteria to all platforms regardless of their relationship to Anthropic.

## Full Evaluation

See evaluations/ for the complete Layer 0 report.