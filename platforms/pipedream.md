---
name: Pipedream
slug: pipedream
operator: Acquired by Workday (Dec 2025)
independence: unrecorded
parent_entity: null
category: Workflow Automation · API Integration
homepage: null
github: null
evaluation_number: 6
evaluation_type: initial
evaluated_at: '2026-03-13'
evaluator_model: unrecorded
framework_version: v0.3.1
layer: '0'
target_version: null
previous_evaluation_date: null
previous_score: null
score: 56
max_score: 85
tier: A
verdict:
  v:
    score: 11
    note: ''
  e:
    score: null
    note: null
  r:
    score: 16
    note: ''
  d:
    score: 12
    note: ''
  i:
    score: 5
    note: ''
  c:
    score: 8
    note: ''
  t:
    score: 4
    note: ''
cisa_kev:
  present: false
  entries: []
cve_count_12mo: 0
cve_count_basis: exact
max_cvss_12mo: null
supply_chain_compromise_12mo: false
known_facts_applied: []
qa:
  factual: unresolved
  legal: unresolved
  quality: unresolved
  revision_cycles: 0
  flagged: false
differential: null
next_review_due: '2026-06-11'
tags: []
rank: null
sources: []
og_description: 'Independent security evaluation of Pipedream. Score: 56/85. VM-isolated sandbox with zero public CVEs — strongest containment in the VERDICT index. Acquired by Workday. Framework v0.3.1.'
category_line: Workflow Automation · API Integration
display_tags: &id001
- text: 0 Public CVEs
  color: dim
- text: VM Isolation · Best Sandbox
  color: amber
- text: SMB Roadmap Risk (Workday)
  color: warn
finding: 'Most certifications of any evaluated platform — SOC2, HIPAA, GDPR, ISO27001, PCI DSS, FedRAMP. VM-isolated sandbox means n8n&#x27;s SSRF problem structurally cannot occur. But independence is gone: Workday now controls the roadmap.'
meta_description: 'Independent security evaluation of Pipedream. Score: 56/85. VM-isolated sandbox with zero public CVEs — strongest containment in the VERDICT index. Acquired by Workday. Framework v0.3.1.'
key_finding: 'Most certifications of any evaluated platform — SOC2, HIPAA, GDPR, ISO27001, PCI DSS, FedRAMP. VM-isolated sandbox means n8n''s SSRF problem structurally cannot occur. But independence is gone: Workday now controls the roadmap.'
card_owner: Acquired by Workday (Dec 2025)
card_category: Workflow Automation · API Integration
card_tags: *id001
---
# Pipedream

Most certifications of any evaluated platform — SOC2, HIPAA, GDPR, ISO27001, PCI DSS, FedRAMP. VM-isolated sandbox means n8n's SSRF problem structurally cannot occur. But independence is gone: Workday now controls the roadmap.

## Layer 0 Score: 56/85 (Tier A)

**V** 11/20 · **R** 16/20 · **D** 12/15 · **I** 5/10 · **C** 8/10 · **T** 4/10

## CISA KEV

該当なし — no Pipedream packages appear in the CISA Known Exploited Vulnerabilities catalog. Zero published CVEs attributed to Pipedream in the trailing 12 months (captured).

## Bias Disclosure

This evaluation uses Claude (Anthropic) as its tooling. Anthropic operates in the AI agent market and may compete with some evaluated vendors. VERDICT discloses this relationship in every report and applies identical evaluation criteria to all platforms regardless of their relationship to Anthropic.

## Full Evaluation

See evaluations/ for the complete Layer 0 report.
