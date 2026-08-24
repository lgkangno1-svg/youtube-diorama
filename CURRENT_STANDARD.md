# CURRENT STANDARD — Tiny Cat Kitchen

최신 적용 기준: **2026-08-24 Progressive Spend H30 + Sequential Frame Chain + Motion-Dense Healing**

## 1. 채널의 기본 감정

Tiny Cat Kitchen은 `viral-chaos`가 아니라 **cozy / healing**이다.

핵심:

> **Hook은 빠르게 이해시키고, 본문은 천천히 보여준다.**

- 첫 0.5~1.5초: 고양이 앞발 + 매우 작은 재료/규칙을 즉시 이해
- 이후: 한 공간에서 느린 행동을 끝까지 보여줌
- 2초마다 컷 전환, flash, meme transition, 과한 zoom 금지
- calm은 static을 뜻하지 않는다. 작은 움직임은 계속 있어야 한다.

권장 최종 길이는 **약 28~36초**를 기본으로 한다. 더 짧아도 완결성이 있으면 허용하고, 40초를 맞추기 위해 정지 keyframe을 길게 패딩하지 않는다.

---

## 2. 기본 Flow 구조 — Progressive Spend H30

현재 공식 Flow 기준 Veo 3.1 Lite는 4/6/8초와 Extend가 generation당 non-Ultra 10 credits / Ultra 5 credits다. 따라서 특별한 이유가 없으면 8초를 쓴다.

### Google AI Pro 비용 진실 — 모델명을 먼저 본다

현재 운영 계정은 Google AI Pro를 기준으로 한다.

공식 Google Flow 기준:
- Google AI Pro 월 기본 Flow credits: **1,000**
- Veo 3.1 Lite 4/6/8초 또는 Extend: **10 credits / generation**
- Veo 3.1 Fast: **20 credits / generation**
- Veo 3.1 Quality 8초: **100 credits / generation**
- Gemini Omni Flash 4초: **15 credits** / 6초 20 / 8초 25 / 10초 30
- Plus/Pro/Ultra의 1080p upscale: **0 credits**

따라서 Flow UI에서 `15 credits`가 보였다는 이유만으로 Veo Lite의 비용을 15로 가정하지 않는다. **반드시 생성 직전 active model + duration + 표시 credit cost를 확인한다.** 현재 H30은 `Veo 3.1 Lite / 8s / output count 1 / 10 credits`가 UI에 실제로 표시될 때만 적용한다.

UI가 공식 문서와 다르면 **UI 표시 비용을 그 생성의 source of truth로 기록하고 일단 생성하지 않은 채 운영 기준을 재검토**한다. 모델이 Gemini Omni Flash 등으로 바뀌어 있으면 Lite로 되돌릴 수 있는지 먼저 확인한다.

기본 최대 first-pass 예산:

```text
Gate A: free image/reference/keyframe preflight = 0
G1: 8s Lite = +10
PASS 후 G2: 8s Lite = +10
PASS 후 G3: 8s Lite = +10
max first pass = 30 credits non-Ultra
```

**G1/G2/G3를 한꺼번에 만들지 않는다.**

- G1이 틀리면 G2/G3 금지
- G2가 틀리면 G3 금지
- minor timing/crop 문제는 편집으로 수리
- 구조적 실패만 해당 generation 1회 reroll 검토
- premise 자체가 약하면 추가 spend 중단

H20은 2개의 8초 Lite로 충분한 단순 episode에 허용한다. H40은 검증된 승자 또는 명확한 1컷 구조적 결함이 있을 때만 허용한다.

---

## 3. Sequential Frame Chain

연속성 기본값:

```text
FREE OPEN FRAME
  ↓
G1 8s
  ↓ save actual last usable frame
G2 First frame
  ↓
G2 8s
  ↓ save actual last usable frame
G3 First frame
  ↓
G3 8s
```

G2/G3에는 무료로 준비한 target last frame을 추가로 사용할 수 있다.

이유:
- 같은 cat / cookware / food state를 실제 직전 프레임에서 이어감
- 새 generation마다 캐릭터를 다시 해석하는 drift 감소
- color/light/scale continuity 개선

현재 Flow 공식 기능상 Veo 3.1 Lite는 First + Last frame을 지원하고, Fast의 First + Last는 아직 동일한 drop-in 대체가 아니다. Extend는 장면상 특별한 이점이 있을 때만 실험하며 기본값은 sequential First+Last chain이다.

---

## 4. 한 8초 generation의 문법

기본:

> **1 clip = 1 calm primary action + optional 1 micro-beat**

좋은 예:

```text
0–1.5s  paw enters slowly
1.5–6s  turns one tiny sweet potato over the heat
6–8s    paw pauses; skin crack/steam continues
```

금지:
- 한 clip 안에서 준비→조리→완성→먹기 전부 수행
- 여러 utensil 동시 사용
- 3~4 camera angle montage
- 서로 무관한 sound event 여러 개 겹치기

---

## 5. 오디오 / 나레이션

기본값:

```text
No narration
No generated music
Quiet room tone + one or two isolated natural ASMR families
```

재사용 SFX:
- tiny paw tap
- pan sizzle
- wooden scrape
- ceramic click
- water pour
- rain ambience
- stove/room tone

Flow 오디오가 깨끗하면 사용한다. 영상은 좋은데 오디오만 이상하면 **영상 재생성 금지**하고 후편집 SFX로 교체한다.

사용자 나레이션은 다음 중 하나일 때만 보통 일본어 0~2문장:
- 화면만으로 규칙/상황 이해가 어려움
- 캐릭터 성격을 한 줄로 강화 가능
- payoff 의미를 한 줄이 크게 증폭

---

## 6. 아이디어 선택 — 조회 가능성 + 제작 안정성

다음 episode는 `ideas/episode_backlog.yaml`의 후보를 기반으로 평가한다.

현재 scoring은 단순 트렌드성만 보지 않고:
- benchmark evidence
- Japan relevance
- healing fit
- visual satisfaction
- **Flow reliability**
- originality
- worldbuilding
- audience demand
- **expected credit efficiency**

를 본다.

Flow reliability와 expected credit efficiency는 근거가 비슷한 후보끼리 비교할 때 특히 중요하다.

현재 2026-08-24 계절 신호:
- 月見 시즌이 실제 일본 외식/식품에서 시작됨
- 9월 3일 グミの日 전후 texture 신제품 집중
- さつまいも / 栗 가을 상품 출시 시작

단, branded menu/plot/design을 복제하지 않고 계절·식감·역할 같은 추상 메커니즘만 사용한다.

현재 저크레딧 관점의 강한 후보는 **한 개의 고구마가 천천히 익고 껍질이 갈라지며 김과 노란 속살이 보이는 焼きいも屋**다. 月見은 계절 인지도가 더 강하지만 계란 취급 + 손님 등장까지 포함하면 continuity risk가 더 높다. 실제 제작 순서는 최근 episode fingerprint와 현재 NEXT_EPISODE 상태를 확인한 뒤 결정한다.

---

## 7. 사용자의 평소 인터페이스

사용자는 원칙적으로 ChatGPT에:

```text
다음 영상 준비해줘.
```

라고만 말하면 된다.

ChatGPT가:
- 최신 benchmark / 일본 신호 확인
- 과거 production + 24h/72h learning 확인
- 후보 선정
- 일본어 title/hook
- narration 필요 여부
- 3개의 느린 8초 action 설계
- episode manifest 생성/수정
- `production/NEXT_EPISODE.txt` 갱신

을 담당한다.

로컬에서는:

```powershell
./tools/make_next_short.ps1
```

을 실행해 bundle / Flow pack / edit plan / publish pack을 만든다. 이 준비 단계는 Flow/LLM/API를 호출하지 않는다.

---

## 8. 성과 학습

실제 데이터가 생기기 전에는 placeholder를 실패 데이터처럼 학습하지 않는다.

매 episode에서 가능한 경우 기록:
- Flow credits spent
- rerolls
- G1/G2/G3 first-pass success
- usable motion seconds
- continuity issue / failed action type
- Flow audio kept/replaced
- narration mode
- final length
- 24h / 72h Stayed to watch
- APV
- engaged views
- subscribers
- comments

장기 최적화 대상:

```text
usable motion / credit
engaged views / credit
subscribers / 100 credits
```

특정 음식이 성공했다고 그 음식을 복제하지 않는다. 성공한 **hook/action/pacing/audio/ending mechanism**만 다음 episode prior로 사용한다.

---

## 9. 원본성 / YPP 안전

각 episode는 다음이 식별 가능해야 한다.
- unique_goal
- unique_conflict
- unique_ending
- character_motivation
- world_state_change
- callback_or_new_lore

최근 5편과 fingerprint 5개 중 최소 3개가 달라야 한다.

음식명만 바꾸고 같은 사건/갈등/결말을 반복하지 않는다. Photorealistic synthetic footage는 필요한 altered/synthetic disclosure를 사용한다.

---

## 10. 현재 Loop Engineering

```text
Fresh benchmark / Japanese signal / audience request
→ candidate scoring with reliability + credit efficiency
→ originality gate
→ free image/reference preflight
→ confirm Flow active model + duration + displayed credit cost
→ G1 8s Lite
→ QC
→ actual end-frame chain
→ G2 only after PASS
→ QC
→ actual end-frame chain
→ G3 only if still needed
→ reusable ASMR / optional short user narration
→ 28–36s motion-dense healing edit
→ publish
→ 24h / 72h engaged-quality + production-cost learning
→ update priors and next candidate
```

최종 목표:

> **가장 싼 영상을 만드는 것이 아니라, 일본 시청자가 오래 보고 다시 찾을 만한 고품질 힐링 영상을 가장 적은 실패 generation으로 만드는 것.**
