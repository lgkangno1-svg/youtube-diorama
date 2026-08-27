# Tiny Cat Kitchen — PROJECT HANDOFF

Last update: **2026-08-27 KST**  
Baseline inspected before this change: `main@3946255675fe15eef0bf4dbcef14c00f1693e433`

This is the durable handoff source of truth for `lgkangno1-svg/youtube-diorama`. Another AI/developer should be able to continue from GitHub without prior chat history. **Every material repository change must update this file in the same branch/PR.** True NO-OP research should not churn it.

## 1. Mission / development intent

Build a Japanese-target Shorts operating system, not merely an AI-cat generator. The system should absorb the repetitive work of current benchmark research, Japanese seasonal/cultural/food research, idea generation and scoring, originality checks, Veo-safe action design, Flow credit/runtime planning, deterministic prompts, continuity, edit/publish packs, and 24h/72h learning.

The normal user interface should remain:

```text
다음 영상 준비해줘
```

The system researches/selects the next novelty-safe episode, updates its manifest and `production/NEXT_EPISODE.txt`, and leaves local operator files ready for:

```powershell
./tools/make_next_short.ps1
```

Never spend Flow credits, generate paid video, or publish to YouTube without explicit user action.

## 2. Viewer-facing goal

Tiny Cat Kitchen Shorts should feel like the viewer **is the cat**, not like the viewer is watching a cat chef.

Core promise:

> True first-person cat POV, only front paws visible, handling food/objects so tiny that the paw-to-object scale contrast itself feels cute and healing.

Initial target market: Japan, especially teen/20s Shorts viewers, while keeping globally readable visual satisfaction and ASMR.

Long-term optimization targets:

```text
usable motion / credit
engaged views / credit
subscribers / 100 credits
```

## 3. Channel identity — do not regress

Canonical docs: `CURRENT_STANDARD.md`, `docs/24_hero_cat_brand_identity.md`, `docs/25_pov_paws_microworld_grammar.md`.

Default grammar: `POV_PAWS_MICROWORLD_V1`
- true first-person cat POV
- only cream + pale-ginger real feline front paws near lower edge
- no face/head/eyes/ears/body/tail/full cat
- hero food/object normally 5–20mm and visually <=0.50 paw width
- macro miniature diorama workbench
- mostly locked camera / subtle breathing drift only
- one calm tactile primary action + at most one micro-payoff per 8s generation
- preferred paw actions: nudge, press, pat, roll, steady, slide, tap
- avoid fingers/thumbs/human grip/chopsticks/tongs/knife handling
- no rapid montage / meme zoom / third-person chef framing

Structural FAIL even when pretty:
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
- never copy another creator's or branded product's exact package, styling, title, plot, or ending

## 5. Flow / Veo baseline

Canonical docs: `docs/23_minimum_credit_operator_architecture.md`, `docs/26_flow_ui_mode_preflight.md`.

Official Google Flow help rechecked **2026-08-27**:
- Veo 3.1 Lite 4s/6s/8s + Extend: non-Ultra 10 credits/generation
- First + Last frames: Lite supports 4s/6s/8s
- Ingredients/References can be 8s-only
- output count = 1
- 1080p upscale: 0 credits for Plus/Pro/Ultra
- actual Flow UI model/mode/output-count/displayed cost is the generation-time source of truth

Do not confuse standard new-video generation with an existing-video `Omni Flash` edit/modify screen.

## 6. Progressive Spend — mandatory

```text
FREE keyframe/reference preflight
→ G1 only
→ QC
→ save actual last usable frame
→ G2 only after G1 PASS
→ QC
→ G3 only after G2 PASS
→ G4 only if immersive_h40 needs an independent world-resolution beat AND G3 PASSed
```

Never proactively generate G2/G3/G4.

Structural failures that stop downstream spend:
- POV
- scale
- anatomy
- premise/action feasibility

Reroll only structural failures. If motion is good and audio alone is bad, repair audio in edit instead of buying another generation.

## 7. Sequential Frame Chain

Continuity uses real prior outputs:

```text
G1
↓ actual last usable frame
G2 First
↓ actual last usable frame
G3 First
↓ actual last usable frame
G4 First (immersive_h40 only)
```

Never substitute the prettier planned target keyframe for the previous PASS scene's real final usable frame.

Continuity priority:
1. first-person camera position
2. paw fur/anatomy
3. hero-object size ratio
4. cookware/food state
5. workbench/lighting

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

Use a short user-recorded Japanese line only when it materially improves comprehension, character voice, or payoff. If motion is good and generated audio is bad, replace audio in edit rather than rerolling the video.

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
- **bundle-level current-standard gate: `tools/build_episode_bundle.py` now validates the canonical episode manifest itself before creating any Flow/edit/publish pack, so direct Python or `make_short.ps1` use cannot bypass the same production safety checks that `make_next_short.ps1` already used**

## 11. Latest change — bundle-level validation closure

Problem found on current main `3946255675fe15eef0bf4dbcef14c00f1693e433`:
- `make_next_short.ps1` ran `validate_current_standard.py` before calling the bundle builder.
- `make_short.ps1` called `build_episode_bundle.py` directly.
- `build_episode_bundle.py` only ran originality validation.
- Therefore a direct `make_short.ps1` or direct `python tools/build_episode_bundle.py ...` invocation could bypass POV/scale/runtime/credit/keyframe/action/progressive-spend validation and still create plausible-looking operator packs.

Fix:
- bundle builder now requires the canonical `episodes/<episode_id>.yaml` repository manifest
- bundle builder runs `validate_current_standard.py <episode_id>` before originality validation
- generated output directory/files are created only after both validation gates pass
- copied/temp manifests cannot be used as a production-bundle bypass
- regression test checks canonical-path behavior and verifies current-standard validation occurs before originality and before generated output creation

Expected effect:
- one production safety path regardless of whether the operator enters through `make_next_short.ps1`, `make_short.ps1`, or direct Python bundle generation
- lower chance of spending credits from stale or hand-edited manifests
- no change to TK-005 story/runtime/budget

## 12. Research / idea policy

Source files: `research/benchmark_log.csv`, `research/seasonal_evidence.yaml`, `ideas/episode_backlog.yaml`, `ideas/novelty_signatures.yaml`, `docs/27_research_evidence_saturation_gate.md`, `docs/28_episode_novelty_authenticity_gate.md`.

Score ideas on benchmark evidence, Japan relevance, healing fit, visual satisfaction, Veo reliability, originality, worldbuilding, audience demand, and expected credit efficiency.

Never copy another creator's exact title, plot, branded product/package, or ending. Abstract only hook mechanic, scale contrast, tactile action, pacing, visual payoff, seasonal timing, and worldbuilding mechanic.

Evidence saturation rule: do not keep committing same-class seasonal PR/retail signals once a candidate is sufficiently supported. A new research commit should normally change score/rank, NEXT_EPISODE, publish timing, evidence class, production mechanic, freshness, Flow assumptions, or actual Tiny Cat Kitchen learning.

Current candidate state:
- `IDEA-009` yakiimo → already realized as TK-005 and blocked as a future repeat
- `IDEA-001` 8mm 月見だんご → priority future candidate
- `IDEA-010` 8mm 新米塩むすび → future candidate supported by current new-rice reservation/arrival behavior
- `IDEA-002` gummy → currently blocked against a recent equivalent conflict/ending structure

Fresh 2026-08-27 review does **not** justify another ranking/research-log change. Autumn/yakiimo signals remain saturated and official Flow assumptions are unchanged.

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
3. same tray slides away; residual heat widens existing crack and reveals golden center
4. same tray slides into miniature serving niche; paws withdraw; steam remains

Continuity/action rules:
- same roasting tray G1–G4
- no surprise new cookware
- no direct pinch/grab of sweet potato
- G2 First = actual last usable frame from G1
- G3 First = actual last usable frame from G2
- G4 First = actual last usable frame from G3
- all planned KF references resolve before preparation
- G1–G4 each have explicit action + action_guard
- zero-cut constraint remains literal in generated prompts
- progressive-spend metadata declares all required PASS gates
- sequential-chain metadata declares correct actual-frame sources

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
At 24h/72h record retention/engagement metrics plus production cost.

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
- no bundle creation from a noncanonical copied/temp manifest
- no bundle creation before current-standard validation passes
- no padding G4
- no reroll of good motion for audio-only defect
- no placeholder analytics treated as real data
- do not modify Cali or unrelated repositories

## 19. Definition of Done

```text
current research
→ scored + novelty-safe candidate
→ POV/tiny-scale production-safe manifest
→ current-standard + originality validation PASS
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

### 2026-08-27 — Bundle-level current-standard validation gate
Baseline: `main@3946255675fe15eef0bf4dbcef14c00f1693e433`.

Changed:
- production bundle generation now requires canonical repository manifest
- current-standard validator runs inside `build_episode_bundle.py`
- originality validation remains required after current-standard validation
- generated files/directories are created only after validation passes
- regression coverage verifies gate order and canonical-path behavior
- synchronized this handoff

Verified assumptions:
- TK-005 remains compatible with current validator and production policy
- official Flow pricing/features remain unchanged on 2026-08-27
- no research evidence class/ranking/NEXT_EPISODE change justified

Unchanged:
- NEXT_EPISODE = TK-005
- TK-005 story/runtime/40-credit first-pass ceiling
- candidate ranking
- no Flow credits spent, no paid generation, no publishing

### Earlier 2026-08-27 work
- progressive-spend manifest integrity gate
- sequential-chain metadata validation
- explicit zero-cut Flow prompt preservation
- scene-action integrity gate
- keyframe-reference integrity gate
- manifest spend consistency fail-closed gate
- runtime-aware operator guidance
- explicit Flow First/Last frame mapping
- IDEA-010 new-rice onigiri candidate
- deterministic novelty/authenticity gate
