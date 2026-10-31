# VERDICT Evaluation #005 — Activepieces — Update

| Field | Value |
|---|---|
| Evaluation number | #005 |
| Platform | Activepieces |
| Evaluation type | Update (Differential Evaluation, T1 interrupt lane) |
| Date | 2026-10-31 |
| Evaluator | VERDICT evaluation engine (Claude, Anthropic); `evaluator_model: claude-fable-5-1` (operator selection, batch 1) |
| Target version | 0.92.3-hotfix.2 (released 2026-10-28; https://github.com/activepieces/activepieces/releases/tag/0.92.3-hotfix.2) |
| Framework | VERDICT v0.3.2 (`zinova-lab/verdict-engine` @ 84b2fa9) |
| Previous evaluation | 2026-03-13 · 52/85 · Tier B · framework v0.3.1 (migrated capture) |
| Operator of record | Activepieces Inc., 95 Third Street, 2nd floor, San Francisco, CA 94103 (Terms, https://www.activepieces.com/terms; Privacy Policy, https://www.activepieces.com/privacy) |
| Independence | Independent · no parent entity |
| Trigger | T1 (repository GHSA set diverges from recorded R facts; quarterly sweep 2026-10-27) |

## Executive Summary

Activepieces scores 36/85 (Tier C) at Layer 0, down from 52/85 (Tier B) on 2026-03-13; the 16-point movement is driven by R (Resilience, 15 → 4), D (Data Conduct, 10 → 4) and V (Verifiability, 13 → 12). The trailing 12 months (2025-11-01 to 2026-10-31) contain eight CVEs attributed to the Activepieces product, with a maximum CVSS of 9.3 (CVE-2026-48499, cross-tenant data exposure and code injection via the Code piece sandbox cache, CNA v4.0), plus a CVE-less advisory rated 9.2 (GHSA-m992-8rcw-vmrx, queue dashboard exposed without authentication); the prior record's "zero CVEs" rested on a migrated capture without sources. The vendor published seven of the eight CVEs through its own GitHub advisories, with the fix release preceding public disclosure in each case, and it disclosed a November 2025 piece-metadata insertion event within three days. The recorded "HIPAA-compliant" and "Germany-hosted" facts were re-verified: the vendor's current pricing page states that its SOC 2 program is in progress and makes no HIPAA or BAA claim, while cloud hosting in Germany (Frankfurt) is confirmed on the vendor's security practices and pricing pages. The product is open core (MIT core with a commercially licensed `packages/ee` directory); the vendor's trust center publishes an undated sub-processor list of eight entries and a vulnerability disclosure program, while its DPA, penetration-test report and policies are listed as restricted documents.

## Scorecard

| Dimension | Score | Max | Rating |
|---|---|---|---|
| V — Verifiability | 12 | 20 | Mid |
| R — Resilience | 4 | 20 | Low |
| D — Data Conduct | 4 | 15 | Low |
| I — Identity & Control | 6 | 10 | Mid |
| C — Containment | 4 | 10 | Mid |
| T — Transparency | 6 | 10 | Mid |
| E — Effectiveness | — | 15 | Not evaluated (Layer 1+) |
| **Layer 0 total** | **36** | **85** | |

Tier: C
Category: Workflow Automation · Open Core (MIT core + Commercial License `packages/ee`)

CISA KEV: None. The KEV JSON feed (catalogVersion 2026.10.30, dateReleased 2026-10-30T17:02:45Z, 1,766 entries; https://www.cisa.gov/sites/default/files/feeds/known_exploited_vulnerabilities.json, operator-retrieved 2026-10-31 per OperatorInput-001) contains none of the eight Activepieces CVE IDs and no entry naming Activepieces. Corroborated by the catalog's vendor filter (https://www.cisa.gov/known-exploited-vulnerabilities-catalog, session-checked 2026-10-31) and per-CVE "not listed" status at https://app.opencve.io/cve/CVE-2026-48499, https://www.strix.ai/cve/CVE-2026-73083, https://www.strix.ai/cve/CVE-2026-73082 and https://www.sentinelone.com/vulnerability-database/cve-2026-73081/.

Previous score: 52/85 (2026-03-13).

## Differential

| Item | Value |
|---|---|
| Previous evaluation date | 2026-03-13 |
| Previous score | 52/85 (Tier B, framework v0.3.1) |
| Base record | `verdict-platforms/platforms/activepieces.md` @ e9a717f (migrated capture; `sources: []`; `updated_at: 2026-05-13` is a migration-era field, not an evaluation) |
| Trigger | T1 — repository GHSA set (9 published advisories in the trailing 12 months, max CVSS 9.2) against a recorded `cve_count_12mo: 0`; sweep 2026-10-27 |
| Routine lane | Not due (365-day interval, ReviewCadence-002) |

Per-dimension state:

| Dimension | State | Basis |
|---|---|---|
| V | re-evaluated | migrated capture, no per-dimension sources |
| R | re-evaluated | T1 mandatory re-check; migrated capture, no per-dimension sources |
| D | re-evaluated | migrated capture, no per-dimension sources |
| I | re-evaluated | migrated capture, no per-dimension sources |
| C | re-evaluated | migrated capture, no per-dimension sources |
| T | re-evaluated | migrated capture, no per-dimension sources |
| E | null | Layer 1+ only |

Carry-forward checks performed: none could be positively satisfied. The base record cites no source URL for any dimension, so carry-forward conditions 1–4 (ENGINE.md, Differential Evaluation) cannot be met; every dimension is re-evaluated from sources retrieved on 2026-10-31.

Prior-record omissions, stated as facts:
- The base record stated `cve_count_12mo: 0`, `max_cvss_12mo: null` and R 15/20. Eight CVEs attributed to the Activepieces product were first publicly disclosed inside the window ending 2026-10-31 (window entry dates 2026-06-21 to 2026-07-18); the base record's own window (ending 2026-03-13) is not re-computed here, and the migrated capture carries no sources against which that earlier count could be checked.
- The base record stated "HIPAA-compliant — the only platform in this index to achieve it." The vendor's current public documentation makes no HIPAA or BAA claim for the hosted service (pricing page, retrieved 2026-10-31); the vendor's blog (2026-01-16) frames HIPAA suitability as dependent on self-hosting. The comparative "only platform" clause is not carried (Absolute Rule 7).
- The base record stated "1 Advisory (Low) · 2025." The repository shows nine published advisories: one Low (2025-11-29) and eight published between 2026-07-13 and 2026-08-09 (one Critical, three High, four Moderate).
- The base record recorded `operator: Independent · Y Combinator` with `independence: unrecorded`. The operator of record is Activepieces Inc. (vendor's Terms and Privacy Policy); independence is set from the public record.

Operator-supplied input (OperatorInput-001; public data, rendered text retrieved by the operator on 2026-10-31 JST; no access-request form was submitted):

1. CISA KEV JSON feed, https://www.cisa.gov/sites/default/files/feeds/known_exploited_vulnerabilities.json — catalogVersion 2026.10.30, dateReleased 2026-10-30T17:02:45Z, count 1,766. None of CVE-2026-12813, CVE-2026-53535, CVE-2026-53536, CVE-2026-48499, CVE-2026-73081, CVE-2026-73082, CVE-2026-73083, CVE-2026-73084 is present; no entry names "activepieces" in vendorProject, product or shortDescription. Used for the Scorecard KEV line and `cisa_kev`.
2. Vendor trust center, https://trust.activepieces.com (served by Oneleet) — tabs Compliance, Documents, Security Controls, Subprocessors, Vulnerability Disclosure Program. Compliance: "SOC 2 Type 2 — In progress." Documents: five restricted items (Q1 2026 Pentest, Incident Response Policy, ConstellationGRC SOC 2 Engagement Letter, Vulnerability Management Policy, SOC 2 Type 2 Letter of Engagement), none public. Subprocessors: eight entries (Cloudflare, Digital Ocean, Google Workspace, Hetzner, Linear, Oneleet, OpenRouter, PostHog) with purpose and PII flags for most; no per-entry processing location in the default view; no last-updated date for the list (the page-level "Updated 35 minutes ago" marker is a live monitoring marker, not a list revision date). Vulnerability Disclosure Program: Cloud in scope, self-hosted out of scope, 7-business-day response, safe harbor, coordinated disclosure with a default embargo of up to 60 days, reward table by CVSS 4.0 severity, private invitation-only reward eligibility. Used for V third-party dependency disclosure, V independent certification, D sub-processor transparency and T security policy publication.

Pages the session tools could not read: the CISA KEV JSON feed and trust.activepieces.com (covered by the operator input above); the Tracxn and Crunchbase company profiles (not used). The Activepieces sandboxing mode table (`execution-mode.mdx` snippet) is not rendered in the fetched docs page; the environment-variables reference was used for the default instead.

## Dimension Detail

### V — Verifiability (12/20, Mid)

| Criterion | Result | Score | Evidence |
|---|---|---|---|
| Developer / company identity | Confirmed. Legal entity "Activepieces Inc." with an office address is named in the vendor's Terms (last updated 2023-11-29) and Privacy Policy (last updated 2026-01-19); contact@activepieces.com (Privacy Policy) and security@activepieces.com (repository SECURITY.md) published. Corporate registration confirmed by the vendor's legal page naming the legal entity; no registry was queried; state of organization not published (governing law is Delaware). | 4 | https://www.activepieces.com/terms ; https://www.activepieces.com/privacy ; https://github.com/activepieces/activepieces/security |
| Source code disclosure | Open core. Core released under the MIT license (`LICENSE`); enterprise and cloud features in `packages/ee` and `packages/server/api/src/app/ee` under a Commercial License (Criterion-VSource-001). | 2 | https://github.com/activepieces/activepieces ; https://www.activepieces.com/docs/about/license.md |
| Version management transparency | GitHub releases carry per-tag notes (bug-fix lists with PR links; hotfix notes naming the fix); a monthly product changelog is published in the docs. | 3 | https://github.com/activepieces/activepieces/releases ; https://www.activepieces.com/docs/about/changelog.md |
| Third-party dependency disclosure | Sub-processor list published on the vendor trust center (8 entries with purpose and PII flags); no last-updated date for the list. The pricing page separately offers the list "on request." | 1 | https://trust.activepieces.com/?tab=subprocessors (operator input, retrieved 2026-10-31) ; https://www.activepieces.com/pricing |
| Independent certification | None. Trust center and pricing page state "SOC 2 Type 2 — In progress"; the engagement letters and the Q1 2026 penetration-test report are restricted documents; no attestation report, SOC 3 or other certification is public. | 0 | https://trust.activepieces.com/?tab=compliance (operator input, retrieved 2026-10-31) ; https://www.activepieces.com/pricing |
| Functional reproducibility docs | API endpoint reference and architecture documentation (durable execution, waitpoints, sandboxing, execution isolation) published. | 2 | https://www.activepieces.com/docs/llms.txt ; https://www.activepieces.com/docs/install/architecture/waitpoints.md ; https://www.activepieces.com/docs/install/guarantees/execution-isolation.md |

Positive findings: the legal entity and two contact channels are published on the vendor's own pages; the MIT core is fully inspectable; release notes are published per tag, including for backported hotfix lines; a trust center lists sub-processors and security controls and states that a penetration test was performed within the last 12 months.

Recorded concerns: the sub-processor list carries no revision date and no processing locations in its default view; no independent attestation report is public (SOC 2 Type 2 in progress, engagement letters restricted); the Terms' last-updated date (2023-11-29) predates the hosted agents and enterprise features now sold.

### R — Resilience (4/20, Low)

Window: 2025-11-01 to 2026-10-31. Product scope bound to `target_version` 0.92.3-hotfix.2 (the `activepieces` platform repository and its hosted editions); individual "pieces" are in scope only where the advisory names the core platform.

| Criterion | Result | Score | Evidence |
|---|---|---|---|
| CVE count (trailing 12 months) | 8 (basis: exact): CVE-2026-12813, CVE-2026-53535, CVE-2026-53536, CVE-2026-48499, CVE-2026-73081, CVE-2026-73082, CVE-2026-73083, CVE-2026-73084. Base 1 (6–9). Penalty −1 for CVSS 9.0+ (CVE-2026-48499, 9.3). | 0 | Incident Timeline below; https://github.com/activepieces/activepieces/security/advisories ; https://fieldguide.lutrasecurity.com/CVE-2026-12813/ |
| Maximum CVSS severity | 9.3 — CVE-2026-48499, CNA (GitHub) CVSS v4.0 `CVSS:4.0/AV:N/AC:L/AT:N/PR:L/UI:N/VC:H/VI:H/VA:N/SC:H/SI:H/SA:N`; NVD carries the same v4.0 score as a secondary source; no NVD v3.1, CNA v3.1 or CISA-ADP score exists (Attribution-CVE-002 order). The repository advisory page displays 8.6 with a vector lacking the subsequent-system impacts (SC:N/SI:N); the CVE record's score is recorded and the GHSA display noted. | 0 | https://app.opencve.io/cve/CVE-2026-48499 ; https://github.com/activepieces/activepieces/security/advisories/GHSA-5h2x-g6m3-grmq |
| Patch response speed | For the seven vendor-published advisories, the fixed release (0.80.0, 0.82.0, 0.83.0, 0.84.0) preceded public disclosure (coordinated disclosure; ≤7 days). For CVE-2026-12813 (VulDB CNA, 2026-06-21, affects ≤ 0.83.0) no vendor advisory or fixed version was located; the VulDB record states the vendor did not respond to early contact. | 3 | Advisory pages in the Incident Timeline; https://stack.watch/vuln/CVE-2026-12813/ |
| Structural issues | Same weakness class recurring in separate components: unvalidated identifiers used in on-disk paths (CVE-2026-53535 git-sync; CVE-2026-48499 sandbox cache), outbound requests to user-supplied URLs without validation (CVE-2026-73082 MCP validation endpoint; CVE-2026-12813 file URL handler), and GHSA-m992-8rcw-vmrx is described by the vendor as a regression of a previously enforced authentication check. | 0 | https://github.com/activepieces/activepieces/security/advisories/GHSA-qqcr-rg2x-97mm ; https://github.com/activepieces/activepieces/security/advisories/GHSA-7qx9-q4xx-rh59 ; https://github.com/activepieces/activepieces/security/advisories/GHSA-m992-8rcw-vmrx |
| Supply chain compromise (trailing 12 months) | One event. On 2025-11-26 a piece named "poc-piece" was inserted into the vendor's cloud piece registry through an internal endpoint used by the CI/CD system, whose authentication logic had an issue after a refactor; the metadata synced to self-hosted instances. The referenced npm package did not exist, the team claimed the name, and the advisory records no code and no impact. Advisory published 2025-11-29 (3 days); 0.72.0 adds metadata retraction. Recorded as the vendor's own distribution endpoint reached without authorization; responded ≤7 days. | 1 | https://github.com/activepieces/activepieces/security/advisories/GHSA-3w4h-jvcx-rw99 |

Positive findings: the vendor runs a published security-advisory response playbook (CVSS 4.0 scoring, 3-business-day acknowledgement target, draft advisories, regression tests, coordinated disclosure) and credited external reporters on every advisory; fixes shipped before publication for all seven vendor-issued advisories; backported Node.js hotfixes were released on 2026-10-27/29 across the 0.82–0.92 lines.

Recorded concerns: eight CVEs and one CVE-less Critical advisory in a single window after a zero-advisory history; two cross-tenant issues (CVE-2026-48499, CVE-2026-53536); two sandbox-boundary issues in the default-recommended `SANDBOX_CODE_ONLY` mode (CVE-2026-73083, CVE-2026-48499); CVE-2026-12813 has no located vendor fix statement.

### D — Data Conduct (4/15, Low)

| Criterion | Result | Score | Evidence |
|---|---|---|---|
| GDPR compliance disclosure | Privacy Policy cites GDPR Article 6(1) lawful bases and EEA/UK rights and refers to "Data Processing Addendum(s), EU Model Clauses" for processors; the DPA is offered on request (pricing page), not published. | 1 | https://www.activepieces.com/privacy ; https://www.activepieces.com/pricing |
| Data minimization | Product analytics telemetry starts ON (`AP_TELEMETRY_ENABLED` default `true`); licensed instances also send a daily deployment snapshot, ON by default. Both can be switched off in Platform Admin; the environment variable opts a platform out from first read. | 1 | https://www.activepieces.com/docs/install/configure-operate/telemetry.md ; https://www.activepieces.com/docs/install/reference/environment-variables.md |
| AI training use | The Privacy Policy states that Google Workspace data is not used to develop, train or improve generalized AI; no statement covers other customer content. The Terms grant a license to use Customer Content "to develop and improve" the Software (section 8.4) and do not mention AI training. | 0 | https://www.activepieces.com/privacy ; https://www.activepieces.com/terms |
| Sub-processor transparency | List without date. The trust center lists eight sub-processors (Cloudflare — R2 application data, PII; Digital Ocean — main database, PII; Google Workspace — company documents and email; Hetzner; Linear — issue tracking; Oneleet — security assessment; OpenRouter; PostHog — application event tracking, PII) with no last-updated date and no per-entry processing location in the default view. The Privacy Policy separately names Google Analytics, Intercom, Mixpanel, Userback and Stripe, which do not appear on the trust-center list. | 1 | https://trust.activepieces.com/?tab=subprocessors (operator input, retrieved 2026-10-31) ; https://www.activepieces.com/privacy |
| Data retention disclosure | Retention stated as "for as long as your account is active" with deletion of unneeded data within 12 months of account termination; no per-category schedule. Audit-log retention is configurable (default forever) for the enterprise feature. | 1 | https://www.activepieces.com/privacy ; https://www.activepieces.com/docs/admin-guide/security/audit-logs/overview.md |

Positive findings: cloud hosting location (Germany / Frankfurt) is stated on the vendor's security practices and pricing pages; the Privacy Policy carries a dated last-updated line (2026-01-19), named lawful bases and a children's-data threshold (16); credentials are described as encrypted with 256-bit keys and masked in logs.

Recorded concerns: no general AI-training statement for customer content; no published DPA; the sub-processor list is undated and does not match the set of third parties named in the Privacy Policy; telemetry ON by default; the Privacy Policy states data is transmitted to the United States for contractual purposes and that Stripe processing occurs there, while the trust-center list names Digital Ocean and Hetzner as infrastructure providers without a displayed processing location.

### I — Identity & Control (6/10, Mid)

| Criterion | Result | Score | Evidence |
|---|---|---|---|
| Emergency stop documentation | Flows can be disabled ("Publish or toggle flows" permission). No documented control stops or cancels an in-flight or paused run; community threads from 2024–2025 report that cancelling a run is not possible, with no vendor answer in the thread. `AP_FLOW_TIMEOUT_SECONDS` (default 600) bounds a single run. | 2 | https://www.activepieces.com/docs/admin-guide/guides/permissions.md ; https://community.activepieces.com/t/can-i-cancel-a-paused-run/6238 ; https://www.activepieces.com/docs/install/reference/environment-variables.md |
| Human-in-the-loop design | Optional. An approval step (waitpoint barrier with resume URL, deadline from `AP_PAUSED_FLOW_TIMEOUT_DAYS`) is added by the flow author; a publish-time review gate ("Sensitive" projects, Flow Approvals) is off by default and requires the Enterprise/Cloud Environments tier. | 1 | https://www.activepieces.com/docs/install/architecture/waitpoints.md ; https://www.activepieces.com/docs/flows/flow-approvals.md ; https://www.activepieces.com/blog/activepieces-human-in-the-loop-a-complete-2026-guide.md |
| Permission delegation transparency | Project RBAC documented with a per-permission table for Admin / Editor / Operator / Viewer plus custom roles; agents are bound to a single project whose connections, flows and files set their reach. | 3 | https://www.activepieces.com/docs/admin-guide/guides/permissions.md ; https://www.activepieces.com/docs/agents/overview.md |

Positive findings: the permission matrix is explicit, including git-sync rights restricted to Admin; the approval mechanism is durable (paused runs survive restarts) and has a deadline.

Recorded concerns: no documented run-cancel control; human review is opt-in per flow or per project.

### C — Containment (4/10, Mid)

| Criterion | Result | Score | Evidence |
|---|---|---|---|
| Sandbox design | Hybrid. `SANDBOX_CODE_ONLY` runs each Code step in a fresh V8 isolate with `require` removed (capability-restricted); `SANDBOX_PROCESS` uses kernel namespaces with read-only mounts; the network guard (`AP_NETWORK_MODE=STRICT`) and the server-side SSRF filter are blocklist-based with `AP_SSRF_ALLOW_LIST` as the exception list. | 2 | https://www.activepieces.com/docs/install/architecture/sandboxing.md ; https://www.activepieces.com/docs/install/architecture/network-security.md |
| Least privilege | Configurable. `AP_EXECUTION_MODE` defaults to `UNSANDBOXED`; `AP_NETWORK_MODE` defaults to `UNRESTRICTED`; `AP_PROJECT_RATE_LIMITER_ENABLED` defaults to `false`. Docs recommend `SANDBOX_CODE_ONLY` for multi-tenant use and state that Cloud uses it. | 1 | https://www.activepieces.com/docs/install/reference/environment-variables.md ; https://www.activepieces.com/docs/install/architecture/sandboxing.md |
| Tenant isolation (cloud) | Claimed but unverified. Docs state execution isolation by sandbox and tenant data isolation by `projectId` / `platformId` query scoping at the application layer. Two cross-tenant vulnerabilities were disclosed in the window (CVE-2026-48499, CVE-2026-53536); no public report of exploitation or breach was located. | 1 | https://www.activepieces.com/docs/install/guarantees/execution-isolation.md ; https://github.com/activepieces/activepieces/security/advisories/GHSA-9723-fmff-mc24 |

Positive findings: the architecture docs describe each mode's isolation and its limits candidly (including that V8 isolation does not survive host-process compromise and that the user-code network guard is best-effort); the server-side SSRF filter is always on.

Recorded concerns: the shipped default is unsandboxed with unrestricted egress; cross-tenant isolation depends on application-layer scoping that two 2026 advisories show was bypassable before their fixes.

### T — Transparency (6/10, Mid)

| Criterion | Result | Score | Evidence |
|---|---|---|---|
| CVE publication posture | Issues CVEs (GitHub CNA) and GitHub advisories; nine published advisories, seven with CVE IDs. | 2 | https://github.com/activepieces/activepieces/security/advisories |
| Incident disclosure speed | The 2025-11-26 metadata insertion event was disclosed by advisory on 2025-11-29 (3 days). | 2 | https://github.com/activepieces/activepieces/security/advisories/GHSA-3w4h-jvcx-rw99 |
| Security policy publication | Security & Data Practices page (credential encryption, log masking, OAuth2 scopes, RBAC, SSO, audit logs, password hashing, hosting location), repository SECURITY.md (scope, researcher rules, 7-business-day response commitment, safe-harbor statement), a published advisory-response playbook (CVSS 4.0 scoring, acknowledgement and disclosure steps) and a trust center listing organizational controls (MFA for critical services, backups, vulnerability-management policy, supply-chain monitoring) and a vulnerability disclosure program with a default embargo of up to 60 days and a severity-based reward table. | 2 | https://www.activepieces.com/docs/admin-guide/security/practices ; https://github.com/activepieces/activepieces/security ; https://www.activepieces.com/docs/handbook/engineering/playbooks/security-advisory-response ; https://trust.activepieces.com/?tab=vulnerabilityDisclosure (operator input, retrieved 2026-10-31) |
| AI safety framework reference | None located (no NIST AI RMF, ISO 42001 or internal AI safety framework published). | 0 | https://www.activepieces.com/docs/agents/overview.md |
| AI system identity disclosure | None located. Agent documentation describes internal workers; no end-user AI identity disclosure is documented. | 0 | https://www.activepieces.com/docs/agents/overview.md |

Positive findings: every advisory names the reporter and the fixed version; the docs changelog and release notes identify security-motivated hotfixes (Node.js October 2026 advisories; the 0.92.3-hotfix.2 unauthenticated webhook-triggered API crash).

Recorded concerns: the docs changelog carries no security-advisory entries although the vendor's playbook describes drafting one per advisory; no AI safety framework or AI identity disclosure.

## Incident Timeline

| Date (window entry) | CVE ID | CVSS (source) | Description | Patch status | KEV |
|---|---|---|---|---|---|
| 2025-11-29 | — (GHSA-3w4h-jvcx-rw99) | Low (no score) | Unauthorized piece metadata ("poc-piece") inserted into the cloud registry via an internal CI/CD endpoint with an authentication logic issue; synced to self-hosted instances; no code existed; event 2025-11-26. | Removed from cloud; 0.72.0 adds retraction | No |
| 2026-06-21 | CVE-2026-12813 | 5.3 CNA v4.0 (VulDB); v3.1 6.3 also published by the CNA | SSRF in `handleUrlFile` (packages/server/engine, File URL Handler); affects ≤ 0.83.0; public exploit stated. | No vendor advisory or fixed version located | No |
| 2026-07-13 | CVE-2026-53535 (GHSA-qqcr-rg2x-97mm) | 5.9 CNA v4.0 | Arbitrary file write in git-sync via path traversal and symlinks (self-hosted EE, requires `WRITE_PROJECT_RELEASE`). CVE record published 2026-07-16. | Fixed 0.82.0 | No |
| 2026-07-13 | CVE-2026-53536 (GHSA-9723-fmff-mc24) | 5.3 CNA v4.0 | Cross-tenant file download via missing JWT audience check on `/v1/step-files/signed`. CVE record published 2026-07-16. | Fixed 0.83.0 | No |
| 2026-07-17 | CVE-2026-48499 (GHSA-5h2x-g6m3-grmq) | 9.3 CNA v4.0 (GHSA page displays 8.6) | Cross-tenant data exposure and code injection via the Code piece sandbox cache; authenticated flow author. CVE record published 2026-07-30. | Fixed 0.84.0 | No |
| 2026-07-17 | CVE-2026-73081 (GHSA-3pfv-m69p-5fv5) | 8.7 CNA v4.0 | RCE via command injection in Code step name (shell-invoked build, pre-sandbox). CVE record published 2026-08-11. | Fixed 0.80.0 | No |
| 2026-07-17 | CVE-2026-73083 (GHSA-gr3h-c2j7-r52g) | 7.6 CNA v4.0 | V8 isolate sandbox bypass via `importFresh` module loading in `SANDBOX_CODE_ONLY`. CVE record published 2026-08-11. | Fixed 0.80.0 | No |
| 2026-07-18 | CVE-2026-73082 (GHSA-7qx9-q4xx-rh59) | 5.3 CNA v4.0 | SSRF in MCP tool validation endpoint. CVE record published 2026-08-11. | Fixed 0.82.0 (hardened further in 0.83.0) | No |
| 2026-07-18 | CVE-2026-73084 (GHSA-hc39-cm5m-q8g7) | 6.1 CNA v3.1 | Reflected XSS in `/api/redirect` OAuth callback. CVE record published 2026-08-11. | Fixed 0.83.0 | No |
| 2026-08-09 | — (GHSA-m992-8rcw-vmrx) | 9.2 (GitHub advisory, v4.0) | Queue dashboard (Bull-Board) at `/api/ui` exposed without authentication in 0.80.0–0.84.0; vendor describes a regression. CVE-less; T1 (≥ 7.0). | Fixed 0.84.1 | No |
| 2026-08-08 | — (GHSA-864f-rcv7-6rh4) | not scored | `dependency: laverdet/isolated-vm` — sandbox escape (TOCTOU type confusion) in the isolate library used by `SANDBOX_CODE_ONLY`; fixed in isolated-vm 7.0.1 / 6.2.0. Not counted. | Upstream fix | No |
| 2026-10-28 | — | — | 0.92.3-hotfix.2: unauthenticated, webhook-triggerable crash of the API process (Return Response header sanitization). Release note; no advisory or CVE located. | Fixed 0.92.3-hotfix.2 | No |

`cve_count_12mo: 8` (basis exact); `max_cvss_12mo: 9.3`; `cisa_kev.present: false`; `supply_chain_compromise_12mo: true` (GHSA-3w4h-jvcx-rw99, as characterized above). No retroactive CVEs were identified.

## Contextual Analysis

The movement from 52/85 to 36/85 is a change in the record, not solely in the product. The base record was a migrated capture carrying no per-dimension sources; its R score of 15/20 rested on a zero-CVE window that the public record for the current window does not support. Evidence rule for this update: every factual claim was confirmed by web retrieval during the session; knowledge-based claims were not used.

On operator of record: the vendor's Terms and Privacy Policy name Activepieces Inc. at a San Francisco address; the recorded display string "Independent · Y Combinator" is replaced by that legal entity. The company's YC profile (batch S22) and secondary funding trackers name Y Combinator, Accel, Jawaker, Propeller and Foodics as seed-stage participants with no lead designation and no publicly stated amounts beyond USD 125K–500K figures that differ between trackers; none of Amazon, Google, Microsoft or NVIDIA appears on the record, and no acquisition is recorded. ENGINE.md disclosure Triggers 0–3 do not fire; the record carries none of the trigger tags.

On the advisory set: eight of the nine repository advisories were published between 2026-07-13 and 2026-08-09, after a period with a single Low advisory. All credit external reporters, and the vendor's handbook now publishes a security-advisory response playbook. The vendor's position, as stated in its own documentation, is that `SANDBOX_CODE_ONLY` is the multi-tenant-safe mode, that Cloud runs it, that the `UNSANDBOXED` mode is intended for trusted-operator deployments and is blocked in EE/Cloud production, and that infrastructure-level egress rules are the real network boundary. Two of the 2026 advisories (CVE-2026-73083, CVE-2026-48499) concern the boundary of that recommended mode before their fixes; the vendor fixed both before publication. The 9.3 score for CVE-2026-48499 comes from the CVE record issued by the same CNA whose advisory page displays 8.6; the difference lies in the subsequent-system impact metrics (SC/SI), which the CVE record sets to High. VERDICT records the CVE record's score and notes the display.

On the "HIPAA" and "Germany" facts: the vendor's security practices page states that cloud services are currently available only in Germany, and the pricing page names Frankfurt, so the hosting fact stands; the trust-center sub-processor list names Hetzner and Digital Ocean as infrastructure providers without a displayed processing location, which neither confirms nor contradicts it. The vendor's public pages, including the trust center's compliance tab, make no HIPAA or BAA claim for the hosted service; both the pricing page and the trust center state that SOC 2 Type 2 is in progress, and the trust center lists the engagement letters and a Q1 2026 penetration-test report as restricted documents.

On the trust center: it was not located by web search during the session and its rendered text was supplied by the operator (OperatorInput-001). Its vulnerability disclosure program scopes Cloud in and self-hosted deployments out, which is consistent with the repository SECURITY.md; the two documents together are the vendor's published position that issues exploitable only in `UNSANDBOXED` mode are outside scope because that mode is blocked in Cloud and EE production. The recorded phrase "HIPAA-compliant — the only platform in this index to achieve it" is therefore not carried. The vendor's own blog describes HIPAA suitability as a property of where and how the software is hosted.

On the queue dashboard advisory: the advisory states the dashboard is off by default (`AP_QUEUE_UI_ENABLED`), while the environment-variables reference lists the default as `true`. Both statements are the vendor's; the discrepancy is recorded without resolution.

On the November 2025 event: the vendor's advisory describes an unauthorized metadata insertion through an internal endpoint, with no code delivered and no impact, disclosed within three days. VERDICT records it under the supply-chain criterion because the vendor's own distribution endpoint was reached without authorization and the inserted metadata propagated to self-hosted instances; the vendor's characterization of the event as no-impact is recorded alongside.

Third-party evaluations: no Activepieces entry was located in the MIT AI Agent Index. The CTIPilot product page lists only the isolated-vm dependency advisory for Activepieces.

## VERDICT Record

**Summary.** Activepieces scores 36/85 (Tier C) at Layer 0 on 2026-10-31, down from 52/85: eight CVEs (max CVSS 9.3) and a CVE-less 9.2 advisory in the trailing 12 months, fixed before publication by the vendor, against an unsandboxed-by-default configuration, a published cloud hosting location in Germany, open-core licensing, an undated sub-processor list and no published attestation report.

**Risk Factor Summary by Use Case**

| Use case | Risk factors recorded |
|---|---|
| Internal testing / single-tenant self-hosted | Default `UNSANDBOXED` execution and `UNRESTRICTED` network mode; CVE-2026-73081 (command injection pre-sandbox) and CVE-2026-12813 (SSRF, no located fix) apply to flow authors; queue dashboard regression applies to 0.80.0–0.84.0. |
| Credential-handling workflows | Credentials encrypted at rest and masked in logs (vendor statement); CVE-2026-73083 and CVE-2026-48499 permitted reading embedded secrets or environment keys before 0.80.0 / 0.84.0; git-sync write (CVE-2026-53535) limited to `WRITE_PROJECT_RELEASE` holders. |
| Cloud multi-tenant | Two cross-tenant vulnerabilities in the window (CVE-2026-48499, CVE-2026-53536), both fixed; tenant data isolation enforced at the application query layer; no breach report located; SOC 2 in progress. |
| Regulated-data workloads | SOC 2 Type 2 in progress (no report public); DPA, pentest report and policies restricted; sub-processor list published but undated and without displayed processing locations; no HIPAA or BAA claim on vendor pages; retention stated without per-category schedule; EU (Frankfurt) cloud region published. |

**Reference Information** (options, not instructions)
1. Operators of self-hosted instances can compare their `AP_EXECUTION_MODE`, `AP_NETWORK_MODE` and `AP_QUEUE_UI_ENABLED` settings against the vendor's sandboxing and network-security documentation.
2. Deployments on 0.80.0–0.84.0 can be checked against GHSA-m992-8rcw-vmrx (fixed 0.84.1), and any deployment at or below 0.83.0 against CVE-2026-12813.
3. Organizations needing the DPA, the Q1 2026 penetration-test report or the security policies can request access through the vendor's trust center, where they are listed as restricted documents; the sub-processor list is viewable there without a request.

**Bias Disclosure**

> "This evaluation uses Claude (Anthropic) as its tooling. Anthropic operates in the AI agent market and may compete with some evaluated vendors. VERDICT discloses this relationship in every report and applies identical evaluation criteria to all platforms regardless of their relationship to Anthropic."

## Evaluation History

| Date | Type | Score | Tier | Framework |
|---|---|---|---|---|
| 2026-03-13 | Initial (migrated capture) | 52/85 | B | v0.3.1 |
| 2026-10-31 | Update (T1 differential, full re-evaluation) | 36/85 | C | v0.3.2 |

## Future Evaluation Plan

- Layer 1 (free-tier behavioral testing, 30 runs × 4 difficulty levels across 3+ days): not scheduled; E remains null.
- Layer C: interrupt lane active (T1–T6); routine review 365 days from `updated_at` 2026-10-31, pipeline-derived. Items to watch at the next sweep: a vendor statement on CVE-2026-12813; completion of SOC 2 Type 2 and publication of a report; a revision date and processing locations on the trust-center sub-processor list; a public DPA; any advisory for the 0.92.3-hotfix.2 API-crash fix.
