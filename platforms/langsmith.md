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
rank: null
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
