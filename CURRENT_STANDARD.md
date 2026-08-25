# CURRENT STANDARD — Tiny Cat Kitchen

최신 적용 기준: **2026-08-25 POV Paws Microworld + Adaptive H30/H40 + Sequential Frame Chain + Seasonal Search Lead**

## 1. 채널의 핵심 경험

Tiny Cat Kitchen의 기본 Shorts는 **고양이를 밖에서 보는 영상이 아니다.**

> **시청자가 고양이가 된 것처럼 1인칭 시점에서 앞발만 보며, 터무니없이 작은 디오라마 음식/물건을 조심스럽게 만드는 힐링 ASMR 영상**이다.

Source of truth:
- character/world: `docs/24_hero_cat_brand_identity.md`
- Shorts camera/scale: `docs/25_pov_paws_microworld_grammar.md`

기본 영상 문법:
- true first-person cat POV
- 화면 아래쪽에 cream + pale ginger 앞발 1~2개만 등장
- 얼굴/눈/귀/머리/몸통/꼬리/full cat 금지
- hero food/object는 앞발보다 압도적으로 작아야 함
- 기본 hero object 약 5~20mm, 화면상 한 앞발 폭의 15~50% 정도
- macro close-up + miniature diorama workbench
- 한 8초 clip에 1 primary tactile action + optional 1 micro-payoff
- no rapid montage / no meme zoom / no third-person chef shot

예쁜 영상이어도 다음이면 FAIL:
- 고양이가 카운터 뒤에서 요리하는 3인칭 구도
- 고양이 얼굴/전신이 보임
- 음식/팬이 앞발과 비슷하거나 더 큼
- 사람 손가락/엄지/사람형 grip
- 주방 전체가 주인공이고 tiny-object scale contrast가 약함

## 2. Paw-action grammar

Veo 안정성을 위해 고양이 발은 사람 손처럼 도구를 움켜쥐지 않는다.

선호:
- nudge
- press
- pat
- roll
- steady
- slide
- tap

조건부:
- 넓은 도구 손잡이를 발바닥으로 위에서 눌러 몇 mm 이동
- 작은 그릇의 옆면을 밀어 기울이기

피함:
- chopsticks / knife / tongs를 손가락처럼 grip
- thumb/index pinch
- 사람 손목처럼 비틀기

## 3. Flow spend — Progressive Spend

현재 운영 계정은 Google AI Pro 기준이다. 생성 직전 Flow UI에서 반드시 확인한다.

```text
active model = Veo 3.1 Lite
duration = 8 seconds
output count = 1
displayed cost = 10 credits / generation
```

UI가 다르면 실제 표시 비용을 source of truth로 기록하고 생성 전에 재검토한다.

모든 generation은 순차 사용한다.

```text
FREE keyframe/reference preflight
→ G1 8s
→ POV/SCALE/ANATOMY/QC
→ save actual last usable frame
→ G2 only after PASS
→ QC
→ G3 only after PASS
→ QC
→ G4 only if runtime gate says it adds an independent beat
```

G2/G3/G4를 미리 생성하지 않는다.

## 4. Runtime policy — 세계관 몰입과 지루함 사이

Shorts가 1분이어야 하는 것은 아니다. 우리 목표는 **길이를 채우는 것보다 작은 세계 안에서 완결된 tactile journey를 느끼게 하는 것**이다.

초기 prior:

### compact_h30
- 3 × 8s Lite = 30 credits first-pass ceiling
- raw motion 24s
- 보통 final 30~36s
- 3개의 독립 beat로 setup → tactile transformation → payoff가 완결될 때

### immersive_h40
- 4 × 8s Lite = 40 credits first-pass ceiling
- raw motion 32s
- 보통 final 38~46s
- 4번째 장면이 독립적인 world-resolution / serving / afterglow / loop beat를 가질 때
- **길이 패딩용 G4 금지**

### 48~60s
- 실제 Tiny Cat Kitchen의 24h/72h retention 및 engaged-views/credit 데이터가 지지할 때만 실험
- 처음부터 60초를 목표로 늘리지 않는다.

현재 worldbuilding 목적의 대표 영상은 `immersive_h40`을 사용할 수 있다. 단, G1→G2→G3까지의 QC gate는 그대로이고 G4도 G3 PASS 후에만 쓴다.

## 5. Immersive beat grammar

좋은 4-beat 구조:

```text
Beat 1 — impossible scale reveal
앞발 옆에 5~20mm 재료/도구가 보여 1초 안에 "너무 작다"가 이해됨

Beat 2 — tactile making
누르기/굴리기/접기/밀기 등 하나의 작은 상태 변화

Beat 3 — satisfying finish
김, 갈라짐, 광택, 단면, 작은 완성품 등 visual payoff

Beat 4 — world resolution
완성품을 미니 서빙 공간에 밀어 넣고 앞발이 빠짐 / 작은 세계가 계속 살아 있음
```

Beat 4를 삭제해도 만족감과 세계관이 동일하면 H30으로 끝낸다.

## 6. Sequential Frame Chain

기본:

```text
G1
↓ actual last usable frame
G2 First frame
↓ actual last usable frame
G3 First frame
↓ actual last usable frame
G4 First frame (only immersive_h40)
```

목적:
- 같은 paw fur pattern
- 같은 first-person camera
- 같은 workbench
- 같은 tiny-object scale
- 같은 food state
- 같은 lighting/material language

G2 이후 긴 full-cat description을 반복하지 않는다. 얼굴이 다시 생길 위험이 있다.

## 7. Audio

기본:

```text
No narration
No generated music
Quiet room tone + close tiny tactile ASMR
```

좋은 소리:
- tiny ceramic click
- wood scrape
- dry crumb / dough press
- soft tiny sizzle
- paper rustle
- faint steam / room ambience

물체가 아주 작으므로 cinematic impact sound를 크게 쓰지 않는다.

영상은 좋고 Flow audio만 이상하면 영상 재생성 금지. 후편집 SFX로 교체한다.

## 8. Seasonal Search Lead

아이디어 base score는 기존 9축을 유지한다.
- benchmark evidence
- Japan relevance
- healing fit
- visual satisfaction
- Flow reliability
- originality
- worldbuilding
- audience demand
- expected credit efficiency

계절 후보에는 최신 일본 근거가 있을 때만 bounded seasonal boost를 추가한다.

```text
peak 36일+ 전   → 0
peak 22~35일 전 → early lead
peak 8~21일 전  → strongest lead
peak 0~7일 전   → strong final lead
peak 기간       → valid but lower than sweet spot
post-peak tail  → small residual
```

정기 loop는 앞으로 2~6주의 일본 시즌/기념일/제철 소재를 선행 스캔한다. 달력 날짜만으로 boost를 주지 않고 `research/seasonal_evidence.yaml` freshness를 확인한다.

## 9. 다음 영상 준비 인터페이스

사용자는:

```text
다음 영상 준비해줘
```

라고만 말하면 된다.

ChatGPT가:
- 일본 최신 시즌/트렌드/벤치마크 조사
- backlog + analytics + production history 비교
- POV_PAWS_MICROWORLD_V1 적합성 평가
- H30 vs H40 runtime gate 선택
- episode manifest 생성/수정
- `production/NEXT_EPISODE.txt` 갱신

사용자는 로컬에서:

```powershell
./tools/make_next_short.ps1
```

을 실행한다.

## 10. 성과 학습

매 episode에서 가능한 경우 기록:
- actual Flow credits
- rerolls
- G1/G2/G3/G4 first-pass success
- POV / scale / anatomy failure
- failed action type
- usable motion seconds
- final runtime
- narration/audio replacement
- 24h/72h Stayed to watch
- APV
- engaged views
- subscribers
- comments

핵심 장기 지표:

```text
usable motion / credit
engaged views / credit
subscribers / 100 credits
```

runtime 학습:
- 30~36s compact_h30
- 38~46s immersive_h40

을 같은 채널에서 비교하고, 실제 drop-off와 engaged-views/credit가 쌓이면 prior를 조정한다.

## 11. 최종 목표

> **고양이 캐릭터를 보여주는 AI 영상이 아니라, 시청자가 고양이의 앞발이 된 듯한 시점에서 믿기 어려울 만큼 작은 음식/물건을 만지며 작은 세계에 잠깐 들어갔다 나오는 힐링 Shorts를 만든다.**
