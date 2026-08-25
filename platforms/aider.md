---
name: aider
slug: aider
operator: Aider AI LLC
independence: independent
parent_entity: null
category: AI Coding Agent
homepage: https://aider.chat
github: https://github.com/Aider-AI/aider
evaluation_number: 57
evaluation_type: initial
evaluated_at: '2026-04-21'
evaluator_model: claude-opus-4-7
framework_version: v0.3.1-final
layer: '0'
target_version: aider-chat 0.86.2
previous_evaluation_date: null
previous_score: null
score: 52
max_score: 85
tier: B
verdict:
  v:
    score: 14
    rating: High
    note: ''
  r:
    score: 17
    rating: High
    note: ''
  d:
    score: 5
    rating: Low
    note: ''
  i:
    score: 8
    rating: High
    note: ''
  c:
    score: 5
    rating: Mid
    note: ''
  t:
    score: 3
    rating: Low
    note: ''
  e:
    score: null
    rating: null
    note: null
cisa_kev:
  present: false
  entries: []
cve_count_12mo: 0
cve_count_basis: exact
max_cvss_12mo: null
supply_chain_compromise_12mo: false
known_facts_applied: []
qa:
  factual: pass
  legal: pass
  quality: pass
  revision_cycles: 0
  flagged: false
differential: null
next_review_due: '2026-07-20'
tags:
- open-source
- apache-2.0
- ai-coding-agent
- terminal-cli
- byok
- python
- local-only
rank: 22
finding: Apache 2.0 open-source terminal coding agent. Zero CVEs in trailing 12 months
  across NVD, OSV, GitHub Security Advisories, Safety DB. Dependency pinning (litellm==1.75.0
  in v0.85.3) structurally blocked the March 2026 TeamPCP litellm 1.82.7/1.82.8 supply-chain
  compromise from reaching pip-install users. Local-only, BYOK architecture — no aider-operated
  server holds user code. HITL approval default. No SECURITY.md / SOC 2 / ISO 27001
  / DPA published.
meta_owner: Aider AI LLC · United States · aider-chat 0.86.2
meta_description: 'Independent security evaluation of aider by Aider AI LLC. Score:
  52/85. Apache 2.0 OSS terminal coding agent. Zero CVEs in 12 months. litellm pinning
  blocked March 2026 supply-chain compromise. Local-only, BYOK. Framework v0.3.1.'
og_description: 'Independent security evaluation of aider by Aider AI LLC. Score:
  52/85. Apache 2.0 OSS terminal coding agent. Zero CVEs. Local-only BYOK. Framework
  v0.3.1.'
category_line: AI Coding Agent · Terminal CLI · Open Source (Apache 2.0)
display_tags:
- text: 0 CVEs · 12 Months
  color: safe
- text: litellm Pinning · Supply-Chain Protected
  color: safe
- text: Local-Only · BYOK
  color: safe
- text: No SECURITY.md · No SOC 2
  color: amber
sources:
- https://aider.chat/
- https://aider.chat/docs/
- https://aider.chat/HISTORY.html
- https://aider.chat/docs/legal/privacy.html
- https://aider.chat/docs/faq.html
- https://aider.chat/docs/more/analytics.html
- https://aider.chat/docs/troubleshooting/imports.html
- https://aider.chat/docs/scripting.html
- https://aider.chat/docs/usage/commands.html
- https://aider.chat/docs/usage/modes.html
- https://aider.chat/docs/usage/tips.html
- https://aider.chat/docs/config/options.html
- https://aider.chat/docs/git.html#commit-attribution
- https://github.com/Aider-AI/aider
- https://github.com/Aider-AI/aider/blob/main/LICENSE.txt
- https://github.com/Aider-AI/aider/releases
- https://github.com/Aider-AI/aider/issues
- https://github.com/Aider-AI/aider/issues/3520
- https://github.com/Aider-AI/aider/security/advisories
- https://github.com/Aider-AI/aider/security/policy
- https://docs.litellm.ai/blog/security-update-march-2026
key_finding: "Apache 2.0 OSS terminal coding agent. Zero CVEs in 12 months across NVD/OSV/GHSA. litellm pinning structurally blocked the March 2026 TeamPCP supply-chain compromise from reaching pip-install users. Local-only, BYOK. No SECURITY.md / SOC 2 attestation."
card_owner: "Aider AI LLC"
card_category: "AI Coding Agent · Terminal CLI · Open Source (Apache 2.0)"
card_tags:
  - text: "0 CVEs · 12 Months"
    color: safe
  - text: "litellm Pinning · Supply-Chain Protected"
    color: safe
  - text: "No SECURITY.md · No SOC 2"
    color: amber
---

# aider

## Executive Summary

aider is an Apache 2.0 open-source terminal coding agent operated by Aider AI LLC. No public CVEs were confirmed against aider in the trailing 12 months across NVD, OSV, GitHub Security Advisories, or CISA KEV. Version pinning of the litellm dependency (aider v0.85.3 pinned litellm==1.75.0, well before the March 2026 TeamPCP compromise of litellm 1.82.7/1.82.8) structurally protected pip-install users from the most prominent AI-ecosystem supply-chain incident of the evaluation window. The architecture (local execution, no cloud backend, user-provided API keys) reduces data-exposure surface, but formal security documentation is minimal: no SECURITY.md, no published advisories, no SOC report, and no formal incident disclosure policy. Telemetry is opt-in and anonymous with a documented disable flag. Layer 0 total: 52/85.

## Scorecard

| Dimension | Score | Max | Rating |
|---|---:|---:|---|
| V — Verifiability       | 14 | 20 | High (70%) |
| R — Resilience          | 17 | 20 | High (85%) |
| D — Data Conduct        |  5 | 15 | Low (33%)  |
| I — Identity & Control  |  8 | 10 | High (80%) |
| C — Containment         |  5 | 10 | Mid (50%)  |
| T — Transparency        |  3 | 10 | Low (30%)  |
| **Total (Layer 0)**     | **52** | **85** | — |

**CISA KEV:** None. No aider-related CVE found in the KEV catalog as of evaluation date.

E (Effectiveness) — not evaluated (Layer 1+ only).

Category: OSS AI Coding Agent / Local Terminal / CLI.

---

## Dimension Detail

### V — Verifiability (14/20)

| Criterion | Result | Score | Evidence |
|---|---|---:|---|
| Developer / company identity | Aider AI LLC confirmed; contact privacy@aider.chat published | 4/4 | https://aider.chat/docs/legal/privacy.html ; https://aider.chat/docs/faq.html#what-is-aider-ai-llc |
| Source code disclosure | Full OSS under Apache 2.0 on GitHub | 4/4 | https://github.com/Aider-AI/aider/blob/main/LICENSE.txt |
| Version management transparency | Full release notes + HISTORY per version | 3/3 | https://aider.chat/HISTORY.html ; https://github.com/Aider-AI/aider/releases |
| Third-party dependency disclosure | requirements.in public on GitHub; analytics sub-processor (PostHog) named; no formal sub-processor list with dated update | 1/3 | https://aider.chat/docs/more/analytics.html ; https://aider.chat/docs/troubleshooting/imports.html |
| Independent certification | No SOC 2 / SOC 3 / ISO 27001 report published for Aider AI LLC | 0/4 | Not found on aider.chat, GitHub, or search results |
| Functional reproducibility docs | Complete user documentation, config reference, scripting docs, source-level tags | 2/2 | https://aider.chat/docs/ ; https://aider.chat/docs/scripting.html |

**Positive findings:** Full Apache 2.0 source on GitHub, detailed HISTORY.html release log, corporate operator publicly named with working contact email.

**Recorded concerns:** No independent certification; no single consolidated sub-processor / dependency-as-of-date registry.

### R — Resilience (17/20)

| Criterion | Result | Score | Evidence |
|---|---|---:|---|
| CVE count (trailing 12 months) | Zero CVEs found across NVD, OSV, GitHub Security Advisories, Safety DB | 5/5 | https://github.com/Aider-AI/aider/security/advisories (none published) ; https://data.safetycli.com/packages/pypi/aider-chat/ |
| Maximum CVSS severity | No CVEs → no maximum to record | 6/6 | Same as above |
| Patch response speed | Unconfirmable (no CVE-triggered patch cycles to measure); scored 0 per rubric | 0/3 | Rule 3: items unconfirmable from public sources score 0 |
| Structural issues | No recurring CVE root causes (because no CVEs); issue tracker shows isolated independent bugs | 3/3 | https://github.com/Aider-AI/aider/issues |
| Supply chain compromise (trailing 12 months) | aider v0.85.3 pinned litellm==1.75.0; March 2026 litellm 1.82.7/1.82.8 compromise did not reach pinned installs | 3/3 | https://aider.chat/HISTORY.html (v0.85.3 notes); https://docs.litellm.ai/blog/security-update-march-2026 |

**Positive findings:** Dependency pinning policy documented ("Aider pins its dependencies and is tested to work with those specific versions"); the pinned litellm version (1.75.0) predates the TeamPCP compromise by several minor releases; zero confirmed aider CVEs in the trailing 12 months.

**Recorded concerns:** Patch-response speed cannot be measured in the absence of CVEs; dependency-bump cadence is visible in HISTORY but not tied to a formal SLA.

### D — Data Conduct (5/15)

| Criterion | Result | Score | Evidence |
|---|---|---:|---|
| GDPR compliance disclosure | Privacy policy mentions international transfers and EU users; no DPA standard provision; no explicit GDPR compliance statement | 1/3 | https://aider.chat/docs/legal/privacy.html (International Visitors section) |
| Data minimization | Analytics opt-in by default; `--analytics-disable` permanent opt-out documented | 3/3 | https://aider.chat/docs/more/analytics.html |
| AI training use | Privacy policy states no code/chat/keys/personal info collection, but does not explicitly state analytics data is excluded from AI training, and no retention period stated | 0/4 | https://aider.chat/docs/legal/privacy.html |
| Sub-processor transparency | PostHog named as analytics processor in documentation, but no formal list with dated update | 1/3 | https://aider.chat/docs/more/analytics.html |
| Data retention disclosure | Privacy policy does not state per-category retention windows | 0/2 | https://aider.chat/docs/legal/privacy.html |

**Positive findings:** Opt-in analytics model with anonymous UUID4 identifier; `aider --analytics-log` lets users inspect exactly what is collected; analytics source code points documented and linkable.

**Recorded concerns:** No DPA, no retention windows, no explicit statement that analytics data is excluded from AI/model training. Note that aider itself does not train models — the user's LLM provider choice governs training behavior — but the aider analytics stream still lacks an explicit non-training clause.

### I — Identity & Control (8/10)

| Criterion | Result | Score | Evidence |
|---|---|---:|---|
| Emergency stop documentation | Ctrl-C / Ctrl-D exit documented; `/undo` for git reversal; per-edit confirmation by default; no formal "emergency stop" procedure section | 2/4 | https://aider.chat/HISTORY.html (Ctrl-Z, Ctrl-D handling); https://aider.chat/docs/usage/commands.html |
| Human-in-the-loop design | Per-edit confirmation and per-shell-command confirmation enabled by default; `--yes-always` is an opt-in override | 3/3 | https://aider.chat/docs/config/options.html |
| Permission delegation transparency | File-scope controls (`.aiderignore`, `--subtree-only`), read-only file support, edit vs ask vs architect modes documented | 3/3 | https://aider.chat/docs/faq.html ; https://aider.chat/docs/usage/modes.html |

**Positive findings:** Interactive confirmation is the default for both file edits and shell commands; `/undo` is a first-class user command; scoping via `.aiderignore` and `--subtree-only` is publicly documented.

**Recorded concerns:** No dedicated "emergency stop / mid-action interruption" section in the documentation; GUI mode historically bound to 0.0.0.0 (Issue #3520, Mar 2025, still marked stale) — users on shared networks should review the bind address.

### C — Containment (5/10)

| Criterion | Result | Score | Evidence |
|---|---|---:|---|
| Sandbox design | No sandbox; runs in user's Python environment. `.aiderignore` provides blocklist-style file-scope control | 1/4 | https://aider.chat/docs/faq.html (large repo / .aiderignore sections) |
| Least privilege | Runs with the invoking user's OS privileges; scope configurable via `.aiderignore` and `--subtree-only` | 1/3 | https://aider.chat/docs/usage/tips.html |
| Tenant isolation (cloud) | Self-hosted / local-only architecture; no multi-tenant cloud surface | 3/3 (N/A) | Architecture confirmed on aider.chat and GitHub |

**Positive findings:** Local-only execution eliminates the multi-tenant cloud attack surface entirely; no aider-operated server holds user code or chats.

**Recorded concerns:** Shell execution (`/run`), web scraping (`/web`), and file writes occur with full user privileges; users running aider as a privileged account inherit that privilege into the agent.

### T — Transparency (3/10)

| Criterion | Result | Score | Evidence |
|---|---|---:|---|
| CVE publication posture | No CVEs issued; GitHub Security Advisories empty; public issue tracker contains security-labeled issues (e.g., #3520) | 1/2 | https://github.com/Aider-AI/aider/security/advisories ; https://github.com/Aider-AI/aider/issues/3520 |
| Incident disclosure speed | No formal incident disclosure policy or published incident history | 0/2 | No dedicated page found |
| Security policy publication | GitHub reports "No security policy detected" (SECURITY.md absent) | 0/2 | https://github.com/Aider-AI/aider/security/policy |
| AI safety framework reference | No reference to NIST AI RMF, ISO/IEC 42001, or an internal AI safety framework found | 0/2 | Not found on aider.chat or GitHub |
| AI system identity disclosure | Commit messages carry "aider:" / co-authored-by attribution by default; git author "(aider)" by default | 2/2 | https://aider.chat/docs/git.html#commit-attribution ; HISTORY v0.85.0 co-authored-by default |

**Positive findings:** AI identity is visible in commit authorship by default, aiding downstream provenance; public issue tracker accepts and preserves security reports.

**Recorded concerns:** Absence of SECURITY.md, advisory channel, coordinated-disclosure policy, and AI safety framework reference. For a tool at 42K+ GitHub stars and 5.7M+ PyPI installs, formalized security-disclosure infrastructure would be proportionate to the install base.

---

## Incident Timeline

Trailing 12 months: 2025-04-21 → 2026-04-21.

No public CVEs were confirmed against aider during this window.

Adjacent dependency event (context, not an aider CVE):

| Date | Event | Severity | aider impact | Source |
|---|---|---|---|---|
| 2026-03-24 | litellm 1.82.7 / 1.82.8 published to PyPI with credential-stealing payload (TeamPCP campaign) | Critical (supply chain) | Not confirmed to reach aider users: aider pins litellm (v0.85.3 pinned litellm==1.75.0; earlier versions pinned other safe releases). PyPI yanked 1.82.7/1.82.8 ~3 hours after publication. | https://docs.litellm.ai/blog/security-update-march-2026 ; https://snyk.io/blog/poisoned-security-scanner-backdooring-litellm/ |

---

## Contextual Analysis

aider's architectural posture is materially different from Cursor, Windsurf, and GitHub Copilot: no cloud backend, no vendor-side code ingestion, no sub-processor chain beyond the user-selected LLM provider. This collapses several threat-model dimensions (tenant isolation, vendor data retention, cloud-side breach exposure) down to the user's own workstation and their LLM provider relationship.

Operator note: Earlier public references to aider as maintained by "Paul Gauthier (individual maintainer)" reflect the project's earlier paul-gauthier/aider repository. Current public evidence (FAQ, privacy policy dated April 2025) names Aider AI LLC as the corporate operator, with the code repository at Aider-AI/aider. This evaluation uses the current operator of record.

On the resilience side, aider's dependency-pinning discipline — explicitly documented in the Dependency versions page — converted the March 2026 litellm supply-chain incident from an active exposure into a structural non-event for pip-install users. Users who upgrade litellm independently outside aider's pinned range lose this protection, and the Dependency versions page explicitly cautions against such upgrades.

On the transparency side, the absence of SECURITY.md, a coordinated-disclosure policy, and a formal advisory channel is notable for a project with 5.7M+ PyPI downloads. Security-relevant issues such as #3520 (GUI bind scope, March 2025) remain open with a "stale" label; reporters without a documented disclosure path may default to the public issue tracker, which is publicly scrapable.

The GUI feature warrants specific review for any user running aider on a shared network, per issue #3520.

### Economic Risk Note

No significant hidden-cost or autonomous-runaway issue identified at Layer 0. Relevant positive factors:

- All LLM API calls originate from user-held keys against user-held accounts; aider does not broker billing.
- aider displays token counts and cost estimates; `/tokens` command available.
- `--stream` + `--cache-prompts` combination triggers a startup warning about potential cost-estimate inaccuracy (HISTORY v0.86 line).
- Auto-commit attribution and shell-command confirmations provide natural friction against runaway loops.

---

## VERDICT Record

**Summary:** aider scores 52/85 at Layer 0 — a B-tier OSS AI coding agent with strong resilience and human-in-the-loop design, offset by limited formal security-transparency artifacts and a privacy policy that lacks GDPR/DPA and retention specificity.

**Risk Factor Summary by Use Case:**

| Use case | Risk factor | Notes |
|---|---|---|
| Internal testing / individual developer | Low | Local execution, opt-in analytics, default per-edit confirmation suit individual use. |
| Credential-handling workloads | Medium | API keys sit in user environment; `/run` executes with user privileges; users should isolate keys per-project. |
| Cloud multi-tenant workloads | N/A | aider is local-only by architecture; no multi-tenant surface to score. |
| Regulated-data workloads (HIPAA / PCI / GDPR-strict) | High | No SOC 2, no DPA, no retention windows published; regulated-data users should evaluate their downstream LLM provider separately and consider disabling analytics. |

**Reference Information (options, not directives):**

- Users on shared networks or who plan to use the GUI mode may wish to verify the GUI bind address (see issue #3520) before exposing the process.
- Organizations pinning aider-chat to a specific version should also pin litellm to the version aider's requirements.in specifies, and avoid independent litellm upgrades inside aider's virtualenv.
- Regulated-data teams may prefer aider-install / uv / pipx isolated installs so that aider's pinned dependency set is not overridden by other project dependencies.

**Bias Disclosure:**

> This evaluation uses Claude (Anthropic) as its tooling. Anthropic operates in the AI agent market and may compete with some evaluated vendors. VERDICT discloses this relationship in every report and applies identical evaluation criteria to all platforms regardless of their relationship to Anthropic.

---

## Future Evaluation Plan

- **Layer 1 (free-tier behavioral testing):** Feasible — aider's free tier is the Apache 2.0 binary with user-provided API keys. Recommended if E-dimension behavioral data (task success rate, cost accuracy, performance degradation) is needed. 30 runs × 4 difficulty levels across 3+ days per framework.
- **Layer C (continuous monitoring):** Monitor NVD / OSV / GitHub Security Advisories for "aider" and "aider-chat"; monitor litellm advisories given the direct dependency; monitor CISA KEV. Re-evaluation trigger on any CVSS 7.0+ aider CVE, any KEV listing, or 90-day routine check.
- **Routine next review:** 2026-07-20 (90 days from this evaluation) or on any qualifying R-dimension trigger, whichever is earlier.

---

## Japanese Summary

```japanese-summary
# aider 評価結果サマリー

## 基本情報
- スコア: 52/85 (Layer 0)
- ランク: AI Coding Agent クラスタの B tier、CVE clean な resilience profile を持つ唯一のクラスタ内ツール
- 評価日: 2026.04.21
- 対象バージョン: aider-chat 0.86.2
- 運営: Aider AI LLC (米国 / 公開連絡先 privacy@aider.chat)
- 独立性: ✅ Independent

## 次元スコア
- V (検証可能性): 14/20
- R (耐性): 17/20
- D (データ運用): 5/15
- I (制御): 8/10
- C (封じ込め): 5/10
- T (透明性): 3/10

## 主要ポジティブ所見
- 直近12ヶ月で公開 CVE ゼロ (NVD / OSV / GHSA / CISA KEV / Safety DB すべて該当なし)
- litellm 1.75.0 pinning により 2026-03 の TeamPCP litellm 1.82.7/1.82.8 改ざんが pip-install ユーザに到達せず、構造的に防御
- ローカル実行のみ、クラウドバックエンドなし、user-provided API keys モデル
- HITL (per-edit / per-shell-command 確認) がデフォルト動作、`--yes-always` は opt-in override
- Apache 2.0 完全 OSS、運営法人 Aider AI LLC 公開、commit に aider 著者属性 default

## 主要リスク所見
- SECURITY.md なし、coordinated-disclosure policy なし、SOC 2 / ISO 27001 等の独立認証なし
- Privacy policy に retention windows の specificity なし、analytics データの AI training 除外明記なし、DPA 不在
- サンドボックスなし。`/run` `/web` 等は user OS privileges full で実行
- GUI mode が 0.0.0.0 にバインド (Issue #3520, 2025-03 から stale) — 共有ネットワーク利用時は要確認

## インシデント
- aider に帰属する CVE: 直近12ヶ月ゼロ
- 隣接事象 (context only): litellm 1.82.7/1.82.8 改ざん (2026-03-24, TeamPCP) は aider pinning により被害到達せず、PyPI が約3時間で yanked

## CISA KEV
- 該当なし

## 同クラスタ位置づけ
- AI Coding Agent クラスタ内で最もクリーンな CVE history (R=17/20) を持つ。Containment と Transparency は Cline (#058, 50/85) や OpenHands (#035, 43/85) と同程度の中位水準。Cline と比較すると、aider は CVE history 面で大幅に上回るが、SECURITY.md・SLA 不在の transparency gap が逆転している。

## HTMLカード用タグ
- tags: open-source, apache-2.0, ai-coding-agent, terminal-cli, byok, python, local-only
- incident_tags: litellm-supply-chain-2026-03-adjacent
- owner: Aider AI LLC
```