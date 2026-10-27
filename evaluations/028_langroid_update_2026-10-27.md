# VERDICT Evaluation Report — #028 Langroid (Update)

| Field | Value |
|---|---|
| Evaluation number | #028 |
| Platform | Langroid |
| Evaluation type | Update (Differential Evaluation) |
| Date | 2026-10-27 |
| Evaluator | VERDICT engine · evaluator model `claude-fable-5` |
| Target version | Langroid 0.69.x (0.69.16 examined, released 2026-10-25; `langroid` PyPI package; github.com/langroid/langroid) |
| Framework | VERDICT v0.3.2 |
| Previous evaluation | 2026-03-31 · 34/85 · Tier D · framework v0.3.1 (migrated capture) |
| Trigger | T1 (interrupt lane) — published advisory set diverges from recorded R facts; quarterly sweep dry run 2026-10-27 |

---

## Executive Summary

Langroid's trailing-12-month public CVE record moved from the 1 CVE / max CVSS 9.4 captured in March 2026 to 8 CVEs with a maximum CVSS of 10.0 (CVE-2026-54769, CNA v3.1), and for every one of the eight a fixed release was on PyPI at or before the advisory's publication. The total score moves from 34/85 to 45/85 (+11, Tier D → Tier B); because the movement exceeds 5 points, the moving dimensions and evidence are: V 10→14 (single-license MIT source tree, complete dependency manifest and lockfile, API reference verified), I 2→8 (interactive-by-default task loop, documented termination controls and tool/delegation scoping), C 3→8 (AST-allowlist pandas sandbox plus restrictive defaults verified in source; self-hosted N/A isolation), T 8→6 (two disclosures published more than 30 days after their fix releases; vulnerability-handling scope narrowed on 2026-07-23), D 6→3 (no privacy policy, DPA, training-use or retention statement located; absence scored as zero), and R 5→6 (count and maximum-severity criteria fall to 0 on the new CVE set, while patch response and the absence of a compromise of Langroid's own package remain confirmed). Three of the eight CVEs continue a single root cause in `TableChatAgent`'s pandas `eval()` path and three others share the `SQLChatAgent` query-blocklist mechanism, so the structural-issues criterion remains 0. No Langroid CVE appears in the CISA KEV catalog.

---

## Scorecard

| Dimension | Score | Max | Rating |
|---|---|---|---|
| V — Verifiability | 14 | 20 | High |
| R — Resilience | 6 | 20 | Low |
| D — Data Conduct | 3 | 15 | Low |
| I — Identity & Control | 8 | 10 | High |
| C — Containment | 8 | 10 | High |
| T — Transparency | 6 | 10 | Mid |
| E — Effectiveness | not evaluated (Layer 1+) | 15 | — |
| **Total (Layer 0)** | **45** | **85** | — |

Tier: B
Category: Multi-Agent LLM Framework · OSS (MIT)

CISA KEV: none — no Langroid CVE appears in the CISA Known Exploited Vulnerabilities catalog (checked 2026-10-27; the CISA-ADP container on CVE-2026-54769 carries SSVC enrichment with Exploitation: poc and no KEV data).

---

## Differential

**Previous evaluation:** 2026-03-31, 34/85 (Tier D, framework v0.3.1, migrated capture).
**This update:** interrupt lane, trigger T1 (published advisory set diverges from recorded R facts: recorded `cve_count_12mo: 1`, `max_cvss_12mo: 9.4`; sweep observed a larger advisory set with max CVSS 10.0). The evaluation prompt also recorded the routine R/T/V re-check as folded into this update; the point is moot because the full re-evaluation set subsumes it.

**Per-dimension state** (checked 2026-10-27):

| Dimension | State | Basis |
|---|---|---|
| V | re-evaluated | migrated capture, no per-dimension sources |
| E | null (Layer 1+ only) | — |
| R | re-evaluated | migrated capture, no per-dimension sources; T1 mandatory scope |
| D | re-evaluated | migrated capture, no per-dimension sources |
| I | re-evaluated | migrated capture, no per-dimension sources |
| C | re-evaluated | migrated capture, no per-dimension sources |
| T | re-evaluated | migrated capture, no per-dimension sources |

Carry-forward checks: none performed — the base record is a migrated capture without per-dimension source URLs, so carry-forward conditions 1–4 cannot be positively satisfied for any dimension (convention 2026-09-22). Carrying forward is a positive finding that cited evidence is unchanged, never an inference from the absence of news.

**Score-change rule:** total moved by 11 points (≥5); the moving dimensions and evidence are named in the Executive Summary. The R-only escalation rule does not apply (this is already a full re-review).

**Evaluation History**

| Date | Type | Score | Tier | Framework |
|---|---|---|---|---|
| 2026-03-31 | Initial (migrated capture) | 34/85 | D | v0.3.1 |
| 2026-10-27 | Update (T1 interrupt, full re-evaluation) | 45/85 | B | v0.3.2 |

---

## Dimension Detail

### V — Verifiability · 14/20 · High

| Criterion | Result | Score | Evidence |
|---|---|---|---|
| Developer / company identity | No legal entity is named on any vendor page; no registry record exists to query. Official contact confirmed: `pchalasani@gmail.com` is published in the README and in the PyPI package metadata, and SECURITY.md publishes a private reporting channel. | 2/4 | https://github.com/langroid/langroid (README, SECURITY.md); https://pypi.org/project/langroid |
| Source code disclosure | Full OSS. The entire repository is published under a single MIT license ("Copyright (c) 2023 langroid"); no enterprise-licensed directories and no hosted control plane are sold for the product. License relied on: MIT (whole tree). | 4/4 | https://github.com/langroid/langroid (LICENSE; `find -iname "*license*"` returns one file) |
| Version management transparency | GitHub releases carry detailed notes (e.g. 0.69.13 documents a lockfile-only dependency sync with alert numbers and verification steps); a `release-notes/` directory and 585 PyPI releases provide a complete version record. | 3/3 | https://github.com/langroid/langroid/releases/tag/0.69.13 ; https://pypi.org/project/langroid |
| Third-party dependency disclosure | Library context: the complete runtime dependency manifest is published in `pyproject.toml` (optional extras included) and the full pinned tree in `uv.lock`; update dates are recorded per release (0.69.13 release note, 2026-10-20). No sub-processors exist for a self-hosted library; the dependency manifest is the applicable third-party disclosure. | 3/3 | https://github.com/langroid/langroid (pyproject.toml, uv.lock); https://github.com/langroid/langroid/releases/tag/0.69.13 |
| Independent certification | No SOC 2, SOC 3 or equivalent report located. Not confirmed → 0. | 0/4 | source unconfirmed (no certification published) |
| Functional reproducibility docs | Complete auto-generated API reference (mkdocs `reference/` section) plus behavioral documentation (e.g. `docs/notes/task-termination.md`, `docs/notes/code-injection-protection.md`) and machine-readable `llms.txt` exports. | 2/2 | https://langroid.github.io/langroid ; https://github.com/langroid/langroid (mkdocs.yml line 176; docs/notes/) |

**Positive findings:** single-license MIT tree with no commercial layer; unusually detailed, security-relevant release notes; complete dependency lockfile maintained and documented.
**Recorded concerns:** no legal entity stands behind the project; no independent certification; identity rests on an individual maintainer's published contact.

### R — Resilience · 6/20 · Low

CVE window: 2025-10-27 → 2026-10-27 (trailing 12 months from the update date). Attribution bound to the `langroid` PyPI package / github.com/langroid/langroid per `target_version` (Attribution-CVE-001). Window entry by first public disclosure date (Attribution-CVE-002): for all eight CVEs below, the earliest public disclosure is the maintainer-published GitHub advisory; MITRE/NVD publication followed. Score source order applied: no NVD-provided CVSS exists for any of the eight (verified for CVE-2026-25481 and CVE-2026-54769; NVD assessment not provided), so CNA (GitHub) v3.1 is used where present, else CNA v4.0, with the version stated per entry. Every recorded score was recomputed from its vector; no stated-vs-computed discrepancy was found.

| Criterion | Result | Score | Evidence |
|---|---|---|---|
| CVE count (trailing 12 months) | 8 CVEs (basis: exact): CVE-2026-25481, -25879, -50180, -50181, -54760, -54769, -54771, -55615. Band 6–9 → 1; CVSS 9.0+ exists → −1 penalty (min 0). | 0/5 | GitHub Advisory Database records (URLs in Incident Timeline); https://nvd.nist.gov/vuln/detail/CVE-2026-25481 |
| Maximum CVSS severity | 10.0 — CVE-2026-54769, CNA (GitHub) CVSS v3.1 `AV:N/AC:L/PR:N/UI:N/S:C/C:H/I:H/A:H` (computed 10.0, matches stated). 9.0+ → 0. | 0/6 | https://cveawg.mitre.org/api/cve/CVE-2026-54769 ; https://github.com/langroid/langroid/security/advisories/GHSA-q9p7-wqxg-mrhc |
| Patch response speed | For all 8 CVEs the fixed release was on PyPI at or before advisory publication: 0.59.32 (2026-02-01) vs advisory 2026-02-02; 0.63.0 (2026-05-27) same-day; 0.64.0 (2026-05-28), 0.65.1–0.65.3 (2026-06-09), 0.65.5 (2026-06-15) all preceded the 2026-07-02/06 advisories. Disclosure-to-patch elapsed time ≤ 0 days → ≤7d. | 3/3 | https://pypi.org/project/langroid (release dates); advisory publication dates in Incident Timeline |
| Structural issues | Recurring root causes. `TableChatAgent` pandas `eval()`: CVE-2025-46724 (pre-window) → fix bypass CVE-2026-25481 → incomplete-mitigation escape CVE-2026-54769. `SQLChatAgent` `_validate_query` blocklist: CVE-2026-25879 → CVE-2026-54760 (quoted/schema-qualified bypass) → CVE-2026-50180 (`pg_read_file` family missed); the CVE-2026-55615 advisory itself describes the Neo4j issue as "mirroring the SQLChatAgent bug fixed in CVE-2026-25879." | 0/3 | Advisory texts at the GHSA URLs in the Incident Timeline |
| Supply chain compromise (trailing 12 months) | None for Langroid's own package, account or build pipeline. Step-3a searches found no compromise of the `langroid` PyPI package. A direct optional dependency, `litellm`, was compromised on PyPI (incident report 2026-04-02); per Attribution-CVE-001 a dependency compromise is recorded in the Incident Timeline, not here. | 3/3 | https://blog.pypi.org/posts/2026-04-02-incident-report-litellm-telnyx-supply-chain-attack/ ; https://pypi.org/project/langroid |

**Positive findings:** maintainer-published advisories with fixes available at disclosure across all eight CVEs; no compromise of Langroid's own distribution; active dependency hygiene (lockfile syncs documented in release notes).
**Recorded concerns:** eight CVEs in twelve months with a 10.0 maximum; two multi-CVE root-cause chains in the code- and query-execution paths; the SECURITY.md policy of 2026-07-23 classifies new SQL/Cypher/AQL denylist bypasses as out of scope for advisories and CVEs, so future issues of the recurring class may not surface in this metric (see Contextual Analysis).

### D — Data Conduct · 3/15 · Low

| Criterion | Result | Score | Evidence |
|---|---|---|---|
| GDPR compliance disclosure | None located — no privacy policy, DPA or GDPR statement exists for the library or any hosted component (none is operated). Silence is data → 0. | 0/3 | https://github.com/langroid/langroid ; https://langroid.github.io/langroid (no privacy documents) |
| Data minimization | No telemetry found in the source tree (no analytics endpoints, no phone-home code); the one telemetry reference disables a dependency's telemetry (`litellm.telemetry = False`, `langroid/language_models/openai_gpt.py` line 410). No telemetry ≙ telemetry default OFF. | 3/3 | https://github.com/langroid/langroid (source grep; openai_gpt.py) |
| AI training use | No statement on training use of user data. → 0. | 0/4 | source unconfirmed (no statement published) |
| Sub-processor transparency | No sub-processor list (no service is operated). → 0 under the criterion as written. | 0/3 | source unconfirmed (none published) |
| Data retention disclosure | No retention statement. → 0. | 0/2 | source unconfirmed (none published) |

**Positive findings:** the library collects nothing — no telemetry code exists, and a dependency's telemetry is explicitly switched off.
**Recorded concerns:** the entire data-governance artifact set (privacy policy, DPA, training-use statement, retention terms) is absent; deployers inherit the full obligation set with no vendor paper to rely on.

### I — Identity & Control · 8/10 · High

| Criterion | Result | Score | Evidence |
|---|---|---|---|
| Emergency stop documentation | Termination is documented in depth (`docs/notes/task-termination.md`: done sequences, `done_if_tool`, turn and iteration limits) and interactive runs let only the user quit the root task (`only_user_quits_root`, task.py). A dedicated emergency-stop procedure for non-interactive runs is not documented → documented but incomplete. | 2/4 | https://github.com/langroid/langroid (docs/notes/task-termination.md; langroid/agent/task.py lines 221, 278) |
| Human-in-the-loop design | Enabled by default: `Task(..., interactive: bool = True)` waits for human input after each non-human step. | 3/3 | https://github.com/langroid/langroid (langroid/agent/task.py line 221) |
| Permission delegation transparency | Tool scope per agent is explicit (`enable_message(message_class, use=..., handle=...)`), and delegation targets are documented (`add_sub_task` in docs/quick-start/multi-agent-task-delegation.md); SECURITY.md names "tool dispatch and the agent/tool trust boundary, message routing, sender verification" as in-scope core controls. | 3/3 | https://github.com/langroid/langroid (chat_agent.py line 929; docs/quick-start/multi-agent-task-delegation.md; SECURITY.md) |

**Positive findings:** human-in-the-loop is the default, not an option; termination semantics have dedicated documentation.
**Recorded concerns:** CVE-2026-54771 showed the tool-scoping gate (`use=False, handle=True`) was bypassable by raw JSON until 0.65.3; no kill-switch procedure for long-running non-interactive tasks.

### C — Containment · 8/10 · High

| Criterion | Result | Score | Evidence |
|---|---|---|---|
| Sandbox design | Hybrid. The pandas `eval()` path uses explicit allowlists (AST nodes, methods, operators, variables, builtins) plus restricted `__builtins__` (`safe_eval_globals()`); the SQL/Cypher/AQL paths use denylists (`_DANGEROUS_SQL_PATTERNS`, `validate_cypher_query()`); SECURITY.md states both and classifies them as best-effort hardening, pointing to the database role, container/VM and egress rules as the actual boundaries. | 2/4 | https://github.com/langroid/langroid (SECURITY.md; docs/notes/code-injection-protection.md) |
| Least privilege | Restrictive defaults verified in source: `full_eval: bool = False` (table_chat_agent.py line 133; vector_store/base.py line 95) and `allow_dangerous_operations: bool = False` (sql_chat_agent.py line 344); SECURITY.md instructs a least-privilege, read-only database role and a credential-free container. | 3/3 | https://github.com/langroid/langroid (source lines cited; SECURITY.md "Deploying these agents safely") |
| Tenant isolation (cloud) | Self-hosted only — Langroid is a library; no hosted multi-tenant service is operated. N/A → 3 per rubric. | 3/3 | https://github.com/langroid/langroid ; https://pypi.org/project/langroid |

**Positive findings:** the project documents its own containment limits candidly and designs defaults closed (`full_eval=False`, `allow_dangerous_operations=False`).
**Recorded concerns:** the window's CVE set repeatedly demonstrated the blocklist layers' incompleteness (CVE-2026-54760, -50180, -25481, -54769); containment in production rests on deployer-side boundaries, exactly as SECURITY.md states.

### T — Transparency · 6/10 · Mid

| Criterion | Result | Score | Evidence |
|---|---|---|---|
| CVE publication posture | Issues CVEs and advisories: all eight window CVEs were published as maintainer-authored GitHub repository advisories with GitHub as CNA. | 2/2 | GHSA URLs in the Incident Timeline |
| Incident disclosure speed | Mixed, with confirmed >30d cases: fix-to-advisory gaps were 1 day (CVE-2026-25481), same-day (CVE-2026-25879), 21–27 days (CVE-2026-54760/-54769/-54771/-55615), and 35 days (CVE-2026-50180/-50181: fixed in 0.64.0 on 2026-05-28, advisories 2026-07-02). Slowest confirmed gap falls in the 31–60d band. | 1/2 | https://pypi.org/project/langroid (release dates); advisory dates in Incident Timeline |
| Security policy publication | Detailed: SECURITY.md (rewritten 2026-07-23, corrected 2026-10-07) states a threat model, names which mechanisms are and are not security boundaries, gives deployment hardening steps, a private reporting channel, a 7-day acknowledgment aim, and explicit in-scope / out-of-scope categories. | 2/2 | https://github.com/langroid/langroid (SECURITY.md; commits 85e03f4, e2ae0cc, c7a0a72) |
| AI safety framework reference | No external framework (NIST AI RMF etc.) adopted; an internal threat model and protection design are documented. | 1/2 | https://github.com/langroid/langroid (SECURITY.md; docs/notes/code-injection-protection.md) |
| AI system identity disclosure | No end-user AI identity disclosure feature exists in the framework. | 0/2 | source unconfirmed (no such feature documented) |

**Positive findings:** the maintainer requests CVEs for his own project's flaws and publishes the advisories himself; the current security policy is unusually explicit about what its mitigations do not guarantee.
**Recorded concerns:** two advisory pairs were published 35 days after their fixes shipped; the 2026-07-23 policy closes new denylist-bypass reports "without a fix, an advisory, or a CVE request," which, by its own terms, removes advisories and CVEs as the public signal for that class (recorded as fact; the policy document gives its reasoning).

---

## Incident Timeline

All dates are first public disclosure (maintainer-published GitHub advisory). CVSS source: CNA (GitHub); version stated per row; NVD assessment not provided for these CVEs (verified for CVE-2026-25481 and CVE-2026-54769). Computed scores match stated scores for all rows.

| Date | CVE ID | CVSS | Description | Patch status | KEV |
|---|---|---|---|---|---|
| 2026-02-02 | CVE-2026-25481 (GHSA-x34r-63hx-w57f) | 9.4 (v4.0) | WAF bypass leading to RCE in `TableChatAgent` — bypass of the CVE-2025-46724 fix in `pandas_utils.py` | Fixed 0.59.32 (2026-02-01, before disclosure) | — |
| 2026-05-27 | CVE-2026-25879 (GHSA-mxfr-6hcw-j9rq) | 9.8 (v3.1) | Prompt-to-SQL injection leading to RCE via `SQLChatAgent` | Fixed 0.63.0 (2026-05-27, same day) | — |
| 2026-07-02 | CVE-2026-50180 (GHSA-pmch-g965-grmr) | 8.7 (v4.0) | `SQLChatAgent` `_validate_query` blocklist misses `pg_read_file` family → arbitrary file read | Fixed 0.64.0 (2026-05-28, 35d before disclosure) | — |
| 2026-07-02 | CVE-2026-50181 (GHSA-fg23-3346-88f5) | 7.1 (v3.1) | Path traversal in `ReadFileTool`/`WriteFileTool` beyond configured `curr_dir` | Fixed 0.64.0 (2026-05-28, 35d before disclosure) | — |
| 2026-07-06 | CVE-2026-54760 (GHSA-6xc5-4r68-67fc) | 9.3 (v4.0) | `SQLChatAgent` blocklist bypass via quoted / schema-qualified function names | Fixed 0.65.1 (2026-06-09, 27d before disclosure) | — |
| 2026-07-06 | CVE-2026-54769 (GHSA-q9p7-wqxg-mrhc) | 10.0 (v3.1) | Sandbox escape to RCE via incomplete `eval()` mitigation in `TableChatAgent` | Fixed 0.65.2 (2026-06-09, 27d before disclosure) | — |
| 2026-07-06 | CVE-2026-54771 (GHSA-gjgq-w2m6-wr5q) | 8.1 (v3.1) | `handle_message()` executes user-supplied tool JSON without sender verification (bypasses `use=False` gate) | Fixed 0.65.3 (2026-06-09, 27d before disclosure) | — |
| 2026-07-06 | CVE-2026-55615 (GHSA-2pq5-3q89-j7cc) | 9.2 (v4.0) | `Neo4jChatAgent` executes LLM-generated Cypher without validation (prompt-to-Cypher injection; config-conditional RCE) | Fixed 0.65.5 (2026-06-15, 21d before disclosure) | — |
| 2026-04-02 | dependency: BerriAI/litellm — PyPI supply chain compromise (with telnyx) | — | Malicious `litellm` releases published via stolen tokens, quarantined within ~2.5 hours; `litellm` is an optional extra of langroid (`langroid[litellm]`, `[all]`), not a default-install dependency. Not counted in the three R fields per Attribution-CVE-001. | Malicious releases removed by PyPI; litellm adopted Trusted Publishers | — |

Advisory record URLs: [GHSA-x34r-63hx-w57f](https://github.com/langroid/langroid/security/advisories/GHSA-x34r-63hx-w57f) · [GHSA-mxfr-6hcw-j9rq](https://github.com/langroid/langroid/security/advisories/GHSA-mxfr-6hcw-j9rq) · [GHSA-pmch-g965-grmr](https://github.com/langroid/langroid/security/advisories/GHSA-pmch-g965-grmr) · [GHSA-fg23-3346-88f5](https://github.com/langroid/langroid/security/advisories/GHSA-fg23-3346-88f5) · [GHSA-6xc5-4r68-67fc](https://github.com/langroid/langroid/security/advisories/GHSA-6xc5-4r68-67fc) · [GHSA-q9p7-wqxg-mrhc](https://github.com/langroid/langroid/security/advisories/GHSA-q9p7-wqxg-mrhc) · [GHSA-gjgq-w2m6-wr5q](https://github.com/langroid/langroid/security/advisories/GHSA-gjgq-w2m6-wr5q) · [GHSA-2pq5-3q89-j7cc](https://github.com/langroid/langroid/security/advisories/GHSA-2pq5-3q89-j7cc); publication dates and vectors per the GitHub Advisory Database records (github.com/github/advisory-database) and PyPA advisory database (github.com/pypa/advisory-database, vulns/langroid/).

Pre-window context (not counted): CVE-2025-46724 (9.8, v3.1), CVE-2025-46725 (8.1, v4.0) and CVE-2025-46726 (7.8, v4.0) were disclosed 2025-05-05/20, before the window start, and form the first links of the recurring chains assessed under R structural issues.

---

## Contextual Analysis

The window's defining fact is volume with consistent handling. Eight CVEs were published against Langroid between February and July 2026 — all through the maintainer's own GitHub advisories, all with a fixed release already on PyPI at publication, two of them (CVE-2026-25481, CVE-2026-25879) within a day of the fix. The 10.0-scored CVE-2026-54769 carries CISA-ADP SSVC enrichment of Exploitation: poc; no Langroid CVE appears in the KEV catalog. The evidence rule applied: every claim in this report is restricted to public sources retrieved during the evaluation session.

Two root-cause chains account for six of the eight. The `TableChatAgent` pandas-`eval()` path produced CVE-2025-46724, its fix bypass CVE-2026-25481, and the mitigation escape CVE-2026-54769; the `SQLChatAgent` query-validation blocklist produced CVE-2026-25879, CVE-2026-54760 and CVE-2026-50180, and the CVE-2026-55615 advisory describes the Neo4j path as mirroring the SQL one. The project's own position on this class is now explicit: the SECURITY.md rewritten on 2026-07-23 (corrected 2026-10-07) states that executing model-generated code and queries "is the feature," classifies the sanitizers and denylists as "best-effort hardening, not security boundaries," names the database credential, the container/VM and egress rules as the actual boundaries, and declares new denylist bypasses out of scope for fixes, advisories and CVE requests, while keeping missing-gate defects and allowlist misclassifications in scope. This is a documented threat-model position with a direct measurement consequence: under the published policy, findings of the recurring denylist-bypass class no longer produce advisories or CVEs, so the public CVE record stops carrying that class. VERDICT records the policy and its date; readers weigh it.

Two recorded facts from the base evaluation are corrected here. First, the operator line `Prasad Chalasani (CMU) · Individual` is not supported by the vendor's own pages as a current-affiliation statement: no legal entity is named anywhere (LICENSE: "Copyright (c) 2023 langroid"; PyPI author: Prasad Chalasani), and the README presents the project as "from CMU and UW-Madison researchers," listing Prasad Chalasani (IIT BTech/CS, CMU PhD/ML; Independent ML Consultant) and Somesh Jha (Professor of CS, U Wisconsin–Madison). Per OperatorOfRecord-001 the record now carries the name under which the product is published — the `langroid` GitHub organization, maintainer Prasad Chalasani — and states that no legal entity is named. Second, the recorded "48-hour response commitment" reflected the pre-2026-07-23 SECURITY.md ("usually within 48 hours"); the current policy aims to acknowledge in-scope reports within 7 days. Both are single corrected cases for this entity and remain in this Contextual Analysis per the KNOWN_FACTS intake rule; no KNOWN_FACTS entry is staged.

The sweep row that fired this update reported 15 published repository advisories in the window with max CVSS 10.0. The maximum is confirmed. The advisory count verifiable from the public structured record — the GitHub Advisory Database (github-reviewed) and the PyPA advisory database — is 8 in-window entries, all CVE-bearing; a third-party scan archive from October 2026 refers to "16 published advisories" on the repository in total ([ai-patchlab scan #102 notes](https://github.com/elfrost/ai-patchlab/pull/142)), which suggests additional repository-level advisories (for example CVE-less ones) that could not be individually enumerated from structured public sources in this session. The discrepancy does not affect `cve_count_12mo`, which counts CVEs only (Attribution-CVE-001) and is exact at 8; the sweep's six NVD-keyword candidates correspond to the six July-window CVEs and are all product-scoped to Langroid. The 2026-04-02 litellm PyPI compromise is recorded as a dependency event: `litellm` is an optional extra, not a default-install dependency, and Langroid's own package, maintainer account and build pipeline show no compromise; the repository's release notes document ongoing lockfile maintenance (0.69.13, 2026-10-20).

On verifiability and control, the picture is stronger than the base capture recorded: the tree is single-license MIT with no commercial layer, releases are documented in detail, the task loop is interactive by default, the gated execution modes default off (`full_eval=False`, `allow_dangerous_operations=False`, verified in source), and the pandas path uses an AST allowlist rather than a blocklist. On data conduct the public record is simply empty — no privacy policy, DPA, training-use or retention statement exists — which the framework scores as zero while noting that the library itself contains no telemetry and disables a dependency's. No Langroid entry was located in the MIT AI Agent Index during this session. No publicly recorded equity investor, parent entity, or non-arms-length channel with a material Anthropic equity-holder was found; disclosure Triggers 0–3 do not fire, and the record carries no trigger tags.

---

## VERDICT Record

**Summary:** Langroid scores 45/85 (Tier B): a transparent, MIT-licensed multi-agent framework whose maintainer ships fixes before disclosing, set against eight CVEs in twelve months (max CVSS 10.0) concentrated in two recurring code/query-execution root causes and an absent data-governance artifact set.

**Risk Factor Summary by Use Case**

| Use case | Risk factors shown by the data |
|---|---|
| Internal testing | Restrictive defaults (`full_eval=False`, `allow_dangerous_operations=False`) and container guidance apply; the window's CVE set shows that untrusted text reaching the model can translate into query/code execution, so even test deployments isolate credentials and data per SECURITY.md. |
| Credential-handling workloads | CVE-2026-54769 (10.0, PoC per CISA-ADP SSVC) and the file-read CVEs (CVE-2026-50180/-50181) demonstrated paths from model output to host files; SECURITY.md directs running "with no credentials, secrets, or data you are unwilling to expose to the LLM." |
| Cloud multi-tenant deployment | N/A as a vendor property — no hosted service is operated; isolation is entirely the deployer's (container/VM, least-privilege database role, egress rules per SECURITY.md). |
| Regulated-data workloads | No compliance artifacts exist (no SOC 2, no DPA, no privacy policy, no retention terms); the data shows no vendor-side compliance posture, so the deployer carries the full control and documentation burden. |

**Reference Information** (options, not instructions)

1. Deployers exposing the query/code-executing agents to untrusted input can review SECURITY.md's deployment section (least-privilege read-only database role, credential-free container/VM, egress restrictions).
2. Pinning `langroid >= 0.65.5` covers the fixes for all eight window CVEs; `>= 0.69.13` additionally carries the October 2026 dependency lockfile maintenance.
3. Organizations that relied on advisory feeds for the denylist-bypass class can note the 2026-07-23 scope policy and, if that signal matters to them, watch changes to `langroid/utils/pandas_utils.py` and `langroid/agent/special/sql/sql_chat_agent.py` directly.

**Bias Disclosure**

> "This evaluation uses Claude (Anthropic) as its tooling. Anthropic operates in the AI agent market and may compete with some evaluated vendors. VERDICT discloses this relationship in every report and applies identical evaluation criteria to all platforms regardless of their relationship to Anthropic."

---

## Future Evaluation Plan

- **Layer 1 (behavioral testing):** not scheduled; free-tier behavioral testing of a self-hosted library requires a ratified runner configuration (30 runs × 4 difficulty levels across 3+ days) and is deferred to a future batch.
- **Layer C:** interrupt lane active (T1–T6); routine review due 365 days from this update's `updated_at` (pipeline-derived). The 2026-07-23 out-of-scope policy makes commit-level monitoring of the eval/SQL paths a useful sweep supplement, since under that policy new denylist-bypass findings do not produce advisories or CVEs.
- **Dormancy:** not applicable — the target is active (0.69.16 released 2026-10-25).
