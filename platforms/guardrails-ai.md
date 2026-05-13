---
slug: guardrails-ai
title: Guardrails AI
score: 40
tier: C
tier_engine: B
tier_override_rationale: |
  ENGINE.md `## Tier Letter Assignment` thresholds (codified 2026-04-29, commit bd8cf2b)
  per Operations Override Rules in QA.md.
  Score 40 ∈ C band [35-44]. Engine output Tier=B was informational; Operations applied
  threshold-derived Tier=C as the canonical assignment.
category: AI Safety
subcategory: LLM Guardrails · Validators · Open-Source Framework + Commercial Cloud Platform
license: Open-source framework Apache 2.0 (`guardrails-ai` on PyPI, github.com/guardrails-ai/guardrails); commercial Pro / Snowglobe platform closed-source
operator: Guardrails AI, Inc.
operator_jurisdiction: Menlo Park, California, United States (Delaware C-corporation; California foreign-entity registration 5678079, incorporated 2023-04-25)
founders: Shreya Rajpal (CEO, ex-Apple ML / Predibase), Diego Oppenheimer (ex-Algorithmia / DataRobot), Safeer Mohiuddin (ex-AWS), Zayd Simjee (ex-AWS)
funding: Seed $7.5M (February 2024); ~11 employees per Tracxn January 2026
major_investors: Zetta Venture Partners (Seed lead), Bloomberg Beta, Pear VC, Factory, GitHub Fund, plus AI angel investors including Ian Goodfellow (Google DeepMind), Logan Kilpatrick (Google / ex-OpenAI), Lip-Bu Tan
evaluation_date: 2026-05-12
evaluation_number: 064
framework_version: VERDICT v0.3.1
layer: 0
independence: ✅ Independent (no Anthropic / Anthropic Ventures equity overlap per public investor records)
anthropic_relationship: |
  Framework-integration only. The Guardrails open-source framework supports Anthropic Claude
  as one of multiple LLM providers (LLM-agnostic by design); the framework operates between
  customer application and any LLM provider using customer-supplied LLM API keys.
  No equity relationship exists per public investor records.
  Additionally, Guardrails AI and VERDICT operate in adjacent institutional categories within
  the AI trust infrastructure space (Guardrails AI provides runtime containment to AI
  applications; VERDICT provides independent evaluation of AI agent platforms). VERDICT
  applies identical evaluation criteria regardless of category adjacency.
dimensions:
  V: { score: 11, max: 20, rating: Mid }
  E: { score: 0,  max: 15, rating: NotEvaluated, note: "Layer 1+ only" }
  R: { score: 17, max: 20, rating: High }
  D: { score: 1,  max: 15, rating: Low }
  I: { score: 4,  max: 10, rating: Mid }
  C: { score: 3,  max: 10, rating: Low }
  T: { score: 4,  max: 10, rating: Mid }
total: 40
max: 85
percentage: 47
cisa_kev: false
cve_count_12mo: 0
supply_chain_compromise_12mo: 0
acquisition: None applicable.
category_precedent: |
  First AI-safety / LLM-guardrails category evaluation under VERDICT framework. C dimension
  adapted to hybrid evaluation surface: the open-source framework runs as a Python library
  in customer process (no operator-side sandbox; containment is customer responsibility);
  the commercial Pro / Snowglobe cloud platform validator runtime is the operator-side
  execution surface evaluated under C dimension. Adaptation recorded for framework precedent.
historical_cve_reference: |
  CVE-2024-45858 (CVSS v3.1 7.8 HIGH / v4 8.5 HIGH, disclosed 2024-09-18, fixed in v0.5.10
  on 2024-09-17) — arbitrary code execution via eval() in parse_token (ValidatorsAttr class)
  when loading maliciously crafted RAIL XML files. Out of trailing-12-month evaluation window
  but recorded for completeness. CNA: HiddenLayer, Inc.
dependency_event_12mo: |
  2026-03-24: litellm PyPI package removed from PyPI simple index, breaking fresh installs
  of guardrails-ai 0.5.1 and guardrails-api 0.2.1–0.3.2. Dependency-availability event, not
  malicious supply-chain compromise. Operator workaround documented (install litellm
  directly from GitHub).
tags:
  - ai-safety
  - llm-guardrails
  - validators
  - apache-2-0
  - open-source-framework
  - guardrails-hub
  - snowglobe
  - seed-stage
  - early-stage
incident_tags:
  - no-cve-trailing-12mo
  - no-kev
  - historical-rce-fixed
  - dependency-availability-event-litellm
  - no-public-soc2
  - no-public-iso27001
  - no-public-trust-center
  - no-public-dpa-url
sources:
  - https://www.guardrailsai.com/
  - https://www.guardrailsai.com/docs
  - https://www.guardrailsai.com/legal/terms-of-use
  - https://www.guardrailsai.com/blog/commitment-to-responsible-vulnerability
  - https://github.com/guardrails-ai/guardrails
  - https://github.com/guardrails-ai/guardrails/releases
  - https://github.com/guardrails-ai/guardrails/security
  - https://hub.guardrailsai.com/
  - https://pypi.org/project/guardrails-ai/
  - https://bizfileonline.sos.ca.gov/search/business
evaluation_url: https://github.com/ZinovaCreation/verdict-platforms/blob/main/evaluations/064_guardrails_ai.md
---

# Guardrails AI

Guardrails AI is the operator of the Apache-2.0 Guardrails open-source framework for LLM input / output validators, the Guardrails Hub community-contributed validator marketplace, and the commercial Pro / Snowglobe cloud platform. The operator (Guardrails AI, Inc., Delaware C-corporation with California foreign-entity registration, principal place of business Menlo Park) is post-Seed ($7.5M raised February 2024, Zetta Venture Partners lead) with approximately 11 employees as of January 2026. This is the first AI-safety / LLM-guardrails category evaluation under VERDICT framework.

## Layer 0 Score: 40/85 (Tier C)

**V** 11/20 · **R** 17/20 · **D** 1/15 · **I** 4/10 · **C** 3/10 · **T** 4/10

Strongest signals: clearly named legal entity (Guardrails AI, Inc.) verifiable via California Secretary of State entity 5678079 + named founders with verifiable backgrounds (Apple ML, AWS, DataRobot) + disclosed investor list including identified AI angel investors + Apache-2.0 open-source core framework on GitHub and PyPI fully auditable + active release cadence (latest stable 0.10.0; PyPI-published) + zero confirmed CVEs in the trailing twelve months (NVD, OSV, Snyk, GHSA verified) + zero CISA KEV entries + published responsible-disclosure policy with safe-harbor language + dedicated security email (security@guardrailsai.com) + coordinated CNA disclosure of historical CVE-2024-45858 with ~1 day public disclosure speed after fix + Snowglobe customers independently verifiable from third-party coverage (Changi Airport Group, Masterclass, IMDA AI Verify, Stanford LIFT Lab) + dependency-availability event (litellm PyPI removal) documented with operator workaround.

Largest gaps: no publicly available SOC 2 / ISO 27001 / HIPAA / equivalent independent certification + no public Trust Center, status page, or sub-processor list located + no public Data Processing Addendum URL (referenced in Terms of Use but not directly accessible) + no public statement on AI training use of customer data (silence-is-data scored zero) + no public retention schedule + commercial Pro / Snowglobe sandbox / tenant-isolation architecture not publicly documented + Guardrails Hub validators downloaded as Python code execute with customer-process privileges without published Hub-side code-review, code-signing, or sandboxing process + GitHub SECURITY.md absent at repository root (substituted by blog post) + no published NIST AI RMF / ISO/IEC 42001 / EU AI Act framework mapping for operator's own posture + customer Robinhood cited on operator website not independently verifiable from customer-side public sources at evaluation date.

CISA KEV: none. Trailing 12-month CVE count: 0. Trailing 12-month supply-chain compromise: 0. Historical CVE-2024-45858 (out of window): documented for completeness.
