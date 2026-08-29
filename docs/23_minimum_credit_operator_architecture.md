# 23 — Quality-First Fast Operator Architecture

> Legacy filename retained for links. Current purpose is **quality + speed first**, not minimum-credit-at-all-costs.

목표: 사용자가 매번 주제/Flow 프롬프트/편집 순서를 고민하지 않고 **한 문장 → Operator Card → strong first pair → 실제 PASS frame 기반 next target → 필요한 paid generation만 순차 실행 → 성과/제작시간 학습**으로 끝내게 한다.

## Priority order

1. video/content quality
2. viewer outcome / channel identity
3. production convenience and speed
4. paid-video reroll/credit efficiency
5. free-image cost policing

Nano Banana는 사용자의 현재 Google 사용 환경에서 무료로 사용할 수 있다. 이미지 단계는 비용 방어보다 **좋은 anchor와 실제 footage에 맞춘 continuity target을 빠르게 만드는 quality tool**로 사용한다.

## User interface

```text
다음 영상 준비해줘
```

로컬:
```powershell
./tools/make_next_short.ps1
```

정상 경로의 PRIMARY RUNBOOK은 `production/<EPISODE>_OPERATOR_CARD.md`다. Bundle/flow-pack은 fallback/reference다.

Operator Card에는 NOW action, hook/scale/payoff target, exact-order image/Flow prompts, PASS/FAIL criteria, paid generation 직전 설정이 포함되어야 한다.

## Visual production intent

> **Mini Forest-style miniature making + human hands naturally replaced by feline front paws only.**

- high-oblique maker view 기본
- top-down / tabletop / side-oblique macro 허용
- true first-person cat POV는 필수 아님
- face/head/body/full cat 금지
- human hands/fingers/thumbs 금지
- human-like paw grip 금지
- hero object 보통 5–20mm, <=0.50 paw width
- process-first / calm tactile realism

`POV_PAWS_MICROWORLD_V1`은 tooling compatibility token이다.

## Content-quality preflight

Paid Veo 전에:
- **HOOK:** 첫 1–2초에 tiny + paws + making을 즉시 이해
- **TRANSFORMATION:** scene마다 눈에 보이는 상태 변화
- **SCALE PROOF:** paw/object 대비가 강함
- **PAYOFF:** stay-to-watch를 정당화하는 완성/재료 payoff
- **NOVELTY/JAPAN FIT:** 현재 일본 타깃에게 의미 있고 exact-copy가 아님

약하면 더 많은 generation을 계획하지 말고 premise/action/frame을 고친다.

## Gate A — first pair, not speculative full chain

기본적으로 G1 전에 필요한 것은 **KF0 + KF1**이다.

```text
strong KF0 maker-view master anchor
→ paw anatomy / scale / camera / props / lighting QC
→ KF1을 approved KF0에서 derive
→ KF0/KF1 PASS
→ G1 only
```

모든 core KF를 G1 전에 미리 만드는 것을 기본값으로 하지 않는다.

## Actual-frame target rebasing

Google Flow 공식 Help는 saved video frame을 future generation의 start/end frame으로 재사용할 수 있다고 안내한다. 이를 core continuity 전략으로 활용한다.

```text
G1 PASS
→ native Save frame
→ actual G1 frame에서 KF2 destination state만 derive
→ G2
→ PASS / Save frame
→ actual G2 frame에서 KF3 destination state만 derive
→ G3
```

원칙:
- manifest의 KF2/KF3/KF4는 **desired destination state**이지 creation timing이 아니다.
- next target source는 가능하면 previous PASS clip의 actual saved frame.
- actual camera/paw/scale/props/light는 그대로 두고 intended material-state change만 적용.
- independent fresh image lottery 금지.

효과:
- real drift를 다음 target에 흡수하여 continuity correction 폭 감소
- time-to-first-valid-G1 단축
- 아직 필요하지 않은 이미지 작업 감소
- planned frame과 실제 footage가 다른 세계가 되는 위험 감소

## Adaptive H40 / optional G4

```text
G1→G3 progressively with actual-frame rebasing
→ real G3 together review
→ core complete = STOP
→ only if G4 adds independent value: derive KF4 from actual saved G3 PASS frame → G4
```

G4 target을 real G3 전에 만들지 않는다.

## Paid Flow baseline

Generate 직전 actual UI 확인:
```text
Veo 3.1 Lite
9:16
8 seconds
output count = 1
displayed cost = current UI truth
```

Paid generation은 explicit user action only.

## Progressive Spend

```text
KF0/KF1 PASS
→ G1 only
→ quality QC
→ PASS: native Save frame
→ derive next target from actual PASS frame
→ G2 only after G1 PASS
→ repeat for G3
→ core complete? STOP
→ optional G4 only if real G3 still benefits
```

구조 FAIL 뒤 다음 paid generation 금지.

## Runtime

H30/H40는 first-pass spend ceiling이지 final runtime target을 억지로 채우는 규칙이 아니다.

### compact_h30
- 3 × 8s raw
- current non-Ultra first-pass ceiling 30 credits
- 보통 24–27s final

### immersive_h40
- 3 core beats + 1 optional G4 candidate
- maximum 4 × 8s raw
- current non-Ultra first-pass ceiling up to 40 credits
- G3가 이미 완결되면 STOP
- G4는 independent resolution value가 real footage에서 남아 있을 때만

Runtime padding 금지.

## One 8-second generation

> **1 calm tactile primary action + optional 1 passive material payoff**

Safe action family: `nudge / press / pat / roll / steady / slide / tap / push`.

피함: human pinch / tongs/chopsticks/knife grip / precise twist / multiple active gestures / rapid montage.

기본은 0-cut long take.

## QC priorities

1. opening premise/scale readability
2. miniature-making realism
3. feline paw anatomy/motion
4. visible tactile transformation
5. continuity of scale/props/camera/light
6. calm but watchable pacing
7. payoff strength

구조적으로 틀리면 다음 spend 금지.

## Audio / finishing

기본: no narration, no generated music, quiet close miniature ASMR.

좋은 motion + 나쁜 audio는 reroll보다 edit replacement.

Eligible Flow UI에서 1080p upscale이 0 credits로 표시되면 continuity chain 완료 뒤 QC-PASS clip에만 적용할 수 있다. Upscaled/re-encoded output은 next-scene continuity bridge로 사용하지 않는다.

## Operator-efficiency metrics

실제 제작에서 가능한 범위로 기록:
- preparation minutes / episode
- manual interventions / episode
- prompt corrections before G1
- time-to-first-valid-G1
- rerolls / finished episode
- next-target continuity corrections after actual-frame rebasing

## Production/audience learning

기존 실제값:
- paid video credits / rerolls
- G1~G4 first-pass success
- maker-view/character/scale/anatomy/continuity failures
- failed action type
- usable motion seconds / final runtime
- 24h/72h Stayed to watch / APV
- engaged views / subscribers / comments

장기 KPI:
```text
content quality first
engaged views / paid credit
subscribers / 100 paid credits
usable motion / paid credit
time-to-first-valid-G1
manual interventions / episode
```
