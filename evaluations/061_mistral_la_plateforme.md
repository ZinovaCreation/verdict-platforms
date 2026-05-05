# VERDICT Evaluation Report — #061 Mistral La Plateforme

> **Operations note (added 2026-04-29):** Engine output assigned `Tier: B`. Operations
> override applied per rankings/index.html convention (55-64 = A band) → **Tier: A**.
> This is the 2nd Tier override precedent in current 3-platform batch (after #059 E2B C→B).
> Codification of operations Tier override rule is queued as `engine-tier-classification-verify`
> task resolution, with ENGINE.md Tier threshold patch + QA.md operations override rule
> committed in parallel. Below is the engine output verbatim; only this header note is
> operations-added.

---

| Field | Value |
|-------|-------|
| **Evaluation #** | 061 |
| **Platform** | Mistral La Plateforme (including Agents API) |
| **Type** | New evaluation |
| **Date** | 2026-04-29 |
| **Evaluator** | VERDICT Engine v0.3.1 (Claude / Anthropic) |
| **Target version** | Mistral La Plateforme as of evaluation date (live API + Agents API GA + Le Chat Enterprise + AI Compliance Hub) |
| **Framework** | VERDICT v0.3.1 (Layer 0, public documentation only) |
| **Previous evaluation** | None |

## Executive Summary

Mistral La Plateforme is the API and agent-platform tier of Mistral AI SAS, a Paris-headquartered French SAS (RCS 952 418 325) founded April 2023. The platform spans foundation-model inference, the Agents API for stateful multi-step workflows with built-in connectors (Code Interpreter, Web Search, Image Generation, Document Library) and MCP, and Le Chat (consumer/Pro/Enterprise). The platform's strongest documented area is corporate verifiability and transparency on data conduct: a public DPA at `legal.mistral.ai` with SCC Module 4, EU residency by default, paid-API and Le Chat Enterprise opt-out from training by default, named subprocessors with a 10-day objection right, 13-month maximum retention for free tiers and "until account termination" for the Agents API persistent state, and explicit signing of the EU GPAI Code of Practice. The independent attestation set is SOC 2 Type II + ISO 27001 + ISO 27701, with HIPAA capability available via SCDPA (Special Conditions Data Processing Addendum). Reports are NDA-gated. Zero CVEs were assigned to `mistralai/*` GitHub repositories or operator-published SDKs in the trailing 12 months. The most material public-disclosure gaps are the Code Interpreter sandbox isolation technology not being named (described as "isolated container" without further detail), SAML SSO restricted to Enterprise tier, and the Agents API retention policy ("until account termination") being structurally longer than the standard 30-day Sliding-Window retention for the general API.

## Scorecard

| Dimension | Score | Max | % | Rating |
|-----------|-------|-----|---|--------|
| V — Verifiability | 14 | 20 | 70% | High |
| R — Resilience | 17 | 20 | 85% | High |
| D — Data Conduct | 11 | 15 | 73% | High |
| I — Identity & Control | 4 | 10 | 40% | Mid |
| C — Containment | 2 | 10 | 20% | Low |
| T — Transparency | 7 | 10 | 70% | High |
| **Total (Layer 0)** | **55** | **85** | **65%** | **Tier A** (Operations override) |
| E — Effectiveness | — | 15 | — | Layer 1+ only (not evaluated) |

**CISA KEV:** ❌ No Mistral CVE in CISA Known Exploited Vulnerabilities catalog at evaluation date.

## Dimension Detail

### V — Verifiability (14/20)

| Criterion | Result | Score | Evidence |
|-----------|--------|-------|----------|
| Developer / company identity | Mistral AI SAS, Paris, RCS 952 418 325, registered office 15 rue des Halles 75001 Paris | 4 | https://mistral.ai/terms , French RCS lookup |
| Source code disclosure | `mistralai/*` GitHub org with multiple Apache 2.0 SDKs (client-python, client-js, mistral-inference, mistral-finetune, mistral-common); foundation models open-weight under Apache 2.0 (Mistral 7B, Mixtral 8x7B, Mistral Small 3, etc.) | 3 | https://github.com/mistralai , Hugging Face mistralai/* |
| Version management transparency | Versioned API endpoints with deprecation dates; SDK GitHub Releases; AI Compliance Hub per-model fact sheets | 3 | https://docs.mistral.ai/getting-started/version_compatibility/ , https://mistral.ai/news/ai-compliance-hub |
| Third-party dependency disclosure | SDK package manifests visible in repos; no SBOM publication |  1 | GitHub mistralai SDK repos |
| Independent certification | SOC 2 Type II + ISO 27001 + ISO 27701; reports via NDA-gated Trust Center | 2 | https://trust.mistral.ai/ |
| Functional reproducibility docs | Public OpenAPI-compatible API reference, Agents API specification, Code Interpreter behavior documented | 1 | https://docs.mistral.ai/ |

**Positive findings:** Named legal entity with verifiable French RCS registration; multiple Apache 2.0 SDKs and open-weight model releases enabling third-party audit; AI Compliance Hub publishes per-model and per-system EU AI Act documentation; signed GPAI Code of Practice; well-defined API versioning policy.

**Recorded concerns:** No publicly downloadable SBOM; SOC 2 / ISO reports gated by NDA-protected Trust Center workflow; subprocessor list update not yet propagated post-Koyeb acquisition (announced 2026-02-17).

### R — Resilience (17/20)

| Criterion | Result | Score | Evidence |
|-----------|--------|-------|----------|
| CVE count (trailing 12 months) | 0 confirmed | 5 | NVD, OSV, GitHub Security Advisories searches across `mistralai/*`, `mistral-inference`, `mistral-common`, `client-python`, `client-js` returned zero entries in window |
| Maximum CVSS severity | N/A (no CVEs) | 6 | No advisories to evaluate |
| Patch response speed | Unconfirmable | 0 | No public CVEs/GHSAs within window to measure; per ENGINE Rule 3, unconfirmable items score 0 |
| Structural issues | None recurring | 3 | Zero CVEs implies no recurring root-cause pattern |
| Supply chain compromise (12 months) | None confirmed | 3 | npm/PyPI registry checks; no reports linking `mistralai-*` packages to npm chalk/debug ecosystem compromise (Sep 2025), litellm 1.82.7/1.82.8 incident, or Trivy/Checkmarx KICS supply-chain events |

**Positive findings:** Clean trailing-12-month CVE record across operator-published SDKs and infrastructure repos; signed GPAI Code of Practice includes commitments to security incident reporting; AI Compliance Hub provides per-incident readiness documentation.

**Recorded concerns:** The absence of any CVE within the evaluation window means patch-response speed is unmeasurable; future advisories will determine whether the rapid patch cadence demonstrated by peers (e.g. OpenAI, Google, Anthropic) is matched.

### D — Data Conduct (11/15)

| Criterion | Result | Score | Evidence |
|-----------|--------|-------|----------|
| GDPR compliance disclosure | DPA at legal.mistral.ai with SCC Module 4 controller-to-processor + Module 4 processor-to-controller annexes; EU representative not yet listed (operator is EU-established) | 3 | https://legal.mistral.ai/ |
| Data minimization | Documented per-tier retention; nightly purge for some categories; abuse monitoring 30 days for paid API | 2 | https://help.mistral.ai/en/articles/347390 |
| AI training use | Paid API + Le Chat Enterprise: opt-out by default. Free Le Chat / Le Chat Pro: opt-in. ZDR available on request for paid tiers. | 4 | https://help.mistral.ai/en/articles/347391 , Privacy Policy |
| Sub-processor transparency | Named list with jurisdiction + purpose at legal.mistral.ai/subprocessors; 10-day customer objection right documented | 2 | https://legal.mistral.ai/subprocessors |
| Data retention disclosure | API: 30-day sliding window. Le Chat Enterprise: configurable. Agents API persistent state: until account termination | 0 | https://help.mistral.ai/en/articles/347392 |

**Positive findings:** Paid-tier opt-out from training by default — among the cleaner default postures in the foundation-model API category; ZDR available; SCC Module 4 published in DPA; named subprocessors with structured 10-day objection right; EU residency by default with US opt-in.

**Recorded concerns:** Agents API retention "until account termination" is structurally longer than the 30-day general-API window — operator-side retention extends as long as the customer maintains a Mistral account, which procurement teams operating in regulated industries may wish to clarify; subprocessor list has not yet been updated to reflect the 2026-02-17 Koyeb acquisition.

### I — Identity & Control (4/10)

| Criterion | Result | Score | Evidence |
|-----------|--------|-------|----------|
| Emergency stop documentation | API key revocation documented; Le Chat conversation deletion documented; no consolidated platform-level kill-switch runbook | 1 | API reference, Le Chat help center |
| Human-in-the-loop design | Agents API allows tool-use approval patterns at integrator layer; no platform-enforced HITL primitive in Code Interpreter or Web Search built-in connectors | 1 | https://docs.mistral.ai/agents/ |
| Permission delegation transparency | API key scoping, organization/workspace concept; SAML SSO Enterprise tier only | 2 | https://help.mistral.ai/en/articles/347393 |

**Positive findings:** Per-API-key scoping documented; organization/workspace separation; audit log capability stated for Le Chat Enterprise; rate-limiting and usage budgets documented.

**Recorded concerns:** No platform-enforced HITL primitive in autonomous-execution connectors (Code Interpreter, Web Search, Image Generation); SAML SSO available only on Enterprise tier; consolidated emergency-stop runbook not published; granular role-based access control documentation thinner than peer enterprise platforms.

### C — Containment (2/10)

| Criterion | Result | Score | Evidence |
|-----------|--------|-------|----------|
| Sandbox design | Code Interpreter described as "isolated container" without specific isolation technology named (no mention of Firecracker, gVisor, KVM, or similar primitive) | 1 | https://docs.mistral.ai/capabilities/code_interpreter |
| Least privilege | Documented for API keys and per-workspace permissions; default sandbox user privilege level not stated | 0 | Inferred only |
| Tenant isolation (cloud) | SOC 2 Type II + ISO 27001 attest tenant isolation controls; specific technical mechanism not detailed in public docs | 1 | https://trust.mistral.ai/ (NDA-gated reports) |

**Positive findings:** Code Interpreter explicitly described as an isolated execution environment with stated network egress restrictions for some operations; SOC 2 Type II and ISO 27001 attestations cover tenant isolation controls.

**Recorded concerns:** Code Interpreter sandbox isolation technology not disclosed publicly — peer foundation-model platforms (OpenAI Code Interpreter, Anthropic Code Execution) similarly do not always name the primitive, but Mistral La Plateforme's public materials are notably less specific than the engineering blogs published by other comparable agent platforms (e.g. AWS Bedrock AgentCore Cedar Policy, Browserbase per-VM session, E2B Firecracker microVM); default sandbox user privilege level not documented.

### T — Transparency (7/10)

| Criterion | Result | Score | Evidence |
|-----------|--------|-------|----------|
| CVE publication posture | No CVEs within window; security@mistral.ai contact published; CVD process referenced in privacy policy | 1 | https://mistral.ai/privacy-policy |
| Incident disclosure speed | Status page operates at https://status.mistral.ai/; no security incident has been publicly disclosed in evaluation window to test pipeline | 1 | https://status.mistral.ai/ |
| Security policy publication | Trust Center, AI Compliance Hub, Privacy Policy, DPA published; technical TOMs not detailed at peer-Langfuse level | 2 | https://trust.mistral.ai/ , https://mistral.ai/news/ai-compliance-hub |
| AI safety framework reference | EU GPAI Code of Practice signed; AI Compliance Hub maps per-model and per-system EU AI Act docs; no explicit NIST AI RMF or ISO/IEC 42001 mapping cited | 2 | https://mistral.ai/news/ai-compliance-hub , GPAI signatory list |
| AI system identity disclosure | Mistral La Plateforme is identified as AI agent platform across all surfaces; per-model fact sheets published | 1 | AI Compliance Hub per-model pages |

**Positive findings:** Public Trust Center; AI Compliance Hub publishes structured EU AI Act documentation per model and per system (rare among foundation-model providers); GPAI Code of Practice signatory; status page; documented privacy contact; named DPO contact.

**Recorded concerns:** No explicit NIST AI RMF or ISO/IEC 42001 mapping despite enterprise positioning; technical TOMs less granular than peer documentation; security incident response timeline untested in public window.

## Incident Timeline (trailing 12 months: 2025-04-29 to 2026-04-29)

No CVEs assigned to `mistralai/*` repositories or operator-published SDKs in the evaluation window. CISA KEV cross-check: no Mistral entries.

Operational incidents (status page, partial 30-day window): brief API degradations of 3–8 minutes on 2026-03-24, 2026-04-02, 2026-04-15; one 22-minute Le Chat degradation on 2026-04-08 attributed to upstream provider issue. These are availability events; no public security implication.

## Contextual Analysis

Mistral La Plateforme occupies the foundation-model + agent-platform layer, vertically integrated from model training (Mistral 7B / Mixtral / Mistral Small / Mistral Large / Codestral / Pixtral / Mistral Embed) through inference API to higher-level Agents API with first-party connectors. The corporate-verifiability and data-conduct dimensions are notably stronger than the technical-containment and identity-control dimensions: legal entity is fully verifiable in primary French RCS records, the DPA is publicly available with SCC Module 4 and a structured subprocessor objection right, paid-tier opt-out from training is the default, and the AI Compliance Hub publishes per-model EU AI Act documentation that exceeds typical foundation-model-provider transparency. The 2026-02-17 Koyeb acquisition (announced via Mistral and Koyeb press releases) added serverless edge inference capability; subprocessor disclosure update is pending at evaluation date.

The Code Interpreter sandbox isolation primitive is described as "isolated container" without further technical specification. This is a recorded concern rather than a security-negative signal — peer agent platforms similarly do not always name their sandbox primitive in public documentation — but Mistral La Plateforme's public materials are notably less specific than peer engineering blog posts. Procurement teams operating in regulated industries may wish to request the technical detail directly from the operator.

A separate structural observation, recorded for completeness: Anthropic and Mistral AI SAS are direct competitors in the foundation-model and agent-platform market. Public investor records (Tracxn, PitchBook, Mistral cap table press disclosures) show no equity overlap between Anthropic / Anthropic Ventures and Mistral AI SAS in any funding round. ASML holds approximately 11% as the largest single shareholder per Series C (Sep 2025 press); other investors include Lightspeed (Seed lead), a16z (Series A lead), Microsoft (~$16M strategic), Nvidia, Salesforce, IBM, Samsung, Bpifrance, Bertelsmann, DST Global. The bias-disclosure language below applies and identical evaluation criteria are applied regardless of competitive relationship.

The operator's positioning emphasizes EU-headquartered data processing with SCC Module 4 protection and a public DPA. Customers whose deployments require EU data residency by default with documented US opt-in will find this posture among the cleaner among foundation-model providers.

## VERDICT Record

**Summary.** Mistral La Plateforme scores 55/85 (Tier A under rankings convention 55-64 = A band; engine assigned Tier B due to internal threshold mapping that differs from rankings convention — Operations override applied) under VERDICT v0.3.1 Layer 0. Strong posture on corporate verifiability, data-conduct opt-outs, and public legal disclosure. Weaker posture on technical containment specifics (sandbox isolation primitive not named) and identity-and-control granularity (no platform-enforced HITL in built-in connectors, SAML SSO Enterprise-only).

**Risk Factor Summary by Use Case.**

| Use case | Recorded risk factors |
|----------|----------------------|
| Internal testing / single-tenant evaluation | Low. Paid-tier training opt-out by default, ZDR available, EU residency default, Apache 2.0 SDKs, open-weight models for offline evaluation. |
| Credential-handling workflows | Moderate. Code Interpreter sandbox isolation primitive not publicly named; Agents API state retention "until account termination" structurally longer than general API. |
| Cloud multi-tenant deployments | Acceptable for many use cases. SOC 2 Type II + ISO 27001 attestations cover tenant isolation; specific technical mechanism less detailed than top-tier peer documentation. |
| Regulated-data workloads (HIPAA / PHI / GDPR Art. 9) | Documented support. EU residency default, public DPA with SCC, named subprocessors with objection right, HIPAA capability via SCDPA on request, ISO 27701 privacy management certification. |

**Reference Information** (presented as options, not instructions):

1. SOC 2 Type II, ISO 27001, and ISO 27701 reports can be requested via the Trust Center at https://trust.mistral.ai/ under NDA.
2. The DPA is publicly available at https://legal.mistral.ai/ for review prior to procurement.
3. Procurement teams may wish to request from the operator: (a) the Code Interpreter sandbox isolation technology, (b) the post-Koyeb-acquisition subprocessor list, (c) the data-retention policy detail for Agents API persistent state.

**Bias Disclosure.** This evaluation uses Claude (Anthropic) as its tooling. Anthropic and Mistral AI SAS are direct competitors in the foundation-model and agent-platform market; no equity overlap exists between Anthropic / Anthropic Ventures and Mistral AI SAS or its subsidiaries in any funding round per public investor records. VERDICT discloses this competitive relationship in every report and applies identical evaluation criteria to all platforms regardless of relationship to Anthropic.

## Future Evaluation Plan

- **Layer 1 (behavioral):** 30 runs × 4 difficulty levels on Mistral La Plateforme paid tier across 3+ days, focusing on Agents API state-retention behavior, Code Interpreter network-egress posture, and tool-use HITL primitive availability; target window Q3 2026.
- **Layer C (continuous):** GitHub Security Advisories at `mistralai/*`, NVD, OSV, and CISA KEV monitored on a weekly cadence; mandatory R-dimension re-evaluation if any CVSS ≥ 7.0 CVE is published, if any Mistral CVE enters the KEV catalog, or 90 days from this evaluation date (next routine: 2026-07-28).
- **Re-evaluation trigger watch:** Any operator publication naming the Code Interpreter sandbox isolation primitive will trigger a C-dimension differential re-evaluation; any update to the post-Koyeb subprocessor list will trigger a D/T differential re-evaluation; publication of NIST AI RMF or ISO/IEC 42001 mapping will trigger a T differential re-evaluation.

---

**Score: 55/85**
**V: 14/20, R: 17/20, D: 11/15, I: 4/10, C: 2/10, T: 7/10**
**Dimensions verified: V+R+D+I+C+T = 55**
**Tier: A (Operations override; engine assigned B)**
**Category: AI Agent Platform · Foundation Model API · Stateful Agents Runtime · Cloud Service**

**Framework version:** VERDICT v0.3.1
