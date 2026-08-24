#!/usr/bin/env python3
"""Build a low-token Google Flow prompt pack from one episode YAML manifest.

Usage:
  python tools/build_flow_pack.py episodes/TK-001.yaml
  python tools/build_flow_pack.py episodes/TK-001.yaml --out generated/TK-001_flow_pack.md

Requires: PyYAML
"""
from __future__ import annotations

import argparse
from pathlib import Path
from typing import Any

import yaml

STYLE = (
    "Photorealistic miniature Japanese kitchen, vertical 9:16, macro lens, shallow depth of field, "
    "warm natural light, realistic food texture and physics. Same orange tabby cat with white-sock "
    "feline front paws. No human fingers, no thumbs, no extra limbs, no text, no logos, no watermark."
)

LOCK = (
    "Preserve exact cat fur pattern, cookware, food scale, kitchen layout and lighting. "
    "Do not duplicate, remove or morph ingredients unless the action explicitly requires it."
)


def humanize(value: Any) -> str:
    if value is None:
        return ""
    return str(value).replace("_", " ").strip()


def get_scene_seconds(scene: dict[str, Any]) -> int:
    value = scene.get("generation_seconds", 8)
    try:
        value = int(value)
    except (TypeError, ValueError):
        value = 8
    return value if value in {4, 6, 8} else 8


def ordered_keyframes(data: dict[str, Any]) -> list[str]:
    explicit = list((data.get("keyframes") or {}).keys())
    if explicit:
        return explicit
    return ["KF0_OPEN", "KF1_CONSTRAINT", "KF2_DANGER", "KF3_PAYOFF", "KF4_RESOLUTION"]


def frame_text(data: dict[str, Any], name: str) -> str:
    explicit = (data.get("keyframes") or {}).get(name)
    if explicit:
        return humanize(explicit)
    return humanize(name)


def build(data: dict[str, Any]) -> str:
    episode_id = data["episode_id"]
    refs = ", ".join(data.get("references", [])) or "master cat, kitchen, cookware references"
    strategy = data.get("flow_strategy", {}) or {}
    scenes = data.get("scenes", []) or []
    kfs = ordered_keyframes(data)
    planned = int(strategy.get("max_lite_generations_first_pass") or len(scenes) or 4)
    non_ultra = int(strategy.get("non_ultra_credit_budget_first_pass") or planned * 10)
    ultra = int(strategy.get("ultra_credit_budget_first_pass") or planned * 5)
    pacing = humanize(strategy.get("pacing") or "controlled")
    max_cuts = strategy.get("max_visual_cuts_per_8s_generation")
    narration_policy = humanize(strategy.get("narration_policy") or "none by default")
    audio_policy = humanize(strategy.get("audio_policy") or "natural cooking ASMR")

    lines: list[str] = [
        f"# {episode_id} — Flow Pack",
        "",
        "> Generated deterministically from the episode manifest. Do not ask an LLM to rewrite unless a scene fails.",
        "",
        "## Fixed settings",
        "",
        "- Primary model: Veo 3.1 Lite",
        "- Video output count: 1",
        "- Aspect ratio: 9:16",
        f"- Frame mode: {humanize(strategy.get('frame_mode') or 'first plus last')}",
        f"- References: {refs}",
        f"- Pacing: {pacing}",
        f"- Narration policy: {narration_policy}",
        f"- Audio policy: {audio_policy}",
        "- Keep First+Last continuity shots on Lite; Fast is not a drop-in replacement for this mode.",
        "- Extend is valid only from an 8s Veo 3.1 source clip and the extension must use Veo 3.1 Lite.",
        "",
        "## Production-card approval",
        "",
        f"- Title: {data.get('title', '')}",
        f"- Hook: {data.get('hook', '')}",
        f"- Approve the {len(kfs)} free keyframes/contact sheet before spending video credits",
        f"- First-pass budget: {planned} Lite generations = {non_ultra} credits non-Ultra / {ultra} Ultra",
        "- Do not create multiple outputs in one request; Flow charges per generation, not per request.",
        "- Do not spend the unused daily allowance just because it exists; reserve it for a clearly failed shot or the next episode.",
        "",
        f"## {len(kfs)} keyframes",
        "",
    ]

    for kf in kfs:
        lines += [f"### {kf}", "", "```text", f"{frame_text(data, kf)}. {STYLE}", "```", ""]

    lines += [f"## {len(scenes)} video generations", ""]

    for scene in scenes:
        scene_id = scene.get("id", "G")
        generation_type = humanize(scene.get("generation_type") or "first plus last")
        action = humanize(scene.get("action"))
        seconds = get_scene_seconds(scene)
        pacing_clause = (
            "Use one calm continuous action with no unnecessary camera change. Let the motion breathe and hold briefly after the action completes."
            if "healing" in pacing
            else "Keep motion simple, legible and physically plausible."
        )
        cut_clause = f" Maximum visual cuts in this {seconds}s generation: {max_cuts}." if max_cuts else ""

        if generation_type == "extend":
            source_scene = scene.get("source_scene", "previous 8s scene")
            lines += [
                f"### {scene_id}: EXTEND {source_scene} ({seconds}s operation)",
                "",
                "- Select the completed 8s source clip in Flow and use Veo 3.1 Lite Extend.",
                "- Do not create a second independent start-state for this beat unless Extend fails QC.",
                "",
                "```text",
                f"Continue seamlessly from the supplied source clip. Action: {action}. {pacing_clause}{cut_clause} "
                f"Maintain camera direction, cat anatomy, miniature scale, lighting and exact food state from the source. {LOCK} {STYLE} "
                "No dialogue. No music. Keep native audio only if it is clean; otherwise replace the join with a reusable ASMR sound bridge in post.",
                "```",
                "",
            ]
        else:
            start = scene.get("start_frame", "")
            end = scene.get("end_frame", "")
            lines += [
                f"### {scene_id}: {start} → {end} ({seconds}s)",
                "",
                "```text",
                f"Animate naturally from the supplied first frame to the supplied last frame in {seconds} seconds. Action: {action}. "
                f"{pacing_clause}{cut_clause} {LOCK} {STYLE} No dialogue. No music. Keep only subtle clean cooking/room ASMR if it renders naturally.",
                "```",
                "",
            ]

    signature = data.get("creator_signature", {}) or {}
    lines += [
        "## Creator signature / narration",
        "",
        "Default to no narration. If an A/B test or story context requires voice, record it in post rather than spending Flow credits on dialogue.",
        f"- narrator_angle: {humanize(signature.get('narrator_angle') or 'optional')}",
        f"- signature_line: {signature.get('signature_line') or 'none'}",
        "",
        "## Failure escalation",
        "",
        "1. Minor defect: fix in editor with crop, freeze, slow push-in, speed adjustment, sound bridge, or a free keyframe cutaway.",
        "2. First+Last structural defect: reroll only that scene with Veo 3.1 Lite.",
        "3. Extend structural defect: reroll only the Extend once, or use the manifest fallback and generate the last beat as one normal Lite First+Last scene.",
        "4. Never generate both Extend and its fallback proactively; choose one path first.",
        "5. Repeated failure: simplify the action or repair the relevant keyframe/source clip before rerolling.",
        "6. Do not upgrade a frame-locked shot to Fast merely because Lite failed; current Flow support does not make Fast a like-for-like First+Last replacement.",
        "7. Use Fast/Quality only for a separate hero insert where losing endpoint lock is acceptable.",
        "",
        "## Final approval",
        "",
        "Approve only the final export after continuity, slow/healing pacing, hook readability, resolution, audio cleanliness, originality, and upload metadata are checked.",
    ]
    return "\n".join(lines) + "\n"


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("manifest", type=Path)
    parser.add_argument("--out", type=Path)
    args = parser.parse_args()
    data = yaml.safe_load(args.manifest.read_text(encoding="utf-8"))
    output = build(data)
    out = args.out or Path("generated") / f"{data['episode_id']}_flow_pack.md"
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(output, encoding="utf-8")
    print(out)


if __name__ == "__main__":
    main()
