# VERDICT Evaluation #016 — Gemini Enterprise Agent Platform (formerly Vertex AI Agent Builder)

| Field | Value |
|---|---|
| Evaluation number | #016 |
| Platform | Gemini Enterprise Agent Platform (formerly Vertex AI Agent Builder) — slug `vertex-ai` |
| Evaluation type | Update (Differential Evaluation, Layer 0) |
| Date | 2026-11-07 (`updated_at`); original Layer 0 `evaluated_at` 2026-03-26 |
| Evaluator | VERDICT evaluation engine · `evaluator_model: claude-fable-5-1` (operator's model selection, Batch1-TrancheA-Authorize-2026-10-31-A1) |
| Target version | Gemini Enterprise Agent Platform (renamed from Vertex AI on 2026-04-22): Agent Runtime (formerly Vertex AI Agent Engine), managed GA / Agent Development Kit for Python (`google/adk-python`, PyPI `google-adk`) 2.13.0 released 2026-10-23 / Conversational Agents (Dialogflow CX), managed |
| Framework | VERDICT v0.3.2 — `zinova-lab/verdict-engine` @ 899f556 (ENGINE.md / QA.md / KNOWN_FACTS.md as pinned at invocation) |
| Previous evaluation | 2026-03-26 · 65/85 · Tier S · framework v0.3.1 (migrated capture) |
| Trailing 12-month window (R) | 2025-11-07 → 2026-11-07 |
| Disclosure layer | Trigger 1 fires (Google). Tags: `evaluator-coi`, `direct-investment`. Triggers 0, 2, 3 do not fire. |

## Executive Summary

Eight CVEs attributable to the evaluated components were published in the trailing 12 months (five against the Agent Development Kit for Python, three against Dialogflow CX), four of them with CNA CVSS 4.0 scores of 9.0 or higher and a maximum of 10.0 (CVE-2026-79696, unauthenticated code injection in the `adk web` development server). The score moves from 65/85 to 51/85 (Tier S → Tier B); the movement comes from R (14 → 6: CVE count, maximum severity and a recurring code-injection class in the same ADK component), V (18 → 16: SOC 2 reports are gated behind the Compliance Reports Manager and the product is open core, not full OSS), C (5 → 3: the sandbox egress model is hybrid and the default service agent's permissions are configurable rather than least-privilege by default) and T (9 → 7: disclosure intervals between fix and public notice ranged from 11 to 239 days, and no default AI-identity disclosure was located). The product was renamed on 2026-04-22 — Vertex AI became Gemini Enterprise Agent Platform and Agent Engine became Agent Runtime — and the training restriction the prior record cited as Service Specific Terms §17 is now §18 with unchanged wording. Google Cloud's contractual no-training commitment, dated sub-processor list, Cloud Data Processing Addendum with SCCs, and per-agent Agent Identity documentation are the strongest recorded controls. No CVE for the evaluated components appears in the CISA KEV catalog (catalogVersion 2026.11.06, operator-supplied check).

## Scorecard

| Dimension | Score | Max | Rating |
|---|---|---|---|
| V — Verifiability | 16 | 20 | High |
| R — Resilience | 6 | 20 | Low |
| D — Data Conduct | 13 | 15 | High |
| I — Identity & Control | 6 | 10 | Mid |
| C — Containment | 3 | 10 | Low |
| T — Transparency | 7 | 10 | High |
| **Layer 0 total** | **51** | **85** | — |
| E — Effectiveness | not evaluated | 15 | Layer 1+ |

Tier: B
Category: No-Code Agent Builder · Enterprise SaaS

CISA KEV: None — no CVE attributed to the evaluated components (Agent Runtime, ADK Python, Dialogflow CX) appears in the CISA KEV catalog (catalogVersion 2026.11.06, dateReleased 2026-11-06T19:44:45Z, 1769 entries; operator-supplied check 2026-11-07; per-CVE trackers consulted in session for each counted ID).

`cve_count_12mo: 8` (basis exact) · `max_cvss_12mo: 10.0` (CNA CVSS 4.0, CVE-2026-79696) · `supply_chain_compromise_12mo: false`

## Differential

| Item | Value |
|---|---|
| Lane | Routine (batch-1 scheduled; interval not elapsed) — LayerC-Triage-001; quarterly sweep 2026-10-27 recorded no T1 / T2 / T5 / dormancy row for `vertex-ai` (operator input, retrieved 2026-11-07 JST) |
| Previous evaluation | 2026-03-26 · 65/85 · Tier S · v0.3.1 |
| V | re-evaluated — migrated capture, no sources |
| R | re-evaluated — migrated capture, no sources |
| D | re-evaluated — migrated capture, no sources |
| I | re-evaluated — migrated capture, no sources |
| C | re-evaluated — migrated capture, no sources |
| T | re-evaluated — migrated capture, no sources |
| E | null (Layer 0) |
| Carry-forward checks | None possible: the base record carries `sources: []`, so conditions 1–4 of the Differential Evaluation procedure cannot be positively satisfied for any dimension (convention 2026-09-22). All six dimensions re-evaluated from sources retrieved 2026-11-07. |
| Dormancy test | Not dormant: ADK Python 2.13.0 released 2026-10-23 (PyPI); Agent Platform release notes newest entry 2026-10-21. `dormant_since` omitted. |
| Operator input (OperatorInput-001) | (1) Quarterly sweep 2026-10-27 public-layer rows for `vertex-ai`: none (retrieved 2026-11-07 JST). (2) CISA KEV JSON feed: catalogVersion 2026.11.06, dateReleased 2026-11-06T19:44:45.1797Z, count 1769; CVE-2026-2473 not in catalog; no entry naming "Vertex", "Agent Builder", "Agent Engine" or "Agent Development Kit"; 11 Google-vendor entries added in the window, none a Vertex AI / Google Cloud product (retrieved 2026-11-07 JST). (3) Rendered text of unread pages: none supplied; no page was reported unread in this session (the `cloud.google.com/terms/service-terms` page was read in two parts). |
| R-only escalation | Not applicable (full re-review). Total movement −14 ≥ 5: dimensions and evidence named in the Executive Summary. |

**Prior-record omissions and inconsistencies, stated as facts**

1. The base record recorded `cve_count_12mo: 2` (basis `exact`) while naming one CVE ID (CVE-2026-2473). Its second recorded incident, the September 2025 streaming misrouting, was recorded as "no CVE assigned"; the public record carries CVE-2025-11915 for that incident (GoogleCloud CNA, published 2025-10-22; bulletin GCP-2025-059 published 2025-10-21), inside the prior window. The prior count therefore rested on at most CVE-2026-2473 and CVE-2025-11915 without naming the second.
2. The base record recorded `max_cvss_12mo: null` beside a count of 2; CNA CVSS 4.0 scores existed for both IDs on the prior evaluation date (7.7 for CVE-2026-2473; 6.9 for CVE-2025-11915). No CVSS 3.1 vector exists for either.
3. CVE-2026-2473 names Vertex AI Experiments (PyPI `google-cloud-aiplatform` 1.21.0 – <1.133.0) as the affected product. Under Attribution-CVE-001 and the product scope bound by `target_version` (Agent Runtime, ADK Python, Dialogflow CX), it is outside scope and is recorded in the Incident Timeline, not in `cve_count_12mo`. The base record counted it.
4. Two in-scope CVEs published inside the prior window are absent from the base record: CVE-2025-12952 (Dialogflow CX, 2025-12-10, CNA CVSS 4.0 8.7) and CVE-2025-13427 (Dialogflow CX Messenger, 2025-12-18, CNA CVSS 4.0 6.9).
5. The base record cites the training restriction as Service Specific Terms §17; the clause is now §18 and is labelled "formerly Section 17" on the vendor's page (AI/ML sections renumbered 2026-02-18).
6. The base record's comparative lines ("highest score in this index", "broadest certification portfolio") are not carried (Absolute Rule 7).

## Dimension Detail

### V — Verifiability — 16/20 (High)

| Criterion | Result | Score | Evidence URL |
|---|---|---|---|
| Developer / company identity | Confirmed: the vendor's legal page names Google LLC, 1600 Amphitheatre Parkway, Mountain View, CA 94043 (default contracting entity; Google Cloud Japan G.K., Google Cloud EMEA Limited and others by billing location; last modified 2026-06-30). Official contact: legal-notices@google.com (Google Cloud Platform Terms of Service §14.1) and vulnerability intake at g.co/vulnz (ADK SECURITY.md). No registry was queried; corporate registration is confirmed by the vendor's own legal page (OperatorOfRecord-001). | 4 | https://cloud.google.com/terms/google-entity · https://cloud.google.com/terms · https://github.com/google/adk-python/security |
| Source code disclosure | Open core (Criterion-VSource-001): ADK Python is Apache-2.0 (`google/adk-python`, PyPI `google-adk`); Agent Runtime, Dialogflow CX and the hosted control plane are closed source. | 2 | https://github.com/google/adk-python · https://pypi.org/project/google-adk/ |
| Version management transparency | Confirmed: dated Gemini Enterprise Agent Platform release notes (newest 2026-10-21), Dialogflow release notes, and ADK `CHANGELOG.md` with GitHub releases (2.13.0, 2026-10-23). | 3 | https://docs.cloud.google.com/gemini-enterprise-agent-platform/release-notes · https://docs.cloud.google.com/dialogflow/docs/release-notes · https://github.com/google/adk-python/releases |
| Third-party dependency disclosure | Confirmed: Google Cloud subprocessor list with activity, processing country and registered address, last modified 2026-10-19, with archived prior versions. | 3 | https://cloud.google.com/terms/subprocessors |
| Independent certification | SOC 2 Type II reports are obtained through the Compliance Reports Manager; the vendor states that select resources require sign-in with a Google Cloud or Google Workspace account and that confidential resources are shared under the confidentiality obligations of the customer or partner agreement. Not publicly downloadable; scored as customers-only. ISO/IEC 27001 and ISO/IEC 42001 certificates "may be requested using the Compliance Reports Manager". | 2 | https://cloud.google.com/security/compliance/compliance-reports-manager · https://cloud.google.com/security/compliance/soc-2 · https://cloud.google.com/security/compliance/iso-27001 · https://cloud.google.com/security/compliance/iso-42001 |
| Functional reproducibility docs | Confirmed: REST / SDK API reference for the Agent Platform API and documented runtime contract for Agent Runtime; ADK reference documentation. | 2 | https://docs.cloud.google.com/gemini-enterprise-agent-platform/apis · https://docs.cloud.google.com/gemini-enterprise-agent-platform/build/runtime |

**Positive findings.** Legal entity, contracting-entity table and official contacts are published by the vendor. Release notes and the ADK changelog are dated and complete. The subprocessor list carries an update date and an archived version history.

**Recorded concerns.** SOC 2 Type II access is gated (sign-in and agreement-based confidentiality); SOC 3 is referenced but no public SOC 3 document was located for the evaluated components. Agent Runtime and ADK are not named on the SOC 2, ISO 27001, ISO 42001 or FedRAMP scope pages; the listed entries are "Gemini Enterprise Agent Platform (formerly Vertex AI Platform)", "Generative AI on Gemini Enterprise Agent Platform" and "Conversational Agents (formerly Dialogflow)".

### R — Resilience — 6/20 (Low)

CVE evaluation window: 2025-11-07 → 2026-11-07. Score source for every counted ID: CNA (GoogleCloud / Google) CVSS 4.0 — no NVD or CNA CVSS 3.1 vector exists for any of them (Attribution-CVE-002 order: NVD v3.1 → CNA v3.1 → CISA-ADP v3.1 → CNA v3.0 → CNA v4.0). CVE List state: PUBLISHED for all eight (no Convention-CVEReserved-001 note required).

| Criterion | Result | Score | Evidence URL |
|---|---|---|---|
| CVE count (trailing 12 months) | 8 (basis exact): CVE-2025-12952, CVE-2025-13427, CVE-2026-4810, CVE-2026-4764, CVE-2026-18236, CVE-2026-79707, CVE-2026-79696, CVE-2026-115522. 6–9 → 1; penalty −1 for CVSS 9.0+ present → 0 (min 0). | 0 | Incident Timeline below |
| Maximum CVSS severity | 10.0 — CVE-2026-79696, CNA CVSS 4.0 (computed 10.0; stated 10.0). Three further IDs at 9.0+: CVE-2026-4764 (9.4), CVE-2026-4810 and CVE-2026-18236 (computed 10.0 from base metrics; stated 9.3, CVSS-BT with E:P). | 0 | https://app.opencve.io/cve/CVE-2026-79696 |
| Patch response speed | Fixes preceded or coincided with public disclosure for every counted ID (hosted components patched server-side before the CVE record; ADK fixed releases 1.22.0, 1.28.1 / 2.0.0a2, 2.5.0, 2.7.0, 1.39.1 published before the corresponding CVE). ≤7d. | 3 | https://docs.cloud.google.com/dialogflow/docs/release-notes · https://github.com/google/adk-python/releases |
| Structural issues | Recurring: two unauthenticated code-injection CVEs in the same ADK component, the `adk web` development server, five months apart — CVE-2026-4810 (2026-04-13, CWE-306) and CVE-2026-79696 (2026-09-09, CWE-184 "Incomplete List of Disallowed Inputs"). The CWE-184 classification on the second record describes an incomplete disallow-list in the same component. | 0 | https://app.opencve.io/cve/CVE-2026-4810 · https://app.opencve.io/cve/CVE-2026-79696 |
| Supply chain compromise (trailing 12 months) | None confirmed against the vendor's own package, account, build pipeline or distribution endpoint. (a) LiteLLM 1.82.7 / 1.82.8 on PyPI carried unauthorized code on 2026-03-24 (10:39–16:00 UTC); LiteLLM is an opt-in ADK extra (`google-adk[eval]`, `[extensions]`); ADK 1.27.4 / 1.27.5 / 1.28.0 pinned an unaffected version — recorded as `dependency: BerriAI/litellm`. (b) Pillar Security's finding on `google/adk-python` GitHub Actions workflows (public 2026-08-03/04): prompt injection through a public issue or PR could invoke a privileged workflow and exfiltrate a bot personal access token; Google removed the three workflows (removal commit author date 2026-06-09; fix confirmed 2026-07-21 per Pillar). No unauthorized commit, merge, release or package publication is reported — "vulnerability only; no publicly confirmed write (SupplyChain-Criterion-001a)". | 3 | https://github.com/google/adk-python/issues/5005 · https://thehackernews.com/2026/08/google-deletes-3-adk-ai-workflows-after.html |

**Positive findings.** Google Cloud operates as a CNA and publishes CVE records with CVSS 4.0 vectors for hosted components; ADK fixes shipped before public disclosure in every counted case; the ADK maintainers posted a dependency-compromise advisory in the repository with rotation guidance and pinned releases.

**Recorded concerns.** Four of eight counted IDs score 9.0 or higher on CNA CVSS 4.0; two are unauthenticated remote code execution in the ADK development server and one is unauthenticated project-level privilege escalation via Dialogflow CX playbook import. ADK CVE records are published through the CVE List and the GitHub Advisory Database; the repository's own advisories page states "There aren't any published security advisories", and the Gemini Enterprise Agent Platform security-bulletins page does not list the ADK or Dialogflow CX CVEs (those appear in the Dialogflow release notes and the CVE List).

### D — Data Conduct — 13/15 (High)

| Criterion | Result | Score | Evidence URL |
|---|---|---|---|
| GDPR compliance disclosure | Confirmed: Cloud Data Processing Addendum with EU SCCs incorporated (Appendix 3), 30-day subprocessor notice, 180-day deletion maximum, Security Measures (Appendix 2); Google Cloud Privacy Notice (effective 2024-07-10) with a GDPR section naming Google Cloud EMEA Ltd. as controller for EU / UK / Swiss Service Data. | 3 | https://cloud.google.com/terms/data-processing-addendum · https://cloud.google.com/terms/cloud-privacy-notice |
| Data minimization | Default ON, easy opt-out: OpenTelemetry tracing is enabled by default for newly deployed ADK agents on Agent Runtime (release note 2026-06-18), disabled with `GOOGLE_CLOUD_AGENT_ENGINE_ENABLE_TELEMETRY=false`; durable and in-memory caching are on by default (≤24 h) with `cacheConfig` opt-out; request-response logging is off by default. Traces go to the customer's own Cloud Trace. Abuse-monitoring prompt logging for Google models is not configurable on the data-governance page. | 1 | https://docs.cloud.google.com/agent-builder/agent-engine/manage/tracing · https://docs.cloud.google.com/vertex-ai/generative-ai/docs/data-governance |
| AI training use | Not used + retention stated: Service Specific Terms §18 "Training Restriction (formerly Section 17)": "Google will not use Customer Data to train or fine-tune any AI/ML models without Customer's prior permission or instruction." Retention: cached data deleted no later than 24 hours after write; CDPA 180-day deletion maximum. | 4 | https://cloud.google.com/terms/service-terms · https://docs.cloud.google.com/vertex-ai/generative-ai/docs/data-governance |
| Sub-processor transparency | List with update date (2026-10-19) and advance-notice mechanism via Essential Contacts. | 3 | https://cloud.google.com/terms/subprocessors |
| Data retention disclosure | Per-category: caching ≤24 h; Grounding with Google Search logs ≤3 days; Google Maps grounding 30 days; CodeMender / Deep Research sessions 7 days; sandbox TTL 7–14 days; Service Data up to 180 days (Privacy Notice); billing data ≥5 years. | 2 | https://docs.cloud.google.com/vertex-ai/generative-ai/docs/data-governance · https://docs.cloud.google.com/gemini-enterprise-agent-platform/scale/sandbox |

**Positive findings.** The no-training commitment is contractual and active by default for enterprise customers; retention is stated per feature; the subprocessor list is dated and version-archived; the DPA incorporates SCCs.

**Recorded concerns.** Operational tracing is on by default for new ADK deployments; abuse-monitoring prompt logging for Google models is described as non-configurable; the page states that some Advanced AI features may not support zero data retention. For Anthropic-managed Claude deployments, the trust page records that Anthropic operates the stack as processor under Anthropic's commercial terms.

### I — Identity & Control — 6/10 (Mid)

| Criterion | Result | Score | Evidence URL |
|---|---|---|---|
| Emergency stop documentation | Documented but incomplete: deployed agents can be deleted and revisions / traffic managed through the Agent Runtime docs and `gcloud`; sandboxes carry TTLs and deletable snapshots. No documented immediate-stop control for an in-flight invocation was located. | 2 | https://docs.cloud.google.com/gemini-enterprise-agent-platform/build/runtime · https://docs.cloud.google.com/gemini-enterprise-agent-platform/scale/sandbox |
| Human-in-the-loop design | Optional: ADK tool confirmation is enabled per tool via `require_confirmation` (Python v1.14.0+), marked Experimental; not enabled by default. CVE-2026-18236 (tool-confirmation forgery, <2.5.0) concerned this mechanism and is fixed. CodeMender (Preview, 2026-07-21) enforces mandatory confirmation for disk writes, but CodeMender is outside the bound scope. | 1 | https://adk.dev/tools-custom/confirmation/ · https://app.opencve.io/cve/CVE-2026-18236 |
| Permission delegation transparency | Scope + delegation targets documented: Agent Identity (`principal://TRUST_DOMAIN/NAMESPACE/AGENT_NAME`, SPIFFE-based, IAM allow / deny and principal access boundary policies; parent-to-subagent delegation requires `roles/agentregistry.viewer` and `roles/aiplatform.user` on the parent identity; mTLS-bound tokens); default service agent role `roles/aiplatform.reasoningEngineServiceAgent` and BYOSA documented. | 3 | https://docs.cloud.google.com/gemini-enterprise-agent-platform/scale/runtime/agent-identity · https://docs.cloud.google.com/gemini-enterprise-agent-platform/scale/runtime/manage-agent-access |

**Positive findings.** Per-agent identity with token binding and delegation roles is documented in detail (page updated 2026-10-15). Default and custom service accounts are documented with VPC-SC ingress requirements.

**Recorded concerns.** Human confirmation is opt-in per tool and experimental; no platform-level kill switch for running invocations is documented; agents deployed without the identity flag continue to use service accounts.

### C — Containment — 3/10 (Low)

| Criterion | Result | Score | Evidence URL |
|---|---|---|---|
| Sandbox design | Hybrid: sandboxes run in gVisor-isolated containers in a Google-managed tenant project; code-execution sandboxes have no outbound internet or VPC access and template-backed sandboxes default to `internet_access: False`; when enabled, egress reaches public IPs with RFC 1918 and metadata ranges blocked (blocklist); domain allowlisting is not built in and requires VPC routing with Cloud NGFW or Secure Web Proxy. The Dialogflow CX Playbook Code Block runtime had unrestricted outbound internet access until remediation in June 2026 (Varonis). | 2 | https://docs.cloud.google.com/gemini-enterprise-agent-platform/scale/sandbox · https://www.varonis.com/blog/rogue-agent-dialogflow-attack |
| Least privilege | Configurable: the default service agent holds `roles/aiplatform.reasoningEngineServiceAgent`; Unit 42 (2026-03-31) recorded that the default permissions allowed read access to all Cloud Storage buckets in the consumer project and downloads from a Google-owned Artifact Registry, and that default OAuth scopes were broad and non-editable; Google revised its access-control documentation and recommends BYOSA; Agent Identity offers per-agent least privilege for agents deployed with the identity flag. | 1 | https://docs.cloud.google.com/gemini-enterprise-agent-platform/scale/runtime/manage-agent-access · https://unit42.paloaltonetworks.com/double-agents-vertex-ai/ |
| Tenant isolation (cloud) | Past cross-tenant breach on the hosting platform: CVE-2025-11915 (streaming responses misrouted between recipients, 2025-09-23 → 2025-09-28, third-party MaaS and self-deployed model endpoints; bulletin GCP-2025-059) and CVE-2026-2473 (predictable staging bucket names enabling cross-tenant code execution, Vertex AI Experiments; bulletin GCP-2026-012, 2026-02-20). Both sit outside the bound component scope but on the same platform tenancy model; both were remediated server-side with no customer action. In-window research on in-scope components recorded intra-project (not cross-customer) boundary findings: Rogue Agent (shared Code Block execution environment per project; VPC-SC perimeter bypass via unrestricted egress; disclosed to Google 2025-11, initial fix 2026-04, full remediation 2026-06) and Double Agents (service-agent credentials reaching the Google-managed tenant project and producer registry). | 0 | https://docs.cloud.google.com/vertex-ai/generative-ai/docs/security-bulletins · https://docs.cloud.google.com/gemini-enterprise-agent-platform/machine-learning/security-bulletins · https://www.varonis.com/blog/rogue-agent-dialogflow-attack |

**Positive findings.** gVisor isolation, no ambient credentials inside sandboxes, metadata-range blocking and VPC Service Controls support (Agent Gateway enforcing VPC-SC perimeter rules since 2026-09-09) are documented; the Code Block finding was remediated without customer action.

**Recorded concerns.** The platform's record includes one confirmed cross-recipient data exposure (CVE-2025-11915) and one cross-tenant RCE vulnerability (CVE-2026-2473) in the prior and current windows; in-scope research found that a per-project shared execution environment and default service-agent permissions crossed boundaries that customers could not observe in Cloud Logging at the time.

### T — Transparency — 7/10 (High)

| Criterion | Result | Score | Evidence URL |
|---|---|---|---|
| CVE publication posture | Issues CVEs + advisories: GoogleCloud / Google CNA records with CVSS 4.0 vectors; Google Cloud security bulletins; Dialogflow release-note security entries; GitHub Advisory Database entries for ADK. | 2 | https://docs.cloud.google.com/support/bulletins · https://github.com/advisories/GHSA-rg7c-g689-fr3x |
| Incident disclosure speed | Elapsed time from fix to public notice, in-scope items: CVE-2026-4810 11 d (fix 1.28.1 2026-04-02 → CVE 2026-04-13); CVE-2026-18236 13 d; CVE-2026-79696 27 d; CVE-2026-4764 53 d (patched 2026-03-15 → release note 2026-05-07); CVE-2026-115522 62 d; CVE-2025-13427 113 d (fixed 2025-08-20 → release note 2025-12-11); CVE-2026-79707 239 d (fix 1.22.0 2026-01-08 → CVE 2026-09-04); CVE-2025-12952 ≈ 10 months (fix 2025-02 → CVE 2025-12-10). Staging-bucket SDK issue: fix and release-note security entry on the same day (2026-03-31). Rogue Agent and Double Agents: no vendor bulletin located; public disclosure by the researchers. Median ≈ 50 days → 31–60 d. | 1 | https://docs.cloud.google.com/dialogflow/docs/release-notes · https://docs.cloud.google.com/gemini-enterprise-agent-platform/release-notes |
| Security policy publication | Detailed technical + organizational measures: CDPA Appendix 2 (Security Measures), Dialogflow compliance and security controls page (CMEK, VPC-SC, Access Transparency, data residency), sandbox security documentation. | 2 | https://cloud.google.com/terms/data-processing-addendum · https://docs.cloud.google.com/dialogflow/docs/compliance-security-controls |
| AI safety framework reference | External framework adopted: ISO/IEC 42001:2023 certification covering Gemini Enterprise Agent Platform and Generative AI on the platform; Google's Secure AI Framework (SAIF) with NIST collaboration and CoSAI. | 2 | https://cloud.google.com/security/compliance/iso-42001 · https://safety.google/intl/en/cybersecurity-advancements/saif |
| AI system identity disclosure | Not confirmed: the Generative AI Prohibited Use Policy prohibits impersonation without disclosure and misrepresenting provenance "in order to deceive", but no default AI-identity disclosure to end users and no documented setting for Agent Runtime or Dialogflow CX Messenger was located. | 0 | https://policies.google.com/terms/generative-ai/use-policy |

**Positive findings.** Google Cloud publishes CNA records, bulletins and release-note security entries; ISO/IEC 42001 certification and SAIF are published; the sandbox documentation states its own limitations (no in-guest intrusion detection, no automatic pre-deployment scanning).

**Recorded concerns.** Fix-to-disclosure intervals exceeded 60 days for three of eight counted IDs; the ADK CVEs are absent from the platform security-bulletins page and from the repository's advisories page; no end-user AI-identity disclosure control was located.

## Incident Timeline

Counted (in scope, inside window). CVSS values are CNA CVSS 4.0; no CVSS 3.1 vector exists for any ID.

| Date (first public disclosure) | CVE ID | CVSS | Description | Patch status | KEV |
|---|---|---|---|---|---|
| 2025-12-10 | CVE-2025-12952 | 8.7 High (CNA v4.0; computed 8.7; stated 8.7) | Dialogflow CX: agent developers with Webhook editor permission could configure webhooks with the Dialogflow service agent's access token, escalating from agent-level to project-level access (CWE-269). The 2025-06-12 release note discontinued service-agent tokens without identifying a vulnerability; window entry is the CVE date. | Server-side fix 2025-02; no customer action | No |
| 2025-12-11 | CVE-2025-13427 | 6.9 Medium (CNA v4.0; computed 6.9; stated 6.9) | Dialogflow CX Messenger: unauthenticated users could interact with restricted chat agents, access knowledge and trigger intents (CWE-287). First disclosure: Dialogflow release-note Security entry 2025-12-11; CVE published 2025-12-18. | Versions after 2025-08-20 protected; no user action | No |
| 2026-04-13 | CVE-2026-4810 | 9.3 Critical stated (CNA v4.0 CVSS-BT with E:P); computed 10.0 from base metrics | ADK Python 1.7.0 – <1.28.1 and 2.0.0a1 – <2.0.0a2: code injection and missing authentication in `adk web` allow an unauthenticated remote attacker to execute code on the hosting server (CWE-306). | Fixed 1.28.1 (2026-04-02), 2.0.0a2 (2026-03-27); redeploy required | No |
| 2026-05-07 | CVE-2026-4764 | 9.4 Critical (CNA v4.0; computed 9.4; stated 9.4) | Dialogflow CX: missing authorization in playbook import lets an authenticated user with specific roles escalate privileges and potentially take over the Google Cloud project (CWE-862). First disclosure: release-note Fixed entry 2026-05-07; CVE published 2026-06-11. | Patched 2026-03-15; no customer action | No |
| 2026-07-29 | CVE-2026-18236 | 9.3 Critical stated (CNA v4.0 CVSS-BT with E:P); computed 10.0 from base metrics | ADK Python <2.5.0: continuation forgery in tool confirmations — an attacker who can inject events into session history can execute unauthorized tools (CWE-863). | Fixed 2.5.0 (2026-07-16) | No |
| 2026-09-04 | CVE-2026-79707 | 8.7 High (CNA v4.0; computed 8.7; stated 8.7) | ADK Python 1.9.0 – 1.21.0: path traversal in the builder endpoint allows an unauthenticated remote attacker to read arbitrary files (CWE-22). | Fixed 1.22.0 (2026-01-08) | No |
| 2026-09-09 | CVE-2026-79696 | 10.0 Critical (CNA v4.0; computed 10.0; stated 10.0) | ADK Python 2.0.0 – 2.6.0: code injection in `adk web` via a crafted test session replay when pytest is installed; unauthenticated remote code execution (CWE-184). | Fixed 2.7.0 (2026-08-13) | No |
| 2026-10-28 | CVE-2026-115522 | 5.3 Medium (CNA v4.0; computed 5.3; stated 5.3) | ADK Python 1.19.0 – <1.39.1 and 2.0.0a1 – <2.7.0: `FileArtifactService` omitted `app_name` from on-disk paths, letting one application list, read, overwrite or delete another's artifacts under a shared root and user ID (CWE-668). | Fixed 1.39.1 (2026-08-27), 2.7.0 (2026-08-13) | No |

Recorded, not counted.

| Date | ID / marker | CVSS | Description | Status | KEV |
|---|---|---|---|---|---|
| 2025-10-21 | CVE-2025-11915 — out of window; out of component scope (Vertex AI MaaS and self-deployed model endpoints) | 6.9 Medium (CNA v4.0) | HTTP desynchronization at proxies handling `Expect: 100-continue`: some streaming responses were delivered to other recipients, 2025-09-23 → 2025-09-28; Gemini models and private endpoints not affected (bulletin GCP-2025-059). Recorded by the prior record as "no CVE". | Remediated 2025-09-28; no customer action | No |
| 2026-02-20 | CVE-2026-2473 — out of component scope (Vertex AI Experiments, `google-cloud-aiplatform` 1.21.0 – <1.133.0) | 7.7 High (CNA v4.0; computed 7.7; stated 7.7) | Predictable Cloud Storage bucket names allow an unauthenticated attacker to pre-create buckets ("bucket squatting"), enabling cross-tenant code execution, model theft and poisoning (CWE-340; bulletin GCP-2026-012). Counted by the prior record. | Mitigated in 1.133.0; no customer action | No (operator feed check 2026-11-07) |
| 2026-02-20 | CVE-2026-2472 — out of component scope (Vertex AI SDK evaluation visualization) | 8.1 High (NVD v3.1 per OpenCVE) | Stored XSS in `_genai/_evals_visualization` executing in Jupyter / Colab (bulletin GCP-2026-011). | Fixed 1.131.0 (2025-12-16); customer update required | No |
| 2026-03-31 | Unit 42 "Double Agents" — no CVE; in scope (Agent Engine / Agent Runtime) | — | Default service-agent permissions on deployed ADK agents allowed credential extraction via the metadata service, read access to all project buckets, and downloads from a Google-owned Artifact Registry; tenant-project deployment artifacts observed. Google revised access-control documentation and recommends BYOSA. No cross-customer data access demonstrated. | Documentation and deployment-workflow changes; dates not published | — |
| 2026-03-31 | Release-note security entry — no CVE; out of component scope (`google-cloud-aiplatform` SDK staging bucket) | — | "Security update for Cloud Storage staging bucket verification" — Unit 42 "Pickle in the Middle" (published 2026-06-16): predictable default staging bucket with ownership check absent; reported 2026-03-05; UUID suffix 1.144.0 (2026-03-31), ownership verification 1.148.0 (2026-04-15). | Fixed; SDK upgrade advised | — |
| 2026-03-24 | `dependency: BerriAI/litellm` — PYSEC-2026-2; not a vendor compromise | — | Unauthorized code in LiteLLM 1.82.7 / 1.82.8 on PyPI (10:39–16:00 UTC); LiteLLM is an opt-in ADK extra. ADK 1.27.4 / 1.27.5 / 1.28.0 pinned an unaffected version; repository advisory with rotation guidance. | Resolved in ADK 1.27.4+ | — |
| 2026-07-07 | Varonis "Rogue Agent" — no CVE; in scope (Dialogflow CX Playbooks Code Blocks) | — | Any principal with `dialogflow.playbooks.update` on one Code Block-enabled agent could overwrite the shared `code_execution_env.py` used by every such agent in the same project; overwrite not captured in Cloud Logging; unrestricted outbound internet from the shared Cloud Run environment (VPC-SC perimeter bypass); reachable IMDS exposing a low-privilege managed service-account token. Reported 2025-11; initial fix 2026-04; full remediation 2026-06. Intra-project scope; no cross-customer access described; no exploitation reported. | Remediated 2026-06; no customer action | — |
| 2026-07-20 | CVE-2026-19486 — out of bound component scope (Agent Studio App Builder, a sibling component of the Agent Platform) | 8.7 High (CNA v4.0) | SSRF in App Builder let an unauthenticated attacker leak the Compute Engine default service account token (affected 2025-10-11 – <2026-06-01). First disclosure: release note 2026-07-20; CVE 2026-09-11. | Patched 2026-06-01; previously deployed apps must be redeployed | No |
| 2026-08-03 | Pillar Security — ADK repository CI workflows; no CVE; "vulnerability only; no publicly confirmed write (SupplyChain-Criterion-001a)" | — | Prompt injection through a public issue or PR could cause a low-privilege triage agent to invoke a privileged workflow, with code execution on the CI runner and exfiltration of a bot PAT in the proof of concept. Google removed the three workflows (removal commit author date 2026-06-09; fix confirmed 2026-07-21). No unauthorized merge, release or package publication reported. | Workflows removed | — |
| 2026-09-30 | Dialogflow CX release-note Fixed entry — no CVE; in scope | — | Sensitive authentication tokens in session parameters could be returned in cleartext through DetectIntent responses; server-side redaction. | Fixed server-side; no customer action | — |
| 2026-10-23 | CVE-2026-107858 — out of bound component scope (ADK for Java, `google/adk-java`; `google-adk-dev` 0.1.0 – <1.13.0) | 7.2 High (CNA v4.0) | Missing WebSocket origin validation and permissive CORS in the ADK Web development server for Java (CWE-1385, CWE-942). | Fixed 1.13.0 | No |

## Contextual Analysis

Evidence rule: every factual claim in this report was confirmed by web retrieval during the evaluation session (2026-11-07); where a page could not be read, the report says so.

**Operator of record and renaming.** The vendor's contracting-entity page names Google LLC (Mountain View) as the default Google entity for Google Cloud Platform agreements, with affiliates by billing location; Google LLC is a subsidiary of Alphabet Inc. (ultimate parent, no controlling owner). On 2026-04-22 Google announced Gemini Enterprise Agent Platform as the evolution of Vertex AI; the vendor's name-changes page (updated 2026-11-05) maps "Vertex AI" → "Agent Platform" and "Vertex AI Agent Engine" → "Agent Runtime on Gemini Enterprise Agent Platform", and the former Agent Builder overview URL now serves "Agent Platform overview" (updated 2026-11-07) listing Agent Runtime, the Agent Development Kit and Agent Garden. "Vertex AI Agent Builder" does not appear on the name-changes page as a line item. Dialogflow CX is listed on compliance pages as "Conversational Agents (formerly Dialogflow)"; its release notes still use "Dialogflow CX". `target_version` is re-bound to the three components under their current names.

**Attribution.** The prior record's product category is the agent-building suite, and the bound components are Agent Runtime, ADK Python and Dialogflow CX. CVE-2026-2473 and CVE-2026-2472 name Vertex AI Experiments and the SDK evaluation visualizer as affected products; CVE-2026-19486 names App Builder in Agent Studio; CVE-2026-107858 names ADK for Java. These are recorded with their scope determination and are not counted. Operations may re-bind the scope (for example, to include App Builder and ADK Java); the count would then be 10 and the maximum unchanged.

**Resilience in context.** Google Cloud's own record for the components shows prompt fixes: every counted CVE was fixed before or at public disclosure, hosted components were patched server-side without customer action, and the ADK maintainers published a dependency-compromise advisory the same week LiteLLM's compromised versions were removed. The concentration of critical findings in the `adk web` development server — a component the vendor documents for local development — is the main driver of the R score; the two code-injection records in that component are separated by five months and the second is classified as an incomplete disallow-list. Dialogflow CX's record in the window is two privilege-escalation CVEs and one authentication bypass, all remediated server-side before disclosure, with fix-to-disclosure intervals of 53 days, roughly 10 months and 113 days respectively.

**Containment in context.** The platform documents gVisor isolation, no ambient credentials in sandboxes, metadata-range blocking and VPC Service Controls support, and Agent Identity offers token-bound, per-agent least privilege. The in-window research from Unit 42 (Double Agents, 2026-03-31) and Varonis (Rogue Agent, 2026-07-07) records that default service-agent permissions and a per-project shared Code Block runtime crossed boundaries customers could not observe at the time; neither report demonstrates access to another customer's data, and Google remediated the Code Block runtime by June 2026 and revised access-control documentation. The tenant-isolation criterion is scored on the platform's confirmed cross-recipient exposure of September 2025 (CVE-2025-11915) and the February 2026 cross-tenant vulnerability (CVE-2026-2473), both of which sit on components outside the bound scope but on the same tenancy model; the prior record scored the same two incidents.

**Data conduct in context.** The contractual training restriction is unchanged in wording and now sits at Service Specific Terms §18. The vendor's data-governance page (updated 2026-11-07) states retention per feature and documents how to reach zero data retention; it also states that abuse-monitoring prompt logging applies to Google models and that some Advanced AI features may not support zero retention. Tracing for new ADK deployments on Agent Runtime defaults to on since 2026-06-18, with a documented environment-variable opt-out, and the destination is the customer's own Cloud Trace.

**Verifiability in context.** SOC 2 Type II, ISO/IEC 27001 and ISO/IEC 42001 documents are obtained through the Compliance Reports Manager; the vendor states that select resources require sign-in and that confidential resources are shared under the customer agreement's confidentiality obligations. Under the framework's criterion this is customers-only access, not public availability. Agent Runtime and ADK are not named individually on the SOC 2, ISO 27001, ISO 42001 or FedRAMP scope pages; "Gemini Enterprise Agent Platform (formerly Vertex AI Platform)" is listed, and FedRAMP High is listed for Dialogflow CX on its compliance page. The HIPAA covered-services list names Gemini Enterprise Agent Platform, Generative AI on Agent Platform and Conversational Agents.

**Vendor's position.** Google states that all hosted-component CVEs in the window were mitigated server-side with no customer action; that the training restriction is active by default for enterprise customers; that sandboxed code does not inherit the agent's identity; and that Agent Identity binds tokens to the runtime through mTLS. Google characterized Pillar Security's CI finding as a demonstration that required social engineering and did not meet its bug-bounty bar, and hardened the repository.

**Source coverage (SourceCoverage-001).** Vendor security bulletins consulted: Google Cloud security bulletins (`/support/bulletins`), Gemini Enterprise Agent Platform security bulletins (machine-learning and generative-ai pages), Dialogflow release notes, Agent Platform release notes, ADK `SECURITY.md` and repository advisories page (states no published advisories), repository issue #5005. No `/trust` or status-page incident entry naming the evaluated components was located for the window ("none located"). The NVD detail pages are client-rendered and did not return record content to the session's tools; CVE List state, CNA vectors and NVD status were read from per-CVE trackers (OpenCVE, Vulnerability-Lookup, GitHub Advisory Database) that mirror the CVE List and NVD records.

**Framework note.** All counted IDs carry CNA CVSS 4.0 only; the Attribution-CVE-002 order ends at CNA v4.0, and the report states the version on every value. For CVE-2026-4810 and CVE-2026-18236 the CNA vector carries the threat metric E:P, so the stated score (9.3, CVSS-BT) differs from the base-metric computation (10.0); both values are recorded.

## VERDICT Record

**Summary.** Gemini Enterprise Agent Platform (formerly Vertex AI Agent Builder), operated by Google LLC (Alphabet Inc.), scores 51/85 (Tier B) on this update, down from 65/85: eight in-scope CVEs in the trailing 12 months, four at CNA CVSS 4.0 ≥ 9.0, alongside a contractual no-training commitment, a dated sub-processor list, SCC-backed DPA and per-agent identity documentation.

**Risk Factor Summary by Use Case**

| Use case | Recorded factors |
|---|---|
| Internal testing | ADK `adk web` development server carried two unauthenticated code-injection CVEs (CVE-2026-4810, CVE-2026-79696) and an arbitrary file read (CVE-2026-79707); fixed in 1.28.1 / 2.7.0 / 1.22.0. ADK Java's development server carried CVE-2026-107858 (out of bound scope). |
| Credential-handling workloads | Default service-agent permissions and non-editable OAuth scopes recorded by Unit 42 (2026-03-31); Agent Identity with mTLS-bound tokens and BYOSA documented as the least-privilege paths; Dialogflow CX webhook and playbook privilege-escalation CVEs remediated server-side; cleartext token return in DetectIntent responses fixed 2026-09-30. |
| Cloud multi-tenant | Platform-level cross-recipient exposure (CVE-2025-11915, Sep 2025) and cross-tenant vulnerability (CVE-2026-2473, Feb 2026) on out-of-scope components; in-scope research recorded intra-project shared runtime (Rogue Agent, remediated 2026-06) with no cross-customer access described; gVisor sandboxes and VPC-SC support documented. |
| Regulated-data workloads | ISO/IEC 27001, SOC 2 Type II (gated access), ISO/IEC 42001, HIPAA coverage for Gemini Enterprise Agent Platform and Conversational Agents, FedRAMP High for Dialogflow CX; Agent Runtime and ADK not named individually on scope pages; CMEK and data residency documented for CX; abuse-monitoring prompt logging for Google models not configurable. |

**Reference Information (options, not instructions)**

1. Readers running ADK locally may wish to compare their installed `google-adk` version against the fixed versions recorded above (1.22.0, 1.28.1, 2.5.0, 2.7.0, 1.39.1 / 2.7.0) and the optional LiteLLM extra against the 2026-03-24 advisory.
2. Readers deploying to Agent Runtime may wish to review the Agent Identity and BYOSA documentation against their IAM requirements, and the `GOOGLE_CLOUD_AGENT_ENGINE_ENABLE_TELEMETRY` default for new deployments.
3. Readers with certification scope requirements may wish to request the SOC 2 Type II and ISO scope statements through the Compliance Reports Manager to confirm whether Agent Runtime is named.

**Bias Disclosure**

"This evaluation uses Claude (Anthropic) as its tooling. Anthropic operates in the AI agent market and may compete with some evaluated vendors. VERDICT discloses this relationship in every report and applies identical evaluation criteria to all platforms regardless of their relationship to Anthropic."

VERDICT additionally discloses a parent-identity relationship (Trigger 1). The evaluated platform is operated by Google LLC, a subsidiary of Alphabet Inc., and Google is a material Anthropic equity-holder as recorded in KNOWN_FACTS.md: Google holds a strategic equity position in Anthropic with publicly disclosed investment exceeding USD 2 billion (announced 2023-10, with subsequent additional commitments reported through 2024–2025; https://www.anthropic.com/news). Bloomberg reported on 2026-04-24, and Axios confirmed, that Google is committing USD 10 billion in cash at a USD 350 billion valuation with up to USD 30 billion more contingent on performance targets, and CNBC reported the same day that the companies confirmed the investment; these figures are cited as reported by the named outlets, not as disclosed by either party, and Google's membership of the material set does not depend on them (https://www.bloomberg.com/news/articles/2026-04-24/google-plans-to-invest-up-to-40-billion-in-anthropic ; https://www.axios.com/2026/04/24/google-amazon-anthropic-investment ; https://www.cnbc.com/2026/04/24/google-to-invest-up-to-40-billion-in-anthropic-as-search-giant-spreads-its-ai-bets.html). The relationship is recorded as `evaluator-coi` + `direct-investment`. Identical evaluation criteria were applied regardless of this relationship.

Product-level integration, separately: Claude models are available on Gemini Enterprise Agent Platform as one of several third-party model options (the vendor's name-changes page lists "Claude/Llama/Deepseek/etc on Vertex AI" → "[Model Name], available on Gemini Enterprise Agent Platform"; Claude Sonnet 5.5 and Claude Haiku 5.5 were added to Model Garden on 2026-09-28 and 2026-10-07 per the release notes). This is a model-provider relationship and not itself a conflict.

Triggers 0, 2 and 3 were assessed and do not fire: the operator is not Anthropic; the chain of control ends at Alphabet Inc., a publicly traded company with no publicly recorded controlling owner and no recorded material investor from the set {Amazon, Microsoft, NVIDIA} on its board or as lead / strategic investor; Anthropic's use of Google Cloud compute is a supplier relationship of the industry-standard kind listed as a non-trigger.

## Future Evaluation Plan

- Layer 1 (behavioral testing): not scheduled; a free-tier run protocol for a managed enterprise runtime has not been ratified. E remains null.
- Layer C: interrupt lane active (T1 for any CVE ≥ 7.0 against Agent Runtime, ADK Python or Dialogflow CX; T2 on KEV listing; T5 on further renaming or operator change). Routine review 365 days from `updated_at` 2026-11-07, computed by the pipeline (`next_review_due`).
- Operations note: a scope re-binding decision (App Builder, ADK Java) and the record name normalization ("Gemini Enterprise Agent Platform (formerly Vertex AI Agent Builder)") are flagged for Operations under the Category line normalization rule.

## Evaluation History

| Date | Type | Score | Tier | Framework |
|---|---|---|---|---|
| 2026-03-26 | Initial (migrated capture) | 65/85 | S | v0.3.1 |
| 2026-11-07 | Update | 51/85 | B | v0.3.2 |

Sources: see Evidence URL columns and Incident Timeline; all retrieved 2026-11-07.
