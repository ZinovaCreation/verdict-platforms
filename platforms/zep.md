---
name: Zep
slug: zep
operator: Zep Software, Inc.
independence: independent
parent_entity: null
category: Agent Memory Layer
homepage: https://www.getzep.com
github: https://github.com/getzep/graphiti
evaluation_number: 67
evaluation_type: initial
evaluated_at: '2026-05-15'
evaluator_model: unrecorded
framework_version: v0.3.1-final
layer: '0'
target_version: graphiti-core 0.28.2 / Zep Cloud API v3
previous_evaluation_date: null
previous_score: null
score: 43
max_score: 85
tier: C
verdict:
  v:
    score: 11
    rating: Mid
    note: ''
  r:
    score: 14
    rating: High
    note: ''
  d:
    score: 0
    rating: Low
    note: ''
  i:
    score: 8
    rating: High
    note: ''
  c:
    score: 4
    rating: Mid
    note: ''
  t:
    score: 6
    rating: Mid
    note: ''
  e:
    score: null
    rating: null
    note: null
cisa_kev:
  present: false
  entries: []
cve_count_12mo: 1
cve_count_basis: exact
max_cvss_12mo: 8.1
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
- agent-memory
- temporal-knowledge-graph
- context-engineering
- soc2-type2
- hipaa
- open-source-core
- byok
- byom
- byoc
- yc-w24
- delaware-c-corp
rank: 46
sources:
- https://www.getzep.com/
- https://help.getzep.com
- https://github.com/getzep/graphiti
- https://www.getzep.com/enterprise
- https://status.getzep.com
finding: 'Zep scores 43/85 (Tier C) under VERDICT v0.3.1 Layer 0, evaluated at graphiti-core
  0.28.2 / Zep Cloud API v3 / ToS v1.1 (2025.08.07) / Privacy Policy v1.0 (2024.01.27).
  Resilience and identity-control lead: Graphiti, the temporal knowledge graph engine,
  is Apache 2.0 open source with named authors (Paul Paliychuk, Preston Rasmussen,
  Daniel Chalef) traceable to operator email, and the operator holds SOC 2 Type 2
  (Oneleet-attested) and a published HIPAA tier with BAA availability. CVE-2026-32247
  (CVSS 8.1, a Cypher injection in Graphiti exploitable in MCP deployments via LLM
  prompt injection) was disclosed and patched the same day (2026.03.11) in v0.28.2
  with a full GHSA advisory crediting the external reporter, and the upstream diskcache
  pickle-deserialization issue (CVE-2025-69872) was mitigated by removing the dependency
  entirely in v0.28.1, roughly eight days after upstream publication. A four-model
  deployment matrix — Managed, Bring Your Own Key (AWS KMS with CloudTrail), Bring
  Your Own Model, and Bring Your Own Cloud — lets customers hold encryption keys and
  route LLM credentials outside the operator''s control plane, with per-tenant dedicated
  database instances. Recorded concerns concentrate in public data conduct and transparency:
  the publicly accessible Privacy Policy (v1.0, 2024.01.27) is a generic website policy
  that does not address customer conversation content, GDPR, AI-training use, sub-processors,
  or retention windows, and the DPA and sub-processor list are gated behind the trust
  center contact flow, so under VERDICT''s silence-is-data principle Data Conduct
  scores 0/15 regardless of the contractual controls the SOC 2/HIPAA posture implies.
  ToS v1.1 §2.1(xi) adds a benchmarking restriction prohibiting public performance
  or comparative analysis without prior written consent, which sits in documented
  tension with the operator''s LoCoMo leadership claim — a claim resting on operator-authored
  evaluations that Mem0''s CTO has publicly disputed on methodology grounds (getzep/zep-papers
  issue #5, open at evaluation date), with independent academic papers reporting Zep
  LoCoMo scores across a 71–85.2% range. The legal entity name also differs between
  contractual documents (Zep Software, Inc.) and the website copyright (Zep AI, Inc.),
  and no AI-specific safety framework such as NIST AI RMF is referenced in public
  documentation.'
meta_owner: Zep Software, Inc. (contractual) / Zep AI, Inc. (brand) · Delaware C-corp
  · Y Combinator W24 · Founder/CEO Daniel Chalef · Independent, seed-stage (~$2.3M
  cumulative, per CB Insights)
meta_description: 'Zep (Agent Memory Layer) scores 43/85, Tier C, under VERDICT v0.3.1
  Layer 0. Strengths: an Apache 2.0 open-source core (Graphiti), SOC 2 Type 2 and
  a HIPAA tier with BAA, same-day patching of CVE-2026-32247 (CVSS 8.1) plus proactive
  removal of an upstream dependency CVE, and a BYOK/BYOM/BYOC deployment matrix. Concerns:
  a generic 2024 privacy policy with no public DPA or sub-processor list (Data Conduct
  0/15 under silence-is-data), a ToS benchmarking restriction, and a contested LoCoMo
  benchmark claim.'
og_description: 'Zep scores 43/85 (Tier C) on VERDICT v0.3.1 Layer 0: strong open-source
  security discipline (same-day CVE patch) and a BYOK/BYOM/BYOC deployment matrix,
  with concerns in thin public data-handling docs, a ToS benchmarking restriction,
  and a contested benchmark claim.'
category_line: Agent Memory Layer · Temporal Knowledge Graph · Context Engineering
  Platform · Apache 2.0 Open-Source Core (Graphiti) · Managed Cloud, BYOK / BYOM /
  BYOC
display_tags:
- text: Apache 2.0 open-source core (Graphiti)
  color: safe
- text: SOC 2 Type 2 + HIPAA tier
  color: safe
- text: Same-day CVE patch + GHSA credit
  color: safe
- text: BYOK / BYOM / BYOC deployment matrix
  color: safe
- text: Generic privacy policy, no public DPA
  color: amber
- text: ToS benchmarking restriction (§2.1(xi))
  color: amber
- text: Enterprise identity controls gated
  color: amber
- text: CVE-2026-32247 (Cypher injection), patched
  color: dim
---

# Zep

<!-- TODO(Zinova/VERDICT project): overview + Strongest signals / Largest gaps prose, and the six display-copy fields (finding/meta_owner/meta_description/og_description/category_line/display_tags) — author from evaluations/067_zep.md. -->

## Layer 0 Score: 43/85 (Tier C)

**V** 11/20 · **R** 14/20 · **D** 0/15 · **I** 8/10 · **C** 4/10 · **T** 6/10

## Bias Disclosure

This evaluation uses Claude (Anthropic) as its tooling. Anthropic operates in the AI agent market and may compete with some evaluated vendors. VERDICT discloses this relationship in every report and applies identical evaluation criteria to all platforms regardless of their relationship to Anthropic.

Anthropic-specific note: Anthropic models (Claude) are one of the LLM providers supported by Zep Cloud and Graphiti. No equity or commercial relationship between Anthropic and Zep AI is recorded in public investor or partnership disclosures. This evaluation applies the v0.3.1 rubric identically to all Memory Layer category candidates and does not adjust scoring on the basis of LLM-provider relationship.