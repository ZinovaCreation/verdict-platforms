---
name: Relevance AI
slug: relevance-ai
operator: Relevance AI Pty Ltd · Sydney, Australia
independence: independent
parent_entity: null
category: AI Agent Platform · Cloud SaaS
homepage: https://relevanceai.com
github: null
evaluation_number: 23
evaluation_type: initial
evaluated_at: '2026-03-30'
evaluator_model: unrecorded
framework_version: v0.3.1
layer: '0'
target_version: Relevance AI SaaS (current production, March 2026)
previous_evaluation_date: null
previous_score: null
score: 43
max_score: 85
tier: C
verdict:
  v:
    score: 7
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
    score: 9
    rating: null
    note: ''
  i:
    score: 5
    rating: null
    note: ''
  c:
    score: 4
    rating: null
    note: ''
  t:
    score: 4
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
next_review_due: '2026-06-28'
tags:
- closed-source
- SaaS
- GTM-focused
- no-code
- SOC2-type2
- multi-region
- Australian-company
- series-B
rank: null
sources:
- https://marketplace.relevanceai.com/
- https://relevanceai.com/
- https://relevanceai.com/data-security-policy
- https://relevanceai.com/privacy-policy
og_description: 'Independent security evaluation of Relevance AI. Score: 43/85. SOC 2 Type II, multi-region (US/AU/EU). No public CVEs. Closed-source GTM agent platform. Framework v0.3.1.'
category_line: AI Agent Platform · Cloud SaaS
display_tags: &id001
- text: SOC 2 Type II
  color: dim
- text: Multi-Region · US/AU/EU
  color: dim
- text: No Public Vuln Disclosure
  color: amber
finding: SOC 2 Type II compliant with explicit data non-training policy. Multi-region data residency (US, AU, EU/UK). Zero CVEs in any public database. Score moderated by closed-source architecture, no public vulnerability disclosure program, and Enterprise-only access to SSO/RBAC and data retention controls.
meta_owner: Relevance AI Pty Ltd
meta_description: 'Independent security evaluation of Relevance AI. Score: 43/85. SOC 2 Type II, multi-region (US/AU/EU). No public CVEs. Closed-source GTM agent platform. Framework v0.3.1.'
key_finding: SOC 2 Type II. Customer data not used for training. Multi-region (US/AU/EU). Zero public CVEs. Closed-source with no public vulnerability disclosure program. SSO/RBAC Enterprise only.
card_owner: Relevance AI Pty Ltd · Sydney, Australia
card_category: AI Agent Platform · Cloud SaaS
card_tags: *id001
---
# Relevance AI

SOC 2 Type II. Customer data not used for training. Multi-region (US/AU/EU). Zero public CVEs. Closed-source with no public vulnerability disclosure program. SSO/RBAC Enterprise only.

## Layer 0 Score: 43/85 (Tier C)

**V** 7/20 · **R** 14/20 · **D** 9/15 · **I** 5/10 · **C** 4/10 · **T** 4/10

## CISA KEV

該当なし — no Relevance AI packages appear in the CISA Known Exploited Vulnerabilities catalog. Zero published CVEs attributed to Relevance AI in the trailing 12 months (captured).

## Bias Disclosure

This evaluation uses Claude (Anthropic) as its tooling. Anthropic operates in the AI agent market and may compete with some evaluated vendors. VERDICT discloses this relationship in every report and applies identical evaluation criteria to all platforms regardless of their relationship to Anthropic.

## Full Evaluation

See evaluations/ for the complete Layer 0 report.
