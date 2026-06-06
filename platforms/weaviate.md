---
name: Weaviate
slug: weaviate
operator: Weaviate B.V.
independence: independent
parent_entity: null
category: Vector Database
homepage: https://weaviate.io
github: https://github.com/weaviate/weaviate
evaluation_number: 65
evaluation_type: initial
evaluated_at: '2026-05-15'
evaluator_model: unrecorded
framework_version: v0.3.1-final
layer: '0'
target_version: Weaviate Database 1.33.x / 1.34.0
previous_evaluation_date: null
previous_score: null
score: 62
max_score: 85
tier: A
verdict:
  v:
    score: 16
    rating: High
    note: ''
  r:
    score: 14
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
    score: 7
    rating: High
    note: ''
  e:
    score: null
    rating: null
    note: null
cisa_kev:
  present: false
  entries: []
cve_count_12mo: 2
max_cvss_12mo: 8.7
supply_chain_compromise_12mo: false
known_facts_applied: []
qa:
  factual: pass
  legal: pass
  quality: pass
  revision_cycles: 0
  flagged: false
differential: null
next_review_due: '2026-08-13'
tags:
- vector-database
- weaviate
- bsd-3-clause
- oss
- gdpr
- soc2-type2
- iso27001-2022
- hipaa-dedicated
- rbac
- oidc
- multi-tenancy
- byoc
- weaviate-cloud
sources:
- https://weaviate.io/
- https://docs.weaviate.io
- https://github.com/weaviate/weaviate
- https://weaviate.io/subprocessors
- https://trust.weaviate.io
- https://weaviate.io/privacy
- https://weaviate.io/blog/weaviate-iso-compliant
rank: null
---

# Weaviate

<!-- TODO(Zinova): overview paragraph + Strongest signals / Largest gaps — to be authored from evaluations/065_weaviate.md (display copy fields finding/meta_owner/meta_description/og_description/category_line/display_tags also pending in frontmatter). -->

## Layer 0 Score: 62/85 (Tier A)

**V** 16/20 · **R** 14/20 · **D** 13/15 · **I** 6/10 · **C** 6/10 · **T** 7/10

## Bias Disclosure

This evaluation uses Claude (Anthropic) as its tooling. Anthropic operates in the AI agent market and may compete with some evaluated vendors. VERDICT discloses this relationship in every report and applies identical evaluation criteria to all platforms regardless of their relationship to Anthropic.

Specific to this evaluation: Weaviate ships a `generative-anthropic` module enabling RAG with Anthropic Claude models, default-enabled on Weaviate Cloud instances. The integration uses customer-supplied Anthropic API keys (BYOK); no direct billing or commercial relationship between Anthropic and Weaviate is publicly disclosed. Anthropic models are also reachable indirectly through the AWS Bedrock generative module. This indirect integration was treated identically to integrations with other model providers (OpenAI, Cohere, Voyage AI, Google, Hugging Face) during scoring.
