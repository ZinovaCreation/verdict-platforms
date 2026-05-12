LangSmith / LangChain, Inc. (Delaware C-corp, San Francisco) / 55/85 / Tier B / 評価 #062

V (検証可能性): 14/20 High — 法人実体・連絡先・変更履歴は公開で確認可能。SOC 2 Type II は監査済みだがレポート本体は Trust Center のアクセス申請制。SDK は OSS、プラットフォーム本体はクローズドソース。
R (耐性): 9/20 Mid — 直近12ヶ月で5件のCVE/脆弱性。最大 CVSS 8.8 (AgentSmith)。3 サーフェスで URL 検証不備のパターン再発。
D (データ運用): 11/15 High — モデル学習への利用なし・顧客データ所有権・GDPR/HIPAA・US/EU リージョン・自己ホスト Enterprise が明文化。保持期間は 14日/400日 の2段階固定。サブプロセッサー一覧はアクセス制限あり。
I (制御): 8/10 High — SAML SSO・SCIM・RBAC・監査ログ (Enterprise)、Human-in-the-loop は LangGraph ランタイムでネイティブ対応。緊急停止の統合ランブックは非公開。
C (封じ込め): 6/10 Mid — LangSmith Sandboxes は microVM 隔離 (Private Preview)。LangSmith Deployment のテナント隔離は SOC 2 認証参照のみで詳細非公開。
T (透明性): 7/10 High — GitHub Security Advisory は技術詳細・SLA・バグバウンティ規模を公開。NIST AI RMF / ISO 42001 への公開マッピングなし。Trust Center 自体がアクセス制限。

定義的インシデント:
- AgentSmith (CVSS 8.8、CVE 未割当、2025-06-17 公開、2024-11-06 パッチ): Prompt Hub の悪意ある AI エージェントが OpenAI API キー等を窃取
- CVE-2026-25750 (CVSS 8.5、2026-01-07 公開): LangSmith Studio の baseUrl パラメータ未検証によるアカウント乗っ取り
- CVE-2026-25528 (CVSS 6.4、2026-02-09 公開): LangSmith SDK 分散トレーシング baggage ヘッダー経由の SSRF
- CVE-2026-40190 (CVSS 5.6、2026-04-09 公開): LangSmith JS SDK の lodash set() による Prototype Pollution
- CVE-2026-41182 (Moderate、2026-04-14 公開): LangSmith SDK のストリーミング new_token イベントが出力リダクションを回避

パターン記録: 3 つの異なるサーフェス (Prompt Hub / SDK 分散トレーシング / Studio フロントエンド) で攻撃者制御可能な URL/送信先入力の検証不備が反復。各パッチは個別に対応されたが、横断的な信頼境界 URL 検証パターンの統一適用は確認できず。

CISA KEV: なし

バイアス開示: LangChain, Inc. と Anthropic に資本関係なし (公開投資家記録)。LangChain は Claude を first-class LLM provider として支援しており間接的な商業関係あり。VERDICT は Claude (Anthropic) をツールとして使用するため標準バイアス開示を適用。

═══ QA REVIEW ═══
Factual:   PASS — All CVE IDs cross-checked against GitHub Security Advisory Database; CVSS scores match GHSA/NVD/Wiz/Miggo sources; SOC 2 Type II dates match changelog announcements (LangSmith 2024-07, LangGraph Platform 2025-08); operator identity (LangChain, Inc., Delaware C-corp, SF) confirmed via Wikipedia, Crunchbase, PrivCo, and ToS; KNOWN_FACTS.md has no entry for LangChain/LangSmith — no override applied
Legal:     PASS — No intent attribution; no prescriptive negative recommendation; structural pattern recorded as fact ("recurring root-cause class") rather than judgment; positive findings included in every dimension; bias disclosure verbatim and present
Quality:   PASS — All Output Format sections present; Executive Summary 5 sentences and lead with specific finding (55/85); Bias Disclosure verbatim; Japanese summary uses user-specified compact format per engine call rules for prompts #017+; AI-writing blocklist items not present in narrative sections
Result:    CLEARED
══════════════

# VERDICT Evaluation Report — #062 LangSmith

| Field | Value |
|-------|-------|
| Evaluation # | 062 |
| Platform | LangSmith |
| Operator | LangChain, Inc. (Delaware C-corporation, San Francisco, California, US) |
| Independence | Independent of Anthropic (no equity overlap with Anthropic / Anthropic Ventures per public investor records); indirect commercial relationship via Claude API support |
| Evaluation type | Initial |
| Layer | Layer 0 (public documentation only) |
| Framework | VERDICT v0.3.1 |
| Target version | LangSmith Cloud (smith.langchain.com / eu.smith.langchain.com); Self-hosted v0.12.71+ / Helm chart langsmith-0.12.33+ |
| Evaluation date | 2026.05.12 |
| Previous evaluation | None |
| Evaluator | VERDICT engine (Claude Opus 4.7, Anthropic) |

---

## Executive Summary

LangSmith presents a mature commercial observability platform with documented SOC 2 Type II attestation (extended to LangGraph Platform / LangSmith Deployment in August 2025), GDPR and HIPAA compliance, US and EU regional data residency, an explicit "no model training on customer data" commitment, and a documented self-hosted Enterprise deployment option for organizations requiring data to stay inside their own infrastructure. Within the trailing twelve months, five distinct platform or SDK vulnerabilities have been disclosed and patched — most notably CVE-2026-25750 (LangSmith Studio account-takeover via baseUrl parameter injection, CVSS 8.5) and the AgentSmith Prompt Hub finding (CVSS 8.8, publicly disclosed June 2025 following an October–November 2024 fix). Three of these involved insufficient validation of attacker-controllable URL or destination inputs across separate surfaces (Studio, SDK distributed tracing, Prompt Hub), a recurrence the engine records as a structural pattern rather than isolated bugs. The Trust Center centralizes compliance artifacts (SOC 2 report, subprocessor list, penetration test summaries, security policies) but gates access behind an authenticated request flow, which limits public verifiability of items that vendors at peer scale often publish openly. Layer 0 total: 55/85.

---

## Scorecard

| Dimension | Score | Max | Rating |
|-----------|-------|-----|--------|
| V — Verifiability | 14 | 20 | High |
| R — Resilience | 9 | 20 | Mid |
| D — Data Conduct | 11 | 15 | High |
| I — Identity & Control | 8 | 10 | High |
| C — Containment | 6 | 10 | Mid |
| T — Transparency | 7 | 10 | High |
| **Total (Layer 0)** | **55** | **85** | — |
| E — Effectiveness | not evaluated | 15 | Layer 1+ only |

**CISA KEV:** なし (No LangSmith or LangChain CVE confirmed in the CISA Known Exploited Vulnerabilities catalog as of 2026.05.12).

---

## Dimension Detail

### V — Verifiability | 14/20 (High)

| Criterion | Result | Score | Evidence URL |
|-----------|--------|------:|--------------|
| Developer / company identity | LangChain, Inc. (Delaware C-corp) named consistently across ToS, Privacy Policy, Trust Center, GitHub; corporate contact via privacy@langchain.dev, security@langchain.dev, support.langchain.com | 4/4 | https://www.langchain.com/terms-of-service ; https://www.langchain.com/privacy-policy |
| Source code disclosure | LangSmith Platform backend closed-source; LangSmith SDK (Python `langsmith`, JS `langsmith`) MIT-licensed and publicly maintained at langchain-ai/langsmith-sdk | 2/4 | https://github.com/langchain-ai/langsmith-sdk |
| Version management transparency | Public changelog at changelog.langchain.com with cadenced release notes; SDK release history at PyPI and npm | 3/3 | https://changelog.langchain.com/ ; https://pypi.org/project/langsmith/#history |
| Third-party dependency disclosure | Subprocessor list referenced via Trust Center but gated behind access-request flow; last-updated date and notification mechanism not publicly visible | 1/3 | https://trust.langchain.com/resources ; https://support.langchain.com/articles/9852244333 |
| Independent certification | SOC 2 Type II attested July 2024 (LangSmith) and August 2025 (LangGraph Platform / LangSmith Deployment); report distributed through Trust Center under access request rather than publicly published | 2/4 | https://changelog.langchain.com/announcements/langsmith-is-now-soc-2-type-ii-compliant ; https://trust.langchain.com/ |
| Functional reproducibility docs | Complete API reference at reference.langchain.com and behavioral documentation at docs.langchain.com/langsmith covering tracing, evaluation, prompts, deployment, and platform setup | 2/2 | https://docs.langchain.com/langsmith ; https://reference.langchain.com/ |

**Positive findings.** Operator identity, contact channels, and version history are unambiguously verifiable from primary sources. Public documentation depth across SDK reference, behavioral specification, and changelog meets enterprise-grade expectations.

**Recorded concerns.** Compliance artifacts (SOC 2 report, subprocessor list, penetration-test summaries, network diagrams) are centralized but access-gated through Trust Center rather than published openly. The SOC 2 Type II audit firm and validity-period dates are not visible without completing the access request. Subprocessor last-updated date and notification mechanism not confirmable from public documents.

### R — Resilience | 9/20 (Mid)

CVE evaluation period: 2025-05-12 → 2026-05-12 (trailing 12 months).

| Criterion | Result | Score | Evidence URL |
|-----------|--------|------:|--------------|
| CVE count (trailing 12 months) | 5 distinct vulnerabilities disclosed: AgentSmith (CVSS 8.8, no CVE ID assigned, public disclosure June 17, 2025), CVE-2026-25750 (CVSS 8.5), CVE-2026-25528 (CVSS 6.4), CVE-2026-40190 (CVSS 5.6), CVE-2026-41182 (CVSS unstated, Moderate). No CVSS 9.0+ in scope; no count penalty applied | 2/5 | https://github.com/langchain-ai/langsmith-sdk/security ; https://www.miggo.io/post/hack-the-ai-brain-uncovering-an-account-takeover-vulnerability-in-langsmith |
| Maximum CVSS severity | 8.8 (AgentSmith), in 7.0–8.9 range | 2/6 | https://thehackernews.com/2025/06/langchain-langsmith-bug-let-hackers.html |
| Patch response speed | AgentSmith: 8 days from researcher report (2024-10-29) to fix deployment (2024-11-06); CVE-2026-25750: SaaS patch 2025-12-15, self-hosted patch 2025-12-20, public advisory 2026-01-07; CVE-2026-25528 fixed in `langsmith` 0.6.3 / 0.4.6 | 2/3 | https://noma.security/blog/how-an-ai-agent-vulnerability-in-langsmith-could-lead-to-stolen-api-keys-and-hijacked-llm-responses/ |
| Structural issues | Three separate URL/destination-validation failures across distinct surfaces (Prompt Hub proxy provider in AgentSmith; LangSmith SDK baggage-header api_url in CVE-2026-25528; LangSmith Studio baseUrl parameter in CVE-2026-25750) — the engine records this as a recurring root-cause class rather than isolated independent bugs | 0/3 | https://github.com/advisories/GHSA-v34v-rq6j-cj6p ; https://thehackernews.com/2026/03/ai-flaws-in-amazon-bedrock-langsmith.html |
| Supply chain compromise (trailing 12 months) | No public compromise of `langsmith` (PyPI or npm) packages or langchain-ai publishing credentials confirmed in trailing 12 months | 3/3 | https://pypi.org/project/langsmith/ ; https://www.npmjs.com/package/langsmith |

**Positive findings.** Patch deployment was prompt in the documented case (AgentSmith fixed within 8 days of report). The platform maintains an active GitHub Security Advisory program with detailed advisories on langchain-ai/langsmith-sdk (GHSA-v34v-rq6j-cj6p, GHSA-fw9q-39r9-c252, GHSA-rr7j-v2q5-chgv) and a published bug-bounty scope and reward scale. No supply-chain compromise of `langsmith` packages confirmed.

**Recorded concerns.** Five vulnerabilities disclosed in trailing twelve months across the LangSmith product surface, with two rated High (CVSS 8.5 and 8.8). The recurring URL-validation root-cause class across three product surfaces (Prompt Hub, SDK distributed tracing, Studio) suggests systematic input-validation patterns are not yet applied uniformly across product boundaries. Status pages (status.smith.langchain.com / eu.status.smith.langchain.com) record availability incidents but published SLA commitments per pricing tier are not publicly enumerated outside Enterprise contracts.

### D — Data Conduct | 11/15 (High)

| Criterion | Result | Score | Evidence URL |
|-----------|--------|------:|--------------|
| GDPR compliance disclosure | DPA available at langchain.com/DPA via pre-signed DocuSign; EU region (eu.smith.langchain.com) available on all plans; explicit GDPR compliance statement | 3/3 | https://docs.langchain.com/langsmith/regions-faq ; https://changelog.langchain.com/announcements/eu-data-residency-for-langsmith |
| Data minimization | Studio collects usage analytics by default for logged-in users (opt-out via anonymous mode); CLI telemetry opt-out documented; client-side trace redaction APIs (`create_anonymizer`, `hide_outputs` / `hideOutputs`) available | 1/3 | https://docs.langchain.com/langsmith/data-storage-and-privacy |
| AI training use | Explicit "We will not train on your data, and you own all rights to your data" in Pricing FAQ, ToS, and product page; retention tiers documented (14-day base / 400-day extended) | 4/4 | https://docs.langchain.com/langsmith/pricing-faq ; https://www.langchain.com/langsmith |
| Sub-processor transparency | List referenced through Trust Center under access-request flow; last-updated date and customer notification mechanism not visible without access | 1/3 | https://trust.langchain.com/ |
| Data retention disclosure | Per-category retention documented: trace base tier 14 days, extended tier 400 days; not currently configurable in-product; deletion within 30 days of customer written request per ToS | 2/2 | https://support.langchain.com/articles/6604776514-can-i-configure-data-retention-periods-for-traces ; https://www.langchain.com/terms-of-service |

**Positive findings.** AI training opt-out is unambiguous and consistent across Pricing FAQ, ToS, and marketing surfaces. Customer data ownership is explicit. Retention tiers are clearly documented and customer-selectable per trace. EU region is available across all plans (not Enterprise-gated). Client-side redaction primitives (`create_anonymizer`, output-hiding hooks) operate before trace serialization, allowing PII to be stripped before it crosses any trust boundary.

**Recorded concerns.** Retention is two-tier and fixed (14-day or 400-day) rather than continuously configurable; organizations with sub-14-day deletion requirements must rely on API-driven deletion or self-hosted deployment. Subprocessor list visibility is gated. CVE-2026-41182 (Streaming token events bypass output redaction) revealed that `hideOutputs` / `hide_outputs` did not cover streaming `new_token` events prior to SDK versions 0.5.19 (JS) / 0.7.31 (Python), creating a documented case where the redaction control did not match its advertised scope until patched.

### I — Identity & Control | 8/10 (High)

| Criterion | Result | Score | Evidence URL |
|-----------|--------|------:|--------------|
| Emergency stop documentation | Tracing disable via `LANGSMITH_TRACING=false` environment variable; LangSmith Deployment supports shutdown via control plane; sandbox lifecycle is ephemeral by design — but a single canonical "emergency stop" procedure for production agents is not centrally documented as a runbook | 2/4 | https://docs.langchain.com/langsmith/data-storage-and-privacy |
| Human-in-the-loop design | Native HITL support in LangGraph runtime (interrupt-and-resume); annotation queues for human review built into the platform; documented as first-class concept | 3/3 | https://www.langchain.com/langsmith-platform ; https://docs.langchain.com/langsmith/pricing-faq |
| Permission delegation transparency | RBAC documented (Enterprise tier); SAML SSO (Enterprise), SCIM provisioning (Enterprise), workspace and organization hierarchy, API key scoping at project / org / service-key level documented | 3/3 | https://docs.langchain.com/langsmith/user-management ; https://changelog.langchain.com/announcements/saml-sso-for-unified-access-to-langsmith |

**Positive findings.** Enterprise identity controls (SAML SSO, SCIM, RBAC) cover the standard procurement requirements. Audit logs are available in self-hosted v0.12.33+ and stored in OCSF 1.7.0 format compatible with SIEM tools (Splunk, Datadog). Human-in-the-loop is a first-class runtime concept rather than an after-thought.

**Recorded concerns.** RBAC, SAML SSO, SCIM, and audit logs are Enterprise-plan-gated; Developer and Plus plans default to admin-role-for-all and do not receive granular access control. A consolidated production-agent "emergency stop" runbook for LangSmith Deployment is not surfaced as a single referenceable document.

### C — Containment | 6/10 (Mid)

| Criterion | Result | Score | Evidence URL |
|-----------|--------|------:|--------------|
| Sandbox design | LangSmith Sandboxes (in Private Preview at evaluation date) documented to use microVM isolation with Authentication Proxy; sandbox technology for general LangSmith Deployment / LangGraph Cloud agent runtime not publicly detailed beyond reference to AWS/GCP managed infrastructure | 2/4 | https://blog.langchain.com/introducing-langsmith-sandboxes-secure-code-execution-for-agents/ ; https://docs.langchain.com/langsmith/deployment |
| Least privilege | RBAC default in Enterprise with workspace isolation; API keys scoped per project / org; self-hosted disables Agent Builder via configuration | 3/3 | https://docs.langchain.com/langsmith/pricing-faq#how-do-i-disable-agent-builder |
| Tenant isolation (cloud) | SOC 2 Type II attestation referenced as evidence of tenant-isolation controls; specific architectural details (database isolation, encryption-key management, cross-tenant boundaries) not disclosed beyond attestation references in public documents | 1/3 | https://trust.langchain.com/ |

**Positive findings.** LangSmith Sandboxes (Private Preview) specify microVM-grade isolation with Auth Proxy that keeps credentials off the sandbox runtime. Multi-deployment architecture supports Cloud SaaS, Self-Hosted Data Plane (hybrid), Self-Hosted Control Plane, and Standalone Container — covering a range of data-residency and isolation needs. RBAC and workspace boundaries documented.

**Recorded concerns.** Public technical depth on tenant isolation between cloud customers is limited to SOC 2 Type II attestation references. The full architectural specification of agent-runtime isolation for LangSmith Deployment (the operator-side LangGraph runtime) is not surfaced in the public documentation. LangSmith Sandboxes — the documented microVM-isolated execution surface — is in Private Preview rather than general availability at evaluation date.

### T — Transparency | 7/10 (High)

| Criterion | Result | Score | Evidence URL |
|-----------|--------|------:|--------------|
| CVE publication posture | LangChain issues GHSA advisories with detailed technical descriptions, affected versions, patch versions, and credits across `langchain-ai/*` repositories; CVE assignment is consistent (CVE-2026-25528, CVE-2026-25750, CVE-2026-40190, CVE-2026-41182) | 2/2 | https://github.com/langchain-ai/langsmith-sdk/security |
| Incident disclosure speed | CVE-2026-25750 cloud fix 2025-12-15, public advisory 2026-01-07 (≈23 days); AgentSmith fix 2024-11-06, public researcher disclosure 2025-06-17 (vendor coordinated extended embargo) | 2/2 | https://www.miggo.io/post/hack-the-ai-brain-uncovering-an-account-takeover-vulnerability-in-langsmith |
| Security policy publication | SECURITY.md published with scope, reporting channels, response targets (initial response 4 business days; triage 15 business days), bug-bounty severity tiers and reward scale; security@langchain.dev contact | 2/2 | https://github.com/langchain-ai/langsmith-sdk/security |
| AI safety framework reference | No public mapping to NIST AI RMF, ISO/IEC 42001, or EU AI Act framework surfaced on Trust Center or marketing pages at evaluation date | 0/2 | (absence-of-evidence) |
| AI system identity disclosure | LangSmith embedded AI features (Polly assistant, Insights Agent) documented in product reference; first-call AI-identity disclosure surfaces visible in docs rather than enforced UI labels by default | 1/2 | https://docs.langchain.com/langsmith/polly |

**Positive findings.** GitHub Security Advisory practice is consistent, technically detailed, and credits external researchers. Vulnerability reporting channel, bug-bounty scope, severity definitions, and reward scale are publicly documented. Two regional status pages (US and EU) operate with public incident history.

**Recorded concerns.** No public mapping to a recognized AI safety framework (NIST AI RMF, ISO/IEC 42001) is published on Trust Center or marketing surfaces. The Trust Center itself is access-gated, which limits how much of LangChain's transparency posture can be assessed from public documents alone — vendors at similar scale (e.g., Anthropic, OpenAI) publish at least summary trust pages openly.

---

## Incident Timeline

| Date (disclosure) | CVE / Identifier | CVSS | Description | Patch status | KEV |
|------|------|------|-------------|--------------|-----|
| 2025-06-17 | AgentSmith (no CVE) | 8.8 | LangSmith Prompt Hub: malicious AI agent could be uploaded with a custom proxy provider URL, capturing OpenAI API keys, prompts, and other data from users who cloned and tried the agent | Patched 2024-11-06 (backend fix + cloning warning banner); embargoed from researcher notification 2024-10-29 to public disclosure 2025-06-17 | No |
| 2026-01-07 | CVE-2026-25750 | 8.5 | LangSmith Studio: missing validation of `baseUrl` URL parameter allowed an attacker-controlled link to redirect an authenticated user's bearer token, user ID, and workspace ID to an attacker-controlled domain (account takeover via 5-minute valid session token) | SaaS patched 2025-12-15; self-hosted patched in v0.12.71 / Helm chart langsmith-0.12.33 on 2025-12-20 | No |
| 2026-02-09 | CVE-2026-25528 (GHSA-v34v-rq6j-cj6p) | 6.4 (Medium) | LangSmith SDK distributed tracing: `RunTree.from_headers()` / `fromHeaders()` accepted attacker-injected `api_url` values via the HTTP `baggage` header, producing SSRF that exfiltrated trace data to attacker-controlled endpoints | Patched in `langsmith` Python 0.6.3 and JS 0.4.6 | No |
| 2026-04-09 | CVE-2026-40190 (GHSA-fw9q-39r9-c252) | 5.6 (Medium) | LangSmith JS SDK: prototype pollution via incomplete `__proto__` guard in internally vendored lodash `set()` utility, exploitable through the `createAnonymizer()` API when an attacker controls keys in data being anonymized | Patched in `langsmith` JS 0.5.18 | No |
| 2026-04-14 | CVE-2026-41182 (GHSA-rr7j-v2q5-chgv) | Moderate | LangSmith SDKs: `hideOutputs` / `hide_outputs` output redaction did not cover the streaming `new_token` events array, allowing sensitive LLM streaming output to bypass redaction and reach LangSmith logs | Patched in `langsmith` JS 0.5.19 and Python 0.7.31 | No |

LangChain framework CVEs disclosed in the trailing twelve months that are not in scope for LangSmith but contextually relevant to the same-operator ecosystem (LangSmith Deployment / LangGraph Cloud operator infrastructure may execute langchain-core code server-side when running customer LangGraph agents): CVE-2025-68664 (langchain-core dumps/loads serialization injection, CVSS 9.3, Critical, patched in `langchain-core` 0.3.81 and 1.2.5, disclosed 2025-12-23), CVE-2025-68665 (LangChain JS equivalent, CVSS 8.6).

---

## Contextual Analysis

LangSmith occupies the LLM observability and agent evaluation category as the commercial product of LangChain, Inc. — the same operator that maintains the open-source LangChain framework and LangGraph orchestration library. The shared operator structure produces a coherent ecosystem story: the SDK is open-source (langchain-ai/langsmith-sdk, MIT), customers can self-host the entire platform under Enterprise terms, and the commercial cloud deployment runs traces in GCP us-central-1 (US) or the EU region. The platform is framework-agnostic by design and ingests traces from applications built on OpenAI SDK, Anthropic SDK, Vercel AI SDK, LlamaIndex, or any OpenTelemetry-instrumented runtime — not only LangChain-framework applications.

The five vulnerabilities disclosed in the trailing twelve months span Studio (Cloud frontend), SDK (Python and JS), and Prompt Hub (community-sharing feature). Three of them — AgentSmith (Prompt Hub proxy provider URL), CVE-2026-25528 (SDK baggage-header `api_url`), and CVE-2026-25750 (Studio `baseUrl`) — share a common root-cause class: insufficient validation of attacker-controllable URL or destination inputs that allow cross-domain data flow. Each was patched in distinct code paths and surfaces, and patch deployment for the documented AgentSmith case was 8 days from researcher report to fix. The recurrence pattern, however, suggests that a uniform "trust-boundary URL-validation" engineering control has not yet been applied consistently across all customer-facing surfaces — a structural observation, not an inference of intent. The other two SDK CVEs (CVE-2026-40190 prototype pollution; CVE-2026-41182 streaming-event redaction bypass) represent incomplete-coverage patterns in defensive logic (the lodash `set()` guard only covered `__proto__`; the redaction pipeline only covered `inputs`/`outputs` fields and not the `events` array).

The Trust Center centralizes a substantial set of artifacts: SOC 2 Type II audit reports, GDPR/HIPAA/Risk-Management/Access-Control policies, penetration test executive summaries, network and system architecture documentation, and a current subprocessor list. This is the structural posture of an enterprise-grade compliance program. The access-request gating model limits how much can be verified from purely public documents — peer vendors of comparable scale frequently publish at least summary trust pages openly. The DPA itself is pre-signed via DocuSign and customers retain executed copies, which is a frictionless legal-onboarding pattern.

LangSmith's two-tier retention (14-day base / 400-day extended) is unusually rigid for an observability platform — most peer observability tools offer continuously configurable retention. The structural rationale (pricing differentiation between $2.50/1K and $5.00/1K trace tiers) is documented but is not the same as configurable retention. Self-hosted Enterprise deployment removes this constraint entirely by giving the customer full control of underlying storage retention.

LangChain, Inc. supports Claude (Anthropic) as one of multiple first-class LLM providers across its products. This produces an indirect commercial relationship between LangChain and Anthropic — recorded here as a structural fact, not as a quality signal — and the standard VERDICT Bias Disclosure applies.

---

## VERDICT Record

**Summary.** LangSmith scores 55/85 (Layer 0) under VERDICT Framework v0.3.1, with strengths in operator verifiability, customer data conduct, identity and access controls, and security-disclosure transparency, and recorded concerns around recurring URL-validation root-cause class across three product surfaces, access-gated Trust Center documentation, and Layer-0-unverifiable specifics of multi-tenant isolation architecture.

**Risk Factor Summary by Use Case.**

| Use case | Risk profile |
|----------|--------------|
| Internal testing / development | Low — free tier and Developer plan are appropriate; tracing is opt-in via SDK and disable-able via `LANGSMITH_TRACING=false`; client-side redaction primitives available |
| Credential-handling workloads | Mid — five trailing-12-month vulnerabilities in the platform/SDK include three URL-trust failures and one redaction-coverage failure that have direct credential-exfiltration impact when chained with prompt injection; mitigation requires SDK version pinning (`langsmith>=0.7.31` Python / `langsmith>=0.5.19` JS) and disabling streaming where sensitive output flows through redaction |
| Cloud multi-tenant deployments | Mid — SOC 2 Type II attestation referenced for tenant isolation; specific isolation architecture not publicly disclosed beyond attestation; Enterprise customers receive workspace-level RBAC, SAML SSO, SCIM, and audit logs |
| Regulated-data workloads (PHI / regulated PII) | Mid → Low (self-hosted) — HIPAA BAA available only on Enterprise plan; for organizations with sub-14-day deletion requirements or "no data leaves environment" mandates, the self-hosted deployment option (Customer-managed Kubernetes on AWS / GCP / Azure) removes the cloud-retention and subprocessor-disclosure constraints |

**Reference Information** (options, not instructions).

- Organizations evaluating LangSmith for credential-handling agents may pin SDK versions to the latest patched releases (`langsmith>=0.7.31` for Python and `>=0.5.19` for JavaScript) and verify their applications do not depend on `secrets_from_env=True` when interacting with langchain-core (CVE-2025-68664 default changed to `False` in patched versions).
- Organizations with strict data-residency requirements may evaluate the self-hosted Enterprise deployment option, which delivers LangSmith to customer-managed Kubernetes on AWS, GCP, or Azure.
- Organizations with non-Enterprise procurement constraints can sign the pre-signed DPA via DocuSign at langchain.com/DPA without bilateral negotiation overhead.

**Bias Disclosure.**

> This evaluation uses Claude (Anthropic) as its tooling. Anthropic operates in the AI agent market and may compete with some evaluated vendors. VERDICT discloses this relationship in every report and applies identical evaluation criteria to all platforms regardless of their relationship to Anthropic.

LangChain, Inc. supports Claude as one of multiple first-class LLM providers in its products, producing an indirect commercial relationship. No equity relationship between Anthropic / Anthropic Ventures and LangChain, Inc. exists per public investor records.

---

## Future Evaluation Plan

- **Layer 1 (behavioral testing) timing.** Defer until a stable free-tier methodology is established for measuring trace-ingestion fidelity, evaluator-effectiveness benchmarks against a standardized dataset, and prompt-regression detection accuracy. Estimated window: Q3 2026.
- **Layer C (continuous monitoring) cadence.** Monthly check for new GHSA advisories on `langchain-ai/langsmith-sdk`, `langchain-ai/langchain`, `langchain-ai/langgraph`, and `langchain-ai/langgraph-platform`; quarterly check of CISA KEV catalog for LangChain-family entries; immediate re-evaluation trigger on CVSS 7.0+ CVE in `langsmith` SDK or `smith.langchain.com` platform.
- **Differential re-evaluation trigger.** Mandatory upon any of: (a) Trust Center transition to publicly accessible content; (b) general availability of LangSmith Sandboxes with publicly documented microVM specification; (c) new CVE in scope; (d) routine 90-day review.

---

Score: 55/85
V: 14/20, R: 9/20, D: 11/15, I: 8/10, C: 6/10, T: 7/10
Dimensions verified: V+R+D+I+C+T = 55

Tier: B
Category: LLM Observability · Agent Evaluation Platform