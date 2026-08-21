---
name: OpenAI Assistants API
slug: openai
operator: OpenAI, L.L.C. · Deprecating August 2026
independence: unrecorded
parent_entity: null
category: LLM Agent API · Managed SaaS
homepage: null
github: null
evaluation_number: 19
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
    score: 17
    note: ''
  e:
    score: null
    note: null
  r:
    score: 15
    note: ''
  d:
    score: 13
    note: ''
  i:
    score: 4
    note: ''
  c:
    score: 5
    note: ''
  t:
    score: 7
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
next_review_due: '2026-06-23'
tags: []
rank: null
sources: []
og_description: "Independent security evaluation of OpenAI Assistants API. Score: 61/85. Zero CVEs but used as C2 channel (SesameOp). Deprecation August 2026. Framework v0.3.1."
category_line: LLM Agent API · Managed SaaS
display_tags: &id001
- text: ISO 42001:2023 · AI Management System
  color: amber
- text: SOC2 Type II · ISO27001 Family · CNA
  color: amber
- text: SesameOp · API C2 Abuse · Not Platform Vuln
  color: dim
- text: Deprecating August 2026 → Responses API
  color: warn
finding: "Broadest certification set among evaluated API platforms: SOC 2 Type II, ISO 27001 family, and ISO 42001:2023 (AI Management System). Explicit no-training policy confirmed across three independent sources. Code Interpreter runs in a &quot;fully sandboxed virtual machine.&quot; SesameOp (Nov 2025): threat actors abused the Assistants API as a C2 channel — API abuse, not a platform vulnerability. Assistants API deprecated August 2026."
meta_description: "Independent security evaluation of OpenAI Assistants API. Score: 61/85. Zero CVEs but used as C2 channel (SesameOp). Deprecation August 2026. Framework v0.3.1."
key_finding: 'Broadest certification set among evaluated API platforms: SOC 2 Type II, ISO 27001 family, and ISO 42001:2023 (AI Management System) — the only platform with a formally audited AI-specific management system standard. Explicit no-training policy confirmed across three independent sources. Code Interpreter runs in a "fully sandboxed virtual machine." SesameOp (Nov 2025): threat actors abused the Assistants API as a C2 channel — API abuse, not a platform vulnerability. Assistants API deprecated August 2026; Responses API is the successor.'
card_owner: OpenAI, L.L.C. · Deprecating August 2026
card_category: LLM Agent API · Managed SaaS
card_tags: *id001
---
# OpenAI Assistants API

Broadest certification set among evaluated API platforms: SOC 2 Type II, ISO 27001 family, and ISO 42001:2023 (AI Management System) — the only platform with a formally audited AI-specific management system standard. Explicit no-training policy confirmed across three independent sources. Code Interpreter runs in a "fully sandboxed virtual machine." SesameOp (Nov 2025): threat actors abused the Assistants API as a C2 channel — API abuse, not a platform vulnerability. Assistants API deprecated August 2026; Responses API is the successor.

## Layer 0 Score: 61/85 (Tier A)

**V** 17/20 · **R** 15/20 · **D** 13/15 · **I** 4/10 · **C** 5/10 · **T** 7/10

## CISA KEV

該当なし — no OpenAI Assistants API packages appear in the CISA Known Exploited Vulnerabilities catalog. Zero published CVEs attributed to OpenAI Assistants API in the trailing 12 months (captured).

## Bias Disclosure

This evaluation uses Claude (Anthropic) as its tooling. Anthropic operates in the AI agent market and may compete with some evaluated vendors. VERDICT discloses this relationship in every report and applies identical evaluation criteria to all platforms regardless of their relationship to Anthropic.

## Full Evaluation

See evaluations/ for the complete Layer 0 report.
