---
name: LangGraph
slug: langgraph
operator: LangChain Inc.
independence: independent
parent_entity: null
category: Agent Orchestration · OSS (MIT)
homepage: https://trust.langchain.com
github: https://github.com/langchain-ai
evaluation_number: 46
evaluation_type: initial
evaluated_at: '2026-04-04'
evaluator_model: unrecorded
framework_version: v0.3.1
layer: '0'
target_version: LangGraph (github.com/langchain-ai/langgraph, latest; LangGraph Platform cloud)
previous_evaluation_date: null
previous_score: null
score: 46
max_score: 85
tier: B
verdict:
  v:
    score: 13
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
    score: 7
    rating: null
    note: ''
  i:
    score: 8
    rating: null
    note: ''
  c:
    score: 5
    rating: null
    note: ''
  t:
    score: 9
    rating: null
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
next_review_due: '2026-07-03'
tags:
- open-source
- MIT
- agent-orchestration
- graph-based
- HITL-first-class
- LangChain-ecosystem
- SOC2-Type-II
- high-adoption
rank: null
sources:
- https://github.com/langchain-ai/langgraph
- https://github.com/langchain-ai/langgraph/releases
- https://trust.langchain.com/
og_description: 'Independent security evaluation of LangGraph by LangChain. Score: 46/85. I:8/10 best HITL. T:9/10. CVSS 9.3 Critical. 3 CVEs (structural data validation pattern). SOC 2 Type II. Framework v0.3.1.'
category_line: Agent Orchestration · OSS (MIT)
display_tags: &id001
- text: 'I: 8/10 · Best HITL'
  color: safe
- text: 'T: 9/10 · SOC 2 II'
  color: safe
- text: CVSS 9.3 · 3 CVEs
  color: red
finding: 'Best HITL in index (I:8/10): interrupt/breakpoint/persistence/time-travel. T:9/10 with exemplary CVE disclosure. 3 CVEs including CVSS 9.3 Critical deserialization. Structural data validation pattern across serialization/storage/loading. SOC 2 Type II.'
meta_owner: LangChain Inc.
meta_description: 'Independent security evaluation of LangGraph by LangChain. Score: 46/85. I:8/10 best HITL. T:9/10. CVSS 9.3 Critical. 3 CVEs (structural data validation pattern). SOC 2 Type II. Framework v0.3.1.'
key_finding: Best HITL (I:8/10). T:9/10. CVSS 9.3 Critical. 3 CVEs structural pattern. SOC 2 Type II. 9M+ weekly downloads.
card_owner: LangChain Inc.
card_category: Agent Orchestration · OSS (MIT)
card_tags: *id001
---
# LangGraph

Best HITL (I:8/10). T:9/10. CVSS 9.3 Critical. 3 CVEs structural pattern. SOC 2 Type II. 9M+ weekly downloads.

## Layer 0 Score: 46/85 (Tier B)

**V** 13/20 · **R** 4/20 · **D** 7/15 · **I** 8/10 · **C** 5/10 · **T** 9/10

## CISA KEV

該当なし — no LangGraph packages appear in the CISA Known Exploited Vulnerabilities catalog. 3 published CVE(s) attributed to LangGraph in the trailing 12 months (captured).

## Bias Disclosure

This evaluation uses Claude (Anthropic) as its tooling. Anthropic operates in the AI agent market and may compete with some evaluated vendors. VERDICT discloses this relationship in every report and applies identical evaluation criteria to all platforms regardless of their relationship to Anthropic.

## Full Evaluation

See evaluations/ for the complete Layer 0 report.
