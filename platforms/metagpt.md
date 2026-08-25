---
name: MetaGPT
slug: metagpt
operator: DeepWisdom · Shenzhen, China
independence: independent
parent_entity: null
category: Multi-Agent Dev Framework · OSS (MIT)
homepage: null
github: https://github.com/FoundationAgents
evaluation_number: 33
evaluation_type: initial
evaluated_at: '2026-03-31'
evaluator_model: unrecorded
framework_version: v0.3.1
layer: '0'
target_version: v0.8.2 (PyPI) / v1.1 (GitHub main)
previous_evaluation_date: null
previous_score: null
score: 23
max_score: 85
tier: D
verdict:
  v:
    score: 11
    rating: Mid
    note: ''
  e:
    score: null
    rating: null
    note: null
  r:
    score: 4
    rating: Low
    note: ''
  d:
    score: 0
    rating: Low
    note: ''
  i:
    score: 2
    rating: Low
    note: ''
  c:
    score: 5
    rating: Mid
    note: ''
  t:
    score: 1
    rating: Low
    note: ''
cisa_kev:
  present: false
  entries: []
cve_count_12mo: 4
cve_count_basis: exact
max_cvss_12mo: 9.8
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
- multi-agent
- OSS
- MIT
- Python
- DeepWisdom
- code-generation
- ICLR
- academic
- Shenzhen
rank: 68
sources:
- https://github.com/FoundationAgents/MetaGPT
- https://github.com/FoundationAgents/MetaGPT/releases
og_description: 'Independent security evaluation of MetaGPT by DeepWisdom. Score: 23/85. Four CVEs including two CVSS 9.8 Critical RCEs unpatched. Vendor unresponsive to disclosures. 66k stars. Framework v0.3.1.'
category_line: Multi-Agent Dev Framework · OSS (MIT)
display_tags: &id001
- text: 2x CVSS 9.8 · Unpatched
  color: red
- text: Vendor Unresponsive
  color: red
- text: 'D: 0/15'
  color: red
- text: MIT · 66k Stars
  color: dim
finding: 66k GitHub stars and ICLR 2024 publication. Four CVEs in trailing 12 months including two CVSS 9.8 Critical RCEs (deserialization + code injection) — all unpatched. Vendor documented as unresponsive to multiple disclosure attempts. D dimension 0/15. No privacy policy, no certifications.
meta_owner: DeepWisdom
meta_description: 'Independent security evaluation of MetaGPT by DeepWisdom. Score: 23/85. Four CVEs including two CVSS 9.8 Critical RCEs unpatched. Vendor unresponsive to disclosures. 66k stars. Framework v0.3.1.'
key_finding: '66k stars, ICLR 2024. Two CVSS 9.8 RCEs unpatched. Vendor unresponsive. D: 0/15. Four CVEs in 12 months.'
card_owner: DeepWisdom · Shenzhen, China
card_category: Multi-Agent Dev Framework · OSS (MIT)
card_tags: *id001
---
# MetaGPT

66k stars, ICLR 2024. Two CVSS 9.8 RCEs unpatched. Vendor unresponsive. D: 0/15. Four CVEs in 12 months.

## Layer 0 Score: 23/85 (Tier D)

**V** 11/20 · **R** 4/20 · **D** 0/15 · **I** 2/10 · **C** 5/10 · **T** 1/10

## CISA KEV

該当なし — no MetaGPT packages appear in the CISA Known Exploited Vulnerabilities catalog. 4 published CVE(s) attributed to MetaGPT in the trailing 12 months (captured).

## Bias Disclosure

This evaluation uses Claude (Anthropic) as its tooling. Anthropic operates in the AI agent market and may compete with some evaluated vendors. VERDICT discloses this relationship in every report and applies identical evaluation criteria to all platforms regardless of their relationship to Anthropic.

## Full Evaluation

See evaluations/ for the complete Layer 0 report.
