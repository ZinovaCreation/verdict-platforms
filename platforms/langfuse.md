---
slug: langfuse
title: Langfuse
score: 62
tier: A
tier_engine: A
tier_override_rationale: None (engine output Tier=A matches rankings convention 55-64 band)
category: AI / LLM Application Observability
subcategory: Open Core (MIT + Commercial EE)
license: MIT (core) + Enterprise Edition (commercial license, /ee directory)
operator: Langfuse GmbH
operator_parent: ClickHouse, Inc. (acquired 2026-01-16)
operator_jurisdiction: Berlin, Germany (Langfuse GmbH); San Francisco, USA (ClickHouse, Inc.)
funding: Y Combinator W23, Lightspeed, La Famiglia ($4.5M seed)
parent_funding: ClickHouse Inc. Series D $400M / total $1.05B / $15B valuation (2026-01-16)
yc_batch: W23
evaluation_date: 2026-04-29
evaluation_number: 060
framework_version: VERDICT v0.3.1
layer: 0
independence: ⚠️ Subsidiary of ClickHouse, Inc. since 2026-01-16
anthropic_relationship: |
  Indirect commercial customer relationship at parent-company level: Anthropic is publicly disclosed as a major
  customer of ClickHouse, Inc. (parent company). No equity overlap with Langfuse or ClickHouse — Anthropic /
  Anthropic Ventures absent from both investor lists per Tracxn / PitchBook.
dimensions:
  V: { score: 14, max: 20, rating: High }
  E: { score: 0,  max: 15, rating: NotEvaluated, note: "Layer 1+ only" }
  R: { score: 12, max: 20, rating: Mid }
  D: { score: 11, max: 15, rating: High }
  I: { score: 8,  max: 10, rating: High }
  C: { score: 8,  max: 10, rating: High }
  T: { score: 9,  max: 10, rating: High }
total: 62
max: 85
percentage: 73
cisa_kev: false
cve_count_12mo: 6
cve_max_cvss: 7.6
cve_top_id: CVE-2025-59305
supply_chain_compromise_12mo: 0
acquisition: ClickHouse, Inc. acquired Langfuse GmbH on 2026-01-16
tags:
  - llm-observability
  - ai-tracing
  - prompt-management
  - evaluation-platform
  - open-core
  - mit-license
  - soc2-type2
  - iso27001
  - hipaa
  - gdpr
  - self-hostable
  - air-gapped
  - clickhouse-acquired
incident_tags:
  - improper-access-control
  - cwe-284
  - cross-tenant-enumeration
  - sso-csrf
  - ssrf-webhook
  - slack-oauth-unauthenticated
  - llm-credential-exposure
  - rapid-patch-cadence
sources:
  - https://langfuse.com/
  - https://langfuse.com/security
  - https://langfuse.com/docs
  - https://github.com/langfuse/langfuse
  - https://langfuse.com/security/dpa
  - https://langfuse.com/security/privacy-policy
  - https://github.com/langfuse/langfuse/security/advisories
evaluation_url: https://github.com/zinova-lab/verdict-platforms/blob/main/evaluations/060_langfuse.md
---

# Langfuse

Langfuse is an open-source LLM application observability platform. The core is MIT-licensed, with an Enterprise Edition under separate commercial license (the `/ee` directory boundary). Operated by Langfuse GmbH, a Berlin company that became a subsidiary of ClickHouse, Inc. (San Francisco) on 2026-01-16. Public compliance posture is unusually complete for an open-core observability vendor at this maturity stage.

## Layer 0 Score: 62/85 (Tier A)

**V** 14/20 · **R** 12/20 · **D** 11/15 · **I** 8/10 · **C** 8/10 · **T** 9/10

Strongest signals: SOC 2 Type II + ISO 27001 + HIPAA region + GDPR with publicly accessible DPA + 13-page security center + explicit no-AI-training commitment + air-gapped self-hosting first-class + same-day patch median time. Largest concerns: six CVEs in trailing 12 months (max CVSS 7.6), four categorized CWE-284 (Improper Access Control) across distinct subsystems — recurrence pattern recorded for procurement decisions involving multi-tenant or cross-organization trust boundaries. Subprocessor list lacks visible last-updated date. Operator-naming on legal pages still references "Langfuse GmbH / Finto Technologies Inc." footer without ClickHouse acquisition reflection.

## Acquisition Disclosure

ClickHouse, Inc. (CEO Aaron Katz; 36 institutional investors including Dragoneer, Khosla, Index, Lightspeed, GIC, T. Rowe Price; Anthropic Ventures **not** present) acquired Langfuse GmbH on 2026-01-16 — same date Series D $400M was announced at $15B valuation. The technical relationship between products predates the acquisition: Langfuse v3 migrated its core data layer from PostgreSQL to ClickHouse in December 2024.

## Anthropic Relationship Surface

No equity overlap. Anthropic is, however, publicly disclosed as a major customer of ClickHouse, Inc. (parent company): ClickHouse press releases dated 2025-05-29 and 2025-10-07; TipRanks 2026-02-20 reporting on Anthropic's air-gapped ClickHouse deployment supporting Claude Code observability. This is an indirect commercial-relationship surface at the parent-company level, disclosed neutrally as fact.

## Bias Disclosure

This evaluation uses Claude (Anthropic) as its tooling. Anthropic operates in the AI agent market and may compete with some evaluated vendors. VERDICT discloses this relationship in every report and applies identical evaluation criteria to all platforms regardless of their relationship to Anthropic.

## Full Evaluation

See [`evaluations/060_langfuse.md`](../evaluations/060_langfuse.md) for the complete Layer 0 report (English + Japanese summary).
