# Cohere 評価結果サマリー

## 基本情報
- スコア: 42/85 (Layer 0)
- ランク: TBD / 69
- 評価日: 2026.05.15
- 対象バージョン: Cohere API プラットフォーム + North + Command / Embed / Rerank (公開ドキュメント時点)
- 運営: Cohere Inc. (カナダ連邦法人, Toronto)
- 独立性: ✅ Independent (Aleph Alpha との合併は 2026.04.24 発表だが規制・株主承認待ち)

## 次元スコア
- V (検証可能性): 14/20 — High。創業者・法人実体・ISO 27001/42001・SOC 2 Type II 認証確認、ただし SOC 2 報告書は mNDA ゲート、サブプロセッサー一覧は更新日非公開。
- R (耐性): 8/20 — Mid。CVE-2026-5752 (CVSS 9.3, Cohere Terrarium サンドボックスエスケープ) 1件、CISA KEV なし、SDK 供給網侵害なし。
- D (データ運用): 7/15 — Mid。DPA + SCCs + TIA、30日自動削除、ZDR 提供、ただし SaaS デフォルトは training opt-in。
- I (制御): 4/10 — Mid。JIT/RBAC・アカウント削除手順は公開、North 側の HITL・エージェント停止手順の公開アーキ詳細は限定的。
- C (封じ込め): 2/10 — Low。Terrarium はアーカイブ、North エージェントランタイムのサンドボックスプリミティブ公開ドキュメント欠落。
- T (透明性): 7/10 — High。ステータスページ・Secure AI Frontier Model Framework・バグバウンティ・ISO 42001 公開、ただし Terrarium インシデント開示速度は 62 日。

## 主要ポジティブ所見
- カナダ連邦法人として法人実体と創業者構成が一次ソースで一貫確認可能
- ISO 27001 + ISO 42001 + SOC 2 Type II の三冠認証
- マルチデプロイ構成 (VPC / オンプレ / Model Vault / クラウドマーケットプレイス) でデータフロー境界を顧客側に移譲可能と明文化
- DPA に EU 標準契約条項を組み込み、Schrems II 後の Transfer Impact Assessment を EU 法務支援下で実施
- Cohere SDK は 2025-2026 の Shai-Hulud / Mini Shai-Hulud / SANDWORM_MODE / LiteLLM 供給網侵害の影響を受けず
- 公開ステータスページ (status.cohere.com) で運用インシデント履歴を継続開示

## 主要リスク所見
- CVE-2026-5752 (CVSS 9.3 Critical): Cohere Terrarium の Pyodide/Node.js プロトタイプチェーン経由でサンドボックスホストへ root 実行。CERT/CC VU#414811 は通知から公開まで 61日、ベンダー status は "Unknown"
- Terrarium はアーカイブ EOL 化されたが、North エージェントランタイムの代替コンテインメントアーキの公開ドキュメントが見当たらず
- SaaS Platform のトレーニング利用は商用有料顧客でも opt-in がデフォルト (ダッシュボードトグルで opt-out 可)
- SOC 2 Type II 報告書アクセスは mNDA ゲート、サブプロセッサー一覧は Trust Center ポータルログイン必要

## インシデント
- CVE-2026-5752 (CVSS 9.3, Critical): Cohere Terrarium Python サンドボックスのプロトタイプチェーン経由ホスト root RCE。2026.04.14 公開, v1.0.1 (final) 2026.04.22 リリース、リポジトリ EOL アーカイブ。

## CISA KEV
- 該当なし (評価日時点で Cohere 関連 KEV エントリー未確認)

## パターン記録
- Pyodide-on-Node.js を分離境界として使う設計パターンは n8n (CVE-2025-68668), Grist (CVE-2026-24002) でも同種の Critical CVE が発生しており業界パターン。Cohere は patch ではなく archival で対応。

## バイアス開示
- VERDICT framework v1.1 Trigger 2 (NVIDIA cap-table compound) + Trigger 3 (NVIDIA NIM 非アームスレングス・チャネル) 同時発火。両者は本評価で開示済み。スコアは公開ソースのみで決定、ベンダー収益・有償認証は影響しない。

## HTMLカード用タグ
- tags: foundation-model, enterprise-ai, agentic-ai, sovereign-ai, canada, command-r, north, embed, rerank, nvidia-trigger2, nvidia-trigger3, iso-42001, aleph-alpha-pending
- incident_tags: cve-2026-5752, terrarium-sandbox-escape, pyodide, cert-vu-414811, repository-archived
- owner: Cohere Inc.

Score: 42/85
V: 14/20, R: 8/20, D: 7/15, I: 4/10, C: 2/10, T: 7/10
Dimensions verified: V+R+D+I+C+T = 42
Tier: C
Category: Foundation Model API · Enterprise AI Platform · Agentic AI · Retrieval and Embedding Infrastructure

═══ QA REVIEW ═══
Factual:   PASS — CVE-2026-5752 CVSS 9.3 verified against GHSA-cmpr-pw8g-6q6c and CERT/CC VU#414811. Corporate identity (Cohere Inc., Canadian federal, Toronto) verified against cohere.com/about and Trust Center. ISO 27001/42001 certifications verified against cohere.com/blog/iso-42001-and-iso-27001-certifications. Aleph Alpha merger framed as "subject to approval" per businesswire announcement 2026.04.24. No KNOWN_FACTS.md entries applicable.
Legal:     CLEAR — No intent attribution to Cohere, NVIDIA, Anthropic, or distribution partners. CERT non-coordination window stated as documented fact per public CERT timeline, not motive. No blocklist words applied to vendor. Positive findings included alongside risks in every dimension.
Quality:   CLEAR — Executive Summary opens with specific scoring finding. Bias Disclosure included verbatim. Japanese summary scores match English (V14/R8/D7/I4/C2/T7=42). Framework v1.1 Trigger 2 + Trigger 3 disclosed per Special Considerations sections 1 and 2 respectively. North documented as distinct evaluation surface. Aleph Alpha merger framed neutrally as pending.
Result:    CLEARED
══════════════

# VERDICT Evaluation Report — #069 Cohere

**Evaluation Number:** #069
**Platform:** Cohere (Command series + Embed + Rerank + North agentic AI platform)
**Type:** New evaluation
**Date:** 2026.05.15
**Evaluator:** VERDICT v0.3.1 engine
**Target version:** Cohere API platform (public documentation as of evaluation date); Command A / Command A Vision / Command R+ generative; Embed 4; Rerank 3.5; North (general availability)
**Framework:** VERDICT v0.3.1 (Layer 0)
**Previous evaluation:** None

---

## Executive Summary

Cohere Inc., a Canadian federal corporation headquartered in Toronto, scores 42/85 (Tier C) on VERDICT Layer 0 public documentation review. The platform demonstrates strong corporate identity transparency, formal certification posture (SOC 2 Type II, ISO 27001, ISO 42001), a published Secure AI Frontier Model Framework, a multi-jurisdictional Data Processing Addendum incorporating EU Standard Contractual Clauses, and a public status page with operational incident history. The Resilience dimension reflects one Critical-severity CVE in the trailing 12 months — CVE-2026-5752 (CVSS 9.3) in the Cohere Terrarium Python sandbox, disclosed via CERT/CC VU#414811 after a 61-day vendor non-response window per CERT's published timeline — and the affected project was archived rather than continued under maintenance. The Containment dimension is constrained by absent public architectural documentation for the North agentic workspace's tool and code execution boundary. Two VERDICT framework v1.1 disclosures fire concurrently: NVIDIA holds equity in both Anthropic (VERDICT's tooling provider) and Cohere across multiple funding rounds (Trigger 2), and Cohere maintains a co-engineered NVIDIA NIM channel relationship for Command-R distribution (Trigger 3, additive). A planned merger with Germany's Aleph Alpha GmbH was announced April 24, 2026 and remains subject to regulatory and shareholder approval at evaluation date.

## Scorecard

| Dimension | Score | Max | Rating |
|---|---|---|---|
| V — Verifiability | 14 | 20 | High |
| R — Resilience | 8 | 20 | Mid |
| D — Data Conduct | 7 | 15 | Mid |
| I — Identity & Control | 4 | 10 | Mid |
| C — Containment | 2 | 10 | Low |
| T — Transparency | 7 | 10 | High |
| **Total (Layer 0)** | **42** | **85** | **Tier C** |

**CISA KEV:** ❌ なし (No Cohere entry confirmed in CISA KEV catalog at evaluation date)

---

## Dimension Detail

### V — Verifiability (14/20, High)

| Criterion | Result | Score | Evidence |
|---|---|---|---|
| Developer / company identity | Cohere Inc., Canadian federal corporation, Toronto. Founders Aidan Gomez, Nick Frosst, Ivan Zhang named. Corporate registration + contact paths confirmed. | 4/4 | https://cohere.com/about ; https://cohere.com/security |
| Source code disclosure | Production Command / Embed / Rerank models closed-source. Research model weights (Command R, Command R+, Command R 08-2024) released on Hugging Face under CC-BY-NC-4.0 non-commercial license. Aya research model under Apache 2.0. SDKs (cohere PyPI, cohere-ai npm) open source. | 2/4 | https://huggingface.co/CohereLabs/c4ai-command-r-plus ; https://github.com/cohere-ai |
| Version management transparency | Public changelog at docs.cohere.com/changelog. Dated model releases (e.g., command-r-08-2024). | 3/3 | https://docs.cohere.com/changelog |
| Third-party dependency disclosure | Subprocessor list accessible via Trust Center (Secureframe-hosted) but public listing without clearly visible last-updated indicator. Third-party trackers report 9 subprocessors. | 1/3 | https://trustcenter.cohere.com/subprocessors ; https://sub-processors.com/company/cohere.com |
| Independent certification | SOC 2 Type II report exists but requires mutual NDA for access. ISO 27001 and ISO 42001 certifications announced June 2025. Annual SOC 2 audit cadence committed. | 2/4 | https://cohere.com/blog/iso-42001-and-iso-27001-certifications ; https://trustcenter.cohere.com/ |
| Functional reproducibility docs | Complete API reference + behavioral specs documented. | 2/2 | https://docs.cohere.com/reference |

**Positive findings:** Founder identity, Canadian federal incorporation, and global office footprint (Toronto, San Francisco, New York, London, Paris) are consistent across primary sources. The ISO 42001 certification (responsible AI management standard) is among the earlier certifications in the foundation-model peer group. Model versioning convention is dated and traceable.

**Recorded concerns:** SOC 2 Type II report access is gated by mutual NDA, limiting public verifiability. Open-weight Command R+ release license (CC-BY-NC-4.0) restricts use to non-commercial / research contexts; this is not equivalent to open-source software under OSI terms, and the boundary between open-weight research releases and the proprietary commercial Cohere API platform is material to procurement evaluation. Cumulative funding figures vary across third-party sources (Crunchbase ~$935M, operator statements ~$970M-$1.7B); the variance is documented but not reconciled to a single canonical figure.

### R — Resilience (8/20, Mid)

| Criterion | Result | Score | Evidence |
|---|---|---|---|
| CVE count (trailing 12 months) | 1 CVE: CVE-2026-5752. Range 1-2 → 3 points. CVSS 9.0+ penalty: -1. Net: 2. | 2/5 | https://github.com/advisories/GHSA-cmpr-pw8g-6q6c |
| Maximum CVSS severity | CVE-2026-5752 CVSS 9.3 (Critical). | 0/6 | https://www.kb.cert.org (VU#414811) |
| Patch response speed | CERT/CC notified vendor 2026.02.19; CERT/CC published VU#414811 on 2026.04.21; Terrarium v1.0.1 released 2026.04.22; total elapsed time 62 days (≥31 day threshold). | 0/3 | https://blog.barrack.ai/pyodide-sandbox-escape-cohere-terrarium-openai-codex/ |
| Structural issues | Single isolated incident; no pattern of recurring root cause across Cohere SDK / API platform. | 3/3 | (absence of additional public CVEs) |
| Supply chain compromise (trailing 12 months) | Cohere SDK packages (cohere PyPI, cohere-ai npm) not affected in Shai-Hulud / Mini Shai-Hulud / SANDWORM_MODE / Trivy / LiteLLM compromise waves. Cohere API keys appeared in credential-harvesting target lists of unrelated malicious npm packages but Cohere distribution channels themselves were not compromised. | 3/3 | https://www.mend.io/blog/mini-shai-hulud-is-back-172-npm-and-pypi-packages-compromised-in-latest-wave/ ; https://security.snyk.io/package/npm/cohere-ai |

**Positive findings:** Cohere's first-party SDK packages were not compromised during the multi-wave 2026 supply-chain campaigns that affected several adjacent AI SDK ecosystems (Mistral AI, OpenSearch, Guardrails AI, UiPath, TanStack). Snyk reports no direct vulnerabilities in cohere-ai npm. Cohere maintains an operational status page (status.cohere.com) with retained incident history.

**Recorded concerns:** CVE-2026-5752 was disclosed by CERT/CC after a documented 61-day non-coordination window per the public CERT advisory; CERT's live VU#414811 page records vendor status as "Unknown" and notes "We have not received a statement from the vendor" at the time of publication. The affected Terrarium project was archived rather than placed under continued maintenance, with v1.0.1 marked as the final release per CERT's updated advisory text. The underlying architectural decision — Pyodide on Node.js used as a security boundary — has produced similar Critical sandbox escapes in adjacent projects (CVE-2025-68668 n8n, CVE-2026-24002 Grist), and the Pyodide maintainers have publicly stated the library is not designed as a multi-tenant isolation primitive.

### D — Data Conduct (7/15, Mid)

| Criterion | Result | Score | Evidence |
|---|---|---|---|
| GDPR compliance disclosure | Multi-jurisdictional DPA with EU Standard Contractual Clauses (2021/06/04 EC-approved). Transfer Impact Assessment conducted with EU counsel. Schrems II safeguards documented. | 3/3 | https://trustcenter.cohere.com/ ; https://cohere.com/enterprise-data-commitments |
| Data minimization | SaaS Platform: training-use toggle default ON for commercial paying customers; opt-out available in dashboard ("Adjust the toggle to 'Off' to opt out"). Private and third-party cloud deployments: no customer data received by Cohere. | 1/3 | https://cohere.com/enterprise-data-commitments |
| AI training use | SaaS Platform default: customer prompts and generations may be used for training of Cohere models unless customer opts out via dashboard toggle. PII filtering applied before training use. Retention 30 days for logged data, then auto-delete (with stated exceptions for legal, contractual, or usage-policy enforcement). | 0/4 | https://cohere.com/enterprise-data-commitments |
| Sub-processor transparency | Subprocessor list available via Trust Center; public access via Secureframe portal; last-updated indicator not visible without portal login. | 1/3 | https://trustcenter.cohere.com/subprocessors |
| Data retention disclosure | 30-day retention for logged prompts/generations on SaaS Platform stated explicitly. Zero Data Retention option available for enterprise customers on request. Account deletion processed within 7 days. | 2/2 | https://cohere.com/enterprise-data-commitments |

**Positive findings:** Data Processing Addendum incorporates Standard Contractual Clauses and a documented Transfer Impact Assessment for EU-to-US transfers. Multiple deployment tiers offer differentiated data-handling postures: private VPC, on-premises, and third-party cloud marketplace deployments are publicly stated to remove Cohere from the data flow entirely. Zero Data Retention (ZDR) availability is documented for enterprise customers willing to make additional usage commitments. HIPAA BAA available for custom model development engagements.

**Recorded concerns:** The SaaS Platform tier defaults to opt-in for training use of customer prompts and generations; an enterprise procurement review should confirm the dashboard toggle state at onboarding. Subprocessor list public access is gated by Trust Center portal sign-in, reducing reproducibility for third-party verification. HIPAA BAA scope is limited to custom model development engagements and explicitly excludes Cohere SaaS services, which is a material boundary for healthcare deployments.

### I — Identity & Control (4/10, Mid)

| Criterion | Result | Score | Evidence |
|---|---|---|---|
| Emergency stop documentation | Self-delete account workflow documented (7-day processing). API key revocation documented. Procedure for in-flight inference halt or agent-execution emergency stop on North not publicly documented. | 2/4 | https://cohere.com/enterprise-data-commitments |
| Human-in-the-loop design | North characterized as "security-first agentic AI platform" with built-in governance; HITL defaults and granularity not publicly documented at architectural detail. | 1/3 | https://cohere.com/security ; https://cohere.com/north |
| Permission delegation transparency | Internal JIT and RBAC controls documented. Customer-side scope, tool delegation, and connector permission model for North not publicly documented in architectural detail. | 1/3 | https://trustcenter.cohere.com/ |

**Positive findings:** Internal access management uses JIT techniques and role-based least-privilege per Trust Center documentation. Self-service account deletion and API key revocation are documented.

**Recorded concerns:** Public documentation for North's agent execution control surface, HITL configuration, and connector permission scoping is limited. Procurement reviews would benefit from architectural diagrams covering these controls being added to public materials.

### C — Containment (2/10, Low)

| Criterion | Result | Score | Evidence |
|---|---|---|---|
| Sandbox design | Cohere Terrarium (the Python code execution sandbox for data agents) was archived as end-of-life after CVE-2026-5752. Replacement containment architecture for North's tool / code execution boundary not publicly documented. | 0/4 | https://github.com/advisories/GHSA-cmpr-pw8g-6q6c |
| Least privilege | Configurable in private and on-premises deployments where customer controls infrastructure. Default privilege model on SaaS / North not publicly detailed. | 1/3 | https://cohere.com/security |
| Tenant isolation | "Multi Tenant with logical customer segmentation" per Slack Marketplace disclosure. No public independent isolation audit; no past cross-tenant breach reported. | 1/3 | https://slack.com/marketplace/A056U9XEQ1W-cohere-ai |

**Positive findings:** Private deployments (VPC, on-premises, Model Vault) and third-party cloud marketplace deployments shift the operational containment boundary to the customer's or the cloud provider's environment, with Cohere documenting that it does not have access to customer infrastructure or data in those modes. No cross-tenant isolation breach is publicly reported for the Cohere SaaS API.

**Recorded concerns:** The archival of Terrarium following the CVE-2026-5752 disclosure leaves a documentation gap regarding the current sandbox architecture for Cohere-hosted code execution and agentic tool use. The CERT/CC advisory notes that the underlying Pyodide-on-Node.js pattern is not a security boundary by design, and several adjacent projects have shipped Critical sandbox escapes from the same architectural pattern. Public clarity on what containment primitives (gVisor, Firecracker, Sysbox, or equivalent) underlie North's agent runtime would strengthen this dimension materially.

### T — Transparency (7/10, High)

| Criterion | Result | Score | Evidence |
|---|---|---|---|
| CVE publication posture | CVE-2026-5752 published via GitHub Security Advisory (GHSA-cmpr-pw8g-6q6c) and CERT/CC. Public bug bounty program with Responsible Disclosure Policy. | 1/2 | https://github.com/advisories/GHSA-cmpr-pw8g-6q6c ; https://cohere.com/security |
| Incident disclosure speed | CVE-2026-5752 disclosure timing: CERT/CC notified vendor 2026.02.19; CERT/CC published 2026.04.21; vendor patch 2026.04.22 (62 days from CERT notification). Beyond 60-day threshold. | 0/2 | https://blog.barrack.ai/pyodide-sandbox-escape-cohere-terrarium-openai-codex/ |
| Security policy publication | Detailed technical and organizational measures at cohere.com/security and trustcenter.cohere.com. Encryption (TLS in transit; AES-256 at rest per partner disclosures), JIT access, RBAC, JIT/least-privilege, penetration testing cadence, cybersecurity insurance. | 2/2 | https://cohere.com/security ; https://trustcenter.cohere.com/monitoring |
| AI safety framework reference | ISO 42001 certification achieved. Cohere Secure AI Frontier Model Framework published (PDF). Referenced in METR Common Elements of Frontier AI Safety Policies comparative analysis. | 2/2 | https://cohere.com/blog/iso-42001-and-iso-27001-certifications ; https://cohere.com/security/the-cohere-secure-ai-frontier-model-framework-february-2025.pdf |
| AI system identity disclosure | Model identity disclosed by default in API responses and documentation; product family naming consistent. | 2/2 | https://docs.cohere.com/reference |

**Positive findings:** Cohere maintains a public operational status page, a published Secure AI Frontier Model Framework, ISO 42001 certification (responsible AI management), a documented bug bounty program with Responsible Disclosure Policy, and detailed security documentation through both cohere.com/security and the Trust Center.

**Recorded concerns:** Per public CERT/CC records for VU#414811, vendor status was recorded as "Unknown" through the disclosure window, and the patch arrived one day after CERT's coordinated disclosure deadline expired. A documented post-incident process — including a security advisory issued by Cohere on its own surfaces with attribution to the reporter and timeline narrative — would strengthen this dimension. Independent verification: no Cohere-issued public advisory linked to CVE-2026-5752 was located via web search during this evaluation.

---

## Incident Timeline

| Date | CVE ID | CVSS | Description | Patch status | KEV |
|---|---|---|---|---|---|
| 2026.04.14 | CVE-2026-5752 | 9.3 (Critical) | Sandbox escape in Cohere Terrarium Python sandbox via JavaScript prototype chain traversal; root code execution on host process. Affected: Cohere Terrarium (Python sandbox for LLM-generated code execution, Pyodide / Node.js based, Docker-deployed). | v1.0.1 released 2026.04.22 as final release; project archived end-of-life per CERT/CC updated advisory. | ❌ Not in CISA KEV |

CERT/CC VU#414811 reports vendor notification 2026.02.19; CERT publication 2026.04.21; vendor patch 2026.04.22 (62 days from CERT notification, 16 days past CERT's standard 45-day disclosure window per the published advisory).

---

## Contextual Analysis

Cohere occupies a distinct position among foundation model providers as the largest enterprise-focused AI lab headquartered outside the United States, with Canadian federal incorporation, a stated cloud-agnostic deployment model, and a publicly-disclosed sovereign AI positioning. The platform's commercial surface is structured across multiple tiers: a Cohere-hosted SaaS API tier, cloud marketplace tiers via Oracle Cloud Infrastructure, Microsoft Azure AI Foundry, AWS Bedrock, and Google Cloud Vertex AI, the NVIDIA NIM distribution channel, and private VPC, on-premises, and Model Vault sovereign deployments. Each tier shifts the data-flow and operational-trust boundary differently, with Cohere's role in private and third-party cloud tiers being characterized publicly as model and software provider rather than data processor.

The certification posture (SOC 2 Type II, ISO 27001, ISO 42001) is consistent with enterprise foundation-model peer expectations. The ISO 42001 certification for responsible AI management is among the earlier such certifications in the foundation-model peer cohort.

The CVE-2026-5752 incident in Cohere Terrarium is technically isolated to one repository — Terrarium, a Python sandbox specifically designed for LLM-generated code execution — but materially relevant for procurement reviews of agentic deployments. The CERT/CC public timeline documents 61 days between vendor notification and CERT publication. The patch was released one day after CERT's publication and the repository was simultaneously archived as end-of-life. Cohere's vendor status on the live VU#414811 advisory remains recorded as "Unknown" per public CERT records, and no vendor statement is filed. The architectural pattern at issue (Pyodide-on-Node.js used as an isolation boundary) is the same pattern that produced Critical CVEs in adjacent projects including n8n (CVE-2025-68668) and Grist (CVE-2026-24002), and the Pyodide maintainers have publicly stated the library is not designed as a multi-tenant isolation primitive. Cohere's response — archival rather than continued patching — is a documented design decision, and the absence of public architectural detail on the current containment primitives used for North's agent runtime is a material documentation gap rather than a security finding per se.

The cloud-agnostic deployment posture is materially distinct from a single-tenant SaaS-only platform: in private VPC, on-premises, and cloud marketplace tiers, Cohere publicly states it does not receive customer prompts or generations, which substantially changes the data-conduct posture from the SaaS API tier. The SaaS API tier itself defaults to training opt-in for paying commercial customers, with an easy dashboard toggle to opt out, 30-day automatic retention for logged data, PII filtering before training use, and a Zero Data Retention option available for enterprise customers on request.

The pending Aleph Alpha merger announced 2026.04.24 (Cohere as surviving entity, $500M EUR Schwarz Group structured financing commitment, dual Toronto-Heidelberg operational footprint) is subject to regulatory and shareholder approval at evaluation date and does not affect the Layer 0 evaluation; the corporate operator continues to be Cohere Inc. (Canadian federal corporation) under publicly documented terms. A material change in corporate structure post-merger-closing would trigger a re-evaluation flag under the 90-day routine check or under the V dimension differential evaluation rules.

---

## Special Considerations

### 1. NVIDIA cap-table compound investor structure (framework v1.1 Trigger 2)

Cohere's strategic investor cohort includes NVIDIA across multiple funding rounds including the Series D ($500M, July 2024 at $5.5B valuation) and Series D extension ($100M, September 2025 at $7B valuation). As of November 2025, NVIDIA also holds a strategic equity commitment in Anthropic (up to USD 10 billion, subject to closing conditions per NVIDIA SEC Form 10-Q FY2026 Q3). This is a compound investor structure under VERDICT framework v1.1: NVIDIA holds equity positions in both the evaluator (Anthropic, operator of VERDICT) and the evaluated platform (Cohere). VERDICT scoring is based exclusively on public data sources per the v0.3.1 framework, and no vendor revenue or paid certification influences the rating.

### 2. NVIDIA non-arms-length channel relationship (framework v1.1 Trigger 3, additive)

Cohere also has a publicly-disclosed commercial channel relationship with NVIDIA beyond standard supplier-customer relations, including: Cohere's Command-R model published as a NVIDIA NIM microservice with co-engineering optimization for NVIDIA-accelerated infrastructure; Command-R availability on the NVIDIA API Catalog (ai.nvidia.com); and a joint GTC 2024 panel featuring Cohere CEO Aidan Gomez alongside NVIDIA CEO Jensen Huang. The operator publicly characterizes the partnership as deepened collaboration with NVIDIA per its own communications. This channel relationship is additive to the cap-table relationship described in Section 1 and constitutes a non-arms-length channel under VERDICT framework v1.1 Trigger 3.

### 3. Cohere North agentic platform (distinct evaluation surface)

North is a distinct product surface within the Cohere product family, characterized by the operator as a "security-first agentic AI platform" combining LLMs, search, and AI agents into an enterprise workspace. North's containment, identity, and audit characteristics are evaluated against its own published documentation, and the engine notes that public architectural detail for North's agent execution sandbox, connector permission model, and HITL defaults is limited at evaluation date. North's characteristics are not conflated with the foundation model API tier or vice versa.

### 4. Pending Aleph Alpha merger (informational)

The April 24, 2026 announcement of Cohere's planned merger with Aleph Alpha GmbH (Germany), with Schwarz Group structured financing, is publicly characterized as subject to regulatory and shareholder approval and has not closed at evaluation date. The corporate operator at evaluation date is Cohere Inc. (Canadian federal corporation). A material change in operator identity post-merger-closing would trigger differential re-evaluation under VERDICT v0.3.1 V dimension rules.

---

## Economic Risk (P dimension)

No material economic risk identified in public documentation for this evaluation. API pricing is published per-token at https://cohere.com/pricing; usage-based billing is documented; no public reports of unexpected charges or runaway-cost incidents in the trailing 12 months were located.

---

## VERDICT Record

**Summary:** Cohere scores 42/85 (Tier C) under VERDICT v0.3.1 Layer 0 review, with the Resilience and Containment dimensions reflecting CVE-2026-5752 (CVSS 9.3, 62-day CERT notification window) and absent public architectural documentation for North's agent runtime; the Verifiability and Transparency dimensions reflect strong corporate identity transparency, ISO 27001 / ISO 42001 / SOC 2 Type II certifications, and a published AI safety framework.

### Risk Factor Summary by Use Case

| Use case | Risk factor summary |
|---|---|
| Internal testing / proof-of-concept | The SaaS Platform free / commercial tier is accessible without enterprise contracting; default training opt-in toggle and 30-day log retention should be reviewed and adjusted before submitting confidential test data. |
| Credential-handling / secrets workflows | Cohere SDK packages were not affected in 2026 supply-chain compromise waves; verify SDK provenance and consider zero data retention configuration if processing credentials adjacent to model inputs. |
| Cloud multi-tenant deployments | The Cohere-hosted SaaS API operates as multi-tenant with logical customer segmentation; private VPC, Model Vault, and cloud marketplace deployments (OCI, Azure AI Foundry, AWS Bedrock, Google Cloud Vertex AI) shift the tenant-isolation boundary to the customer's infrastructure or to the cloud marketplace provider's isolation guarantees. CVE-2026-5752 in Cohere Terrarium has been resolved through archival of that project; current sandbox primitives for North agent execution are not publicly documented. |
| Regulated-data workloads (healthcare, finance, public sector) | DPA with EU Standard Contractual Clauses, Transfer Impact Assessment, ISO 27001, ISO 42001, and SOC 2 Type II are documented; HIPAA BAA available for custom model development engagements only (excludes Cohere SaaS services). Sovereign AI deployments, on-premises, and Model Vault tiers are publicly characterized as appropriate for highly-regulated workloads with stronger data residency guarantees. |

### Reference Information

- For the deployment surface where Cohere does not receive customer data (private VPC, on-premises, Model Vault, third-party cloud marketplace tiers), procurement reviews can refer to the documented separation in https://cohere.com/enterprise-data-commitments.
- For multi-jurisdictional data transfers, the Cohere DPA, Standard Contractual Clauses, and Transfer Impact Assessment are referenced at https://trustcenter.cohere.com/.
- For the open-weight Command R+ research release, the CC-BY-NC-4.0 license terms restrict commercial use; the Cohere API is the commercial path for production deployments of Command-family models.

### Bias Disclosure

This evaluation uses Claude (Anthropic) as its tooling. Anthropic operates in the AI agent market and may compete with some evaluated vendors. VERDICT discloses this relationship in every report and applies identical evaluation criteria to all platforms regardless of their relationship to Anthropic.

---

## Future Evaluation Plan

- **Layer 1 (behavioral testing):** 30-run × 4-difficulty-level evaluation of Command A / Command A Vision foundation models for task success rate, cost accuracy, and sustained performance degradation. Free-tier feasibility to be confirmed. Suggested earliest scheduling: Q3 2026.
- **Layer C (continuous monitoring):** Monitor NVD / GitHub Advisories / CISA KEV / PyPI OSV / npm OSV for cohere-ai package and Cohere platform CVEs on weekly cadence. Trigger re-evaluation if any new CVE with CVSS 7.0+, CISA KEV listing, supply chain compromise, or major incident with two-source confirmation is published.
- **Differential evaluation triggers:** Closing of the Aleph Alpha merger (V, T re-check), any North platform architectural disclosure update (C, I re-check), publication of post-incident security advisory for CVE-2026-5752 by Cohere on its own surfaces (T re-check), or 90 days from this evaluation (2026.08.13 routine check).