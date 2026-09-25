# VERDICT Evaluation Report #064
## Guardrails AI

Evaluation type: Update
Evaluation date: 2026.09.25
Evaluator: VERDICT by ZinovaCreation
Target version: guardrails-ai 0.11.0 (PyPI, released 2026-08-14; GitHub Release v0.11.0 auto-cut on publish) — the Guardrails framework as distributed via PyPI `guardrails-ai` and github.com/guardrails-ai/guardrails. Guardrails Hub (catalog), Guardrails Pro and Snowglobe are the operator's other surfaces; incident effects on them are recorded in the Contextual Analysis and as operator-side evidence under C / I, and are not scored as the target.
Framework: VERDICT v0.3.2
Previous evaluation: 2026-05-12 (Initial, Layer 0, 40/85, Tier C, v0.3.1-final)
Disclosure layer (Trigger 0/1/2/3): Trigger 2 fires via the parent entity. Harvey announced its acquisition of Guardrails AI on 2026-09-09; GV (Alphabet / Google) led Harvey's $100M Series C on 2024-07-23 and participated in the Series D, and Google is a material Anthropic equity-holder under KNOWN_FACTS.md. Triggers 0, 1 and 3: none. See the Bias Disclosure for the disclosure paragraph.
Evaluator model: claude-fable-5-1

---

## Executive Summary

Two Critical CVEs were published against the `guardrails-ai` package inside the trailing window (2025-09-25 → 2026-09-25): CVE-2026-31233 (CVSS 3.1 9.8; code injection in the Hub installer's `post_install` path, versions through 0.6.7, no patched version declared, no vendor advisory) and CVE-2026-45758 (CVSS 3.1 9.6; a malicious `guardrails-ai==0.10.1` published to PyPI on 2026-05-11 at ~18:00 PT after an employee GitHub Personal Access Token was compromised, identified by third-party researchers within ~2 hours, vendor advisory on 2026-05-12, clean 0.10.2 published 2026-06-04 under PyPI Trusted Publishing). The Layer 0 total moves from 40/85 (Tier C) to 32/85 (Tier D): R falls from 17 to 6 on the CVE count, maximum severity, patch record and supply-chain compromise; V (+2), D (+1) and T (+1) rise on re-application of the criteria to current documentation, and I (−1) falls on the absence of a documented human-in-the-loop mode. Two structural events also fall in the window: the Guardrails Hub installer, private registry and hosted inference were retired on 2026-08-25 (announced 2026-07-06) in favour of public PyPI packages, and Harvey announced its acquisition of Guardrails AI on 2026-09-09, so `independence` moves from independent to subsidiary (Harvey AI Corporation). Two earlier CVEs (CVE-2024-6961, CVE-2024-45858) were re-published as PYSEC records on 2026-07-07 and remain out of window.

---

## Scorecard

| Dimension | Score | Max | Rating |
|---|---|---|---|
| V Verifiability | 13 | 20 | Mid |
| E Effectiveness | N/A | 15 | Layer 1 pending |
| R Resilience | 6 | 20 | Low |
| D Data Conduct | 2 | 15 | Low |
| I Identity & Control | 3 | 10 | Low |
| C Containment | 3 | 10 | Low |
| T Transparency | 5 | 10 | Mid |
| **Total (Layer 0)** | **32** | **85** | |

Tier: D
Category: AI Safety · LLM Guardrails · Validators · Open-Source Framework (Apache 2.0) · Operator: Harvey (via Guardrails AI, Inc.)

CISA KEV: None. Neither CVE-2026-31233 nor CVE-2026-45758 appears in the KEV catalog (OpenCVE KEV mirror for both IDs, 2026-09-25; CISA alert stream 2026-05 → 2026-09 contains no Guardrails entry). The CISA KEV JSON could not be retrieved inside this session (network restriction); Operations pre-flight: grep the JSON for the two CVE IDs and for vendorProject/product "Guardrails".

---

## Differential

Previous evaluation: 2026-05-12, 40/85 (Tier C, v0.3.1-final). This is the first update in the series.

| Dimension | State | Reason |
|---|---|---|
| V | re-evaluated | Folded routine scope + T5 (ownership change 2026-09-09) |
| R | re-evaluated | T3 + T1 (two Critical CVEs) + T4 (Socket / SafeDep independent reports); R-only change −11 ≥ 3 → full re-review rule |
| D | re-evaluated | Full re-review rule (R-only ≥ 3); T5 also re-opens D |
| I | re-evaluated | Full re-review rule; incident touches operator-side control surfaces (condition 4) |
| C | re-evaluated | Full re-review rule; incident and Hub retirement touch validator distribution (conditions 3, 4) |
| T | re-evaluated | T3 / T1 mandatory scope |
| E | null | Layer 0 |

Carry-forward checks performed (2026-09-25), recorded for the audit trail even though the full re-review rule governs:

| Dimension | URL | Resolves | Date vs 2026-05-12 | Window change touching the dimension |
|---|---|---|---|---|
| D | https://www.guardrailsai.com/legal/terms-of-use | yes (→ guardrailsai.com/legal/terms-of-use) | "Last Updated: August 14, 2025" — older | none in the document; T5 ownership change 2026-09-09 (condition 3) |
| D | https://guardrailsai.com/legal/privacy-policy | yes | "Effective as of May 1, 2025" — older | none in the document; forced API-key rotation 2026-05-13 recorded (condition 4, operator surfaces) |
| D / I / C | https://www.guardrailsai.com/docs | yes (→ guardrailsai.com/guardrails/docs) | 0.11 migration guide added (window) | Hub CLI / private registry / hosted inference retired (condition 3) — fails for I and C |
| I / C | https://github.com/guardrails-ai/guardrails | yes | pushes through 2026-09 | SECURITY_ADVISORY.md added 2026-05-12; incident (condition 4) — fails |
| C | https://hub.guardrailsai.com/ | yes (→ guardrailsai.com/hub, catalog of 65 validators) | catalog live | installer retired 2026-08-25 (condition 3) — fails |
| C | https://github.com/guardrails-ai/guardrails/blob/main/SECURITY_ADVISORY.md | yes | created 2026-05-12 | post-incident controls stated by the operator (see C) |

Result: D would have satisfied conditions 1–2 but not 3 (ownership change); I and C fail conditions 3 and 4. All six dimensions are re-evaluated under the full re-review rule regardless.

Prior-record omissions found (stated as facts):
- CVE-2026-31233 (CNA: MITRE; reserved 2026-03-09; published 2026-05-12; NVD published 2026-05-12T18:16Z; CVSS 3.1 9.8) fell inside the prior record's trailing window on its evaluation date. The prior record carries `cve_count_12mo: 0`, `max_cvss_12mo: null` and "0 CVEs · 12 Months" tags.
- The malicious `guardrails-ai==0.10.1` was published 2026-05-11 ~18:00 PT (2026-05-12 ~01:00 UTC) and the vendor advisory GHSA-xmpw-2vmm-p4p6 on 2026-05-12, the prior evaluation date. The prior record carries `supply_chain_compromise_12mo: false` and R 17/20. The CVE ID was reserved 2026-05-13 and published 2026-06-05, after the prior evaluation. Elapsed time from event to CVE publication: 24 days.
- The 2026-09-22 sweep dry run that drafted this update observed one Critical advisory; the window contains two Critical CVEs. The T5 event (2026-09-09) pre-dates the sweep and was not in the trigger table; both were detected during this update.
- The prior evaluation artifact (`evaluations/064_guardrails_ai.md`) states "ティア: B" in its Japanese summary while 40/85 falls in the C band; the canonical record and this update carry Tier C for 2026-05-12 (Tier override rule, QA.md).
- `target_version: null` and `evaluator_model: unrecorded` in the prior record are set in this update.

Window used for R: 2025-09-25 → 2026-09-25. `cve_count_basis: exact` (enumerated from OSV `guardrails-ai`, GitHub Advisory Database, cvelistV5 mirror and NVD mirror; aliases resolved so that each event is counted once).

---

## Dimension Detail

### V — Verifiability | 13/20

| Criterion | Result | Score | Evidence (source URL) |
|---|---|---|---|
| Developer / company identity | confirmed | 4 | Guardrails AI, Inc. (Delaware C-corp; California foreign-entity 5678079 confirmed in the 2026-05-12 evaluation via bizfileonline.sos.ca.gov). Official contacts: support@ and security@guardrailsai.com (ToU §11.10; advisory), admin@guardrailsai.com / +1 415-251-6780 (privacy policy §11). Acquisition by Harvey AI Corporation announced 2026-09-09 — https://www.harvey.ai/blog/guardrails-ai-joins-harvey ; counsel announcement https://www.lw.com/en/news/2026/09/Latham%20Advises%20Harvey%20on%20Acquisition%20of%20Guardrails ; https://www.abajournal.com/news/article/harvey-raises-550-million-in-latest-round-of-funding (citing Reuters). Terms not disclosed. |
| Source code disclosure | confirmed | 4 | Apache-2.0, full framework source — https://github.com/guardrails-ai/guardrails ; https://pypi.org/project/guardrails-ai/ |
| Version management transparency | confirmed | 3 | GitHub Releases with per-version notes through v0.11.0 (auto-cut on PyPI publish, PR #1586) — https://github.com/guardrails-ai/guardrails/releases ; https://github.com/guardrails-ai/guardrails/releases/tag/v0.11.0 ; migration guide https://guardrailsai.com/guardrails/docs/migration-guides/0-11-migration |
| Third-party dependency disclosure | not confirmed | 0 | No sub-processor list located. The privacy policy names PostHog and Google Analytics as providers but publishes no dated list — https://guardrailsai.com/legal/privacy-policy |
| Independent certification | not confirmed | 0 | No public SOC 2 / ISO 27001 / equivalent for Guardrails AI. Harvey's own attestations (https://www.harvey.ai/security) cover Harvey's platform, not the evaluated target. |
| Functional reproducibility docs | confirmed | 2 | API reference (Guard / AsyncGuard, OnFailAction types) and behavioral concept docs (validation loop, on-fail actions, error remediation) — https://guardrailsai.com/guardrails/docs/api_reference_markdown/guards ; https://guardrailsai.com/guardrails/docs/concepts/validator_on_fail_actions |

Positive findings: legal entity, contacts and founders remain verifiable; Apache-2.0 source and PyPI releases are fully auditable; from 0.10.2 (2026-06-04) every release carries a PyPI Trusted Publishing attestation signed by GitHub Actions and logged in Sigstore (https://pypi.org/project/guardrails-ai/0.10.2/ ; https://pypi.org/project/guardrails-ai/).
Recorded concerns: no sub-processor list, no independent certification, no Trust Center. The post-acquisition legal structure (merger vs. continuing subsidiary) is not publicly stated; the site footer still reads "Guardrails AI 2025" and PyPI ownership remains the "Guardrails AI" organization. Prior V 11/20; the prior record did not publish a criterion-level breakdown, so the +2 reflects fresh application of the criteria (release notes and reproducibility docs), not a documented change.

### R — Resilience | 6/20

| Criterion | Result | Score | Evidence (source URL) |
|---|---|---|---|
| CVE count (trailing 12 months) | 2 CVEs; CVSS 9.0+ present | 2 | 1–2 → 3, penalty −1 for CVSS 9.0+ → 2. CVE-2026-31233 — https://github.com/advisories/GHSA-r6hf-g5x6-7pv9 ; CVE-2026-45758 — https://github.com/advisories/GHSA-xmpw-2vmm-p4p6 ; https://osv.dev/list?q=guardrails-ai |
| Maximum CVSS severity | 9.8 (CVE-2026-31233); 9.6 (CVE-2026-45758) | 0 | CVSS:3.1/AV:N/AC:L/PR:N/UI:N/S:U/C:H/I:H/A:H (31233); CVSS:3.1/AV:N/AC:L/PR:N/UI:R/S:C/C:H/I:H/A:H (45758) — https://osv.dev/vulnerability/GHSA-r6hf-g5x6-7pv9 ; https://github.com/guardrails-ai/guardrails/security/advisories/GHSA-xmpw-2vmm-p4p6 |
| Patch response speed | not confirmed for all in-window CVEs | 0 | CVE-2026-45758: mitigation (pin 0.10.0 / install from tag) published 2026-05-12; clean successor 0.10.2 on 2026-06-04 = 23 days from the 2026-05-12 UTC event (15–30 d band → 1 if taken alone). CVE-2026-31233: GitHub Advisory Database records "Patched versions: None"; no vendor advisory or fix statement located as of 2026-09-25, 136 days after publication. Unconfirmed patch → 0 (Absolute Rule 3). |
| Structural issues | isolated (with class-level note) | 3 | Root causes on record: 2024 eval of RAIL XML (CWE-95, fixed 0.5.10) and RAIL XXE (CWE-611, fixed 0.5.0); 2026 Hub-manifest `post_install` execution (CWE-94, different component); 2026 compromised CI credential (CWE-506). No public evidence of a single design-level root cause recurring across these. A stricter reading (code-injection class recurring in two components) would score 0 and R 3/20; the alternative is recorded, not applied. |
| Supply chain compromise (trailing 12 months) | record exists; responded ≤7 d | 1 | Timeline: publication 2026-05-11 ~18:00 PT; identified by Socket within ~2 h and PyPI quarantine (issue #1473, 2026-05-12); GHSA + SECURITY_ADVISORY.md 2026-05-12; org-wide token rotation, employee account reset and device factory-reset stated 2026-05-12; Snowglobe / Hub API keys invalidated 2026-05-13 14:00 PT; clean 0.10.2 with Trusted Publishing 2026-06-04 — https://github.com/guardrails-ai/guardrails/blob/main/SECURITY_ADVISORY.md ; https://github.com/guardrails-ai/guardrails/issues/1473 ; https://safedep.io/mass-npm-supply-chain-attack-tanstack-mistral/ |

Positive findings: third-party detection within ~2 hours and registry quarantine the same night; the operator's advisory named the root cause (compromised employee PAT → GitHub Action across 30 organization repositories → deploy tokens extracted from artifacts → PyPI publish) within one day; the operator states restriction of classic PATs, approval and expiry for fine-grained PATs, mandatory verified commit signatures on all branches, and telemetry / log review with no evidence of data exfiltration; 0.10.2 and 0.11.0 carry PyPI attestations; GitHub Actions template-injection fixes landed in 0.10.2 and 0.11.0 (PRs #1467, #1537, #1585).
Recorded concerns: two Critical CVEs in the window; no vendor advisory or declared patched version for CVE-2026-31233 (the affected path — Hub installer `post_install` — was retired with the Hub installer on 2026-08-25, but no source states this as a fix); the SECURITY_ADVISORY.md header still reads "Last updated: May 12, 2026" although the changelog records later edits (PRs #1478, #1490, #1499), and the "more detailed postmortem in the coming days" announced there was not located. Prior R 17/20.

### D — Data Conduct | 2/15

| Criterion | Result | Score | Evidence (source URL) |
|---|---|---|---|
| GDPR compliance disclosure | mention only | 1 | ToU §2.3 requires a DPA before Personal Data is processed; no public DPA URL; the privacy policy contains no GDPR / legal-basis section — https://guardrailsai.com/legal/terms-of-use ; https://guardrailsai.com/legal/privacy-policy |
| Data minimization | default ON, easy opt-out | 1 | `guardrails configure --enable-metrics / --disable-metrics` "[default: enable-metrics]"; `allow_metrics_collection` on Guard — https://guardrailsai.com/guardrails/docs/cli ; https://guardrailsai.com/guardrails/docs/api_reference_markdown/guards |
| AI training use | no mention | 0 | No statement in the privacy policy or ToU; ToU §5.2 licenses Customer Data "for purposes of providing and/or improving the Services" |
| Sub-processor transparency | none | 0 | No list located (see V) |
| Data retention disclosure | none | 0 | No retention schedule in the privacy policy or ToU |

Positive findings: a privacy policy with a dated effective date (2025-05-01) and a named contact; the ToU's DPA clause and higher-protection conflict rule (§2.3).
Recorded concerns: silence on training use, sub-processors and retention is scored as zero; the privacy policy describes session-replay (PostHog) and interest-based advertising for the web service. Prior D 1/15; +1 reflects fresh application of the criteria (documented telemetry opt-out), with the prior criterion-level breakdown unpublished.

### I — Identity & Control | 3/10

| Criterion | Result | Score | Evidence (source URL) |
|---|---|---|---|
| Emergency stop documentation | documented but incomplete | 2 | `OnFailAction.EXCEPTION` (raises ValidationError) and `REFRAIN` (returns empty) are documented fail-closed controls at validator level; no documented stop procedure for `guardrails start` servers or the operator's hosted surfaces. During the incident the operator took the Ray cluster and validator hub offline (advisory) — https://guardrailsai.com/guardrails/docs/concepts/validator_on_fail_actions ; https://github.com/guardrails-ai/guardrails/blob/main/SECURITY_ADVISORY.md |
| Human-in-the-loop design | not confirmed | 0 | No documented human-review mode. `OnFailAction.CUSTOM` calls an application-supplied function; it is an extension point, not a documented HITL design — https://guardrailsai.com/guardrails/docs/api_reference_markdown/types |
| Permission delegation transparency | partial | 1 | Docs describe the `llm_api` callable, local vs self-hosted validator inference (`use_local=True`, `validation_endpoint=`) and, since 0.11.0, installation of validators as public PyPI packages without an API key; no permission model for validators, which run with the host process's privileges — https://github.com/guardrails-ai/guardrails/issues/1560 ; https://guardrailsai.com/guardrails/docs/migration-guides/0-11-migration |

Positive findings: fail-closed actions are documented and configurable per validator; API-key dependence for validator installation was removed in 0.11.0; forced rotation of Snowglobe / Hub API keys was announced with a fixed time (2026-05-13 14:00 PT).
Recorded concerns: no HITL mode; no operator-side stop or incident procedure documented outside the incident advisory. Prior I 4/10; −1 reflects fresh application of the HITL criterion.

### C — Containment | 3/10

| Criterion | Result | Score | Evidence (source URL) |
|---|---|---|---|
| Sandbox design | unknown | 0 | Validators are Python packages executed in-process with the host's privileges; no sandbox is documented. CVE-2026-31233 documents that the Hub installer executed a script path taken from an untrusted Hub manifest (`post_install`) — https://github.com/advisories/GHSA-r6hf-g5x6-7pv9 . The Hub installer, private registry (pypi.guardrailsai.com) and hosted inference (hub.api.guardrailsai.com) were retired 2026-08-25 (hosted inference stated as 2026-08-06 in the same issue and in the migration guide); validators now install from public PyPI as `guardrails-ai-<name>` — https://github.com/guardrails-ai/guardrails/issues/1560 |
| Least privilege | broad defaults | 0 | No privilege scoping for validators or guards is documented; in-process execution is the only documented model |
| Tenant isolation (cloud) | self-hosted only for the target (N/A) | 3 | The evaluated target is the self-hosted framework; the operator's hosted validator inference was taken offline in the incident and retired in the window. Snowglobe / Pro remain hosted operator surfaces with no published isolation architecture (out of target scope; recorded here as operator-side evidence) |

Positive findings: the operator's stated rationale for retiring the Hub installer was install cleanliness and hosting cost; the change removes the manifest-driven post-install execution path and the private registry from new installs, and the operator now states verified-signature commits and Trusted Publishing for its own artifacts.
Recorded concerns: no sandbox, no privilege model; the validator packages ship under separate version lines and, in at least one documented case, a different licence from the core (third-party report); hosted surfaces' isolation architecture remains unpublished. Prior C 3/10.

### T — Transparency | 5/10

| Criterion | Result | Score | Evidence (source URL) |
|---|---|---|---|
| CVE publication posture | issues CVEs + advisories | 2 | Vendor-published GHSA-xmpw-2vmm-p4p6 with CVE-2026-45758 via the GitHub CNA (reserved 2026-05-13, published 2026-06-05) — https://github.com/guardrails-ai/guardrails/security/advisories ; CVE-2026-31233 was assigned by MITRE from a third-party report with no vendor advisory |
| Incident disclosure speed | ≤30 d | 2 | Event 2026-05-11 ~18:00 PT; GHSA and SECURITY_ADVISORY.md published 2026-05-12 (~1 day) |
| Security policy publication | general mention | 1 | Responsible-disclosure blog with safe harbor and security@ channel (2024-02-22) — https://guardrailsai.com/blog/commitment-to-responsible-vulnerability ; SECURITY_ADVISORY.md lists incident-specific organizational controls; no SECURITY.md at repository root ("No security policy detected") — https://github.com/guardrails-ai/guardrails/security/policy |
| AI safety framework reference | none | 0 | No NIST AI RMF / ISO/IEC 42001 mapping for the operator's own posture located |
| AI system identity disclosure | none | 0 | Not applicable to a validation framework; no disclosure feature documented |

Positive findings: same-day incident advisory with a named root cause, a tracking issue and a fixed key-rotation deadline; CVE assignment through the GitHub CNA.
Recorded concerns: no vendor advisory for CVE-2026-31233 (136 days after publication); SECURITY.md still absent; no security page or framework mapping. Prior T 4/10; +1 reflects fresh application of the criteria.

---

## Incident Timeline

| Date | CVE ID | CVSS | Description | Patch status | CISA KEV |
|---|---|---|---|---|---|
| 2026-05-12 (NVD publish; reserved 2026-03-09) | CVE-2026-31233 / GHSA-r6hf-g5x6-7pv9 / PYSEC-2026-347 | 9.8 (3.1) | Code injection (CWE-94) in the Hub package installer: script path taken from the `post_install` field of an untrusted Hub manifest and executed; affects guardrails-ai through 0.6.7 | No patched version declared; no vendor advisory; Hub installer retired 2026-08-25 (not stated as a fix) | None |
| 2026-05-11 ~18:00 PT (2026-05-12 UTC) | CVE-2026-45758 / GHSA-xmpw-2vmm-p4p6 / PYSEC-2026-206 / MAL-2026-3607 | 9.6 (3.1) | Malicious `guardrails-ai==0.10.1` on PyPI (CWE-506): code appended to `guardrails/__init__.py` downloads and executes a remote payload on import (Linux only); part of the 2026-05-11 npm/PyPI campaign (TanStack, Mistral AI, UiPath, OpenSearch, Guardrails AI); researchers attribute the infrastructure to "TeamPCP" | Quarantined by PyPI ~2 h after publication; advisory 2026-05-12; keys invalidated 2026-05-13; clean 0.10.2 2026-06-04 (Trusted Publishing); CVE published 2026-06-05 | None |
| 2026-07-07 | PYSEC-2026-1432 (alias CVE-2024-45858 / GHSA-w392-75q8-vr67) | 8.8 (3.1) / 8.6 (4.0) | Re-publication by PyPA of the 2024 eval-based code execution in RAIL XML (0.2.9–0.5.9) | Fixed 0.5.10 (2024-09-17); out of window; not counted | None |
| 2026-07-07 | PYSEC-2026-1431 (alias CVE-2024-6961 / GHSA-f8hx-f4xw-c646) | 5.9 (3.1) / 8.2 (4.0) | Re-publication by PyPA of the 2024 RAIL XXE | Fixed 0.5.0 (2024-07-17); out of window; not counted | None |
| 2026-03 | dependency: BerriAI/litellm | — | litellm PyPI removal broke fresh installs; 0.9.3 pinned litellm below the affected version (2026-03-24), 0.10.2 re-opened the pin to ≥1.83.0 | Availability event on a dependency; not a Guardrails artifact compromise; not counted | None |

---

## Contextual Analysis

The May 2026 compromise was a publishing-credential event rather than a code defect: the operator states that an employee's GitHub PAT was used to trigger a GitHub Action across 30 repositories in the `guardrails-ai` organization, that artifacts from those runs contained repository secrets, and that deploy tokens extracted from them were used to publish 0.10.1 to PyPI. The same operator statement records unsuccessful attempts against the Ray cluster used for remote validator inference and against other package registries. Independent analysis by SafeDep and Socket recovered the 0.10.1 diff (15 lines appended to `__init__.py`, executing only on `sys.platform.startswith("linux")`) and placed the package inside a campaign that spanned npm and PyPI in a single night. The elapsed times on record are short: ~2 hours to detection and quarantine, ~1 day to a vendor advisory naming the root cause, ~2 days to forced API-key rotation, and 23 days to a clean successor release, which was also the first release published under PyPI Trusted Publishing with a Sigstore-logged attestation. The operator's subsequent controls (classic PATs blocked, fine-grained PATs with approval and expiry, mandatory verified commit signatures, GitHub Actions template-injection fixes) are stated in its own advisory and release notes; VERDICT records them as stated and has not verified their enforcement.

CVE-2026-31233 is a different kind of record. It was assigned by MITRE on the basis of a third-party write-up, describes the Hub installer executing a script path from manifest data, and lists no patched version and no vendor response. Within the same window the operator retired the Hub installer and private registry for stated reasons of install cleanliness and hosting cost, and 0.11.0 moved validators to public PyPI packages under the `guardrails_ai` namespace. The retirement removes the affected path from new installs, but no public source connects the two, and users on versions through 0.6.7 have no vendor statement to act on. The data therefore shows one Critical vulnerability handled in hours and one Critical vulnerability with no vendor record after 136 days; the report scores the patch criterion on the second.

Whether the 2024 RAIL code-execution issues and the 2026 Hub-manifest issue share a design-level root cause is a question the public record does not settle. Both belong to the code-injection class (CWE-94/95) and both execute content the framework receives from outside the process — RAIL documents in one case, Hub manifests in the other — but they sit in different components with different fixes and different reporters. The Scorecard treats them as isolated and records the stricter reading and its score impact so a reader can apply it.

Ownership changed after the sweep that drafted this update. Harvey, a legal-AI company, announced on 2026-09-09 that it had acquired Guardrails AI and that co-founders Shreya Rajpal and Zayd Simjee and their team would join Harvey's product and engineering organization; Latham & Watkins announced it advised Harvey on the transaction; terms were not disclosed. The announcement lists Guardrails' investors as Zetta Venture Partners, Bloomberg Beta, Pear VC, Factory and Microsoft (the 2024 seed announcements name GitHub Fund; Zetta led the $7.5M round). The announcement makes no statement about future maintenance of the open-source framework; the repository shipped 0.11.0 on 2026-08-14 and continued to receive pushes in September. Third-party commentary describes the deal as an acqui-hire and notes that Harvey's CEO has characterized its acquisitions that way; VERDICT records the characterization as reported and attributes no intent. For the disclosure layer, the relevant structural fact is that GV led Harvey's Series C and Google is a material Anthropic equity-holder; that relationship now sits one corporate level above the evaluated platform and is disclosed below.

The hosted inference retirement also changes the economic and operational shape of the framework: validators that ran on Guardrails-hosted endpoints, offered free since 2024, now run in-process (`use_local=True`) or on an endpoint the user hosts. No hidden-charge or cost-runaway issue was found (P dimension: no issue recorded); the change moves compute cost to the user and is documented in the migration guide. The Hub catalog (65 validators) remains online as documentation; the issue announcing the cutoff states that 50 of 64 validators were on PyPI at announcement, with the remainder to follow.

Dormancy test: not dormant — 0.11.0 released 2026-08-14 (PyPI, GitHub Release), repository activity through 2026-09.

---

## VERDICT Record

### Summary
The data shows two Critical CVEs in twelve months — a same-night PyPI supply-chain compromise disclosed by the vendor within a day, and a Hub-installer code injection with no vendor record — alongside an ownership change to Harvey and the retirement of the Hub installer and hosted inference. Layer 0 total: 32/85, Tier D (previous: 40/85, Tier C).

### Risk Factor Summary by Use Case

| Use case | Risk factors recorded | Key data points |
|---|---|---|
| Internal testing / non-sensitive workflows | In-process validator execution with no sandbox; anonymous metrics on by default | C 0/4 sandbox; `guardrails configure [default: enable-metrics]` |
| Workflows handling API keys / credentials | Import-time payload in 0.10.1 targeted host credentials; Hub-installer code injection through 0.6.7 with no declared fix | CVE-2026-45758 (9.6), CVE-2026-31233 (9.8); advisory instructs rotation of PATs, cloud keys, registry tokens |
| Cloud version (multi-tenant) | Hosted validator inference retired 2026-08-25; Snowglobe / Pro isolation architecture unpublished (out of target scope) | issue #1560; forced API-key rotation 2026-05-13 |
| Medical / financial / legal data | No public DPA URL, sub-processor list, retention schedule or training-use statement; no independent certification; parent now a legal-AI vendor whose attestations do not cover this target | D 2/15; V certification 0/4 |

### Reference Information
- 0.10.2 and later carry PyPI Trusted Publishing attestations; users may wish to verify attestations at install time and to pin away from 0.10.1, which remains quarantined.
- Users on guardrails-ai versions through 0.6.7 have no vendor statement on CVE-2026-31233; reviewing the installer path in use and the 0.11 migration guide (public PyPI validators, `use_local=True` or a self-hosted endpoint) is one available option.
- Credential rotation after a supply-chain incident is a common industry practice; the operator's advisory lists the credential classes it considers exposed on hosts that installed 0.10.1.

### Bias Disclosure
"This evaluation uses Claude (Anthropic) as its tooling. Anthropic operates in the AI agent market and may compete with some evaluated vendors. VERDICT discloses this relationship in every report and applies identical evaluation criteria to all platforms regardless of their relationship to Anthropic."

VERDICT additionally discloses a shared-investor relationship at the parent-entity level (Trigger 2). Harvey announced its acquisition of Guardrails AI on 2026-09-09. GV (Google Ventures, Alphabet) led Harvey's $100M Series C on 2024-07-23 and participated in its Series D; Google is a material Anthropic equity-holder as recorded in KNOWN_FACTS.md. This is a corporate-level equity relationship one level above the evaluated platform; it does not change the scoring methodology, which remains based exclusively on public sources. Separately, and at product level only, the Guardrails framework supports Claude as one of multiple LLM providers (PyPI extra `anthropic`); this integration is not a disclosure trigger. Microsoft (via GitHub Fund) participated in Guardrails AI's 2024 seed round; on the public record that participation does not meet the material-investor threshold and is noted for completeness.

---

## Evaluation History

| Date | Type | Score | Tier | Framework |
|---|---|---|---|---|
| 2026-05-12 | Initial (Layer 0) | 40 | C | v0.3.1-final |
| 2026-09-25 | Update | 32 | D | v0.3.2 |

---

## Future Evaluation Plan

| Phase | Content | Planned timing |
|---|---|---|
| Layer 1 | Behavioral testing on a local install (30 runs × 4 levels, 3+ days) | Not scheduled |
| Layer C — routine | Full routine differential (R, T, V; D/I/C per carry-forward conditions) | 365 days from 2026-09-25 (provisional, ReviewCadence-002) |
| Layer C — interrupt | T1 / T2 / T3 sweep; KEV feed weekly; T5 follow-up on the post-acquisition entity structure and framework maintenance statements | Continuous; next quarterly sweep |

---

```japanese-summary
# Guardrails AI 評価結果サマリー

## 基本情報
- 評価種別: 更新
- スコア: 32/85 (Layer 0)
- 前回スコア: 40/85（2026.05.12、Tier C）
- ランク: 66 / 70（build_index ローカル実行値、前回 53/69）
- 評価日: 2026.09.25
- 対象バージョン: guardrails-ai 0.11.0（PyPI 2026-08-14）
- 運営: Harvey（via Guardrails AI, Inc.）— 2026-09-09 買収発表
- 独立性: ⚠️ Harvey AI Corporation

## 次元スコア
- V (検証可能性): 13/20
- R (耐性): 6/20
- D (データ運用): 2/15
- I (制御): 3/10
- C (封じ込め): 3/10
- T (透明性): 5/10

## 主要ポジティブ所見
- 悪性 0.10.1 の公開から約 2 時間で第三者検知・PyPI 隔離、翌 2026-05-12 に根本原因（従業員 PAT 侵害 → GitHub Action 30 repo → deploy token 抽出）を明記した vendor advisory を公開
- API key 強制ローテーション（2026-05-13 14:00 PT）、classic PAT 禁止・fine-grained PAT 承認制・全 commit 署名必須を運営が明記
- 0.10.2（2026-06-04）以降は PyPI Trusted Publishing + Sigstore attestation 付きリリース
- Apache-2.0 で全コード監査可能、GitHub Release ノートと 0.11 移行ガイドを公開

## 主要リスク所見
- 12 か月で Critical CVE 2 件（最大 CVSS 9.8）、うち CVE-2026-31233（Hub installer post_install コード注入、≤0.6.7）は patched version 宣言・vendor advisory とも無し（公開後 136 日）
- サプライチェーン侵害 1 件（運営自身の PyPI パッケージ）。clean 版 0.10.2 まで 23 日
- Hub installer・private registry・hosted inference を 2026-08-25 に廃止、validator は public PyPI package 化（サンドボックス無し・in-process 実行は不変）
- 公開 DPA URL・サブプロセッサ一覧・保持期間・学習利用の記載無し、SOC 2 等の第三者認証無し
- 2026-09-09 に Harvey が買収を発表。OSS フレームワークの今後の保守方針は未表明

## インシデント
- CVE-2026-31233, CVSS 9.8, Hub installer の post_install 経由コード注入（≤0.6.7）、修正版宣言なし
- CVE-2026-45758, CVSS 9.6, PyPI に悪性 guardrails-ai 0.10.1 が公開（2026-05-11 18:00 PT）、import 時に遠隔ペイロード実行（Linux）
- PYSEC-2026-1431 / PYSEC-2026-1432: 2024 年 CVE（CVE-2024-6961 / CVE-2024-45858）の再掲、window 外・不算入
- 依存関係: litellm PyPI 削除（2026-03）— 可用性事象、不算入

## CISA KEV
- 該当なし

## HTMLカード用タグ
- tags: ai-safety, llm-guardrails, validators, apache-2-0, open-source-framework, guardrails-hub, snowglobe, harvey, subsidiary, supply-chain-compromise, tier-d, evaluator-coi, shared-investor
- incident_tags: supply-chain-compromise, cve-2026-45758, cve-2026-31233, pypi-malicious-package, hub-installer-code-injection, ownership-change
- owner: Harvey（via Guardrails AI, Inc.）
```

```
Score: 32/85
V: 13/20, R: 6/20, D: 2/15, I: 3/10, C: 3/10, T: 5/10
Dimensions verified: V+R+D+I+C+T = 32
Tier: D · Category: AI Safety
```
