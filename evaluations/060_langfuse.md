# VERDICT Evaluation Report — #060 Langfuse

> **Operations note (added 2026-04-29):** Engine output assigned `Tier: A` (62/85, 55-64 = A band).
> Operations confirmed; no override required. Anthropic-relationship surface (parent ClickHouse customer) disclosed neutrally in Contextual Analysis. Below is the engine output verbatim; only this header note is operations-added.

---

| Field | Value |
|-------|-------|
| **Evaluation #** | 060 |
| **Platform** | Langfuse |
| **Type** | New evaluation |
| **Date** | 2026-04-29 |
| **Evaluator** | VERDICT Engine v0.3.1 (Claude / Anthropic) |
| **Target version** | Self-hosted ≥ v3.167.0 (latest at evaluation date); Langfuse Cloud (US, EU, HIPAA regions) |
| **Framework** | VERDICT v0.3.1 (Layer 0, public documentation only) |
| **Previous evaluation** | None |

## Executive Summary

Langfuse is an open-source LLM engineering platform under MIT license for the core, with a separately licensed Enterprise Edition (`ee/`) for SCIM, project-level RBAC, and extended audit log retention. Public compliance posture is among the more complete in the LLM observability category: SOC 2 Type II (NDA-gated), ISO 27001, HIPAA region, GDPR with self-serve DPA, named subprocessors, documented penetration testing cadence, 72-hour breach notification SLA, explicit no-AI-training commitment for client data, and configurable data retention from ≥3 days to unlimited with nightly purge. Six CVEs were published in the trailing 12 months (2025-04-29 to 2026-04-29), maximum CVSS 7.6 (CVE-2025-59305, background-migration improper authorization, same-day patch); none are listed in the CISA KEV catalog. Patch response is rapid — most reported issues were patched on the same day or within 24 hours of disclosure on Langfuse Cloud, with parallel OSS releases. The most material public-disclosure gap as of the evaluation date is that the operator entity statements on the public security pages still reference "Langfuse GmbH / Finto Technologies Inc." in the footer and "Finto Technologies Inc., 100% parent company" on the subprocessors page, while the ClickHouse, Inc. acquisition (announced 2026-01-16) is reflected in the press section and a top-of-page banner but has not yet propagated to the legal-entity disclosures, DPA operator naming, or subprocessors page.

## Scorecard

| Dimension | Score | Max | % | Rating |
|-----------|-------|-----|---|--------|
| V — Verifiability | 14 | 20 | 70% | High |
| R — Resilience | 12 | 20 | 60% | Mid |
| D — Data Conduct | 11 | 15 | 73% | High |
| I — Identity & Control | 8 | 10 | 80% | High |
| C — Containment | 8 | 10 | 80% | High |
| T — Transparency | 9 | 10 | 90% | High |
| **Total (Layer 0)** | **62** | **85** | **73%** | **Tier A** |
| E — Effectiveness | — | 15 | — | Layer 1+ only (not evaluated) |

**CISA KEV:** ❌ No Langfuse CVE present in the CISA Known Exploited Vulnerabilities catalog at evaluation date.

## Dimension Detail

### V — Verifiability (14/20)

| Criterion | Result | Score | Evidence |
|-----------|--------|-------|----------|
| Developer / company identity | Langfuse GmbH (Berlin), subsidiary of Finto Technologies Inc. (San Francisco) per subprocessors page; security@/privacy@/compliance@langfuse.com contacts | 4 | https://langfuse.com/security/subprocessors , https://langfuse.com/security |
| Source code disclosure | MIT license for core; `ee/` directory under separate Enterprise license | 2 | https://github.com/langfuse/langfuse , https://langfuse.com/docs/open-source |
| Version management transparency | GitHub Releases + langfuse.com/changelog with multiple-per-week cadence | 3 | https://github.com/langfuse/langfuse/releases , https://langfuse.com/changelog |
| Third-party dependency disclosure | Dependencies page links to package manifests; license-check policy stated; no SBOM with explicit update date | 1 | https://langfuse.com/security/dependencies |
| Independent certification | SOC 2 Type II + ISO 27001 + HIPAA referenced; reports available via NDA-gated request flow | 2 | https://langfuse.com/request-security-docs , https://langfuse.com/security/soc2 |
| Functional reproducibility docs | Public API reference, OpenTelemetry compatibility, behavioral docs | 2 | https://langfuse.com/docs/api-and-data-platform/overview |

**Positive findings:** Open-core boundary inspectable in repository (`ee/LICENSE` separate from MIT root); three certification tracks (SOC 2 Type II, ISO 27001, HIPAA); dedicated security/privacy/compliance contact addresses; comprehensive public security center with thirteen distinct topic pages.

**Recorded concerns:** Operator-naming on legal pages has not yet been updated to reflect the 2026-01-16 ClickHouse, Inc. acquisition (footer and subprocessors page still cite Finto Technologies Inc. as 100% parent); SOC 2 Type II report is NDA-gated rather than publicly downloadable; subprocessors list lacks an explicit "last updated" date.

### R — Resilience (12/20)

| Criterion | Result | Score | Evidence |
|-----------|--------|-------|----------|
| CVE count (trailing 12 months) | 6 CVEs (2025-04-29 to 2026-04-29) | 1 | NVD, GitHub Security Advisories |
| Maximum CVSS severity | 7.6 (CVE-2025-59305) | 2 | https://nvd.nist.gov/vuln/detail/CVE-2025-59305 |
| Patch response speed | 5 of 6 patched within 24 hours of disclosure; 1 case (CVE-2026-41487) took 9 days due to initial triage misclassification, then 1 day after re-triage | 3 | GHSA timelines per advisory pages |
| Structural issues | Multiple authorization-control bugs across distinct components and code paths; treated as independent bugs rather than a single recurring root cause | 3 | Per-CVE technical analyses |
| Supply chain compromise (12 months) | None confirmed for `langfuse` npm/PyPI/Docker packages | 3 | npm/PyPI registries, GitHub Releases |

**Positive findings:** Median time-to-patch is same-day on Langfuse Cloud; OSS patch releases shipped in parallel; operator publishes detailed disclosure timelines on each advisory; access-log review documented for each Cloud-relevant issue; no Langfuse entry in the CISA KEV catalog; no supply-chain compromise of Langfuse packages identified in the trailing 12 months.

**Recorded concerns:** Six CVEs in trailing 12 months places Langfuse in the 6–9 band (1 point); maximum CVSS in the 7.0–8.9 band; four of the six CVEs are categorized under CWE-284 (Improper Access Control) and surfaced in distinct subsystems (Slack OAuth install, project membership APIs, background migration, LLM connection update); CVE-2025-9799 (SSRF via prompt webhook) was assigned via a third-party CNA route rather than the maintainer-published GHSA channel.

### D — Data Conduct (11/15)

| Criterion | Result | Score | Evidence |
|-----------|--------|-------|----------|
| GDPR compliance disclosure | DPA self-serve, GDPR page, Article 28 scope documented | 3 | https://langfuse.com/security/dpa , https://langfuse.com/security/gdpr |
| Data minimization | Self-hosted PostHog telemetry default-on with documented opt-out; aggregated metrics only | 1 | Telemetry documentation referenced from GitHub README |
| AI training use | Privacy FAQ explicit "No. Langfuse does not train or fine-tunes ML/LLM models on Client Data"; retention policy stated | 4 | https://langfuse.com/security/privacy-faq |
| Sub-processor transparency | List by name + jurisdiction + purpose; no last-updated date visible on the public page | 1 | https://langfuse.com/security/subprocessors |
| Data retention disclosure | Per-project policy: ≥ 3 days to unlimited, purged nightly; 30-day deletion post-termination | 2 | https://langfuse.com/security/privacy-faq , https://langfuse.com/docs/data-retention |

**Positive findings:** Three deployment regions with distinct subprocessor sets (US, EU, HIPAA); HIPAA region restricts PHI processing to AWS + ClickHouse Inc. only; self-serve DPA, BAA available on entitled plans; explicit no-AI-training commitment in the Privacy FAQ; configurable per-project retention windows; granular deletion APIs.

**Recorded concerns:** Subprocessors list does not display a last-updated date; PostHog telemetry default-on for self-hosted (mitigated by documented opt-out and aggregated-only contents); ClickHouse, Inc. is not yet named as a subprocessor or controller on the public privacy pages despite the 2026-01-16 acquisition.

### I — Identity & Control (8/10)

| Criterion | Result | Score | Evidence |
|-----------|--------|-------|----------|
| Emergency stop documentation | Data deletion via UI + API for traces, projects, organizations; audit logs available; no single dedicated "emergency stop" runbook published | 2 | https://langfuse.com/docs/data-deletion |
| Human-in-the-loop design | Platform is observation-only; all data consumption is by humans through the UI or API; no autonomous outbound actions other than configurable webhooks/Slack | 3 | Product overview |
| Permission delegation transparency | RBAC documented; project-level RBAC and SCIM provisioning gated to Enterprise Edition; API key scoping documented | 3 | https://langfuse.com/docs/rbac , https://langfuse.com/security/auth |

**Positive findings:** Granular delete operations exposed in both the UI and the public API; audit log feature documented; OAuth/SAML SSO via Auth.js providers; PKCE+state checks documented after CVE-2025-65107.

**Recorded concerns:** No single consolidated "emergency stop" or "kill-switch" runbook is published; project-level RBAC and SCIM are EE-gated.

### C — Containment (8/10)

| Criterion | Result | Score | Evidence |
|-----------|--------|-------|----------|
| Sandbox design (data-plane analog) | Logical separation at database and API layers documented; no code-execution sandbox needed (platform does not execute customer code) | 2 | https://langfuse.com/security/privacy-faq |
| Least privilege | Default project-scoped API keys; production access disabled by default for personnel | 3 | https://langfuse.com/security/privacy-faq , TOMs |
| Tenant isolation (cloud) | Multi-tenant isolation enforced via SOC 2 Type II + ISO 27001 attested controls; HIPAA region narrows subprocessor scope | 3 | SOC 2 Type II report (NDA), ISO 27001 certificate (NDA) |

**Positive findings:** Air-gapped self-host explicitly supported; HIPAA region segregates PHI processing to a minimal subprocessor set; encryption at rest stated; logical separation enforced at database and API layers.

**Recorded concerns:** Three of the six trailing-12-month CVEs (CVE-2025-64504 cross-organization member enumeration, CVE-2026-24055 unauthenticated Slack install, CVE-2026-41487 LLM-connection credential exposure) involve cross-tenant or cross-project boundary issues.

### T — Transparency (9/10)

| Criterion | Result | Score | Evidence |
|-----------|--------|-------|----------|
| CVE publication posture | Maintainer-issued GHSA advisories with detailed timelines; CVEs assigned for each | 2 | https://github.com/langfuse/langfuse/security/advisories |
| Incident disclosure speed | 72-hour breach notification SLA published; advisory disclosure within 8–19 days of patch | 2 | https://langfuse.com/security/incident-and-breach |
| Security policy publication | Detailed TOMs, Encryption, Vulnerability Management, Incident Response, Penetration Testing pages | 2 | https://langfuse.com/security |
| AI safety framework reference | SOC 2 + ISO 27001 (general); no explicit external AI-safety framework (NIST AI RMF, ISO 42001) cited | 1 | https://langfuse.com/security |
| AI system identity disclosure | Langfuse is identified as an AI/LLM observability platform across all surfaces; AI features documented separately | 2 | https://langfuse.com/security/ai-features |

**Positive findings:** Each maintainer-issued advisory includes the discovery channel, internal triage timeline, Cloud patch deployment time, OSS patch release time, and access-log review outcome; security center has thirteen dedicated topic pages including Whistleblowing and Penetration Testing pages; status page operates independently.

**Recorded concerns:** No explicit reference to an external AI-safety governance framework on the security pages; AI Features security page is at a higher level than the dedicated NIST AI RMF or ISO/IEC 42001 mappings that some peer platforms publish.

## Incident Timeline (trailing 12 months: 2025-04-29 to 2026-04-29)

| Date | CVE ID | CVSS | Description | Patch status | KEV |
|------|--------|------|-------------|--------------|-----|
| 2025-09 | CVE-2025-59305 | 7.6 | Improper authorization in background-migration TRPC endpoints | Patched same-day (commit `d67b317`) | No |
| 2025-11-09 | CVE-2025-64504 | 5.0 | Cross-organization enumeration via project membership APIs | Patched 2025-11-01 in v3.124.1 | No |
| 2025-11-19 | CVE-2025-65107 | 6.5 | SSO account takeover via CSRF | Patched same-day in v3.131.0 | No |
| 2025-12-02 | CVE-2025-9799 | 5.0 | SSRF in `promptChangeEventSourcing` webhook handler | Subsequent releases address | No |
| 2026-01-21 | CVE-2026-24055 | 5.3/6.3 | `/api/public/slack/install` accepted client `projectId` without auth | Patched in v3.147.0 | No |
| 2026-04-17 | CVE-2026-41487 | Low | LLM-connection update flow allowed `member` role to redirect provider secret reuse | Patched in v3.167.0 | No |

## Contextual Analysis

Langfuse's documented compliance and disclosure posture is more complete than typical for an open-core observability vendor at its maturity stage: the security center separates Security, Compliance, Privacy, and Legal into thirteen public pages, attestations are in place across three frameworks (SOC 2 Type II, ISO 27001, HIPAA), three deployment regions are offered with distinct subprocessor sets, and air-gapped self-hosting is supported as a first-class deployment topology. The vulnerability-management process exhibits a consistent pattern: external researchers report through a published `security@langfuse.com` channel, internal triage produces Cloud and OSS patches usually on the same day, an access-log review is conducted before disclosure, and an advisory is published with the full timeline once an enterprise advance-notice period elapses.

The recurring presence of Improper Access Control (CWE-284) findings across distinct subsystems — Slack OAuth (CVE-2026-24055), project membership APIs (CVE-2025-64504), background-migration endpoints (CVE-2025-59305), LLM connection management (CVE-2026-41487) — is a pattern worth recording for procurement audiences whose deployments include multi-tenant or cross-organization trust boundaries. Each individual issue was patched rapidly and Cloud access-log reviews returned no exploitation evidence, but the recurrence warrants the attention of buyers operating in regulated industries.

The 2026-01-16 acquisition by ClickHouse, Inc. is publicly disclosed in the operator's blog ("Langfuse joins ClickHouse"), the press page, and a top-of-page banner across the security site, and is corroborated by primary press coverage from ClickHouse (corporate blog, Series D financing announcement at $15B valuation), Orrick (Langfuse legal counsel), SiliconANGLE, InfoWorld, and others. As of the evaluation date, however, the operator-level legal disclosures (subprocessors page, footer copyright line) still reference "Langfuse GmbH / Finto Technologies Inc." with Finto Technologies named as 100% parent. The corporate-entity successor relationship and the controller/processor designation post-acquisition are matters that procurement teams should clarify with the operator until the public legal pages are updated.

A separate structural observation, recorded for completeness without intent attribution: ClickHouse, Inc. publicly counts Anthropic among its customers (ClickHouse press releases dated 2025-05-29 and 2025-10-07; TipRanks coverage 2026-02-20 of Anthropic's air-gapped ClickHouse deployment supporting Claude Code observability). Public investor records (Tracxn, PitchBook) show no equity overlap between Anthropic / Anthropic Ventures and either Langfuse or ClickHouse, Inc. This evaluation is conducted by Claude (Anthropic) and the indirect commercial-relationship surface at the parent-company level is disclosed here as fact; the bias-disclosure language below applies and identical evaluation criteria are applied regardless of relationship.

## VERDICT Record

**Summary.** Langfuse scores 62/85 (Tier A, 73%) under VERDICT v0.3.1 Layer 0, with strong public compliance documentation and rapid vulnerability response counterbalanced by a pattern of access-control findings across distinct subsystems and a public legal-entity disclosure that has not yet been updated to reflect the 2026-01-16 ClickHouse acquisition.

**Risk Factor Summary by Use Case.**

| Use case | Recorded risk factors |
|----------|----------------------|
| Internal testing / single-tenant evaluation | Low. Self-hosted MIT core, air-gapped operation supported, configurable retention, AI-training opt-out explicit. |
| Credential-handling workflows | Moderate. CVE-2026-41487 (Low severity, patched in v3.167.0) involved cross-tenant exposure of stored LLM provider secrets to a `member` role under specific conditions. |
| Cloud multi-tenant deployments | Moderate. Three of the six trailing-12-month CVEs touched cross-tenant or cross-organization boundaries; SOC 2 Type II + ISO 27001 attestations cover tenant-isolation controls. |
| Regulated-data workloads (PHI, GDPR Art. 9) | Documented support. HIPAA region with restricted subprocessor set, BAA available, GDPR with self-serve DPA, EU region. SOC 2 Type II and ISO 27001 reports available via NDA-gated request flow. |

**Reference Information** (presented as options, not instructions):

1. The SOC 2 Type II, ISO 27001, and HIPAA attestation reports can be requested via https://langfuse.com/request-security-docs under NDA.
2. Self-hosted air-gapped operation is documented at https://langfuse.com/self-hosting.
3. Buyers tracking the ClickHouse acquisition's effect on the legal-entity stack may wish to request from the operator a confirmation of the controller/processor designation.

**Bias Disclosure.** This evaluation uses Claude (Anthropic) as its tooling. Anthropic operates in the AI agent market and may compete with some evaluated vendors. VERDICT discloses this relationship in every report and applies identical evaluation criteria to all platforms regardless of their relationship to Anthropic.

## Future Evaluation Plan

- **Layer 1 (behavioral):** 30 runs × 4 difficulty levels on Langfuse Cloud Hobby tier across 3+ days, focusing on ingestion correctness, evaluation orchestration, and cost-cap behavior; target window Q2–Q3 2026.
- **Layer C (continuous):** GitHub Security Advisories at `langfuse/langfuse`, NVD, OSV, and CISA KEV monitored on a weekly cadence; mandatory R-dimension re-evaluation if any CVSS ≥ 7.0 CVE is published, if any Langfuse CVE enters the KEV catalog, or 90 days from this evaluation date (next routine: 2026-07-28).
- **Re-evaluation trigger watch:** Any operator-page update reflecting the ClickHouse, Inc. acquisition in the DPA, Subprocessors, or Privacy Policy will trigger a V/T differential re-evaluation.

---

**Score: 62/85**
**V: 14/20, R: 12/20, D: 11/15, I: 8/10, C: 8/10, T: 9/10**
**Dimensions verified: V+R+D+I+C+T = 62**
**Tier: A**
**Category: AI/LLM Application Observability Platform · Open Core (MIT + commercial EE)**

**Framework version:** VERDICT v0.3.1
