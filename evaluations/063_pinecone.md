# Pinecone 評価結果サマリー

## 基本情報
- スコア: 71/85 (Layer 0)
- ランク: TBD / 63 (インデックス反映待ち)
- 評価日: 2026.05.12
- 対象バージョン: Pinecone Serverless (GA), BYOC public preview (multi-cloud, 2026.02), Python SDK pinecone v8.x, TypeScript SDK @pinecone-database/pinecone v6.x
- 運営: Pinecone Systems, Inc. (デラウェア州 C-corp、本社 NY)
- 独立性: ✅ Independent (Anthropicとの資本関係なし。Andreessen Horowitz主導のSeries Bなど計$138M調達)

## 次元スコア
- V (検証可能性): 16/20 — 運営主体・ライセンス・サブプロセッサ公開リスト・SOC 2 Type II 2025ゼロ偏差・ISO 27001:2022更新監査済み (SOC 2レポートはSafeBase経由のアクセス制限あり)
- R (耐性): 20/20 — 直近12ヶ月のPinecone製品CVEゼロ、CISA KEVなし、Shai-Hulud/Axios/Vercel(Context.ai)について「影響なし」声明をTrust Centerに掲載
- D (データ運用): 11/15 — DPA公開・SCC Module 2&3+UK Addendum+Swiss FADP完備、AI Services Addendum §5で「Pineconeは他顧客向け共有Modelの学習にCustomer Dataを使用しない」と明記。テレメトリのデフォルトポジションは未開示
- I (制御): 8/10 — Control plane/Data plane分離APIキー、組織/プロジェクト2層RBAC、SAML SSO、サービスアカウントGA。MFAは "Coming Soon" 表示
- C (封じ込め): 8/10 — Namespace隔離 (公式に多テナンシー第一推奨)、BYOC zero-access運用モデル (SSH/VPN/inbound不要)、CMEK GA (2026.03)、Private Endpoint。デフォルトAPIキーは広範権限
- T (透明性): 8/10 — SafeBase Trust Centerに10カテゴリ超のポリシー、Status pageで公開インシデント年表、AI Services AddendumがEU AI Actを参照しPinecone Assistant出力の人間生成偽装を契約で禁止

## 主要ポジティブ所見
- SOC 2 Type II 2025年監査をゼロ偏差で完了 (Trust Centerに公開声明)
- ISO 27001:2022更新監査 active、IAF CertSearch経由で第三者検証可能
- AI Services Addendum §5に明示的なno-training条項 (共有Modelへの学習・再学習・fine-tune禁止)
- DPAが公開URLで取得可能、SCC Module 2/3 + UK Addendum + Swiss FADPフルカバー
- EDPOがGDPR Article 27代理人 (EU/UK両方)
- 業界サプライチェーン事象 (Shai-Hulud, Shai-Hulud 2.0, Axios, Vercel/Context.ai) すべてに肯定的影響なし声明を実施
- BYOCゼロアクセス運用モデルでベクター・メタデータ・クエリが顧客環境を離れない
- 2026.05.06 のマイナー障害2件いずれも28分以内に解決、公開タイムライン付き
- HIPAA: Standardプラン$190/月アドオン or Enterprise

## 主要リスク所見
- MFAが "Coming Soon" 表示のまま (SSO非利用顧客にとっての認証面のギャップ)
- AI Services (Pinecone Assistant, Pinecone Inference) はAI Services Addendum §7(e)によりデフォルトでBAAスコープ外、別途書面合意が必要
- SOC 2 Type II / Pentest / HIPAAレポートはSafeBase経由のアクセス制限 (業界標準だが公開検証性を制限)
- BYOCはマルチクラウド構成では2026.02時点でpublic preview (GAではない)
- /legal/subprocessors/ ページの最終更新日 2024-05-24 がTrust Center版より古く同期不完全
- テレメトリのデフォルト収集ポジションが公開資料に明記なし (Silence-is-dataルールにより該当項目0点)
- デフォルト発行APIキーは広範権限 (least-privilegeは設定可能だがデフォルトではない)

## インシデント
- 直近12ヶ月の公開Pinecone製品CVEなし (NVD, GHSA, OSV検索済み)
- "pinecone" でヒットする2件 (matrix-org/pinecone P2P routing, WordPress AI ChatBotプラグイン) はPinecone Systems製品ではない

## CISA KEV
- なし (2026.05.12時点でPinecone関連エントリ確認できず)

## パターン記録
- ベクターデータベース・カテゴリのVERDICT初回評価。C次元は「multi-tenant index isolation + namespace + BYOC + CMEK」へ正式に意味調整
- AnthropicとPinecone Assistantの直接的な商用関係 (Claude Sonnet 4.5自動ルーティング) を中立的事実として記録、Bias Disclosure節で開示済み
- Trust Centerの「肯定的非影響声明」パターン (4件) は閉鎖SaaS提供者として透明性スコアにプラス寄与

## HTMLカード用タグ
- tags: vector-database, retrieval-infrastructure, pinecone-serverless, BYOC, CMEK, RAG, multi-cloud, soc2-type2, iso27001, hipaa-addon
- incident_tags: zero-cve-12mo, no-cisa-kev, shai-hulud-unaffected, axios-unaffected, vercel-context-unaffected
- owner: Pinecone Systems, Inc. (Delaware C-corp / NY HQ)
- tier: S
- category: Vector Database · Retrieval Infrastructure

═══ QA REVIEW ═══
Factual:   PASS — All CVE/KEV searches returned no Pinecone-product entries in trailing 12 months. SOC 2 Type II 2025 (zero deviations) and ISO 27001:2022 surveillance audit verified on Trust Center. DPA / AI Services Addendum / Privacy Policy / MSA all verified at pinecone.io/legal/. No KNOWN_FACTS.md entry exists for Pinecone.
Legal:     PASS — No intent attribution, no inflammatory language, positive and negative findings recorded in parallel, vendor position represented fairly in Contextual Analysis.
Quality:   PASS — All mandatory sections present. Bias Disclosure verbatim. C-dimension adaptation explicitly noted. Pinecone Assistant Claude commercial relationship recorded neutrally. Japanese summary scores match English report exactly.
Result:    CLEARED
══════════════

# VERDICT Evaluation #063 — Pinecone

| Field | Value |
|-------|-------|
| Evaluation Number | #063 |
| Platform | Pinecone (Pinecone Serverless + Pinecone Assistant + Pinecone Inference + BYOC) |
| Evaluation Type | Initial (Layer 0) |
| Evaluation Date | 2026.05.12 |
| Evaluator | VERDICT evaluation engine v0.3.1 |
| Target Version | Pinecone Serverless (current GA); BYOC public preview (multi-cloud, Feb 2026); Python SDK `pinecone` v8.x; TypeScript SDK `@pinecone-database/pinecone` v6.x |
| Framework | VERDICT v0.3.1 (Layer 0) |
| Previous Evaluation | None (first evaluation; first vector database category under VERDICT framework) |

## Executive Summary

Pinecone scores 71/85 on Layer 0 public-documentation review. Across the six scored dimensions, every dimension reaches the High rating threshold (V 16/20, R 20/20, D 11/15, I 8/10, C 8/10, T 8/10). The Resilience dimension is the strongest data point: no CVEs were confirmed against Pinecone Systems products in the trailing twelve months, no entries appear in the CISA KEV catalog, and the Trust Center carries affirmative not-affected statements for the Shai-Hulud and Shai-Hulud 2.0 NPM worm campaigns, the Axios package compromise, and the Vercel / Context.ai April 2026 incident. The publicly available Data Processing Addendum (May 2024) incorporates SCC Modules 2 and 3, the UK Addendum, and the Swiss FADP, and the AI Services Addendum (January 2025) §5 includes an explicit no-training commitment for any shared model. Documentation gaps recorded for transparency: multi-factor authentication is currently published as "Coming Soon," the SOC 2 Type II report is access-gated through the SafeBase Trust Center, and Pinecone Assistant is by default excluded from the scope of any executed BAA.

## Scorecard

| Dimension | Score | Max | Rating |
|-----------|-------|-----|--------|
| V — Verifiability | 16 | 20 | High |
| R — Resilience | 20 | 20 | High |
| D — Data Conduct | 11 | 15 | High |
| I — Identity & Control | 8 | 10 | High |
| C — Containment | 8 | 10 | High |
| T — Transparency | 8 | 10 | High |
| **Layer 0 Total** | **71** | **85** | **—** |

**CISA KEV:** なし (No Pinecone-related entries in the CISA Known Exploited Vulnerabilities catalog as of 2026.05.12.)

**Tier:** S (71/85 = 83.5%)
**Category:** Vector Database · Retrieval Infrastructure

Score: 71/85
V: 16/20, R: 20/20, D: 11/15, I: 8/10, C: 8/10, T: 8/10
Dimensions verified: V+R+D+I+C+T = 71

## Dimension Detail

### V — Verifiability (16/20)

| Criterion | Result | Score | Evidence |
|-----------|--------|-------|----------|
| Developer / company identity | Pinecone Systems, Inc. (Delaware C-corp); NY State DOS #6443133; HQ 1375 Broadway, 11th Fl, New York, NY 10018; privacy@pinecone.io | 4/4 | https://www.pinecone.io/legal/data-processing-addendum/ ; https://opengovny.com/corporation/6443133 |
| Source code disclosure | SDKs (Python, TypeScript, Java) open-source under pinecone-io GitHub organization; vector database engine itself is closed-source SaaS | 2/4 | https://github.com/pinecone-io |
| Version management transparency | Year-by-year release notes published (2022–2026); per-SDK GitHub release pages with full changelog | 3/3 | https://docs.pinecone.io/release-notes/2026 ; https://github.com/pinecone-io/pinecone-python-client/releases |
| Third-party dependency disclosure | Public subprocessor list at /legal/subprocessors/ dated 2024-05-24; Trust Center carries current subprocessor view (AWS, Azure, Confluent, Salesforce, Pylon, Zendesk, Databricks) | 3/3 | https://security.pinecone.io/ ; DPA §5 |
| Independent certification | SOC 2 Type II 2025 completed with zero deviations; ISO 27001:2022 surveillance audit active (publicly verifiable via IAF CertSearch); HIPAA, GDPR, CCPA documented. SOC 2 report access-gated through SafeBase | 2/4 | https://security.pinecone.io/ ; https://www.pinecone.io/security/ |
| Functional reproducibility docs | Full API reference, integration guides, models documentation, examples library | 2/2 | https://docs.pinecone.io/ |

**Positive findings.** SOC 2 Type II 2025 completed with zero deviations is published on the Trust Center as an affirmative statement. ISO 27001:2022 surveillance audit certificate is verifiable through the IAF CertSearch database independently of Pinecone's own materials. Operator entity is consistently named (Pinecone Systems, Inc., Delaware corporation) across MSA, DPA, Privacy Policy, AI Services Addendum, Security Measures document, and corporate footer. Subprocessor list is published with an authoritative URL referenced in the DPA itself.

**Recorded concerns.** Source code for the vector database engine is closed; only the client SDKs are open. SOC 2 Type II report is access-gated (NDA-style) through SafeBase rather than publicly summarized. The subprocessor legal page carries a last-updated date of 2024-05-24, which is older than the Trust Center version where additional subprocessors (Salesforce, Pylon) are now visible; alignment between the two surfaces is incomplete.

### R — Resilience (20/20)

CVE evaluation period: 2025.05.12 – 2026.05.12.

| Criterion | Result | Score | Evidence |
|-----------|--------|-------|----------|
| CVE count (trailing 12 months) | 0 CVEs attributed to Pinecone Systems products | 5/5 | https://github.com/advisories?query=pinecone (the two "pinecone" hits are matrix-org/pinecone P2P routing and a WordPress AI ChatBot plugin, both unrelated) |
| Maximum CVSS severity | No CVEs → 0–3.9 effectively | 6/6 | NVD search; OSV.dev |
| Patch response speed | Visible rapid dependency-lockfile updates (CVE-2026-22815 aiohttp, pygments ReDoS) and operational incident resolution (28 minutes on 2026-05-06) | 3/3 | https://github.com/pinecone-io/pinecone-python-client/releases ; https://status.pinecone.io/ |
| Structural issues | Two minor incidents on 2026-05-06 are independent (AWS us-east-1 5xx; Console hosting slowness); no recurring root cause documented | 3/3 | https://status.pinecone.io/ |
| Supply chain compromise (trailing 12 months) | Trust Center affirmatively confirms "not affected" for Shai-Hulud, Shai-Hulud 2.0, Axios, and Vercel/Context.ai (April 2026) with documented audit and monitoring | 3/3 | https://security.pinecone.io/ |

**Positive findings.** Zero Pinecone-product CVEs in the trailing twelve months. Trust Center carries four distinct affirmative supply-chain disclosure statements within the evaluation window. Status page incidents are documented with timestamped status transitions (Investigating → Identified → Monitoring → Resolved) and are visible publicly without authentication.

**Recorded concerns.** The two NVD/GHSA hits for the keyword "pinecone" relate to unrelated software (matrix-org P2P routing, a WordPress plugin); engine confirms they are not Pinecone Systems products. Patch-response and structural-issue scoring is partly inferential because there are no Pinecone-product CVEs to time, but the dependency-bump cadence in the Python SDK lockfile and 28-minute incident resolution on 2026-05-06 are direct observable proxies.

### D — Data Conduct (11/15)

| Criterion | Result | Score | Evidence |
|-----------|--------|-------|----------|
| GDPR compliance disclosure | DPA publicly available; SCCs Modules 2 & 3 explicitly incorporated; UK Addendum incorporated; Swiss FADP covered; EDPO appointed as Article 27 representative for EU and UK | 3/3 | https://www.pinecone.io/legal/data-processing-addendum/ |
| Data minimization | Telemetry default position not explicitly documented in public materials | 0/3 | (silence) |
| AI training use | AI Services Addendum §5: "Pinecone will not use Customer Data to train, retrain or fine-tune any Model that Pinecone makes available to other Pinecone customers." Retention defined per DPA Schedule 1 | 4/4 | https://www.pinecone.io/legal/2025.1_Pinecone%20AI%20Services%20Addendum.pdf |
| Sub-processor transparency | Public list with last-updated date and 15-day objection window documented in DPA §5.3 | 3/3 | DPA §5 |
| Data retention disclosure | DPA Schedule 1 covers term-of-Agreement retention plus post-termination retrieval period and legally-required period; per-category granularity is partial | 1/2 | DPA §9, Schedule 1 |

**Positive findings.** The AI Services Addendum (Last updated 2025-01-22) §5 contains an explicit no-training commitment for any shared model. The DPA is publicly accessible at the legal URL rather than gated behind sales contact, and incorporates the full SCC framework with Module 2 (controller-to-processor) and Module 3 (processor-to-subprocessor) selections specified in §11.3. EDPO is appointed as both the EU GDPR Article 27 representative and the UK GDPR representative.

**Recorded concerns.** The no-training clause is scoped to "any Model that Pinecone makes available to other Pinecone customers," which is a strong limitation on shared-model training but leaves theoretical scope for non-shared-model uses. Telemetry default position (collection of usage data from customer SDK calls and console activity) is not explicitly disclosed in public materials; per the Silence-is-data rule this scored as zero. Post-deletion backup retention is not explicitly stated.

### I — Identity & Control (8/10)

| Criterion | Result | Score | Evidence |
|-----------|--------|-------|----------|
| Emergency stop documentation | Deletion protection feature documented; API key revocation and rotation documented; pause/halt of autonomous operations not directly applicable (no autonomous execution surface) | 2/4 | https://www.pinecone.io/security/ ; https://docs.pinecone.io/guides/production/security-overview |
| Human-in-the-loop design | Vector database and Pinecone Assistant operate request-response; no autonomous loop runs without customer-initiated API calls | 3/3 | docs.pinecone.io |
| Permission delegation transparency | API key roles documented with control plane / data plane separation; RBAC at organization and project levels; SAML SSO; service accounts GA at organization and project levels (March 2026) | 3/3 | https://www.pinecone.io/security/ ; https://docs.pinecone.io/release-notes/2026 |

**Positive findings.** Control-plane and data-plane API-key role separation is explicitly documented. Service accounts at organization and project levels were promoted to GA in March 2026, extending least-privilege options. Audit logs were also promoted to GA in March 2026 with a documented event schema and identity-typed actor records (user, api_key, service_account).

**Recorded concerns.** Multi-factor authentication is marked "Coming Soon" on the security page as of evaluation date, which is a notable gap for an enterprise vector-database platform processing potentially sensitive embeddings. SSO mitigates this for federated identity flows but does not cover all credential paths.

### C — Containment (8/10)

**Dimension adaptation note.** Pinecone is a vector database and does not execute customer code, so the C dimension here evaluates multi-tenant index isolation, namespace separation, BYOC infrastructure isolation, and customer-managed encryption keys rather than sandbox-level code-execution isolation. This is the first vector database category evaluation under VERDICT and the adaptation is recorded for framework precedent.

| Criterion | Result | Score | Evidence |
|-----------|--------|-------|----------|
| Sandbox design (adapted: multi-tenant index isolation) | Namespace-based isolation is the documented multi-tenancy pattern (Jan 2026 release note explicitly recommends namespace-based isolation); BYOC offers infrastructure-level isolation; API-key whitelist + project-scoped permissions | 4/4 | https://docs.pinecone.io/release-notes/2026 ; https://docs.pinecone.io/guides/production/bring-your-own-cloud |
| Least privilege | API key roles configurable for control-plane and data-plane separation; default key carries broad permissions; least privilege achievable but not default | 1/3 | https://docs.pinecone.io/guides/production/security-overview |
| Tenant isolation (cloud) | SOC 2 Type II zero deviations 2025; ISO 27001:2022 surveillance audit active; CMEK GA (March 2026); private endpoints; BYOC zero-access operating model | 3/3 | https://security.pinecone.io/ ; https://docs.pinecone.io/guides/production/configure-cmek |

**Positive findings.** The Feb 2026 BYOC public-preview release note specifies a zero-access operating model where Pinecone never needs SSH, VPN, or inbound network access into the customer environment and where vectors, metadata, and queries never leave the customer's cloud account. CMEK was promoted to GA in March 2026, allowing data within a Pinecone project to be encrypted under customer-managed keys. The Jan 2026 release note on metadata filter limits explicitly recommends namespace-based isolation over filter-based access control, framing namespace isolation as the operationally preferred multi-tenancy primitive.

**Recorded concerns.** Default API keys created at project provisioning carry broad permissions; explicit configuration is required to enforce least privilege. The boundary between Pinecone-operated control plane and customer-operated BYOC data plane is described at a high level in the release notes but a complete public architectural diagram covering control-plane data flow back to Pinecone is not visible without engaging the Trust Center document gate.

### T — Transparency (8/10)

| Criterion | Result | Score | Evidence |
|-----------|--------|-------|----------|
| CVE publication posture | No CVEs assigned to Pinecone products; Trust Center publishes supply-chain advisories under Vulnerabilities and Incidents categories | 1/2 | https://security.pinecone.io/ |
| Incident disclosure speed | Vercel/Context.ai (Apr 19, 2026) acknowledged on Trust Center within days; Shai-Hulud campaign acknowledged during active campaign; 2026-05-06 incidents resolved in 28 minutes with public timeline | 2/2 | https://security.pinecone.io/ ; https://status.pinecone.io/ |
| Security policy publication | SafeBase Trust Center with 10+ policy categories (Acceptable Use, Access Control, Anti-Malicious Software, Asset Management, Backup, etc.); Technical and Organizational Security Measures published at /legal/security-measures.pdf | 2/2 | https://security.pinecone.io/ ; https://www.pinecone.io/legal/security-measures.pdf |
| AI safety framework reference | AI Services Addendum references EU AI Act ((EU) 2024/1689) by name and prohibits prohibited-AI-practice uses; NIST AI RMF or ISO/IEC 42001 mapping not visible publicly | 1/2 | AI Services Addendum §1, §6.2 |
| AI system identity disclosure | Pinecone Assistant chat playground identifies the underlying LLM by name in the model dropdown; AI Services Addendum classifies Outputs as Customer Data with explicit "do not mislead anyone that Output is human generated" clause | 2/2 | https://docs.pinecone.io/guides/assistant/chat-with-assistant ; AI Services Addendum §4 |

**Positive findings.** The Trust Center pattern of affirmative not-affected statements during industry-wide supply-chain incidents (Shai-Hulud, Axios, Vercel/Context.ai) is an unusually visible posture for a closed-source SaaS vendor. The status page provides public incident timelines with status transitions visible without authentication. The AI Services Addendum §4 explicitly prohibits customers from misrepresenting AI-generated Outputs as human-generated, which is a stronger AI-identity-disclosure stance than many comparable platforms publish.

**Recorded concerns.** The Trust Center reports (SOC 2, HIPAA, Pentest) are access-gated through SafeBase; while access is granted on request, the gating limits independent third-party verification. NIST AI RMF or ISO/IEC 42001 framework adoption is not explicitly published at evaluation date; the EU AI Act reference in the AI Services Addendum is the closest published external-framework anchor.

## Incident Timeline

No CVEs were confirmed against Pinecone Systems products in the trailing twelve months (2025.05.12 – 2026.05.12) in NVD, GHSA, or OSV search results.

Supply-chain-adjacent affirmative disclosure events recorded on the Trust Center within the evaluation window:

| Date | Type | Description | Pinecone Position |
|------|------|-------------|------------------|
| 2026.04.19+ | Industry incident (Vercel / Context.ai OAuth) | Vercel disclosed unauthorized access to internal Vercel systems involving the Context.ai OAuth application | Not affected; Context.ai never installed or authorized in Pinecone Google Workspace; environment variables rotated as precaution |
| 2026.Q1 | Industry incident (Axios NPM compromise) | Supply-chain attack targeting the axios NPM package | Not affected; comprehensive infrastructure and dependency audit confirmed; monitoring and detection logic deployed |
| 2025–2026 | Industry incident (Shai-Hulud / Shai-Hulud 2.0 NPM worm) | Active worm campaigns against the NPM ecosystem | Not affected; audit confirmed; worm-specific monitoring and detection logic deployed |
| 2025 | Compliance milestone | SOC 2 Type II 2025 audit | Completed with zero deviations |

## Contextual Analysis

Pinecone is operated by Pinecone Systems, Inc., a Delaware C-corporation headquartered at 1375 Broadway, 11th Floor, New York. Edo Liberty, the founder and prior CEO, transitioned to Chief Scientist in September 2025; Ash Ashutosh assumed the CEO role. Investors include Andreessen Horowitz (Series B lead, April 2023), ICONIQ Growth, Wing Venture Capital, Menlo Ventures, and Tiger Global, with total disclosed funding of $138M per LinkedIn. No equity relationship exists between Anthropic or Anthropic Ventures and Pinecone Systems per public investor records.

Pinecone Assistant integrates Anthropic Claude as a supported LLM provider. The January 2026 release notes document that Pinecone implemented operator-side routing logic to redirect chat requests specifying `claude-3-5-sonnet` or `claude-3-7-sonnet` to `claude-sonnet-4-5` following Anthropic's model deprecation, with no customer code changes required. This represents a direct commercial relationship in which Pinecone Assistant consumes the Anthropic Claude API and responds operationally to Anthropic's model lifecycle decisions. The relationship is recorded here as a structural fact; the Bias Disclosure below covers Anthropic's role as the tooling provider for the VERDICT evaluation itself.

The BYOC offering, promoted from initial 2024 release to public preview on AWS, GCP, and Azure in February 2026, is structured under a zero-access operating model in which Pinecone never needs SSH, VPN, or inbound network access into the customer's cloud account, and customer vectors, metadata, and queries never leave the customer environment. This is the strongest tenant-isolation guarantee Pinecone makes publicly and is meaningful for regulated-data deployments. Customers should note that BYOC is currently public preview rather than GA in the multi-cloud configuration.

HIPAA compliance is available either through the $190/month Standard-plan add-on (introduced February 2026) or included with the Enterprise plan. The AI Services Addendum §7(e) states that AI Services (Pinecone Assistant, Pinecone Inference) are by default not in scope of any BAA outstanding between the parties, unless otherwise agreed separately in writing after the addendum's 2025-01-22 effective date. Regulated-data customers intending to use Pinecone Assistant with PHI should confirm BAA scope separately.

A third-party security review by IronCore Labs (March 2024) had previously scored Pinecone as "weak" on a custom maturity index and pointed to the then-state of RBAC and certain encryption-claim language. IronCore Labs subsequently withdrew that scoring and noted that Pinecone had added CMEK and enhanced RBAC. This trajectory is recorded for completeness; the current evaluation reflects the present-day public documentation only.

Multi-factor authentication is documented on the security page as "Coming Soon" at evaluation date. SSO via SAML mitigates this for federated workforce identity flows. For customers operating outside federated identity, this is a notable credential-surface gap.

## VERDICT Record

**Summary.** Pinecone scores 71/85 on Layer 0, with every dimension reaching the High rating threshold; the publicly accessible DPA + AI Services Addendum + Trust Center together provide the documentation density that supports the score, while MFA availability and selected NDA-gated reports are the recorded transparency gaps.

**Risk Factor Summary by Use Case**

| Use Case | Risk |
|----------|------|
| Internal testing / non-sensitive workloads | Low — Starter plan available; namespace isolation, audit logs (GA), and deletion protection are accessible without enterprise contract. |
| Credential-handling workloads | Low–Mid — RBAC, control/data plane API key separation, SAML SSO, and service accounts (GA) are documented; MFA availability marked "Coming Soon" is the open gap. |
| Cloud multi-tenant workloads | Low — Namespace-based isolation, SOC 2 Type II 2025 zero deviations, ISO 27001:2022 surveillance audit, CMEK (GA), private endpoints, and BYOC zero-access option are publicly documented. |
| Regulated-data workloads (HIPAA / GDPR) | Low–Mid — HIPAA available via Standard add-on ($190/mo) or Enterprise; GDPR DPA with full SCC Module 2 / Module 3 and UK Addendum publicly accessible. Mid for Pinecone-Assistant-dependent workloads because AI Services are by default not in scope under any BAA per AI Services Addendum §7(e); customers should confirm BAA scope separately. |

**Reference Information** (options, not instructions)

- Customers considering BYOC for tenant-isolation reasons may verify the current GA / public-preview status of BYOC per cloud provider against the latest release notes at docs.pinecone.io/release-notes/, since the multi-cloud BYOC offering was at public-preview status as of the February 2026 release note.
- Customers considering Pinecone Assistant for regulated-data workflows may confirm separately the BAA scope for AI Services with Pinecone's sales / legal contact, since the default position in AI Services Addendum §7(e) excludes AI Services from any outstanding BAA absent separate written agreement.
- Customers operating outside SSO-federated identity may track the availability of MFA against the "Coming Soon" status on the security page.

**Bias Disclosure**

> "This evaluation uses Claude (Anthropic) as its tooling. Anthropic operates in the AI agent market and may compete with some evaluated vendors. VERDICT discloses this relationship in every report and applies identical evaluation criteria to all platforms regardless of their relationship to Anthropic."

## Future Evaluation Plan

- **Layer 1 (behavioral testing):** Free-tier behavioral evaluation under VERDICT Layer 1 protocol is scheduled per the 30-runs × 4-difficulty-levels × 3-day cadence. Pinecone's free Starter tier supports Serverless index creation and Pinecone Assistant evaluation tokens (500,000 chat input / 300,000 chat output / 500,000 context retrieval / 1,000 ingestion units per month per the April 2026 release notes), which is sufficient for E-dimension scoring.
- **Layer C (continuous monitoring):** R-dimension re-evaluation triggers on: any new CVE with CVSS 7.0+ assigned to a Pinecone Systems product; any CISA KEV addition; any supply-chain compromise; any incident reported by two or more independent sources; or 90-day routine refresh. Trust Center and status.pinecone.io are the canonical monitoring surfaces.
- **Differential re-evaluation:** Recommended on MFA general availability, BYOC promotion from public preview to GA on each of AWS / GCP / Azure, and any change to the AI Services Addendum no-training clause scope.

---

**Framework version:** VERDICT v0.3.1
**Evaluation engine:** v0.3.1-final