---
slug: e2b
title: E2B
score: 46
tier: B
tier_engine: C
tier_override_rationale: |
  rankings/index.html convention (45-54 = B band) takes precedence over engine output Tier=C.
  Operations layer applies Tier from rankings convention, not engine output, per
  PENDING task engine-tier-classification-verify resolution (2026-04-29).
category: AI Agent Code Execution Sandbox
subcategory: Cloud Runtime Infrastructure
license: Apache 2.0
operator: FoundryLabs, Inc.
operator_jurisdiction: Delaware, USA
founders: Vasek Mlejnsky (CEO), Tomas Valenta (CTO)
funding: Insight Partners $21M Series A (Jul 2025); Decibel Partners $11.5M seed (Oct 2024)
yc_batch: W23
evaluation_date: 2026-04-28
evaluation_number: 059
framework_version: VERDICT v0.3.1
layer: 0
independence: Independent
anthropic_relationship: None (no equity overlap; reference Claude as one integration option among many)
dimensions:
  V: { score: 13, max: 20, rating: Mid }
  E: { score: 0,  max: 15, rating: NotEvaluated, note: "Layer 1+ only" }
  R: { score: 17, max: 20, rating: High }
  D: { score: 2,  max: 15, rating: Low }
  I: { score: 5,  max: 10, rating: Mid }
  C: { score: 6,  max: 10, rating: Mid }
  T: { score: 3,  max: 10, rating: Low }
total: 46
max: 85
percentage: 54
cisa_kev: false
cve_count_12mo: 0
supply_chain_compromise_12mo: 0
tags:
  - sandbox
  - firecracker
  - microvm
  - code-execution
  - agent-runtime
  - open-source
  - apache-2.0
  - byoc
  - self-hostable
  - layer-0
incident_tags:
  - zero-cve-12mo
  - no-soc2
  - no-security-md
  - no-dpa
  - allow-all-egress-default
  - env-var-secrets
  - broad-tos-license
sources:
  - https://e2b.dev/
  - https://e2b.dev/privacy
  - https://e2b.dev/terms
  - https://e2b.dev/enterprise
  - https://e2b.dev/docs
  - https://github.com/e2b-dev
  - https://status.e2b.dev/
evaluation_url: https://github.com/zinova-lab/verdict-platforms/blob/main/evaluations/059_e2b.md
---

# E2B

E2B is sandbox-runtime infrastructure for AI agent code execution. Operated by FoundryLabs, Inc. (Delaware), it provides Firecracker microVM-isolated environments through Apache 2.0-licensed SDKs and orchestrator. Backs downstream platforms including Perplexity, Hugging Face, Manus, Groq, and Lindy.

## Layer 0 Score: 46/85 (Tier B)

**V** 13/20 · **R** 17/20 · **D** 2/15 · **I** 5/10 · **C** 6/10 · **T** 3/10

Strongest signal: zero CVEs across NVD / OSV / GHSA in trailing 12 months, hardware-level Firecracker microVM tenant isolation. Largest gaps: no public SOC 2 / ISO 27001 attestation, no sub-processors list, no DPA, no SECURITY.md in primary repository. Privacy policy last revised April 2024 (~24 months stale relative to evaluation date). ToS "Submissions" clause grants perpetual royalty-free license without explicit AI-training-exclusion statement. Default network egress is allow-all; deny-by-default requires explicit configuration. Secrets pass via environment variables visible inside the sandbox (Issue #1160 tracks host-side broker discussion).

## Operations Override Note

Engine output assigned Tier=C; Operations applied Tier=B per rankings/index.html convention (45-54 score band = B tier). This is the 2nd recorded application of Operations layer Tier override (precedent: same evaluation in original engine session 2026-04-28). Codification of operations-side Tier-determination rule pending in ENGINE.md patch.

## Bias Disclosure

This evaluation uses Claude (Anthropic) as its tooling. Anthropic operates in the AI agent market and may compete with some evaluated vendors. VERDICT discloses this relationship in every report and applies identical evaluation criteria to all platforms regardless of their relationship to Anthropic. Public-data review of E2B's investor list (Insight Partners, Decibel Partners, Sunflower Capital, KAYA VC) found no Anthropic, Anthropic Ventures, or related-party investment.

## Full Evaluation

See [`evaluations/059_e2b.md`](../evaluations/059_e2b.md) for the complete Layer 0 report (English + Japanese summary).
