---
name: Weaviate
slug: weaviate
operator: Weaviate B.V.
independence: independent
parent_entity: null
category: Vector Database
homepage: https://weaviate.io
github: https://github.com/weaviate/weaviate
evaluation_number: 65
evaluation_type: initial
evaluated_at: '2026-05-15'
evaluator_model: unrecorded
framework_version: v0.3.1-final
layer: '0'
target_version: Weaviate Database 1.33.x / 1.34.0
previous_evaluation_date: null
previous_score: null
score: 62
max_score: 85
tier: A
verdict:
  v:
    score: 16
    rating: High
    note: ''
  r:
    score: 14
    rating: High
    note: ''
  d:
    score: 13
    rating: High
    note: ''
  i:
    score: 6
    rating: Mid
    note: ''
  c:
    score: 6
    rating: Mid
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
cve_count_12mo: 2
cve_count_basis: exact
max_cvss_12mo: 8.7
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
- vector-database
- weaviate
- bsd-3-clause
- oss
- gdpr
- soc2-type2
- iso27001-2022
- hipaa-dedicated
- rbac
- oidc
- multi-tenancy
- byoc
- weaviate-cloud
rank: 6
sources:
- https://weaviate.io/
- https://docs.weaviate.io
- https://github.com/weaviate/weaviate
- https://weaviate.io/subprocessors
- https://trust.weaviate.io
- https://weaviate.io/privacy
- https://weaviate.io/blog/weaviate-iso-compliant
finding: 'Weaviate scores 62/85 (Tier A) under VERDICT v0.3.1 Layer 0, evaluated at
  Database 1.33.x / 1.34.0. Verifiability and data conduct lead: a BSD 3-Clause open-source
  core, a dual-entity legal structure (Weaviate B.V. in Amsterdam and Weaviate, LLC
  in the US) published with jurisdictional clarity, a versioned and dated Data Processing
  Agreement (v1.4, February 2026) whose §2.2 states Personal Data is not processed
  for model training without documented customer instruction, a publicly dated sub-processor
  list (October 2025), and ISO 27001:2022 certification (September 2025) alongside
  existing SOC 2 Type II. Two path-traversal CVEs — CVE-2025-67818 (Backup ZipSlip,
  CVSS v4.0 8.7) and CVE-2025-67819 (Shard Movement, CVSS 4.9) — were reported through
  Weaviate''s Vulnerability Disclosure Program by an external researcher and patched
  in coordinated release across four supported minor branches (1.30.20 / 1.31.19 /
  1.32.16 / 1.33.4) in November–December 2025. Recorded concerns cluster in identity-control
  and containment: OSS telemetry is on by default with cloud-metadata shared with
  hyperscalers for commercial lead identification (opt-out via DISABLE_TELEMETRY=true),
  generative modules execute in the main process without a documented egress allowlist,
  human-in-the-loop is not stated as a default-enforced control for the Query Agent
  and Transformation Agent surfaces, SOC 2 and ISO 27001 evidence is gated behind
  the trust portal, and no AI-specific safety framework (NIST AI RMF, ISO/IEC 42001)
  is referenced in public documentation.'
meta_owner: Weaviate B.V. (Amsterdam, NL) / Weaviate, LLC (US) · Independent, venture-backed
  · Series B, 2023, Index Ventures lead · No parent company, no acquisition history
meta_description: 'Weaviate (Vector Database) scores 62/85, Tier A, under VERDICT
  v0.3.1 Layer 0. Strengths: a BSD 3-Clause open-source core, a dated DPA (v1.4) stating
  no model training without customer instruction, ISO 27001:2022 plus SOC 2 Type II,
  and coordinated patching of two path-traversal CVEs. Concerns: default-on OSS telemetry
  with cloud-metadata sharing, in-process generative modules without a documented
  egress allowlist, and trust-portal-gated audit evidence.'
og_description: 'Weaviate scores 62/85 (Tier A) on VERDICT v0.3.1 Layer 0: strong
  open-source verifiability and data conduct, with concerns in default-on telemetry,
  in-process module egress, and gated audit evidence.'
category_line: Vector Database · Open Source (BSD 3-Clause) · Self-Hosted & Managed
  Cloud · Bring Your Own Cloud · Retrieval Infrastructure
display_tags:
- text: BSD 3-Clause open-source core
  color: safe
- text: ISO 27001:2022 + SOC 2 Type II
  color: safe
- text: No model training without instruction
  color: safe
- text: Coordinated CVE disclosure, four branches patched
  color: safe
- text: OSS telemetry on by default
  color: amber
- text: In-process module egress, no allowlist
  color: amber
- text: Audit evidence trust-portal gated
  color: amber
- text: Two path-traversal CVEs (CWE-22), patched
  color: dim
---

# Weaviate

<!-- TODO(Zinova): overview paragraph + Strongest signals / Largest gaps — to be authored from evaluations/065_weaviate.md (display copy fields finding/meta_owner/meta_description/og_description/category_line/display_tags also pending in frontmatter). -->

## Layer 0 Score: 62/85 (Tier A)

**V** 16/20 · **R** 14/20 · **D** 13/15 · **I** 6/10 · **C** 6/10 · **T** 7/10

## Bias Disclosure

This evaluation uses Claude (Anthropic) as its tooling. Anthropic operates in the AI agent market and may compete with some evaluated vendors. VERDICT discloses this relationship in every report and applies identical evaluation criteria to all platforms regardless of their relationship to Anthropic.

Specific to this evaluation: Weaviate ships a `generative-anthropic` module enabling RAG with Anthropic Claude models, default-enabled on Weaviate Cloud instances. The integration uses customer-supplied Anthropic API keys (BYOK); no direct billing or commercial relationship between Anthropic and Weaviate is publicly disclosed. Anthropic models are also reachable indirectly through the AWS Bedrock generative module. This indirect integration was treated identically to integrations with other model providers (OpenAI, Cohere, Voyage AI, Google, Hugging Face) during scoring.