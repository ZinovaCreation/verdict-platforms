---
name: Cohere
slug: cohere
operator: Cohere Inc.
independence: independent
parent_entity: null
category: Foundation Model API
homepage: https://cohere.com
github: https://github.com/cohere-ai
evaluation_number: 69
evaluation_type: initial
evaluated_at: '2026-05-15'
evaluator_model: unrecorded
framework_version: v0.3.1-final
layer: '0'
target_version: Cohere API platform; Command A / Command R+; Embed 4; Rerank 3.5; North
previous_evaluation_date: null
previous_score: null
score: 42
max_score: 85
tier: C
verdict:
  v:
    score: 14
    rating: High
    note: ''
  r:
    score: 8
    rating: Mid
    note: ''
  d:
    score: 7
    rating: Mid
    note: ''
  i:
    score: 4
    rating: Mid
    note: ''
  c:
    score: 2
    rating: Low
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
cve_count_12mo: 1
max_cvss_12mo: 9.3
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
- foundation-model
- enterprise-ai
- agentic-ai
- sovereign-ai
- canada
- command-r
- north
- embed
- rerank
- iso-42001
- aleph-alpha-pending
- evaluator-coi
- shared-investor
- commercial-channel
sources:
- https://cohere.com/
- https://docs.cohere.com
- https://github.com/cohere-ai
- https://trustcenter.cohere.com/
- https://www.sec.gov/
rank: null
"finding": |-
  Cohere Inc., a Canadian federal corporation in Toronto, scores 42/85 (Tier C) on VERDICT Layer 0 public-documentation review. Verifiability (14/20) and Transparency (7/10) are the strengths: corporate identity that is consistent across primary sources, SOC 2 Type II / ISO 27001 / ISO 42001 certifications, a published Secure AI Frontier Model Framework, a multi-jurisdictional Data Processing Addendum incorporating EU Standard Contractual Clauses, and a public operational status page. Resilience (8/20) reflects one Critical-severity vulnerability in the trailing twelve months — CVE-2026-5752 (CVSS 9.3), a sandbox escape in the Cohere Terrarium Python sandbox via JavaScript prototype-chain traversal that yields root code execution on the host — disclosed through CERT/CC VU#414811, whose published timeline records a 61-day window from vendor notification to disclosure with vendor status listed as "Unknown," after which the affected project was archived as end-of-life rather than placed under continued maintenance. Containment (2/10) is constrained because no public architectural documentation describes the tool and code-execution boundary for the North agentic workspace following Terrarium's archival. Open-weight Command R+ research releases are licensed under CC-BY-NC-4.0 (non-commercial), which is not equivalent to OSI open-source and is distinct from the proprietary commercial Cohere API.
"meta_owner": |-
  Cohere Inc., a Canadian federal corporation headquartered in Toronto (founders Aidan Gomez, Nick Frosst, Ivan Zhang); cumulative funding is reported across an unreconciled range (~$935M to ~$1.7B across public sources) rather than a single confirmed figure.
"meta_description": |-
  VERDICT's independent Layer 0 review scores Cohere (Command, Embed, Rerank, and the North agentic platform) 42/85 (Tier C) using only public data. Strengths include SOC 2 Type II / ISO 27001 / ISO 42001 certification, a published Secure AI Frontier Model Framework, and a multi-jurisdictional DPA with EU Standard Contractual Clauses; the score is constrained by CVE-2026-5752 (CVSS 9.3, Cohere Terrarium sandbox escape) and the absence of public containment documentation for the North agent runtime.
"og_description": |-
  Cohere scores 42/85 (Tier C) on VERDICT's public-data trust review — strong on certification and transparency (SOC 2 Type II, ISO 27001/42001, published safety framework), constrained by a Critical sandbox-escape CVE (CVE-2026-5752, CVSS 9.3) and limited public containment documentation for its North agentic platform.
"category_line": |-
  Foundation Model API · Enterprise AI Platform · Agentic AI · Retrieval and Embedding Infrastructure
display_tags:
- text: SOC 2 Type II · ISO 27001 · ISO 42001
  color: safe
- text: Canadian federal corporation · verifiable founder identity
  color: safe
- text: Secure AI Frontier Model Framework published
  color: safe
- text: Multi-jurisdiction DPA · EU SCC · Transfer Impact Assessment
  color: safe
- text: Public status page · bug bounty program
  color: safe
- text: CVE-2026-5752 · CVSS 9.3 · Terrarium archived EOL
  color: amber
- text: North agent runtime containment undocumented
  color: amber
- text: Command R+ open-weight CC-BY-NC-4.0 · not OSI open-source
  color: amber
- text: SOC 2 Type II report mNDA-gated
  color: amber
---

# Cohere

<!-- TODO(VERDICT project): overview + Strongest/Largest prose, and the six display-copy fields - author from evaluations/069_cohere.md. -->

## Layer 0 Score: 42/85 (Tier C)

**V** 14/20 · **R** 8/20 · **D** 7/15 · **I** 4/10 · **C** 2/10 · **T** 7/10

## Bias Disclosure

This evaluation uses Claude (Anthropic) as its tooling. Anthropic operates in the AI agent market and may compete with some evaluated vendors. VERDICT discloses this relationship in every report and applies identical evaluation criteria to all platforms regardless of their relationship to Anthropic.

VERDICT additionally discloses that the operator of this platform (Cohere Inc.) has a shared-investor and commercial-channel relationship with VERDICT's evaluation tooling provider (Anthropic): NVIDIA holds equity in Cohere across multiple rounds (Series D USD 500M, July 2024; extension USD 100M, September 2025) and separately holds a strategic equity commitment in Anthropic (up to USD 10B, subject to closing conditions per NVIDIA SEC Form 10-Q FY2026 Q3) — a compound investor structure in which NVIDIA holds equity in both the evaluator and the evaluated platform. This corresponds to VERDICT Trigger 2 (shared investor). Additively, Cohere maintains a co-engineered NVIDIA NIM channel relationship for Command-R distribution (Trigger 3). Source: NVIDIA SEC Form 10-Q FY2026 Q3. Identical evaluation criteria were applied regardless of this relationship.

## Contextual Note

A planned merger with Germany's Aleph Alpha GmbH was announced 2026-04-24 and remains subject to regulatory and shareholder approval at evaluation date. This forward-looking ownership change is tracked separately (tag: aleph-alpha-pending) and will trigger re-evaluation on close; it is independent of the NVIDIA-routed evaluator-COI disclosure above.
