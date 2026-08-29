# Tiny Cat Kitchen — PROJECT HANDOFF

Last update: **2026-08-29 KST**
Baseline inspected for this iteration: `main@8f91f04e95a8d42ae9597be91a5a639dbe610f89`

Durable current-state handoff for `lgkangno1-svg/youtube-diorama`. Every material repository change must update this file in the same branch/PR. True NO-OPs do not churn it.

## Start-of-run contract

Before material work:
1. inspect latest main SHA and recent commits/PRs
2. read this handoff
3. read `PRODUCT_CHARTER.md`
4. cross-check `START_HERE.md`, `CURRENT_STANDARD.md`, docs/22/23/27, `production/NEXT_EPISODE.txt`, current manifest, benchmark/backlog/ledger
5. newest explicit user direction + latest merged state override stale automation/chat wording

Document roles:
- `PROJECT_HANDOFF.md`: current state / decisions / failures / learning / next priorities
- `PRODUCT_CHARTER.md`: durable purpose / priority order / improvement criteria
- `CURRENT_STANDARD.md`: executable production/QC/operator rules
- manifests + ledgers: episode plan + observed evidence

## Durable priority order

1. video/content quality
2. viewer outcome / recognizable channel identity
3. production convenience and speed
4. paid-video reroll/credit efficiency
5. free-image cost policing

Nano Banana is free in the user's current Google usage context. Existing model/cost checks remain safety rails only. Do not spend improvement cycles polishing them unless a real problem returns. Paid Veo generation and publishing remain explicit user actions.

## Durable product intent

Japanese-target healing Shorts: realistic handcrafted miniature cooking/making with one or two cream/pale-ginger feline front paws replacing the visual role of human hands.

Non-negotiable:
- no face/head/body/full cat
- no human hands/fingers/thumbs
- no human-like feline grip
- hero normally 5–20mm and <=0.50 paw width
- miniature process is the protagonist
- high-oblique maker view default; top-down/side macro allowed
- literal first-person POV not mandatory
- calm tactile long takes / close ASMR
- no AI-cat job/character-performance regression

## Current production state

`production/NEXT_EPISODE.txt` = **TK-005**
Title: `猫の前足で作る、12mmの焼きいも。`
Manifest: `episodes/TK-005.yaml`
Runtime tier: `immersive_h40`
Current non-Ultra first-pass ceiling: **up to** 4 Veo 3.1 Lite generations / 40 video credits
Primary operator runbook: `production/TK-005_OPERATOR_CARD.md`

Core story:
- G1 `nudge` — impossible scale + warming start
- G2 `press` — crack + steam
- G3 `slide` — complete golden-center payoff
- G4 `slide` — optional same-world serving resolution only after real G3 review

Normal final runtime if G3 is complete: ~24–27s. Optional G4 may extend to ~32–35s.

## Material improvement in this iteration — next targets now rebase on actual PASS footage

Problem found after PR #70:
- PR #70 correctly deferred optional KF4/G4 until after real G3.
- but the operator path still asked the user to prebuild **KF2 and KF3 before G1**.
- once G1 is generated, its actual last usable frame may differ slightly from planned KF1 in paw fur, camera, tray position, hero scale, lighting or geometry.
- G2 would then start from actual G1 but aim at a KF2 derived from planned KF1, forcing Veo to reconcile two slightly different worlds.
- the same mismatch could repeat for G3.
- prebuilding KF2/KF3 also delays time-to-first-valid-G1 even though those targets are not needed yet.

Corrected current strategy:

```text
KF0 → derive KF1 → G1
G1 PASS → native Save frame → derive KF2 from ACTUAL G1 saved frame → G2
G2 PASS → native Save frame → derive KF3 from ACTUAL G2 saved frame → G3
G3 PASS → review core → STOP if complete
optional only: derive KF4 from ACTUAL G3 saved frame → G4
```

Important semantic clarification:
- `episodes/TK-005.yaml` may continue to describe KF2/KF3/KF4 destination states.
- those descriptions define **what the future state should become**, not when the image must be created.
- the production source for each next target is now the previous real PASS frame whenever Flow permits it.

Why this matters:
- improves real continuity because each target inherits actual paw/camera/scale/props/light
- reduces how far Veo must correct between real start frame and planned end frame
- shortens pre-G1 preparation to KF0 + KF1 only
- reduces speculative image work
- provides a measurable hypothesis for fewer continuity rerolls and faster production

Google Flow official Help was rechecked on 2026-08-29 and explicitly documents that a saved video frame can be used as a future generation's start or end frame. Veo 3.1 First+Last Frames remains supported in current model documentation. Actual Flow UI remains final truth.

Changed in this branch:
- `production/TK-005_OPERATOR_CARD.md`
  - G1 requires only KF0+KF1
  - after G1 PASS, KF2 is derived from actual saved G1 frame
  - after G2 PASS, KF3 is derived from actual saved G2 frame
  - optional KF4 remains derived from actual saved G3 frame
- `CURRENT_STANDARD.md`
  - actual-frame target rebasing is now default core continuity rule
- `START_HERE.md`
  - user-facing normal path reflects first-pair-only pre-G1 preparation
- `docs/23_minimum_credit_operator_architecture.md`
  - operator architecture now prioritizes actual-frame rebasing over speculative full-chain prebuild
- `docs/22_continuous_episode_learning_engine.md`
  - adds actual-frame rebasing as a production hypothesis to measure
- this handoff synchronized in the same branch

Production impact:
- no paid generation performed
- no publishing
- TK-005 story/ranking/actions/runtime ceiling unchanged
- maximum paid ceiling remains up to 40 credits
- user reaches first paid checkpoint sooner and each later target is based on real footage

## Canonical validation / safety state

- candidate selector fail-closed for <=0.50 paw-width scale and feline-safe actions
- canonical manifest/bundle semantic entry is `tools/validate_maker_view_manifest.py`
- every paid scene declares exactly one safe `paw_action_family`
- `maker_view_failure` / `character_failure` are current learning fields; `pov_failure` compatibility-only
- non-first-person maker view is not a failure by itself
- structural FAIL stops the next paid scene
- actual previous PASS native saved frame is the next-scene continuity bridge
- **actual previous PASS frame should also be the source/reference for deriving the next target KF whenever supported**
- adaptive H40 current semantic: three complete core beats, optional fourth only after real G3 review

## Research / evidence state

Fresh 2026-08-29 cross-check did not reveal a new benchmark/seasonal evidence class that changes TK-005 ranking, timing or content mechanics. Existing yakiimo/oimo evidence remains saturated and supportive. `research/benchmark_log.csv` and backlog were intentionally not churned.

TK-005 / IDEA-009 remains current. 月見 and 新米塩むすび remain strong future seasonal candidates.

## Current learning

One real preflight failure remains recorded:
- full cat/body visible
- hero scale too large
- human-like tool-use risk

Interpretation:
- observer maker-view itself is fine
- character framing, weak scale and human-like manipulation are failures

No trustworthy public 24h/72h Tiny Cat Kitchen performance sample yet. Do not learn from placeholders.

When real production begins, record when practical:
- preparation minutes
- manual interventions
- prompt corrections before G1
- time-to-first-valid-G1
- credits/rerolls/G-stage pass-fail
- whether actual-frame target rebasing reduced continuity corrections/rerolls
- whether optional G4 was correctly skipped or used after real G3 review
- 24h/72h Stayed to watch/APV/engaged views/subscribers/comments

## Current roadmap / next priorities

1. Run `./tools/make_next_short.ps1`; it should surface `production/TK-005_OPERATOR_CARD.md`.
2. Create/approve KF0.
3. Derive/approve KF1 only. **Do not prebuild KF2/KF3.**
4. Generate G1 only after KF0/KF1 pass.
5. If G1 PASS: Save native last usable frame and derive KF2 from that actual frame.
6. Generate G2; PASS → Save frame → derive KF3 from actual G2.
7. Generate G3 and watch G1→G3 together.
8. If golden-center payoff is complete, stop and edit the ~24–27s Short.
9. Only if real G3 benefits from closure: derive KF4 from actual G3 saved frame and generate optional G4.
10. Record actual preparation time, manual interventions, target corrections, rerolls and audience performance.

## Validation note

This run used connected GitHub state and official Google Flow Help. No local repository clone was available, so `python tools/validate_handoff_update.py --base origin/main` was not run locally. Before merge, inspect branch comparison/PR changed files and ensure this handoff is included.

## Safety / invariants

- no automatic paid generation
- no automatic YouTube publishing
- no exact competitor copying
- no full-cat/face/body default shots
- no human hands/fingers/thumbs or human-like paw grip
- no weak-scale regression
- no next paid scene after structural failure
- actual previous PASS native frame is continuity bridge
- next target should derive from actual PASS frame when supported
- no runtime padding
- no research churn after saturation
- no unrelated repository changes
- every material change synchronizes this handoff

## Change log

### 2026-08-29 — actual-frame-rebased core target chaining
Baseline: `main@8f91f04e95a8d42ae9597be91a5a639dbe610f89`.

Changed:
- before G1, prepare only KF0/KF1
- after each PASS generation, save actual frame and derive the next destination KF from that real frame
- TK-005 Operator Card / CURRENT_STANDARD / START_HERE / docs22 / docs23 synchronized
- this handoff synchronized in the same branch

Why:
- planned KF2/KF3 derived before any video existed could drift away from actual G1/G2 output and make subsequent generations solve unnecessary continuity corrections
- actual-frame rebasing improves continuity and reduces pre-G1 work

Production impact:
- TK-005 remains adaptive H40, G1→G3 core + optional G4
- maximum ceiling unchanged: up to 4 Lite generations / 40 non-Ultra credits
- no credits spent; no publishing

### 2026-08-29 — adaptive H40 core-first / lazy optional G4
- G1→G3 complete core Short; optional KF4/G4 only after real G3 review

### 2026-08-29 — quality-first operating-system alignment
- START_HERE/docs22/docs23 aligned with quality-first Operator-Card-First workflow

### 2026-08-29 — Operator-Card-First normal path
- normal scripts surface episode Operator Card before generated fallback docs

### 2026-08-29 — TK-005 quality operator card
- explicit HOOK / TRANSFORMATION / SCALE PROOF / PAYOFF / JAPAN FIT
