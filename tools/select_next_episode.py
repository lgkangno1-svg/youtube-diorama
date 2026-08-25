#!/usr/bin/env python3
"""Rank Tiny Cat Kitchen episode ideas with production + seasonal timing priors.

This tool does not invent ideas. It ranks ideas already maintained in
ideas/episode_backlog.yaml, skips expired trend windows and stale visual grammar,
and applies a bounded seasonal lead-time boost only when the matching Japanese
evidence ledger entry is still fresh.
"""
from __future__ import annotations

import argparse
from datetime import date
from pathlib import Path
from typing import Any

import yaml

ROOT = Path(__file__).resolve().parent.parent
BACKLOG = ROOT / "ideas" / "episode_backlog.yaml"
SEASONAL_EVIDENCE = ROOT / "research" / "seasonal_evidence.yaml"
CURRENT_VISUAL_GRAMMAR = "POV_PAWS_MICROWORLD_V1"


def load_yaml(path: Path) -> dict[str, Any]:
    if not path.exists():
        return {}
    return yaml.safe_load(path.read_text(encoding="utf-8")) or {}


def parse_date(value: Any) -> date | None:
    if not value:
        return None
    try:
        return date.fromisoformat(str(value))
    except Exception:
        return None


def trend_valid(value: Any, today: date) -> bool:
    if not value:
        return True
    try:
        start_s, end_s = str(value).split("..", 1)
        start = date.fromisoformat(start_s)
        end = date.fromisoformat(end_s)
        return start <= today <= end
    except Exception:
        return True


def production_compatible(candidate: dict[str, Any]) -> tuple[bool, str]:
    """Fail closed on backlog rows that predate the current paw-only POV grammar."""
    grammar = str(candidate.get("visual_grammar") or "")
    if grammar != CURRENT_VISUAL_GRAMMAR:
        return False, f"visual-grammar:{grammar or 'missing'}"

    hero_scale = str(candidate.get("hero_scale") or "").strip()
    if not hero_scale:
        return False, "hero-scale-missing"

    actions = candidate.get("paw_action_family") or []
    if not isinstance(actions, list) or not actions:
        return False, "paw-action-family-missing"

    runtime = str(candidate.get("runtime_prior") or "")
    if runtime not in {"compact_h30", "immersive_h40"}:
        return False, f"runtime-prior:{runtime or 'missing'}"

    return True, "compatible"


def base_score(candidate: dict[str, Any], weights: dict[str, int]) -> float:
    total = 0.0
    max_total = 0.0
    for key, weight in weights.items():
        max_total += 20 * float(weight)
        total += float(candidate.get(key, 0) or 0) * float(weight)
    return round((total / max_total) * 100, 1) if max_total else 0.0


def seasonal_evidence_state(
    candidate: dict[str, Any],
    today: date,
    ledger: dict[str, Any],
) -> tuple[bool, str]:
    evidence_map = ledger.get("evidence", {}) or {}
    entry = evidence_map.get(candidate.get("id"), {}) or {}
    checked = parse_date(entry.get("checked_at"))
    if not checked:
        return False, "evidence-missing"

    max_age = max(
        1,
        int(entry.get("max_age_days", ledger.get("default_max_age_days", 14)) or 14),
    )
    age_days = (today - checked).days
    if age_days < 0:
        return False, f"evidence-future:{abs(age_days)}d"
    if age_days > max_age:
        return False, f"evidence-stale:{age_days}d"
    return True, f"evidence-fresh:{age_days}d"


def seasonal_adjustment(
    candidate: dict[str, Any],
    today: date,
    defaults: dict[str, Any],
    evidence_ledger: dict[str, Any],
) -> tuple[float, str, str]:
    config = candidate.get("seasonality") or {}
    if not isinstance(config, dict) or not config:
        return 0.0, "evergreen", "not-required"

    evidence_ok, evidence_state = seasonal_evidence_state(candidate, today, evidence_ledger)

    peak_start = parse_date(config.get("peak_start"))
    if not peak_start:
        return 0.0, "season-date-missing", evidence_state
    peak_end = parse_date(config.get("peak_end")) or peak_start
    if peak_end < peak_start:
        peak_end = peak_start

    lead_days = max(1, int(config.get("lead_days", defaults.get("default_lead_days", 35)) or 35))
    tail_days = max(0, int(config.get("tail_days", defaults.get("default_tail_days", 7)) or 0))
    searchability = max(0.0, min(20.0, float(config.get("searchability", 0) or 0)))
    max_boost = max(0.0, float(config.get("max_boost_points", defaults.get("max_boost_points", 8)) or 0))

    if today < peak_start:
        days_to_peak = (peak_start - today).days
        if days_to_peak > lead_days:
            timing_factor = 0.0
            phase = f"too-early:{days_to_peak}d"
        elif days_to_peak >= 22:
            timing_factor = 0.45
            phase = f"early-lead:{days_to_peak}d"
        elif days_to_peak >= 8:
            timing_factor = 1.0
            phase = f"sweet-spot:{days_to_peak}d"
        else:
            timing_factor = 0.85
            phase = f"final-lead:{days_to_peak}d"
    elif today <= peak_end:
        timing_factor = 0.70
        phase = "in-peak"
    else:
        days_after_peak = (today - peak_end).days
        if days_after_peak <= tail_days:
            timing_factor = 0.20
            phase = f"tail:{days_after_peak}d"
        else:
            timing_factor = 0.0
            phase = f"post-season:{days_after_peak}d"

    if not evidence_ok:
        return 0.0, phase, evidence_state

    adjustment = max_boost * (searchability / 20.0) * timing_factor
    return round(adjustment, 1), phase, evidence_state


def final_score(base: float, seasonal_boost: float) -> float:
    return round(min(100.0, base + seasonal_boost), 1)


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--top", type=int, default=3)
    parser.add_argument("--date", help="Override today's date (YYYY-MM-DD) for deterministic seasonal checks.")
    args = parser.parse_args()

    data = load_yaml(BACKLOG)
    evidence_ledger = load_yaml(SEASONAL_EVIDENCE)
    weights = data.get("scoring", {}) or {}
    seasonal_defaults = data.get("seasonal_ranking", {}) or {}
    today = date.fromisoformat(args.date) if args.date else date.today()
    ranked = []
    rejected = []

    for candidate in data.get("candidates", []):
        if candidate.get("status") not in {"candidate", "ready", "priority_candidate"}:
            continue
        compatible, compatibility_state = production_compatible(candidate)
        if not compatible:
            rejected.append((candidate.get("id", "?"), compatibility_state))
            continue
        if not trend_valid(candidate.get("trend_window"), today):
            continue
        base = base_score(candidate, weights)
        seasonal_boost, phase, evidence_state = seasonal_adjustment(
            candidate,
            today,
            seasonal_defaults,
            evidence_ledger,
        )
        ranked.append(
            (
                final_score(base, seasonal_boost),
                base,
                seasonal_boost,
                phase,
                evidence_state,
                candidate,
            )
        )

    ranked.sort(key=lambda item: (item[0], item[1]), reverse=True)

    if not ranked:
        print("No eligible ideas under the current POV paw-only production grammar. Refresh the backlog before production.")
        if rejected:
            print("Rejected stale candidates: " + ", ".join(f"{idea}({reason})" for idea, reason in rejected))
        return

    print(f"Tiny Cat Kitchen next-episode candidates — {today.isoformat()}\n")
    for idx, (value, base, boost, phase, evidence_state, item) in enumerate(ranked[: max(1, args.top)], 1):
        print(f"{idx}. {item.get('id')} — {value}/100 (base {base} + seasonal {boost})")
        print(f"   {item.get('working_title_ja', '')}")
        print(f"   premise: {item.get('premise', '')}")
        print(f"   visual_grammar: {item.get('visual_grammar')}")
        print(f"   hero_scale: {item.get('hero_scale')}")
        print(f"   paw_actions: {', '.join(item.get('paw_action_family', []))}")
        print(f"   runtime_prior: {item.get('runtime_prior')}")
        print(f"   narration: {item.get('narration_recommendation', 'none')}")
        print(f"   trend_window: {item.get('trend_window') or 'evergreen'}")
        print(f"   seasonal_phase: {phase}")
        print(f"   seasonal_evidence: {evidence_state}")
        print(f"   flow_reliability: {item.get('flow_reliability', 'n/a')}/20")
        print(f"   expected_credit_efficiency: {item.get('expected_credit_efficiency', 'n/a')}/20")
        print()

    if rejected:
        print(f"Rejected {len(rejected)} stale candidate(s) that do not match {CURRENT_VISUAL_GRAMMAR}.")
    print("Selection is not automatic production approval.")
    print("ChatGPT should refresh stale seasonal evidence and compare the winner with the last five episode fingerprints before creating the manifest.")


if __name__ == "__main__":
    main()
