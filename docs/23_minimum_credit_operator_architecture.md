# 23 — Quality-First Fast Operator Architecture

> Legacy filename retained for links. Current purpose is **quality + speed first**, not minimum-credit-at-all-costs.

목표: 사용자가 매번 주제/Flow 프롬프트/편집 순서를 고민하지 않고 **한 문장 → Operator Card → strong KF chain → 필요한 paid generation만 순차 실행 → 성과/제작시간 학습**으로 끝내게 한다.

## Priority order

1. video/content quality
2. viewer outcome / channel identity
3. production convenience and speed
4. paid-video reroll/credit efficiency
5. free-image cost policing

Nano Banana는 사용자의 현재 Google 사용 환경에서 무료로 사용할 수 있다. 이미지 단계는 비용 방어보다 **좋은 KF0와 continuity를 빠르게 만드는 quality preflight**로 사용한다. 기존 cost/model 확인 문구는 safety rail일 뿐, 실제 문제가 없으면 더 고도화하지 않는다.

## User interface

```text
다음 영상 준비해줘
```

로컬:
```powershell
./tools/make_next_short.ps1
```

정상 경로의 PRIMARY RUNBOOK은 `production/<EPISODE>_OPERATOR_CARD.md`다. Bundle/flow-pack은 fallback/reference다.

Operator Card에는 한 번에 필요한 것만 있어야 한다.
- NOW action
- hook/scale/payoff target
- exact-order KF prompts
- exact-order G prompts
- PASS/FAIL criteria
- paid generation 직전 설정

사용자가 여러 문서에서 프롬프트와 negative constraints를 재조립하게 하지 않는다.

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

Paid Veo 전에 다섯 항목이 명확해야 한다.

- **HOOK:** 첫 1–2초에 tiny + paws + making을 즉시 이해
- **TRANSFORMATION:** scene마다 눈에 보이는 상태 변화
- **SCALE PROOF:** paw/object 대비가 강함
- **PAYOFF:** stay-to-watch를 정당화하는 완성/재료 payoff
- **NOVELTY/JAPAN FIT:** 현재 일본 타깃에게 의미 있고 exact-copy가 아님

약하면 더 많은 generation을 계획하지 말고 premise/action/frame을 고친다.

## Gate A — planned visual continuity

```text
strong KF0 maker-view master anchor
→ paw anatomy / scale / camera / props / lighting QC
→ KF1은 승인 KF0에서 derive/edit/reference
→ KF2는 KF1에서 파생
→ ...
→ all planned KFs PASS
→ G1 only
```

KF1+를 fresh independent text-to-image lottery로 만들지 않는다.

보존 우선순위:
1. paw fur/anatomy/count
2. hero scale
3. maker-view camera/lens
4. workbench geometry
5. fixed props
6. lighting/DOF
7. intended material-state change only

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
visual chain PASS
→ G1 only
→ quality QC
→ PASS: native Save frame
→ G2 only after G1 PASS
→ G3 only after G2 PASS
→ G4 only if real G3 뒤에도 independent resolution value가 있음
```

다음 scene First frame은 previous PASS clip의 actual native saved frame이다.

구조 FAIL 뒤 다음 paid generation 금지.

## Runtime

H30/H40는 first-pass spend tier이지 final runtime target을 억지로 채우는 규칙이 아니다.

### compact_h30
- 3 × 8s raw
- current non-Ultra first-pass ceiling 30 credits
- 보통 24–27s final

### immersive_h40
- 최대 4 × 8s raw
- current non-Ultra first-pass ceiling 40 credits
- G4는 independent serving/world-resolution/afterglow value가 있을 때만

G3가 이미 완결되면 G4를 생략한다. Runtime padding 금지.

## One 8-second generation

> **1 calm tactile primary action + optional 1 passive material payoff**

Safe action family:
`nudge / press / pat / roll / steady / slide / tap / push`

피함:
- human pinch
- tongs/chopsticks/knife grip
- precise twist
- multiple active gestures
- rapid montage

기본은 0-cut long take.

## QC priorities — quality before technical checkboxing

1. opening premise/scale readability
2. miniature-making realism
3. feline paw anatomy/motion
4. visible tactile transformation
5. continuity of scale/props/camera/light
6. calm but watchable pacing
7. payoff strength

구조적으로 틀리면 다음 spend 금지.

## Audio / finishing

기본:
- no narration
- no generated music
- quiet close miniature ASMR

좋은 motion + 나쁜 audio는 reroll보다 edit replacement.

Eligible Flow UI에서 1080p upscale이 0 credits로 표시되면 continuity chain 완료 뒤 QC-PASS clip에만 적용할 수 있다. Upscaled/re-encoded output은 next-scene continuity bridge로 사용하지 않는다.

## Operator-efficiency metrics

실제 제작에서 가능한 범위로 기록:
- preparation minutes / episode
- manual interventions / episode
- prompt corrections before G1
- time-to-first-valid-G1
- rerolls / finished episode

이 지표는 `credits/video`보다 **사용자가 실제로 얼마나 빨리 좋은 영상을 만드는지**를 보여준다.

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

핵심 원칙:

> **무료 image/reference 단계에서는 가장 강한 visual premise와 continuity를 빠르게 만든다. Paid Veo는 한 번에 하나씩 quality-gated로 사용한다. 비용 최소화 자체보다 좋은 Short를 더 빠르고 반복 가능하게 만드는 것이 우선이다.**
