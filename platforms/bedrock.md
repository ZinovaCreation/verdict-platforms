---
name: AWS Bedrock Agents
slug: bedrock
operator: Amazon Web Services, Inc.
independence: subsidiary
parent_entity: Amazon.com, Inc.
category: Managed Agent Platform · Enterprise SaaS
homepage: https://aws.amazon.com/bedrock/agentcore/
github: https://github.com/aws
evaluation_number: 17
evaluation_type: update
evaluated_at: '2026-03-25'
updated_at: '2026-11-06'
evaluator_model: claude-fable-5-1
framework_version: v0.3.2
layer: '0'
target_version: 'Hosted Amazon Bedrock Agents (classic; maintenance mode since 2026-07-30) and Amazon Bedrock AgentCore (Runtime, Code Interpreter, Policy, Gateway, harness) as examined 2026-11-06; AWS-maintained client tooling bedrock-agentcore v1.21.0, bedrock-agentcore-starter-toolkit 0.3.14, @aws/agentcore 0.14.2'
previous_evaluation_date: '2026-03-25'
previous_score: 55
score: 49
max_score: 85
tier: B
verdict:
  v:
    score: 12
    rating: Mid
    note: 'Legal entity on AWS Customer Agreement; closed-source service; SOC 2 gated'
  e:
    score: null
    rating: null
    note: null
  r:
    score: 6
    rating: Low
    note: '8 CVEs (CNA AMZN), max 9.0 v3.1; CVE-2026-16796 bypasses CVE-2026-12530 fix'
  d:
    score: 13
    rating: High
    note: 'No training use (FAQ, Service Terms); retention stated; abuse detection on'
  i:
    score: 6
    rating: Mid
    note: 'Session stop documented, no platform-wide stop; user confirmation optional'
  c:
    score: 4
    rating: Mid
    note: 'Hybrid sandbox; broad default roles recorded by researchers; isolation claimed'
  t:
    score: 8
    rating: High
    note: 'CNA, same-day bulletins, ISO/IEC 42001; no end-user AI identity disclosure'
cisa_kev:
  present: false
  entries: []
cve_count_12mo: 8
cve_count_basis: exact
max_cvss_12mo: 9.0
supply_chain_compromise_12mo: false
known_facts_applied:
- Amazon — strategic equity position in Anthropic
qa:
  factual: pass
  legal: pass
  quality: pass
  revision_cycles: 0
  flagged: false
differential:
  v: re-evaluated
  e: null
  r: re-evaluated
  d: re-evaluated
  i: re-evaluated
  c: re-evaluated
  t: re-evaluated
next_review_due: '2027-11-06'
tags:
- evaluator-coi
- direct-investment
rank: 30
sources:
- https://aws.amazon.com/agreement/
- https://aws.amazon.com/privacy/
- https://aws.amazon.com/service-terms/
- https://aws.amazon.com/compliance/sub-processors/
- https://aws.amazon.com/compliance/gdpr-center/
- https://aws.amazon.com/compliance/soc-faqs/
- https://aws.amazon.com/compliance/services-in-scope/SOC/
- https://aws.amazon.com/compliance/services-in-scope/FedRAMP/
- https://aws.amazon.com/compliance/iso-certified
- https://aws.amazon.com/compliance/hipaa-eligible-services-reference
- https://aws.amazon.com/compliance/shared-responsibility-model/
- https://aws.amazon.com/security/vulnerability-reporting/
- https://aws.amazon.com/security/security-bulletins/
- https://aws.amazon.com/security/security-bulletins/2026-008-aws/
- https://aws.amazon.com/security/security-bulletins/2026-040-aws/
- https://aws.amazon.com/security/security-bulletins/2026-044-aws/
- https://aws.amazon.com/cn/security/security-bulletins/2026-058-aws/
- https://aws.amazon.com/security/security-bulletins/2026-065-aws/
- https://aws.amazon.com/security/security-bulletins/2026-073-aws/
- https://aws.amazon.com/security/security-bulletins/2026-127-aws/
- https://nvd.nist.gov/vuln/detail/CVE-2026-4269
- https://nvd.nist.gov/vuln/detail/CVE-2026-11393
- https://app.opencve.io/cve/CVE-2026-105812
- https://github.com/aws/bedrock-agentcore-starter-toolkit/security/advisories/GHSA-xfhr-q72q-jcrj
- https://github.com/aws/agentcore-cli/security/advisories/GHSA-m4x6-gwgp-4pm7
- https://github.com/aws/bedrock-agentcore-sdk-python/security/advisories/GHSA-6rfw-mq36-jm8h
- https://github.com/aws/bedrock-agentcore-sdk-python/security/advisories/GHSA-j6g5-3hh3-pgw8
- https://github.com/aws/bedrock-agentcore-sdk-python/releases/tag/v1.21.0
- https://pypi.org/project/bedrock-agentcore/1.18.1/
- https://www.npmjs.com/package/@aws/agentcore/v/0.14.2
- https://aws.amazon.com/bedrock/faqs/
- https://docs.aws.amazon.com/bedrock/latest/userguide/data-protection.html
- https://docs.aws.amazon.com/bedrock/latest/userguide/data-retention.html
- https://docs.aws.amazon.com/bedrock/latest/userguide/abuse-detection.html
- https://docs.aws.amazon.com/bedrock/latest/userguide/model-invocation-logging.html
- https://docs.aws.amazon.com/bedrock/latest/userguide/agents-userconfirmation.html
- https://docs.aws.amazon.com/bedrock/latest/userguide/agents-classic-maintenance-mode.html
- https://docs.aws.amazon.com/bedrock/latest/userguide/security.html
- https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/data-protection.html
- https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/memory.html
- https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/runtime-sessions.html
- https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/runtime-security-best-practices.html
- https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/code-interpreter-resource-management.html
- https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/policy-core-concepts.html
- https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/security-credentials-management.html
- https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/identity-data-protection.html
- https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/compliance-validation.md
- https://aws.amazon.com/about-aws/whats-new/2025/10/amazon-bedrock-agentcore-available/
- https://aws.amazon.com/blogs/security/aws-successfully-completed-its-first-surveillance-audit-for-iso-420012023-with-no-findings
- https://aws.amazon.com/machine-learning/responsible-ai/policy
- https://www.beyondtrust.com/blog/entry/pwning-aws-agentcore-code-interpreter
- https://unit42.paloaltonetworks.com/bypass-of-aws-sandbox-network-isolation-mode/
- https://sonraisecurity.com/blog/sandboxed-to-compromised-new-research-exposes-credential-exfiltration-paths-in-aws-code-interpreters/
- https://thenextweb.com/news/aws-agentcore-zenity-agentcorruption-one-prompt-agents
- https://aiagentindex.mit.edu/2025
- https://press.aboutamazon.com/aws
- https://www.aboutamazon.com/news/company-news/amazon-anthropic-ai-investment
- https://www.aboutamazon.com/news/company-news/amazon-invests-additional-5-billion-anthropic-ai
- https://www.anthropic.com/news/series-h
- https://www.cisa.gov/sites/default/files/feeds/known_exploited_vulnerabilities.json
og_description: "Independent security evaluation of AWS Bedrock Agents / AgentCore. Score: 49/85 (previously 55/85). 8 CVEs in 12 months, max CVSS 9.0; same-day AWS bulletins; ISO/IEC 42001. Framework v0.3.2."
category_line: Managed Agent Platform · Enterprise SaaS
display_tags: &id001
- text: 8 CVEs · Max CVSS 9.0 (CNA v3.1) · Fix Bypass Recorded
  color: red
- text: Code Interpreter DNS Tunneling · Remediated 2026-04-15
  color: amber
- text: SOC (Artifact) · FedRAMP · ISO 42001 · HIPAA Eligible
  color: safe
- text: Cedar Policy · Default-Deny Enforcement at Gateway
  color: safe
- text: Supply Chain · No Confirmed Write (Criterion-001a)
  color: dim
finding: "Eight CVEs with the Amazon CNA in the trailing 12 months, two scored 9.0 (CNA v3.1): code injection in the @aws/agentcore CLI (CVE-2026-11393) and the starter toolkit (CVE-2026-105812); CVE-2026-16796 recorded as a bypass of the CVE-2026-12530 fix; one service-side CVE (CVE-2026-18830, 8.1) fixed by AWS with no customer action. Every bulletin published with its fix on the same date. Code Interpreter Sandbox DNS tunneling (reported 2025-09-01) remediated by AWS 2026-04-15. Training-use exclusion with stated retention periods; ISO/IEC 42001; SOC 2 reports via AWS Artifact. supply_chain_compromise_12mo re-evaluated to false: CVE-2026-4269 is a vulnerability only; no publicly confirmed write (SupplyChain-Criterion-001a)."
meta_description: "Independent security evaluation of AWS Bedrock Agents / AgentCore. Score: 49/85 (previously 55/85). 8 CVEs in 12 months, max CVSS 9.0; same-day AWS bulletins; ISO/IEC 42001. Framework v0.3.2."
key_finding: 'Eight CVEs with the Amazon CNA in the trailing 12 months (2025-11-06 → 2026-11-06), two scored 9.0 on the CNA v3.1 vector: code injection in the @aws/agentcore CLI (CVE-2026-11393) and in the bedrock-agentcore-starter-toolkit (CVE-2026-105812). CVE-2026-16796 is recorded by AWS as a bypass of the CVE-2026-12530 fix. CVE-2026-18830 (InvokeHarness, 8.1) was fixed service-side on 2026-07-31 with no customer action. Each AWS bulletin was published with the fixed version on the same date. The Code Interpreter Sandbox DNS-tunneling path reported on 2025-09-01 was remediated by AWS on 2026-04-15 per the reporting researcher''s dated update; AWS documentation now describes Sandbox mode as limited external network access to AWS services. Bedrock FAQ and Service Terms state that inputs and outputs are not used to train Amazon or third-party models, with abuse-detection retention up to 30 days. AgentCore Cedar Policy provides default-deny enforcement at the Gateway outside the model loop. supply_chain_compromise_12mo re-evaluated from true to false: CVE-2026-4269 is a vulnerability only; no publicly confirmed write (SupplyChain-Criterion-001a).'
card_owner: Amazon Web Services, Inc.
card_category: Managed Agent Platform · Enterprise SaaS
card_tags: *id001
score_basis: consistent
---
# AWS Bedrock Agents

Eight CVEs with the Amazon CNA in the trailing 12 months (2025-11-06 → 2026-11-06), two scored 9.0 on the CNA v3.1 vector: code injection in the @aws/agentcore CLI (CVE-2026-11393) and in the bedrock-agentcore-starter-toolkit (CVE-2026-105812). CVE-2026-16796 is recorded by AWS as a bypass of the CVE-2026-12530 fix. CVE-2026-18830 (InvokeHarness, 8.1) was fixed service-side on 2026-07-31 with no customer action. Each AWS bulletin was published with the fixed version on the same date. The Code Interpreter Sandbox DNS-tunneling path reported on 2025-09-01 was remediated by AWS on 2026-04-15 per the reporting researcher's dated update; AWS documentation now describes Sandbox mode as limited external network access to AWS services. Bedrock FAQ and Service Terms state that inputs and outputs are not used to train Amazon or third-party models, with abuse-detection retention up to 30 days. AgentCore Cedar Policy provides default-deny enforcement at the Gateway outside the model loop. `supply_chain_compromise_12mo` re-evaluated from true to false: CVE-2026-4269 is a vulnerability only; no publicly confirmed write (SupplyChain-Criterion-001a).

## Layer 0 Score: 49/85 (Tier B)

**V** 12/20 · **R** 6/20 · **D** 13/15 · **I** 6/10 · **C** 4/10 · **T** 8/10 — previous 55/85 (2026-03-25, Tier A, v0.3.1); updated 2026-11-06 (routine lane, batch 1).

## CISA KEV

None — no CVE attributed to AWS Bedrock Agents / AgentCore appears in the CISA Known Exploited Vulnerabilities catalog (catalogVersion 2026.11.04, 1,768 entries; operator-supplied JSON check retrieved 2026-11-06). 8 published CVEs attributed to the product scope in the trailing 12 months (exact): CVE-2026-4269 (7.5), CVE-2026-11393 (9.0), CVE-2026-12530 (7.3), CVE-2026-15737 (5.7), CVE-2026-16796 (7.3), CVE-2026-18830 (8.1), CVE-2026-105812 (9.0), CVE-2026-106032 (5.7) — CNA v3.1 scores, NVD primary assessment not provided at evaluation time. Supply chain: none confirmed — CVE-2026-4269 is a vulnerability only; no publicly confirmed write (SupplyChain-Criterion-001a).

## Bias Disclosure

This evaluation uses Claude (Anthropic) as its tooling. Anthropic operates in the AI agent market and may compete with some evaluated vendors. VERDICT discloses this relationship in every report and applies identical evaluation criteria to all platforms regardless of their relationship to Anthropic.

VERDICT additionally discloses a parent-identity relationship (Trigger 1). The operator of record, Amazon Web Services, Inc., is an Amazon.com, Inc. company (https://press.aboutamazon.com/aws; https://aws.amazon.com/agreement/). Amazon holds a strategic equity position in Anthropic: USD 8 billion previously invested (https://www.aboutamazon.com/news/company-news/amazon-anthropic-ai-investment), and on 2026-04-20 Amazon stated that it will invest USD 5 billion in Anthropic and up to an additional USD 20 billion in the future tied to certain commercial milestones (https://www.aboutamazon.com/news/company-news/amazon-invests-additional-5-billion-anthropic-ai); Anthropic's Series H announcement of 2026-05-28 states that the round includes USD 5 billion from Amazon, listed separately (https://www.anthropic.com/news/series-h). Amazon is a material Anthropic equity-holder as recorded in KNOWN_FACTS.md. Related commitments on the public record: Anthropic uses AWS as its primary cloud provider and has adopted AWS Trainium and Inferentia chips. Identical evaluation criteria were applied regardless of this relationship.

Product-level integration, recorded separately: Anthropic Claude models are among the third-party models selectable in Amazon Bedrock (https://aws.amazon.com/bedrock/anthropic/).

Trigger 2 (compound cap-table) and Trigger 3 (non-arms-length channel) were assessed separately and do not fire: the chain of control ends at Amazon.com, Inc., a publicly listed company with no controlling owner, and no exclusive distribution, joint venture, white-label or revenue-share arrangement with a material equity-holder beyond standard supplier-customer relations was located.

## Evaluation History

| Date | Type | Score | Tier | Framework |
|---|---|---|---|---|
| 2026-03-25 | Initial (Layer 0) | 55/85 | A | v0.3.1 |
| 2026-11-06 | Update (Layer 0, routine lane, batch 1) | 49/85 | B | v0.3.2 |

## Full Evaluation

# VERDICT Evaluation #017 — AWS Bedrock Agents (Update)

| Field | Value |
|---|---|
| Evaluation number | #017 |
| Platform | AWS Bedrock Agents (Amazon Bedrock Agents · Amazon Bedrock AgentCore) |
| Type | Update (Differential Evaluation, Layer 0) |
| Date | 2026-11-06 (`updated_at`); original Layer 0 `evaluated_at` 2026-03-25 |
| Evaluator | VERDICT engine · `evaluator_model: claude-fable-5-1` (as supplied at invocation, Batch1-TrancheA-Authorize-2026-10-31-A1) |
| Target version | Hosted services as examined on 2026-11-06: Amazon Bedrock Agents (classic; maintenance mode since 2026-07-30) and Amazon Bedrock AgentCore (GA 2025-10-13: Runtime, Code Interpreter, Policy, Gateway, harness); AWS-maintained AgentCore client tooling — `bedrock-agentcore` (PyPI; latest release examined v1.21.0, 2026-08-06), `bedrock-agentcore-starter-toolkit` (PyPI; deprecated by AWS 2026-03-27; last fix 0.3.14), `@aws/agentcore` (npm; fix 0.14.2 / 1.0.0-preview.9) |
| Framework | VERDICT v0.3.2 (zinova-lab/verdict-engine @ 73d9a09) |
| Previous evaluation | 2026-03-25 · 55/85 · Tier A · framework v0.3.1 (migrated capture) |
| Operator of record | Amazon Web Services, Inc. (subsidiary; `parent_entity: Amazon.com, Inc.`) |
| Lane | Routine (batch-1 scheduled; interval not elapsed) |

## Executive Summary

Eight CVEs with the Amazon CNA were published against the AgentCore product scope in the trailing 12 months (2025-11-06 → 2026-11-06), two of them scored 9.0 on the CNA's CVSS v3.1 vector (CVE-2026-11393, CVE-2026-105812), against a count of 1 with no recorded maximum in the 2026-03-25 record. The Layer 0 total moves from 55/85 to 49/85 (Tier B); the movement comes from R (11 → 6: CVE count 8 with a 9.0 penalty, maximum CVSS 9.0, and CVE-2026-16796 recorded as a bypass of the CVE-2026-12530 fix), from V (14 → 12: closed-source hosted service with Apache-2.0 client tooling, SOC 2 reports available to customers through AWS Artifact only), and from I and C (8 → 6 and 5 → 4: session-level stop documented without a platform-level emergency-stop procedure, user confirmation optional, execution-role defaults documented by third-party research as broad until 2026), partly offset by T (5 → 8: Amazon acts as CNA with same-day bulletins, ISO/IEC 42001 certification) and D (12 → 13: training-use exclusion with stated retention periods). `supply_chain_compromise_12mo` is re-evaluated from `true` to `false`: CVE-2026-4269 is a vulnerability only; no publicly confirmed write (SupplyChain-Criterion-001a). The DNS-tunneling path in the Code Interpreter sandbox mode recorded in March 2026 was, per the reporting researcher's dated update and AWS's current documentation, remediated by AWS on 2026-04-15; no CVE in the counted set appears in the CISA KEV catalog (catalogVersion 2026.11.04, operator-supplied check).

## Scorecard

| Dimension | Score | Max | Rating | Differential |
|---|---|---|---|---|
| V — Verifiability | 12 | 20 | Mid | re-evaluated (prev. 14) |
| R — Resilience | 6 | 20 | Low | re-evaluated (prev. 11) |
| D — Data Conduct | 13 | 15 | High | re-evaluated (prev. 12) |
| I — Identity & Control | 6 | 10 | Mid | re-evaluated (prev. 8) |
| C — Containment | 4 | 10 | Mid | re-evaluated (prev. 5) |
| T — Transparency | 8 | 10 | High | re-evaluated (prev. 5) |
| **Layer 0 total** | **49** | **85** | | previous 55 (−6) |

Tier: B
Category: Managed Agent Platform · Enterprise SaaS

CISA KEV: none — no counted CVE appears in the catalog (catalogVersion 2026.11.04, count 1768; operator-supplied JSON check, retrieved 2026-11-06).

## Dimension Detail

### V — Verifiability · 12/20 (Mid)

| Criterion | Result | Score | Evidence |
|---|---|---|---|
| Developer / company identity | Corporate registration confirmed by the vendor's own legal page: AWS Customer Agreement §12 names Amazon Web Services, Inc., 410 Terry Avenue North, Seattle, WA 98109-5210 as the default contracting party (Last Updated October 29, 2026); AWS Privacy Notice (Last Updated May 18, 2026) names the same entity. No public registry was queried. Official contact: aws-security@amazon.com and the AWS VDP on HackerOne. | 4/4 | https://aws.amazon.com/agreement/ · https://aws.amazon.com/privacy/ · https://aws.amazon.com/security/vulnerability-reporting/ |
| Source code disclosure | The evaluated product is a hosted service (Bedrock Agents, AgentCore Runtime / Code Interpreter / Policy / Gateway); its service source is not published. AWS-maintained client tooling is published under Apache-2.0 (`bedrock-agentcore-sdk-python`, `bedrock-agentcore-starter-toolkit`, `agentcore-cli`). Client SDKs are not the product's core or control plane (Criterion-VSource-001), so the hosted product scores as closed source. | 0/4 | https://github.com/aws/bedrock-agentcore-sdk-python · https://github.com/aws/bedrock-agentcore-starter-toolkit · https://github.com/aws/agentcore-cli |
| Version management transparency | Client tooling: GitHub releases with release notes and per-release change lists (SDK v1.21.0, 2026-08-06). Hosted services: dated "What's New" announcements and documentation history; no versioned changelog for the service itself. Partial. | 1/3 | https://github.com/aws/bedrock-agentcore-sdk-python/releases/tag/v1.21.0 · https://aws.amazon.com/about-aws/whats-new/2025/10/amazon-bedrock-agentcore-available/ |
| Third-party dependency disclosure | AWS sub-processors list published with update date (Last Updated October 30, 2026) and a 30-day change-notification subscription. | 3/3 | https://aws.amazon.com/compliance/sub-processors/ |
| Independent certification | SOC 1 / SOC 2 reports are available to AWS customers through AWS Artifact (customers-only); SOC 3 is public. Amazon Bedrock and Amazon Bedrock AgentCore are listed in SOC scope (page last updated August 11, 2026). | 2/4 | https://aws.amazon.com/compliance/soc-faqs/ · https://aws.amazon.com/compliance/services-in-scope/SOC/ |
| Functional reproducibility docs | Complete API references (Bedrock Agents API, AgentCore developer guide with runtime, session, policy and network-mode behaviour). | 2/2 | https://docs.aws.amazon.com/bedrock/latest/userguide/agents.html · https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/what-is-bedrock-agentcore.html |

Positive findings: operator of record confirmed on the vendor's own legal pages; dated sub-processor list; AgentCore and Bedrock named in SOC, ISO (list dated September 1, 2026), FedRAMP (page dated October 15, 2026: Bedrock and AgentCore in both the East/West and GovCloud columns) and HIPAA-eligible (list dated September 3, 2026) scope pages.

Recorded concerns: the hosted service is closed source; SOC 2 reports are gated behind AWS Artifact (what is public: SOC 3 and the services-in-scope lists; what is gated: SOC 1/2 Type 2 reports); the hosted service carries no versioned changelog.

### R — Resilience · 6/20 (Low)

CVE window: 2025-11-06 → 2026-11-06. Product scope bound to `target_version` (hosted Bedrock Agents / AgentCore services and the three AWS-maintained AgentCore client packages). CVSS source: NVD shows no NIST primary assessment for any of the eight IDs at the time of evaluation; the CNA (Amazon, AMZN) v3.1 vector is used for each (Attribution-CVE-002 order NVD v3.1 → CNA v3.1). Each vector was recomputed in-session; every computed score equals the stated CNA v3.1 score. CNA v4.0 scores are noted where published.

| Criterion | Result | Score | Evidence |
|---|---|---|---|
| CVE count (trailing 12 months) | 8 (exact). Band 6–9 → 1; penalty −1 because CVSS 9.0+ exists (CVE-2026-11393, CVE-2026-105812) → 0. | 0/5 | AWS security bulletins 2026-008 / -040 / -044 / -058 / -065 / -073 / -127 (URLs in Incident Timeline) |
| Maximum CVSS severity | 9.0 (CNA v3.1; vector-computed 9.0) — CVE-2026-11393 and CVE-2026-105812. | 0/6 | https://nvd.nist.gov/vuln/detail/CVE-2026-11393 · https://app.opencve.io/cve/CVE-2026-105812 |
| Patch response speed | Every bulletin was published with the fixed version (or the service-side fix) available on the bulletin date; CVE-2026-18830 was fixed service-side 2026-07-31, bulletin 2026-08-04. ≤7 days. | 3/3 | https://aws.amazon.com/security/security-bulletins/2026-073-aws/ |
| Structural issues | Same root cause recurring: CVE-2026-16796 (2026-07-23) is recorded by AWS and the reporting researcher as a bypass of the CVE-2026-12530 fix (`install_packages()` argument injection, 2026-06-17); CVE-2026-105812 (starter toolkit import-agent code injection) and CVE-2026-11393 (`@aws/agentcore` import-agent code injection) share the issue class. | 0/3 | https://aws.amazon.com/security/security-bulletins/2026-065-aws/ · https://github.com/aws/bedrock-agentcore-sdk-python/security/advisories/GHSA-j6g5-3hh3-pgw8 |
| Supply chain compromise (trailing 12 months) | None. Searches of PyPI / npm / GitHub for `bedrock-agentcore`, `bedrock-agentcore-starter-toolkit` and `@aws/agentcore` located no public confirmation of an unauthorized write to an AWS package, account, build pipeline or distribution endpoint. CVE-2026-4269 (S3 bucket-ownership bypass permitting build-time injection into AgentCore Runtime builds) is a vulnerability only; no publicly confirmed write (SupplyChain-Criterion-001a). Unrelated malicious npm packages with "agentcore" in their names located in the window are not AWS packages and are not attributed. | 3/3 | https://aws.amazon.com/security/security-bulletins/2026-008-aws/ · https://pypi.org/project/bedrock-agentcore/1.18.1/ · https://www.npmjs.com/package/@aws/agentcore/v/0.14.2 |

Positive findings: Amazon operates as a CNA and published a bulletin for each ID with the fix version on the same date; AWS applied the CVE-2026-18830 fix service-side with no customer action required; the deprecated starter toolkit still received a fix release (0.3.14) on 2026-10-06.

Recorded concerns: two 9.0-scored code-injection CVEs in client tooling; a fix bypass (CVE-2026-12530 → CVE-2026-16796) within five weeks; one service-side CVE (CVE-2026-18830, InvokeHarness tool-use block dispatched without the model, CNA v3.1 8.1); the prior record's `max_cvss_12mo: null` beside `cve_count_12mo: 1` is an omission of the 2026-03-25 capture — CVE-2026-4269 carried a CNA v3.1 score of 7.5 on its bulletin date.

### D — Data Conduct · 13/15 (High)

| Criterion | Result | Score | Evidence |
|---|---|---|---|
| GDPR compliance disclosure | AWS GDPR Data Processing Addendum incorporated into the AWS Service Terms (§1.14.1; Service Terms Last Updated November 5, 2026) with SCCs and UK/Swiss addenda; AWS GDPR Center states the compliance position explicitly. | 3/3 | https://aws.amazon.com/service-terms/ · https://aws.amazon.com/compliance/gdpr-center/ |
| Data minimization | Model invocation logging is off by default. Abuse-detection retention of inputs and outputs for up to 30 days applies by default to certain models (Service Terms §50.12.2; Bedrock data-retention modes `none` / `default` / `aws_review` / `inherit`, with `inherit` the default for new accounts). Opt-out is available per model where the model permits `none`; some models require `aws_review`. Default ON, easy opt-out. | 1/3 | https://docs.aws.amazon.com/bedrock/latest/userguide/model-invocation-logging.html · https://docs.aws.amazon.com/bedrock/latest/userguide/data-retention.html · https://docs.aws.amazon.com/bedrock/latest/userguide/abuse-detection.html |
| AI training use | Bedrock FAQ: "AWS and the third-party model providers will not use any inputs to or outputs from Amazon Bedrock to train Amazon Nova, Amazon Titan, or any third-party models"; inputs/outputs "not shared with any model providers". Service Terms §50.3 (service-improvement use) does not list Amazon Bedrock. Retention period stated (abuse detection up to 30 days; retention modes documented). | 4/4 | https://aws.amazon.com/bedrock/faqs/ · https://aws.amazon.com/service-terms/ · https://docs.aws.amazon.com/bedrock/latest/userguide/data-retention.html |
| Sub-processor transparency | List with update date (October 30, 2026). | 3/3 | https://aws.amazon.com/compliance/sub-processors/ |
| Data retention disclosure | Per-category: Bedrock abuse-detection retention up to 30 days; AgentCore Memory short-term retention configurable up to 365 days; AgentCore Browser session data TTL 30 days; AgentCore Gateway content stored in DynamoDB/S3 under KMS and not used to provide or maintain the service. | 2/2 | https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/data-protection.html · https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/memory.html |

Positive findings: training-use exclusion stated on the vendor's FAQ and consistent with the Service Terms; per-category retention published for AgentCore components.

Recorded concerns: the sentence quoted in the 2026-03-25 record ("Amazon Bedrock doesn't store or use your data to train models") no longer appears on the Bedrock data-protection page, which now links to the data-retention and abuse-detection pages (documentation change recorded as a fact; the FAQ wording above carries the commitment). Abuse-detection retention is on by default for certain models and cannot be disabled for models that require `aws_review`. Service Terms §50.12.5.1 provides for metadata notification to Anthropic in defined circumstances.

### I — Identity & Control · 6/10 (Mid)

| Criterion | Result | Score | Evidence |
|---|---|---|---|
| Emergency stop documentation | AgentCore Runtime session lifecycle and session termination are documented; IAM can revoke invocation permissions; Bedrock Agents (classic) can be disabled through the agent configuration. No platform-level emergency-stop procedure (single documented action halting all running agents) was located. Documented but incomplete. | 2/4 | https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/runtime-sessions.html · https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/runtime-security-best-practices.html |
| Human-in-the-loop design | Bedrock Agents user confirmation (CONFIRM / DENY before an action-group function executes) is available and developer-configured per action; not enabled by default. | 1/3 | https://docs.aws.amazon.com/bedrock/latest/userguide/agents-userconfirmation.html |
| Permission delegation transparency | Execution-role scope, AgentCore Identity (inbound/outbound credentials, workload identity), Gateway targets and credential management are documented with scope and delegation targets. | 3/3 | https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/security-credentials-management.html · https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/identity-data-protection.html |

Positive findings: AgentCore Policy (Cedar) provides deterministic, default-deny enforcement at the Gateway with forbid-overrides-permit semantics and ENFORCE / LOG_ONLY modes, outside the model's reasoning loop.

Recorded concerns: user confirmation is optional and per-action; no documented platform-wide stop procedure.

### C — Containment · 4/10 (Mid)

| Criterion | Result | Score | Evidence |
|---|---|---|---|
| Sandbox design | Code Interpreter offers Sandbox (documented as "limited external network access to AWS services"; access to Amazon S3), Public and VPC network modes; AgentCore Runtime runs each session in a dedicated microVM with memory sanitized on termination. Allowlisted access in Sandbox mode, but Public mode is available and the DNS path in Sandbox mode was open until 2026-04-15 (dated facts below). Hybrid. | 2/4 | https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/code-interpreter-resource-management.html · https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/runtime-sessions.html |
| Least privilege | Execution roles are customer-configurable. Third-party research (BeyondTrust, 2026-03-16; Zenity Labs, reported October 2026) recorded broad default roles created by the starter toolkit and by the AgentCore default execution role, with AWS's permissions change recorded by Zenity between 2026-06-22 and 2026-09-29. Configurable. | 1/3 | https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/runtime-security-best-practices.html · https://www.beyondtrust.com/blog/entry/pwning-aws-agentcore-code-interpreter · https://thenextweb.com/news/aws-agentcore-zenity-agentcorruption-one-prompt-agents |
| Tenant isolation (cloud) | Per-session microVM isolation is documented by AWS; no independent verification of cross-tenant isolation was located and no public cross-tenant breach was located. Claimed but unverified. | 1/3 | https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/runtime-sessions.html |

Positive findings: microVM-per-session design documented; VPC mode available for Code Interpreter; IMDSv2 / MMDSv2 defaults applied to new agents from 2026-02-14 (as recorded by Unit 42 and Zenity).

Recorded concerns: Sandbox-mode DNS tunneling (reported 2025-09-01, remediated 2026-04-15); metadata-service credential-exposure paths reported by Unit 42, Sonrai and Zenity in the window (no CVE issued); default execution-role breadth recorded by two research teams.

### T — Transparency · 8/10 (High)

| Criterion | Result | Score | Evidence |
|---|---|---|---|
| CVE publication posture | Amazon is a CNA; AWS Security Bulletins published for every counted CVE with GHSA cross-references. | 2/2 | https://aws.amazon.com/security/security-bulletins/ · https://aws.amazon.com/security/vulnerability-reporting/ |
| Incident disclosure speed | All eight bulletins published on the fix date (≤30 days). The Code Interpreter DNS item carried no AWS bulletin; AWS's position was published through documentation changes and statements to the researchers (recorded in Contextual Analysis). | 2/2 | https://aws.amazon.com/security/security-bulletins/2026-127-aws/ |
| Security policy publication | Detailed technical and organizational measures: Bedrock security chapter, AgentCore security best practices, shared-responsibility model. | 2/2 | https://docs.aws.amazon.com/bedrock/latest/userguide/security.html · https://aws.amazon.com/compliance/shared-responsibility-model/ |
| AI safety framework reference | External framework adopted: ISO/IEC 42001:2023 certification (first surveillance audit completed with no findings, November 2025; Amazon Bedrock in scope) and a published AWS Responsible AI Policy. | 2/2 | https://aws.amazon.com/blogs/security/aws-successfully-completed-its-first-surveillance-audit-for-iso-420012023-with-no-findings · https://aws.amazon.com/machine-learning/responsible-ai/policy |
| AI system identity disclosure | No default disclosure to end users that they are interacting with an AI agent was located for Bedrock Agents or AgentCore (Titan image watermarking / provenance data applies to images only). | 0/2 | https://docs.aws.amazon.com/bedrock/latest/userguide/titan-image-models.html#titanimage-watermark |

Positive findings: CNA status, same-day bulletins, ISO/IEC 42001 certification.

Recorded concerns: no end-user AI identity disclosure for agents; the DNS item had no vendor bulletin.

## Incident Timeline

Window 2025-11-06 → 2026-11-06. CVSS = CNA v3.1 (vector-computed value equal to the stated value in every case); CNA v4.0 in parentheses where published. NVD per-CVE pages returned only the page shell in-session (client-rendered); CNA data was read through the AWS bulletins, the GitHub advisories and CVE mirrors (opencve, cvefeed, GitLab advisories). All eight IDs have published CVE List records (no RESERVED state; Convention-CVEReserved-001 note not required).

| Date | CVE ID | CVSS | Description | Patch status | KEV |
|---|---|---|---|---|---|
| 2026-03-16 | CVE-2026-4269 | 7.5 (v4.0 5.8) | `bedrock-agentcore-starter-toolkit` < 0.1.13: S3 bucket-ownership check bypass (CWE-283/340) permitting build-time code injection into AgentCore Runtime builds created after 2025-09-24. Vulnerability only; no publicly confirmed write (SupplyChain-Criterion-001a). | Fixed 0.1.13 · bulletin 2026-008 · GHSA-xfhr-q72q-jcrj | No |
| 2026-06-08 | CVE-2026-11393 | 9.0 (v4.0 8.8) | `@aws/agentcore` CLI 0.4.0–0.14.1 and 1.0.0 previews: code injection on `agentcore add agent --type import` (CWE-94). | Fixed 0.14.2 / 1.0.0-preview.9 · bulletin 2026-040 · GHSA-m4x6-gwgp-4pm7 | No |
| 2026-06-17 | CVE-2026-12530 | 7.3 (v4.0 8.4) | `bedrock-agentcore` ≥ 1.1.3 < 1.6.1: argument injection in `install_packages()` (CWE-88). | Fixed 1.6.1 · bulletin 2026-044 · GHSA-6rfw-mq36-jm8h | No |
| 2026-07-16 | CVE-2026-15737 | 5.7 (v4.0 5.7) | `bedrock-agentcore` 1.4.8, 1.5.0: OpenTelemetry spans wrote raw prompts and responses to the `aws/spans` CloudWatch log group (CWE-532). | Fixed 1.5.1 · bulletin 2026-058 · GHSA-hqf8-7w95-9r33 | No |
| 2026-07-23 | CVE-2026-16796 | 7.3 (v4.0 8.4) | `bedrock-agentcore` < 1.18.1: bypass of the CVE-2026-12530 fix through extras-group handling (same root cause). | Fixed 1.18.1 · bulletin 2026-065 · GHSA-j6g5-3hh3-pgw8 | No |
| 2026-08-04 | CVE-2026-18830 | 8.1 (v4.0 8.6) | Amazon Bedrock AgentCore harness, InvokeHarness API (service-side): tool-use block dispatched without model involvement (CWE-1287). | Fixed service-side 2026-07-31; no customer action · bulletin 2026-073 | No |
| 2026-10-06 | CVE-2026-105812 | 9.0 (v4.0 8.8) | `bedrock-agentcore-starter-toolkit` ≥ 0.1.4 ≤ 0.3.13: code injection in import-agent handling (CWE-94); toolkit deprecated by AWS 2026-03-27. | Fixed 0.3.14 · bulletin 2026-127 | No |
| 2026-10-06 | CVE-2026-106032 | 5.7 (v4.0 5.7) | `bedrock-agentcore-starter-toolkit` ≥ 0.1.4 ≤ 0.3.13: SSRF / local file read through OpenAPI reference resolution (CWE-918). | Fixed 0.3.14 · bulletin 2026-127 | No |

Bulletin URLs: https://aws.amazon.com/security/security-bulletins/2026-008-aws/ · https://aws.amazon.com/security/security-bulletins/2026-040-aws/ · https://aws.amazon.com/security/security-bulletins/2026-044-aws/ · https://aws.amazon.com/cn/security/security-bulletins/2026-058-aws/ · https://aws.amazon.com/security/security-bulletins/2026-065-aws/ · https://aws.amazon.com/security/security-bulletins/2026-073-aws/ · https://aws.amazon.com/security/security-bulletins/2026-127-aws/

Non-CVE items in the window (dated facts; no CVE issued; not counted):

| Date | Item | Source |
|---|---|---|
| 2025-09-01 | BeyondTrust Phantom Labs reports DNS tunneling from Code Interpreter Sandbox mode to AWS via HackerOne (#3323153). | https://www.beyondtrust.com/blog/entry/pwning-aws-agentcore-code-interpreter |
| 2025-11-01 / 2025-11-17 | AWS deploys an initial fix; fix rolled back (as recorded by BeyondTrust). | same |
| 2025-11-17 | Unit 42 reports Sandbox-mode DNS tunneling and metadata-service (MMDS) access without token enforcement to AWS. | https://unit42.paloaltonetworks.com/bypass-of-aws-sandbox-network-isolation-mode/ |
| 2025-12-23 / 2025-12-30 | AWS states that no code fix will ship and that documentation will change; AWS assigns CVSS 7.5 to the HackerOne report (as recorded by BeyondTrust). | BeyondTrust, above |
| 2025-12-25 / 2026-01-12 | Zenity Labs reports IMDSv1 credential-exposure and default execution-role findings to AWS (as reported). | https://thenextweb.com/news/aws-agentcore-zenity-agentcorruption-one-prompt-agents |
| 2026-02-14 | IMDSv2 / MMDSv2 becomes the default for new agents (as recorded by Unit 42 and Zenity). | Unit 42, above |
| 2026-03-16 | BeyondTrust public disclosure; AWS documentation wording recorded as changed from "complete isolation with no external access" to "limited external network access". | BeyondTrust, above |
| 2026-04-07 | Unit 42 publication. | Unit 42, above |
| 2026-04-15 | AWS remediates the DNS tunneling path; BeyondTrust's dated update states "DNS exfiltration is no longer possible". | BeyondTrust, above |
| 2026 (window) | Sonrai Security publishes a metadata-service string-filter bypass in AWS code interpreters. | https://sonraisecurity.com/blog/sandboxed-to-compromised-new-research-exposes-credential-exfiltration-paths-in-aws-code-interpreters/ |
| 2026-07-30 | Amazon Bedrock Agents (classic) closed to new customers; maintenance mode; model catalog frozen; no end-of-life date published. | https://docs.aws.amazon.com/bedrock/latest/userguide/agents-classic-maintenance-mode.html |
| 2026-10 | Zenity Labs "AgentCorruption" presentation; AWS statement describes the behaviours as expected and documented; permissions change recorded between 2026-06-22 and 2026-09-29. | thenextweb, above |

## Contextual Analysis

The 2026-03-25 record captured one CVE. The count of eight recorded here reflects the period after that capture: seven of the eight IDs were published between June and October 2026, all in AgentCore client tooling except CVE-2026-18830 (service-side). Five of the eight concern code or argument injection in developer-facing import, build and package-installation paths of the SDK, CLI and starter toolkit; these affect the developer workstation or build environment rather than the hosted runtime, and AWS's bulletins state the fixed versions in each case. CVE-2026-16796 is documented by AWS and by the reporting researcher as a bypass of the fix for CVE-2026-12530; this is the basis of the structural-issues score. CVE-2026-18830 is the one service-side issue; AWS fixed it on 2026-07-31 and published the bulletin on 2026-08-04 with the note that no customer action was required.

On the Code Interpreter Sandbox mode, the record states the dated sequence as published by the researchers and by AWS's documentation: a report on 2025-09-01, an initial fix and rollback in November 2025, a statement in December 2025 that the behaviour would be addressed through documentation, a public disclosure on 2026-03-16, and a remediation on 2026-04-15 recorded in the researcher's dated update. AWS's published position, as quoted by the researchers, is that Sandbox mode provides network access exclusively to Amazon S3 and that DNS resolution is enabled for S3 operations; the current documentation describes Sandbox mode as providing limited external network access to AWS services. The March 2026 record's statement that no code-level remedy was deployed was accurate on its date and is superseded by the 2026-04-15 remediation.

On metadata-service and execution-role findings (Unit 42, Sonrai, Zenity), AWS issued no CVE; its statements, as reported, describe the behaviours as expected and documented, and the vendors' and researchers' dated accounts record IMDSv2 / MMDSv2 defaults for new agents from 2026-02-14 and a permissions change in the third quarter of 2026. The record presents both the researchers' findings and AWS's position without characterizing either.

Supply chain: CVE-2026-4269 permitted injection into customers' AgentCore Runtime builds through an S3 bucket-ownership bypass in the starter toolkit. No vendor or independent source states that an unauthorized write occurred to an AWS-controlled package, account, build pipeline or distribution endpoint; the field is therefore false and the CVE is scored under R. The 2026-03-25 record's `supply_chain_compromise_12mo: true` rested on this vulnerability alone.

Product status: Amazon Bedrock Agents (classic) entered maintenance mode on 2026-07-30 with no published end-of-life date; AgentCore (GA 2025-10-13) is the actively developed surface, with client tooling releases through August 2026 and a fix release in October 2026. The dormancy test is not met; `dormant_since` is omitted.

Compliance scope: AWS publishes the services-in-scope lists (SOC, ISO, FedRAMP, HIPAA) and the SOC 3 report; SOC 1/2 reports are available to customers through AWS Artifact. The base record's "FedRAMP High" wording is replaced by what the current page states (Bedrock and AgentCore listed in the East/West and GovCloud columns, page dated October 15, 2026); the authorization level is read from that page rather than restated here. AWS's AgentCore compliance page lists HIPAA eligibility, FedRAMP, SOC 2, ISO 27001/27017/27018/27701/22301/20000-1/9001 and CSA STAR.

Operator of record: AWS Customer Agreement §12 names Amazon Web Services, Inc. as the contracting party; AWS press material describes AWS as an Amazon.com, Inc. company (https://press.aboutamazon.com/aws). `independence` is recorded as `subsidiary` with `parent_entity: Amazon.com, Inc.`; the chain of control ends at Amazon.com, Inc. (publicly listed, no controlling owner).

Third-party evaluations: no entry for Amazon Bedrock Agents or AgentCore was located in the MIT AI Agent Index 2025 (https://aiagentindex.mit.edu/2025) — none located.

Evidence rule: every factual claim in this report is cited to a URL retrieved during the session or to operator input recorded in the Differential section.

## VERDICT Record

**Summary.** AWS Bedrock Agents / AgentCore scores 49/85 (Tier B) on 2026-11-06, down from 55/85: eight CNA-published CVEs including two scored 9.0 and one fix bypass lower R, while CNA status, same-day bulletins, ISO/IEC 42001 and a stated training-use exclusion with retention periods hold T and D high.

**Risk Factor Summary by Use Case**

| Use case | Observations |
|---|---|
| Internal testing | Client-tooling CVEs (SDK, CLI, starter toolkit) affect developer environments; fixed versions published; starter toolkit deprecated 2026-03-27. |
| Credential-handling workloads | Metadata-service credential-exposure paths reported by three research teams in the window, no CVE; IMDSv2 / MMDSv2 default for new agents from 2026-02-14; execution-role scope is customer-configured. |
| Cloud multi-tenant | Per-session microVM isolation documented by AWS; no independent verification located; no public cross-tenant breach located. |
| Regulated-data workloads | Bedrock and AgentCore listed in SOC, ISO, FedRAMP and HIPAA-eligible scope; abuse-detection retention up to 30 days applies by default for certain models and is required for some. |

**Reference Information** (options, not instructions)

1. The AWS bulletin index and the three package advisories pages can be used to pin client tooling at or above the fixed versions (bedrock-agentcore ≥ 1.18.1, @aws/agentcore ≥ 0.14.2, starter toolkit ≥ 0.3.14).
2. The Bedrock data-retention page documents per-model retention modes for accounts that want to set an explicit mode rather than inherit the default.
3. The AgentCore Code Interpreter network-mode documentation and the runtime security best-practices page describe VPC mode and execution-role scoping.

**Bias Disclosure**

This evaluation uses Claude (Anthropic) as its tooling. Anthropic operates in the AI agent market and may compete with some evaluated vendors. VERDICT discloses this relationship in every report and applies identical evaluation criteria to all platforms regardless of their relationship to Anthropic.

VERDICT additionally discloses a parent-identity relationship (Trigger 1). The operator of record, Amazon Web Services, Inc., is an Amazon.com, Inc. company (https://press.aboutamazon.com/aws; https://aws.amazon.com/agreement/). Amazon holds a strategic equity position in Anthropic: USD 8 billion previously invested (https://www.aboutamazon.com/news/company-news/amazon-anthropic-ai-investment), and on 2026-04-20 Amazon stated that it will invest USD 5 billion in Anthropic and up to an additional USD 20 billion in the future tied to certain commercial milestones (https://www.aboutamazon.com/news/company-news/amazon-invests-additional-5-billion-anthropic-ai); Anthropic's Series H announcement of 2026-05-28 states that the round includes USD 5 billion from Amazon, listed separately (https://www.anthropic.com/news/series-h). Amazon is a material Anthropic equity-holder as recorded in KNOWN_FACTS.md. Related commitments on the public record: Anthropic uses AWS as its primary cloud provider and has adopted AWS Trainium and Inferentia chips. Identical evaluation criteria were applied regardless of this relationship.

Product-level integration, recorded separately: Anthropic Claude models are among the third-party models selectable in Amazon Bedrock (https://aws.amazon.com/bedrock/anthropic/).

Trigger 2 (compound cap-table) does not fire: the chain of control ends at Amazon.com, Inc., a publicly listed company with no controlling owner, and no material-investor relationship in the evaluated platform by another material equity-holder was located. Trigger 3 (non-arms-length channel) does not fire: no exclusive distribution, joint venture, white-label or revenue-share arrangement with a material equity-holder beyond standard supplier-customer relations was located. Tags: `evaluator-coi`, `direct-investment`.

## Future Evaluation Plan

- Layer 1 (behavioral testing): not scheduled; AgentCore has no free tier that meets Absolute Rule 2 without account billing, and Bedrock Agents (classic) is closed to new customers — Layer 1 awaits a free-tier path or a separately ratified runner protocol.
- Layer C: routine lane, 365 days from `updated_at` (pipeline-derived `next_review_due`). Interrupt-lane watch items: further AgentCore client-tooling CVEs (T1), any KEV addition (T2), a published end-of-life date for Bedrock Agents (classic) (T5 if accompanied by a terms change), and any AWS bulletin on the metadata-service findings.

## Differential

| Item | Value |
|---|---|
| Previous evaluation | 2026-03-25 · 55/85 · Tier A · framework v0.3.1 |
| This evaluation | 2026-11-06 · 49/85 · Tier B · framework v0.3.2 · −6 |
| Lane | Routine (batch-1 scheduled; interval not elapsed) — no sweep row fired an interrupt trigger (operator input below) |

**Per-dimension state (carry-forward checks, 2026-11-06):** V — re-evaluated — migrated capture, no sources. R — re-evaluated — migrated capture, no sources. D — re-evaluated — migrated capture, no sources. I — re-evaluated — migrated capture, no sources. C — re-evaluated — migrated capture, no sources. T — re-evaluated — migrated capture, no sources. E — null (Layer 0). Reason no carry-forward was possible: the base record carries `sources: []`, so carry-forward conditions 1–4 (URL resolution, document dates, window changes, window incidents) could not be positively satisfied for any dimension; none was carried forward by inference from the absence of news.

**Prior-record omissions and inconsistencies, stated as facts:** `max_cvss_12mo: null` beside `cve_count_12mo: 1` (CVE-2026-4269 carried CNA v3.1 7.5 on 2026-03-16); `supply_chain_compromise_12mo: true` rested on a vulnerability (CVE-2026-4269) with no recorded write — re-evaluated to `false` under SupplyChain-Criterion-001a on the evidence read (AWS bulletin 2026-008, GHSA-xfhr-q72q-jcrj, PyPI/npm/GitHub searches, no confirming source located), an in-pipeline differential that contributes to the R movement through the count and maximum rather than the supply-chain criterion itself (3/3 in both evaluations); `sources: []`; `qa` unresolved ×3 (resolved here by full protocol); `evaluator_model: unrecorded` (now `claude-fable-5-1`); `target_version: null` (now bound); `independence: unrecorded` (now `subsidiary`); comparative and superlative wording of the prior record not carried (Absolute Rule 7).

**Score movement (≥5):** R 11 → 6 (count 8 with 9.0 penalty, max 9.0, fix bypass); V 14 → 12 (closed-source hosted service; SOC 2 customers-only; partial changelog); I 8 → 6 (session-level stop only; confirmation optional); C 5 → 4 (hybrid sandbox; configurable least privilege; isolation claimed); D 12 → 13 (retention periods stated beside the training exclusion); T 5 → 8 (CNA, same-day bulletins, ISO/IEC 42001).

**Operator input (OperatorInput-001), supplied 2026-11-06 (JST) as Message 3:**
1. Quarterly sweep 2026-10-27 (operations_sweep_procedure.md, dry run), public-layer rows for slug `bedrock`: none — no T1 / T2 / T5 / dormancy observation row; the record entered batch 1 under LayerC-Triage-001 on its recorded `cve_count_12mo` (1, exact). Attribution judgment on the eight IDs above is this evaluation's own.
2. CISA KEV JSON feed (https://www.cisa.gov/sites/default/files/feeds/known_exploited_vulnerabilities.json), retrieved 2026-11-06: catalogVersion "2026.11.04", dateReleased "2026-11-04T20:00:05.774Z", count 1768. CVE-2026-4269 not present; no entry whose vendorProject, product, vulnerabilityName or shortDescription contains "Bedrock" or "AgentCore"; no entry with vendorProject beginning "Amazon" added in the window 2025-11-06 → 2026-11-06. The remaining seven IDs are recorded as not present on the same basis (no Bedrock / AgentCore / Amazon-vendor entry in the window) and were additionally checked in-session against per-CVE trackers, which show no KEV listing; a per-ID feed check can be run by Operations on request.
3. Rendered text of unread pages: none supplied. Pages the session could not read: the NVD per-CVE pages (https://nvd.nist.gov/vuln/detail/CVE-2026-4269 and the other seven IDs; client-rendered shell only — CNA data was read through the AWS bulletins, GitHub advisories and CVE mirrors, and NVD's "assessment not yet provided" status through search excerpts) and the English Bedrock Agents maintenance-mode page (https://docs.aws.amazon.com/bedrock/latest/userguide/agents-classic-maintenance-mode.html; a localized rendering supplied the 2026-07-30 facts). These are stated as unread, not scored as silence; operator-rendered text can be recorded at the next pass.

**Disclosure layer:** Trigger 1 fires (Amazon.com, Inc. parent; Amazon in the material set). Trigger 2 and Trigger 3 assessed separately: neither fires. Tags `evaluator-coi`, `direct-investment`. Lightspeed: not in the set; record silent.

**Known Fact Corrections:** Amazon entry applied (figures listed separately, never summed; no cumulative total above USD 8 billion plus USD 5 billion). No Bedrock entry exists at base; no KNOWN_FACTS candidate staged (no published fact found to have become incorrect).

## Evaluation History

| Date | Type | Score | Tier | Framework |
|---|---|---|---|---|
| 2026-03-25 | Initial (Layer 0) | 55/85 | A | v0.3.1 |
| 2026-11-06 | Update (Layer 0, routine lane, batch 1) | 49/85 | B | v0.3.2 |
