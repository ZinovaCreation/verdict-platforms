---
name: LlamaIndex
slug: llamaindex
operator: LlamaIndex, Inc.
independence: independent
parent_entity: null
category: RAG / Agent Data Framework · Open core (MIT framework; closed-source LlamaCloud)
homepage: https://www.llamaindex.ai
github: https://github.com/run-llama/llama_index
evaluation_number: 14
evaluation_type: update
evaluated_at: '2026-03-25'
updated_at: '2026-11-06'
evaluator_model: claude-fable-5-1
framework_version: v0.3.2
layer: '0'
target_version: 'llama-index / llama-index-core 0.14.25 (PyPI 2026-09-21); run-llama/llama_index @ 444fdf0 (2026-11-03); LlamaCloud hosted (no public version string; ToS/Privacy Notice 2026-10-25)'
previous_evaluation_date: '2026-03-25'
previous_score: 41
score: 44
max_score: 85
tier: C
verdict:
  v:
    score: 14
    rating: High
    note: 'LlamaIndex, Inc. named in ToS; MIT framework, closed LlamaCloud; SOC 2 under NDA'
  e:
    score: null
    rating: null
    note: null
  r:
    score: 8
    rating: Mid
    note: '2 CVEs, max 7.5; CVE-2024-58339 no fix located; shared resource-exhaustion cause'
  d:
    score: 10
    rating: Mid
    note: 'Public DPA w/ SCCs; no-training + 48h deletion in ToS; sub-processors undated'
  i:
    score: 4
    rating: Mid
    note: 'cancel_run() documented; HITL optional via events; project-scoped API keys'
  c:
    score: 2
    rating: Low
    note: 'Threat model places sandboxing in host app; no tenant-isolation statement'
  t:
    score: 6
    rating: Mid
    note: 'Detailed SECURITY.md threat model; same-day status disclosure; 3rd-party CNAs'
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
  revision_cycles: 0
  flagged: false
differential:
  v: re-evaluated
  e: null
  r: re-evaluated
  d: re-evaluated
  i: re-evaluated
  c: re-evaluated
  t: re-evaluated
next_review_due: '2027-11-06'
tags:
  - rag-framework
  - open-core
  - mit
  - llamacloud
  - soc2-type2
  - hipaa
  - public-dpa
  - eu-region
  - no-training-default
  - resource-exhaustion
  - pickle-deserialization
  - no-kev
  - no-supply-chain-compromise
rank: 47
sources:
  - https://github.com/run-llama/llama_index
  - https://github.com/run-llama/llama_index/blob/main/SECURITY.md
  - https://github.com/run-llama/llama_index/blob/main/LICENSE
  - https://github.com/run-llama/llama_index/blob/main/CHANGELOG.md
  - https://github.com/run-llama/llama_index/releases
  - https://github.com/run-llama/llama_index/pull/17121
  - https://github.com/run-llama/llama_index/commit/53614e2f7913c0e86b58add9470b3c900b6c60b2
  - https://pypi.org/project/llama-index/
  - https://pypi.org/project/llama-index-packs-vanna/
  - https://pypi.org/project/llama-index-indices-managed-bge-m3/
  - https://nvd.nist.gov/vuln/detail/CVE-2024-58339
  - https://www.vulncheck.com/advisories/llamaindex-vannaqueryengine-sql-execution-allows-resource-exhaustion
  - https://www.vulncheck.com/advisories/llamaindex-bgem3index-unsafe-deserialization
  - https://db.gcve.eu/vuln/fkie_cve-2024-14021
  - https://db.gcve.eu/vuln/cve-2025-6208
  - https://osv.dev/vulnerability/PYSEC-2026-1560
  - https://osv.dev/vulnerability/PYSEC-2026-86
  - https://osv.dev/vulnerability/PYSEC-2026-85
  - https://newreleases.io/project/pypi/llama-index-core/release/0.14.16
  - https://intel.aikido.dev/cve/AIKIDO-2026-10351
  - https://nuka-ai.github.io/posts/2026-05-12-Llamaindex-SelfNuke-disclosure/
  - https://osv.dev/vulnerability/MAL-2026-227
  - https://app.opencve.io/cve/?vendor=run-llama
  - https://www.cvelogic.com/vendor/llamaindex
  - https://www.llamaindex.ai/legal/terms-of-service
  - https://www.llamaindex.ai/legal/privacy-notice
  - https://security.llamaindex.ai
  - https://security.llamaindex.ai/subprocessors
  - https://security.llamaindex.ai/resources
  - https://llamaindex.statuspage.io/
  - https://llamaindex.statuspage.io/api/v2/incidents.json
  - https://mcp.llamaindex.ai/terms-of-service
  - https://crossposter.llamaindex.ai/privacy-policy
  - https://developers.llamaindex.ai/llamaparse/general/enterprise-readiness/
  - https://developers.llamaindex.ai/llamaparse/general/enterprise-readiness/compliance/index.md
  - https://developers.llamaindex.ai/llamaparse/general/enterprise-readiness/data-privacy-security/index.md
  - https://developers.llamaindex.ai/llamaparse/general/enterprise-readiness/eu-compliance/
  - https://developers.llamaindex.ai/llamaparse/general/enterprise-readiness/deployment/
  - https://developers.llamaindex.ai/llamaparse/general/enterprise-readiness/access-identity/
  - https://developers.llamaindex.ai/llamaparse/general/status/
  - https://developers.llamaindex.ai/llamaparse/general/api_key/index.md
  - https://developers.llamaindex.ai/llamaparse/self_hosting/configuration/user-roles/index.md
  - https://developers.llamaindex.ai/llamaparse/general/billing/index.md
  - https://developers.llamaindex.ai/llamaparse/self_hosting/configuration/usage-controls/index.md
  - https://developers.llamaindex.ai/python/framework/understanding/privacy
  - https://developers.llamaindex.ai/python/llamaagents/workflows/human_in_the_loop/index.md
  - https://www.llamaindex.ai/blog/announcing-our-series-a-and-llamacloud-general-availability
  - https://www.norwest.com/blog/llamaindex-harnesses-the-power-of-enterprise-data-for-ai-agent-workflows/
  - https://www.llamaindex.ai/blog/llamaindex-welcomes-investments-from-databricks-and-kpmg
  - https://databricks.com/blog/databricks-invests-llamaindex-advance-knowledge-agents-over-enterprise-data
  - https://www.cisa.gov/sites/default/files/feeds/known_exploited_vulnerabilities.json
og_description: 'Independent security evaluation of LlamaIndex. Score: 44/85 (Tier C). 2 CVEs in the trailing 12 months, max CVSS 7.5, one without a located fix. MIT framework; closed-source LlamaCloud with a public DPA, sub-processor list, no-training default and SOC 2 Type II (under NDA). Framework v0.3.2, updated 2026-11-06.'
category_line: RAG / Agent Data Framework · Open core (MIT framework; closed-source LlamaCloud)
display_tags: &id001
- text: 2 CVEs · Max CVSS 7.5 · 1 Without Located Fix
  color: amber
- text: Resource-Exhaustion Pattern · Trusted-Env Threat Model
  color: amber
- text: Pickle Path Unpatched · BGEM3Index (Retroactive CVE)
  color: warn
- text: Public DPA · Subprocessor List · No-Training Default
  color: safe
- text: SOC2 Type II (NDA) · HIPAA (Enterprise) · EU Region
  color: safe
- text: No KEV · No Supply Chain Compromise
  color: dim
finding: '2 CVEs in the trailing 12 months (CVE-2024-58339, CVSS 7.5, no fix located; CVE-2025-6208, CVSS 5.3, fixed before publication), both resource-exhaustion issues in independent components. CVE-2024-14021 (BGEM3Index pickle) is retroactive and its pickle.load() remains at 444fdf0. LlamaCloud (ToS 2026-10-25): no-training default, 48h deletion, public self-serve DPA with SCCs, 13-entry sub-processor list (undated), SOC 2 Type II on request under NDA.'
meta_description: 'Independent security evaluation of LlamaIndex. Score: 44/85 (Tier C). 2 CVEs in the trailing 12 months, max CVSS 7.5, one without a located fix. MIT framework; closed-source LlamaCloud with a public DPA, sub-processor list, no-training default and SOC 2 Type II (under NDA). Framework v0.3.2, updated 2026-11-06.'
key_finding: 'Two CVEs attributable to the llama_index framework were published in the trailing 12 months: CVE-2024-58339 (VannaPack query engine, resource exhaustion, NVD CVSS 3.1 7.5, no fix release located) and CVE-2025-6208 (SimpleDirectoryReader, CVSS 5.3, fixed in v0.12.41 eight months before the CVE). Both share a root cause — no bound on resource consumption from caller-supplied input — in independent components. CVE-2024-14021 (BGEM3Index unsafe pickle) is recorded as a retroactive CVE (first disclosed in PR #17121, 2024-12-02); the pickle.load() it describes is still present at commit 444fdf0. The vendor''s SECURITY.md places input validation, sandboxing and DoS from unbounded input outside the library''s scope. LlamaCloud''s Terms of Service (2026-10-25) state a no-training default, deletion of inputs and outputs within 48 hours, and an automatically incorporated self-serve DPA with EU SCCs that is publicly downloadable; a 13-entry sub-processor list is public but undated; the SOC 2 Type II report (opinion 2026-11-04) is available on request under NDA; no BAA is entered into for self-serve use.'
card_owner: LlamaIndex, Inc.
card_category: RAG / Agent Data Framework · Open core (MIT framework; closed-source LlamaCloud)
card_tags: *id001
score_basis: consistent
---
# LlamaIndex

Two CVEs attributable to the llama_index framework were published in the trailing 12 months (2025-11-06 to 2026-11-06): CVE-2024-58339 (VannaPack query engine, resource exhaustion, NVD CVSS 3.1 7.5, no fix release located) and CVE-2025-6208 (SimpleDirectoryReader, CVSS 5.3, fixed in v0.12.41 eight months before the CVE was published). Both share a root cause — no bound on resource consumption from caller-supplied input — in independent components. CVE-2024-14021 (BGEM3Index unsafe pickle deserialization) is recorded as a retroactive CVE, first disclosed in PR #17121 on 2024-12-02; the `pickle.load()` it describes is still present at commit 444fdf0. The vendor's SECURITY.md places input validation, sandboxing and denial of service from unbounded input outside the library's scope. LlamaCloud's Terms of Service and Privacy Notice (2026-10-25) state a no-training default, deletion of inputs and outputs within 48 hours, and a publicly downloadable self-serve DPA with EU Standard Contractual Clauses that is incorporated automatically; a 13-entry sub-processor list is public but carries no update date; the SOC 2 Type II report (Security criteria, opinion issued 2026-11-04) is available on request under NDA; no Business Associate Agreement is entered into for self-serve use.

## Layer 0 Score: 44/85 (Tier C)

**V** 14/20 · **R** 8/20 · **D** 10/15 · **I** 4/10 · **C** 2/10 · **T** 6/10

Previous: 41/85 (2026-03-25, framework v0.3.1, migrated capture). Updated 2026-11-06 under framework v0.3.2; all six dimensions re-evaluated, none carried forward.

## CISA KEV

None — no LlamaIndex CVE appears in the CISA Known Exploited Vulnerabilities catalog (catalogVersion 2026.11.04, 1,768 entries, checked 2026-11-06; per-ID check negative for CVE-2024-14021, CVE-2024-58339, CVE-2025-6208 and CVE-2025-1793). Two published CVEs in the trailing 12 months (basis: exact): CVE-2024-58339 (CVSS 7.5, no fix located) and CVE-2025-6208 (CVSS 5.3, fixed). CVE-2024-14021 was published in the window but is excluded as a retroactive CVE (first disclosed 2024-12-02). No supply chain compromise of the vendor's packages was confirmed.

## Bias Disclosure

This evaluation uses Claude (Anthropic) as its tooling. Anthropic operates in the AI agent market and may compete with some evaluated vendors. VERDICT discloses this relationship in every report and applies identical evaluation criteria to all platforms regardless of their relationship to Anthropic.

## Evaluation History

| Date | Type | Score | Tier | Framework |
|---|---|---|---|---|
| 2026-03-25 | Initial (migrated capture) | 41/85 | C | v0.3.1 |
| 2026-11-06 | Update (full re-review; no carry-forward) | 44/85 | C | v0.3.2 |

## Full Evaluation

# VERDICT Evaluation #014 — LlamaIndex (Update)

| Field | Value |
|---|---|
| Evaluation number | #014 |
| Platform | LlamaIndex (llama_index framework + LlamaCloud) |
| Evaluation type | Update (Differential Evaluation) |
| Date (`updated_at`) | 2026-11-06 |
| Original Layer 0 date (`evaluated_at`) | 2026-03-25 |
| Evaluator | VERDICT evaluation engine; `evaluator_model: claude-fable-5-1` (as supplied at invocation, EvaluatorModel-Provenance-001) |
| Target version | llama-index 0.14.25 / llama-index-core 0.14.25 (PyPI, 2026-09-21); repository run-llama/llama_index @ 444fdf0 (2026-11-03); LlamaCloud hosted service (no public version string; vendor changelog through 2026-09; Terms of Service and Privacy Notice last updated 2026-10-25) |
| Framework | VERDICT v0.3.2 (`zinova-lab/verdict-engine` @ 73d9a09; ENGINE.md / QA.md / KNOWN_FACTS.md as pinned at invocation) |
| Previous evaluation | 2026-03-25 · 41/85 · Tier C · framework v0.3.1 (migrated capture) |
| Layer | 0 (public documentation only; E not evaluated) |
| Lane | Routine (batch-1 scheduled; interval not elapsed) |

## Executive Summary

Two CVEs attributable to the llama_index framework were published in the trailing 12 months (2025-11-06 to 2026-11-06): CVE-2024-58339 (VannaPack query engine, resource exhaustion, NVD CVSS 3.1 7.5, no fix release located) and CVE-2025-6208 (SimpleDirectoryReader, uncontrolled memory consumption, CNA CVSS 3.0 5.3, fixed in v0.12.41 eight months before the CVE was published). A third ID, CVE-2024-14021 (BGEM3Index pickle deserialization), was published in the window but is recorded as a retroactive CVE because the vulnerability was publicly identified in pull request #17121 on 2024-12-02; the `pickle.load()` call it describes is still present in the repository at commit 444fdf0. The Layer 0 score is 44/85 (Tier C), up from 41/85: the base record was a migrated capture without per-dimension sources, so every dimension was re-evaluated and none was carried forward, and the hosted surface's documents read for this update — Terms of Service and Privacy Notice dated 2026-10-25, a publicly downloadable self-serve Data Processing Addendum with EU Standard Contractual Clauses (published 2026-10-26), a 13-entry sub-processor list, a no-training default with 48-hour deletion, and a SOC 2 Type II report (opinion issued 2026-11-04) available on request under NDA — are more extensive than the base record captured. No CISA KEV entry, no supply chain compromise and no disclosure-layer trigger were found.

## Scorecard

| Dimension | Score | Max | Rating |
|---|---|---|---|
| V — Verifiability | 14 | 20 | High |
| R — Resilience | 8 | 20 | Mid |
| D — Data Conduct | 10 | 15 | Mid |
| I — Identity & Control | 4 | 10 | Mid |
| C — Containment | 2 | 10 | Low |
| T — Transparency | 6 | 10 | Mid |
| E — Effectiveness | — | 15 | Not evaluated (Layer 1+) |
| **Layer 0 total** | **44** | **85** | |

Tier: C
Category: RAG / Agent Data Framework · Open core (MIT framework; closed-source LlamaCloud)

CISA KEV: none. No LlamaIndex CVE appears in the CISA Known Exploited Vulnerabilities catalog (operator JSON check, catalogVersion 2026.11.04, 1,768 entries, retrieved 2026-11-06; per-ID check: CVE-2024-14021, CVE-2024-58339, CVE-2025-6208 and CVE-2025-1793 not present; no entry whose vendorProject, product, vulnerabilityName or shortDescription contains "llama").

Previous score: 41/85 (2026-03-25). Change: +3.

## Differential

**Previous evaluation:** 2026-03-25 · 41/85 · Tier C · framework v0.3.1 · migrated capture (`sources: []`, `qa` unresolved ×3, `evaluator_model: unrecorded`).

**Trigger and lane.** Scheduled batch-1 differential (Tranche B 2 of 14; LayerC-Triage-001 entry on recorded `cve_count_12mo: 3`, basis `range`, at the 2026-10-27 quarterly sweep). Lane: Routine (batch-1 scheduled; interval not elapsed). No interrupt trigger fired at the sweep. During this evaluation a change of terms of service and privacy policy was publicly confirmed (both documents "Last Updated: Oct 25, 2026"; self-serve DPA published 2026-10-26) — a T5 condition whose mandatory re-check scope (V, D; `independence` / `parent_entity`) is absorbed by this full re-review. No change of operator or ownership was found; no KNOWN_FACTS.md entry is staged.

**Per-dimension state.**

| Dimension | State | Reason |
|---|---|---|
| V | re-evaluated | migrated capture, no sources |
| R | re-evaluated | migrated capture, no sources |
| D | re-evaluated | migrated capture, no sources |
| I | re-evaluated | migrated capture, no sources |
| C | re-evaluated | migrated capture, no sources |
| T | re-evaluated | migrated capture, no sources |
| E | null | Layer 1+ only |

**Carry-forward checks.** None were possible. The base record carries no per-dimension citations (`sources: []`), so carry-forward conditions 1–4 (ENGINE.md, Differential Evaluation) could not be positively satisfied for any dimension (convention 2026-09-22). Every dimension was re-evaluated from sources retrieved in this session on 2026-11-06, supplemented by operator-supplied rendered text (below).

**Operator input (OperatorInput-001).** All items retrieved by the operator on 2026-11-06 (JST). No access-request form was submitted and no gated document was requested; only publicly rendered text was supplied.

*First supply (Message 3):*
1. Quarterly sweep 2026-10-27 (operations_sweep_procedure.md, dry run), public-layer observation rows for slug `llamaindex`: none. No T1 / T2 / T5 / dormancy row was recorded; the record entered batch 1 under LayerC-Triage-001 on its recorded `cve_count_12mo` (3, basis range).
2. CISA KEV JSON feed (https://www.cisa.gov/sites/default/files/feeds/known_exploited_vulnerabilities.json): catalogVersion "2026.11.04", dateReleased 2026-11-04T20:00:05.774Z, count 1,768. CVE-2025-1793: not present. No entry whose vendorProject, product, vulnerabilityName or shortDescription contains "llama".

*Second supply (Message 4), rendered text of pages this session had reported as unread:*
3. https://security.llamaindex.ai (Vanta-hosted trust center, client-rendered): Overview (contact security@runllama.ai; Compliance sections SOC 2 / GDPR / HIPAA; Controls list; Data collected: "Credit card information", "Personal health information"); Updates — one entry, 2026-10-26, announcing a single self-serve DPA for US and EU instances (applies on acceptance of the ToS, includes EU SCCs and UK Addendum, pre-signed, downloadable from Resources) and a standard Mutual NDA whose acceptance is the only step for gated documents such as the SOC 2 report; sub-processor changes notified by subscription. https://security.llamaindex.ai/subprocessors: 13 entries with role, region and vendor URL, no list-level date on the page (AWS, Google Cloud Platform, Microsoft, OpenAI, Anthropic, Modal, Hugging Face, Cohere, Sentry, WorkOS, PostHog, Pylon, Stripe). https://security.llamaindex.ai/resources: DPA (Self-Serve, US & EU) — public view; Mutual NDA (Standard) — public view; Penetration Test Report Executive Summary (2026) — request access; 2026 Penetration Testing Remediation Status Letter — request access; "LlamaIndex SOC 2 Type II Report (2026)" — request access under NDA, Security criteria, period 2026-05-31 to 2026-08-31, auditor Advantage Partners, unqualified opinion issued 2026-11-04.
4. https://llamaindex.statuspage.io/ (Atlassian Statuspage, vendor-operated): /history and the public API https://llamaindex.statuspage.io/api/v2/incidents.json — 50 incidents in total, 30 created in the window 2025-11-06 to 2026-11-06, all "resolved" with created and resolved timestamps; all titled as availability or latency incidents (e.g. 2026-03-01 critical "Currently down in EU and NA"; 2026-07-16 critical "Website Login Issues"; 2026-09-17 major "High error rate for agentic parse in EU"); none titled as a security incident.
5. Main-site legal pages: https://www.llamaindex.ai/privacy and /terms return HTTP 404; the footer links are https://www.llamaindex.ai/legal/privacy-notice and https://www.llamaindex.ai/legal/terms-of-service. Privacy Notice "Last Updated: Oct 25, 2026" (controller "LlamaIndex Inc."; "LlamaIndex, Inc., 447 Sutter St. Ste. 405 PMB 1259, San Francisco, CA 94108, United States"; privacy@runllama.ai; Prighter Group as EU representative; SCCs / UK Addendum for transfers; EEA/UK/Swiss rights and legal bases; sub-processor list referenced at security.llamaindex.ai/subprocessors; retention "no longer than reasonably necessary"; no training on Customer Content except under separate terms). Terms of Service "Last Updated: Oct 25, 2026" (parties "LlamaIndex, Inc. ... and you"; §4.3 no training, third-party model providers on no-training terms, encryption in transit and at rest, deletion no later than 48 hours after processing, stored indexes kept until deleted; §4.4 separate terms apply only on affirmative administrator acceptance; §4.5 no BAA for self-serve use; §5.2 Usage Data definition and ownership; §8.2 DPA incorporated automatically; §8.3 data location US / EU-Frankfurt and sub-processor list; §14.1 Delaware law; §16.8 mailing address). The 2024 subdomain copies read in session (mcp.llamaindex.ai/terms-of-service; crossposter.llamaindex.ai/privacy-policy) are superseded by these versions for the hosted service.
6. CISA KEV per-ID check (same feed): CVE-2024-14021, CVE-2024-58339, CVE-2025-6208, CVE-2025-1793 — not present.

**Pages not read directly by the session (SourceCoverage-001 / -002):** security.llamaindex.ai (metadata only), llamaindex.statuspage.io, www.llamaindex.ai/legal/* and github.com/run-llama/llama_index/security/advisories were not fetchable from the session; the first three are now covered by operator input items 3–5 above; the repository advisory listing was enumerated through the GitHub Advisory Database mirrors (OSV, GitLab Advisory Database, Vulnerability-Lookup), NVD mirrors, PyPI and the cloned repository. huntr report pages for the three in-window IDs were not fetchable; dates were taken from the CVE records, the VulnCheck advisories and the repository.

**Re-score on second supply.** V third-party dependency disclosure 0 → 1 (list without date); V independent certification 2 → 2 (access mode now confirmed: on request under NDA; `[UNVERIFIED]` flag removed); D GDPR compliance disclosure 1 → 3 (public DPA with SCCs + explicit GDPR statement in the Privacy Notice); D sub-processor transparency 0 → 1 (list without date); T incident disclosure speed 0 → 2 (vendor-operated public incident record with same-day disclosure; availability incidents only — see T detail). Total 38 → 44; Tier C unchanged.

**Prior-record omissions (stated as facts):**

- The base record stated `cve_count_12mo: 3` with basis `range` ("at least 3 published CVEs … published as a bound") but named a single CVE ID (CVE-2025-1793, published 2025-06-05). Public advisory databases list at least nineteen further CVEs for run-llama/llama_index published between 2025-03-20 and 2025-10-13 (CVE-2024-11958, CVE-2024-12704, CVE-2024-12909, CVE-2024-12910, CVE-2024-12911, CVE-2025-1750, CVE-2025-1752, CVE-2025-1753, CVE-2025-3044, CVE-2025-3046, CVE-2025-3108, CVE-2025-3225, CVE-2025-5302, CVE-2025-5472, CVE-2025-6209, CVE-2025-6210, CVE-2025-6211, CVE-2025-7647, CVE-2025-7707). The base record's count was therefore a lower bound on a much larger set; this update recomputes the window as `exact`.
- The base record's `max_cvss_12mo: 9.8` was correct for its window (CVE-2025-1793 and CVE-2025-1750, both 9.8). Both IDs fall outside the current window.
- The base record carried `independence: unrecorded`, `target_version: null` and an operator display string ("Independent · Norwest / Greylock · Series A Mar 2025"); all three are resolved in this update.
- The base record described the SQL-injection pattern across "8 vector store integrations" as the "highest … in this index" in its summary text. Comparative claims are not carried forward (Absolute Rule 7; QA §2).

**Fields recomputed on update:** `updated_at` 2026-11-06; `previous_evaluation_date` 2026-03-25; `previous_score` 41; `framework_version` v0.3.2; `target_version` as in the header; `cve_count_12mo` 2 (basis `exact`); `max_cvss_12mo` 7.5; `cisa_kev.present` false; `supply_chain_compromise_12mo` false; `independence` independent; `parent_entity` null; `qa` full protocol result; `evaluator_model` claude-fable-5-1; `dormant_since` omitted (not frozen: release v0.14.25 on 2026-09-21 and commit 444fdf0 on 2026-11-03).

## Evaluation History

| Date | Type | Score | Tier | Framework |
|---|---|---|---|---|
| 2026-03-25 | Initial (migrated capture) | 41/85 | C | v0.3.1 |
| 2026-11-06 | Update (full re-review; no carry-forward) | 44/85 | C | v0.3.2 |

## Dimension Detail

### V — Verifiability (14/20, High)

| Criterion | Result | Score | Evidence URL |
|---|---|---|---|
| Developer / company identity | Confirmed. Operator of record: LlamaIndex, Inc., named as a party in the vendor's Terms of Service (last updated 2026-10-25) and as controller in the Privacy Notice (last updated 2026-10-25), with mailing address 447 Sutter St. Ste. 405 PMB 1259, San Francisco, CA 94108; governing law Delaware (ToS §14.1). No public registry was queried. Official contact: security@runllama.ai (trust center), security@llamaindex.ai (SECURITY.md), privacy@runllama.ai (Privacy Notice). | 4 | https://www.llamaindex.ai/legal/terms-of-service ; https://www.llamaindex.ai/legal/privacy-notice (operator input 2026-11-06) ; https://github.com/run-llama/llama_index/blob/main/SECURITY.md |
| Source code disclosure | Open core. The framework (run-llama/llama_index: llama-index-core, integrations, utils) is MIT-licensed. LlamaCloud (the hosted control plane, cloud.llamaindex.ai; self-hosting via Helm under commercial terms) is closed source. Criterion-VSource-001: core components only. | 2 | https://github.com/run-llama/llama_index/blob/main/LICENSE ; https://developers.llamaindex.ai/llamaparse/general/enterprise-readiness/deployment/ |
| Version management transparency | Confirmed. GitHub releases (v0.14.25, 2026-09-21) and a generated CHANGELOG.md listing every package version per release. | 3 | https://github.com/run-llama/llama_index/releases ; https://github.com/run-llama/llama_index/blob/main/CHANGELOG.md |
| Third-party dependency disclosure | List without date. The trust center publishes 13 sub-processors with role, region and vendor URL; no list-level update date is shown on the page (changes are notified by subscription per the 2026-10-26 Updates entry). | 1 | https://security.llamaindex.ai/subprocessors (operator input 2026-11-06) |
| Independent certification | SOC 2 Type II report (Security criteria; period 2026-05-31 to 2026-08-31; auditor Advantage Partners; unqualified opinion 2026-11-04) available on request under NDA through the trust center — not publicly downloadable. Scored as customers-only / on request. | 2 | https://security.llamaindex.ai/resources (operator input 2026-11-06) ; https://developers.llamaindex.ai/llamaparse/general/enterprise-readiness/compliance/index.md |
| Functional reproducibility docs | Confirmed. Full framework API reference (developers.llamaindex.ai), LlamaCloud REST API reference (api.cloud.llamaindex.ai/docs), SECURITY.md threat model describing the assumed execution environment. | 2 | https://developers.llamaindex.ai/python/framework-api-reference/indices/bge_m3/ ; https://github.com/run-llama/llama_index/blob/main/SECURITY.md |

**Positive findings.** The legal entity and its mailing address are named on the vendor's own Terms of Service and Privacy Notice; the framework is fully MIT-licensed with a per-package changelog; a public sub-processor list and a public, pre-signed self-serve DPA are published on the trust center; API references cover both the framework and the hosted API.

**Recorded concerns.** The sub-processor list carries no update date; the SOC 2 Type II report and the penetration-test documents are gated behind an NDA request.

### R — Resilience (8/20, Mid)

CVE evaluation window: 2025-11-06 to 2026-11-06. `cve_count_12mo: 2` (basis `exact`); `max_cvss_12mo: 7.5`.

| Criterion | Result | Score | Evidence URL |
|---|---|---|---|
| CVE count (trailing 12 months) | 2 counted: CVE-2024-58339, CVE-2025-6208. CVE-2024-14021 excluded as a retroactive CVE (first public disclosure 2024-12-02, PR #17121). No CVSS 9.0+ in the window; no penalty. | 3 | https://cvefeed.io/vuln/detail/CVE-2024-58339 ; https://db.gcve.eu/vuln/cve-2025-6208 ; https://github.com/run-llama/llama_index/pull/17121 |
| Maximum CVSS severity | 7.5 (CVE-2024-58339; NIST NVD Primary CVSS 3.1, vector AV:N/AC:L/PR:N/UI:N/S:U/C:N/I:N/A:H; CNA VulnCheck also publishes CVSS 4.0 8.7, not used per Attribution-CVE-002 order). | 2 | https://nvd.nist.gov/vuln/detail/CVE-2024-58339 |
| Patch response speed | Not confirmed for the set. CVE-2025-6208: fix commit 53614e2 (PR #18983, 2025-06-05) released in v0.12.41 on 2025-06-07, eight months before the CVE was published (2026-02-02). CVE-2024-58339: no fixed version in the CVE record; the affected package (llama-index-packs-vanna) was last released on PyPI on 2024-11-17 (0.3.0) and is not present in the repository at commit 444fdf0; no vendor statement located. Patch status unconfirmed for one of two counted CVEs → scored 0 (Absolute Rule 3). | 0 | https://github.com/run-llama/llama_index/commit/53614e2f7913c0e86b58add9470b3c900b6c60b2 ; https://pypi.org/project/llama-index-packs-vanna ; https://osv.dev/vulnerability/PYSEC-2026-1560 |
| Structural issues | Same root cause recurring. Both counted CVEs are uncontrolled resource consumption from caller-supplied input in independent components (CWE-770 in VannaQueryEngine `custom_query()`; CWE-400 in SimpleDirectoryReader, where `num_files_limit` was applied after all files were loaded). | 0 | https://cvefeed.io/vuln/detail/CVE-2024-58339 ; https://db.gcve.eu/vuln/cve-2025-6208 |
| Supply chain compromise (trailing 12 months) | None. No publicly confirmed unauthorized write to the vendor's PyPI packages, npm package (`llamaindex`), GitHub organization or build pipeline. The npm package `llamaindex-js` flagged as malicious (MAL-2026-227, 2026-01-12) is not a vendor package. | 3 | https://osv.dev/vulnerability/MAL-2026-227 ; https://pypi.org/project/llama-index/ |

**Positive findings.** The 2025-06 fix for CVE-2025-6208 shipped before any public disclosure; no CVSS 9.0+ CVE in the window (the 2025 window carried two 9.8 SQL-injection CVEs); no supply chain compromise; no KEV entry; the vendor added a `RestrictedUnpickler` to `SimpleObjectNodeMapping` in llama-index-core 0.14.16 (PR #20857, 2026-03-10) ahead of any CVE assignment.

**Recorded concerns.** CVE-2024-58339 has no located fix. The `pickle.load()` call described by CVE-2024-14021 (BGEM3Index.load_from_disk) is present in the repository at commit 444fdf0 (`llama-index-integrations/indices/llama-index-indices-managed-bge-m3/.../base.py`, package version 0.8.0 on PyPI 2026-08-31); the community pull request proposing a `safe_pickle_load` (#17121) is not merged. Both in-window CVEs share a root cause, and the vendor's SECURITY.md declares "Denial of Service caused by unbounded or malformed user input" out of scope, which is consistent with the absence of a vendor fix for CVE-2024-58339.

### D — Data Conduct (10/15, Mid)

Scored on the hosted surface (LlamaCloud / LlamaParse) documents.

| Criterion | Result | Score | Evidence URL |
|---|---|---|---|
| GDPR compliance disclosure | DPA standard provision + explicit statement. A self-serve Data Processing Addendum (US & EU) is publicly viewable on the trust center, applies automatically on acceptance of the ToS (§8.2), is pre-signed and includes the EU Standard Contractual Clauses (Modules 2 and 3) and the UK Addendum. The Privacy Notice states legal bases, EEA/UK/Swiss data-subject rights, the right to lodge a complaint with a supervisory authority, transfer mechanisms (SCCs / UK Addendum) and an Article 27 representative (Prighter Group). EU instance data stored in Frankfurt (ToS §8.3). | 3 | https://security.llamaindex.ai/resources ; https://www.llamaindex.ai/legal/privacy-notice ; https://www.llamaindex.ai/legal/terms-of-service (operator input 2026-11-06) ; https://developers.llamaindex.ai/llamaparse/general/enterprise-readiness/eu-compliance/ |
| Data minimization | Default ON, no documented opt-out for the hosted surface. ToS §5.2 defines Usage Data (logs, metadata, performance metrics, credit consumption; excludes User Content), states "We own Usage Data" and that it is shared with third parties "only in aggregated or de-identified form"; PostHog is listed as a product-analytics sub-processor. No opt-out is documented. (The framework itself has no telemetry: no telemetry or analytics endpoint is present in llama-index-core, and the vendor's privacy page states a fully local pipeline makes "no outbound network calls from the embedding, reranking, or retrieval steps".) | 0 | https://www.llamaindex.ai/legal/terms-of-service ; https://security.llamaindex.ai/subprocessors (operator input 2026-11-06) ; https://developers.llamaindex.ai/python/framework/understanding/privacy |
| AI training use | Not used + retention period stated. ToS §4.3: "we do not use User Content to train or fine-tune any artificial intelligence or machine learning model"; third-party model providers engaged "only on terms or configuration that prohibit them from using User Content to train or improve their models"; "input files and parse or extraction outputs are deleted no later than 48 hours after processing completes". §4.4: separate terms (opt-in programs) apply only on affirmative administrator acceptance. Privacy Notice: no use of Customer Content to train or fine-tune models except under separate terms. | 4 | https://www.llamaindex.ai/legal/terms-of-service ; https://www.llamaindex.ai/legal/privacy-notice (operator input 2026-11-06) ; https://developers.llamaindex.ai/llamaparse/general/enterprise-readiness/data-privacy-security/index.md |
| Sub-processor transparency | List without date. 13 sub-processors with role, region and vendor URL; four marked "No access to customer documents" (WorkOS, PostHog, Pylon, Stripe); no list-level update date shown; changes notified by subscription. Referenced from the ToS (§8.3) and the Privacy Notice. | 1 | https://security.llamaindex.ai/subprocessors (operator input 2026-11-06) |
| Data retention disclosure | Per-category. Input files and parse/extract outputs: deleted no later than 48 hours after processing (ToS §4.3; `do_not_cache=true` skips caching per docs); stored indexes and pipelines: kept until deleted or account closed; personal data (controller scope): "no longer than reasonably necessary". | 2 | https://www.llamaindex.ai/legal/terms-of-service ; https://www.llamaindex.ai/legal/privacy-notice (operator input 2026-11-06) ; https://developers.llamaindex.ai/llamaparse/general/enterprise-readiness/data-privacy-security/index.md |

**Positive findings.** A no-training default with 48-hour deletion is written into the Terms of Service, and opt-in programs are stated to require affirmative administrator acceptance; the self-serve DPA with SCCs is public and pre-signed; the sub-processor list is public and names the model providers that receive User Content; EU hosting with an Article 27 representative is documented.

**Recorded concerns.** Usage Data of the hosted service is collected by default with no documented opt-out; the sub-processor list carries no update date; ToS §4.5 states that no Business Associate Agreement is entered into for self-serve use, while the trust center lists "Personal health information" among data collected — readers handling PHI should note that the HIPAA pipeline and BAA are enterprise-contract features.

### I — Identity & Control (4/10, Mid)

| Criterion | Result | Score | Evidence URL |
|---|---|---|---|
| Emergency stop documentation | Documented but incomplete. Workflows document `handler.cancel_run()` and context snapshot/restore for hand-off; no documentation of an immediate kill for a running agent step or of tool-call interruption was located. | 2 | https://developers.llamaindex.ai/python/llamaagents/workflows/human_in_the_loop/index.md |
| Human-in-the-loop design | Optional. HITL is built from `InputRequiredEvent` / `HumanResponseEvent` in workflows; it is not enabled by default. | 1 | https://developers.llamaindex.ai/python/llamaagents/workflows/human_in_the_loop/index.md |
| Permission delegation transparency | Partial. LlamaCloud API keys are tied to the creating user and to one project ("cannot be used across different projects"); organization roles are Admin, Viewer (read-only, ViewerV2) and Viewer (legacy, "not read-only"). Delegation scope of agent tools in the framework is not documented. | 1 | https://developers.llamaindex.ai/llamaparse/general/api_key/index.md ; https://developers.llamaindex.ai/llamaparse/self_hosting/configuration/user-roles/index.md |

**Positive findings.** Project-scoped API keys with documented revocation; a read-only role (ViewerV2) exists and the docs state that the legacy Viewer role can still submit jobs.

**Recorded concerns.** No immediate-stop procedure for agents; HITL is a pattern the developer assembles, not a default.

### C — Containment (2/10, Low)

| Criterion | Result | Score | Evidence URL |
|---|---|---|---|
| Sandbox design | Unknown. SECURITY.md states the library "is intended to be used inside a trusted execution environment" and that input validation is "the responsibility of the hosting application". Code-executing components carry a source-level warning ("Arbitrary code execution is possible on the machine running this tool"); the core `PandasQueryEngine` now raises a `DeprecationWarning` pointing to `llama-index-experimental`. No sandbox is provided. | 0 | https://github.com/run-llama/llama_index/blob/main/SECURITY.md ; https://github.com/run-llama/llama_index/blob/main/llama-index-core/llama_index/core/query_engine/pandas/pandas_query_engine.py |
| Least privilege | Configurable. Hosted: project-scoped keys and a read-only role. Framework: no default privilege boundary; the threat model places all controls in the hosting application. | 1 | https://developers.llamaindex.ai/llamaparse/general/api_key/index.md ; https://github.com/run-llama/llama_index/blob/main/SECURITY.md |
| Tenant isolation (cloud) | Claimed but unverified. Managed SaaS is multi-tenant; the deployment page offers single-tenant SaaS, BYOC and self-hosting as alternatives but makes no statement on how multi-tenant data is separated. SOC 2 Type II completion is stated (opinion 2026-11-04); the report is gated under NDA and was not read. No cross-tenant incident was found in the vendor's incident record. | 1 | https://developers.llamaindex.ai/llamaparse/general/enterprise-readiness/deployment/ ; https://security.llamaindex.ai/resources (operator input 2026-11-06) |

**Positive findings.** Single-tenant, BYOC (AWS / Azure / GCP) and self-hosted deployment options are documented; the `eval`-based PandasQueryEngine was moved out of the core package behind an explicit deprecation and a source-level warning.

**Recorded concerns.** The framework's published threat model places sandboxing, authentication and input validation entirely outside the project; no tenant-isolation statement for the managed SaaS.

### T — Transparency (6/10, Mid)

| Criterion | Result | Score | Evidence URL |
|---|---|---|---|
| CVE publication posture | Partial. CVEs for the framework are assigned by third-party CNAs (huntr, VulnCheck) from the vendor's huntr bug-bounty program; the vendor publishes a SECURITY.md with scope and a GitHub "Report a vulnerability" channel, but no vendor-authored advisory or vendor-requested CVE was located in the window. | 1 | https://github.com/run-llama/llama_index/blob/main/SECURITY.md ; https://db.gcve.eu/vuln/cve-2025-6208 |
| Incident disclosure speed | ≤30 days. The vendor operates a public status page with an open incident API; 30 incidents were created in the window, each disclosed at creation and carrying a resolved timestamp (same-day disclosure). All 30 are titled as availability or latency incidents; no security incident appears in the vendor's record, and none was located elsewhere. The score records the disclosure speed of the incidents the vendor has published; it does not establish that no security incident occurred. | 2 | https://llamaindex.statuspage.io/api/v2/incidents.json ; https://llamaindex.statuspage.io/history (operator input 2026-11-06) |
| Security policy publication | Detailed. SECURITY.md defines in-scope packages, a threat model, out-of-scope classes and example reports; the hosted docs and trust center state AES-256 at rest, TLS 1.2+ in transit, third-party penetration tests (executive summary and remediation letter gated under NDA), SSO (SAML / OIDC) and a controls list by category. | 2 | https://github.com/run-llama/llama_index/blob/main/SECURITY.md ; https://developers.llamaindex.ai/llamaparse/general/enterprise-readiness/data-privacy-security/index.md ; https://security.llamaindex.ai (operator input 2026-11-06) |
| AI safety framework reference | Internal framework documented (the SECURITY.md threat model). No adoption of an external framework (NIST AI RMF, ISO 42001 or similar) was located. | 1 | https://github.com/run-llama/llama_index/blob/main/SECURITY.md |
| AI system identity disclosure | None located. | 0 | — (source unconfirmed) |

**Positive findings.** The security policy is specific about scope and threat model; incidents are disclosed in real time on a vendor-operated status page with a public API; the 2026-09-21 release resolved dependency security alerts across integration packages ("fix: resolve a ton of security alerts", PR #22855).

**Recorded concerns.** The vendor's advisory output is mediated by third-party CNAs; the status record contains 30 availability incidents in twelve months, including three rated critical by the vendor (2025-11-06, 2026-03-01, 2026-06-03) and one critical login incident (2026-07-16).

## Incident Timeline

Window 2025-11-06 to 2026-11-06. Product scope: run-llama/llama_index packages (PyPI `llama-index-*`) and LlamaCloud.

| Date | ID | CVSS (source) | Description | Patch status | KEV |
|---|---|---|---|---|---|
| 2026-01-12 | CVE-2024-14021 — **retroactive CVE — first disclosed PR #17121 2024-12-02** (excluded from count and maximum) | 7.8 (NVD Primary v3.1; CNA VulnCheck v4.0 8.4) | Unsafe `pickle.load()` in `BGEM3Index.load_from_disk()`; CNA VulnCheck; huntr report ab4ceeb4 linked from the PR. | No fix merged; `pickle.load()` present at commit 444fdf0 (bge-m3 package 0.8.0). | No |
| 2026-01-12 | CVE-2024-58339 (counted) | 7.5 (NVD Primary v3.1; CNA VulnCheck v4.0 8.7) | VannaPack `VannaQueryEngine.custom_query()` executes LLM-generated SQL without execution limits (CWE-770); affects ≤ 0.12.2; CNA VulnCheck. | No fixed version in the CVE record; `llama-index-packs-vanna` last released 2024-11-17; pack not present in repository at 444fdf0. Unconfirmed. | No |
| 2026-02-02 | CVE-2025-6208 (counted) | 5.3 (CNA @huntr_ai v3.0; no NVD Primary — NVD status Deferred) | `SimpleDirectoryReader` applied `num_files_limit` after loading all files (CWE-400); GHSA-488g-hw5f-x29p; PYSEC-2026-1560. | Fixed: commit 53614e2 (PR #18983, 2025-06-05), released v0.12.41 (2025-06-07) — before CVE publication. | No |
| 2026-03-10 / 2026-03-13 | No CVE — vendor fix PR #20857 ("security: add RestrictedUnpickler to SimpleObjectNodeMapping (CWE-502)", llama-index-core 0.14.16); third-party pre-CVE advisory AIKIDO-2026-10351 (affected 0.9.8–0.14.15). | — | Unrestricted `pickle.load()` in `SimpleObjectNodeMapping.from_persist_dir()`. Not counted (no CVE ID). | Fixed in 0.14.16 (2026-03-10). | No |
| 2026-03-27 to 2026-05-12 | No CVE — third-party disclosure NUKA-AI-2026-003 (Project Nuka-AI) | — (discloser self-scored v3.1 10.0; no CNA score) | Claimed path-traversal-to-code-injection in llama-index-core ≤ 0.14.19, reported through huntr (case bb0b2efb). The discloser states the vendor classified the report "N/A" and that commits in v0.14.20 (2026-04-03) and v0.14.21 (2026-04-21) changed the relevant sanitization logic. The vendor's position is known only through the discloser's write-up; no vendor publication on the report was located. Not counted; not adjudicated. | Disputed (per discloser); no advisory. | No |
| 2026-01-12 | MAL-2026-227 (GHSA-675f-h4p7-2vp4) — npm `llamaindex-js` | — | Package flagged as malicious on npm. Not a vendor package (the vendor's npm package is `llamaindex`); not a supply chain compromise of the evaluated target. Recorded for disambiguation. | n/a | No |
| 2026-09-21 | Release v0.14.25 — PR #22855 "fix: resolve a ton of security alerts" | — | Dependency-alert resolution across integration packages; no vendor CVE. | Shipped. | No |
| 2025-11-06 to 2026-09-29 | Vendor status page — 30 availability / latency incidents (all resolved) | — | Vendor-titled, e.g. 2025-11-06 critical "Elevated Job Error Rates"; 2026-03-01 critical "Currently down in EU and NA"; 2026-03-02 major "System Outage"; 2026-06-03 critical "Increased parse latency"; 2026-07-16 critical "Website Login Issues"; 2026-09-17 major "High error rate for agentic parse in EU". None titled as a security incident. Considered under T (incident disclosure speed); not CVE events. | Resolved (vendor timestamps). | n/a |

Pre-window context (not counted): CVE-2025-7707 (2025-10-13), CVE-2025-7647 (2025-09-27), CVE-2025-5302 (2025-08-25), CVE-2025-6211 (2025-07-10), the 2025-07-06/07 batch (CVE-2025-3044, -3046, -3108, -3225, -5472, -6209, -6210), CVE-2025-1793 (2025-06-05, 9.8), CVE-2025-1750 (2025-06-02, 9.8), CVE-2025-1753, CVE-2025-1752, and the 2025-03-20 batch (CVE-2024-11958, -12704, -12909, -12910, -12911). CVE-2025-6211 was re-published by a secondary bulletin on 2026-02-19 (SB2026021917) without changing its 2025-07-10 CVE date.

CVE List status: all three in-window IDs are PUBLISHED; no RESERVED, REJECTED or DISPUTED state applies (Convention-CVEReserved-001).

## Contextual Analysis

Evidence rule for this report: every factual claim was confirmed by web retrieval, PyPI metadata, the cloned repository, or operator-supplied rendered text of public vendor pages (retrieved 2026-11-06, recorded in the Differential section) during the evaluation session; knowledge-based claims were not used.

LlamaIndex is two products under one name, and the data for the two diverge. The framework is MIT-licensed, releases on a visible cadence (eight releases between 2026-03-16 and 2026-09-21; last commit 2026-11-03) and carries a security policy that is more explicit than most in this category about what it will and will not treat as a vulnerability. The hosted LlamaCloud / LlamaParse service is closed source and is where the compliance posture lives, and that posture was rewritten twelve days before this evaluation: Terms of Service and Privacy Notice dated 2026-10-25, a single self-serve DPA for the US and EU instances published 2026-10-26 (public, pre-signed, with EU SCCs and the UK Addendum, incorporated automatically on acceptance of the ToS), a 13-entry sub-processor list that names the cloud and model providers receiving User Content, 48-hour deletion of inputs and outputs, a no-training default with opt-in programs that "apply only if an administrator of your account affirmatively accepts them", and a SOC 2 Type II report whose unqualified opinion was issued 2026-11-04 and is available on request under NDA. Those are stronger and more specific written commitments than the base record captured, and they are the reason the score rises despite an unchanged containment picture.

The CVE picture in this window is quieter than the previous one in severity but not in kind. The 2025 window was dominated by SQL injection through LLM-generated queries (CVE-2025-1793 and CVE-2025-1750, both CVSS 9.8). The 2026 window's two counted CVEs are both resource-exhaustion issues in independent components (VannaPack's query engine; SimpleDirectoryReader), which is why the structural-issues criterion scores 0 again on a different root cause than before. The vendor's SECURITY.md declares "Denial of Service caused by unbounded or malformed user input" out of scope and places input validation, authentication and sandboxing in the hosting application. That position is published and consistent: CVE-2025-6208 was fixed in June 2025 as a memory-behaviour change and only acquired a CVE eight months later, while CVE-2024-58339 has no located fix and its package has not been released since November 2024. Readers should weigh the threat model as written: the library assumes a trusted execution environment, and several of the CVEs assigned by third-party CNAs describe behaviour the vendor's policy says it does not treat as a library vulnerability.

Pickle deserialization recurs across the record without entering the count. CVE-2024-14021 (BGEM3Index) is excluded as retroactive because the issue was publicly described, with a link to the huntr report, in pull request #17121 on 2024-12-02; the pull request is not merged and the `pickle.load()` call remains in the integration package at commit 444fdf0. A separate pickle path (`SimpleObjectNodeMapping.from_persist_dir`) was closed by the vendor in llama-index-core 0.14.16 (2026-03-10) with a `RestrictedUnpickler`, three days before a third-party pre-CVE advisory appeared; no CVE was assigned. The two cases show the same weakness class handled in two ways within one repository: a core component fixed by the vendor without an advisory, and a managed-index integration left as reported.

One third-party disclosure (NUKA-AI-2026-003) alleges a path-traversal issue in llama-index-core and states that the vendor rejected the huntr report as not applicable. The report is recorded as the discloser's position; the vendor's reasoning was not located in any vendor publication, and VERDICT does not adjudicate the dispute.

The hosted service's incident record is public and granular: 30 availability or latency incidents in twelve months on a vendor-operated status page with an open API, each disclosed at creation and closed with a timestamp, including an EU-and-NA outage on 2026-03-01 and a login incident on 2026-07-16. None is titled as a security incident. The T score for disclosure speed records how the vendor discloses the incidents it publishes; it is not evidence that no security incident occurred. Two further points bear on regulated use: the Terms of Service state that no Business Associate Agreement is entered into for self-serve use, so the HIPAA pipeline is an enterprise-contract feature, while the trust center lists "Personal health information" among data the service collects; and Usage Data (logs, metadata, metrics — not User Content) is owned by the vendor and collected without a documented opt-out, with PostHog named as a product-analytics sub-processor.

On the disclosure layer: LlamaIndex, Inc. is independent. Its recorded investors are Greylock (seed, 2023), Norwest Venture Partners (Series A lead, 2025-03-04, with Greylock participating), and Databricks Ventures and KPMG Ventures (minority equity investments announced 2025-05-01, amounts undisclosed, no strategic designation or board seat stated by any party). None is in the material Anthropic equity-holder set, and no Trigger 0–3 fires. Anthropic appears on the sub-processor list as one of several LLM providers to the hosted service; that is a product-integration relationship, recorded separately from the Bias Disclosure. Operator of record: the vendor's Terms of Service and Privacy Notice (2026-10-25) name LlamaIndex, Inc. at 447 Sutter St. Ste. 405 PMB 1259, San Francisco; the base record's operator display string ("Independent · Norwest / Greylock · Series A Mar 2025") is replaced by that legal name. The change of terms and privacy policy confirmed during this evaluation is a T5 condition; its re-check scope is covered by this full re-review, and no published fact has become incorrect in a way that warrants a KNOWN_FACTS.md entry.

## Economic Risk (P dimension)

LlamaCloud bills in credits (10,000 free credits per month on pay-as-you-go). When the balance reaches zero, an organization admin chooses between pausing jobs (API returns 402), automatic reload with a monthly cap set by the customer, or "keep going, bill me for extra usage", which the vendor's billing page states had no cap on the Starter plan and cannot be re-enabled once disabled. Self-hosted deployments offer per-organization and per-project daily or monthly usage caps whose enforcement mode defaults to `off` and which the vendor states "fail open" if the check degrades. No serious issue is recorded: the default behaviours are documented and a hard-stop mode exists; the uncapped overage mode is opt-in. Source: https://developers.llamaindex.ai/llamaparse/general/billing/index.md ; https://developers.llamaindex.ai/llamaparse/self_hosting/configuration/usage-controls/index.md

## VERDICT Record

**Summary.** LlamaIndex scores 44/85 (Tier C) at Layer 0 on 2026-11-06: two framework CVEs in the trailing 12 months (maximum CVSS 7.5, one without a located fix), a published threat model that places input validation and sandboxing outside the library, and a hosted service whose October 2026 terms, public DPA, sub-processor list, no-training default with 48-hour deletion and SOC 2 Type II report (on request under NDA) are documented on the vendor's own pages.

**Risk Factor Summary by Use Case**

| Use case | Observations |
|---|---|
| Internal testing | Framework is MIT-licensed and runs fully local without outbound calls from embedding, reranking or retrieval steps; code-executing engines carry explicit warnings and the core PandasQueryEngine is deprecated behind `llama-index-experimental`. |
| Credential-handling workloads | The framework assumes a trusted execution environment; secrets handling, input validation and privilege boundaries are the hosting application's responsibility per SECURITY.md. LlamaCloud API keys are project-scoped and revocable (eventual consistency up to one minute); SSO via SAML / OIDC is documented. |
| Cloud multi-tenant | Managed SaaS has no published tenant-isolation statement; SOC 2 Type II (Security criteria, opinion 2026-11-04) is available on request under NDA; 30 availability incidents in twelve months are disclosed on the public status page; single-tenant, BYOC and self-hosted options are documented. |
| Regulated-data workloads | Public self-serve DPA with EU SCCs and UK Addendum, EU-Frankfurt instance, Article 27 representative, 48-hour deletion and a no-training default are documented; the sub-processor list is public but undated; no BAA for self-serve use — the HIPAA pipeline and BAA are enterprise-contract features. |

**Reference Information (options, not instructions)**

1. Organizations evaluating LlamaCloud may read the public self-serve DPA and sub-processor list at security.llamaindex.ai, request the SOC 2 Type II report under the standard Mutual NDA, and compare them with the retention and training statements in ToS §4.3–4.5.
2. Deployments of the framework that load persisted indexes from shared or untrusted storage may review the pickle-based `BGEM3Index.load_from_disk()` path, which is unchanged at commit 444fdf0, and the `RestrictedUnpickler` introduced for `SimpleObjectNodeMapping` in llama-index-core 0.14.16.
3. Teams exposing the framework behind a network service may read the vendor's SECURITY.md threat model, which lists the vulnerability classes the project treats as out of scope, when deciding where resource limits and input validation are enforced.

**Bias Disclosure**

> "This evaluation uses Claude (Anthropic) as its tooling. Anthropic operates in the AI agent market and may compete with some evaluated vendors. VERDICT discloses this relationship in every report and applies identical evaluation criteria to all platforms regardless of their relationship to Anthropic."

Product-level integration note: the framework offers Anthropic models as one of many LLM provider integrations (`llama-index-llms-anthropic`), and the hosted service lists Anthropic as one of several LLM-provider sub-processors; these are product-integration choices and not disclosure triggers. Disclosure-layer result: no Trigger 0, 1, 2 or 3 fires; the record carries none of `evaluator-identity`, `direct-investment`, `shared-investor`, `commercial-channel`.

## Future Evaluation Plan

- **Layer 1:** not scheduled. LlamaCloud offers a public free tier (10,000 credits/month) that would permit free-tier behavioural testing under Absolute Rule 2; scheduling is at Operations' discretion.
- **Layer C:** routine re-review 365 days from `updated_at` (2027-11-06, pipeline-derived). Interrupt lane active for T1–T6. Items to watch at the next quarterly sweep: CVE assignment for the SimpleObjectNodeMapping fix, any vendor action on CVE-2024-14021 / PR #17121, the vendor's handling of the VannaPack package, and whether the sub-processor list acquires a published update date.

## Sources

- https://github.com/run-llama/llama_index (clone @ 444fdf0, 2026-11-03: LICENSE, SECURITY.md, CHANGELOG.md, llama-index-core/llama_index/core/query_engine/pandas/pandas_query_engine.py, llama-index-integrations/indices/llama-index-indices-managed-bge-m3/llama_index/indices/managed/bge_m3/base.py; refs/pull/17121/head b419051 2024-12-02; refs/pull/18983/head db03637 2025-06-05; tag v0.12.41 98739a6 2025-06-07)
- https://github.com/run-llama/llama_index/releases
- https://github.com/run-llama/llama_index/pull/17121
- https://github.com/run-llama/llama_index/commit/53614e2f7913c0e86b58add9470b3c900b6c60b2
- https://pypi.org/pypi/llama-index/json ; https://pypi.org/pypi/llama-index-core/json ; https://pypi.org/pypi/llama-index-packs-vanna/json ; https://pypi.org/pypi/llama-index-indices-managed-bge-m3/json ; https://registry.npmjs.org/llamaindex
- https://nvd.nist.gov/vuln/detail/CVE-2024-58339 ; https://cvefeed.io/vuln/detail/CVE-2024-58339 ; https://www.vulncheck.com/advisories/llamaindex-vannaqueryengine-sql-execution-allows-resource-exhaustion ; https://api.osv.dev/v1/vulns/PYSEC-2026-86
- https://www.vulncheck.com/advisories/llamaindex-bgem3index-unsafe-deserialization ; https://db.gcve.eu/vuln/fkie_cve-2024-14021 ; https://osv.dev/vulnerability/PYSEC-2026-85
- https://db.gcve.eu/vuln/cve-2025-6208 ; https://osv.dev/vulnerability/PYSEC-2026-1560
- https://newreleases.io/project/pypi/llama-index-core/release/0.14.16 ; https://intel.aikido.dev/cve/AIKIDO-2026-10351 ; https://www.netzilo.com/threats/llamaindex-pickle-deserialization
- https://nuka-ai.github.io/posts/2026-05-12-Llamaindex-SelfNuke-disclosure/
- https://osv.dev/vulnerability/MAL-2026-227
- https://app.opencve.io/cve/?vendor=run-llama ; https://www.cvelogic.com/vendor/llamaindex ; https://corgea.com/advisories/packages/pypi/llama-index ; https://www.cybersecurity-help.cz/vdb/SB2026021917
- https://www.llamaindex.ai/legal/terms-of-service ; https://www.llamaindex.ai/legal/privacy-notice (operator-supplied rendered text, 2026-11-06)
- https://security.llamaindex.ai ; https://security.llamaindex.ai/subprocessors ; https://security.llamaindex.ai/resources (operator-supplied rendered text, 2026-11-06)
- https://llamaindex.statuspage.io/ ; https://llamaindex.statuspage.io/history ; https://llamaindex.statuspage.io/api/v2/incidents.json (operator-supplied rendered text, 2026-11-06)
- https://mcp.llamaindex.ai/terms-of-service ; https://crossposter.llamaindex.ai/privacy-policy (2024 subdomain copies read in session; superseded for the hosted service by the 2026-10-25 main-site versions)
- https://developers.llamaindex.ai/llamaparse/general/enterprise-readiness/ ; …/compliance/index.md ; …/data-privacy-security/index.md ; …/eu-compliance/ ; …/deployment/ ; …/access-identity/ ; https://developers.llamaindex.ai/llamaparse/general/status/ ; https://developers.llamaindex.ai/llamaparse/general/api_key/index.md ; https://developers.llamaindex.ai/llamaparse/self_hosting/configuration/user-roles/index.md ; https://developers.llamaindex.ai/llamaparse/general/billing/index.md ; https://developers.llamaindex.ai/llamaparse/self_hosting/configuration/usage-controls/index.md
- https://developers.llamaindex.ai/python/framework/understanding/privacy ; https://developers.llamaindex.ai/python/llamaagents/workflows/human_in_the_loop/index.md ; https://developers.llamaindex.ai/python/workflows/managing_events
- https://www.llamaindex.ai/blog/announcing-our-series-a-and-llamacloud-general-availability ; https://www.norwest.com/blog/llamaindex-harnesses-the-power-of-enterprise-data-for-ai-agent-workflows/ ; https://www.llamaindex.ai/blog/llamaindex-welcomes-investments-from-databricks-and-kpmg ; https://databricks.com/blog/databricks-invests-llamaindex-advance-knowledge-agents-over-enterprise-data ; https://www.hpcwire.com/aiwire/2025/05/02/llamaindex-announces-investments-from-databricks-and-kpmg-llp/
- Operator input 2026-11-06: CISA KEV JSON (catalogVersion 2026.11.04; substring and per-ID checks); sweep 2026-10-27 rows (none).
