---
name: E2B
slug: e2b
operator: FoundryLabs, Inc.
independence: independent
parent_entity: null
category: AI Agent Code Execution Sandbox
homepage: https://e2b.dev
github: https://github.com/e2b-dev
evaluation_number: 59
evaluation_type: initial
evaluated_at: '2026-04-28'
evaluator_model: unrecorded
framework_version: v0.3.1-final
layer: '0'
target_version: E2B SDK e2b (latest stable, npm/PyPI as of evaluation date); infrastructure repo e2b-dev/infra HEAD
previous_evaluation_date: null
previous_score: null
score: 46
max_score: 85
tier: null
verdict:
  v:
    score: 13
    rating: Mid
    note: Entity/OSS/changelog confirmed; independent cert and sub-processor list absent
  r:
    score: 17
    rating: High
    note: Zero CVEs trailing 12mo; no supply-chain compromise
  d:
    score: 2
    rating: Low
    note: No DPA, sub-processor list, or AI-training-exclusion in public docs
  i:
    score: 5
    rating: Mid
    note: Lifecycle controls complete; RBAC marked SOON, not yet GA
  c:
    score: 6
    rating: Mid
    note: Firecracker microVM isolation; egress default allow-all
  t:
    score: 3
    rating: Low
    note: No SECURITY.md; no AI safety framework reference
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
next_review_due: '2026-07-27'
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
sources:
- https://e2b.dev/
- https://e2b.dev/privacy
- https://e2b.dev/terms
- https://e2b.dev/enterprise
- https://e2b.dev/docs
- https://github.com/e2b-dev
- https://status.e2b.dev/
rank: null
"og_description": |-
  Independent security evaluation of E2B by FoundryLabs, Inc. Score: 46/85. Firecracker microVM sandbox. Apache 2.0. Zero CVEs trailing 12 months. No SOC 2. Framework v0.3.1.
"category_line": |-
  AI Agent Code Execution Sandbox · Cloud Runtime Infrastructure · Open Source (Apache 2.0)
display_tags:
- text: Firecracker microVM · Apache 2.0
  color: safe
- text: 0 CVEs · Trailing 12 Months
  color: safe
- text: No SOC 2 · No SECURITY.md · No DPA
  color: amber
- text: Allow-All Egress Default · ToS Submissions Broad
  color: amber
"finding": |-
  Sandbox-runtime infrastructure powering downstream platforms including Perplexity, Hugging Face, Manus, Groq, and Lindy. Firecracker microVM provides hardware-level KVM tenant isolation. Zero CVEs across NVD / OSV / GHSA in trailing 12 months. Apache 2.0 across SDK, infra, dashboard, code-interpreter, and forked Firecracker. Largest scoring gaps: no public SOC 2 / ISO 27001 attestation, no sub-processors list, no DPA, no SECURITY.md in primary repository. Privacy policy last revised April 2024 (~24 months stale). ToS "Submissions" clause grants perpetual royalty-free license without explicit AI-training-exclusion statement. Default network egress is allow-all; deny-by-default requires explicit configuration. Secrets pass via environment variables visible inside the sandbox (Issue #1160 tracks host-side broker discussion). RBAC marked "SOON" on enterprise page.
"meta_owner": |-
  FoundryLabs, Inc. · Founders Vasek Mlejnsky & Tomas Valenta · Insight Partners $21M Series A · YC W23
"meta_description": |-
  Independent security evaluation of E2B by FoundryLabs, Inc. Score: 46/85. Firecracker microVM sandbox runtime infrastructure. Apache 2.0. Zero CVEs trailing 12 months. No SOC 2 / no SECURITY.md / no DPA. ToS Submissions clause broad. Framework v0.3.1.
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
