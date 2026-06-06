---
name: Guardrails AI
slug: guardrails-ai
operator: Guardrails AI, Inc.
independence: independent
parent_entity: null
category: AI Safety
homepage: https://www.guardrailsai.com
github: https://github.com/guardrails-ai
evaluation_number: 64
evaluation_type: initial
evaluated_at: '2026-05-12'
evaluator_model: unrecorded
framework_version: v0.3.1-final
layer: '0'
target_version: null
previous_evaluation_date: null
previous_score: null
score: 40
max_score: 85
tier: C
verdict:
  v:
    score: 11
    rating: Mid
    note: ''
  r:
    score: 17
    rating: High
    note: ''
  d:
    score: 1
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
    score: 4
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
next_review_due: '2026-08-10'
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
rank: null
---
# Guardrails AI

Guardrails AI is the operator of the Apache-2.0 Guardrails open-source framework for LLM input / output validators, the Guardrails Hub community-contributed validator marketplace, and the commercial Pro / Snowglobe cloud platform. The operator (Guardrails AI, Inc., Delaware C-corporation with California foreign-entity registration, principal place of business Menlo Park) is post-Seed ($7.5M raised February 2024, Zetta Venture Partners lead) with approximately 11 employees as of January 2026. This is the first AI-safety / LLM-guardrails category evaluation under VERDICT framework.

## Layer 0 Score: 40/85 (Tier C)

**V** 11/20 · **R** 17/20 · **D** 1/15 · **I** 4/10 · **C** 3/10 · **T** 4/10

Strongest signals: clearly named legal entity (Guardrails AI, Inc.) verifiable via California Secretary of State entity 5678079 + named founders with verifiable backgrounds (Apple ML, AWS, DataRobot) + disclosed investor list including identified AI angel investors + Apache-2.0 open-source core framework on GitHub and PyPI fully auditable + active release cadence (latest stable 0.10.0; PyPI-published) + zero confirmed CVEs in the trailing twelve months (NVD, OSV, Snyk, GHSA verified) + zero CISA KEV entries + published responsible-disclosure policy with safe-harbor language + dedicated security email (security@guardrailsai.com) + coordinated CNA disclosure of historical CVE-2024-45858 with ~1 day public disclosure speed after fix + Snowglobe customers independently verifiable from third-party coverage (Changi Airport Group, Masterclass, IMDA AI Verify, Stanford LIFT Lab) + dependency-availability event (litellm PyPI removal) documented with operator workaround.

Largest gaps: no publicly available SOC 2 / ISO 27001 / HIPAA / equivalent independent certification + no public Trust Center, status page, or sub-processor list located + no public Data Processing Addendum URL (referenced in Terms of Use but not directly accessible) + no public statement on AI training use of customer data (silence-is-data scored zero) + no public retention schedule + commercial Pro / Snowglobe sandbox / tenant-isolation architecture not publicly documented + Guardrails Hub validators downloaded as Python code execute with customer-process privileges without published Hub-side code-review, code-signing, or sandboxing process + GitHub SECURITY.md absent at repository root (substituted by blog post) + no published NIST AI RMF / ISO/IEC 42001 / EU AI Act framework mapping for operator's own posture + customer Robinhood cited on operator website not independently verifiable from customer-side public sources at evaluation date.

CISA KEV: none. Trailing 12-month CVE count: 0. Trailing 12-month supply-chain compromise: 0. Historical CVE-2024-45858 (out of window): documented for completeness.

## Bias Disclosure

This evaluation uses Claude (Anthropic) as its tooling. Anthropic operates in the AI agent market and may compete with some evaluated vendors. VERDICT discloses this relationship in every report and applies identical evaluation criteria to all platforms regardless of their relationship to Anthropic.
