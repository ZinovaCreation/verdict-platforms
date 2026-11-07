# VERDICT Evaluation #015 — Semantic Kernel — Update

| Field | Value |
|---|---|
| Evaluation number | #015 |
| Platform | Semantic Kernel |
| Evaluation type | Update (Differential Evaluation) |
| Update date | 2026-11-07 |
| Original Layer 0 date | 2026-03-26 |
| Evaluator | VERDICT evaluation engine; `evaluator_model: claude-fable-5-1` (operator's model selection for batch 1, Batch1-TrancheA-Authorize-2026-10-31-A1, written as supplied at invocation) |
| Target version | Python SDK `semantic-kernel` 1.47.0 (PyPI, 2026-11-05) / .NET `Microsoft.SemanticKernel` 1.82.0 (NuGet, 2026-11-07) / Java `semantickernel` 1.4.4-RC1 (published from the separate repository `microsoft/semantic-kernel-java`); repository `microsoft/semantic-kernel`, MIT |
| Framework | VERDICT v0.3.2 (`zinova-lab/verdict-engine` @ 899f556) |
| Previous evaluation | 2026-03-26 · 46/85 · Tier B · framework v0.3.1 (migrated capture) |
| CVE window | 2025-11-07 → 2026-11-07 (trailing 12 months from the update date) |
| Disclosure tags | `evaluator-coi`, `direct-investment` (Trigger 1) |

## Executive Summary

Semantic Kernel scores 41/85 (Tier C) at this update, down from the migrated capture's 46/85 (Tier B); the five-point movement comes from V (14→13: no third-party dependency disclosure for the SDK), R (11→10: the .NET release named as the fix for CVE-2026-25592 shipped ten days after the advisory), D (5→4: a default-on version header the vendor's own source calls telemetry, with an environment-variable opt-out) and T (8→6: no AI system identity disclosure and a security policy that routes to MSRC without product-level measures). Two CVEs are product-scoped to Semantic Kernel in the trailing 12 months, CVE-2026-25592 (arbitrary file write through `SessionsPythonPlugin` in the .NET SDK, published 2026-02-06) and CVE-2026-26030 (remote code execution through the `InMemoryVectorStore` filter in the Python SDK, published 2026-02-19); both carry the CNA vector `CVSS:3.1/AV:N/AC:L/PR:L/UI:N/S:C/C:H/I:H/A:H`, which computes to 9.9, so `max_cvss_12mo` is recorded as 9.9 and the base record's 10.0 is superseded. Neither CVE is in the CISA KEV catalog, and no supply chain compromise of the vendor's packages was located. Microsoft's October 2025 statement commits to supporting Semantic Kernel v1.x, including security fixes, for at least one year after Microsoft Agent Framework left preview (1.0 released 2026-04-03), and release activity continues on both PyPI and NuGet into November 2026; the record is not dormant.

## Scorecard

| Dimension | Score | Max | Rating |
|---|---|---|---|
| V — Verifiability | 13 | 20 | Mid |
| R — Resilience | 10 | 20 | Mid |
| D — Data Conduct | 4 | 15 | Low |
| I — Identity & Control | 4 | 10 | Mid |
| C — Containment | 4 | 10 | Mid |
| T — Transparency | 6 | 10 | Mid |
| E — Effectiveness | not evaluated (Layer 1+) | 15 | — |
| **Layer 0 total** | **41** | **85** | — |

Tier: C
Category: AI Orchestration SDK · Open Source (MIT)

CISA KEV: None — CVE-2026-25592 and CVE-2026-26030 are not in the catalog, and no catalog entry names Semantic Kernel (operator KEV JSON check 2026-11-07: catalogVersion 2026.11.06, 1769 entries). Previous score: 46/85.

## Dimension Detail

### V — Verifiability (13/20, Mid)

| Criterion | Result | Score | Evidence URL |
|---|---|---|---|
| Developer / company identity | Operator of record: Microsoft Corporation, One Microsoft Way, Redmond, Washington 98052, USA, named in the Microsoft Privacy Statement ("How to contact us"; Microsoft Ireland Operations Limited for EEA/UK/Swiss users) and in the Microsoft Terms of Use; the repository LICENSE carries the Microsoft Corporation copyright. Official contacts: MSRC report channel in SECURITY.md, `SK-Support@microsoft.com` in the PyPI package metadata, `opencode@microsoft.com` in the repository. Corporate registration confirmed by the vendor's legal pages; no registry was queried. | 4 | https://www.microsoft.com/en-US/privacy/privacystatement ; https://microsoft.com/en-us/legal/terms-of-use ; https://raw.githubusercontent.com/microsoft/semantic-kernel/main/SECURITY.md ; https://pypi.org/pypi/semantic-kernel/json |
| Source code disclosure | Full OSS. The Python, .NET and Java SDKs are published under the MIT License (OSI-approved); no hosted control plane or commercial layer is sold for the product (Criterion-VSource-001). | 4 | https://raw.githubusercontent.com/microsoft/semantic-kernel/main/LICENSE ; https://github.com/microsoft/semantic-kernel |
| Version management transparency | Release notes + changelog: each Python and .NET release is tagged on GitHub (`python-1.47.0`, `dotnet-1.82.0`) with generated release notes listing pull requests and a full-changelog diff link; PyPI and NuGet carry the dated version histories. | 3 | https://github.com/microsoft/semantic-kernel/releases/tag/python-1.39.4 ; https://pypi.org/pypi/semantic-kernel/json ; https://www.nuget.org/packages/Microsoft.SemanticKernel |
| Third-party dependency disclosure | None. No sub-processor list exists for the SDK (no service is operated for it); the Microsoft Online Services Subprocessors List covers online services, not this library. | 0 | source unconfirmed (none published for the SDK) |
| Independent certification | None. No SOC 2 or SOC 3 report is published for the SDK; Azure service attestations do not cover the library. | 0 | source unconfirmed (none published for the SDK) |
| Functional reproducibility docs | Complete API reference (Microsoft Learn .NET API browser and Python API reference) plus behavioral documentation (filters, function calling, observability, process framework). | 2 | https://learn.microsoft.com/en-us/dotnet/api/microsoft.semantickernel.autofunctioninvocationcontext?view=semantic-kernel-dotnet ; https://learn.microsoft.com/en-us/python/api/semantic-kernel/semantic_kernel.core_plugins?view=semantic-kernel-python ; https://learn.microsoft.com/semantic-kernel/concepts/enterprise-readiness/filters |

**Positive findings.** The legal entity is named on Microsoft's own legal pages; the whole product is MIT-licensed with no closed layer; every release is tagged with generated notes and a changelog link.

**Recorded concerns.** No dependency or sub-processor disclosure and no independent attestation exist for the SDK; readers inherit those obligations at deployment.

### R — Resilience (10/20, Mid)

| Criterion | Result | Score | Evidence URL |
|---|---|---|---|
| CVE count (trailing 12 months) | 2 (basis exact): CVE-2026-25592 (published 2026-02-06) and CVE-2026-26030 (published 2026-02-19). 1–2 → 3; penalty −1 because both compute to 9.9 (CVSS 9.0+) → 2. | 2 | https://github.com/microsoft/semantic-kernel/security/advisories ; https://raw.githubusercontent.com/CVEProject/cvelistV5/main/cves/2026/25xxx/CVE-2026-25592.json ; https://raw.githubusercontent.com/CVEProject/cvelistV5/main/cves/2026/26xxx/CVE-2026-26030.json |
| Maximum CVSS severity | 9.9 (CNA v3.1, GitHub_M). Score source per Attribution-CVE-002: no NIST Primary score exists (NVD carries only the CNA's Secondary metric); the CNA container states a baseScore of 10 for the vector `CVSS:3.1/AV:N/AC:L/PR:L/UI:N/S:C/C:H/I:H/A:H`, which computes to 9.9; the computed score is recorded and the stated value noted. Both CVEs carry the same vector. 9.0+ → 0. | 0 | https://cve.circl.lu/vuln/cve-2026-26030 ; https://cvefeed.io/vuln/detail/CVE-2026-25592 ; https://github.com/microsoft/semantic-kernel/security/advisories/GHSA-2ww3-72rp-wpp4 |
| Patch response speed | 8–14 days. CVE-2026-25592: advisory 2026-02-06; the NuGet release it names as the fix, `Microsoft.SemanticKernel.Core` / `Plugins.Core` 1.71.0, was published 2026-02-16 (10 days); the pip fix 1.39.3 (2026-02-02) preceded the advisory. CVE-2026-26030: fix `python-1.39.4` released 2026-02-10, advisory 2026-02-19 (fix preceded disclosure). The longest interval governs. | 2 | https://www.nuget.org/packages/Microsoft.SemanticKernel.Core ; https://pypi.org/pypi/semantic-kernel/json ; https://github.com/microsoft/semantic-kernel/security/advisories/GHSA-xjw9-4gw8-4rqx |
| Structural issues | Isolated independent bugs: CWE-22 path traversal in the .NET `SessionsPythonPlugin` host-side file transfer and CWE-94 code injection in the Python `InMemoryVectorStore` filter parser are different weakness classes in different SDKs and components. Both involve model-influenced input reaching a privileged operation, a theme the vendor's own research post states; it is recorded in the Contextual Analysis and not scored as a recurring root cause. | 3 | https://microsoft.com/en-us/security/blog/2026/05/07/prompts-become-shells-rce-vulnerabilities-ai-agent-frameworks/ |
| Supply chain compromise (trailing 12 months) | None. No public confirmation of an unauthorized write to the `semantic-kernel` PyPI package, the `Microsoft.SemanticKernel.*` NuGet packages, the Maven artifacts, the `microsoft` GitHub organization or its build pipeline was located. OSV MAL-2026-4760 concerns `nvidia-nat-semantic-kernel`, a different PyPI package (withdrawn 2026-06-13), not the vendor's. `supply_chain_compromise_12mo: false`. | 3 | https://osv.dev/vulnerability/MAL-2026-4760 ; https://osv.dev/vulnerability/CVE-2026-25592 |

**Positive findings.** Both CVEs were issued through Microsoft's own GitHub CNA with advisories, CWE identifiers, workarounds and fix versions; the Python fixes preceded both advisories; the vendor published a research post with hunting queries and a CTF reproduction.

**Recorded concerns.** Two critical-severity (computed 9.9) vulnerabilities in the plugin and vector-store layers within 13 days; the .NET fix release followed its advisory by ten days; a third-party researcher claims the CVE-2026-25592 remediation can be bypassed (Incident Timeline), with no vendor advisory on the claim located.

### D — Data Conduct (4/15, Low)

| Criterion | Result | Score | Evidence URL |
|---|---|---|---|
| GDPR compliance disclosure | Mention only. The Microsoft Privacy Statement names Microsoft Ireland Operations Limited as controller for EEA/UK/Swiss users, lists data-subject rights and cites the EU–U.S. Data Privacy Framework and standard contractual clauses; no DPA or product-level statement covers the open-source SDK. | 1 | https://www.microsoft.com/en-US/privacy/privacystatement |
| Data minimization | Default ON, easy opt-out. The Python SDK adds a `semantic-kernel-python/{version}` User-Agent and a `semantic-kernel-version` header to requests sent to the AI, search and vector services the developer configures; the source names this "telemetry", enables it unless `AZURE_TELEMETRY_DISABLED` is set to true, and the .NET SDK sends a `Semantic-Kernel-Version` header the same way. No Microsoft-operated telemetry endpoint exists in the package (wheel inspection 2026-11-07, 1.47.0: no analytics host; OpenTelemetry diagnostics default off, exporters developer-configured). | 1 | https://pypi.org/pypi/semantic-kernel/json ; https://raw.githubusercontent.com/microsoft/semantic-kernel/main/dotnet/src/InternalUtilities/src/Http/HttpHeaderConstant.cs ; https://raw.githubusercontent.com/microsoft/semantic-kernel/main/dotnet/docs/TELEMETRY.md ; https://learn.microsoft.com/en-us/semantic-kernel/concepts/enterprise-readiness/observability |
| AI training use | No mention for the SDK. The Microsoft Privacy Statement's general statement that Microsoft may use data to develop and train its AI models is not scoped to this library, and no SDK-level statement exists. | 0 | https://www.microsoft.com/en-US/privacy/privacystatement |
| Sub-processor transparency | None for the SDK. | 0 | source unconfirmed (none published for the SDK) |
| Data retention disclosure | None for the SDK; the Privacy Statement's retention text is generic ("as long as necessary"). | 0 | https://www.microsoft.com/en-US/privacy/privacystatement |

**Positive findings.** The package contains no vendor telemetry endpoint; OpenTelemetry diagnostics, including sensitive-content capture, are opt-in through environment variables; the .NET telemetry document states that trace-level logging may contain sensitive data and should not be enabled in production.

**Recorded concerns.** The version header is on by default and opt-out is documented only in source; the data-governance artifacts (DPA, training-use statement, retention terms) exist at the Microsoft corporate level and not for the SDK.

### I — Identity & Control (4/10, Mid)

| Criterion | Result | Score | Evidence URL |
|---|---|---|---|
| Emergency stop documentation | Documented but incomplete. The Auto Function Invocation Filter can end the function-calling loop (`context.Terminate = true` / `context.terminate = True`) and a filter that does not call `next` prevents execution; filters must be registered by the developer and the documentation does not describe an immediate stop for a running plugin. | 2 | https://learn.microsoft.com/semantic-kernel/concepts/enterprise-readiness/filters |
| Human-in-the-loop design | Optional. HITL is a pattern the developer builds: approval checks in filters, and the Process Framework's pause-on-missing-parameter with external events; not enabled by default. | 1 | https://learn.microsoft.com/semantic-kernel/concepts/enterprise-readiness/filters ; https://learn.microsoft.com/en-us/semantic-kernel/frameworks/process/examples/example-human-in-loop |
| Permission delegation transparency | Partial. The Responsible AI FAQ states that developers control what information plugins can access; the dynamic-sessions tutorial documents the Azure roles delegated to the code-interpreter plugin (Session Executor, Contributor). No general model of agent permission scope is documented. | 1 | https://raw.githubusercontent.com/microsoft/semantic-kernel/main/TRANSPARENCY_FAQS.md ; https://learn.microsoft.com/en-my/azUre/container-apps/sessions-tutorial-semantic-kernel |

**Positive findings.** A documented termination point in the auto-invocation loop; filter-based approval and PII-redaction samples; the filters page states the ordering guarantees when filters are added directly to the Kernel.

**Recorded concerns.** Controls are opt-in and developer-assembled; no default HITL; no delegation model beyond the one plugin tutorial.

### C — Containment (4/10, Mid)

| Criterion | Result | Score | Evidence URL |
|---|---|---|---|
| Sandbox design | Unknown / none built in. Plugins and functions execute in the host process; the SDK provides no sandbox. The optional `SessionsPythonPlugin` / `SessionsPythonTool` sends model-generated code to Azure Container Apps dynamic sessions, an Azure service that states Hyper-V isolation; that boundary belongs to the service, not the SDK, and the plugin's host-side file transfer was the subject of CVE-2026-25592. | 0 | https://learn.microsoft.com/azure/container-apps/sessions-code-interpreter ; https://learn.microsoft.com/en-my/azUre/container-apps/sessions-tutorial-semantic-kernel |
| Least privilege | Configurable. Filters and allow-listing are documented as developer measures; the dynamic-sessions tutorial grants the managed identity the Contributor role on the session pool in addition to Session Executor. | 1 | https://learn.microsoft.com/en-my/azUre/container-apps/sessions-tutorial-semantic-kernel ; https://learn.microsoft.com/semantic-kernel/concepts/enterprise-readiness/filters |
| Tenant isolation (cloud) | Self-hosted only: the SDK runs in the deployer's process; N/A. | 3 | https://github.com/microsoft/semantic-kernel |

**Positive findings.** Code execution through the dynamic-sessions plugin is opt-in and runs outside the host process; the tutorial documents per-user session separation.

**Recorded concerns.** No built-in sandbox; the tutorial's role grant is broader than the plugin's stated need; sharing one kernel across users shares a session.

### T — Transparency (6/10, Mid)

| Criterion | Result | Score | Evidence URL |
|---|---|---|---|
| CVE publication posture | Issues CVEs + advisories: two GitHub Security Advisories with CNA-assigned CVE IDs (GitHub_M), CWE, vectors and fix versions. | 2 | https://github.com/microsoft/semantic-kernel/security/advisories |
| Incident disclosure speed | ≤30 days. Advisories were published within days of the fix releases (CVE-2026-25592: 4 days after pip 1.39.3; CVE-2026-26030: 9 days after python-1.39.4); the vendor's research post followed on 2026-05-07. | 2 | https://github.com/microsoft/semantic-kernel/security/advisories ; https://microsoft.com/en-us/security/blog/2026/05/07/prompts-become-shells-rce-vulnerabilities-ai-agent-frameworks/ |
| Security policy publication | General mention. SECURITY.md is Microsoft's standard block: MSRC reporting, 24-hour acknowledgement target, Coordinated Vulnerability Disclosure, bug bounty link; no product-level technical or organizational measures. | 1 | https://raw.githubusercontent.com/microsoft/semantic-kernel/main/SECURITY.md |
| AI safety framework reference | Internal framework documented. The repository's Responsible AI FAQ (TRANSPARENCY_FAQS.md) describes intended uses, limitations and operational factors and points to Prompt Shields and Azure AI Content Safety; no external framework (NIST AI RMF, ISO/IEC 42001) is referenced for the SDK. | 1 | https://raw.githubusercontent.com/microsoft/semantic-kernel/main/TRANSPARENCY_FAQS.md |
| AI system identity disclosure | None. The SDK documents no mechanism that discloses to end users that they are interacting with an AI system; the FAQ advises developers to add output for user awareness. | 0 | https://raw.githubusercontent.com/microsoft/semantic-kernel/main/TRANSPARENCY_FAQS.md |

**Positive findings.** CVEs issued through the vendor's own CNA with public advisories; a vendor research post with detection queries; a Responsible AI FAQ in the repository.

**Recorded concerns.** No external AI governance framework referenced for the product; no end-user AI disclosure mechanism; the security policy is a routing document.

## Incident Timeline

| Date | CVE ID | CVSS | Description | Patch status | KEV |
|---|---|---|---|---|---|
| 2026-02-06 (GHSA-2ww3-72rp-wpp4; pip fix 1.39.3 released 2026-02-02; NuGet fix 1.71.0 released 2026-02-16) | CVE-2026-25592 | 9.9 computed (CNA v3.1 stated 10; NVD: CNA Secondary 9.9, no NIST Primary) | Arbitrary file write via AI agent function calling in the .NET SDK: `SessionsPythonPlugin` `DownloadFileAsync` / `UploadFileAsync` accept an unvalidated `localFilePath` (CWE-22). Workaround: a function invocation filter allow-listing the path. | Fixed: `Microsoft.SemanticKernel.Core` / `Plugins.Core` 1.71.0; `semantic-kernel` (pip) 1.39.3 | No |
| 2026-02-19 (GHSA-xjw9-4gw8-4rqx; fix python-1.39.4 released 2026-02-10) | CVE-2026-26030 | 9.9 computed (CNA v3.1 stated 10; NVD: CNA Secondary 9.9, no NIST Primary) | Remote code execution through the `InMemoryVectorStore` filter functionality in the Python SDK: the filter expression is evaluated as a lambda (CWE-94). Workaround: avoid `InMemoryVectorStore` in production. | Fixed: `semantic-kernel` (pip) 1.39.4 (PR #13505, "refinement of filtering") | No |

Non-CVE items (recorded, not counted):
- 2026-04-25 — A third-party white paper (JDP-Security, "Project Nuka-AI", NUKA-AI-2026-001; mirrored by PT Security's dbugs on 2026-05-06) claims six bypasses of the CVE-2026-25592 remediation in the .NET SDK and asks Microsoft to assign a new CVE. The author states a report to MSRC on 2026-03-24 and a case closure on 2026-04-08. No CVE, GHSA or vendor advisory on the claim was located. The affected versions the author gives (".NET v1.47.0–1.48.0") do not match the `Microsoft.SemanticKernel` NuGet version numbers of that period (1.76.0 on 2026-05-11). Recorded as the author's position; VERDICT does not adjudicate it. Source: https://nuka-ai.github.io/posts/2026-07-28-Semantic-Kernel-disclosure/ ; https://dbugs.ptsecurity.com/news/bypassing-the-cve-2026-25592-patch-in-microsoft-semantic-kernel-20260506
- 2026-05-07 — Microsoft Security Blog, "When prompts become shells: RCE vulnerabilities in AI agent frameworks" (Microsoft Defender Security Research Team): states that both CVEs were found by Microsoft's own researchers and disclosed to MSRC, publishes KQL hunting queries, and mentions a related arbitrary file read in `upload_file()` across the Python and .NET SDKs without a CVE ID. Source: https://microsoft.com/en-us/security/blog/2026/05/07/prompts-become-shells-rce-vulnerabilities-ai-agent-frameworks/
- Out of scope — OSV MAL-2026-4760, malicious code in the PyPI package `nvidia-nat-semantic-kernel` (published 2026-05-21, withdrawn 2026-06-13): a different package, not the vendor's `semantic-kernel`; not a Semantic Kernel supply chain event. Source: https://osv.dev/vulnerability/MAL-2026-4760

## Contextual Analysis

Microsoft's documented position is that Semantic Kernel is a model-agnostic SDK whose controls — filters, approval flows, content-safety integration — are assembled by the developer, and that Microsoft Agent Framework is its successor. The October 2025 announcement states that Semantic Kernel v1.x will continue to be supported, with critical bugs and security issues addressed, for at least one year after Agent Framework leaves preview; Agent Framework 1.0 was released on 2026-04-03, and the repository banner directs new work to it. The release record is consistent with that statement: Python 1.40.0 through 1.47.0 and .NET 1.76.0 through 1.82.0 shipped between March and November 2026. Maintenance mode is not dormancy; the Layer C test finds release activity within the last month.

The two February 2026 CVEs were found by Microsoft's own security research team, fixed, and then published through the GitHub CNA; the vendor's May research post frames both as a single lesson — that tool parameters a model can influence are attacker-controlled input — and notes a related file-read issue in `upload_file()` for which no CVE was assigned. VERDICT scores the two CVEs as isolated under the R structural-issues criterion because they differ in weakness class, language and component, and records the vendor's own framing here. The researcher who claims the CVE-2026-25592 remediation can be bypassed states that MSRC closed the case; Microsoft has published no statement on that claim that this session could locate. The record carries the author's position and version numbers as stated, with the observation that those numbers do not correspond to the NuGet release stream of the period.

CVSS score source: the CNA container states a base score of 10 for a vector that computes to 9.9; GitHub, OSV and NVD's Secondary entry display 9.9. Under Attribution-CVE-002 the computed score is recorded. The base record's `max_cvss_12mo: 10.0` matches the CNA's stated value as shown on the CVE List; the base record cites no source, so its origin is not stated in the record. The operator's sweep row (observed 9.9) is consistent with this resolution.

Operator of record: the public record corrects the base record's display string "Microsoft Research · Migrating to Agent Framework". The legal entity named on Microsoft's Privacy Statement and Terms of Use is Microsoft Corporation; the project is published under the `microsoft` GitHub organization and its packages name Microsoft as author. `independence` is recorded as `parent` because the operator is itself the ultimate parent.

Data conduct for a library is thin by construction: nothing is sent to a Microsoft telemetry service, but the SDK does identify itself by version to every AI, search and vector endpoint the developer configures unless an environment variable disables it, and the corporate Privacy Statement's training and retention language is not scoped to the SDK. Readers deploying the SDK carry the GDPR, retention and sub-processor obligations themselves.

Evidence rule for this report: every factual claim was confirmed by web retrieval during the session. Pages the session tools could not render are listed in the Differential section with the sources used in their place.

## VERDICT Record

**Summary.** Semantic Kernel records 41/85 (Tier C) at the 2026-11-07 update, with two critical-severity CVEs (computed CVSS 9.9) in the plugin and vector-store layers, no built-in sandbox, a public MIT codebase under a stated maintenance commitment, and release activity continuing alongside its successor.

**Risk Factor Summary by Use Case**

| Use case | Observation |
|---|---|
| Internal testing | MIT SDK runs in-process; OpenTelemetry diagnostics are opt-in; the CTF reproduction published by the vendor is marked not for production. |
| Credential-handling | Plugins execute with the host process's privileges; CVE-2026-25592 wrote to host paths through a model-callable function; the dynamic-sessions tutorial grants Contributor on the session pool. |
| Cloud multi-tenant | N/A — the SDK is self-hosted; the only multi-tenant component documented is the Azure dynamic-sessions service, whose isolation is the service's statement, and the tutorial warns that a shared kernel shares a session. |
| Regulated-data workloads | No DPA, sub-processor list, retention terms or attestation exist for the SDK; the version header is on by default; the Privacy Statement's general training language is not scoped to the library. |

**Reference Information** (options, not instructions)
1. `AZURE_TELEMETRY_DISABLED=true` removes the version header the SDK adds to outbound requests; `SEMANTICKERNEL_EXPERIMENTAL_GENAI_ENABLE_OTEL_DIAGNOSTICS*` control diagnostics capture.
2. A function invocation filter that allow-lists `localFilePath` is the vendor's documented mitigation for the `SessionsPythonPlugin` class of issue; `InMemoryVectorStore` is documented as not for production.
3. Microsoft's migration guide and the Agent Framework 1.0 release are the documented path for new agent work; the support statement for v1.x runs at least to 2027-04-03.

**Bias Disclosure**

"This evaluation uses Claude (Anthropic) as its tooling. Anthropic operates in the AI agent market and may compete with some evaluated vendors. VERDICT discloses this relationship in every report and applies identical evaluation criteria to all platforms regardless of their relationship to Anthropic."

VERDICT additionally discloses a parent-identity relationship (Trigger 1). The operator of the evaluated platform, Microsoft Corporation, is a material Anthropic equity-holder as recorded in KNOWN_FACTS.md: Microsoft committed to invest up to USD 5 billion in Anthropic as part of the strategic partnership announced on 2025-11-18 (https://blogs.microsoft.com/blog/2025/11/18/microsoft-nvidia-and-anthropic-announce-strategic-partnerships/ ; https://www.anthropic.com/news/microsoft-nvidia-anthropic-announce-strategic-partnerships). Anthropic's Series G announcement of 2026-02-12 states that the round includes a portion of the previously announced investments from Microsoft and NVIDIA; the amount closed is not public, and no statement is made here that the commitment has closed in full (https://www.anthropic.com/news/anthropic-raises-30-billion-series-g-funding-380-billion-post-money-valuation). The relationship is recorded with the tags `evaluator-coi` and `direct-investment`. Identical evaluation criteria were applied regardless of this relationship.

Product-level integration (separate from the corporate relationship above): the Python SDK ships an Anthropic chat-completion connector (`semantic_kernel.connectors.ai.anthropic`) alongside connectors for OpenAI, Azure OpenAI, Google, Mistral, NVIDIA, Hugging Face, Ollama and Amazon Bedrock. This is a model-provider relationship of the kind VERDICT evaluates across platforms and is not itself a disclosure trigger.

Triggers 0, 2 and 3 were assessed and do not fire: the operator is not Anthropic; no material Anthropic equity-holder is recorded as a material investor in Microsoft Corporation, which has no controlling owner; and no non-arms-length channel beyond the operator relationship disclosed under Trigger 1 was located.

## Future Evaluation Plan

- Layer 1 (behavioral testing): not scheduled; the SDK is free to run, but Layer 1 timing is deferred to Operations.
- Layer C: routine lane 365 days from `updated_at` (pipeline-derived `next_review_due`); interrupt lane active for T1–T6. Items to watch: any advisory on the claimed CVE-2026-25592 remediation bypass or the `upload_file()` file-read issue; the end of the stated v1.x support window (one year after 2026-04-03); any change to the version-header default.

## Differential

| Item | Value |
|---|---|
| Lane | Routine (batch-1 scheduled; interval not elapsed). One T1 repo-ghsa sweep row for `semantic-kernel` (2026-10-27) was supplied as operator input; it describes the two already-recorded advisories and fires no new interrupt. |
| Previous evaluation | 2026-03-26 · 46/85 · Tier B · v0.3.1 (migrated capture; `sources: []`; `qa` unresolved ×3; `evaluator_model: unrecorded`) |
| This evaluation | 2026-11-07 · 41/85 · Tier C · v0.3.2 · `evaluator_model: claude-fable-5-1` |
| Score movement | −5 (V 14→13, R 11→10, D 5→4, I 4→4, C 4→4, T 8→6). At the 5-point threshold; the Executive Summary names the moved dimensions and evidence. Tier B→C applied as computed. |

Per-dimension state: V re-evaluated — migrated capture, no sources; R re-evaluated — migrated capture, no sources; D re-evaluated — migrated capture, no sources; I re-evaluated — migrated capture, no sources; C re-evaluated — migrated capture, no sources; T re-evaluated — migrated capture, no sources; E null (Layer 0). No carry-forward check could be performed because the base record cites no sources (convention 2026-09-22).

Prior-record omissions stated as facts: the base record carried `max_cvss_12mo: 10.0`; the CNA vector for both CVEs computes to 9.9 (Attribution-CVE-002). It stated that both CVEs were patched concurrently with disclosure; the .NET release named as the fix for CVE-2026-25592 was published ten days after the advisory. Its operator string named "Microsoft Research", a display string rather than the legal entity; `independence: unrecorded`, `evaluator_model: unrecorded` and the three `unresolved` QA fields are resolved at this update. Its key finding named the researchers' identity and described Agent Framework as "RC March 2026"; researcher identity is not a scored fact, and Agent Framework 1.0 was released 2026-04-03.

Dormancy test: not dormant — `semantic-kernel` 1.47.0 on PyPI (2026-11-05), `Microsoft.SemanticKernel` 1.82.0 on NuGet (2026-11-07), GitHub release tags through October 2026; `dormant_since` is omitted.

Operator input recorded (OperatorInput-001), all retrieved 2026-11-07 JST:
1. Quarterly sweep 2026-10-27 public-layer row: `T1 | repo-ghsa | https://github.com/microsoft/semantic-kernel/security/advisories | 2 published advisories in trailing 12 months; max CVSS 9.9 | 2026-10-27 | cve_count_12mo=2 max_cvss_12mo=10.0`. Resolution: NIST Primary absent → CNA v3.1 vector computes 9.9 (stated 10 noted); `max_cvss_12mo` recorded as 9.9; the recorded 10.0 matches the CNA's stated base score, source not cited in the base record.
2. CISA KEV JSON feed (https://www.cisa.gov/sites/default/files/feeds/known_exploited_vulnerabilities.json): catalogVersion 2026.11.06, dateReleased 2026-11-06T19:44:45.1797Z, count 1769; CVE-2026-25592 and CVE-2026-26030 not present; no entry naming "Semantic Kernel"; 42 Microsoft-vendor entries added in the window, none naming Semantic Kernel. `cisa_kev.present: false`.
3. Rendered text of unread pages: none supplied.

Pages the session tools could not render (stated as unread, not scored as silence):
- https://nvd.nist.gov/vuln/detail/CVE-2026-25592 and CVE-2026-26030 (empty render); the CISA KEV JSON feed, services.nvd.nist.gov, api.nuget.org and search.maven.org (not reachable from the session). Content used: the cvelistV5 CNA records, the GitHub advisory pages, OSV records, cve.circl.lu (which mirrors the NVD entry: CNA Secondary 9.9, status Analyzed, CPE `microsoft:semantic_kernel` python), cvefeed.io, the nuget.org package pages, and the operator's KEV JSON check.
- https://github.com/microsoft/semantic-kernel/releases (listing) and the pull-request page for PR #13478; content used: individual release pages, the `releasealert.dev` mirror of the release listing, the GHSA text and the Microsoft Security Blog post.
- The MSRC Security Update Guide was not consulted for these IDs: both are GitHub_M CNA records and no MSRC entry was located by search.
The operator may supply rendered text for any of these per OperatorInput-001; the scores above do not depend on content behind those pages beyond what is recorded.

Sources consulted with "none located" results: MIT AI Agent Index entry for Semantic Kernel (none located by search); a vendor advisory or statement on the claimed CVE-2026-25592 remediation bypass (none located); a Semantic Kernel-specific privacy, DPA or sub-processor document (none located).

KNOWN_FACTS candidate (staged, not applied): "Semantic Kernel — CVE-2026-25592 and CVE-2026-26030 carry the CNA vector `CVSS:3.1/AV:N/AC:L/PR:L/UI:N/S:C/C:H/I:H/A:H`, which computes to 9.9; the CNA's stated base score of 10 is not recorded as the maximum. The .NET fix for CVE-2026-25592 (1.71.0) was published 2026-02-16, ten days after the advisory; 'patched concurrently with disclosure' applies to the Python fixes only. Operator of record is Microsoft Corporation, not 'Microsoft Research'." Intake per the KNOWN_FACTS rule is an Operations decision.

## Evaluation History

| Date | Type | Score | Tier | Framework |
|---|---|---|---|---|
| 2026-03-26 | Initial (migrated capture) | 46/85 | B | v0.3.1 |
| 2026-11-07 | Update | 41/85 | C | v0.3.2 |
