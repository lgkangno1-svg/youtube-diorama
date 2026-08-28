# Tiny Cat Kitchen — PROJECT HANDOFF

Last update: **2026-08-28 KST**  
Baseline inspected before this iteration: `main@904a045f9f3cd5b084af6492fa6e71141231be84`

This is the durable handoff source of truth for `lgkangno1-svg/youtube-diorama`. Another AI/developer must be able to continue from GitHub without prior chat history. Every material repository change must update this file in the same branch/PR. True NO-OP research must not churn it.

## Development execution policy

`AGENTS.md` is authoritative.

- repository development is performed directly by the active Chat/Codex session
- inspect latest main SHA + recent commits/PRs before every run
- latest merged repository state overrides stale chat or scheduled-prompt details
- modify only `lgkangno1-svg/youtube-diorama`; do not touch Cali or unrelated repositories
- do not spend Flow credits, generate paid video, or publish to YouTube without explicit user action

## Mission

Build a Japanese-target Shorts operating system around a simple user interface:

```text
다음 영상 준비해줘
```

The system should research current Japanese/global AI-cat, miniature cooking, ASMR, relaxing-food and adjacent signals, choose a novelty-safe episode, prepare the manifest and `production/NEXT_EPISODE.txt`, generate deterministic local operator packs, minimize paid-generation failures, and learn from actual Flow production plus 24h/72h YouTube results.

User local entrypoint:

```powershell
./tools/make_next_short.ps1
```

## Viewer-facing identity

Default grammar: `POV_PAWS_MICROWORLD_V1`.

- true first-person cat POV
- only cream + pale-ginger feline front paws near lower edge
- no face/head/body/full-cat reveal
- hero object normally 5–20mm and <=0.50 of one visible paw width
- macro miniature diorama workbench
- mostly locked camera
- one calm tactile primary action + at most one passive micro-payoff per 8s generation
- preferred paw actions: nudge, press, pat, roll, steady, slide, tap
- no human fingers/thumbs/human-like gripping
- no rapid montage / no third-person chef framing

Core appeal: the viewer feels like the cat handling an impossibly tiny world. Scale contrast + tactile calm matter more than showing a cat face.

Canonical identity docs:
- `CURRENT_STANDARD.md`
- `docs/24_hero_cat_brand_identity.md`
- `docs/25_pov_paws_microworld_grammar.md`

## Current Flow / Veo baseline

Official Google Flow Help rechecked **2026-08-28**:
- Google AI Pro: 1,000 Flow credits/month
- Veo 3.1 Lite 4s/6s/8s + Extend: non-Ultra 10 credits/generation
- First + Last frames: Lite supports 4s/6s/8s
- output count = 1
- 1080p upscale = 0 credits for Plus/Pro/Ultra
- actual Flow UI active model/mode/output count/displayed cost is the generation-time source of truth

Do not confuse an existing-video edit / Omni Flash edit screen with standard new-video generation.

## Gate A — planned keyframe continuity

Mandatory before any paid G1:

```text
verify image model + displayed cost in Flow
→ use no-charge image path only when UI confirms it
→ create KF0 master visual anchor
→ QC POV / paws / scale / camera / fixed props / lighting
→ derive KF1 from approved KF0 via edit/refine or reference/ingredient
→ derive KF2 from approved KF1
→ continue sequentially through all manifest-required KFs
→ all planned KFs PASS
→ only then generate G1
```

KF1+ must not become independent fresh text-to-image lottery tickets when a previous approved KF can anchor continuity.

Planned keyframe order is numeric `KF0`, `KF1`, `KF2` ... rather than YAML mapping insertion order. Both validator and Flow Pack follow that numeric sequence.

Important distinction:
- planned KF = destination / target state
- actual saved video frame = next-scene continuity bridge

## Progressive Spend / actual-frame chain

```text
planned KF chain PASS
→ G1 only
→ QC
→ Flow native Save frame from actual last usable frame
→ G2 only after G1 PASS
→ QC + Save frame
→ G3 only after G2 PASS
→ G4 only if immersive_h40 explicitly needs independent world-resolution value and G3 PASSed
```

Never substitute a prettier planned target KF for the actual previous PASS frame.

## Runtime policy

`compact_h30` / `immersive_h40` numbers refer to the **current 30/40-credit first-pass ceilings**, not promised final seconds.

### compact_h30
- exactly 3 × 8s Lite scenes = raw motion 24s
- current first-pass ceiling = 30 credits
- default final target ≈ 24–27s
- use when three independent beats complete scale reveal → making → payoff

### immersive_h40
- exactly 4 × 8s Lite scenes = raw motion 32s
- current first-pass ceiling = 40 credits
- default final target ≈ 32–35s
- G4 must add independent serving/world-resolution/afterglow value

Runtime invariants:
- natural slowdown only inside `post_production.preferred_playback_speed_range`
- playback-speed range must be exactly `[min,max]`, numeric, `0 < min <= max <= 1.0`
- malformed/reversed/>1.0 speed ranges fail closed before paid generation
- static/keyframe holds count only when explicitly declared in `editorial_seconds`
- `max_total_static_hold_seconds` is a ceiling, not an automatic padding budget
- if generated motion + allowed slowdown + explicit holds cannot reach requested minimum, validation fails
- accept a shorter natural Short rather than inventing runtime padding

`tools/validate_current_standard.py` enforces runtime feasibility and playback-speed range integrity. `tools/build_healing_edit_plan.py` does not fabricate default hero/loop holds when the manifest did not request them.

## 8-second scene grammar

Default:

```text
1 calm tactile primary action
+ optional 1 passive micro-payoff
```

Production manifests must explicitly declare:
- `max_visual_cuts_per_8s_generation: 0` or `1`
- `preferred_action_count_per_generation: 1`

Normal Tiny Cat Kitchen style is 0-cut long take.

## Audio policy

Default:

```text
No narration
No generated music
Quiet room tone + close tiny tactile ASMR
```

If motion is good and audio alone is bad, replace audio in edit rather than rerolling video.

## Deterministic safeguards already built

- latest-main / recent-PR / handoff-first work-start order
- POV paw-only + tiny-scale hard gates
- Flow generation-vs-edit UI preflight
- planned KF0→KFn continuity chain
- numeric KF0..KFn semantics independent of YAML mapping order
- generated Flow Pack follows numeric KF order
- manifest-aware H30/H40 credit-tier guidance
- scene-count/generation-count/credit-budget consistency validation
- keyframe map/reference integrity
- non-empty action/action_guard for every paid scene
- explicit zero-cut prompt preservation
- actual-last-frame First-frame mapping
- Flow native Save-frame bridge instructions
- progressive-spend PASS dependency validation
- sequential-chain metadata validation
- novelty/authenticity gate against repeated recent fingerprints
- seasonal evidence saturation/no-churn gate
- long-take manifest guard: 0/1 cut max and exactly one preferred primary action
- runtime-feasibility no-padding gate
- edit-plan explicit-holds-only rule
- full playback-speed-range integrity gate
- **strict integer scalar gate for paid-generation control fields**
- local handoff-update guard
- regression tests for core production invariants

## Latest material change — strict integer manifest scalars

Problem found after PR #45:
- several production-critical fields still passed through Python `int(...)` coercion
- `True` becomes integer `1`
- `1.5` truncates to integer `1`
- `3.5` truncates to integer `3`
- `8.0` becomes integer `8`
- therefore malformed YAML could silently pass controls such as output count, preferred action count, generation count, credit budget or generation duration

This is especially dangerous because those fields control paid-generation behavior and runtime/credit arithmetic.

Fix in branch `fix/strict-integer-manifest-scalars`:
- add `strict_manifest_int()` accepting only actual integer scalars
- reject booleans, floats and numeric strings instead of coercing them
- apply strict integer semantics to:
  - `flow_strategy.output_count`
  - `flow_strategy.max_visual_cuts_per_8s_generation`
  - `flow_strategy.preferred_action_count_per_generation`
  - `flow_strategy.max_lite_generations_first_pass`
  - `flow_strategy.non_ultra_credit_budget_first_pass`
  - `runtime_strategy.minimum_distinct_motion_beats` for immersive H40
  - every scene `generation_seconds`
- add regression coverage for boolean/fractional/float cases that previously could coerce into valid-looking values

TK-005 already uses real YAML integers for all these fields, so its production state does not change.

## Research / idea policy

Sources:
- `research/benchmark_log.csv`
- `research/seasonal_evidence.yaml`
- `ideas/episode_backlog.yaml`
- `ideas/novelty_signatures.yaml`
- `docs/27_research_evidence_saturation_gate.md`
- `docs/28_episode_novelty_authenticity_gate.md`

Never copy exact competitor title, plot, branded product/package or ending. Extract only abstract mechanisms: hook, scale contrast, tactile action, pacing, payoff, seasonal timing, worldbuilding.

Evidence saturation rule: do not keep committing same-class seasonal retail/PR signals after a candidate is already well supported unless the new evidence changes ranking, NEXT_EPISODE, timing, evidence class, production mechanics, freshness, Flow assumptions or real Tiny Cat Kitchen learning.

2026-08-28 research check:
- official Flow pricing/features remain unchanged for the current Lite workflow
- current Japanese 月見 activation remains strong: additional 2026-08-26 traditional moon-dumpling announcements and a 2026-09-02 nationwide cafe moon/yakiimo campaign reinforce recognition
- these are same-class seasonal activation signals already represented by existing saturated 月見/yakiimo evidence, so they do **not** justify new benchmark rows, candidate-score changes, ranking changes or NEXT_EPISODE changes
- current AI-cat/miniature/ASMR discovery still supports calm food/worldbuilding mechanics but does not provide stronger causal evidence than the existing benchmark memory

Current candidate state:
- `IDEA-009` yakiimo → realized as TK-005; blocked as future repeat
- `IDEA-001` 8mm 月見だんご → priority future candidate
- `IDEA-010` 8mm 新米塩むすび → priority future candidate backed by current reservation/arrival behavior
- `IDEA-002` gummy → blocked against recent equivalent conflict/ending structure

## Current production state

`production/NEXT_EPISODE.txt` = **TK-005**

Title:

```text
猫の前足で作る、12mmの焼きいも。
```

Manifest: `episodes/TK-005.yaml`  
Runtime mode: `immersive_h40`  
First-pass ceiling: 4 Lite generations / current 40 credits  
Final target: **32–35s**, nominal `length_target_seconds: 34`

Planned KFs:
1. `KF0_OPEN`
2. `KF1_WARM`
3. `KF2_CRACK`
4. `KF3_OPEN`
5. `KF4_SERVE`

Paid scene destinations:
- G1: `KF0_OPEN → KF1_WARM`
- G2: actual saved G1 frame → `KF2_CRACK`
- G3: actual saved G2 frame → `KF3_OPEN`
- G4: actual saved G3 frame → `KF4_SERVE`

Beats:
1. impossible-scale reveal — 12mm purple sweet potato beside paws
2. slow roast / skin crack
3. same tray slides away; residual warmth widens crack and reveals golden center
4. same tray slides into already-visible serving niche; paws withdraw; steam remains

Continuity/action rules:
- same roasting tray G1–G4
- same fixed tabletop warmer KF0–KF4
- same serving niche KF0–KF4
- no surprise new cookware/structure
- no direct pinch/grab
- KF1→KF4 = sequential edit/reference derivations from previous approved planned KF
- G2/G3/G4 First = actual saved frame from previous PASS clip
- explicit action + action_guard in every G scene
- `output_count: 1` is a true integer
- `max_lite_generations_first_pass: 4` is a true integer
- `non_ultra_credit_budget_first_pass: 40` is a true integer
- `max_visual_cuts_per_8s_generation: 0` is a true integer
- `preferred_action_count_per_generation: 1` is a true integer
- every `generation_seconds: 8` is a true integer
- `minimum_distinct_motion_beats: 4` is a true integer
- `preferred_playback_speed_range: [0.92, 1.00]` remains valid
- no invented editorial holds merely to push runtime toward 40s

Highest-value next real-world step remains **approve TK-005 KF0→KF4 in real Flow, then generate G1 only and QC it.** Automation must not spend that credit.

## Production learning available

`analytics/learning_ledger.csv` currently has one real preflight failure:
- third-person/full-cat framing
- body visible
- scale too large
- human-like tool-use risk

Hard response:
- true first-person camera
- front paws only
- hero object <=0.50 paw width
- prefer nudge/press/slide over gripping

No trustworthy public 24h/72h sample exists yet. Never treat placeholder zeroes as observations.

Long-term KPIs:

```text
usable motion / credit
engaged views / credit
subscribers / 100 credits
```

## Roadmap

### Phase A — TK-005 production truth
1. run local preparation/validation
2. create/approve KF0 master anchor using UI-confirmed no-charge image path
3. derive/approve KF1→KF4 through sequential edit/reference chaining
4. generate G1 only
5. QC POV / scale / anatomy / camera / action / cut count / fixed-prop continuity
6. on PASS, native Save frame
7. continue G2 → G3 → justified G4 through progressive gates
8. edit to the best natural runtime
9. record actual credits, rerolls, usable seconds, failure type

### Phase B — first public Shorts learning
At 24h/72h record Stayed to watch, APV, engaged views, subscribers, comments, final runtime, credits, rerolls.

### Phase C — runtime learning
Compare compact_h30 vs immersive_h40 using actual final runtime, APV, engaged views/credit, subscribers/100 credits, and beat drop-off. Do not infer runtime from the H30/H40 label.

### Phase D — operator simplification
Keep `다음 영상 준비해줘` sufficient; reduce manual judgment only when real Flow behavior supports it.

### Phase E — worldbuilding expansion
Expand distinct worlds only after performance evidence, without repeating recent story fingerprints.

## Next priorities

1. real Flow TK-005 KF0→KF4 continuity validation
2. actual G1 production/QC
3. verify real 0-cut long-take behavior
4. actual saved-frame continuity
5. actual credits/rerolls/usable motion
6. first public 24h/72h sample
7. learn whether 24–27s vs 32–35s beats fit this channel better before adding longer generation strategies

## Work-start order

1. latest main SHA
2. recent commits/PRs
3. `AGENTS.md`
4. `PROJECT_HANDOFF.md`
5. `START_HERE.md`
6. `CURRENT_STANDARD.md`
7. `docs/22_continuous_episode_learning_engine.md`
8. `docs/23_minimum_credit_operator_architecture.md`
9. `production/NEXT_EPISODE.txt`
10. current episode manifest
11. research/backlog/learning ledger

## Safety / invariants

- no automatic Flow credit spend
- no automatic paid generation
- no automatic YouTube publish
- no exact competitor copying
- no third-person/full-cat regression
- no paid G1 before full planned KF chain PASS
- no independent fresh KF1+ when a previous approved planned KF can anchor it
- no planned KF substituted for previous actual PASS frame
- no undefined/malformed/duplicate/non-contiguous KF sequence
- no YAML mapping order changing planned KF semantics
- no blank action/action_guard
- no missing cut ceiling
- no >1 visual cut per 8s production scene plan
- no preferred action count other than integer 1
- no boolean/float/string coercion for paid-generation integer controls
- no next-scene spend after previous-scene failure
- no scene-count/runtime/credit mismatch
- no padding G4
- no impossible final-runtime target that requires undeclared padding
- no malformed/reversed/>1.0 playback-speed range
- no invented still/loop hold merely to satisfy H30/H40 naming
- no reroll of good motion for audio-only defects
- no placeholder analytics treated as real observations
- do not modify Cali or unrelated repositories

## Definition of Done

```text
current research
→ scored + novelty-safe candidate
→ production-safe + runtime-feasible manifest
→ deterministic validation PASS
→ planned KF continuity PASS
→ progressive paid generation
→ actual-frame continuity chain
→ natural edit/export without padding
→ upload
→ 24h/72h learning
→ next prior update
```

Success is measured by first-pass success, usable motion/credit, engaged views/credit, subscribers/credit, fewer continuity/camera/reroll failures, less operator judgment and fewer repeated story fingerprints — not by commit count or artificially long runtime.

## Change log

### 2026-08-28 — Strict integer manifest scalar integrity
Baseline `main@904a045f9f3cd5b084af6492fa6e71141231be84`.

Changed:
- close validator coercion gap where bools/floats/numeric strings could masquerade as integer production controls
- add `strict_manifest_int()`
- enforce exact integer scalar semantics for output count, cut ceiling, action count, first-pass generation count, credit budget, immersive-H40 motion-beat count and scene generation duration
- add regression coverage for `True`, `0.0`, `1.5`, `3.5`, `30.0`, `8.0`
- synchronize this handoff in the same branch

Verified assumptions:
- TK-005 uses correct integer scalars and remains unchanged
- official Google Flow credit baseline remains Pro 1,000/month and Veo 3.1 Lite 10 credits/generation for non-Ultra
- newly surfaced 月見/yakiimo signals are same-class saturated evidence and do not change ranking/NEXT_EPISODE
- no Flow credits spent, no paid generation, no publishing

### Earlier 2026-08-28 work
- playback-speed-range integrity
- runtime feasibility / no-padding correction
- Flow Pack numeric KF-order alignment
- operator Gate A sequential-KF synchronization
- long-take manifest drift guard
- numeric planned-keyframe sequence gate
- planned-keyframe scene-order gate
- planned keyframe continuity chain
- Flow native Save-frame chain guidance
