# Methodology

This repository follows the VERDICT evaluation framework maintained in a separate repository.

## Authoritative sources

The following documents in the [`verdict-engine`](https://github.com/zinova-lab/verdict-engine) repository are the single source of truth for how every evaluation in this repository is produced. This file intentionally does not duplicate their contents; it points to them.

| Source | Purpose |
|---|---|
| [`ENGINE.md`](https://github.com/zinova-lab/verdict-engine/blob/main/ENGINE.md) | Framework v0.3.1: dimensions, scoring criteria, evaluation sequence, output format, absolute rules. |
| [`QA.md`](https://github.com/zinova-lab/verdict-engine/blob/main/QA.md) | Three-category quality review: factual accuracy, legal risk, report quality. Severity classification and blocklists. |
| [`KNOWN_FACTS.md`](https://github.com/zinova-lab/verdict-engine/blob/main/KNOWN_FACTS.md) | Documented fact corrections the engine must apply during every evaluation. |
| [`prompts/_template.md`](https://github.com/zinova-lab/verdict-engine/blob/main/prompts/_template.md) | Standard template for platform-specific evaluation prompts. |

## Summary

VERDICT evaluates AI agent and workflow automation platforms on seven dimensions:

- **V — Verifiability** (20 points)
- **E — Effectiveness** (15 points, Layer 1+ only)
- **R — Resilience** (20 points)
- **D — Data Conduct** (15 points)
- **I — Identity & Control** (10 points)
- **C — Containment** (10 points)
- **T — Transparency** (10 points)

Layer 0 (public documentation analysis) totals 85 points. Layer 1 (free-tier behavioral testing) unlocks the E dimension and totals 100 points. A hidden dimension **P — Economic Integrity** is verified on every evaluation but is not scored; material findings appear in an Economic Risk section.

## How this maps to files in this repository

Each file in [`platforms/`](./platforms) captures one evaluation in two parts:

- **Front matter** — structured metadata conforming to [`data/schema.json`](./data/schema.json). Includes dimension scores, CISA KEV entries, QA outcomes, and review cadence.
- **Body** — the full English report in the structure defined by `ENGINE.md`'s Output Format, followed by a Japanese summary in a `japanese-summary` code block.

The [`scripts/build_index.py`](./scripts/build_index.py) pipeline:
- Computes the layer-appropriate composite score
- Assigns per-dimension rating (High / Mid / Low) against the v0.3.1 thresholds
- Assigns tier (S / A / B / C / D)
- Sets `next_review_due` to `evaluated_at + 90 days` per the framework's routine-check trigger
- Generates ranking tables and the machine-readable `data/platforms.json`

The [`scripts/validate.py`](./scripts/validate.py) pipeline enforces schema conformance plus the Internal Consistency Check defined in ENGINE.md and the CISA KEV four-location protocol.

## Framework version

All files in this repository are currently bound to **VERDICT v0.3.1-final**.

When `verdict-engine` publishes a new framework version, affected evaluations in this repository are flagged for re-evaluation per ENGINE.md Rule 9 ("Evaluations are bound to a framework version. Version change triggers re-evaluation flag.").

## Bias disclosure

Every evaluation includes the mandated verbatim bias disclosure defined in ENGINE.md. The validator enforces its presence.

## License

Framework documents in `verdict-engine` and evaluation records in this repository are both licensed under **CC BY 4.0**.
