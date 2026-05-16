# NeMo Guardrails 評価結果サマリー

## 基本情報
- スコア: 52/85 (Layer 0)
- ランク: Tier B
- 評価日: 2026.05.15
- 対象バージョン: nemoguardrails v0.20.x系 (評価日時点の最新安定版OSSリリース)
- 運営: NVIDIA Corporation (デラウェア州C-corporation, 本社カリフォルニア州サンタクララ, 米国)
- 独立性: ⚠️ NVIDIA Corporation (Anthropic との多層的な商業・出資関係を構造的開示)

## 次元スコア
- V (検証可能性): 18/20 — Apache 2.0 OSS、NVIDIA法人実体、EMNLP 2023査読論文、PSIRT公開
- R (耐性): 17/20 — `nemoguardrails` パッケージ固有のCVEなし(直近12ヶ月)、CISA KEV該当なし
- D (データ運用): 5/15 — DPA・サブプロセッサー一覧・トレーニング使用記述が NVIDIA AI Enterprise セールス経由ゲート
- I (制御): 4/10 — 認証はデプロイ組織責務、HITLはデフォルト無効、エマージェンシーストップは部分文書化
- C (封じ込め): 3/10 — ライブラリは開発者プロセス内実行、カスタムアクションのサンドボックスなし
- T (透明性): 5/10 — NVIDIA は CNA、PSIRTポリシー詳細公開、ただし AI Safety 外部フレームワーク採用は内部文書のみ

## 主要ポジティブ所見
- Apache License 2.0 完全OSS、SPDX-FileCopyrightText: NVIDIA CORPORATION & AFFILIATES
- EMNLP 2023査読論文によるアカデミックな設計プロベナンス (Rebedea et al., 2023)
- NVIDIA は CVE Numbering Authority、Security Bulletins公開、coordinated disclosure プロセス文書化
- 直近12ヶ月で `nemoguardrails` パッケージ固有CVE は確認されず (NeMo Framework のCVEとは別個に評価)
- ライブラリはローカル実行アーキテクチャでありNVIDIA向けテレメトリ既定なし

## 主要リスク所見
- SOC 2 レポートは NVIDIA AI Trust Center 上で枠組み記載のみ、報告書本体はセールス経由
- 製品レベルのGDPR DPA / サブプロセッサー一覧 / トレーニング利用ステートメント / カテゴリ別保存期間が公開文書外
- カスタム Python アクションは開発者プロセス権限で実行されサンドボックスなし
- `nemoguardrails server` HTTPエンドポイントは標準で認証機構なし、デプロイ組織責務
- NeMo Microservices 商用ティアの Helm チャート既定セキュリティ設定はエンタープライズ契約ゲート

## インシデント
- 直近12ヶ月の公開CVEなし (2025.05.15 – 2026.05.15)
- NVD、GitHub Security Advisories (NVIDIA-NeMo/Guardrails)、GitHub Advisory Database、OSV.dev (PyPI:nemoguardrails) いずれも該当なし
- 12ヶ月窓外として PyUp Safety DB に PVE-2024-72352 (v0.9.1で修正) 及び PVE-2024-64722 (v0.7.0で修正) が記録されているが正式なCVE割当なし

## CISA KEV
- 該当なし

## バイアス開示
- NVIDIA (NeMo Guardrails 運営) と Anthropic (VERDICT 評価ツール提供) の間に多層的な商業・出資関係 (Anthropic による NVIDIA経由 Azure容量 最大 USD 30B、NVIDIA から Anthropic への 最大 USD 10B 出資コミット, 2025-11-18 NVIDIA SEC Form 10-Q FY2026 Q3 開示) が存在することを構造的事実として開示
- VERDICT v0.3.1 は公開情報のみで採点しベンダー収益・有償認証を排除する非交渉条件のため本評価レートには影響しない

## HTMLカード用タグ
- tags: NVIDIA, AI Safety, LLM Guardrails, Open-Source Toolkit, Apache-2.0, programmable rails, Colang, NIM
- incident_tags: no-cve-trailing-12mo, no-kev, no-supply-chain-compromise, PVE-out-of-window
- owner: NVIDIA

═══ QA REVIEW ═══
Factual:   PASS — CVE scope verified (no NeMo Guardrails-specific CVEs trailing 12mo; NeMo Framework CVEs excluded per Special Considerations §3); Apache 2.0 license confirmed via LICENSE.md; NVIDIA PSIRT process verified; KNOWN_FACTS.md not applicable to this evaluation
Legal:     PASS — No intent attribution; positive findings included (corporate transparency, EMNLP 2023 provenance, OSS licensing, zero CVEs in window); NVIDIA-Anthropic equity relationship disclosed neutrally per Special Considerations §1
Quality:   PASS — All mandatory sections present; Executive Summary 3-5 sentences; Bias Disclosure verbatim; Japanese summary aligned
Result:    CLEARED
══════════════

Score: 52/85
V: 18/20, R: 17/20, D: 5/15, I: 4/10, C: 3/10, T: 5/10
Dimensions verified: V+R+D+I+C+T = 52
Tier: B
Category: AI Safety · LLM Guardrails / Programmable Constraints · Open-Source Toolkit (with commercial NIM deployment tier)

# VERDICT Evaluation Report — #066 NeMo Guardrails

| Field | Value |
|-------|-------|
| **Evaluation #** | 066 |
| **Platform** | NeMo Guardrails |
| **Operator** | NVIDIA Corporation (Delaware C-corporation, Santa Clara, California, USA) |
| **Evaluation Type** | Initial (Layer 0) |
| **Evaluation Date** | 2026.05.15 |
| **Evaluator** | VERDICT Engine (Claude/Anthropic tooling) |
| **Target Version** | `nemoguardrails` v0.20.x series (latest stable open-source release as of evaluation date) |
| **Framework Version** | VERDICT v0.3.1 |
| **Previous Evaluation** | None |

## Executive Summary

NeMo Guardrails scores 52/85 (Tier B) under VERDICT v0.3.1 Layer 0. The toolkit is an Apache 2.0 open-source Python library distributed via PyPI as `nemoguardrails` and via GitHub at NVIDIA-NeMo/Guardrails, with full source code visibility, peer-reviewed academic provenance (EMNLP 2023), versioned documentation at docs.nvidia.com, and clear operator identity backed by NVIDIA's SEC filings as a publicly-traded company. No CVEs were confirmed in the trailing 12 months for the `nemoguardrails` package distinct from the NeMo Framework (`nemo-toolkit`), and no entries appear in the CISA Known Exploited Vulnerabilities catalog. Documentation gaps concentrate in product-level data governance disclosures — sub-processor lists, GDPR DPA references, AI training data use statements, and SOC 2 report public availability are gated to NVIDIA AI Enterprise sales contact rather than published on the public documentation site. The library executes in the developer's Python process with no built-in sandboxing of custom actions; deployment-time isolation (Kubernetes pod security, network policies, authentication for the server endpoint) is the deploying organization's responsibility, as the documentation makes explicit.

## Scorecard

| Dimension | Score | Max | Percentage | Rating |
|-----------|-------|-----|------------|--------|
| V — Verifiability | 18 | 20 | 90% | High |
| R — Resilience | 17 | 20 | 85% | High |
| D — Data Conduct | 5 | 15 | 33% | Low |
| I — Identity & Control | 4 | 10 | 40% | Mid |
| C — Containment | 3 | 10 | 30% | Low |
| T — Transparency | 5 | 10 | 50% | Mid |
| **Total (Layer 0)** | **52** | **85** | **61%** | **Tier B** |

**CISA KEV:** None at evaluation date.

## Dimension Detail

### V — Verifiability (18/20)

| Criterion | Result | Score | Evidence |
|-----------|--------|-------|----------|
| Developer / company identity | NVIDIA Corporation (Delaware C-corporation, SEC-registered, Santa Clara CA); PSIRT contact `psirt@nvidia.com` and security submission form published | 4/4 | https://www.nvidia.com/en-us/security/psirt-policies/ |
| Source code disclosure | Full open-source under Apache License 2.0 (SPDX-FileCopyrightText: NVIDIA CORPORATION & AFFILIATES) | 4/4 | https://github.com/NVIDIA-NeMo/Guardrails/blob/main/LICENSE.md |
| Version management transparency | GitHub Releases with detailed feature/breaking-change notes; PyPI release history; recent releases include LangChain 1.x compatibility (v0.19.0, Dec 2025) and v0.20.0 | 3/3 | https://github.com/NVIDIA-NeMo/Guardrails/releases |
| Third-party dependency disclosure | Dependencies declared in `pyproject.toml` per PyPI release; versioned releases provide implicit update dates; optional extras (NVIDIA, LangChain, AlignScore) documented | 3/3 | https://pypi.org/project/nemoguardrails/ |
| Independent certification | NVIDIA AI Trust Center lists SOC 2 and ISO 27001 as compliance offerings; SOC 2 report access gated to sales contact (customers-only) | 2/4 | https://www.nvidia.com/en-us/ai-trust-center/security-compliance/ |
| Functional reproducibility docs | Complete documentation site: overview, installation guide, configuration, rail types, Colang language reference, API reference, examples | 2/2 | https://docs.nvidia.com/nemo/guardrails/latest/ |

**Positive findings:** EMNLP 2023 peer-reviewed academic paper (Rebedea et al., 2023) provides independent design provenance; full source code visibility for the OSS toolkit; publicly-traded operator with SEC disclosure obligations; consistent corporate identity across GitHub repository, documentation domain, and PyPI publisher.

**Recorded concerns:** SOC 2 attestation report not publicly downloadable from NVIDIA Trust Center; sales contact required for full audit evidence.

### R — Resilience (17/20)

CVE evaluation period: 2025.05.15 – 2026.05.15 (trailing 12 months).

| Criterion | Result | Score | Evidence |
|-----------|--------|-------|----------|
| CVE count (trailing 12 months) | 0 CVEs assigned specifically to `nemoguardrails` package or NeMo Guardrails repository; NVD product-string search, GitHub Advisory Database, OSV.dev (PyPI ecosystem) all return zero results | 5/5 | https://github.com/advisories?query=nemoguardrails ; https://osv.dev/list?q=nemoguardrails |
| Maximum CVSS severity | Not applicable (zero CVEs); scoring tier 0–3.9 applied by absence | 6/6 | (no CVE source) |
| Patch response speed | Not measurable in the trailing 12 months due to absence of CVE disclosures; per framework rule 3 (unconfirmable scores 0) | 0/3 | (no patch event source) |
| Structural issues | No recurring root-cause pattern identified in absence of CVE disclosures; isolated independent bugs only by default | 3/3 | (no recurring-issue source) |
| Supply chain compromise (trailing 12 months) | No supply chain compromise of the `nemoguardrails` PyPI package identified in trailing 12 months; no entry in PyPI security advisories or independent supply chain incident trackers | 3/3 | https://github.com/NVIDIA-NeMo/Guardrails/security/advisories (no advisories) |

**CISA KEV flag:** None.

**Positive findings:** No CVEs assigned to the `nemoguardrails` package distinct from the broader NeMo Framework family during the trailing 12 months; no supply chain compromise observed; NVIDIA holds CVE Numbering Authority (CNA) status and operates a formal PSIRT process for coordinated disclosure.

**Recorded concerns:** Earlier PyUp Safety DB entries (PVE-2024-72352, fixed in v0.9.1; PVE-2024-64722, fixed in v0.7.0) pre-date the trailing 12-month window and did not receive formal CVE assignment, which limits independent verifiability of NVIDIA's product-level CVE issuance discipline for this specific toolkit. Patch response speed is unmeasurable for this product in the current window.

### D — Data Conduct (5/15)

| Criterion | Result | Score | Evidence |
|-----------|--------|-------|----------|
| GDPR compliance disclosure | General NVIDIA Corporate Privacy Policy applies; DPA available under NVIDIA AI Enterprise contract (sales-gated); OSS library documentation does not explicitly address GDPR controller / processor framing | 1/3 | https://www.nvidia.com/en-us/about-nvidia/privacy-policy/ |
| Data minimization | OSS library has no telemetry channel to NVIDIA by design; library executes in developer's Python process; outbound calls go only to developer-configured endpoints | 3/3 | https://github.com/NVIDIA-NeMo/Guardrails (library design) |
| AI training use | Documentation does not explicitly state whether NVIDIA uses any user data for model training; for the OSS library, data does not flow to NVIDIA by architecture but no formal statement covers the production microservice tier | 0/4 | (source unconfirmed) |
| Sub-processor transparency | No publicly published NeMo Microservices sub-processor list comparable to enterprise SaaS sub-processor disclosures | 0/3 | (source unconfirmed) |
| Data retention disclosure | OSS library is stateless and runs locally (implied retention by NVIDIA: none); explicit per-category retention statement at the product level is absent | 1/2 | https://docs.nvidia.com/nemo/guardrails/latest/about/overview.html |

**Positive findings:** The OSS library's local-execution architecture means user prompts and LLM responses do not flow to NVIDIA at runtime; outbound network calls are limited to developer-configured providers using developer-supplied credentials.

**Recorded concerns:** Product-level data governance documentation (DPA, sub-processor list, training data use statement, per-category retention) is either absent from public documentation or gated to NVIDIA AI Enterprise sales contact. The boundary between OSS library data flow (developer-controlled) and NeMo Microservices production-tier data flow (NVIDIA-tier deployment context) is not crisply documented in publicly accessible material.

### I — Identity & Control (4/10)

| Criterion | Result | Score | Evidence |
|-----------|--------|-------|----------|
| Emergency stop documentation | Guardrails block individual LLM inputs/outputs by design, but no formal system-level kill-switch procedure documented; deployment-level emergency stop is the deploying organization's responsibility, as documentation states | 2/4 | https://docs.nvidia.com/nemo/guardrails/latest/about/overview.html |
| Human-in-the-loop design | HITL is configurable via developer-defined Colang flows but not enabled by default; the library supports human escalation patterns through custom actions | 1/3 | https://docs.nvidia.com/nemo/guardrails/latest/about/rail-types.html |
| Permission delegation transparency | Custom actions and tool integrations are developer-defined; LangChain tool integration documented; library does not enforce an explicit permission/delegation model beyond what the deploying application implements | 1/3 | https://docs.nvidia.com/nemo/guardrails/latest/about/overview.html |

**Positive findings:** The library exposes five distinct rail types (input, dialog, retrieval, execution, output) allowing fine-grained control insertion at multiple stages of the LLM interaction; explanations module documented for blocked-decision visibility.

**Recorded concerns:** Authentication for the `nemoguardrails server` HTTP endpoint and the production microservice is the deploying organization's responsibility; the library does not ship with built-in authentication by default, and secure-default deployment recipes are not the primary focus of installation documentation.

### C — Containment (3/10)

| Criterion | Result | Score | Evidence |
|-----------|--------|-------|----------|
| Sandbox design | Library executes in-process with no built-in sandbox; custom actions run with the developer's Python process privileges; security guidelines document the trust boundary explicitly as the developer's responsibility | 0/4 | https://github.com/NVIDIA-NeMo/Guardrails/blob/develop/docs/security/guidelines.md |
| Least privilege | Library inherits process privileges; no built-in privilege constraint mechanism; documented as a developer responsibility | 0/3 | (source as above) |
| Tenant isolation | Self-hosted only (library-level); deployment tenant isolation is governed by the deploying organization's Kubernetes / container configuration | 3/3 (N/A) | https://docs.nvidia.com/nemo/guardrails/latest/about/overview.html |

**Positive findings:** Security guidelines page explicitly enumerates the trust boundary and advises treating LLM output as untrusted; topic control, jailbreak detection, and content safety rails provide content-level containment of LLM behavior; the documentation discusses the implications of LangChain integration on the trust boundary.

**Recorded concerns:** Custom Python actions execute without sandboxing; configuration loading from untrusted sources is documented as a developer responsibility; the production-tier Helm chart's default resource limits, network policies, and pod security standards are not directly assessable from the public documentation site without enterprise contact.

### T — Transparency (5/10)

| Criterion | Result | Score | Evidence |
|-----------|--------|-------|----------|
| CVE publication posture | NVIDIA is a CVE Numbering Authority; PSIRT publishes Security Bulletins for NVIDIA products; GitHub Security Advisories interface configured (currently zero published advisories for this repository) | 2/2 | https://www.nvidia.com/en-us/security/psirt-policies/ |
| Incident disclosure speed | No incidents disclosed in trailing 12 months for this product; NVIDIA PSIRT policy describes coordinated disclosure process but does not publish a numeric target SLA | 0/2 | https://www.nvidia.com/en-us/security/psirt-policies/ |
| Security policy publication | Detailed PSIRT policy publication covering CVSS v3.1 usage, communication plan by severity, coordinated vulnerability disclosure, acknowledgements, and remediation forms | 2/2 | https://www.nvidia.com/en-us/security/psirt-policies/ |
| AI safety framework reference | Internal security guidelines and design rationale documented (EMNLP 2023 academic paper, NVIDIA Trust Center "Halos" framework); explicit adoption of external AI safety frameworks (e.g., NIST AI RMF) not stated on the NeMo Guardrails documentation site | 1/2 | https://www.nvidia.com/en-us/ai-trust-center/ |
| AI system identity disclosure | The library is middleware that wraps developer-configured LLMs; AI system identity disclosure to end users is the deploying application's responsibility and is not configured at the library level | 0/2 | (source unconfirmed at product level) |

**Positive findings:** NVIDIA's CNA status, formal PSIRT process, and publication of Security Bulletins establish a transparency baseline at the corporate level; the EMNLP 2023 paper provides academic peer-review provenance for the toolkit's design.

**Recorded concerns:** Earlier security fixes were tracked in PyUp Safety DB (PVE entries) without formal CVE assignment, which leaves the product-level CVE issuance practice for `nemoguardrails`-specific issues partially documented; NeMo Microservices commercial-tier SLA, support tiers, and compliance posture for the managed offering are gated to enterprise sales contact rather than publicly documented.

## Incident Timeline

No public CVEs were confirmed for the `nemoguardrails` package distinct from the NeMo Framework (`nemo-toolkit`) in the trailing 12 months (2025.05.15 – 2026.05.15). NVD product-string searches, GitHub Security Advisories at NVIDIA-NeMo/Guardrails, GitHub Advisory Database, and OSV.dev (PyPI ecosystem `nemoguardrails`) all returned zero matching advisories. CISA KEV catalog contains no entry for this product.

CVEs assigned to other NeMo-family products (CVE-2025-23361, CVE-2025-23312, CVE-2025-33205, CVE-2025-33212, CVE-2025-23249, CVE-2025-23250, CVE-2025-23251, CVE-2024-0129 and similar) describe vulnerabilities in the NeMo Framework speech / model / training stack (`nemo-toolkit` package) and are excluded from this evaluation per the prompt's Special Considerations §3 (CVE attribution scope).

For historical context outside the trailing 12-month window, PyUp Safety DB tracks two prior entries — PVE-2024-72352 (fixed in v0.9.1) and PVE-2024-64722 (fixed in v0.7.0). These were not formally assigned CVE identifiers and are outside the R-dimension trailing-12-month evaluation window.

## Contextual Analysis

NeMo Guardrails occupies an architectural position distinct from typical AI agent platforms: it is a middleware library wrapped around a developer-configured LLM, rather than a hosted agent service. This shapes the evaluation profile. Verifiability and Resilience are favored — Apache 2.0 source visibility, formal NVIDIA PSIRT process, CVE Numbering Authority status, EMNLP 2023 academic provenance, and absence of CVE history in the trailing 12 months produce strong scores. Data Conduct, Identity & Control, and Containment register lower scores not because the library introduces specific risks, but because product-level documentation does not address governance topics that apply more naturally to managed SaaS offerings — sub-processor lists, GDPR DPA references, training data use statements, default authentication, and built-in sandboxing. The architectural answer to several of these — "the deploying organization controls this" — is correct but is documented through security guidelines rather than addressed via product-default mechanisms.

The boundary between the OSS toolkit and the NeMo Microservices commercial tier is a recurring documentation question. The OSS library is fully transparent; the production microservice container image, Kubernetes Helm chart defaults, and NVIDIA AI Enterprise managed-deployment posture are gated to sales contact. For organizations evaluating NeMo Guardrails for production agentic AI deployments, the OSS toolkit assessment under Layer 0 reflects the library's governance properties as published; the production-tier posture is not directly assessable from public documentation alone.

NVIDIA's operator profile is materially different from independent OSS projects: SEC-disclosed publicly-traded company, CVE Numbering Authority, CSA CAIQ availability, ISO 27001 and SOC 2 compliance program participation per the AI Trust Center listing. These structural transparency anchors are positive for the V and T dimensions despite the documentation gaps at the product-data-governance level.

## VERDICT Record

**Summary:** NeMo Guardrails scores 52/85 (Tier B) under VERDICT v0.3.1 Layer 0, reflecting strong verifiability and resilience (Apache 2.0 source visibility, zero CVEs in trailing 12 months, CISA KEV clear, NVIDIA CNA + formal PSIRT) alongside lower data-governance and containment scores tied to the architecturally-local OSS library scope and the sales-gated NVIDIA AI Enterprise tier.

**Risk Factor Summary by Use Case:**

| Use Case | Notes |
|----------|-------|
| Internal testing / sandbox development | Strong fit: full source visibility, no NVIDIA-bound telemetry, local execution, Apache 2.0 license; suitable for safety prototyping and adversarial testing of LLM-wrapped applications. |
| Credential-handling workflows | Mixed: the library executes in the developer's process with custom actions running unsanded; secure credential handling (environment variables, secret managers) is the deploying application's responsibility per documentation. Authentication for the server endpoint is not built in. |
| Cloud multi-tenant production agents | Documentation-gated for the NeMo Microservices commercial tier; the OSS library is single-tenant by deployment; multi-tenant isolation requires production-tier deployment under NVIDIA AI Enterprise with sales-gated configuration details. |
| Regulated-data workloads (HIPAA, GDPR, FedRAMP) | NVIDIA AI Trust Center participates in SOC 2, ISO 27001, ISO 27018, ISO 27701; product-level GDPR DPA, sub-processor list, and per-category retention disclosures are sales-gated. Suitable subject to enterprise-contract review for managed deployment; OSS library scope is limited to in-developer-environment processing. |

**Reference Information (options, not instructions):**

1. Organizations adopting the OSS library may pin `nemoguardrails` to specific PyPI versions and review the changelog before each upgrade, given the library's active development cadence (v0.19.0 LangChain 1.x compatibility, v0.20.0 series in December 2025).
2. For production microservice deployment under NVIDIA AI Enterprise, organizations may request the SOC 2 report, sub-processor list, DPA, and Helm chart default security configuration via NVIDIA sales contact before binding to the managed tier.
3. For applications wrapping NeMo Guardrails around external LLM providers (Anthropic, OpenAI, Google, AWS Bedrock, NVIDIA NIM, Hugging Face), organizations may review the upstream LLM provider's data flow terms separately, since the library acts as middleware and does not change the upstream provider's data handling.

**Bias Disclosure:** This evaluation uses Claude (Anthropic) as its tooling. Anthropic operates in the AI agent market and may compete with some evaluated vendors. VERDICT discloses this relationship in every report and applies identical evaluation criteria to all platforms regardless of their relationship to Anthropic.

*Additional structural disclosure (per evaluation prompt Special Considerations §1):* NVIDIA, the operator of NeMo Guardrails, has a multi-layer commercial and equity relationship with Anthropic. NVIDIA is a supplier of compute infrastructure to Anthropic, and Anthropic has committed up to USD 30 billion in Azure capacity (powered by NVIDIA) plus additional capacity up to 1 GW. Separately, as of November 2025, NVIDIA has committed to invest up to USD 10 billion in Anthropic, subject to closing conditions, per NVIDIA's SEC Form 10-Q (FY2026 Q3). VERDICT scoring is based exclusively on public data sources per the v0.3.1 framework, and no vendor revenue or paid certification influences this rating. Readers should weigh this multi-layer relationship when interpreting the evaluation.

## Future Evaluation Plan

- **Layer 1 (behavioral, free-tier):** Candidate for behavioral evaluation across the OSS library's five rail types (input, dialog, retrieval, execution, output) on a free-tier upstream LLM provider; would enable scoring of the E dimension and verification of cost-accuracy claims.
- **Layer C (continuous monitoring):** Routine 90-day re-check; trigger-based update on any new CVE assigned to `nemoguardrails`, CISA KEV addition, supply chain compromise of the PyPI package, or major security incident reported by two or more independent sources.
- **Documentation watch:** Re-evaluate D, I, C, and T dimensions if NVIDIA publishes a NeMo Microservices sub-processor list, makes the SOC 2 report publicly accessible, or formalizes default authentication and Helm chart security posture in public documentation.