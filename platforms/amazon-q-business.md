---
name: Amazon Q Business
slug: amazon-q-business
operator: Amazon Web Services
independence: independent
parent_entity: null
category: Enterprise AI Assistant · Cloud SaaS (AWS)
homepage: null
github: null
evaluation_number: 26
evaluation_type: initial
evaluated_at: '2026-03-30'
evaluator_model: unrecorded
framework_version: v0.3.1
layer: '0'
target_version: Generally Available (managed SaaS; no discrete version number)
previous_evaluation_date: null
previous_score: null
score: 68
max_score: 85
tier: S
verdict:
  v:
    score: 14
    rating: High
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
    score: 13
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
    score: 9
    rating: High
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
next_review_due: '2026-06-28'
tags:
- enterprise-ai
- managed-saas
- aws
- rag
- iam
- soc2
- iso27001
- fedramp
- hipaa
- iso42001
- cmek
- vpc-privatelink
rank: 2
sources:
- https://aws.amazon.com/contact-us/
og_description: 'Independent security evaluation of Amazon Q Business. Score: 68/85 — highest in the VERDICT index. SOC 1/2/3, ISO 27001, ISO 42001, FedRAMP, HIPAA. Zero CVEs. Framework v0.3.1.'
category_line: Enterprise AI Assistant · Cloud SaaS (AWS)
display_tags: &id001
- text: SOC 1/2/3 · ISO 27001 · FedRAMP
  color: dim
- text: ISO 42001 · First Cloud Provider
  color: dim
- text: Q Developer CVE · Sibling Product
  color: amber
finding: 'Highest score in the VERDICT index. SOC 1/2/3, ISO 27001, ISO 42001 (first major cloud provider), FedRAMP, HIPAA BAA, PCI DSS. Customer data explicitly not used for model training. Zero CVEs for Q Business. Sibling product Q Developer experienced a supply chain compromise (CVE-2025-8217). Enhanced bias disclosure: Amazon is a major investor in Anthropic.'
meta_owner: AWS (Amazon)
meta_description: 'Independent security evaluation of Amazon Q Business. Score: 68/85 — highest in the VERDICT index. SOC 1/2/3, ISO 27001, ISO 42001, FedRAMP, HIPAA. Zero CVEs. Framework v0.3.1.'
key_finding: 'Highest score in the index. SOC 1/2/3, ISO 27001, ISO 42001, FedRAMP, HIPAA. Customer data not used for model training. Zero CVEs. Enhanced bias disclosure: Amazon is Anthropic''s major investor.'
card_owner: Amazon Web Services
card_category: Enterprise AI Assistant · Cloud SaaS (AWS)
card_tags: *id001
---
# Amazon Q Business

Highest score in the index. SOC 1/2/3, ISO 27001, ISO 42001, FedRAMP, HIPAA. Customer data not used for model training. Zero CVEs. Enhanced bias disclosure: Amazon is Anthropic's major investor.

## Layer 0 Score: 68/85 (Tier S)

**V** 14/20 · **R** 20/20 · **D** 13/15 · **I** 6/10 · **C** 6/10 · **T** 9/10

## CISA KEV

該当なし — no Amazon Q Business packages appear in the CISA Known Exploited Vulnerabilities catalog. Zero published CVEs attributed to Amazon Q Business in the trailing 12 months (captured).

## Bias Disclosure

This evaluation uses Claude (Anthropic) as its tooling. Anthropic operates in the AI agent market and may compete with some evaluated vendors. VERDICT discloses this relationship in every report and applies identical evaluation criteria to all platforms regardless of their relationship to Anthropic.

## Full Evaluation

See evaluations/ for the complete Layer 0 report.
