---
name: Browserbase
slug: browserbase
operator: Browserbase Inc. · Y Combinator S24 · $67.5M
independence: independent
parent_entity: null
category: Browser Infrastructure · Cloud (Proprietary)
homepage: https://docs.browserbase.com
github: https://github.com/browserbase
evaluation_number: 52
evaluation_type: initial
evaluated_at: '2026-04-07'
evaluator_model: unrecorded
framework_version: v0.3.1
layer: '0'
target_version: Browserbase Cloud (current production); Stagehand SDK 3.x
previous_evaluation_date: null
previous_score: null
score: 58
max_score: 85
tier: A
verdict:
  v:
    score: 12
    rating: Mid
    note: ''
  e:
    score: null
    rating: null
    note: null
  r:
    score: 20
    rating: High
    note: ''
  d:
    score: 9
    rating: Mid
    note: ''
  i:
    score: 8
    rating: High
    note: ''
  c:
    score: 6
    rating: Mid
    note: ''
  t:
    score: 3
    rating: Low
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
next_review_due: '2026-07-06'
tags:
- browser-agent-infrastructure
- cloud-saas
- headless-browser
- ycombinator-s24
- soc2-type2
- hipaa
- zero-trust-isolation
- vm-per-session
- gdpr-ready
- stagehand-oss
- mit-license
- sso-saml
- byo-llm
- multi-region
- zero-data-retention-option
- no-training-on-data
- 1password-integration
rank: null
sources:
- https://docs.browserbase.com/
- https://github.com/browserbase/stagehand
- https://github.com/browserbase/stagehand/releases
- https://github.com/browserbase/stagehand/security
- https://trust.browserbase.com/
- https://www.browserbase.com/privacy-policy
- https://www.browserbase.com/terms-of-service
og_description: VERDICT independent evaluation of Browserbase. Score 58/85.
category_line: Browser Infrastructure · Cloud (Proprietary)
display_tags: &id001
- text: 'R: 20/20 · VM-Per-Session Isolation'
  color: safe
- text: SOC 2 II · HIPAA BAA · No Training
  color: safe
- text: 'Trust Center Gated · T: 3/10'
  color: amber
finding: ''
meta_owner: Browserbase, Inc. (US, independent, Series B $300M valuation)
meta_description: 'Browserbase: VERDICT score 58/85. R: 20/20 · VM-Per-Session Isolation. Browserbase Inc. · Y Combinator S24 · $67.5M.'
key_finding: 'First perfect R: 20/20 in the index. One VM per browser session, destroyed after each use. SOC 2 Type II, HIPAA BAA, third-party pen testing. Explicit no-training commitment on all browser data. Trust Center gated.'
card_owner: Browserbase Inc. · Y Combinator S24 · $67.5M
card_category: Browser Infrastructure · Cloud (Proprietary)
card_tags: *id001
---
# Browserbase

First perfect R: 20/20 in the index. One VM per browser session, destroyed after each use. SOC 2 Type II, HIPAA BAA, third-party pen testing. Explicit no-training commitment on all browser data. Trust Center gated.

## Layer 0 Score: 58/85 (Tier A)

**V** 12/20 · **R** 20/20 · **D** 9/15 · **I** 8/10 · **C** 6/10 · **T** 3/10

## CISA KEV

該当なし — no Browserbase packages appear in the CISA Known Exploited Vulnerabilities catalog. Zero published CVEs attributed to Browserbase in the trailing 12 months (captured).

## Bias Disclosure

This evaluation uses Claude (Anthropic) as its tooling. Anthropic operates in the AI agent market and may compete with some evaluated vendors. VERDICT discloses this relationship in every report and applies identical evaluation criteria to all platforms regardless of their relationship to Anthropic.

## Full Evaluation

See evaluations/ for the complete Layer 0 report.
