# 23 — Minimum-Credit Operator Architecture

목표: 사용자가 매번 주제, 대본, Flow 프롬프트, 편집 순서를 고민하지 않고 **ChatGPT에 한 문장 → 필요한 generation만 순차 실행 → 결과를 다시 학습**하게 한다.

관련 source of truth:
- production: `CURRENT_STANDARD.md`
- learning: `docs/22_continuous_episode_learning_engine.md`
- brand continuity: `docs/24_hero_cat_brand_identity.md`

## 최종 사용자 인터페이스

평소 사용자가 ChatGPT에 말할 것은 원칙적으로 하나다.

```text
다음 영상 준비해줘.
```

ChatGPT가 수행:
- 최근 일본/글로벌 AI cat / miniature / ASMR / relaxing Shorts 벤치마킹
- 일본 계절/문화/음식 트렌드 확인
- 과거 24h/72h 성과와 Flow 실패 기록 확인
- 후보 점수화/중복 제거
- 다음 episode 선정
- 일본어 title / hook / optional narration 작성
- episode manifest 생성
- `production/NEXT_EPISODE.txt` 갱신

사용자가 로컬에서 실행:

```powershell
./tools/make_next_short.ps1
```

그 뒤 Flow에서 G1부터 순차 진행한다.

---

## 핵심 비용 원칙 — Progressive Spend H30

운영 계정은 Google AI Pro 기준이다. 현재 공식 Google Flow 표에서 Pro는 월 1,000 Flow credits이며, Veo 3.1 Lite 4/6/8초와 Extend는 non-Ultra 10 credits/generation이다. Plus/Pro/Ultra의 1080p upscale은 0 credits다.

`15 credits`가 보인다는 이유만으로 Lite라고 가정하지 않는다. 현재 공식표에서 Gemini Omni Flash 4초가 15 credits다.

생성 직전 확인:

```text
active model = Veo 3.1 Lite
duration = 8s
output count = 1
displayed cost = 10 credits / generation
```

UI가 공식 문서와 다르면 실제 UI 비용을 기록하고 생성 전에 모델/조건을 재확인한다.

기본 first-pass 최대:

```text
G1 = 10
G2 = 10
G3 = 10
max first pass = 30 credits
```

하지만 30 credits를 미리 쓰지 않는다.

### Gate A — 0 credits

무료 image/reference/keyframe을 먼저 검수한다.

현재 brand identity:
- `HERO_CAT_V1`: cream fur + pale ginger markings, round amber eyes, pink nose, beige linen apron
- 실제 feline paws, human fingers/thumbs 금지
- `KITCHEN_WORLD_V1`: warm miniature Japanese-inspired wooden kitchen, pottery, soft natural light

FAIL 조건:
- cat face/fur/apron identity drift
- human hand/finger anatomy
- kitchen identity가 크게 달라짐
- cookware/food scale 붕괴
- 첫 1초의 행동이 읽히지 않음
- 복잡하고 산만한 composition

**음식이 예뻐도 hero identity가 다르면 Veo를 진행하지 않는다.**

### Gate B — G1만 생성: 누적 10 credits

G1은 영상 전체의 스타일 앵커다.

다음이 틀리면 G2/G3 금지:
- HERO_CAT_V1
- KITCHEN_WORLD_V1
- scale
- lighting/material language
- main physical action

작은 timing 문제는 편집으로 수리하고 구조적 문제만 G1 reroll을 검토한다.

### Gate C — G2: 누적 20 credits

G1의 실제 마지막 usable frame을 이미지로 저장해 **G2 First frame**으로 사용한다.

G2는 새로운 세계를 다시 생성하지 않고 G1 상태를 이어간다.

G2가 구조적으로 통과한 뒤에만 G3로 간다.

### Gate D — G3: 누적 30 credits

G2의 실제 마지막 usable frame을 다시 저장해 G3 First frame으로 사용한다.

G3는 payoff/resolution만 담당한다.

G1+G2만으로 충분한 완성도가 나오면 G3를 반드시 쓸 필요는 없다. 단, 정지화면 패딩으로 10 credits를 아끼지 않는다.

---

## Sequential Frame Chain

```text
FREE OPEN FRAME
   ↓
G1 8s
   ↓ save actual last usable frame
G2 8s
   ↓ save actual last usable frame
G3 8s
```

각 G2/G3에는 미리 만든 target last frame을 추가할 수 있다.

장점:
- 실제 직전 cat / cookware / food state 계승
- 캐릭터 재해석 drift 감소
- color/light/scale continuity 개선
- endpoint 통제 강화

현재 기본값은 sequential First+Last chain이며 Extend는 명확한 장면상 이점이 있을 때만 실험한다.

---

## 8초 generation 문법

한 clip은:

> **1 calm primary action + optional 1 micro-beat**

좋은 예:

```text
0–1.5s  real feline paw enters slowly
1.5–6s  turns one tiny sweet potato over the heat
6–8s    paw pauses; skin crack/steam continues
```

금지:
- 2초마다 shot change
- 3~4 camera angle montage
- 여러 utensil 동시 사용
- 여러 unrelated sound event
- 한 clip 안에서 준비→조리→완성→먹기 전부 수행

---

## 오디오 정책

기본:
- no narration
- no generated music
- quiet room tone + one or two isolated natural ASMR families

권장 prompt:

```text
No speech. No music. Quiet room tone. Only isolated natural miniature cooking sounds appropriate to the visible action. No overlapping unrelated sound effects.
```

영상은 좋은데 audio만 이상하면 영상 재생성 금지. reusable SFX로 교체한다.

나레이션은 다음 중 하나가 명확할 때만 일본어 0~2문장:
1. 화면만으로 constraint 이해가 어려움
2. character personality를 한 줄로 강화
3. payoff 의미를 크게 증폭

---

## 크레딧 구조 선택

### H20
2 × 8s Lite = 20 credits.

조건:
- 매우 단순한 process
- 18~26초 Short로 충분
- 무료 frame이 패딩처럼 보이지 않음

### H30 — DEFAULT
3 × 8s Lite = 30 credits.

조건:
- setup → transformation/conflict → payoff가 필요
- 대부분의 Tiny Cat Kitchen Shorts

### H40 — WINNER / STRUCTURAL FIX ONLY
H30 + 1 Lite generation.

허용:
- 상위권으로 검증된 episode
- 명확한 한 컷 구조적 실패
- 추가 generation이 retention/payoff를 실제 개선할 이유가 있음

금지:
- 남은 credit 소진 목적
- minor visual defect
- runtime을 억지로 늘리기 위해

Quality/Fast/Omni는 탐색 기본값으로 사용하지 않는다.

---

## 사용자가 결과를 돌려주는 최소 입력

```text
G1 만들었어. 봐줘.
```

영상/스크린샷 첨부.

ChatGPT 판단:
- PASS → G2
- EDITABLE → regeneration 없이 편집
- REROLL → 해당 scene만 수정
- STOP → premise/identity/visual system 문제, 추가 spend 중단

업로드 후에는 24h/72h Studio screenshot만 보내도 된다.

---

## 매 영상 후 학습

콘텐츠:
- Stayed to watch
- APV
- engaged views
- subscribers / 1k engaged
- comments / 1k engaged

제작:
- actual Flow credits
- reroll count
- G1/G2/G3 first-pass success
- usable motion seconds
- failed action type
- continuity failure type
- narration yes/no
- Flow audio kept/replaced
- final duration

장기 최적화:

```text
usable motion / credit
engaged views / credit
subscribers / 100 credits
```

가장 싼 영상을 만드는 것이 아니라 **성과 가능성이 높은 고품질 영상을 가장 적은 실패 generation으로 만드는 시스템**이 목표다.
