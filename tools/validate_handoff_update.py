#!/usr/bin/env python3
"""Fail when a repository change is not accompanied by PROJECT_HANDOFF.md.

This is intentionally local/deterministic and does not require GitHub Actions.

Typical usage before opening or merging a PR:

    python tools/validate_handoff_update.py --base origin/main

For connector/remote workflows, the same policy still applies conceptually: every
material branch/PR that changes repository state must update PROJECT_HANDOFF.md
in that same branch/PR.
"""
from __future__ import annotations

import argparse
import subprocess
import sys
from pathlib import Path

HANDOFF = "PROJECT_HANDOFF.md"
# Generated operator bundles are reproducible artifacts and do not represent a
# durable project-state change by themselves.
IGNORED_PREFIXES = ("generated/",)


def git_lines(*args: str) -> set[str]:
    try:
        result = subprocess.run(
            ["git", *args],
            check=True,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            text=True,
            encoding="utf-8",
        )
    except (OSError, subprocess.CalledProcessError) as exc:
        detail = getattr(exc, "stderr", "") or str(exc)
        raise RuntimeError(detail.strip()) from exc
    return {line.strip().replace("\\", "/") for line in result.stdout.splitlines() if line.strip()}


def relevant(path: str) -> bool:
    if path == HANDOFF:
        return False
    return not any(path.startswith(prefix) for prefix in IGNORED_PREFIXES)


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--base",
        default="origin/main",
        help="Base ref used for committed branch changes (default: origin/main)",
    )
    args = parser.parse_args()

    try:
        committed = git_lines("diff", "--name-only", f"{args.base}...HEAD")
        staged = git_lines("diff", "--cached", "--name-only")
        unstaged = git_lines("diff", "--name-only")
    except RuntimeError as exc:
        print(f"HANDOFF CHECK ERROR: {exc}", file=sys.stderr)
        print("Use a valid --base ref, e.g. --base main or --base origin/main.", file=sys.stderr)
        return 2

    changed = committed | staged | unstaged
    durable_changes = sorted(path for path in changed if relevant(path))
    handoff_changed = HANDOFF in changed

    if not durable_changes:
        print("HANDOFF CHECK PASS — no durable repository change requires a handoff update.")
        return 0

    if not handoff_changed:
        print("HANDOFF CHECK FAIL — repository changed without PROJECT_HANDOFF.md.")
        print("Durable changed files:")
        for path in durable_changes:
            print(f"- {path}")
        print("Update PROJECT_HANDOFF.md in the same branch/PR before considering the change complete.")
        return 1

    print("HANDOFF CHECK PASS — PROJECT_HANDOFF.md accompanies this repository change.")
    print(f"Durable changed files: {len(durable_changes)}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
