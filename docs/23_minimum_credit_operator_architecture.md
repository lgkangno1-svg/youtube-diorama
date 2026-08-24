# 23 — Minimum-Credit Operator Architecture

목표: 사용자가 매번 주제, 대본, Flow 프롬프트, 편집 순서를 고민하지 않고 **ChatGPT에 한 문장 → Flow에서 필요한 생성만 순차 실행 → 결과를 다시 학습**하는 구조를 만든다.

## 최종 사용자 인터페이스

평소 사용자가 ChatGPT에 말할 것은 원칙적으로 하나다.

```text
다음 영상 준비해줘.
```

ChatGPT가 수행:
- 최근 일본/글로벌 AI cat / miniature / ASMR / relaxing Shorts 벤치마킹
- 일본 계절/문화/음식 트렌드 확인
- 과거 Tiny Cat Kitchen 24h/72h 성과와 Flow 실패 기록 확인
- 후보 생성/점수화/중복 제거
- 다음 에피소드 선정
- 일본어 title / hook / optional narration 작성
- episode manifest 생성
- `production/NEXT_EPISODE.txt` 갱신
- GitHub에 기록

사용자가 로컬에서 실행:

```powershell
./tools/make_next_short.ps1
```

그 뒤 Flow에서 아래 3단계만 수행한다.

---

## 핵심 비용 원칙 — Progressive Spend H30

운영 계정은 **Google AI Pro** 기준이다. 현재 공식 Google Flow 표에서 Pro는 월 1,000 Flow credits이며, Veo 3.1 Lite 4/6/8초와 Extend는 non-Ultra 10 credits/generation이다. Plus/Pro/Ultra의 1080p upscale은 0 credits다.

중요: Flow에서 보이는 `15 credits`는 Veo Lite 비용이라고 단정하지 않는다. 현재 공식표에서 **Gemini Omni Flash 4초가 15 credits**다. 생성 직전 반드시 `active model + duration + displayed credit cost + output count`를 확인한다.

H30 적용 조건:

```text
active model = Veo 3.1 Lite
duration = 8s
output count = 1
displayed cost = 10 credits / generation
```

실제 Flow UI 표시가 공식표와 다르면 UI를 해당 생성의 source of truth로 기록하고 **일단 생성하지 않은 채 비용 기준을 재확인**한다. 모델이 Omni Flash/Fast/Quality로 바뀌어 있으면 Lite로 되돌릴 수 있는지 먼저 확인한다.

4/6/8초 비용이 같으므로 특별한 이유가 없으면 8초를 사용한다.

기본 최대 예산:

```text
G1 = 10
G2 = 10
G3 = 10
max first pass = 30 credits
```

하지만 **30 credits를 미리 쓰지 않는다.**

### Gate A — 0 credits

먼저 무료 이미지/reference/keyframe을 검수한다.

FAIL이면 Veo 생성 금지.

확인:
- cat fur / white-sock paws
- no human fingers/thumbs
- kitchen/cookware scale
- first 1 second visual readability
- calm composition
- food looks appetizing/real

### Gate B — G1만 생성: 누적 10 credits

G1은 영상 전체의 스타일 앵커다.

G1에서 다음이 틀리면 G2/G3를 만들지 않는다.
- cat identity
- kitchen identity
- scale
- overall lighting
- main physical action

작은 타이밍 문제는 편집으로 수리한다.
구조적 문제만 G1 Lite reroll.

### Gate C — G2 생성: 누적 20 credits

G1의 실제 마지막 usable frame을 Flow에서 이미지로 저장하고 **G2 First frame**으로 사용한다.

G2는 새로운 독립 세계를 다시 만들지 않고 G1의 상태를 이어간다.

G2가 구조적으로 통과한 뒤에만 G3로 간다.

### Gate D — G3 생성: 누적 30 credits

G2의 실제 마지막 usable frame을 다시 저장해 G3 First frame으로 사용한다.

G3는 payoff/resolution만 담당한다.

최종 영상이 G1+G2와 free keyframe/edit만으로 이미 충분하면 G3를 반드시 쓸 필요는 없다. 단, 억지 정지화면 패딩으로 10 credits를 아끼지는 않는다.

---

## Sequential Frame Chain

기본 연속성 구조:

```text
FREE OPEN FRAME
   ↓
G1 8s
   ↓ save actual end frame
G2 8s
   ↓ save actual end frame
G3 8s
```

각 G2/G3에는 미리 만든 target last frame을 사용할 수 있다.

장점:
- 직전 영상의 실제 cat / pan / food state가 다음 장면 시작점이 됨
- 생성마다 새 캐릭터를 다시 해석하는 문제 감소
- color/light/scale drift 감소
- Extend보다 각 장면의 endpoint를 더 강하게 통제 가능

Extend는 연결성이 특별히 유리한 장면에서만 실험한다. 기본값은 sequential First+Last chain이다.

---

## 8초를 고품질로 채우는 법

힐링 영상에서 한 8초 generation은 여러 camera cut이 아니라 **한 공간에서 1 primary action + 1 micro beat**를 쓴다.

좋은 예:

```text
0–1.5s  paw slowly enters
1.5–6s  stirs tiny pan twice
6–8s    paw pauses; steam continues
```

또는:

```text
0–5s    pours sauce slowly
5–8s    one drop nearly spills; paw freezes
```

금지:
- 2초마다 shot change
- 3~4개 camera angle montage
- 여러 utensil을 동시에 사용
- 여러 sound event가 동시에 발생
- one clip 안에서 준비→조리→완성→먹기까지 전부 수행

원칙:

> One clip = one calm physical action, optionally one small emotional beat.

---

## 오디오 비용/품질 정책

기본:
- no narration
- no generated music
- one or two isolated natural sound families only

Flow prompt는 가능하면:

```text
No speech. No music. Quiet room tone. Only isolated natural miniature cooking sounds appropriate to the visible action. No overlapping unrelated sound effects.
```

Flow audio가 깨끗하면 사용한다.
그렇지 않으면 생성 영상을 다시 만들지 않고 reusable SFX library로 교체한다.

재사용 기본 SFX:
- tiny paw tap
- soft kitchen room tone
- pan sizzle
- wooden scrape
- ceramic click
- water pour
- rain ambience

나레이션은 다음 셋 중 하나가 명확할 때만 사용자 녹음을 제안한다.
1. visual만으로 constraint 이해가 어려움
2. character personality를 한 줄로 강화 가능
3. payoff의 의미를 한 줄이 크게 증폭함

일반적으로 0~2문장.

---

## 크레딧 구조 선택

### H20
2 × 8s Lite = 20 credits.

사용 조건:
- 매우 단순한 process
- 18~26초 Short로 충분
- 무료 keyframe footage가 패딩처럼 보이지 않음

### H30 — DEFAULT
3 × 8s Lite = 30 credits.

사용 조건:
- 대부분의 Tiny Cat Kitchen Shorts
- setup → transformation/conflict → payoff 구조

### H40 — WINNER ONLY
H30 + 1 Lite generation.

허용:
- 기존 영상 성과가 상위권
- 명확한 한 컷의 구조적 실패
- extra generation이 retention/payoff를 실제 개선할 이유가 있음

금지:
- "남은 무료 credit이 있으니까"
- minor visual defect
- 완성본 길이를 억지로 늘리기 위해

Quality/Fast/Omni는 탐색 기본값으로 사용하지 않는다.

---

## 사용자가 결과를 ChatGPT에 돌려주는 최소 입력

생성 직후 가장 쉬운 방식:

```text
G1 만들었어. 이거 봐줘.
```

영상/스크린샷 첨부.

ChatGPT가 판단:
- PASS → G2 prompt/주의점 그대로 진행
- EDITABLE → regeneration 없이 편집 지시
- REROLL → 해당 scene만 수정 prompt
- STOP → premise/visual system 문제, 추가 credit 중단

업로드 후에는 가능하면 24h/72h Studio screenshot만 보내도 된다.
ChatGPT가 metric 값을 읽어 learning ledger에 반영할 수 있도록 한다.

---

## 매 영상 후 반드시 학습할 것

콘텐츠 성과:
- Stayed to watch
- APV
- subscribers / 1k engaged
- comments / 1k engaged

제작 성과:
- actual Flow credits
- reroll count
- failed action type
- continuity failure type
- narration yes/no
- Flow audio kept/replaced
- final duration

목적은 특정 음식 복제가 아니라 다음과 같은 production prior를 축적하는 것이다.

예:
- `liquid pour + one paw`는 성공률 높음
- `two paws + wrapping fragile egg`는 reroll률 높음
- `steam hero hold 1.2s`가 payoff에 좋음
- narration이 없는 편이 APV가 높음

이 prior를 다음 후보 scoring에 넣어 **조회 가능성뿐 아니라 expected credits per usable Short**를 줄인다.

---

## 최종 최적화 목표

단순 `credits/video`가 아니라:

```text
usable high-quality Shorts / Flow credit
```

그리고 장기적으로:

```text
engaged views / Flow credit
qualified views / Flow credit
subscribers / Flow credit
```

를 높인다.

즉 가장 싼 영상을 만드는 것이 아니라 **성과가 나올 가능성이 높은 고품질 영상을 가장 적은 재생성으로 만드는 시스템**이 목표다.
