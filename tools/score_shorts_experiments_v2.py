#!/usr/bin/env python3
"""Horizon-aware Tiny Cat Kitchen Shorts experiment scorer.

Compare only snapshots with the same observation_hours (24h with 24h, 72h with
72h). Public views are kept as external reach context but excluded from the
internal quality score.
"""

from __future__ import annotations

import csv
import math
import sys
from collections import defaultdict
from pathlib import Path

REQUIRED = [
    "episode_id", "published_at", "observation_hours", "public_views",
    "engaged_views", "stayed_to_watch_pct", "avg_percentage_viewed_pct",
    "likes", "comments", "subscribers_gained",
]


def num(row, key):
    try:
        return float(row.get(key, "") or 0)
    except ValueError:
        return 0.0


def rate(n, d, scale=1.0):
    return (n / d * scale) if d > 0 else 0.0


def percentile(values, x):
    vals = [v for v in values if not math.isnan(v)]
    if len(vals) <= 1:
        return 50.0
    less = sum(v < x for v in vals)
    equal = sum(v == x for v in vals)
    return 100.0 * (less + 0.5 * equal) / len(vals)


def diagnose(stw, apv, subs):
    hi, lo = 60, 40
    if stw <= lo and apv >= hi:
        return "HOOK_FIX_ONLY"
    if stw >= hi and apv <= lo:
        return "MIDDLE_RETENTION_FIX"
    if stw >= hi and apv >= hi and subs <= lo:
        return "IP_CONVERSION_FIX"
    if stw <= lo and apv <= lo:
        return "STOP_SPENDING_RETHINK_HYPOTHESIS"
    return "KEEP_TESTING"


def main(path_str):
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

    cohorts = defaultdict(list)
    for r in rows:
        engaged = num(r, "engaged_views")
        item = dict(r)
        item["hours"] = int(num(r, "observation_hours"))
        item["stw"] = num(r, "stayed_to_watch_pct")
        item["apv"] = num(r, "avg_percentage_viewed_pct")
        item["subs_1k"] = rate(num(r, "subscribers_gained"), engaged, 1000)
        item["comments_1k"] = rate(num(r, "comments"), engaged, 1000)
        item["engaged_100_public"] = rate(engaged, num(r, "public_views"), 100)
        cohorts[item["hours"]].append(item)

    for hours in sorted(cohorts):
        group = cohorts[hours]
        stws = [x["stw"] for x in group]
        apvs = [x["apv"] for x in group]
        subs = [x["subs_1k"] for x in group]
        comments = [x["comments_1k"] for x in group]

        for x in group:
            x["stw_rank"] = percentile(stws, x["stw"])
            x["apv_rank"] = percentile(apvs, x["apv"])
            x["sub_rank"] = percentile(subs, x["subs_1k"])
            x["comment_rank"] = percentile(comments, x["comments_1k"])
            x["score"] = (
                .35 * x["stw_rank"] + .35 * x["apv_rank"]
                + .20 * x["sub_rank"] + .10 * x["comment_rank"]
            )
            x["diagnosis"] = diagnose(x["stw_rank"], x["apv_rank"], x["sub_rank"])

        group.sort(key=lambda x: x["score"], reverse=True)
        print(f"\n=== {hours}h cohort ===")
        print("episode\tscore\tSTW\tAPV\tpublic\tengaged\tsubs/1k\tcomments/1k\tdiagnosis")
        for x in group:
            print(
                f"{x['episode_id']}\t{x['score']:.1f}\t{x['stw']:.1f}%\t{x['apv']:.1f}%\t"
                f"{int(num(x, 'public_views'))}\t{int(num(x, 'engaged_views'))}\t"
                f"{x['subs_1k']:.2f}\t{x['comments_1k']:.2f}\t{x['diagnosis']}"
            )

    print("\nPublic views = reach context only; not included in quality score.")
    return 0


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python tools/score_shorts_experiments_v2.py analytics/shorts_metrics_v2.csv", file=sys.stderr)
        raise SystemExit(2)
    raise SystemExit(main(sys.argv[1]))
