---
slug: langsmith
title: LangSmith
score: 55
tier: A
tier_engine: B
tier_override_rationale: |
  ENGINE.md `## Tier Letter Assignment` thresholds (codified 2026-04-29, commit bd8cf2b)
  per Operations Override Rules in QA.md.
  Score 55 ∈ A band [55-64]. Engine output Tier=B was informational; Operations applied
  threshold-derived Tier=A as the canonical assignment.
  Precedent in current evaluation cycle: AWS Bedrock Agents (55 = A), Mistral La Plateforme (#061, 55 = A).
category: LLM Observability
subcategory: Agent Evaluation Platform · Cloud Service · Self-Hosted Enterprise Option
license: Closed-source platform; LangSmith SDK (Python `langsmith`, JS `langsmith`) MIT-licensed
operator: LangChain, Inc.
operator_jurisdiction: San Francisco, California, United States (Delaware C-corporation)
founders: Harrison Chase (CEO), Ankush Gola
funding: ~$1.1B post-money valuation (Series A co-lead Sequoia Capital, Feb 2024); prior Series A lead Benchmark, April 2023
major_investors: Benchmark, Sequoia Capital, Conviction, Lux Capital, Cowboy Ventures
evaluation_date: 2026-05-12
evaluation_number: 062
framework_version: VERDICT v0.3.1
layer: 0
independence: ✅ Independent (no Anthropic / Anthropic Ventures equity overlap per public investor records)
anthropic_relationship: |
  Indirect commercial. LangChain Inc.'s products (LangChain framework, LangGraph, LangSmith)
  support Anthropic Claude as a first-class LLM provider; LangChain derives commercial value
  from this support, and Anthropic derives commercial value from LangChain framework adoption.
  No equity relationship exists per public investor records.
dimensions:
  V: { score: 14, max: 20, rating: High }
  E: { score: 0,  max: 15, rating: NotEvaluated, note: "Layer 1+ only" }
  R: { score: 9,  max: 20, rating: Mid }
  D: { score: 11, max: 15, rating: High }
  I: { score: 8,  max: 10, rating: High }
  C: { score: 6,  max: 10, rating: Mid }
  T: { score: 7,  max: 10, rating: High }
total: 55
max: 85
percentage: 65
cisa_kev: false
cve_count_12mo: 5
supply_chain_compromise_12mo: 0
acquisition: None applicable.
ecosystem_context: |
  Same-operator ecosystem: LangChain framework (Agent Framework, prior evaluation #025) and
  LangGraph orchestration library (Agent Orchestration, prior evaluation #035) are operated by
  LangChain, Inc. LangSmith is the operator's commercial observability platform.
  Same-category prior evaluation: LangFuse (#060, Tier A, score 62/85).
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
incident_tags:
  - 5-cve-12mo
  - url-validation-root-cause-pattern
  - no-kev
  - supply-chain-clean
  - patch-response-8-days
  - private-preview-microvm-sandbox
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
evaluation_url: https://github.com/ZinovaCreation/verdict-platforms/blob/main/evaluations/062_langsmith.md
---

# LangSmith

LangSmith is the commercial observability, evaluation, and deployment platform operated by LangChain, Inc. (Delaware C-corporation, San Francisco). The platform ingests trace events from customer LLM and agent applications via SDK or HTTP API, runs dataset-based evaluations, manages versioned prompts, and offers managed deployment for LangGraph agents via LangSmith Deployment. SaaS surfaces are available in US (smith.langchain.com) and EU (eu.smith.langchain.com) regions; a self-hosted Enterprise deployment runs on customer-managed Kubernetes on AWS, GCP, or Azure.

## Layer 0 Score: 55/85 (Tier A)

**V** 14/20 · **R** 9/20 · **D** 11/15 · **I** 8/10 · **C** 6/10 · **T** 7/10

Strongest signals: SOC 2 Type II attestation (extended to LangGraph Platform / LangSmith Deployment August 2025) + GDPR compliance + HIPAA at Enterprise tier + explicit "no model training on customer data" commitment in Pricing FAQ + customer data ownership + EU region availability across all plans + self-hosted Enterprise option for in-customer-environment deployment + public changelog with cadenced release notes + GitHub Security Advisory program with technical detail, SLA, and bug-bounty scope publicly documented + native Human-in-the-loop support in LangGraph runtime + Enterprise identity controls (SAML SSO, SCIM, RBAC, audit logs in OCSF 1.7.0 format).

Largest gaps: five distinct platform / SDK vulnerabilities disclosed in the trailing twelve months (AgentSmith CVSS 8.8 in Prompt Hub, CVE-2026-25750 CVSS 8.5 LangSmith Studio account takeover, CVE-2026-25528 CVSS 6.4 SDK distributed tracing SSRF, CVE-2026-40190 CVSS 5.6 lodash prototype pollution, CVE-2026-41182 streaming-redaction bypass) with three of them sharing a recurring URL-validation root-cause class across separate surfaces (Prompt Hub proxy provider, SDK baggage-header api_url, Studio baseUrl parameter). Trust Center centralizes compliance artifacts (SOC 2 report, subprocessor list, penetration test summaries) but gates access behind authenticated request. LangSmith Sandboxes (microVM-isolated execution surface) is in Private Preview rather than general availability. Tenant isolation specifics for LangSmith Deployment cloud beyond SOC 2 attestation references are not publicly disclosed. No public NIST AI RMF / ISO/IEC 42001 / EU AI Act mapping at evaluation date.

CISA KEV: none. Trailing 12-month CVE count: 5. Trailing 12-month supply-chain compromise: 0.
