# verdict-platforms

The canonical, machine-readable dataset of VERDICT platform evaluations.

VERDICT is the Independent AI Agent Trust Index operated by [ZinovaCreation](https://github.com/ZinovaCreation). Published evaluations live at **[getverdict.fyi](https://getverdict.fyi)**. This repository is the **structured source-of-truth** behind those evaluations — one markdown file per platform, with YAML front matter metadata and the full report body.

## Repository roles within the VERDICT ecosystem

| Repo | Role |
|---|---|
| [`verdict-engine`](https://github.com/zinova-lab/verdict-engine) | Framework specification (ENGINE.md, QA.md, KNOWN_FACTS.md, prompt templates). Defines _how_ evaluations are produced. |
| **`verdict-platforms`** (this repo) | Canonical evaluation records. One markdown file per platform. Machine-readable. |
| [`verdict-index`](https://github.com/zinova-lab/verdict-index) | The `getverdict.fyi` site — HTML rendering of the dataset. Updated from this repo. |

## What's in this repo

| Path | Purpose |
|---|---|
| [`platforms/`](./platforms) | One markdown file per evaluated platform. |
| [`rankings/`](./rankings) | Auto-generated ranking tables (overall / by category / by tier / CISA KEV). |
| [`data/platforms.json`](./data/platforms.json) | Machine-readable index built from front matter. |
| [`data/schema.json`](./data/schema.json) | JSON Schema for front matter validation. |
| [`METHODOLOGY.md`](./METHODOLOGY.md) | Pointer to the authoritative framework spec in `verdict-engine`. |
| [`CONTRIBUTING.md`](./CONTRIBUTING.md) | How to add or update a platform evaluation. |

## Framework

- **Version:** VERDICT v0.3.1-final
- **Dimensions:** V / E / R / D / I / C / T (E is Layer 1+ only)
- **Layer 0 max:** 85 points — V + R + D + I + C + T
- **Layer 1 max:** 100 points — V + E + R + D + I + C + T
- **Tiers:** S / A / B / C / D (assigned from composite score)
- **Review cadence:** 90 days per evaluation

Full specification in [`verdict-engine/ENGINE.md`](https://github.com/zinova-lab/verdict-engine/blob/main/ENGINE.md).

## Top 10 (auto-generated)

<!-- BEGIN:TOP10 -->
| Rank | Tier | Platform | Operator | Category | Score | KEV |
|---:|:---:|---|---|---|---:|:---:|
| 1 | S | [Pinecone](./platforms/pinecone.md) | Pinecone Systems, Inc. | Vector Database | 71/85 |  |
| 2 | S | [Amazon Q Business](./platforms/amazon-q-business.md) | Amazon Web Services | Enterprise AI Assistant · Cloud SaaS (AWS) | 68/85 |  |
| 3 | S | [Gemini Code Assist](./platforms/gemini-code-assist.md) | Google LLC | AI Coding Agent | 67/85 |  |
| 4 | S | [Vertex AI Agent Builder](./platforms/vertex-ai.md) | Google LLC (Alphabet Inc.) | No-Code Agent Builder · Enterprise SaaS | 65/85 |  |
| 5 | A | [Lovable](./platforms/lovable.md) | Lovable Labs AB · Sweden · $6.6B | AI App Builder · Cloud SaaS | 63/85 |  |
| 6 | A | [Devin](./platforms/devin.md) | Cognition AI · $10.2B | AI Coding Agent · Cloud SaaS | 62/85 |  |
| 6 | A | [Langfuse](./platforms/langfuse.md) | Langfuse GmbH | AI / LLM Application Observability | 62/85 |  |
| 6 | A | [Weaviate](./platforms/weaviate.md) | Weaviate B.V. | Vector Database | 62/85 |  |
| 9 | A | [Microsoft Copilot Studio](./platforms/copilot-studio.md) | Microsoft Corporation | No-Code Agent Builder · Enterprise SaaS | 61/85 |  |
| 9 | A | [OpenAI Assistants API](./platforms/openai.md) | OpenAI, L.L.C. · Deprecating August 2026 | LLM Agent API · Managed SaaS | 61/85 |  |
<!-- END:TOP10 -->

Full ranking: [`rankings/overall.md`](./rankings/overall.md)

## Principles (from `verdict-engine`)

- No vendor sponsorship. No paid certifications. No pre-publication sharing with vendors.
- Public data only (Layer 0). Silence is data — absence of disclosure is scored zero.
- VERDICT is a witness, not a judge.
- Every factual claim cites a URL. Unconfirmable items score 0.
- Framework version is bound to every evaluation. Version changes trigger re-evaluation.

## Using the dataset

```bash
# Machine-readable index
curl -sL https://raw.githubusercontent.com/ZinovaCreation/verdict-platforms/main/data/platforms.json | jq '.'

# Filter by tier
jq '.platforms[] | select(.tier == "S")' data/platforms.json

# Platforms with CISA KEV entries
jq '.platforms[] | select(.cisa_kev.present == true)' data/platforms.json
```

## Reproducibility

Every evaluation records:
- `framework_version` — bound to a specific `verdict-engine` revision
- `evaluator_model` — exact model + version that produced the scoring
- `evaluated_at` — ISO date of evaluation
- `layer` — `0`, `1`, or `C`
- `qa` — review outcomes across factual / legal / quality categories

Re-evaluations replace prior records in place. History is preserved via git.

## License

- Dataset content: [CC BY 4.0](./LICENSE) (consistent with `verdict-engine`).
- Scripts and CI: [MIT](./LICENSE-CODE).

## Maintainer

Tatsuya Suzuki — ZinovaCreation, Japan. Index: [getverdict.fyi](https://getverdict.fyi). Contact: hello@getverdict.fyi.
