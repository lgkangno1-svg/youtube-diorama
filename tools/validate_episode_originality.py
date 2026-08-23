#!/usr/bin/env python3
"""Validate one episode against nearby manifests without spending AI tokens.

Usage:
  python tools/validate_episode_originality.py episodes/TK-003.yaml

Checks:
- creator signature exists
- generic resolution keyframe exists (legacy twist keyframe accepted with warning)
- fingerprint differs in at least 3 of 5 fields from each of the previous five episode files
- exact ending/conflict pair is not reused
"""

from __future__ import annotations

import argparse
from pathlib import Path
from typing import Any

import yaml

FINGERPRINT_KEYS = [
    "hook_mechanic",
    "dominant_visual",
    "conflict_mechanic",
    "emotional_turn",
    "ending_mechanic",
]


def load(path: Path) -> dict[str, Any]:
    return yaml.safe_load(path.read_text(encoding="utf-8")) or {}


def episode_number(path: Path) -> int:
    stem = path.stem
    try:
        return int(stem.split("-")[-1])
    except ValueError:
        return 10**9


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("manifest", type=Path)
    args = parser.parse_args()

    current_path = args.manifest
    current = load(current_path)
    errors: list[str] = []
    warnings: list[str] = []

    signature = current.get("creator_signature", {})
    if not signature.get("narrator_angle") or not signature.get("signature_line"):
        errors.append("creator_signature requires narrator_angle and signature_line")

    keyframes = current.get("keyframes", {})
    if "KF4_RESOLUTION" not in keyframes:
        if "KF4_TWIST" in keyframes:
            warnings.append("legacy KF4_TWIST found; migrate to KF4_RESOLUTION")
        else:
            errors.append("missing KF4_RESOLUTION")

    current_fp = current.get("episode_fingerprint", {})
    missing_fp = [k for k in FINGERPRINT_KEYS if not current_fp.get(k)]
    if missing_fp:
        errors.append("missing fingerprint fields: " + ", ".join(missing_fp))

    all_paths = sorted(current_path.parent.glob("TK-*.yaml"), key=episode_number)
    prior = [p for p in all_paths if episode_number(p) < episode_number(current_path)][-5:]

    current_guard = current.get("originality_guard", {})
    current_pair = (
        current_guard.get("unique_conflict"),
        current_guard.get("unique_ending"),
    )

    for other_path in prior:
        other = load(other_path)
        other_fp = other.get("episode_fingerprint", {})
        same = sum(
            1 for key in FINGERPRINT_KEYS
            if current_fp.get(key) and current_fp.get(key) == other_fp.get(key)
        )
        different = len(FINGERPRINT_KEYS) - same
        if different < 3:
            errors.append(
                f"fingerprint too similar to {other_path.name}: only {different}/5 fields differ"
            )

        other_guard = other.get("originality_guard", {})
        other_pair = (
            other_guard.get("unique_conflict"),
            other_guard.get("unique_ending"),
        )
        if all(current_pair) and current_pair == other_pair:
            errors.append(f"conflict+ending pair duplicates {other_path.name}")

    print(f"Episode: {current.get('episode_id', current_path.stem)}")
    for warning in warnings:
        print(f"WARN: {warning}")
    for error in errors:
        print(f"ERROR: {error}")

    if errors:
        print("RESULT: FAIL")
        return 1

    print("RESULT: PASS")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
