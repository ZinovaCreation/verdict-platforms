---
slug: mistral-la-plateforme
title: Mistral La Plateforme
score: 55
tier: A
tier_engine: B
tier_override_rationale: |
  ENGINE.md `## Tier Letter Assignment` thresholds (codified 2026-04-29, commit bd8cf2b)
  per Operations Override Rules in QA.md.
  Score 55 ∈ A band [55-64], at the lower boundary. Engine output Tier=B was informational;
  Operations applied threshold-derived Tier=A as the canonical assignment.
  Precedent in current evaluation cycle: AWS Bedrock Agents (55 = A in existing index).

  Note (2026-05-12): Reference framework wording updated retroactively to align with the
  ENGINE.md / QA.md codification of Operations Override Rules (commit bd8cf2b, 2026-04-29).
  Tier=A assignment and underlying rationale (threshold-based application) remain unchanged
  from original 2026-04-29 evaluation.
category: AI Agent Platform
subcategory: Foundation Model API · Stateful Agents Runtime · Cloud Service
license: Closed-source platform; selected base models (Mistral 7B, Mixtral, Codestral, Devstral, Mistral Small 4) under Apache 2.0
operator: Mistral AI SAS
operator_jurisdiction: Paris, France (RCS 952 418 325, 15 rue des Halles 75001 Paris)
founders: Arthur Mensch (CEO, ex-DeepMind), Timothée Lacroix (CTO, ex-Meta), Guillaume Lample (ex-Meta)
funding: ~$2.7B-$3.05B across 8-9 rounds; latest $830M debt round (Mar 2026, Credit Agricole CIB / HSBC / MUFG)
major_investors: Lightspeed, a16z, Microsoft, Nvidia, Salesforce, IBM, Samsung, Bpifrance, ASML (~11% largest, Series C Sep 2025), Bertelsmann, DST Global
evaluation_date: 2026-04-29
evaluation_number: 061
framework_version: VERDICT v0.3.1
layer: 0
independence: ✅ Independent (no Anthropic equity overlap; Anthropic listed as competitor by PitchBook)
anthropic_relationship: |
  None. Public investor records (Tracxn, PitchBook) show no Anthropic / Anthropic Ventures presence in any
  Mistral funding round. PitchBook lists Anthropic as competitor.
dimensions:
  V: { score: 14, max: 20, rating: High }
  E: { score: 0,  max: 15, rating: NotEvaluated, note: "Layer 1+ only" }
  R: { score: 17, max: 20, rating: High }
  D: { score: 11, max: 15, rating: High }
  I: { score: 4,  max: 10, rating: Mid }
  C: { score: 2,  max: 10, rating: Low }
  T: { score: 7,  max: 10, rating: High }
total: 55
max: 85
percentage: 65
cisa_kev: false
cve_count_12mo: 0
supply_chain_compromise_12mo: 0
acquisition: Mistral AI SAS acquired Koyeb on 2026-02-17 (per PitchBook M&A record)
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
incident_tags:
  - no-cve-12mo
  - no-kev
  - status-page-public
  - supply-chain-clean
  - sandbox-isolation-undisclosed
  - saml-enterprise-only
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
evaluation_url: https://github.com/zinova-lab/verdict-platforms/blob/main/evaluations/061_mistral_la_plateforme.md
---

# Mistral La Plateforme

Mistral La Plateforme is the cloud API platform of Mistral AI SAS (Paris), a vertically integrated foundation model + agent platform operator. The platform exposes the Chat Completion API, Agents API (stateful conversation with code interpreter, web search, image generation, document library, MCP support), and Fine-Tuning API. Self-hosted, on-premises, and dedicated-environment deployment options exist at the enterprise tier.

## Layer 0 Score: 55/85 (Tier A)

**V** 14/20 · **R** 17/20 · **D** 11/15 · **I** 4/10 · **C** 2/10 · **T** 7/10

Strongest signals: publicly accessible DPA at legal.mistral.ai (no NDA gate) with SCC Module 4 + 10-day subprocessor objection right + EU data residency by default + paid API training opt-out by default + Zero Data Retention available on request + SOC 2 Type II + ISO 27001 / 27701 + zero CVEs across `mistralai/*` GitHub org and SDKs in trailing 12 months + EU GPAI Code of Practice signed + AI Compliance Hub mapping per-model and per-AI-system EU AI Act docs. Largest gaps: Code Interpreter sandbox isolation technology not disclosed in public materials beyond "isolated container" phrasing. SAML SSO Enterprise tier only. Agents API retention "until account termination" structurally longer than 30-day general API window. Subprocessor list last-updated date not directly observable in public-only fetched HTML.
