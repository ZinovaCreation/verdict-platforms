---
name: AutoGen
slug: autogen
operator: Microsoft Research
independence: independent
parent_entity: null
category: Multi-Agent Framework · Open Source (MIT)
homepage: null
github: https://github.com/microsoft
evaluation_number: 12
evaluation_type: initial
evaluated_at: '2026-03-25'
evaluator_model: unrecorded
framework_version: v0.3.1
layer: '0'
target_version: autogen-agentchat 0.7.5 / AutoGen v0.4 architecture
previous_evaluation_date: null
previous_score: null
score: 56
max_score: 85
tier: A
verdict:
  v:
    score: 11
    rating: null
    note: ''
  e:
    score: null
    rating: null
    note: null
  r:
    score: 20
    rating: null
    note: ''
  d:
    score: 3
    rating: null
    note: ''
  i:
    score: 8
    rating: null
    note: ''
  c:
    score: 6
    rating: null
    note: ''
  t:
    score: 8
    rating: null
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
next_review_due: '2026-06-23'
tags:
- open-source
- multi-agent
- microsoft-research
- python
- MIT-license
- docker-sandbox
- maintenance-mode
rank: null
sources:
- https://github.com/microsoft/autogen
- https://github.com/microsoft/autogen/releases
- https://github.com/microsoft/autogen/security
og_description: 'Independent security evaluation of Microsoft AutoGen. Score: 56/85. Zero public CVEs, MSRC formal coverage since December 2025. Multi-agent orchestration framework. Framework v0.3.1.'
category_line: Multi-Agent Framework · Open Source (MIT)
display_tags: &id001
- text: 0 CVEs · Trailing 12 Months
  color: amber
- text: MSRC In Scope by Default · Dec 2025
  color: amber
- text: AG2 Fork · Package Namespace Split
  color: dim
finding: Zero confirmed CVEs in the trailing 12 months. MSRC provides institutional vulnerability response infrastructure. Docker-based code execution was made the default in v0.2.8 — a proactive secure-by-default design. Now in maintenance mode; successor is the Microsoft Agent Framework.
meta_owner: Microsoft Research
meta_description: 'Independent security evaluation of Microsoft AutoGen. Score: 56/85. Zero public CVEs, MSRC formal coverage since December 2025. Multi-agent orchestration framework. Framework v0.3.1.'
key_finding: 'Zero confirmed CVEs in the trailing 12 months — cleanest security record in this index. Docker-based code execution is the documented and recommended default (PR #7035). MSRC "In Scope by Default" policy (Dec 2025) explicitly covers AutoGen. NIST AI RMF adopted at Microsoft corporate level. AG2 community fork (Nov 2024): pip install autogen installs the AG2 fork, not this codebase.'
card_owner: Microsoft Research
card_category: Multi-Agent Framework · Open Source (MIT)
card_tags: *id001
---
# AutoGen

Zero confirmed CVEs in the trailing 12 months — cleanest security record in this index. Docker-based code execution is the documented and recommended default (PR #7035). MSRC "In Scope by Default" policy (Dec 2025) explicitly covers AutoGen. NIST AI RMF adopted at Microsoft corporate level. AG2 community fork (Nov 2024): pip install autogen installs the AG2 fork, not this codebase.

## Layer 0 Score: 56/85 (Tier A)

**V** 11/20 · **R** 20/20 · **D** 3/15 · **I** 8/10 · **C** 6/10 · **T** 8/10

## CISA KEV

該当なし — no AutoGen packages appear in the CISA Known Exploited Vulnerabilities catalog. Zero published CVEs attributed to AutoGen in the trailing 12 months (captured).

## Bias Disclosure

This evaluation uses Claude (Anthropic) as its tooling. Anthropic operates in the AI agent market and may compete with some evaluated vendors. VERDICT discloses this relationship in every report and applies identical evaluation criteria to all platforms regardless of their relationship to Anthropic.

## Full Evaluation

See evaluations/ for the complete Layer 0 report.
