---
name: Gemini Code Assist
slug: gemini-code-assist
operator: Google LLC
independence: subsidiary
parent_entity: Alphabet Inc.
category: AI Coding Agent
homepage: https://cloud.google.com/products/gemini/code-assist
github: https://github.com/google-gemini/gemini-cli
evaluation_number: 56
evaluation_type: initial
evaluated_at: '2026-04-11'
evaluator_model: claude-opus-4-7
framework_version: v0.3.1-final
layer: '0'
target_version: null
previous_evaluation_date: null
previous_score: null
score: 67
max_score: 85
tier: S
verdict:
  v:
    score: 17
    rating: High
    note: ''
  r:
    score: 17
    rating: High
    note: ''
  d:
    score: 11
    rating: High
    note: ''
  i:
    score: 6
    rating: Mid
    note: ''
  c:
    score: 6
    rating: Mid
    note: ''
  t:
    score: 10
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
supply_chain_compromise_12mo: false
known_facts_applied: []
qa:
  factual: pass
  legal: pass
  quality: pass
  revision_cycles: 0
  flagged: false
differential: null
next_review_due: '2026-07-10'
tags:
- ai-coding-agent
- enterprise-saas
- closed-source
- iso-42001
- saif
- ip-indemnification
- source-citation
- vpc-service-controls
rank: 1
"finding": |-
  Highest cert portfolio in the index. ISO 42001 (May 2025) — unique among AI agent platforms in VERDICT. SOC 1/2/3 + ISO 27001 + FedRAMP + HIPAA-BAA + PCI DSS. SAIF + NIST AI RMF. Zero direct Code Assist CVEs in trailing 12 months. Standard/Enterprise contractually exempt from training; Individuals tier defaults to data collection (opt-out flow reported confusing in GitHub Issues #14104, #17480, #20569).
"meta_owner": |-
  Google LLC · Subsidiary of Alphabet Inc. · Public Company
"meta_description": |-
  Independent security evaluation of Gemini Code Assist by Google LLC. Score: 67/85. ISO 42001 (only in index) + SOC 1/2/3 + FedRAMP + HIPAA-BAA. Zero direct CVEs. SAIF + NIST AI RMF. Tier-stratified training policy. Framework v0.3.1.
"og_description": |-
  Independent security evaluation of Gemini Code Assist by Google LLC. Score: 67/85. ISO 42001 (only in index) + SOC 1/2/3 + FedRAMP + HIPAA-BAA. Zero direct CVEs. SAIF + NIST AI RMF. Framework v0.3.1.
"category_line": |-
  AI Coding Agent · Enterprise SaaS · Proprietary
display_tags:
- text: ISO 42001 · Only in Index
  color: safe
- text: SOC 1/2/3 + FedRAMP + HIPAA
  color: safe
- text: SAIF + NIST AI RMF
  color: safe
- text: Individuals Tier Training Default-On
  color: amber
---

# Gemini Code Assist

## Executive Summary

Gemini Code Assist scores **67/85 (S-tier)** on Layer 0, placing #2 in the VERDICT index between Amazon Q Business (68) and Vertex AI Agent Builder (65). The platform's strengths concentrate in verifiability — the most extensive certification portfolio in the index, uniquely including ISO 42001 (AI management system, May 2025) — and transparency, where Google's publicly documented Secure AI Framework (SAIF), NIST AI RMF alignment, automatic source citation when code suggestions directly quote existing sources, and IP indemnification for paid tiers represent category-leading compliance features. Zero CVEs were attributed to Gemini Code Assist itself in the trailing 12-month window. The recorded concerns concentrate in two areas: (1) a tier-stratified data policy in which Gemini Code Assist for Individuals (free tier) defaults to data collection for model training with opt-out flow difficulties documented in multiple GitHub issues (#14104, #17480, #20569), and (2) an adjacent prompt injection pattern across the broader Gemini product family — Gemini CLI (Tracebit July 2025, Cyera November 2025), Gemini Cloud Assist (Tenable Trifecta October 2025), Gemini Enterprise (Noma Security December 2025), and CVE-2026-0628 in the Chrome Gemini Live panel (CVSS 8.8, January 2026) — none of which directly affect the Code Assist IDE extension but bound the broader risk perimeter, particularly for Individuals-tier users since Gemini CLI is bundled with that tier. Standard and Enterprise tiers using the IDE extension exclusively are materially less exposed.

## Scorecard

| Dimension | Score | Max | Rating |
|---|---:|---:|---|
| V — Verifiability       | 17 | 20 | High (85%)  |
| R — Resilience          | 17 | 20 | High (85%)  |
| D — Data Conduct        | 11 | 15 | High (73%)  |
| I — Identity & Control  |  6 | 10 | Mid  (60%)  |
| C — Containment         |  6 | 10 | Mid  (60%)  |
| T — Transparency        | 10 | 10 | High (100%) |
| **Total (Layer 0)**     | **67** | **85** | **S** |

**CISA KEV:** None. No Gemini Code Assist entries in the CISA Known Exploited Vulnerabilities catalog as of evaluation date. CVE-2026-0628 (Chrome Gemini Live panel, CVSS 8.8) is a distinct Chrome browser vulnerability, not on KEV, and is not Code Assist.

E (Effectiveness) — not evaluated (Layer 1+ only).

Suggested category label: **AI Coding Agent · Enterprise SaaS**.

---

## Dimension Detail

### V — Verifiability (17/20)

| Criterion | Result | Score | Evidence |
|---|---|---:|---|
| Developer / company identity | Confirmed: Google LLC, subsidiary of Alphabet Inc. Public company. Trivially verifiable. | 4/4 | https://cloud.google.com/products/gemini/code-assist |
| Source code disclosure | Partial: Core Gemini Code Assist IDE extension and Gemini for Google Cloud API are proprietary closed-source. Gemini CLI component is Apache 2.0 OSS at github.com/google-gemini/gemini-cli. | 1/4 | https://github.com/google-gemini/gemini-cli |
| Version management transparency | Confirmed: active release notes for Gemini Code Assist extension; Google Cloud Release Notes for the Gemini for Google Cloud API; regular blog posts; Gemini CLI public release history on GitHub. | 3/3 | https://cloud.google.com/gemini/docs/codeassist/release-notes |
| Third-party dependency disclosure | Confirmed: Google Cloud Customer Data Processing Addendum (CDPA) publishes a sub-processor list with regular updates. | 3/3 | https://cloud.google.com/terms/data-processing-addendum |
| Independent certification | Most extensive certification portfolio in VERDICT index: SOC 1, SOC 2 Type II, SOC 3 (Q2 2025 reassessment), ISO 27001, ISO 27017, ISO 27018, ISO 27701, ISO 42001 (AI management system, May 2025 — only platform in VERDICT index with this AI-specific certification), FedRAMP (via Google Cloud), HIPAA-ready with BAA, PCI DSS. | 4/4 | https://cloud.google.com/gemini/docs/codeassist/security-privacy-compliance ; https://www.datastudios.org/post/google-gemini-gdpr-hipaa-and-enterprise-compliance-standards-explained |
| Functional reproducibility documentation | Confirmed: comprehensive documentation at cloud.google.com/gemini/docs/codeassist and developers.google.com/gemini-code-assist; complete API reference, tier comparison, setup guides, privacy notices, FAQs. | 2/2 | https://cloud.google.com/gemini/docs/codeassist/overview |

**Positive findings:** The most extensive certification portfolio in the VERDICT index. ISO 42001 is the ISO/IEC standard for AI management systems, specifically addressing AI governance — Gemini Code Assist workflows are explicitly in scope (per third-party analysis). This is the only platform in the VERDICT index with standing ISO 42001 certification. Google Cloud's compliance infrastructure, FedRAMP authorization, and BAA availability represent institutional-grade compliance.

**Recorded concerns:** Core Gemini Code Assist platform is closed-source. Gemini 2.5 / 3 model architecture not fully documented publicly.

### R — Resilience (17/20)

| Criterion | Result | Score | Evidence |
|---|---|---:|---|
| CVE count (trailing 12 months) | Zero confirmed Code Assist-specific CVEs in NVD or GHSA for the trailing 12-month window (April 9, 2025 → April 8, 2026). CVE-2026-0628 is Chrome Gemini Live panel, not Code Assist. | 5/5 | NVD search ; GHSA search |
| Maximum CVSS severity | N/A (no direct CVEs); adjacent Gemini family CVE-2026-0628 CVSS 8.8 is for Chrome integration, not scored here. | 6/6 | NVD search |
| Patch response speed | No Code Assist-specific CVEs required patching. Adjacent: Gemini CLI prompt injection (Tracebit, June 27, 2025) patched in 0.1.14 on July 25, 2025 (~28 days). CVE-2026-0628 disclosed Oct 23, 2025; patched early January 2026 (~2.5 months). Google VRP infrastructure mature. | 1/3 | https://cyberscoop.com/google-gemini-cli-prompt-injection-arbitrary-code-execution/ |
| Structural issues | Gemini Code Assist itself shows no recurring vulnerability pattern. The broader Gemini product family has accumulated multiple prompt injection findings: Gemini CLI Tracebit (July 2025), Gemini CLI Cyera (November 2025), Gemini Cloud Assist Tenable Trifecta (October 2025), Gemini Enterprise Noma Security (December 2025). Gemini CLI is bundled with Gemini Code Assist for Individuals, making these findings adjacent. | 2/3 | Tenable Research, Tracebit, Cyera, Noma Security |
| Supply chain compromise | No supply chain compromise confirmed for Gemini Code Assist extensions or Gemini CLI npm/pip distributions in the trailing 12-month window. Google Binary Authorization and SLSA-aligned build infrastructure applies. | 3/3 | Advisory searches |

**Positive findings:** Zero direct Code Assist CVEs. Google maintains one of the most mature security response infrastructures in the industry (Google VRP, Google Project Zero, Google Threat Analysis Group). Mature SLSA build infrastructure. Demonstrated 28-day patch response for Gemini CLI Tracebit finding.

**Recorded concerns:** The Gemini product family has a notable pattern of prompt injection findings across multiple agentic surfaces. Gemini CLI — bundled with Gemini Code Assist for Individuals — has received two independent prompt injection findings (Tracebit July 2025 "silent code execution through toxic combination of improper validation, prompt injection, and misleading UX"; Cyera November 2025 "command injection and prompt injection exploitable in production"). The IDE extension surfaces themselves have not received comparable findings, but organizations deploying Gemini CLI in agentic workflows should track this structural concern.

### D — Data Conduct (11/15)

| Criterion | Result | Score | Evidence |
|---|---|---:|---|
| GDPR compliance disclosure | Confirmed: Google Cloud CDPA with Standard Contractual Clauses; EU data residency options; Data Privacy Framework alignment; explicit GDPR compliance statement for Gemini for Google Cloud. | 3/3 | https://cloud.google.com/terms/data-processing-addendum |
| Data minimization | Partial: Enterprise tier has VPC Service Controls, CMEK, Private Google Access, zero data egress configuration. Gemini Code Assist for Individuals (free) defaults to data collection for model training with opt-out. Multiple GitHub issues (#14104, #17480, #20569) report opt-out flow as confusing or "roundabout loop". | 1/3 | https://developers.google.com/gemini-code-assist/resources/privacy-notice-gemini-code-assist-individuals ; https://github.com/google-gemini/gemini-cli/issues/14104 |
| AI training use | Tier-stratified: Individuals (free) — collected and may be used to improve Google's products including model training; opt-out available; human reviewers access disconnected copies up to 18 months. Google AI Pro / Ultra (paid individual) — Developer FAQ states data not used for training (documented inconsistency vs Gemini CLI ToS, Issue #20569). Standard / Enterprise (paid) — contractually exempt from training per CDPA. | 2/4 | https://google-gemini.github.io/gemini-cli/docs/tos-privacy.html ; https://developers.google.com/gemini-code-assist/resources/faqs |
| Sub-processor transparency | Confirmed: Google Cloud sub-processor list published with regular update dates via the CDPA framework. | 3/3 | Google Cloud Trust Center |
| Data retention period disclosure | Confirmed: prompts and responses stored ≤30 days for debugging and abuse detection; Individual tier disconnected copies stored up to 18 months for human review; Workspace admins can shorten or disable prompt storage for Enterprise. | 2/2 | https://www.datastudios.org/post/google-gemini-gdpr-hipaa-and-enterprise-compliance-standards-explained |

**Positive findings:** Google Cloud CDPA with standard GDPR provisions. Explicit published sub-processor list. Retention periods documented per category (≤30 days prompts/responses, 18 months disconnected reviewer copies for Individuals). Standard and Enterprise tiers contractually exempt from model training. VPC Service Controls, CMEK, and Private Google Access for Enterprise data isolation. IP indemnification for paid tiers. Source citation when AI suggestions directly quote existing code.

**Recorded concerns:** The D dimension is the most significant constraint on Gemini Code Assist's overall score. Gemini Code Assist for Individuals (free) defaults to data collection for model training — data is collected by default to "develop and improve Google's machine learning technologies." Opt-out is available but multiple developer-reported GitHub issues document that the opt-out flow is confusing or produces a "roundabout loop" between privacy notice and setup pages. Documentation inconsistency reported between the Gemini CLI ToS page (which states Individual data IS used for training) and the Developer FAQ (which states paid AI Pro subscribers are exempt) — filed as Issue #20569 February 2026. Organizations using Gemini Code Assist on personal Gmail accounts for proprietary code work should verify their opt-out status.

### I — Identity & Control (6/10)

| Criterion | Result | Score | Evidence |
|---|---|---:|---|
| Emergency stop documentation | Partial: standard IDE stop semantics apply; agent mode operations can be cancelled; Gemini CLI Usage Statistics setting provides runtime control over data collection. Specific agent mode emergency stop documentation not consolidated in one place. | 2/4 | Gemini CLI documentation |
| Human-in-the-loop design | Available with caveat: IDE code completion is inherently HITL (user accepts each suggestion); agent mode requests approval. Gemini CLI supports command allowlisting — exact mechanism exploited in Tracebit July 2025 finding via crafted "grep" command containing hidden transfer operations. | 2/3 | https://cyberscoop.com/google-gemini-cli-prompt-injection-arbitrary-code-execution/ |
| Permission delegation chain transparency | Partial: Google Cloud IAM and RBAC available for Enterprise; VPC Service Controls; SSO/SAML via Google Workspace; SCIM provisioning. These controls primarily apply to Enterprise tier. | 2/3 | https://docs.cloud.google.com/gemini/docs/codeassist/faqs |

**Positive findings:** Google Cloud IAM is mature and well-documented. Enterprise tier supports comprehensive access controls (SSO, SCIM, RBAC, VPC SC). IDE code completion is naturally HITL. Source citation provides transparency about when AI suggestions quote existing code.

**Recorded concerns:** Agent mode HITL enforcement depends on user-configured allowlist, which was the exact vector exploited in the Tracebit Gemini CLI finding. The documented attack "through a toxic combination of improper validation, prompt injection and misleading UX" specifically bypassed user approval via a seemingly benign allowlisted command. Individual tier lacks enterprise IAM controls.

### C — Containment (6/10)

| Criterion | Result | Score | Evidence |
|---|---|---:|---|
| Sandbox design philosophy | Hybrid: IDE extensions run in VS Code/JetBrains extension host process; Gemini for Google Cloud API runs in Google's managed infrastructure with tenant isolation; Gemini CLI executes in user's shell environment with filesystem and network access per user credentials. No per-execution sandbox for CLI operations beyond standard OS process isolation. | 2/4 | Architecture review |
| Least privilege principle | Configurable: Enterprise supports IAM-based access control and VPC Service Controls; Gemini CLI runs with user privileges and supports allowlisted commands (bypassed in Tracebit). Defaults are not strictly least privilege. | 1/3 | Documentation review |
| Tenant isolation (cloud version) | Confirmed: Google Cloud provides multi-tenant isolation validated by SOC 2 Type II, ISO 27001, ISO 42001, FedRAMP. Gemini for Google Cloud API "doesn't have access to any of the other APIs or resources in your project." VPC Service Controls + CMEK with EKM/HSM available. | 3/3 | https://cloud.google.com/gemini/docs/codeassist/security-privacy-compliance |

**Positive findings:** Google Cloud's tenant isolation is among the most extensively audited in the industry. SOC 2, ISO 27001, ISO 42001, FedRAMP, PCI DSS all validate isolation boundaries. VPC Service Controls provide customer-configurable isolation perimeters. CMEK with EKM/HSM available for Enterprise. Per-project scoping of Gemini for Google Cloud API access.

**Recorded concerns:** Gemini CLI's allowlist-based command approval was explicitly bypassed in the Tracebit July 2025 finding. Gemini Code Assist for Individuals (free) does not have access to Enterprise containment features. IDE extensions inherit the privileges of the IDE process. Agent mode operations in CLI context can execute with user privileges.

### T — Transparency (10/10)

| Criterion | Result | Score | Evidence |
|---|---|---:|---|
| CVE publication posture | Confirmed: Google Bug Hunters / Vulnerability Reward Program (VRP) publishes confirmed vulnerabilities; Google Cloud Security Bulletins; dedicated AI security research by Google Project Zero and Google Threat Analysis Group; active public disclosure. | 2/2 | https://bughunters.google.com/ |
| Incident disclosure speed | Confirmed: Google publishes security bulletins promptly; multiple documented examples (Tracebit Gemini CLI 28 days, CVE-2026-0628 ~2.5 months, Tenable Trifecta all three patched before disclosure). Detailed Google Cloud Security Blog post-mortems. | 2/2 | https://cyberscoop.com/google-gemini-cli-prompt-injection-arbitrary-code-execution/ |
| Security policy publication | Confirmed: dedicated Gemini Code Assist security, privacy, and compliance page; data governance documentation; privacy notices for each tier; comprehensive Google Cloud Trust Center. | 2/2 | https://cloud.google.com/gemini/docs/codeassist/security-privacy-compliance |
| AI safety framework reference | Confirmed: Google Secure AI Framework (SAIF) — publicly documented AI security framework, widely referenced as a reference architecture. NIST AI RMF alignment. ISO 42001 AI management system certification (May 2025) — only evaluated platform in VERDICT index with this AI-specific certification. Ongoing Responsible AI principles, Red Team research, Gemini model cards. | 2/2 | Google SAIF documentation ; ISO 42001 certification |
| AI system identity disclosure | Confirmed: IDE extension clearly identifies AI-generated suggestions. Source citation is automatically provided when code suggestions directly quote existing sources at length — documented in official FAQs as a compliance feature for license requirements. Generated code clearly distinguished from user-authored code in IDE UX. | 2/2 | https://codeassist.google/products/business |

**Positive findings:** T dimension score of 10/10 reflects Google's industry-leading AI security transparency. Google SAIF (Secure AI Framework) is a widely adopted public framework for AI security. ISO 42001 AI management system certification (May 2025) is rare and specifically addresses AI governance. Google VRP bug bounty, dedicated Gemini security research, and comprehensive public security documentation. Source citation when directly quoting existing code is a category-leading transparency feature. The only platform in the VERDICT index with this combination of published AI safety framework, ISO 42001 certification, and automatic source citation.

**Recorded concerns:** None material at this dimension level. Documentation inconsistencies exist (GitHub Issue #20569) but are tracked and publicly visible, which itself is transparency.

---

## Incident Timeline

Trailing 12-month window: 2025-04-09 → 2026-04-08.

No CVEs were confirmed specifically for Gemini Code Assist (IDE extension or Gemini for Google Cloud API) during the trailing 12-month window.

Adjacent Gemini family security findings (noted for context, not scored directly against Code Assist):

| Date | Finding | Severity | Description | Status | Product affected |
|---|---|---|---|---|---|
| 2025-07 | Tracebit Gemini CLI | Not assigned CVE | Silent code execution via prompt injection in context files combined with allowlist bypass. Discovered June 27, 2025; patched in Gemini CLI 0.1.14 on July 25, 2025 (~28 days). | Patched | Gemini CLI (bundled with Gemini Code Assist for Individuals) |
| 2025-10 | Tenable "Gemini Trifecta" | Critical (pre-patch) | Three vulnerabilities: search-injection in Search Personalization Model; log-to-prompt injection in Gemini Cloud Assist; exfiltration via Gemini Browsing Tool. | Patched before disclosure | Gemini Cloud Assist (distinct from Gemini Code Assist), Search Personalization, Browsing Tool |
| 2025-11 | Cyera Research Labs Gemini CLI | Not assigned CVE | Command injection + prompt injection, both confirmed exploitable in production environments. | Disclosure in progress per blog | Gemini CLI |
| 2025-12 | Noma Security Gemini Enterprise | Not assigned CVE | Indirect malicious prompt technique targeting Gemini Enterprise Edition. | Patched | Gemini Enterprise (distinct product) |
| 2026-01 | CVE-2026-0628 "Glic Jack" | CVSS 8.8 High | Insufficient policy enforcement in WebView tag allowed malicious Chrome extension to inject scripts into privileged Gemini Live panel, accessing local files, camera, microphone. Reported Oct 23, 2025; patched early January 2026 (~2.5 months). | Patched in Chrome 143.0.7499.192 | Chrome Gemini Live panel (distinct from Gemini Code Assist) |

**Note on scope:** CVE-2026-0628 and the Tenable Trifecta affect Gemini products other than Gemini Code Assist and are not scored against Code Assist's R dimension directly. The Tracebit and Cyera findings affect Gemini CLI, which is explicitly bundled with Gemini Code Assist for Individuals, and are reflected in the structural issues consideration within the R dimension.

---

## Contextual Analysis

Gemini Code Assist at 67/85 places 2nd in the VERDICT index, behind Amazon Q Business (68) and ahead of Vertex AI Agent Builder (65). This positioning reflects three distinctive strengths that no other evaluated platform currently matches.

**ISO 42001 AI Management System Certification.** Google achieved ISO 42001 certification in May 2025 — the ISO/IEC standard for AI management systems, specifically addressing AI governance, risk management, and responsible AI development. Per third-party compliance analysis, the ISO 42001 scope "Applies to Gemini for Google Cloud, Vertex AI Agents, and Gemini Code Assist workflows." This is the only platform in the VERDICT index with standing ISO 42001 certification. While SOC 2, ISO 27001, and FedRAMP certifications are shared across multiple evaluated platforms, ISO 42001 represents a materially different certification category focused on AI-specific governance rather than general information security.

**Secure AI Framework (SAIF).** Google publicly documented SAIF as a reference architecture for securing AI systems. SAIF is widely cited in industry as a public AI security framework and predates many competing frameworks. Combined with NIST AI RMF alignment and ISO 42001 certification, this represents the most comprehensive AI safety framework story among evaluated platforms.

**Source Citation and IP Indemnification.** Gemini Code Assist Standard and Enterprise is a "Generative AI Indemnified Service" with automatic source citation when code suggestions directly quote existing sources at length. The combination of IP indemnification (protecting enterprise customers from copyright claims) and transparent source citation (allowing developers to make informed licensing decisions) is a category-leading compliance feature. Only GitHub Copilot Business/Enterprise provides comparable IP indemnification in the evaluated AI coding agent set.

The +5 point margin over Devin (the previous AI coding agent leader at 62/85) is driven primarily by ISO 42001 (+2 T), broader Google Cloud certification stack (+2 V), and SAIF framework documentation (+1 T). The +10 point margin over GitHub Copilot (57/85) — Gemini Code Assist's most direct competitor — is driven by the clearer tier stratification of Gemini's training policy (Standard/Enterprise explicit contractual exemption vs Copilot's April 2026 opt-in change controversy), plus ISO 42001 (+2 T).

**The Gemini family prompt injection pattern.** While Gemini Code Assist's own R dimension scores 17/20 (zero direct CVEs), the broader Gemini product family has accumulated a notable prompt injection pattern across multiple surfaces within the trailing 12-month window. Tenable's "Gemini Trifecta" (October 2025) documented three distinct prompt injection vulnerabilities in Gemini Cloud Assist (log-to-prompt injection via User-Agent headers), Gemini Search Personalization Model (search-injection), and Gemini Browsing Tool (data exfiltration). Tracebit (July 2025) and Cyera Research Labs (November 2025) independently documented prompt injection and command injection in Gemini CLI. Noma Security (December 2025) documented indirect prompt injection in Gemini Enterprise. CVE-2026-0628 "Glic Jack" (Chrome Gemini Live panel, CVSS 8.8) further extended the pattern to browser integrations.

For organizations evaluating Gemini Code Assist, the distinction between the core Code Assist IDE extension (no documented prompt injection findings) and adjacent Gemini surfaces (multiple findings) matters. Gemini Code Assist for Individuals is explicitly bundled with Gemini CLI — the tool that received two independent prompt injection findings — which creates a direct category-adjacent concern for individual developers using CLI workflows. Standard and Enterprise tiers using the IDE extension exclusively are less exposed.

**Tier stratification of data policy.** The Gemini Code Assist tier-stratified data policy is the second most important contextual finding after the compliance portfolio. The distinction is clear in Google's own documentation. Individuals (free) on personal Gmail collects data by default for product improvement and model training; opt-out available but reported to be confusing (GitHub Issues #14104, #17480, #20569); human reviewers access disconnected copies for up to 18 months. Google AI Pro / Ultra (paid individual) — per Developer FAQ, data not used for training (Gemini CLI documentation and Developer FAQ inconsistent on this point per Issue #20569). Standard / Enterprise (paid team/org) — contractually not used for training per Google Cloud CDPA; VPC SC, CMEK, Private Google Access available. This pattern is functionally similar to GitHub Copilot's tier stratification, but Gemini Code Assist's documentation is more explicit about tier differences. The weakest-tier principle (Individual free = opt-in by default) moderates the D dimension score to 11/15, but this is still the second-highest D score among evaluated AI coding agents.

**Gemini Code Assist in GitHub (PR review agent).** The GitHub pull request review agent is a more agentic surface than IDE completion. Available public documentation on its specific permission model, container isolation, and autonomy boundaries is limited in the sources reviewed. This is a Layer 1 evaluation gap worth flagging.

### Economic Risk Note

Pricing: Gemini Code Assist for Individuals (free, no credit card), Standard (~$22.80/user/month), Enterprise (~$54/user/month), Google AI Pro/Ultra (paid individual upgrades with higher limits). Usage-based quota (6,000 code requests/day + 240 chat requests/day for free tier). No documented cost-runaway prevention for agent mode autonomous execution. Google Cloud billing alerts available. Pay-as-you-go available via Vertex AI / Gemini API key authentication.

---

## VERDICT Record

**Summary:** Gemini Code Assist scores 67/85 (S-tier) at Layer 0, with the most extensive compliance portfolio in the VERDICT index (uniquely including ISO 42001), zero direct Code Assist CVEs in the trailing 12-month window, and Google's publicly documented Secure AI Framework, moderated by tier-stratified data handling (Individuals tier defaults to data collection with opt-out flow difficulties) and an adjacent prompt injection pattern across the broader Gemini product family.

**Risk Factor Summary by Use Case:**

| Use case | Risk factors recorded | Key data points |
|---|---|---|
| Internal testing / non-sensitive workflows | Low | Zero Code Assist CVEs. Free tier available. Extensive certification stack. Source citation. |
| Workflows handling API keys / credentials | Low (Enterprise) / Moderate (Individual) | Enterprise: VPC SC, CMEK, IAM. Individual: Gemini CLI bundled — track Tracebit/Cyera prompt injection findings if using CLI. |
| Cloud version (multi-tenant) | Low | Google Cloud SOC 2 + ISO 27001 + ISO 42001 + FedRAMP validated tenant isolation. Gemini for Google Cloud API project-scoped. |
| Medical / financial / legal data | Low (Enterprise) | HIPAA BAA available. FedRAMP via Google Cloud. PCI DSS. ISO 42001 AI governance. Enterprise VPC SC + CMEK. IP indemnification. Organizations should verify BAA scope for specific use cases. |

**Reference Information (options, not directives):**

- ISO 42001 certification (May 2025) is the ISO/IEC standard for AI management systems and is explicitly documented as applying to Gemini Code Assist workflows. Organizations with internal AI governance requirements may wish to reference this certification in procurement decisions.
- The Gemini Code Assist for Individuals privacy notice states that data is collected by default for product and model improvement. Developers using the free tier for proprietary code work may wish to verify their opt-out status in the VS Code / JetBrains extension settings. Multiple GitHub issues (#14104, #17480, #20569) document reported difficulties with the opt-out flow.
- Gemini CLI — bundled with Gemini Code Assist for Individuals — has received independent prompt injection findings (Tracebit July 2025, Cyera November 2025). Organizations using Gemini CLI for agentic coding workflows may wish to stay current with the latest Gemini CLI version and review allowlist configurations.

**Bias Disclosure:**

> This evaluation uses Claude (Anthropic) as its tooling. Anthropic operates in the AI agent market and may compete with some evaluated vendors. VERDICT discloses this relationship in every report and applies identical evaluation criteria to all platforms regardless of their relationship to Anthropic.

Methodology note for this specific report: Google is a direct competitor to Anthropic across multiple dimensions. (1) Foundation model competition: Gemini 2.5 / 3 is a directly competing frontier foundation model against Claude (Opus, Sonnet, Haiku); Gemini Code Assist is powered by Gemini, while Claude Code is powered by Claude. (2) AI coding agent competition: Gemini Code Assist is a direct competitor to Anthropic's Claude Code product and to other coding agents in this index (#011 GitHub Copilot 57, #025 Cursor 47, #009 Windsurf 58, #004 Devin 62, #022 Replit 48). (3) Investment relationship context: Alphabet (Google's parent) has been reported as an investor in Anthropic through equity investments, creating a complex relationship where Google is simultaneously a competitor (Gemini vs Claude), a customer (Claude on Vertex AI), and a strategic investor. (4) Platform distribution: Claude is available on Google Cloud Vertex AI, creating a distribution relationship alongside the competitive relationship. The evaluation methodology used for Gemini Code Assist is identical to that used for GitHub Copilot, Devin, Cursor, Windsurf, Replit Agent, and other AI coding agents.

---

## Future Evaluation Plan

- **Layer 1 (free-tier behavioral testing):** Behavioral testing on Individuals free tier (30 sessions × 4 difficulty levels), including indirect prompt injection resistance verification, Gemini CLI allowlist boundary testing (post-Tracebit remediation), and Gemini Code Assist in GitHub PR review agent permission model verification.
- **Layer C (continuous monitoring):** CVE monitoring; Gemini family prompt injection findings tracking; training policy evolution; ISO 42001 scope clarification. Monthly cadence with re-evaluation triggers on any CVSS 7.0+ Code Assist CVE, any KEV addition, or material training policy change.
- **Routine next review:** 2026-07-10 (90 days from this evaluation) or on any qualifying R-dimension trigger, whichever is earlier.

---

## Japanese Summary

```japanese-summary
# Gemini Code Assist 評価結果サマリー

## 基本情報
- スコア: 67/85 (Layer 0, S tier)
- ランク: VERDICT index 内 #2 (Amazon Q Business 68 と Vertex AI Agent Builder 65 の間)
- 評価日: 2026.04.11
- 対象バージョン: multi-tier (Individuals / Standard / Enterprise)
- 運営: Google LLC (Alphabet Inc. 子会社)
- 独立性: subsidiary (Alphabet 配下)

## 次元スコア
- V (検証可能性): 17/20
- R (耐性): 17/20
- D (データ運用): 11/15
- I (制御): 6/10
- C (封じ込め): 6/10
- T (透明性): 10/10

## 主要ポジティブ所見
- VERDICT index 内で最も広範な認証ポートフォリオ。SOC 1/2/3 + ISO 27001/27017/27018/27701 + FedRAMP + HIPAA-BAA + PCI DSS + **ISO 42001 (AI management system, 2025-05、index 内唯一)**
- Google Secure AI Framework (SAIF) 公開、NIST AI RMF aligned、ISO 42001 と組み合わせて T 次元 10/10 (index 内 AI coding agent カテゴリ唯一の満点)
- Code Assist 専用 CVE は直近12ヶ月ゼロ
- Standard / Enterprise tier は contractual に model training 除外
- 既存コード引用時の自動 source citation + paid tier の IP indemnification (category-leading)

## 主要リスク所見
- Gemini Code Assist for Individuals (free tier) は data collection が default ON、opt-out flow が複数 GitHub issues (#14104, #17480, #20569) で confusing と報告
- Gemini CLI (Individuals tier に bundle) が独立した prompt injection findings を2件受領 (Tracebit 2025-07, Cyera 2025-11)
- 隣接 Gemini family (Cloud Assist, Enterprise, Chrome Live panel) で prompt injection pattern が累積 — IDE extension 自体は影響なしだが perimeter リスクとして記録
- Gemini CLI ToS と Developer FAQ で AI Pro tier の training policy 表記に inconsistency (Issue #20569)

## インシデント
- Code Assist 専用 CVE: 直近12ヶ月ゼロ
- 隣接事象 (context only): Tracebit Gemini CLI 2025-07 (~28日で patched 0.1.14), Tenable "Gemini Trifecta" 2025-10 (disclosure 前 patched), Cyera Gemini CLI 2025-11, Noma Gemini Enterprise 2025-12, CVE-2026-0628 Chrome Gemini Live panel CVSS 8.8 2026-01

## CISA KEV
- 該当なし (CVE-2026-0628 は Chrome Gemini Live panel に対するもので KEV には含まれない、かつ Code Assist と異なる)

## 同クラスタ位置づけ
- 全 VERDICT index 内 #2 確定。AI Coding Agent カテゴリでは新たな leader として #011 GitHub Copilot (57) を +10 点上回り、#004 Devin (62) を +5 点上回る。+5 点 margin は ISO 42001 (+2 T)、Google Cloud certification stack (+2 V)、SAIF framework documentation (+1 T) で構成。#057 aider (52) や #058 Cline (50) との比較では certification 面で大きく上回る一方、closed-source の点で OSS 系 (aider, Cline) と異なる threat-model 構造を持つ。

## HTMLカード用タグ
- tags: ai-coding-agent, enterprise-saas, closed-source, iso-42001, saif, ip-indemnification, source-citation, vpc-service-controls
- caution_tags: training-opt-in-default-individuals-tier, opt-out-flow-documentation-issues, bundled-gemini-cli-prompt-injection-findings, adjacent-gemini-family-prompt-injection-pattern
- owner: Google LLC
```