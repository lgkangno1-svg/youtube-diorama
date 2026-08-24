#!/usr/bin/env python3
"""Build the complete zero-LLM production bundle for one Tiny Cat Kitchen episode.

Usage:
  python tools/build_episode_bundle.py episodes/TK-001.yaml

Pipeline:
1. Run deterministic originality validation. Abort on failure.
2. Build the Google Flow prompt pack.
3. Build the YouTube publish pack.
4. Write a compact bundle index with two human approval gates.

No API calls, LLM calls, Flow generations, or uploads are performed.
"""
from __future__ import annotations

import argparse
import subprocess
import sys
from pathlib import Path
from typing import Any

import yaml


def run(cmd: list[str]) -> None:
    print("+", " ".join(cmd))
    subprocess.run(cmd, check=True)


def load_manifest(path: Path) -> dict[str, Any]:
    return yaml.safe_load(path.read_text(encoding="utf-8")) or {}


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("manifest", type=Path)
    parser.add_argument("--generated-dir", type=Path, default=Path("generated"))
    args = parser.parse_args()

    manifest = args.manifest
    data = load_manifest(manifest)
    episode_id = data.get("episode_id")
    if not episode_id:
        print("ERROR: manifest requires episode_id", file=sys.stderr)
        return 2

    root = Path(__file__).resolve().parent.parent
    generated_dir = args.generated_dir
    if not generated_dir.is_absolute():
        generated_dir = root / generated_dir
    generated_dir.mkdir(parents=True, exist_ok=True)

    python = sys.executable
    tools = root / "tools"
    manifest_abs = manifest if manifest.is_absolute() else root / manifest

    try:
        run([python, str(tools / "validate_episode_originality.py"), str(manifest_abs)])
    except subprocess.CalledProcessError:
        print("\nBUILD STOPPED: originality validation failed. No prompt or publish pack was created.", file=sys.stderr)
        return 1

    flow_pack = generated_dir / f"{episode_id}_flow_pack.md"
    publish_pack = generated_dir / f"{episode_id}_publish_pack.md"
    bundle_index = generated_dir / f"{episode_id}_bundle.md"

    run([python, str(tools / "build_flow_pack.py"), str(manifest_abs), "--out", str(flow_pack)])
    run([python, str(tools / "build_publish_pack.py"), str(manifest_abs), "--out", str(publish_pack)])

    title = data.get("title", "")
    hook = data.get("hook", "")
    signature = data.get("creator_signature", {}).get("signature_line", "")
    strategy = data.get("flow_strategy", {}) or {}
    planned = int(strategy.get("max_lite_generations_first_pass") or len(data.get("scenes", [])) or 4)
    non_ultra = int(strategy.get("non_ultra_credit_budget_first_pass") or planned * 10)
    ultra = int(strategy.get("ultra_credit_budget_first_pass") or planned * 5)
    keyframe_count = int(strategy.get("keyframe_count") or len(data.get("keyframes", {})) or 0)
    pacing = strategy.get("pacing", "controlled")
    narration_policy = strategy.get("narration_policy", "none_by_default")

    bundle_index.write_text(
        "\n".join(
            [
                f"# {episode_id} — Production Bundle",
                "",
                "> Generated locally with zero LLM/API/Flow usage.",
                "",
                "## Approval A — before spending Flow credits",
                "",
                f"- Title: {title}",
                f"- Hook: {hook}",
                f"- Creator signature: {signature or 'none'}",
                f"- Pacing: {pacing}",
                f"- Narration policy: {narration_policy}",
                f"- Flow pack: `{flow_pack.relative_to(root)}`",
                f"- Approve {keyframe_count} free keyframes/contact sheet.",
                "- Verify Flow output count is 1 before each generation.",
                f"- Planned first-pass spend: {planned} × Veo 3.1 Lite = {non_ultra} credits non-Ultra / {ultra} Ultra.",
                "- Unused daily credits are not a target; spend them only on a clearly failed shot or a separate validated episode.",
                "",
                "## Approval B — before upload",
                "",
                f"- Publish pack: `{publish_pack.relative_to(root)}`",
                "- Check first 0.5–1.0s readability and cat/tool/scale continuity.",
                "- Check that the final pace still feels calm after editing; do not create urgency with unnecessary cuts.",
                "- Default to no narration. If voice is used, record it in post and keep it episode-specific.",
                "- Set AI disclosure as required for photorealistic synthetic footage.",
                "- Do not mark paid promotion or add Shopping/product tags unless the relationship and Studio eligibility are real.",
                "",
                "## After publishing",
                "",
                "- Enter a 24h row and a 72h row in `analytics/shorts_metrics_v2.csv`.",
                "- Reinvest Flow credits based on engaged-quality diagnostics, not raw public views alone.",
                "",
            ]
        ),
        encoding="utf-8",
    )

    print("\nREADY")
    print(bundle_index)
    print(flow_pack)
    print(publish_pack)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
