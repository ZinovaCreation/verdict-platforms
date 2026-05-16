# Weaviate 評価結果サマリー

## 基本情報
- スコア: 62/85 (Layer 0)
- ランク: Tier A
- 評価日: 2026.05.15
- 対象バージョン: Weaviate Database 1.33.x / 1.34.0
- 運営: Weaviate B.V. (Amsterdam, NL) / Weaviate, LLC (US)
- 独立性: ✅ Independent (Series B、Index Ventures主導、買収履歴なし)

## 次元スコア
- V (検証可能性): 16/20
- R (耐性): 14/20
- D (データ運用): 13/15
- I (制御): 6/10
- C (封じ込め): 6/10
- T (透明性): 7/10

## 主要ポジティブ所見
- V: BSD 3-Clauseコアの公開、Weaviate B.V.(蘭)とWeaviate LLC(米)の二重法人構造を契約書で明示
- D: DPA v1.4(2026年2月)§2.2が「顧客の文書化された指示なしにモデル訓練のためのPersonal Data処理を行わない」と明文化、保管期間180+180日明記
- D: サブプロセッサー一覧が公開かつ更新日(2025年10月)明示
- R: CVE-2025-67818 / 67819を2025年11月にVDP経由で協調開示、1.30.x/1.31.x/1.32.x/1.33.xの4サポートブランチで同時パッチリリース
- T: DPA Annex Aで14カテゴリのTOMを詳細記述、OSS Hardening Guide / Security Checklistを公開
- C: テナント分離はテナントごとに専用シャード、論理・物理分離をアーキテクチャドキュメントで明示

## 主要リスク所見
- V: SOC 2 Type II / ISO 27001:2022 監査報告書はtrust.weaviate.ioでゲーティング(未認証アクセスはHTTP 403)
- D: OSSテレメトリーがデフォルト有効、クラウドメタデータ(AWS Account ID等)をハイパースケーラーと共有(商業リード識別目的を明示開示)、オプトアウトはDISABLE_TELEMETRY=true一発
- I: エージェント(Query Agent / Transformation Agent / Personalization Agent)のHIL既定値とエマージェンシーストップが明示ドキュメント化されていない
- C: 生成モジュール(generative-anthropic / generative-openai 等)はメインプロセス内実行、デフォルトの送信先allowlist未文書化
- T: NIST AI RMF / ISO/IEC 42001等のAI固有安全フレームワーク参照なし(ISO 27001は情報セキュリティISMSでAI固有ではない)

## インシデント
- CVE-2025-67818: Backup ZipSlipパストラバーサル、CVSS v4.0 8.7 High(ベンダーブログCVSS v3.1 7.2 High)
- CVE-2025-67819: Shard Movement GetFileパストラバーサル、CVSS v3.1 4.9 Medium
- いずれも外部研究者(soohyun)がVDP経由で報告、2025年11月協調開示、1.33.4等で修正
- 定義的インシデント: 2025年11–12月の協調パストラバーサル開示2件(Backup ZipSlip + Shard Movement GetFile)
- パターン記録: 2件ともCWE-22(パストラバーサル)、隣接するファイル処理サブシステムに発生

## CISA KEV
- なし

## バイアス開示
- Weaviateは `generative-anthropic` モジュールを同梱しAnthropicモデルとのRAG連携を提供(顧客提供APIキー方式 / BYOK、直接の商業関係は公開情報なし)。他モデルプロバイダーとの統合と同一基準で評価。

## HTMLカード用タグ
- tags: vector-database, weaviate, bsd-3-clause, oss, gdpr, soc2-type2, iso27001-2022, hipaa-dedicated, rbac, oidc, multi-tenancy, byoc, weaviate-cloud
- incident_tags: cve-2025-67818, cve-2025-67819, path-traversal, cwe-22, zipslip, shard-movement, coordinated-disclosure, vdp
- owner: Weaviate B.V. (NL) / Weaviate LLC (US)

═══ QA REVIEW ═══
Factual:   [PASS] — CVE numbers, CVSS scores (v4.0 8.7 and v3.1 7.2 both noted for CVE-2025-67818), patch versions, certification dates, KEV status, sub-processor list date all verified against cited sources. No KNOWN_FACTS.md entries applicable.
Legal:     [PASS] — No intent attribution. No prescriptive negative recommendations. No blocklist words applied to vendor. Positive findings included alongside risks. Bias disclosure verbatim with Anthropic indirect-integration context added.
Quality:   [PASS] — Executive Summary 4 sentences leading with specific finding. All mandatory sections present. Bias disclosure complete. Japanese summary scores match English exactly. No AI-writing blocklist phrases in narrative sections.
Result:    CLEARED
══════════════

Score: 62/85
V: 16/20, R: 14/20, D: 13/15, I: 6/10, C: 6/10, T: 7/10
Dimensions verified: V+R+D+I+C+T = 62
Tier: A
Category: Vector Database

# VERDICT Evaluation #065 — Weaviate

**Evaluation Number:** #065
**Platform:** Weaviate (Vector Database)
**Type:** New evaluation
**Date:** 2026.05.15
**Evaluator:** VERDICT Evaluation Engine
**Target Version:** Weaviate Database 1.33.x / 1.34.0 (latest stable per cr.weaviate.io)
**Framework:** VERDICT v0.3.1 (Layer 0)
**Previous Evaluation:** None

---

## Executive Summary

Weaviate scores **62/85** on Layer 0 (Tier A) under VERDICT v0.3.1. The platform demonstrates strong verifiability and data-conduct posture: a BSD 3-Clause open-source core, a versioned and dated Data Processing Agreement (v1.4, February 2026) with Standard Contractual Clauses, an explicit DPA clause stating Personal Data is not processed for model training without customer instruction, a publicly dated sub-processor list (Last Updated: October 2025), and ISO 27001:2022 certification (announced September 2025) alongside existing SOC 2 Type II. Two path-traversal CVEs were disclosed and patched in coordinated release in November–December 2025 (CVE-2025-67818, CVSS v4.0 8.7 / CVSS v3.1 7.2; CVE-2025-67819, CVSS 4.9), both reported through Weaviate's Vulnerability Disclosure Program by an external researcher and patched across four supported minor branches. Recorded concerns: telemetry collection is on by default in OSS with cloud-metadata sharing used for commercial lead identification (easy opt-out via `DISABLE_TELEMETRY=true`); audit reports and ISO certificate access are gated through trust.weaviate.io; no explicit external AI safety framework (NIST AI RMF, ISO/IEC 42001) is referenced in public documentation.

## Scorecard

| Dimension | Score | Max | % | Rating |
|-----------|-------|-----|------|--------|
| V — Verifiability | 16 | 20 | 80% | High |
| R — Resilience | 14 | 20 | 70% | High |
| D — Data Conduct | 13 | 15 | 87% | High |
| I — Identity & Control | 6 | 10 | 60% | Mid |
| C — Containment | 6 | 10 | 60% | Mid |
| T — Transparency | 7 | 10 | 70% | High |
| **Total (Layer 0)** | **62** | **85** | **72.9%** | **Tier A** |

**CISA KEV:** なし — No Weaviate CVEs appear in the CISA Known Exploited Vulnerabilities catalog as of evaluation date.

---

## Dimension Detail

### V — Verifiability (16/20)

| Criterion | Result | Score | Evidence |
|-----------|--------|-------|----------|
| Developer / company identity | Weaviate B.V. (Amsterdam, NL) for non-US; Weaviate, LLC for US contracting | 4/4 | https://weaviate.io/privacy ; https://weaviate.io/service/weaviate-non-enterprise-agreement |
| Source code disclosure | BSD 3-Clause core; managed-tier (Cloud Console, Query Agent server-side, Marketplace integrations) closed | 2/4 | https://github.com/weaviate/weaviate (LICENSE) |
| Version management transparency | GitHub Releases + dedicated release-notes site | 3/3 | https://github.com/weaviate/weaviate/releases ; https://docs.weaviate.io/weaviate/release-notes |
| Third-party dependency disclosure | Public sub-processor list with explicit update date | 3/3 | https://weaviate.io/subprocessors (Last Updated: October 2025) |
| Independent certification | SOC 2 Type II + ISO 27001:2022; audit reports gated via trust portal (HTTP 403 to unauthenticated request) | 2/4 | https://trust.weaviate.io ; https://weaviate.io/blog/weaviate-iso-compliant |
| Functional reproducibility docs | Complete API reference for REST, gRPC, GraphQL; behavioral spec via release notes and module docs | 2/2 | https://docs.weaviate.io |

**Positive findings:** Dual-entity legal structure published with jurisdictional clarity; sub-processor list updates dated; ISO 27001:2022 certification disclosed via vendor blog with date (2025-09-24).
**Recorded concerns:** Trust portal access is gated; SOC 2 and ISO 27001 evidence requires registration/NDA process.

### R — Resilience (14/20)

| Criterion | Result | Score | Evidence |
|-----------|--------|-------|----------|
| CVE count (trailing 12 months) | 2 CVEs (CVE-2025-67818, CVE-2025-67819); no CVSS 9.0+ | 3/5 | https://github.com/advisories/GHSA-7v39-2hx7-7c43 ; https://www.wiz.io/vulnerability-database/cve/cve-2025-67819 |
| Maximum CVSS severity | CVE-2025-67818: CVSS v4.0 8.7 (NVD/GHSA); CVSS v3.1 7.2 (vendor) — both in 7.0–8.9 band | 2/6 | https://nvd.nist.gov/vuln/detail/CVE-2025-67818 |
| Patch response speed | Coordinated disclosure with same-day patches across 1.30.x / 1.31.x / 1.32.x / 1.33.x; managed cloud and Marketplace patched without customer action | 3/3 | https://weaviate.io/blog/weaviate-security-release-november-2025 |
| Structural issues | Two distinct modules affected (backup zip-extraction handling vs shard movement file transfer); isolated independent bugs surfaced in single VDP audit batch | 3/3 | https://github.com/advisories/GHSA-7v39-2hx7-7c43 |
| Supply chain compromise (trailing 12 months) | No public reports of Weaviate OSS, weaviate-client (PyPI), or weaviate-agents package compromise | 3/3 | https://pypi.org/project/weaviate-client/ ; https://pypi.org/project/weaviate-agents/ |

**Positive findings:** Coordinated disclosure protocol executed across four supported minor branches; Vulnerability Disclosure Program operates externally and credits researcher (soohyun); backup module can be disabled via `enabled_modules` workaround; Shard Movement API documented as default-disabled.
**Recorded concerns:** Two path-traversal class vulnerabilities (CWE-22) in adjacent file-handling subsystems indicate broader review of input-validation patterns across file-path operations would be informative; structured CVE assignment is recent (CVE-2025-67818 / 67819 are the first independently catalogued CVEs since CVE-2023-38976).

### D — Data Conduct (13/15)

| Criterion | Result | Score | Evidence |
|-----------|--------|-------|----------|
| GDPR compliance disclosure | DPA v1.4 (February 2026) with SCCs, Article 28 framing, Annex A (14-section Technical and Organisational Measures) | 3/3 | https://weaviate.io/dpa |
| Data minimization | OSS telemetry enabled by default; opt-out via `DISABLE_TELEMETRY=true`; cloud-metadata sharing with hyperscalers for commercial lead-identification disclosed | 1/3 | https://docs.weaviate.io/deploy/configuration/telemetry |
| AI training use | DPA §2.2 explicit: Personal Data not processed for model training without documented customer instruction; retention period stated (180d post-account closure + 180d backup) | 4/4 | https://weaviate.io/dpa (§2.2 and Annex A §8) |
| Sub-processor transparency | Public list with October 2025 update date; 30-day prior-notice obligation for additions or replacements | 3/3 | https://weaviate.io/subprocessors ; DPA §5 |
| Data retention disclosure | Per-category retention stated: 180d post-account + 180d backup; 30-day post-cessation deletion commitment | 2/2 | https://weaviate.io/dpa (Annex A §8) |

**Positive findings:** DPA Annex A enumerates TOMs across 14 categories including encryption (AES-256 at rest, TLS 1.2+ in transit), DPO and ISO designation, daily backups, and annual BC/DR tests; customer-as-controller framing consistent across Privacy Policy, DPA, and ToS; HIPAA available via Dedicated Cloud (boundary explicitly documented).
**Recorded concerns:** OSS telemetry default-on with cloud-metadata pass-through to hyperscalers (AWS, GCP) for commercial-lead identification is disclosed in the telemetry documentation but may surprise OSS users who do not read the telemetry page; Privacy Policy general retention statement (5-year default) and DPA TOM retention statement (180+180d) describe different data categories and warrant reading together.

### I — Identity & Control (6/10)

| Criterion | Result | Score | Evidence |
|-----------|--------|-------|----------|
| Emergency stop documentation | Cluster lifecycle documented (cluster pause, hibernation after 8 hours stale on Enterprise tier, deletion via console); agent-task abort not separately documented | 2/4 | https://weaviate.io/service/service-schedule |
| Human-in-the-loop design | Database operations are explicit by design; Query Agent / Transformation Agent (alpha) / Personalization Agent execute under user auth scope but HIL is not specified as enforced default for autonomous transformation flows | 1/3 | https://docs.weaviate.io/agents |
| Permission delegation transparency | RBAC GA from v1.29 with collection / tenant / operation-level filters, OIDC group mapping, custom roles, and root role | 3/3 | https://docs.weaviate.io/weaviate/configuration/rbac ; https://docs.weaviate.io/weaviate/configuration/rbac/manage-users |

**Positive findings:** RBAC integrates with OIDC group claims (Okta, Auth0, Azure AD, Keycloak referenced in vendor security guide); MFA required for privileged accounts per DPA TOM §3; root user requirement is configuration-explicit.
**Recorded concerns:** For autonomous agent surfaces (Query Agent GA, Transformation Agent alpha), public documentation does not explicitly state human-in-the-loop as a default-enforced control; emergency-stop semantics for in-flight agent tasks not specifically described.

### C — Containment (6/10)

| Criterion | Result | Score | Evidence |
|-----------|--------|-------|----------|
| Sandbox design | Module-level allowlist via `enabled_modules`; modules execute in main Weaviate process; outbound egress controlled by which generative/vectorizer modules are enabled | 2/4 | https://docs.weaviate.io/deploy/configuration |
| Least privilege | RBAC available and configurable; principle of least privilege explicitly enforced when RBAC enabled; not default on every deployment path | 1/3 | https://docs.weaviate.io/weaviate/tutorials/rbac |
| Tenant isolation (cloud) | Per-tenant dedicated shard architecture with physical and logical separation documented; no public cross-tenant breach disclosed | 3/3 | https://weaviate.io/blog/weaviate-multi-tenancy-architecture-explained |

**Positive findings:** Tenant model places each tenant on a dedicated shard, supporting strong data isolation; Shard Movement API default-disabled; backup module disable available as workaround for CVE-2025-67818; OSS Hardening Guide and Security Checklist published.
**Recorded concerns:** Generative modules (`generative-anthropic`, `generative-openai`, `generative-cohere`, AWS Bedrock, etc.) make outbound API calls from the main Weaviate process; documentation does not enumerate a default network-egress allowlist or proxy-based egress control; least-privilege is configurable rather than default-enforced on all install paths.

### T — Transparency (7/10)

| Criterion | Result | Score | Evidence |
|-----------|--------|-------|----------|
| CVE publication posture | Issues CVEs (CVE-2025-67818 / 67819); maintains GitHub Security Advisories (GHSA-7v39-2hx7-7c43); blog-based advisories with affected versions, fix versions, and mitigations | 2/2 | https://github.com/weaviate/weaviate/security/advisories |
| Incident disclosure speed | Vendor blog disclosure November 2025; NVD published 2025-12-12 — coordinated release within ≤30 days | 2/2 | https://weaviate.io/blog/weaviate-security-release-november-2025 |
| Security policy publication | Detailed TOMs in DPA Annex A; published Security Checklist for self-managed deployments; OSS Hardening Guide; VDP via security-report page | 2/2 | https://weaviate.io/img/site/Security-Checklist.pdf ; https://weaviate.io/blog/hardening-oss |
| AI safety framework reference | No explicit NIST AI RMF, ISO/IEC 42001, or AI-specific safety framework referenced in public documentation; ISO 27001:2022 is information-security ISMS, not AI-specific | 0/2 | https://weaviate.io/blog/weaviate-iso-compliant |
| AI system identity disclosure | Agent products named explicitly as AI agents in documentation and product surfaces; default-on identity disclosure framework not separately specified | 1/2 | https://weaviate.io/product/query-agent |

**Positive findings:** Investor list published (https://weaviate.io/company/investors); security disclosures include affected ranges, fix versions, and mitigation flags; release-notes site offers per-version detail; coordinated disclosure pattern is consistent across the 2025 security blog series.
**Recorded concerns:** Forward-looking roadmap signals are limited to retrospective year-in-review posts; AI-specific safety framework adoption is not publicly documented; trust portal gating limits reviewer ability to verify control evidence without a customer relationship.

---

## Incident Timeline

| Date | CVE | CVSS | Description | Patch | KEV |
|------|-----|------|-------------|-------|-----|
| 2025-12-12 (NVD) | CVE-2025-67818 | v4.0: 8.7 High / v3.1: 7.2 High | Backup ZipSlip path traversal (CWE-22, CWE-61) in backup restore allowing arbitrary file creation/overwrite within Weaviate process scope | Fixed in 1.30.20, 1.31.19, 1.32.16, 1.33.4 | No |
| 2025-12-12 (NVD) | CVE-2025-67819 | v3.1: 4.9 Medium | Path traversal in Shard Movement GetFile (FileReplicationService) allowing arbitrary file read while shard in "Pause file activity" state | Fixed in 1.30.20, 1.31.19, 1.32.16, 1.33.4 | No |
| 2023-08-21 (NVD) | CVE-2023-38976 | (out of trailing 12-month window; recorded for historical completeness) | DoS via `handleUnbatchedGraphQLRequest` function in v1.20.0 | Fixed in subsequent 1.20.x | No |

---

## Contextual Analysis

Weaviate publishes an unusually detailed Data Processing Agreement for a venture-backed Series B vendor at its size: Annex A enumerates fourteen technical and organisational measure categories with named tooling (Drata for compliance automation, Google Workspace and SSO for identity, AWS/GCP/Azure KMS for key management). The DPA explicitly addresses model training in §2.2, which is uncommon clarity for a vector database vendor that primarily handles customer-supplied embeddings.

The November–December 2025 security release illustrates a maturing disclosure posture. Two path-traversal vulnerabilities — one in backup zip handling and one in shard movement file transfer — were discovered by an external researcher through the VDP program, patched across four supported minor branches in coordinated release, and disclosed via vendor blog with affected versions, fix versions, CVSS scores, and disable-workaround flags. Enterprise customers received embargo notification; managed Cloud and Marketplace customers were patched without customer action. The pattern aligns with industry practice for coordinated vulnerability disclosure. Two CWE-22 findings in adjacent file-handling subsystems are worth noting for context: the shared class signature suggests value in a broader review of file-path input validation across the codebase.

Telemetry warrants reader attention. Per the public documentation, OSS telemetry is collected by default and includes cluster statistics plus cloud-provider metadata (AWS Account ID, GCP Project ID, Azure Subscription ID). The telemetry documentation states this data may be shared with cloud providers to enable them to contact the user about Weaviate support, maintenance, or hosting services. This is disclosed clearly in the telemetry documentation and Privacy Policy §2(a), and opt-out is a single environment variable. The disclosure is complete; readers operating in regulated environments may wish to set `DISABLE_TELEMETRY=true` as part of baseline configuration.

Multi-tenancy architecture is documented at depth: one shard per tenant, with logical and physical isolation at the storage layer and per-tenant write-ahead logging. No public cross-tenant data exposure has been disclosed. SOC 2 Type II and ISO 27001:2022 audits are referenced, with audit reports and certificates accessible only via the gated trust portal — a posture consistent with peer vendors at this stage but limiting independent reviewer verification.

Anthropic-related context: Weaviate ships a `generative-anthropic` module that enables RAG with Claude models. The integration is BYOK (customer provides Anthropic API key); no direct billing or commercial relationship between Anthropic and Weaviate is publicly disclosed. Anthropic models are also reachable indirectly through the AWS Bedrock module. This relationship is disclosed in the Bias Disclosure section below.

---

## VERDICT Record

**Summary:** Weaviate scores 62/85 (Tier A) on VERDICT v0.3.1 Layer 0, with strong verifiability, data conduct, and transparency dimensions and mid-range identity-control and containment dimensions reflecting the platform's database-first (rather than agent-first) architecture.

### Risk Factor Summary by Use Case

| Use Case | Risk Posture | Rationale |
|----------|--------------|-----------|
| Internal testing / evaluation | Low | BSD 3-Clause OSS, Docker / Kubernetes deployment paths, comprehensive docs and tutorials, free Cloud sandbox tier available |
| Credential-handling workloads | Mid | Generative modules execute in-process and use customer-supplied API keys; recent backup-module CVE (CVE-2025-67818) patched but root-cause class warrants attention; RBAC + MFA available but not default-enforced on all install paths |
| Cloud multi-tenant deployments | Low–Mid | Per-tenant shard isolation documented in detail with no public cross-tenant breach; SOC 2 Type II + ISO 27001:2022 reports gated, limiting independent verification |
| Regulated-data workloads (GDPR / HIPAA) | Mid | DPA v1.4 with SCCs and detailed TOMs; HIPAA limited to Dedicated Cloud (not Serverless); customer-as-controller framing explicit; trust-portal gating means audit-report review requires customer relationship |

### Reference Information

Readers evaluating Weaviate for production may wish to consider:
1. Patching to ≥1.33.4 / ≥1.32.16 / ≥1.31.19 / ≥1.30.20 to address CVE-2025-67818 / 67819, or disabling backup and shard-movement modules where not required.
2. Reviewing telemetry defaults; setting `DISABLE_TELEMETRY=true` for environments where cloud-metadata sharing with hyperscalers is not appropriate.
3. For regulated-data workloads, requesting trust-portal access to verify SOC 2 Type II and ISO 27001:2022 evidence under NDA before procurement decisions.

### Bias Disclosure

This evaluation uses Claude (Anthropic) as its tooling. Anthropic operates in the AI agent market and may compete with some evaluated vendors. VERDICT discloses this relationship in every report and applies identical evaluation criteria to all platforms regardless of their relationship to Anthropic.

Specific to this evaluation: Weaviate ships a `generative-anthropic` module enabling RAG with Anthropic Claude models, default-enabled on Weaviate Cloud instances. The integration uses customer-supplied Anthropic API keys (BYOK); no direct billing or commercial relationship between Anthropic and Weaviate is publicly disclosed. Anthropic models are also reachable indirectly through the AWS Bedrock generative module. This indirect integration was treated identically to integrations with other model providers (OpenAI, Cohere, Voyage AI, Google, Hugging Face) during scoring.

---

## Future Evaluation Plan

- **Layer 1 (free-tier behavioral testing):** Not yet scheduled. Candidate scope: RBAC enforcement validation, telemetry default behavior, generative-module egress observation, backup workflow re-test post 1.33.4+.
- **Layer C (continuous CVE / incident monitoring):** Active. Re-evaluation triggers: new CVE with CVSS 7.0+, CISA KEV listing, supply chain incident affecting weaviate-client / weaviate-agents / cr.weaviate.io image, or 90-day routine check (next review: 2026-08-15).

---

**Framework version:** VERDICT v0.3.1
**Score:** 62/85
**Dimensions verified:** V+R+D+I+C+T = 16+14+13+6+6+7 = 62 ✓
**Tier:** A
**Category:** Vector Database