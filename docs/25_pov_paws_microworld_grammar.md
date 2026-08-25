# 25 — POV Paws Microworld Visual Grammar

목표: Tiny Cat Kitchen Shorts를 **고양이를 구경하는 영상**이 아니라 **내가 고양이가 된 것처럼 두 앞발로 아주 작은 디오라마 음식/물건을 만드는 힐링 영상**으로 고정한다.

이 문서는 Shorts 영상 framing의 source of truth다. 프로필/배너에서는 HERO_CAT_V1 얼굴과 전신을 보여줄 수 있지만, 기본 Shorts에서는 보여주지 않는다.

## POV_PAWS_MICROWORLD_V1

핵심 한 줄:

> **True first-person cat POV + front paws only + absurdly tiny hero object + tactile miniature making + calm ASMR.**

### 반드시 보여야 하는 것

- 카메라는 고양이의 시점에서 아래 작업대를 바라본다.
- 화면 아래쪽에서 `HERO_CAT_V1`의 크림색 + 연한 진저 앞발 1~2개만 자연스럽게 들어온다.
- 고양이 얼굴, 눈, 귀, 머리, 가슴, 몸통, 꼬리는 기본 Shorts에서 보이지 않는다.
- 주인공은 고양이 자체가 아니라 **앞발과 비교했을 때 터무니없이 작은 음식/물건**이다.
- 첫 0.5~1.0초 안에 paw-to-object scale contrast가 읽혀야 한다.
- hero object는 기본적으로 약 5~20mm, 특별한 이유가 있어도 앞발 폭의 절반 이하로 보이게 한다.
- 작은 도자기, 미니 팬, 미니 접시, 나무판, 종이상자 같은 디오라마 소품을 사용한다.
- macro / shallow depth of field로 작은 재료의 질감과 증기, 부스러기, 광택, 눌림을 크게 보여준다.

### 절대 기본값이 아닌 것

다음은 결과가 예쁘더라도 기본 Shorts QC에서 FAIL이다.

- full cat / cat face / head / torso가 화면에 등장
- 카메라가 고양이를 정면에서 보는 third-person chef shot
- 고양이가 카운터 뒤에 서서 요리하는 장면
- 음식이나 팬이 앞발과 비슷하거나 더 크게 보여 miniature scale가 약함
- 일반 크기의 주방을 배경으로 고양이 캐릭터가 주인공처럼 보임
- 사람 손, 손가락, 엄지, 사람형 손바닥
- 고양이 발이 사람처럼 손가락으로 도구를 움켜쥠
- 빠른 montage, 과한 camera orbit, meme zoom

## Paw-action grammar

Veo reliability를 위해 고양이 발은 사람 손처럼 `grip`하지 않는다.

우선 동작:
- nudge — 살짝 밀기
- press — 눌러 모양 잡기
- pat — 톡톡 두드리기
- roll — 작은 재료 굴리기
- steady — 그릇/판을 한쪽 발로 고정하기
- slide — 접시/종이/판을 미끄러뜨리기
- tap — 마지막 장식이나 재료를 가볍게 건드리기

조건부 동작:
- 아주 작은 도구의 넓은 손잡이를 발바닥으로 위에서 눌러 움직이기
- 발 옆면으로 작은 그릇을 기울이기

피할 동작:
- tongs/knife/chopsticks를 손가락처럼 잡기
- 두 발로 정교하게 집어서 회전시키기
- 사람 손목처럼 비틀기
- 매우 작은 음식 자체를 두 발 사이에서 정밀하게 squeeze/pinch하기

## Scale-cuteness gate

귀여움의 핵심은 단순한 `miniature`가 아니라 **비교 가능한 크기 대비**다.

좋은 프레임:

```text
paw width = dominant natural scale reference
hero food/object = 15–50% of visible paw width
tiny cookware = just large enough for hero object
background props = secondary, never larger visual priority than hero object
```

첫 프레임에 가능한 한 다음 중 하나를 포함한다.
- 앞발 바로 옆 8~15mm 음식
- 앞발보다 훨씬 작은 팬/접시
- 쌀알/깨/작은 잎처럼 익숙한 자연 scale cue

텍스트 자, 숫자표, 화면 설명에 의존하지 않는다. **보자마자 작다고 느껴져야 한다.**

## Camera grammar

기본:
- vertical 9:16
- true first-person cat POV
- camera at cat-eye/chest-forward working position, looking slightly downward
- paws enter from bottom left/right edge
- macro close-up
- mostly locked camera
- very subtle breathing drift만 허용
- no cut inside one 8s generation unless unavoidable

세계관 몰입을 위해 카메라를 매 장면 완전히 다른 위치로 순간이동시키지 않는다. G2/G3/G4는 실제 직전 usable frame을 이어서 같은 작업대에 계속 앉아 있는 느낌을 만든다.

## Prop/state continuity gate

Sequential frame chain은 고양이와 카메라뿐 아니라 **소품 상태까지 이어져야 한다.**

기본 규칙:
- G2 이후의 primary cookware/plate/tray는 가능하면 직전 usable frame에 이미 존재해야 한다.
- 새 접시·그릇·도구를 다음 target last frame에 갑자기 추가하지 않는다.
- `G3에는 roasting tray`, `G4에는 이유 없이 새 leaf plate`처럼 바뀌면 **PROP CONTINUITY FAIL**이다.
- 새로운 소품이 꼭 필요하면 이전 generation의 실제 행동으로 먼저 화면에 도입하고, 그 행동 자체가 독립 beat로 가치가 있을 때만 허용한다.
- 단순 서빙용이라면 새 접시를 생성하기보다 기존 tray/board/plate를 그대로 세계관 resolution에 재사용하는 편을 우선한다.

이유:
- First+Last chain에서 갑작스러운 새 소품은 food/cookware morph, duplicate props, scale drift를 유발할 수 있다.
- Tiny Cat Kitchen은 작은 수공예 세계이므로 **같은 소품이 실제로 계속 존재하는 느낌**이 몰입에도 유리하다.

## Runtime grammar — immersion without padding

목표는 60초를 채우는 것이 아니라 **작은 세계에 들어왔다가 만족스럽게 빠져나오는 시간**을 만드는 것이다.

초기 production prior:
- `compact_h30`: 3×8s raw motion → 보통 30~36s final
- `immersive_h40`: 4×8s raw motion → 보통 38~46s final
- 48~60s는 실제 채널 retention 데이터가 지지할 때만 확장

기본적으로 worldbuilding 또는 tactile process가 4개의 독립 beat를 가질 때 `immersive_h40`을 선호한다.

4번째 generation은 **길이 패딩이 아니라 독립적인 의미가 있을 때만** 허용한다.
예:
1. impossible scale reveal
2. tactile making/transformation
3. satisfying finish/reveal
4. quiet world-resolution / tiny serving / paws withdraw / loopable afterglow

4번째 beat를 삭제해도 이야기와 만족감이 똑같다면 H30으로 끝낸다.

## 8초 scene 문법

각 generation:

> 1 primary tactile action + optional 1 micro-payoff

예:

```text
G1: paw approaches a 10mm dough ball → gently presses once
G2: paw rolls the now-flat dough → tiny filling becomes visible
G3: paw taps the final garnish → steam or gloss payoff
G4: paws slide the same tiny serving tray into its diorama serving spot → withdraw, living steam remains
```

## Audio

기본:
- no narration
- no generated music
- close tactile ASMR
- tiny ceramic click
- dry crumb / dough press
- soft sizzle
- paper rustle
- wood scrape
- quiet room tone

소리가 클수록 좋은 것이 아니다. 물체가 아주 작기 때문에 소리도 작고 가까워야 한다.

## Prompt anchor

모든 독립 keyframe / G1에는 다음 의미를 유지한다.

```text
True first-person POV of the cat itself. Only one or two cream-and-pale-ginger feline front paws are visible entering from the bottom edge. Never show the cat's face, eyes, head, ears, torso or full body. The hero food/object is absurdly tiny, usually 5–20mm and clearly much smaller than one paw. Macro miniature diorama workbench, tactile realistic physics, calm healing ASMR. Real feline paws only; no human fingers or thumbs and no human-like gripping.
```

## QC shorthand

- `POV PASS`: 1인칭 + 앞발만 + 초소형 물체가 즉시 읽힘
- `SCALE FAIL`: 물체가 충분히 작아 보이지 않음
- `CHARACTER FAIL`: 얼굴/몸통/전신 노출
- `ANATOMY FAIL`: 사람 손/손가락/그립
- `CAMERA FAIL`: 3인칭 셰프 구도
- `PROP CONTINUITY FAIL`: 직전 장면에 없던 핵심 tray/plate/tool이 이유 없이 생김
- `PADDING FAIL`: 독립 beat 없이 길이만 늘림
