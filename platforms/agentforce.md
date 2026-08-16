---
name: Salesforce Agentforce
slug: agentforce
operator: 'Salesforce, Inc. (NYSE: CRM)'
independence: unrecorded
parent_entity: null
category: CRM-Native Agent Builder · Enterprise SaaS
homepage: null
github: null
evaluation_number: 20
evaluation_type: initial
evaluated_at: '2026-03-25'
evaluator_model: unrecorded
framework_version: v0.3.1
layer: '0'
target_version: null
previous_evaluation_date: null
previous_score: null
score: 58
max_score: 85
tier: A
verdict:
  v:
    score: 16
    note: ''
  e:
    score: null
    note: null
  r:
    score: 8
    note: ''
  d:
    score: 13
    note: ''
  i:
    score: 8
    note: ''
  c:
    score: 6
    note: ''
  t:
    score: 7
    note: ''
cisa_kev:
  present: false
  entries: []
cve_count_12mo: 1
cve_count_basis: exact
max_cvss_12mo: 9.4
supply_chain_compromise_12mo: false
known_facts_applied: []
qa:
  factual: unresolved
  legal: unresolved
  quality: unresolved
  revision_cycles: 0
  flagged: false
differential: null
next_review_due: '2026-06-23'
tags: []
rank: null
sources: []
og_description: 'Independent security evaluation of Salesforce Agentforce. Score: 58/85. ForcedLeak vulnerability (CVSS 9.4), 42-day patch window. Strong compliance documentation. Framework v0.3.1.'
category_line: CRM-Native Agent Builder · Enterprise SaaS
display_tags: &id001
- text: ForcedLeak · CVSS 9.4 · 42-Day Patch
  color: red
- text: Topic Containment Bypass · Model-Guidance Only
  color: red
- text: FedRAMP High · SOC2 · HIPAA BAA · ISO27001
  color: amber
- text: Data Masking Disabled · Autonomous Workflows
  color: warn
finding: 'FedRAMP High explicitly confirmed for Agentforce (Jun 2025) — first AI agent platform with FedRAMP High for the product itself. Native OLS/FLS platform-layer permission enforcement: strongest least-privilege architecture in this index. ForcedLeak (CVSS 9.4, Sep 2025): indirect prompt injection via Web-to-Lead form, 42-day patch window. Topic containment confirmed bypassable. Data masking disabled for autonomous agent workflows.'
meta_description: 'Independent security evaluation of Salesforce Agentforce. Score: 58/85. ForcedLeak vulnerability (CVSS 9.4), 42-day patch window. Strong compliance documentation. Framework v0.3.1.'
key_finding: 'FedRAMP High explicitly confirmed for Agentforce (Jun 2025) — first AI agent platform in this index with FedRAMP High for the product itself. Native OLS/FLS platform-layer permission enforcement: strongest least-privilege architecture in this index. Escalation Topic pre-built for HITL. ForcedLeak (CVSS 9.4, Sep 2025): indirect prompt injection via Web-to-Lead form, expired CSP domain ($5 to purchase), 42-day patch window. Topic containment confirmed bypassable at model-guidance layer. Einstein Trust Layer data masking disabled for autonomous agent workflows.'
card_owner: 'Salesforce, Inc. (NYSE: CRM)'
card_category: CRM-Native Agent Builder · Enterprise SaaS
card_tags: *id001
---
# Salesforce Agentforce

FedRAMP High explicitly confirmed for Agentforce (Jun 2025) — first AI agent platform in this index with FedRAMP High for the product itself. Native OLS/FLS platform-layer permission enforcement: strongest least-privilege architecture in this index. Escalation Topic pre-built for HITL. ForcedLeak (CVSS 9.4, Sep 2025): indirect prompt injection via Web-to-Lead form, expired CSP domain ($5 to purchase), 42-day patch window. Topic containment confirmed bypassable at model-guidance layer. Einstein Trust Layer data masking disabled for autonomous agent workflows.

## Layer 0 Score: 58/85 (Tier A)

**V** 16/20 · **R** 8/20 · **D** 13/15 · **I** 8/10 · **C** 6/10 · **T** 7/10

## CISA KEV

該当なし — no Salesforce Agentforce packages appear in the CISA Known Exploited Vulnerabilities catalog. 1 published CVE(s) attributed to Salesforce Agentforce in the trailing 12 months (captured).

## Bias Disclosure

This evaluation uses Claude (Anthropic) as its tooling. Anthropic operates in the AI agent market and may compete with some evaluated vendors. VERDICT discloses this relationship in every report and applies identical evaluation criteria to all platforms regardless of their relationship to Anthropic.

## Full Evaluation

See evaluations/ for the complete Layer 0 report.
