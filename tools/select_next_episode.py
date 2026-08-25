#!/usr/bin/env python3
"""Rank Tiny Cat Kitchen episode ideas with production + seasonal timing priors.

Usage:
  python tools/select_next_episode.py
  python tools/select_next_episode.py --top 5
  python tools/select_next_episode.py --date 2026-09-10

This tool does not invent ideas. It ranks ideas already maintained in
ideas/episode_backlog.yaml, skips expired trend windows, and applies a bounded
seasonal lead-time boost when a candidate has explicit seasonality metadata.
"""
from __future__ import annotations

import argparse
from datetime import date
from pathlib import Path
from typing import Any

import yaml

ROOT = Path(__file__).resolve().parent.parent
BACKLOG = ROOT / "ideas" / "episode_backlog.yaml"


def load() -> dict[str, Any]:
    return yaml.safe_load(BACKLOG.read_text(encoding="utf-8")) or {}


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


def base_score(candidate: dict[str, Any], weights: dict[str, int]) -> float:
    total = 0.0
    max_total = 0.0
    for key, weight in weights.items():
        max_total += 20 * float(weight)
        total += float(candidate.get(key, 0) or 0) * float(weight)
    return round((total / max_total) * 100, 1) if max_total else 0.0


def seasonal_adjustment(
    candidate: dict[str, Any],
    today: date,
    defaults: dict[str, Any],
) -> tuple[float, str]:
    """Return bounded +points and a human-readable timing phase.

    The highest boost is intentionally before the peak rather than on the
    event day. This lets the operator publish while audience interest/search
    intent is rising, without allowing seasonality to override poor Flow
    reliability or weak visual payoff.
    """
    config = candidate.get("seasonality") or {}
    if not isinstance(config, dict) or not config:
        return 0.0, "evergreen"

    peak_start = parse_date(config.get("peak_start"))
    if not peak_start:
        return 0.0, "season-date-missing"
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

    adjustment = max_boost * (searchability / 20.0) * timing_factor
    return round(adjustment, 1), phase


def final_score(base: float, seasonal_boost: float) -> float:
    return round(min(100.0, base + seasonal_boost), 1)


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--top", type=int, default=3)
    parser.add_argument(
        "--date",
        help="Override today's date (YYYY-MM-DD) for deterministic seasonal checks.",
    )
    args = parser.parse_args()

    data = load()
    weights = data.get("scoring", {}) or {}
    seasonal_defaults = data.get("seasonal_ranking", {}) or {}
    today = date.fromisoformat(args.date) if args.date else date.today()
    ranked = []

    for candidate in data.get("candidates", []):
        if candidate.get("status") not in {"candidate", "ready", "priority_candidate"}:
            continue
        if not trend_valid(candidate.get("trend_window"), today):
            continue
        base = base_score(candidate, weights)
        seasonal_boost, phase = seasonal_adjustment(candidate, today, seasonal_defaults)
        ranked.append((final_score(base, seasonal_boost), base, seasonal_boost, phase, candidate))

    ranked.sort(key=lambda item: (item[0], item[1]), reverse=True)

    if not ranked:
        print("No eligible ideas. Ask ChatGPT to refresh benchmark research and the backlog.")
        return

    print(f"Tiny Cat Kitchen next-episode candidates — {today.isoformat()}\n")
    for idx, (value, base, boost, phase, item) in enumerate(ranked[: max(1, args.top)], 1):
        print(f"{idx}. {item.get('id')} — {value}/100 (base {base} + seasonal {boost})")
        print(f"   {item.get('working_title_ja', '')}")
        print(f"   premise: {item.get('premise', '')}")
        print(f"   narration: {item.get('narration_recommendation', 'none')}")
        print(f"   trend_window: {item.get('trend_window') or 'evergreen'}")
        print(f"   seasonal_phase: {phase}")
        print(f"   flow_reliability: {item.get('flow_reliability', 'n/a')}/20")
        print(f"   expected_credit_efficiency: {item.get('expected_credit_efficiency', 'n/a')}/20")
        print()

    print("Selection is not automatic production approval.")
    print("ChatGPT should still verify current Japanese evidence and compare the winner with the last five episode fingerprints before creating the manifest.")


if __name__ == "__main__":
    main()
