#!/usr/bin/env python3
"""
build_index.py — Generate data/platforms.json and rankings/*.md from platform files.

Follows VERDICT Framework v0.3.1:
  - Layer 0 composite = V + R + D + I + C + T (max 85)
  - Layer 1 composite = V + E + R + D + I + C + T (max 100)
  - Rating auto-assigned per dimension (70%+ High, 40–69% Mid, 0–39% Low)
  - Tier auto-assigned from composite score (see TIER_THRESHOLDS)
  - next_review_due = evaluated_at + 90 days
  - CISA KEV-present platforms surface in rankings

Outputs:
  - data/platforms.json
  - rankings/overall.md
  - rankings/by-category.md
  - rankings/by-tier.md
  - rankings/cisa-kev.md
  - README.md TOP10 block between <!-- BEGIN:TOP10 --> and <!-- END:TOP10 -->

Writes computed fields back into each platform file's front matter so the source
of truth stays in sync: rating (per dimension), tier, next_review_due, rank.

Usage: python scripts/build_index.py
"""
from __future__ import annotations

import json
import re
import sys
from datetime import date, datetime, timedelta, timezone
from pathlib import Path

try:
    import frontmatter
except ImportError:
    sys.stderr.write(
        "Missing dependency 'python-frontmatter'. Install:\n"
        "  pip install -r scripts/requirements.txt\n"
    )
    sys.exit(2)

ROOT = Path(__file__).resolve().parent.parent
PLATFORMS_DIR = ROOT / "platforms"
RANKINGS_DIR = ROOT / "rankings"
DATA_DIR = ROOT / "data"
README = ROOT / "README.md"

TOP10_BEGIN = "<!-- BEGIN:TOP10 -->"
TOP10_END = "<!-- END:TOP10 -->"

# Axis maximums per ENGINE.md v0.3.1
AXIS_MAX = {"v": 20, "r": 20, "d": 15, "i": 10, "c": 10, "t": 10, "e": 15}
LAYER_0_AXES = ("v", "r", "d", "i", "c", "t")
LAYER_1_AXES = ("v", "e", "r", "d", "i", "c", "t")

# Rating thresholds (percentage of axis maximum)
RATING_HIGH_MIN = 0.70
RATING_MID_MIN = 0.40

# Tier thresholds (absolute Layer-0 score). Reviewed against Worklog v3
# distribution (S:2 / A:13 / B:17 / C:16 / D:7) and the inferred 10-point
# bands. Editable; authority of record is rankings/index.html on getverdict.fyi.
TIER_THRESHOLDS = [
    ("S", 65),  # >= 65
    ("A", 55),
    ("B", 45),
    ("C", 35),
    ("D",  0),
]

REVIEW_CADENCE_DAYS = 90

# Canonical front-matter key order — preserved on every write-back so source
# files stay readable for humans. Unknown keys are appended in original order.
CANONICAL_KEY_ORDER = [
    "name", "slug", "operator", "independence", "parent_entity",
    "category", "homepage", "github",
    "evaluation_number", "evaluation_type",
    "evaluated_at", "evaluator_model", "framework_version", "layer",
    "target_version", "previous_evaluation_date", "previous_score",
    "score", "max_score", "tier",
    "verdict",
    "cisa_kev",
    "cve_count_12mo", "max_cvss_12mo", "supply_chain_compromise_12mo",
    "known_facts_applied",
    "qa",
    "differential",
    "next_review_due",
    "tags",
    "rank",
]
AXIS_WRITE_ORDER = ["v", "r", "d", "i", "c", "t", "e"]
AXIS_FIELD_ORDER = ["score", "rating", "note"]


# ─── Computation helpers ───────────────────────────────────────────────────

def rating_for(score: int | float | None, axis: str) -> str | None:
    """Map (score, axis) to 'High' / 'Mid' / 'Low' per v0.3.1 thresholds."""
    if score is None:
        return None
    pct = score / AXIS_MAX[axis]
    if pct >= RATING_HIGH_MIN:
        return "High"
    if pct >= RATING_MID_MIN:
        return "Mid"
    return "Low"


def composite_score(verdict: dict, layer: str) -> int:
    """Compute layer-appropriate composite. E is excluded at Layer 0."""
    axes = LAYER_1_AXES if layer == "1" else LAYER_0_AXES
    total = 0
    for axis in axes:
        axis_block = verdict.get(axis) or {}
        score = axis_block.get("score")
        if score is None:
            continue  # E at Layer 0 is null — treated as excluded
        total += int(score)
    return total


def max_score_for_layer(layer: str) -> int:
    return 100 if layer == "1" else 85


def tier_for(score: int | None, max_score: int) -> str | None:
    """Assign S/A/B/C/D based on absolute Layer-0 score bands."""
    if score is None:
        return None
    # Tier thresholds are defined against the 85-point scale. For Layer 1
    # (max=100), we compare against the equivalent 85-scale value.
    effective = score * 85 / max_score if max_score else 0
    for tier, minimum in TIER_THRESHOLDS:
        if effective >= minimum:
            return tier
    return "D"


def plus_days(iso_date: str, days: int) -> str:
    d = datetime.strptime(iso_date, "%Y-%m-%d").date()
    return (d + timedelta(days=days)).isoformat()


def coerce_date(value) -> str:
    """YAML may give us date or str; always return ISO string."""
    if isinstance(value, (date, datetime)):
        return value.isoformat() if isinstance(value, date) else value.date().isoformat()
    return str(value) if value is not None else ""


# ─── Metadata normalization ────────────────────────────────────────────────

def normalize_axis(axis_block: dict, axis: str) -> dict:
    """Canonicalize one verdict.<axis> block: key order + auto-rating."""
    if not isinstance(axis_block, dict):
        axis_block = {}
    score = axis_block.get("score")
    normalized = {
        "score":  score,
        "rating": rating_for(score, axis),
        "note":   axis_block.get("note", "") if score is not None else axis_block.get("note"),
    }
    return normalized


def reorder_metadata(meta: dict) -> dict:
    """Canonical key order + normalized verdict block."""
    ordered: dict = {}
    for key in CANONICAL_KEY_ORDER:
        if key in meta:
            ordered[key] = meta[key]
    for key, value in meta.items():
        if key not in ordered:
            ordered[key] = value

    verdict = ordered.get("verdict")
    if isinstance(verdict, dict):
        reordered_verdict: dict = {}
        for axis in AXIS_WRITE_ORDER:
            if axis in verdict:
                reordered_verdict[axis] = normalize_axis(verdict[axis], axis)
        for axis, value in verdict.items():
            if axis not in reordered_verdict:
                reordered_verdict[axis] = value
        ordered["verdict"] = reordered_verdict

    # Dates: coerce to ISO string (YAML date objects would otherwise persist).
    for k in ("evaluated_at", "previous_evaluation_date", "next_review_due"):
        if k in ordered and ordered[k] is not None:
            ordered[k] = coerce_date(ordered[k])

    return ordered


# ─── Core pipeline ─────────────────────────────────────────────────────────

def load_platforms() -> list[tuple[Path, frontmatter.Post]]:
    out: list[tuple[Path, frontmatter.Post]] = []
    for path in sorted(PLATFORMS_DIR.glob("*.md")):
        if path.name.startswith("_"):
            continue
        post = frontmatter.load(path)
        if "slug" not in post.metadata:
            sys.stderr.write(f"Skipping {path.name}: no 'slug' in front matter.\n")
            continue
        out.append((path, post))
    return out


def enrich_and_rank(posts: list[tuple[Path, frontmatter.Post]]) -> list[dict]:
    """Compute derived fields, assign rank, write back to each file."""
    records: list[dict] = []

    for path, post in posts:
        m = post.metadata
        layer = str(m.get("layer", "0"))
        verdict = m.get("verdict") or {}

        # Auto-compute: rating per axis, composite score, tier, next_review_due
        computed_score = composite_score(verdict, layer)
        max_score = max_score_for_layer(layer)
        authored_score = m.get("score")
        tier = tier_for(authored_score if authored_score is not None else computed_score,
                        m.get("max_score", max_score))

        evaluated_at = coerce_date(m.get("evaluated_at"))
        authored_due = coerce_date(m.get("next_review_due")) if m.get("next_review_due") else ""
        derived_due = plus_days(evaluated_at, REVIEW_CADENCE_DAYS) if evaluated_at else ""
        next_due = authored_due or derived_due

        records.append({
            "path": path,
            "post": post,
            "meta": m,
            "name": m.get("name"),
            "slug": m.get("slug"),
            "operator": m.get("operator"),
            "independence": m.get("independence"),
            "parent_entity": m.get("parent_entity"),
            "category": m.get("category"),
            "homepage": m.get("homepage"),
            "github": m.get("github"),
            "evaluation_number": m.get("evaluation_number"),
            "evaluation_type": m.get("evaluation_type"),
            "evaluated_at": evaluated_at,
            "evaluator_model": m.get("evaluator_model"),
            "framework_version": m.get("framework_version"),
            "layer": layer,
            "target_version": m.get("target_version"),
            "score": authored_score if authored_score is not None else computed_score,
            "computed_score": computed_score,
            "max_score": m.get("max_score", max_score),
            "tier": tier,
            "verdict": verdict,
            "cisa_kev": m.get("cisa_kev") or {"present": False, "entries": []},
            "cve_count_12mo": m.get("cve_count_12mo", 0),
            "max_cvss_12mo": m.get("max_cvss_12mo"),
            "supply_chain_compromise_12mo": m.get("supply_chain_compromise_12mo", False),
            "known_facts_applied": m.get("known_facts_applied", []),
            "qa": m.get("qa") or {},
            "next_review_due": next_due,
            "tags": m.get("tags", []),
        })

    # Sort by score desc, then name asc for stable display
    records.sort(key=lambda r: (-(r["score"] or 0), r["name"] or ""))

    # Competition-style ranking (1, 2, 2, 4)
    last_score = None
    last_rank = 0
    for idx, rec in enumerate(records, start=1):
        s = rec["score"]
        if s != last_score:
            last_rank = idx
            last_score = s
        rec["rank"] = last_rank

    # Persist derived fields back into each file
    for rec in records:
        meta = rec["post"].metadata
        meta["rank"] = rec["rank"]
        meta["tier"] = rec["tier"]
        meta["score"] = rec["score"]
        meta["next_review_due"] = rec["next_review_due"]
        rec["post"].metadata = reorder_metadata(meta)
        # After normalization, pull the canonicalized verdict (with ratings
        # auto-assigned) back onto the record so the JSON reflects it.
        rec["verdict"] = rec["post"].metadata.get("verdict", rec["verdict"])
        with open(rec["path"], "wb") as fh:
            frontmatter.dump(rec["post"], fh, sort_keys=False, allow_unicode=True)

    return records


# ─── Output writers ────────────────────────────────────────────────────────

def write_json_index(records: list[dict]) -> None:
    DATA_DIR.mkdir(exist_ok=True)
    payload = {
        "generated_at": datetime.now(timezone.utc).isoformat(timespec="seconds"),
        "framework_version": records[0]["framework_version"] if records else None,
        "count": len(records),
        "platforms": [
            {
                "rank": r["rank"],
                "tier": r["tier"],
                "slug": r["slug"],
                "name": r["name"],
                "operator": r["operator"],
                "independence": r["independence"],
                "parent_entity": r["parent_entity"],
                "category": r["category"],
                "homepage": r["homepage"],
                "github": r["github"],
                "score": r["score"],
                "max_score": r["max_score"],
                "layer": r["layer"],
                "verdict": r["verdict"],
                "cisa_kev": r["cisa_kev"],
                "cve_count_12mo": r["cve_count_12mo"],
                "max_cvss_12mo": r["max_cvss_12mo"],
                "supply_chain_compromise_12mo": r["supply_chain_compromise_12mo"],
                "evaluated_at": r["evaluated_at"],
                "evaluator_model": r["evaluator_model"],
                "framework_version": r["framework_version"],
                "next_review_due": r["next_review_due"],
                "tags": r["tags"],
            }
            for r in records
        ],
    }
    (DATA_DIR / "platforms.json").write_text(
        json.dumps(payload, indent=2, ensure_ascii=False) + "\n",
        encoding="utf-8",
    )


def _axis(rec: dict, axis: str) -> int | str:
    val = (rec["verdict"].get(axis) or {}).get("score")
    return val if val is not None else "—"


def _kev_marker(rec: dict) -> str:
    return "✅" if rec["cisa_kev"].get("present") else ""


def _platform_link(rec: dict) -> str:
    return f"[{rec['name']}](../platforms/{rec['slug']}.md)"


def write_overall_ranking(records: list[dict]) -> None:
    RANKINGS_DIR.mkdir(exist_ok=True)
    lines = [
        "# Overall ranking",
        "",
        f"_Auto-generated — {len(records)} platform(s). Do not edit by hand._",
        "",
        "| Rank | Tier | Platform | Operator | Category | Score | V | R | D | I | C | T | KEV |",
        "|---:|:---:|---|---|---|---:|---:|---:|---:|---:|---:|---:|:---:|",
    ]
    if not records:
        lines.append("| — | — | _No platforms yet_ | — | — | — | — | — | — | — | — | — | — |")
    else:
        for r in records:
            lines.append(
                f"| {r['rank']} "
                f"| {r['tier'] or '—'} "
                f"| {_platform_link(r)} "
                f"| {r['operator'] or '—'} "
                f"| {r['category'] or '—'} "
                f"| {r['score']}/{r['max_score']} "
                f"| {_axis(r, 'v')} "
                f"| {_axis(r, 'r')} "
                f"| {_axis(r, 'd')} "
                f"| {_axis(r, 'i')} "
                f"| {_axis(r, 'c')} "
                f"| {_axis(r, 't')} "
                f"| {_kev_marker(r)} |"
            )
    (RANKINGS_DIR / "overall.md").write_text("\n".join(lines) + "\n", encoding="utf-8")


def write_by_category(records: list[dict]) -> None:
    lines = ["# Ranking by category", "", "_Auto-generated. Do not edit by hand._", ""]
    by_cat: dict[str, list[dict]] = {}
    for r in records:
        by_cat.setdefault(r["category"] or "Uncategorized", []).append(r)
    if not by_cat:
        lines.append("_No platforms yet._")
    else:
        for cat in sorted(by_cat):
            lines.append(f"## {cat}")
            lines.append("")
            lines.append("| Rank | Tier | Platform | Operator | Score |")
            lines.append("|---:|:---:|---|---|---:|")
            for r in by_cat[cat]:
                lines.append(
                    f"| {r['rank']} | {r['tier'] or '—'} | {_platform_link(r)} "
                    f"| {r['operator'] or '—'} | {r['score']}/{r['max_score']} |"
                )
            lines.append("")
    (RANKINGS_DIR / "by-category.md").write_text("\n".join(lines) + "\n", encoding="utf-8")


def write_by_tier(records: list[dict]) -> None:
    lines = ["# Ranking by tier", "", "_Auto-generated. Do not edit by hand._", ""]
    by_tier: dict[str, list[dict]] = {"S": [], "A": [], "B": [], "C": [], "D": []}
    for r in records:
        t = r["tier"] or "D"
        by_tier.setdefault(t, []).append(r)
    if not records:
        lines.append("_No platforms yet._")
    else:
        for tier in ["S", "A", "B", "C", "D"]:
            rows = by_tier.get(tier, [])
            lines.append(f"## Tier {tier}")
            lines.append("")
            if not rows:
                lines.append("_No platforms in this tier._")
            else:
                lines.append("| Rank | Platform | Operator | Category | Score |")
                lines.append("|---:|---|---|---|---:|")
                for r in rows:
                    lines.append(
                        f"| {r['rank']} | {_platform_link(r)} | {r['operator'] or '—'} "
                        f"| {r['category'] or '—'} | {r['score']}/{r['max_score']} |"
                    )
            lines.append("")
    (RANKINGS_DIR / "by-tier.md").write_text("\n".join(lines) + "\n", encoding="utf-8")


def write_cisa_kev(records: list[dict]) -> None:
    kev_records = [r for r in records if r["cisa_kev"].get("present")]
    lines = ["# CISA KEV catalog references", "",
             "_Auto-generated. Do not edit by hand._",
             "",
             "Platforms with one or more CVEs in the CISA Known Exploited Vulnerabilities catalog.",
             ""]
    if not kev_records:
        lines.append("_No platforms in the index currently have CISA KEV entries._")
    else:
        lines.append("| Platform | CVE ID | KEV added | FCEC deadline | Elapsed (days) |")
        lines.append("|---|---|---|---|---:|")
        for r in kev_records:
            for e in r["cisa_kev"].get("entries", []):
                lines.append(
                    f"| {_platform_link(r)} "
                    f"| {e.get('cve_id', '—')} "
                    f"| {coerce_date(e.get('kev_added_date')) or '—'} "
                    f"| {coerce_date(e.get('fcec_deadline')) or '—'} "
                    f"| {e.get('elapsed_days') if e.get('elapsed_days') is not None else '—'} |"
                )
    (RANKINGS_DIR / "cisa-kev.md").write_text("\n".join(lines) + "\n", encoding="utf-8")


def update_readme_top10(records: list[dict]) -> None:
    if not README.exists():
        return
    text = README.read_text(encoding="utf-8")
    if TOP10_BEGIN not in text or TOP10_END not in text:
        return
    if not records:
        replacement = (
            f"{TOP10_BEGIN}\n"
            "_Ranking will populate once platforms are added. "
            "Run `python scripts/build_index.py` to regenerate._\n"
            f"{TOP10_END}"
        )
    else:
        top = records[:10]
        rows = [
            "| Rank | Tier | Platform | Operator | Category | Score | KEV |",
            "|---:|:---:|---|---|---|---:|:---:|",
        ]
        for r in top:
            rows.append(
                f"| {r['rank']} | {r['tier'] or '—'} "
                f"| [{r['name']}](./platforms/{r['slug']}.md) "
                f"| {r['operator'] or '—'} | {r['category'] or '—'} "
                f"| {r['score']}/{r['max_score']} | {_kev_marker(r)} |"
            )
        replacement = f"{TOP10_BEGIN}\n" + "\n".join(rows) + f"\n{TOP10_END}"
    new_text = re.sub(
        re.escape(TOP10_BEGIN) + r".*?" + re.escape(TOP10_END),
        replacement,
        text,
        flags=re.DOTALL,
    )
    README.write_text(new_text, encoding="utf-8")


def main() -> int:
    posts = load_platforms()
    records = enrich_and_rank(posts)
    write_json_index(records)
    write_overall_ranking(records)
    write_by_category(records)
    write_by_tier(records)
    write_cisa_kev(records)
    update_readme_top10(records)
    print(f"Built index for {len(records)} platform(s).")
    return 0


if __name__ == "__main__":
    sys.exit(main())
