# Tiny Cat Kitchen — PROJECT HANDOFF

Last update: **2026-08-28 KST**
Baseline inspected before this iteration: `main@f515c3469df8d35cd5ffd55b78dd0d3ff9768011`

This is the durable handoff source of truth for `lgkangno1-svg/youtube-diorama`. Every material repository change must update this file in the same branch/PR. True NO-OP research should not churn it.

## Development execution policy

- inspect latest main SHA + recent commits/PRs before every run
- latest merged repository state overrides stale chat/scheduled-prompt wording
- modify only `lgkangno1-svg/youtube-diorama`
- do not spend Flow credits, generate paid video, or publish to YouTube without explicit user action

## Mission

Build a Japanese-target Shorts operating system with the normal user interface:

```text
다음 영상 준비해줘
```

The system researches current miniature/ASMR/food signals, chooses a novelty-safe episode, prepares its manifest and NEXT_EPISODE, generates deterministic local operator packs, minimizes paid-generation failures, and learns from real production plus 24h/72h YouTube results.

User local entrypoint:

```powershell
./tools/make_next_short.ps1
```

## Critical user-directed visual correction — 2026-08-28

The user explicitly clarified the desired reference:

> **Mini Forest-style miniature cooking/making, except the human hands are replaced by the cat's front paws. The cat's full body does not need to appear.**

This supersedes the previous assumption that Shorts must always be a literal first-person cat-eye POV.

### Current canonical viewer-facing identity

Tiny Cat Kitchen is **not** an AI-cat character-performance channel.

It is:
- realistic miniature cooking / making
- handcrafted tiny workbench/world
- process-first pacing
- calm tactile ASMR
- human-hand role replaced by one or two feline front paws
- no face/head/body/full cat
- absurdly tiny hero food/object

Default camera priority:
1. high-oblique maker view — preferred
2. top-down macro
3. tabletop / side-oblique macro
4. first-person-like cat angle only when it naturally improves the making shot

The viewer watches the paws make the tiny object; the viewer does **not** need to literally inhabit the cat's eyes.

### Machine-label compatibility

Existing repository enum/path names such as:
- `POV_PAWS_MICROWORLD_V1`
- `camera_grammar.mode: first_person_cat_pov`
- `docs/25_pov_paws_microworld_grammar.md`

are retained temporarily because current validator/selector and historical backlog use them.

**Do not interpret those legacy names as permission to restore mandatory true first-person framing.**

The semantic source of truth is now:

```text
mini_forest_style_paws_only_miniature_making
```

The current TK-005 manifest carries `semantic_override: mini_forest_style_observational_maker_view` and `first_person_required: false` while retaining the old machine-compatible camera enum.

A future cleanup may version the enum and migrate validator/backlog once there is a safe all-at-once schema migration with regression coverage. Until then, production prompts/docs must follow current semantics, not the legacy enum name.

## Flow Pack behavior

`tools/build_flow_pack.py` no longer injects a mandatory true first-person cat-eye prompt.

It injects a `MAKER_STYLE` anchor requiring:
- realistic Mini Forest-style miniature-making composition
- high-oblique/top-down/tabletop macro camera as appropriate
- only one or two feline front paws where human hands normally would enter
- no cat face/head/body/full cat
- no human hands/fingers/thumbs
- hero object about 15–50% of paw width
- real miniature materials / tactile physics
- process-first calm pacing
- no cat character-performance framing

Existing continuity, scale, no-human-grip, output-count and progressive-spend protections remain.

## Research benchmark policy

Primary production benchmark class:
- Mini Forest-style miniature cooking
- handcrafted tiny-food making
- relaxing ASMR / tactile food process

Use only abstract mechanics:
- hand-centric making composition
- miniature craftsmanship
- process clarity
- tiny scale contrast
- tactile sensory payoff
- seasonal food timing

Do not copy exact titles, dishes, sets, plots, branded presentation, or endings.

AI-cat character channels are no longer a primary style benchmark. They may be used only for narrow secondary evidence such as paw appearance/reliability when useful.

## Current Flow / Veo production assumption

Official Google Flow Help rechecked **2026-08-28**:
- Google AI Pro: 1,000 Flow credits/month
- Veo 3.1 Lite 4s/6s/8s + Extend: non-Ultra 10 credits/generation
- actual Flow UI active model/mode/output count/displayed cost remains generation-time truth

Repository production baseline:
- Veo 3.1 Lite
- output count 1
- progressive one-generation-at-a-time spend
- current non-Ultra assumption 10 credits/generation

No paid Flow generation occurred in this iteration.

## Planned keyframe continuity

Before paid G1:

```text
verify image model + displayed cost
→ KF0 maker-view master anchor
→ QC paws / scale / camera / fixed props / lighting
→ derive KF1 from approved KF0
→ derive KF2 from approved KF1
→ continue through all required KFs
→ all planned KFs PASS
→ G1 only
```

KF1+ must not become unrelated fresh text-to-image lottery tickets.

Planned KF = destination.
Actual previous PASS video frame = next-scene continuity bridge.

## Progressive Spend

```text
planned KF chain PASS
→ G1 only
→ QC
→ native Save frame
→ G2 only after G1 PASS
→ G3 only after G2 PASS
→ G4 only when immersive_h40 + G3 PASS + independent world-resolution value
```

## Runtime policy

H30/H40 denote current first-pass credit tiers, not promised final seconds.

### compact_h30
- 3 × 8s raw = 24s
- current ceiling 30 credits
- normal final ~24–27s

### immersive_h40
- 4 × 8s raw = 32s
- current ceiling 40 credits
- normal final ~32–35s
- G4 only with independent serving/world-resolution/afterglow value

No invented still/loop padding.

## Scene grammar

Default:

```text
1 calm tactile primary action
+ optional 1 passive material micro-payoff
```

Preferred paw actions:
- nudge
- press
- pat
- roll
- steady
- slide
- tap
- push

Avoid:
- human pinch
- chopsticks/tongs/knife human grip
- precise wrist twist
- chaining a second active paw gesture after the primary action merely for visual flourish

A human-hand action from a Mini Forest reference must be re-designed into a feline-safe equivalent rather than copied literally.

### 2026-08-28 production-risk correction — G4 single-action integrity

TK-005 G4 previously asked for two active paw motions in one 8-second generation: slide the serving tray, then withdraw both paws. That contradicted `preferred_action_count_per_generation: 1` and the repository's calm one-action scene grammar.

Corrected G4:
- **one active action only:** one paw slides the same tray into the already-visible serving niche and stops
- **passive payoff only after stop:** warm steam continues
- no paw-withdrawal gesture
- KF4 now shows the post-slide resting state rather than requiring another gesture

Rationale: fewer simultaneous/serial paw motions should reduce anatomy drift, unintended character-performance behavior, and avoidable reroll risk while better matching the Mini Forest process-first reference class.

## Current production state

`production/NEXT_EPISODE.txt` = **TK-005**

Title:

```text
猫の前足で作る、12mmの焼きいも。
```

Manifest: `episodes/TK-005.yaml`
Runtime: `immersive_h40`
First-pass ceiling: 4 Lite generations / current 40 credits
Final target: 32–35s, nominal 34s

### TK-005 visual intent

Mini Forest-style tiny yakiimo making:
- stable high-oblique macro maker camera
- only cream/pale-ginger front paws enter like hands in a miniature-cooking video
- no cat face/head/body
- 12mm sweet potato remains dramatically smaller than paw
- realistic handcrafted miniature tray/warmer/serving niche
- same set and props through KF0→KF4
- zero-cut calm long takes

Planned KFs:
1. `KF0_OPEN`
2. `KF1_WARM`
3. `KF2_CRACK`
4. `KF3_OPEN`
5. `KF4_SERVE`

Paid destinations:
- G1: KF0 → KF1
- G2: actual saved G1 frame → KF2
- G3: actual saved G2 frame → KF3
- G4: actual saved G3 frame → KF4

G4 is now intentionally limited to **one tray-slide action + passive steam**, with no extra paw-withdrawal motion.

## Production learning available

`analytics/learning_ledger.csv` has one real preflight failure:
- full cat / body visible
- scale too large
- human-like tool-use risk

Important reinterpretation after user clarification:
- `third-person` itself is not the failure.
- **character-performance third-person with cat body visible** is the failure.
- observer/maker-view camera is desirable when it resembles real miniature cooking and shows only paws + workbench.

Hard response:
- paws only
- no face/head/body/full cat
- hero object <=0.50 paw width
- maker process is the subject
- feline-safe action family
- one active paw action per 8-second generation by default

The ledger's historical hypothesis remains preserved as observed history, but its actionable `next_learning` now reflects the corrected Mini Forest-style maker-view standard rather than forcing first-person cat-eye POV.

There is still no trustworthy public 24h/72h Tiny Cat Kitchen performance sample.

Long-term KPIs:

```text
usable motion / credit
engaged views / credit
subscribers / 100 credits
```

## Roadmap

### Phase A — validate corrected visual identity in real Flow
1. create/approve TK-005 KF0 maker-view master anchor
2. confirm it visually resembles a real miniature-cooking setup rather than an AI-cat character scene
3. derive KF1→KF4 with stable camera/paws/scale/props
4. generate G1 only
5. QC MAKER VIEW / paws-only / scale / anatomy / zero-cut / fixed props
6. on PASS, native Save frame
7. continue progressively
8. when G4 is reached, verify the single slide + passive steam ending remains stable without a second paw gesture

### Phase B — enum/schema cleanup after production proof
If real Flow confirms the new maker-view standard is correct and stable:
- introduce a clean visual-grammar version name without mandatory `POV`
- migrate validator
- migrate selector
- migrate backlog candidate labels/premises
- add regression tests preventing accidental return to mandatory cat-eye POV

Do **not** perform this schema migration piecemeal; current legacy enum compatibility prevents breaking the selection/validation toolchain before production proof.

### Phase C — first public Shorts learning
At 24h/72h record Stayed to watch, APV, engaged views, subscribers, comments, runtime, credits, rerolls.

### Phase D — runtime learning
Compare compact_h30 vs immersive_h40 using actual final runtime and performance-per-credit.

## Next priorities

1. real Flow TK-005 KF0 maker-view visual validation
2. KF1→KF4 continuity
3. actual G1 production/QC
4. verify paws-only miniature-making identity in motion
5. actual saved-frame continuity
6. verify single-action scene reliability, especially G4
7. credits/rerolls/usable motion
8. first public 24h/72h sample
9. only then decide whether to perform full enum/backlog schema rename

## Safety / invariants

- no automatic Flow credit spend
- no automatic paid generation
- no automatic YouTube publish
- no exact competitor copying
- no full-cat/face/body in default Shorts
- no AI-cat character-performance regression
- no human hands/fingers/thumbs
- no human-like feline tool grip
- no hero scale >0.50 paw width without explicit evidence-backed exception
- no paid G1 before planned KF chain PASS
- no planned KF substituted for actual previous PASS frame
- no next-scene spend after previous failure
- no runtime padding
- no second active paw gesture after the declared primary action unless a future evidence-backed manifest explicitly changes the action-count policy
- no unrelated repository modifications

## Definition of Done

```text
current research
→ novelty-safe candidate
→ Mini Forest-style paw-only miniature-making manifest
→ free planned-KF continuity PASS
→ progressive Flow generation
→ actual-frame chain
→ edit/export
→ upload
→ 24h/72h learning
→ next prior update
```

Success is measured by usable motion/credit, engaged views/credit, subscribers/credit, continuity, tactile realism and fewer structural rerolls — not commit count.

## Change log

### 2026-08-28 — learning-ledger maker-view correction
Baseline: `main@f515c3469df8d35cd5ffd55b78dd0d3ff9768011`.

Changed:
- preserved the original POV preflight observation/hypothesis as historical evidence
- corrected only the actionable `next_learning` field that still said `force true first-person camera`
- new learning now requires Mini Forest-style maker view, paws only, no cat body, tiny scale, and feline-safe actions
- synchronized this handoff in the same branch

Why:
- the stale ledger instruction could feed future learning/selection logic and accidentally regress the user-directed Mini Forest-style maker-view standard even though canonical docs had already been corrected

Verified:
- NEXT_EPISODE remains TK-005
- no episode/runtime/credit-budget change
- fresh miniature/seasonal research remains same-class/saturated and does not justify backlog or benchmark churn
- official Google Flow Help still lists non-Ultra Veo 3.1 Lite 4/6/8s + Extend at 10 credits/generation
- no Flow credits spent and no YouTube publishing

### 2026-08-28 — TK-005 G4 single-action correction
Baseline: `main@f3c72c9bf8db8bee3a1a047f79008f5ed7db92a1`.

Changed:
- removed the second active paw-withdrawal gesture from TK-005 G4
- G4 now contains one tray-slide action followed only by passive steam
- aligned `fourth_beat_value`, KF4, G4 action/action_guard, and originality ending with the one-action rule
- documented the production-risk rationale and next validation target in this handoff

Verified:
- NEXT_EPISODE remains TK-005
- Mini Forest-style paw-only maker-view direction remains canonical
- immersive_h40 / four Lite generations / current 40-credit first-pass ceiling unchanged
