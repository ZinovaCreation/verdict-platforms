---
name: Microsoft Copilot Studio
slug: copilot-studio
operator: Microsoft Corporation
independence: unrecorded
parent_entity: null
category: No-Code Agent Builder · Enterprise SaaS
homepage: null
github: null
evaluation_number: 13
evaluation_type: initial
evaluated_at: '2026-03-25'
evaluator_model: unrecorded
framework_version: v0.3.1
layer: '0'
target_version: null
previous_evaluation_date: null
previous_score: null
score: 61
max_score: 85
tier: A
verdict:
  v:
    score: 16
    rating: High
    note: ''
  e:
    score: null
    rating: null
    note: null
  r:
    score: 11
    rating: Mid
    note: ''
  d:
    score: 10
    rating: Mid
    note: ''
  i:
    score: 7
    rating: High
    note: ''
  c:
    score: 8
    rating: High
    note: ''
  t:
    score: 9
    rating: High
    note: ''
cisa_kev:
  present: false
  entries: []
cve_count_12mo: 5
cve_count_basis: exact
max_cvss_12mo: 9.3
supply_chain_compromise_12mo: false
known_facts_applied: []
qa:
  factual: unresolved
  legal: unresolved
  quality: unresolved
  revision_cycles: 0
  flagged: false
differential: null
next_review_due: '2026-06-23'
tags: []
rank: 9
sources: []
og_description: 'Independent security evaluation of Microsoft Copilot Studio. Score: 61/85. EchoLeak CVE-2025-32711 (CVSS 9.3) — first zero-click prompt injection on a production AI system. Framework v0.3.1.'
category_line: No-Code Agent Builder · Enterprise SaaS
display_tags: &id001
- text: EchoLeak · CVE-2025-32711 · CVSS 9.3
  color: red
- text: Zero-Click Prompt Injection · First in Industry
  color: red
- text: SOC2 · ISO27001 · FedRAMP · HIPAA BAA
  color: amber
- text: Anthropic Sub-processor · Dec 2025
  color: amber
finding: 'Highest compliance posture in this index: SOC 2, ISO 27001, FedRAMP, and HIPAA BAA all explicitly confirmed — the only platform with all four. CVE-2025-32711 &quot;EchoLeak&quot; (CVSS 9.3): first documented zero-click prompt injection on a production AI system. All CVEs patched server-side by Microsoft with no customer action required. SSRF and spoofing classes have recurred across the evaluation window.'
meta_description: 'Independent security evaluation of Microsoft Copilot Studio. Score: 61/85. EchoLeak CVE-2025-32711 (CVSS 9.3) — first zero-click prompt injection on a production AI system. Framework v0.3.1.'
key_finding: 'Highest compliance posture in this index: SOC 2, ISO 27001, FedRAMP, and HIPAA BAA all explicitly confirmed — the only platform with all four. CVE-2025-32711 "EchoLeak" (CVSS 9.3): first documented zero-click prompt injection on a production AI system. All CVEs patched server-side by Microsoft with no customer action required. SSRF and spoofing classes have recurred across the evaluation window.'
card_owner: Microsoft Corporation
card_category: No-Code Agent Builder · Enterprise SaaS
card_tags: *id001
---
# Microsoft Copilot Studio

Highest compliance posture in this index: SOC 2, ISO 27001, FedRAMP, and HIPAA BAA all explicitly confirmed — the only platform with all four. CVE-2025-32711 "EchoLeak" (CVSS 9.3): first documented zero-click prompt injection on a production AI system. All CVEs patched server-side by Microsoft with no customer action required. SSRF and spoofing classes have recurred across the evaluation window.

## Layer 0 Score: 61/85 (Tier A)

**V** 16/20 · **R** 11/20 · **D** 10/15 · **I** 7/10 · **C** 8/10 · **T** 9/10

## CISA KEV

該当なし — no Microsoft Copilot Studio packages appear in the CISA Known Exploited Vulnerabilities catalog. 5 published CVE(s) attributed to Microsoft Copilot Studio in the trailing 12 months (captured).

## Bias Disclosure

This evaluation uses Claude (Anthropic) as its tooling. Anthropic operates in the AI agent market and may compete with some evaluated vendors. VERDICT discloses this relationship in every report and applies identical evaluation criteria to all platforms regardless of their relationship to Anthropic.

## Full Evaluation

See evaluations/ for the complete Layer 0 report.
