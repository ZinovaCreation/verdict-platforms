# Arize AI 評価結果サマリー

## 基本情報
- スコア: 51/85 (Layer 0)
- ランク: Tier B
- 評価日: 2026.05.15
- 対象バージョン: Arize AX (現行) / arize-phoenix v14.16.0
- 運営: Arize AI, Inc.(Delaware C-corp、本社カリフォルニア州バークレー)
- 独立性: ⚠️ Microsoft(M12)が Series C で出資、Anthropic にも戦略的出資(複合投資家構造)/Azure AI Foundry 商業統合あり(Trigger 2 + Trigger 3)

## 次元スコア
- V (検証可能性): 13/20 — 法人特定・認証は明確、Phoenix は ELv2 source-available(完全 OSI ではない)、サブプロセッサ公開リストなし
- R (耐性): 17/20 — 直近12ヶ月の CVE なし、PyPI Trusted Publishing 署名済、GPG 検証済リリース
- D (データ運用): 3/15 — Customer Data の AI 学習非使用の明文化なし、公開 DPA なし、サブプロセッサ公開リストなし、AX 保持期間の公表なし
- I (制御): 8/10 — SAML SSO/RBAC/カスタムロール/3層監査ログ(GraphQL)/Human-in-the-Loop が標準
- C (封じ込め): 4/10 — マルチテナント分離は宣言ベース、独立検証(ペンテスト要約等)の公開なし、CMEK/評価LLM の BYOK 言及なし
- T (透明性): 6/10 — SECURITY.md/Trust Center/Yogosha バグバウンティ/ステータスページあり、外部AI安全フレームワーク参照は限定的

## 主要ポジティブ所見
- SOC 2 Type II、ISO/IEC 27001、HIPAA、PCI DSS 4.0、GDPR Compliant、CSA STAR Level 1 を保有
- 直近12ヶ月の CVE 0件、CISA KEV 該当なし
- arize-phoenix の PyPI Trusted Publishing(attestation 付)+ GitHub 検証済 GPG 署名(key B5690EEEBB952194)
- 3層構造の監査ログ(unauthenticated / authenticated / exporter)を GraphQL で API 公開
- USA / EU(eu-west-1a)/ Canada(ca-central-1a)のデータリージョン選択を公開ドキュメントで明示
- Phoenix OSS 自己ホストにより、ユーザーがトラストバウンダリ内でデータ完結可能
- CISO(Remi Cattiau)と Compliance Officer(Jim Groff)を実名公開、AFWERX SBIR(契約番号 FA864925P0276)獲得

## 主要リスク所見
- ToS §5.1 は Customer Data を「improve the Application and the Services」に使用可能とする広範なライセンスを付与、§8.3 で集約・匿名化データの所有権を Arize に移転 — 学習非使用の明文化なし
- 公開サブプロセッサリスト(更新日付き)が確認できない(trust.arize.com は Vanta 経由のゲート付ポータル)
- 公開 DPA が確認できず、SOC 2 Type II レポートは「contact us」によるリクエスト制
- Arize Phoenix の ELv2 ライセンスは「open source」とマーケティングされているが、第三者ホスト型競合サービス禁止条項を持つ source-available ライセンス
- 公開 Privacy Policy(effective 2020-02-01、最終更新 2022-08-20)はウェブサイト訪問者向けで、AX プラットフォームのデータライフサイクルを扱っていない
- Velvet 買収(2025-03-13)が公開 Privacy Policy / Trust Center / DPA / 法人フッターに反映されていない
- 「Council of judges」評価方式が複数 LLM プロバイダを内部呼び出しするが、顧客トレースデータの当該プロバイダへの送信可否、オプトアウト、BYOK は公開ドキュメントに明示なし
- FedRAMP / IL4 / IL5 / StateRAMP の認定は確認できず(AFWERX SBIR は研究契約であり本番クラウド認可ではない)
- 顧客名(Booking.com、Uber、Wayfair 等)は運営側主張、独立した外部技術ブログ等での裏付けは大半が確認できず(#064 Guardrails AI 顧客検証規律準拠)

## インシデント
- 直近12ヶ月の公開 CVE なし(NVD / GitHub Security Advisories / OSV / GitHub Advisory DB を確認)
- 公開サプライチェーン侵害の確認なし

## CISA KEV
- 該当なし

## バイアス開示
- Microsoft が M12 経由で Arize に、別途 Anthropic に出資(複合投資家構造、Trigger 2)
- Microsoft × Arize の Azure AI Foundry 商業統合が存在(Trigger 3、付加的事実)
- VERDICT は v0.3.1 framework により公開情報のみで採点、ベンダー収益・有償認証は採点に影響しない

## HTMLカード用タグ
- tags: llm-observability, ai-evaluation, ml-monitoring, opentelemetry, openinference, elv2, microsoft-trigger-2, microsoft-trigger-3
- incident_tags: no-cve-12mo, no-cisa-kev, no-supply-chain-compromise
- owner: Arize AI, Inc.

Score: 51/85
V: 13/20, R: 17/20, D: 3/15, I: 8/10, C: 4/10, T: 6/10
Dimensions verified: V+R+D+I+C+T = 51

Tier classification: B | Category: LLM Observability · AI Evaluation · Model Monitoring (Cloud + OSS dual-tier)

═══ QA REVIEW ═══
Factual:   PASS — CLEAR (no CVEs/KEV confirmed via NVD, OSV, GitHub Advisory DB; corporate facts cross-checked against PR Newswire, TechCrunch, PitchBook, CB Insights; ELv2 license verified at repository; certifications verified at Trust Center)
Legal:     PASS — CLEAR (no intent attribution; Microsoft Trigger 2 + Trigger 3 disclosed neutrally per Strategy Brief #3 §3 B3; Velvet acquisition noted as fact; positive findings included)
Quality:   PASS — CLEAR (Executive Summary 4 sentences; Bias Disclosure verbatim; Japanese summary scores match English; institutional tone maintained)
Result:    CLEARED
══════════════

# VERDICT Evaluation #068 — Arize AI (Arize AX + Arize Phoenix)

| Field | Value |
|---|---|
| Evaluation Number | #068 |
| Platform | Arize AI (product family: Arize AX commercial + Arize Phoenix OSS) |
| Evaluation Type | Initial |
| Evaluation Date | 2026-05-15 |
| Evaluator | VERDICT Engine v0.3.1 |
| Target Version | Arize AX (current); arize-phoenix v14.16.0 (28 Apr 2026) |
| Framework | VERDICT v0.3.1 (Layer 0) |
| Previous Evaluation | None |

## Executive Summary

Arize AI scores **51/85** at Layer 0, with strong showings in Resilience (no CVEs in trailing 12 months; signed PyPI Trusted-Publishing releases) and Identity & Control (documented SSO/SAML, RBAC with custom roles, three-tier audit logging via GraphQL, and human-in-the-loop evaluation by design). Verifiability is Mid: corporate identity and certification posture (SOC 2 Type II, ISO/IEC 27001, HIPAA, PCI DSS 4.0) are well-documented, but the operator-claimed open-source positioning of Arize Phoenix is technically source-available under Elastic License 2.0 (ELv2), and the public Privacy Policy is scoped to website visitors rather than the AX platform. The lowest dimension is Data Conduct: the Terms of Service grant Arize a broad license to "enhance and improve" the Application using Customer Data and assign aggregate-data ownership to Arize, without an explicit statement that customer trace data is not used to train Arize's evaluator models, and no public dated subprocessor list, public DPA, or platform-level retention schedule was located at evaluation date. Containment is Mid (multi-tenant cloud isolation is claimed but not independently verified in public sources; IP whitelisting and Arize Private Connect are documented for enterprise tier).

## Scorecard

| Dimension | Score | Max | % | Rating |
|---|---|---|---|---|
| V — Verifiability | 13 | 20 | 65% | Mid |
| R — Resilience | 17 | 20 | 85% | High |
| D — Data Conduct | 3 | 15 | 20% | Low |
| I — Identity & Control | 8 | 10 | 80% | High |
| C — Containment | 4 | 10 | 40% | Mid |
| T — Transparency | 6 | 10 | 60% | Mid |
| **Total (Layer 0)** | **51** | **85** | **60%** | **Tier B** |

**CISA KEV:** None confirmed for Arize AI products at evaluation date.

## Dimension Detail

### V — Verifiability (13/20, Mid)

| Criterion | Result | Score | Evidence |
|---|---|---|---|
| Developer / company identity | Confirmed corporate registration + multiple official contact paths | 4/4 | arize.com/terms-of-service (Notice Address Lafayette, CA); PR Newswire 2025-02-20 (Berkeley, CA); finance@arize.com, support@arize.com, contacts@arize.com, opensource-security@arize.com documented |
| Source code disclosure | Phoenix tier source-available under ELv2; Arize AX commercial is closed | 2/4 | github.com/Arize-ai/phoenix/blob/main/LICENSE (Elastic License 2.0) |
| Version management transparency | Release notes + tagged GitHub Releases with GPG-verified signatures; semantic versioning; active cadence | 3/3 | github.com/Arize-ai/phoenix/releases (v14.16.0 on 2026-04-28, v14.15.0 on 2026-04-25, GPG key B5690EEEBB952194); arize.com/docs/phoenix/release-notes |
| Third-party dependency disclosure | No publicly dated subprocessor list located | 0/3 | arize.com/trust-center/ lists "Partners" (Vanta, Google Cloud, Kandji) without subprocessor categorization or last-updated indicator; trust.arize.com is access-gated (Vanta-hosted) |
| Independent certification | SOC 2 Type II is request-only; ISO 27001, HIPAA, PCI DSS 4.0 displayed as badges | 2/4 | arize.com/trust-center/; arize.com/docs/ax/security-and-settings/compliance ("To request a copy of the report, please contact us") |
| Functional reproducibility docs | Comprehensive API reference + behavioral specifications | 2/2 | arize.com/docs/ax; arize.com/docs/phoenix; GraphQL audit log API documented |

**Positive findings:** Corporate identity, executive team, and CISO (Remi Cattiau) publicly named; release cadence is rapid with verified signatures; OpenInference / OpenTelemetry semantic conventions published as an open standard.

**Recorded concerns:** ELv2 is source-available rather than OSI-approved open source, and the operator's public positioning of Phoenix as "fully open source" does not match the license's "no hosted/managed competing service" restriction. No publicly dated subprocessor list. SOC 2 Type II report requires a customer request channel. Velvet acquisition (2025-03-13) is not reflected in the public Privacy Policy, Trust Center, or corporate footer at evaluation date.

### R — Resilience (17/20, High)

| Criterion | Result | Score | Evidence |
|---|---|---|---|
| CVE count (trailing 12 months) | 0 CVEs confirmed | 5/5 | NVD search (no Arize entries); github.com/advisories?query=arize (0 results); osv.dev/list?q=arize (no results); github.com/Arize-ai/phoenix/security/advisories (no published advisories) |
| Maximum CVSS severity | No CVEs to score | 6/6 | Same sources as above |
| Patch response speed | Not evaluable from public sources (no CVEs in window) | 0/3 | Silence = 0 per framework Rule 10; SECURITY.md confirms supported versions discipline (2.x.x supported, 1.x.x and 0.0.x unsupported) |
| Structural issues | No recurrence pattern (no CVEs to recur) | 3/3 | Same sources |
| Supply chain compromise (trailing 12 months) | None confirmed | 3/3 | PyPI Trusted Publishing attestations on arize-phoenix-client, arize-phoenix-evals, arize-phoenix-otel (Publisher: publish.yaml on Arize-ai/phoenix); no public reports of Arize involvement in Shai-Hulud, TeamPCP, or related recent npm/PyPI compromises |

**Positive findings:** No CVEs assigned to `arize` or `arize-phoenix` packages in the trailing 12 months. PyPI Trusted Publishing with verified attestations is configured for sub-packages. GitHub Releases are GPG-signed by a verified maintainer key. Published SECURITY.md with explicit supported-version matrix.

**Recorded concerns:** Patch response speed cannot be independently confirmed from public sources due to the absence of CVEs in the evaluation window; this is structurally favorable but reduces the score under the Silence = 0 rule.

### D — Data Conduct (3/15, Low)

| Criterion | Result | Score | Evidence |
|---|---|---|---|
| GDPR compliance disclosure | GDPR badge displayed; EU residency supported; public DPA not located | 1/3 | arize.com/trust-center/ (GDPR Compliant badge); arize.com/blog/arize-ai-support-for-eu-data-residency/; arize.com/docs/ax/security-and-settings/whitelisting (EU region eu-west-1a) |
| Data minimization | Phoenix OSS web analytics default-on with env-var opt-out; AX-level telemetry default not documented publicly | 1/3 | github.com/Arize-ai/phoenix README (`PHOENIX_TELEMETRY_ENABLED=false`) |
| AI training use | No explicit "not used for training" statement; broad license + aggregate-data ownership | 0/4 | arize.com/terms-of-service/ §5.1 ("Customer grants Arize a nonexclusive, worldwide, royalty-free right to reproduce, display, adapt, modify, transmit, distribute and otherwise use the Customer Data ... to maintain, provide, enhance, and improve the Application and the Services"); §8.3 ("Arize shall solely and exclusively own ... any de-identified, aggregated, and/or anonymized data ... derived from Customer Data") |
| Sub-processor transparency | No publicly dated list located | 0/3 | trust.arize.com is access-gated (Vanta); Trust Center "Partners" list lacks subprocessor classification and last-updated indicator |
| Data retention disclosure | Phoenix self-hosted retention is configurable and documented; AX-managed retention schedules not stated in public ToS or Trust Center | 1/2 | arize.com/docs/phoenix/settings/data-retention (Phoenix 9.0+ retention policies with cron schedules; default = 0 days = indefinite); AX public docs do not specify default trace retention windows |

**Positive findings:** EU and Canada data residency regions documented (eu-west-1a, ca-central-1a). Phoenix self-hosted gives full data-residency control to the deploying organization. GDPR-compliant badge displayed. Customer-as-controller framing is consistent with the architectural intent of an observability product.

**Recorded concerns:** The ToS does not include an explicit statement that customer trace, prompt, or response data sent to Arize AX is excluded from training Arize's internal evaluator models, including the "council of judges" architecture that invokes multiple LLM providers. No public dated subprocessor list — critical for an observability platform whose evaluation methodology depends on multiple LLM-provider dependencies. No public DPA. Retention windows for AX-managed trace data not stated in public ToS. The Privacy Policy (effective 2020-02-01, last modified 2022-08-20) is scoped to website visitor data and does not address the platform data lifecycle.

### I — Identity & Control (8/10, High)

| Criterion | Result | Score | Evidence |
|---|---|---|---|
| Emergency stop documentation | "Delete Traces with Sensitive Data" workflow documented; full emergency-stop procedure for compromised AI agents not explicitly documented | 2/4 | arize.com/docs/ax/security-and-settings/compliance/delete-traces-with-sensitive-data |
| Human-in-the-loop design | Annotation Configs, Labeling Queues, Human Review enabled by design; "council of judges" includes human-in-the-loop | 3/3 | arize.com/docs/ax/evaluate/human-review; arize.com/docs/ax/evaluate/labeling-queues; TechCrunch 2025-02-20 (operator description of evaluation methodology) |
| Permission delegation transparency | SAML SSO, JIT provisioning, RBAC with custom roles, Service Keys, API Keys all documented | 3/3 | arize.com/docs/ax/security-and-settings/sso-and-rbac; arize.com/docs/ax/security-and-settings/api-keys |

**Positive findings:** Three-tier audit logging (unauthenticated login attempts, authenticated mutations, exporter audit logs) accessible via GraphQL API with pagination. SAML 2.0 SSO with Identity-Provider-driven role mapping. Fine-grained custom roles assignable at space or project level. Service Keys are scope-limited and rotation-capable.

**Recorded concerns:** A platform-level "emergency stop" procedure for terminating data ingestion or evaluator runs on a compromised customer agent is not explicitly documented; remediation appears to depend on customer-side API key revocation and Space-level access controls.

### C — Containment (4/10, Mid)

| Criterion | Result | Score | Evidence |
|---|---|---|---|
| Sandbox design | Platform does not execute customer code (observability surface); network egress allowlisting documented; Arize Private Connect available | 2/4 | arize.com/docs/ax/security-and-settings/whitelisting; arize.com/docs/ax/security-and-settings/arize-private-connect (referenced in nav) |
| Least privilege | Default RBAC roles plus configurable custom roles; "default least privilege" not explicitly claimed | 1/3 | arize.com/docs/ax/security-and-settings/sso-and-rbac |
| Tenant isolation (cloud) | Multi-tenant cloud claimed in shared-responsibility model; no public independent verification (e.g., pen-test summary) located | 1/3 | arize.com/trust-center/ ("If we can configure it, we are responsible for it" — explicit Tenant Isolation responsibility); no public pen-test summary located on Trust Center |

**Positive findings:** Documented per-region service endpoints (USA, EU, Canada) for UI, ingestion, OTLP, and Flight data. Arize Private Connect referenced for enterprise tier. Bug bounty program hosted by Yogosha publicly listed.

**Recorded concerns:** Tenant isolation is claimed in the shared-responsibility model but not independently verified by a publicly available pen-test summary or third-party attestation. CMEK (customer-managed encryption keys) availability not located in public documentation. The "council of judges" evaluation architecture invokes external LLM providers — whether customer trace data is routed to these providers and whether customers can opt out or BYOK for evaluator LLMs is not explicitly stated in public documentation.

### T — Transparency (6/10, Mid)

| Criterion | Result | Score | Evidence |
|---|---|---|---|
| CVE publication posture | Coordinated disclosure channel documented; bug bounty active; no CVEs issued | 1/2 | github.com/Arize-ai/phoenix/security/policy (opensource-security@arize.com); arize.com/trust-center/ (Yogosha bug bounty) |
| Incident disclosure speed | Status page exists; no recent material public incident postmortems located | 0/2 | status.arize.com (active) |
| Security policy publication | Trust Center with Security Periodic Table (16 elements), shared-responsibility model, named CISO, SECURITY.md | 2/2 | arize.com/trust-center/; github.com/Arize-ai/phoenix/security/policy |
| AI safety framework reference | OpenInference / OpenTelemetry adopted (instrumentation standard); internal LLM Red Teaming methodology documented; no explicit NIST AI RMF or comparable AI-safety-specific framework reference located | 1/2 | github.com/Arize-ai/openinference; arize.com/docs/ax/security-and-settings/llm-security/llm-red-teaming |
| AI system identity disclosure | Alyx is identified as an "AI Engineering Agent"; docs "Ask AI" feature is clearly AI-labeled | 2/2 | arize.com/alyx/; arize.com/docs/ax (Mintlify "Ask AI" badge) |

**Positive findings:** Published SECURITY.md with explicit supported-version table. Named CISO (Remi Cattiau) and Compliance Officer (Jim Groff). Public status page. Bug bounty via Yogosha. Open-source instrumentation standard (OpenInference) published and adopted across the ecosystem.

**Recorded concerns:** No recent material incident postmortems located on the status page or blog within the evaluation window. AI safety framework reference is internal (LLM Red Teaming, "council of judges") rather than aligned to a named external framework such as NIST AI RMF or ISO/IEC 42001.

## Incident Timeline

No public CVEs were confirmed for `arize`, `arize-phoenix`, or Arize platform surfaces in the trailing 12 months (2025-05-15 to 2026-05-15) per NVD, GitHub Security Advisories, OSV, and GitHub Advisory Database searches. No CISA KEV listings. No publicly reported supply chain compromises affecting Arize-published packages.

## Contextual Analysis

Arize AI operates at the intersection of two structural relationships material to this evaluation. Under VERDICT framework v1.1 Trigger 2, Microsoft (via its corporate venture fund M12) holds equity in Arize AI through the Series C round announced 2025-02-20, and Microsoft separately holds a strategic equity commitment in Anthropic (up to USD 5 billion, subject to closing conditions per the November 2025 Microsoft / NVIDIA / Anthropic joint announcement). This constitutes a compound investor structure in which Microsoft holds equity positions in both the evaluator (Anthropic, operator of VERDICT) and the evaluated platform (Arize AI). VERDICT scoring is based exclusively on public data sources per the v0.3.1 framework, and no vendor revenue or paid certification influences the rating.

Additively, under framework v1.1 Trigger 3, Arize AI has a publicly disclosed commercial channel relationship with Microsoft beyond the cap-table relationship described above, including deep product integration with Azure AI Studio and Azure AI Foundry (portal, SDK, CLI). The operator publicly describes the partnership as a "long-standing collaboration" reinforced by M12's investment. This channel relationship is recorded as a structural fact and noted neutrally.

On 2025-03-13, Arize AI acquired Velvet (Business / Productivity Software, per PitchBook M&A record). As of evaluation date, the acquisition is not reflected in the public Privacy Policy, Trust Center subprocessor categorization, DPA controller / processor designations, or corporate footer. The architectural impact of the acquisition on the AX platform's feature lineage and data flows is therefore unverified from public sources. The fact of the acquisition is recorded; no architectural inference is made beyond that.

The platform's underlying architecture is LLM-provider-agnostic by design; the deploying developer chooses which LLM providers and evaluation backends are integrated. Operator-claimed enterprise customers (Booking.com, Condé Nast, Duolingo, Hyatt, PepsiCo, Priceline, TripAdvisor, Uber, Wayfair, Klaviyo) appear in the operator's homepage testimonials and press materials; independent external corroboration (e.g., customer engineering blogs with named Arize integration) was not located within the evaluation window for most of these references, and they are treated as operator-claimed but independently unverified per the #064 Guardrails AI customer testimonial verification discipline. The Uber testimonial on arize.com/customers is attributed to Uber's Michelangelo ML platform team but is published on the Arize property rather than on a separate Uber engineering blog.

Two recent operator-claimed positioning claims warrant noting: the "two million monthly Arize Phoenix PyPI downloads" claim is operator-stated as of the 2025-02-20 Series C announcement and the "first-to-market audio evaluation" claim is operator-self-positioning. Neither is reproduced here as verified. The arize-phoenix GitHub repository at evaluation date shows 9.7k stars and 871 forks.

Government and defense engagement is documented: AFWERX Direct-to-Phase II SBIR contract awarded 2025-07-22 (Contract No. FA864925P0276, approximately USD 1.2M / year, 12-month period of performance) for AI engineering capabilities supporting NIPRGPT / GCP AI; and U.S. Navy Project AMMO referenced on the operator's homepage. FedRAMP, IL4 / IL5, or StateRAMP authorizations are not documented at evaluation date; the SBIR vehicle is a research contract, not a production cloud authorization.

## VERDICT Record

**Summary.** Arize AI scores 51/85 (Tier B) under VERDICT v0.3.1 at Layer 0. Resilience and Identity & Control are strong; Data Conduct disclosure is the principal gap, driven by the absence of a public dated subprocessor list, public DPA, AI-training-use disclaimer, and AX-platform retention schedule.

### Risk Factor Summary by Use Case

| Use Case | Risk | Notes |
|---|---|---|
| Internal testing / non-sensitive workloads | Low | Phoenix OSS self-hosted available under ELv2; no recent CVEs; signed releases; rich SDK |
| Credential-handling workloads | Moderate | SSO/SAML, RBAC, three-tier audit logging strong; CMEK availability and BYOK for evaluator LLMs not documented publicly |
| Cloud multi-tenant workloads | Moderate | Multi-tenant isolation claimed in shared-responsibility model; SOC 2 Type II, ISO 27001 support; independent verification (e.g., pen-test summary) not publicly located; EU and Canada residency available |
| Regulated-data workloads (PHI, PCI, federal) | Moderate to elevated | HIPAA, PCI DSS 4.0, SOC 2 Type II, ISO 27001 compliance posture is strong; FedRAMP / IL4 / IL5 / StateRAMP not documented; public DPA and subprocessor list not located, which constrains regulated-procurement transparency |

### Reference Information (options, not instructions)

1. For evaluations where customer trace data must remain inside the deploying organization's trust boundary, Arize Phoenix can be self-hosted under ELv2 with full retention, deletion, and egress control by the deploying team.
2. For AX cloud deployments in regulated environments, requesting the SOC 2 Type II report, DPA, and current subprocessor list through Arize's commercial channel under NDA may close documentation gaps that are not addressed in the public Trust Center.
3. For data-residency-sensitive evaluations, the EU (eu-west-1a) or Canada (ca-central-1a) region selection at deployment may be relevant; verification of retention controls in the customer-side Space configuration is the customer's responsibility under the documented shared-responsibility model.

### Bias Disclosure

> "This evaluation uses Claude (Anthropic) as its tooling. Anthropic operates in the AI agent market and may compete with some evaluated vendors. VERDICT discloses this relationship in every report and applies identical evaluation criteria to all platforms regardless of their relationship to Anthropic."

## Future Evaluation Plan

- **Layer 1 timing:** A Layer 1 free-tier behavioral evaluation is scheduled following Layer 0 publication, covering observability accuracy, evaluation methodology effectiveness, and audio evaluation behavioral characteristics where the free tier permits.
- **Layer C monitoring:** Continuous CVE and CISA KEV monitoring per ENGINE.md §Re-evaluation triggers; routine re-evaluation at 90 days (next scheduled review window: approximately 2026-08-13).
- **Re-evaluation triggers fire on:** publication of any new Arize CVE with CVSS 7.0+; CISA KEV addition; confirmed supply chain compromise affecting Arize-published packages; two-or-more-source major security incident; or material change to public ToS, Privacy Policy, Trust Center, or DPA posture (including publication of a public subprocessor list).

---

**Framework:** VERDICT v0.3.1 | **Evaluation type:** Initial | **Score:** 51/85 (Layer 0) | **Tier:** B