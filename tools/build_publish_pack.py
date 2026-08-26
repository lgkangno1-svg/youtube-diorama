#!/usr/bin/env python3
"""Build a zero-LLM YouTube Shorts publish pack from an episode YAML manifest.

Usage:
  python tools/build_publish_pack.py episodes/TK-001.yaml
  python tools/build_publish_pack.py episodes/TK-001.yaml --out generated/TK-001_publish_pack.md

Requires: PyYAML
"""
from __future__ import annotations

import argparse
from pathlib import Path
from typing import Any
import yaml


def h(v: Any) -> str:
    return "" if v is None else str(v).replace("_", " ").strip()


def audience_loop_lines(data: dict[str, Any]) -> list[str]:
    cfg = data.get("audience_loop", {}) or {}
    mode = str(cfg.get("mode") or "").strip().lower()
    if not mode:
        return [
            "## Audience loop",
            "",
            "- No interactive sticker is planned for this episode; use the pinned comment only.",
            "- Do not add a generic like/subscribe CTA just to fill space.",
        ]

    lines = [
        "## Audience loop — turn this Short into the next episode seed",
        "",
        "> Use only one primary interaction mechanic per episode. The goal is to collect the next creative input without another brainstorming/LLM pass.",
        "",
    ]

    if mode == "poll":
        question = cfg.get("question") or "次に見たいのはどっち？"
        options = cfg.get("options") or []
        lines += [f"- Mode: Poll Sticker", f"- Question: {question}"]
        if options:
            lines.append("- Options: " + " / ".join(str(x) for x in options[:2]))
        lines.append("- Rule: the winning option becomes a candidate premise, not an automatic copy of the previous episode.")
    elif mode in {"q&a", "qa", "qna"}:
        question = cfg.get("question") or "次に小さくしてほしい料理は？"
        lines += [
            "- Mode: Q&A Sticker",
            f"- Question: {question}",
            "- Rule: collect recurring nouns/problems; use the strongest repeated suggestion as an idea seed, then run originality validation before Flow spend.",
        ]
    elif mode == "video_reply":
        trigger = cfg.get("trigger") or "a specific funny or repeated viewer comment that can become a genuinely new episode premise"
        lines += [
            "- Mode: Video Reply",
            f"- Trigger: {trigger}",
            "- Rule: reply with a Short only when the comment creates a new goal/conflict/resolution; do not generate a near-duplicate just to acknowledge a comment.",
            "- The original commenter will be notified by YouTube when the video reply is posted.",
        ]
    else:
        lines += [
            f"- Mode requested in manifest: {mode}",
            "- Unknown mode: fall back to the pinned comment rather than improvising a new interaction workflow.",
        ]

    seed_rule = cfg.get("next_manifest_seed")
    if seed_rule:
        lines.append(f"- Next-manifest seed rule: {h(seed_rule)}")
    return lines


def build(data: dict[str, Any]) -> str:
    eid = data["episode_id"]
    title = data.get("title", "")
    food = h(data.get("food"))
    hook = data.get("hook", "")
    sig = data.get("creator_signature", {}).get("signature_line", "")
    resolution = h(data.get("resolution") or data.get("payoff"))
    target = data.get("target_market", "JP")

    publishing = data.get("publishing", {})
    audience_prompt = publishing.get("audience_prompt") or "次はどんな小さな料理を見たい？"
    description_line = publishing.get("description_line") or f"{hook} {food}を小さな世界で作ります。"
    hashtags = publishing.get("hashtags") or ["#Shorts", "#ミニチュア料理", "#猫", "#AI猫"]

    lines = [
        f"# {eid} — YouTube Publish Pack",
        "",
        "> Deterministic metadata pack. No LLM rewrite is needed unless the content premise changes.",
        "",
        "## Copy/paste metadata",
        "",
        f"**Title**  \n{title}",
        "",
        "**Description**",
        "",
        "```text",
        description_line,
    ]
    if sig:
        lines.append(sig)
    lines += [
        "",
        " ".join(hashtags),
        "```",
        "",
        "**Pinned comment**",
        "",
        "```text",
        audience_prompt,
        "```",
        "",
    ]
    lines += audience_loop_lines(data)
    lines += [
        "",
        "## Studio checklist",
        "",
        f"- Target market: {target}",
        "- Format: Short / 9:16",
        "- AI use disclosure: YES for photorealistic synthetic Tiny Cat Kitchen footage",
        "- Paid promotion: NO unless money/free product/other value was received from a brand",
        "- Do not add a generic like/subscribe CTA if the episode already has an audience prompt or sticker",
        "- Keep sponsor/product tags empty unless actual Studio eligibility and a real commercial relationship/product are present",
        "- Check that the visible title/description do not claim the food or tools are physically real if the footage is synthetic",
        "",
        "## Originality note for channel records",
        "",
        f"- Hook: {hook}",
        f"- Resolution: {resolution}",
        f"- Creator signature: {sig or 'none'}",
        "- Keep this record with the episode so sponsorship/YPP reviews can quickly see the creative premise and authorship layer.",
        "",
        "## Post-publish data entry — do not split learning truth",
        "",
        "At 24h and 72h, enter only REAL YouTube Studio snapshots in `analytics/shorts_metrics_v2.csv`.",
        "Do not prefill future rows with zeros; zero placeholders are not failed experiments.",
        "After each real snapshot, also copy the matching horizon metrics into `analytics/learning_ledger.csv` together with the episode's actual Flow credits, rerolls, first-pass/QC, usable-motion, continuity and audio fields.",
        "`shorts_metrics_v2.csv` is the raw horizon snapshot table; `learning_ledger.csv` is the canonical combined production + performance decision memory used by the continuous learning loop.",
        "Compare 24h only with 24h and 72h only with 72h; do not judge a winner from raw public views alone.",
        "See `docs/29_analytics_truth_model.md` before changing this data path.",
    ]
    return "\n".join(lines) + "\n"


def main() -> None:
    p = argparse.ArgumentParser()
    p.add_argument("manifest", type=Path)
    p.add_argument("--out", type=Path)
    args = p.parse_args()
    data = yaml.safe_load(args.manifest.read_text(encoding="utf-8")) or {}
    out = args.out or Path("generated") / f"{data['episode_id']}_publish_pack.md"
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(build(data), encoding="utf-8")
    print(out)


if __name__ == "__main__":
    main()
