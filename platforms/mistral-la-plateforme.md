---
name: Mistral La Plateforme
slug: mistral-la-plateforme
operator: Mistral AI SAS
independence: independent
parent_entity: null
category: AI Agent Platform
homepage: https://mistral.ai
github: https://github.com/mistralai
evaluation_number: 61
evaluation_type: initial
evaluated_at: '2026-04-29'
evaluator_model: unrecorded
framework_version: v0.3.1-final
layer: '0'
target_version: null
previous_evaluation_date: null
previous_score: null
score: 55
max_score: 85
tier: A
verdict:
  v:
    score: 14
    rating: High
    note: ''
  r:
    score: 17
    rating: High
    note: ''
  d:
    score: 11
    rating: High
    note: ''
  i:
    score: 4
    rating: Mid
    note: ''
  c:
    score: 2
    rating: Low
    note: ''
  t:
    score: 7
    rating: High
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
next_review_due: '2026-07-28'
tags:
- foundation-model-api
- agents-api
- eu-ai-provider
- gdpr-default-eu
- soc2-iso27001
- public-dpa
- zdr-on-request
- apache-2.0-base-models
- vertical-integration
sources:
- https://mistral.ai/
- https://docs.mistral.ai/
- https://trust.mistral.ai/
- https://legal.mistral.ai/terms/data-processing-addendum
- https://legal.mistral.ai/terms/privacy-policy
- https://legal.mistral.ai/ai-governance
- https://help.mistral.ai/en/collections/789666-trust-security-compliance
- https://status.mistral.ai/
- https://annuaire-entreprises.data.gouv.fr/entreprise/mistral-ai-952418325
rank: null
---
# Mistral La Plateforme

Mistral La Plateforme is the cloud API platform of Mistral AI SAS (Paris), a vertically integrated foundation model + agent platform operator. The platform exposes the Chat Completion API, Agents API (stateful conversation with code interpreter, web search, image generation, document library, MCP support), and Fine-Tuning API. Self-hosted, on-premises, and dedicated-environment deployment options exist at the enterprise tier.

## Layer 0 Score: 55/85 (Tier A)

**V** 14/20 · **R** 17/20 · **D** 11/15 · **I** 4/10 · **C** 2/10 · **T** 7/10

Strongest signals: publicly accessible DPA at legal.mistral.ai (no NDA gate) with SCC Module 4 + 10-day subprocessor objection right + EU data residency by default + paid API training opt-out by default + Zero Data Retention available on request + SOC 2 Type II + ISO 27001 / 27701 + zero CVEs across `mistralai/*` GitHub org and SDKs in trailing 12 months + EU GPAI Code of Practice signed + AI Compliance Hub mapping per-model and per-AI-system EU AI Act docs. Largest gaps: Code Interpreter sandbox isolation technology not disclosed in public materials beyond "isolated container" phrasing. SAML SSO Enterprise tier only. Agents API retention "until account termination" structurally longer than 30-day general API window. Subprocessor list last-updated date not directly observable in public-only fetched HTML.

## Bias Disclosure

This evaluation uses Claude (Anthropic) as its tooling. Anthropic operates in the AI agent market and may compete with some evaluated vendors. VERDICT discloses this relationship in every report and applies identical evaluation criteria to all platforms regardless of their relationship to Anthropic.
