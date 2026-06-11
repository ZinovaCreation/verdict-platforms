---
name: Cline
slug: cline
operator: Cline Bot, Inc.
independence: independent
parent_entity: null
category: AI Coding Agent
homepage: https://cline.bot
github: https://github.com/cline/cline
evaluation_number: 58
evaluation_type: initial
evaluated_at: '2026-04-27'
evaluator_model: claude-opus-4-7
framework_version: v0.3.1-final
layer: '0'
target_version: v3.79.0
previous_evaluation_date: null
previous_score: null
score: 50
max_score: 85
tier: B
verdict:
  v:
    score: 14
    rating: High
    note: ''
  r:
    score: 5
    rating: Low
    note: ''
  d:
    score: 8
    rating: Mid
    note: ''
  i:
    score: 10
    rating: High
    note: ''
  c:
    score: 6
    rating: Mid
    note: ''
  t:
    score: 7
    rating: High
    note: ''
  e:
    score: null
    rating: null
    note: null
cisa_kev:
  present: false
  entries: []
cve_count_12mo: 0
max_cvss_12mo: null
supply_chain_compromise_12mo: true
known_facts_applied: []
qa:
  factual: pass
  legal: pass
  quality: pass
  revision_cycles: 0
  flagged: false
differential: null
next_review_due: '2026-07-26'
tags:
- open-source
- vscode-extension
- jetbrains
- byok
- hitl
- apache-2.0
- ai-coding-agent
rank: 10
finding: 'OSS VS Code / JetBrains AI coding agent with HITL approval default — 10/10
  on Identity & Control. BYOK keeps prompts and code off Cline servers. Apache 2.0,
  signed GitHub releases, named US C-corp operator. Mindgard disclosed 4 prompt-injection
  / RCE flaws (Aug 2025, partial mitigation v3.35.0). "Clinejection" supply-chain
  attack: GitHub Actions cache poisoning → unauthorized npm publish, contained in
  ~8h with OIDC provenance migration (Feb 2026). No SOC 2 / ISO 27001 attestation.
  Host-level execution with full user privileges.'
meta_owner: Cline Bot, Inc. · Founder Saoud Rizwan · $32M Seed+Series A · v3.79.0
meta_description: 'Independent security evaluation of Cline by Cline Bot, Inc. Score:
  50/85. OSS VS Code/JetBrains AI coding agent. HITL default (10/10). Apache 2.0.
  Mindgard disclosures + Clinejection supply-chain incident (contained ~8h, OIDC migration).
  Framework v0.3.1.'
og_description: 'Independent security evaluation of Cline by Cline Bot, Inc. Score:
  50/85. OSS VS Code/JetBrains agent. HITL default. Mindgard + Clinejection findings.
  Framework v0.3.1.'
category_line: AI Coding Agent · IDE Extension · Open Source (Apache 2.0)
display_tags:
- text: HITL Default · I:10/10
  color: safe
- text: BYOK · Apache 2.0
  color: safe
- text: Mindgard 4 Disclosures · Aug 2025
  color: amber
- text: Clinejection Supply-Chain · Feb 2026
  color: red
sources:
- https://cline.bot/privacy
- https://cline.bot/tos
- https://cline.bot/enterprise
- https://cline.bot/mcp-marketplace
- https://cline.bot/blog/introducing-anonymous-telemetry-in-cline
- https://docs.cline.bot
- https://docs.cline.bot/more-info/telemetry
- https://docs.cline.bot/enterprise-solutions/security-concerns
- https://github.com/cline/cline
- https://github.com/cline/cline/security
- https://github.com/cline/cline/releases
- https://github.com/cline/cline/security/advisories/GHSA-9ppg-jx86-fqw7
- https://github.com/cline/cline/discussions/411
- https://github.com/cline/cline/pull/9211
- https://raw.githubusercontent.com/cline/cline/refs/heads/main/CHANGELOG.md
---

# Cline

## Executive Summary

Cline scores **50/85 (Mid)** on Layer 0. The platform's strengths concentrate in identity & control (HITL approval default, plan/act mode, clear emergency-stop UX) and verifiability (Apache 2.0 source code, signed GitHub releases, named US C-corp operator with $32M funding documented). The platform's recorded concerns concentrate in resilience: an independent security researcher disclosed four prompt-injection / API-key-exfiltration / RCE flaws in August 2025 (Mindgard) with vendor acknowledgment occurring after public pressure in October, and a supply-chain compromise of the Cline CLI npm package occurred on 2026-02-17 (GHSA-9ppg-jx86-fqw7), traceable to a prompt-injection vulnerability in a Claude-powered GitHub Actions issue-triage workflow ("Clinejection"). No CISA KEV entries are associated with Cline. No SOC 2 or equivalent independent attestation is publicly available.

## Scorecard

| Dimension | Score | Max | % | Rating |
|---|---:|---:|---:|---|
| V — Verifiability       | 14 | 20 |  70% | High |
| R — Resilience          |  5 | 20 |  25% | Low  |
| D — Data Conduct        |  8 | 15 |  53% | Mid  |
| I — Identity & Control  | 10 | 10 | 100% | High |
| C — Containment         |  6 | 10 |  60% | Mid  |
| T — Transparency        |  7 | 10 |  70% | High |
| **Total (Layer 0)**     | **50** | **85** | **58.8%** | **Mid** |

**CISA KEV:** None. No Cline-attributed CVE present in the CISA Known Exploited Vulnerabilities catalog as of evaluation date.

E (Effectiveness) — not evaluated (Layer 1+ only).

---

## Dimension Detail

### V — Verifiability (14/20)

| Criterion | Result | Score | Evidence |
|---|---|---:|---|
| Developer / company identity | Cline Bot, Inc. confirmed; security@cline.bot + support@cline.bot published | 4/4 | https://cline.bot/privacy ; https://www.crunchbase.com/organization/cline-4914 ; https://github.com/cline/cline/security |
| Source code disclosure | Full OSS, Apache 2.0 | 4/4 | https://github.com/cline/cline |
| Version management transparency | GitHub Releases + CHANGELOG.md, signed tags | 3/3 | https://github.com/cline/cline/releases ; https://raw.githubusercontent.com/cline/cline/refs/heads/main/CHANGELOG.md |
| Third-party dependency disclosure | package.json publicly visible; no formal sub-processor list with update date | 1/3 | https://github.com/cline/cline (repo) |
| Independent certification | No publicly available SOC 2 / ISO 27001 / HIPAA / PCI DSS attestation | 0/4 | Comparison source: https://www.augmentcode.com/tools/github-copilot-vs-cline ; cline.bot does not publish a trust portal / compliance page |
| Functional reproducibility docs | Full docs site at docs.cline.bot + open-source reference implementation | 2/2 | https://docs.cline.bot |

**Positive findings:** Operator legal entity is publicly named in the Privacy Notice ("Cline Bot Inc."), GitHub releases are signed with a verified GPG key (B5690EEEBB952194), and the codebase is fully open under a permissive license, allowing independent audit.

**Recorded concerns:** No third-party attestation (SOC 2, ISO 27001, HIPAA, PCI DSS) is publicly available; enterprise procurement teams cannot rely on independent compliance verification at the platform level. No formal sub-processor list with last-updated date is published.

### R — Resilience (5/20)

| Criterion | Result | Score | Evidence |
|---|---|---:|---|
| Disclosed vuln count (trailing 12 months: 2025-04-27 → 2026-04-27) | ~5 publicly disclosed flaws (4 Mindgard + 1 Cline GHSA); no NVD CVE assignments verified | 2/5 | https://mindgard.ai/blog/cline-coding-agent-vulnerabilities ; https://github.com/cline/cline/security/advisories/GHSA-9ppg-jx86-fqw7 |
| | Third-party security research (Mindgard). The corresponding vendor advisory GHSA-3c6h-5gc7-73gj is private as of this evaluation; no NVD/CVE assigned. Facts publicly acknowledged by the vendor. | | |
| Maximum severity | Mindgard self-classifies findings as critical (RCE, API-key exfil); no formal CVSS published | 2/6 | https://mindgard.ai/blog/cline-coding-agent-vulnerabilities ; https://hackread.com/cline-bot-ai-agent-vulnerable-data-theft-code-execution/ |
| | Third-party security research (Mindgard). The corresponding vendor advisory GHSA-3c6h-5gc7-73gj is private as of this evaluation; no NVD/CVE assigned. Facts publicly acknowledged by the vendor. | | |
| Patch response speed | Mindgard disclosed 2025-08-22; partial mitigation in v3.35.0 (~2025-10-31), >60d. Clinejection: privately reported 2026-01-01; public disclosure 2026-02-09; PR #9211 fix ~30 min after public disclosure | 0/3 | https://adnanthekhan.com/posts/clinejection/ ; https://mindgard.ai/blog/cline-coding-agent-vulnerabilities |
| | Third-party security research (Mindgard). The corresponding vendor advisory GHSA-3c6h-5gc7-73gj is private as of this evaluation; no NVD/CVE assigned. Facts publicly acknowledged by the vendor. | | |
| Structural issues | Recurring root cause: prompt-injection boundary failures in agentic contexts (host machine via .clinerules; CI/CD via issue-triage workflow) | 0/3 | https://snyk.io/blog/cline-supply-chain-attack-prompt-injection-github-actions/ |
| Supply chain compromise (trailing 12 months) | Confirmed: unauthorized cline@2.3.0 npm publish 2026-02-17, ~8h live; 2.4.0 published as remediation; tokens revoked; OIDC provenance adopted | 1/3 | https://github.com/cline/cline/security/advisories/GHSA-9ppg-jx86-fqw7 ; https://safedep.io/cline-cli-compromised/ |

**Positive findings:** The 2026-02-17 unauthorized npm publish was contained within ~8 hours; the team revoked the compromised token, published a corrected version (2.4.0), deprecated the malicious version, and adopted GitHub Actions OIDC provenance for npm publishing. The injected payload installed a separate non-malicious package (`openclaw`) globally; the CLI binary itself (`dist/cli.mjs`) was byte-identical to the prior legitimate release, limiting direct execution-time damage.

**Recorded concerns:** Mindgard's vendor-response timeline records public acknowledgment occurring after public pressure rather than at initial private disclosure. The Clinejection root cause — granting an LLM-driven workflow broad CI/CD permissions over an attacker-reachable trigger surface — was a recurring instance of the same prompt-injection-in-agentic-context pattern Mindgard had flagged six months earlier.

### D — Data Conduct (8/15)

| Criterion | Result | Score | Evidence |
|---|---|---:|---|
| GDPR compliance disclosure | Privacy Notice references rights but no published DPA standard provision / explicit Article 28 statement | 1/3 | https://cline.bot/privacy |
| Data minimization (telemetry) | Anonymous telemetry via PostHog; explicit Allow/Deny prompt at install ("Help Improve Cline"); respects VS Code global telemetry setting | 3/3 | https://docs.cline.bot/more-info/telemetry ; https://cline.bot/blog/introducing-anonymous-telemetry-in-cline |
| AI training use | Cline itself does not train on user content; BYOK architecture keeps prompts/code with user-chosen LLM provider; no explicit retention period stated by Cline | 2/4 | https://github.com/cline/cline/discussions/411 ; https://cline.bot/tos (Section 3 — User Content transmission to AI Model Providers) |
| Sub-processor transparency | Stripe, Google Analytics, AI Model Providers mentioned in Privacy Notice; no consolidated list with update date | 1/3 | https://cline.bot/privacy |
| Data retention disclosure | Cookie consent stored 12 months; no per-category retention statement | 1/2 | https://cline.bot/privacy |

**Positive findings:** Telemetry follows an explicit-consent prompt rather than silent default-on; the documented telemetry scope excludes prompt content, code, and conversation contents. The BYOK (bring-your-own-key) architecture means user code and prompts can flow directly from the local extension to the user-selected LLM provider without traversing Cline-operated infrastructure.

**Recorded concerns:** No consolidated sub-processor list with a last-updated date is published. The Privacy Notice transfers the AI-training-opt-out responsibility to the underlying AI Model Provider rather than offering Cline-level guarantees, which can complicate downstream compliance reviews.

### I — Identity & Control (10/10)

| Criterion | Result | Score | Evidence |
|---|---|---:|---|
| Emergency stop documentation | Per-action approval gate; cancel button in UI; extension can be disabled instantly | 4/4 | https://github.com/cline/cline (README HITL section) |
| Human-in-the-loop design | HITL is the default execution mode; auto-approve is opt-in per command class | 3/3 | https://github.com/cline/cline ; https://www.latent.space/p/cline |
| Permission delegation transparency | MCP server scopes documented; auto-approve patterns user-configurable; .clinerules behavior documented | 3/3 | https://docs.cline.bot ; https://cline.bot/mcp-marketplace |

**Positive findings:** HITL approval is structurally central to Cline's published design philosophy and is the default state at install. The plan/act mode separation gives users an explicit review surface before file modifications or shell execution.

**Recorded concerns:** None at the dimension level. (Implementation gaps in how HITL was bypassed via .clinerules / safe-command lists are recorded under R — Resilience.)

### C — Containment (6/10)

| Criterion | Result | Score | Evidence |
|---|---|---:|---|
| Sandbox design | HITL approval gating is whitelist-style (default deny commands), but no process-level isolation; commands run with full user privileges on the host | 2/4 | https://github.com/cline/cline ; https://docs.cline.bot/enterprise-solutions/security-concerns |
| Least privilege | Configurable auto-approve patterns; default state requires per-action approval; executed commands inherit user privileges | 1/3 | https://github.com/cline/cline |
| Tenant isolation | Self-hosted client-side architecture (extension on user machine); cloud-tenancy N/A for code-execution path | 3/3 (N/A) | https://docs.cline.bot/enterprise-solutions/security-concerns ; https://cline.bot/enterprise |

**Positive findings:** The client-side architecture means user code and prompts do not traverse Cline-operated cloud infrastructure for the core agent execution path; this materially reduces cross-tenant exposure compared to platforms that route prompts through a vendor cloud.

**Recorded concerns:** Cline has no Docker / container / VM isolation comparable to #035 OpenHands. Approved commands execute on the host with full user-account privileges, and the .clinerules configuration mechanism documented by Mindgard provided a path to override the per-command approval gate, illustrating that the authorization model lacks isolation as a defense-in-depth layer.

### T — Transparency (7/10)

| Criterion | Result | Score | Evidence |
|---|---|---:|---|
| CVE / advisory publication posture | GitHub Security Advisories published (GHSA-9ppg-jx86-fqw7); SECURITY.md with reporting channel and SLA | 2/2 | https://github.com/cline/cline/security |
| Incident disclosure speed | Mixed: Mindgard >60d; Clinejection ~40d (private→public); 2026-02-17 unauthorized publish disclosed within hours | 1/2 | https://mindgard.ai/blog/cline-coding-agent-vulnerabilities ; https://adnanthekhan.com/posts/clinejection/ |
| | Third-party security research (Mindgard). The corresponding vendor advisory GHSA-3c6h-5gc7-73gj is private as of this evaluation; no NVD/CVE assigned. Facts publicly acknowledged by the vendor. | | |
| Security policy publication | SECURITY.md present; 48h ack target, 30d fix target; Security Concerns docs page describes architecture | 2/2 | https://github.com/cline/cline/security ; https://docs.cline.bot/enterprise-solutions/security-concerns |
| AI safety framework reference | No public reference to NIST AI RMF / OWASP LLM Top 10 / MITRE ATLAS as adopted external framework | 0/2 | Cline public docs |
| AI system identity disclosure | Agent operation is plainly visible in IDE UI; plan/act mode and tool-use blocks are surfaced in chat | 2/2 | https://github.com/cline/cline |

**Positive findings:** Security advisories are published on the canonical GitHub repository with publicly accessible details, a reporting channel (security@cline.bot), and stated SLA targets. The agent's operation is explicitly visible to the user (no hidden background actions).

**Recorded concerns:** No external AI safety / risk-management framework is publicly cited as adopted. Vendor-response timing for the Mindgard cluster of disclosures fell outside the 60-day window before public acknowledgment.

---

## Incident Timeline

Trailing 12 months: 2025-04-27 → 2026-04-27.

| Date | Identifier | Severity | Description | Status | KEV |
|---|---|---|---|---|---|
| 2025-08-22 → 2025-08-24 | Mindgard #1–4 (no CVE assigned) | Critical (researcher self-assessment; RCE / API-key exfil / safety-rule bypass / model-info leakage) | Prompt-injection chain via source-file analysis; ping (whitelisted as "safe") used for DNS-based exfil; .clinerules override of `requires_approval`; TOCTOU race Third-party security research (Mindgard). The corresponding vendor advisory GHSA-3c6h-5gc7-73gj is private as of this evaluation; no NVD/CVE assigned. Facts publicly acknowledged by the vendor. | Partial mitigation v3.35.0 (~2025-10-31); researcher notes mitigation depth not fully verified | No |
| 2026-01-01 | Clinejection (GHSA submitted) | High (chained: prompt injection → Actions cache poisoning → publication-token theft) | Issue-triage Claude Action with broad permissions reachable by any GitHub-account holder via crafted issue title | Public disclosure 2026-02-09; fix PR #9211 ~30 min after public disclosure (removes AI workflows; nightly jobs no longer consume Actions cache) | No |
| 2026-02-17 | GHSA-9ppg-jx86-fqw7 | Supply-chain compromise (unauthorized npm publish using stolen token) | `cline@2.3.0` published with added `postinstall` (`npm install -g openclaw@latest`); CLI binary unmodified; live ~8 hours | Remediated: `cline@2.4.0` published; 2.3.0 deprecated; tokens revoked; OIDC provenance adopted; VS Code Marketplace + OpenVSX + JetBrains plugin unaffected | No |

---

## Contextual Analysis

Cline occupies a distinctive position in the AI Coding Agent / IDE Extension category: a fully open-source, BYOK-architected agent embedded in VS Code (and JetBrains, and a CLI), with explicit HITL gating as the central safety mechanism rather than container-level isolation. Adoption is substantial (the cline.bot site cites 5M+ installs across VS Code Marketplace and OpenVSX as of mid-2025; the Series A announcement cites 2.7M; enterprise customer logos on cline.bot/enterprise include Samsung, Salesforce, Visa, IBM, and others).

The architectural divergence from the comparative anchors is consequential. #035 OpenHands runs the agent inside a Docker sandbox; #022 Replit has CSA-Star containment; #011 GitHub Copilot ships with the broadest certification portfolio in the cluster. Cline ships with none of these and instead relies on per-action user approval as its primary safety boundary. This design choice is internally consistent with the platform's stated preference for transparency and direct user control, and the BYOK architecture meaningfully reduces vendor-cloud data-handling exposure. The trade-off shows up empirically: when Mindgard demonstrated that the approval-gate could be subverted via .clinerules-resident instructions, the design lacked a second layer (process / filesystem isolation) to contain the bypass.

The Clinejection incident is the more structurally informative finding for risk assessment. The vulnerability was not in the Cline code that ships to users; it was in the project's own use of an LLM-powered GitHub Actions workflow with broad tool permissions reachable by an unauthenticated trigger surface (issue creation). When that workflow was chained with a recently-changed GitHub cache eviction policy and a credential model in which nightly-publish tokens carried production-publish authority, the resulting attack chain reached the production npm package. The eventual unauthorized publish (a separate actor, ~5 weeks later) demonstrated that the attack chain was reachable in practice. The vendor's response after public disclosure — workflow removal, cache decoupling from publishing, OIDC provenance adoption, full credential rotation across VSCE / OVSX / NPM — addresses the demonstrated chain. The CLI-binary integrity at the time of unauthorized publish (byte-identical to the prior legitimate release) was the primary factor that limited direct user impact.

For procurement teams evaluating Cline against the comparative anchors: the platform's verifiability profile (open source, named entity, published security policy, GHSA process) is competitive with the cluster, and the HITL design ranks among the strongest in the category for user-facing control. The certification gap (no SOC 2 / ISO 27001) and the demonstrated supply-chain attack surface are the dimensions where the platform trails most of the cluster.

---

## VERDICT Record

**Summary:** Cline scores 50/85 (Mid) on Layer 0, with strengths in identity & control and verifiability and recorded concerns in resilience and data-conduct disclosure depth.

**Risk Factor Summary by Use Case:**

| Use case | Risk-factor profile |
|---|---|
| Internal developer testing / personal projects | Strong HITL surface, BYOK architecture, open-source auditable code; trailing-12-month supply-chain compromise on the npm CLI distribution channel was contained in ~8 hours and the VS Code / JetBrains channels were unaffected. |
| Credential-handling workflows | Mindgard demonstrated DNS-based exfiltration via whitelisted "safe" commands and .clinerules-driven approval-gate override; partial mitigation in v3.35.0; absence of process-level isolation means approved commands inherit full user-account credentials. |
| Cloud multi-tenant deployments | N/A in the conventional sense — Cline's core execution path is client-side; tenant-isolation criterion does not apply to the agent loop. Enterprise dashboard (app.cline.bot) is a separate cloud surface for credit / governance only. |
| Regulated-data workloads (HIPAA / PCI / SOC 2-required) | No published SOC 2 / HIPAA / ISO 27001 attestation; compliance posture in regulated environments depends on the customer's own controls plus the chosen LLM provider's certifications, not on a Cline-issued attestation. |

**Reference Information (options, not directives):**

- For environments requiring vendor-level SOC 2 / ISO 27001 attestation, the trailing-12-month public-data state shows no such attestation; procurement teams may wish to request the Cline Enterprise security documentation directly via cline.bot/contact-sales.
- For host-isolation needs beyond HITL, comparison with #035 OpenHands (Docker sandbox) provides a contrasting architectural model in the same category.
- For BYOK-architecture continuity in regulated environments, AI Model Provider zero-retention configurations (where offered by the chosen provider) are the documented path Cline points users toward, since Cline itself does not retain user content under BYOK.

**Bias Disclosure:**

> This evaluation uses Claude (Anthropic) as its tooling. Anthropic operates in the AI agent market and may compete with some evaluated vendors. VERDICT discloses this relationship in every report and applies identical evaluation criteria to all platforms regardless of their relationship to Anthropic.

Methodology note for this specific report: the Clinejection attack vector publicly documented against Cline made use of `claude-code-action`, an Anthropic-published GitHub Action, configured with broad permissions in Cline's repository. This is a factual element of the public record and is reported as such. The criteria applied to Cline are identical to those applied to all other platforms in the VERDICT index.

---

## Future Evaluation Plan

- **Layer C monitoring:** Continuous CVE / NVD / GHSA / CISA-KEV monitoring against `cline`, `cline-bot`, and `Cline Bot Inc.` Trigger thresholds per ENGINE.md (CVSS ≥7.0, KEV addition, supply-chain compromise, ≥2-source major incident, 90-day routine).
- **Next routine review:** 2026-07-26 (90 days from this evaluation).
- **Layer 1 candidacy:** Cline is a strong candidate for Layer 1 behavioral testing given its free OSS distribution and BYOK model (free-tier accessible without vendor-provided trials). Recommended Layer 1 focus areas: (a) post-mitigation prompt-injection robustness on v3.35.0+, (b) auto-approve pattern-matching edge cases, (c) MCP server permission-scope enforcement.
- **Re-evaluation triggers:** Any new GHSA / CVE with CVSS ≥7.0, any additional supply-chain event, any KEV addition, any new SOC 2 / ISO 27001 / HIPAA attestation publication.

---

## Japanese Summary

```japanese-summary
# Cline 評価結果サマリー

## 基本情報
- スコア: 50/85 (Layer 0)
- ランク: AI Coding Agent クラスタ内で #022 Replit (48) と #057 aider (52) の中間
- 評価日: 2026.04.27
- 対象バージョン: v3.79.0
- 運営: Cline Bot, Inc. (米国 / 創業者 Saoud Rizwan / $32M Seed+Series A 調達済 / Emergence Capital + Pace Capital リード)
- 独立性: ✅ Independent (買収なし、独立スタートアップ)

## 次元スコア
- V (検証可能性): 14/20
- R (耐性): 5/20
- D (データ運用): 8/15
- I (制御): 10/10
- C (封じ込め): 6/10
- T (透明性): 7/10

## 主要ポジティブ所見
- HITL (Human-in-the-loop) 承認がデフォルト動作、I 次元満点
- Apache 2.0 完全 OSS、署名付き GitHub リリース、運営法人公開
- BYOK アーキテクチャでコード/プロンプトが Cline サーバを経由しない
- 2026-02-17 の不正 npm 公開を約8時間で封じ込め、OIDC provenance へ移行

## 主要リスク所見
- SOC 2 / ISO 27001 等の独立認証が公開されていない
- Mindgard 開示の4件の prompt injection / RCE / API キー流出系の指摘が公的圧力後に認知（>60日）
- "Clinejection" supply chain 攻撃チェーン (GHSA-9ppg-jx86-fqw7): GitHub Issues → Claude Issue Triage → Actions cache poisoning → 公開クレデンシャル盗難 → npm 不正リリース、影響期間8時間
- ホスト分離なし。承認後コマンドはユーザ権限フルで実行される

## インシデント
- Mindgard 4件 (2025.08, 部分修正 v3.35.0, CVE 未割当)
- GHSA-9ppg-jx86-fqw7 (2026.02.17 不正 cline@2.3.0 publish, 8時間で deprecate)
- "Clinejection" 攻撃チェーン (2026.02.09 公開, PR #9211 で30分以内に修正)

## CISA KEV
- 該当なし

## 同クラスタ位置づけ
- #056 Gemini Code Assist (Google 運営、cloud-backed) と #057 aider (Aider AI LLC, terminal-based, 52/85) と比較すると、Cline は OSS + IDE 統合 + HITL の点で aider と近いが、agentic 多段実行とホストマシンへの広い権限のため C 次元で劣る。Gemini Code Assist の vendor cloud 経由 vs Cline の BYOK client-side は本質的に異なる脅威モデル。

## HTMLカード用タグ
- tags: open-source, vscode-extension, jetbrains, byok, hitl, apache-2.0, ai-coding-agent
- incident_tags: mindgard-2025-08, clinejection-2026-02, supply-chain, prompt-injection, npm-compromise
- owner: Cline Bot, Inc.
```