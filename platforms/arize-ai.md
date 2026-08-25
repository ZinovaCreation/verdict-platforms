---
name: Arize AI
slug: arize-ai
operator: Arize AI, Inc.
independence: independent
parent_entity: null
category: LLM Observability
homepage: https://arize.com
github: https://github.com/Arize-ai/phoenix
evaluation_number: 68
evaluation_type: initial
evaluated_at: '2026-05-15'
evaluator_model: unrecorded
framework_version: v0.3.1-final
layer: '0'
target_version: Arize AX / arize-phoenix v14.16.0
previous_evaluation_date: null
previous_score: null
score: 51
max_score: 85
tier: B
verdict:
  v:
    score: 13
    rating: Mid
    note: ''
  r:
    score: 17
    rating: High
    note: ''
  d:
    score: 3
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
cve_count_12mo: 0
cve_count_basis: exact
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
- llm-observability
- ai-evaluation
- ml-monitoring
- opentelemetry
- openinference
- elv2
- evaluator-coi
- shared-investor
- commercial-channel
rank: 28
sources:
- https://arize.com/
- https://docs.arize.com
- https://github.com/Arize-ai/phoenix
- https://arize.com/trust-center/
- https://www.sec.gov/
finding: 'Arize AI scores 51/85 (Tier B) at Layer 0 under VERDICT v0.3.1. Its strongest
  dimensions are Resilience (17/20) and Identity & Control (8/10): public sources
  show no CVEs in the trailing twelve months, arize-phoenix releases are published
  via PyPI Trusted Publishing with verified attestations and GPG-signed GitHub Releases,
  and the platform documents SAML SSO, RBAC with custom roles, three-tier audit logging
  via GraphQL, and human-in-the-loop evaluation by design. Compliance posture is well-documented
  (SOC 2 Type II, ISO/IEC 27001, HIPAA, PCI DSS 4.0, GDPR). The lowest dimension is
  Data Conduct (3/15): the Terms of Service grant Arize a broad license to use Customer
  Data to "enhance and improve" the Application and assign ownership of aggregated
  data to Arize, with no explicit statement that customer trace data is excluded from
  training Arize''s evaluator models, and at evaluation date no publicly dated subprocessor
  list, public DPA, or AX-platform retention schedule was located. Arize positions
  its Phoenix tier as open source, but it is licensed under the Elastic License 2.0
  — a source-available license carrying a hosted-competing-service restriction rather
  than OSI-approved open source.'
meta_owner: Arize AI, Inc. · Delaware C-corp · Berkeley, California
meta_description: 'Independent VERDICT v0.3.1 evaluation of Arize AI (Arize AX + Arize
  Phoenix), an LLM observability platform. Score: 51/85 (Tier B). Strong supply-chain
  resilience and access controls; the principal gap is Data Conduct disclosure, and
  the Phoenix tier is source-available under the Elastic License 2.0 rather than OSI-approved
  open source.'
og_description: VERDICT scores Arize AI 51/85 (Tier B) on its 85-point AI agent trust
  framework — strong supply-chain resilience and access controls, with the principal
  gap in published data-governance commitments.
category_line: LLM Observability · AI Evaluation · Model Monitoring (Cloud + OSS dual-tier)
display_tags:
- text: Zero CVEs (trailing 12 mo)
  color: safe
- text: Signed releases (Trusted Publishing + GPG)
  color: safe
- text: RBAC + three-tier audit logging
  color: safe
- text: Phoenix is ELv2, not OSI open source
  color: amber
- text: Data governance gated
  color: amber
- text: No explicit no-training commitment
  color: amber
---

# Arize AI

<!-- TODO(VERDICT project): overview + Strongest/Largest prose, and the six display-copy fields - author from evaluations/068_arize_ai.md. -->

## Layer 0 Score: 51/85 (Tier B)

**V** 13/20 · **R** 17/20 · **D** 3/15 · **I** 8/10 · **C** 4/10 · **T** 6/10

## Bias Disclosure

This evaluation uses Claude (Anthropic) as its tooling. Anthropic operates in the AI agent market and may compete with some evaluated vendors. VERDICT discloses this relationship in every report and applies identical evaluation criteria to all platforms regardless of their relationship to Anthropic.

VERDICT additionally discloses that the operator of this platform (Arize AI, Inc.) has a shared-investor and commercial-channel relationship with VERDICT's evaluation tooling provider (Anthropic): Microsoft, via its corporate venture fund M12, holds equity in Arize AI (Series C, announced 2025-02-20) and separately holds a strategic equity commitment in Anthropic (up to USD 5B, subject to closing conditions per the November 2025 Microsoft / NVIDIA / Anthropic joint announcement) — a compound investor structure in which Microsoft holds equity in both the evaluator and the evaluated platform. This corresponds to VERDICT Trigger 2 (shared investor). Additively, Arize AI has a commercial channel relationship with Microsoft via Azure AI Foundry integration (Trigger 3). Source: Microsoft / NVIDIA / Anthropic joint announcement (November 2025). Identical evaluation criteria were applied regardless of this relationship.