---
name: AutoGPT
slug: autogpt
operator: Determinist Ltd · UK
independence: independent
parent_entity: null
category: Autonomous AI Agent · Source-Available
homepage: https://agpt.co
github: https://github.com/Significant-Gravitas
evaluation_number: 37
evaluation_type: initial
evaluated_at: '2026-03-31'
evaluator_model: unrecorded
framework_version: v0.3.1
layer: '0'
target_version: AutoGPT Platform beta v0.6.52 (github.com/Significant-Gravitas/AutoGPT)
previous_evaluation_date: null
previous_score: null
score: 36
max_score: 85
tier: C
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
    score: 4
    rating: null
    note: ''
  d:
    score: 5
    rating: null
    note: ''
  i:
    score: 3
    rating: null
    note: ''
  c:
    score: 4
    rating: null
    note: ''
  t:
    score: 10
    rating: null
    note: ''
cisa_kev:
  present: false
  entries: []
cve_count_12mo: null
cve_count_basis: unrecorded
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
- source-available
- Polyform-Shield
- MIT-partial
- UK-company
- autonomous-agent
- most-starred-github
- platform-beta
- Docker
rank: null
sources:
- https://agpt.co/
- https://github.com/Significant-Gravitas/AutoGPT
- https://github.com/Significant-Gravitas/AutoGPT/releases
- https://github.com/Significant-Gravitas/AutoGPT/security
og_description: 'Independent security evaluation of AutoGPT. Score: 36/85. T:10/10 (index highest). 6 security advisories including 2 Critical SSRF. Recurring SSRF pattern. Cross-user data leak. Framework v0.3.1.'
category_line: Autonomous AI Agent · Source-Available
display_tags: &id001
- text: 'T: 10/10 · Index Highest'
  color: safe
- text: 6 Advisories · 2 Critical
  color: red
- text: Cross-User Data Leak
  color: red
finding: 'Highest transparency score in the VERDICT index (T: 10/10). Six self-published security advisories with patches. Recurring SSRF pattern (3/6 advisories). Cross-user data leak via WebSockets (patched). 183k GitHub stars. $12M funded.'
meta_owner: Determinist Ltd (AutoGPT)
meta_description: 'Independent security evaluation of AutoGPT. Score: 36/85. T:10/10 (index highest). 6 security advisories including 2 Critical SSRF. Recurring SSRF pattern. Cross-user data leak. Framework v0.3.1.'
key_finding: T:10/10 (index highest). 6 advisories, 2 Critical SSRF. Recurring SSRF pattern. Cross-user data leak. 183k stars.
card_owner: Determinist Ltd · UK
card_category: Autonomous AI Agent · Source-Available
card_tags: *id001
---
# AutoGPT

T:10/10 (index highest). 6 advisories, 2 Critical SSRF. Recurring SSRF pattern. Cross-user data leak. 183k stars.

## Layer 0 Score: 36/85 (Tier C)

**V** 10/20 · **R** 4/20 · **D** 5/15 · **I** 3/10 · **C** 4/10 · **T** 10/10

## CISA KEV

該当なし — no AutoGPT packages appear in the CISA Known Exploited Vulnerabilities catalog. The original evaluation published its advisory count in GHSA units — '6 confirmed GHSAs' (preserved verbatim; no CVE-unit count published; basis: unrecorded).

## Bias Disclosure

This evaluation uses Claude (Anthropic) as its tooling. Anthropic operates in the AI agent market and may compete with some evaluated vendors. VERDICT discloses this relationship in every report and applies identical evaluation criteria to all platforms regardless of their relationship to Anthropic.

## Full Evaluation

See evaluations/ for the complete Layer 0 report.
