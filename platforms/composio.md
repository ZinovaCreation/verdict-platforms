---
name: Composio
slug: composio
operator: Sampark, Inc. d/b/a Composio · San Francisco
independence: independent
parent_entity: null
category: AI Agent Tool Integration · OSS SDK + Cloud
homepage: https://composio.dev
github: https://github.com/ComposioHQ/composio
evaluation_number: 25
evaluation_type: update
evaluated_at: '2026-03-30'
updated_at: '2026-10-30'
evaluator_model: claude-fable-5-1
framework_version: v0.3.2
layer: '0'
target_version: Composio Python SDK composio 0.29.1 (PyPI 2026-10-22); TypeScript @composio/core 0.27.0; composio.dev cloud platform, REST API v3.1
previous_evaluation_date: '2026-03-30'
previous_score: 46
score: 48
max_score: 85
tier: B
verdict:
  v:
    score: 14
    rating: High
    note: Legal entity on DPA; MIT SDKs, closed platform; SOC 2 report on request
  e:
    score: null
    rating: null
    note: null
  r:
    score: 11
    rating: Mid
    note: 2 CVEs in window (max 7.5); 4-day fix in 2026; path-validation defects recur
  d:
    score: 9
    rating: Mid
    note: DPA with SCCs; payload not trained on; logging default ON; ZDR priced add-on
  i:
    score: 6
    rating: Mid
    note: Scoped keys documented; approvals optional and experimental
  c:
    score: 3
    rating: Low
    note: May 2026 multi-customer credential exposure; E2B sandbox isolation unpublished
  t:
    score: 5
    rating: Mid
    note: Incident disclosed same day; no vendor advisories or AI identity disclosure
cisa_kev:
  present: false
  entries: []
cve_count_12mo: 2
cve_count_basis: exact
max_cvss_12mo: 7.5
supply_chain_compromise_12mo: false
known_facts_applied: []
qa:
  factual: pass
  legal: pass
  quality: pass
  revision_cycles: 1
  flagged: false
differential:
  v: re-evaluated
  r: re-evaluated
  d: re-evaluated
  i: re-evaluated
  c: re-evaluated
  t: re-evaluated
  e: null
next_review_due: '2027-10-30'
tags:
- open-core
- MIT-SDK
- cloud-SaaS
- SOC2
- DPA
- zero-data-retention
- managed-auth
- credential-isolation
- tool-integration
- firewall
- security-incident-2026
rank: 31
sources:
- https://composio.dev/legal/dpa
- https://composio.dev/terms
- https://composio.dev/privacy
- https://composio.dev/enterprise
- https://docs.composio.dev/docs/security/overview
- https://docs.composio.dev/docs/security/token-custody
- https://docs.composio.dev/docs/security/data-retention
- https://docs.composio.dev/docs/security/zero-data-retention
- https://docs.composio.dev/docs/approvals
- https://docs.composio.dev/reference/authenticating-to-composio/project-api-key-permissions
- https://github.com/ComposioHQ/composio
- https://github.com/ComposioHQ/composio/releases
- https://nvd.nist.gov/vuln/detail/CVE-2025-56427
- https://nvd.nist.gov/vuln/detail/CVE-2026-59807
- https://app.opencve.io/cve/CVE-2026-59807
- https://pypi.org/project/composio/0.29.1/
- https://composio.dev/blog/composio-may-2026-security-incident
- https://trust.composio.dev/resources
- https://trust.composio.dev/subprocessors
og_description: 'Independent security evaluation of Composio. Score: 48/85. May 2026 incident exposed ~0.3% of connections and 5,241 API keys, disclosed same day. Published DPA with no-training statement for payload data. Recurring file-path validation defects. Framework v0.3.2.'
category_line: AI Agent Tool Integration · OSS SDK + Cloud
display_tags: &id001
- text: May 2026 Incident · Credential Exposure
  color: red
- text: CVE-2026-59807 · Path Validation
  color: amber
- text: CVE-2025-56427 · Dir Traversal
  color: red
- text: Path Handling · Recurring
  color: red
finding: May 2026 security incident — attacker reached the tool-execution sandbox and a credential cache, exposing ~0.3% of connections (5,001 GitHub) and 5,241 API keys; disclosed same day, remediation documented through 2026-09-16. Published DPA (2026-10-17) with EU SCCs, UK Addendum and Swiss FADP; payload data not used for model training. CVE-2026-59807 fixed four days after public report. File-path validation defects recur 2024–2026. Approvals and least privilege are opt-in; payload logging on by default.
meta_owner: Sampark, Inc. d/b/a Composio
meta_description: 'Independent security evaluation of Composio. Score: 48/85. May 2026 incident exposed ~0.3% of connections and 5,241 API keys, disclosed same day. Published DPA with no-training statement for payload data. Recurring file-path validation defects. Framework v0.3.2.'
key_finding: May 2026 incident exposed ~0.3% of connections and 5,241 API keys, disclosed same day. Published DPA with no-training statement for payload data. 2026 CVE fixed in four days. Recurring file-path validation defects.
card_owner: Sampark, Inc. d/b/a Composio · San Francisco
card_category: AI Agent Tool Integration · OSS SDK + Cloud
card_tags: *id001
score_basis: consistent
---
# Composio

May 2026 security incident exposed about 0.3% of active connections and 5,241 API keys from an operator-side credential cache; disclosed the same day, with remediation documented through 2026-09-16. Published DPA (2026-10-17) with a no-training statement for payload data and one-year retention. CVE-2026-59807 fixed four days after public report. File-path validation defects recur 2024–2026. Approvals and least privilege are opt-in; payload logging is on by default.

## Layer 0 Score: 48/85 (Tier B)

**V** 14/20 · **R** 11/20 · **D** 9/15 · **I** 6/10 · **C** 3/10 · **T** 5/10

Updated 2026-10-30 (previous 46/85, 2026-03-30; triggers T5 and T4).

## CISA KEV

None — no Composio CVE appears in the CISA Known Exploited Vulnerabilities catalog (checked 2026-10-30). 2 published CVEs attributed to Composio in the trailing 12 months (CVE-2025-56427, CVE-2026-59807; basis exact).

## Bias Disclosure

This evaluation uses Claude (Anthropic) as its tooling. Anthropic operates in the AI agent market and may compete with some evaluated vendors. VERDICT discloses this relationship in every report and applies identical evaluation criteria to all platforms regardless of their relationship to Anthropic.

## Evaluation History

| Date | Type | Score | Tier | Framework |
|---|---|---|---|---|
| 2026-03-30 | Initial (migrated capture) | 46/85 | B | v0.3.1 |
| 2026-10-30 | Update (T5 + T4; full re-evaluation) | 48/85 | B | v0.3.2 |

## Full Evaluation

# VERDICT Evaluation #025 — Composio (Update)

| Field | Value |
|---|---|
| Evaluation number | #025 |
| Platform | Composio |
| Evaluation type | Update (Differential Evaluation, T5 interrupt lane; routine R/T/V re-check folded in) |
| Update date | 2026-10-30 |
| Evaluator | VERDICT engine · evaluator_model: claude-fable-5-1 |
| Target version | Composio Python SDK `composio` 0.29.1 (PyPI, 2026-10-22); TypeScript SDK `@composio/core` 0.27.0 (repository, 2026-10-29); `@composio/cli` 0.2.32 line; composio.dev cloud platform, REST API v3.1 |
| Framework | VERDICT v0.3.2 (`zinova-lab/verdict-engine` @ 9eb464b) |
| Previous evaluation | 2026-03-30 · 46/85 · Tier B · framework v0.3.1 (migrated capture) |
| Trigger | T5 — Privacy Policy, Terms of Service and DPA re-dated 2026-10-17 (sweep 2026-10-27). T4 also satisfied in-window: May 2026 security incident reported by the vendor and two or more independent sources (R, T re-check subsumed by the full re-evaluation). |

---

## Executive Summary

Composio's Layer 0 score moves from 46/85 to 48/85 (Tier B, unchanged). On 2026-05-21 Composio disclosed, the same day, a security incident in which an attacker gained a foothold in an internal agentic monitoring tool, registered malicious tool definitions in the execution sandbox and reached an auxiliary credential cache, exposing about 0.3% of active connections (5,001 GitHub connections, 12 Gmail and single-digit counts on other toolkits) and 5,241 API keys; the disclosure was versioned through 2026-09-16 with a documented remediation program. The 2026-10-17 revision of the Privacy Policy, Terms of Service and Data Processing Addendum adds a contractual statement that tool-call payload data is not used to train AI or machine-learning models, a one-year payload retention period, and a published DPA with EU SCCs, UK Addendum and Swiss FADP terms; these documents also name the operator of record as Sampark, Inc. d/b/a Composio, a Delaware corporation, which corrects the previously recorded "Composio Inc." Two CVEs fall in the trailing 12 months: CVE-2025-56427 (directory traversal in the legacy Python 0.7.x server module, CVSS 7.5) and CVE-2026-59807 (path-validation bypass in the TypeScript SDK/CLI file-upload path, CVSS 6.8), the latter fixed four days after public disclosure; no CISA KEV entry was found and the vendor states its SDK and CLI distribution was verified untampered. File-path validation defects recur across the vulnerability record (2024 through 2026), which sets the R structural-issues criterion to 0, and the multi-customer credential exposure sets the C tenant-isolation criterion to 0.

---

## Scorecard

| Dimension | Score | Max | Rating |
|---|---|---|---|
| V — Verifiability | 14 | 20 | High |
| R — Resilience | 11 | 20 | Mid |
| D — Data Conduct | 9 | 15 | Mid |
| I — Identity & Control | 6 | 10 | Mid |
| C — Containment | 3 | 10 | Low |
| T — Transparency | 5 | 10 | Mid |
| E — Effectiveness | — | 15 | not evaluated (Layer 1+) |
| **Layer 0 total** | **48** | **85** | |

Tier: B
Category: AI Agent Tool Integration · OSS SDK + Cloud

CISA KEV: None — no Composio CVE appears in the CISA Known Exploited Vulnerabilities catalog (checked 2026-10-30).
Previous score: 46/85 (2026-03-30).

---

## Differential

| Item | Value |
|---|---|
| Previous evaluation date / score | 2026-03-30 / 46 |
| Base record | `verdict-platforms/platforms/composio.md` @ b62983f (canonical read at 4dc9224) |
| V | re-evaluated — migrated capture, no per-dimension sources |
| R | re-evaluated — migrated capture, no per-dimension sources |
| D | re-evaluated — migrated capture, no per-dimension sources (T5 mandatory) |
| I | re-evaluated — migrated capture, no per-dimension sources |
| C | re-evaluated — migrated capture, no per-dimension sources |
| T | re-evaluated — migrated capture, no per-dimension sources |
| E | null (Layer 0) |
| Carry-forward checks | None performed: conditions 1–4 cannot be positively satisfied for a migrated capture without per-dimension source URLs (convention 2026-09-22). |
| `independence` / `parent_entity` | Re-assessed: independent / null (see Contextual Analysis) |
| Disclosure triggers | Checked 2026-10-30: Triggers 0–3 do not fire. No tags. |
| Trust Center | Rendered text of trust.composio.dev (root, /resources, /subprocessors) supplied by the operator on 2026-10-30 (retrieved 2026-10-27 JST) and applied; no access-request form was submitted. |
| QA revision | Cycle 1: Operations factual note supplied the vendor's May 2026 incident bulletin; incident read in-session and folded into R, C, T, the Incident Timeline and the Contextual Analysis. |
| KNOWN_FACTS candidate | Staged (see Contextual Analysis): operator string "Composio Inc." is not the legal entity; vendor legal pages name Sampark, Inc. d/b/a Composio. |

### Evaluation History

| Date | Type | Score | Tier | Framework |
|---|---|---|---|---|
| 2026-03-30 | Initial (migrated capture) | 46/85 | B | v0.3.1 |
| 2026-10-30 | Update (T5 + T4; full re-evaluation) | 48/85 | B | v0.3.2 |

---

## Dimension Detail

### V — Verifiability (14/20, High)

| Criterion | Result | Score | Evidence URL |
|---|---|---|---|
| Developer / company identity | Legal entity named on the vendor's own legal pages: Sampark, Inc. d/b/a Composio, a Delaware company, 2 Bryant St., Suite 220, San Francisco, CA 94105 (DPA, last updated 2026-10-17; ToS and Privacy Policy effective 2026-10-17). Official contacts published: support@composio.dev (ToS §15, Privacy §10), security@composio.dev (SECURITY.md, docs). No public registry was queried; corporate registration is confirmed by the vendor's legal page (OperatorOfRecord-001). | 4 | https://composio.dev/legal/dpa · https://composio.dev/terms · https://composio.dev/privacy |
| Source code disclosure | Open core. The `ComposioHQ/composio` monorepo (Python SDK, TypeScript SDK and CLI, docs) is MIT-licensed ("Copyright (c) 2025 Sampark Inc."). The hosted platform (backend.composio.dev, dashboard, tool execution service, credential store, Firewall, Workbench) is closed source and is the product the operator sells. Criterion-VSource-001: core components only. | 2 | https://github.com/ComposioHQ/composio/blob/main/LICENSE · https://docs.composio.dev/docs/security/token-custody |
| Version management transparency | Per-package GitHub releases with "What's Changed" notes (391 `@composio/cli@*` tags at 2026-10-30), `CHANGELOG.md` in the repository, and a dated docs changelog (e.g. 2026-09-29 entry). | 3 | https://github.com/ComposioHQ/composio/releases · https://docs.composio.dev/docs/changelog/2026/09/29 |
| Third-party dependency disclosure | Sub-processor list published at trust.composio.dev/subprocessors (DPA §4): 8 entries — Amazon Web Services (us-east-1), Cloudflare, Vercel, OpenAI, E2B, Pusher, ClickHouse, OpenRouter — each with purpose and region/URL. The page carries no last-updated date (operator-rendered text, 2026-10-27). List without date. | 1 | https://trust.composio.dev/subprocessors · https://composio.dev/legal/dpa |
| Independent certification | Trust Center Resources (operator-rendered, 2026-10-27): "SOC 2 Type II Report — Request access"; "SOC 2 Bridge Letter — View"; "ISO 27001 Certificate — View"; Trust Center update of 2026-03-13 announces the renewed SOC 2 Type II report. The report is behind an access request, not publicly downloadable. SOC 2 report customers/requesters only. | 2 | https://trust.composio.dev/resources · https://trust.composio.dev |
| Functional reproducibility docs | Full REST API reference (v3.1) and SDK references, with behavioral documentation of sessions, token custody, execution paths, approvals and retention. | 2 | https://docs.composio.dev/reference · https://docs.composio.dev/docs/security/token-custody |

**Positive findings.** The vendor's DPA names the legal entity, address and a named contact (CEO, Soham Ganatra), and the repository LICENSE carries the same entity. Release notes are per-package and the docs changelog is dated.

**Recorded concerns.** The complete product is not open source; the control plane and execution service are closed. The SOC 2 Type II report, incident response plan, data management policy, secure development policy and the 7 October 2026 pentest report are all behind an access request on the Trust Center; the ISO 27001 certificate and SOC 2 bridge letter are viewable. The sub-processor list carries no update date.

### R — Resilience (11/20, Mid)

Trailing 12-month window: 2025-10-30 to 2026-10-30. Attribution bound to the evaluated target (`composio` Python package, `@composio/*` npm packages, composio.dev cloud) per Attribution-CVE-001.

| Criterion | Result | Score | Evidence URL |
|---|---|---|---|
| CVE count (trailing 12 months) | 2, basis exact: CVE-2025-56427 (first public disclosure 2025-12-04, NVD) and CVE-2026-59807 (first public disclosure 2026-07-03, researcher issue #3746; CVE published 2026-07-08). No CVSS 9.0+ in window. | 3 | https://nvd.nist.gov/vuln/detail/CVE-2025-56427 · https://nvd.nist.gov/vuln/detail/CVE-2026-59807 |
| Maximum CVSS severity | 7.5 — CVE-2025-56427, CISA-ADP CVSS v3.1 (AV:N/AC:L/PR:N/UI:N/S:U/C:H/I:N/A:N); NVD and CNA v3.1 not provided, so the CISA-ADP score is recorded per the Attribution-CVE-002 source order. CVE-2026-59807: CNA (VulnCheck) CVSS v3.1 6.8 (AV:N/AC:H/PR:N/UI:N/S:C/C:H/I:N/A:N; vector-computed 6.8, matches stated); CNA v4.0 8.9 noted, not used. | 2 | https://nvd.nist.gov/vuln/detail/CVE-2025-56427 · https://app.opencve.io/cve/CVE-2026-59807 |
| Patch response speed | CVE-2026-59807: public issue 2026-07-03 → fix commit fc17c37 tagged `@composio/cli@0.2.32-beta.283` on 2026-07-07 (4 days). CVE-2025-56427: affects `composio` 0.7.20 (legacy Python line); the vulnerable module `python/composio/server/api.py` is absent from the current repository (NVD marks the reference a broken link) and the v3 Python SDK line began at 0.8.0 on 2025-07-21, before disclosure; no fix release for the 0.7.x line is recorded. The only measurable patch event in the window is ≤7 days. | 3 | https://github.com/ComposioHQ/composio/commit/fc17c37bf95b7ece5c038cb7e2ab7e3e4a064e3a · https://github.com/ComposioHQ/composio/issues/3746 · https://pypi.org/project/composio/0.29.1/ |
| Structural issues | File-path validation defects recur across the product's record: CVE-2024-8865 (path traversal, server api.py), CVE-2024-8958 (unrestricted file read/write), CVE-2025-56427 (directory traversal, `_download_file_or_dir`), CVE-2026-59807 (missing `assertSafeFileUploadPath` check) and an internally found path-traversal fix in `FileDownloadable.download()` (SEC-316, 2026-05-06). Same root-cause class recurring. | 0 | https://app.opencve.io/cve/?vendor=composio · https://github.com/ComposioHQ/composio/commit/2428a955 |
| Supply chain compromise (trailing 12 months) | No compromise of a Composio package, registry account or build artifact is on the public record. The May 2026 incident (below) reached internal systems, a production codebase via a leaked GitHub token, and the tool-building service; the vendor states that its SDK and CLI supply chain was verified untampered, that Buildkite credentials were revoked and that the tool-building service was rebuilt with OIDC in place of shared static secrets. The vendor's 2026-05-12 statement records non-impact from the Vercel April 2026 incident (`dependency: Vercel`). PyPI `composio` 0.29.1 carries provenance attestations (GitHub Actions, 2026-10-22). | 3 | https://composio.dev/blog/composio-may-2026-security-incident · https://trust.composio.dev · https://pypi.org/project/composio/0.29.1/ |

**Positive findings.** The 2026 CVE was fixed and released within four days of the public report; the fix commit references a GitHub advisory identifier (GHSA-hp3h-89pf-5q58) and CI hardening landed in the adjacent release (least-privilege tokens, fork-PR guards, audit gate; `@composio/cli@0.2.32-beta.282`). PyPI releases carry provenance.

**Recorded concerns.** Path-handling issues have been reported in 2024, 2025 and 2026 and found internally in 2026. CVE-2025-56427 carries no vendor advisory or fixed-version statement on the public record; the affected code line was superseded rather than patched. The May 2026 incident involved arbitrary code execution inside the tool-execution sandbox through registered tool definitions and an onward path to a credential cache; it carries no CVE and is recorded in the Incident Timeline, not in `cve_count_12mo`.

### D — Data Conduct (9/15, Mid)

| Criterion | Result | Score | Evidence URL |
|---|---|---|---|
| GDPR compliance disclosure | Published DPA (last updated 2026-10-17) with controller/processor roles, EU SCCs Modules Two and Three incorporated by reference (Attachment 4), UK Addendum, Swiss FADP terms, CCPA service-provider terms; accepted in-dashboard by Pro and Enterprise customers. | 3 | https://composio.dev/legal/dpa |
| Data minimization | Request arguments and response data are stored in execution logs by default on every plan. Zero Data Retention is a per-project/organization toggle, "available on paid plans for a usage-based price and included on Enterprise"; audit logs and operational telemetry are stored on every plan and are not affected by ZDR. Default ON with an opt-out toggle. | 1 | https://docs.composio.dev/docs/security/data-retention · https://docs.composio.dev/docs/security/zero-data-retention |
| AI training use | Privacy Policy §2, ToS §9 and DPA §2.8 state payload data is not used to develop, train or improve AI/ML models; retention is stated (one year, 30 days after organization deletion). The same clauses permit training on de-identified execution metadata, retained indefinitely. Scored as a not-used statement that is qualified by a permitted-use carve-out. | 2 | https://composio.dev/privacy · https://composio.dev/terms · https://composio.dev/legal/dpa |
| Sub-processor transparency | 8 sub-processors listed with purpose (AWS, Cloudflare, Vercel, OpenAI, E2B, Pusher, ClickHouse, OpenRouter); Vercel and OpenRouter entries note zero-data-retention settings and OpenAI notes training opt-out. No last-updated date on the list; the DPA commits to 30 days' notice of additions via the Trust Center. List without date. | 1 | https://trust.composio.dev/subprocessors · https://composio.dev/legal/dpa |
| Data retention disclosure | Per-category: payload and identified execution metadata 1 year; de-identified metadata indefinite; account data until deletion request (30 days to delete, hashed email retained); staged files 24 hours; presigned URLs 1 hour (configurable to 24); Workbench state ~12 hours idle; YouTube API data 30 days. | 2 | https://docs.composio.dev/docs/security/data-retention · https://composio.dev/privacy |

**Positive findings.** The 2026-10-17 revision moved the no-training statement from the Privacy Policy into the ToS and DPA, defined Payload Data and Execution Metadata consistently across all three documents, and added a "more protective term applies" conflict rule (ToS §9).

**Recorded concerns.** Payload storage is on by default; the opt-out is a priced add-on outside Enterprise. De-identified execution metadata may be used for model training and retained indefinitely. The Privacy Policy does not name a data protection officer or an EU representative.

### I — Identity & Control (6/10, Mid)

| Criterion | Result | Score | Evidence URL |
|---|---|---|---|
| Emergency stop documentation | Scoped API keys can be deleted (permissions fixed at creation; rotation documented); connected-account revoke operation exists where the provider supports programmatic revocation, otherwise the docs direct users to the provider's connected-app settings; the sandbox can be disabled. No single documented procedure states that revocation or key deletion stops in-flight agent execution immediately. Documented but incomplete. | 2 | https://docs.composio.dev/kb/guide/platform-connected-accounts · https://docs.composio.dev/reference/authenticating-to-composio/project-api-key-permissions |
| Human-in-the-loop design | Approvals (elicitation-based sign-off before a gated tool runs) exist but are "off by default", experimental, and bypassable by Workbench/bash scripts unless the sandbox is disabled; MCP clients without elicitation support have gated calls denied unless a fallback is set to "allow". Optional. | 1 | https://docs.composio.dev/docs/approvals |
| Permission delegation transparency | Scoped project API keys with documented permission areas and access levels (auth configs, connected accounts, tools, session management, session tool execution, triggers, webhooks, observability, MCP, proxy execute); per-session tool and connected-account scoping; OAuth scope control documented; token custody and execution paths documented. | 3 | https://docs.composio.dev/reference/authenticating-to-composio/project-api-key-permissions · https://docs.composio.dev/docs/security/token-custody |

**Positive findings.** The permission model is documented at the route level, and the token-custody page explains which code path holds a credential in each execution mode.

**Recorded concerns.** Approval gating is opt-in and experimental; default project API keys retain full project access.

### C — Containment (3/10, Low)

| Criterion | Result | Score | Evidence URL |
|---|---|---|---|
| Sandbox design | Tool access per session is allowlist-based (configured tools and connected accounts; "Set the tools each session can use"). The Firewall screens tool results with a model and the 2026-07 CLI fix is a sensitive-file denylist. The code sandbox (Workbench) runs on E2B ("isolated cloud sandboxes", per the sub-processor list); Composio publishes no isolation model or network policy for it, and the May 2026 incident involved arbitrary code execution in the tool-execution environment through registered tool definitions. Hybrid. | 2 | https://composio.dev/enterprise · https://trust.composio.dev/subprocessors · https://docs.composio.dev/docs/workbench |
| Least privilege | Vendor states "least-privilege defaults"; in practice default project API keys have full project access, scoped keys are opt-in, the sandbox is enabled by default in standard sessions, and payload logging is on by default. Configurable. | 1 | https://docs.composio.dev/docs/security/overview · https://docs.composio.dev/reference/authenticating-to-composio/project-api-key-permissions |
| Tenant isolation (cloud) | Organization and project isolation stated; credentials AES-256-GCM at rest; SOC 2 Type II attested. In May 2026 an attacker inside Composio-operated infrastructure exfiltrated connected-account tokens belonging to many customers (about 0.3% of active connections; 5,001 GitHub) and reached a cache holding 5,241 API keys, from an auxiliary service. The vendor's bulletin does not characterize customer-to-customer access; the exposure crossed tenant boundaries from the operator's side. Past multi-tenant credential breach. | 0 | https://composio.dev/blog/composio-may-2026-security-incident · https://docs.composio.dev/docs/security/overview |

**Positive findings.** Proxy Execute is restricted to the connected account's registrable domain and requires its own permission; customer-managed-key, private-VPC and self-hosted deployments are documented as Enterprise options. Post-incident remediation (per the vendor) removed token return from APIs, moved to envelope encryption for OAuth credentials and hash-only storage of API and session keys, and rebuilt the tool-building service.

**Recorded concerns.** The sandbox isolation boundary is not published; least privilege is available rather than default; the May 2026 incident demonstrated a path from internal tooling through the execution environment to customer credentials.

### T — Transparency (5/10, Mid)

| Criterion | Result | Score | Evidence URL |
|---|---|---|---|
| CVE publication posture | Published security policy (GitHub Security Advisories preferred, security@composio.dev; 48-hour acknowledgement, 7-day response). The vendor is not a CNA; the window's CVEs were assigned by MITRE (CVE-2025-56427) and VulnCheck (CVE-2026-59807). The CVE-2026-59807 fix commit references GHSA-hp3h-89pf-5q58, whose publication could not be confirmed in-session; the sweep found no published repository advisories in the window. Release notes carry fixes. No vendor-issued CVEs; fix notes only. | 1 | https://github.com/ComposioHQ/composio/blob/main/.github/SECURITY.md · https://github.com/ComposioHQ/composio/releases |
| Incident disclosure speed | May 2026 incident: review window 2026-05-21 01:05–09:15 PT; public bulletin "Published May 21, 2026", versioned 2026-05-23 to 2026-05-27 and updated 2026-09-16 with a remediation summary; Trust Center non-impact statement for the Vercel incident published 2026-05-12 (Vercel disclosure 2026-04-19). Same-day disclosure, ≤30 days. | 2 | https://composio.dev/blog/composio-may-2026-security-incident · https://trust.composio.dev |
| AI safety framework reference | Trust Center Compliance lists SOC 2 and ISO 27001:2022 only; no NIST AI RMF, ISO 42001 or other AI framework in the docs, Firewall page, legal documents or Trust Center. None. | 0 | https://trust.composio.dev · https://composio.dev/firewall |
| Security policy publication | Security overview (isolation, key scoping, MFA, encryption, webhook signing) plus DPA Attachment 3 (nine-point technical and organizational measures: access control, vulnerability management, segmentation, DLP, encryption, secure SDLC with OWASP Top Ten, personnel screening). Detailed technical and organizational. | 2 | https://docs.composio.dev/docs/security/overview · https://composio.dev/legal/dpa |
| AI system identity disclosure | No documentation that end users or counterparties are informed that an action was taken by an AI agent via Composio. | 0 | https://docs.composio.dev/docs/security/overview |

**Positive findings.** The May 2026 incident was disclosed on the day of the review window, kept as a versioned public page, and followed by a dated remediation summary naming the third-party responders (IntrusionOps), testers (AppSecure Security) and reviewers (Latacora). The security policy sets explicit acknowledgement and response timelines, and the DPA's technical measures annex is specific.

**Recorded concerns.** The vendor issues no CVEs or published advisories for its own SDK defects; the incident bulletin does not state the initial-access date, the detection time or whether payload data was accessed; AI identity disclosure is absent.

---

## Incident Timeline

| Date | CVE ID | CVSS | Description | Patch status | KEV |
|---|---|---|---|---|---|
| 2026-05-21 | — (security incident, no CVE) | — | Attacker gained a foothold in an internal agentic infrastructure-monitoring tool, reached automated remediation systems, registered malicious tool definitions in the sandboxed execution environment and ran code there, and reached an auxiliary credential cache. Separately, employee Gmail OAuth tokens were compromised and magic-link sign-in abused on auxiliary systems. Exposure: about 0.3% of active connections (5,001 GitHub, 12 Gmail, 1–12 each on other toolkits) and 5,241 API keys; GitHub review window 01:05–09:15 PT on 2026-05-21. | Disclosed 2026-05-21; API keys created before 2026-05-22 23:00 PST deleted from 2026-05-23; OAuth tokens revoked across ~100 toolkits; Buildkite revocations completed 2026-05-24; remediation summary 2026-09-16 | No |
| 2026-05-12 | — (`dependency: Vercel`) | — | Vendor statement of non-impact from the Vercel April 2026 security incident (Vercel disclosure 2026-04-19); environment variables rotated as a precaution. | Not applicable | No |
| 2026-07-03 | CVE-2026-59807 | 6.8 (CNA v3.1; v4.0 8.9) | Missing `assertSafeFileUploadPath` check in `readFileFromDisk` (`tool-file-uploads.ts`), `@composio/*` before 0.2.32-beta.283; prompt injection can direct the CLI to upload sensitive local files. Public issue #3746 (datePublic 2026-07-03); CVE published 2026-07-08. | Fixed 2026-07-07 (commit fc17c37, `@composio/cli@0.2.32-beta.283`); 4 days | No |
| 2025-12-04 | CVE-2025-56427 | 7.5 (CISA-ADP v3.1) | Directory traversal via `_download_file_or_dir` in `composio` 0.7.20 (legacy Python server module). PoC published (TOAST-Research). | No vendor advisory or fixed version recorded; module absent from current SDK (v3 line from 0.8.0, 2025-07-21) | No |

History (outside window, not counted):

| Date | CVE ID | CVSS | Description | Patch status | KEV |
|---|---|---|---|---|---|
| 2025-03-20 | CVE-2024-8953 | 9.8 (NVD v3.1; CNA v3.0 7.2) | Unsafe `eval()` in `mathematical_calculator` (`composio-core` 0.4.3). Huntr report; GHSA-5xg7-5662-8x7j. Same calculator.py code path as CVE-2024-8864. | Fixed in 0.5.43 per GHSA | No |
| 2025-03-20 | CVE-2024-8952 / 8954 / 8955 / 8958 | 9.1 / 9.8 / 7.5 / 9.8 | SSRF (×2), `x-api-key` authentication bypass, unrestricted file read/write in legacy `composio-core` 0.4.x–0.5.10 | Per advisories | No |
| 2025-01-08 | CVE-2024-53526 | 6.4 | Command execution via `handle_tool_calls` in `composio_openai` / `composio_claude` / `composio_julep` (≥0.5.40) | Issue #1073 | No |
| 2024-09-15 | CVE-2024-8864 | 8.8 (NVD v3.1; CNA 5.5) | Code injection in `Calculator` (`calculator.py`), ≤0.5.6. VulDB record states the vendor was contacted and did not respond. | Fixed in 0.5.43 (same code path as CVE-2024-8953) | No |
| 2024-09-15 | CVE-2024-8865 | 3.5 | Path traversal in `composio/server/api.py` (≤0.5.8). VulDB record states the vendor was contacted and did not respond. | Not recorded | No |

---

## Contextual Analysis

**Operator of record.** The base record carries "Composio Inc. · San Francisco." The vendor's current legal pages name the entity as Sampark, Inc. d/b/a Composio, a Delaware company at 2 Bryant St., Suite 220, San Francisco (DPA, last updated 2026-10-17); the Terms of Service and Privacy Policy, both effective 2026-10-17, open with "Sampark Inc, doing business as Composio"; the repository LICENSE reads "Copyright (c) 2025 Sampark Inc." Earlier Privacy Policy editions (effective 2024-01-01) already named Sampark Inc. Per Evaluation Sequence step 2 the public record governs: the operator is recorded as Sampark, Inc. d/b/a Composio. Venture Intelligence (2025-07-23, secondary) describes the company as headquartered in Bengaluru and San Francisco; the legal pages give only the San Francisco address. No acquisition or change of control was found; `independence` is recorded as independent and `parent_entity` as null.

**Disclosure layer.** A USD 25 million Series A was reported on 2025-07-23 as led by Lightspeed Venture Partners, with Elevation Capital, Together Fund and angel investors (Venture Intelligence, secondary); Lightspeed's own portfolio page lists two 2025 Series A investments (LSVP and LSIP) in Composio without stating a lead. CB Insights lists additional Series A participants including HubSpot, SV Angel, Operator Partners and Blitzscaling Ventures. None of Amazon, Google, Microsoft or NVIDIA appears on the public record as an investor, parent or non-arms-length channel partner, and Composio is not an Anthropic product. Triggers 0–3 do not fire; no disclosure tags are applied. Product-level integration (Anthropic listed as one of many supported model providers; Claude as one of several supported agent harnesses) is an industry-standard relationship under the framework's non-trigger list.

**Vulnerability record and the eval() question.** The base record describes a "recurring eval() pattern (CVE-2024-8864/8953)." The two records describe the same `calculator.py` `eval()` call in the legacy `composio-core` package (VulDB entry 2024-09-15 for ≤0.5.6; huntr report, CVE published 2025-03-20 for 0.4.3), fixed in 0.5.43 per the GitHub advisory: one root cause with two identifiers, not a recurrence. The pattern that does recur on the record is file-path validation, with reports in 2024 (CVE-2024-8865, CVE-2024-8958), 2025 (CVE-2025-56427) and 2026 (CVE-2026-59807), and an internally fixed instance in May 2026 (SEC-316). This is the basis for the structural-issues score of 0.

**Disclosure handling.** The 2024 VulDB records state the vendor was contacted and did not respond within the reporter's window; no fix release is recorded against the 0.5.x line for CVE-2024-8864/8865 beyond the 0.5.43 advisory. In 2026 the pattern differs: the CVE-2026-59807 report was posted as a public issue on 2026-07-03, the fix commit landed on 2026-07-07 with a release the same day, and the repository SECURITY.md now sets a 48-hour acknowledgement and 7-day response commitment. CVE-2025-56427 (0.7.20) has no vendor advisory; the affected server module is not present in the v3 SDK line that had been the current release for over four months at disclosure, so the exposure is confined to installations that remained on 0.7.x.

**Data conduct after the T5 change.** The 2026-10-17 revision is more specific than the previous policy: it defines Payload Data and Execution Metadata, states that payload data is not used for model training, sets a one-year payload retention and 30-day deletion on organization removal, and binds the DPA by in-dashboard acceptance (no countersignature). The carve-out permitting training on de-identified execution metadata, retained indefinitely, is stated in all three documents. The vendor's position is that this metadata excludes payloads, error text and all account identifiers.

**May 2026 security incident.** The vendor's bulletin (published 2026-05-21, versioned through 2026-05-27, updated 2026-09-16) describes an attack chain that began with a foothold in an internal agentic tool used to monitor infrastructure and report connector failures, moved through automated remediation systems into the sandboxed tool-execution environment via registered tool definitions, and ended at an auxiliary credential cache; a leaked GitHub token also gave access to a production codebase, and employee Gmail OAuth tokens were abused for magic-link sign-in on auxiliary systems. The stated scope is about 0.3% of active connections and 5,241 API keys in the cache during the breach window; the bulletin does not state the initial-access date, the detection timestamp, whether payload logs were read, or whether the attacker moved between customer tenants, and says the vendor is "not characterizing specific data exposure at this time." Composio's remediation, as published: all GitHub tokens and OAuth tokens on ~100 toolkits revoked, API keys created before 2026-05-22 deleted, APIs changed to stop returning connected-account tokens and custom OAuth secrets, envelope encryption for OAuth credentials and hash-only storage of API and session keys, the tool-building service rebuilt with OIDC, over 50 third-party providers contacted, and independent testing by AppSecure Security and a cloud/GitHub review by Latacora with findings closed or in progress. Under 5% of connections (API-key connections) could not be revoked by Composio and required end-user rotation. Independent coverage (Material Security, 2026-06-03; Metorial, 2026-05-22) reports the same scope figures and attributes them to the vendor's disclosure. The incident carries no CVE and is recorded in the Incident Timeline; it is not a package or build-artifact compromise on the public record and is therefore not entered as a supply chain compromise. It is the basis for the C tenant-isolation score of 0, and the same-day disclosure is the basis for the T incident-disclosure score of 2.

**Trust Center.** trust.composio.dev is a Vanta-hosted application that renders client-side and returned no readable content to session tools; the operator supplied the rendered text (retrieved 2026-10-27 JST, no access request submitted). Resources: SOC 2 Type II report, four policies, an engagement letter and a pentest report dated 7 October 2026 are behind "Request access"; the ISO 27001 certificate, SOC 2 bridge letter, DPA and BAA are viewable. Compliance lists SOC 2 and ISO 27001:2022. The sub-processor list has eight entries and no date. These readings replace the provisional floors in the first draft; the resulting criterion scores are unchanged from the floors (V dependency 1, V certification 2, D sub-processor 1, T framework 0).

**Firewall and approvals.** Composio has added an approval flow (elicitation before gated tools run) and a Firewall that screens tool results for injected instructions. Both are opt-in; approvals are marked experimental and can be bypassed by sandbox scripts unless the sandbox is disabled. The enterprise page lists "Permitted tools, checked in context" as coming soon.

**Sweep candidate disposition.** The two NVD keyword candidates in the sweep resolve to CVE-2026-59807 (product-scoped, counted) and CVE-2025-56427 (product-scoped, counted); PYSEC-2026-1262 and PYSEC-2026-1263 (2026-07-07) are PyPI advisory re-issues of CVE-2025-56427 and CVE-2024-8955 and are not counted separately.

**KNOWN_FACTS candidate (staged for Operations).** Entity: Composio / Sampark, Inc. — Operator: Sampark, Inc. d/b/a Composio, Delaware; 2 Bryant St., Suite 220, San Francisco, CA 94105; support@composio.dev, security@composio.dev (DPA 2026-10-17; ToS/Privacy 2026-10-17; repository LICENSE). Status: independent; USD 25M Series A reported 2025-07-23 led by Lightspeed (secondary); no Trigger 0–3 relationship found. Do NOT state: "Composio Inc." as the legal entity; "recurring eval() CVE pattern" (CVE-2024-8864 and CVE-2024-8953 describe the same calculator.py flaw); that the complete product is open source (SDKs/CLI MIT, hosted platform closed; V source code 2). Approved language: "Composio, operated by Sampark, Inc. d/b/a Composio (Delaware; San Francisco); MIT-licensed SDKs and CLI with a closed hosted platform (open core)." Root cause: the #025 migrated capture (2026-03-30) carried a trade-name operator string and a key finding that read two identifiers for one flaw as a recurrence.

---

## VERDICT Record

**Summary.** Composio scores 48/85 (Tier B) at the 2026-10-30 update: a published DPA with a no-training statement for payload data, documented permission scoping and token custody, a same-day disclosed and documented May 2026 incident response, and a four-day fix for the 2026 CVE, set against a multi-customer credential exposure in that incident, recurring file-path validation defects, opt-in approval and least-privilege controls, and no vendor advisories or AI-identity disclosure on the public record.

**Risk Factor Summary by Use Case**

| Use case | Risk factors recorded |
|---|---|
| Internal testing | MIT SDKs and CLI; free tier; payload logging on by default (ZDR priced); CLI file-upload path had a 2026 path-validation CVE, fixed from 0.2.32-beta.283. |
| Credential-handling workloads | Credentials held by Composio Cloud (AES-256-GCM at rest; envelope encryption and hash-only key storage stated post-incident); May 2026 incident exposed ~0.3% of connections and 5,241 API keys; customer-managed-key, VPC and self-hosted options are Enterprise arrangements; recurring path-handling defects in SDK file paths. |
| Cloud multi-tenant | Org/project isolation stated, SOC 2 Type II attested (report on request); May 2026 multi-customer credential exposure from an operator-side auxiliary service; sandbox runs on E2B, isolation model not published. |
| Regulated-data workloads | DPA with SCCs/UK Addendum/Swiss FADP accepted in-dashboard; BAA offered; ZDR excludes triggers, audit logs and telemetry; de-identified execution metadata retained indefinitely; 8 sub-processors listed without a date; whether payload logs were read in the May 2026 incident is not characterized. |

**Reference Information** (options, not instructions)
1. Enable Zero Data Retention per project and review what ZDR does not cover (triggers, search caches, telemetry) before routing sensitive payloads.
2. Issue scoped project API keys with IP allowlisting and grant Proxy Execute only where raw provider access is required.
3. Where approvals are used, disable the sandbox for sessions where approval must not be bypassed, or route gated tools through `session.execute()`.

**Bias Disclosure**

> "This evaluation uses Claude (Anthropic) as its tooling. Anthropic operates in the AI agent market and may compete with some evaluated vendors. VERDICT discloses this relationship in every report and applies identical evaluation criteria to all platforms regardless of their relationship to Anthropic."

---

## Future Evaluation Plan

- **Layer 1:** not scheduled; free-tier behavioral testing (30 runs × 4 difficulty levels over 3+ days) may be scheduled at Operations' discretion.
- **Layer C:** routine review 365 days from `updated_at` (pipeline-derived); interrupt lane active — T1 on any new CVE/GHSA attributable to `composio` / `@composio/*` / composio.dev, T4 on further incident reporting, T5 on further legal-page or ownership changes.
