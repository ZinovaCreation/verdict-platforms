---
name: NeMo Guardrails
slug: nemo-guardrails
operator: NVIDIA Corporation
independence: parent
parent_entity: null
category: AI Safety
homepage: https://developer.nvidia.com/nemo-guardrails
github: https://github.com/NVIDIA-NeMo/Guardrails
evaluation_number: 66
evaluation_type: initial
evaluated_at: '2026-05-15'
evaluator_model: unrecorded
framework_version: v0.3.1-final
layer: '0'
target_version: nemoguardrails v0.20.x
previous_evaluation_date: null
previous_score: null
score: 52
max_score: 85
tier: B
verdict:
  v:
    score: 18
    rating: High
    note: ''
  r:
    score: 17
    rating: High
    note: ''
  d:
    score: 5
    rating: Low
    note: ''
  i:
    score: 4
    rating: Mid
    note: ''
  c:
    score: 3
    rating: Low
    note: ''
  t:
    score: 5
    rating: Mid
    note: ''
  e:
    score: null
    rating: null
    note: null
cisa_kev:
  present: false
  entries: []
cve_count_12mo: 0
max_cvss_12mo: null
supply_chain_compromise_12mo: false
known_facts_applied: []
qa:
  factual: pass
  legal: pass
  quality: pass
  revision_cycles: 0
  flagged: false
differential: null
next_review_due: '2026-08-13'
tags:
- nvidia
- ai-safety
- llm-guardrails
- open-source-toolkit
- apache-2.0
- programmable-rails
- colang
- nim
- evaluator-coi
- direct-investment
- commercial-channel
sources:
- https://github.com/NVIDIA-NeMo/Guardrails
- https://docs.nvidia.com/nemo/guardrails/
- https://developer.nvidia.com/nemo-guardrails
- https://www.nvidia.com/en-us/security/
- https://www.sec.gov/
rank: null
---

# NeMo Guardrails

<!-- TODO(VERDICT project): overview + Strongest signals / Largest gaps prose, and the six display-copy fields (finding/meta_owner/meta_description/og_description/category_line/display_tags) — author from evaluations/066_nemo_guardrails.md. -->

## Layer 0 Score: 52/85 (Tier B)

**V** 18/20 · **R** 17/20 · **D** 5/15 · **I** 4/10 · **C** 3/10 · **T** 5/10

## Bias Disclosure

This evaluation uses Claude (Anthropic) as its tooling. Anthropic operates in the AI agent market and may compete with some evaluated vendors. VERDICT discloses this relationship in every report and applies identical evaluation criteria to all platforms regardless of their relationship to Anthropic.

VERDICT additionally discloses that the operator of this platform (NVIDIA Corporation) has a direct-investment and commercial-channel relationship with VERDICT's evaluation tooling provider (Anthropic): NVIDIA has committed up to USD 10B in equity investment into Anthropic, and Anthropic has committed up to USD 30B in Azure compute capacity routed via NVIDIA, as disclosed in NVIDIA's SEC Form 10-Q for FY2026 Q3 (2025-11-18). This corresponds to VERDICT Trigger 2 (shared/direct investment) and Trigger 3 (commercial channel). Source: https://www.sec.gov/ (NVIDIA Form 10-Q FY2026 Q3). Identical evaluation criteria were applied regardless of this relationship.
