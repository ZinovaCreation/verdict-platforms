---
name: Salesforce Agentforce
slug: agentforce
operator: 'Salesforce, Inc. (NYSE: CRM)'
independence: independent
parent_entity: null
category: CRM-Native Agent Builder · Enterprise SaaS
homepage: https://www.salesforce.com/agentforce/
github: https://github.com/salesforce
evaluation_number: 20
evaluation_type: update
evaluated_at: '2026-03-25'
updated_at: '2026-11-06'
evaluator_model: claude-fable-5-1
framework_version: v0.3.2
layer: '0'
target_version: "Winter '27 (release 264)"
previous_evaluation_date: '2026-03-25'
previous_score: 58
score: 59
max_score: 85
tier: A
verdict:
  v:
    score: 13
    rating: Mid
    note: 'Closed source; SOC 2/ISO login-gated; dated sub-processors; dated change log'
  e:
    score: null
    rating: null
    note: null
  r:
    score: 14
    rating: High
    note: 'No CVE in window; Web-to-Lead injection recurs; SalesBleed fix 79–112 days'
  d:
    score: 11
    rating: High
    note: 'DPA+SCC/BCR; no-training stated; masking off for agents; aggregated use'
  i:
    score: 8
    rating: High
    note: 'Confirmation default on standard actions; escalation topic; no stop runbook'
  c:
    score: 6
    rating: Mid
    note: 'Trusted URLs bypassed twice; least privilege configurable; isolation claimed'
  t:
    score: 7
    rating: High
    note: 'CNA + advisories; ISO 42001; no vendor bulletin for in-window advisories'
cisa_kev:
  present: false
  entries: []
cve_count_12mo: 0
cve_count_basis: exact
max_cvss_12mo: null
supply_chain_compromise_12mo: false
known_facts_applied: []
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
- prompt-injection
- web-to-lead
- cve-less-advisories
- data-masking-disabled
- iso-42001
- hitl-defaults
- closed-source
rank: 10
sources:
- https://www.salesforce.com/company/msa.jsp
- https://www.sec.gov/Archives/edgar/data/1108524/000110852426000060/crm-20260131.htm
- https://www.salesforce.com/company/privacy/
- https://security.salesforce.com/responsible-disclosure-policy/
- https://salesforce.com/news/stories/winter-2027-product-release-announcement
- https://www.salesforce.com/en-us/wp-content/uploads/sites/4/documents/legal/misc/trust-and-compliance-change-log.pdf?bc=OTH
- https://www.salesforce.com/en-us/wp-content/uploads/sites/4/documents/legal/misc/salesforce-infrastructure-and-subprocessors.pdf
- https://compliance.salesforce.com/en/documents/a00Kd00000z7FAnIAM
- https://compliance.salesforce.com/en/documents/a00Kd00000zh1D6IAI
- https://compliance.salesforce.com/en/services/agentforce-einstein-platform
- https://compliance.salesforce.com/en/documents/a00Kd00000z7GXZIA2
- https://www.salesforce.com/en-us/wp-content/uploads/sites/4/documents/legal/misc/einstein-platform-security-privacy-and-architecture.pdf
- https://developer.salesforce.com/docs/ai/agentforce/guide/agent-api.html
- https://developer.salesforce.com/docs/einstein/genai/guide/agent-api-overview.html
- https://app.opencve.io/cve/?vendor=salesforce
- https://www.cvelogic.com/product/salesforce/agentforce_vibes
- https://cve.circl.lu/vuln/fkie_cve-2025-64320
- https://venturebeat.com/security/microsoft-salesforce-copilot-agentforce-prompt-injection-cve-agent-remediation-playbook
- https://www.csoonline.com/article/4159079/copilot-and-agentforce-fall-to-form-based-prompt-injection-tricks.html
- https://www.securityweek.com/salesbleed-flaws-in-salesforce-agentforce-enabled-zero-click-data-exfiltration/
- https://www.theregister.com/security/2026/09/24/salesforce-agentforce-vulns-allowed-0-click-crm-data-theft-anonymous-phishing/5298958
- https://www.theregister.com/2025/09/26/salesforce_agentforce_forceleak_attack/
- https://noma.security/blog/forcedleak-agent-risks-exposed-in-salesforce-agentforce/
- https://security.salesforce.com/advisory-archives/
- https://help.salesforce.com/s/articleView?id=005133036&type=1
- https://help.salesforce.com/s/articleView?id=005132147&type=1
- https://help.salesforce.com/s/articleView?id=005134951&type=1
- https://www.salesforce.com/wp-content/uploads/sites/4/documents/legal/Agreements/data-processing-addendum.pdf
- https://www.salesforce.com/en-us/wp-content/uploads/sites/4/documents/legal/Privacy/agentforce-privacy-FAQ.pdf
- https://developer.salesforce.com/docs/ai/agentforce/guide/trust.html
- https://developer.salesforce.com/blogs/2024/07/the-einstein-audit-and-feedback-data-model-in-data-cloud
- https://developer.salesforce.com/blogs/2023/10/inside-the-einstein-trust-layer
- https://developer.salesforce.com/docs/einstein/genai/guide/org-setup.html
- https://www.salesforce.com/blog/llm-data-masking/
- https://trailhead.salesforce.com/content/learn/modules/the-einstein-trust-layer/meet-the-einstein-trust-layer
- https://trailhead.salesforce.com/content/learn/modules/trusted-agentic-ai/explore-agentforce-guardrails-and-trust-patterns
- https://trailhead.salesforce.com/content/learn/projects/build-an-agent-to-nurture-leads/create-a-user-record-for-your-agent
- https://architect.salesforce.com/docs/architect/well-architected/guide/trust-agentic-patterns.html
- https://www.salesforce.com/blog/agent-handoff/
- https://releasebot.io/updates/salesforce/agentforce
- https://www.salesforceben.com/salesforce-to-auto-enable-agentforce-in-winter-27-what-that-means-for-you/
- https://www.technadu.com/?p=610626
- https://promptarmor.com/resources/one-key-way-salesforce-mitigates-ai-risk
- https://www.salesforce.com/blog/salesforce-iso-42001-agentforce-certification/
- https://aiagentindex.mit.edu/2025/agentforce/
- https://www.salesforce.com/news/stories/fedramp-high-agentforce-salesforce-platform/
- https://www.fedramp.gov/marketplace/products/FR2003061248/
- https://compliance.salesforce.com/en/documents/a005A00000t4NpRQAU
- https://www.salesforce.com/fedramp/
- https://help.salesforce.com/s/articleView?id=release-notes.rn_einstein.htm&release=264&type=5
- https://help.salesforce.com/s/articleView?id=release-notes.rn_einstein_copilot.htm&release=264&type=5
- https://help.salesforce.com/s/articleView?id=000396813&type=1
- https://help.salesforce.com/s/articleView?id=ai.generative_ai_trust_setup.htm&type=5
- https://api.status.salesforce.com/v1/generalMessages
og_description: 'Independent security evaluation of Salesforce Agentforce. Score: 59/85 (prev 58). No CVE in the trailing 12 months; two CVE-less prompt-injection disclosures (PipeLeak, SalesBleed) repeat the Web-to-Lead exfiltration pattern. Data masking disabled for agents. Framework v0.3.2.'
category_line: CRM-Native Agent Builder · Enterprise SaaS
display_tags: &id001
- text: No CVE in Window · 2 CVE-less Advisories
  color: amber
- text: Web-to-Lead Injection · Recurring Root Cause
  color: red
- text: SalesBleed · 79–112 Day Fix Confirmation
  color: warn
- text: Data Masking Disabled · Agents
  color: warn
- text: ISO 42001 · DPA · HITL Defaults
  color: safe
finding: 'Update 2026-11-06: 59/85 (prev 58). No CVE with Agentforce as the affected product in the trailing 12 months; PipeLeak (Apr 2026) and SalesBleed (Sep 2026) are CVE-less advisories, not counted. All three published chains since 2025 start with a Web-to-Lead prompt injection and end with CRM data leaving through an agent output channel (structural issue). SalesBleed fix confirmed 79 days (first chain) and 112 days (all three) after report. Einstein Trust Layer data masking disabled for agents. Closed source; SOC 2 / ISO reports login-gated. DPA with SCCs/BCRs, dated sub-processor list and release-note change log, no-training statement, ISO 42001, confirmation defaults for standard actions; Agentforce listed within the Government Cloud Plus FedRAMP High boundary.'
meta_description: 'Independent security evaluation of Salesforce Agentforce. Score: 59/85 (prev 58). No CVE in the trailing 12 months; two CVE-less prompt-injection disclosures (PipeLeak, SalesBleed) repeat the Web-to-Lead exfiltration pattern. Data masking disabled for agents. Framework v0.3.2.'
key_finding: 'No CVE with Agentforce as the affected product was published in the trailing 12 months (2025-11-06 → 2026-11-06); PipeLeak (Capsule Security, 2026-04-15) and SalesBleed (Zenity Labs, 2026-09-24) carry no CVE ID and are recorded as advisories. Each published Agentforce chain since 2025 (ForcedLeak, PipeLeak, SalesBleed) begins with indirect prompt injection through a Web-to-Lead form and ends with CRM data leaving through an agent output channel. SalesBleed: reported 2026-06-01, Trusted URLs bypass fix confirmed 2026-08-19, all three fixes confirmed 2026-09-21. Einstein Trust Layer data masking is disabled for Agentforce agents. Confirmation is default for ten standard actions, email actions and Slack actions; custom actions are admin-configured. DPA (Apr 2026) with SCCs and BCRs, dated sub-processor list, explicit no-training statement, ISO 42001 covering Agentforce. Closed source; SOC 2 and ISO reports require portal login; release notes carry a week-dated change log. Salesforce lists Agentforce (Customer & Employee Agents) as Authorized within the Government Cloud Plus FedRAMP High boundary (Help 000396813, 2026-10-07; not DoD IL5).'
card_owner: 'Salesforce, Inc. (NYSE: CRM)'
card_category: CRM-Native Agent Builder · Enterprise SaaS
card_tags: *id001
score_basis: consistent
---
# Salesforce Agentforce

No CVE with Agentforce as the affected product was published in the trailing 12 months (2025-11-06 → 2026-11-06); PipeLeak (Capsule Security, 2026-04-15) and SalesBleed (Zenity Labs, 2026-09-24) carry no CVE ID and are recorded as advisories. Each published Agentforce chain since 2025 (ForcedLeak, PipeLeak, SalesBleed) begins with indirect prompt injection through a Web-to-Lead form and ends with CRM data leaving through an agent output channel. SalesBleed: reported 2026-06-01, Trusted URLs bypass fix confirmed 2026-08-19, all three fixes confirmed 2026-09-21. Einstein Trust Layer data masking is disabled for Agentforce agents. Confirmation is default for ten standard actions, email actions and Slack actions; custom actions are admin-configured. DPA (Apr 2026) with SCCs and BCRs, dated sub-processor list, explicit no-training statement, ISO 42001 covering Agentforce. Closed source; SOC 2 and ISO reports require portal login; release notes carry a week-dated change log. Salesforce lists Agentforce (Customer & Employee Agents) as Authorized within the Government Cloud Plus FedRAMP High boundary (Help 000396813, 2026-10-07; not DoD IL5).

## Layer 0 Score: 59/85 (Tier A)

**V** 13/20 · **R** 14/20 · **D** 11/15 · **I** 8/10 · **C** 6/10 · **T** 7/10 · previous 58/85 (2026-03-25)

## CISA KEV

None — no entry in the CISA Known Exploited Vulnerabilities catalog names Salesforce or Agentforce (catalogVersion 2026.11.04, 1,768 entries, checked 2026-11-06). 0 published CVEs attributed to Salesforce Agentforce in the trailing 12 months (basis: exact); two CVE-less advisories (PipeLeak, SalesBleed) are recorded in the Incident Timeline and are not counted.

## Bias Disclosure

This evaluation uses Claude (Anthropic) as its tooling. Anthropic operates in the AI agent market and may compete with some evaluated vendors. VERDICT discloses this relationship in every report and applies identical evaluation criteria to all platforms regardless of their relationship to Anthropic.

## Evaluation History

| Date | Type | Score | Tier | Framework |
|---|---|---|---|---|
| 2026-03-25 | Initial (migrated capture) | 58/85 | A | v0.3.1 |
| 2026-11-06 | Update (differential, full re-evaluation; run 2 with operator input) | 59/85 | A | v0.3.2 |

## Full Evaluation

# VERDICT Evaluation #020 — Salesforce Agentforce

| Field | Value |
|---|---|
| Evaluation number | #020 |
| Platform | Salesforce Agentforce |
| Evaluation type | Update (Differential Evaluation, Layer 0) |
| Evaluated at (original Layer 0) | 2026-03-25 |
| Updated at | 2026-11-06 |
| Evaluator | VERDICT evaluation engine · `evaluator_model: claude-fable-5-1` (operator selection, EvaluatorModel-Provenance-001) |
| Target version | Winter '27 (Salesforce release 264, GA 2026-10-12); hosted service, continuously updated |
| Framework | VERDICT v0.3.2 · zinova-lab/verdict-engine @ 899f556 |
| Previous evaluation | 2026-03-25 · 58/85 · Tier A · framework v0.3.1 (migrated capture) |
| Lane | Routine (batch-1 scheduled; interval not elapsed) — Tranche B 4 of 14 |
| Trailing 12-month window (R) | 2025-11-06 → 2026-11-06 |

## Executive Summary

No CVE with Agentforce as the affected product was published in the trailing 12 months; the vulnerabilities disclosed in the window — "PipeLeak" (Capsule Security, published 2026-04-15) and the three "SalesBleed" flaws (Zenity Labs, reported 2026-06-01, fixes confirmed 2026-08-19 and 2026-09-21, published 2026-09-24) — carry no CVE ID and are recorded as CVE-less advisories (Attribution-CVE-001). Each of the three publicly documented Agentforce attack chains since 2025 (ForcedLeak, PipeLeak, SalesBleed) begins with an indirect prompt injection through a Web-to-Lead form and ends with CRM data leaving the org through an agent output channel, which the R dimension records as a recurring root cause. The score moves from 58/85 to 59/85 (Tier A unchanged): R rises from 8 to 14 because the window contains no CVE and no supply chain compromise, V falls from 16 to 13 because source code is closed and the SOC 2 and ISO reports sit behind a portal login, and D falls from 13 to 11 on the telemetry and retention criteria. Salesforce publishes a DPA with SCCs and BCRs, a dated sub-processor list with a change log, ISO 42001 certification covering Agentforce, and default confirmation for a set of standard agent actions. No CISA KEV entry names Salesforce or Agentforce.

## Scorecard

| Dimension | Score | Max | Rating | Previous (2026-03-25) |
|---|---|---|---|---|
| V — Verifiability | 13 | 20 | Mid | 16 |
| E — Effectiveness | — | 15 | not evaluated (Layer 1+) | — |
| R — Resilience | 14 | 20 | High | 8 |
| D — Data Conduct | 11 | 15 | High | 13 |
| I — Identity & Control | 8 | 10 | High | 8 |
| C — Containment | 6 | 10 | Mid | 6 |
| T — Transparency | 7 | 10 | High | 7 |
| **Layer 0 total** | **59** | **85** | | **58** |

Tier: A
Category: CRM-Native Agent Builder · Enterprise SaaS

CISA KEV: None — no catalog entry names Salesforce or Agentforce (catalogVersion 2026.11.04, 1,768 entries; operator JSON check 2026-11-06, OperatorInput-001).

`cve_count_12mo: 0` (basis: exact) · `max_cvss_12mo: null` · `supply_chain_compromise_12mo: false`

## Differential

**Previous evaluation:** 2026-03-25 · 58/85 · Tier A · framework v0.3.1 · migrated capture (`sources: []`, `qa` unresolved ×3, `evaluator_model: unrecorded`).

**Trigger:** Scheduled batch-1 differential (LayerC-Triage-001; quarterly sweep 2026-10-27; Batch1-TrancheA-Authorize-2026-10-31-A1). Routine 365-day interval not elapsed. No interrupt trigger fired.

**Per-dimension state:**

| Dimension | State | Basis |
|---|---|---|
| V | re-evaluated — migrated capture, no sources | carry-forward conditions 1–4 cannot be met |
| R | re-evaluated — migrated capture, no sources | mandatory in every differential |
| D | re-evaluated — migrated capture, no sources | carry-forward conditions 1–4 cannot be met |
| I | re-evaluated — migrated capture, no sources | carry-forward conditions 1–4 cannot be met |
| C | re-evaluated — migrated capture, no sources | carry-forward conditions 1–4 cannot be met |
| T | re-evaluated — migrated capture, no sources | mandatory in every differential |
| E | null | Layer 1+ only |

**Carry-forward checks:** none performed. The base record cites no source URL for any dimension, so none of the four carry-forward conditions (URL resolves; no later effective date; no changing release note; no incident touching the dimension) can be positively satisfied (convention 2026-09-22).

**Operator input (OperatorInput-001), retrieved by the operator 2026-11-06 JST:**

1. Quarterly sweep 2026-10-27, public-layer rows for slug `agentforce`: none. No T1 / T2 / T5 / dormancy observation row; the record entered batch 1 on its recorded `cve_count_12mo: 1` (exact).
2. CISA KEV JSON feed (https://www.cisa.gov/sites/default/files/feeds/known_exploited_vulnerabilities.json): catalogVersion "2026.11.04", dateReleased 2026-11-04T20:00:05.774Z, 1,768 entries. No entry whose vendorProject, product, vulnerabilityName or shortDescription contains "Salesforce" or "Agentforce"; none added in the window 2025-11-06 → 2026-11-06.
3. Rendered text of pages the session could not read — supplied as operator input, run 2, retrieved by the operator with a browser on 2026-11-06 JST (OperatorInput-001):
   - https://help.salesforce.com/s/articleView?id=release-notes.rn_einstein.htm&release=264&type=5 — Winter '27 "Agentforce and Generative AI" release-notes landing page with a change log by month (additions, updates and removals dated by week, August 2026 through entries scheduled to April 2027). The URL named in run 1 (release-notes.rn_agentforce.htm) does not exist; the Agentforce landing page is rn_einstein.htm.
   - https://help.salesforce.com/s/articleView?id=release-notes.rn_einstein_copilot.htm&release=264&type=5 — the Winter '27 Agentforce and Generative AI feature notes (child page).
   - https://help.salesforce.com/s/articleView?id=000396813&type=1 — "Government Cloud Available Products and Features" (publish date 2026-10-07); the URL named in run 1 (000384503) redirects server-side to this article.
   - https://help.salesforce.com/s/articleView?id=ai.generative_ai_trust_setup.htm&type=5 — "Set up Einstein Trust Layer" (no publish date shown). The linked "Data Masking and Agents" article could not be resolved from the rendered page and remains unread.
   - https://status.salesforce.com/ landing text and the public feed https://api.status.salesforce.com/v1/generalMessages (15 current general messages, with full bodies for the Agentforce-named message and the security advisories).

**Pages the session tools could not read in run 1, and their resolution (SourceCoverage-001 / OperatorInput-001):**

| URL (run 1) | Bearing | Run 1 observation | Resolution (run 2, operator input 2026-11-06) |
|---|---|---|---|
| release-notes.rn_agentforce.htm&release=264 (does not exist) and release-notes.salesforce_release_notes.htm&release=264 | V — version management | JavaScript loading shell only | Read via operator input: rn_einstein.htm (change log by month) and rn_einstein_copilot.htm (feature notes). V version management re-judged 1 → 3. |
| articleView?id=000384503 | V — independent certification (FedRAMP) | loading shell only | Read via operator input: redirects to article 000396813 "Government Cloud Available Products and Features" (2026-10-07). SOC 2 criterion unchanged (2); FedRAMP boundary statement recorded in the Contextual Analysis. |
| Salesforce Help "Set up Einstein Trust Layer" (ai.generative_ai_trust_setup.htm) | D — data minimization defaults | not retrievable | Read via operator input. The page carries data-masking toggles only ("Data Masking is enabled by default" at org level; "Data masking for LLMs is disabled for agents"); it states no telemetry or aggregated-use opt-out. D data minimization unchanged (0). The linked "Data Masking and Agents" article remains unread. |
| https://status.salesforce.com/ | T — vendor bulletins | JavaScript required | Read via operator input (landing text + /v1/generalMessages feed). No general message names PipeLeak, SalesBleed, ForcedLeak or Web-to-Lead; T incident disclosure speed unchanged (0). One Agentforce-named operational message in the window (20000269, 2026-10-30) recorded in the Incident Timeline. |

Run 1 of this evaluation was delivered at 57/85 with the four pages stated as unread; this run re-judges only the dimensions named there (V version management, V certification, D data minimization, T) against the operator-supplied text. Still unread: the Salesforce Help article "Data Masking and Agents" (linked from the Trust Layer setup page; not resolvable from the rendered links).

**Prior-record omissions and corrections, stated as facts:**

- The base record recorded `cve_count_12mo: 1` (exact) and `max_cvss_12mo: 9.4` without naming a CVE ID. No CVE ID was ever assigned to ForcedLeak: the 9.4 is a CVSS v4.0 score calculated by Noma Security, the reporting researcher, and The Register reported that no CVE was issued (https://www.theregister.com/2025/09/26/salesforce_agentforce_forceleak_attack/). Under Attribution-CVE-001 a CVE-less advisory is not counted and does not set `max_cvss_12mo`; the prior count of 1 and maximum of 9.4 are superseded, not corrected to a known value. ForcedLeak's first public disclosure (2025-09-25) is outside the current window.
- The base record carried `independence: unrecorded`, `target_version: null`, `evaluator_model: unrecorded` and `qa` unresolved ×3; all are resolved in this update.
- The base record's comparative lines ("first AI agent platform in this index …", "strongest least-privilege architecture in this index") are not carried (Absolute Rule 7, QA §2).

## Dimension Detail

### V — Verifiability · 13/20 · Mid

| Criterion | Result | Score | Evidence URL |
|---|---|---|---|
| Developer / company identity | Confirmed both. Legal entity Salesforce, Inc. (Delaware), Salesforce Tower, 415 Mission Street, San Francisco, named in the Main Services Agreement §12.9 (updated 2023-10-16) and as registrant of the Form 10-K for FY ended 2026-01-31 (SEC EDGAR, Commission file 001-32224 — public registry record). Official contacts: privacy@salesforce.com and the Data Protection Officer (Privacy Statement, effective 2026-05-19); security contact form at security.salesforce.com/contact/ (Responsible Disclosure Policy). | 4/4 | https://www.salesforce.com/company/msa.jsp · https://www.sec.gov/Archives/edgar/data/1108524/000110852426000060/crm-20260131.htm · https://www.salesforce.com/company/privacy/ · https://security.salesforce.com/responsible-disclosure-policy/ |
| Source code disclosure | Closed source. Agentforce is a hosted service; no source repository for the agents, the reasoning engine or the Einstein Trust Layer is published (Criterion-VSource-001). | 0/4 | https://www.sec.gov/Archives/edgar/data/1108524/000110852426000060/crm-20260131.htm (Item 1: Agentforce as the agentic layer of the Agentforce 360 Platform) |
| Version management transparency | Release notes + full changelog. The Winter '27 "Agentforce and Generative AI" release notes (release 264, GA 2026-10-12) carry per-feature notes and a "Release Note Changes by Month" change log that dates each addition, update and removal by week (for example "Build and Activate Agents with a Simpler Versioning Process — Removed the week of October 12, 2026"; "Agents Now Default to Error Mode for File Uploads — Added the week of October 12, 2026"), with forward-dated model reroute notices to April 2027. A separate dated Trust & Compliance change log covers the legal documents. Pages read via operator input, run 2 (retrieved 2026-11-06). | 3/3 | https://help.salesforce.com/s/articleView?id=release-notes.rn_einstein.htm&release=264&type=5 · https://help.salesforce.com/s/articleView?id=release-notes.rn_einstein_copilot.htm&release=264&type=5 · https://salesforce.com/news/stories/winter-2027-product-release-announcement · https://www.salesforce.com/en-us/wp-content/uploads/sites/4/documents/legal/misc/trust-and-compliance-change-log.pdf?bc=OTH |
| Third-party dependency disclosure | Sub-processor list with update dates. "Salesforce Infrastructure and Sub-processors" names, for Einstein Generative AI Services (covering Agentforce), OpenAI L.L.C., Microsoft Corporation (Azure), Google LLC, Amazon Web Services and Bright Data Inc., with processing locations; the Trust & Compliance change log dates each revision (e.g. 2025-10-21 Agentforce IT Service sub-processors added; 2025-12-16 Einstein Platform clarification; 2026-01-06 Agentforce Supply Chain initial publication). Customers may subscribe to new sub-processor notifications. | 3/3 | https://www.salesforce.com/en-us/wp-content/uploads/sites/4/documents/legal/misc/salesforce-infrastructure-and-subprocessors.pdf · https://compliance.salesforce.com/en/documents/a00Kd00000z7FAnIAM · https://www.salesforce.com/en-us/wp-content/uploads/sites/4/documents/legal/misc/trust-and-compliance-change-log.pdf?bc=OTH |
| Independent certification | SOC 2 customers/registered users only. "SOC 2 Report - Salesforce Agentforce Operations" (period 2026-02-01 to 2026-06-30, updated 2026-06-09) is listed on the compliance portal with "Login to download"; ISO/IEC 27001:2022, 27017, 27018 (updated 2026-10-30) and ISO 42001:2023 (updated 2026-10-01) certificates are likewise login-gated. The Einstein Platform Security, Privacy and Architecture document (2026-07-24) states SOC 2 is "available on request". No SOC 2 or SOC 3 report is publicly downloadable. | 2/4 | https://compliance.salesforce.com/en/documents/a00Kd00000zh1D6IAI · https://compliance.salesforce.com/en/services/agentforce-einstein-platform · https://compliance.salesforce.com/en/documents/a00Kd00000z7GXZIA2 · https://www.salesforce.com/en-us/wp-content/uploads/sites/4/documents/legal/misc/einstein-platform-security-privacy-and-architecture.pdf |
| Functional reproducibility docs | Partial. An Agent API developer guide and reference exist (session lifecycle, REST access); the guide describes agents as "goal-oriented, autonomous AI agents" but publishes no behavioral specification of the reasoning engine (planning, topic selection, escalation decision rules). | 1/2 | https://developer.salesforce.com/docs/ai/agentforce/guide/agent-api.html · https://developer.salesforce.com/docs/einstein/genai/guide/agent-api-overview.html |

**Positive findings.** Operator identity, registration and contacts are confirmed on vendor legal pages and a public registry. Release notes carry a week-dated change log of additions, updates and removals. The sub-processor documentation is dated, revision-logged and covers the generative-AI providers used by Agentforce. A public responsible-disclosure policy pledges not to initiate legal action against researchers who follow it.

**Recorded concerns.** The product is closed source. SOC 2 and ISO certificates are behind a portal login. The Agent API documentation covers the interface, not agent behaviour.

### R — Resilience · 14/20 · High

CVE evaluation window: 2025-11-06 → 2026-11-06. Product scope: Agentforce (agents, Atlas reasoning engine, Einstein Trust Layer as applied to Agentforce) as bound by `target_version`.

| Criterion | Result | Score | Evidence URL |
|---|---|---|---|
| CVE count (trailing 12 months) | 0. NVD and CVE aggregators list no CVE whose affected product is Agentforce in the window. The three Salesforce-CNA CVEs that carry the Agentforce name (CVE-2025-64320, -64321, -64322) affect the Agentforce Vibes Extension, a Visual Studio Code IDE extension outside the evaluated product scope, and were published 2025-11-04, two days before the window start. PipeLeak (2026-04-15) and SalesBleed (2026-09-24) carry no CVE ID (Attribution-CVE-001; not a Convention-CVEReserved-001 case — no CNA advisory or CNA vector exists). | 5/5 | https://app.opencve.io/cve/?vendor=salesforce · https://www.cvelogic.com/product/salesforce/agentforce_vibes · https://cve.circl.lu/vuln/fkie_cve-2025-64320 · https://venturebeat.com/security/microsoft-salesforce-copilot-agentforce-prompt-injection-cve-agent-remediation-playbook · https://www.securityweek.com/salesbleed-flaws-in-salesforce-agentforce-enabled-zero-click-data-exfiltration/ |
| Maximum CVSS severity | No CVE of record in the window; `max_cvss_12mo: null`. The 9.4 attached to ForcedLeak is a researcher-calculated CVSS v4.0 value (Noma Security), not a CVSS of record, and ForcedLeak predates the window. | 6/6 | https://www.theregister.com/2025/09/26/salesforce_agentforce_forceleak_attack/ · https://noma.security/blog/forcedleak-agent-risks-exposed-in-salesforce-agentforce/ |
| Patch response speed | 31+ days, measured on the in-window CVE-less disclosures (no CVE exists to measure). SalesBleed: reported 2026-06-01; Trusted URLs bypass fix confirmed 2026-08-19 (79 days); all three fixes confirmed 2026-09-21 (112 days). PipeLeak: Salesforce stated on 2026-04-16 that "the specific scenario described" was remediated; report and fix dates are not published. (Reference, outside window: ForcedLeak reported 2025-07-28, Trusted URLs enforcement 2025-09-08 — 42 days.) | 0/3 | https://www.theregister.com/security/2026/09/24/salesforce-agentforce-vulns-allowed-0-click-crm-data-theft-anonymous-phishing/5298958 · https://www.securityweek.com/salesbleed-flaws-in-salesforce-agentforce-enabled-zero-click-data-exfiltration/ · https://venturebeat.com/security/microsoft-salesforce-copilot-agentforce-prompt-injection-cve-agent-remediation-playbook · https://noma.security/blog/forcedleak-agent-risks-exposed-in-salesforce-agentforce/ |
| Structural issues | Same root cause recurring. Three independently published chains share the entry point (indirect prompt injection via a public Web-to-Lead form processed by an agent) and the outcome (CRM data leaving through an agent output channel): ForcedLeak (image tag to an expired CSP-allowlisted domain, 2025-09), PipeLeak (email action, 2026-04), SalesBleed (Trusted URLs parsing weaknesses, DNS and Slack link unfurling, 2026-09). Two of the three fall inside the window. | 0/3 | https://noma.security/blog/forcedleak-agent-risks-exposed-in-salesforce-agentforce/ · https://www.csoonline.com/article/4159079/copilot-and-agentforce-fall-to-form-based-prompt-injection-tricks.html · https://www.theregister.com/security/2026/09/24/salesforce-agentforce-vulns-allowed-0-click-crm-data-theft-anonymous-phishing/5298958 |
| Supply chain compromise (trailing 12 months) | None. Searches for Agentforce npm / PyPI / SDK / package compromise return no public confirmation of an unauthorized write to a Salesforce-owned package, account, build pipeline or distribution endpoint for Agentforce (SupplyChain-Criterion-001). The Salesloft Drift third-party OAuth incident (Salesforce advisories 2025-08-27/28) concerns a third-party connected app, predates the window, and is not an Agentforce distribution-path event. | 3/3 | https://security.salesforce.com/advisory-archives/ · https://help.salesforce.com/s/articleView?id=005134951&type=1 |

**Positive findings.** No CVE and no supply chain compromise attributable to Agentforce in the window. Salesforce operates as a CVE Numbering Authority (security@salesforce.com is the sourceIdentifier on its CVE records) and publishes a vendor advisory for each Vibes CVE. The SalesBleed chains were fixed before publication, and Salesforce stated it had no evidence of customer exploitation.

**Recorded concerns.** The indirect-prompt-injection-to-exfiltration pattern recurred in two separate disclosures inside the window after a third in 2025. Fix confirmation for SalesBleed took 79 days for the first chain and 112 days for all three. Capsule Security stated on retest that the email channel remained exploitable on custom topics (sub-agents); Salesforce stated the specific scenario was remediated. VERDICT records both positions and does not adjudicate.

### D — Data Conduct · 11/15 · High

| Criterion | Result | Score | Evidence URL |
|---|---|---|---|
| GDPR compliance disclosure | DPA standard provision + explicit statement. Data Processing Addendum (Revision April 2026) with SCC Modules 2 and 3 (Decision (EU) 2021/914), UK ICO Addendum, Swiss transfers, Processor BCRs; the Agentforce Privacy FAQ (June 2025) states Agentforce is covered by the DPA, the SCCs and Appendix A of the Processor BCR. | 3/3 | https://www.salesforce.com/wp-content/uploads/sites/4/documents/legal/Agreements/data-processing-addendum.pdf · https://www.salesforce.com/en-us/wp-content/uploads/sites/4/documents/legal/Privacy/agentforce-privacy-FAQ.pdf |
| Data minimization | Default ON without a documented opt-out in the pages read. The Einstein Platform SPARC (2026-07-24) states Salesforce may use Customer Data in aggregated, anonymized form for research, benchmarking and product innovation; the Trust Layer stores requests, responses, quality scores and feedback in the customer's Data 360 (required for the Trust Layer to function), and the 2023 developer blog states feedback outcomes are used to refine Salesforce's models. The "Set up Einstein Trust Layer" Help page (read via operator input, run 2) carries data-masking toggles only and states no telemetry or aggregated-use opt-out; no opt-out for the aggregated-use statement is published in the documents read. | 0/3 | https://www.salesforce.com/en-us/wp-content/uploads/sites/4/documents/legal/misc/einstein-platform-security-privacy-and-architecture.pdf · https://developer.salesforce.com/blogs/2024/07/the-einstein-audit-and-feedback-data-model-in-data-cloud · https://developer.salesforce.com/blogs/2023/10/inside-the-einstein-trust-layer · https://developer.salesforce.com/docs/einstein/genai/guide/org-setup.html · https://help.salesforce.com/s/articleView?id=ai.generative_ai_trust_setup.htm&type=5 |
| AI training use | Not used + retention period stated. The Agentforce Privacy FAQ states Salesforce "does not currently use Customer Data to train generative AI models", that any future training would require opt-in under the Product Terms, and that zero-data-retention terms with LLM providers mean third-party LLMs do not retain or train on Customer Data. The SPARC states post-termination data may remain inactive up to 120 days and is then deleted within a further 120 days. | 4/4 | https://www.salesforce.com/en-us/wp-content/uploads/sites/4/documents/legal/Privacy/agentforce-privacy-FAQ.pdf · https://www.salesforce.com/en-us/wp-content/uploads/sites/4/documents/legal/misc/einstein-platform-security-privacy-and-architecture.pdf · https://developer.salesforce.com/docs/ai/agentforce/guide/trust.html |
| Sub-processor transparency | List with update date (see V). | 3/3 | https://www.salesforce.com/en-us/wp-content/uploads/sites/4/documents/legal/misc/salesforce-infrastructure-and-subprocessors.pdf · https://www.salesforce.com/en-us/wp-content/uploads/sites/4/documents/legal/misc/trust-and-compliance-change-log.pdf?bc=OTH |
| Data retention disclosure | Stated but vague. Agentforce "does not store Customer Data" (FAQ); retention follows the underlying Service; post-termination 120 + 120 days (SPARC). No retention period is published for Trust Layer audit, prompt or feedback records held in Data 360. | 1/2 | https://www.salesforce.com/en-us/wp-content/uploads/sites/4/documents/legal/Privacy/agentforce-privacy-FAQ.pdf · https://www.salesforce.com/en-us/wp-content/uploads/sites/4/documents/legal/misc/einstein-platform-security-privacy-and-architecture.pdf |

**Positive findings.** DPA with SCCs, UK addendum and Processor BCRs; 30-day objection right to new sub-processors with a termination-and-refund remedy; explicit no-training statement with an opt-in requirement for any change; zero-data-retention commitments with LLM providers; dated sub-processor list.

**Recorded concerns.** Einstein Trust Layer data masking is disabled for Agentforce agents — the Trust Layer setup page states "Data Masking is enabled by default" at org level and "Data masking for LLMs is disabled for agents" (Salesforce Help, operator input 2026-11-06; also Salesforce blog 2025-06-10, Privacy FAQ June 2025, Trailhead, Salesforce Architects guide). A Winter '27 beta masks PII in Agentforce session logs at query time (observability data, not LLM prompts). Aggregated, anonymized use of Customer Data is stated without a published opt-out. Audit/feedback retention periods are not stated.

### I — Identity & Control · 8/10 · High

| Criterion | Result | Score | Evidence URL |
|---|---|---|---|
| Emergency stop documentation | Documented but incomplete. Vendor release notes (as reproduced by Releasebot from help.salesforce.com) state admins can activate or deactivate individual agents in Agentforce Builder and that the Agentforce platform is enabled by default in Winter '27 with the org-level toggle removed; the platform can be disabled through the Einstein setting. No vendor-published emergency-stop procedure for a running autonomous agent (session termination, kill switch) was read in-session. | 2/4 | https://releasebot.io/updates/salesforce/agentforce · https://www.salesforceben.com/salesforce-to-auto-enable-agentforce-in-winter-27-what-that-means-for-you/ · https://developer.salesforce.com/docs/einstein/genai/guide/org-setup.html |
| Human-in-the-loop design | Enabled by default for standard sensitive actions. Salesforce changed `isConfirmationRequired` from false to true for ten named Agentforce Standard actions (advisories published 2025-09-27, listed 2025-08-14/25 in the advisory archive); stated 2026-04-16 that confirmation is enabled by default for email-based agentic actions; and stated in September 2026 that default settings for certain Agentforce actions in Slack now require user confirmation. Escalation is a standard automatic topic-level action routed through an Omni Flow (Salesforce blog 2026-03-11). Custom actions: confirmation is recommended, not default. | 3/3 | https://help.salesforce.com/s/articleView?id=005133036&type=1 · https://help.salesforce.com/s/articleView?id=005132147&type=1 · https://venturebeat.com/security/microsoft-salesforce-copilot-agentforce-prompt-injection-cve-agent-remediation-playbook · https://www.securityweek.com/salesbleed-flaws-in-salesforce-agentforce-enabled-zero-click-data-exfiltration/ · https://www.salesforce.com/blog/agent-handoff/ |
| Permission delegation transparency | Scope + delegation targets documented. An agent operates as a Salesforce user (Einstein Agent license / Einstein Agent User profile) with assigned permission sets; the Salesforce Architects "Trust — Agentic Enterprise" guide documents the running user as the security boundary, subagent and action assignment as permission boundaries, Apex sharing modes, and System Administrator as running user as an anti-pattern. | 3/3 | https://trailhead.salesforce.com/content/learn/projects/build-an-agent-to-nurture-leads/create-a-user-record-for-your-agent · https://architect.salesforce.com/docs/architect/well-architected/guide/trust-agentic-patterns.html |

**Positive findings.** Confirmation defaults were tightened three times on the public record (September 2025, April 2026, September 2026); escalation to a human is a standard topic; the permission model is documented end-to-end.

**Recorded concerns.** Confirmation defaults apply to standard actions; custom actions and custom topics (sub-agents) rely on admin configuration. The SalesBleed "Reply to a Slack Thread" action required no confirmation and carried no invoking-user attribution until the September 2026 default change. No emergency-stop runbook was read.

### C — Containment · 6/10 · Mid

| Criterion | Result | Score | Evidence URL |
|---|---|---|---|
| Sandbox design | Whitelist-based. Agent output and callouts are confined by Trusted URLs enforcement (allowlist, enforced since 2025-09-08: unapproved URLs are blocked or redacted) and by topics/actions, where an action not assigned to the agent or subagent cannot be invoked. Salesforce's own guide states that anything listed is reachable through prompt manipulation and that instruction-only limits may be overridden by prompt injection — the topic-containment finding of the base record, re-verified on a vendor source. | 4/4 | https://www.technadu.com/?p=610626 · https://promptarmor.com/resources/one-key-way-salesforce-mitigates-ai-risk · https://architect.salesforce.com/docs/architect/well-architected/guide/trust-agentic-patterns.html · https://trailhead.salesforce.com/content/learn/modules/trusted-agentic-ai/explore-agentforce-guardrails-and-trust-patterns |
| Least privilege | Configurable. The agent's data access is that of its running user; least privilege is a documented recommendation (purpose-built integration users, minimal permission sets, field minimization) rather than a verified default profile scope. | 1/3 | https://architect.salesforce.com/docs/architect/well-architected/guide/trust-agentic-patterns.html |
| Tenant isolation (cloud) | Claimed but unverified. The Einstein Platform SPARC describes a multitenant architecture with logical separation by unique ID; the supporting SOC 2 and ISO reports are login-gated. No cross-tenant breach of Agentforce is on the public record. | 1/3 | https://www.salesforce.com/en-us/wp-content/uploads/sites/4/documents/legal/misc/einstein-platform-security-privacy-and-architecture.pdf · https://compliance.salesforce.com/en/documents/a00Kd00000zh1D6IAI |

**Positive findings.** Allowlist-based outbound URL control enforced org-wide; action and subagent assignment functions as a capability allowlist; platform-level object, field and record permissions bound what an agent can read.

**Recorded concerns.** The Trusted URLs allowlist was bypassed by unrecognised top-level domains and parsing-interfering characters (SalesBleed) and, in 2025, by an expired allowlisted domain (ForcedLeak). Least privilege depends on configuration. Isolation evidence is not publicly downloadable.

### T — Transparency · 7/10 · High

| Criterion | Result | Score | Evidence URL |
|---|---|---|---|
| CVE publication posture | Issues CVEs + advisories. Salesforce assigns CVEs as a CNA (security@salesforce.com) with vendor advisories (e.g. article 005228032 for the Vibes CVEs) and maintains an advisory archive (93 entries) including the two 2025 Agentforce confirmation advisories. | 2/2 | https://cve.circl.lu/vuln/fkie_cve-2025-64320 · https://security.salesforce.com/advisory-archives/ |
| Incident disclosure speed | >60 days / none vendor-initiated for the in-window vulnerabilities. No Salesforce advisory or bulletin for PipeLeak or SalesBleed was located in the advisory archive (most recent listed entry 2025-10-02), on security.salesforce.com, or in the Trust Status general-messages feed (15 current messages, read via operator input 2026-11-06 — none names PipeLeak, SalesBleed, ForcedLeak or Web-to-Lead); Salesforce's statements appeared in press coverage on the researchers' publication dates (2026-04-16; 2026-09-24/25), 115 days after the SalesBleed report. VentureBeat reported no public advisory for PipeLeak as of publication. | 0/2 | https://security.salesforce.com/advisory-archives/ · https://api.status.salesforce.com/v1/generalMessages · https://venturebeat.com/security/microsoft-salesforce-copilot-agentforce-prompt-injection-cve-agent-remediation-playbook · https://www.securityweek.com/salesbleed-flaws-in-salesforce-agentforce-enabled-zero-click-data-exfiltration/ |
| Security policy publication | Detailed technical + organizational measures: Einstein Platform Security, Privacy and Architecture document (2026-07-24) covering architecture, logging, incident management, backups, physical controls and sub-processor governance; DPA §6 security and audit clauses. | 2/2 | https://www.salesforce.com/en-us/wp-content/uploads/sites/4/documents/legal/misc/einstein-platform-security-privacy-and-architecture.pdf · https://www.salesforce.com/wp-content/uploads/sites/4/documents/legal/Agreements/data-processing-addendum.pdf |
| AI safety framework reference | External framework adopted: ISO/IEC 42001:2023 certification for "Salesforce AI Platform, Agentforce and Slack AI" (announced 2025-10-09; certificate record updated 2026-10-01, login-gated); an AI Acceptable Use Policy governs customer use. | 2/2 | https://www.salesforce.com/blog/salesforce-iso-42001-agentforce-certification/ · https://compliance.salesforce.com/en/documents/a00Kd00000z7GXZIA2 |
| AI system identity disclosure | Available via settings/patterns. Salesforce documents "transparency by design" disclosure of AI-generated content as a trust pattern and standard disclosure patterns for outbound content; the MIT AI Agent Index records that whether these are on by default is unclear. | 1/2 | https://trailhead.salesforce.com/content/learn/modules/trusted-agentic-ai/explore-agentforce-guardrails-and-trust-patterns · https://aiagentindex.mit.edu/2025/agentforce/ |

**Positive findings.** CNA status with per-CVE advisories; detailed SPARC documentation; ISO 42001 certification covering Agentforce; a public responsible-disclosure policy.

**Recorded concerns.** For the two in-window Agentforce vulnerability disclosures the public record contains press statements but no vendor advisory, while the same status feed carries same-week advisories for platform-level third-party CVEs (PHP, Brotli/Node.js, October 2026).

## Incident Timeline

No public CVEs were confirmed in the trailing 12 months (2025-11-06 → 2026-11-06) with Agentforce as the affected product.

| Date | Identifier | CVSS | Description | Patch status | KEV |
|---|---|---|---|---|---|
| 2026-10-30 | Trust Status 20000269 "Agentforce Feature Degradation" (operational, not a security incident) | — | Some Agentforce customers using third-party LLMs saw 4xx errors after a change by a third-party LLM service provider; 12:37Z → 18:06Z; message created 16:10Z, resolved same day. | Resolved; provider rolled back and applied a follow-up fix. | — |
| 2026-09-24 | SalesBleed (CVE-less advisory; Zenity Labs) | none of record | Three flaws: zero-click CRM exfiltration via Web-to-Lead prompt injection and Trusted URLs parsing weaknesses (DNS); the same via Slack link unfurling; agent-identity phishing via the "Reply to a Slack Thread" action without confirmation or attribution. Reported 2026-06-01. | Fixed — Trusted URLs bypass confirmed 2026-08-19; all three confirmed 2026-09-21; Slack action defaults changed to require confirmation. Salesforce: no evidence of customer exploitation. | No |
| 2026-04-15 | PipeLeak (CVE-less advisory; Capsule Security) | none of record | Indirect prompt injection via a public lead form; agent exfiltrated lead records by email through an authorized tool action. | Salesforce (2026-04-16): specific scenario remediated; HITL default for email-based actions. Capsule: email channel still exploitable on custom topics on retest. Report and fix dates not published. | No |
| 2025-11-04 | CVE-2025-64320 / -64321 / -64322 (out of product scope; outside window) | 6.5 / 5.3 / 5.3 (NVD v3.1) | Agentforce Vibes Extension (VS Code IDE extension) — LLM prompt neutralization and permission-assignment flaws, fixed in 3.2.0 / 3.3.0. Separate product; published two days before the window start. | Fixed (vendor advisory 005228032). | No |
| 2025-09-25 | ForcedLeak (CVE-less advisory; Noma Security) — outside window | 9.4 (researcher CVSS v4.0; not a CVSS of record) | Indirect prompt injection via Web-to-Lead Description field; exfiltration through an image tag to an expired CSP-allowlisted domain (my-salesforce-cms.com, purchased for USD 5). Reported 2025-07-28; acknowledged 2025-07-31. | Trusted URLs enforcement 2025-09-08 (42 days); expired domain re-secured. | No |
| 2025-08-14 / 2025-08-25 (listed) | Salesforce advisories 005132147 / 005133036 — outside window | — | `isConfirmationRequired` set to true for ten Agentforce Standard actions "to better protect customers against prompt injection risks"; "Our platform has not been compromised." | Applied | — |

## Contextual Analysis

Evidence rule for this report: every factual claim is tied to a URL retrieved during the evaluation session; where a page could not be rendered by the session tools it is listed as unread in the Differential section rather than scored as silence.

Agentforce's public vulnerability record over the last fourteen months consists of three researcher publications rather than vendor CVEs. The structure is the same in each: an untrusted external input (a Web-to-Lead submission) is stored as a CRM record, an employee or an automation later asks an agent to process it, the agent follows the embedded instructions, and data leaves through a channel the agent is permitted to use — an image URL, an email action, a DNS lookup, a Slack link preview. Salesforce's position, stated consistently since 2025, is that prompt injection is an industry-wide challenge addressed through layered safeguards: Trusted URLs enforcement (September 2025), confirmation-by-default for standard sensitive actions (September 2025), confirmation defaults for email actions (stated April 2026) and for Slack actions (September 2026), instruction isolation and tool-use restrictions. The data shows each disclosure was followed by a control change, and that each subsequent researcher found a route around the previous control. VERDICT records the sequence and the elapsed times; it does not attribute intent.

The absence of CVEs is a product of Salesforce's disclosure practice for hosted-service fixes rather than an absence of vulnerabilities: The Register reported that no CVE was issued for ForcedLeak because it did not involve a customer software upgrade, and neither PipeLeak nor SalesBleed has a CVE. Under the framework, CVE-less advisories do not enter `cve_count_12mo` or `max_cvss_12mo`, which is why R rises from 8 to 14 in this update even as the structural-issue and patch-speed criteria score zero. Readers comparing Agentforce with platforms that issue CVEs for comparable findings should weigh this difference in disclosure practice.

The Capsule Security dispute is recorded without adjudication: Salesforce stated on 2026-04-16 that the specific PipeLeak scenario was remediated and that email actions carry a default confirmation; Capsule stated that custom topics (sub-agents) remained exploitable on retest. Both statements are on the public record and neither has been superseded by a later public statement located in this session.

On data conduct, two findings are stable across vendor sources: Salesforce does not use Customer Data to train generative models and holds zero-data-retention terms with LLM providers; and Einstein Trust Layer data masking is disabled for Agentforce agents, a design choice Salesforce attributes to latency, planner disruption and accuracy. Salesforce's own architecture guidance tells customers not to assume masking protects PII in agent prompts. The Trust Layer's audit and feedback data model requires Data 360 and stores requests, responses and quality scores there; no retention period for that data was found.

Operator of record: Salesforce, Inc. (Delaware), confirmed on the Main Services Agreement (§12.9) and the FY2026 Form 10-K; the base record's operator string is confirmed and `independence` is recorded as `independent` (no controlling shareholder; publicly listed, NYSE: CRM). FedRAMP: Salesforce announced on 2025-06-04 that Agentforce "achieved FedRAMP High authorization"; the FedRAMP Marketplace entry FR2003061248 is Salesforce Government Cloud Plus (Class D / High, JAB path) and does not list Agentforce by name. The Salesforce Help article "Government Cloud Available Products and Features" (000396813, 2026-10-07; read via operator input) lists "Agentforce (Customer & Employee Agents)" as Authorized within the Government Cloud Plus FedRAMP High / DoD IL2 boundary and as not authorized for Government Cloud Plus – Defense (DoD IL5), with Salesforce's own disclaimer that specific features of an included product may or may not fall within the boundary. The per-product statement is therefore confirmed on a vendor page; the non-vendor marketplace record names only the environment.

Product-level integration note (not a disclosure trigger): Agentforce routes prompts to third-party models including OpenAI (US, with Azure failover), Microsoft Azure, Google and models hosted on AWS; Salesforce stated in June 2025 that Anthropic Claude models are hosted within the Salesforce trust boundary via Amazon Bedrock, and the MIT AI Agent Index lists Anthropic among supported model providers. A model-provider relationship is the premise of VERDICT and is not itself a conflict (ENGINE.md non-trigger list). Disclosure Triggers 0–3: none fire. Salesforce is not in the material Anthropic equity-holder set; no member of that set holds a recorded board seat, lead/strategic designation or USD 100 million position in Salesforce, Inc.; distribution on hyperscaler marketplaces is industry-standard.

## VERDICT Record

**Summary.** Salesforce Agentforce scores 59/85 (Tier A), up one point from 58: no CVE or supply chain compromise in the window, a documented recurring prompt-injection-to-exfiltration pattern with multi-month fix confirmation, closed source and login-gated audit reports, and a DPA, dated sub-processor list and ISO 42001 certification on the positive side.

**Risk Factor Summary by Use Case**

| Use case | Recorded factors |
|---|---|
| Internal testing | Platform enabled by default in Winter '27 orgs with Agentforce access; individual agents activated per agent; data masking disabled for agents; Trust Layer audit data requires Data 360. |
| Credential-handling workflows | Three published chains show agent output channels (URL, email, DNS, Slack unfurl) used for exfiltration; confirmation defaults cover standard actions, custom actions are admin-configured; Trusted URLs allowlist bypassed twice on the public record. |
| Cloud multi-tenant deployment | Multitenant logical separation claimed in the SPARC; SOC 2 / ISO 27001 / ISO 42001 evidence login-gated; no cross-tenant incident on record. |
| Regulated-data workloads | DPA with SCCs/BCRs, no-training statement, zero-data-retention LLM terms, ISO 42001; data masking disabled for agents; aggregated anonymized use stated without opt-out; FedRAMP High: Agentforce (Customer & Employee Agents) listed by Salesforce as Authorized within the Government Cloud Plus boundary (not DoD IL5); the marketplace record names the environment only. |

**Reference Information (options, not instructions)**

1. Organizations may review which Web-to-Lead and other external-input records their agents can read, and whether Trusted URLs and CSP `img-src` settings are limited to required domains.
2. Organizations may compare the default-confirmation list of standard actions against their custom actions and sub-agent topics, since Salesforce's own guidance treats instruction-only limits as overridable.
3. Organizations handling regulated data may request the login-gated SOC 2 and ISO reports through the compliance portal and confirm, per Salesforce's boundary disclaimer, which Agentforce features fall inside the Government Cloud Plus boundary for their edition.

**Bias Disclosure**

"This evaluation uses Claude (Anthropic) as its tooling. Anthropic operates in the AI agent market and may compete with some evaluated vendors. VERDICT discloses this relationship in every report and applies identical evaluation criteria to all platforms regardless of their relationship to Anthropic."

## Evaluation History

| Date | Type | Score | Tier | Framework |
|---|---|---|---|---|
| 2026-03-25 | Initial (migrated capture) | 58/85 | A | v0.3.1 |
| 2026-11-06 | Update (differential, full re-evaluation; run 2 with operator input) | 59/85 | A | v0.3.2 |

## Future Evaluation Plan

- Layer 1 (behavioral testing): not scheduled; Agentforce offers no public free tier that permits 30-run × 4-level testing without vendor-provided trial access (Absolute Rule 2).
- Layer C: routine review 365 days from `updated_at` (pipeline-derived `next_review_due`); interrupt lane active for T1–T6. Watch items: any CVE assignment for Agentforce-scoped findings; vendor advisory publication for SalesBleed/PipeLeak; the still-unread Salesforce Help article "Data Masking and Agents".
- Dormancy test: not applicable — Winter '27 release GA 2026-10-12 and release-note entries through November 2026.

---

**Score tag line:** `V13 R14 D11 I8 C6 T7 = 59/85 · Tier A · prev 58 · cve_count_12mo 0 (exact) · max_cvss_12mo null · KEV none · supply_chain false`
Dimension sum check: 13 + 14 + 11 + 8 + 6 + 7 = 59 ✔
