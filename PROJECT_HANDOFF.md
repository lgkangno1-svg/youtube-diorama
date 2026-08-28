# Tiny Cat Kitchen — PROJECT HANDOFF

Last update: **2026-08-28 KST**
Baseline inspected before this iteration: `main@24ae7e6bdfe5ab9892a8895de9952dc657df706a`

Durable current-state handoff for `lgkangno1-svg/youtube-diorama`. Every material repository change must update this file in the same branch/PR. True NO-OP research should not churn it.

## Start-of-run contract

Before every material run:
1. inspect latest `main` SHA
2. inspect recent commits/PRs
3. read this handoff
4. cross-check `PRODUCT_CHARTER.md`, `START_HERE.md`, `CURRENT_STANDARD.md`, docs/22/23/27, `production/NEXT_EPISODE.txt`, benchmark/backlog/ledger, and recent manifests
5. newest explicit user direction and merged repository state override stale prompts

`PRODUCT_CHARTER.md` is now the durable statement of **why/what we are building and how future improvements are judged**. This handoff remains the source for **where the project is now, what changed, failures/learnings, and next priorities**.

## Durable product intent

Tiny Cat Kitchen is a Japanese-target healing Shorts production system for realistic miniature cooking/making where **the human hands are naturally replaced by feline front paws**.

Creative shorthand: Mini Forest-like realistic miniature making mechanics, without copying exact creative expression.

Non-negotiable identity:
- cream/pale-ginger front paws only; normally 1–2
- no face/head/body/full cat
- no human hands/fingers/thumbs
- no human-like feline tool grip
- absurdly tiny hero object, normally 5–20mm and <=0.50 paw width
- handcrafted miniature workbench/diorama realism
- process-first tactile making
- calm long-take ASMR
- high-oblique maker view default; top-down/side-oblique allowed
- literal first-person cat-eye POV is not mandatory
- no AI-cat human-job/character-performance regression

Primary optimization target is not simply minimum credits/video. Prefer **usable motion/credit, engaged views/credit, and subscribers/100 credits**, while protecting creative quality and user control.

## Current production state

`production/NEXT_EPISODE.txt` = **TK-005**

Title: `猫の前足で作る、12mmの焼きいも。`
Manifest: `episodes/TK-005.yaml`
Runtime tier: `immersive_h40`
Current non-Ultra first-pass ceiling: 4 Veo 3.1 Lite generations / 40 credits
Expected final: ~32–35s when all four scenes are justified and usable

Visual intent:
- stable Mini Forest-style high-oblique maker view
- front paws enter only where hands normally would
- 12mm yakiimo dramatically smaller than paw
- same tray/warmer/serving niche through KF0→KF4
- zero-cut calm long takes
- one active paw-safe action per generation + optional passive material payoff
- G4 = tray slide, then passive steam only

Paid continuity chain:
- G1: KF0 → KF1
- G2: actual saved G1 PASS frame → KF2
- G3: actual saved G2 PASS frame → KF3
- G4 only when still justified: actual saved G3 PASS frame → KF4

## Flow / spend baseline

Generation-time Flow UI is final truth. Current documented assumption:
- Veo 3.1 Lite
- 9:16
- 8 seconds
- output count 1
- non-Ultra: 10 credits/generation
- Ultra: 5 credits/generation
- non-subscriber tier: 50 credits/day, not additive to paid-plan allocations

Progressive Spend:

```text
free/no-charge planned keyframe chain PASS
→ G1 only
→ QC
→ native Save frame
→ G2 only after G1 PASS
→ G3 only after G2 PASS
→ G4 only if runtime/manifest still justifies independent final value
```

Never spend Flow credits, generate paid video, or publish to YouTube without explicit user action.

## Current learning

One real preflight failure is recorded in `analytics/learning_ledger.csv`:
- full cat/body visible
- hero scale too large
- human-like tool-use risk

Correct interpretation:
- observational/third-person maker view itself is not a failure
- body reveal + character-performance framing + weak miniature scale is the failure
- maker-view + paws-only + tiny workpiece is desirable

There is not yet a trustworthy public 24h/72h Tiny Cat Kitchen performance sample. Do not pretend theoretical assumptions are audience evidence.

## Research policy

Primary benchmark class:
- realistic miniature cooking/making
- handcrafted tiny-food process
- relaxing tactile ASMR

AI-cat channels are secondary evidence only for narrow paw/anatomy/reliability questions.

Abstract mechanics only. Never copy exact competitor title, plot, branded product/package, distinctive set, or ending.

Evidence saturation remains active: do not commit repeated same-class promotional/retail signals unless they change ranking, timing, evidence class, production mechanics, Flow assumptions, freshness, or actual Tiny Cat Kitchen learning.

## Normal user interface

The intended routine remains extremely simple:

```text
User: 다음 영상 준비해줘
```

ChatGPT/system should inspect current state and evidence, choose the next original episode, prepare/update manifest and prompt pack, update `production/NEXT_EPISODE.txt`, synchronize this handoff when material state changes, and leave the repo ready for:

```powershell
./tools/make_next_short.ps1
```

The user should not need to manually research topics, engineer prompts, remember Flow settings, or administer repository state. The user retains explicit control over paid generation, QC acceptance, and publishing.

## Current roadmap / next priorities

1. Create and approve TK-005 KF0 master anchor in real Flow.
2. Confirm it reads as genuine miniature making with paws replacing hands, not an AI-cat character scene.
3. Derive KF1→KF4 sequentially with stable paws/scale/camera/props/lighting.
4. Generate G1 only after the planned KF chain passes.
5. QC maker-view, paws-only identity, tiny scale, anatomy, fixed props, zero-cut behavior.
6. On PASS, save the actual usable final frame and continue progressively.
7. Record actual credits, rerolls, usable motion, G-stage pass/fail and failure class.
8. After upload, record 24h/72h Stayed to watch, APV, engaged views, subscribers and comments.
9. Use real accumulated evidence to adjust action grammar, runtime tiers, candidate scoring and spend strategy.
10. Keep the user-facing workflow simpler over time, not more complicated.

## Safety / invariants

- no automatic paid generation
- no automatic YouTube publishing
- no exact competitor copying
- no full-cat/face/body default shots
- no human hands/fingers/thumbs
- no human-like paw grip
- no weak miniature scale without documented exception
- no paid G1 before planned KF continuity passes
- no next paid scene after prior structural failure
- actual previous PASS frame is the continuity bridge
- no runtime padding for its own sake
- no research churn after saturation
- no unrelated repository modifications
- every material repository change synchronizes this handoff

## Change log

### 2026-08-28 — durable product charter
Baseline: `main@24ae7e6bdfe5ab9892a8895de9952dc657df706a`.

Changed:
- added `PRODUCT_CHARTER.md` as the stable product-purpose and decision-standard document requested by the user
- codified the durable goal, visual identity, audience strategy, production economics, credit philosophy, continuity philosophy, anti-goals, success definition, development philosophy, and a 10-question merge decision test
- explicitly separated durable intent (`PRODUCT_CHARTER.md`) from current state (`PROJECT_HANDOFF.md`) and executable operating rules (`CURRENT_STANDARD.md`)
- synchronized this handoff in the same branch

Why:
- repeated incremental corrections showed that future AI/developers need a single durable document explaining the user's actual desired product, not only transient episode state or implementation rules
- this reduces regressions from stale scheduled prompts, legacy POV enum names, isolated benchmarks, or cost-only optimization

Production impact:
- no change to TK-005 selection, manifest, NEXT_EPISODE, H40 runtime, current 40-credit first-pass ceiling, or Progressive Spend
- future improvements should be rejected when they save credits or add automation but damage paws-only miniature-making identity, tactile healing quality, or user control

### 2026-08-28 — Flow free-tier eligibility clarification
- persisted official no-subscription 50 credits/day eligibility and non-stacking behavior
- TK-005 remained H40 / current 40-credit non-Ultra first-pass ceiling

### 2026-08-28 — operator maker-view QC correction
- removed stale operator wording that treated non-first-person camera as failure

### 2026-08-28 — backlog/learning semantic correction
- removed mandatory true-first-person and cat-job-world semantics from actionable planning
- preserved maker-view, paws-only, tiny-scale intent

### 2026-08-28 — TK-005 G4 correction
- reduced G4 to one active tray-slide action followed by passive steam

### 2026-08-28 — canonical Mini Forest paw-only correction
- established realistic miniature making + feline front paws replacing human hands as the channel grammar
- demoted literal first-person POV from mandatory to optional
