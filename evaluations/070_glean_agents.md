# VERDICT Evaluation Report #070
## Glean Agents

Evaluation type: Layer 0
Evaluation date: 2026.09.24
Evaluator: VERDICT by ZinovaCreation (evaluator model: claude-fable-5-1)
Target version: Glean Agents (GA 2025-05-20) on the Glean cloud platform as publicly documented 2026-09; Independent agents in beta
Framework: VERDICT v0.3.2
Previous evaluation: First evaluation
Selection basis: list:mit-2025 (MIT AI Agent Index 2025 entry `glean-agents`)
Disclosure layer (ENGINE.md Triggers 0–3): None. The Series F investor list (2025-06-10) contains none of Amazon, Google, Microsoft or NVIDIA; those entities appear only as cloud / LLM sub-processors, an industry-standard supplier relationship. Product-level integration with Anthropic is disclosed in the Bias Disclosure.

---

## Executive Summary

Glean Agents scores 73/85 (Tier S) on VERDICT v0.3.2 Layer 0. The evaluated unit is the agent product of the Glean Work AI platform, matched to the MIT AI Agent Index 2025 entry `glean-agents`; the platform-level privacy, security and data-processing documents govern it and form the evidence base, so the score is not a rating of Glean Search alone. The strongest documented controls are in Identity & Control and Containment: write actions in interactive web sessions pause for user approval by default, agents execute with the permissions of the signed-in user who triggered the run regardless of who built the agent, and the Agent Sandbox is allowlist-based with per-tenant, per-session isolation and no credentials inside the sandbox. No CVE attributable to a Glean Technologies product and no publicly reported security incident were confirmed in the trailing 12 months (2025-09-24 to 2026-09-24); the only "Glean" CVE returned by the search set (CVE-2026-54339) belongs to an unrelated self-hosted RSS reader. Recorded gaps are closed source, a SOC 2 Type II report and Security Standard available only under NDA, an anonymized analytics export to Glean's central infrastructure that is on by default with no documented opt-out, and no public CVE or advisory channel beyond a Bugcrowd program.

---

## Scorecard

| Dimension | Score | Max | Rating |
|---|---|---|---|
| V Verifiability | 14 | 20 | High |
| E Effectiveness | N/A | 15 | Layer 1 pending |
| R Resilience | 20 | 20 | High |
| D Data Conduct | 12 | 15 | High |
| I Identity & Control | 10 | 10 | High |
| C Containment | 10 | 10 | High |
| T Transparency | 7 | 10 | High |
| **Total (Layer 0)** | **73** | **85** | |

CISA KEV: None
Tier: S
Category: Enterprise AI Assistant · Agent Platform · Cloud SaaS

---

## Dimension Detail

### V — Verifiability | 14/20

| Criterion | Result | Score | Evidence (source URL) |
|---|---|---|---|
| Developer / company identity | confirmed | 4 | Terms of Service v5Jun2026 names "Glean Technologies, Inc., a Delaware corporation, headquartered at 634 2nd Street, San Francisco, CA 94107"; privacy@glean.com, legal@glean.com, security@glean.com and a named Data Protection Officer published; Palo Alto office (260 Sheridan Ave) in site footer; MIT Index cites the Delaware certificate of incorporation. https://assets.glean.com/marketing/Legal/Glean%20Technologies-%20Inc.%20Terms%20of%20Service%20Jun%205%202026.pdf ; https://www.glean.com/privacy ; https://aiagentindex.mit.edu/2025/glean-agents |
| Source code disclosure | not confirmed (closed source) | 0 | Platform is closed source. The `gleanwork` GitHub organization publishes API clients, CLI and MCP configuration tooling only, not core components. https://github.com/gleanwork/mcp-server |
| Version management transparency | confirmed | 3 | Dated monthly release notes (e.g. 2026-05-06, 2026-07-15) with feature-level entries; every documentation page carries a "Last updated" date; SDK RELEASES.md on GitHub. https://docs.glean.com/release-notes/releases/2026-07-15-july-release |
| Third-party dependency disclosure | confirmed | 3 | Sub-processor list with entity, activity and location, "Last Updated: July 28, 2026". https://www.glean.com/legal/subprocessors |
| Independent certification | partial | 2 | SOC 2 Type II, ISO/IEC 27001, ISO/IEC 42001:2023, HIPAA and TX-RAMP Level 2 stated by Glean; SOC 2 report and penetration-test results available only under NDA through the Trust Portal (customers-only tier). https://www.glean.com/legal ; https://docs.glean.com/security ; https://docs.glean.com/security/agent-sandbox-ptc |
| Functional reproducibility docs | confirmed | 2 | REST / Agents API reference (implements the LangChain Agent Protocol Runs and Agents subset) with SDKs; behavioural documentation for triggers, tools, flow, memory, confirmation and scheduling. https://developers.glean.com/api/client-api/agents/overview ; https://docs.glean.com/agents/how-agents-work |

Positive findings: Legal entity, jurisdiction and multiple official contacts are confirmable from Glean's own legal documents; the sub-processor list is dated; release notes are dated and granular; API and behavioural documentation are extensive.
Recorded concerns: Closed source; SOC 2 Type II report, Security Standard and penetration-test reports are NDA-gated; certification claims are vendor statements without a public attestation document.

### R — Resilience | 20/20

| Criterion | Result | Score | Evidence (source URL) |
|---|---|---|---|
| CVE count (trailing 12 months) | confirmed: 0 | 5 | Search set: "Glean CVE", "Glean Technologies CVE vulnerability 2026", NVD keyword "Glean Technologies", OSV q=glean, "Glean security incident". The only hit, CVE-2026-54339 (CVSS 7.7, SSRF), affects `LeslieLeung/glean`, a self-hosted RSS reader unrelated to Glean Technologies; Mozilla Glean telemetry is likewise unrelated. Both excluded under product-scoped attribution (Attribution-CVE-001). https://osv.dev/vulnerability/CVE-2026-54339 ; https://aiagentindex.mit.edu/2025/glean-agents ("Any known incidents or reported vulnerabilities?: None found") |
| Maximum CVSS severity | none | 6 | No product-scoped CVE. |
| Patch response speed | no CVE to time; process documented | 3 | Zero-CVE convention applied. SDLC page documents per-release automated vulnerability analysis, release gating for Critical findings and unscheduled patches "when appropriate"; status-page operational incidents Jul–Sep 2026 resolved in 0 min to 8 h 41 min with public timelines. Strict alternative reading (0/3 where no patch event exists to measure) would yield 70/85, still Tier S. https://docs.glean.com/security/architecture/sdlc ; https://status.glean.com/history?date=2026-09-23 |
| Structural issues | isolated | 3 | Nine operational incidents Jul–Sep 2026 are independent; three relate to upstream LLM-provider availability (Azure OpenAI, OpenAI capacity, Amazon Bedrock), none to a recurring security root cause. https://status.glean.com/history?date=2026-09-23 |
| Supply chain compromise (trailing 12 months) | none found | 3 | `@gleanwork/*` npm packages and PyPI client: no compromise found in searches ("gleanwork npm compromised", Shai-Hulud package lists); local MCP packages are deprecated in favour of the managed remote MCP server; Chrome extension: no reported compromise. Build pipeline uses signed artifacts and binary authorization. https://www.npmjs.com/package/@gleanwork/local-mcp-server ; https://docs.glean.com/security/architecture/sdlc |

Positive findings: No product-scoped CVE, KEV entry or public security incident; documented signed-artifact build chain and per-release vulnerability gating; public status page with incident history.
Recorded concerns: Full marks on patch response and structural issues rest on documented process and operational incidents rather than an observed vulnerability lifecycle; per-release vulnerability reports are delivered privately to customer-hosted deployments, so third parties cannot observe patch timelines.

### D — Data Conduct | 12/15

| Criterion | Result | Score | Evidence (source URL) |
|---|---|---|---|
| GDPR compliance disclosure | confirmed | 3 | Online Data Processing Addendum (Sep 3, 2024 version public) with EU Standard Contractual Clauses and 30-day sub-processor notice; Privacy Statement GDPR section; EU-U.S., UK and Swiss Data Privacy Framework certification stated. https://cdn.prod.website-files.com/6127a84dfe068e153ef20572/66d7cec39c298d698624e7f1_Glean%20Technologies,%20Inc.%20DPA%20Sep%203%202024%20(Online).pdf ; https://www.glean.com/privacy |
| Data minimization | default ON, no documented opt-out | 0 | "Anonymized, non-PII logs" with hashed user IDs, document URLs and query terms are exported by default from the customer's project to a BigQuery table in Glean's central project via a GCP Log Sink; no opt-out procedure is documented publicly. Customer Event logging is on by default (stays in the customer project). https://docs.glean.com/security/architecture/shared-centralized-services ; https://docs.glean.com/administration/gce-logs/data-dictionary |
| AI training use | confirmed, with retention | 4 | End-user guide: "your data isn't used for training or testing. Glean also uses models with a zero-day retention policy"; model-choice page: providers configured with zero-retention commitments, not used for training by model vendors; Terms: no training on Azure OpenAI/OpenAI key. https://docs.glean.com/user-guide/about/end-user-quick-start-guide ; https://docs.glean.com/get-started/golive/model-choice |
| Sub-processor transparency | confirmed | 3 | Dated list (July 28, 2026); customers may select a different cloud provider and location. https://www.glean.com/legal/subprocessors |
| Data retention disclosure | per category | 2 | Chat history: Off / 30 / 90 / 180 / 365 days (admin-set, auto-deletion); admin audit logs: 30-day default; data-analysis files: retained while the session is in history, abuse-flagged files up to 30 days; LLM providers: zero-day; DPA: term of agreement. https://docs.glean.com/administration/assistant/configuration/chat-history ; https://docs.glean.com/administration/management/audit-logs/admin-audit-logs ; https://docs.glean.com/administration/assistant/data-analysis/about-data-analysis |

Positive findings: Explicit no-training statement paired with zero-day LLM retention; dated sub-processor list; configurable, documented retention per data category; DPF certification.
Recorded concerns: The website Privacy Statement expressly does not apply to the Solutions, so product data conduct rests on the Terms, DPA and documentation; the default analytics export to Glean central infrastructure has no documented opt-out (data is stated to be hashed and non-PII).

### I — Identity & Control | 10/10

| Criterion | Result | Score | Evidence (source URL) |
|---|---|---|---|
| Emergency stop documentation | confirmed | 4 | Agent Builder "Disable agent / Enable agent — pause or resume an agent without deleting it"; Agent Library Active table: pause or resume, Active toggle; deactivating an agent pauses all subscriptions; Admin and Agent Moderator roles "Can disable agent"; admins gate which write tools may run at all; Glean Protect alignment check can block write actions before execution. Documented limitation: agents cannot be cancelled while waiting for user input. https://docs.glean.com/agents/concepts/agent-builder ; https://docs.glean.com/agents/concepts/agent-library ; https://docs.glean.com/administration/managing-agents/agent-access ; https://docs.glean.com/agents/actions/glean/wait-for-user-input |
| Human-in-the-loop design | enabled by default | 3 | "Write actions in agents running in the Glean web app pause for user approval before executing ... applies by default to all write actions in interactive web app sessions"; removing confirmation is an explicit admin opt-in per action; background runs that reach a tool still requiring confirmation e-mail the subscriber. Exception recorded: behaviour in Slack / Microsoft Teams is stated as unchanged. https://docs.glean.com/security/security-principles ; https://docs.glean.com/agents/concepts/schedule-triggers |
| Permission delegation transparency | confirmed | 3 | "Agents execute with the identity and permissions of the signed-in user who triggered the run, regardless of who created or published the agent"; service credentials for independent agents are created and scoped per connected system by administrators; access tiers (Viewer/Editor/Owner) and role tables documented. https://docs.glean.com/security/security-principles ; https://docs.glean.com/agents/independent-agents ; https://docs.glean.com/administration/managing-agents/agent-access |

Positive findings: Confirmation-by-default for write actions, executor-identity enforcement, admin and moderator gates, audit logs of subscriptions, runs, traces and tool executions with SIEM export.
Recorded concerns: Slack/Teams surfaces and scheduled runs shift control from per-action confirmation to governance settings; no in-run cancel during "wait for user input"; the MIT Index annotation (2025) recorded "None found" for user-approval requirements, whereas the current Glean pages (last updated Aug–Sep 2026) document the confirmation behaviour.

### C — Containment | 10/10

| Criterion | Result | Score | Evidence (source URL) |
|---|---|---|---|
| Sandbox design | allowlist-based | 4 | Agent Sandbox: "Only explicitly allowlisted tools are exposed. By default, the allowlist is restricted to a curated set of read-only native tools. Write tools are not supported through programmatic tool calling"; no outbound internet by default with domain allowlisting; non-root execution; no credentials in the sandbox; per-session call budget; code logged for audit. https://docs.glean.com/security/agent-sandbox-ptc |
| Least privilege | default | 3 | Permission mirroring: "Glean never grants broader access than the source system provides"; tools are enabled by admins; write tools remain interactive unless an admin explicitly allows background execution; independent-agent credentials scoped per system. Concern: an agent's scope equals the full scope of the executing user, and Default Member "Can create and publish agents" is On by default. https://docs.glean.com/security/security-principles ; https://docs.glean.com/security/agents/background-agents ; https://docs.glean.com/administration/managing-agents/agent-access |
| Tenant isolation (cloud) | documented single-tenant | 3 | Each customer runs in its own cloud project ("your company's Glean GCP project"), customer-hosted (GCP/AWS) or Glean-hosted; per-tenant, per-session sandboxes with no cross-tenant access; SOC 2 Type II and ISO 27001 stated (reports NDA-gated). https://docs.glean.com/security/architecture/shared-centralized-services ; https://docs.glean.com/security/agent-sandbox-ptc |

Positive findings: Allowlist tool and egress model, credential-free sandbox, single-tenant project architecture with a customer-hosted option.
Recorded concerns: Agent Sandbox / PTC are enabled "for eligible customers" in Thinking mode, so containment for other configurations rests on the tool-gating model; independent evidence of isolation is limited to NDA-gated audit reports.

### T — Transparency | 7/10

| Criterion | Result | Score | Evidence (source URL) |
|---|---|---|---|
| CVE publication posture | private only | 0 | Public Bugcrowd program and security@glean.com; no published CVEs or security advisories; per-release vulnerability reports are delivered privately to customer-hosted deployments. https://docs.glean.com/security ; https://bugcrowd.com/engagements/glean-technologies-public |
| Incident disclosure speed | ≤30 days | 2 | Public status page with incident history, impact windows and remediation notes posted the same day (e.g. 2026-08-31 Azure OpenAI degradation, 2026-07-10 extension actions). No security incident was found to disclose. https://status.glean.com/history?date=2026-09-23 |
| Security policy publication | detailed | 2 | SDLC page (protected branches, signed commits, Google Cloud Build with binary authorization, per-release scanning and reachability analysis, release gating, MFA/SSO, separation of duties); security principles; sandbox security; secure-configuration guides. The Security Standard itself moved behind the Trust Portal (Sep 2024 notice); the Sep 3, 2024 PDF remains public. https://docs.glean.com/security/architecture/sdlc |
| AI safety framework reference | external | 2 | ISO/IEC 42001:2023 certification stated; Responsible AI Policy on the Trust Portal; runtime AI security (prompt-injection, jailbreak, malicious-code detection) with optional Palo Alto Networks Prisma AIRS. https://www.glean.com/legal ; https://docs.glean.com/security/agent-sandbox-ptc |
| AI system identity disclosure | partial | 1 | Independent agents carry a dedicated profile and agent principal; actions taken with a service credential are attributed to the agent's identity in the connected app; Builder Assistant responses identify the generating model. Actions run under the user's own credentials are attributed to the user, and no organization-wide labelling of agent output as AI-generated is documented (MIT Index: "None found"). https://docs.glean.com/agents/independent-agents ; https://docs.glean.com/get-started/golive/model-choice ; https://aiagentindex.mit.edu/2025/glean-agents |

Positive findings: Detailed public SDLC and architecture documentation, ISO 42001, public status page, public bug bounty.
Recorded concerns: No public CVE or advisory channel; Security Standard, policies and audit reports NDA-gated; AI identity disclosure depends on agent type and credential model.

---

## Incident Timeline

No public CVEs were confirmed in the trailing 12 months (2025-09-24 – 2026-09-24).

Excluded by product-scoped attribution: CVE-2026-54339 (published 2026-09-17, CVSS 7.7, SSRF in `LeslieLeung/glean` ≤0.2.5, a self-hosted RSS reader with no relation to Glean Technologies, Inc.). Not a KEV entry.

Operational incidents recorded on status.glean.com (Jul–Sep 2026): nine, resolved between 0 min and 8 h 41 min; none classified by Glean as a security incident.

---

## Contextual Analysis

Glean's platform is built around permission mirroring: connectors ingest source-system ACLs, and every surface — search, answers, agents, MCP servers and embedded integrations — evaluates the querying or triggering user's identity at execution time. For agents this means the builder's permissions never transfer to the runner, which is the property most enterprise-agent buyers ask about first. The documentation dated August–September 2026 is unusually specific about the control model: interactive write actions pause for a confirmation panel, administrators opt individual actions out of confirmation, scheduled agents shift control to who may publish and which tools may run unattended, and independent agents (beta) act under admin-scoped service credentials with their own principal. The MIT AI Agent Index annotations, compiled in late 2025, recorded "None found" for user-approval requirements and for sandboxing; the pages that now document both carry later update dates, so the difference is consistent with documentation published after the Index's observation window.

The Agent Sandbox and Programmatic Tool Calling pages describe an allowlist design — read-only native tools by default, write tools excluded from programmatic calls, no outbound internet except allowlisted domains, no credentials inside the sandbox and a per-session call budget. These are the kinds of statements a security reviewer can test against contract documentation, though they are Glean's own descriptions and the supporting SOC 2 Type II and penetration-test reports are available only under NDA. The architecture places each customer in a single-tenant cloud project, customer-hosted or Glean-hosted, with a central Glean project limited to static asset delivery, tenant resolution, an anonymized analytics export and break-glass debugging under approval and audit. The analytics export is the one data flow that leaves the tenant by default; Glean states that user IDs, URLs and query terms are hashed before export, and no opt-out is documented publicly.

Glean is model-agnostic: OpenAI, Anthropic, Google, Amazon, Microsoft, Groq, Fireworks, Baseten, Modal and Snowflake appear on the sub-processor list as LLM providers, configured under zero-retention commitments, and customers can bring their own key. Three of the nine operational incidents in the last quarter trace to upstream LLM-provider availability, which is a dependency characteristic of the multi-model design rather than a vulnerability pattern. The disclosure posture is asymmetric: Glean publishes a detailed SDLC and a public Bugcrowd program, but no CVEs or advisories, and customer-hosted deployments receive vulnerability reports privately per release. Readers should weigh that the absence of public CVEs for a closed SaaS reflects the disclosure model as much as the security record.

Economic controls: some agent features are subject to usage-based pricing, the platform documents admin usage controls and a per-session tool-call budget, and the PTC design is described as reducing token usage. No P-dimension issue was recorded.

---

## VERDICT Record

### Summary
The data shows an enterprise agent platform whose public documentation describes confirmation-by-default write actions, executor-identity permission enforcement and an allowlist-based sandbox in single-tenant projects, with no product-scoped CVE or public security incident in the trailing 12 months, alongside a closed-source, NDA-gated assurance model and a default analytics export without a documented opt-out.

### Risk Factor Summary by Use Case

| Use case | Risk factors recorded | Key data points |
|---|---|---|
| Internal testing / non-sensitive workflows | Low recorded risk; write actions confirm by default; some features usage-priced | HITL default on; admin opt-out per action; usage controls documented |
| Workflows handling API keys / credentials | Custom tools are configured with API keys; Glean's guidance is to prefer product tools for unattended runs; sandbox holds no credentials | Service credentials admin-scoped per system; "No credentials in sandbox"; rotate/revoke guidance |
| Cloud version (multi-tenant) | Single-tenant project per customer; isolation evidence is vendor documentation plus NDA-gated SOC 2 Type II / ISO 27001; anonymized analytics leave the tenant by default | Per-tenant, per-session sandbox; customer-hosted GCP/AWS option |
| Medical / financial / legal data | HIPAA BAA available; ISO 42001; DPF and DPA; sub-processors include multiple US LLM providers under zero-retention terms | Customer selects CSP and region; LLM region determined by provider on Glean key |

### Reference Information
- Administrators may wish to review which write actions are marked "Run without user confirmation" and the Default Member setting "Can create and publish agents" (On by default) before enabling scheduled or independent agents.
- Organizations with data-minimization requirements may wish to ask Glean about the anonymized analytics log sink to central infrastructure, since no opt-out procedure is documented publicly.
- Customer-hosted deployments receive a per-release vulnerability report (HTML and CSV) in the release-notes bucket; reviewing it alongside internal scanning is one way to track dependency exposure.

### Bias Disclosure
"This evaluation uses Claude (Anthropic) as its tooling. Anthropic operates in the AI agent market and may compete with some evaluated vendors. VERDICT discloses this relationship in every report and applies identical evaluation criteria to all platforms regardless of their relationship to Anthropic."

Product-level integration disclosure: Anthropic PBC is listed on Glean's sub-processor list as an LLM Provider (last updated July 28, 2026) and Claude models are among the models selectable in Glean's Model Hub; Glean also publishes a "Glean vs Claude Enterprise" comparison page. These are standard model-provider and market-competition relationships; framework Triggers 0–3 do not fire. The record carries the structured tag `evaluator-coi`.

---

## Future Evaluation Plan

| Phase | Content | Planned timing |
|---|---|---|
| Layer 1 | Behavioral testing on free tier (30 runs × 4 difficulty levels across 3+ days) | Not scheduled: no public free tier confirmed (demo-request only); awaits a public trial surface |
| Layer C interrupt lane | T1–T5 monitoring: CVE/GHSA attributable to Glean products, KEV, supply chain (`@gleanwork/*`, extension), incidents from two independent sources, ToS/DPA/ownership changes | Continuous via Operations sweeps |
| Layer C routine | R, T, V re-evaluated; D, I, C carried forward only under carry-forward conditions | 365 days from 2026-09-24 (provisional pending ReviewCadence-002) |

---

**Framework version:** VERDICT v0.3.2
**Evaluator model:** claude-fable-5-1

```japanese-summary
# Glean Agents 評価結果サマリー

## 基本情報
- スコア: 73/85 (Layer 0)
- ランク: 1 / 70（現行 platforms.json 69 件 + 本件。pipeline 再計算で確定）
- 評価日: 2026.09.24
- 対象バージョン: Glean Agents（GA 2025-05-20）、Glean クラウド基盤の 2026-09 時点公開ドキュメント準拠、Independent agents はベータ
- 運営: Glean Technologies, Inc.（デラウェア州法人、本社 San Francisco、Palo Alto オフィス）
- 独立性: ✅ Independent

## 次元スコア
- V (検証可能性): 14/20
- R (耐性): 20/20
- D (データ運用): 12/15
- I (制御): 10/10
- C (封じ込め): 10/10
- T (透明性): 7/10

## 主要ポジティブ所見
- 対話セッションの書き込みアクションは既定でユーザー承認待ちになり、確認省略は管理者による明示的なアクション単位のオプトイン
- エージェントは作成者・公開者に関係なく「実行した署名済みユーザー」の権限で実行（権限ミラーリング）。Independent agents は管理者がシステム単位でスコープした service credential を使用
- Agent Sandbox は許可リスト方式（既定は読み取り専用ネイティブツール、PTC で書き込み不可、外部通信は許可ドメインのみ、sandbox 内に資格情報なし、セッション単位の呼び出し上限）
- 顧客ごとの単一テナントクラウドプロジェクト（顧客ホスト GCP/AWS または Glean ホスト）
- SOC 2 Type II・ISO 27001・ISO 42001・HIPAA・TX-RAMP Level 2、日付付きサブプロセッサ一覧（2026-07-28 更新）、DPA・DPF 認証
- 「学習・テストに使用しない」明記と LLM プロバイダのゼロ日保持、カテゴリ別の保持期間（チャット履歴 Off/30/90/180/365 日、監査ログ既定 30 日）
- 署名済みアーティファクトと binary authorization、リリース単位の脆弱性ゲーティングを公開する SDLC ドキュメント、公開ステータスページ、公開 Bugcrowd プログラム

## 主要リスク所見
- クローズドソース。SOC 2 Type II レポート、Security Standard、ペネトレーションテスト結果は NDA 下の Trust Portal 限定
- 匿名化（ハッシュ化）分析ログの Glean 中央基盤への既定エクスポートに、公開されたオプトアウト手順なし（D データ最小化 0/3）
- 公開 CVE・アドバイザリの発行チャネルなし（Bugcrowd と security@ のみ）。顧客ホスト向けの脆弱性レポートはリリース単位で非公開配布
- Slack / Teams 面では書き込み確認の挙動が「変更なし」と記載され、スケジュール実行はガバナンス設定に依存。ユーザー入力待ち中のエージェントはキャンセル不可
- 既定メンバーの「Can create and publish agents」が既定 On。エージェントの権限範囲は実行ユーザーの全権限と同一
- AI であることの開示は Independent agents の agent principal と Builder Assistant のモデル表示に限られ、ユーザー資格情報で実行した書き込みは当該ユーザーに帰属

## インシデント
- 直近12ヶ月の公開CVEなし（2025-09-24〜2026-09-24）。同名の CVE-2026-54339（LeslieLeung/glean RSS リーダー、CVSS 7.7）は無関係製品として除外
- status.glean.com の運用インシデント 9 件（2026 年 7〜9 月、0 分〜8 時間 41 分で解決、うち 3 件は上流 LLM プロバイダの可用性起因）。セキュリティインシデントとしての公開事例なし

## CISA KEV
- 該当なし

## HTMLカード用タグ
- tags: enterprise-ai, agent-platform, enterprise-search, managed-saas, customer-hosted, soc2, iso27001, iso42001, hipaa, gdpr, txramp, human-in-the-loop, agent-sandbox, model-agnostic, mit-2025, evaluator-coi
- incident_tags: none
- owner: Glean Technologies, Inc.
```
