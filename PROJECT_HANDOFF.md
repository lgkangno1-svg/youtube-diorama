# Tiny Cat Kitchen — PROJECT HANDOFF

Last update: **2026-08-29 KST**
Baseline inspected for this iteration: `main@9120f69fcac0874e2b5f4aa03ddc6f3a0b3ae73f`

Durable current-state handoff for `lgkangno1-svg/youtube-diorama`. Every material change updates this file in the same branch/PR; true NO-OP does not churn it.

## Start-of-run contract

Before material work: inspect latest main/recent PRs → read this handoff → `PRODUCT_CHARTER.md` → cross-check `START_HERE.md`, `CURRENT_STANDARD.md`, docs/22/23/27, NEXT_EPISODE/current manifest, benchmark/backlog/ledger. Newer explicit user direction and latest merged state override stale scheduled wording.

Document roles:
- `PROJECT_HANDOFF.md`: current state / decisions / failures / learning / next priorities
- `PRODUCT_CHARTER.md`: durable purpose / priority order / improvement criteria
- `CURRENT_STANDARD.md`: executable production/QC/operator rules
- manifests + ledgers: episode plan + observed evidence

## Durable priority order

Latest explicit user direction:
1. video/content quality
2. viewer outcome / recognizable channel identity
3. production convenience and speed
4. paid-video reroll/credit efficiency
5. free-image cost policing

Nano Banana is available free in the user's Google usage context. Existing safety wording can remain, but do not spend iterations polishing image-cost gates unless a real problem returns. Paid Veo generation and publishing still require explicit user action.

## Durable product intent

Japanese-target healing Shorts: realistic handcrafted miniature cooking/making with one or two cream/pale-ginger feline front paws replacing the visual role of human hands.

Non-negotiable:
- no face/head/body/full cat
- no human hands/fingers/thumbs
- no human-like feline grip
- hero normally 5–20mm and <=0.50 paw width
- miniature process is the protagonist
- high-oblique maker view by default; top-down/side macro allowed
- literal first-person POV not mandatory
- calm tactile long takes / close ASMR
- no AI-cat job/character-performance regression

## Current production state

`production/NEXT_EPISODE.txt` = **TK-005**
Title: `猫の前足で作る、12mmの焼きいも。`
Manifest: `episodes/TK-005.yaml`
Runtime tier: `immersive_h40`
Current non-Ultra first-pass ceiling: up to 4 Veo 3.1 Lite generations / 40 video credits

Visual intent:
- Mini Forest-style high-oblique maker view
- paws only
- 12mm yakiimo dramatically smaller than paw
- same tray/warmer/serving niche through KF0→KF4
- zero-cut calm takes
- G1 `nudge`, G2 `press`, G3 `slide`, G4 `slide`

Continuity:
- G1 KF0→KF1
- G2 actual saved G1 PASS frame→KF2
- G3 actual saved G2 PASS frame→KF3
- G4 only if still justified: actual saved G3 PASS frame→KF4

## Material improvement in this iteration — TK-005 is now quality-first and operator-ready

Problem found after cross-checking the current manifest against the newly merged quality/speed standard:
- TK-005 had technically valid keyframes/actions, but the manifest did not explicitly encode the new five-part quality gate: HOOK / TRANSFORMATION / SCALE PROOF / PAYOFF / JAPAN FIT.
- A user still had to reconstruct the exact production order and copy/paste prompts from multiple files/generated artifacts.
- The most important first-pass quality decision — whether KF0 instantly communicates `cat paws + absurdly tiny 12mm food + real miniature making` — was not isolated as the current action.

Changed:
- `episodes/TK-005.yaml` now includes a `content_quality` block with:
  - explicit visual hook
  - scale proof
  - Japan-fit rationale
  - final payoff
  - G1→G4 visible state transformations
  - first-pass quality priorities
- added `production/TK-005_OPERATOR_CARD.md`, a single fast-production surface containing:
  - one clear current action: create/approve KF0 first
  - copy/paste-ready KF0 prompt
  - sequential KF1→KF4 change prompts
  - exact G1→G4 video prompts
  - scene-specific PASS criteria
  - G3→G4 adaptive runtime decision
  - final-edit priorities

Why this is material:
- it directly improves the Short rather than adding another process/cost warning
- it makes scale/readability/payout goals explicit before paid generation
- it reduces prompt reconstruction/manual decision load
- it makes G1 the primary paid quality checkpoint and preserves Progressive Spend

Production impact:
- no change to TK-005 ranking, H40 ceiling, safe paw actions or paid-video authorization
- no Flow/Veo credits spent
- no publishing

## TK-005 quality gate now encoded

HOOK:
- KF0 must instantly read as two real feline paws + one impossibly tiny 12mm purple sweet potato on a thumbnail-sized tray.

TRANSFORMATION:
- G1: tray moves toward heat / skin subtly warms
- G2: small natural crack + thin steam
- G3: existing crack widens / golden center appears
- G4: same finished tray slides into the already-visible serving niche

SCALE PROOF:
- hero remains roughly 18–32% of one visible paw width; KF0/G1 is the strongest proof shot.

PAYOFF:
- bright golden center + soft steam; optional final world-resolution in the same serving niche.

JAPAN FIT:
- current late-August/early-autumn sweet-potato recognition remains strong; use generic yakiimo cues only.

## Fast-production operator target

Normal interface remains:
```text
다음 영상 준비해줘
```

For TK-005, the immediate execution surface is now:
`production/TK-005_OPERATOR_CARD.md`

The card is intentionally organized so the operator does not need to reconstruct the flow:
```text
KF0 strongest scale frame
→ derive KF1→KF4 in same world
→ G1 only
→ PASS / native Save frame
→ G2
→ PASS / native Save frame
→ G3
→ decide if story is already complete
→ G4 only if it adds a real final payoff
```

Future tooling should make this kind of card generated automatically from manifest `content_quality` + scene data rather than hand-maintained, once that can be done without adding fragility.

## Canonical validation state

- candidate selector fail-closed for <=0.50 paw-width scale and feline-safe actions
- canonical manifest/bundle semantic entry is `tools/validate_maker_view_manifest.py`
- every paid scene declares exactly one safe `paw_action_family`
- `maker_view_failure` / `character_failure` are current learning fields; `pov_failure` is compatibility-only
- non-first-person maker view is not a failure by itself

These gates stay; current priority is content/operator quality unless a real structural regression appears.

## Flow / production baseline

Progressive Spend remains:
```text
strong visual/keyframe continuity PASS
→ G1 only
→ quality QC
→ actual native Save frame
→ G2 only after G1 PASS
→ G3 only after G2 PASS
→ G4 only if independent payoff remains worthwhile
```

Actual Flow UI at paid generation time remains final truth for model/mode/output count/displayed cost. No automatic paid generation/publishing.

## Current learning

One real preflight failure remains:
- full cat/body visible
- hero scale too large
- human-like tool-use risk

Interpretation: observer maker-view is fine; character framing, weak scale and human-like manipulation are failures.

No trustworthy public 24h/72h Tiny Cat Kitchen sample yet. Do not learn from placeholders.

When real production begins, also record when practical:
- preparation minutes
- manual interventions
- prompt corrections before G1
- time-to-first-valid-G1

## Research / candidate state

Fresh 2026-08-29 cross-check:
- current Japanese sweet-potato launches continue into early September and reinforce existing yakiimo timing.
- adjacent Japanese food Shorts continue to show strong engagement for clear close-up process/ASMR, but this adds no distinct mechanic beyond the already saturated process-first ASMR evidence.
- therefore `research/benchmark_log.csv` and candidate ranking were intentionally not churned.

TK-005 / IDEA-009 remains current production choice. 月見 and 新米塩むすび remain strong future seasonal classes.

## Current roadmap / next priorities

1. Use `production/TK-005_OPERATOR_CARD.md` to make and approve the strongest possible KF0 anchor.
2. Derive KF1→KF4 from the approved prior frame; reject scale/camera/prop drift before video spend.
3. Generate G1 only after the visual chain passes; judge first-1–2s scale readability and feline-safe nudge quality.
4. If G1 passes, use the native saved frame and continue progressively.
5. After real G3, decide whether G4 still adds independent satisfaction; drop it if it has become padding.
6. Record actual preparation time, prompt corrections, manual interventions, rerolls and video metrics.
7. After at least one real production run, consider generating the fast operator card automatically from manifest `content_quality` and scene data to remove hand-maintenance.
8. Use 24h/72h actual audience results to adjust hook/action/runtime priors.

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

### 2026-08-29 — TK-005 quality operator card
Baseline: `main@9120f69fcac0874e2b5f4aa03ddc6f3a0b3ae73f`.

Changed:
- `episodes/TK-005.yaml`: explicit content-quality gate and scene transformations
- `production/TK-005_OPERATOR_CARD.md`: exact-order, copy/paste-ready KF/G production card with PASS criteria
- synchronized this handoff

Why:
- quality/speed priorities were merged in #66, but TK-005 itself still required manual reconstruction; this turns the new standard into an immediately usable production artifact

Research:
- fresh sweet-potato/ASMR signals were checked but are same-class/saturated and did not justify benchmark/backlog churn

Production impact:
- TK-005 remains H40 / up to four paid Lite video generations / current 40-credit non-Ultra ceiling
- no paid generation or publishing

### 2026-08-29 — quality/speed priority correction
- product priority order changed to video/content quality → viewer outcome → production speed/convenience → paid-video efficiency → free-image cost policing
- Nano Banana cost-gate hardening explicitly deprioritized
