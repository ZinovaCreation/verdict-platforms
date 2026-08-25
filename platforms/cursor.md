---
name: Cursor
slug: cursor
operator: Anysphere · $29.3B
independence: independent
parent_entity: null
category: AI Coding IDE · Proprietary
homepage: https://trust.cursor.com
github: https://github.com/cursor
evaluation_number: 42
evaluation_type: initial
evaluated_at: '2026-04-03'
evaluator_model: unrecorded
framework_version: v0.3.1
layer: '0'
target_version: 2.6.21 (latest stable as of evaluation date)
previous_evaluation_date: null
previous_score: null
score: 47
max_score: 85
tier: B
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
    score: 8
    rating: Mid
    note: ''
  d:
    score: 11
    rating: High
    note: ''
  i:
    score: 7
    rating: High
    note: ''
  c:
    score: 5
    rating: Mid
    note: ''
  t:
    score: 6
    rating: Mid
    note: ''
cisa_kev:
  present: false
  entries: []
cve_count_12mo: 3
cve_count_basis: exact
max_cvss_12mo: 8.6
supply_chain_compromise_12mo: false
known_facts_applied: []
qa:
  factual: unresolved
  legal: unresolved
  quality: unresolved
  revision_cycles: 0
  flagged: false
differential: null
next_review_due: '2026-07-02'
tags:
- AI IDE
- proprietary
- VS Code fork
- SOC 2 Type II
- Privacy Mode
- MCP
- agent mode
- enterprise
- SSO
- SCIM
- RBAC
- desktop application
rank: 34
sources:
- https://cursor.com/changelog
- https://cursor.com/data-use
- https://cursor.com/docs
- https://cursor.com/enterprise
- https://cursor.com/privacy
- https://cursor.com/security
- https://trust.cursor.com/
og_description: 'Independent security evaluation of Cursor by Anysphere. Score: 47/85. SOC 2 Type II. 3 MCP CVEs (structural pattern). Privacy Mode zero-retention. $29.3B valuation. Framework v0.3.1.'
category_line: AI Coding IDE · Proprietary
display_tags: &id001
- text: SOC 2 Type II · Privacy Mode
  color: safe
- text: 3 MCP CVEs · CVSS 8.6
  color: red
- text: Workspace Trust Off
  color: amber
finding: 'Most widely adopted AI IDE ($29.3B, $1B+ ARR). SOC 2 Type II. Privacy Mode: zero-retention + no training. 3 MCP CVEs (CVSS 8.6 highest) — structural trust model pattern. 94+ inherited Chromium CVEs. Workspace Trust disabled by default.'
meta_owner: Anysphere
meta_description: 'Independent security evaluation of Cursor by Anysphere. Score: 47/85. SOC 2 Type II. 3 MCP CVEs (structural pattern). Privacy Mode zero-retention. $29.3B valuation. Framework v0.3.1.'
key_finding: SOC 2 Type II. Privacy Mode zero-retention. 3 MCP CVEs (structural). $29.3B, $1B+ ARR.
card_owner: Anysphere · $29.3B
card_category: AI Coding IDE · Proprietary
card_tags: *id001
---
# Cursor

SOC 2 Type II. Privacy Mode zero-retention. 3 MCP CVEs (structural). $29.3B, $1B+ ARR.

## Layer 0 Score: 47/85 (Tier B)

**V** 10/20 · **R** 8/20 · **D** 11/15 · **I** 7/10 · **C** 5/10 · **T** 6/10

## CISA KEV

該当なし — no Cursor packages appear in the CISA Known Exploited Vulnerabilities catalog. 3 published CVE(s) attributed to Cursor in the trailing 12 months (captured).

## Bias Disclosure

This evaluation uses Claude (Anthropic) as its tooling. Anthropic operates in the AI agent market and may compete with some evaluated vendors. VERDICT discloses this relationship in every report and applies identical evaluation criteria to all platforms regardless of their relationship to Anthropic.

## Full Evaluation

See evaluations/ for the complete Layer 0 report.
