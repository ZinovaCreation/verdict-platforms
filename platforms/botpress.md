---
name: Botpress
slug: botpress
operator: Botpress Inc. · Montreal, Canada
independence: unrecorded
parent_entity: null
category: Chatbot / Agent Builder · Open Source (MIT integrations)
homepage: null
github: null
evaluation_number: 18
evaluation_type: initial
evaluated_at: '2026-03-25'
evaluator_model: unrecorded
framework_version: v0.3.1
layer: '0'
target_version: null
previous_evaluation_date: null
previous_score: null
score: 45
max_score: 85
tier: B
verdict:
  v:
    score: 12
    note: ''
  e:
    score: null
    note: null
  r:
    score: 14
    note: ''
  d:
    score: 7
    note: ''
  i:
    score: 5
    note: ''
  c:
    score: 2
    note: ''
  t:
    score: 5
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
next_review_due: '2026-06-23'
tags: []
rank: null
sources: []
og_description: 'Independent security evaluation of Botpress. Score: 45/85. No documented sandbox for plugin execution. SOC 2 certified. Open-source chatbot and agent framework. Framework v0.3.1.'
category_line: Chatbot / Agent Builder · Open Source (MIT integrations)
display_tags: &id001
- text: 0 CVEs · Trailing 12 Months
  color: amber
- text: SOC 2 Certified · GDPR Confirmed
  color: amber
- text: No Sandbox · Execute Cards In-Process
  color: dim
- text: 'HITL: Team/Enterprise Plans Only'
  color: dim
finding: Zero CVEs in trailing 12-month window. SOC 2 certified and GDPR compliant. Execute cards run without confirmed sandbox. AI training non-use stated in community channel only. HITL on Team/Enterprise plans only.
meta_description: 'Independent security evaluation of Botpress. Score: 45/85. No documented sandbox for plugin execution. SOC 2 certified. Open-source chatbot and agent framework. Framework v0.3.1.'
key_finding: Zero CVEs confirmed in the trailing 12-month window. SOC 2 certified and GDPR compliant. Execute cards (custom JavaScript) run without a confirmed platform-enforced sandbox — pre-window CVE-2024-28234 (RCE via hook execution in v12) documents this architectural surface. AI training non-use policy stated in community channel only, not in a published policy page. Sub-processors list not public. HITL available on Team/Enterprise plans only.
card_owner: Botpress Inc. · Montreal, Canada
card_category: Chatbot / Agent Builder · Open Source (MIT integrations)
card_tags: *id001
---
# Botpress

Zero CVEs confirmed in the trailing 12-month window. SOC 2 certified and GDPR compliant. Execute cards (custom JavaScript) run without a confirmed platform-enforced sandbox — pre-window CVE-2024-28234 (RCE via hook execution in v12) documents this architectural surface. AI training non-use policy stated in community channel only, not in a published policy page. Sub-processors list not public. HITL available on Team/Enterprise plans only.

## Layer 0 Score: 45/85 (Tier B)

**V** 12/20 · **R** 14/20 · **D** 7/15 · **I** 5/10 · **C** 2/10 · **T** 5/10

## CISA KEV

該当なし — no Botpress packages appear in the CISA Known Exploited Vulnerabilities catalog. Zero published CVEs attributed to Botpress in the trailing 12 months (captured).

## Bias Disclosure

This evaluation uses Claude (Anthropic) as its tooling. Anthropic operates in the AI agent market and may compete with some evaluated vendors. VERDICT discloses this relationship in every report and applies identical evaluation criteria to all platforms regardless of their relationship to Anthropic.

## Full Evaluation

See evaluations/ for the complete Layer 0 report.
