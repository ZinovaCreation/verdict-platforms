---
name: Langfuse
slug: langfuse
operator: Langfuse GmbH
independence: subsidiary
parent_entity: ClickHouse, Inc.
category: AI / LLM Application Observability
homepage: https://langfuse.com
github: https://github.com/langfuse
evaluation_number: 60
evaluation_type: initial
evaluated_at: '2026-04-29'
evaluator_model: unrecorded
framework_version: v0.3.1-final
layer: '0'
target_version: null
previous_evaluation_date: null
previous_score: null
score: 62
max_score: 85
tier: A
verdict:
  v:
    score: 14
    rating: High
    note: ''
  r:
    score: 12
    rating: Mid
    note: ''
  d:
    score: 11
    rating: High
    note: ''
  i:
    score: 8
    rating: High
    note: ''
  c:
    score: 8
    rating: High
    note: ''
  t:
    score: 9
    rating: High
    note: ''
  e:
    score: null
    rating: null
    note: null
cisa_kev:
  present: false
  entries: []
cve_count_12mo: 6
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
sources:
- https://langfuse.com/
- https://langfuse.com/security
- https://langfuse.com/docs
- https://github.com/langfuse/langfuse
- https://langfuse.com/security/dpa
- https://langfuse.com/security/privacy-policy
- https://github.com/langfuse/langfuse/security/advisories
rank: null
"finding": |-
  LLM observability platform with annual SOC 2 Type II + ISO 27001 + HIPAA + GDPR self-serve DPA + 13-page security center. Configurable retention 3 days to unlimited, nightly purge. Explicit no-AI-training commitment. Open-core: MIT outside ee/ + EE under separate license. Six CVEs in trailing 12 months, max CVSS 7.6 (CVE-2025-59305 background-migration improper authorization, same-day patch). Four CVEs categorized CWE-284 across distinct subsystems — recurrence pattern recorded for cross-tenant deployments. Acquired by ClickHouse, Inc. on 2026.01.16; legal-entity disclosures on subprocessors page and footer not yet updated. Anthropic is publicly disclosed as a major customer of parent ClickHouse, Inc.; no equity overlap with Langfuse or ClickHouse.
"meta_owner": |-
  Langfuse GmbH (Berlin) · Subsidiary of ClickHouse, Inc. since 2026.01.16 · Founders Marc Klingen · YC W23 + Lightspeed
"meta_description": |-
  Independent security evaluation of Langfuse by Langfuse GmbH (subsidiary of ClickHouse, Inc. since 2026.01.16). Score: 62/85. LLM observability platform. SOC 2 Type II + ISO 27001 + HIPAA. MIT core + EE. Six CVEs trailing 12 months, four CWE-284 access control. Anthropic indirect commercial customer of parent ClickHouse. Framework v0.3.1.
"og_description": |-
  Independent security evaluation of Langfuse by Langfuse GmbH (ClickHouse subsidiary). Score: 62/85. LLM observability. SOC 2 II + ISO 27001 + HIPAA. Six CVEs (4 access control). Framework v0.3.1.
"category_line": |-
  AI / LLM Application Observability Platform · Open Core (MIT + Commercial EE)
display_tags:
- text: SOC 2 II + ISO 27001 + HIPAA
  color: safe
- text: No AI Training · Configurable Retention
  color: safe
- text: 6 CVEs · 4× CWE-284 Access Control
  color: amber
- text: ClickHouse Acquisition · 2026.01.16
  color: amber
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