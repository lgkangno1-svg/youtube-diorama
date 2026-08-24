#!/usr/bin/env python3
"""Score Tiny Cat Kitchen production efficiency from analytics/learning_ledger.csv.

The goal is not to reward the cheapest video. It highlights episodes that turn Flow credits
into usable motion, engaged views, and subscribers while keeping rerolls low.

Usage:
  python tools/score_credit_efficiency.py analytics/learning_ledger.csv
"""
from __future__ import annotations

import argparse
import csv
from pathlib import Path


def f(row: dict[str, str], key: str) -> float:
    try:
        return float((row.get(key) or "").strip())
    except ValueError:
        return 0.0


def yn(row: dict[str, str], key: str) -> float:
    value = (row.get(key) or "").strip().lower()
    if value in {"1", "true", "yes", "y", "pass"}:
        return 1.0
    if value in {"0", "false", "no", "n", "fail"}:
        return 0.0
    return 0.5


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("csv_path", type=Path, nargs="?", default=Path("analytics/learning_ledger.csv"))
    args = parser.parse_args()

    if not args.csv_path.exists():
        print(f"missing: {args.csv_path}")
        return 2

    with args.csv_path.open(encoding="utf-8-sig", newline="") as fh:
        rows = list(csv.DictReader(fh))

    if not rows:
        print("No episode data yet. Publish a Short and add 24h/72h rows first.")
        return 0

    print("episode | obs | credits | rerolls | usable_s/credit | engaged/credit | subs/100cr | first-pass | note")
    print("-" * 120)

    for row in rows:
        credits = f(row, "flow_credits_spent")
        engaged = f(row, "engaged_views")
        subs = f(row, "subscribers_gained")
        usable = f(row, "usable_motion_seconds")
        rerolls = f(row, "rerolls")
        obs = int(f(row, "observation_hours"))

        usable_per_credit = usable / credits if credits else 0.0
        engaged_per_credit = engaged / credits if credits else 0.0
        subs_per_100 = (subs / credits * 100.0) if credits else 0.0
        first_pass = (yn(row, "g1_pass_first_try") + yn(row, "g2_pass_first_try") + yn(row, "g3_pass_first_try")) / 3.0

        if credits > 30 and rerolls > 0:
            note = "CUT_REROLLS"
        elif first_pass < 0.67:
            note = "SIMPLIFY_GENERATION"
        elif usable_per_credit < 0.55 and credits:
            note = "LOW_USABLE_MOTION"
        elif obs >= 72 and engaged_per_credit > 0:
            note = "KEEP_AND_COMPARE"
        else:
            note = "COLLECT_MORE_DATA"

        print(
            f"{row.get('episode_id','?'):7} | {obs:3}h | {credits:7.0f} | {rerolls:7.0f} | "
            f"{usable_per_credit:15.2f} | {engaged_per_credit:14.1f} | {subs_per_100:10.2f} | "
            f"{first_pass:10.0%} | {note}"
        )

    print("\nInterpretation:")
    print("- Optimize engaged views and subscribers per credit, not credits/video alone.")
    print("- A low first-pass rate means the next episode should simplify actions/keyframes before buying more generations.")
    print("- Compare 24h rows with 24h rows and 72h rows with 72h rows; do not mix horizons.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
