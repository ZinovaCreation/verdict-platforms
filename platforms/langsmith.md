---
name: LangSmith
slug: langsmith
operator: LangChain, Inc.
independence: independent
parent_entity: null
category: LLM Observability
homepage: https://www.langchain.com
github: https://github.com/langchain-ai
evaluation_number: 62
evaluation_type: initial
evaluated_at: '2026-05-12'
evaluator_model: unrecorded
framework_version: v0.3.1-final
layer: '0'
target_version: null
previous_evaluation_date: null
previous_score: null
score: 55
max_score: 85
tier: A
verdict:
  v:
    score: 14
    rating: High
    note: ''
  r:
    score: 9
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
cve_count_12mo: 5
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
- llm-observability
- agent-evaluation
- soc2-type2
- gdpr
- hipaa-enterprise
- us-eu-regions
- self-hosted-enterprise
- public-changelog
- github-security-advisory
- bug-bounty
rank: 5
sources:
- https://www.langchain.com/langsmith
- https://docs.langchain.com/langsmith
- https://trust.langchain.com/
- https://changelog.langchain.com/
- https://www.langchain.com/terms-of-service
- https://www.langchain.com/privacy-policy
- https://github.com/langchain-ai/langsmith-sdk
- https://github.com/langchain-ai/langsmith-sdk/security
- https://status.smith.langchain.com/
- https://eu.status.smith.langchain.com/
finding: 'Commercial observability, evaluation, and deployment platform from LangChain,
  Inc. (San Francisco). SOC 2 Type II attested (extended to LangGraph Platform / LangSmith
  Deployment August 2025). GDPR compliance, HIPAA at Enterprise tier, US and EU regions,
  self-hosted Enterprise on customer-managed Kubernetes. Explicit "no model training
  on customer data" commitment in Pricing FAQ; customer data ownership. SDK MIT-licensed
  (Python `langsmith`, JS `langsmith`); platform backend closed-source. Five distinct
  platform / SDK vulnerabilities disclosed in trailing 12 months: AgentSmith CVSS
  8.8 (Prompt Hub proxy provider URL), CVE-2026-25750 CVSS 8.5 (Studio baseUrl account
  takeover), CVE-2026-25528 CVSS 6.4 (SDK distributed tracing SSRF), CVE-2026-40190
  CVSS 5.6 (lodash prototype pollution), CVE-2026-41182 (streaming-event redaction
  bypass). Three of five share a recurring URL-validation root-cause class across
  distinct surfaces (Prompt Hub / SDK / Studio). Trust Center centralizes compliance
  artifacts but gates access behind authenticated request. LangSmith Sandboxes (microVM-isolated)
  in Private Preview. Independent of Anthropic at every layer (no equity overlap);
  indirect commercial relationship via Claude framework support.'
meta_owner: LangChain, Inc. · San Francisco, CA · Delaware C-corp · Founders Chase
  / Gola · ~$1.1B Series A (Sequoia / Benchmark)
meta_description: 'Independent security evaluation of LangSmith by LangChain, Inc.
  (Delaware C-corp, San Francisco). Score: 55/85. LLM observability + agent evaluation
  platform. SOC 2 Type II + GDPR + HIPAA Enterprise. US/EU regions + self-hosted Enterprise.
  5 CVEs trailing 12 months including URL-validation root-cause pattern across 3 surfaces.
  Framework v0.3.1.'
og_description: 'Independent security evaluation of LangSmith by LangChain, Inc. Score:
  55/85. LLM observability platform. SOC 2 Type II + GDPR. 5 CVEs trailing 12 months.
  URL-validation root-cause pattern. Framework v0.3.1.'
category_line: LLM Observability · Agent Evaluation Platform · Cloud Service · Self-Hosted
  Enterprise Option
display_tags:
- text: SOC 2 II + GDPR + HIPAA Enterprise
  color: safe
- text: US/EU + Self-Hosted Enterprise
  color: safe
- text: 5 CVEs · 12 Months
  color: amber
- text: URL-Validation Recurrence Pattern
  color: amber
key_finding: "Commercial observability, evaluation, and deployment platform from LangChain, Inc. SOC 2 Type II attested (extended to LangGraph Platform / LangSmith Deployment Aug 2025). GDPR compliance, HIPAA at Enterprise tier, US and EU regions, self-hosted Enterprise. Explicit no-training commitment. Five CVEs trailing 12 months: AgentSmith CVSS 8.8, CVE-2026-25750 CVSS 8.5, CVE-2026-25528, CVE-2026-40190, CVE-2026-41182. Three share URL-validation root-cause recurrence pattern across distinct surfaces."
card_owner: "LangChain, Inc. · San Francisco · Sequoia / Benchmark"
card_category: "LLM Observability · Agent Evaluation Platform · Cloud + Self-Hosted Enterprise"
---

# LangSmith

LangSmith is the commercial observability, evaluation, and deployment platform operated by LangChain, Inc. (Delaware C-corporation, San Francisco). The platform ingests trace events from customer LLM and agent applications via SDK or HTTP API, runs dataset-based evaluations, manages versioned prompts, and offers managed deployment for LangGraph agents via LangSmith Deployment. SaaS surfaces are available in US (smith.langchain.com) and EU (eu.smith.langchain.com) regions; a self-hosted Enterprise deployment runs on customer-managed Kubernetes on AWS, GCP, or Azure.

## Layer 0 Score: 55/85 (Tier A)

**V** 14/20 · **R** 9/20 · **D** 11/15 · **I** 8/10 · **C** 6/10 · **T** 7/10

Strongest signals: SOC 2 Type II attestation (extended to LangGraph Platform / LangSmith Deployment August 2025) + GDPR compliance + HIPAA at Enterprise tier + explicit "no model training on customer data" commitment in Pricing FAQ + customer data ownership + EU region availability across all plans + self-hosted Enterprise option for in-customer-environment deployment + public changelog with cadenced release notes + GitHub Security Advisory program with technical detail, SLA, and bug-bounty scope publicly documented + native Human-in-the-loop support in LangGraph runtime + Enterprise identity controls (SAML SSO, SCIM, RBAC, audit logs in OCSF 1.7.0 format).

Largest gaps: five distinct platform / SDK vulnerabilities disclosed in the trailing twelve months (AgentSmith CVSS 8.8 in Prompt Hub, CVE-2026-25750 CVSS 8.5 LangSmith Studio account takeover, CVE-2026-25528 CVSS 6.4 SDK distributed tracing SSRF, CVE-2026-40190 CVSS 5.6 lodash prototype pollution, CVE-2026-41182 streaming-redaction bypass) with three of them sharing a recurring URL-validation root-cause class across separate surfaces (Prompt Hub proxy provider, SDK baggage-header api_url, Studio baseUrl parameter). Trust Center centralizes compliance artifacts (SOC 2 report, subprocessor list, penetration test summaries) but gates access behind authenticated request. LangSmith Sandboxes (microVM-isolated execution surface) is in Private Preview rather than general availability. Tenant isolation specifics for LangSmith Deployment cloud beyond SOC 2 attestation references are not publicly disclosed. No public NIST AI RMF / ISO/IEC 42001 / EU AI Act mapping at evaluation date.

CISA KEV: none. Trailing 12-month CVE count: 5. Trailing 12-month supply-chain compromise: 0.

## Bias Disclosure

This evaluation uses Claude (Anthropic) as its tooling. Anthropic operates in the AI agent market and may compete with some evaluated vendors. VERDICT discloses this relationship in every report and applies identical evaluation criteria to all platforms regardless of their relationship to Anthropic.