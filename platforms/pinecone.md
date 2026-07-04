---
name: Pinecone
slug: pinecone
operator: Pinecone Systems, Inc.
independence: independent
parent_entity: null
category: Vector Database
homepage: https://www.pinecone.io
github: https://github.com/pinecone-io
evaluation_number: 63
evaluation_type: initial
evaluated_at: '2026-05-12'
evaluator_model: unrecorded
framework_version: v0.3.1-final
layer: '0'
target_version: Pinecone Serverless (current GA); BYOC public preview (multi-cloud,
  Feb 2026); Python SDK pinecone v8.x; TypeScript SDK @pinecone-database/pinecone
  v6.x
previous_evaluation_date: null
previous_score: null
score: 71
max_score: 85
tier: S
verdict:
  v:
    score: 16
    rating: High
    note: SOC 2 Type II zero-deviation, ISO 27001 active; engine closed, SOC2 report
      gated
  r:
    score: 20
    rating: High
    note: Zero product CVEs 12mo; four affirmative supply-chain not-affected statements
  d:
    score: 11
    rating: High
    note: Public DPA, SCC M2/M3, no-train clause; telemetry default undocumented
  i:
    score: 8
    rating: High
    note: Control/data-plane keys, RBAC, SAML, service accounts GA; MFA Coming Soon
  c:
    score: 8
    rating: High
    note: Namespace isolation, BYOC zero-access, CMEK GA; default keys broad-permission
  t:
    score: 8
    rating: High
    note: Trust Center advisories, public status timelines; SOC2/Pentest SafeBase-gated
  e:
    score: null
    rating: null
    note: null
cisa_kev:
  present: false
  entries: []
cve_count_12mo: 0
cve_count_basis: exact
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
rank: 1
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
og_description: 'Independent security evaluation of Pinecone by Pinecone Systems Inc.
  Score: 71/85. Managed vector database. SOC 2 II zero deviations. Zero CVEs. BYOC
  zero-access. Direct Anthropic Claude integration via Pinecone Assistant. Framework
  v0.3.1.'
category_line: Vector Database · Retrieval Infrastructure · Cloud Service · BYOC ·
  Enterprise Options
display_tags:
- text: SOC 2 II Zero Deviations + ISO 27001:2022
  color: safe
- text: 0 CVEs · 12 Months
  color: safe
- text: Shai-Hulud / Axios / Vercel Unaffected
  color: safe
- text: BYOC Zero-Access + CMEK GA
  color: safe
- text: MFA "Coming Soon"
  color: amber
finding: Fully managed vector database from Pinecone Systems, Inc. (New York). Every
  dimension reaches High rating threshold. SOC 2 Type II 2025 audit completed with
  zero deviations; ISO 27001:2022 surveillance audit active (verifiable via IAF CertSearch
  independent of operator materials). Zero Pinecone-product CVEs in trailing twelve
  months across NVD / GHSA / OSV. Trust Center carries four affirmative not-affected
  statements within evaluation window (Shai-Hulud and Shai-Hulud 2.0 NPM worm campaigns,
  Axios package compromise, Vercel/Context.ai April 2026 incident). Publicly accessible
  Data Processing Addendum incorporates SCC Modules 2 and 3, UK Addendum, and Swiss
  FADP; EDPO appointed as GDPR Article 27 representative. AI Services Addendum §5
  explicit no-training commitment for any shared model. HIPAA via Standard add-on
  ($190/month) or Enterprise inclusion. BYOC zero-access operating model (no SSH /
  VPN / inbound network access; vectors / metadata / queries never leave customer
  cloud account) at public-preview multi-cloud February 2026. CMEK GA March 2026;
  service accounts and audit logs GA March 2026. First vector database category evaluation
  under VERDICT framework; C dimension adapted for multi-tenant index isolation semantics.
  Direct commercial integration with Anthropic Claude via Pinecone Assistant (automatic
  routing of deprecated Claude 3.5/3.7 Sonnet to Claude Sonnet 4.5 documented in January
  2026 release notes). Independent of Anthropic at every equity layer. MFA marked
  "Coming Soon" at evaluation date.
meta_owner: Pinecone Systems, Inc. · New York, NY · Delaware C-corp · Founder Liberty
  · CEO Ashutosh (Sep 2025) · ~$138M (a16z Series B lead)
meta_description: 'Independent security evaluation of Pinecone by Pinecone Systems,
  Inc. (Delaware C-corp, NY HQ). Score: 71/85. Managed vector database (Pinecone Serverless
  + Assistant + Inference + BYOC). SOC 2 II 2025 zero deviations + ISO 27001:2022
  + HIPAA + GDPR. Zero CVEs trailing 12 months. Affirmative Shai-Hulud / Axios / Vercel-Context
  unaffected disclosures. 1st vector database category evaluation. Framework v0.3.1.'
key_finding: "Fully managed vector database from Pinecone Systems, Inc. Every dimension reaches High rating. SOC 2 Type II 2025 with zero deviations + ISO 27001:2022. Zero CVEs trailing 12 months. Affirmative Shai-Hulud / Axios / Vercel-Context unaffected disclosures. BYOC zero-access multi-cloud public preview Feb 2026. CMEK GA March 2026. Direct Anthropic Claude integration via Pinecone Assistant. First vector database category evaluation. MFA \"Coming Soon\" at evaluation date."
card_owner: "Pinecone Systems, Inc. · New York · a16z Series B"
card_category: "Vector Database · Retrieval Infrastructure · Cloud Service + BYOC"
card_tags:
  - text: "SOC 2 II Zero Deviations + ISO 27001:2022"
    color: safe
  - text: "0 CVEs · 12 Months"
    color: safe
  - text: "Shai-Hulud / Axios / Vercel Unaffected"
    color: safe
  - text: "BYOC Zero-Access + CMEK GA"
    color: safe
  - text: "MFA Coming Soon"
    color: amber
---

# Pinecone

Pinecone is the fully-managed vector database operated by Pinecone Systems, Inc. (Delaware C-corporation, New York headquarters). The platform serves high-recall nearest-neighbor similarity queries at production scale and is the first vector database category evaluation under VERDICT framework. Components include Pinecone Serverless (multi-tenant cloud, pay-per-use, AWS / Azure / GCP regions), Pinecone Assistant (retrieval-augmented generation service with operator-side routing to LLM providers including Anthropic Claude), Pinecone Inference (managed embedding model hosting), and BYOC (Bring Your Own Cloud, public preview multi-cloud February 2026) where the Pinecone cluster runs inside the customer's own AWS / Azure / GCP account.

## Layer 0 Score: 71/85 (Tier S)

**V** 16/20 · **R** 20/20 · **D** 11/15 · **I** 8/10 · **C** 8/10 · **T** 8/10

Strongest signals: every dimension reaches High rating threshold + SOC 2 Type II 2025 audit completed with zero deviations (published on Trust Center) + ISO 27001:2022 surveillance audit active (verifiable via IAF CertSearch) + zero Pinecone Systems product CVEs in trailing twelve months + zero CISA KEV entries + Trust Center carries four affirmative not-affected statements (Shai-Hulud and Shai-Hulud 2.0 NPM worm campaigns, Axios package compromise, Vercel/Context.ai April 2026 incident) + publicly accessible Data Processing Addendum incorporating SCC Modules 2 and 3, UK Addendum, and Swiss FADP + AI Services Addendum §5 explicit no-training commitment for any shared model + HIPAA available via Standard add-on ($190/month) or Enterprise inclusion + BYOC zero-access operating model (no SSH / VPN / inbound network access needed by Pinecone) + CMEK GA March 2026 + service accounts and audit logs GA March 2026 + AI Services Addendum §4 prohibits misrepresenting AI Output as human-generated (EU AI Act-referenced contractual stance).

Largest gaps: multi-factor authentication marked "Coming Soon" on security page at evaluation date (SSO via SAML mitigates this for federated identity flows only) + SOC 2 / HIPAA / Pentest reports access-gated through SafeBase Trust Center + AI Services (Pinecone Assistant, Pinecone Inference) by default excluded from BAA scope per AI Services Addendum §7(e) absent separate written agreement + telemetry default collection position not publicly documented (silence-is-data zero) + default-issued API keys carry broad permissions (least-privilege configurable but not default) + BYOC multi-cloud at public preview rather than GA at evaluation date + /legal/subprocessors/ page last-updated 2024-05-24 out of sync with current Trust Center version.

CISA KEV: none. Trailing 12-month CVE count: 0. Trailing 12-month supply-chain compromise: 0 (with four affirmative not-affected disclosures during evaluation window).

## Bias Disclosure

This evaluation uses Claude (Anthropic) as its tooling. Anthropic operates in the AI agent market and may compete with some evaluated vendors. VERDICT discloses this relationship in every report and applies identical evaluation criteria to all platforms regardless of their relationship to Anthropic.