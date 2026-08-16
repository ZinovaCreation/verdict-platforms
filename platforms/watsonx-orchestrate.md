---
name: IBM watsonx Orchestrate
slug: watsonx-orchestrate
operator: IBM Corporation
independence: independent
parent_entity: null
category: Enterprise AI Agent Platform · Cloud SaaS + On-Prem
homepage: null
github: null
evaluation_number: 21
evaluation_type: initial
evaluated_at: '2026-03-30'
evaluator_model: unrecorded
framework_version: v0.3.1
layer: '0'
target_version: watsonx Orchestrate SaaS (current) / Cartridge 5.3.x / Developer Edition 2.3.0
previous_evaluation_date: null
previous_score: null
score: 48
max_score: 85
tier: B
verdict:
  v:
    score: 11
    rating: null
    note: ''
  e:
    score: null
    rating: null
    note: null
  r:
    score: 7
    rating: null
    note: ''
  d:
    score: 9
    rating: null
    note: ''
  i:
    score: 7
    rating: null
    note: ''
  c:
    score: 6
    rating: null
    note: ''
  t:
    score: 8
    rating: null
    note: ''
cisa_kev:
  present: false
  entries: []
cve_count_12mo: 10
cve_count_basis: lower_bound
max_cvss_12mo: 9.1
supply_chain_compromise_12mo: false
known_facts_applied: []
qa:
  factual: unresolved
  legal: unresolved
  quality: unresolved
  revision_cycles: 0
  flagged: false
differential: null
next_review_due: '2026-06-28'
tags:
- enterprise
- closed-source
- IBM-cloud
- FedRAMP
- SOC2
- multi-agent
- governance
- hybrid-deploy
- subscription
rank: null
sources: []
og_description: 'Independent security evaluation of IBM watsonx Orchestrate. Score: 48/85. FedRAMP authorized, SOC 2 certified. 10+ CVEs including CVSS 9.1. Langflow (CISA KEV) integrated. Framework v0.3.1.'
category_line: Enterprise AI Agent Platform · Cloud SaaS + On-Prem
display_tags: &id001
- text: 10+ CVEs · CVSS 9.1
  color: red
- text: CVE-2025-0165 · SQL Injection
  color: red
- text: Langflow · CISA KEV Portfolio
  color: amber
finding: 'Enterprise-grade compliance infrastructure: FedRAMP authorized, SOC 2, ISO 27001. Client data explicitly not used for IBM model training. However, 10+ dependency CVEs in the trailing 12 months (including CVSS 9.1) and one IBM-specific SQL injection (CVE-2025-0165). Langflow (CISA KEV listed, 30/85) now integrated via DataStax acquisition.'
meta_owner: IBM
meta_description: 'Independent security evaluation of IBM watsonx Orchestrate. Score: 48/85. FedRAMP authorized, SOC 2 certified. 10+ CVEs including CVSS 9.1. Langflow (CISA KEV) integrated. Framework v0.3.1.'
key_finding: FedRAMP authorized, SOC 2, ISO 27001. Client data explicitly not used for IBM model training. 10+ dependency CVEs including CVSS 9.1, plus IBM-specific SQL injection (CVE-2025-0165). Langflow (CISA KEV, 30/85) integrated via DataStax acquisition.
card_owner: IBM Corporation
card_category: Enterprise AI Agent Platform · Cloud SaaS + On-Prem
card_tags: *id001
---
# IBM watsonx Orchestrate

FedRAMP authorized, SOC 2, ISO 27001. Client data explicitly not used for IBM model training. 10+ dependency CVEs including CVSS 9.1, plus IBM-specific SQL injection (CVE-2025-0165). Langflow (CISA KEV, 30/85) integrated via DataStax acquisition.

## Layer 0 Score: 48/85 (Tier B)

**V** 11/20 · **R** 7/20 · **D** 9/15 · **I** 7/10 · **C** 6/10 · **T** 8/10

## CISA KEV

該当なし — no IBM watsonx Orchestrate packages appear in the CISA Known Exploited Vulnerabilities catalog. At least 10 published CVEs in the trailing 12 months (published as a bound; basis: lower_bound).

## Bias Disclosure

This evaluation uses Claude (Anthropic) as its tooling. Anthropic operates in the AI agent market and may compete with some evaluated vendors. VERDICT discloses this relationship in every report and applies identical evaluation criteria to all platforms regardless of their relationship to Anthropic.

## Full Evaluation

See evaluations/ for the complete Layer 0 report.
