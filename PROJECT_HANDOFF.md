# Tiny Cat Kitchen — PROJECT HANDOFF

Last update: **2026-08-28 KST**
Baseline inspected before this iteration: `main@3f2aab3aa365cb67422a3bdbee09104a49230e4c`

Durable handoff source of truth for `lgkangno1-svg/youtube-diorama`. Every material repository change must update this file in the same branch/PR. True NO-OP research should not churn it.

## Execution policy

- Before every run inspect latest main SHA, recent commits/PRs, then this handoff.
- Latest merged repository state overrides stale chat or scheduled-prompt wording.
- Modify only `lgkangno1-svg/youtube-diorama`.
- Never spend Flow credits, generate paid video, or publish to YouTube without explicit user action.
- Normal user interface remains: `다음 영상 준비해줘` → prepare repo state → user runs `./tools/make_next_short.ps1`.

## Canonical visual identity

User-directed correction from 2026-08-28:

> **Mini Forest-style realistic miniature cooking/making, except the human hands are replaced by the cat's front paws. The cat's full body does not need to appear.**

Tiny Cat Kitchen is not an AI-cat character-performance channel.

Required:
- realistic handcrafted miniature food/object making
- one or two cream/pale-ginger feline front paws only
- no face/head/body/full cat
- no human hands/fingers/thumbs
- absurdly tiny hero object, normally 5–20mm and <=0.50 paw width
- process-first calm tactile ASMR
- stable workbench/diorama continuity
- one primary paw-safe tactile action per 8-second generation, plus at most one passive material payoff

Default camera priority:
1. high-oblique maker view
2. top-down macro
3. tabletop/side-oblique macro
4. first-person-like angle only when it materially improves the making shot

Literal true first-person cat-eye POV is **not mandatory**.

Legacy labels such as `POV_PAWS_MICROWORLD_V1` and `camera_grammar.mode: first_person_cat_pov` remain temporarily for tooling compatibility. Their semantic meaning is `mini_forest_style_paws_only_miniature_making`; do not use the legacy name to restore mandatory POV.

## Research / benchmark policy

Primary production benchmark class:
- Mini Forest-style miniature cooking
- handcrafted tiny-food making
- relaxing ASMR / tactile process

Abstract only:
- hand-centric maker composition
- tiny-scale contrast
- material transformation
- calm pacing
- seasonal timing
- tactile payoff

Do not copy exact titles, plots, branded products/packages, sets, dish styling, or endings.

AI-cat character channels are secondary only for narrow paw appearance/reliability evidence, not for character storytelling or job-role structure.

Evidence saturation remains active: do not add same-class retail/promotional signals unless they change candidate ranking, timing, evidence class, production mechanics, Flow assumptions, or actual Tiny Cat Kitchen learning.

## Flow / Veo production baseline

Official Google Flow Help rechecked 2026-08-28:
- Veo 3.1 Lite supports 4s/6s/8s and Extend
- non-Ultra cost: 10 credits/generation
- actual active Flow UI model/mode/output count/displayed cost at generation time is final truth

Repository baseline:
- Veo 3.1 Lite
- output count 1
- progressive one-generation-at-a-time spend
- no paid spend before free planned-keyframe continuity passes

## Planned keyframe continuity

```text
verify image model + displayed cost
→ KF0 maker-view master anchor
→ QC paws / scale / camera / props / lighting
→ derive KF1 from approved KF0
→ derive KF2 from approved KF1
→ continue through required KFs
→ all planned KFs PASS
→ G1 only
```

KF1+ must not become unrelated fresh text-to-image lottery tickets.

Planned KF = destination. Actual previous PASS video frame = next-scene continuity bridge.

## Progressive Spend

```text
planned KF chain PASS
→ G1 only
→ QC
→ native Save frame
→ G2 only after G1 PASS
→ G3 only after G2 PASS
→ G4 only if immersive_h40 + G3 PASS + independent world-resolution value
```

## Runtime policy

H30/H40 are first-pass credit tiers, not promised final seconds.

- `compact_h30`: 3 × 8s raw = 24s, current ceiling 30 credits, normal final ~24–27s
- `immersive_h40`: 4 × 8s raw = 32s, current ceiling 40 credits, normal final ~32–35s

No invented still/loop padding.

## Paw-action grammar

Preferred:
- nudge
- press
- pat
- roll
- steady
- slide
- tap
- push

Avoid:
- human pinch
- chopsticks/tongs/knife human grip
- precise wrist twist
- multiple serial active paw gestures in one generation without explicit evidence-backed justification

A Mini Forest human-hand action must be translated into a feline-safe equivalent, not copied literally.

## Current production state

`production/NEXT_EPISODE.txt` = **TK-005**

Title: `猫の前足で作る、12mmの焼きいも。`
Manifest: `episodes/TK-005.yaml`
Runtime: `immersive_h40`
First-pass ceiling: 4 Lite generations / current 40 credits
Final target: 32–35s

TK-005 visual intent:
- stable high-oblique Mini Forest-style maker view
- only front paws enter where human hands normally would
- no face/head/body/full cat
- 12mm yakiimo dramatically smaller than paw
- same tray/warmer/serving niche through KF0→KF4
- zero-cut calm long takes
- G4 = one tray-slide action, then passive steam only

Paid chain:
- G1: KF0 → KF1
- G2: actual saved G1 frame → KF2
- G3: actual saved G2 frame → KF3
- G4: actual saved G3 frame → KF4

## Production learning available

`analytics/learning_ledger.csv` has one real preflight failure:
- full cat/body visible
- scale too large
- human-like tool-use risk

Correct interpretation:
- third-person/observer view itself is not a failure
- character-performance framing + body reveal + weak miniature scale is the failure
- Mini Forest-style observer/maker view with paws + workbench is desirable

There is still no trustworthy public 24h/72h Tiny Cat Kitchen performance sample.

Long-term KPIs:
- usable motion / credit
- engaged views / credit
- subscribers / 100 credits

## Backlog correction — 2026-08-28

Material issue found after the canonical Mini Forest correction: `ideas/episode_backlog.yaml` still contained multiple literal `True first-person cat POV` premises and `cat_job_world` mechanics. That could reintroduce the old AI-cat character direction when future episodes are selected even though START_HERE/CURRENT_STANDARD/learning ledger were already corrected.

Corrected in this iteration:
- all current candidate premises now describe high-oblique/top-down/tabletop Mini Forest-style maker views instead of mandatory cat-eye POV
- explicit no-face/no-body/no-character-performance semantics added where relevant
- `cat_job_world` mechanics replaced with diorama-workspace/environmental worldbuilding mechanics
- bakery/kissaten/oden settings remain allowed only as handcrafted miniature environments, not as a cat acting out a human job
- IDEA-008 ending no longer asks for an extra paw-withdrawal gesture after the tray slide
- legacy `POV_PAWS_MICROWORLD_V1` field remains only for tooling compatibility
- candidate scores/ranking and NEXT_EPISODE were intentionally not changed because this is a semantic correction, not new demand evidence

## Current roadmap / next priorities

1. Create and approve TK-005 KF0 maker-view master anchor in real Flow.
2. Confirm it looks like real miniature cooking with paws replacing hands, not an AI-cat character scene.
3. Derive KF1→KF4 with stable camera/paws/scale/props.
4. Generate G1 only after all planned KFs PASS.
5. QC maker-view / paws-only / scale / anatomy / zero-cut / fixed props.
6. On PASS, native Save frame and continue progressively.
7. Record actual credits/rerolls/usable motion and failure type.
8. After upload, record 24h/72h Stayed to watch, APV, engaged views, subscribers, comments.
9. Consider full enum/schema rename only after real Flow production proves the maker-view standard; do not migrate piecemeal.

## Safety / invariants

- no automatic Flow credit spend
- no automatic paid generation
- no automatic YouTube publish
- no exact competitor copying
- no full-cat/face/body default shots
- no AI-cat character-performance regression
- no human hands/fingers/thumbs
- no human-like feline tool grip
- no hero scale >0.50 paw width without documented exception
- no paid G1 before planned KF chain PASS
- no planned KF substituted for actual previous PASS frame
- no next-scene spend after previous failure
- no runtime padding
- no unrelated repository modifications

## Change log

### 2026-08-28 — backlog maker-view semantic correction
Baseline: `main@3f2aab3aa365cb67422a3bdbee09104a49230e4c`.

Changed:
- migrated all active backlog premises away from mandatory `True first-person cat POV`
- replaced `cat_job_world` mechanics with miniature-environment/workbench worldbuilding
- made settings such as kissaten/bakery/oden stall environmental only, not cat-roleplay premises
- removed IDEA-008's extra paw-withdrawal ending gesture
- kept candidate scores, ranking, TK-005 selection, runtime and credit budget unchanged
- synchronized this handoff in the same branch

Why:
- the backlog is part of the operating system and could otherwise regenerate the superseded AI-cat/mandatory-POV direction during future episode selection

Research verification:
- official Flow cost assumption still holds: non-Ultra Veo 3.1 Lite 4/6/8s + Extend = 10 credits/generation
- fresh late-August Japanese sweet-potato/seasonal evidence remains same-class and does not materially change the current ranking, so benchmark log was not churned

### 2026-08-28 — learning-ledger maker-view correction
- corrected stale actionable learning that said to force true first-person camera
- preserved historical observation/hypothesis while updating future action to Mini Forest-style maker-view semantics

### 2026-08-28 — TK-005 G4 single-action correction
- removed a second active paw-withdrawal gesture
- G4 now contains one tray slide followed only by passive steam

### 2026-08-28 — canonical Mini Forest paw-only correction
- established Mini Forest-style miniature making + human hands replaced by feline front paws as channel grammar
- demoted literal first-person POV from mandatory to optional
