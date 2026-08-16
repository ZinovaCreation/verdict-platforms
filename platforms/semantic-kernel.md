---
name: Semantic Kernel
slug: semantic-kernel
operator: Microsoft Research · Migrating to Agent Framework
independence: unrecorded
parent_entity: null
category: AI Orchestration SDK · Open Source (MIT)
homepage: null
github: null
evaluation_number: 15
evaluation_type: initial
evaluated_at: '2026-03-26'
evaluator_model: unrecorded
framework_version: v0.3.1
layer: '0'
target_version: Python SDK 1.39.4 / .NET Core 1.74.0
previous_evaluation_date: null
previous_score: null
score: 46
max_score: 85
tier: B
verdict:
  v:
    score: 14
    note: ''
  e:
    score: null
    note: null
  r:
    score: 11
    note: ''
  d:
    score: 5
    note: ''
  i:
    score: 4
    note: ''
  c:
    score: 4
    note: ''
  t:
    score: 8
    note: ''
cisa_kev:
  present: false
  entries: []
cve_count_12mo: 2
cve_count_basis: exact
max_cvss_12mo: 10.0
supply_chain_compromise_12mo: false
known_facts_applied: []
qa:
  factual: unresolved
  legal: unresolved
  quality: unresolved
  revision_cycles: 0
  flagged: false
differential: null
next_review_due: '2026-06-24'
tags: []
rank: null
sources: []
og_description: 'Independent security evaluation of Microsoft Semantic Kernel. Score: 46/85. No documented sandbox — plugins execute in-process. Microsoft Research project with MSRC coverage. Framework v0.3.1.'
category_line: AI Orchestration SDK · Open Source (MIT)
display_tags: &id001
- text: CVE-2026-25592 · CVSS 10.0 · Arbitrary File Write
  color: red
- text: CVE-2026-26030 · CVSS 10.0 · RCE · InMemoryVectorStore
  color: red
- text: No Built-In Sandbox · Plugin Execution In-Process
  color: dim
- text: Migrating to Microsoft Agent Framework
  color: warn
finding: 'Two CVSS 10.0 vulnerabilities in February 2026. CVE-2026-25592: arbitrary file write via SessionsPythonPlugin. CVE-2026-26030: RCE via InMemoryVectorStore. Both patched concurrently with disclosure. No built-in execution sandbox. Migrating to Agent Framework.'
meta_description: 'Independent security evaluation of Microsoft Semantic Kernel. Score: 46/85. No documented sandbox — plugins execute in-process. Microsoft Research project with MSRC coverage. Framework v0.3.1.'
key_finding: 'Two CVSS 10.0 vulnerabilities published within 13 days in February 2026, both in the plugin/code execution layer, both found by the same three researchers. CVE-2026-25592: arbitrary file write via SessionsPythonPlugin (CWE-22). CVE-2026-26030: RCE via InMemoryVectorStore filter expression parser (CWE-94). Both patched concurrently with disclosure. No built-in execution sandbox — plugins run in-process. Microsoft announced migration to Agent Framework (RC March 2026).'
card_owner: Microsoft Research · Migrating to Agent Framework
card_category: AI Orchestration SDK · Open Source (MIT)
card_tags: *id001
---
# Semantic Kernel

Two CVSS 10.0 vulnerabilities published within 13 days in February 2026, both in the plugin/code execution layer, both found by the same three researchers. CVE-2026-25592: arbitrary file write via SessionsPythonPlugin (CWE-22). CVE-2026-26030: RCE via InMemoryVectorStore filter expression parser (CWE-94). Both patched concurrently with disclosure. No built-in execution sandbox — plugins run in-process. Microsoft announced migration to Agent Framework (RC March 2026).

## Layer 0 Score: 46/85 (Tier B)

**V** 14/20 · **R** 11/20 · **D** 5/15 · **I** 4/10 · **C** 4/10 · **T** 8/10

## CISA KEV

該当なし — no Semantic Kernel packages appear in the CISA Known Exploited Vulnerabilities catalog. 2 published CVE(s) attributed to Semantic Kernel in the trailing 12 months (captured).

## Bias Disclosure

This evaluation uses Claude (Anthropic) as its tooling. Anthropic operates in the AI agent market and may compete with some evaluated vendors. VERDICT discloses this relationship in every report and applies identical evaluation criteria to all platforms regardless of their relationship to Anthropic.

## Full Evaluation

See evaluations/ for the complete Layer 0 report.
