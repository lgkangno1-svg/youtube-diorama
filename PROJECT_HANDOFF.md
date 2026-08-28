# Tiny Cat Kitchen — PROJECT HANDOFF

Last update: **2026-08-29 KST**
Baseline inspected before this iteration: `main@738175d39467280f831642c96cb288778e189aea`

Durable current-state handoff for `lgkangno1-svg/youtube-diorama`. Every material repository change updates this file in the same branch/PR. True NO-OP research does not churn it.

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

Tiny Cat Kitchen is a Japanese-target healing Shorts system for realistic miniature cooking/making where **human hands are naturally replaced by feline front paws**.

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

Primary optimization is not minimum credits/video. Prefer **usable motion/credit, engaged views/credit, subscribers/100 credits** while protecting quality and explicit user control.

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

## New material correction — bundle builder validator bypass

A second-stage regression remained after the earlier maker-view validator fix.

Observed path before this iteration:

```text
make_next_short.ps1
→ validate_maker_view_manifest.py PASS
→ make_short.ps1
→ build_episode_bundle.py
→ validate_current_standard.py DIRECTLY
```

The direct legacy structural validator still requires compatibility-only fields such as the old `stop_if_pov_scale_anatomy_or_premise_fails` gate. TK-005 intentionally uses the current `stop_if_maker_view_scale_anatomy_or_premise_fails` gate, so the normal command could pass the first maker-view preflight and then be rejected while building the bundle. Direct `build_episode_bundle.py` invocation had the same regression risk.

Corrected behavior:
- `build_episode_bundle.py` now calls `validate_maker_view_manifest.py` as its canonical production-standard preflight
- the maker-view adapter validates current semantics first
- only inside that adapter are compatibility-only fields translated before delegating mature runtime/credit/keyframe/sequential-chain checks to `validate_current_standard.py`
- `build_episode_bundle.py` no longer calls the legacy structural validator directly
- regression test now asserts the canonical maker-view gate exists and the direct legacy call does not
- originality validation still runs after current-standard validation and before any generated files are created

Why this matters:
- the user's intended one-command interface must actually reach production-pack generation with a current valid manifest
- a validator architecture that passes at the shell entry point but fails deeper in the same command is operationally equivalent to a broken workflow
- this change does not weaken structural validation; it only routes it through the current semantic adapter

Production impact:
- TK-005 selection/content/runtime/credit budget unchanged
- no Flow credits spent
- no publishing

## Candidate selector safety gate

`tools/select_next_episode.py` is fail-closed on current candidate mechanics.

Current behavior:
- legacy `POV_PAWS_MICROWORLD_V1` is compatibility-only
- candidate `hero_scale` must declare a paw-width ratio with maximum <=0.50
- `paw_action_family` must remain within `nudge / press / pat / roll / steady / slide / tap / push`
- unsupported actions such as `pinch` are rejected before ranking
- runtime prior must be `compact_h30` or `immersive_h40`
- evidence/trend/novelty gates remain active

## Manifest validation state

The canonical production semantic gate is `tools/validate_maker_view_manifest.py`.

Current semantics require:
- `visual_intent = mini_forest_style_paws_only_miniature_making`
- `semantic_override = mini_forest_style_observational_maker_view`
- `first_person_required = false`
- preferred angles include `high_oblique_maker_view`
- `stop_if_maker_view_scale_anatomy_or_premise_fails = true`
- legacy `stop_if_pov...` gate is not active

All production bundle entry points must route through this adapter. `validate_current_standard.py` is an internal structural/runtime validator behind the adapter, not a direct current-semantic production entry point.

Legacy `first_person_cat_pov` / `POV_PAWS_MICROWORLD_V1` values can remain only as compatibility data and must never restore literal first-person as a creative requirement.

## Flow / spend baseline

Current repository baseline remains:
- Veo 3.1 Lite
- output count 1
- non-Ultra: 10 credits/generation
- Ultra: 5 credits/generation
- non-subscriber baseline: 50 free Flow credits/day under the currently documented free route
- actual active Flow UI model/mode/output count/displayed cost is generation-time final truth

This run rechecked current public information and found no sufficiently verified official change that justifies altering production assumptions. Third-party discussion of temporary subscriber bonus credits was not promoted into repository truth without direct official verification.

Progressive Spend:

```text
free/no-charge planned KF chain PASS
→ G1 only
→ QC
→ native Save frame
→ G2 only after G1 PASS
→ G3 only after G2 PASS
→ G4 only if runtime/manifest still justifies independent final value
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

AI-cat channels are secondary only for narrow paw/anatomy/reliability evidence. Never copy exact title, plot, branded product/package, distinctive set/dish styling, or ending.

Evidence saturation remains active. Same-class promotional/retail signals do not justify commits unless they change ranking, timing, evidence class, production mechanics, Flow assumptions, freshness, or actual production learning.

Fresh 2026-08-29 checks:
- current miniature-cooking channels remain large and active, supporting the existing tactile miniature benchmark class rather than introducing a new production mechanic
- sweet-potato/yakiimo evidence remains saturated across behavioral/search/preference/activation classes
- no stronger creator-performance or seasonal evidence changed TK-005 ranking in this run
- no research/backlog churn was justified

Candidate state:
- TK-005 / IDEA-009 remains current production choice
- IDEA-001 月見 and IDEA-010 新米塩むすび remain strong future seasonal candidates
- no ranking change justified without stronger creator-performance, behavioral demand, or Tiny Cat Kitchen production evidence

## Legacy artifact caution

TK-001–TK-004 may contain pre-correction concepts/statuses. They are history, not authority over the current maker-view standard.

Do not revive an old manifest solely from `ready-for-flow`/`planned` status. Refresh it through current candidate + maker-view validation first.

## Current roadmap / next priorities

1. Keep all production entry points routed through `validate_maker_view_manifest.py`; do not reintroduce direct legacy structural validation.
2. Run the current maker-view manifest validation/bundle path for TK-005 locally when the user executes the command.
3. Create/approve TK-005 KF0 master anchor in real Flow.
4. Confirm genuine miniature making with paws replacing hands, not an AI-cat character scene.
5. Derive KF1→KF4 sequentially with stable paws/scale/camera/props/lighting.
6. Generate G1 only after planned KF chain passes.
7. QC maker-view / paws-only / scale / anatomy / fixed props / zero-cut behavior.
8. PASS → save actual usable final frame → continue progressively.
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
- actual previous PASS frame is the continuity bridge
- non-first-person maker view is not a failure by itself
- no direct production entry point to legacy structural validator
- no runtime padding for its own sake
- no research churn after saturation
- no unrelated repository modifications
- every material change synchronizes this handoff

## Change log

### 2026-08-29 — canonical bundle maker-view validation path
Baseline: `main@738175d39467280f831642c96cb288778e189aea`.

Changed:
- fixed `tools/build_episode_bundle.py` to invoke `validate_maker_view_manifest.py` instead of `validate_current_standard.py` directly
- preserved legacy structural/runtime validation behind the adapter rather than bypassing it
- updated bundle regression test to reject reintroduction of the direct legacy gate
- synchronized `CURRENT_STANDARD.md` and this handoff

Why:
- the normal one-command path could otherwise pass maker-view validation and then fail during bundle creation on the obsolete POV stop-gate requirement

Production impact:
- no change to TK-005, NEXT_EPISODE, H40, 40-credit non-Ultra first-pass ceiling, current manifest actions, keyframes, audio, or Flow settings
- no credits spent; no publishing

### 2026-08-29 — candidate selector maker-view safety gates
- strengthened `tools/select_next_episode.py` production compatibility gate
- enforced explicit <=0.50 paw-width scale declaration and feline-safe action allowlist
- synchronized `CURRENT_STANDARD.md` and handoff

### 2026-08-29 — canonical maker-view manifest validator
- added `validate_maker_view_manifest.py`
- aligned shell entry preflight with current maker-view semantics

### 2026-08-29 — TK-005 maker-view spend-gate correction
- renamed active progressive spend gate from stale POV wording to maker-view semantics

### 2026-08-29 — sweet-potato search-demand evidence
- added new search-behavior evidence class for `さつまいもスイーツ`; TK-005 remained top-ranked

### 2026-08-28 — product governance
- added `PRODUCT_CHARTER.md`
- wired charter into improvement loop
- established Mini Forest-style miniature making + feline front paws replacing human hands as canonical visual identity
