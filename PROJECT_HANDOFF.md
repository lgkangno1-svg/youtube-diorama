# Tiny Cat Kitchen — PROJECT HANDOFF

Last update: **2026-08-29 KST**
Baseline inspected for this iteration: `main@a4b24d907c71a2c245e44d089c25d4e893b6eb95`

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

Nano Banana is free in the user's current Google usage context. Existing cost/model checks remain safety rails only. Do not spend improvement cycles polishing those guards unless a real problem returns. Paid Veo generation and publishing remain explicit user actions.

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
Current non-Ultra first-pass ceiling: up to 4 Veo 3.1 Lite generations / 40 video credits
Primary operator runbook: `production/TK-005_OPERATOR_CARD.md`

Quality intent:
- HOOK: first 1–2s instantly read as feline paws + absurdly tiny 12mm yakiimo + real miniature making
- TRANSFORMATION: warm/darken → crack/steam → golden center → optional quiet serving resolution
- SCALE PROOF: hero roughly 18–32% of visible paw width
- PAYOFF: bright golden center + steam; G4 only if serving niche adds independent satisfaction
- same tray / warmer / serving niche / camera / paw identity through the chain

Scene actions:
- G1 `nudge`
- G2 `press`
- G3 `slide`
- G4 `slide` only if value-gated after real G3

Continuity:
- G1 KF0→KF1
- G2 actual saved G1 PASS frame→KF2
- G3 actual saved G2 PASS frame→KF3
- G4 actual saved G3 PASS frame→KF4 only if still justified

## Material improvement in this iteration — normal one-command path now uses Operator Card first

Problem found after inspecting the merged PR #67 state:
- PR #67 created a strong `production/TK-005_OPERATOR_CARD.md` with exact-order, copy/paste-ready prompts and a clear NOW action.
- however, the actual normal command `./tools/make_next_short.ps1` still told the user to follow generated bundle/flow-pack files and prominently surfaced the older cost-first checklist.
- `tools/make_short.ps1` likewise sent the user first to generated artifacts.
- result: the repo had a faster quality-first runbook, but the user's one-command path did not actually lead to it. This preserved avoidable navigation/decision burden and contradicted the latest quality/speed priority.

Changed:
- `tools/make_next_short.ps1`
  - detects `production/${EpisodeId}_OPERATOR_CARD.md`
  - shows **YOUR NEXT ACTION** and points to the Operator Card first
  - for TK-005 explicitly tells the operator to make/approve the strongest KF0 scale-hook anchor first
  - moves generated bundle/flow-pack to technical reference/fallback status
  - replaces the cost-centric visible checklist with quality-first Progressive Flow: visual preflight → G1 quality gate → PASS/native frame → next scene → optional value-gated G4
- `tools/make_short.ps1`
  - surfaces **PRIMARY RUNBOOK** = episode Operator Card when present
  - keeps generated artifacts as fallbacks
  - prioritizes hook/scale/transformation/continuity and Progressive Spend
  - preserves the prior Nano Banana 2 Lite + UI no-charge + STOP wording as a safety rail so existing regression protection is not weakened
- `tools/test_operator_card_first_path.py`
  - regression guard requiring both normal scripts to prefer the Operator Card while retaining generated fallbacks
- `CURRENT_STANDARD.md`
  - executable standard now explicitly defines Operator-Card-First as the primary production surface

Why material:
- directly reduces manual navigation and ambiguity in the user's normal one-command path
- makes the strongest current quality artifact actually discoverable at the moment of production
- reduces time-to-first-valid-G1 without spending credits or adding fragile automation
- aligns implementation with the user's explicit priority: video quality + convenience + faster production

Production impact:
- no change to TK-005 concept, H40 ceiling, scene actions, candidate ranking, or paid authorization
- no Flow/Veo credits spent
- no publishing

## Canonical validation / safety state

- candidate selector fail-closed for <=0.50 paw-width scale and feline-safe actions
- canonical manifest/bundle semantic entry is `tools/validate_maker_view_manifest.py`
- every paid scene declares exactly one safe `paw_action_family`
- `maker_view_failure` / `character_failure` are current learning fields; `pov_failure` compatibility-only
- non-first-person maker view is not a failure by itself
- actual previous PASS native saved frame is the next-scene continuity bridge
- structural FAIL stops the next paid scene

These safety gates stay. Current improvement focus is content/operator quality unless a real regression appears.

## Research / evidence state

This run rechecked current miniature/ASMR ecosystem signals. Large miniature-cooking channels remain active at scale, and current public channel snapshots continue to reinforce the already-known combination of tiny-food readability, tactile/satisfying process and ASMR. No new evidence changed TK-005 ranking, timing or mechanics, so `research/benchmark_log.csv` and backlog were intentionally not churned under the saturation gate.

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
- 24h/72h Stayed to watch/APV/engaged views/subscribers/comments

## Current roadmap / next priorities

1. Run `./tools/make_next_short.ps1`; it should now point directly to `production/TK-005_OPERATOR_CARD.md`.
2. Do only the Operator Card NOW action first: make the strongest KF0 scale-hook anchor.
3. Derive KF1→KF4 sequentially; reject scale/camera/prop drift before paid video.
4. Generate G1 only after visual continuity passes; judge first-1–2s readability and feline-safe nudge quality.
5. PASS → native Save frame → continue progressively.
6. After real G3, keep G4 only if it adds independent resolution value.
7. Record production-time/manual-intervention data so future tooling can remove the next largest friction point.
8. After at least one real run, consider automatic Operator Card generation from manifest data if it reduces maintenance without fragility.
9. Use real 24h/72h audience results to adjust hook/action/runtime priors.

## Safety / invariants

- no automatic paid generation
- no automatic YouTube publishing
- no exact competitor copying
- no full-cat/face/body default shots
- no human hands/fingers/thumbs or human-like paw grip
- no weak-scale regression
- no next paid scene after structural failure
- actual previous PASS native frame is continuity bridge
- no runtime padding
- no research churn after saturation
- no unrelated repository changes
- every material change synchronizes this handoff

## Change log

### 2026-08-29 — Operator-Card-First normal path
Baseline: `main@a4b24d907c71a2c245e44d089c25d4e893b6eb95`.

Changed:
- `tools/make_next_short.ps1`: primary next action now points to the episode Operator Card and quality-first G1 path
- `tools/make_short.ps1`: Operator Card becomes PRIMARY RUNBOOK; generated artifacts become fallbacks; old safety rail retained without dominating UX
- `tools/test_operator_card_first_path.py`: regression coverage
- `CURRENT_STANDARD.md`: executable Operator-Card-First rule
- synchronized this handoff

Why:
- PR #67 created the right fast-quality artifact but the real one-command path did not surface it

Production impact:
- TK-005 remains H40 / up to four paid Lite scenes / current 40-credit non-Ultra ceiling
- no paid generation/publishing

### 2026-08-29 — TK-005 quality operator card
- explicit HOOK / TRANSFORMATION / SCALE PROOF / PAYOFF / JAPAN FIT
- exact-order copy/paste KF/G prompts

### 2026-08-29 — quality/speed priority correction
- video/content quality → viewer outcome → production speed/convenience → paid-video efficiency → free-image cost policing
