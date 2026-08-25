---
name: Superagent
slug: superagent
operator: Superagent · Gothenburg, Sweden
independence: independent
parent_entity: null
category: AI Agent Security Platform · OSS + Cloud
homepage: https://www.superagent.sh
github: https://github.com/superagent-ai
evaluation_number: 31
evaluation_type: initial
evaluated_at: '2026-03-31'
evaluator_model: unrecorded
framework_version: v0.3.1
layer: '0'
target_version: Superagent (superagent.sh; github.com/superagent-ai/superagent, post-pivot)
previous_evaluation_date: null
previous_score: null
score: 42
max_score: 85
tier: C
verdict:
  v:
    score: 9
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
    score: 8
    rating: Mid
    note: ''
  i:
    score: 3
    rating: Low
    note: ''
  c:
    score: 4
    rating: Mid
    note: ''
  t:
    score: 4
    rating: Mid
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
- pivoted-to-security
- open-source-MIT
- YC-W24
- red-teaming
- guardrails
- ai-firewall
- Swedish-origin
- small-team
rank: 49
sources:
- https://docs.superagent.sh/
- https://docs.superagent.sh/mcp
- https://github.com/superagent-ai
- https://github.com/superagent-ai/superagent
- https://github.com/superagent-ai/superagent/releases
- https://www.superagent.sh/
- https://www.superagent.sh/about
- https://www.superagent.sh/legal
og_description: 'Independent security evaluation of Superagent. Score: 42/85. Pivoted to AI agent security. Guard/Redact/Scan APIs. Zero CVEs. 2-person team. Swedish origin. Framework v0.3.1.'
category_line: AI Agent Security Platform · OSS + Cloud
display_tags: &id001
- text: Security Pivot · YC W24
  color: dim
- text: Guard/Redact/Scan
  color: dim
- text: 2-Person Team
  color: amber
finding: Pivoted from AI agent framework to AI agent security company. Guard/Redact/Scan APIs + AI Firewall + VibeKit sandbox. Zero CVEs. Comprehensive legal docs (GDPR, DPA). 2-person team with $500K creates vendor viability question. No confirmed SOC 2. No SECURITY.md despite being a security company.
meta_owner: Superagent (Alan Zabihi, Ismail Pelaseyed)
meta_description: 'Independent security evaluation of Superagent. Score: 42/85. Pivoted to AI agent security. Guard/Redact/Scan APIs. Zero CVEs. 2-person team. Swedish origin. Framework v0.3.1.'
key_finding: Pivoted to AI security. Guard/Redact/Scan APIs. Zero CVEs. 2-person team. No confirmed SOC 2.
card_owner: Superagent · Gothenburg, Sweden
card_category: AI Agent Security Platform · OSS + Cloud
card_tags: *id001
---
# Superagent

Pivoted to AI security. Guard/Redact/Scan APIs. Zero CVEs. 2-person team. No confirmed SOC 2.

## Layer 0 Score: 42/85 (Tier C)

**V** 9/20 · **R** 14/20 · **D** 8/15 · **I** 3/10 · **C** 4/10 · **T** 4/10

## CISA KEV

該当なし — no Superagent packages appear in the CISA Known Exploited Vulnerabilities catalog. Zero published CVEs attributed to Superagent in the trailing 12 months (captured).

## Bias Disclosure

This evaluation uses Claude (Anthropic) as its tooling. Anthropic operates in the AI agent market and may compete with some evaluated vendors. VERDICT discloses this relationship in every report and applies identical evaluation criteria to all platforms regardless of their relationship to Anthropic.

## Full Evaluation

See evaluations/ for the complete Layer 0 report.
