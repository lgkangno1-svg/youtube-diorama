# Tiny Cat Kitchen — PROJECT HANDOFF

Last update: **2026-08-29 KST**
Baseline inspected before this iteration: `main@ffba0bde59ac67d282ce459265b77b03288cd3b5`

Durable current-state handoff for `lgkangno1-svg/youtube-diorama`. Every material repository change must update this file in the same branch/PR. True NO-OP research must not churn it.

## Start-of-run contract

Before every material run:
1. inspect latest `main` SHA and recent commits/PRs
2. read this handoff
3. read `PRODUCT_CHARTER.md`
4. cross-check `START_HERE.md`, `CURRENT_STANDARD.md`, docs/22/23/27, `production/NEXT_EPISODE.txt`, current manifest, benchmark/backlog/ledger
5. newest explicit user direction + latest merged repository state override stale scheduled-prompt wording

Document roles:
- `PROJECT_HANDOFF.md` = current state / decisions / failures / learning / next priorities
- `PRODUCT_CHARTER.md` = durable product purpose / identity / economics / improvement criteria
- `CURRENT_STANDARD.md` = executable production/QC/Flow/selection rules
- manifests + ledgers = episode plan + observed evidence

Sync policy:
- material change → handoff
- production/QC/Flow/selection rule change → current standard
- durable purpose/identity/economics philosophy change → product charter
- true NO-OP → no documentation churn

## Durable product intent

Tiny Cat Kitchen is a Japanese-target healing Shorts system for realistic miniature cooking/making where human hands are naturally replaced by feline front paws.

Non-negotiable:
- cream/pale-ginger front paws only, normally 1–2
- no face/head/body/full cat
- no human hands/fingers/thumbs
- no human-like feline tool grip
- absurdly tiny hero object, normally 5–20mm and <=0.50 paw width
- handcrafted miniature workbench/diorama realism
- process-first tactile making
- calm long-take ASMR
- default high-oblique maker view; top-down/side-oblique allowed
- literal cat-eye first-person POV is not mandatory
- no AI-cat human-job/character-performance regression

Primary optimization is **usable motion/credit, engaged views/credit, subscribers/100 credits**, not simply minimum credits/video.

## Current production state

`production/NEXT_EPISODE.txt` = **TK-005**

Title: `猫の前足で作る、12mmの焼きいも。`
Manifest: `episodes/TK-005.yaml`
Runtime tier: `immersive_h40`
Current non-Ultra first-pass ceiling: 4 Veo 3.1 Lite generations / 40 credits
Expected final: ~32–35s if all four beats remain independently useful

Visual intent:
- stable Mini Forest-style high-oblique maker view
- front paws only where human hands normally would enter
- 12mm yakiimo dramatically smaller than paw
- same tray / warmer / serving niche through KF0→KF4
- zero-cut calm long takes
- one active paw-safe action per generation + optional passive payoff
- G4 = tray slide, then passive steam only

Paid continuity:
- G1: KF0 → KF1
- G2: actual saved G1 PASS frame → KF2
- G3: actual saved G2 PASS frame → KF3
- G4 only if still justified: actual saved G3 PASS frame → KF4

## Material improvement in this iteration — zero-credit 1080p finishing

Official Google Flow Help rechecked 2026-08-29 documents:
- Veo 3.1 Lite: non-Ultra 10 credits/generation, Ultra 5 credits/generation
- non-subscriber: 50 free Flow credits/day
- **1080p upscale: 0 credits for Google AI Plus / Pro / Ultra subscribers**
- 1080p upscale is unavailable to non-subscribers
- actual Flow UI displayed cost remains final truth at execution time

This is materially useful because it improves delivered visual quality without increasing paid generation count.

New operator rule:
- use 1080p upscale only on QC-PASS clips
- preferably wait until the continuity chain is complete, or until that clip is no longer needed as a continuity source
- before clicking, verify the active account is eligible and Flow currently displays 0 credits
- do not upscale FAIL/reroll candidates
- do not use an upscaled/re-encoded export as the next scene First frame
- next-scene continuity remains the previous PASS clip's **native Save frame**
- 1080p upscale never justifies extra generation, padding, or weaker QC

Updated in the same change:
- `tools/make_next_short.ps1` now surfaces the PASS-only 1080p finishing rule to the normal operator path
- `CURRENT_STANDARD.md` now makes the rule executable production policy
- `docs/23_minimum_credit_operator_architecture.md` now includes the finishing step and continuity guard
- this handoff synchronized in the same branch

Production impact:
- no change to TK-005 content, runtime, H40, scene count, keyframes, Progressive Spend, or 40-credit non-Ultra first-pass ceiling
- no Flow credits spent
- no publishing

## Canonical validation / selection state

Candidate selection:
- `tools/select_next_episode.py` is fail-closed
- hero-scale ratio max must be <=0.50 paw width
- paw actions must stay in `nudge / press / pat / roll / steady / slide / tap / push`
- unsupported human-dexterity actions are rejected before ranking
- legacy `POV_PAWS_MICROWORLD_V1` is compatibility-only

Manifest / bundle validation:
- canonical production semantic gate is `tools/validate_maker_view_manifest.py`
- all production bundle entry points route through it
- `validate_current_standard.py` is internal structural/runtime validation behind the adapter, not a direct current-semantic entry point
- legacy POV values may remain only as compatibility data and cannot restore mandatory literal first-person framing

## Flow / spend baseline

Current baseline:
- Veo 3.1 Lite
- output count 1
- non-Ultra 10 credits/generation
- Ultra 5 credits/generation
- actual UI model/mode/output count/displayed cost = generation-time final truth

Progressive Spend:

```text
free/no-charge planned KF chain PASS
→ G1 only
→ QC
→ native Save frame
→ G2 only after G1 PASS
→ G3 only after G2 PASS
→ G4 only if runtime/manifest still justifies independent final value
→ continuity chain complete
→ eligible subscription + UI shows 0 credits: QC-PASS clips may be upscaled to 1080p
```

Never spend Flow credits, generate paid video, or publish without explicit user action.

## Current learning

One real preflight failure remains recorded:
- full cat/body visible
- hero scale too large
- human-like tool-use risk

Correct interpretation:
- observer/maker-view itself is not a failure
- body reveal + character-performance framing + weak miniature scale is the failure
- maker-view + paws-only + tiny workpiece is desirable

No trustworthy public 24h/72h Tiny Cat Kitchen performance sample yet. Do not learn from placeholders/theoretical zeros.

## Research / candidate state

Primary benchmark class:
- realistic miniature cooking/making
- handcrafted tiny-food process
- relaxing tactile ASMR

AI-cat channels remain secondary only for narrow paw/anatomy/reliability evidence. Never copy exact title, plot, branded product/package, distinctive set/dish styling, or ending.

Evidence saturation remains active. Same-class promotional/retail signals do not justify commits unless they change ranking, timing, evidence class, production mechanics, Flow assumptions, freshness, or actual production learning.

2026-08-29 cross-check:
- sweet-potato/yakiimo evidence remains saturated and still supports TK-005
- no stronger current creator-performance or Japanese seasonal signal changed candidate ordering
- benchmark/backlog were intentionally not churned
- official Flow 1080p upscale eligibility/cost is a new platform-cost/quality mechanic and therefore did justify this material change

Candidate state:
- TK-005 / IDEA-009 remains current production choice
- IDEA-001 月見 and IDEA-010 新米塩むすび remain strong future seasonal candidates

## Current roadmap / next priorities

1. Keep all production entry points routed through `validate_maker_view_manifest.py`.
2. Run current maker-view manifest/bundle path for TK-005 when the user executes `./tools/make_next_short.ps1`.
3. Create/approve TK-005 KF0 master anchor in real Flow.
4. Derive KF1→KF4 sequentially with stable paws/scale/camera/props/lighting.
5. Generate G1 only after planned KF chain passes.
6. QC maker-view / paws-only / scale / anatomy / fixed props / zero-cut behavior.
7. PASS → save actual native usable final frame → continue progressively.
8. After chain completion, if eligible and UI shows 0 credits, upscale QC-PASS clips to 1080p before final editing/export.
9. Record actual credits, rerolls, usable motion, G-stage pass/fail, failure class.
10. After upload, record 24h/72h Stayed to watch, APV, engaged views, subscribers, comments.
11. Use accumulated real evidence to adjust actions, runtimes, scores, and spend strategy.

## Safety / invariants

- no automatic paid generation
- no automatic YouTube publishing
- no exact competitor copying
- no full-cat/face/body default shots
- no human hands/fingers/thumbs
- no human-like paw grip
- no candidate hero-scale ratio >0.50 paw width without documented exception
- no unsafe candidate paw-action family through selector
- no paid G1 before planned KF continuity passes
- no next paid scene after prior structural failure
- actual previous PASS native saved frame is the continuity bridge
- upscaled/re-encoded exports are not continuity bridges
- non-first-person maker view is not a failure by itself
- no direct production entry point to legacy structural validator
- no runtime padding
- no research churn after saturation
- no unrelated repository modifications
- every material change synchronizes this handoff

## Change log

### 2026-08-29 — zero-credit 1080p PASS finishing
Baseline: `main@ffba0bde59ac67d282ce459265b77b03288cd3b5`.

Changed:
- documented official Plus/Pro/Ultra 1080p upscale at current 0-credit cost
- added PASS-only, post-continuity upscale rule to `CURRENT_STANDARD.md`
- added same finishing rule to `docs/23_minimum_credit_operator_architecture.md`
- surfaced the rule in `tools/make_next_short.ps1`
- synchronized this handoff

Why:
- this increases delivered resolution without increasing paid generation count, while protecting native saved-frame continuity and Progressive Spend

Production impact:
- TK-005 remains H40 / four Lite generations / 40-credit non-Ultra first-pass ceiling
- no content/ranking/keyframe/action changes
- no credits spent; no publishing

### 2026-08-29 — canonical bundle maker-view validation path
- routed bundle creation through `validate_maker_view_manifest.py`
- preserved structural/runtime validation behind the current-semantic adapter

### 2026-08-29 — candidate selector maker-view safety gates
- enforced <=0.50 paw-width scale and feline-safe action allowlist before ranking

### 2026-08-29 — canonical maker-view manifest validator
- aligned one-command manifest validation with Mini Forest-style maker-view semantics

### 2026-08-29 — TK-005 maker-view spend-gate correction
- replaced stale active POV stop-gate wording with maker-view semantics

### 2026-08-29 — sweet-potato search-demand evidence
- added a distinct search-behavior evidence class; TK-005 remained top-ranked

### 2026-08-28 — product governance
- added `PRODUCT_CHARTER.md`
- wired charter into the improvement loop
- established Mini Forest-style miniature making + feline front paws replacing human hands as canonical visual identity
