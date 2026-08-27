# Tiny Cat Kitchen — PROJECT HANDOFF

Last update: **2026-08-27 KST**  
Baseline inspected before this change: `main@6cba79965b589b90f2879d8c8288b05619f2902b`

This is the durable handoff source of truth for `lgkangno1-svg/youtube-diorama`. Another AI/developer should be able to continue from GitHub without prior chat history. **Every material repository change must update this file in the same branch/PR.** True NO-OP research should not churn it.

## 1. Mission / development intent

Build a Japanese-target Shorts operating system, not merely an AI-cat generator. The system should absorb the repetitive work of:
- current Japanese/global benchmark research
- Japanese seasonal/cultural/food signal research
- idea generation and scoring
- originality/fingerprint checks
- Veo-safe action design
- Flow credit/runtime planning
- deterministic scene prompts
- character/camera/prop continuity
- edit/publish packs
- 24h/72h production and audience learning

The normal user interface should remain:

```text
다음 영상 준비해줘
```

The system then researches/selects the next novelty-safe episode, creates/updates its manifest and `production/NEXT_EPISODE.txt`, and leaves local operator files ready for:

```powershell
./tools/make_next_short.ps1
```

Never spend Flow credits, generate paid video, or publish to YouTube without explicit user action.

## 2. Viewer-facing goal

Tiny Cat Kitchen Shorts should feel like the viewer **is the cat**, not like the viewer is watching a cat chef.

Core promise:

> True first-person cat POV, only front paws visible, handling food/objects so tiny that the paw-to-object scale contrast itself feels cute and healing.

Initial target market: Japan, especially teen/20s Shorts viewers, while keeping globally readable visual satisfaction and ASMR.

Long-term channel success is not measured by uploads or commits. Optimize:

```text
usable motion / credit
engaged views / credit
subscribers / 100 credits
```

## 3. Channel identity — do not regress

Canonical docs:
- `CURRENT_STANDARD.md`
- `docs/24_hero_cat_brand_identity.md`
- `docs/25_pov_paws_microworld_grammar.md`

Default grammar: `POV_PAWS_MICROWORLD_V1`
- true first-person cat POV
- only cream + pale-ginger real feline front paws near lower edge
- no face/head/eyes/ears/body/tail/full cat
- hero food/object normally 5–20mm
- hero object visually <=0.50 of one visible paw width, preferably 0.15–0.50
- macro miniature diorama workbench
- mostly locked camera / subtle breathing drift only
- one calm tactile primary action + at most one micro-payoff per 8s generation
- preferred paw actions: nudge, press, pat, roll, steady, slide, tap
- avoid fingers/thumbs/human grip/chopsticks/tongs/knife handling
- no rapid montage / meme zoom / third-person chef framing

Structural FAIL even when visually pretty:
- full cat or cat face visible
- third-person cat cooking at a counter
- food/pan comparable to paw size
- human fingers/thumbs
- paw grips tools like a hand
- wide kitchen shot weakens tiny-scale contrast

The core attraction is **impossible miniature scale from the cat's own perspective**, not a cute cat face.

## 4. Hero cat / world

### HERO_CAT_V1
- cream fur base
- pale ginger markings
- real feline paw anatomy
- soft premium/healing tone
- face may exist in profile/branding assets, but default Shorts show paws only

### KITCHEN_WORLD_V1
- cozy Japanese-inspired miniature environment
- warm wood / ceramic / paper / tiny stall / workbench
- hero object must read before decoration
- seasonal cues allowed
- never copy another creator's/branded product's exact package, styling, title, plot, or ending

## 5. Flow / Veo baseline

Canonical docs:
- `docs/23_minimum_credit_operator_architecture.md`
- `docs/26_flow_ui_mode_preflight.md`

Official Google Flow help rechecked **2026-08-27**:
- Veo 3.1 Lite 4s/6s/8s + Extend: non-Ultra 10 credits/generation
- First + Last frames: Lite supports 4s/6s/8s
- Ingredients/References can be 8s-only
- output count = 1
- 1080p upscale: 0 credits for Plus/Pro/Ultra
- actual Flow UI model/mode/output-count/displayed cost is the generation-time source of truth

Do not confuse standard new-video generation with an existing-video `Omni Flash` edit/modify screen.

## 6. Progressive Spend — mandatory credit-safety rule

```text
FREE keyframe/reference preflight
→ G1 only
→ QC
→ save actual last usable frame
→ G2 only after G1 PASS
→ QC
→ G3 only after G2 PASS
→ G4 only if immersive_h40 explicitly needs an independent world-resolution beat AND G3 PASSed
```

Never proactively generate G2/G3/G4.

Structural failures that stop downstream spend:
- POV
- scale
- anatomy
- premise/action feasibility

Reroll only structural failures. If motion is good and audio alone is bad, repair audio in edit instead of buying another generation.

### Latest validator hardening — 2026-08-27

Before this change, `tools/validate_current_standard.py` verified scene count, credits, frames, keyframes, actions and runtime, but **did not verify the manifest's own `progressive_spend_gate` or `sequential_chain` metadata**. A stale or hand-edited manifest could therefore say G2/G3/G4 did not require the previous PASS and still pass preparation.

Now production validation requires, when applicable:
- `g2_requires_g1_pass: true`
- `g3_requires_g2_pass: true`
- `g4_requires_g3_pass: true`
- `stop_if_pov_scale_anatomy_or_premise_fails: true`
- `reroll_only_structural_failure: true`
- G2/G3/G4 sequential-chain metadata must explicitly point to the previous scene's **actual last usable frame**

This makes the manifest, validator, generated operator pack and documented credit policy agree before any paid generation.

## 7. Sequential Frame Chain

Continuity must use real prior outputs:

```text
G1
↓ actual last usable frame
G2 First
↓ actual last usable frame
G3 First
↓ actual last usable frame
G4 First (immersive_h40 only)
```

Do **not** substitute the prettier planned target keyframe for the previous PASS scene's real final usable frame.

Continuity priority:
1. first-person camera position
2. paw fur/anatomy
3. hero-object size ratio
4. cookware/food state
5. workbench/lighting

The generated Flow Pack already translates symbolic tokens such as `ACTUAL_LAST_USABLE_FRAME_G1` into explicit operator instructions.

## 8. Runtime policy

### compact_h30
- exactly 3 first-pass Lite scenes
- current first-pass ceiling: 30 credits
- raw motion 24s
- final roughly 30–36s
- use when 3 distinct beats fully complete the tactile journey

### immersive_h40
- exactly 4 first-pass Lite scenes
- current first-pass ceiling: 40 credits
- raw motion 32s
- final roughly 38–46s
- G4 must add independent serving/world-resolution/afterglow value
- never buy G4 just to pad runtime

48–60s is not the default. Test longer runtimes only after real channel retention and engaged-views-per-credit evidence supports them.

## 9. Audio policy

Default:

```text
No narration
No generated music
Quiet room tone + close tiny tactile ASMR
```

Good sounds:
- tiny ceramic click
- soft wood scrape
- dough/crumb press
- subtle tiny sizzle
- paper rustle
- faint steam/room ambience

Use a short user-recorded Japanese line only when it materially improves comprehension, character voice, or payoff.

## 10. Deterministic production gates already built

Current safeguards include:
- source-of-truth work-start order
- HERO_CAT_V1 / KITCHEN_WORLD_V1 identity
- POV paw-only + tiny-scale hard gates
- Flow generation-vs-edit UI preflight
- manifest-aware H30/H40 runtime guidance
- exact scene-count / generation-count / credit-budget consistency
- 8s scene requirement for current production grammar
- keyframe map required
- planned `KF*` references must exist and have non-empty prompts
- each paid scene must have non-empty `action`
- each paid scene must have non-empty `action_guard`
- explicit `max_visual_cuts_per_8s_generation: 0` is preserved literally in generated prompts
- actual-last-frame First-frame mapping
- progressive-spend PASS dependencies validated in manifest
- sequential-chain metadata validated against actual-frame policy
- novelty/authenticity gate against repeated recent hook/conflict/ending fingerprints
- seasonal evidence saturation/no-churn gate
- local deterministic handoff update guard
- regression tests for major production invariants

## 11. Research / idea policy

Source files:
- `research/benchmark_log.csv`
- `research/seasonal_evidence.yaml`
- `ideas/episode_backlog.yaml`
- `ideas/novelty_signatures.yaml`
- `docs/27_research_evidence_saturation_gate.md`
- `docs/28_episode_novelty_authenticity_gate.md`

Score ideas on:
- benchmark evidence
- Japan relevance
- healing fit
- visual satisfaction
- Veo reliability
- originality
- worldbuilding
- audience demand
- expected credit efficiency

Never copy another creator's exact title, plot, branded product/package, or ending. Abstract only:
- hook mechanic
- scale contrast
- tactile action
- pacing
- visual payoff
- seasonal timing
- worldbuilding mechanic

### Evidence saturation

Do not keep committing another same-class seasonal PR/retail signal once a candidate is already sufficiently supported. A new research commit should normally change at least one of:
- score/rank
- NEXT_EPISODE
- publish timing
- evidence class
- production mechanic
- freshness after staleness
- official Flow assumption
- actual Tiny Cat Kitchen production/performance learning

## 12. Current candidate state

- `IDEA-009` yakiimo → already realized as TK-005 and blocked as a future repeat
- `IDEA-001` 8mm 月見だんご → priority future candidate
- `IDEA-010` 8mm 新米塩むすび → future candidate supported by current new-rice reservation/arrival behavior
- `IDEA-002` gummy → currently blocked against a recent equivalent conflict/ending structure

Fresh 2026-08-27 review does **not** justify another ranking/research-log change. New-rice arrivals are continuing, but this is the same already-recorded evidence class; autumn/yakiimo retail signals are saturated. Official Flow assumptions remain unchanged.

## 13. Current production state

`production/NEXT_EPISODE.txt` = **TK-005**

Title:

```text
猫の前足で作る、12mmの焼きいも。
```

Manifest: `episodes/TK-005.yaml`  
Runtime: `immersive_h40`  
Current first-pass ceiling: 4 Lite generations / 40 credits

Beats:
1. impossible-scale reveal — 12mm purple sweet potato beside paws
2. slow roast / skin crack
3. same tray slides away; residual heat widens the existing crack and reveals golden center
4. same tray slides into the miniature serving niche; paws withdraw; steam remains

Continuity/action rules:
- same roasting tray G1–G4
- no surprise new cookware
- no direct pinch/grab of the sweet potato
- G2 First = actual last usable frame from G1
- G3 First = actual last usable frame from G2
- G4 First = actual last usable frame from G3
- all planned KF references resolve before preparation
- G1–G4 each have explicit action + action_guard
- `max_visual_cuts_per_8s_generation: 0` remains literal in generated scene prompts
- progressive spend metadata currently declares all required PASS gates
- sequential-chain metadata currently declares G2/G3/G4 actual-frame sources correctly

The highest-value next real-world step remains: **generate TK-005 G1 only and QC it.** Automation must not spend that credit for the user.

## 14. Production learning available so far

`analytics/learning_ledger.csv` currently contains one real preflight failure:
- third-person/full-cat framing
- body visible
- scale too large
- human-like tool-use risk

Hard response:
- true first-person camera
- front paws only
- hero object <=0.50 paw width
- prefer nudge/press/slide over gripping

There is not yet enough real public 24h/72h performance data. Never treat placeholder zeroes as observations.

Metrics to record when available:
- actual Flow credits
- rerolls
- G1/G2/G3/G4 first-pass success
- usable motion seconds
- POV/scale/anatomy failures
- continuity issues
- failed action type
- narration/audio replacement
- final runtime
- 24h/72h Stayed to watch
- APV
- engaged views
- subscribers
- comments

## 15. Roadmap

### Phase A — TK-005 production truth
1. approve free opening/target frames
2. run local preparation/validation
3. generate G1 only
4. QC POV / scale / anatomy / camera / action / zero-cut behavior
5. on PASS, save actual last usable frame
6. continue G2 → G3 → justified G4 only through progressive gates
7. record actual credits/rerolls/usable seconds/failure type

### Phase B — first public Shorts learning
At 24h/72h record retention and engagement metrics plus production cost.

### Phase C — runtime learning
Compare compact_h30 vs immersive_h40 using APV, engaged views/credit, subscribers/100 credits and beat drop-off.

### Phase D — operator simplification
Keep reducing manual judgment so `다음 영상 준비해줘` remains sufficient. Only add tooling where actual Flow behavior or production evidence shows a real operator risk.

### Phase E — worldbuilding expansion
After performance evidence exists, expand tiny stalls, rainy shop, after-hours bakery, seasonal rituals and other worlds while keeping story fingerprints distinct.

## 16. Next priorities

1. TK-005 actual G1 production/QC data
2. verify zero-cut long-take behavior in real Flow output
3. verify actual-last-frame continuity in practice
4. record actual credits/rerolls/usable motion
5. obtain first public 24h/72h sample
6. only then re-weight runtime/action/idea priors

More same-class retail PR collection is not a priority.

## 17. Work-start order

Always inspect in this order:
1. latest main SHA
2. recent commits/PRs
3. `PROJECT_HANDOFF.md`
4. `START_HERE.md`
5. `CURRENT_STANDARD.md`
6. `docs/22_continuous_episode_learning_engine.md`
7. `docs/23_minimum_credit_operator_architecture.md`
8. `production/NEXT_EPISODE.txt`
9. current episode manifest
10. research/backlog/learning ledger

Newer merged repository state beats stale chat/automation wording.

## 18. Safety / invariants

- no automatic Flow credit spend
- no automatic paid generation
- no automatic YouTube publish
- no exact competitor copying
- no third-person/full-cat regression
- no human fingers/thumbs/tool grip regression
- no undefined/missing KF improvisation
- no blank paid-scene action/action_guard
- no next-scene spend before previous PASS
- no stale progressive-spend gate metadata
- no stale sequential-chain metadata
- no planned target frame substituted for previous actual PASS frame
- no scene-count/runtime/credit mismatch
- no padding G4
- no reroll of good motion for audio-only defect
- no placeholder analytics treated as real data
- do not modify Cali or unrelated repositories

## 19. Definition of Done

```text
current research
→ scored + novelty-safe candidate
→ POV/tiny-scale production-safe manifest
→ spend/runtime/keyframe/action/cut/progressive-chain validation PASS
→ free frame preflight
→ progressive Flow generation
→ actual-frame continuity chain
→ edit/export
→ upload
→ 24h/72h learning
→ next episode prior update
```

## 20. Change log

### 2026-08-27 — Progressive-spend manifest integrity gate
Baseline: `main@6cba79965b589b90f2879d8c8288b05619f2902b`.

Problem:
- manifest validator did not verify `progressive_spend_gate` or `sequential_chain` metadata
- a stale/hand-edited manifest could conflict with the documented no-downstream-spend policy and still pass local preparation

Changed:
- validate G2/G3/G4 previous-PASS requirements when those scenes exist
- require structural-failure stop gate
- require reroll-only-structural-failure gate
- validate G2/G3/G4 actual-last-frame sequential-chain metadata
- add regression coverage
- synchronize this handoff

Verified:
- TK-005 already declares the required gates and chain sources, so no episode/story/runtime/budget change is needed
- official Google Flow pricing/features remain unchanged on 2026-08-27
- fresh research does not justify candidate ranking/NEXT_EPISODE changes

Unchanged:
- NEXT_EPISODE = TK-005
- immersive_h40 / 40-credit first-pass ceiling
- no paid generation
- no YouTube publishing

### Earlier 2026-08-27 work
- explicit zero-cut Flow prompt preservation
- scene-action integrity gate
- keyframe-reference integrity gate
- manifest scene-count/runtime/credit consistency gate
- runtime-aware operator guidance
- explicit Flow First/Last frame mapping
- IDEA-010 new-rice onigiri candidate
- deterministic novelty/authenticity gate
