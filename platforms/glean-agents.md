---
name: Glean Agents
slug: glean-agents
operator: Glean Technologies, Inc.
independence: independent
parent_entity: null
category: Enterprise AI Assistant · Agent Platform · Cloud SaaS
homepage: https://www.glean.com
github: https://github.com/gleanwork
evaluation_number: 70
evaluation_type: initial
evaluated_at: '2026-09-24'
evaluator_model: claude-fable-5-1
selection_basis: list:mit-2025
framework_version: v0.3.2
layer: '0'
target_version: Glean Agents (GA 2025-05-20) on the Glean cloud platform as publicly documented 2026-09; Independent agents in beta
previous_evaluation_date: null
previous_score: null
score: 73
max_score: 85
tier: S
score_basis: consistent
verdict:
  v:
    score: 14
    rating: High
    note: Delaware corp; dated sub-processor list; SOC 2 report NDA-only; closed source
  r:
    score: 20
    rating: High
    note: No product-scoped CVE or public incident in trailing 12mo; zero-CVE convention
  d:
    score: 12
    rating: High
    note: DPA + DPF; no-training + zero-retention stated; analytics export lacks opt-out
  i:
    score: 10
    rating: High
    note: Write actions pause for approval by default; executor-identity enforcement
  c:
    score: 10
    rating: High
    note: Allowlist Agent Sandbox; no credentials in sandbox; single-tenant project
  t:
    score: 7
    rating: High
    note: SDLC + status page public; ISO 42001; no CVE/advisory channel beyond Bugcrowd
  e:
    score: null
    rating: null
    note: null
cisa_kev:
  present: false
  entries: []
cve_count_12mo: 0
cve_count_basis: exact
max_cvss_12mo: null
supply_chain_compromise_12mo: false
known_facts_applied: []
qa:
  factual: pass
  legal: pass
  quality: pass
  revision_cycles: 0
  flagged: false
differential: null
next_review_due: '2026-12-23'
tags:
- enterprise-ai
- agent-platform
- enterprise-search
- managed-saas
- customer-hosted
- soc2
- iso27001
- iso42001
- hipaa
- gdpr
- txramp
- human-in-the-loop
- agent-sandbox
- model-agnostic
- mit-2025
- evaluator-coi
rank: 1
sources:
- https://www.glean.com
- https://www.glean.com/privacy
- https://www.glean.com/legal
- https://www.glean.com/legal/subprocessors
- https://www.glean.com/press/glean-150-million-series-f-raised-at-7-2-billion-valuation-for-advancing-enterprise-ai-agent-technology
- https://assets.glean.com/marketing/Legal/Glean%20Technologies-%20Inc.%20Terms%20of%20Service%20Jun%205%202026.pdf
- https://cdn.prod.website-files.com/6127a84dfe068e153ef20572/66d7cec39c298d698624e7f1_Glean%20Technologies,%20Inc.%20DPA%20Sep%203%202024%20(Online).pdf
- https://docs.glean.com/security
- https://docs.glean.com/security/security-principles
- https://docs.glean.com/security/architecture/sdlc
- https://docs.glean.com/security/architecture/shared-centralized-services
- https://docs.glean.com/security/agents/background-agents
- https://docs.glean.com/security/agent-sandbox-ptc
- https://docs.glean.com/agents/how-agents-work
- https://docs.glean.com/agents/independent-agents
- https://docs.glean.com/agents/concepts/agent-builder
- https://docs.glean.com/agents/concepts/agent-library
- https://docs.glean.com/agents/concepts/schedule-triggers
- https://docs.glean.com/agents/actions/glean/wait-for-user-input
- https://docs.glean.com/administration/managing-agents/agent-access
- https://docs.glean.com/administration/assistant/configuration/chat-history
- https://docs.glean.com/administration/management/audit-logs/admin-audit-logs
- https://docs.glean.com/administration/assistant/data-analysis/about-data-analysis
- https://docs.glean.com/administration/gce-logs/data-dictionary
- https://docs.glean.com/get-started/golive/model-choice
- https://docs.glean.com/user-guide/about/end-user-quick-start-guide
- https://docs.glean.com/release-notes/releases/2026-07-15-july-release
- https://developers.glean.com/api/client-api/agents/overview
- https://status.glean.com/history?date=2026-09-23
- https://bugcrowd.com/engagements/glean-technologies-public
- https://aiagentindex.mit.edu/2025/glean-agents
- https://osv.dev/vulnerability/CVE-2026-54339
- https://www.npmjs.com/package/@gleanwork/local-mcp-server
finding: 'Glean Technologies, Inc., a Delaware corporation headquartered in San Francisco with a Palo Alto office, scores 73/85 (Tier S) on VERDICT Layer 0 public-documentation review for Glean Agents, the agent product of its Work AI platform (evaluated at product level to match the MIT AI Agent Index 2025 entry). Identity & Control (10/10) and Containment (10/10) are the strengths: write actions in interactive web sessions pause for user approval by default and administrators must explicitly opt an action out of confirmation; agents execute with the identity and permissions of the signed-in user who triggered the run regardless of who built or published them; the Agent Sandbox is allowlist-based (read-only native tools by default, no outbound internet except allowlisted domains, no credentials inside the sandbox) with per-tenant, per-session isolation; and each customer runs in a single-tenant cloud project, customer-hosted or Glean-hosted. Platform-level certifications are SOC 2 Type II, ISO 27001, ISO 42001, HIPAA and TX-RAMP Level 2, and the sub-processor list carries a last-updated date. No CVE attributable to a Glean Technologies product and no publicly reported security incident were confirmed in the trailing 12 months; the one "Glean" CVE in the search set belongs to an unrelated self-hosted RSS reader. Recorded gaps are closed source, a SOC 2 Type II report and Security Standard available only under NDA, an anonymized analytics export to Glean central infrastructure that is on by default with no documented opt-out, and a vulnerability-disclosure posture limited to a Bugcrowd program and a security@ address with no public CVE or advisory channel.'
meta_owner: 'Glean Technologies, Inc., a Delaware corporation headquartered at 634 2nd Street, San Francisco, with a Palo Alto office (260 Sheridan Ave); founded 2019 by Arvind Jain (CEO); Series F of $150 million led by Wellington Management (June 2025) at a company-stated $7.2 billion valuation; independent, no parent entity.'
meta_description: 'Independent security evaluation of Glean Agents. Score: 73/85 (Tier S). SOC 2 Type II, ISO 27001, ISO 42001, HIPAA. Write actions pause for approval by default, allowlist-based Agent Sandbox, zero product-scoped CVEs. Framework v0.3.2.'
og_description: 'Glean Agents scores 73/85 (Tier S) on VERDICT: default write-action approval, allowlist sandbox, single-tenant isolation, zero product-scoped CVEs; analytics export to Glean has no documented opt-out.'
category_line: Enterprise AI Assistant · Agent Platform · Cloud SaaS
display_tags:
- text: SOC 2 Type II · ISO 27001 · ISO 42001 · HIPAA
  color: safe
- text: Write actions pause for user approval by default
  color: safe
- text: Allowlist Agent Sandbox · single-tenant project
  color: safe
- text: Analytics export to Glean · no documented opt-out
  color: amber
- text: Closed source · SOC 2 report under NDA
  color: dim
key_finding: 'Glean Agents scores 73/85 (Tier S) on VERDICT v0.3.2 Layer 0: SOC 2 Type II, ISO 27001, ISO 42001 and HIPAA, write actions that pause for user approval by default, execution-time permission enforcement on the triggering user''s identity, and an allowlist-based Agent Sandbox with per-tenant isolation and no credentials inside it. No product-scoped CVE or public security incident was confirmed in the trailing 12 months; recorded gaps are closed source, a SOC 2 report available only under NDA, no documented opt-out for the anonymized analytics export to Glean, and no public advisory channel beyond a Bugcrowd program.'
card_owner: Glean Technologies, Inc. · San Francisco / Palo Alto · Series F ($150M, Wellington Management)
card_category: Enterprise AI Assistant · Agent Platform
card_tags:
- text: SOC 2 Type II · ISO 27001 · ISO 42001 · HIPAA
  color: safe
- text: Write actions pause for user approval by default
  color: safe
- text: Allowlist Agent Sandbox · single-tenant project
  color: safe
- text: Analytics export to Glean · no documented opt-out
  color: amber
---
# Glean Agents

Glean Agents scores 73/85 (Tier S) on VERDICT v0.3.2 Layer 0: SOC 2 Type II, ISO 27001, ISO 42001 and HIPAA, write actions that pause for user approval by default, execution-time permission enforcement on the triggering user's identity, and an allowlist-based Agent Sandbox with per-tenant isolation and no credentials inside it. No product-scoped CVE or public security incident was confirmed in the trailing 12 months; recorded gaps are closed source, a SOC 2 report available only under NDA, no documented opt-out for the anonymized analytics export to Glean, and no public advisory channel beyond a Bugcrowd program.

## Layer 0 Score: 73/85 (Tier S)

**V** 14/20 · **R** 20/20 · **D** 12/15 · **I** 10/10 · **C** 10/10 · **T** 7/10

## Selection basis

`list:mit-2025` — MIT AI Agent Index 2025 entry `glean-agents`, evaluated at product level per Population Definition §5; platform-level privacy, security and data-processing documents form the evidence base.

## CISA KEV

該当なし — no Glean Technologies product appears in the CISA Known Exploited Vulnerabilities catalog. Zero published CVEs attributed to a Glean Technologies product in the trailing 12 months (2025-09-24 – 2026-09-24); CVE-2026-54339 (`LeslieLeung/glean`, an unrelated self-hosted RSS reader) is excluded by product-scoped attribution.

## Bias Disclosure

This evaluation uses Claude (Anthropic) as its tooling. Anthropic operates in the AI agent market and may compete with some evaluated vendors. VERDICT discloses this relationship in every report and applies identical evaluation criteria to all platforms regardless of their relationship to Anthropic.

Product-level integration disclosure: Anthropic PBC is listed on Glean's sub-processor list as an LLM Provider (last updated July 28, 2026) and Claude models are among the models selectable in Glean's Model Hub; Glean also publishes a "Glean vs Claude Enterprise" comparison page. These are standard model-provider and market-competition relationships; framework Triggers 0–3 do not fire. The record carries the structured tag `evaluator-coi`.

## Full Evaluation

See evaluations/070_glean_agents.md for the complete Layer 0 report.
