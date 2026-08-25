#!/usr/bin/env python3
"""Build a no-LLM healing edit plan from an episode YAML manifest."""
from __future__ import annotations

import argparse
from pathlib import Path
from typing import Any
import yaml


def clamp(value: float, lo: float, hi: float) -> float:
    return max(lo, min(hi, value))


def build(data: dict[str, Any]) -> str:
    episode_id = data["episode_id"]
    scenes = data.get("scenes", [])
    post = data.get("post_production", {})
    runtime = data.get("runtime_strategy", {})
    editorial = data.get("editorial_seconds", {})

    preferred = runtime.get("target_final_seconds") or post.get("preferred_final_runtime_seconds", [30, 36])
    target_runtime = sum(preferred) / 2 if isinstance(preferred, list) and len(preferred) == 2 else float(data.get("length_target_seconds", 34))
    target_motion_density = float(post.get("target_motion_density_pct_min", 80)) / 100.0
    max_static = float(post.get("max_total_static_hold_seconds", 5))
    speed_range = post.get("preferred_playback_speed_range", [0.90, 1.00])
    min_speed = float(speed_range[0]) if isinstance(speed_range, list) and speed_range else 0.90

    raw_motion = sum(float(s.get("generation_seconds", 8)) for s in scenes)
    desired_motion = target_runtime * target_motion_density
    required_speed = raw_motion / desired_motion if desired_motion > 0 else 1.0
    chosen_speed = clamp(required_speed, min_speed, 1.0)
    stretched_motion = raw_motion / chosen_speed

    holds = {
        "opening": float(editorial.get("opening_keyframe_hold", 0)),
        "room": float(editorial.get("environmental_room_hold", 0)),
        "danger": float(editorial.get("cliffhanger_freeze", editorial.get("conflict_micro_hold", 0))),
        "hero": float(editorial.get("hero_keyframe_slow_push_in", editorial.get("hero_keyframe_punch_in", editorial.get("hero_frame_slow_push_in", 0)))),
        "reaction": float(editorial.get("reaction_hold", 0)),
        "loop": float(editorial.get("opening_keyframe_reuse_for_loop", 0)),
    }
    hold_total = min(sum(holds.values()), max_static)
    estimated_runtime = stretched_motion + hold_total
    motion_density = stretched_motion / estimated_runtime if estimated_runtime else 0

    lines = [
        f"# {episode_id} — Healing Edit Plan",
        "",
        "> Deterministic plan. No LLM, Flow generation, or upload is performed.",
        "",
        "## Guardrails",
        "",
        f"- Runtime mode: {runtime.get('mode', 'compact_h30')}",
        f"- Generated motion source: {raw_motion:.1f}s",
        f"- Suggested playback speed: {chosen_speed:.2f}x (only if paw/object motion still looks natural)",
        f"- Estimated moving footage after speed adjustment: {stretched_motion:.1f}s",
        f"- Static/keyframe material budget: ≤ {max_static:.1f}s",
        f"- Estimated final runtime: ~{estimated_runtime:.1f}s",
        f"- Estimated motion density: {motion_density*100:.0f}% (target ≥ {target_motion_density*100:.0f}%)",
        "- Keep true first-person cat POV and front-paws-only framing throughout the edit.",
        "- The tiny hero object should remain visually much smaller than one paw; do not crop away the scale reference.",
        "- Do not pad runtime merely to hit a round number.",
        "- If slowdown creates judder, paw deformation, or unnatural steam, use 1.00x and accept the shorter Short.",
        "",
        "## Timeline",
        "",
    ]

    cursor = 0.0
    if holds["opening"] > 0:
        duration = min(holds["opening"], 0.8)
        lines.append(f"- {cursor:04.1f}–{cursor+duration:04.1f}s: OPEN scale-reveal keyframe / tiny subtle push-in")
        cursor += duration

    for idx, scene in enumerate(scenes, 1):
        source = float(scene.get("generation_seconds", 8))
        duration = source / chosen_speed
        purpose = str(scene.get("purpose", f"scene_{idx}")).replace("_", " ")
        lines.append(f"- {cursor:04.1f}–{cursor+duration:04.1f}s: {scene.get('id', f'G{idx}')} — {purpose}; {chosen_speed:.2f}x")
        cursor += duration
        if idx == 2 and holds["danger"] > 0:
            duration2 = min(holds["danger"], 0.35)
            lines.append(f"- {cursor:04.1f}–{cursor+duration2:04.1f}s: tactile micro-hold; keep ASMR natural")
            cursor += duration2

    remaining = max(0.0, min(max_static, target_runtime - cursor))
    if remaining > 0:
        hero = min(remaining, max(0.4, holds["hero"]))
        lines.append(f"- {cursor:04.1f}–{cursor+hero:04.1f}s: hero micro-detail with living motion if available")
        cursor += hero
        remaining -= hero
    if remaining > 0:
        loop = min(remaining, max(0.3, holds["loop"]))
        lines.append(f"- {cursor:04.1f}–{cursor+loop:04.1f}s: quiet loop return / paws withdraw")
        cursor += loop

    narration = post.get("narration_default", "none")
    lines += [
        "",
        "## Audio",
        "",
        f"- Narration default: {narration}",
        "- Prefer close, tiny tactile ASMR over large cinematic impacts.",
        "- Maintain one subtle room-tone bed across joins.",
        "- If footage is slowed, replace or separately time-process native audio rather than leaving pitch artifacts.",
        "",
        "## QC stop rule",
        "",
        "A fourth Lite generation is valid only when the manifest declares immersive_h40 and G4 adds an independent tactile/world-resolution beat. "
        "If G4 merely extends runtime, skip it. Never buy G2/G3/G4 before the previous scene passes POV, scale, anatomy and continuity QC.",
    ]
    return "\n".join(lines) + "\n"


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("manifest", type=Path)
    parser.add_argument("--out", type=Path)
    args = parser.parse_args()

    data = yaml.safe_load(args.manifest.read_text(encoding="utf-8"))
    output = build(data)
    out = args.out or Path("generated") / f"{data['episode_id']}_edit_plan.md"
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(output, encoding="utf-8")
    print(out)


if __name__ == "__main__":
    main()
