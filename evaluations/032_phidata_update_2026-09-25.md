# VERDICT Evaluation Report #032
## Agno (formerly Phidata)

Evaluation type: Update
Evaluation date: 2026.09.25
Evaluator: VERDICT by ZinovaCreation
Target version: agno 3.0.11 (PyPI `agno`, released 2026-09-23; github.com/agno-agi/agno) — the Agno SDK and AgentOS runtime as distributed via PyPI. The legacy `phidata` package and repository (agno-agi/phidata) are the operator's predecessor artifacts and are excluded from CVE attribution; the hosted Control Plane (os.agno.com) is recorded as operator-side evidence under D / C and is not scored as the target.
Framework: VERDICT v0.3.2
Previous evaluation: 2026-03-31 (Initial, Layer 0, 38/85, Tier C, v0.3.1)
Disclosure layer (Trigger 0/1/2/3): None. The operator is Agno Inc.; its only recorded funding is a USD 5.4M seed round on 2024-08-29 with three venture investors including GreatPoint Ventures (CB Insights, secondary), and no Amazon / Google / Microsoft / NVIDIA equity, board or non-arms-length channel relationship appears in the sources consulted. Product level only: Anthropic is one of two AI service providers named in the operator's Privacy Notice; a model-provider relationship is not a disclosure trigger.
Evaluator model: claude-fable-5-1


## Executive Summary

Four product-scoped CVEs were published against Agno in the trailing 12 months (2025-09-25 → 2026-09-25), the highest being CVE-2026-35002, an eval()-based arbitrary code execution flaw rated CVSS 9.8 by NIST and fixed in v2.3.24 on 2026-01-08, 84 days before the CVE was published. The total moves from 38/85 (2026-03-31) to 40/85 and the tier stays C, but the composition changes: R falls from 14 to 4 on the CVE count with the 9.0+ penalty, the maximum-CVSS band, a 77-day interval between the public report of the ClickHouse SQL injection (CVE-2026-10105, issue #7866 opened 2026-05-11) and its release fix (v2.8.5, 2026-07-27), and a path-containment weakness class fixed separately in four components, while V rises from 11 to 16 and D from 3 to 7 on the legal pages now published by Agno Inc. — a New York-registered entity per its Terms of Service — which carry a dated third-party vendor list, GDPR legal bases and per-category retention. I, C and T each rise by one point on documented run cancellation, JWT-based RBAC scopes, base-directory containment defaults and the maintainer-published advisory for CVE-2025-64168. The record also corrects prior-record facts: the operator has published as Agno Inc. since at least its January 2025 Terms, the repository license is Apache-2.0, and two CVEs (CVE-2025-8665, CVE-2025-64168) already existed inside the prior record's window when it recorded zero.


## Scorecard

| Dimension | Score | Max | Rating |
|---|---|---|---|
| V Verifiability | 16 | 20 | High |
| E Effectiveness | N/A | 15 | Layer 1 pending |
| R Resilience | 4 | 20 | Low |
| D Data Conduct | 7 | 15 | Mid |
| I Identity & Control | 6 | 10 | Mid |
| C Containment | 4 | 10 | Mid |
| T Transparency | 3 | 10 | Low |
| **Total (Layer 0)** | **40** | **85** | |

Tier: C
Category: Agent Framework & Runtime · Open-Source (Apache 2.0) · Operator: Agno Inc.

CISA KEV: None — KEV catalog version 2026.09.24 (1,723 entries; read from the cisagov/kev-data mirror of known_exploited_vulnerabilities.json) contains no entry for CVE-2025-64168, CVE-2026-35002, CVE-2026-10105, CVE-2026-76832 or CVE-2025-8665, and no vendorProject/product "Agno" or "Phidata".


## Differential

**Previous evaluation:** 2026-03-31, 38/85, Tier C, framework v0.3.1, evaluator model unrecorded, migrated capture (`qa` unresolved ×3).
**Lane:** Interrupt (T1) with folded routine scope. The prompt listed three T1 events; enumeration of OSV/NVD found a fourth (CVE-2026-76832, published 2026-08-19), also T1.
**Dimension states:** V re-evaluated · R re-evaluated · D re-evaluated · I re-evaluated · C re-evaluated · T re-evaluated · E null (Layer 0).
**Carry-forward checks:** None possible. The prior record's `sources` are five organization-level URLs (docs.phidata.com/introduction, github.com/agno-agi, github.com/agno-agi/agno, github.com/agno-agi/phidata, agno.com) with no per-dimension citations, so carry-forward condition 1 cannot be evaluated per dimension. Independently, the license (MPL 2.0 → Apache-2.0, February 2026), the operator's published name (Phidata Inc. → Agno Inc.) and the telemetry endpoint (api.phidata.com → os-api.agno.com) changed, which re-opens D, I and C on condition 3. The R-only change (−10) also exceeds the 3-point escalation threshold.
**Trailing window for R:** 2025-09-25 → 2026-09-25. CVE-2025-8665 (NVD published 2025-08-06) falls outside the window by 50 days and is excluded from the count.
**Attribution scope decision:** `target_version` is bound to the PyPI `agno` package and the agno-agi/agno repository. The legacy `phidata` package/repository is excluded; no CVE assigned against a `phidata` version appeared in the OSV results for "agno" (a separate OSV query for "phidata" was not run in this session [UNVERIFIED]).
**KEV check:** Performed against catalog 2026.09.24 (mirror cisagov/kev-data): no entries by CVE ID or vendor/product.
**Post-draft evidence (2026-09-25):** The operator supplied browser captures of os.agno.com/legal/privacy (Last updated April 20, 2026) and os.agno.com/legal/tos (Last updated January 21, 2025), which the engine's tooling could not render. V (identity; third-party disclosure) and D (GDPR; sub-processors; retention) were re-scored before publication: draft 29 → 40, Tier D → C. AI training use stays 0 (no statement in the notice).
**Prior-record omissions (stated as facts):**
1. CVE-2025-8665 (published 2025-08-06, Medium) was inside the prior window (2025-03-31 → 2026-03-31) and is not carried in the prior record.
2. CVE-2025-64168 / GHSA-vw84-hprm-cxmm (published 2025-10-31, High) was inside the prior window and is not carried in the prior record. The prior `cve_count_12mo: 0` (basis `exact`) did not match the public record at capture; the "Zero CVEs" language in the prior body, finding, key_finding and descriptions is replaced.
3. The prior category line "OSS (MPL 2.0)" post-dates the vendor's February 2026 license change; the license was Apache-2.0 at the prior evaluation date.
4. The prior `sources` entry docs.phidata.com/introduction is superseded by docs.agno.com (current documentation host).
5. The Terms of Service dated 2025-01-21 already name "Agno Inc., a company registered in New York"; the prior record's `operator: Phidata Inc.` (captured 2026-03-31) post-dates that document by 14 months. The same Terms reference a Privacy Policy at agno.com/privacy; whether that URL resolved on 2026-03-31 was not verified.
**T5 (rename / operator):** Fired. Public notices name Agno Inc. (Terms of Service, Privacy Notice §16, agno.com footer, LICENSE, PyPI author "Agno Team <hello@agno.com>"). Registration jurisdiction confirmed from the Terms: New York, United States; postal address 169 Madison Ave STE 2420, New York, NY 10016. `operator` set to Agno Inc.; `independence: independent`; `parent_entity: null`.
**KNOWN_FACTS.md:** An entity entry for Agno / Agno Inc. (formerly Phidata / Phidata Inc.) was ratified separately by Engine as KnownFacts-Agno-001 (rev.1) after this evaluation was drafted; it is not applied in this record (`known_facts_applied: []`) and takes effect for the next Agno report once committed.
**Prompt reconciliation:** (a) "fixed 2.6.6" for CVE-2026-10105 is not supported by primary sources: the v2.6.6 notes (2026-05-14) contain no ClickHouse fix, the GHSA lists no patched version, and PR #7883 appears in the v2.8.5 notes. (b) CVE-2025-8665 publication date is 2025-08-06 on NVD, not 2025-09-18; outside the current window either way. (c) The "finder credited to Palo Alto Networks" note for CVE-2026-35002 was not found on the NVD, OSV or VulnCheck records read; not stated.
**Special Consideration 1 (elapsed times, first public record → fix release):**

| CVE | First public record | Fix commit | Fix release | Elapsed |
|---|---|---|---|---|
| CVE-2025-64168 | 2025-10-31 (maintainer GHSA) | — | 2.2.2, 2025-10-29 | fix preceded advisory by 2 d |
| CVE-2026-35002 | 2026-04-02 (CVE, VulnCheck) | cbf6755, 2026-01-07 | 2.3.24, 2026-01-08 | fix preceded CVE by 84 d |
| CVE-2026-76832 | 2026-08-19 (CVE, VulnCheck) | 710d7e7, 2026-01-07 | 2.3.24, 2026-01-08 | fix preceded CVE by 223 d |
| CVE-2026-10105 | 2026-05-11 (issue #7866) | PR #7883 | 2.8.5, 2026-07-27 | 77 d |

**Score change:** 38 → 40 (+2). V 11 → 16, R 14 → 4, D 3 → 7, I 5 → 6, C 3 → 4, T 2 → 3. Tier C → C by the assignment rule (40 in the 35–44 band). The R-only change (−10) exceeded the 3-point escalation threshold; all six dimensions were re-evaluated.
**Unverified items carried in this record:** issue #8823 body/status (R structural, non-scoring), v2.6.6 release notes read via a mirror (R supply-chain note), separate OSV query for "phidata" not run (attribution scope).


## Dimension Detail

### V — Verifiability | 16/20

| Criterion | Result | Score | Evidence (source URL) |
|---|---|---|---|
| Developer / company identity | confirmed | 4 | Terms of Service (last updated 2025-01-21): "Agno Inc. … a company registered in New York, United States at 169 Madison Ave STE 2420, New York, NY 10016"; contact support@agno.com (Terms §24, Privacy Notice §16); consistent with the site copyright "© 2026 Agno Inc." and the repository LICENSE "Copyright 2025-2026 Agno Inc." The New York Department of State registry was not queried; the Terms' legal-entity clause is treated as the operator's public identification. https://os.agno.com/legal/tos ; https://os.agno.com/legal/privacy ; https://github.com/agno-agi/agno/blob/main/LICENSE |
| Source code disclosure | confirmed | 4 | SDK and AgentOS runtime distributed under Apache-2.0 (LICENSE; README "Agno is distributed under the Apache-2.0 license"). PyPI `agno` releases carry GitHub Actions provenance attestations verified by PyPI. The hosted Control Plane (os.agno.com) is not open source and sits outside `target_version`. https://github.com/agno-agi/agno ; https://pypi.org/project/agno/ |
| Version management transparency | confirmed | 3 | Per-release changelogs on GitHub Releases (verified v2.3.24, v2.7.2–v2.7.4, v2.8.0–v2.8.5) and a changelog page linked from agno.com; 264 PyPI releases to date. https://github.com/agno-agi/agno/releases |
| Third-party dependency disclosure | confirmed | 3 | Privacy Notice §4 lists the third parties that receive personal data, by category and name (AI service providers: Anthropic, OpenAI; cloud: AWS; billing: Stripe; analytics/session replay: PostHog, Google Analytics, Google Tag Manager; auth: GitHub OAuth, Google OAuth; hosting: Webflow; CRM: Attio; community: Common Room; consent tooling: Termly.io). The notice carries "Last updated April 20, 2026"; there is no standalone sub-processor page or per-list change log. https://os.agno.com/legal/privacy |
| Independent certification | not confirmed | 0 | agno.com and agno.com/enterprise display the line "SOC 2 compliant"; no report, trust center, auditor statement or customer-access statement located. Recorded as a vendor claim (Absolute Rule 4). https://www.agno.com/enterprise |
| Functional reproducibility docs | confirmed | 2 | docs.agno.com carries an API reference (e.g. /reference/agents/agent) and behavioral documentation for telemetry, security, HITL and run cancellation. https://docs.agno.com/ |

Positive findings: Legal entity, jurisdiction and postal address published in the Terms; full open-source distribution under Apache-2.0; per-release changelogs; PyPI build provenance attestations; a dated list of third-party data recipients.
Recorded concerns: "SOC 2 compliant" claim without a public report or access statement; registry record not independently queried.

### R — Resilience | 4/20

CVE window: 2025-09-25 → 2026-09-25. Attribution: product-scoped to the `agno` package / agno-agi/agno repository.

| Criterion | Result | Score | Evidence (source URL) |
|---|---|---|---|
| CVE count (trailing 12 months) | confirmed | 1 | 4 CVEs (band 3–5 = 2 points) with the −1 penalty because CVE-2026-35002 carries CVSS 9.8. Enumerated from the OSV search for "agno" (10 records: 4 CVEs plus GHSA/PYSEC aliases) and the NVD records. https://osv.dev/list?q=agno |
| Maximum CVSS severity | confirmed | 0 | 9.8 Critical (CVSS 3.1, NIST-assessed) for CVE-2026-35002; CNA (VulnCheck) CVSS 4.0 9.3. https://nvd.nist.gov/vuln/detail/CVE-2026-35002 |
| Patch response speed | confirmed | 0 | The only publicly measurable first-report → fix interval in the window is CVE-2026-10105: public issue #7866 (2026-05-11) → fix released in v2.8.5 (2026-07-27), 77 days. The other three CVEs were fixed before any public record existed (fix release dates precede the advisory or CVE publication by 2, 84 and 223 days respectively); their first-report dates are not public. https://github.com/agno-agi/agno/issues/7866 ; https://github.com/agno-agi/agno/releases/tag/v2.8.5 |
| Structural issues | confirmed | 0 | The path-containment weakness class (CWE-22) was addressed in four separate components across the window: PythonTools/MLXTranscribeTools (commit 710d7e7, v2.3.24, 2026-01-08; later CVE-2026-76832), FileSystemKnowledge.get_file (#8624, v2.7.2, 2026-07-09), FileTools root-search containment (#8719, v2.7.3, 2026-07-14) and Antigravity symlinked-source loading (#8721, v2.7.3). A shared `_check_path` helper was added to `Toolkit` on 2026-01-07. PR #7883 cross-references issue #8823, titled as the same metadata-injection class as CVE-2026-10105 in the Milvus, SurrealDB and Couchbase backends [UNVERIFIED — issue body and status not read in this session; resolving source: https://github.com/agno-agi/agno/issues/8823]. https://github.com/agno-agi/agno/releases ; https://github.com/agno-agi/agno/commit/710d7e7f846f93b7a3eadfd3e77075428c39e803 ; https://github.com/agno-agi/agno/pull/7883 |
| Supply chain compromise (trailing 12 months) | confirmed none | 3 | No compromise of the `agno` package, the agno-agi GitHub organization, or the build pipeline appears in OSV/GHSA/NVD. PyPI releases carry provenance attestations signed by GitHub Actions (verified by PyPI 2026-09-16). Dependency note (not an Agno compromise): the v2.6.6 release notes record disabling the `agno[mistral]` extra because the `mistralai` package was quarantined on PyPI — `dependency: mistralai` (notes read via a Renovate mirror; secondary). https://pypi.org/project/agno/ ; https://github.com/AlphaSphereDotAI/chattr/pull/3019 |

Positive findings: Every window CVE has a fix in a released version; three of four were fixed before public disclosure; finders are credited in the maintainer advisory (JasonLovesDoggo) and CNA records (YU SUN; Ali Raza / locus-x64); a shared path-check helper was introduced; PyPI provenance attestations in place.
Recorded concerns: One CVSS 9.8 remote code execution flaw and three High-severity flaws in 12 months; 77 days from public report to release for the SQL injection; the containment class recurred across components after the shared helper was introduced; the GHSA record for CVE-2026-10105 lists no patched version (as of its 2026-07-13 modification), so advisory-driven scanners may not point users to v2.8.5.

### D — Data Conduct | 7/15

| Criterion | Result | Score | Evidence (source URL) |
|---|---|---|---|
| GDPR compliance disclosure | partial | 1 | Privacy Notice §3 sets out GDPR / UK GDPR legal bases (consent, performance of a contract, legitimate interests, legal obligations, vital interests) and §11 EEA/UK/Swiss data-subject rights. No customer-facing DPA is offered. Terms §11 state the Services are hosted in the United States and that use from other regions transfers data there. https://os.agno.com/legal/privacy ; https://os.agno.com/legal/tos |
| Data minimization | partial | 1 | SDK telemetry is enabled by default (per-run metadata: model provider, database type, feature flags); disable via `AGNO_TELEMETRY=false` or `telemetry=False` (AgentOS and evals require the per-instance flag); endpoint observed by a community member as os-api.agno.com, opt-out confirmed by the vendor. The Privacy Notice additionally discloses session replay (PostHog), location data and Google Analytics remarketing on the Services, with cookie and Global Privacy Control opt-outs. https://docs.agno.com/telemetry ; https://community.agno.com/t/logs-to-os-api-agno-com/1864 ; https://os.agno.com/legal/privacy |
| AI training use | not confirmed | 0 | Privacy Notice §6 ("AI Products": AI deployment, AI bots) states that personal information processed by AI Products is handled per the notice and third-party agreements; §4 names Anthropic and OpenAI as AI service providers; §13 records use of personal information for "internal research for technological development." No statement that customer or account data is, or is not, used for model training. Telemetry docs state the SDK does not transmit prompts or outputs. https://os.agno.com/legal/privacy ; https://docs.agno.com/telemetry |
| Sub-processor transparency | confirmed | 3 | Privacy Notice §4 named third-party list (see V), document dated 2026-04-20. https://os.agno.com/legal/privacy |
| Data retention disclosure | confirmed | 2 | §8: personal information kept no longer than the period in which the user holds an account, then deleted or anonymized (or isolated in backups until deletion is possible); §13 per-category table (identifiers, customer-records information, commercial, network activity, geolocation, professional, inferences): "As long as the user has an account with us." https://os.agno.com/legal/privacy |

Positive findings: Published Privacy Notice (2026-04-20) and Terms (2025-01-21) where the prior record found none; named third-party recipients; per-category retention bound to account lifetime; self-hosted data model for agent data (sessions, memory, knowledge, traces in the operator's own database); SDK telemetry documented with an example payload and two-level opt-out.
Recorded concerns: No DPA; no model-training statement; SDK telemetry default ON; website-level session replay, location and remarketing collection; Terms §1 state the Services are not tailored to HIPAA or FISMA and may not be used in a way that would violate GLBA.

### I — Identity & Control | 6/10

| Criterion | Result | Score | Evidence (source URL) |
|---|---|---|---|
| Emergency stop documentation | partial | 2 | Run cancellation is a documented runtime feature (docs navigation "Run Cancellation"; release notes reference cancellation checks in team delegation, v2.6.19). Immediate-stop semantics for in-flight tool calls were not verified in this session. https://docs.agno.com/ ; https://github.com/agno-agi/agno/releases |
| Human-in-the-loop design | partial | 1 | HITL (confirmation, user input, external execution, admin approvals; multi-round team HITL; AG-UI HITL) is available per tool/agent as configuration (`human_review=HumanReview(...)` from 3.0.0a2; earlier `requires_confirmation`), not enabled by default. https://github.com/agno-agi/agno/releases |
| Permission delegation transparency | confirmed | 3 | JWT-based RBAC with documented scope format, available scopes and endpoint→scope mappings; service accounts; per-agent and per-tool permissions; admin approval gates. https://docs.agno.com/agent-os/security/overview |

Positive findings: RBAC scopes and endpoint mappings are documented; HITL primitives cover confirmation, user input and admin approval; audit logs and approvals are part of the runtime.
Recorded concerns: HITL and authorization are opt-in; immediate-stop guarantee not documented in a form verified here.

### C — Containment | 4/10

| Criterion | Result | Score | Evidence (source URL) |
|---|---|---|---|
| Sandbox design | partial | 2 | Hybrid: file-handling tools are constrained to a base directory (`restrict_to_base_dir=True` default since v2.3.24; `_check_path` in Toolkit); ShellTools hardening is limited to documentation and the confirmation API (#8854, v2.7.3); process-level code sandboxes (e.g. Superserve Firecracker tools, v2.7.4) are external integrations rather than a built-in allowlist sandbox. https://github.com/agno-agi/agno/releases/tag/v2.3.24 ; https://github.com/agno-agi/agno/releases |
| Least privilege | partial | 1 | AgentOS authorization is opt-in (`AgentOS(authorization=True)`); scopes are configurable; the FileSystem primitive ships "fail-closed per-user namespace isolation" (v2.8.2). https://docs.agno.com/agent-os/security/overview |
| Tenant isolation (cloud) | claimed | 1 | The runtime is self-hosted; the hosted Control Plane is described as connecting the browser directly to the operator's runtime with no data path through Agno; the README states "multi-user, multi-tenant isolation out of the box". CVE-2025-64168 documents a cross-session `session_state` exposure under concurrency in agno 2.0.0–2.2.1 (fixed 2.2.2). Isolation of the hosted Control Plane is not independently documented. https://www.agno.com/agentos ; https://github.com/agno-agi/agno/security/advisories/GHSA-vw84-hprm-cxmm |

Positive findings: Base-directory containment is now the default for file tools; per-user namespace isolation in the durable filesystem; runtime runs inside the operator's own cloud.
Recorded concerns: Authorization opt-in; no built-in execution sandbox; tenant-isolation claims not independently verified; one cross-session exposure CVE in the window.

### T — Transparency | 3/10

| Criterion | Result | Score | Evidence (source URL) |
|---|---|---|---|
| CVE publication posture | confirmed | 2 | The maintainers published a repository advisory (GHSA-vw84-hprm-cxmm, CVE-2025-64168, 2025-10-31) with credits. The other three window CVEs were assigned by VulnCheck as CNA without a vendor advisory. https://github.com/agno-agi/agno/security/advisories |
| Incident disclosure speed | partial | 0 | 1 of 4: the maintainer advisory followed the 2.2.2 fix by 2 days. No vendor disclosure for CVE-2026-35002 and CVE-2026-76832 — the fixes shipped in v2.3.24 (2026-01-08) with release-note entries reading "fix: replace eval() with type mapping" and "Forbid tools to operate out of base directory" without a security identifier; third-party CVEs followed 84 and 223 days later. No vendor advisory for CVE-2026-10105 (public issue; fix release notes describe it as a bug fix). https://github.com/agno-agi/agno/releases/tag/v2.3.24 ; https://github.com/agno-agi/agno/releases/tag/v2.8.5 |
| Security policy publication | partial | 1 | Technical security documentation exists (JWT, RBAC, scopes, guardrails) and Privacy Notice §9 describes "technical and organizational security measures" in general terms; no SECURITY.md in the repository (root and .github/ checked 2026-09-25, HTTP 404); no organizational security page or vulnerability disclosure policy located. https://docs.agno.com/agent-os/security/overview |
| AI safety framework reference | not confirmed | 0 | No external framework (NIST AI RMF etc.) reference located. |
| AI system identity disclosure | not confirmed | 0 | No default AI-identity disclosure feature located. |

Positive findings: One maintainer-authored advisory with CVSS vector and credits; security documentation for the runtime.
Recorded concerns: Three of four window CVEs lack a vendor advisory; no SECURITY.md or disclosure channel; no AI safety framework reference.


## Incident Timeline

| Date (public) | CVE ID | CVSS | Description | Patch status | CISA KEV |
|---|---|---|---|---|---|
| 2025-10-31 | CVE-2025-64168 (GHSA-vw84-hprm-cxmm, PYSEC-2026-1077) | 7.1 High (v3.1, maintainer/GitHub) | Race condition: `session_state` persisted to the wrong session under high concurrency; cross-user exposure. Affects agno ≥2.0.0 <2.2.2. CWE-362/668. | Fixed 2.2.2 (PyPI 2025-10-29) | No |
| 2026-04-02 | CVE-2026-35002 (GHSA-77rh-m34w-rv36, PYSEC-2026-256) | 9.8 Critical (v3.1, NIST) / 9.3 (v4.0, CNA VulnCheck) | `field_type` in a FunctionCall passed to `eval()`; arbitrary Python code execution. Affects <2.3.24. CWE-95. | Fixed 2.3.24 (2026-01-08; commit cbf6755, PR #5912) | No |
| 2026-05-29 | CVE-2026-10105 (GHSA-82m5-3pcp-hccq, PYSEC-2026-2333) | 8.3 High (v3.1, CNA) / 8.7 (v4.0, CNA); NVD "Not Scheduled" | SQL injection in the ClickHouse vector backend `delete_by_metadata()` via f-string interpolation of metadata keys/values. Affects 2.6.5 (advisory: last affected 2.6.5). CWE-89. Public issue #7866 opened 2026-05-11. | Fix PR #7883 released in 2.8.5 (2026-07-27); advisory lists no patched version | No |
| 2026-08-19 | CVE-2026-76832 | 8.8 High (v3.1, CNA) / 8.5 (v4.0, CNA); NVD "Received" | Path traversal via `file_name` in PythonTools `read_file` / `save_to_file` / `run_python_file`; arbitrary file read/write/execute within the process user's authority. CWE-22. | Fixed 2.3.24 (2026-01-08; commit 710d7e7, PR #5940) | No |

Outside the window, recorded and not counted: 2025-08-06 CVE-2025-8665 (GHSA-r34x-38p8-9whw), 6.3 Medium (v3.1, CNA VulDB) / 5.3 (v4.0), OS command injection via the `command` argument of MCPTools/MultiMCPTools in agno ≤1.7.5; Snyk lists 1.7.7 as the fixed version (secondary). https://nvd.nist.gov/vuln/detail/CVE-2025-8665 ; https://security.snyk.io/vuln/SNYK-PYTHON-AGNO-11787823


## Contextual Analysis

Agno is the successor line of Phidata: the current repository agno-agi/agno publishes under Apache-2.0 (changed from MPL 2.0 in February 2026 per the vendor's community roundup), copyright Agno Inc., while the legacy agno-agi/phidata repository remains under MPL 2.0. The operator's Terms of Service have carried the name Agno Inc., registered in New York, since at least January 2025. The project is highly active — 264 PyPI releases, a 3.0.0 major release on 2026-08-24, 3.0.11 on 2026-09-23, and more than a thousand commits since the January 2026 release that carried two of the four security fixes — so the dormancy test does not apply.

The security record of the window is defined less by the number of flaws than by how they surfaced. Two of the four CVEs (the eval() injection and the path traversal) were fixed in the same release, v2.3.24 on 2026-01-08, and the release notes describe the changes as a bug fix and an improvement; the CVE records were later created by a third-party CNA (VulnCheck) 84 and 223 days after the fix. Users tracking release notes had the fix early; users tracking advisories learned of the issues months later. The third CVE, the ClickHouse SQL injection, followed the opposite path: the finder opened a public issue with a proof of concept on 2026-05-11, VulnCheck assigned the CVE on 2026-05-29, an external contributor's PR was automatically closed by the repository's assignment bot, and the fix was later merged and released in v2.8.5 on 2026-07-27 with a maintainer comment that the fix "will be released today". The GitHub advisory for this CVE records "last affected 2.6.5" and no patched version, so dependency tooling may treat any version above 2.6.5 as unaffected although the code change shipped in 2.8.5. The fourth, CVE-2025-64168, is the one case handled through a maintainer-published advisory with a fix two days before disclosure.

On structure, the four CVEs have four distinct CWEs. What recurs is the containment pattern for file paths: after the shared `_check_path` helper landed in January 2026, three further containment fixes (FileSystemKnowledge, FileTools search, Antigravity symlinked sources) shipped in July 2026. PR #7883 also cross-references an issue titled as the same metadata-injection class in three other vector-database backends; its content and status were not read in this session and are flagged as unverified. The vendor's own hardening steps are visible in the same period: `restrict_to_base_dir` on by default, a hardened judge prompt fence (v2.8.0), OAuth on the AgentOS MCP endpoint (v2.7.2), and per-user namespace isolation in the durable filesystem (v2.8.2).

On data conduct, the picture improved relative to the prior record: Agno Inc.'s Privacy Notice (last updated 2026-04-20) and Terms of Service (last updated 2025-01-21) are published, identify a New York-registered entity with a postal address, set out GDPR/UK GDPR legal bases, name the third parties that receive personal data (including Anthropic and OpenAI as AI service providers, AWS, Stripe and PostHog) and state retention as the lifetime of the account, per category. What the notice does not contain is a customer-facing DPA or any statement on whether account or customer data is used for model training; it also discloses website session replay, location data and remarketing on the Services. For the self-hosted SDK the telemetry documentation remains specific: per-run metadata only, no prompts or outputs, opt-out at two levels, endpoint os-api.agno.com rather than the api.phidata.com recorded previously. Product-level integration note for the disclosure layer: Anthropic appears as one of two AI service providers for Agno's hosted Services; under framework v0.3.2 a model-provider relationship is not itself a disclosure trigger.

Two data-quality observations on the public records themselves: NVD has not enriched CVE-2026-10105 ("Not Scheduled") or CVE-2026-76832 ("Received"), so the CVSS values recorded for them are CNA values; and the CNA record for CVE-2026-76832 carries the affected packageURL `pkg:cargo/dua-cli`, which does not correspond to Agno, while its description, repository and patch commit do.

Anthropic equity-holder disclosure (framework v0.3.2 disclosure layer): Triggers 0, 1, 2, 3 — None. The operator is Agno Inc.; its only recorded funding is a USD 5.4M seed round on 2024-08-29 with three venture investors including GreatPoint Ventures (CB Insights, secondary; the profile is retained under the former name Phidata), and no Amazon, Google, Microsoft or NVIDIA equity, board, or non-arms-length channel relationship appears in the sources consulted. Customer logos on agno.com (including Meta, IBM, Oracle, Adobe) are customer relationships and not disclosure triggers.

P dimension (Economic Integrity): checked; agno.com states fixed pricing with no metering of storage, retention or traces, and the Terms describe auto-renewing subscriptions cancellable from the account; no issue found, so the Economic Risk section is omitted.


## VERDICT Record

### Summary
Agno's trailing-12-month record shows four product-scoped CVEs including a CVSS 9.8 remote code execution flaw, all fixed in released versions, with one 77-day public-report-to-release interval and three fixes that shipped without a vendor advisory; the published legal pages of the New York-registered operator, the self-hosted data model and documented RBAC are the platform's strongest recorded controls.

### Risk Factor Summary by Use Case

| Use case | Risk factors recorded | Key data points |
|---|---|---|
| Internal testing / non-sensitive workflows | SDK telemetry default ON (metadata only); file-tool containment default since 2.3.24 | `AGNO_TELEMETRY=false` opt-out; `restrict_to_base_dir=True` |
| Workflows handling API keys / credentials | CVE-2026-35002 (RCE, <2.3.24); CVE-2026-76832 (path traversal via prompt-injectable `file_name`, <2.3.24); ShellTools relies on confirmation rather than a sandbox | Both fixed in 2.3.24; HITL confirmation opt-in |
| Cloud version (multi-tenant) | Runtime is self-hosted; hosted Control Plane isolation claimed, not independently documented; CVE-2025-64168 cross-session exposure (2.0.0–2.2.1) | Fixed 2.2.2; authorization opt-in (`authorization=True`) |
| Medical / financial / legal data | Terms §1: Services not tailored to HIPAA or FISMA; use that would violate GLBA prohibited; no DPA; no model-training statement; SOC 2 claimed without public report; CVE-2026-10105 SQL injection in the ClickHouse backend (≤2.6.5) | Data hosted in the United States (Terms §11); fix in 2.8.5; advisory lists no patched version |

This table records what risk factors the data shows. It does not recommend or prohibit use. All decisions belong to the reader.

### Reference Information
- Version 2.3.24 addresses CVE-2026-35002 and CVE-2026-76832, and version 2.8.5 carries the ClickHouse fix for CVE-2026-10105; users on earlier versions may wish to review their update status, noting that the GHSA record for CVE-2026-10105 does not name a patched version.
- Telemetry can be disabled with `AGNO_TELEMETRY=false` for agents, teams and workflows; AgentOS and eval instances take `telemetry=False` directly.
- AgentOS authorization (`authorization=True` with a JWT verification key) and per-tool `human_review` settings are configuration options documented at docs.agno.com.

### Bias Disclosure
"This evaluation uses Claude (Anthropic) as its tooling. Anthropic operates in the AI agent market and may compete with some evaluated vendors. VERDICT discloses this relationship in every report and applies identical evaluation criteria to all platforms regardless of their relationship to Anthropic."

---

## Evaluation History

| Date | Type | Score | Tier | Framework |
|---|---|---|---|---|
| 2026-03-31 | Initial (Layer 0) | 38 | C | v0.3.1 |
| 2026-09-25 | Update (interrupt lane T1 ×4, folded routine; all dimensions re-evaluated) | 40 | C | v0.3.2 |

---

## Future Evaluation Plan

| Phase | Content | Planned timing |
|---|---|---|
| Layer 1 | Free-tier behavioral testing (30 runs × 4 difficulty levels across 3+ days) on the open-source SDK/runtime and the free Control Plane tier | After the Stage 3 backlog; not scheduled |
| Layer C — routine | Full routine differential (R, T, V; D/I/C per carry-forward conditions against the per-dimension URLs cited above) | 365 days from 2026-09-25 (provisional, ReviewCadence-002) |
| Layer C — interrupt | T1 / T2 / T3 sweep (NVD/GHSA/OSV for `agno`, KEV JSON); T5 follow-up on os.agno.com legal pages; read of issue #8823 to close the remaining structural-issues flag | Continuous; next quarterly sweep |

---

```japanese-summary
# Agno（旧 Phidata）評価結果サマリー

## 基本情報
- 評価種別: 更新
- スコア: 40/85 (Layer 0)
- 前回スコア: 38/85（2026.03.31、Tier C、v0.3.1）
- ランク: 再計算待ち（build_index.py） / —
- 評価日: 2026.09.25（初回評価日: 2026.03.31）
- 対象バージョン: agno 3.0.11（PyPI、2026.09.23 リリース）
- 運営: Agno Inc.（ニューヨーク州登記、前回記録: Phidata Inc.）
- 独立性: ✅ Independent

## 次元スコア
- V (検証可能性): 16/20
- R (耐性): 4/20
- D (データ運用): 7/15
- I (制御): 6/10
- C (封じ込め): 4/10
- T (透明性): 3/10

## 主要ポジティブ所見
- 利用規約（2025.01.21 改定）に法人名・登記州・住所・連絡先を明記。プライバシーポリシー（2026.04.20 改定）に GDPR 法的根拠、第三者提供先の社名一覧、カテゴリ別保持期間（アカウント存続期間）を記載
- SDK と AgentOS ランタイムを Apache-2.0 で全面公開（2026年2月に MPL 2.0 から変更）。PyPI リリースに provenance attestation
- 直近12ヶ月の CVE 4件すべてにリリース済み修正あり。うち3件は公開前に修正済み
- セッション・メモリ・ナレッジ・トレースを利用者自身のデータベースに保存する self-hosted 構成
- JWT ベース RBAC のスコープとエンドポイント対応を文書化。HITL が設定で利用可。2.3.24 以降ファイル系ツールの base directory 制限がデフォルト有効

## 主要リスク所見
- CVE-2026-35002（eval() 経由の任意コード実行、CVSS 9.8）を含む4件の CVE。R は 14 → 4
- ClickHouse SQL インジェクション（CVE-2026-10105）は公開 issue（2026.05.11）から修正リリース（v2.8.5、2026.07.27）まで77日。GHSA 記録に修正版の記載なし
- 4件中3件にベンダーアドバイザリなし（2件は 2026.01.08 のリリースノートに不具合修正／改善として記載）
- パス封じ込め系の弱点が4コンポーネントで個別に修正（同種の再発）
- 学習利用の有無を述べる記載なし。顧客向け DPA なし。AI service providers として Anthropic・OpenAI を記載
- SDK テレメトリはデフォルト ON（メタデータのみ、os-api.agno.com）。サイト側で PostHog セッションリプレイ・位置情報・GA リマーケティングを収集
- 利用規約 §1: HIPAA・FISMA 非対応、GLBA 違反となる利用は不可。データはアメリカ合衆国でホスト
- SECURITY.md なし。サイト上の「SOC 2 compliant」表記に公開レポートなし

## インシデント
- CVE-2025-64168, 7.1 (v3.1), 高並行時に session_state が別セッションへ保存される競合状態（2.0.0–2.2.1、2.2.2 で修正、2025.10.31 公開）
- CVE-2026-35002, 9.8 (v3.1 NIST) / 9.3 (v4.0), FunctionCall の field_type を eval() に渡す任意コード実行（<2.3.24、2.3.24 で修正、2026.04.02 公開）
- CVE-2026-10105, 8.3 (v3.1) / 8.7 (v4.0), ClickHouse delete_by_metadata() の SQL インジェクション（2.6.5、2.8.5 で修正、2026.05.29 公開）
- CVE-2026-76832, 8.8 (v3.1) / 8.5 (v4.0), PythonTools の file_name によるパストラバーサル（2.3.24 で修正、2026.08.19 公開）
- 窓外（参考）: CVE-2025-8665, 6.3 (v3.1), MCPTools のコマンドインジェクション（≤1.7.5、2025.08.06 公開、前回記録の窓内）

## CISA KEV
- 該当なし（カタログ 2026.09.24、1,723件を確認）

## HTMLカード用タグ
- tags: open-source, apache-2-0, self-hosted, multi-agent, agent-runtime, hitl, telemetry-default-on, rebranded, critical-cve-12mo, tier-c
- incident_tags: eval-injection, sql-injection, path-traversal, race-condition, cross-session-exposure
- owner: Agno Inc.
```

```
Score: 40/85
V: 16/20, R: 4/20, D: 7/15, I: 6/10, C: 4/10, T: 3/10
Dimensions verified: V+R+D+I+C+T = 40
Tier: C · Category: Agent Framework & Runtime · Open-Source (Apache 2.0) · Previous: 38/85 (Tier C)
```
