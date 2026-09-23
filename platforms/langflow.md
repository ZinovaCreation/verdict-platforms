---
name: Langflow
slug: langflow
operator: IBM (via DataStax)
independence: subsidiary
parent_entity: IBM
category: Visual AI Agent Builder · Open Source
homepage: https://www.langflow.org
github: https://github.com/langflow-ai/langflow
evaluation_number: 8
evaluation_type: update
evaluated_at: '2026-03-13'
updated_at: '2026-09-23'
evaluator_model: claude-fable-5-1
framework_version: v0.3.2
layer: '0'
target_version: langflow 1.12.3
previous_evaluation_date: '2026-03-24'
previous_score: 30
score: 29
max_score: 85
tier: D
verdict:
  v:
    score: 13
    rating: Mid
    note: 'IBM stewardship confirmed; MIT OSS; no sub-processor list or SOC report'
  e:
    score: null
    rating: null
    note: null
  r:
    score: 3
    rating: Low
    note: '158 CVEs; max CVSS 10.0; 6 KEV; recurring root causes; no supply-chain event'
  d:
    score: 1
    rating: Low
    note: 'Telemetry default on (opt-out); no GDPR/DPA, sub-processor or retention notice'
  i:
    score: 4
    rating: Mid
    note: 'Kill-switch env vars documented; no tool approval gate; RBAC is optional plugin'
  c:
    score: 3
    rating: Low
    note: 'In-process exec default; optional microVM; no tenant isolation; IDOR exploited'
  t:
    score: 5
    rating: Mid
    note: 'Advisories complete (GHSA/IBM PSIRT); mixed disclosure timing; no AI safety ref'
cisa_kev:
  present: true
  entries:
  - cve_id: CVE-2025-3248
    kev_added_date: '2025-05-05'
    fcec_deadline: '2025-05-26'
  - cve_id: CVE-2026-33017
    kev_added_date: '2026-03-25'
    fcec_deadline: '2026-04-08'
  - cve_id: CVE-2025-34291
    kev_added_date: '2026-05-21'
    fcec_deadline: '2026-06-04'
  - cve_id: CVE-2026-55255
    kev_added_date: '2026-07-07'
    fcec_deadline: '2026-07-10'
  - cve_id: CVE-2026-0770
    kev_added_date: '2026-07-21'
    fcec_deadline: '2026-07-24'
  - cve_id: CVE-2026-9198
    kev_added_date: '2026-08-04'
    fcec_deadline: '2026-08-07'
cve_count_12mo: 158
cve_count_basis: exact
max_cvss_12mo: 10.0
supply_chain_compromise_12mo: false
known_facts_applied: []
qa:
  factual: pass
  legal: pass
  quality: pass
  revision_cycles: 0
  flagged: false
differential:
  v: re-evaluated
  r: re-evaluated
  d: re-evaluated
  i: re-evaluated
  c: re-evaluated
  t: re-evaluated
  e: null
next_review_due: '2026-12-22'
tags:
- open-source
- mit
- visual-agent-builder
- low-code
- python
- ibm
- datastax
- mcp
- cisa-kev
- tier-d
rank: 67
sources:
- https://www.langflow.org
- https://docs.langflow.org/
- https://docs.langflow.org/security
- https://docs.langflow.org/authentication-overview
- https://docs.langflow.org/environment-variables
- https://docs.langflow.org/contributing-telemetry
- https://github.com/langflow-ai/langflow
- https://github.com/langflow-ai/langflow/blob/main/SECURITY.md
- https://github.com/langflow-ai/langflow/blob/main/LICENSE
- https://github.com/langflow-ai/langflow/security/advisories
- https://github.com/advisories?query=langflow
- https://github.com/CVEProject/cvelistV5
- https://pypi.org/project/langflow/
- https://osv.dev/list?q=langflow
- https://www.cisa.gov/news-events/alerts/2026/03/25/cisa-adds-one-known-exploited-vulnerability-catalog
- https://www.cisa.gov/news-events/alerts/2026/05/21/cisa-adds-two-known-exploited-vulnerabilities-catalog
- https://db.gcve.eu/vuln/cve-2025-3248
- https://www.sysdig.com/blog/understanding-langflow-cve-2026-55255-and-why-higher-cvss-vulnerabilities-arent-always-the-most-exploited
- https://www.sysdig.com/blog/cve-2026-33017-how-attackers-compromised-langflow-ai-pipelines-in-20-hours
- https://thehackernews.com/2026/07/cisa-adds-4-actively-exploited-adobe.html
- https://thehackernews.com/2026/05/cisa-adds-exploited-langflow-and-trend.html
- https://thehackernews.com/2026/08/cisa-flags-langflow-rce-tomcat-and-n.html
- https://thehackernews.com/2026/06/unpatched-langflow-flaw-cve-2026-5027.html
- https://www.securityweek.com/hackers-start-exploiting-critical-langflow-vulnerability/
- https://blog.kevintel.com/cve-2026-0770-exploited-in-the-wild-langflow-rce-added-to-cisa-kev/
- https://www.resecurity.com/blog/article/exploiting-langflows-validatecode-endpoint-for-remote-code-execution
- https://labs.cloudsecurityalliance.org/research/csa-research-note-langflow-cve-2026-5027-ai-platform-rce-202/
- https://labs.cloudsecurityalliance.org/research/csa-research-note-langflow-cve-2025-34291-ai-orchestration-r/
- https://cybercrime.club/posts/langflow-cve-2026-33017-incomplete-fix-unauthenticated-rce/
- https://www.incibe.es/en/incibe-cert/early-warning/vulnerabilities/cve-2026-10561
- https://www.ibm.com/support/pages/node/7278927
- https://www.techtimes.com/articles/319918/20260708/cisa-adds-first-ai-agent-platform-kev-sets-thursday-deadline-4-cves.htm
- https://newsroom.ibm.com/2025-02-25-ibm-to-acquire-datastax,-deepening-watsonx-capabilities-and-addressing-generative-ai-data-needs-for-the-enterprise
- https://iconnect007.com/article/145543/ibm-officially-closes-deal-acquiring-datastax/145540/ein
- https://community.ibm.com/community/user/blogs/datastax-pm-team-datastax-pm-team/2025/10/02/ibm-datastax
- https://docs.datastax.com/en/astra-db-serverless/release-notes.html
- https://phoenix.security/accelerating-supply-chain-attacks-npm-pypi-vsx-ai-enabled-2026/
- https://docs.litellm.ai/blog/security-update-march-2026
finding: '158 CVEs published against Langflow OSS in the trailing 12 months (43 at CVSS 9.0+, three at 10.0); six CISA KEV entries; independent telemetry records in-the-wild exploitation of at least eight vulnerabilities in 2026. Vendor documents in-process code execution and no tenant isolation; hardening controls are documented but opt-in. IBM operates disclosure and CVE assignment; hosted DataStax Langflow was removed 2026-04-09.'
meta_owner: IBM · via DataStax · langflow 1.12.3
meta_description: 'Independent security evaluation of Langflow (IBM). Score: 29/85. 158 CVEs in 12 months, six CISA KEV entries, cross-tenant IDOR exploited. Framework v0.3.2.'
og_description: 'Independent security evaluation of Langflow (IBM). Score: 29/85. 158 CVEs in 12 months, six CISA KEV entries. Framework v0.3.2.'
category_line: Visual AI Agent Builder · Open Source (MIT)
display_tags:
- text: CISA KEV ×6
  color: red
- text: 158 CVEs · 12 Months
  color: red
- text: No Tenant Isolation (documented)
  color: red
- text: IBM (via DataStax)
  color: dim
key_finding: '158 CVEs in 12 months, six CISA KEV entries, cross-tenant IDOR exploited in the wild. Vendor documents no tenant isolation; hardening is opt-in. Operator: IBM.'
card_owner: IBM (via DataStax)
card_category: Visual AI Agent Builder · Open Source (MIT)
card_tags:
- text: CISA KEV ×6
  color: red
- text: 158 CVEs · 12 Months
  color: red
- text: IBM (via DataStax)
  color: dim
score_basis: consistent
---

# Langflow

158 CVEs published against Langflow OSS in the trailing 12 months (43 at CVSS 9.0+, three at 10.0); six CISA KEV entries; independent telemetry records in-the-wild exploitation of at least eight vulnerabilities in 2026. Vendor documents in-process code execution and no tenant isolation; hardening controls are documented but opt-in. IBM operates disclosure and CVE assignment; hosted DataStax Langflow was removed 2026-04-09.

## Layer 0 Score: 29/85 (Tier D)

**V** 13/20 · **R** 3/20 · **D** 1/15 · **I** 4/10 · **C** 3/10 · **T** 5/10

## CISA KEV

Listed — six entries: CVE-2025-3248 (added 2025-05-05), CVE-2026-33017 (added 2026-03-25), CVE-2025-34291 (added 2026-05-21), CVE-2026-55255 (added 2026-07-07), CVE-2026-0770 (added 2026-07-21), CVE-2026-9198 (added 2026-08-04). Details in the Scorecard and Incident Timeline below.

## Bias Disclosure

This evaluation uses Claude (Anthropic) as its tooling. Anthropic operates in the AI agent market and may compete with some evaluated vendors. VERDICT discloses this relationship in every report and applies identical evaluation criteria to all platforms regardless of their relationship to Anthropic.

## Full Evaluation

# VERDICT Evaluation Report #008
## Langflow

Evaluation type: Update
Evaluation date: 2026.09.23
Evaluator: VERDICT by ZinovaCreation
Target version: langflow 1.12.3 (PyPI, released 2026-09-22) — Langflow OSS as distributed via PyPI `langflow` / github.com/langflow-ai/langflow. Langflow Desktop and IBM-hosted offerings are out of scope for scoring; Desktop-only CVEs are recorded in the Incident Timeline with the surface named and are NOT counted in `cve_count_12mo`.
Framework: VERDICT v0.3.2
Previous evaluation: 2026-03-24 (Update, 30/85, Tier D, v0.3.1) — original Layer 0: 2026-03-13 (33/85)
Disclosure layer (Trigger 0/1/2/3): None. IBM is not in the material Anthropic equity-holder set {Amazon, Google, Microsoft, NVIDIA}; no IBM–Anthropic material relationship is recorded in KNOWN_FACTS.md.
Evaluator model: claude-fable-5-1

---

## Executive Summary

Between 2025-09-23 and 2026-09-23, 158 CVEs were published against Langflow OSS (CVE List V5, product-scoped; 8 further CVEs affect Langflow Desktop only), 43 of them at CVSS 9.0 or higher, with three scored 10.0 (CVE-2026-33309, CVE-2026-10561, CVE-2026-10134). Five of those CVEs were added to the CISA KEV catalog inside the window (CVE-2026-33017, CVE-2025-34291, CVE-2026-55255, CVE-2026-0770, CVE-2026-9198), joining CVE-2025-3248 (added 2025-05-05), and independent telemetry from Sysdig, VulnCheck, KEVIntel and CrowdSec records in-the-wild exploitation of at least eight distinct Langflow vulnerabilities in 2026. The Layer 0 total moves from 30/85 to 29/85 (Tier D unchanged): V rises from the prior card value on verified ownership, MIT licensing and documentation evidence, while R, D, C and T fall on the CVE record, the absence of GDPR/sub-processor/retention disclosures for the OSS product, and the documented absence of tenant isolation. The publicly documented security model — in-process Python execution, no isolation between users, infrastructure-level responsibility placed on the deployer — is stated plainly by the vendor, and an optional QEMU microVM sandbox plus a set of hardening flags are now documented.

---

## Scorecard

| Dimension | Score | Max | Rating |
|---|---|---|---|
| V Verifiability | 13 | 20 | Mid |
| E Effectiveness | N/A | 15 | Layer 1 pending |
| R Resilience | 3 | 20 | Low |
| D Data Conduct | 1 | 15 | Low |
| I Identity & Control | 4 | 10 | Mid |
| C Containment | 3 | 10 | Low |
| T Transparency | 5 | 10 | Mid |
| **Total (Layer 0)** | **29** | **85** | |

Tier: D
Category: Visual AI Agent Builder · Open Source (MIT) · Operator: IBM (via DataStax)

CISA KEV: ✅ 6 entries
- CVE-2025-3248 (added 2025.05.05, FCEB due 2025.05.26) — older than the trailing-12-month window; retained per KEV protocol. 28 days from publication (2025.04.07) to KEV. KEV ransomware-use field: Unknown. Source: KEV mirror https://db.gcve.eu/vuln/cve-2025-3248
- CVE-2026-33017 (added 2026.03.25, FCEB due 2026.04.08) — 8 days from advisory (2026.03.17) to KEV
- CVE-2025-34291 (added 2026.05.21, FCEB due 2026.06.04) — 167 days from publication (2025.12.05) to KEV
- CVE-2026-55255 (added 2026.07.07, FCEB due 2026.07.10) — 18 days from advisory (2026.06.19) to KEV
- CVE-2026-0770 (added 2026.07.21, FCEB due 2026.07.24) — 179 days from publication (2026.01.23) to KEV
- CVE-2026-9198 (added 2026.08.04, FCEB due 2026.08.07) — 18 days from publication (2026.07.17) to KEV; KEV vendorProject "IBM", product Langflow; ID↔description mapping confirmed (auto_login → validate/code chain, IBM bulletin node 7278927)

---

## Differential

Previous evaluation: 2026-03-24, 30/85 (Tier D, v0.3.1). Original Layer 0: 2026-03-13, 33/85.

| Dimension | State | Reason |
|---|---|---|
| V | re-evaluated | Routine scope |
| R | re-evaluated | Routine scope + T2 ×4 folded (33017 confirmed on KEV via CISA alert 2026-03-25) |
| D | re-evaluated | Prior record carries no `sources`; carry-forward conditions 1–4 cannot be checked |
| I | re-evaluated | Same |
| C | re-evaluated | Same |
| T | re-evaluated | Routine scope |
| E | null | Layer 0 |

Carry-forward checks performed: none possible. The prior record (`platforms/langflow.md` @ 1143559) is a migrated capture with `sources: []`, so no URL could be re-resolved or date-compared.

Prior-record omissions found (stated as facts):
- CVE-2025-34291 (published 2025-12-05, CVSS 3.1 8.8 NVD / 4.0 9.4 CNA) fell inside the prior record's trailing window but is absent from its front matter.
- CVE-2026-33017 was cited as KEV in the prior body text but not carried in `cisa_kev.entries`; KEV addition (2026-03-25) post-dates the prior update by one day.
- `cve_count_12mo: null (conflicting)` in the prior record is superseded by an exact count of 158 (window 2025-09-23 → 2026-09-23).
- `target_version`, `evaluator_model`, `independence` were unrecorded; all are set in this update.
- The prior record's display tag "IBM Acquired · Aug 2025" is not supported by retrieved sources (intent announced 2025-02-25; closing announced by DataStax 2025-05-28; IBM states completion on 2025-11-01). The tag is superseded by this record's `display_tags`; a KNOWN_FACTS.md entry for Langflow/DataStax/IBM ownership dates is proposed (Engine scope).

Source Divergence resolution: the prior record's two dimension sets (live card V5/R4/D4/I5/C4/T6 = 28; Notion v2 V8/R8/D3/I5/C2/T4 = 30) are superseded by this Scorecard. Neither prior set is adopted as "correct"; both are retained in repository history.

Window used for R: 2025-09-23 → 2026-09-23. `cve_count_basis: exact` (enumerated from CVEProject/cvelistV5, cross-checked against the GitHub Advisory Database, OSV and NVD mirrors).

---

## Dimension Detail

### V — Verifiability | 13/20

| Criterion | Result | Score | Evidence |
|---|---|---|---|
| Developer / company identity | confirmed | 4 | Operator stewardship by IBM confirmed on retrieval: SECURITY.md routes reports to https://hackerone.com/ibm; IBM is the CNA for 118 of 158 window CVEs (product string "IBM Langflow OSS") with IBM PSIRT bulletins (e.g. https://www.ibm.com/support/pages/node/7278927); KEV vendorProject "IBM" (CVE-2026-9198). Ownership chain Logspace → DataStax → IBM: intent to acquire announced 2025-02-25 (https://newsroom.ibm.com/2025-02-25-ibm-to-acquire-datastax,-deepening-watsonx-capabilities-and-addressing-generative-ai-data-needs-for-the-enterprise); DataStax announced the closing on 2025-05-28 (https://iconnect007.com/article/145543/ibm-officially-closes-deal-acquiring-datastax/145540/ein); IBM's DataStax PM team states the acquisition "will be completed on November 1" [2025], with DataStax offerings moving to IBM paper and Langflow support rebranded as IBM Elite Support (https://community.ibm.com/community/user/blogs/datastax-pm-team-datastax-pm-team/2025/10/02/ibm-datastax). IBM corporate registration is public record (SEC registrant). |
| Source code disclosure | confirmed | 4 | MIT License — https://github.com/langflow-ai/langflow/blob/main/LICENSE |
| Version management transparency | confirmed | 3 | Tagged GitHub Releases with notes (referenced by advisories, e.g. https://github.com/langflow-ai/langflow/releases/tag/1.7.1); versioned docs 1.8.x–1.13.x; Changelog page linked from https://www.langflow.org; 463 PyPI releases, latest 1.12.3 on 2026-09-22 (https://pypi.org/project/langflow/) |
| Third-party dependency disclosure | not confirmed | 0 | No sub-processor list published for the OSS product or its telemetry endpoint. |
| Independent certification | not confirmed | 0 | No SOC 2 / SOC 3 report published for Langflow OSS. |
| Functional reproducibility docs | confirmed | 2 | API reference (https://docs.langflow.org/api-reference-api-examples), components reference (https://docs.langflow.org/concepts-components), CLI reference; FastAPI-served OpenAPI. |

Positive findings: Full OSS under MIT; frequent tagged releases (daily dev builds, ~weekly patch releases in Sept 2026); operator identity and vulnerability-intake path (HackerOne/IBM) are unambiguous.
Recorded concerns: No sub-processor list, DPA or SOC report for the OSS product.

### R — Resilience | 3/20

| Criterion | Result | Score | Evidence |
|---|---|---|---|
| CVE count (trailing 12 months) | 158 (OSS) | 0 | Window 2025-09-23 → 2026-09-23. Enumerated 2026-09-23 (~05:00 UTC) from CVEProject/cvelistV5 @ 80247b1f62424a8110c2fdd447910e4b8f69de31 (commit 2026-09-23T04:00:17Z); latest in-window record published 2026-09-14; no records dated 2026-09-15 → 09-23 existed at that commit. 10+ → 0; −1 penalty for CVSS ≥ 9.0 (min 0). CVE List V5 enumeration: IBM CNA 118, GitHub CNA 22, VulDB 8, ZDI 5, Tenable 4, VulnCheck 1. Monthly: Dec-25 3, Jan 6, Feb 1, Mar 12, Apr 6, May 5, Jun 24, Jul 26, Aug 34, Sep (to 14th) 41. Severity: 43 ≥9.0, 72 at 7.0–8.9, 43 at 4.0–6.9, 0 below 4.0. |
| Maximum CVSS severity | 10.0 | 0 | CVE-2026-10561 (CVSS:3.1/AV:N/AC:L/PR:N/UI:N/S:C/C:H/I:H/A:H, NVD 10.0 — https://www.incibe.es/en/incibe-cert/early-warning/vulnerabilities/cve-2026-10561), CVE-2026-10134 (10.0), CVE-2026-33309 (CNA 10.0 / GHSA 9.9). |
| Patch response speed | 31+ days (representative) | 0 | CVE-2026-0768/0769/0770/0771/0772: reported via ZDI July 2025, published as zero-days 2026-01-23 (https://www.securityweek.com/hackers-start-exploiting-critical-langflow-vulnerability/); 0770 remediated in release-1.10.1 (https://www.resecurity.com/blog/article/exploiting-langflows-validatecode-endpoint-for-remote-code-execution). CVE-2026-5027: Tenable reports three contact attempts Jan–Feb 2026, disclosure 2026-03-27, fix in 1.9.0 (https://thehackernews.com/2026/06/unpatched-langflow-flaw-cve-2026-5027.html). Counter-example: CVE-2026-33017 advisory 2026-03-17, version 1.8.2 reported as incomplete by JFrog, complete fix 1.9.0 by 2026-04-03 (https://cybercrime.club/posts/langflow-cve-2026-33017-incomplete-fix-unauthenticated-rce/). SECURITY.md states fixes ship in the next minor or an on-demand patch. |
| Structural issues | same root cause recurring | 0 | exec()/eval() on user code in validate/code and component paths: CVE-2025-3248 → 2026-0770 → 2026-8481 → 2026-9198 → 2026-17632 → 2026-78571 (unguarded eval); public flow build endpoint: 2026-33017 → 2026-10560 → 2026-13448 → 2026-48519 → 2026-85025; files API path traversal: 2025-68478 → 2026-33309 (described by the CNA as a bypass of the 68478 patch) → 2026-5027 → 2026-8859 → 2026-12942 → 2026-18899 → 2026-19303; auto_login superuser token: 2025-57760 → 2026-9103 → 2026-9198 → 2026-8182; missing ownership checks: 2026-21445, 34046, 33760, 55255, 7787, 19294, 81268. |
| Supply chain compromise (trailing 12 months) | no record | 3 | STEP 3a queries run (langflow PyPI supply chain / package malware / sdk compromised). No compromised `langflow` PyPI release, maintainer account or build pipeline was reported in the window. Recorded but not a compromise: (a) CVE-2026-33475 (CVSS 9.1) — unauthenticated shell injection in the repository's GitHub Actions workflows, a CI vulnerability; (b) the "TrapDoor" campaign opened pull requests against langflow-ai/langflow to distribute poisoned AI-assistant configuration files — an attempted vector, with no report of a merged change (https://phoenix.security/accelerating-supply-chain-attacks-npm-pypi-vsx-ai-enabled-2026/). The March 2026 litellm 1.82.7/1.82.8 compromise (https://docs.litellm.ai/blog/security-update-march-2026) is a third-party package event and is not attributed to Langflow. |

Positive findings: Every CVE in the window carries a public advisory (GHSA and/or IBM PSIRT bulletin) with fixed versions; the September 2026 IBM batch (18 CVEs on 2026-09-10) was published with fixes in 1.11.6/1.12.x; release cadence is high (1.12.1–1.12.3 in 15 days).
Recorded concerns: 158 CVEs, 43 critical; six KEV entries; four documented incomplete-fix or patch-bypass chains; ZDI zero-day publications after a 6-month vendor window; researcher-reported unanswered contact attempts.

### D — Data Conduct | 1/15

| Criterion | Result | Score | Evidence |
|---|---|---|---|
| GDPR compliance disclosure | not confirmed | 0 | No GDPR statement or DPA in the Langflow OSS documentation or telemetry page (https://docs.langflow.org/contributing-telemetry). langflow.org exposes a "Manage Privacy Choices" control only; docs.datastax.com links the general IBM Privacy Statement (https://www.ibm.com/privacy), which is not referenced from the OSS docs and names no controller for OSS telemetry. |
| Data minimization | default ON, easy opt-out | 1 | Anonymous product telemetry is on by default; opt-out via `DO_NOT_TRACK=True` documented (https://docs.langflow.org/environment-variables#telemetry). Free-text, password, file, auth and MCP fields are never sent; Desktop registration e-mail is sent unless DO_NOT_TRACK is set. |
| AI training use | no mention | 0 | Telemetry page states data is "used solely for improving Langflow"; no explicit statement on model-training use; no retention period. |
| Sub-processor transparency | none | 0 | Not published. |
| Data retention disclosure | none (vendor-held data) | 0 | No retention statement for telemetry. Product-level retention controls exist for self-hosted data (`LANGFLOW_MAX_TRANSACTIONS_TO_KEEP`, `LANGFLOW_PUBLIC_FLOW_EXPIRATION` 24 h default). |

Positive findings: Telemetry fields are enumerated per event with an explicit list of never-collected field types; OpenTelemetry export is off unless an endpoint is configured; self-hosting keeps flow data on the deployer's infrastructure.
Recorded concerns: No GDPR/DPA, sub-processor, training-use or retention disclosure for the OSS product's telemetry; telemetry on by default.

### I — Identity & Control | 4/10

| Criterion | Result | Score | Evidence |
|---|---|---|---|
| Emergency stop documentation | documented but incomplete | 2 | Documented runtime kill-switches: `LANGFLOW_ALLOW_CUSTOM_COMPONENTS=false` disables custom components and built-in code-execution components; `LANGFLOW_BLOCK_CODE_INTERPRETER_COMPONENTS`; `LANGFLOW_AGENTIC_EXPERIENCE=false` (https://docs.langflow.org/environment-variables). These require configuration/restart; no documented immediate-stop procedure for a running agent was retrieved. |
| Human-in-the-loop design | optional | 1 | Playground is an interactive test loop (https://docs.langflow.org/); flows run automatically once triggered via API/webhook; no approval-gate for agent tool calls is documented. |
| Permission delegation transparency | partial | 1 | Built-in JWT/API-key auth, external OIDC/SSO, optional RBAC plugin (https://docs.langflow.org/authentication-overview); `LANGFLOW_TWEAKS_POLICY`, `LANGFLOW_MCP_SERVER_ENV_ALLOWLIST` documented. Per-key scope and delegation targets for agents/tools not fully documented in the pages reviewed. |

Positive findings: Authentication paths and hardening flags are consolidated in one environment-variable reference; production preflight (`LANGFLOW_DEPLOYMENT_PROFILE=prod`) aborts boot on missing services.
Recorded concerns: Auto-login remains a documented configuration; CVE-2026-9198 and CVE-2026-9103 concern default `auto_login` behaviour issuing superuser tokens.

### C — Containment | 3/10

| Criterion | Result | Score | Evidence |
|---|---|---|---|
| Sandbox design | hybrid | 2 | Default `LANGFLOW_SANDBOX_BACKEND=none` (in-process execution). Optional QEMU microVM (`exec-sandbox`) with offline default and domain allow-list; static security scanner for custom component code is denylist-based (CVE-2026-78569 "incomplete denylist", CVE-2026-79742 "incomplete environment variable blocklist"). https://docs.langflow.org/environment-variables#langflow-sandbox |
| Least privilege | configurable | 1 | Defaults: custom components allowed, local file access unrestricted, tweaks `permissive`, deployment profile `dev`, MCP Docker hardening off; each has a documented restrictive setting. Public shared flows refuse custom components by default (`LANGFLOW_ALLOW_PUBLIC_CUSTOM_COMPONENTS=False`). |
| Tenant isolation | past cross-tenant breach confirmed | 0 | Vendor documentation: "Langflow neither enforces isolation between users within a single Langflow process … provides no isolation between tenants" (https://docs.langflow.org/security). Cross-tenant IDOR CVE-2026-55255 observed exploited in the wild on 2026-06-25 (https://www.sysdig.com/blog/understanding-langflow-cve-2026-55255-and-why-higher-cvss-vulnerabilities-arent-always-the-most-exploited); cross-tenant CVEs 2026-10140 (voice mode), 2026-13444 (Chroma), 2026-12763 (MCP cache). The operator's hosted offering, DataStax Langflow (Tech Preview), was deprecated on 2026-03-09 and removed from Astra on 2026-04-09 with all hosted data deleted; the vendor directs users to Langflow OSS (https://docs.datastax.com/en/astra-db-serverless/release-notes.html#datastax-langflow-removal). Scoring note: the "Self-hosted only: 3 (N/A)" rule is not applied because the OSS server is a multi-user product whose own documentation addresses multi-tenant and third-party deployments and states that no isolation is enforced; the cross-tenant IDOR was exploited on a self-hosted instance. |

Positive findings: The security model is stated explicitly rather than implied; the microVM sandbox, file-system tool base directory and per-flag hardening give deployers documented containment options.
Recorded concerns: Containment is opt-in; default deployment executes code in-process with broad permissions.

### T — Transparency | 5/10

| Criterion | Result | Score | Evidence |
|---|---|---|---|
| CVE publication posture | issues CVEs + advisories | 2 | 32 published repository advisories (https://github.com/langflow-ai/langflow/security/advisories); IBM CNA assignments with PSIRT bulletins. |
| Incident disclosure speed | mixed | 1 | GHSA published same day as fix for GitHub-flow reports (e.g. CVE-2026-33017, 2026-03-17); ZDI-reported issues published by ZDI as zero-days on 2026-01-23 after a July-2025 report; Tenable reported three unanswered contacts before 2026-03-27 disclosure. |
| Security policy publication | detailed | 2 | SECURITY.md (HackerOne intake, 7-business-day response target, release policy); Security page with threat model and deployer responsibilities; hardening guides (Block custom components, Restrict API tweaks, Component hardening for untrusted users). |
| AI safety framework reference | none | 0 | No NIST AI RMF / OWASP LLM reference found in the documentation reviewed. |
| AI system identity disclosure | none | 0 | No documented default disclosure that end users are interacting with an AI system in the chat widget/Playground. |

Positive findings: Advisory coverage is complete for the window; vendor documentation describes the code-execution nature of the product without qualification.
Recorded concerns: Disclosure timing is uneven across intake channels; no AI safety framework or AI-identity disclosure documented.

---

## Incident Timeline

KEV-listed and independently reported exploited CVEs (Langflow OSS):

| Date (published) | CVE ID | CVSS | Description | Patch status | CISA KEV |
|---|---|---|---|---|---|
| 2025.04.07 | CVE-2025-3248 | 9.8 | Unauthenticated code injection, /api/v1/validate/code (exec) — outside window | Fixed 1.3.0 | ✅ added 2025.05.05 |
| 2025.12.05 | CVE-2025-34291 | 8.8 (NVD) / 9.4 (v4) | CORS + SameSite=None refresh token → account takeover → RCE; exploitation observed from 2026.01.23 (CrowdSec); MuddyWater attribution reported | Fixed 1.7.0 | ✅ added 2026.05.21, due 2026.06.04 |
| 2026.01.02 | CVE-2026-21445 | 8.8 (v4) | Missing auth on monitor endpoints; reported exploited | Fixed 1.7.1 | — |
| 2026.01.23 | CVE-2026-0768 | 9.8 | Code injection in custom component validator (root); exploitation reported Sept 2026 (VulnCheck) | Fixed 1.10.1 branch | — |
| 2026.01.23 | CVE-2026-0769 | 9.8 | eval_custom_component_code injection; exploitation reported (VulnCheck) | Fixed 1.10.1 branch | — |
| 2026.01.23 | CVE-2026-0770 | 9.8 | exec_globals in validate endpoint, unauthenticated RCE; exploitation from 2026.06.27 (KEVIntel: 137 attempts/46 IPs by 07.21) | Fixed release-1.10.1 | ✅ added 2026.07.21, due 2026.07.24 |
| 2026.03.17 | CVE-2026-33017 | 9.3 (v4) | Unauthenticated RCE via /api/v1/build_public_tmp; exploited within ~20 h (Sysdig); 1.8.2 incomplete (JFrog) | Fixed 1.9.0 | ✅ added 2026.03.25, due 2026.04.08 |
| 2026.03.27 | CVE-2026-5027 | 8.8 | Path traversal in POST /api/v2/files → file write/RCE; exploitation confirmed (VulnCheck honeypots, June 2026) | Fixed 1.9.0 | — |
| 2026.06.19 | CVE-2026-55255 | 8.4 (NVD) / 9.9 (advisory) / 6.1 (as reported by THN) | IDOR on /api/v1/responses, cross-tenant flow execution; first exploitation 2026.06.25 (Sysdig) | Fixed 1.9.1 | ✅ added 2026.07.07, due 2026.07.10 |
| 2026.07.17 | CVE-2026-9198 | 9.8 | auto_login superuser token + validate/code exec chain; 650 attempts/244 IPs from 2026.07.06 (KEVIntel) | Fixed 1.10.1 | ✅ added 2026.08.04, due 2026.08.07 |

VulnCheck (Sept 2026) reports 11 Langflow vulnerabilities exploited in the wild in 2026 and >15,000 successful attacks against instances vulnerable to CVE-2026-0769, CVE-2025-3248 or CVE-2026-5027 (https://www.securityweek.com/hackers-start-exploiting-critical-langflow-vulnerability/). Coverage of the July 2026 KEV additions references a ransomware intrusion (JADEPUFFER) in which Langflow was the initial access point (https://www.techtimes.com/articles/319918/20260708/cisa-adds-first-ai-agent-platform-kev-sets-thursday-deadline-4-cves.htm).

Langflow Desktop only (surface: Desktop; not counted): CVE-2026-3357 (8.8, FAISS deserialization, 1.6.0–1.8.2), CVE-2026-3340 (6.5), CVE-2026-3341 (5.4), CVE-2026-3345 (6.5), CVE-2026-3346 (6.4), CVE-2026-4502 (6.5), CVE-2026-4503 (7.5), CVE-2026-6543 (8.8).

CVE-less advisory: GHSA-4hmc-cfm3-w43c (2026-09-22, authenticated cross-project file disclosure via MCP resource handlers) — recorded, not counted.

Appendix — all 158 in-window OSS CVEs (window 2025-09-23 → 2026-09-23; enumerated 2026-09-23 from CVE List V5 @ 80247b1; latest record 2026-09-14). CNA/NVD score; v4 where no v3.x:
- 2025-12: 34291 8.8/9.4v4 · 68477 7.7 · 68478 7.1
- 2026-01: 21445 8.8v4 · 0768 9.8 · 0769 9.8 · 0770 9.8 · 0771 7.1 · 0772 7.5
- 2026-02: 27966 9.8
- 2026-03: 33017 9.3v4 · 33053 6.1v4 · 33309 10.0 · 33475 9.1 (CI workflows) · 33484 7.5 · 33497 8.7v4 · 33873 9.3v4 · 34046 8.7v4 · 5022 6.3v4 · 5025 6.5 · 5026 7.0v4 · 5027 8.8
- 2026-04: 6542 6.5 · 6596 6.9v4 · 6597 5.1v4 · 6598 5.3v4 · 6599 5.3v4 · 6600 5.1v4
- 2026-05: 7524 9.8 · 7528 7.1 · 7687 5.3v4 · 7700 5.3v4 · 42048 9.6
- 2026-06: 7663 9.1 · 7664 9.8 · 7787 7.5 · 7803 9.8 · 7871 9.8 · 7873 9.9 · 7874 9.1 · 10129 8.5 · 10134 10.0 · 10140 9.6 · 10546 7.1 · 10560 8.2 · 10561 10.0 · 10564 8.2 · 12822 4.8v4 · 33760 8.8 · 42867 6.5 · 48519 9.6 · 48520 6.1 · 55255 8.4 · 55423 6.1 · 55446 7.5 · 55447 9.6 · 55450 9.3
- 2026-07: 7667 8.8 · 7754 7.7 · 7755 8.8 · 7872 7.5 · 8056 8.8 · 8476 9.9 · 8481 9.9 · 8505 9.8 · 8635 9.9 · 8859 9.9 · 9103 9.8 · 9135 9.9 · 9198 9.8 · 9202 9.8 · 10700 6.5 · 12940 9.8 · 12942 7.5 · 12945 7.1 · 12946 9.9 · 13435 9.9 · 13442 7.1 · 13444 8.1 · 13445 8.1 · 13446 9.8 · 13448 8.1 · 14499 8.8
- 2026-08: 7646 6.5 · 7657 6.5 · 7658 6.5 · 7869 5.4 · 8182 8.8 · 8183 7.7 · 8446 7.5 · 8470 7.4 · 8478 8.8 · 9077 8.5 · 9081 7.1 · 9130 7.1 · 9196 8.1 · 9201 8.8 · 9205 7.4 · 10128 6.5 · 10547 5.9 · 17623 8.8 · 17624 8.5 · 17625 7.2 · 17626 8.8 · 17630 7.2 · 17632 8.8 · 17633 8.5 · 18545 4.3 · 18729 8.8 · 18891 8.2 · 18899 7.5 · 18904 8.2 · 19286 9.8 · 19294 6.4 · 19295 9.9 · 19297 9.1 · 19875 7.5
- 2026-09 (latest record 09-14): 8447 6.1 · 9138 6.5 · 9186 6.5 · 9225 6.5 · 12763 4.2 · 12765 6.5 · 12766 5.4 · 12767 6.5 · 12944 9.6 · 14470 6.5 · 17621 5.4 · 17622 6.5 · 17627 4.9 · 17628 5.4 · 17631 5.0 · 19298 8.8 · 19299 6.5 · 19300 7.5 · 19301 5.0 · 19302 6.5 · 19303 8.1 · 19304 7.7 · 19305 8.6 · 19306 7.7 · 76059 8.8 · 78569 8.8 · 78571 8.8 · 78575 8.8 · 79723 5.0 · 79724 9.8 · 79725 6.5 · 79742 8.8 · 81204 9.8 · 81211 8.8 · 81213 8.6 · 81265 7.5 · 81268 8.1 · 81940 8.8 · 81941 8.8 · 84889 8.8 · 85025 9.8

---

## Contextual Analysis

The CVE volume reflects two overlapping processes rather than a single event. From April 2026, IBM's PSIRT began assigning CVEs in batches (24 on 2026-08-05, 17 on 2026-09-04, 18 on 2026-09-10), many for issues that would previously have been fixed silently; this raises the count while also raising the completeness of the public record. In parallel, external researchers (ZDI, Tenable, huntr contributors, Sysdig, Obsidian) reported a series of flaws that converge on one architectural fact the vendor states itself: Langflow is an IDE and code-execution platform in which developer-provided Python runs in the backend process with host, filesystem and network access.

The exploitation record follows the architecture. CVE-2025-3248 (validate/code) was patched by adding authentication; CVE-2026-33017 reached the same exec() through the unauthenticated public-flow endpoint; CVE-2026-9198 reached it again through the default auto_login token. Attackers observed by Sysdig and KEVIntel favoured the unauthenticated RCEs over the higher-scored IDOR, and used footholds for credential harvesting (LLM provider keys, cloud credentials, .env files) and loader delivery. The compressed disclosure-to-exploitation interval (about 20 hours for CVE-2026-33017, with no public PoC) is a property of the current threat environment as much as of Langflow.

On the vendor side, the trajectory within the window is toward explicit hardening: an optional QEMU microVM sandbox, `LANGFLOW_ALLOW_CUSTOM_COMPONENTS`, code-interpreter blocking, local-file restriction, MCP Docker hardening, a tweaks policy, production preflight, and public-flow refusal of custom components by default. The documentation places tenant isolation and authentication enforcement outside the container and says so directly. The recurrence of patch bypasses (CVE-2026-33309 on the 68478 fix, 1.8.2 for 33017) and the ZDI zero-day publications are recorded as elapsed-time facts; no motive is attributed.

Ownership: Langflow moved from Logspace to DataStax and then to IBM. IBM announced its intent to acquire DataStax on 2025-02-25, DataStax announced the closing on 2025-05-28, and IBM's DataStax product team stated the acquisition would be completed on 2025-11-01 with offerings moving to IBM paper and Langflow support rebranded as IBM Elite Support. IBM now operates the disclosure program (HackerOne), assigns CVEs and publishes bulletins, and Langflow is documented as a deployment source for watsonx Orchestrate. The hosted DataStax Langflow tech preview was deprecated on 2026-03-09 and removed on 2026-04-09; the OSS distribution is the operator's remaining Langflow surface alongside Langflow Desktop.

Dormancy test: not dormant — 1.12.3 released 2026-09-22, daily 1.13.0.dev builds through 2026-09-23.

---

## VERDICT Record

### Summary
The data shows 158 published CVEs (43 critical, three at CVSS 10.0) and six CISA KEV entries for a product whose vendor documents in-process code execution and no built-in tenant isolation, alongside a growing set of documented but opt-in hardening controls. Layer 0 total: 29/85, Tier D (previous: 30/85).

### Risk Factor Summary by Use Case

| Use case | Risk factors recorded | Key data points |
|---|---|---|
| Internal testing / non-sensitive workflows | In-process code execution by default; telemetry on by default | `LANGFLOW_SANDBOX_BACKEND=none` default; `DO_NOT_TRACK` opt-out |
| Workflows handling API keys / credentials | Credential exposure documented in exploitation reports; weak key-derivation CVEs | CVE-2026-7874 (9.1), CVE-2026-9205 (7.4); Sysdig/CSA credential-harvest reports |
| Cloud version (multi-tenant) | Vendor states no tenant isolation; cross-tenant IDOR exploited | https://docs.langflow.org/security; CVE-2026-55255 (KEV), CVE-2026-10140 |
| Medical / financial / legal data | No GDPR/DPA, sub-processor or retention disclosure for OSS; no SOC report | D 1/15, V certification 0/4 |

### Reference Information
- IBM's September 2026 bulletins list Langflow OSS through 1.11.5 as affected; users on earlier versions may wish to review their upgrade status against 1.12.3.
- The documentation describes `LANGFLOW_AUTO_LOGIN=false`, `LANGFLOW_ALLOW_CUSTOM_COMPONENTS=false` and the `exec-sandbox` backend as deployer-side controls.
- Credential rotation after exposure of an internet-reachable instance is a common industry practice.

### Bias Disclosure
"This evaluation uses Claude (Anthropic) as its tooling. Anthropic operates in the AI agent market and may compete with some evaluated vendors. VERDICT discloses this relationship in every report and applies identical evaluation criteria to all platforms regardless of their relationship to Anthropic."

---

## Evaluation History

| Date | Type | Score | Tier | Framework |
|---|---|---|---|---|
| 2026-03-13 | Initial (Layer 0) | 33 | D | v0.3.1 |
| 2026-03-24 | Update | 30 | D | v0.3.1 |
| 2026-09-23 | Update | 29 | D | v0.3.2 |

Provenance correction (2026-09-22): `evaluated_at` restored to the original Layer 0 date, 2026-03-13; the capture date 2026-03-24 stands as the first update (`updated_at`). Verdict, score and tier of that record unchanged (StrategyApproval-001 clause (c), approved 2026-09-22).

---

## Future Evaluation Plan

| Phase | Content | Planned timing |
|---|---|---|
| Layer 1 | Behavioral testing on a local OSS install (30 runs × 4 levels, 3+ days) | Not scheduled |
| Layer C — routine | Full routine differential (R, T, V; D/I/C per carry-forward conditions) | 365 days from 2026-09-23 (provisional, ReviewCadence-002) |
| Layer C — interrupt | T1/T2 sweep; KEV feed weekly | Continuous |
