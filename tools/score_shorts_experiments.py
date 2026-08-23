#!/usr/bin/env python3
"""Score Tiny Cat Kitchen Shorts experiments from YouTube Studio metrics.

Uses Python stdlib only. Designed for post-2026-08-24 Shorts analytics where
public views begin at playback start, while engaged/qualified views remain the
better optimization target for YPP and retention decisions.
"""

from __future__ import annotations

import csv
import math
import sys
from pathlib import Path

REQUIRED = [
    "episode_id",
    "published_at",
    "public_views",
    "engaged_views",
    "stayed_to_watch_pct",
    "avg_percentage_viewed_pct",
    "likes",
    "comments",
    "subscribers_gained",
]


def f(row, key):
    try:
        return float(row.get(key, "") or 0)
    except ValueError:
        return 0.0


def safe_rate(n, d, scale=1.0):
    return (n / d * scale) if d > 0 else 0.0


def percentile_rank(values, x):
    vals = [v for v in values if not math.isnan(v)]
    if len(vals) <= 1:
        return 50.0
    less = sum(v < x for v in vals)
    equal = sum(v == x for v in vals)
    return 100.0 * (less + 0.5 * equal) / len(vals)


def diagnosis(stw_rank, apv_rank, sub_rank):
    hi = 60
    lo = 40
    if stw_rank <= lo and apv_rank >= hi:
        return "HOOK_FIX_ONLY"
    if stw_rank >= hi and apv_rank <= lo:
        return "MIDDLE_RETENTION_FIX"
    if stw_rank >= hi and apv_rank >= hi and sub_rank <= lo:
        return "IP_CONVERSION_FIX"
    if stw_rank <= lo and apv_rank <= lo:
        return "STOP_SPENDING_RETHINK_HYPOTHESIS"
    return "KEEP_TESTING"


def main(path_str: str) -> int:
    path = Path(path_str)
    if not path.exists():
        print(f"Missing file: {path}", file=sys.stderr)
        return 2

    with path.open("r", encoding="utf-8-sig", newline="") as fh:
        rows = list(csv.DictReader(fh))

    if not rows:
        print("No rows found.", file=sys.stderr)
        return 2

    missing = [c for c in REQUIRED if c not in rows[0]]
    if missing:
        print("Missing columns: " + ", ".join(missing), file=sys.stderr)
        return 2

    enriched = []
    for r in rows:
        engaged = f(r, "engaged_views")
        public = f(r, "public_views")
        item = dict(r)
        item["engaged_per_100_public"] = safe_rate(engaged, public, 100)
        item["subs_per_1000_engaged"] = safe_rate(f(r, "subscribers_gained"), engaged, 1000)
        item["likes_per_1000_engaged"] = safe_rate(f(r, "likes"), engaged, 1000)
        item["comments_per_1000_engaged"] = safe_rate(f(r, "comments"), engaged, 1000)
        item["stw"] = f(r, "stayed_to_watch_pct")
        item["apv"] = f(r, "avg_percentage_viewed_pct")
        enriched.append(item)

    stw_vals = [r["stw"] for r in enriched]
    apv_vals = [r["apv"] for r in enriched]
    sub_vals = [r["subs_per_1000_engaged"] for r in enriched]
    engaged_vals = [f(r, "engaged_views") for r in enriched]

    for r in enriched:
        r["stw_rank"] = percentile_rank(stw_vals, r["stw"])
        r["apv_rank"] = percentile_rank(apv_vals, r["apv"])
        r["sub_rank"] = percentile_rank(sub_vals, r["subs_per_1000_engaged"])
        r["engaged_rank"] = percentile_rank(engaged_vals, f(r, "engaged_views"))
        # Relative within-channel exploration score. Avoids hard-coded universal thresholds.
        r["score"] = (
            0.35 * r["stw_rank"]
            + 0.35 * r["apv_rank"]
            + 0.20 * r["sub_rank"]
            + 0.10 * r["engaged_rank"]
        )
        r["diagnosis"] = diagnosis(r["stw_rank"], r["apv_rank"], r["sub_rank"])

    enriched.sort(key=lambda x: x["score"], reverse=True)

    print("episode\tscore\tSTW\tAPV\tengaged\tsubs/1k-eng\tdiagnosis")
    for r in enriched:
        print(
            f"{r['episode_id']}\t{r['score']:.1f}\t{r['stw']:.1f}%\t{r['apv']:.1f}%\t"
            f"{int(f(r, 'engaged_views'))}\t{r['subs_per_1000_engaged']:.2f}\t{r['diagnosis']}"
        )

    print("\nDecision legend:")
    print("HOOK_FIX_ONLY = regenerate/re-edit OPEN only; do not reroll all Flow clips")
    print("MIDDLE_RETENTION_FIX = redesign DANGER/PAYOFF only")
    print("IP_CONVERSION_FIX = improve creator signature/lore/callback")
    print("STOP_SPENDING_RETHINK_HYPOTHESIS = do not spend more Flow credits on this concept")
    print("KEEP_TESTING = no single dominant failure yet")
    return 0


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python tools/score_shorts_experiments.py analytics/shorts_metrics.csv", file=sys.stderr)
        raise SystemExit(2)
    raise SystemExit(main(sys.argv[1]))
