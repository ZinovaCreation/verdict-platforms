---
name: AG2
slug: ag2
operator: AG2AI Inc. · Community Fork
independence: independent
parent_entity: null
category: Multi-Agent Framework · OSS (Apache 2.0)
homepage: https://docs.ag2.ai
github: https://github.com/ag2ai
evaluation_number: 27
evaluation_type: initial
evaluated_at: '2026-03-31'
evaluator_model: unrecorded
framework_version: v0.3.1
layer: '0'
target_version: AG2 (ag2 PyPI package, latest stable + Beta; github.com/ag2ai/ag2)
previous_evaluation_date: null
previous_score: null
score: 40
max_score: 85
tier: C
verdict:
  v:
    score: 12
    rating: Mid
    note: ''
  e:
    score: null
    rating: null
    note: null
  r:
    score: 14
    rating: High
    note: ''
  d:
    score: 5
    rating: Low
    note: ''
  i:
    score: 3
    rating: Low
    note: ''
  c:
    score: 4
    rating: Mid
    note: ''
  t:
    score: 2
    rating: Low
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
next_review_due: '2026-06-29'
tags:
- open-source
- apache-2.0
- autoGen-fork
- community-governance
- python
- multi-agent
- volunteer-maintained
rank: 52
sources:
- https://docs.ag2.ai/
- https://github.com/ag2ai
- https://github.com/ag2ai/ag2
- https://github.com/ag2ai/ag2/releases
- https://github.com/ag2ai/build-with-ag2
- https://github.com/ag2ai/faststream/security
og_description: 'Independent security evaluation of AG2 (AutoGen fork). Score: 40/85. Zero AG2-specific CVEs. No MSRC coverage. PyPI namespace governance concern. Community-maintained. Framework v0.3.1.'
category_line: Multi-Agent Framework · OSS (Apache 2.0)
display_tags: &id001
- text: AutoGen Fork · Apache 2.0
  color: dim
- text: No MSRC Coverage
  color: amber
- text: PyPI Namespace Issue
  color: amber
finding: Community fork of Microsoft AutoGen. Zero AG2-specific CVEs. Inherits Docker code execution from AutoGen. No MSRC coverage (16-point gap vs AutoGen 56/85). Controls autogen/pyautogen PyPI namespaces — unique supply chain governance concern. No SECURITY.md.
meta_owner: AG2AI Inc. (community)
meta_description: 'Independent security evaluation of AG2 (AutoGen fork). Score: 40/85. Zero AG2-specific CVEs. No MSRC coverage. PyPI namespace governance concern. Community-maintained. Framework v0.3.1.'
key_finding: AutoGen fork. Zero AG2-specific CVEs. No MSRC. Controls autogen PyPI namespace.
card_owner: AG2AI Inc. · Community Fork
card_category: Multi-Agent Framework · OSS (Apache 2.0)
card_tags: *id001
---
# AG2

AutoGen fork. Zero AG2-specific CVEs. No MSRC. Controls autogen PyPI namespace.

## Layer 0 Score: 40/85 (Tier C)

**V** 12/20 · **R** 14/20 · **D** 5/15 · **I** 3/10 · **C** 4/10 · **T** 2/10

## CISA KEV

該当なし — no AG2 packages appear in the CISA Known Exploited Vulnerabilities catalog. Zero published CVEs attributed to AG2 in the trailing 12 months (captured).

## Bias Disclosure

This evaluation uses Claude (Anthropic) as its tooling. Anthropic operates in the AI agent market and may compete with some evaluated vendors. VERDICT discloses this relationship in every report and applies identical evaluation criteria to all platforms regardless of their relationship to Anthropic.

## Full Evaluation

See evaluations/ for the complete Layer 0 report.
