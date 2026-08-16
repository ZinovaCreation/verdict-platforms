---
name: BabyAGI
slug: babyagi
operator: Yohei Nakajima · Individual
independence: independent
parent_entity: null
category: Experimental Autonomous Agent · OSS (MIT)
homepage: https://yoheinakajima.com
github: https://github.com/yoheinakajima
evaluation_number: 35
evaluation_type: initial
evaluated_at: '2026-03-31'
evaluator_model: unrecorded
framework_version: v0.3.1
layer: '0'
target_version: BabyAGI (github.com/yoheinakajima/babyagi, post-September 2024 rewrite)
previous_evaluation_date: null
previous_score: null
score: 24
max_score: 85
tier: D
verdict:
  v:
    score: 8
    rating: null
    note: ''
  e:
    score: null
    rating: null
    note: null
  r:
    score: 14
    rating: null
    note: ''
  d:
    score: 2
    rating: null
    note: ''
  i:
    score: 0
    rating: null
    note: ''
  c:
    score: 0
    rating: null
    note: ''
  t:
    score: 0
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
next_review_due: '2026-06-29'
tags:
- experimental
- MIT
- individual-maintainer
- historical-significance
- self-building-agent
- non-production
- VC-creator
rank: null
sources:
- https://github.com/yoheinakajima
- https://github.com/yoheinakajima/babyagi
- https://github.com/yoheinakajima/babyagi-2o
- https://github.com/yoheinakajima/babyagi_archive
- https://yoheinakajima.com/
og_description: 'Independent security evaluation of BabyAGI. Score: 24/85. Experimental, not for production. Self-building agent with no containment. I/C/T all 0/10. Historical significance as first popular autonomous agent. Framework v0.3.1.'
category_line: Experimental Autonomous Agent · OSS (MIT)
display_tags: &id001
- text: MIT · 22.2k Stars
  color: dim
- text: 'I/C/T: All 0/10'
  color: red
- text: Not for Production
  color: amber
finding: Historical origin of the autonomous AI agent movement (March 2023, 22.2k stars). Explicitly not for production use. Self-building agent executes arbitrary LLM-generated code with no sandboxing. I, C, T dimensions all score 0/10 — unique in the index. Zero CVEs.
meta_owner: Yohei Nakajima (individual)
meta_description: 'Independent security evaluation of BabyAGI. Score: 24/85. Experimental, not for production. Self-building agent with no containment. I/C/T all 0/10. Historical significance as first popular autonomous agent. Framework v0.3.1.'
key_finding: 'First popular autonomous agent (2023). Experimental only. Self-building agent, no containment. I/C/T: all 0.'
card_owner: Yohei Nakajima · Individual
card_category: Experimental Autonomous Agent · OSS (MIT)
card_tags: *id001
---
# BabyAGI

First popular autonomous agent (2023). Experimental only. Self-building agent, no containment. I/C/T: all 0.

## Layer 0 Score: 24/85 (Tier D)

**V** 8/20 · **R** 14/20 · **D** 2/15 · **I** 0/10 · **C** 0/10 · **T** 0/10

## CISA KEV

該当なし — no BabyAGI packages appear in the CISA Known Exploited Vulnerabilities catalog. Zero published CVEs attributed to BabyAGI in the trailing 12 months (captured).

## Bias Disclosure

This evaluation uses Claude (Anthropic) as its tooling. Anthropic operates in the AI agent market and may compete with some evaluated vendors. VERDICT discloses this relationship in every report and applies identical evaluation criteria to all platforms regardless of their relationship to Anthropic.

## Full Evaluation

See evaluations/ for the complete Layer 0 report.
