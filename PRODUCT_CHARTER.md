# Tiny Cat Kitchen — PRODUCT CHARTER

Status: **Durable product intent / decision standard**
Owner intent synthesized: **2026-08-28 KST**

This document answers one question for every future AI/developer:

> **What is the user actually trying to build, and by what standard should every future development, research, production, and optimization decision be judged?**

It is intentionally more stable than an episode manifest or implementation detail. `PROJECT_HANDOFF.md` describes current state; `CURRENT_STANDARD.md` describes current operating rules; this charter describes the durable product purpose and decision philosophy.

When documents conflict, use this precedence:
1. explicit newer user instruction
2. latest merged `PROJECT_HANDOFF.md` and accepted repository state
3. this `PRODUCT_CHARTER.md` for durable intent
4. `CURRENT_STANDARD.md` / specialized docs for implementation details
5. older manifests, prompts, research notes, or legacy enum names

Do not use this charter to override a newer explicit user correction. Update this charter when the user's durable goal materially changes.

---

## 1. Product purpose

Tiny Cat Kitchen is a repeatable Japanese-target YouTube Shorts production system for creating **high-quality, calming, highly watchable miniature making/cooking videos in which the visual role normally occupied by human hands is naturally performed by a cat's front paws**.

The desired viewer reaction is approximately:

> "This feels like a real, beautifully made miniature cooking video — except tiny cat paws are making it. It is absurdly small, tactile, cute, satisfying, and relaxing."

The product is **not** primarily an AI-cat character channel, a talking-cat channel, a comedy roleplay channel, or a showcase of generative-AI spectacle.

AI is an invisible production tool. The miniature world, tactile process, tiny scale, paw interaction, and healing viewing experience are the product.

---

## 2. Core creative thesis

The clearest creative shorthand is:

> **Mini Forest-like realistic miniature making, but replace the human hands with believable feline front paws.**

This is a reference to an abstract production grammar, not permission to copy a creator's exact work.

Preserve:
- handcrafted miniature realism
- extreme tiny-scale contrast
- process-first composition
- tactile material transformation
- calm, legible pacing
- macro/maker-view intimacy
- satisfying physical payoff
- close ASMR / quiet healing mood

Transform:
- human-hand actions into feline-safe paw actions
- competitor subject matter into original Tiny Cat Kitchen episodes
- seasonal/cultural demand signals into original concepts

Never copy:
- exact title
- exact plot or scene sequence
- branded package/product presentation
- distinctive set dressing
- exact ending/payoff
- creator-specific signature composition

---

## 3. Non-negotiable visual identity

Default subject grammar:
- one or two cream/pale-ginger feline front paws
- no cat face, head, torso, or full body
- no human hand, finger, or thumb
- no human-like paw grip
- hero food/object is absurdly tiny, normally 5–20mm and <= 0.50 paw width
- realistic miniature workbench/diorama
- paws enter the working area where hands would naturally appear
- the making process is visually dominant; the cat is not acting as a human character

Default camera grammar:
1. high-oblique maker view
2. top-down macro
3. tabletop / side-oblique macro
4. first-person-like angle only when it genuinely improves the shot

Literal cat-eye first-person POV is **not a product requirement**. Legacy names containing `POV` must never be allowed to regress the channel into mandatory first-person framing.

A successful frame should still work as a satisfying miniature-making image if the viewer mentally substitutes the paws with hands. The paws then add the Tiny Cat Kitchen identity, cuteness, and scale contrast.

---

## 4. Motion and pacing philosophy

The user wants a soothing miniature process, not an AI montage.

Default per paid 8-second generation:

> **one primary tactile paw-safe action + at most one passive material payoff**

Preferred active verbs include:
- nudge
- press
- pat
- roll
- steady
- slide
- tap
- push

Passive payoffs include:
- steam
- gloss
- crack
- crumb
- gentle sizzle
- settling sauce/material

Avoid asking Veo to solve several independent hand-like gestures inside one clip. Complex serial manipulation increases anatomy, continuity, and wasted-credit risk while reducing the calm long-take quality.

Default editing grammar:
- stable long take
- zero or very few cuts inside a generation
- no rapid montage
- no invented still/loop padding simply to reach a target runtime

---

## 5. Audio philosophy

Default:
- no narration
- no generated music
- quiet room tone
- isolated close miniature ASMR

Use a short user-recorded Japanese line only when it materially improves comprehension, personality, or payoff. Do not add speech merely because a Shorts format convention exists.

If motion is excellent but generated audio is poor, preserve the valuable video and replace/fix audio in post rather than automatically spending credits on a reroll.

---

## 6. Audience and content strategy

Primary audience: Japanese Shorts viewers, while keeping the visual premise globally understandable without language dependence.

Episode selection should combine:
- Japanese cultural/seasonal relevance
- recognizable food or tiny-object appeal
- healing fit
- tactile visual satisfaction
- Veo reliability
- originality / novelty safety
- miniature-world continuity potential
- audience demand
- expected usable-quality-per-credit

Japanese relevance is a demand/timing advantage, not a requirement to force Japanese text, narration, or stereotypes into every episode.

Research Japanese and global miniature cooking, ASMR, relaxing food, AI-cat and adjacent Shorts to extract success mechanics. Research is useful only when it changes a decision. Once an evidence class is saturated, repeated same-class promotional/retail news is noise.

---

## 7. Production economics

The goal is **not simply the cheapest possible video**. The goal is the best sustainable combination of quality, viewer response, learning speed, and credit efficiency.

Optimize toward:
- usable motion seconds / credit
- engaged views / credit
- subscribers / 100 credits

Secondary diagnostics:
- first-pass success by G1/G2/G3/G4
- rerolls
- anatomy failures
- scale failures
- continuity failures
- failed action types
- final usable runtime
- 24h/72h Stayed to watch
- APV
- engaged views
- subscriber gain
- comments / qualitative viewer response

Do not optimize a proxy such as `credits/video` if it produces weaker videos or fewer subscribers per credit.

---

## 8. Credit-spend philosophy

Paid generation must be progressive, not speculative.

Before paid video:
- verify the real Flow UI/model/mode/output count/displayed price
- use no-charge image/reference preflight when genuinely available
- establish a stable KF0 visual anchor
- derive planned keyframes sequentially rather than generating unrelated lottery frames
- reject structural paw/scale/camera/prop problems before video spend

Then:

```text
planned KF chain PASS
→ generate G1 only
→ QC G1
→ save actual last usable frame
→ generate G2 only if G1 PASS
→ repeat
```

G4 is not automatic. It is justified only when the current runtime strategy and episode manifest say an independent final world-resolution/serving/afterglow beat adds enough value.

The current H30/H40 model is a credit tier, not a promise that every final video must be exactly 30 or 40 seconds.

Never spend Flow credits, generate paid video, or publish to YouTube without explicit user action.

---

## 9. Continuity philosophy

Continuity is a first-class quality feature, not an afterthought.

Preserve across scenes:
- paw fur/color/count/anatomy
- hero-object scale
- workbench geometry
- fixed props
- camera family
- lighting
- food/object state progression

Use planned keyframes as destinations and the **actual previous PASS video's saved frame** as the bridge into the next paid generation whenever supported.

Do not substitute a planned destination image for the actual previous result when the purpose is to preserve motion continuity.

---

## 10. What counts as a structural failure

Reject or redesign when the output materially contains:
- cat face/head/body/full-cat character framing
- a cat performing a human job/role behind a counter
- human hands/fingers/thumbs
- human-like feline tool grip
- weak tiny-scale contrast
- implausible paw anatomy
- uncontrolled prop/camera/world drift
- making process becoming secondary to character spectacle
- rapid AI montage that destroys tactile readability

A third-person or observational maker view is **not itself a failure**.

---

## 11. Development philosophy

Every repository change should reduce one or more of these burdens:
- user deciding what episode to make
- user researching trends manually
- user writing prompts manually
- user remembering Flow settings
- user wasting credits on preventable failures
- user manually reconstructing continuity
- user forgetting to record production/analytics learning
- future AI/developer misunderstanding the creative goal

Prefer robust, simple operator workflows over clever but fragile automation.

The ideal normal interaction is:

```text
User: 다음 영상 준비해줘
```

Then the system/ChatGPT should:
1. inspect latest repository state and handoff
2. inspect current production history and analytics
3. research only enough fresh evidence to make a better decision
4. choose the next original episode
5. choose appropriate runtime/spend tier
6. prepare/update the episode manifest and Flow prompt pack
7. update `production/NEXT_EPISODE.txt`
8. synchronize `PROJECT_HANDOFF.md` for material state changes
9. leave the repository ready for `./tools/make_next_short.ps1`

The user should primarily make creative/QC decisions and explicitly trigger paid generation — not perform repository administration.

---

## 12. Continuous-learning loop

Each real episode is an experiment.

Planning should use actual prior production evidence when available, not theoretical assumptions alone.

Record:
- actual Flow credits
- rerolls
- G-stage first-pass success
- usable motion seconds
- failure class and failed action type
- narration/audio mode
- final runtime
- 24h/72h Shorts metrics
- subscriber and comment outcomes

Then update future episode scoring, action grammar, runtime choice, prompt structure, and spend policy only when evidence warrants it.

Do not rewrite strategy after one noisy datapoint. Do not ignore repeated failure patterns either.

---

## 13. Decision test for every future improvement

Before merging a material improvement, ask:

1. Does this preserve the paws-only miniature-making identity?
2. Does it make the tiny scale clearer or more satisfying?
3. Does it improve tactile process readability/healing quality?
4. Does it reduce anatomy, continuity, camera, or scale failure risk?
5. Does it improve expected usable quality per credit or audience outcome per credit?
6. Does it simplify the user's normal workflow?
7. Is it supported by real production data or meaningful non-saturated evidence?
8. Does it avoid copying a competitor's protected/distinctive expression?
9. Does it preserve explicit user control over paid generation and publishing?
10. Has `PROJECT_HANDOFF.md` been synchronized if the change is material?

If an improvement fails the identity tests (#1–3), lower cost or technical elegance alone is not sufficient justification.

---

## 14. Anti-goals

Do not drift toward:
- generic AI cat videos
- full-cat chef/worker roleplay
- talking-cat story channels
- spectacle-first AI transformations
- human-like paw dexterity for its own sake
- maximizing video length
- maximizing number of scenes
- maximizing research volume
- maximizing automation at the expense of user control
- blindly minimizing credits/video
- copying successful competitor episodes
- repeatedly changing standards without production evidence

---

## 15. Definition of success

Near term:
- reliably produce visually coherent Tiny Cat Kitchen episodes with very low preventable reroll rate
- make the first seconds instantly communicate `cat paws + absurdly tiny real miniature making`
- establish a repeatable operator workflow the user can execute without prompt engineering

Medium term:
- accumulate enough real episode data to identify reliable action types, runtimes, subjects, hooks, and payoffs
- increase engaged views and subscriber conversion per credit
- develop recognizable recurring world/visual continuity without turning the paws into a human-roleplaying character

Long term:

> **Build a distinctive, scalable Japanese-target healing Shorts channel whose signature is believable cat paws quietly making absurdly tiny things, with an evidence-driven production system that continuously improves quality and audience return while controlling generation cost.**

---

## 16. Documentation maintenance contract

For future AI/developers:
- read this after `PROJECT_HANDOFF.md` when starting material planning/development
- do not silently reinterpret the product from a legacy enum, old prompt, or isolated benchmark row
- update this file only for durable changes in product intent, creative identity, economics philosophy, or operator philosophy
- put transient state, current episode, failures, and next actions in `PROJECT_HANDOFF.md`
- put executable/current production rules in `CURRENT_STANDARD.md` and specialized docs
- every material repository change still requires a same-change `PROJECT_HANDOFF.md` update

This separation is intentional:

```text
PRODUCT_CHARTER.md  = why / what we are building / how decisions are judged
PROJECT_HANDOFF.md  = where the project is now / what changed / what is next
CURRENT_STANDARD.md = how production is currently executed
manifests + ledgers = episode-specific plan and observed evidence
```
