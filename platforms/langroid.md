---
name: Langroid
slug: langroid
operator: Prasad Chalasani (CMU) · Individual
independence: independent
parent_entity: null
category: Multi-Agent LLM Framework · OSS (MIT)
homepage: https://langroid.substack.com
github: https://github.com/langroid
evaluation_number: 28
evaluation_type: initial
evaluated_at: '2026-03-31'
evaluator_model: unrecorded
framework_version: v0.3.1
layer: '0'
target_version: Langroid 0.53.x (langroid PyPI package; github.com/langroid/langroid)
previous_evaluation_date: null
previous_score: null
score: 34
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
    score: 5
    rating: Low
    note: ''
  d:
    score: 6
    rating: Mid
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
    score: 8
    rating: High
    note: ''
cisa_kev:
  present: false
  entries: []
cve_count_12mo: 1
cve_count_basis: exact
max_cvss_12mo: 9.4
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
- MIT
- python
- academic-origin
- CMU
- multi-agent
- actor-model
- lightweight
rank: 63
sources:
- https://github.com/langroid/langroid
- https://github.com/langroid/langroid/security
- https://langroid.substack.com/
og_description: 'Independent security evaluation of Langroid. Score: 34/85. CVE-2026-25481 CVSS 9.4 Critical RCE. Highest transparency (T: 8/10) among OSS frameworks. CMU origin. Framework v0.3.1.'
category_line: Multi-Agent LLM Framework · OSS (MIT)
display_tags: &id001
- text: CVE-2026-25481 · CVSS 9.4
  color: red
- text: 'T: 8/10 · Transparency Leader'
  color: safe
- text: MIT · CMU Origin
  color: dim
finding: CVE-2026-25481 (CVSS 9.4 Critical RCE in TableChatAgent) within evaluation window. Recurring code injection pattern in same component. Despite this, transparency score 8/10 is highest among OSS frameworks — maintainer published the CVE himself with fix available at disclosure. 48-hour response commitment.
meta_owner: Prasad Chalasani (individual)
meta_description: 'Independent security evaluation of Langroid. Score: 34/85. CVE-2026-25481 CVSS 9.4 Critical RCE. Highest transparency (T: 8/10) among OSS frameworks. CMU origin. Framework v0.3.1.'
key_finding: 'CVE-2026-25481 CVSS 9.4 RCE. But T: 8/10 — maintainer published CVE himself. 48h response commitment.'
card_owner: Prasad Chalasani (CMU) · Individual
card_category: Multi-Agent LLM Framework · OSS (MIT)
card_tags: *id001
---
# Langroid

CVE-2026-25481 CVSS 9.4 RCE. But T: 8/10 — maintainer published CVE himself. 48h response commitment.

## Layer 0 Score: 34/85 (Tier D)

**V** 10/20 · **R** 5/20 · **D** 6/15 · **I** 2/10 · **C** 3/10 · **T** 8/10

## CISA KEV

該当なし — no Langroid packages appear in the CISA Known Exploited Vulnerabilities catalog. 1 published CVE(s) attributed to Langroid in the trailing 12 months (captured).

## Bias Disclosure

This evaluation uses Claude (Anthropic) as its tooling. Anthropic operates in the AI agent market and may compete with some evaluated vendors. VERDICT discloses this relationship in every report and applies identical evaluation criteria to all platforms regardless of their relationship to Anthropic.

## Full Evaluation

See evaluations/ for the complete Layer 0 report.
