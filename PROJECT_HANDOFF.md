# Tiny Cat Kitchen — PROJECT HANDOFF

Last update: **2026-08-27 KST**  
Latest baseline inspected before this change: `main@eff1366b1de91b414c9440e048502a9942408373`

This is the durable handoff source of truth for `lgkangno1-svg/youtube-diorama`. Another AI/developer must be able to continue from GitHub without prior chat history. **Every material repository change must update this file in the same branch/PR.** True NO-OP research should not churn it.

## 1. Mission

Build a Japanese-target Shorts operating system, not merely an AI-cat video generator.

The normal user interface should remain:

```text
다음 영상 준비해줘
```

The system should handle current benchmark research, Japanese seasonal/cultural/food signals, idea scoring, originality checks, Veo-safe action design, Flow runtime/credit planning, deterministic prompt packs, continuity, edit/publish packs, and 24h/72h learning.

The user's local operator entrypoint is:

```powershell
./tools/make_next_short.ps1
```

Never spend Flow credits, generate paid video, or publish to YouTube without explicit user action.

## 2. Viewer-facing goal

Tiny Cat Kitchen should feel like the viewer **is the cat**.

Core promise:

> True first-person cat POV, only front paws visible, handling an absurdly tiny miniature food/object so the paw-to-object scale contrast itself feels cute, tactile, and healing.

Initial target: Japanese teen/20s Shorts viewers, while keeping the visual payoff globally readable.

Long-term KPIs:

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
- cream + pale-ginger real feline front paws only near lower edge
- no face/head/eyes/ears/body/tail/full-cat reveal
- hero food/object normally 5–20mm and visually <=0.50 of one paw width
- macro miniature diorama workbench
- mostly locked camera / subtle breathing drift only
- one calm tactile primary action + at most one micro-payoff per 8s generation
- preferred paw actions: nudge, press, pat, roll, steady, slide, tap
- no human fingers/thumbs/human-like grip
- no chopsticks/tongs/knife manipulation like human hands
- no rapid montage / meme zoom / third-person chef shot

Structural FAIL even when visually attractive:
- full cat or face visible
- cat cooking from across a counter
- hero object comparable to paw size
- human fingers/thumbs
- tool gripping like a person
- wide establishing shot that weakens tiny-scale contrast

## 4. Hero cat / world

### HERO_CAT_V1
- cream fur base
- pale ginger markings
- real feline paw anatomy
- premium/healing tone
- face may exist in branding assets, but default Shorts use paws only

### KITCHEN_WORLD_V1
- cozy Japanese-inspired miniature environment
- warm wood / ceramic / paper / tiny stall / workbench
- hero object must read before decoration
- seasonal cues allowed
- never copy another creator's exact title, plot, branded product/package, visual design, or ending

## 5. Flow / Veo baseline

Canonical docs:
- `docs/23_minimum_credit_operator_architecture.md`
- `docs/26_flow_ui_mode_preflight.md`

Official Google Flow help rechecked **2026-08-27**:
- Veo 3.1 Lite: 4s/6s/8s + Extend
- non-Ultra: 10 credits per generation
- First + Last frames: Lite supports 4s/6s/8s
- Ingredients/References may be 8s-only
- output count = 1
- 1080p upscale = 0 credits for Plus/Pro/Ultra
- actual Flow UI model/mode/output-count/displayed cost is final generation-time truth

Do not confuse standard new-video generation with an existing-video edit / Omni Flash modify screen.

## 6. Progressive Spend — mandatory

```text
FREE keyframe/reference preflight
→ G1 only
→ QC
→ save actual last usable frame
→ G2 only after G1 PASS
→ QC
→ G3 only after G2 PASS
→ G4 only when immersive_h40 explicitly needs an independent world-resolution beat AND G3 PASSed
```

Never proactively generate later scenes.

Structural downstream stop conditions:
- POV failure
- scale failure
- anatomy failure
- premise/action infeasibility

If motion is good and audio alone is bad, repair audio in edit instead of buying another generation.

## 7. Sequential Frame Chain

Use real prior outputs:

```text
G1
↓ actual last usable frame
G2 First
↓ actual last usable frame
G3 First
↓ actual last usable frame
G4 First (immersive_h40 only)
```

Never substitute a prettier planned target keyframe for the real previous PASS frame.

Continuity priority:
1. camera position
2. paw fur/anatomy
3. hero-object size ratio
4. cookware/food state
5. workbench/lighting

## 8. Runtime policy

### compact_h30
- exactly 3 first-pass Lite scenes
- current first-pass ceiling 30 credits
- raw motion 24s
- final roughly 30–36s
- use when 3 distinct beats fully complete the tactile journey

### immersive_h40
- exactly 4 first-pass Lite scenes
- current first-pass ceiling 40 credits
- raw motion 32s
- final roughly 38–46s
- G4 must add independent serving/world-resolution/afterglow value
- never buy G4 to pad runtime

48–60s is not default. Test longer runtime only after real retention and engaged-views-per-credit evidence supports it.

## 9. Audio policy

Default:

```text
No narration
No generated music
Quiet room tone + close tiny tactile ASMR
```

Use a short user-recorded Japanese line only when it materially improves comprehension, character voice, or payoff.

## 10. Deterministic production gates already built

Current safeguards include:
- source-of-truth work-start order
- HERO_CAT_V1 / KITCHEN_WORLD_V1 identity
- POV paw-only + tiny-scale hard gates
- Flow new-generation vs edit-mode preflight
- manifest-aware H30/H40 guidance
- exact scene-count / generation-count / credit-budget validation
- 8s production-scene requirement for current grammar
- required keyframe map
- planned `KF*` references must exist and be non-empty
- every paid scene requires non-empty `action`
- every paid scene requires non-empty `action_guard`
- explicit `max_visual_cuts_per_8s_generation: 0` remains literal in generated prompts
- actual-last-frame First-frame mapping
- progressive-spend PASS dependencies validated in manifest
- sequential-chain metadata validated against actual-frame policy
- novelty/authenticity gate against repeated recent hook/conflict/ending fingerprints
- seasonal evidence saturation/no-churn gate
- local deterministic handoff update guard
- regression tests for core production invariants
- bundle-level current-standard validation so `make_short.ps1` or direct bundle generation cannot bypass canonical production checks

## 11. Latest material change — TK-005 G1 prop continuity

A semantic continuity risk was found immediately before paid G1 production.

Before this fix:
- `KF0_OPEN` showed paws + the tiny sweet potato + roasting tray, but did **not** explicitly include the heat source.
- `KF1_WARM` introduced the heat source.
- G1 action said the tray moves toward that heat source.

Risk:
- First+Last generation could invent the missing heat source mid-shot, move it, duplicate it, or rearrange the workbench.
- That would consume the first paid generation on avoidable prop invention and weaken continuity before any channel performance data exists.

Fix in `episodes/TK-005.yaml`:
- opening frame now explicitly contains the same miniature tabletop warmer already fixed in place
- warm target frame refers to that **same already-present** warmer
- G1 action moves only the tray toward it
- G1 guard explicitly forbids creating the warmer mid-shot

This does not change the story, runtime, scene count, title, target market, or credit ceiling. It only removes avoidable G1 prop invention.

## 12. Research / idea policy

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

Never copy exact competitor titles, plots, branded products/packages, or endings. Extract only abstract mechanisms: hook, scale contrast, tactile action, pacing, visual payoff, seasonal timing, and worldbuilding.

Evidence saturation rule: do not keep committing same-class seasonal retail/PR signals after a candidate is already sufficiently supported. A new research change should normally alter score/rank, NEXT_EPISODE, publish timing, evidence class, production mechanic, freshness, Flow assumptions, or actual Tiny Cat Kitchen learning.

Current candidate state:
- `IDEA-009` yakiimo → realized as TK-005; blocked as future repeat
- `IDEA-001` 8mm 月見だんご → priority future candidate
- `IDEA-010` 8mm 新米塩むすび → future candidate supported by current rice reservation/arrival behavior
- `IDEA-002` gummy → currently blocked against a recent equivalent conflict/ending structure

Fresh 2026-08-27 review did not justify a new ranking/research-log change. Autumn/yakiimo signals remain saturated and official Flow assumptions remain unchanged.

## 13. Current production state

`production/NEXT_EPISODE.txt` = **TK-005**

Title:

```text
猫の前足で作る、12mmの焼きいも。
```

Manifest: `episodes/TK-005.yaml`  
Runtime: `immersive_h40`  
First-pass ceiling: 4 Lite generations / 40 credits

Beats:
1. impossible-scale reveal — 12mm purple sweet potato beside paws
2. slow roast / skin crack
3. same tray slides away; residual warmth widens the existing crack and reveals golden center
4. same tray slides into miniature serving niche; paws withdraw; steam remains

Continuity/action rules:
- same roasting tray G1–G4
- same miniature tabletop warmer is present from KF0 onward rather than appearing during G1
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

Highest-value next real-world step remains: **generate TK-005 G1 only and QC it.** Automation must not spend that credit for the user.

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

There is not yet enough public 24h/72h performance data. Never treat placeholder zeroes as observations.

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
4. QC POV / scale / anatomy / camera / action / zero-cut behavior / prop continuity
5. on PASS, save actual last usable frame
6. continue G2 → G3 → justified G4 only through progressive gates
7. record credits/rerolls/usable seconds/failure type

### Phase B — first public Shorts learning
At 24h/72h record retention/engagement plus production cost.

### Phase C — runtime learning
Compare compact_h30 vs immersive_h40 on APV, engaged views/credit, subscribers/100 credits, and beat drop-off.

### Phase D — operator simplification
Keep reducing manual judgment so `다음 영상 준비해줘` remains sufficient. Add tooling only when actual Flow behavior or production evidence reveals a real risk.

### Phase E — worldbuilding expansion
After performance evidence exists, expand tiny stalls, rainy shops, after-hours bakery, seasonal rituals, and other distinct worlds without repeating story fingerprints.

## 16. Next priorities

1. TK-005 actual G1 production/QC data
2. confirm same warmer/tray/paw/camera layout survives G1
3. verify zero-cut long-take behavior in real Flow output
4. verify actual-last-frame continuity in practice
5. record actual credits/rerolls/usable motion
6. obtain first public 24h/72h sample
7. only then re-weight runtime/action/idea priors

More same-class retail PR collection is not a priority.

## 17. Work-start order

Always inspect:
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

Newer merged repository state overrides stale chat or automation wording.

## 18. Safety / invariants

- no automatic Flow credit spend
- no automatic paid generation
- no automatic YouTube publish
- no exact competitor copying
- no third-person/full-cat regression
- no human fingers/thumbs/tool-grip regression
- no undefined/missing KF improvisation
- no blank paid-scene action/action_guard
- no next-scene spend before previous PASS
- no stale progressive-spend metadata
- no stale sequential-chain metadata
- no planned target frame substituted for previous actual PASS frame
- no scene-count/runtime/credit mismatch
- no new major static prop appearing mid-generation when it can be present in the planned First frame
- no bundle creation from noncanonical copied/temp manifest
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

Success is measured by first-pass success, usable motion/credit, engaged views/credit, subscribers/credit, fewer camera/continuity rerolls, and less operator judgment — not by commit count.

## 20. Change log

### 2026-08-27 — TK-005 G1 static-prop continuity fix
Baseline: `main@eff1366b1de91b414c9440e048502a9942408373`.

Changed:
- found that G1 start frame omitted the heat source that existed in G1 target frame/action
- added the same fixed miniature tabletop warmer to `KF0_OPEN`
- made `KF1_WARM` explicitly preserve that same warmer
- changed G1 action/guard so only the tray moves; the warmer must not be invented mid-shot
- synchronized this handoff

Verified assumptions:
- official Flow pricing/features remain unchanged on 2026-08-27
- research evidence did not justify ranking/NEXT_EPISODE changes

Unchanged:
- NEXT_EPISODE = TK-005
- immersive_h40
- 4 Lite generations / 40-credit first-pass ceiling
- no Flow credits spent, no paid generation, no publishing

### Earlier 2026-08-27 work
- bundle-level current-standard validation closure
- progressive-spend/sequential-chain manifest validation
- explicit zero-cut prompt preservation
- scene-action integrity gate
- keyframe-reference integrity gate
- runtime-aware operator guidance
- explicit First/Last actual-frame mapping
- new-rice onigiri future candidate
- deterministic novelty/authenticity gate
