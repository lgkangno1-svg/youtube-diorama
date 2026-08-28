# 25 — Paws-Only Miniature Making Visual Grammar

목표: Tiny Cat Kitchen Shorts를 **Mini Forest류의 실제 미니어처 요리/공예 영상처럼 보이게 하되, 사람 손만 고양이 앞발로 치환**한다.

이 문서는 Shorts framing의 source of truth다. 파일명과 기존 enum `POV_PAWS_MICROWORLD_V1`은 기존 도구 호환성을 위해 당분간 유지하지만, **`true first-person cat POV`는 더 이상 필수 조건이 아니다.** 최신 의미는 아래 `PAWS_ONLY_MINIATURE_MAKING` 규칙이다.

## 핵심 한 줄

> **Mini Forest-style miniature making shot + only feline front paws instead of human hands + absurdly tiny real-looking food/objects + calm tactile ASMR.**

## 가장 중요한 시각 원리

시청자가 봐야 하는 것은 `고양이 캐릭터`가 아니라 **작은 것을 실제로 만드는 과정**이다.

- 카메라는 miniature workbench를 관찰한다.
- 사람 손이 들어올 자리에서 cream + pale-ginger 고양이 앞발 1~2개만 들어온다.
- 고양이 얼굴/눈/귀/머리/몸통/꼬리/full cat은 보이지 않는다.
- camera가 고양이 눈 위치일 필요는 없다.
- top-down, high-oblique, tabletop macro, side-oblique close-up 모두 허용한다.
- 단, 카메라는 `작은 물체 + 앞발 동작`을 읽기 위한 제작 카메라여야 한다.
- hero object는 보통 5~20mm, 화면상 한 앞발 폭의 15~50% 수준으로 읽혀야 한다.
- 실제 miniature set, real materials, shallow depth of field, realistic food texture/steam/crumb/gloss를 우선한다.

## Mini Forest에서 가져올 추상 메커니즘

복제하지 말고 다음 제작 문법만 추출한다.

1. 실제 손이 작은 재료를 만지는 **hand-centric making composition**
2. 세트와 음식이 장난감처럼 보이지 않는 **real miniature craftsmanship**
3. 만드는 과정을 천천히 따라가는 **process-first pacing**
4. 불, 김, 질감, 부스러기, 윤기, 작은 도자기 소리 같은 **tactile sensory payoff**
5. 고정된 작업 공간에서 이어지는 **world continuity**
6. 인물 연기보다 요리/공예 과정 자체가 주인공인 구조

## 반드시 지킬 것

- feline front paws only
- no cat face/head/body/full-cat reveal
- no human hand/fingers/thumbs
- no human-like feline fingers
- tiny hero object must remain clearly smaller than a paw
- macro miniature workbench
- real miniature-food/material look
- mostly locked or gently observational camera
- one calm primary action + at most one passive micro-payoff per 8s generation
- no rapid montage

## 카메라 허용 범위

### 기본 1순위 — high-oblique maker view

Mini Forest처럼 작업대를 약간 위에서 비스듬히 내려다본다.

```text
camera outside the cat
workbench visible
one or two paws enter frame naturally
hero miniature centered near paw action
```

이 구도가 기본값이다. 시청자는 `고양이가 된 사람`이 아니라 **고양이 앞발이 실제 미니어처를 만드는 장면을 가까이서 보는 관찰자**다.

### 허용 — top-down macro

모양 잡기, 누르기, 장식, 접시 이동 등 위에서 봐야 동작이 명확할 때 사용한다.

### 허용 — side/low oblique macro

증기, 불, 크랙, 늘어남, 굽기처럼 재료 변화가 측면에서 더 잘 보일 때 사용한다.

### 조건부 — first-person-like angle

결과가 자연스럽고 손동작이 잘 읽힐 때만 사용할 수 있다. 더 이상 채널 정체성의 필수 조건은 아니다.

## FAIL 구도

결과가 예뻐도 다음이면 구조적 FAIL이다.

- full cat / cat face / head / torso가 등장
- 고양이가 카운터 뒤에서 사람처럼 요리하는 캐릭터 연기
- AI 고양이 일상극/직업극이 메인 콘텐츠가 됨
- 사람 손이 등장
- 앞발에 손가락/엄지 같은 구조가 생김
- 앞발이 칼/젓가락/집게를 사람처럼 움켜쥠
- 음식/팬이 paw와 비슷하거나 더 커서 miniature contrast가 약함
- 거대한 주방 establishing shot 때문에 making action이 작게 보임
- 빠른 montage / meme zoom / 과한 orbit

## Paw-action grammar

고양이 발 구조에서 자연스러운 동작을 우선한다.

선호:
- nudge
- press
- pat
- roll
- steady
- slide
- tap
- push

조건부:
- 넓은 도구 표면을 발바닥으로 눌러 밀기
- 발 옆면으로 작은 그릇/트레이 방향 조정

피함:
- thumb-index pinch
- chopsticks/tongs/knife grip
- 정교한 손목 비틀기
- 사람 손처럼 재료를 집어 들어 회전시키기

중요: Mini Forest에서 사람 손으로 가능한 동작을 그대로 고양이 발에 복사하지 않는다. **동작의 목적은 유지하되 feline-safe 동작으로 재설계**한다.

## Scale-cuteness gate

귀여움은 고양이 얼굴이 아니라 **paw-to-object scale contrast**에서 나온다.

```text
visible paw width = natural size reference
hero food/object = normally 15–50% of paw width
mini cookware = only large enough for hero object
background props = secondary
```

첫 1초 안에 `엄청 작다`가 읽혀야 한다.

## Prop/state continuity

- 같은 작업대, 조명, tray/pan/board를 가능한 한 계속 유지한다.
- 다음 장면 target frame에 핵심 도구를 갑자기 생성하지 않는다.
- 새 소품이 필요하면 이전 장면에서 자연스럽게 등장시킬 이유가 있어야 한다.
- serving beat도 가능하면 기존 tray/board를 재사용한다.

## 8초 scene grammar

> **1 calm tactile primary action + optional 1 passive material payoff**

예:

```text
G1: paw gently pushes a tiny tray toward heat
G2: paw steadies tray → skin slowly cracks
G3: paw slides tray away → steam and golden center reveal
G4: paw slides same tray into tiny serving position → withdraw
```

## Runtime

H30/H40 숫자는 현재 first-pass credit tier다.

- `compact_h30`: 3×8s raw = 24s, 보통 final 24~27s
- `immersive_h40`: 4×8s raw = 32s, 보통 final 32~35s
- G4는 독립적인 serving/world-resolution 가치가 있을 때만
- 긴 영상이 필요하다는 이유로 still/loop/padding 금지

## Audio

기본:
- no narration
- no generated music
- quiet close ASMR
- tiny ceramic click
- paper/wood scrape
- tiny sizzle
- steam / crust / crumb texture

소리도 miniature scale에 맞게 작고 가까워야 한다.

## Prompt anchor

독립 keyframe/G1의 핵심 문장:

```text
A realistic Mini Forest-style miniature making shot. The camera observes a tiny handcrafted workbench from a high-oblique or macro tabletop angle. Only one or two cream-and-pale-ginger real feline front paws enter the frame where human hands normally would. Never show the cat's face, head, torso or full body. The hero food/object is absurdly tiny, usually 5–20mm and clearly much smaller than one paw. Real miniature materials, tactile realistic physics, calm process-first pacing, shallow depth of field, healing close ASMR. No human hands, fingers or thumbs; no human-like gripping.
```

## QC shorthand

- `MAKER VIEW PASS`: hand-centric miniature making composition is clear
- `SCALE FAIL`: hero object is not dramatically smaller than paw
- `CHARACTER FAIL`: face/head/body/full cat appears
- `ANATOMY FAIL`: fingers/thumbs/human hand or grip
- `CAMERA FAIL`: character-performance shot replaces miniature-making shot
- `PROP CONTINUITY FAIL`: key prop appears/disappears without action
- `PADDING FAIL`: extra generation adds duration without independent making/payoff value

## 최종 정체성

> **Tiny Cat Kitchen은 AI 고양이 캐릭터 영상이 아니다. Mini Forest처럼 아주 작은 것을 실제로 만드는 힐링 미니어처 영상이며, 사람 손 대신 고양이 앞발만 등장한다.**
