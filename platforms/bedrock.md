---
name: AWS Bedrock Agents
slug: bedrock
operator: Amazon Web Services, Inc.
independence: unrecorded
parent_entity: null
category: Managed Agent Platform · Enterprise SaaS
homepage: null
github: null
evaluation_number: 17
evaluation_type: initial
evaluated_at: '2026-03-25'
evaluator_model: unrecorded
framework_version: v0.3.1
layer: '0'
target_version: null
previous_evaluation_date: null
previous_score: null
score: 55
max_score: 85
tier: A
verdict:
  v:
    score: 14
    note: ''
  e:
    score: null
    note: null
  r:
    score: 11
    note: ''
  d:
    score: 12
    note: ''
  i:
    score: 8
    note: ''
  c:
    score: 5
    note: ''
  t:
    score: 5
    note: ''
cisa_kev:
  present: false
  entries: []
cve_count_12mo: 1
cve_count_basis: exact
max_cvss_12mo: null
supply_chain_compromise_12mo: true
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
og_description: "Independent security evaluation of AWS Bedrock Agents. Score: 55/85. DNS tunneling path classified as intended functionality. Strong compliance infrastructure. Framework v0.3.1."
category_line: Managed Agent Platform · Enterprise SaaS
display_tags: &id001
- text: CVE-2026-4269 · Supply Chain · Build-Time Injection
  color: red
- text: DNS Tunneling · "Intended Functionality" · Unpatched
  color: warn
- text: SOC1/2/3 · FedRAMP High · ISO Family · HIPAA
  color: amber
- text: Cedar Policy · LLM-Bypass-Resistant Enforcement
  color: amber
finding: "Broadest compliance certification stack: SOC 1/2/3 Type 2, FedRAMP High, ISO family, HIPAA eligibility. Clearest AI training data commitment. CVE-2026-4269: S3 ownership bypass (supply chain, patched). DNS tunneling in Code Interpreter Sandbox: AWS classified as &quot;intended functionality&quot; — no code-level remedy. AgentCore Cedar Policy: deterministic enforcement outside LLM reasoning loop."
meta_description: "Independent security evaluation of AWS Bedrock Agents. Score: 55/85. DNS tunneling path classified as intended functionality. Strong compliance infrastructure. Framework v0.3.1."
key_finding: 'Broadest compliance certification stack in this index: SOC 1/2/3 Type 2, FedRAMP High, ISO family, HIPAA eligibility. Clearest AI training data commitment: "Amazon Bedrock doesn''t store or use your data to train models." CVE-2026-4269: S3 ownership bypass allowing build-time code injection into AgentCore Runtime (supply chain, patched). DNS tunneling in Code Interpreter Sandbox: AWS reverted the fix, then classified the behavior as "intended functionality" — documentation-only guidance, no code-level remedy deployed. AgentCore Cedar Policy: deterministic enforcement outside LLM reasoning loop.'
card_owner: Amazon Web Services, Inc.
card_category: Managed Agent Platform · Enterprise SaaS
card_tags: *id001
---
# AWS Bedrock Agents

Broadest compliance certification stack in this index: SOC 1/2/3 Type 2, FedRAMP High, ISO family, HIPAA eligibility. Clearest AI training data commitment: "Amazon Bedrock doesn't store or use your data to train models." CVE-2026-4269: S3 ownership bypass allowing build-time code injection into AgentCore Runtime (supply chain, patched). DNS tunneling in Code Interpreter Sandbox: AWS reverted the fix, then classified the behavior as "intended functionality" — documentation-only guidance, no code-level remedy deployed. AgentCore Cedar Policy: deterministic enforcement outside LLM reasoning loop.

## Layer 0 Score: 55/85 (Tier A)

**V** 14/20 · **R** 11/20 · **D** 12/15 · **I** 8/10 · **C** 5/10 · **T** 5/10

## CISA KEV

該当なし — no AWS Bedrock Agents packages appear in the CISA Known Exploited Vulnerabilities catalog. 1 published CVE(s) attributed to AWS Bedrock Agents in the trailing 12 months (captured).

## Bias Disclosure

This evaluation uses Claude (Anthropic) as its tooling. Anthropic operates in the AI agent market and may compete with some evaluated vendors. VERDICT discloses this relationship in every report and applies identical evaluation criteria to all platforms regardless of their relationship to Anthropic.

## Full Evaluation

See evaluations/ for the complete Layer 0 report.
