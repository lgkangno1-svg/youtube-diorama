#!/usr/bin/env python3
"""Rank benchmark-derived Tiny Cat Kitchen episode ideas without an LLM.

Usage:
  python tools/select_next_episode.py
  python tools/select_next_episode.py --top 5

This tool does not invent ideas. It ranks the ideas already maintained in
ideas/episode_backlog.yaml by the project scoring weights and skips candidates
whose trend window has expired.
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


def score(candidate: dict[str, Any], weights: dict[str, int]) -> float:
    total = 0.0
    max_total = 0.0
    for key, weight in weights.items():
        max_total += 20 * float(weight)
        total += float(candidate.get(key, 0) or 0) * float(weight)
    return round((total / max_total) * 100, 1) if max_total else 0.0


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--top", type=int, default=3)
    args = parser.parse_args()

    data = load()
    weights = data.get("scoring", {}) or {}
    today = date.today()
    ranked = []

    for candidate in data.get("candidates", []):
        if candidate.get("status") not in {"candidate", "ready"}:
            continue
        if not trend_valid(candidate.get("trend_window"), today):
            continue
        ranked.append((score(candidate, weights), candidate))

    ranked.sort(key=lambda item: item[0], reverse=True)

    if not ranked:
        print("No eligible ideas. Ask ChatGPT to refresh benchmark research and the backlog.")
        return

    print(f"Tiny Cat Kitchen next-episode candidates — {today.isoformat()}\n")
    for idx, (value, item) in enumerate(ranked[: max(1, args.top)], 1):
        print(f"{idx}. {item.get('id')} — {value}/100")
        print(f"   {item.get('working_title_ja', '')}")
        print(f"   premise: {item.get('premise', '')}")
        print(f"   narration: {item.get('narration_recommendation', 'none')}")
        print(f"   trend_window: {item.get('trend_window') or 'evergreen'}")
        print()

    print("Selection is not automatic production approval.")
    print("ChatGPT should still compare the winner with the last five episode fingerprints before creating the manifest.")


if __name__ == "__main__":
    main()
