# Tiny Cat Kitchen — PROJECT HANDOFF

Last update: **2026-08-29 KST**
Baseline inspected before this iteration: `main@6ced3691d587c43ecfdd0033c552e2423e82eb17`

Durable current-state handoff for `lgkangno1-svg/youtube-diorama`. Every material repository change must update this file in the same branch/PR. True NO-OP research should not churn it.

## Start-of-run contract

Before every material run:
1. inspect latest `main` SHA and recent commits/PRs
2. read this handoff
3. read `PRODUCT_CHARTER.md`
4. cross-check `START_HERE.md`, `CURRENT_STANDARD.md`, docs/22/23/27, `production/NEXT_EPISODE.txt`, current manifest, benchmark/backlog/ledger
5. newest explicit user direction and merged repository state override stale scheduled-prompt wording

Document roles:
- `PROJECT_HANDOFF.md` = current state / decisions / failures / learning / next priorities
- `PRODUCT_CHARTER.md` = durable product purpose / identity / economics and improvement criteria
- `CURRENT_STANDARD.md` = executable production/QC/Flow rules
- manifests + ledgers = episode plan + observed evidence

Sync policy:
- every material change updates this handoff
- executable production/QC/Flow rule changes also update `CURRENT_STANDARD.md`
- durable purpose/identity/economics philosophy changes also update `PRODUCT_CHARTER.md`
- true NO-OP does not churn docs

## Durable product intent

Tiny Cat Kitchen is a Japanese-target healing Shorts system for realistic miniature cooking/making where **human hands are naturally replaced by feline front paws**.

Non-negotiable identity:
- cream/pale-ginger front paws only; normally 1–2
- no face/head/body/full cat
- no human hands/fingers/thumbs
- no human-like feline tool grip
- absurdly tiny hero object, normally 5–20mm and <=0.50 paw width
- handcrafted miniature workbench/diorama realism
- process-first tactile making
- calm long-take ASMR
- default high-oblique maker view; top-down/side-oblique allowed
- literal first-person cat-eye POV is **not mandatory**
- no AI-cat human-job/character-performance regression

Primary optimization is not minimum credits/video. Prefer **usable motion/credit, engaged views/credit, and subscribers/100 credits** while protecting quality and explicit user control.

## Current production state

`production/NEXT_EPISODE.txt` = **TK-005**

Title: `猫の前足で作る、12mmの焼きいも。`
Manifest: `episodes/TK-005.yaml`
Runtime tier: `immersive_h40`
Current non-Ultra first-pass ceiling: 4 Veo 3.1 Lite generations / 40 credits
Expected final: ~32–35s when all four beats remain independently useful

Visual intent:
- stable Mini Forest-style high-oblique maker view
- only front paws enter where hands normally would
- 12mm yakiimo dramatically smaller than paw
- same tray/warmer/serving niche through KF0→KF4
- zero-cut calm long takes
- one active paw-safe action per generation + optional passive material payoff
- G4 = tray slide, then passive steam only

Paid continuity chain:
- G1: KF0 → KF1
- G2: actual saved G1 PASS frame → KF2
- G3: actual saved G2 PASS frame → KF3
- G4 only if still justified: actual saved G3 PASS frame → KF4

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

One real preflight failure remains recorded in `analytics/learning_ledger.csv`:
- full cat/body visible
- hero scale too large
- human-like tool-use risk

Correct interpretation:
- observational/third-person maker view itself is not a failure
- body reveal + character-performance framing + weak miniature scale is the failure
- maker-view + paws-only + tiny workpiece is desirable

There is still no trustworthy public 24h/72h Tiny Cat Kitchen performance sample. Do not treat placeholders or theoretical assumptions as audience evidence.

## Research / candidate state

Primary benchmark class:
- realistic miniature cooking/making
- handcrafted tiny-food process
- relaxing tactile ASMR

AI-cat channels are secondary evidence only for narrow paw/anatomy/reliability questions. Never copy exact competitor title, plot, branded product/package, distinctive set, dish styling, or ending.

Evidence saturation remains active. Same-class promotional/retail signals do not justify commits unless they change ranking, timing, evidence class, production mechanics, Flow assumptions, freshness, or actual production learning.

### Fresh evidence accepted — 2026-08-29

A Maruyanagi official release dated 2026-08-19 cites Google Trends and reports that Japanese search volume for `さつまいもスイーツ` rises strongly from September through December and reaches roughly **9× summer levels in October**.

Why this was accepted despite saturation:
- it is a **search-behavior evidence class**, not another same-class product-launch announcement
- it strengthens the seasonal demand curve behind yakiimo/oimo concepts through early autumn
- it supports keeping TK-005 timing rather than replacing it with a fresher but weaker promotional signal

Caution:
- raw Google Trends query data was not independently reproduced in this runtime
- treat the quoted 9× figure as directional evidence from the cited company release, not a universal population estimate
- no branded product/campaign mechanics are copied

Candidate re-evaluation:
- TK-005 / IDEA-009 remains the strongest current production choice
- no backlog score/rank change was made because IDEA-009 was already priority-ranked with maximum benchmark/visual/reliability/credit-efficiency signals, and the new source improves confidence more than relative ordering
- 月見, グミの日, 栗ご飯 candidates remain secondary; no evidence justified replacing the current episode

`research/benchmark_log.csv` now contains this new evidence row.

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

### 2026-08-29 — sweet-potato search-demand evidence
Baseline: `main@6ced3691d587c43ecfdd0033c552e2423e82eb17`.

Changed:
- added one new `research/benchmark_log.csv` row for a search-behavior evidence class: a 2026-08-19 Maruyanagi release citing Google Trends for `さつまいもスイーツ`
- recorded the reported September–December rise and roughly 9× October-vs-summer search level as directional evidence
- synchronized this handoff in the same branch

Why:
- unlike repeated retail-launch evidence, this adds a different behavioral/search-demand class and improves confidence in the current yakiimo seasonal timing

Production impact:
- no change to TK-005, NEXT_EPISODE, H40 runtime, four-generation/40-credit first-pass ceiling, visual grammar, Flow assumptions, candidate ranking, or Progressive Spend
- no Flow credits spent; no publishing

Validation:
- latest main/commits/PRs/handoff inspected first
- START_HERE, docs/22, docs/23, NEXT_EPISODE, backlog, learning ledger and TK-005 manifest cross-checked
- local git validation was attempted but network resolution prevented cloning; branch was created directly from inspected `main@6ced3691...`, and both material files are included in the same branch

### 2026-08-28 — product charter governance wiring
- made `PRODUCT_CHARTER.md` mandatory in the improvement loop
- synchronized START_HERE, docs/22, CURRENT_STANDARD and handoff governance

### 2026-08-28 — durable product charter
- added `PRODUCT_CHARTER.md` as the stable product-purpose and decision-standard document

### 2026-08-28 — Flow / operator / maker-view corrections
- clarified Flow free-tier eligibility without changing H40 spend discipline
- removed stale operator wording that treated non-first-person camera as failure
- removed mandatory first-person/cat-job semantics from actionable backlog/learning
- reduced TK-005 G4 to one active tray-slide action + passive steam
- established Mini Forest-style miniature making + feline front paws replacing human hands as the canonical visual grammar
