# 28 — Episode Novelty & YouTube Authenticity Gate

Checked: **2026-08-26**

## Why this exists

Tiny Cat Kitchen intentionally uses a repeatable visual identity and production pipeline, but repeatable production must not become interchangeable storytelling.

YouTube's current channel monetization policy explicitly treats repetitive or mass-produced content as `inauthentic content`. The same official guidance also says automated tools/templates can be used when the finished videos still demonstrate original creative vision and meaningful entertainment or educational value.

Official source checked 2026-08-26:
- https://support.google.com/youtube/answer/1311392
- current help copy surfaced through YouTube Creator/Help pages under the channel monetization policy

This is not a claim that Tiny Cat Kitchen is currently monetized or that any individual video is guaranteed to qualify. It is a design constraint: **keep the recognizable channel grammar, but vary the substance.**

## What may stay consistent

These are channel identity, not story duplication:
- first-person cat POV
- front paws only
- cream + pale ginger paw identity
- absurdly tiny 5–20mm hero objects
- macro miniature workbench
- calm long-take pacing
- clean close ASMR
- sequential actual-frame chaining
- one primary tactile action per generation

## What must not become interchangeable

Do not repeatedly ship the same combination of:
- hook mechanic
- conflict mechanic
- ending mechanic

Changing only the food name, color, garnish, season, or title is not enough if the underlying conflict and resolution are the same.

## Deterministic recent-episode gate

`ideas/novelty_signatures.yaml` stores an abstract signature for backlog candidates.

`tools/select_next_episode.py` reads the newest five episode manifests containing `episode_fingerprint` and blocks a candidate when:
- its `conflict_mechanic + ending_mechanic` pair exactly matches one of those recent manifests, or
- its `hook + conflict + ending` triple exactly matches one of those recent manifests.

This check is deliberately conservative and exact. It does **not** pretend to solve semantic similarity with fuzzy AI scoring. ChatGPT still reviews broader conceptual similarity before creating a new manifest.

Planned/ready manifests count in the recent window. A story already in the production pipeline should prevent the next story from cloning it even before publication.

## Current consequence

At introduction of this gate:
- `IDEA-009` structurally matches the already-created TK-005 fingerprint. It should not be selected again as a future episode merely because its seasonal score remains high.
- `IDEA-002` intentionally maps to the same physics-tension + measurement-proof structure already represented by TK-004, so the selector blocks that repeat until it leaves the recent-five window or the idea is redesigned with a genuinely different conflict/resolution.
- `production/NEXT_EPISODE.txt` remains TK-005 because TK-005 was selected before this future-selection guard and is the current production task, not a newly selected duplicate.

## When redesigning a blocked candidate

Do not just rename mechanics to bypass the guard. Change at least the actual story substance, preferably one or more of:
- viewer question / hook logic
- physical problem
- emotional turn
- world-state change
- ending/resolution
- character motivation

Then update the candidate novelty signature to describe the real new structure.

## Success criterion

The channel should feel recognizably Tiny Cat Kitchen while consecutive episodes remain meaningfully different experiences.

The optimization target remains:
- engaged views / credit
- subscribers / credit
- usable motion / credit

The novelty gate is there to protect long-term audience satisfaction and channel authenticity, not to maximize superficial variation.
