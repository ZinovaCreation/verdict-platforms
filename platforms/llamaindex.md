---
name: LlamaIndex
slug: llamaindex
operator: Independent · Norwest / Greylock · Series A Mar 2025
independence: unrecorded
parent_entity: null
category: RAG / Data Framework · Open Source (MIT core)
homepage: null
github: null
evaluation_number: 14
evaluation_type: initial
evaluated_at: '2026-03-25'
evaluator_model: unrecorded
framework_version: v0.3.1
layer: '0'
target_version: null
previous_evaluation_date: null
previous_score: null
score: 41
max_score: 85
tier: C
verdict:
  v:
    score: 15
    note: ''
  e:
    score: null
    note: null
  r:
    score: 7
    note: ''
  d:
    score: 5
    note: ''
  i:
    score: 4
    note: ''
  c:
    score: 5
    note: ''
  t:
    score: 5
    note: ''
cisa_kev:
  present: false
  entries: []
cve_count_12mo: 3
cve_count_basis: range
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
next_review_due: '2026-06-23'
tags: []
rank: null
sources: []
og_description: 'Independent security evaluation of LlamaIndex. Score: 41/85. RAG and agent framework. Limited public security documentation. Norwest Venture Partners backed. Framework v0.3.1.'
category_line: RAG / Data Framework · Open Source (MIT core)
display_tags: &id001
- text: CVE-2025-1793 · CVSS 9.8 · 8 Integrations
  color: red
- text: Structural SQLi Pattern · LLM as Attack Vector
  color: red
- text: SOC2 Type II · HIPAA · LlamaCloud
  color: amber
finding: 'CVE-2025-1793 (CVSS 9.8): SQL injection across 8 vector store integrations via LLM-generated queries. Structural SQLi pattern confirmed. LlamaCloud: SOC 2 Type 2 and HIPAA confirmed. PandasQueryEngine WARNING: &quot;arbitrary code execution is possible.&quot;'
meta_description: 'Independent security evaluation of LlamaIndex. Score: 41/85. RAG and agent framework. Limited public security documentation. Norwest Venture Partners backed. Framework v0.3.1.'
key_finding: 'CVE-2025-1793 (CVSS 9.8): SQL injection across 8 vector store integrations via LLM-generated queries — the LLM itself becomes the injection attack vector. Structural pattern confirmed: Text-to-SQL SQLi (pre-window) and vector store SQLi (in-window) share the same root cause across independent components. LlamaCloud: SOC 2 Type 2 and HIPAA confirmed. PandasQueryEngine WARNING persists: "arbitrary code execution is possible."'
card_owner: Independent · Norwest / Greylock · Series A Mar 2025
card_category: RAG / Data Framework · Open Source (MIT core)
card_tags: *id001
---
# LlamaIndex

CVE-2025-1793 (CVSS 9.8): SQL injection across 8 vector store integrations via LLM-generated queries — the LLM itself becomes the injection attack vector. Structural pattern confirmed: Text-to-SQL SQLi (pre-window) and vector store SQLi (in-window) share the same root cause across independent components. LlamaCloud: SOC 2 Type 2 and HIPAA confirmed. PandasQueryEngine WARNING persists: "arbitrary code execution is possible."

## Layer 0 Score: 41/85 (Tier C)

**V** 15/20 · **R** 7/20 · **D** 5/15 · **I** 4/10 · **C** 5/10 · **T** 5/10

## CISA KEV

該当なし — no LlamaIndex packages appear in the CISA Known Exploited Vulnerabilities catalog. At least 3 published CVEs in the trailing 12 months (published as a bound; basis: range).

## Bias Disclosure

This evaluation uses Claude (Anthropic) as its tooling. Anthropic operates in the AI agent market and may compete with some evaluated vendors. VERDICT discloses this relationship in every report and applies identical evaluation criteria to all platforms regardless of their relationship to Anthropic.

## Full Evaluation

See evaluations/ for the complete Layer 0 report.
