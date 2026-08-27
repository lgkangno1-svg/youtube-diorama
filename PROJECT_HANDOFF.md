# Tiny Cat Kitchen — PROJECT HANDOFF

Last update: **2026-08-27 KST**  
Baseline inspected before this change: `main@4c61aeb32dcde224730ec18f424923392735bfbf`

This is the durable handoff source of truth for `lgkangno1-svg/youtube-diorama`. Another AI/developer should be able to continue from the repository without prior chat history. Every material repository change must update this file in the same branch/PR. True NO-OP research should not churn it.

## Mission

Build a Japanese-target Shorts operating system, not merely an AI-cat generator. The normal user interface should remain:

```text
다음 영상 준비해줘
```

The system researches current Japanese/global signals, chooses a novelty-safe episode, prepares the manifest and `production/NEXT_EPISODE.txt`, generates deterministic local operator packs, and learns from production plus 24h/72h YouTube results. The user runs:

```powershell
./tools/make_next_short.ps1
```

Never spend Flow credits, generate paid video, or publish to YouTube without explicit user action.

## Channel identity

Canonical docs: `CURRENT_STANDARD.md`, `docs/24_hero_cat_brand_identity.md`, `docs/25_pov_paws_microworld_grammar.md`.

Default visual grammar is `POV_PAWS_MICROWORLD_V1`:
- true first-person cat POV
- only cream + pale-ginger front paws visible near the lower edge
- no cat face/head/body/full-cat reveal
- hero food/object normally 5–20mm and <=0.50 of one visible paw width
- macro miniature diorama workbench
- mostly locked camera
- one calm tactile primary action + at most one micro-payoff per 8s generation
- preferred paw actions: nudge, press, pat, roll, steady, slide, tap
- avoid human-like gripping/tool manipulation
- no rapid montage or third-person chef framing

The core appeal is not showing a cute cat face. It is making the viewer feel like the cat while handling an impossibly tiny world.

## Flow / Veo baseline

Canonical docs: `docs/23_minimum_credit_operator_architecture.md`, `docs/26_flow_ui_mode_preflight.md`.

Official Google Flow help rechecked **2026-08-27**:
- Veo 3.1 Lite 4s/6s/8s + Extend: non-Ultra 10 credits/generation
- First + Last frames: Lite supports 4s/6s/8s
- output count = 1
- 1080p upscaling: 0 credits for Plus/Pro/Ultra
- Ingredients/References can be 8s-only
- actual Flow UI model/mode/output-count/displayed cost is the generation-time source of truth

Do not confuse an existing-video edit / Omni Flash edit screen with standard new-video generation.

Progressive Spend:

```text
FREE keyframe/reference preflight
→ G1 only
→ QC
→ save actual last usable frame
→ G2 only after G1 PASS
→ QC
→ G3 only after G2 PASS
→ G4 only when immersive_h40 explicitly needs an independent world-resolution beat and G3 PASSed
```

Sequential continuity uses the real previous PASS frame, not the prettier planned target frame.

## Runtime policy

`compact_h30`:
- exactly 3 first-pass Lite scenes
- 30-credit current first-pass ceiling
- final roughly 30–36s

`immersive_h40`:
- exactly 4 first-pass Lite scenes
- 40-credit current first-pass ceiling
- final roughly 38–46s
- G4 must have independent serving/world-resolution/afterglow value

48–60s is not the default. Test longer runtimes only after the channel's own retention and engaged-views-per-credit data supports them.

## Deterministic production gates already built

- source-of-truth ordering from `START_HERE.md`
- HERO_CAT_V1 / KITCHEN_WORLD_V1
- POV paw-only + tiny-scale hard gates
- Flow generation-vs-edit UI preflight
- Progressive Spend
- actual-last-frame sequential chaining
- generated Flow Pack with explicit First/Last operator mapping
- manifest-aware H30/H40 operator guidance
- novelty/authenticity gate against recent repeated hook/conflict/ending fingerprints
- seasonal evidence saturation/no-churn gate
- manifest scene-count/runtime/credit consistency validation
- keyframe-reference integrity: planned `KF*` tokens must exist and contain non-empty prompts
- scene-action integrity: every paid G scene must have a non-empty `action` and `action_guard`
- **explicit zero-cut preservation: when a manifest says `max_visual_cuts_per_8s_generation: 0`, the generated paid prompt now literally says `Maximum visual cuts ...: 0` instead of silently dropping the constraint**
- local regression tests for runtime, frame chain, novelty, manifest consistency, keyframes, scene-action instructions, and zero-cut prompt rendering

## Latest change — Explicit Zero-Cut Prompt Preservation

Problem found in `tools/build_flow_pack.py` before TK-005 production:
- TK-005 declares `max_visual_cuts_per_8s_generation: 0` to enforce calm long-take pacing.
- The Flow Pack builder used `if max_cuts`, so numeric zero was treated as false and the scene-level cut constraint disappeared from the paid prompt.
- Global text still discouraged rapid montage, but the strongest deterministic scene-level instruction was missing exactly when the manifest demanded zero cuts.
- This could increase unnecessary shot changes, continuity drift, and reroll risk per credit.

Fix:
- render the cut clause whenever the value is explicitly present, including `0`
- leave it absent only when the manifest did not specify a cut limit
- regression coverage proves `0` is rendered and an unset value is not invented

This is a 0-credit operator/tooling fix. It does not change TK-005's story, runtime, generation count, or budget.

## Research / idea policy

Source files: `research/benchmark_log.csv`, `research/seasonal_evidence.yaml`, `ideas/episode_backlog.yaml`, `ideas/novelty_signatures.yaml`, `docs/27_research_evidence_saturation_gate.md`, `docs/28_episode_novelty_authenticity_gate.md`.

Score candidates on benchmark evidence, Japan relevance, healing fit, visual satisfaction, Veo reliability, originality, worldbuilding, audience demand, and expected credit efficiency.

Never copy a competitor's exact title, plot, branded product/package, or ending. Keep only abstract mechanisms: hook, scale contrast, tactile action, pacing, payoff, seasonal timing, and worldbuilding.

Current candidate state:
- IDEA-009 yakiimo is already realized as TK-005 and blocked as a future repeat
- IDEA-001 8mm 月見だんご remains a priority future candidate
- IDEA-010 8mm 新米塩むすび is a future candidate backed by current rice-reservation behavior
- IDEA-002 gummy is blocked against a recent equivalent conflict/ending structure

Fresh 2026-08-27 research does **not** justify another research/backlog change: official Flow assumptions are unchanged and newly found autumn retail/adjacent content signals do not change evidence class, candidate ranking, production timing, or NEXT_EPISODE.

## Current production state

`production/NEXT_EPISODE.txt` = **TK-005**

Title:

```text
猫の前足で作る、12mmの焼きいも。
```

Manifest: `episodes/TK-005.yaml`  
Runtime: `immersive_h40`

Beats:
1. impossible-scale reveal: 12mm purple sweet potato beside paws
2. slow roast / skin crack
3. same tray slides away; residual heat opens the existing crack and reveals golden center
4. same tray slides into the tiny serving niche; paws withdraw; steam remains

Continuity and action rules:
- same roasting tray G1–G4
- no surprise new cookware
- no direct pinch/grab of the sweet potato
- G2 First = actual last usable frame from G1
- G3 First = actual last usable frame from G2
- G4 First = actual last usable frame from G3
- all planned KF references must resolve before preparation
- every G1–G4 scene has explicit `action` and `action_guard`
- `max_visual_cuts_per_8s_generation: 0` must remain literal in generated G prompts

The highest-value next real-world step remains **generate TK-005 G1 only and QC it**. Automation must not spend that credit for the user.

## Production learning available so far

`analytics/learning_ledger.csv` currently contains one real preflight failure showing:
- third-person/full-cat framing
- body visible
- scale too large
- human-like tool-use risk

Hard response:
- true first-person camera
- front paws only
- hero object <=0.50 paw width
- prefer nudge/press/slide family

There is not yet enough real 24h/72h public performance data. Never learn from placeholder zeroes as real performance.

Long-term KPIs:

```text
usable motion / credit
engaged views / credit
subscribers / 100 credits
```

## Roadmap

### Phase A — TK-005 production truth
1. approve free opening/target frames
2. generate G1 only
3. QC POV / scale / anatomy / camera / action / unwanted cuts
4. on PASS, save actual last usable frame
5. continue G2 → G3 → justified G4 only through progressive gates
6. record actual credits, rerolls, usable seconds, failure type

### Phase B — first public Shorts learning
At 24h/72h record Stayed to watch, APV, engaged views, subscribers, comments, final runtime, credits, rerolls.

### Phase C — runtime learning
Compare compact_h30 vs immersive_h40 on APV, engaged views/credit, subscribers/100 credits, and beat drop-off.

### Phase D — operator simplification
Keep reducing manual judgment so `다음 영상 준비해줘` remains sufficient. Update tooling only when actual Flow behavior or production evidence changes.

### Phase E — worldbuilding expansion
Only after performance evidence supports it, expand tiny-stall, rainy-shop, after-hours bakery, seasonal ritual, and other distinct worlds without repeating the same story fingerprint.

## Next priorities

1. TK-005 actual G1 production/QC data
2. confirm true zero-cut long-take behavior in the real Flow output
3. verify actual-last-usable-frame continuity in practice
4. record actual credits/rerolls/usable motion
5. obtain first public 24h/72h sample
6. only then re-weight runtime/action/idea priors

More same-class retail PR collection is not a priority.

## Work-start order

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

Stale chat or automation wording never overrides newer merged repository state.

## Safety / invariants

- no automatic Flow credit spend
- no automatic paid generation
- no automatic YouTube publish
- no exact competitor copying
- no third-person/full-cat regression
- no substitute planned frame for an actual previous PASS frame
- no undefined/missing KF improvisation at production time
- no paid scene with blank action or blank action_guard
- no silent loss of an explicit `0`-cut scene constraint
- no next-scene spend after previous-scene failure
- no scene-count/runtime/credit mismatch
- no padding G4 merely to hit a duration
- no reroll of good motion for audio-only defects
- no placeholder analytics treated as real observations
- do not modify Cali or unrelated repositories

## Definition of Done

```text
current research
→ scored + novelty-safe candidate
→ POV/tiny-scale production-safe manifest
→ spend/runtime/keyframe/action/cut consistency PASS
→ free frame preflight
→ progressive Flow generation
→ actual-frame continuity chain
→ edit/export
→ upload
→ 24h/72h learning
→ next episode prior update
```

Success is measured by first-pass success, usable motion/credit, engaged views/credit, subscribers/credit, fewer continuity/camera rerolls, less operator judgment, and fewer repeated story fingerprints — not by commit count.

## Change log

### 2026-08-27 — Explicit zero-cut Flow prompt preservation
Baseline `main@4c61aeb32dcde224730ec18f424923392735bfbf`.

Changed:
- fix truthiness bug that dropped `max_visual_cuts_per_8s_generation: 0`
- paid scene prompts now explicitly preserve a declared zero-cut constraint
- add regression coverage for explicit zero and unset cut limit
- synchronize this handoff

Verified assumptions:
- TK-005 already declares zero cuts and directly benefits from the fix
- official Flow pricing/features remain unchanged on 2026-08-27
- fresh research did not justify ranking/NEXT_EPISODE changes

Unchanged:
- NEXT_EPISODE = TK-005
- TK-005 story/runtime/40-credit first-pass ceiling
- candidate ranking
- no credits spent, no paid generation, no publishing

### Earlier 2026-08-27 work
- scene-action integrity gate
- keyframe-reference integrity gate
- manifest spend consistency fail-closed gate
- runtime-aware operator guidance
- explicit Flow First/Last frame mapping
- IDEA-010 new-rice onigiri candidate
- deterministic novelty/authenticity gate
