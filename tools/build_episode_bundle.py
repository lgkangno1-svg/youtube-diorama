#!/usr/bin/env python3
"""Build the complete zero-LLM production bundle for one Tiny Cat Kitchen episode.

Usage:
  python tools/build_episode_bundle.py episodes/TK-001.yaml

Pipeline:
1. Require the canonical repository manifest for the requested episode.
2. Run deterministic current-production-standard validation. Abort on failure.
3. Run deterministic originality validation. Abort on failure.
4. Build the Google Flow prompt pack.
5. Build a deterministic healing edit plan.
6. Build the YouTube publish pack.
7. Write a compact bundle index with two human approval gates.

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


def canonical_manifest_path(root: Path, episode_id: str) -> Path:
    return (root / "episodes" / f"{episode_id}.yaml").resolve()


def runtime_guidance(data: dict[str, Any]) -> str:
    """Return operator guidance that respects the manifest's runtime policy."""
    runtime = data.get("runtime_strategy", {}) or {}
    mode = str(runtime.get("mode") or "adaptive")
    scenes = data.get("scenes", []) or []

    if mode == "compact_h30":
        return (
            "- Runtime mode: `compact_h30`. Normally finish after G3 when the tactile journey is complete; "
            "do not add a G4 merely to make the Short longer."
        )
    if mode == "immersive_h40":
        fourth_value = str(runtime.get("fourth_beat_value") or "independent world-resolution beat")
        return (
            "- Runtime mode: `immersive_h40`. G4 is part of the current plan only after G3 PASS and only while "
            f"its documented independent value remains real (`{fourth_value}`). Do not drop it merely to force H30, "
            "and do not keep it if real footage turns it into padding."
        )

    return (
        f"- Runtime mode: `{mode}` with {len(scenes)} planned scene(s). Follow the manifest/Flow pack scene count; "
        "do not assume a fixed H30 or H40 length."
    )


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("manifest", type=Path)
    parser.add_argument("--generated-dir", type=Path, default=Path("generated"))
    args = parser.parse_args()

    root = Path(__file__).resolve().parent.parent
    manifest = args.manifest
    manifest_abs = (manifest if manifest.is_absolute() else root / manifest).resolve()
    if not manifest_abs.exists():
        print(f"ERROR: manifest not found: {manifest_abs}", file=sys.stderr)
        return 2

    data = load_manifest(manifest_abs)
    episode_id = str(data.get("episode_id") or "").strip()
    if not episode_id:
        print("ERROR: manifest requires episode_id", file=sys.stderr)
        return 2

    # The bundle builder is a production entry point, so it must never accept a
    # copied/temporary manifest that bypasses repository validation. The canonical
    # episodes/TK-XXX.yaml file is the only production manifest source.
    canonical = canonical_manifest_path(root, episode_id)
    if manifest_abs != canonical:
        print(
            "BUILD STOPPED: production bundles must use the canonical repository manifest "
            f"{canonical}. Received {manifest_abs}. No production pack was created.",
            file=sys.stderr,
        )
        return 2

    python = sys.executable
    tools = root / "tools"

    # Current-standard validation must live inside the bundle builder itself. This
    # closes bypasses through direct `make_short.ps1` or direct Python invocation;
    # callers do not get to opt out of maker-view/scale/runtime/credit/frame/action
    # gates. Use the canonical maker-view adapter rather than the legacy structural
    # validator directly, because the adapter enforces current semantics and then
    # delegates the mature structural/runtime checks safely.
    try:
        run([python, str(tools / "validate_maker_view_manifest.py"), episode_id])
    except subprocess.CalledProcessError:
        print("\nBUILD STOPPED: current maker-view production-standard validation failed. No production pack was created.", file=sys.stderr)
        return 1

    try:
        run([python, str(tools / "validate_episode_originality.py"), str(manifest_abs)])
    except subprocess.CalledProcessError:
        print("\nBUILD STOPPED: originality validation failed. No production pack was created.", file=sys.stderr)
        return 1

    generated_dir = args.generated_dir
    if not generated_dir.is_absolute():
        generated_dir = root / generated_dir
    generated_dir.mkdir(parents=True, exist_ok=True)

    flow_pack = generated_dir / f"{episode_id}_flow_pack.md"
    edit_plan = generated_dir / f"{episode_id}_edit_plan.md"
    publish_pack = generated_dir / f"{episode_id}_publish_pack.md"
    bundle_index = generated_dir / f"{episode_id}_bundle.md"

    run([python, str(tools / "build_flow_pack.py"), str(manifest_abs), "--out", str(flow_pack)])
    run([python, str(tools / "build_healing_edit_plan.py"), str(manifest_abs), "--out", str(edit_plan)])
    run([python, str(tools / "build_publish_pack.py"), str(manifest_abs), "--out", str(publish_pack)])

    title = data.get("title", "")
    hook = data.get("hook", "")
    signature = data.get("creator_signature", {}).get("signature_line", "")
    strategy = data.get("flow_strategy", {}) or {}
    post = data.get("post_production", {}) or {}
    runtime = data.get("runtime_strategy", {}) or {}
    runtime_mode = runtime.get("mode", "adaptive")
    target_runtime = post.get("preferred_final_runtime_seconds") or runtime.get("target_final_runtime_seconds") or []
    planned = int(strategy.get("max_lite_generations_first_pass") or len(data.get("scenes", [])) or 4)
    non_ultra = int(strategy.get("non_ultra_credit_budget_first_pass") or planned * 10)
    ultra = int(strategy.get("ultra_credit_budget_first_pass") or planned * 5)
    keyframe_count = int(strategy.get("keyframe_count") or len(data.get("keyframes", {})) or 0)
    pacing = strategy.get("pacing", "controlled")
    narration_policy = strategy.get("narration_policy", post.get("narration_default", "none_by_default"))
    motion_density = int(post.get("target_motion_density_pct_min", 0) or 0)
    if isinstance(target_runtime, (list, tuple)) and len(target_runtime) == 2:
        runtime_target_text = f"{target_runtime[0]}–{target_runtime[1]}s"
    elif target_runtime:
        runtime_target_text = str(target_runtime)
    else:
        runtime_target_text = "manifest-defined"

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
                f"- Runtime mode: {runtime_mode}",
                f"- Preferred final runtime: {runtime_target_text}",
                f"- Pacing: {pacing}",
                f"- Narration policy: {narration_policy}",
                f"- Flow pack: `{flow_pack.relative_to(root)}`",
                f"- Edit plan: `{edit_plan.relative_to(root)}`",
                f"- Approve {keyframe_count} planned keyframes/contact sheet only after Flow is set to `Nano Banana 2 Lite` and the UI confirms no charge.",
                "- If the active image model or displayed keyframe cost is different or unclear, STOP; do not treat Gate A as free.",
                "- Verify Flow output count is 1 before each generation.",
                f"- Planned first-pass spend: {planned} × Veo 3.1 Lite = {non_ultra} credits non-Ultra / {ultra} Ultra.",
                "- Unused daily credits are not a target; spend them only on a clearly failed shot or a separate validated episode.",
                "",
                "## Approval B — before upload",
                "",
                f"- Publish pack: `{publish_pack.relative_to(root)}`",
                f"- Keep moving-footage density at or above {motion_density}% when specified; calm does not mean static.",
                runtime_guidance(data),
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
    print(edit_plan)
    print(publish_pack)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
