#!/usr/bin/env python3
"""
validate.py — Validate platform files against VERDICT Framework v0.3.1.

Checks performed per file:
  1.  JSON Schema (data/schema.json)
  2.  Filename matches slug  (platforms/<slug>.md)
  3.  Layer-appropriate composite:
         Layer 0: score == V + R + D + I + C + T (max 85, E excluded)
         Layer 1: score == V + E + R + D + I + C + T (max 100)
  4.  max_score matches layer (85 / 100)
  5.  Layer-0 E must be null; Layer-1 E must be integer
  6.  CISA KEV Protocol: if cisa_kev.present, entries must be non-empty AND
      body must mention KEV in Scorecard / Incident Timeline / Executive Summary
      / Contextual Analysis (4-location check per ENGINE.md)
  7.  Bias Disclosure verbatim check (body must contain ENGINE.md mandated text)
  8.  Rating consistency: each axis rating matches threshold (70/40)
  9.  next_review_due == base + 90 days (base = updated_at if present else evaluated_at)
  10. Update evaluations must declare differential states

Usage:
  python scripts/validate.py platforms/<slug>.md [...]
  python scripts/validate.py            # validates all platforms/*.md

Exit code: 0 if all files pass, 1 if any fail, 2 if dependencies missing.
"""
from __future__ import annotations

import datetime
import json
import re
import sys
from pathlib import Path

try:
    import frontmatter
    from jsonschema import Draft202012Validator
except ImportError:
    sys.stderr.write(
        "Missing dependencies. Install:\n"
        "  pip install -r scripts/requirements.txt\n"
    )
    sys.exit(2)

ROOT = Path(__file__).resolve().parent.parent
SCHEMA_PATH = ROOT / "data" / "schema.json"
PLATFORMS_DIR = ROOT / "platforms"

AXIS_MAX = {"v": 20, "r": 20, "d": 15, "i": 10, "c": 10, "t": 10, "e": 15}
LAYER_0_AXES = ("v", "r", "d", "i", "c", "t")
LAYER_1_AXES = ("v", "e", "r", "d", "i", "c", "t")

RATING_HIGH_MIN = 0.70
RATING_MID_MIN = 0.40
REVIEW_CADENCE_DAYS = 90

# ENGINE.md v0.3.1 mandated bias disclosure — verbatim
BIAS_DISCLOSURE_VERBATIM = (
    "This evaluation uses Claude (Anthropic) as its tooling. Anthropic operates "
    "in the AI agent market and may compete with some evaluated vendors. VERDICT "
    "discloses this relationship in every report and applies identical evaluation "
    "criteria to all platforms regardless of their relationship to Anthropic."
)

# CISA KEV must be recorded in these 4 locations per ENGINE.md
KEV_REQUIRED_SECTIONS = ["Scorecard", "Incident Timeline", "Executive Summary", "Contextual Analysis"]


# ─── Helpers ───────────────────────────────────────────────────────────────

def rating_for(score: int | None, axis: str) -> str | None:
    if score is None:
        return None
    pct = score / AXIS_MAX[axis]
    if pct >= RATING_HIGH_MIN:
        return "High"
    if pct >= RATING_MID_MIN:
        return "Mid"
    return "Low"


def composite_from_verdict(verdict: dict, layer: str) -> int:
    axes = LAYER_1_AXES if layer == "1" else LAYER_0_AXES
    total = 0
    for axis in axes:
        block = verdict.get(axis) or {}
        score = block.get("score")
        if score is None:
            continue
        total += int(score)
    return total


def plus_days(iso_date: str, days: int) -> str:
    d = datetime.datetime.strptime(iso_date, "%Y-%m-%d").date()
    return (d + datetime.timedelta(days=days)).isoformat()


def normalize_for_schema(meta: dict) -> dict:
    """YAML may parse dates as date objects; schema expects strings."""
    normalized = dict(meta)
    for k in ("evaluated_at", "updated_at", "previous_evaluation_date", "next_review_due"):
        v = normalized.get(k)
        if isinstance(v, (datetime.date, datetime.datetime)):
            normalized[k] = v.isoformat() if isinstance(v, datetime.date) else v.date().isoformat()
    # Dates inside cisa_kev.entries as well
    kev = normalized.get("cisa_kev") or {}
    entries = kev.get("entries") or []
    new_entries = []
    for e in entries:
        ne = dict(e) if isinstance(e, dict) else {}
        for dk in ("kev_added_date", "fcec_deadline"):
            if isinstance(ne.get(dk), datetime.date):
                ne[dk] = ne[dk].isoformat()
        new_entries.append(ne)
    if entries:
        normalized["cisa_kev"] = {**kev, "entries": new_entries}
    return normalized


def section_text(body: str, section: str) -> str:
    """
    Extract text under a markdown heading (##/###) whose title contains the
    given section name. Returns empty string if no such heading is found.
    Iterates line-by-line to avoid fragile multi-line regex.
    """
    lines = body.splitlines()
    collecting = False
    out: list[str] = []
    heading_re = re.compile(r"^(#{1,6})\s+(.*)$")
    target_re = re.compile(rf"\b{re.escape(section)}\b", re.IGNORECASE)
    for line in lines:
        m = heading_re.match(line)
        if m:
            title = m.group(2)
            if not collecting and target_re.search(title):
                collecting = True
                continue
            if collecting:
                # Next heading of any level ends the section.
                break
        elif collecting:
            out.append(line)
    return "\n".join(out)


# ─── File-level validator ──────────────────────────────────────────────────

def validate_file(path: Path, validator: Draft202012Validator) -> list[str]:
    errors: list[str] = []
    post = frontmatter.load(path)
    meta = post.metadata
    body = post.content
    normalized = normalize_for_schema(meta)

    # 1. JSON Schema validation
    for err in sorted(validator.iter_errors(normalized), key=lambda e: list(e.path)):
        loc = ".".join(str(p) for p in err.path) or "<root>"
        errors.append(f"schema: {loc}: {err.message}")

    # 2. Filename ↔ slug consistency
    expected = f"{meta.get('slug', '')}.md"
    if path.name != expected:
        errors.append(f"filename: expected '{expected}', got '{path.name}'")

    layer = str(meta.get("layer", "0"))
    verdict = meta.get("verdict") or {}
    authored_score = meta.get("score")
    max_score = meta.get("max_score")

    # 3. Composite formula
    if verdict and layer in ("0", "1"):
        expected_composite = composite_from_verdict(verdict, layer)
        if authored_score != expected_composite:
            errors.append(
                f"score: expected {expected_composite} from "
                f"{'V+E+R+D+I+C+T' if layer == '1' else 'V+R+D+I+C+T'} "
                f"(Layer {layer}), got {authored_score}"
            )

    # 4. max_score matches layer
    expected_max = 100 if layer == "1" else 85
    if max_score != expected_max:
        errors.append(f"max_score: Layer {layer} requires {expected_max}, got {max_score}")

    # 5. E-dimension layer rule
    e_block = verdict.get("e") or {}
    e_score = e_block.get("score")
    if layer == "0" and e_score is not None:
        errors.append("verdict.e.score: must be null at Layer 0")
    if layer == "1" and e_score is None:
        errors.append("verdict.e.score: must be integer at Layer 1")

    # 6. CISA KEV Protocol
    kev = meta.get("cisa_kev") or {}
    kev_present = kev.get("present", False)
    kev_entries = kev.get("entries") or []
    if kev_present and not kev_entries:
        errors.append("cisa_kev: present=true but entries is empty")
    if not kev_present and kev_entries:
        errors.append("cisa_kev: present=false but entries is non-empty")
    if kev_present:
        for section in KEV_REQUIRED_SECTIONS:
            text = section_text(body, section)
            if "KEV" not in text and "kev" not in text:
                errors.append(
                    f"cisa_kev: 'KEV' not mentioned in '{section}' section "
                    f"(required in Scorecard / Incident Timeline / Executive Summary / Contextual Analysis)"
                )

    # 7. Bias Disclosure verbatim check
    if BIAS_DISCLOSURE_VERBATIM not in body:
        errors.append(
            "bias_disclosure: verbatim wording missing from body "
            "(see ENGINE.md mandated text)"
        )

    # 8. Rating auto-consistency
    for axis in AXIS_WRITE_ORDER_FOR_VALIDATION:
        block = verdict.get(axis) or {}
        if not block:
            continue
        s = block.get("score")
        authored_rating = block.get("rating")
        expected_rating = rating_for(s, axis)
        if authored_rating is not None and authored_rating != expected_rating:
            errors.append(
                f"verdict.{axis}.rating: expected '{expected_rating}' from "
                f"score {s}/{AXIS_MAX[axis]}, got '{authored_rating}'"
            )

    # 9. next_review_due
    base = normalized.get("updated_at") or normalized.get("evaluated_at")
    next_due = normalized.get("next_review_due")
    if base and next_due:
        expected_due = plus_days(base, REVIEW_CADENCE_DAYS)
        if next_due != expected_due:
            errors.append(
                f"next_review_due: expected {expected_due} "
                f"(base + {REVIEW_CADENCE_DAYS}d; base = updated_at if present "
                f"else evaluated_at), got {next_due}"
            )

    # 10. Differential evaluations
    if meta.get("evaluation_type") == "update":
        diff = meta.get("differential")
        if not isinstance(diff, dict):
            errors.append("differential: must be an object for evaluation_type=update")
        else:
            for axis in LAYER_0_AXES:
                if diff.get(axis) not in ("re-evaluated", "carried-forward"):
                    errors.append(
                        f"differential.{axis}: must be 're-evaluated' or 'carried-forward' "
                        f"for update evaluations"
                    )

    return errors


AXIS_WRITE_ORDER_FOR_VALIDATION = ["v", "r", "d", "i", "c", "t", "e"]


# ─── Entry point ───────────────────────────────────────────────────────────

def main() -> int:
    if not SCHEMA_PATH.exists():
        sys.stderr.write(f"Schema not found: {SCHEMA_PATH}\n")
        return 2
    schema = json.loads(SCHEMA_PATH.read_text(encoding="utf-8"))
    validator = Draft202012Validator(schema)

    args = sys.argv[1:]
    if args:
        paths = [Path(a).resolve() for a in args]
    else:
        paths = [p for p in sorted(PLATFORMS_DIR.glob("*.md")) if not p.name.startswith("_")]

    total_errors = 0
    for path in paths:
        if not path.exists():
            print(f"❌ {path}: file not found")
            total_errors += 1
            continue
        errors = validate_file(path, validator)
        if errors:
            print(f"❌ {path.name}")
            for e in errors:
                print(f"   - {e}")
            total_errors += len(errors)
        else:
            print(f"✓  {path.name}")

    if total_errors:
        print(f"\n{total_errors} error(s) across {len(paths)} file(s).")
        return 1
    print(f"\nAll {len(paths)} file(s) valid.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
