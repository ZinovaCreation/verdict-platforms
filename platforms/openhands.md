---
name: OpenHands
slug: openhands
operator: All Hands AI · Cambridge, MA
independence: independent
parent_entity: null
category: AI Coding Agent · OSS (MIT)
homepage: null
github: https://github.com/OpenHands
evaluation_number: 38
evaluation_type: initial
evaluated_at: '2026-04-01'
evaluator_model: unrecorded
framework_version: v0.3.1
layer: '0'
target_version: 1.13.0 (PyPI) / latest main branch
previous_evaluation_date: null
previous_score: null
score: 43
max_score: 85
tier: C
verdict:
  v:
    score: 13
    rating: Mid
    note: ''
  e:
    score: null
    rating: null
    note: null
  r:
    score: 12
    rating: Mid
    note: ''
  d:
    score: 1
    rating: Low
    note: ''
  i:
    score: 6
    rating: Mid
    note: ''
  c:
    score: 4
    rating: Mid
    note: ''
  t:
    score: 7
    rating: High
    note: ''
cisa_kev:
  present: false
  entries: []
cve_count_12mo: 1
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
next_review_due: '2026-06-30'
tags:
- AI coding agent
- open source
- MIT license
- Docker sandbox
- HITL
- LLM-agnostic
- Python
- CLI
- SDK
- cloud service
rank: 46
sources:
- https://github.com/OpenHands/OpenHands
- https://github.com/OpenHands/OpenHands/releases
- https://github.com/OpenHands/software-agent-sdk
- https://openhands.dev/privacy
og_description: 'Independent security evaluation of OpenHands (formerly OpenDevin). Score: 43/85. Docker sandbox. HITL by default. D:1/15 — cloud service permits AI training on user code. Framework v0.3.1.'
category_line: AI Coding Agent · OSS (MIT)
display_tags: &id001
- text: MIT · Docker Sandbox
  color: dim
- text: HITL Default
  color: safe
- text: 'D: 1/15 · AI Training Use'
  color: red
finding: Docker-based sandbox for code execution. HITL enabled by default (opt-in for autonomous mode). D:1/15 — cloud privacy policy permits AI model training on user content including source code. Self-hosted deployment avoids cloud data concerns.
meta_owner: All Hands AI
meta_description: 'Independent security evaluation of OpenHands (formerly OpenDevin). Score: 43/85. Docker sandbox. HITL by default. D:1/15 — cloud service permits AI training on user code. Framework v0.3.1.'
key_finding: Docker sandbox. HITL by default. D:1/15 — cloud permits AI training on user code. 69.5k stars.
card_owner: All Hands AI · Cambridge, MA
card_category: AI Coding Agent · OSS (MIT)
card_tags: *id001
---
# OpenHands

Docker sandbox. HITL by default. D:1/15 — cloud permits AI training on user code. 69.5k stars.

## Layer 0 Score: 43/85 (Tier C)

**V** 13/20 · **R** 12/20 · **D** 1/15 · **I** 6/10 · **C** 4/10 · **T** 7/10

## CISA KEV

該当なし — no OpenHands packages appear in the CISA Known Exploited Vulnerabilities catalog. 1 published CVE(s) attributed to OpenHands in the trailing 12 months (captured).

## Bias Disclosure

This evaluation uses Claude (Anthropic) as its tooling. Anthropic operates in the AI agent market and may compete with some evaluated vendors. VERDICT discloses this relationship in every report and applies identical evaluation criteria to all platforms regardless of their relationship to Anthropic.

## Full Evaluation

See evaluations/ for the complete Layer 0 report.
