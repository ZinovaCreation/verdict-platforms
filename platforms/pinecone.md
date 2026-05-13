---
slug: pinecone
title: Pinecone
score: 71
tier: S
tier_engine: S
tier_override_rationale: |
  No override applied. Engine output Tier=S; ENGINE.md `## Tier Letter Assignment` threshold
  (score 71 ∈ S band [65-85]) yields Tier=S. Engine output and threshold-derived Tier are
  consistent; canonical Tier follows engine output unchanged.
category: Vector Database
subcategory: Retrieval Infrastructure · Cloud Service · BYOC · Enterprise Options
license: Closed-source platform; SDKs (Python `pinecone-client`, TypeScript `@pinecone-database/pinecone`, Java, Go community) open-source under pinecone-io GitHub organization
operator: Pinecone Systems, Inc.
operator_jurisdiction: New York, NY, United States (Delaware C-corporation; NY State DOS #6443133)
founders: Edo Liberty (founder, transitioned to Chief Scientist September 2025); Ash Ashutosh (CEO from September 2025)
funding: ~$138M total disclosed across rounds; Series B lead Andreessen Horowitz ($100M, April 2023, ~$750M post-money per third-party reporting)
major_investors: Andreessen Horowitz, ICONIQ Growth, Wing Venture Capital, Menlo Ventures, Tiger Global
evaluation_date: 2026-05-12
evaluation_number: 063
framework_version: VERDICT v0.3.1
layer: 0
independence: ✅ Independent (no Anthropic / Anthropic Ventures equity overlap per public investor records)
anthropic_relationship: |
  Direct commercial integration via Pinecone Assistant. Pinecone Assistant directly consumes
  Anthropic Claude API as a supported LLM provider; January 2026 release notes document
  operator-side routing logic that automatically redirects requests specifying claude-3-5-sonnet
  or claude-3-7-sonnet to claude-sonnet-4-5 following Anthropic's model deprecation. No equity
  relationship exists per public investor records. VERDICT applies identical evaluation criteria.
dimensions:
  V: { score: 16, max: 20, rating: High }
  E: { score: 0,  max: 15, rating: NotEvaluated, note: "Layer 1+ only" }
  R: { score: 20, max: 20, rating: High }
  D: { score: 11, max: 15, rating: High }
  I: { score: 8,  max: 10, rating: High }
  C: { score: 8,  max: 10, rating: High }
  T: { score: 8,  max: 10, rating: High }
total: 71
max: 85
percentage: 83.5
cisa_kev: false
cve_count_12mo: 0
supply_chain_compromise_12mo: 0
acquisition: None applicable.
category_precedent: |
  First vector database category evaluation under VERDICT framework. C dimension adapted from
  sandbox-isolation semantics (used for agent platforms) to multi-tenant index isolation
  semantics (namespace separation, BYOC infrastructure isolation, customer-managed encryption
  keys). Adaptation recorded for framework precedent.
tags:
  - vector-database
  - retrieval-infrastructure
  - pinecone-serverless
  - byoc
  - cmek
  - rag
  - multi-cloud
  - soc2-type2
  - iso27001
  - hipaa-addon
  - public-dpa
  - ai-services-addendum
  - eu-ai-act-reference
incident_tags:
  - zero-cve-12mo
  - no-kev
  - shai-hulud-unaffected
  - shai-hulud-2-unaffected
  - axios-unaffected
  - vercel-context-unaffected
  - status-page-public
  - supply-chain-clean
sources:
  - https://www.pinecone.io/
  - https://docs.pinecone.io/
  - https://docs.pinecone.io/release-notes/2026
  - https://security.pinecone.io/
  - https://www.pinecone.io/security/
  - https://www.pinecone.io/legal/data-processing-addendum/
  - https://www.pinecone.io/legal/2025.1_Pinecone%20AI%20Services%20Addendum.pdf
  - https://www.pinecone.io/blog/hipaa/
  - https://github.com/pinecone-io
  - https://status.pinecone.io/
evaluation_url: https://github.com/ZinovaCreation/verdict-platforms/blob/main/evaluations/063_pinecone.md
---

# Pinecone

Pinecone is the fully-managed vector database operated by Pinecone Systems, Inc. (Delaware C-corporation, New York headquarters). The platform serves high-recall nearest-neighbor similarity queries at production scale and is the first vector database category evaluation under VERDICT framework. Components include Pinecone Serverless (multi-tenant cloud, pay-per-use, AWS / Azure / GCP regions), Pinecone Assistant (retrieval-augmented generation service with operator-side routing to LLM providers including Anthropic Claude), Pinecone Inference (managed embedding model hosting), and BYOC (Bring Your Own Cloud, public preview multi-cloud February 2026) where the Pinecone cluster runs inside the customer's own AWS / Azure / GCP account.

## Layer 0 Score: 71/85 (Tier S)

**V** 16/20 · **R** 20/20 · **D** 11/15 · **I** 8/10 · **C** 8/10 · **T** 8/10

Strongest signals: every dimension reaches High rating threshold + SOC 2 Type II 2025 audit completed with zero deviations (published on Trust Center) + ISO 27001:2022 surveillance audit active (verifiable via IAF CertSearch) + zero Pinecone Systems product CVEs in trailing twelve months + zero CISA KEV entries + Trust Center carries four affirmative not-affected statements (Shai-Hulud and Shai-Hulud 2.0 NPM worm campaigns, Axios package compromise, Vercel/Context.ai April 2026 incident) + publicly accessible Data Processing Addendum incorporating SCC Modules 2 and 3, UK Addendum, and Swiss FADP + AI Services Addendum §5 explicit no-training commitment for any shared model + HIPAA available via Standard add-on ($190/month) or Enterprise inclusion + BYOC zero-access operating model (no SSH / VPN / inbound network access needed by Pinecone) + CMEK GA March 2026 + service accounts and audit logs GA March 2026 + AI Services Addendum §4 prohibits misrepresenting AI Output as human-generated (EU AI Act-referenced contractual stance).

Largest gaps: multi-factor authentication marked "Coming Soon" on security page at evaluation date (SSO via SAML mitigates this for federated identity flows only) + SOC 2 / HIPAA / Pentest reports access-gated through SafeBase Trust Center + AI Services (Pinecone Assistant, Pinecone Inference) by default excluded from BAA scope per AI Services Addendum §7(e) absent separate written agreement + telemetry default collection position not publicly documented (silence-is-data zero) + default-issued API keys carry broad permissions (least-privilege configurable but not default) + BYOC multi-cloud at public preview rather than GA at evaluation date + /legal/subprocessors/ page last-updated 2024-05-24 out of sync with current Trust Center version.

CISA KEV: none. Trailing 12-month CVE count: 0. Trailing 12-month supply-chain compromise: 0 (with four affirmative not-affected disclosures during evaluation window).
