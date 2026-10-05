# VERDICT Evaluation Report #007
## Flowise

Evaluation type: Update
Evaluation date: 2026.09.25
Evaluator: VERDICT by ZinovaCreation
Target version: flowise 3.1.4 (npm, published 2026-07-29; dist-tag `latest` on 2026-09-25; final release before the repository was archived) — Flowise as distributed via npm `flowise` (server) and `flowise-components`, source github.com/FlowiseAI/Flowise. Flowise Cloud (cloud.flowiseai.com) is the operator's hosted surface; incident effects on it are recorded in the Contextual Analysis and as operator-side evidence under C / I, and are not scored as the target.
Framework: VERDICT v0.3.2
Previous evaluation: 2026-03-24 (Update, 33/85, Tier D, v0.3.1); initial Layer 0 2026-03-13 (37/85, Tier C)
Disclosure layer (Trigger 0/1/2/3): None. Trigger 1 does not fire (Workday, Inc. is not in the material Anthropic equity-holder set {Amazon, Google, Microsoft, NVIDIA}). Trigger 2 checked at the parent level per Trigger2-ParentLevel-001: Workday's public record shows index-fund holders (Vanguard, BlackRock, State Street) as its largest shareholders and no set member with a disclosed position of USD 100M or more, a board seat, or a lead / strategic designation. Trigger 3: Workday's cloud-provider and marketplace relationships with set members are standard supplier relations. Product level only: Flowise offers Claude (ChatAnthropic node) as one of many LLM providers; not a trigger.
Evaluator model: claude-fable-5-1

---

## Executive Summary

119 CVE records attributable to Flowise were first publicly disclosed in the trailing window (2025-09-25 → 2026-09-25), 30 of them at CVSS 9.0 or above on the recorded basis and the highest at 10.0 (CVE-2026-70478, NVD v3.1), while the operator published 118 repository security advisories in the same window, 105 of them under a Workday-affiliated maintainer account; eight further CVEs assigned in the window to advisories published before it are recorded as retroactive and not counted. The operator wound the product down inside the window: code freeze on 2026-07-29 (final release flowise 3.1.4), repository archived on 2026-08-13, end of life declared for 2026-08-31, and SECURITY.md replaced with a notice that new vulnerability reports are no longer accepted, while six advisories published on 2026-09-10 (two Critical, CVSS 4.0 9.2) and five VulnCheck CVEs published 2026-08-06 → 08-10 affect 3.1.4 with no patched version declared. The Layer 0 total moves from 33/85 (Tier D) to 31/85 (Tier D): R falls from 4 to 3 (count and severity criteria at the floor; patch record and structural-issue criteria now 0), T falls from 6 to 4 and I from 5 to 2 on re-application of the criteria to current documentation, while V (+2) and D (+2) rise on the corporate identity now confirmed in the Terms of Service and on the telemetry default. `independence` moves from unrecorded to subsidiary: FlowiseAI Inc. (Delaware) is owned by Workday, Inc. since the acquisition announced 2025-08-14, and the Terms of Service incorporate the Workday Online Terms of Service by reference.

---

## Scorecard

| Dimension | Score | Max | Rating |
|---|---|---|---|
| V Verifiability | 12 | 20 | Mid |
| E Effectiveness | N/A | 15 | Layer 1 pending |
| R Resilience | 3 | 20 | Low |
| D Data Conduct | 6 | 15 | Mid |
| I Identity & Control | 2 | 10 | Low |
| C Containment | 4 | 10 | Mid |
| T Transparency | 4 | 10 | Mid |
| **Total (Layer 0)** | **31** | **85** | |

Tier: D
Category: LLM Agent Builder · Low-Code Agent Platform · Open Source (Apache 2.0, archived 2026-08-13)

CISA KEV: None — the KEV JSON (catalog 2026.09.24, 1,723 entries) was checked on 2026-09-25 for all 145 CVE IDs in the Flowise advisory universe and for vendorProject / product / description matches on "Flowise", "FlowiseAI" and "Workday"; no entry. VulnCheck reported in-the-wild exploitation attempts against CVE-2025-59528 (10.0, CNA v3.1; published 2025-09-22, before the window) on 2026-04-07; the CVE is not KEV-listed.

---

## Differential

Previous evaluation: 2026-03-24, 33/85 (Tier D, v0.3.1). The series: 2026-03-13 initial 37 (Tier C) · 2026-03-24 update 33 (Tier D) · this update.

| Dimension | State | Reason |
|---|---|---|
| V | re-evaluated | T5 (ownership confirmed; archive / EOL 2026-08-13) + folded routine scope |
| R | re-evaluated | T1 ×n (118 repository advisories; 119 CVE records first disclosed in window) |
| D | re-evaluated | T5 re-opens D; prior record carries no `sources`, carry-forward conditions cannot be verified |
| I | re-evaluated | Prior record carries no `sources`; conditions 1–4 unverifiable |
| C | re-evaluated | Prior record carries no `sources`; sandbox-escape advisories touch the dimension (condition 4) |
| T | re-evaluated | Folded routine scope; SECURITY.md replaced 2026-08 (condition 3) |
| E | null | Layer 0 |

Carry-forward: none possible. The prior record is a migrated capture with `sources: []`, so no cited URL exists against which conditions 1–4 could be positively checked; all six dimensions are re-evaluated.

Rulings applied (2026-09-25, clarifications, no version change): Attribution-CVE-002 (clause 1: window by first public disclosure; clause 2: CVSS recording rule) and Criterion-VSource-001 (V source-code criterion). This version supersedes the first delivery of this update (same date), which counted by CVE publication date.

Enumeration method: (1) repository advisory listing, github.com/FlowiseAI/Flowise/security/advisories, `?page=1` … `?page=13` (10 per page; page 14 empty) — 130 advisories all-time, 118 published inside the window, every advisory page retrieved for CVE ID, CVSS, affected and patched versions; (2) GitHub Advisory Database web listing — `ecosystem:npm flowise` (5 pages, 121), `ecosystem:npm flowise-components` (43), `flowise` (172 incl. unreviewed), `type:unreviewed flowise` (51); (3) cvelistV5 JSON for every CVE ID surfaced (145); (4) NVD records via the fkie-cad/nvd-json-data-feeds mirror for the 134 CVEs published since 2025-03-24 (107 Analyzed, 10 Modified, 11 Deferred, 6 Awaiting Analysis). Not used: GitHub REST (unauthenticated rate limit exhausted on the shared egress address) and the OSV API (not reachable from the execution environment).

Window rule (Attribution-CVE-002 clause 1): first public disclosure = the earliest of the CVE record's `datePublished`, the publication date of any GHSA / vendor advisory linked to the CVE (by the CVE's references or the advisory's CVE field), and any public issue identifying it as a vulnerability. Issue, pull-request and gist references were inspected for all 127 CVE records published in the window. PR #4905 ("Chore/Safe Parse HTML", 2025-07-19; referenced by CVE-2025-29192 and CVE-2025-50538) and PR #5231 ("Chore/Disable Available Dep By Default", 2025-09-18; referenced by CVE-2025-34267) pre-date the window but do not identify a vulnerability, so the earliest vulnerability record for those three is the vendor advisory of 2025-10-03; the remaining issue, PR and gist references are dated 2026. Result: 127 CVE records published in the window − 8 retroactive = `cve_count_12mo: 119`, basis `exact`. For 105 of the 119 a vendor advisory precedes the CVE record; for 14 the CVE record is the first disclosure (11 of them have no vendor advisory at all). CNAs among the 119: GitHub 64, VulnCheck 47, VulDB 5, MITRE 3. Seven repository advisories inside the window carry no CVE ID on any source; they are listed in the Incident Timeline and considered under T, not counted (Attribution-CVE-001). Duplicate-advisory entries in the Advisory Database (GHSA-q4xx-mc3q-23x8, GHSA-7rgr-72hp-9wp3, GHSA-wq95-wr7m-26h4, GHSA-3g4j-r53p-22wx, GHSA-5w6g-rc45-wvv9, GHSA-w4hm-rrxg-pxcf) were de-duplicated against their CVE aliases.

Retroactive CVEs (published in the window, first disclosed before 2025-09-25; recorded, not counted): CVE-2024-58351 ← GHSA-5cph-wvm9-45gj 2024-11-21; CVE-2025-71333 ← GHSA-h42x-xx2q-6v6g 2025-03-13; CVE-2025-71338 ← GHSA-8vvx-qvq9-5948 2025-03-14; CVE-2025-71332 ← GHSA-9c4c-g95m-c8cp 2025-04-07; CVE-2025-57164 ← GHSA-7944-7c6r-55vv 2025-09-13; CVE-2025-71324 ← GHSA-99pg-hqvx-r4gf 2025-09-13; CVE-2025-71334 ← GHSA-q67q-549q-p849 2025-09-13; CVE-2025-71336 ← GHSA-6933-jpx5-q87q 2025-09-13. Seven are VulnCheck records published 2026-06-20 → 06-25; CVE-2025-57164 is a MITRE record published 2025-10-17.

CVSS recording rule (Attribution-CVE-002 clause 2): NVD v3.1 (Primary) where present — 79 of the 119; otherwise the CNA's v3.1 — 35. Where a stated score differs from the score computed from its own vector, the computed value is recorded with the stated value shown: CVE-2026-40933 (CNA stated 10.0 → computed 9.9). CVE-2025-61913 is recorded at NVD v3.1 9.9 on the same vector the CNA stated as 10.0. Five records carry neither an NVD nor a CNA v3.1 score; the ruling states no fallback for them, and this report applied, in order, CNA v3.0 (CVE-2026-30822 7.7, CVE-2026-30823 8.8), CISA-ADP v3.1 (CVE-2026-52098 9.8) and CNA v4.0 (CVE-2026-56267 6.9, CVE-2026-56276 6.0); none of the five sets the maximum or changes a band. NVD and CNA values differ by 0.5 or more on 13 counted records, in both directions (e.g. CVE-2026-41267 NVD 9.8 / CNA 8.1; CVE-2025-29192 NVD 6.1 / CNA 8.2); the NVD value is recorded.

`max_cvss_12mo`: 10.0 — CVE-2026-70478 (GHSA-qgvm-j2hm-6m38, unauthenticated OAuth2 token-refresh endpoint returning access tokens; first disclosed 2026-07-29; NVD v3.1 AV:N/AC:L/PR:N/UI:N/S:C/C:H/I:H/A:H = 10.0; CNA CVSS 4.0 9.2; fixed in 3.1.3). Next are seven records at 9.9 (CVE-2025-34267, CVE-2025-61913, CVE-2026-40933, CVE-2026-46442, CVE-2026-56274, CVE-2026-67622, CVE-2026-73602). 30 of the 119 are at 9.0 or above on the recorded basis. The first delivery's "three at 10.0" (CVE-2025-61913, CVE-2026-40933, CVE-2025-71338) is withdrawn: the first two are 9.9 under clause 2 and CVE-2025-71338 is retroactive (NVD v3.1 9.8).

CVE-2026-46440 (GHSA-php6-83fg-gw3g, checkBasicAuth; first disclosed 2026-05-14): recorded 9.1 — NVD v3.1 Primary, AV:N/AC:L/PR:N/UI:N/S:U/C:H/I:H/A:N. The CNA (GitHub) value is 7.5 on CVSS 3.0 (AV:N/AC:H/PR:N/UI:R/S:U/C:H/I:H/A:H), as shown on the vendor advisory. The first delivery's statement that 9.1 was unconfirmed is corrected.

Placement of the records named in the trigger table, by first public disclosure: CVE-2025-55346 and CVE-2025-8943 (2025-08-14), CVE-2025-58434 (2025-09-12), CVE-2025-59528, CVE-2025-59434 and CVE-2025-59527 (2025-09-22) — before the window; CVE-2025-57164 (GHSA-7944-7c6r-55vv) and CVE-2025-71324 (GHSA-99pg-hqvx-r4gf), both first disclosed 2025-09-13 — retroactive, not counted; CVE-2025-61913 (GHSA-jv9m-vf54-chjj / GHSA-j44m-5v8f-gc9c, 2025-10-08), CVE-2025-61687 (GHSA-35g6-rrw3-v6xc, 2025-10-06) and the 3.0.13 cluster (CVE-2026-30820 → 30824, 2026-03-05; CVE-2026-31829, 2026-03-09) — inside. GHSA-4fr9-3x69-36wv (XSS, 2025-10-03) received CVE-2025-71331 on 2026-06-20 and is counted at 2025-10-03.

Prior-record findings (stated as facts):
- Count: the prior record's `cve_count_12mo: 12` with basis `lower_bound` is consistent, as a lower bound, with the actual count for its window (2025-03-24 → 2026-03-24): 19 CVE records existed on 2026-03-24 for vulnerabilities first disclosed in that window (the same 19 under Attribution-CVE-002; none had an earlier first disclosure). Its `max_cvss_12mo: 9.8` sits below CVE-2025-61913 (9.9, NVD v3.1) and CVE-2025-59528 (10.0, CNA v3.1), both first disclosed in that window.
- Key finding (a separate error): the prior `key_finding` ("March 2026 cluster: 6 CVEs patched in v3.0.13, including CVE-2025-55346 and CVE-2025-58434 (both CVSS 9.8)") places two records in the 3.0.13 cluster that do not belong to it: CVE-2025-55346 (JFrog CNA, published 2025-08-14, affects ≤ 2.2.7-patch.1; GHSA-hmgh-466j-fx4c with no patched version declared) and CVE-2025-58434 (GitHub CNA, published 2025-09-12, fixed in 3.0.6). The six CVEs fixed in 3.0.13 are CVE-2026-30820, -30821, -30822, -30823, -30824 and CVE-2026-31829.
- `operator: Acquired by Workday (Aug 2025)` is a status phrase, not a legal entity; the entity is FlowiseAI Inc. (Delaware, EIN 37-2097367) and the parent Workday, Inc.
- `homepage`, `github`, `target_version`, `sources` and `tags` were empty; `evaluator_model` was `unrecorded`; `qa` was unresolved ×3. All are set in this update.

T5 findings:
- Ownership: Workday, Inc. announced on 2025-08-14 that it had acquired Flowise (Workday newsroom; terms not disclosed). The npm maintainers of `flowise` are Workday accounts (henryhengwday, jocelynlin-wd and eight others at workday.com). The Terms of Service at flowiseai.com/terms name FlowiseAI Inc., a Delaware corporation (EIN 37-2097367; mailing address 9450 SW Gemini Drive, Beaverton, Oregon 97008) and state that they "incorporate the Workday Online Terms of Service by reference"; the page still carries the effective date June 3, 2024. The site footer reads "© FlowiseAI Inc." → `operator: Workday (via FlowiseAI Inc.)`, `independence: subsidiary`, `parent_entity: Workday, Inc.`
- Archive and end of life: GitHub displays "This repository was archived by the owner on Aug 13, 2026. It is now read-only." Discussion #6727 "The Future of Flowise" (HenryHengZJ, maintainer, 2026-08-13 12:33 UTC) and flowiseai.com/sunset set the timeline: 2026-07-29 announcement and code freeze (no further pull requests reviewed), repository archival (the site page says August 10, the discussion and GitHub say August 13), 2026-08-31 end of life (core-team presence on Discord and GitHub concludes), npm packages and Docker images "will be marked deprecated". The Apache 2.0 code remains and forking is encouraged. SECURITY.md on the archived tree now states that new vulnerability reports are no longer accepted. As of 2026-09-25 no version of `flowise` on npm carries a deprecation flag. No successor repository was found; dblagbro/flow-wiser is a third-party community fork.
- Activity after the archive: security advisories continued to be published on the archived repository on 2026-08-28, 2026-08-31 and 2026-09-10 (igor-magun-wd), the last six with no patched version. VulnCheck and VulDB CVE records against 3.1.4 continued through 2026-09-15.
- Dormancy: not frozen. The product's own release record shows flowise 3.1.4 on 2026-07-29; the 12-consecutive-month test would first be met on 2027-07-29. `dormant_since` is not authored; the record stays in the routine lane, where the 2027-07-29 date is the dormancy check point.
- Flowise Cloud: cloud.flowiseai.com refuses automated retrieval; the homepage still links "Get Started" to cloud.flowiseai.com/signin and the sunset statement does not mention the hosted service. Its status is `[UNVERIFIED]` (resolving source: the cloud.flowiseai.com sign-in page or a shutdown notice, checked in a browser).

KNOWN_FACTS.md entry candidate (staged; Engine ratifies separately):
- Entity: Flowise / FlowiseAI Inc. (Workday, Inc. subsidiary). Operator: FlowiseAI Inc., Delaware corporation, EIN 37-2097367, 9450 SW Gemini Drive, Beaverton, OR 97008 (ToS); acquired by Workday, Inc. (announced 2025-08-14). Status: product wound down — code freeze 2026-07-29, repository archived 2026-08-13, EOL 2026-08-31, last release flowise 3.1.4 (2026-07-29); SECURITY.md no longer accepts vulnerability reports. Do NOT state: "actively maintained"; "6 CVEs in a March 2026 cluster including CVE-2025-55346 and CVE-2025-58434" (those two are not in the 3.0.13 cluster); "no CVEs" for any window ending 2025-10 or later; "three CVEs at 10.0" for the window ending 2026-09-25; "acquired by Workday" as the operator's legal name. Root cause: the #007 migrated capture (2026-03-24) carried a status phrase as `operator`, `independence: unrecorded`, and a key finding that merged the 3.0.13 cluster with two earlier 9.8 records.

Window used for R: 2025-09-25 → 2026-09-25, by first public disclosure (Attribution-CVE-002). `cve_count_basis: exact`.

---

## Dimension Detail

### V — Verifiability | 12/20

| Criterion | Result | Score | Evidence (source URL) |
|---|---|---|---|
| Developer / company identity | confirmed | 4 | FlowiseAI Inc., Delaware corporation, EIN 37-2097367, mailing address 9450 SW Gemini Drive, Beaverton, OR 97008; contacts support@flowiseai.com (ToS), privacy@flowiseai.com (Privacy Policy), hello@flowiseai.com (site) — https://flowiseai.com/terms ; https://flowiseai.com/privacy . Parent: Workday, Inc., acquisition announced 2025-08-14 — https://newsroom.workday.com/2025-08-14-Workday-Acquires-Flowise,-Bringing-Powerful-AI-Agent-Builder-Capabilities-to-the-Workday-Platform ; npm maintainers at workday.com — https://registry.npmjs.org/flowise |
| Source code disclosure | partial | 2 | Criterion-VSource-001: 4 only when the product's full source, including any hosted service or management plane the operator sells, is published under an OSI license; an OSS core with a commercially licensed enterprise layer or a closed cloud scores 2 (precedent #060 Langfuse `ee/`). Flowise: repository core under Apache-2.0; `packages/server/src/enterprise` and files with an explicit notice (e.g. IdentityManager.ts) under the FlowiseAI Inc Commercial License (source visible, production use requires a subscription) — https://github.com/FlowiseAI/Flowise/blob/main/LICENSE.md ; https://github.com/FlowiseAI/Flowise/blob/main/packages/server/src/enterprise/LICENSE.md |
| Version management transparency | confirmed | 3 | GitHub Releases with per-version notes through flowise@3.1.4; npm publish dates 3.0.8 2025-10-08 → 3.1.4 2026-07-29 — https://github.com/FlowiseAI/Flowise/releases ; https://registry.npmjs.org/flowise |
| Third-party dependency disclosure | partial | 1 | Privacy Policy names Stripe, PostHog, Google Analytics and "hosting providers" in prose; no dated sub-processor list — https://flowiseai.com/privacy |
| Independent certification | not confirmed | 0 | No SOC 2 / SOC 3 / ISO 27001 report or trust center found on flowiseai.com (home, pricing, sunset), docs.flowiseai.com (index) or the repository. `[UNVERIFIED]` if a trust-center URL exists for Flowise Cloud; resolving source: the URL. |
| Functional reproducibility docs | confirmed | 2 | API Reference (13 endpoint groups), CLI Reference, SDK and embed documentation — https://docs.flowiseai.com/api-reference.md ; https://docs.flowiseai.com/llms.txt |

Positive findings: legal entity, EIN and parent confirmed on the operator's own pages and the parent's newsroom; release notes for every version; Apache-2.0 core, with the commercially licensed enterprise directory also source-visible.
Recorded concerns: enterprise directory under a commercial license inside an archived repository; no independent certification found; sub-processors named only in prose.

### R — Resilience | 3/20

| Criterion | Result | Score | Evidence (source URL) |
|---|---|---|---|
| CVE count (trailing 12 months) | confirmed | 0 | 119 CVE records first publicly disclosed 2025-09-25 → 2026-09-25 (Attribution-CVE-002; 8 retroactive CVEs excluded). Band 10+: 0; −1 penalty for 9.0+ applied, floor 0. Enumeration in the Differential — https://github.com/FlowiseAI/Flowise/security/advisories ; https://github.com/advisories?query=ecosystem%3Anpm+flowise ; https://github.com/CVEProject/cvelistV5 |
| Maximum CVSS severity | confirmed | 0 | 10.0 — CVE-2026-70478 (NVD v3.1; unauthenticated OAuth2 token refresh returning access tokens; fixed in 3.1.3). Seven further records at 9.9 (incl. CVE-2025-61913, NVD v3.1; CVE-2026-40933, CNA stated 10.0, computed 9.9); 30 records at 9.0+ on the recorded basis (Attribution-CVE-002 clause 2) — https://github.com/fkie-cad/nvd-json-data-feeds/blob/main/CVE-2026/CVE-2026-704xx/CVE-2026-70478.json ; https://github.com/FlowiseAI/Flowise/security/advisories/GHSA-qgvm-j2hm-6m38 ; https://github.com/FlowiseAI/Flowise/security/advisories/GHSA-c9gw-hvqq-f33r |
| Patch response speed | confirmed | 0 | Unpatched at window end: six advisories of 2026-09-10 (GHSA-vf3j-89vf-r697 and GHSA-cffm-583c-vffr Critical 9.2) list "Patched versions: None" against ≤ 3.1.4; CVE-2026-67620, -67621, -67622, -70636, -71962 (VulnCheck, 2026-08-06 → 08-10) affect "through 3.1.4" with no fix; 46–50 days elapsed by 2026-09-25 with no release after 3.1.4. Report-to-fix where the reporter dates the report: elttam disclosed GHSA-wg86-r78f-74mp on 2026-04-11, fixed in 3.1.3 on 2026-06-25 (75 days; the advisory records that the original report was first closed as a vm2 version issue) — https://github.com/FlowiseAI/Flowise/security/advisories/GHSA-wg86-r78f-74mp ; https://github.com/FlowiseAI/Flowise/security/advisories/GHSA-vf3j-89vf-r697 ; https://registry.npmjs.org/flowise |
| Structural issues | confirmed | 0 | Same root causes recur across independent endpoints and releases: mass-assignment / cross-workspace reassignment in 14 advisories across 3.1.0, 3.1.2 and 3.1.3 (DocumentStore, Chatflow, Tool, Variable, Assistant, Dataset, DatasetRow, CustomTemplate, Evaluation, Evaluator, Vector Store, PUT /user, /leads); code-execution sandbox escapes in 2025-10 (Puppeteer / Playwright, dynamic Function), 2026-04 (MCP adapters, CSV / Airtable agents), 2026-05 (node-custom-function NodeVM), 2026-07 (vm2 and NodeVM escapes, Pyodide validator bypasses, TypeORM, SQLite record manager) and 2026-08 (Custom MCP npx, cwd bypass, SQL Database Chain); explicit patch bypasses (CVE-2026-69263 "CVE-2025-8943 Patch Bypass", GHSA-qqvm-66q4-vf5c "Patch Enforcement Failure", GHSA-52fh-8v99-63c2 validator homoglyph bypass); SSRF-protection bypasses in five advisories — https://github.com/FlowiseAI/Flowise/security/advisories/GHSA-xc48-889x-5qmw ; https://github.com/FlowiseAI/Flowise/security/advisories/GHSA-7j65-65cr-6644 ; https://github.com/FlowiseAI/Flowise/security/advisories/GHSA-52fh-8v99-63c2 |
| Supply chain compromise (trailing 12 months) | not found | 3 | No compromise of the vendor's npm packages, Docker images, GitHub organization or build pipeline was found in the advisory set, the npm registry metadata, or web searches for `flowise npm supply chain`, `flowise package malware`, `flowise sdk compromised`, `flowise dependency compromise`. GHSA-jrcq-qjw5-xx5q (2026-08-31, CVE-2026-91936) describes script-injection weaknesses in the Docker image build workflows; it is a vulnerability report, not a confirmed compromise — https://github.com/FlowiseAI/Flowise/security/advisories/GHSA-jrcq-qjw5-xx5q ; https://registry.npmjs.org/flowise |

Positive findings: the operator published 118 advisories in the window with CVSS vectors, affected / patched versions and reporter credits, and shipped seven fix releases (3.0.8, 3.0.10, 3.0.13, 3.1.0, 3.1.2, 3.1.3, 3.1.4); default security checks for Custom MCP, HTTP and path traversal are on; the elttam advisory records that the default JavaScript sandbox was changed to E2B.
Recorded concerns: 119 CVE records first disclosed in twelve months, 30 at 9.0+ and the highest at 10.0; issues affecting the final release with no patched version; the same vulnerability classes recurring release after release; no channel for new reports after 2026-08.

### D — Data Conduct | 6/15

| Criterion | Result | Score | Evidence (source URL) |
|---|---|---|---|
| GDPR compliance disclosure | partial | 1 | Privacy Policy §3 lists GDPR legal bases and §5 states SCCs for transfers; no DPA offered or referenced — https://flowiseai.com/privacy |
| Data minimization | confirmed | 3 | Self-hosted telemetry is off unless `POSTHOG_PUBLIC_API_KEY` is set (the `Telemetry` class instantiates no client otherwise); Privacy Policy §2.2: self-hosted usage "we do not collect any metrics nor data" — https://github.com/FlowiseAI/Flowise/blob/main/packages/server/src/utils/telemetry.ts ; https://github.com/FlowiseAI/Flowise/blob/main/packages/server/.env.example ; https://flowiseai.com/privacy |
| AI training use | not confirmed | 0 | No statement on model-training use of user content in the Privacy Policy or ToS (ToS §6 grants a license "solely to operate and improve the Services"; §7 reserves anonymized aggregated usage data) — https://flowiseai.com/terms |
| Sub-processor transparency | partial | 1 | Providers named in prose (Stripe, PostHog, Google Analytics, hosting providers), no dated list — https://flowiseai.com/privacy |
| Data retention disclosure | partial | 1 | "only as long as needed for the purposes outlined or as required by law"; anonymized data "may be retained indefinitely"; storage region US East 1 — https://flowiseai.com/privacy |

Positive findings: telemetry requires an explicit key; policy states no sale of data, SCCs for transfers, and a named privacy contact.
Recorded concerns: Privacy Policy and ToS dated June 3, 2024 with the Workday incorporation added without a new effective date; no DPA, no training-use statement, no per-category retention; the Spanish docs still carry a telemetry page describing anonymous collection.

### I — Identity & Control | 2/10

| Criterion | Result | Score | Evidence (source URL) |
|---|---|---|---|
| Emergency stop documentation | not confirmed | 0 | No documented procedure for stopping running flows / executions in the documentation reviewed (index, Environment Variables, Application auth, Human In The Loop tutorial). `[UNVERIFIED]` — resolving source: a docs page describing an abort / stop control for executions — https://docs.flowiseai.com/llms.txt |
| Human-in-the-loop design | partial | 1 | Optional: Human Input node pauses execution; "Require Human Input" toggle on agent tools; neither is enabled by default — https://docs.flowiseai.com/tutorials/human-in-the-loop.md |
| Permission delegation transparency | partial | 1 | RBAC, workspaces and SSO listed as security controls; API keys and JWT roles documented; the window's advisories record scope-enforcement gaps (cross-workspace IDOR, mass assignment, SSO invite-token bypass) that the documentation does not describe — https://docs.flowiseai.com/readme.md ; https://docs.flowiseai.com/configuration/authorization/app-level.md ; https://github.com/FlowiseAI/Flowise/security/advisories/GHSA-vf3j-89vf-r697 |

Positive findings: Human Input node and per-tool approval exist and are documented with a worked example; execution traces can be shared for external review.
Recorded concerns: no stop procedure documented; approval is opt-in; delegation scope documentation does not match the enforcement record.

### C — Containment | 4/10

| Criterion | Result | Score | Evidence (source URL) |
|---|---|---|---|
| Sandbox design | hybrid | 2 | Custom JavaScript runs in FlowiseAI/nodevm (vm2 fork) with allowlists for built-in / external modules (`TOOL_FUNCTION_BUILTIN_DEP`, `TOOL_FUNCTION_EXTERNAL_DEP`); Custom MCP uses a command allowlist; HTTP egress uses a built-in blocklist (`HTTP_SECURITY_CHECK`) plus `HTTP_DENY_LIST`; elttam records the default sandbox later moved to E2B — https://docs.flowiseai.com/configuration/environment-variables.md ; https://github.com/FlowiseAI/Flowise/security/advisories/GHSA-wg86-r78f-74mp |
| Least privilege | configurable | 1 | `CUSTOM_MCP_SECURITY_CHECK`, `HTTP_SECURITY_CHECK`, `PATH_TRAVERSAL_SAFETY` default true; JWT / session / token-hash secrets use documented defaults unless configured (docs warn of forged tokens); `ALLOW_BUILTIN_DEP` and `CORS_ORIGINS=*` available — https://docs.flowiseai.com/configuration/authorization/app-level.md ; https://docs.flowiseai.com/configuration/environment-variables.md |
| Tenant isolation (cloud) | claimed, unverified | 1 | Flowise Cloud is multi-tenant (workspaces, organizations); no isolation architecture published. Window advisories describe cross-tenant and cross-organization authorization gaps (GHSA-pprx-4prj-35mj, GHSA-7x8x-vv46-4579, GHSA-rpcc-gw54-mfgx) and CVE-2025-59434 (2025-09-22, before the window) "Multi-Tenant Variable Disclosure in Flowise Cloud"; no confirmed cross-tenant breach is on the public record — https://github.com/FlowiseAI/Flowise/security/advisories/GHSA-pprx-4prj-35mj ; https://github.com/FlowiseAI/Flowise/security/advisories/GHSA-435c-mg9p-fv22 |

Positive findings: allowlist-based module and command controls with security checks on by default; an E2B option for code execution; self-hosting with air-gapped deployment documented.
Recorded concerns: eleven sandbox-escape or code-injection advisories inside the window; defaults rely on operator configuration for secrets; cloud isolation undocumented.

### T — Transparency | 4/10

| Criterion | Result | Score | Evidence (source URL) |
|---|---|---|---|
| CVE publication posture | confirmed | 2 | 118 repository advisories in the window with CVSS vectors and credits; 64 CVEs issued through the GitHub CNA. Forward-looking: SECURITY.md now states new vulnerability reports are not accepted (not scored; recorded) — https://github.com/FlowiseAI/Flowise/security/advisories ; https://github.com/FlowiseAI/Flowise/blob/main/SECURITY.md |
| Incident disclosure speed | partial | 1 | Fix-to-advisory lag: 3.1.2 (2026-04-14) → advisories 2026-05-14 (30 days); 3.1.3 (2026-06-25) → 2026-07-27 / 29 (32–34 days); 3.1.4 (2026-07-29) → 2026-08-28 / 31 (30–33 days); 3.0.8 (2025-10-08) → same day. Report-to-advisory for the dated elttam report: 2026-04-11 → 2026-07-29 (109 days). No vendor statement was found on the 2026-04-07 exploitation report for CVE-2025-59528 — https://github.com/FlowiseAI/Flowise/security/advisories ; https://registry.npmjs.org/flowise |
| Security policy publication | partial | 1 | Technical security configuration documented (MCP checks, HTTP blocklist, path-traversal safety, secrets guidance); no organizational security page; SECURITY.md replaced by the sunset notice — https://docs.flowiseai.com/configuration/environment-variables.md |
| AI safety framework reference | not confirmed | 0 | No NIST AI RMF / ISO 42001 or internal AI-safety framework reference found on the site or docs |
| AI system identity disclosure | not confirmed | 0 | No AI-identity disclosure feature documented for the chat widget or API — https://docs.flowiseai.com/using-flowise/embed.md |

Positive findings: one of the largest vendor-published advisory sets in the index, with reporter credits and affected / patched versions on each record; sunset timeline published on the site, the repository and SECURITY.md.
Recorded concerns: monthly batching of advisories after fixes; the last six advisories with no fix; no organizational security policy; no report channel after EOL.

---

## Incident Timeline

CVE records attributable to Flowise whose first public disclosure falls inside the window (2025-09-25 → 2026-09-25), ordered by first-disclosure date (Attribution-CVE-002 clause 1). Date = first public disclosure; the disclosing advisory and the CVE publication date are shown where they differ. CVSS = recorded value under clause 2 with its basis. No entry is KEV-listed.

| Date | CVE ID | CVSS | Description | Patch status | CISA KEV |
|---|---|---|---|---|---|
| 2025-10-03 | CVE-2025-29192 | 6.1 (NVD v3.1) | Flowise before 3.0.5 allows XSS via a FORM element and an INPUT element  — GHSA-7r4h-vmj9-wg42; CVE pub 2025-10-06 | no patched version declared | No |
| 2025-10-03 | CVE-2025-34267 | 9.9 (NVD v3.1) | Flowise Authenticated Command Execution and Sandbox Bypass via Puppeteer — GHSA-5w3r-f6gm-c25w; CVE pub 2025-10-14 | see advisory | No |
| 2025-10-03 | CVE-2025-50538 | 6.1 (NVD v3.1) | Flowise before 3.0.5 allows XSS via an IFRAME element when an admin view — GHSA-7r4h-vmj9-wg42; CVE pub 2025-10-06 | no patched version declared | No |
| 2025-10-03 | CVE-2025-71331 | 6.1 (CNA v3.1) | Cross-Site Scripting in Chat Messages and Agent Workflows — GHSA-4fr9-3x69-36wv; CVE pub 2026-06-20 | patched 3.0.8 | No |
| 2025-10-06 | CVE-2025-61687 | 8.8 (NVD v3.1) | FlowiseAI/Flosise has File Upload vulnerability | patched 3.0.8 | No |
| 2025-10-08 | CVE-2025-61913 | 9.9 (NVD v3.1) | Flowise is vulnerable to arbitrary file read, arbitrary file write | patched 3.0.8 | No |
| 2025-11-12 | CVE-2025-71328 | 8.8 (NVD v3.1) | Unverified Password Change via Account Settings — GHSA-fjh6-8679-9pch; CVE pub 2026-06-25 | patched 3.0.10 | No |
| 2025-11-12 | CVE-2025-71335 | 8.1 (CNA v3.1) | Session Invalidation Failure After Password Change — GHSA-x7rp-qj2h-ghgw; CVE pub 2026-06-25 | patched 3.0.10 | No |
| 2025-11-12 | CVE-2025-71337 | 8.3 (CNA v3.1) | Unverified Email Change via Account Profile Endpoint — GHSA-x39m-3393-3qp4; CVE pub 2026-06-23 | patched 3.0.10 | No |
| 2025-11-15 | CVE-2025-71327 | 9.1 (CNA v3.1) | Authentication Bypass via Unprotected Registration Endpoint — GHSA-v5w9-prxf-w882; CVE pub 2026-06-25 | no patched version declared | No |
| 2026-03-05 | CVE-2026-30820 | 8.8 (NVD v3.1) | Flowise Authorization Bypass via Spoofed x-request-from Header — GHSA-wvhq-wp8g-c7vq; CVE pub 2026-03-07 | patched 3.0.13 | No |
| 2026-03-05 | CVE-2026-30821 | 9.8 (NVD v3.1) | Arbitrary File Upload via MIME Spoofing — GHSA-j8g8-j7fc-43v6; CVE pub 2026-03-07 | patched 3.0.13 | No |
| 2026-03-05 | CVE-2026-30822 | 7.7 (CNA v3.0) | Mass Assignment in `/api/v1/leads` Endpoint — GHSA-mq4r-h2gh-qv7x; CVE pub 2026-03-07 | patched 3.0.13 | No |
| 2026-03-05 | CVE-2026-30823 | 8.8 (CNA v3.0) | IDOR leading to Account Takeover and Enterprise Feature Bypass via SSO C — GHSA-cwc3-p92j-g7qm; CVE pub 2026-03-07 | patched 3.0.13 | No |
| 2026-03-05 | CVE-2026-30824 | 9.8 (NVD v3.1) | Missing Authentication on NVIDIA NIM Endpoints — GHSA-5f53-522j-j454; CVE pub 2026-03-07 | patched 3.0.13 | No |
| 2026-03-05 | CVE-2026-56267 | 6.9 (CNA v4.0) | PII Disclosure via Unauthenticated Forgot Password Endpoint — GHSA-jc5m-wrp2-qq38; CVE pub 2026-06-20 | patched 3.0.13 | No |
| 2026-03-05 | CVE-2026-56272 | 4.1 (CNA v3.1) | Insufficient Password Salt Rounds in Bcrypt Hashing — GHSA-x2g5-fvc2-gqvp; CVE pub 2026-06-24 | patched 3.0.13 | No |
| 2026-03-09 | CVE-2026-31829 | 8.8 (NVD v3.1) | Flowise affected by Server-Side Request Forgery (SSRF) in HTTP Node Lead — GHSA-fvcw-9w9r-pxc7; CVE pub 2026-03-10 | patched 3.0.13 | No |
| 2026-04-15 | CVE-2026-40933 | 9.9 (CNA v3.1; stated 10.0, computed from vector) | Authenticated RCE Via MCP Adapters — GHSA-c9gw-hvqq-f33r; CVE pub 2026-04-21 | patched 3.1.0 | No |
| 2026-04-15 | CVE-2026-41137 | 8.8 (NVD v3.1) | Code Injection in CSVAgent leads to Authenticated RCE — GHSA-9wc7-mj3f-74xv; CVE pub 2026-04-23 | patched 3.1.0 | No |
| 2026-04-15 | CVE-2026-41138 | 8.8 (NVD v3.1) | Remote code execution vulnerability in AirtableAgent.ts caused by lack o — GHSA-f228-chmx-v6j6; CVE pub 2026-04-23 | patched 3.1.0 | No |
| 2026-04-15 | CVE-2026-41264 | 9.8 (NVD v3.1) | CSV Agent Prompt Injection Remote Code Execution Vulnerability — GHSA-3hjv-c53m-58jj; CVE pub 2026-04-23 | patched 3.1.0 | No |
| 2026-04-15 | CVE-2026-41265 | 9.8 (NVD v3.1) | Airtable_Agent Code Injection Remote Code Execution Vulnerability — GHSA-v38x-c887-992f; CVE pub 2026-04-23 | patched 3.1.0 | No |
| 2026-04-15 | CVE-2026-41266 | 7.5 (NVD v3.1) | Sensitive Data Leak in public-chatbotConfig — GHSA-4jpm-cgx2-8h37; CVE pub 2026-04-23 | patched 3.1.0 | No |
| 2026-04-15 | CVE-2026-41267 | 9.8 (NVD v3.1) | Improper Mass Assignment in Account Registration Enables Unauthorized Or — GHSA-48m6-ch88-55mj; CVE pub 2026-04-23 | patched 3.1.0 | No |
| 2026-04-15 | CVE-2026-41268 | 9.8 (NVD v3.1) | Flowise Parameter Override Bypass Remote Command Execution — GHSA-cvrr-qhgw-2mm6; CVE pub 2026-04-23 | patched 3.1.0 | No |
| 2026-04-15 | CVE-2026-41269 | 8.8 (NVD v3.1) | File Upload Validation Bypass in createAttachment — GHSA-rh7v-6w34-w2rr; CVE pub 2026-04-23 | patched 3.1.0 | No |
| 2026-04-15 | CVE-2026-41270 | 8.3 (NVD v3.1) | SSRF Protection Bypass via Unprotected Built-in HTTP Modules in Custom F — GHSA-xhmj-rg95-44hv; CVE pub 2026-04-23 | patched 3.1.0 | No |
| 2026-04-15 | CVE-2026-41271 | 8.3 (NVD v3.1) | APIChain Prompt Injection SSRF in GET/POST API Chains — GHSA-6r77-hqx7-7vw8; CVE pub 2026-04-23 | patched 3.1.0 | No |
| 2026-04-15 | CVE-2026-41272 | 7.1 (CNA v3.1) | SSRF Protection Bypass (TOCTOU & Default Insecure) — GHSA-2x8m-83vc-6wv4; CVE pub 2026-04-23 | patched 3.1.0 | No |
| 2026-04-15 | CVE-2026-41273 | 8.2 (NVD v3.1) | Unauthenticated OAuth 2.0 Access Token Disclosure via Public Chatflow — GHSA-6f7g-v4pp-r667; CVE pub 2026-04-23 | patched 3.1.0 | No |
| 2026-04-15 | CVE-2026-41274 | 9.8 (NVD v3.1) | Cypher Injection in GraphCypherQAChain — GHSA-28g4-38q8-3cwc; CVE pub 2026-04-23 | patched 3.1.0 | No |
| 2026-04-15 | CVE-2026-41275 | 7.5 (NVD v3.1) | Password Reset Link Sent Over Unsecured HTTP — GHSA-x5w6-38gp-mrqh; CVE pub 2026-04-23 | patched 3.1.0 | No |
| 2026-04-15 | CVE-2026-41276 | 9.8 (NVD v3.1) | AccountService resetPassword Authentication Bypass Vulnerability — GHSA-f6hc-c5jr-878p; CVE pub 2026-04-23 | patched 3.1.0 | No |
| 2026-04-15 | CVE-2026-41277 | 8.8 (NVD v3.1) | Mass Assignment in DocumentStore Create Endpoint Leads to Cross-Workspac — GHSA-3prp-9gf7-4rxx; CVE pub 2026-04-23 | patched 3.1.0 | No |
| 2026-04-15 | CVE-2026-41278 | 7.5 (NVD v3.1) | Public chatflow endpoints return unsanitized flowData including plaintex — GHSA-w47f-j8rh-wx87; CVE pub 2026-04-23 | patched 3.1.0 | No |
| 2026-04-15 | CVE-2026-41279 | 7.5 (NVD v3.1) | Unauthenticated TTS endpoint accepts arbitrary credential IDs — enables  — GHSA-5fw2-mwhh-9947; CVE pub 2026-04-23 | patched 3.1.0 | No |
| 2026-04-15 | CVE-2026-43995 | 9.8 (NVD v3.1) | SSRF Protection Bypass via Direct node-fetch / axios Usage (Patch Enforc — GHSA-qqvm-66q4-vf5c; CVE pub 2026-05-11 | patched 3.1.0 | No |
| 2026-04-15 | CVE-2026-56269 | 4.6 (CNA v3.1) | Weak Default Token Hash Secret in JWT Token Encryption — GHSA-m7mq-85xj-9x33; CVE pub 2026-06-24 | patched 3.1.0 | No |
| 2026-04-15 | CVE-2026-56270 | 7.5 (CNA v3.1) | Unauthenticated OAuth Secrets Disclosure via /api/v1/loginmethod Endpoin — GHSA-6pcv-j4jx-m4vx; CVE pub 2026-06-24 | patched 3.1.0 | No |
| 2026-04-15 | CVE-2026-56271 | 9.8 (CNA v3.1) | Weak Default JWT Secrets in Authentication Middleware — GHSA-cc4f-hjpj-g9p8; CVE pub 2026-07-12 | patched 3.1.0 | No |
| 2026-04-15 | CVE-2026-56273 | 6.5 (CNA v3.1) | Path Traversal in Vector Store basePath Parameter — GHSA-w6v6-49gh-mc9w; CVE pub 2026-07-08 | patched 3.1.0 | No |
| 2026-04-15 | CVE-2026-56275 | 7.1 (NVD v3.1) | Server-Side Request Forgery via Execute Flow Base URL — GHSA-9hrv-gvrv-6gf2; CVE pub 2026-06-23 | patched 3.1.0 | No |
| 2026-04-15 | CVE-2026-56278 | 9.1 (CNA v3.1) | Session Hijacking via Weak Default Express Session Secret — GHSA-2qqc-p94c-hxwh; CVE pub 2026-06-30 | patched 3.1.0 | No |
| 2026-05-06 | CVE-2026-8026 | 5.3 (NVD v3.1) | FlowiseAI Flowise API Response account.service.ts login information disc | see advisory | No |
| 2026-05-06 | CVE-2026-8027 | 4.3 (CNA v3.1) | FlowiseAI Flowise User Controller authorization | see advisory | No |
| 2026-05-06 | CVE-2026-8028 | 3.7 (CNA v3.1) | FlowiseAI Flowise Endpoint account.service.ts verify information disclos | see advisory | No |
| 2026-05-14 | CVE-2026-42861 | 9.6 (NVD v3.1) | Mass Assignment in Variable Update Endpoint Allows Cross-Workspace Resou — GHSA-6fw7-3q8r-m5vj; CVE pub 2026-06-08 | patched 3.1.2 | No |
| 2026-05-14 | CVE-2026-42862 | 5.0 (NVD v3.1) | Mass Assignment in Tool Update Endpoint Allows Cross-Workspace Resource  — GHSA-x5v6-pj28-cwwm; CVE pub 2026-06-08 | patched 3.1.2 | No |
| 2026-05-14 | CVE-2026-42863 | 8.1 (NVD v3.1) | Mass Assignment in Chatflow Update Endpoint Allows Cross-Workspace Agent — GHSA-5wxp-qjgq-fx6m; CVE pub 2026-06-08 | patched 3.1.2 | No |
| 2026-05-14 | CVE-2026-46440 | 9.1 (NVD v3.1) | Basic Auth Credentials Exposed via API — GHSA-php6-83fg-gw3g; CVE pub 2026-06-08 | patched 3.1.2 | No |
| 2026-05-14 | CVE-2026-46441 | 9.6 (NVD v3.1) | Mass Assignment in Assistant Update Endpoint Allows Cross-Workspace Reso — GHSA-hp26-q66v-q2w7; CVE pub 2026-06-08 | patched 3.1.2 | No |
| 2026-05-14 | CVE-2026-46442 | 9.9 (NVD v3.1) | Authenticated Host RCE via POST /api/v1/node-custom-function and NodeVM  — GHSA-9rvc-vf7m-pgm2; CVE pub 2026-06-08 | patched 3.1.2 | No |
| 2026-05-14 | CVE-2026-46443 | 6.5 (NVD v3.1) | Credential Data Leak — GHSA-7g73-99r4-m4mj; CVE pub 2026-06-08 | patched 3.1.2 | No |
| 2026-05-14 | CVE-2026-46444 | 8.8 (NVD v3.1) | Vector Store No Permission Checks — GHSA-hmg2-jjjx-jcp2; CVE pub 2026-06-08 | patched 3.1.2 | No |
| 2026-05-14 | CVE-2026-46475 | 8.8 (NVD v3.1) | Assistant create+update mass-assignment allows cross-workspace assistant — GHSA-78pr-c5x5-jggc; CVE pub 2026-06-08 | patched 3.1.2 | No |
| 2026-05-14 | CVE-2026-46476 | 8.8 (NVD v3.1) | CustomTemplate create+update mass-assignment allows cross-workspace temp — GHSA-728h-4mwj-f2p4; CVE pub 2026-06-08 | patched 3.1.2 | No |
| 2026-05-14 | CVE-2026-46477 | 8.8 (NVD v3.1) | Dataset create+update mass-assignment allows cross-workspace dataset tak — GHSA-5h9v-837x-m97r; CVE pub 2026-06-08 | patched 3.1.2 | No |
| 2026-05-14 | CVE-2026-46478 | 8.8 (NVD v3.1) | DatasetRow create+update mass-assignment allows cross-workspace row take — GHSA-7j65-65cr-6644; CVE pub 2026-06-08 | patched 3.1.2 | No |
| 2026-05-14 | CVE-2026-46479 | 8.8 (NVD v3.1) | Evaluation create+update mass-assignment allows cross-workspace evaluati — GHSA-mq53-pc65-wjc4; CVE pub 2026-06-08 | patched 3.1.2 | No |
| 2026-05-14 | CVE-2026-46480 | 8.8 (NVD v3.1) | Evaluator create+update mass-assignment allows cross-workspace evaluator — GHSA-wxrr-jp8m-qq7f; CVE pub 2026-06-08 | patched 3.1.2 | No |
| 2026-05-14 | CVE-2026-56268 | 7.7 (CNA v3.1) | Cross-Workspace Information Disclosure via chatflows/apikey Endpoint — GHSA-c2c9-mfw7-p8hw; CVE pub 2026-06-22 | patched 3.1.2 | No |
| 2026-05-14 | CVE-2026-56274 | 9.9 (CNA v3.1) | Remote Code Execution via MCP Security Bypass in validateCommandFlags an — GHSA-m99r-2hxc-cp3q; CVE pub 2026-06-23 | patched 3.1.2 | No |
| 2026-05-14 | CVE-2026-56276 | 6.0 (CNA v4.0) | Mass Assignment in PUT /api/v1/user Allows Password Hash Override — GHSA-59fh-9f3p-7m39; CVE pub 2026-06-20 | patched 3.1.2 | No |
| 2026-05-14 | CVE-2026-56277 | 6.5 (NVD v3.1) | Hardcoded CORS Wildcard in TTS Endpoint — GHSA-m837-xvxr-vqwg; CVE pub 2026-06-30 | patched 3.1.2 | No |
| 2026-06-21 | CVE-2026-12821 | 6.3 (CNA v3.1) | FlowiseAI Flowise S3 Document Loader S3.ts path traversal | patched 3.1.3 | No |
| 2026-06-28 | CVE-2026-58057 | 5.0 (CNA v3.1) | Custom MCP Environment Variable Denylist Bypass via Case Sensitivity | see advisory | No |
| 2026-07-27 | CVE-2026-73488 | 6.5 (NVD v3.1) | Flowise before 3.1.3 IDOR via customer-default-source endpoint — GHSA-2364-jh4q-m9vm; CVE pub 2026-08-13 | patched 3.1.3 | No |
| 2026-07-27 | CVE-2026-73603 | 5.3 (NVD v3.1) | Flowise before 3.1.4 Credential Abuse via Text-to-Speech — GHSA-8gj2-2cvc-6xx7; CVE pub 2026-08-13 | patched 3.1.4 | No |
| 2026-07-27 | CVE-2026-73604 | 6.5 (CNA v3.1) | Flowise before 3.1.3 Credential Exposure via API — GHSA-rwrp-9823-p2xq; CVE pub 2026-08-13 | patched 3.1.3 | No |
| 2026-07-29 | CVE-2026-69250 | 7.5 (NVD v3.1) | Unauthenticated OAuth2 Refresh Enables Non-Blind SSRF and Secret Exfiltr — GHSA-r745-8hwv-h473; CVE pub 2026-08-04 | patched 3.1.3 | No |
| 2026-07-29 | CVE-2026-69251 | 8.8 (NVD v3.1) | Flowise RCE via TypeORM DataSource — GHSA-g32j-mmxr-gfq5; CVE pub 2026-08-04 | patched 3.1.3 | No |
| 2026-07-29 | CVE-2026-69252 | 8.8 (NVD v3.1) | Missing authorization on `/api/v1/files` allows low-privileged API keys  — GHSA-wp74-f5hh-5f3r; CVE pub 2026-08-04 | patched 3.1.3 | No |
| 2026-07-29 | CVE-2026-69253 | 8.8 (NVD v3.1) | Flowise Sandbox Escape to RCE — GHSA-wg86-r78f-74mp; CVE pub 2026-08-04 | patched 3.1.3 | No |
| 2026-07-29 | CVE-2026-69254 | 8.8 (NVD v3.1) | RCE via NodeVM Sandbox Escape in executeJavaScriptCode() nodeVMOptions O — GHSA-3769-jgqc-cxm7; CVE pub 2026-08-04 | patched 3.1.3 | No |
| 2026-07-29 | CVE-2026-69255 | 8.8 (NVD v3.1) | CSV Agent Remote Code Execution via Pyodide Code Injection — Root Shell  — GHSA-vmv7-4m6c-3cg5; CVE pub 2026-08-04 | patched 3.1.3 | No |
| 2026-07-29 | CVE-2026-69256 | 8.8 (NVD v3.1) | Remote Code Execution Vulnerability in CSVAgent — GHSA-x6vm-w76m-8j7g; CVE pub 2026-08-04 | patched 3.1.3 | No |
| 2026-07-29 | CVE-2026-69257 | 8.6 (NVD v3.1) | SSRF Protection Bypass via IPv4-Mapped IPv6 Addresses — GHSA-c6xh-wv4j-ppv5; CVE pub 2026-08-04 | patched 3.1.3 | No |
| 2026-07-29 | CVE-2026-69258 | 9.1 (NVD v3.1) | Unauthenticated Property Injection into Flow Execution Context via Ungat — GHSA-6vh2-wg4h-4vwj; CVE pub 2026-08-04 | patched 3.1.3 | No |
| 2026-07-29 | CVE-2026-69259 | 8.8 (NVD v3.1) | Flowise RCE via SQLite Record Manager Node — GHSA-x3hf-7cj6-3r4m; CVE pub 2026-08-04 | patched 3.1.3 | No |
| 2026-07-29 | CVE-2026-69262 | 8.1 (NVD v3.1) | `DELETE /api/v1/chatflows/:id` does not validate resource type, allowing — GHSA-p5w8-m249-4r4v; CVE pub 2026-08-04 | patched 3.1.3 | No |
| 2026-07-29 | CVE-2026-69263 | 9.8 (NVD v3.1) | CVE-2025-8943 Patch Bypass: npm_config_yes bypasses MCP environment vari — GHSA-xc48-889x-5qmw; CVE pub 2026-08-04 | patched 3.1.3 | No |
| 2026-07-29 | CVE-2026-69264 | 9.8 (NVD v3.1) | RCE via CSVAgent csvFile data URI base64 segment is interpolated into Py — GHSA-4j8x-x6v7-w9rq; CVE pub 2026-08-04 | patched 3.1.3 | No |
| 2026-07-29 | CVE-2026-70470 | 9.8 (NVD v3.1) | Pyodide validator Unicode homoglyph bypass leads to RCE — GHSA-52fh-8v99-63c2; CVE pub 2026-08-04 | patched 3.1.3 | No |
| 2026-07-29 | CVE-2026-70471 | 6.5 (NVD v3.1) | RBAC Bypass Leading to Unauthorized Workspace Variables Disclosure — GHSA-8r8h-6vcc-xhrv; CVE pub 2026-08-04 | patched 3.1.3 | No |
| 2026-07-29 | CVE-2026-70472 | 8.8 (NVD v3.1) | Cross-workspace credential IDOR in openai-assistants-vector-store — GHSA-chm3-vqcf-52rx; CVE pub 2026-08-04 | patched 3.1.3 | No |
| 2026-07-29 | CVE-2026-70473 | 8.5 (NVD v3.1) | Information Disclosure in GET /api/v1/upsert-history returns the entire  — GHSA-fr6g-7cq8-fg82; CVE pub 2026-08-04 | patched 3.1.3 | No |
| 2026-07-29 | CVE-2026-70474 | 8.1 (NVD v3.1) | Cross-Workspace OAuth2 Credential Metadata Leak — GHSA-wch5-xp77-fxg4; CVE pub 2026-08-04 | patched 3.1.3 | No |
| 2026-07-29 | CVE-2026-70475 | 6.5 (NVD v3.1) | Missing Authorization on Execution Update Endpoint — GHSA-fm2f-4339-4p2f; CVE pub 2026-08-04 | patched 3.1.3 | No |
| 2026-07-29 | CVE-2026-70476 | 8.2 (NVD v3.1) | Broken Access Control in Stripe Subscription Endpoints Allows Cross-Tena — GHSA-gmmw-qg98-6j6p; CVE pub 2026-08-04 | patched 3.1.3 | No |
| 2026-07-29 | CVE-2026-70477 | 9.8 (NVD v3.1) | CSV Agent Prompt Injection Remote Code Execution Vulnerability — GHSA-5xvg-pmgg-3mxr; CVE pub 2026-08-04 | patched 3.1.3 | No |
| 2026-07-29 | CVE-2026-70478 | 10.0 (NVD v3.1) | Unauthenticated OAuth2 token refresh endpoint returns access tokens — en — GHSA-qgvm-j2hm-6m38; CVE pub 2026-08-04 | patched 3.1.3 | No |
| 2026-07-29 | CVE-2026-73483 | 8.8 (NVD v3.1) | Flowise before 3.1.3 Sandbox Escape via Puppeteer — GHSA-9gvv-qjj3-2p6g; CVE pub 2026-08-13 | patched 3.1.3 | No |
| 2026-07-29 | CVE-2026-73484 | 8.1 (NVD v3.1) | Flowise before 3.1.3 Sandbox Escape via Pandas Methods — GHSA-x58f-9m57-qc4m; CVE pub 2026-08-13 | patched 3.1.3 | No |
| 2026-07-29 | CVE-2026-73485 | 8.8 (NVD v3.1) | Flowise before 3.1.3 Remote Code Execution via Airtable Agent — GHSA-c5hr-rc98-xp3g; CVE pub 2026-08-13 | patched 3.1.3 | No |
| 2026-07-29 | CVE-2026-73486 | 8.8 (NVD v3.1) | Flowise before 3.1.3 Code Injection via CSV Agent customReadCSV — GHSA-4878-cqgq-j53v; CVE pub 2026-08-13 | patched 3.1.3 | No |
| 2026-07-29 | CVE-2026-73487 | 9.8 (NVD v3.1) | Flowise before 3.1.3 Prompt Injection RCE via CSV Agent — GHSA-w7x8-q2gp-5cgg; CVE pub 2026-08-13 | patched 3.1.3 | No |
| 2026-07-29 | CVE-2026-73601 | 8.8 (NVD v3.1) | Flowise before 3.1.3 Remote Code Execution via Custom MCP — GHSA-g98q-rm45-q9h8; CVE pub 2026-08-13 | patched 3.1.3 | No |
| 2026-07-29 | CVE-2026-73602 | 9.9 (NVD v3.1) | Flowise before 3.1.3 Sandbox Escape to RCE — GHSA-rqh4-rxw3-93rp; CVE pub 2026-08-13 | patched 3.1.3 | No |
| 2026-08-06 | CVE-2026-67621 | 7.6 (CNA v3.1) | Flowise 3.1.4 Missing Authorization on Document Store Mutation Endpoints | see advisory | No |
| 2026-08-06 | CVE-2026-67622 | 9.9 (CNA v3.1) | Flowise 3.1.4 IDOR in OpenAI Assistants Integration | see advisory | No |
| 2026-08-06 | CVE-2026-70636 | 7.5 (CNA v3.1) | Flowise 3.1.4 Authentication Bypass via OAuth2 Credential Refresh Endpoi | see advisory | No |
| 2026-08-08 | CVE-2026-67620 | 7.7 (CNA v3.1) | Flowise 3.1.4 SSRF via fetch-links Endpoint Incomplete Deny-List | see advisory | No |
| 2026-08-10 | CVE-2026-71962 | 7.5 (CNA v3.1) | Flowise 2.2.4 - 3.1.4 Missing Authorization via openai-assistants-file/d | see advisory | No |
| 2026-08-28 | CVE-2026-90533 | 6.5 (NVD v3.1) | Flowise before 3.1.4 Broken Access Control via organizationuser — GHSA-fhxm-xxcx-g6x3; CVE pub 2026-09-12 | patched 3.1.4 | No |
| 2026-08-28 | CVE-2026-90534 | 6.5 (NVD v3.1) | Flowise before 3.1.4 Cross-Workspace Credential IDOR via node-load-metho — GHSA-hqvm-7539-v83j; CVE pub 2026-09-12 | patched 3.1.4 | No |
| 2026-08-28 | CVE-2026-90535 | 7.5 (NVD v3.1) | Flowise before 3.1.4 Denial of Service via text-to-speech/abort — GHSA-xhxx-56g3-mx2r; CVE pub 2026-09-12 | patched 3.1.4 | No |
| 2026-08-31 | CVE-2026-91929 | 7.1 (CNA v3.1) | Flowise before 3.1.4 Cross-Tenant Authorization Bypass — GHSA-7x8x-vv46-4579; CVE pub 2026-09-15 | patched 3.1.4 | No |
| 2026-08-31 | CVE-2026-91930 | 7.5 (CNA v3.1) | Flowise before 3.1.4 Cross-Tenant Organization Admin Takeover — GHSA-pprx-4prj-35mj; CVE pub 2026-09-15 | patched 3.1.4 | No |
| 2026-08-31 | CVE-2026-91931 | 8.5 (CNA v3.1) | Flowise before 3.1.4 Remote Code Execution via Custom MCP npx — GHSA-vcwp-f9rq-3887; CVE pub 2026-09-15 | patched 3.1.4 | No |
| 2026-08-31 | CVE-2026-91932 | 8.5 (CNA v3.1) | Flowise before 3.1.4 Remote Code Execution via cwd Parameter — GHSA-x7x8-95gh-42xm; CVE pub 2026-09-15 | patched 3.1.4 | No |
| 2026-08-31 | CVE-2026-91933 | 7.1 (CNA v3.1) | Flowise before 3.1.4 Authorization Bypass via openai-realtime — GHSA-gggp-6qmf-xwwc; CVE pub 2026-09-15 | patched 3.1.4 | No |
| 2026-08-31 | CVE-2026-91934 | 8.8 (CNA v3.1) | Flowise before 3.1.4 Remote Code Execution via SQL Database Chain — GHSA-pwfj-wh95-7mwp; CVE pub 2026-09-15 | patched 3.1.4 | No |
| 2026-08-31 | CVE-2026-91935 | 8.3 (CNA v3.1) | Flowise before 3.1.4 SSRF and API Key Exfiltration via Chat Model Nodes — GHSA-hx55-h48h-7rw9; CVE pub 2026-09-15 | patched 3.1.4 | No |
| 2026-08-31 | CVE-2026-91936 | 6.8 (CNA v3.1) | Flowise before 3.1.4 Script Injection via Docker Workflows — GHSA-jrcq-qjw5-xx5q; CVE pub 2026-09-15 | patched 3.1.4 | No |
| 2026-08-31 | CVE-2026-91937 | 7.5 (CNA v3.1) | Flowise before 3.1.4 NoSQL Injection via sessionId — GHSA-wpvf-4vfx-rgxm; CVE pub 2026-09-15 | patched 3.1.4 | No |
| 2026-08-31 | CVE-2026-91938 | 7.1 (CNA v3.1) | Flowise before 3.1.4 Server-Side Request Forgery via document loaders — GHSA-9cvr-5wv9-2gxr; CVE pub 2026-09-15 | patched 3.1.4 | No |
| 2026-09-10 | CVE-2026-52098 | 9.8 (CISA-ADP v3.1) | An issue in Flowise 3.1.2 allows a remote attacker to execute arbitrary  | see advisory | No |
| 2026-09-13 | CVE-2026-90580 | 6.3 (CNA v3.1) | FlowiseAI Flowise Evaluations Endpoint index.ts axios.post server-side r | see advisory | No |

Retroactive CVEs — published inside the window for vulnerabilities first disclosed before 2025-09-25; recorded, not counted in `cve_count_12mo` or `max_cvss_12mo` (Date = CVE publication):

| Date | CVE ID | CVSS | Description | Patch status | CISA KEV |
|---|---|---|---|---|---|
| 2026-06-20 | CVE-2024-58351 | 9.8 (CNA v3.1) | retroactive CVE — first disclosed GHSA-5cph-wvm9-45gj 2024-11-21; Remote Code Execution via overrideConfig Parameter | patched >=2.1.4 | No |
| 2026-06-25 | CVE-2025-71333 | 9.8 (NVD v3.1) | retroactive CVE — first disclosed GHSA-h42x-xx2q-6v6g 2025-03-13; Arbitrary File Upload via Unauthenticated /api/v1/attachment | no patched version declared | No |
| 2026-06-25 | CVE-2025-71338 | 9.8 (NVD v3.1) | retroactive CVE — first disclosed GHSA-8vvx-qvq9-5948 2025-03-14; Flowise through 2.2.7 - Arbitrary File Write to Remote Code  | no patched version declared | No |
| 2026-06-24 | CVE-2025-71332 | 8.8 (NVD v3.1) | retroactive CVE — first disclosed GHSA-9c4c-g95m-c8cp 2025-04-07; SQL Injection in importChatflows API via chatflow.id Paramet | no patched version declared | No |
| 2025-10-17 | CVE-2025-57164 | 6.5 (CISA-ADP v3.1) | retroactive CVE — first disclosed GHSA-7944-7c6r-55vv 2025-09-13; Flowise through v3.0.4 is vulnerable to remote code executio | patched 3.0.6 | No |
| 2026-06-25 | CVE-2025-71324 | 7.5 (CNA v3.1) | retroactive CVE — first disclosed GHSA-99pg-hqvx-r4gf 2025-09-13; Arbitrary File Read via chatId Parameter | patched 3.0.6 | No |
| 2026-06-25 | CVE-2025-71334 | 9.8 (CNA v3.1) | retroactive CVE — first disclosed GHSA-q67q-549q-p849 2025-09-13; Arbitrary File Access via Missing Chat Flow ID Validation | patched 3.0.6 | No |
| 2026-06-25 | CVE-2025-71336 | 9.8 (CNA v3.1) | retroactive CVE — first disclosed GHSA-6933-jpx5-q87q 2025-09-13; Unsandboxed Remote Code Execution via Custom MCP | patched 3.0.6 | No |

Repository advisories inside the window with no CVE ID on any source (not counted; recorded per Attribution-CVE-001):

| Date | Advisory | Severity / CVSS | Description | Patch status | CISA KEV |
|---|---|---|---|---|---|
| 2026-08-31 | GHSA-vrr6-xgc3-j99r (no CVE) | High 7.6 (v4.0) | Multiple AI infrastructure issues: credential exposure, MCP bypass, sandbox (<= 3.1.3) | patched 3.1.4 | No |
| 2026-09-10 | GHSA-ppmg-4cx6-95hh (no CVE) | High 7.5 (v3.1) | Missing authorization on chat message routes for low-privileged API keys (<= 3.1.4) | no patched version declared | No |
| 2026-09-10 | GHSA-vf3j-89vf-r697 (no CVE) | Critical 9.2 (v4.0) | INVITED users auto-promoted via SSO email match, invite-token bypass (<= 3.1.4) | no patched version declared | No |
| 2026-09-10 | GHSA-cffm-583c-vffr (no CVE) | Critical 9.2 (v4.0) | Cross-IdP account takeover via email-only SSO matching (<= 3.1.4) | no patched version declared | No |
| 2026-09-10 | GHSA-rpcc-gw54-mfgx (no CVE) | High 8.7 (v4.0) | BullMQ dashboard /admin/queues auth-only, no RBAC; cross-tenant job payloads (<= 3.1.4) | no patched version declared | No |
| 2026-09-10 | GHSA-27w2-26m5-x82c (no CVE) | High 7.6 (v4.0) | Cross-workspace credential IDOR (<= 3.1.4) | no patched version declared | No |
| 2026-09-10 | GHSA-jvx3-mjpw-r4gh (no CVE) | High 7.7 (v4.0) | Missing authorization on upsert-history endpoints (<= 3.1.4) | no patched version declared | No |

Events outside the count but inside the window:
- 2026-04-07 — VulnCheck reported in-the-wild exploitation attempts against CVE-2025-59528 (10.0, CNA v3.1; Custom MCP configuration evaluated as JavaScript; affects ≤ 3.0.5, fixed in 3.0.6 on 2025-09-15), citing 12,000–15,000 publicly reachable Flowise instances (SecurityWeek, 2026-04-07). The CVE was published 2025-09-22 (before the window) and is not KEV-listed.
- 2026-07-29 — Code freeze; final release flowise 3.1.4. 2026-08-13 — Repository archived; "The Future of Flowise" published. 2026-08-31 — Declared end of life. 2026-09-10 — Six advisories published against ≤ 3.1.4 with no patched version.
- Dependency lineage: the JavaScript sandbox is FlowiseAI/nodevm, the operator's own fork of vm2; escapes in it are product-scoped (no `dependency:` marker applies). No third-party dependency CVE exploited against Flowise deployments was identified.

---

## Contextual Analysis

The window records two things at once: the most active vulnerability-disclosure year in the product's history and the product's wind-down. Between 2025-10 and 2026-09 the maintainers, first the original team and from March 2026 a Workday-affiliated account, published 118 advisories, most with reporter credits, CVSS vectors and a fixed version, and shipped fixes in seven releases. The count of 119 is taken by first public disclosure (Attribution-CVE-002). Two secondary effects remain visible in the record: VulnCheck and MITRE assigned CVE IDs inside the window to eight vendor advisories first published between 2024-11 and 2025-09, which this report lists as retroactive and does not count, and VulDB, VulnCheck and MITRE published eleven records with no vendor advisory at all, which are counted at their CVE dates. Severity also depends on the scorer: NVD's v3.1 assessments differ from the CNA's by 0.5 or more on thirteen counted records, in both directions, and the recorded maximum (10.0, CVE-2026-70478) is NVD's score for an issue the CNA scored 9.2 on CVSS 4.0.

The structural pattern the prior record described for March 2026 — authentication not enforced for critical functions — is one of four classes that recur across the window. The largest is object-level authorization: fourteen mass-assignment or cross-workspace reassignment advisories across 3.1.0, 3.1.2 and 3.1.3, followed by cross-tenant gaps in the enterprise organization, SSO and BullMQ surfaces in August and September 2026. The second is code execution through sandboxes: the nodevm / vm2 lineage, the Pyodide validator for CSV and Airtable agents, Custom MCP command handling and TypeORM / SQLite node configuration, each escaped in more than one release. The third is SSRF-protection bypass, and the fourth is default secrets. Two advisories name a prior fix by number as bypassed. The elttam advisory adds a process detail: the report was first closed on the understanding that it concerned an outdated vm2 version, and the fix landed 75 days after disclosure.

The end-of-life sequence changes what the R and T records mean going forward, and the report states this without predicting the vendor's behaviour. The code freeze of 2026-07-29 makes 3.1.4 the final version; the six advisories of 2026-09-10 and the five VulnCheck records against 3.1.4 therefore describe conditions with no vendor fix, and SECURITY.md states that new reports are not accepted. Under this framework the patch record of the window stands as published; a fork that ships fixes is a different target with its own record. The operator's own statement gives the reason it chose to give — a shift toward coding agents such as Claude Code — and this report records that statement as the operator's position. Workday's 2025-08-14 announcement had described "investing in its open-source foundation"; the archival twelve months later is recorded as a dated fact.

Mitigating factors on the record: the disclosure volume is itself a product of the vendor opening a public advisory channel and of two vulnerability-intelligence CNAs cataloguing the backlog; default security checks for MCP commands, HTTP egress and path traversal are on; the JavaScript sandbox default was moved to E2B; telemetry needs an explicit key; and the sunset gave a dated timeline with the Apache 2.0 code and forking path stated. The exploitation report for CVE-2025-59528 concerns a version fixed six months earlier; the exposure it describes is of unpatched internet-facing instances, which is recorded here as the reporter's observation.

Economic risk (P dimension): no hidden-charge or cost-runaway issue was found for the self-hosted target. Flowise Cloud pricing is published per plan with prediction and storage caps; the Cloud's post-EOL status is unverified (see Differential).

Dormancy test: not dormant — flowise 3.1.4 released 2026-07-29; the test would first be met on 2027-07-29 and is routed to the routine lane.

---

## VERDICT Record

### Summary
The data shows 119 CVE records first disclosed in twelve months, the highest at 10.0 (NVD v3.1), with recurring authorization and sandbox-escape classes, alongside a product wound down mid-window: final release 2026-07-29, repository archived 2026-08-13, end of life 2026-08-31, and eleven records against the final version with no fix. Layer 0 total: 31/85, Tier D (previous: 33/85, Tier D).

### Risk Factor Summary by Use Case

| Use case | Risk factors recorded | Key data points |
|---|---|---|
| Internal testing / non-sensitive workflows | Final release carries unpatched advisories; no report channel; code-execution nodes escape allowlist sandboxes | 11 records against 3.1.4 with no fix; SECURITY.md notice; C 2/4 sandbox |
| Workflows handling API keys / credentials | Credential IDOR / leak advisories across workspaces; SSRF paths that exfiltrate provider keys; default token secrets unless configured | GHSA-hx55-h48h-7rw9 (CVE-2026-91935, 8.3, CNA v3.1), GHSA-27w2-26m5-x82c, CVE-2026-46443; docs warning on default secrets |
| Cloud version (multi-tenant) | Cross-tenant / cross-organization authorization gaps in enterprise surfaces; Cloud status after EOL unverified; isolation architecture unpublished | GHSA-pprx-4prj-35mj, GHSA-7x8x-vv46-4579 (2026-08-31); `[UNVERIFIED]` cloud status |
| Medical / financial / legal data | No DPA, no training-use statement, no per-category retention, no independent certification found; operator wind-down | D 6/15; V certification 0/4; EOL 2026-08-31 |

### Reference Information
- Users on any version before 3.1.4 have advisories with declared fixes through 3.1.4; users on 3.1.4 have eleven records with no declared fix, and the operator's sunset page names forking as the continuation path.
- Operators may wish to review the documented security configuration (custom JWT / session / token-hash secrets, `CUSTOM_MCP_PROTOCOL=sse`, `HTTP_DENY_LIST`) since several window advisories concern defaults.
- Credential rotation for provider keys stored in a Flowise instance is a common industry practice after SSRF- and IDOR-class disclosures of the kind recorded in this window.

### Bias Disclosure
"This evaluation uses Claude (Anthropic) as its tooling. Anthropic operates in the AI agent market and may compete with some evaluated vendors. VERDICT discloses this relationship in every report and applies identical evaluation criteria to all platforms regardless of their relationship to Anthropic."

Disclosure layer: none of Triggers 0–3 fires. Workday, Inc., the parent entity, is not a material Anthropic equity-holder, and no member of the set {Amazon, Google, Microsoft, NVIDIA} appears on Workday's public record as a material investor, board member or non-arms-length channel partner. At product level only, Flowise supports Claude as one of many LLM providers, and the operator's sunset statement names Claude Code among the coding agents it cites as changing how developers build; neither is a disclosure trigger.

---

## Evaluation History

| Date | Type | Score | Tier | Framework |
|---|---|---|---|---|
| 2026-03-13 | Initial (Layer 0) | 37 | C | v0.3.1 |
| 2026-03-24 | Update | 33 | D | v0.3.1 |
| 2026-09-25 | Update | 31 | D | v0.3.2 |

---

## Future Evaluation Plan

| Phase | Content | Planned timing |
|---|---|---|
| Layer 1 | Behavioral testing on a self-hosted 3.1.4 install (30 runs × 4 levels, 3+ days) | Not scheduled (product at end of life) |
| Layer C — routine | Routine differential (R, T, V; D/I/C per carry-forward conditions); dormancy check point 2027-07-29 | 365 days from 2026-09-25 (provisional, ReviewCadence-002) |
| Layer C — interrupt | T1 / T2 sweep of CVE records against 3.1.4 and any KEV listing; T5 follow-up on Flowise Cloud status and npm deprecation | Continuous; next quarterly sweep |
