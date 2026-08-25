# 23 — Minimum-Credit Operator Architecture

목표: 사용자가 매번 주제, 대본, Flow 프롬프트, 편집 순서를 고민하지 않고 **한 문장 → 무료 preflight → 필요한 generation만 순차 실행 → 결과 학습**으로 끝내게 한다.

관련 source of truth:
- production: `CURRENT_STANDARD.md`
- learning: `docs/22_continuous_episode_learning_engine.md`
- character/world: `docs/24_hero_cat_brand_identity.md`
- Shorts camera/scale: `docs/25_pov_paws_microworld_grammar.md`

## 사용자 인터페이스

평소 사용자는:

```text
다음 영상 준비해줘
```

라고만 말한다.

ChatGPT가:
- 최신 일본 seasonal/search/social signal 확인
- benchmark mechanics 확인
- production/analytics history 확인
- POV paw-only 적합성 평가
- 다음 episode 선정
- H30 vs H40 runtime gate 선택
- manifest / NEXT_EPISODE 준비

사용자는:

```powershell
./tools/make_next_short.ps1
```

만 실행한다.

## Gate A — 0 credits

Flow video를 만들기 전에 무료 keyframe/reference를 먼저 검수한다.

반드시 PASS:
- true first-person cat POV
- front paws only
- face/head/body/full cat hidden
- real feline paw anatomy
- hero object가 한 앞발 폭의 절반 이하로 보임
- 5~20mm 수준의 tiny-object 느낌
- macro miniature diorama workbench
- 첫 1초에 scale contrast가 이해됨

다음이면 즉시 STOP:
- 고양이가 카운터 뒤에서 보이는 third-person chef shot
- 고양이 얼굴/전신 노출
- 음식/도구가 앞발과 비슷하거나 더 큼
- human fingers/thumbs
- paw가 사람처럼 tool을 grip

## Flow settings

생성 직전 실제 UI 확인:

```text
Veo 3.1 Lite
9:16
8 seconds
output count = 1
표시 비용 = 10 credits / generation (현재 UI가 그렇게 보일 때)
```

UI가 다르면 생성하지 말고 모델/비용을 재검토한다.

## Progressive Spend

### G1 — 누적 10

G1은 channel grammar anchor다.

QC:
- POV
- paws only
- scale cuteness
- anatomy
- miniature material language
- primary action

하나라도 구조적으로 틀리면 G2 금지.

### G2 — 누적 20

G1의 actual last usable frame을 G2 First frame으로 사용한다.

### G3 — 누적 30

G2의 actual last usable frame을 G3 First frame으로 사용한다.

여기까지로 완결되면 `compact_h30`으로 끝낸다.

### G4 — 누적 40, 조건부

다음 조건을 모두 만족할 때만 사용:
- G3까지 PASS
- manifest runtime mode = `immersive_h40`
- 네 번째 독립 motion/world beat가 존재
- G4를 빼면 세계관 여운/serving/resolution이 실제로 약해짐

예:
- 완성품을 tiny serving alcove에 밀어 넣기
- paws가 천천히 빠지고 작은 세계가 계속 살아 있음
- loopable afterglow

금지:
- 40초를 맞추기 위한 패딩
- 이미 끝난 음식의 반복 close-up
- 남은 credits 소진

## Runtime 선택

### compact_h30

```text
3 × 8s raw motion = 24s
final target ≈ 30~36s
```

적합:
- 3개 beat로 이야기 완결
- scale reveal → making → payoff

### immersive_h40

```text
4 × 8s raw motion = 32s
final target ≈ 38~46s
```

적합:
- tiny world를 느끼게 할 4번째 독립 beat가 있음
- world-resolution이 retention/payoff를 높일 합리적 이유가 있음

### 48~60s

실제 채널 성과 데이터가 지지하기 전에는 기본값이 아니다.

## Paw-action rule

Veo reliability 우선:

좋음:
- nudge
- press
- pat
- roll
- steady
- slide
- tap

나쁨:
- tongs/chopsticks/knife를 fingers로 잡는 동작
- 인간형 pinch
- 손목 twist

도구가 필요하면 넓은 손잡이를 paw pad로 눌러 움직이게 한다.

## 8초 generation 문법

> **1 calm tactile primary action + optional 1 micro-payoff**

예:

```text
0~1.5s  paw approaches absurdly tiny object
1.5~6s  one press / roll / slide action
6~8s    paw stops; steam/crack/gloss/crumb continues
```

no rapid montage / no camera orbit / no full-cat reveal.

## Sequential Frame Chain

```text
G1
↓ actual last usable frame
G2
↓ actual last usable frame
G3
↓ actual last usable frame
G4 only if immersive_h40
```

연속성 우선순위:
1. first-person camera position
2. paw fur/anatomy
3. hero-object size ratio
4. cookware/food state
5. lighting/workbench

## Audio

기본:
- no narration
- no generated music
- quiet close ASMR

좋은 소리:
- tiny ceramic click
- subtle wood scrape
- crumb/dough press
- soft sizzle
- paper rustle

영상이 좋고 audio만 나쁘면 재생성하지 않고 후편집 교체.

## 결과를 보여줄 때

```text
G1 만들었어. 봐줘
```

ChatGPT 판정:
- `PASS`
- `EDITABLE`
- `REROLL`
- `STOP`

추가 shorthand:
- `POV FAIL`
- `SCALE FAIL`
- `ANATOMY FAIL`
- `CAMERA FAIL`
- `PADDING FAIL`

## 학습

콘텐츠:
- Stayed to watch
- APV
- engaged views
- subscribers
- comments
- beat별 drop-off 가능하면 기록

제작:
- actual credits
- rerolls
- G1/G2/G3/G4 first-pass success
- POV/scale/anatomy failures
- failed action type
- usable motion seconds
- final runtime

장기 최적화:

```text
usable motion / credit
engaged views / credit
subscribers / 100 credits
```

초기 runtime experiment는 `30~36s compact_h30`과 `38~46s immersive_h40`을 비교한다. 더 긴 영상은 실제 데이터가 지지할 때만 확장한다.
