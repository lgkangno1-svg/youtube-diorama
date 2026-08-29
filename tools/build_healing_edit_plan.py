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
    all_scenes = data.get("scenes", [])
    post = data.get("post_production", {})
    runtime = data.get("runtime_strategy", {})
    editorial = data.get("editorial_seconds", {})

    optional_fourth = (
        str(runtime.get("mode") or "") == "immersive_h40"
        and runtime.get("fourth_beat_optional_after_g3") is True
        and len(all_scenes) >= 4
    )
    # Current adaptive H40 semantics: build the initial edit plan around the
    # complete G1-G3 core. G4 is not part of the edit timeline until real G3
    # footage proves that the fourth beat improves the ending.
    scenes = all_scenes[:3] if optional_fourth else all_scenes
    optional_scene = all_scenes[3] if optional_fourth else None

    if optional_fourth:
        preferred = runtime.get("core_target_final_runtime_seconds") or [24, 27]
    else:
        preferred = (
            runtime.get("target_final_runtime_seconds")
            or post.get("preferred_final_runtime_seconds")
            or [24, 27]
        )

    target_runtime = (
        sum(preferred) / 2
        if isinstance(preferred, list) and len(preferred) == 2
        else float(data.get("length_target_seconds", 26))
    )
    target_motion_density = float(post.get("target_motion_density_pct_min", 80)) / 100.0
    max_static = float(post.get("max_total_static_hold_seconds", 0))
    speed_range = post.get("preferred_playback_speed_range", [0.92, 1.00])
    min_speed = float(speed_range[0]) if isinstance(speed_range, list) and speed_range else 0.92

    raw_motion = sum(float(s.get("generation_seconds", 8)) for s in scenes)

    holds = {
        "opening": max(0.0, float(editorial.get("opening_keyframe_hold", 0))),
        "room": max(0.0, float(editorial.get("environmental_room_hold", 0))),
        "danger": max(0.0, float(editorial.get("cliffhanger_freeze", editorial.get("conflict_micro_hold", 0)))),
        "hero": max(0.0, float(editorial.get("hero_keyframe_slow_push_in", editorial.get("hero_keyframe_punch_in", editorial.get("hero_frame_slow_push_in", 0))))),
        "reaction": max(0.0, float(editorial.get("reaction_hold", 0))),
        "loop": max(0.0, float(editorial.get("opening_keyframe_reuse_for_loop", 0))),
    }
    explicit_hold_total = min(sum(holds.values()), max(0.0, max_static))

    desired_motion_runtime = max(raw_motion, target_runtime - explicit_hold_total)
    required_speed = raw_motion / desired_motion_runtime if desired_motion_runtime > 0 else 1.0
    chosen_speed = clamp(required_speed, min_speed, 1.0)
    stretched_motion = raw_motion / chosen_speed if chosen_speed > 0 else raw_motion
    feasible_runtime = stretched_motion + explicit_hold_total
    motion_density = stretched_motion / feasible_runtime if feasible_runtime else 0

    lines = [
        f"# {episode_id} — Healing Edit Plan",
        "",
        "> Deterministic plan. No LLM, Flow generation, or upload is performed.",
        "",
        "## Guardrails",
        "",
        f"- Runtime mode: {runtime.get('mode', 'compact_h30')} (mode name tracks first-pass credit tier, not promised final seconds)",
        f"- Generated motion source in this core plan: {raw_motion:.1f}s",
        f"- Suggested playback speed: {chosen_speed:.2f}x (only if paw/object motion still looks natural)",
        f"- Estimated moving footage after speed adjustment: {stretched_motion:.1f}s",
        f"- Explicit editorial hold budget: {explicit_hold_total:.1f}s / max {max_static:.1f}s",
        f"- Estimated core final runtime from declared material: ~{feasible_runtime:.1f}s",
        f"- Estimated motion density: {motion_density*100:.0f}% (target ≥ {target_motion_density*100:.0f}%)",
        "- Keep the accepted maker-view / front-paws-only framing throughout the edit.",
        "- The tiny hero object should remain visually much smaller than one paw; do not crop away the scale reference.",
        "- Do not pad runtime merely to hit a round number or a runtime-mode label.",
        "- If slowdown creates judder, paw deformation, or unnatural steam, use 1.00x and accept the shorter Short.",
        "- If a requested runtime cannot be reached from generated motion + natural slowdown + explicit holds, accept the shorter edit or change the manifest before paid generation.",
    ]

    if optional_fourth:
        lines += [
            "- Adaptive H40: this plan intentionally includes only G1-G3. G4 is excluded until real G3 footage is reviewed.",
            "- Do not generate or edit optional G4 merely because it exists in the manifest.",
        ]

    lines += ["", "## Timeline", ""]

    cursor = 0.0
    remaining_hold_budget = explicit_hold_total

    if holds["opening"] > 0 and remaining_hold_budget > 0:
        duration = min(holds["opening"], 0.8, remaining_hold_budget)
        lines.append(f"- {cursor:04.1f}–{cursor+duration:04.1f}s: OPEN scale-reveal keyframe / tiny subtle push-in")
        cursor += duration
        remaining_hold_budget -= duration

    for idx, scene in enumerate(scenes, 1):
        source = float(scene.get("generation_seconds", 8))
        duration = source / chosen_speed
        purpose = str(scene.get("purpose", f"scene_{idx}")).replace("_", " ")
        lines.append(f"- {cursor:04.1f}–{cursor+duration:04.1f}s: {scene.get('id', f'G{idx}')} — {purpose}; {chosen_speed:.2f}x")
        cursor += duration
        if idx == 2 and holds["danger"] > 0 and remaining_hold_budget > 0:
            duration2 = min(holds["danger"], 0.35, remaining_hold_budget)
            lines.append(f"- {cursor:04.1f}–{cursor+duration2:04.1f}s: tactile micro-hold; keep ASMR natural")
            cursor += duration2
            remaining_hold_budget -= duration2

    for key, label in (
        ("room", "quiet environmental room hold"),
        ("hero", "hero micro-detail hold with living motion if available"),
        ("reaction", "brief tactile reaction hold"),
        ("loop", "quiet loop return / paws withdraw"),
    ):
        if holds[key] > 0 and remaining_hold_budget > 0:
            duration = min(holds[key], remaining_hold_budget)
            lines.append(f"- {cursor:04.1f}–{cursor+duration:04.1f}s: {label}")
            cursor += duration
            remaining_hold_budget -= duration

    preferred_min = preferred[0] if isinstance(preferred, list) and len(preferred) == 2 else None
    if preferred_min is not None and cursor + 0.05 < float(preferred_min):
        lines += [
            "",
            "## Runtime feasibility note",
            "",
            f"- Declared preferred minimum: {float(preferred_min):.1f}s",
            f"- Current plan reaches only ~{cursor:.1f}s without invented padding.",
            "- Do not add fake holds. Accept the shorter Short or revise the production manifest before generating more paid footage.",
        ]

    if optional_scene is not None:
        optional_purpose = str(optional_scene.get("purpose", "optional fourth beat")).replace("_", " ")
        lines += [
            "",
            "## Optional G4 decision — after real G3 only",
            "",
            f"- Candidate: {optional_scene.get('id', 'G4')} — {optional_purpose}.",
            "- First watch the edited G1-G3 core. If the golden-center/payoff already feels complete, STOP and publish the shorter edit.",
            "- Only if a fourth beat clearly improves closure: derive its target from the actual saved G3 PASS frame, generate G4, then rebuild/revise the edit plan with the real footage.",
        ]

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
        "A fourth Lite generation is valid only when the manifest declares adaptive immersive_h40, G3 has already passed, and real G1-G3 footage still benefits from an independent tactile/world-resolution beat. If G4 merely extends runtime, skip it. Never buy G2/G3/G4 before the previous scene passes maker-view, scale, anatomy and continuity QC.",
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
