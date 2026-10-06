# VERDICT Evaluation #064 — Guardrails AI

| Field | Value |
|-------|-------|
| Evaluation number | #064 |
| Platform | Guardrails AI (open-source Guardrails framework + Guardrails Hub + Guardrails Pro / Snowglobe commercial platform) |
| Evaluation type | Initial (Layer 0) |
| Evaluation date | 2026-05-12 |
| Evaluator | VERDICT Engine v0.3.1 |
| Target version | guardrails-ai 0.10.0 (PyPI), guardrails-api 0.4.2, guardrails-api-client 0.4.0 |
| Framework | VERDICT v0.3.1 |
| Previous evaluation | None |
| Category | AI Safety · LLM Guardrails / Validators · Open-Source Framework + Commercial Cloud Platform (first VERDICT evaluation in this category) |

## Executive Summary

Guardrails AI scores **40/85** (Layer 0, Tier B). The operator is a clearly named, publicly registered Delaware C-corporation (with California foreign-entity registration, principal place of business Menlo Park, CA) operating a publicly available Apache-2.0 framework on GitHub and PyPI alongside a commercial cloud platform (Guardrails Pro, Snowglobe). Resilience scores High (17/20) on the basis of zero confirmed CVEs in the trailing twelve months and one historical isolated arbitrary-code-execution vulnerability (CVE-2024-45858, fixed September 2024) that has aged out of the evaluation window. Data Conduct (1/15, Low) and Containment (3/10, Low) are the principal documented gaps: no publicly accessible Data Processing Addendum, no published sub-processor list, no public statement on AI training use of customer data, and no published Trust Center or compliance attestations (SOC 2, ISO 27001, HIPAA) are visible for the commercial platform surface.

## Scorecard

| Dimension | Score | Max | Rating |
|-----------|------:|----:|--------|
| V — Verifiability | 11 | 20 | Mid |
| R — Resilience | 17 | 20 | High |
| D — Data Conduct | 1 | 15 | Low |
| I — Identity & Control | 4 | 10 | Mid |
| C — Containment | 3 | 10 | Low |
| T — Transparency | 4 | 10 | Mid |
| **Layer 0 Total** | **40** | **85** | **B** |
| E — Effectiveness | — | 15 | Layer 1+ only (not scored) |

**CISA KEV:** None. No Guardrails-AI-assigned CVE appears in the CISA Known Exploited Vulnerabilities catalog as of evaluation date.

---

## Dimension Detail

### V — Verifiability (11/20, Mid)

| Criterion | Result | Score | Evidence |
|-----------|--------|------:|----------|
| Developer / company identity | Corporate registration + official contact both confirmed | 4/4 | California SoS entity 5678079 (incorporated 2023-04-25, 801 El Camino Real, Menlo Park, CA 94025); Tracxn company profile; contact emails `contact@guardrailsai.com`, `security@guardrailsai.com`, `privacy@guardrailsai.com` referenced in disclosure timelines |
| Source code disclosure | Core open-source framework Apache-2.0; commercial Pro / Snowglobe layer closed source | 2/4 | github.com/guardrails-ai/guardrails; PyPI metadata; guardrailsai.com/pro and guardrailsai.com/snowglobe |
| Version management transparency | GitHub Releases active with release notes; PyPI release history complete | 3/3 | github.com/guardrails-ai/guardrails/releases; pypi.org/project/guardrails-ai/#history |
| Third-party dependency disclosure | No public sub-processor list with update date | 0/3 | guardrailsai.com/legal/terms-of-use mentions DPA but no public sub-processor list located |
| Independent certification | No publicly available SOC 2, ISO 27001, HIPAA, or equivalent attestation | 0/4 | No Trust Center page located; no compliance section on guardrailsai.com |
| Functional reproducibility docs | Complete API reference + behavioral specification | 2/2 | guardrailsai.com/docs; validators reference; integration guides |

**Positive findings.** Legal entity named consistently across Terms of Use, GitHub organization, and corporate registration. Apache-2.0 framework is fully open source on GitHub. Documentation site covers installation, validators, integrations, and the Guardrails Hub workflow.

**Recorded concerns.** No public sub-processor list. No independent certification (SOC 2, ISO 27001, HIPAA) publicly visible. Documentation does not include a public boundary diagram delineating which components run in customer infrastructure versus operator-managed infrastructure for the commercial Pro / Snowglobe surfaces.

### R — Resilience (17/20, High)

Trailing 12 months: 2025-05-12 to 2026-05-12.

| Criterion | Result | Score | Evidence |
|-----------|--------|------:|----------|
| CVE count (trailing 12 months) | 0 CVEs assigned to `guardrails-ai` | 5/5 | NVD, OSV (PyPI:`guardrails-ai`), Snyk Vulnerability Database, GitHub Advisories search |
| Maximum CVSS severity | No CVEs in window → maximum severity ≤ 3.9 by absence | 6/6 | Derived from above |
| Patch response speed | Historical CVE-2024-45858 elapsed ~63 days from vendor receipt of formal report (2024-07-16) to fix release v0.5.10 (2024-09-17) | 0/3 | HiddenLayer SAI Security Advisory 2024-09 disclosure timeline |
| Structural issues | Historical CVE pattern not recurring; isolated independent bug | 3/3 | One historical CVE (CVE-2024-45858); no second CVE of same root cause documented |
| Supply chain compromise (trailing 12 months) | No direct compromise of `guardrails-ai` package; dependency-availability disruption (litellm removed from PyPI March 2026) is a downstream operational issue, not a malicious compromise | 3/3 | github.com/guardrails-ai/guardrails-ai issue #5 (2026-03-24) |

**Positive findings.** Zero new CVEs in trailing twelve months. Release cadence remains active (latest stable 0.10.0; Snyk-classified maintenance "Healthy"). Historical CVE-2024-45858 was an isolated `eval`-based code-execution issue in RAIL XML loading, addressed in version 0.5.10 with coordinated public disclosure.

**Recorded concerns.** Historical patch response on CVE-2024-45858 spanned multiple rounds of researcher-initiated contact across multiple administrators before the formal security email channel was used, contributing to the ~63-day elapsed time from first contact to fix. The litellm PyPI removal in March 2026 broke fresh installs of guardrails-ai 0.5.1 and guardrails-api 0.2.1–0.3.2 — a dependency-supply-chain availability event the engine notes neutrally per the supply chain risk check protocol.

### D — Data Conduct (1/15, Low)

| Criterion | Result | Score | Evidence |
|-----------|--------|------:|----------|
| GDPR compliance disclosure | Terms of Use mention DPA exists as separate document, "Applicable Data Protection Laws" defined; no public DPA URL | 1/3 | guardrailsai.com/legal/terms-of-use (clause 2.3 and 1.3) |
| Data minimization | Telemetry default state for commercial platform not publicly documented; framework's local-process execution does not by itself transmit data operator-side | 0/3 | No public telemetry policy located |
| AI training use | No public statement on whether customer data is used for any model training, fine-tuning, or product improvement | 0/4 | "Aggregated Data" defined in ToU clause 1.2 as de-identified statistical use; no statement on AI training specifically |
| Sub-processor transparency | No public sub-processor list | 0/3 | Not located on guardrailsai.com |
| Data retention disclosure | No per-category retention schedule publicly published | 0/2 | ToU permits Customer to export data; no retention period table located |

**Positive findings.** The open-source framework, when used standalone, runs entirely in the customer's process and does not require customer data to leave customer infrastructure (a structural data-minimization property of the framework architecture, distinct from operator-side commercial surfaces).

**Recorded concerns.** Five of five D-dimension public-documentation items fall short of the rubric threshold. Per VERDICT Absolute Rule #10 ("silence is data"), absence of disclosure is scored as zero, with no leniency applied for operator stage. The commercial Pro / Snowglobe surfaces are particularly affected: customer data routed through operator infrastructure (for managed runtime guards, simulation, or LLM-as-judge calls) has no publicly documented retention period, sub-processor inventory, or training-use commitment.

### I — Identity & Control (4/10, Mid)

| Criterion | Result | Score | Evidence |
|-----------|--------|------:|----------|
| Emergency stop documentation | Framework-level `on_fail` actions (`exception`, `fix`, `refrain`, `reask`, `filter`) documented; operator-side emergency stop for commercial platform not documented | 2/4 | guardrailsai.com/docs; validator integration examples |
| Human-in-the-loop design | Programmatic gating via validators is the framework's design pattern; configurable per Guard, not a default-on human review step | 1/3 | Validator and Guard API documentation |
| Permission delegation transparency | Token-based authentication for Guardrails Hub CLI documented; scope and delegation targets for commercial platform not detailed publicly | 1/3 | guardrailsai.com/docs/faq (token / `.guardrailsrc` documentation) |

**Positive findings.** The framework's `on_fail` action vocabulary is well documented and provides clear runtime control surfaces at the validator level. Token-based Hub authentication with token rotation via the Hub UI (`hub.guardrailsai.com/tokens`) is documented.

**Recorded concerns.** No published documentation of SSO / SAML availability, MFA enforcement, RBAC granularity, or scope-of-permission delegation for the commercial platform surface. No published emergency-stop procedure for operator-side managed runtime.

### C — Containment (3/10, Low)

Adapted scoring per evaluation-prompt special context: the open-source framework executes as a Python library in the customer process and does not provide its own sandbox; the commercial cloud platform's operator-side execution surface is the relevant containment-evaluation question.

| Criterion | Result | Score | Evidence |
|-----------|--------|------:|----------|
| Sandbox design | Framework is in-process library; Guardrails Hub validators downloaded as Python packages execute with customer-process privileges; no documented operator-side sandbox for commercial surfaces | 0/4 | github.com/guardrails-ai/guardrails (library architecture); Hub install commands documentation |
| Least privilege | Framework runs with the calling application's existing privileges; no operator-side least-privilege model documented for commercial surfaces | 0/3 | Architecture documentation |
| Tenant isolation (cloud) | Framework is self-hosted by design when used as the OSS library; commercial multi-tenant cloud surface tenancy model not publicly documented; no past cross-tenant breach reported | 3/3 | Self-hosted framework surface qualifies for the rubric's "Self-hosted only: 3 (N/A)" condition |

**Positive findings.** Customers who use only the open-source framework retain full control of the execution boundary. Apache-2.0 licensing permits customer-side auditability of the validator code that will execute in their environment. A Docker hosting guide (`guardrailsai.com/guardrails/docs/how-to-guides/hosting_with_docker`) documents a containerized deployment pattern.

**Recorded concerns.** Guardrails Hub validators, when installed by a customer, execute as Python code in the customer's environment without a Hub-side code-review, code-signing, or sandboxed-execution disclosure publicly visible at the Hub URL. Submission and review process for Hub validators is not publicly documented.

### T — Transparency (4/10, Mid)

| Criterion | Result | Score | Evidence |
|-----------|--------|------:|----------|
| CVE publication posture | Responsible-disclosure policy published; CVE-2024-45858 coordinated with external CNA (HiddenLayer); no own-CNA CVEs issued | 1/2 | guardrailsai.com/blog/commitment-to-responsible-vulnerability |
| Incident disclosure speed | CVE-2024-45858 publicly disclosed within ~1 day of fix release | 2/2 | HiddenLayer advisory timeline (fix 2024-09-17, public disclosure 2024-09-18) |
| Security policy publication | GitHub `SECURITY.md` absent at repository root; equivalent policy published as a blog post | 1/2 | github.com/guardrails-ai/guardrails/security (GitHub UI: "This project has not set up a SECURITY.md file yet"); blog post above |
| AI safety framework reference | No explicit adoption of NIST AI RMF, ISO/IEC 42001, or EU AI Act mapping documented for the operator's own posture | 0/2 | No public framework-adoption page located |
| AI system identity disclosure | No public policy on AI-system identity disclosure (e.g., when LLM-as-judge validators are used or when Snowglobe simulates user personas) | 0/2 | No such policy located |

**Positive findings.** Published responsible-disclosure policy with a dedicated security email (`security@guardrailsai.com`), explicit safe-harbor language for researchers, and a documented engagement workflow. Operator-published blog and changelog cadence is active. Public benchmark publication (Guardrails Index, February 2025) demonstrates a posture of comparative measurement.

**Recorded concerns.** Customer testimonials cited on the operator's website (Robinhood, Masterclass) are independently verifiable in differing degrees. Masterclass usage of Snowglobe is independently confirmed in third-party coverage (MarkTechPost, August 2025), alongside Changi Airport Group, IMDA AI Verify, and Stanford LIFT Lab; Robinhood's usage was not independently verified from customer-side public sources at evaluation date. No publicly visible Trust Center, status page, or operator-published sub-processor list. No formal SECURITY.md file at the GitHub repository root.

---

## Incident Timeline

Within the trailing-twelve-month window (2025-05-12 to 2026-05-12): no public CVEs were confirmed for `guardrails-ai`, `guardrails-api`, `guardrails-api-client`, or other `guardrails-ai/*` GitHub repositories.

Historical reference (outside trailing-12-month scoring window):

| Date | CVE ID | CVSS | Description | Patch status | KEV |
|------|--------|-----:|-------------|--------------|-----|
| 2024-09-18 | CVE-2024-45858 | 7.8 (v3.1 HIGH) / 8.5 (v4 HIGH) | Arbitrary code execution via `eval` in `parse_token` (ValidatorsAttr class) when loading a maliciously crafted RAIL XML file; affects versions 0.2.9–0.5.10 | Fixed in 0.5.10 (2024-09-17, ~63 days from formal vendor receipt of report); CNA: HiddenLayer, Inc. | Not listed |

Dependency-availability event (trailing 12 months): on or before 2026-03-24, the `litellm` PyPI package was removed from the PyPI simple index, breaking fresh installs of `guardrails-ai` versions that pin `litellm<2,>=1.39.3`. The litellm GitHub repository remained active; the operator's documented workaround is to install litellm directly from GitHub. This is recorded neutrally as a dependency availability event rather than a malicious supply-chain compromise.

---

## Contextual Analysis

Guardrails AI occupies an unusual position in this evaluation: the platform under review is itself a provider of containment-like services to LLM applications, while VERDICT (the evaluating party) provides independent evaluation of AI agent and infrastructure platforms. The two operate in adjacent institutional categories within the AI trust infrastructure space; identical evaluation criteria are applied regardless of this adjacency, and the Bias Disclosure (below) records the relevant relationship.

The operator's posture is consistent with an open-source-led project at an early commercial stage. The Apache-2.0 framework, public GitHub organization, named founders, published seed-round investor list, and active release cadence are documentation strengths. The principal documentation gaps cluster in the D dimension (Data Conduct) and the operator-side surfaces of the C dimension (Containment) — specifically: no publicly accessible Data Processing Addendum, sub-processor list, retention schedule, or AI-training-use statement; and no publicly documented sandbox, least-privilege model, or tenant-isolation architecture for the commercial Pro / Snowglobe execution surfaces.

The score reflects what is publicly documented at evaluation date, not the underlying engineering quality. Per VERDICT Absolute Rule #10, absence of disclosure is scored as zero independent of operator stage; the early-stage footprint (post-Seed, ~11 employees) is noted as context for the absence of major compliance attestations but does not modify the scoring.

Behavioral evaluation of validator effectiveness (hallucination detection rate, PII recall, prompt-injection block rate, jailbreak detection) is not within scope at Layer 0 and is deferred to the Future Evaluation Plan.

---

## VERDICT Record

**Summary.** Guardrails AI scores 40/85 (Tier B) at Layer 0: strong Resilience and clear operator identity coupled with documentation gaps in Data Conduct, Containment of operator-side surfaces, and compliance attestation that are characteristic of an early-stage open-source-led AI safety vendor.

**Risk Factor Summary by Use Case.**

| Use case | Risk profile |
|----------|--------------|
| Internal testing / non-production prototyping | Low documented friction. Open-source framework executes in customer environment; Apache-2.0 licensing supports auditability. |
| Credential-handling workflows | Public documentation does not detail credential-handling guarantees for commercial platform surfaces. Customers handling credentials should review the framework's data flow boundaries directly against their own threat model. |
| Cloud multi-tenant workloads | Commercial Pro / Snowglobe tenancy architecture is not publicly documented. Customers operating in multi-tenant configurations should request architecture documentation from the operator before procurement. |
| Regulated-data workloads (HIPAA, GDPR, FedRAMP, similar) | No publicly available SOC 2, ISO 27001, HIPAA, or equivalent attestation located. No public DPA URL; DPA reportedly available through separate contracting. Customers in regulated workloads should request the DPA and compliance evidence directly from the operator. |

**Reference Information** (options, not instructions):

1. The open-source `guardrails-ai` framework (Apache-2.0, github.com/guardrails-ai/guardrails) is the public surface with the most directly auditable behavior. Customers seeking deeper assurance can inspect the framework source, validator implementations, and Hub validator code prior to deployment.
2. For procurement evaluation of the commercial Pro / Snowglobe surfaces, requesting from the operator the DPA, sub-processor list, retention schedule, training-use commitment, and any internal SOC 2 / ISO 27001 readiness documentation directly is one path to filling the documented gaps identified in D and T dimensions.
3. Subscribing to the operator's GitHub Releases and the `security@guardrailsai.com` advisory channel is one path to staying current on framework-level security updates.

**Bias Disclosure.** This evaluation uses Claude (Anthropic) as its tooling. Anthropic operates in the AI agent market and may compete with some evaluated vendors. VERDICT discloses this relationship in every report and applies identical evaluation criteria to all platforms regardless of their relationship to Anthropic.

---

## Future Evaluation Plan

**Layer 1 timing.** Layer 1 behavioral evaluation is appropriate when the operator publishes (or VERDICT independently sources) representative free-tier or open-source-only configurations suitable for 30-run × 4-difficulty testing across hallucination-detection accuracy, PII recall, prompt-injection block rate, and jailbreak-detection block rate. Estimated Layer 1 readiness: when at least three validator categories (PII, jailbreak, hallucination) have a public free-tier behavioral baseline against published benchmarks. Tentative target window: H2 2026.

**Layer C monitoring cadence.** Monthly: NVD / OSV / GHSA / Snyk monitoring for `guardrails-ai`, `guardrails-api`, `guardrails-api-client`, `guardrails-hub-*` PyPI namespace, and `guardrails-ai/*` GitHub organization. CISA KEV continuous monitoring for any CVE involving the package. Trigger conditions per ENGINE.md §Re-evaluation triggers.

**Routine re-evaluation.** 90 days from evaluation date (2026-08-10) for a delta review of V, R, T dimensions.

---

**Framework version:** VERDICT v0.3.1
**Evaluation status:** Delivered.
