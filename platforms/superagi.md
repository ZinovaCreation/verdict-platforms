---
name: SuperAGI
slug: superagi
operator: TransformErr Inc.
independence: independent
parent_entity: null
category: Agent Management · OSS (MIT)
homepage: https://superagi.com
github: https://github.com/TransformerOptimus
evaluation_number: 40
evaluation_type: initial
evaluated_at: '2026-04-01'
evaluator_model: unrecorded
framework_version: v0.3.1
layer: '0'
target_version: SuperAGI (github.com/TransformerOptimus/SuperAGI, latest main)
previous_evaluation_date: null
previous_score: null
score: 21
max_score: 85
tier: D
verdict:
  v:
    score: 7
    rating: Low
    note: ''
  e:
    score: null
    rating: null
    note: null
  r:
    score: 5
    rating: Low
    note: ''
  d:
    score: 2
    rating: Low
    note: ''
  i:
    score: 2
    rating: Low
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
- open-source
- MIT
- effectively-unmaintained
- Docker
- agent-management
- marketplace
- credential-exposure
rank: 69
sources:
- https://github.com/TransformerOptimus
- https://github.com/TransformerOptimus/SuperAGI
- https://github.com/TransformerOptimus/SuperAGI/releases
- https://github.com/TransformerOptimus/SuperAGI/security
- https://superagi.com/
og_description: 'Independent security evaluation of SuperAGI. Score: 21/85 (index lowest). Effectively unmaintained since mid-2024. Unpatched CVE-2024-9418 (plaintext password). No SECURITY.md. Framework v0.3.1.'
category_line: Agent Management · OSS (MIT)
display_tags: &id001
- text: Unmaintained · Unpatched CVE
  color: red
- text: Plaintext Passwords
  color: red
- text: MIT · 17k Stars
  color: dim
finding: 'Effectively unmaintained since mid-2024. Unpatched CVE-2024-9418: API endpoint returns plaintext passwords enabling account takeover. No SECURITY.md. 17k stars but issues unanswered since 2025. Aging dependencies.'
meta_owner: TransformErr Inc.
meta_description: 'Independent security evaluation of SuperAGI. Score: 21/85 (index lowest). Effectively unmaintained since mid-2024. Unpatched CVE-2024-9418 (plaintext password). No SECURITY.md. Framework v0.3.1.'
key_finding: 'Unmaintained since ~2024. Unpatched CVE: plaintext passwords in API. No SECURITY.md. 17k stars.'
card_owner: TransformErr Inc.
card_category: Agent Management · OSS (MIT)
card_tags: *id001
---
# SuperAGI

Unmaintained since ~2024. Unpatched CVE: plaintext passwords in API. No SECURITY.md. 17k stars.

## Layer 0 Score: 21/85 (Tier D)

**V** 7/20 · **R** 5/20 · **D** 2/15 · **I** 2/10 · **C** 3/10 · **T** 2/10

## CISA KEV

該当なし — no SuperAGI packages appear in the CISA Known Exploited Vulnerabilities catalog. 1 published CVE(s) attributed to SuperAGI in the trailing 12 months (captured).

## Bias Disclosure

This evaluation uses Claude (Anthropic) as its tooling. Anthropic operates in the AI agent market and may compete with some evaluated vendors. VERDICT discloses this relationship in every report and applies identical evaluation criteria to all platforms regardless of their relationship to Anthropic.

## Full Evaluation

See evaluations/ for the complete Layer 0 report.
