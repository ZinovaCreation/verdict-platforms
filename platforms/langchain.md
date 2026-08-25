---
name: LangChain
slug: langchain
operator: Independent · Sequoia / IVP · $1.25B Unicorn (Oct 2025)
independence: unrecorded
parent_entity: null
category: LLM Agent Framework · Open Source (MIT core)
homepage: null
github: null
evaluation_number: 11
evaluation_type: initial
evaluated_at: '2026-03-25'
evaluator_model: unrecorded
framework_version: v0.3.1
layer: '0'
target_version: null
previous_evaluation_date: null
previous_score: null
score: 49
max_score: 85
tier: B
verdict:
  v:
    score: 15
    rating: High
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
    score: 7
    rating: Mid
    note: ''
  i:
    score: 6
    rating: Mid
    note: ''
  c:
    score: 6
    rating: Mid
    note: ''
  t:
    score: 7
    rating: High
    note: ''
cisa_kev:
  present: false
  entries: []
cve_count_12mo: 3
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
rank: 30
sources: []
og_description: 'Independent security evaluation of LangChain. Score: 49/85. LangGrinch CVE-2025-68664 (CVSS 9.3). SOC 2 Type II certified, $1.25B valuation. LiteLLM dependency exposure. Framework v0.3.1.'
category_line: LLM Agent Framework · Open Source (MIT core)
display_tags: &id001
- text: LangGrinch · CVE-2025-68664 · CVSS 9.3
  color: red
- text: Prompt Injection Attack Vector
  color: red
- text: SOC 2 Type II · 2 Products
  color: amber
- text: HIPAA · GDPR DPA Self-Service
  color: amber
finding: CVE-2025-68664 &quot;LangGrinch&quot; (CVSS 9.3) in langchain-core — serialization injection exploitable via prompt injection alone, affecting ~847M downloads. Patched in 20 days. SOC 2 Type II for both LangSmith and LangGraph Platform, HIPAA BAA, self-service GDPR DPA, explicit no-training policy.
meta_description: 'Independent security evaluation of LangChain. Score: 49/85. LangGrinch CVE-2025-68664 (CVSS 9.3). SOC 2 Type II certified, $1.25B valuation. LiteLLM dependency exposure. Framework v0.3.1.'
key_finding: 'CVE-2025-68664 "LangGrinch" (CVSS 9.3) in langchain-core — serialization injection exploitable via prompt injection alone, affecting ~847M downloads. Patched in 20 days. No CISA KEV. Strongest compliance posture in series: SOC 2 Type II for both LangSmith and LangGraph Platform, HIPAA BAA, self-service GDPR DPA, explicit no-training policy.'
card_owner: Independent · Sequoia / IVP · $1.25B Unicorn (Oct 2025)
card_category: LLM Agent Framework · Open Source (MIT core)
card_tags: *id001
---
# LangChain

CVE-2025-68664 "LangGrinch" (CVSS 9.3) in langchain-core — serialization injection exploitable via prompt injection alone, affecting ~847M downloads. Patched in 20 days. No CISA KEV. Strongest compliance posture in series: SOC 2 Type II for both LangSmith and LangGraph Platform, HIPAA BAA, self-service GDPR DPA, explicit no-training policy.

## Layer 0 Score: 49/85 (Tier B)

**V** 15/20 · **R** 8/20 · **D** 7/15 · **I** 6/10 · **C** 6/10 · **T** 7/10

## CISA KEV

該当なし — no LangChain packages appear in the CISA Known Exploited Vulnerabilities catalog. 3 published CVE(s) attributed to LangChain in the trailing 12 months (captured).

## Bias Disclosure

This evaluation uses Claude (Anthropic) as its tooling. Anthropic operates in the AI agent market and may compete with some evaluated vendors. VERDICT discloses this relationship in every report and applies identical evaluation criteria to all platforms regardless of their relationship to Anthropic.

## Full Evaluation

See evaluations/ for the complete Layer 0 report.
