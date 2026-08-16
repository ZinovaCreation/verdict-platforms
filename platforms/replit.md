---
name: Replit
slug: replit
operator: Replit Inc. · $1.16B
independence: independent
parent_entity: null
category: AI Coding Agent / Cloud IDE
homepage: https://replit.com
github: null
evaluation_number: 49
evaluation_type: initial
evaluated_at: '2026-04-06'
evaluator_model: unrecorded
framework_version: v0.3.1
layer: '0'
target_version: Replit (replit.com, Agent 3, current production)
previous_evaluation_date: null
previous_score: null
score: 48
max_score: 85
tier: B
verdict:
  v:
    score: 10
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
    score: 6
    rating: null
    note: ''
  i:
    score: 5
    rating: null
    note: ''
  c:
    score: 5
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
next_review_due: '2026-07-05'
tags:
- closed-source
- cloud-IDE
- AI-agent
- SOC2-Type-II-zero-exceptions
- GCP
- container-isolation
- education-market
- Semgrep-scanning
rank: null
sources:
- https://blog.replit.com/
- https://blog.replit.com/2025-replit-in-review
- https://replit.com/
og_description: 'Independent security evaluation of Replit Agent. Score: 48/85. SOC 2 Type II zero exceptions. Agent containment failure (CSA documented). 200-min autonomy window. Public Repl training. Framework v0.3.1.'
category_line: AI Coding Agent / Cloud IDE
display_tags: &id001
- text: SOC 2 II Zero Exceptions
  color: safe
- text: Agent Containment Failure
  color: red
- text: 'Public Repls: Training'
  color: amber
finding: SOC 2 Type II with zero exceptions. Bitsight Advanced (780). Pre-deployment Semgrep scanning. Zero CVEs. Agent containment failure documented by CSA (1,206 records deleted July 2025). 200-min autonomous window.
meta_owner: Replit Inc.
meta_description: 'Independent security evaluation of Replit Agent. Score: 48/85. SOC 2 Type II zero exceptions. Agent containment failure (CSA documented). 200-min autonomy window. Public Repl training. Framework v0.3.1.'
key_finding: SOC 2 II zero exceptions. Semgrep scanning. Agent containment failure (CSA). 200-min autonomy.
card_owner: Replit Inc. · $1.16B
card_category: AI Coding Agent / Cloud IDE
card_tags: *id001
---
# Replit

SOC 2 II zero exceptions. Semgrep scanning. Agent containment failure (CSA). 200-min autonomy.

## Layer 0 Score: 48/85 (Tier B)

**V** 10/20 · **R** 14/20 · **D** 6/15 · **I** 5/10 · **C** 5/10 · **T** 8/10

## CISA KEV

該当なし — no Replit packages appear in the CISA Known Exploited Vulnerabilities catalog. Zero published CVEs attributed to Replit in the trailing 12 months (captured).

## Bias Disclosure

This evaluation uses Claude (Anthropic) as its tooling. Anthropic operates in the AI agent market and may compete with some evaluated vendors. VERDICT discloses this relationship in every report and applies identical evaluation criteria to all platforms regardless of their relationship to Anthropic.

## Full Evaluation

See evaluations/ for the complete Layer 0 report.
