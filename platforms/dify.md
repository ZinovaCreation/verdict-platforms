---
name: Dify
slug: dify
operator: Independent · $30M Series Pre-A (2026)
independence: unrecorded
parent_entity: null
category: LLM Application Builder · Open Source
homepage: null
github: null
evaluation_number: 4
evaluation_type: initial
evaluated_at: '2026-03-13'
updated_at: 2026-05-13
evaluator_model: unrecorded
framework_version: v0.3.1
layer: '0'
target_version: null
previous_evaluation_date: null
previous_score: null
score: 46
max_score: 85
tier: B
verdict:
  v:
    score: 16
    note: ''
  e:
    score: null
    note: null
  r:
    score: 6
    note: ''
  d:
    score: 10
    note: ''
  i:
    score: 4
    note: ''
  c:
    score: 3
    note: ''
  t:
    score: 7
    note: ''
cisa_kev:
  present: false
  entries: []
cve_count_12mo: 3
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
next_review_due: 2026-08-11
tags: []
rank: null
sources: []
og_description: 'Independent security evaluation of Dify. Score: 46/85. React2Shell CVE-2025-55182 caused cryptominer infections. Strong transparency with 4 certifications. Structural SSRF issue persists. Framework v0.3.1.'
category_line: LLM Application Builder · Open Source
display_tags: &id001
- text: React2Shell · Cryptominer Infections
  color: red
- text: SSRF Structural Issue · Ongoing
  color: red
- text: Chinese VC Investors (P Dimension)
  color: warn
finding: Strong transparency and 4 certifications. But React2Shell (CVE-2025-55182) resulted in confirmed cryptominer infections on user servers. SSRF proxy structural problem persists across versions.
meta_description: 'Independent security evaluation of Dify. Score: 46/85. React2Shell CVE-2025-55182 caused cryptominer infections. Strong transparency with 4 certifications. Structural SSRF issue persists. Framework v0.3.1.'
key_finding: Strong transparency and 4 certifications. But React2Shell (CVE-2025-55182) resulted in confirmed cryptominer infections on user servers — a real supply chain breach. SSRF proxy structural problem persists across versions, mirroring n8n's pattern.
card_owner: Independent · $30M Series Pre-A (2026)
card_category: LLM Application Builder · Open Source
card_tags: *id001
---
# Dify

Strong transparency and 4 certifications. But React2Shell (CVE-2025-55182) resulted in confirmed cryptominer infections on user servers — a real supply chain breach. SSRF proxy structural problem persists across versions, mirroring n8n's pattern.

## Layer 0 Score: 46/85 (Tier B)

**V** 16/20 · **R** 6/20 · **D** 10/15 · **I** 4/10 · **C** 3/10 · **T** 7/10

## CISA KEV

該当なし — no Dify packages appear in the CISA Known Exploited Vulnerabilities catalog. 3 published CVE(s) attributed to Dify in the trailing 12 months (captured).

## Bias Disclosure

This evaluation uses Claude (Anthropic) as its tooling. Anthropic operates in the AI agent market and may compete with some evaluated vendors. VERDICT discloses this relationship in every report and applies identical evaluation criteria to all platforms regardless of their relationship to Anthropic.

## Full Evaluation

See evaluations/ for the complete Layer 0 report.
