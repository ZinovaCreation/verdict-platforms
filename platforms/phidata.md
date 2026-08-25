---
name: Phidata (Agno)
slug: phidata
operator: Phidata Inc.
independence: independent
parent_entity: null
category: Multi-Agent Framework · OSS (MPL 2.0)
homepage: https://www.agno.com
github: https://github.com/agno-agi
evaluation_number: 32
evaluation_type: initial
evaluated_at: '2026-03-31'
evaluator_model: unrecorded
framework_version: v0.3.1
layer: '0'
target_version: Agno (github.com/agno-agi/agno, latest; agno.com)
previous_evaluation_date: null
previous_score: null
score: 38
max_score: 85
tier: C
verdict:
  v:
    score: 11
    rating: Mid
    note: ''
  e:
    score: null
    rating: null
    note: null
  r:
    score: 14
    rating: High
    note: ''
  d:
    score: 3
    rating: Low
    note: ''
  i:
    score: 5
    rating: Mid
    note: ''
  c:
    score: 3
    rating: Low
    note: ''
  t:
    score: 2
    rating: Low
    note: ''
cisa_kev:
  present: false
  entries: []
cve_count_12mo: 0
cve_count_basis: exact
max_cvss_12mo: null
supply_chain_compromise_12mo: false
known_facts_applied: []
qa:
  factual: unresolved
  legal: unresolved
  quality: unresolved
  revision_cycles: 0
  flagged: false
differential: null
next_review_due: '2026-06-29'
tags:
- open-source
- MPL-2.0
- self-hosted
- multi-agent
- multi-modal
- HITL-native
- telemetry-default-on
- rebranded
rank: 56
sources:
- https://docs.phidata.com/introduction
- https://github.com/agno-agi
- https://github.com/agno-agi/agno
- https://github.com/agno-agi/phidata
- https://www.agno.com/
og_description: 'Independent security evaluation of Phidata/Agno. Score: 38/85. Zero CVEs. Self-hosted data sovereignty. HITL as architecture primitive. Telemetry default ON. Framework v0.3.1.'
category_line: Multi-Agent Framework · OSS (MPL 2.0)
display_tags: &id001
- text: MPL 2.0 · Self-Hosted
  color: dim
- text: Telemetry Default ON
  color: red
- text: No SECURITY.md
  color: amber
finding: 'Zero CVEs. Self-hosted architecture: all agent data in user''s own database. HITL and runtime approval as architectural primitives. Telemetry enabled by default (model usage to api.phidata.com). No privacy policy on agno.com. No SECURITY.md.'
meta_owner: Phidata Inc.
meta_description: 'Independent security evaluation of Phidata/Agno. Score: 38/85. Zero CVEs. Self-hosted data sovereignty. HITL as architecture primitive. Telemetry default ON. Framework v0.3.1.'
key_finding: Zero CVEs. Self-hosted data sovereignty. HITL as architecture primitive. Telemetry default ON.
card_owner: Phidata Inc.
card_category: Multi-Agent Framework · OSS (MPL 2.0)
card_tags: *id001
---
# Phidata (Agno)

Zero CVEs. Self-hosted data sovereignty. HITL as architecture primitive. Telemetry default ON.

## Layer 0 Score: 38/85 (Tier C)

**V** 11/20 · **R** 14/20 · **D** 3/15 · **I** 5/10 · **C** 3/10 · **T** 2/10

## CISA KEV

該当なし — no Phidata (Agno) packages appear in the CISA Known Exploited Vulnerabilities catalog. Zero published CVEs attributed to Phidata (Agno) in the trailing 12 months (captured).

## Bias Disclosure

This evaluation uses Claude (Anthropic) as its tooling. Anthropic operates in the AI agent market and may compete with some evaluated vendors. VERDICT discloses this relationship in every report and applies identical evaluation criteria to all platforms regardless of their relationship to Anthropic.

## Full Evaluation

See evaluations/ for the complete Layer 0 report.
