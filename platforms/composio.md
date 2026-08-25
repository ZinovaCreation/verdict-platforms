---
name: Composio
slug: composio
operator: Composio Inc. · San Francisco
independence: independent
parent_entity: null
category: AI Agent Tool Integration · OSS SDK + Cloud
homepage: https://composio.dev
github: https://github.com/ComposioHQ
evaluation_number: 25
evaluation_type: initial
evaluated_at: '2026-03-30'
evaluator_model: unrecorded
framework_version: v0.3.1
layer: '0'
target_version: Composio (composio PyPI package, latest; composio.dev cloud platform)
previous_evaluation_date: null
previous_score: null
score: 46
max_score: 85
tier: B
verdict:
  v:
    score: 10
    rating: Mid
    note: ''
  e:
    score: null
    rating: null
    note: null
  r:
    score: 8
    rating: Mid
    note: ''
  d:
    score: 10
    rating: Mid
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
    score: 6
    rating: Mid
    note: ''
cisa_kev:
  present: false
  entries: []
cve_count_12mo: 1
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
next_review_due: '2026-06-28'
tags:
- open-source-sdk
- cloud-SaaS
- SOC2
- ISO27001
- managed-auth
- credential-isolation
- tool-integration
- YC-backed
rank: 37
sources:
- https://composio.dev/
- https://composio.dev/enterprise
- https://composio.dev/privacy
- https://github.com/ComposioHQ/composio
- https://github.com/ComposioHQ/composio/releases
og_description: 'Independent security evaluation of Composio. Score: 46/85. SOC 2 + ISO 27001. Credential isolation architecture. Recurring eval() CVE pattern. Vendor non-response to disclosure. Framework v0.3.1.'
category_line: AI Agent Tool Integration · OSS SDK + Cloud
display_tags: &id001
- text: CVE-2025-56427 · Dir Traversal
  color: red
- text: eval() Injection · Recurring
  color: red
- text: Vendor Non-Response
  color: amber
finding: SOC 2 Type II + ISO 27001:2022 dual certification. Credentials never reach agent context — architectural isolation. Published DPA with sub-processor list. Recurring eval() code injection pattern (CVE-2024-8864/8953). Directory traversal CVE-2025-56427 in SDK. Vendor documented as non-responsive to disclosure.
meta_owner: Composio Inc.
meta_description: 'Independent security evaluation of Composio. Score: 46/85. SOC 2 + ISO 27001. Credential isolation architecture. Recurring eval() CVE pattern. Vendor non-response to disclosure. Framework v0.3.1.'
key_finding: SOC 2 + ISO 27001. Credentials never reach agent context. Recurring eval() code injection pattern. Directory traversal CVE-2025-56427. Vendor non-responsive to security disclosure.
card_owner: Composio Inc. · San Francisco
card_category: AI Agent Tool Integration · OSS SDK + Cloud
card_tags: *id001
---
# Composio

SOC 2 + ISO 27001. Credentials never reach agent context. Recurring eval() code injection pattern. Directory traversal CVE-2025-56427. Vendor non-responsive to security disclosure.

## Layer 0 Score: 46/85 (Tier B)

**V** 10/20 · **R** 8/20 · **D** 10/15 · **I** 6/10 · **C** 6/10 · **T** 6/10

## CISA KEV

該当なし — no Composio packages appear in the CISA Known Exploited Vulnerabilities catalog. 1 published CVE(s) attributed to Composio in the trailing 12 months (captured).

## Bias Disclosure

This evaluation uses Claude (Anthropic) as its tooling. Anthropic operates in the AI agent market and may compete with some evaluated vendors. VERDICT discloses this relationship in every report and applies identical evaluation criteria to all platforms regardless of their relationship to Anthropic.

## Full Evaluation

See evaluations/ for the complete Layer 0 report.
