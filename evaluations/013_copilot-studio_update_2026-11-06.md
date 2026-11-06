# VERDICT Evaluation #013 — Microsoft Copilot Studio — Update

| Field | Value |
|---|---|
| Evaluation number | #013 |
| Platform | Microsoft Copilot Studio |
| Evaluation type | Update (Differential Evaluation) |
| Update date | 2026-11-06 |
| Original Layer 0 date | 2026-03-25 |
| Evaluator | VERDICT evaluation engine; `evaluator_model: claude-fable-5-1` (operator's model selection for batch 1, Batch1-TrancheA-Authorize-2026-10-31-A1, written as supplied at invocation) |
| Target version | Hosted service. Platform 2026.6.3 / UX 26.06.21-24 as shown on the Released Versions page (page last updated 2026-07-01); release activity through September 2026 recorded on the What's new page (last updated 2026-11-04) |
| Framework | VERDICT v0.3.2 (`zinova-lab/verdict-engine` @ 73d9a09) |
| Previous evaluation | 2026-03-25 · 61/85 · Tier A · framework v0.3.1 (migrated capture) |
| CVE window | 2025-11-06 → 2026-11-06 (trailing 12 months from the update date) |
| Disclosure tags | `evaluator-coi`, `direct-investment` (Trigger 1) |

## Executive Summary

Microsoft Copilot Studio scores 58/85 (Tier A) at this update, down from the migrated capture's 61/85; no single dimension moved the total by five points or more. Two CVEs are product-scoped to Copilot Studio in the trailing 12 months: CVE-2026-21520 (information disclosure through indirect prompt injection via SharePoint form input, CNA CVSS 3.1 7.5, published 2026-01-22) and CVE-2026-80098 (elevation of privilege through improper verification of a cryptographic signature, CNA CVSS 3.1 9.3, published 2026-09-03, public 2026-09-08); Microsoft records both as mitigated service-side with no customer action. The base record's CVE-2025-32711 "EchoLeak" entry is attributed on MSRC and NVD to Microsoft 365 Copilot, not Copilot Studio, and falls outside the window; it is removed from the R fields at this update. The documented control set has expanded since March 2026 — Microsoft Entra Agent IDs for every new agent (mandatory from July 2026), a quarantine API for administrators, admin control over maker-provided tool credentials, and ISO/IEC 42001 certification scope extended to Copilot Studio — while the C dimension is scored at 4/10 because the connector data-policy model is hybrid, least-privilege tool authentication is configurable rather than default, and tenant isolation rests on audit reports that are available to customers only. No entry in the CISA KEV catalog is product-scoped to Copilot Studio.

## Scorecard

| Dimension | Score | Max | Rating |
|---|---|---|---|
| V — Verifiability | 14 | 20 | High |
| R — Resilience | 11 | 20 | Mid |
| D — Data Conduct | 11 | 15 | High |
| I — Identity & Control | 8 | 10 | High |
| C — Containment | 4 | 10 | Mid |
| T — Transparency | 10 | 10 | High |
| E — Effectiveness | not evaluated (Layer 1+) | 15 | — |
| **Layer 0 total** | **58** | **85** | — |

Tier: A
Category: No-Code Agent Builder · Enterprise SaaS

CISA KEV: None — no catalog entry is product-scoped to Microsoft Copilot Studio (operator KEV JSON check 2026-11-06: catalogVersion 2026.11.04, 1768 entries, no entry naming "Copilot"; CVE-2026-21520 and CVE-2026-80098 are not listed per the catalog's vendor filter as reflected in the public trackers consulted). Previous score: 61/85.

## Dimension Detail

### V — Verifiability (14/20, High)

| Criterion | Result | Score | Evidence URL |
|---|---|---|---|
| Developer / company identity | Operator of record: Microsoft Corporation, One Microsoft Way, Redmond, WA 98052, USA, named in the Microsoft Privacy Statement ("How to contact us"; Microsoft Ireland Operations Limited named for EU users) and in the Product Terms / DPA that govern Copilot Studio per the security and governance page. Official contact: Microsoft privacy web form (https://www.microsoft.com/concern/privacy) and MSRC. Corporate registration confirmed by the vendor's legal pages; no registry was queried. | 4 | https://www.microsoft.com/en-us/privacy/privacystatement ; https://learn.microsoft.com/en-us/microsoft-copilot-studio/security-and-governance |
| Source code disclosure | Closed source. Copilot Studio is a hosted Online Service; no source is published (Criterion-VSource-001). | 0 | https://learn.microsoft.com/en-us/microsoft-copilot-studio/admin-certification |
| Version management transparency | Weekly Released Versions page with per-version release-note pages (platform and UX versions, first-available and worldwide dates) and a monthly What's new page. | 3 | https://learn.microsoft.com/en-us/power-platform/released-versions/copilotstudio ; https://learn.microsoft.com/en-us/microsoft-copilot-studio/whats-new |
| Third-party dependency disclosure | Microsoft Online Services Subprocessors List carries a "DATE OF ISSUE" and is published through the Trust Center data-access page and the Service Trust Portal; update notices are issued through the Microsoft 365 Message Center (e.g. MC1470426, 2026-09-11). The edition readable in-session carried the date of issue 2025-02-28; the current edition's date was not readable in-session (see Differential). | 3 | https://www.microsoft.com/en-us/trust-center/privacy/data-access ; https://api.servicetrust.microsoft.com/api/v2/downloadDocuments/f2cc90fe-471f-4f07-a9ae-af71ebce8486/7b1d8c02-6105-4be4-9995-ff01f87443bc |
| Independent certification | SOC audit reports for Copilot Studio are available from the Service Trust Portal, which requires sign-in; no SOC 2 report is publicly readable. | 2 | https://learn.microsoft.com/en-us/microsoft-copilot-studio/admin-certification |
| Functional reproducibility docs | Power Platform API reference (Copilot Studio operations) and product documentation covering agent behavior, orchestration, tools and channels. | 2 | https://learn.microsoft.com/en-us/rest/api/power-platform/copilotstudio/bots ; https://learn.microsoft.com/en-us/microsoft-copilot-studio/ |

Positive findings: the legal entity is named on the vendor's own privacy and licensing pages; release notes are published per version on a weekly cadence; the sub-processor list is dated and change-notified.

Recorded concerns: closed source; SOC reports are customer-only (sign-in).

### R — Resilience (11/20, Mid)

| Criterion | Result | Score | Evidence URL |
|---|---|---|---|
| CVE count (trailing 12 months) | 2 product-scoped CVEs (CVE-2026-21520, CVE-2026-80098): base 3; penalty −1 for CVSS 9.0+ present. Basis: exact. | 2 | https://app.opencve.io/cve/?product=copilot_studio&vendor=microsoft ; https://vulners.com/search/vendors/microsoft/products/copilot%20studio |
| Maximum CVSS severity | 9.3 (CVE-2026-80098; CNA v3.1; vector AV:N/AC:L/PR:N/UI:N/S:C/C:L/I:H/A:N computes to 9.3, matching the stated score). | 0 | https://raw.githubusercontent.com/CVEProject/cvelistV5/main/cves/2026/80xxx/CVE-2026-80098.json |
| Patch response speed | Both CVEs were mitigated service-side before or at publication (MSRC: "already been fully mitigated"; "no customer action"). Measured from public disclosure to fix: 0 days. The private report-to-fix interval for CVE-2026-21520 (reported 2025-11-26, fix 2026-01-15 per the reporting researcher) is recorded in the Contextual Analysis. | 3 | https://msrc.microsoft.com/update-guide/vulnerability/CVE-2026-21520 ; https://msrc.microsoft.com/update-guide/vulnerability/CVE-2026-80098 |
| Structural issues | Two distinct root causes in the window (CWE-77 command injection via untrusted input; CWE-347 signature verification). The base record's "SSRF and spoofing classes recurring" finding rested on 2024 CVEs (CVE-2024-38206, CVE-2024-43610, CVE-2024-49038) outside this window and is not carried. | 3 | https://raw.githubusercontent.com/CVEProject/cvelistV5/main/cves/2026/80xxx/CVE-2026-80098.json ; https://nvd.nist.gov/vuln/detail/CVE-2026-21520 |
| Supply chain compromise (trailing 12 months) | None located for Copilot Studio's own packages, accounts, build pipeline or distribution endpoints. Searches per step 3a returned no Copilot Studio result; the TeamPCP compromise of Microsoft's `durabletask` PyPI SDK (May 2026) is a different Microsoft product and is not attributed here. `supply_chain_compromise_12mo: false`. | 3 | https://radar.offseq.com/threat/teampcp-supply-chain-campaign-activity-through-202-e0ec22c1 (secondary; out of product scope) |

Positive findings: Microsoft issues CVEs for service-side fixes in a hosted product and records them in the MSRC Security Update Guide; both window CVEs required no customer action.

Recorded concerns: a CVSS 9.3 unauthenticated network elevation of privilege with changed scope (CVE-2026-80098) was recorded in the window; the researcher who reported CVE-2026-21520 published post-fix testing in which data exfiltration still occurred through a legitimate connector action (see Contextual Analysis).

Convention-CVEReserved-001: both counted IDs have PUBLISHED CVE List records (CVE-2026-21520 NVD published 2026-01-22; CVE-2026-80098 cvelistV5 state PUBLISHED, datePublished 2026-09-03). No as-of note is required.

### D — Data Conduct (11/15, High)

| Criterion | Result | Score | Evidence URL |
|---|---|---|---|
| GDPR compliance disclosure | Copilot Studio is governed by the Microsoft Product Terms and the Products and Services Data Protection Addendum (standard DPA provision); a Copilot Studio-specific GDPR / personal data requests page and EU Data Boundary coverage are published (Anthropic models excluded from the EU Data Boundary). | 3 | https://learn.microsoft.com/en-us/microsoft-copilot-studio/security-and-governance ; https://learn.microsoft.com/en-us/power-virtual-agents/personal-data-summary ; https://learn.microsoft.com/en-us/microsoft-copilot-studio/geo-data-residency |
| Data minimization | Service-generated data (audit telemetry, runtime activity signals) is collected by default; the security and governance page states this telemetry is processed by the Purview pipeline outside Customer Lockbox coverage, and no customer opt-out of service telemetry is documented. Optional data sharing for AI improvement is off by default (admin opt-in). Scored on the service-telemetry default. | 0 | https://learn.microsoft.com/en-us/microsoft-copilot-studio/security-and-governance ; https://learn.microsoft.com/en-us/power-platform/faqs-copilot-data-security-privacy |
| AI training use | Prompts and responses "are NOT used to train or improve Microsoft AI models, unless your tenant admin opts in" and not used to train third-party models; abuse monitoring is transient with no storage. Retention stated: session transcripts retained in Copilot Studio storage up to 28 days; Dataverse conversation transcripts 30 days by default (configurable). | 4 | https://learn.microsoft.com/en-us/power-platform/faqs-copilot-data-security-privacy ; https://learn.microsoft.com/microsoft-copilot-studio/analytics-transcripts-studio |
| Sub-processor transparency | Dated Microsoft Online Services Subprocessors List with change notification (see V). Anthropic was onboarded as a Microsoft sub-processor for Copilot Studio from 2026-01-07; OpenAI-operated models added as a sub-processor 2026-06-23. | 3 | https://learn.microsoft.com/en-us/microsoft-365/copilot/connect-to-ai-subprocessor ; https://learn.microsoft.com/en-za/power-platform/admin/allow-llm-generative-responses ; https://learn.microsoft.com/en-gb/microsoft-365/copilot/openai-subprocessor |
| Data retention disclosure | Retention is stated for conversation transcripts (28 days service storage; 30 days Dataverse default) but not per category for other Copilot Studio data (audit telemetry, agent configuration, analytics). | 1 | https://learn.microsoft.com/microsoft-copilot-studio/analytics-transcripts-studio ; https://learn.microsoft.com/en-us/microsoft-copilot-studio/guidance/custom-analytics-strategy |

Positive findings: explicit no-training statement with admin opt-in; customer-managed keys; EU Data Boundary coverage and configurable cross-geo data movement; dated sub-processor list with Anthropic and OpenAI disclosures.

Recorded concerns: no documented opt-out of service telemetry; retention stated for transcripts only; Anthropic models are excluded from the EU Data Boundary, FedRAMP and PCI DSS scope within Copilot Studio.

### I — Identity & Control (8/10, High)

| Criterion | Result | Score | Evidence URL |
|---|---|---|---|
| Emergency stop documentation | Quarantine API (`SetAsQuarantined` / `SetAsUnquarantined` / status) documented with endpoints, required admin roles and effect: quarantined agents cannot be interacted with in any channel other than the maker test pane. Tenant-level disabling of agent publishing is also documented. The documentation does not state a propagation time. | 4 | https://learn.microsoft.com/en-us/microsoft-copilot-studio/admin-api-quarantine ; https://learn.microsoft.com/en-us/microsoft-copilot-studio/security-and-governance |
| Human-in-the-loop design | Optional: "request information" action pauses an agent flow for designated reviewers (preview, Nov 2025); approvals are maker-configured, not default. | 1 | https://learn.microsoft.com/en-us/microsoft-copilot-studio/flows-request-for-information ; https://learn.microsoft.com/en-us/microsoft-copilot-studio/whats-new |
| Permission delegation transparency | Microsoft Entra Agent ID created for every new agent from July 2026 (scopes connector permissions, Conditional Access and DLP per agent); tool authentication (end-user vs maker-provided) documented; connector dependency insights for admins; Agent 365 identity governance. | 3 | https://learn.microsoft.com/en-us/microsoft-copilot-studio/admin-use-entra-agent-identities ; https://learn.microsoft.com/en-us/microsoft-copilot-studio/configure-no-maker-authentication ; https://learn.microsoft.com/en-us/microsoft-copilot-studio/security-and-governance |

Positive findings: per-agent identities are now mandatory for new agents; quarantine is exposed through a documented admin API; audit logs flow to Purview and Sentinel.

Recorded concerns: human approval is opt-in per flow; agent creation cannot be disabled (per the security FAQ), only chat access via data policies.

### C — Containment (4/10, Mid)

| Criterion | Result | Score | Evidence URL |
|---|---|---|---|
| Sandbox design | Hybrid: data policies classify connectors into Business / Non-business / Blocked; new connectors land in the default (Non-business) group and are usable unless an admin blocks them; DLP enforcement is on by default since early 2025. | 2 | https://learn.microsoft.com/en-us/microsoft-copilot-studio/admin-data-loss-prevention ; https://learn.microsoft.com/lb-lu/power-platform/admin/dlp-connector-classification |
| Least privilege | Configurable: by default both end-user and maker-provided credentials are enabled for tools; admins can enforce end-user credentials per environment or environment group. | 1 | https://learn.microsoft.com/en-us/microsoft-copilot-studio/configure-no-maker-authentication |
| Tenant isolation (cloud) | Claimed but not publicly verified: Microsoft states that authentication and authorization segregate requests among tenants; SOC/ISO audit reports are customer-only. CVE-2026-80098 (changed scope, unauthenticated) carries no public cross-tenant statement either way. The security FAQ states Copilot Studio does not support the Power Platform "tenant isolation" setting for cross-tenant connections. | 1 | https://learn.microsoft.com/en-us/power-platform/faqs-copilot-data-security-privacy ; https://learn.microsoft.com/en-us/microsoft-copilot-studio/security-faq |

Positive findings: real-time DLP enforcement; endpoint filtering for HTTP and SharePoint knowledge; admins can require end-user credentials and block "no authentication" chat; image-rendering and embedded-URL controls (Aug 2026).

Recorded concerns: permissive default connector group; maker-provided credentials allowed by default; isolation evidence is behind sign-in.

### T — Transparency (10/10, High)

| Criterion | Result | Score | Evidence URL |
|---|---|---|---|
| CVE publication posture | Issues CVEs with MSRC advisories for service-side fixes. | 2 | https://msrc.microsoft.com/update-guide/vulnerability/CVE-2026-21520 |
| Incident disclosure speed | CVE-2026-21520 fix 2026-01-15, advisory 2026-01-22 (7 days); CVE-2026-80098 published at fix. No security incident separate from the CVEs was located in the window. | 2 | https://www.capsulesecurity.io/blog-post/shareleak-taking-the-wheel-of-microsofts-copilot-studio-cve-2026-21520 ; https://msrc.microsoft.com/update-guide/en-US/advisory/CVE-2026-80098 |
| Security policy publication | SDL adherence, a control-by-control security and governance table, security FAQ, Lockbox scope and exclusions, Trust Center. | 2 | https://learn.microsoft.com/en-us/microsoft-copilot-studio/security-and-governance ; https://learn.microsoft.com/en-us/microsoft-copilot-studio/security-faq |
| AI safety framework reference | External framework: Microsoft states that its ISO/IEC 42001:2023 certification scope was extended to Copilot Studio at the 2026 recertification (Microsoft blog, 2026-05-28, as reported); Responsible AI Standard and a Copilot Studio Platform Card are published. | 2 | https://techcommunity.microsoft.com/blog/microsoft365copilotblog/recertified-how-microsoft-365-copilot-continues-to-earn-trust-and-what-changed-i/4521693 ; https://www.helpnetsecurity.com/2026/05/28/microsoft-365-copilot-iso-42001-certification/ ; https://learn.microsoft.com/en-us/microsoft-copilot-studio/responsible-ai-overview |
| AI system identity disclosure | Default: generative answers carry the default message "Just so you are aware, I sometimes use AI to answer your questions" and an AI-generated footer; makers can remove it. | 2 | https://learn.microsoft.com/bs-latn-ba/microsoft-copilot-studio/faqs-generative-answers |

Positive findings: CVEs issued for a hosted service; detailed governance documentation; AI-management-system certification scope.

Recorded concerns: the AI disclosure footer is maker-removable; the ISO 42001 scope statement is a vendor announcement whose certificate is held on the Service Trust Portal (sign-in).

## Incident Timeline

| Date | CVE ID | CVSS | Description | Patch status | KEV |
|---|---|---|---|---|---|
| 2026-01-22 (fix 2026-01-15; reported 2025-11-26) | CVE-2026-21520 | 7.5 (CNA v3.1; NVD assessment not provided) | Copilot Studio information disclosure: unauthenticated network attacker can view sensitive information; CWE-77. Researcher name "ShareLeak" (indirect prompt injection via SharePoint form input). | Mitigated service-side; no customer action | No |
| 2026-09-03 (public 2026-09-08) | CVE-2026-80098 | 9.3 (CNA v3.1) | Copilot Studio elevation of privilege: improper verification of cryptographic signature allows an unauthorized attacker to elevate privileges over a network; CWE-347; scope changed. | Mitigated service-side; no customer action | No |

Out of product scope (recorded, not counted): CVE-2025-32711 "EchoLeak" — affected product Microsoft 365 Copilot (NVD CPE `microsoft:365_copilot`), published 2025-06-11; outside the window and outside `target_version` scope (Attribution-CVE-001). CVE-2026-42824, CVE-2026-24299, CVE-2026-26133, CVE-2026-45497, CVE-2026-41106, CVE-2026-50517 — Microsoft 365 Copilot / Microsoft Copilot; not Copilot Studio. CVE-2024-38206, CVE-2024-43610, CVE-2024-49038 — Copilot Studio, published 2024; outside the window.

Related non-CVE items: Datadog Security Labs reported Copilot Studio audit-logging gaps for certain administrative actions (reported 2025-09-02; MSRC fixes through an ETA of 2026-01-15); no CVE assigned.

## Contextual Analysis

Microsoft's position, as documented, is that Copilot Studio is an Online Service governed by the Product Terms and DPA, developed under the SDL, and that service-side vulnerabilities are remediated by Microsoft and then published as CVEs "to provide further transparency." The two window CVEs fit that pattern: each MSRC entry states the issue was fully mitigated with no customer action. Measured from public disclosure, the fix precedes the advisory in both cases. The reporting researcher for CVE-2026-21520 (Capsule Security) publishes a timeline of initial report 2025-11-26, MSRC confirmation 2025-12-05 and fix 2026-01-15 — a 50-day private interval — and states that in its post-fix testing an injected instruction still caused an agent to send data through a legitimate Outlook action that DLP did not flag. VERDICT records the researcher's statement without adjudicating it; Microsoft's advisory does not address it.

Evidence rule for this report: every factual claim was confirmed by web retrieval during the session; where the vendor's own page could not be rendered by the session tools (MSRC Security Update Guide, NVD detail pages), the content was taken from search-engine renderings of those same pages and, for CVE-2026-80098, from the CNA's cvelistV5 record. These are listed in the Differential section.

Operator of record: the public record agrees with the prompt. Microsoft Corporation is the legal entity named on Microsoft's Privacy Statement and licensing pages; no correction is required. `independence` is recorded as `parent` because the operator is itself the parent company.

Scope correction to the base record: the migrated capture recorded five CVEs with a maximum of 9.3 and named only CVE-2025-32711, which MSRC and NVD attribute to Microsoft 365 Copilot. Under Attribution-CVE-001 that ID does not enter Copilot Studio's R fields. The 9.3 maximum in this update is coincidental and comes from CVE-2026-80098, a Copilot Studio CVE. A KNOWN_FACTS candidate is staged (see Differential).

Control-plane changes in the window that bear on I and C: automatic Microsoft Entra Agent IDs became mandatory for new agents in July 2026; the quarantine API moved to the `copilotstudio` namespace; admins gained control over maker-provided credentials, image rendering and embedded URLs in responses; Agent 365 onboarding adds Conditional Access and network egress/ingress controls. Against that, defaults remain permissive in two places the framework scores: new connectors land in the usable Non-business group, and maker-provided credentials are enabled unless an admin turns them off, which the documentation notes also disables background and scheduled triggers.

Model-provider changes: Anthropic models (Claude) have been offered in Copilot Studio since 2025, and from 2026-01-07 Anthropic operates as a Microsoft sub-processor under the Product Terms and DPA; Microsoft documents that these models are excluded from the EU Data Boundary, FedRAMP and PCI DSS scope within Copilot Studio, and that EU/UK tenants have them off by default. OpenAI-operated models were added as a sub-processor on 2026-06-23. These are product-level integration facts and are separated from the corporate disclosure below.

Base-record superlatives ("highest compliance posture in this index", "the only platform with all four", "first documented zero-click prompt injection") are not carried (Absolute Rule 7). The compliance facts themselves stand: Copilot Studio's documentation states HIPAA BAA coverage, SOC audit, ISO 27001/27017/27018/27701 and other certifications with reports on the Service Trust Portal, and FedRAMP through the US Government cloud.

## VERDICT Record

**Summary.** Microsoft Copilot Studio records 58/85 (Tier A) at the 2026-11-06 update, with two product-scoped CVEs in the window (maximum CNA CVSS 9.3), expanded per-agent identity and quarantine controls, and permissive default settings for connector classification and tool credentials.

**Risk Factor Summary by Use Case**

| Use case | Observation |
|---|---|
| Internal testing | Makers can test quarantined agents in the test pane; security scan warns before publishing; environment routing provides maker sandboxes. |
| Credential-handling | Maker-provided credentials are enabled by default and run tools under the maker's identity unless an admin enforces end-user credentials; the 2026 CVEs involved untrusted input reaching agent context (CVE-2026-21520) and signature verification (CVE-2026-80098). |
| Cloud multi-tenant | Hosted only; isolation evidence is in customer-only audit reports; CVE-2026-80098 is unauthenticated with changed scope and carries no public cross-tenant statement. |
| Regulated-data workloads | HIPAA BAA, SOC, ISO, FedRAMP (GCC) and EU Data Boundary documented; Anthropic models excluded from EUDB, FedRAMP and PCI DSS scope; customer-managed keys available. |

**Reference Information** (options, not instructions)
1. Enforcing end-user credentials and classifying new connectors as Blocked by default are documented admin options that change the two C defaults scored here.
2. The quarantine API and Entra Agent IDs are documented paths for per-agent isolation and Conditional Access.
3. The per-model exclusions (EU Data Boundary, FedRAMP, PCI DSS) are documented per provider and can be reviewed per tenant.

**Bias Disclosure**

"This evaluation uses Claude (Anthropic) as its tooling. Anthropic operates in the AI agent market and may compete with some evaluated vendors. VERDICT discloses this relationship in every report and applies identical evaluation criteria to all platforms regardless of their relationship to Anthropic."

VERDICT additionally discloses a parent-identity relationship (Trigger 1). The operator of the evaluated platform, Microsoft Corporation, is a material Anthropic equity-holder as recorded in KNOWN_FACTS.md: Microsoft committed to invest up to USD 5 billion in Anthropic as part of the strategic partnership announced on 2025-11-18 (https://blogs.microsoft.com/blog/2025/11/18/microsoft-nvidia-and-anthropic-announce-strategic-partnerships/ ; https://www.anthropic.com/news/microsoft-nvidia-anthropic-announce-strategic-partnerships). Anthropic's Series G announcement of 2026-02-12 states that the round includes a portion of the previously announced investments from Microsoft and NVIDIA; the amount closed is not public, and no statement is made here that the commitment has closed in full (https://www.anthropic.com/news/anthropic-raises-30-billion-series-g-funding-380-billion-post-money-valuation). The relationship is recorded with the tags `evaluator-coi` and `direct-investment`. Identical evaluation criteria were applied regardless of this relationship.

Product-level integration (separate from the corporate relationship above): Copilot Studio offers Anthropic Claude models as one of several selectable primary models alongside OpenAI, Mistral and xAI models, and Anthropic has operated as a Microsoft sub-processor for these models since 2026-01-07 (https://learn.microsoft.com/en-us/microsoft-365/copilot/connect-to-ai-subprocessor). This is a model-provider relationship of the kind VERDICT evaluates across platforms and is not itself a disclosure trigger.

Triggers 2 and 3 were assessed and do not fire: no material Anthropic equity-holder is recorded as a material investor in Microsoft Corporation, and no non-arms-length channel beyond the operator relationship already disclosed under Trigger 1 was located.

## Future Evaluation Plan

- Layer 1 (behavioral testing): not scheduled; Copilot Studio's public free tier is a time-limited trial, and Layer 1 timing is deferred to Operations.
- Layer C: routine lane 365 days from `updated_at` (pipeline-derived `next_review_due`); interrupt lane active for T1–T6. Items to watch: the CVE List / NVD state of CVE-2026-80098, any public statement on cross-tenant impact, and any change to default connector classification or credential settings.

## Differential

| Item | Value |
|---|---|
| Lane | Routine (batch-1 scheduled; interval not elapsed). No T1 / T2 / T5 / dormancy observation row was recorded for `copilot-studio` at the 2026-10-27 sweep (operator input, retrieved 2026-11-06 JST). |
| Previous evaluation | 2026-03-25 · 61/85 · Tier A · v0.3.1 (migrated capture; `sources: []`; `qa` unresolved ×3; `evaluator_model: unrecorded`) |
| This evaluation | 2026-11-06 · 58/85 · Tier A · v0.3.2 · `evaluator_model: claude-fable-5-1` |
| Score movement | −3 (V 16→14, R 11→11, D 10→11, I 7→8, C 8→4, T 9→10). Below the 5-point threshold; the Executive Summary names the moved dimensions nonetheless. |

Per-dimension state: V re-evaluated — migrated capture, no sources; R re-evaluated — migrated capture, no sources; D re-evaluated — migrated capture, no sources; I re-evaluated — migrated capture, no sources; C re-evaluated — migrated capture, no sources; T re-evaluated — migrated capture, no sources; E null (Layer 0). No carry-forward check could be performed because the base record cites no sources (convention 2026-09-22).

Prior-record omissions stated as facts: the base record recorded `cve_count_12mo: 5` while naming one CVE ID (CVE-2025-32711); that ID is attributed by MSRC and NVD to Microsoft 365 Copilot, not Copilot Studio. The four unnamed IDs cannot be reconstructed from the record. `independence: unrecorded`, `target_version: null`, `evaluator_model: unrecorded` and the three `unresolved` QA fields are resolved at this update.

Dormancy test: not dormant — platform releases through June 2026 and feature releases through September 2026 are published; `dormant_since` is omitted.

Operator input recorded (OperatorInput-001), all retrieved 2026-11-06 JST:
1. Quarterly sweep 2026-10-27 public-layer rows for `copilot-studio`: none.
2. CISA KEV JSON feed (https://www.cisa.gov/sites/default/files/feeds/known_exploited_vulnerabilities.json): catalogVersion 2026.11.04, dateReleased 2026-11-04T20:00:05.774Z, count 1768; CVE-2025-32711 not present; no entry whose vendorProject, product, vulnerabilityName or shortDescription contains "Copilot". `cisa_kev.present: false`.
3. Rendered text of unread pages: none supplied.

Pages the session tools could not render (stated as unread, not scored as silence):
- https://msrc.microsoft.com/update-guide/vulnerability/CVE-2026-21520 and https://msrc.microsoft.com/update-guide/vulnerability/CVE-2026-80098 (client-rendered). Content used: search-engine renderings of the same MSRC pages (title, release date, CNA, affected product "Microsoft Copilot Studio", CVSS vector/score, FAQ text) and, for CVE-2026-80098, the CNA record at https://raw.githubusercontent.com/CVEProject/cvelistV5/main/cves/2026/80xxx/CVE-2026-80098.json.
- https://nvd.nist.gov/vuln/detail/CVE-2026-21520 and CVE-2026-80098 (empty render). Content used: search-engine rendering of the NVD page for CVE-2026-21520 (CPE `microsoft:copilot_studio`, CNA 7.5, "NVD assessment not yet provided").
- https://www.cisa.gov/known-exploited-vulnerabilities-catalog (not fetched); operator JSON check used.
- Service Trust Portal audit reports and the current edition of the Microsoft Online Services Subprocessors List (sign-in / viewer); an older edition (date of issue 2025-02-28) was readable at the STP download URL cited in V.
- https://www.microsoft.com/en-us/trust-center/privacy/data-access (not fetched directly; search-engine rendering used).
The operator may supply rendered text for any of these per OperatorInput-001; the scores above do not depend on content behind those walls beyond what is recorded.

Sources consulted with "none located" results: MIT AI Agent Index entry for Copilot Studio (none located by search); vendor incident bulletins specific to Copilot Studio beyond MSRC entries (none located).

KNOWN_FACTS candidate (staged, not applied): "Microsoft Copilot Studio — CVE-2025-32711 (EchoLeak) is attributed to Microsoft 365 Copilot and is out of Copilot Studio product scope; the #013 base record's count of 5 and its EchoLeak finding are superseded by the 2026-11-06 update."

## Evaluation History

| Date | Type | Score | Tier | Framework |
|---|---|---|---|---|
| 2026-03-25 | Initial (migrated capture) | 61/85 | A | v0.3.1 |
| 2026-11-06 | Update | 58/85 | A | v0.3.2 |
