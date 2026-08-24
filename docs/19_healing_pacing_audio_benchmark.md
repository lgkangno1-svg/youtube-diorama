# Healing Pacing + Audio Benchmark — Tiny Cat Kitchen

작성 기준: 2026-08-24
상태: CURRENT CREATIVE DIRECTION

## 결론

Tiny Cat Kitchen의 기본 감정은 **viral-chaos가 아니라 cozy/healing**이다.

따라서 `2초마다 새 컷`을 기본값으로 두지 않는다. Flow 크레딧을 아끼기 위해 한 generation에서 여러 usable moment를 회수하되, **시청자가 보는 최종 편집은 느리고 부드럽게** 유지한다.

---

# 1. 성공 채널 벤치마킹

## Miniature Cusina

- 약 2.9M subscribers / 약 508.8M total views (2026-07 기준)
- 2015년부터 실제 miniature kitchen + real food 포맷
- 최근 Shorts도 16~56초 범위가 많음
- 채널 핵심 설명은 miniature cooking + soothing sizzling/chopping/clinking sounds
- `No Music Background`, `ASMR`, `Fully Functional Tiny Kitchen`를 반복 사용

벤치마킹 포인트:

> narration으로 설명하기보다 실제 조리 소리와 작은 도구의 촉각적 재미가 콘텐츠 자체가 된다.

우리 적용:
- 지글거림, 작은 도자기 소리, 나무 주걱 소리 중심
- 대사는 선택사항
- 한 action을 충분히 보여줌

## Chef Cat ChangAn

- 약 10.6M subscribers / 약 7.3B views (2026-08 기준)
- YouTube Culture & Trends에서도 Shorts 중심 ASMR cat cooking 성장 사례로 소개됨
- 대표 Shorts:
  - biggest lollipop: 약 491M / 22s
  - poached egg: 약 336M / 34s
  - orange custard: 약 298M / 23s
- 음식 자체의 시각적 변형 + 고양이 캐릭터 + ASMR이 핵심
- 언어 의존성이 낮음

벤치마킹 포인트:

> 고양이 캐릭터가 있어도 긴 설명이 없어도 된다. 화면만으로 목적을 이해할 수 있고, 음식 변화와 tactile sound가 충분히 강하면 글로벌 확장이 쉽다.

주의:
- ChangAn은 pure healing보다 satisfying/funny 쪽이 더 강함.
- 우리의 pace를 그대로 빠르게 복제하지 말고 `cat + food + low-language` 구조만 가져온다.

## Cat Chef's Cooking ねこシェフ

- AI cat cooking을 명시적으로 `癒し映像`으로 포지셔닝
- 인기 영상: hamburger+fries 약 280K, margherita pizza 약 148K, strawberry cake 약 94K
- 설명에서 `日常から解放されて、頭のスイッチがオフになり、安眠できるような`라는 힐링 목적을 반복
- 일부 인기 영상은 2분대 일반 영상으로도 운용

벤치마킹 포인트:

> 힐링형 고양이 요리는 반드시 Shorts 템포로 쪼갤 필요가 없다. 캐릭터가 천천히 한 끼를 완성하는 과정 자체가 시청 목적이 될 수 있다.

## Peaceful Cuisine

Shorts benchmark는 아니지만 `healing cooking grammar` 참고용.

- 일본 기반 relaxing cooking 대표 사례
- 카메라가 재료와 행동에 오래 머뭄
- 부드러운 자연광
- spoon/jar/bowl/flour 등 실제 작은 소리를 강조
- 별도 no-music 버전을 제공할 정도로 cooking sound 자체가 핵심

벤치마킹 포인트:

> 힐링은 컷 수보다 `머무는 시간 + 자연음 + 반복 동작 + 조명`에서 만들어진다.

---

# 2. Tiny Cat Kitchen 권장 Pace

## 기본 38~48초 Healing Short

권장 shot 수:

```text
5~7 shots total
```

평균 shot duration:

```text
4~7 seconds
```

첫 훅만 예외:

```text
0~1.5s = 즉시 상황 인식
1.5s 이후 = 느린 호흡
```

예시 42초:

```text
0.0~3.5   OPEN — 앞발 + 미니 달걀
3.5~9.5   PREP — 쌀/재료를 천천히 팬에 넣음
9.5~16.0  COOK — 볶고 지글거림
16.0~23.0 DANGER — 계란이 찢어질 듯한 긴장
23.0~30.0 ASSEMBLY — 천천히 밥 위에 올림
30.0~37.0 PAYOFF — 완성 음식 Hero / 증기
37.0~42.0 RESOLUTION — 파슬리 선택 / 조용한 개그
```

컷마다 화면을 바꾸기보다 **한 동작이 끝날 때 전환**한다.

---

# 3. Flow 경제성 — Fast Cut Packing을 Healing Packing으로 변경

## 권장: 8초 generation = 1~2 slow actions

Lite 4초와 8초 비용이 같으므로 8초를 사용한다.

하지만 8초에 4개 scene을 넣지 않는다.

### 방식 H1 — One Slow Take

```text
0~2s: cat paw slowly enters
2~6s: slowly stirs rice once or twice
6~8s: stops; steam rises; quiet pause
```

한 8초 생성 전체를 그대로 쓰거나, 앞/뒤 1초만 trim한다.

장점:
- model complexity 낮음
- continuity 높음
- 힐링 감정 유지
- 재생성 가능성 감소

### 방식 H2 — Two-Beat 8s

```text
[00:00-00:04] slow ingredient action
[00:04-00:08] reaction / texture payoff
```

두 shot 모두 같은 주방, 같은 food state, 같은 카메라 family를 유지한다.

예:

```text
[00:00-00:04] Overhead macro. Ten rice grains slowly slide into the tiny pan. Let them settle naturally.
[00:04-00:08] Side macro. One ketchup drop lands and begins to sizzle. Hold on the gentle steam for the final two seconds.
No music, no dialogue, no fast cuts. The transition is a calm hard cut at exactly 4 seconds.
```

2-beat packing은 `한 generation에서 2개의 4초 source`를 얻는 경제형 default 후보.

---

# 4. 20/30/40 Credit Healing Ladder

## H20 — 2 generations

```text
G1 8s: OPEN + PREP
G2 8s: COOK + DANGER
video motion = 16s
```

여기에 무료 keyframe:
- opening push-in
- payoff still
- reaction still
- environmental still

을 사용해 25~32초 Short 제작.

용도:
- premise 테스트
- trend 테스트
- hook validation

## H30 — 3 generations — 추천 기본 실험

```text
G1: OPEN + PREP
G2: COOK + DANGER
G3: ASSEMBLY + PAYOFF/RESOLUTION
= 24s generated motion
```

무료 keyframe slow zoom/freeze, room detail, ending loop를 합쳐 **35~45초**.

이게 현재 가장 유망한 healing/credit 균형점.

## H40 — 4 frame-locked generations

- continuity가 매우 중요한 flagship
- complicated food transformation
- H30이 QC를 통과하지 못할 때

40 credits를 기본으로 자동 소비하지 않는다.

---

# 5. Collage 전략 재평가

## 2×2 VIDEO collage

기술적으로는 9:16 master의 각 2×2 quadrant도 9:16이어서 crop 가능하지만 **healing main footage에는 비권장**.

이유:
- 한 화면에서 네 행동이 동시에 일어나 모델 부담 증가
- 작은 food/fur detail 감소
- generated audio가 4 panel에서 섞임
- panel boundary leakage / object crossing 가능
- 결국 재생성하면 절감분 상실

### 사용 가능 범위

단순 ambient B-roll bank에만 LAB 사용:
- steam only
- rain on window
- paw resting
- bowl sitting on wood
- lamp glow

## 2×2 IMAGE contact sheet

이쪽은 적극 권장.

Nano Banana 2 Lite 이미지 preflight에서 한 장에:
- OPEN
- DANGER
- PAYOFF
- RESOLUTION

4개 thumbnail을 넣어 전체 mood/continuity를 빠르게 검토한다.

단 contact sheet crop을 final hero image로 쓰지 않고 storyboard/approval/reference로 사용한다.

무료 image 단계에서는 크레딧보다 **사용자 클릭 횟수 감소**가 목적이다.

---

# 6. Narration Benchmark + 정책

## 기본값 = No narration

Miniature Cusina / Chef Cat ChangAn 류의 강점은 언어 없이도 이해되는 ASMR 구조다.

따라서 기본 episode:

```text
No narration
No BGM or extremely subtle BGM
Cooking SFX + room tone
```

## narration을 넣는 조건

다음 중 하나가 있을 때만 사람 목소리 사용:

1. 화면만으로 이해되지 않는 story context
2. 고양이 캐릭터 성격을 기억시킬 한 줄
3. 일본 시청자에게 감정적 친밀감을 줄 수 있는 observational line
4. 결말의 의미가 영상만으로 약할 때

### narration 양

42초 영상 기준:

```text
1~3문장
총 5~12초 이내
```

영상 전체를 설명하지 않는다.

예 TK-001:

```text
3センチなら、簡単だと思ってた。
…そこまで作って、パセリなんだ。
```

또는 완전 무나레이션도 가능.

### 사용자 직접 녹음 방식

사용자가 목소리를 녹음한다면 script pack에:
- Japanese line
- 한국어 뜻
- 권장 시작 time
- 읽는 속도
- 감정

만 제공한다.

Flow에서 dialogue를 생성하지 않는다.

---

# 7. Sound Design

## 기본 원칙

Healing 영상은 audio가 편집 리듬을 만든다.

사용:
- subtle room tone
- light rain / stove hum
- tiny sizzle
- wood scrape
- ceramic click
- soft paw tap
- steam / liquid pour

피함:
- 큰 whoosh
- meme pop sound 반복
- 2초마다 transition SFX
- 과도하게 증폭된 ASMR
- 빠른 EDM/BGM

## Flow-generated audio

full-frame single slow take에서 소리가 깨끗하면 살릴 수 있다.

Timestamp 2-beat / collage처럼 editing flexibility가 중요한 source는 **generated audio를 버리고 후편집 SFX를 사용**한다.

SFX는 작은 reusable library를 만들어 episode마다 다시 생성하지 않는다.

---

# 8. 편집 전환

Healing 기본 transition:

1. action completion cut
2. gentle match cut
3. sound bridge
4. short dissolve (필요 시)

fast swipe/zoom/flash transition은 사용하지 않는다.

가장 좋은 전환 예:

```text
팬의 지글 소리는 계속 유지
→ 화면만 다음 macro angle로 바뀜
```

즉 sound continuity가 visual cut을 부드럽게 만든다.

---

# 9. 최종 권장 포지셔닝

Tiny Cat Kitchen은 `초고속 viral cooking edit`이 아니다.

> **작은 일본 세계에서 고양이가 천천히 한 끼를 완성하는 40초짜리 휴식**

바이럴 장치는 pace가 아니라 다음에서 만든다:
- 첫 1초의 비정상적 크기
- 귀여운 앞발
- 한 가지 조용한 위험
- satisfying food transformation
- 마지막의 작은 감정/개그

즉:

> **Hook은 빠르게 이해시키고, 본문은 천천히 보여준다.**
