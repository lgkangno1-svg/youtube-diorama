# CURRENT STANDARD — Tiny Cat Kitchen

최신 적용 기준: **2026-08-24 Healing H30 + Audience-to-Manifest + Dual-Metric Horizon Gate**

## 1. 현재 최우선 제작 원칙

Tiny Cat Kitchen의 기본 감정은 `viral-chaos`가 아니라 **cozy/healing**이다.

핵심 문장:

> **Hook은 빠르게 이해시키고, 본문은 천천히 보여준다.**

따라서 첫 0.5~1.5초에는 `고양이 앞발 + 말도 안 되게 작은 재료/규칙`을 즉시 보여주되, 이후에는 2초마다 컷을 바꾸지 않는다.

권장 최종 Short:
- 35~45초
- 총 5~7개 visual beat
- 평균 체감 shot duration 4~7초
- action completion cut / sound bridge / gentle match cut 우선
- fast swipe / flash / meme transition 금지

현재 우선 문서:
1. `docs/19_healing_pacing_audio_benchmark.md` — creative direction / H20-H30-H40
2. `docs/17_audience_to_manifest_loop.md` — audience signal → next episode seed
3. `docs/12_dual_metric_horizon_gate.md` — 24h/72h 성과판단
4. `docs/11_engaged_view_truth_layer.md` — engaged-quality 중심 Flow 재투자
5. `docs/10_frame_lock_compatibility_credit_reserve_hype.md` — Flow 기능/호환성
6. `docs/09_resolution_diversity_creator_signature.md` — 원본성 / 결말 다양성

---

## 2. Flow 기본 예산 — H30

현재 첫 파일럿 기본값:

```text
Nano Banana image preflight
→ Veo 3.1 Lite 8s × 3 generations
→ 24s generated motion
→ free keyframe holds / slow push-ins / environmental stills / reaction holds
→ 35~45s final Short
```

비용:
- Non-Ultra: 3 × 10 = **30 credits**
- Ultra: 3 × 5 = **15 credits**

H40은 자동 기본값이 아니다.

### H20
- 2 generations
- premise / trend / hook validation
- 25~32초 편집 후보

### H30 — 기본
- 3 generations
- 24초 실제 motion + 무료 still/editorial hold
- healing/credit 균형점

### H40
- 4 frame-locked generations
- 복잡한 음식 변화나 flagship만
- H30 QC가 명확히 부족할 때만 승격

Google Flow 현재 공식 비용 기준:
- Veo 3.1 Lite: 4/6/8초 모두 non-Ultra 10 / Ultra 5 credits
- Fast: non-Ultra 20 / Ultra 10
- Quality: 8초 100
- 무료 비구독: 하루 50 Flow credits
- 비용은 request가 아니라 generation당 부과
- output count는 항상 1 확인

중요:
- Lite는 First + Last frame 지원
- Fast는 First + Last가 동일한 drop-in upgrade가 아님
- frame continuity가 중요한 컷은 Lite 유지
- 남는 무료 크레딧을 억지로 다 쓰지 않는다

---

## 3. 8초 generation 사용법

8초가 4초와 같은 비용이므로 특별한 이유가 없으면 8초를 사용한다.

하지만 **8초에 4개의 빠른 컷을 강제로 넣지 않는다.**

기본:

```text
8초 = 1 calm action
또는
8초 = 최대 2개의 느린 beat
```

예:

```text
0~2s  앞발이 천천히 들어옴
2~6s  작은 밥을 한두 번 젓음
6~8s  멈춤 + 증기 + 여운
```

Timestamp multi-shot은 기술적으로 가능하지만, healing main footage의 기본값이 아니다. 실험/정보형 영상 또는 B-roll 회수 목적에만 사용한다.

2×2 video collage는 main footage에서 비권장. 이미지 contact sheet는 storyboard/approval 용도로 권장한다.

---

## 4. 오디오 / 나레이션

### 기본값

```text
No narration
No music 또는 거의 들리지 않는 ambient music
Cooking SFX + room tone
```

사용 가능한 핵심 SFX:
- tiny sizzle
- wood scrape
- ceramic click
- soft paw tap
- water pour
- rain / stove hum

Flow native audio가 깨끗한 single slow take라면 살릴 수 있다. 편집 flexibility가 필요한 source는 generated audio를 버리고 reusable SFX library로 교체한다.

### 사용자 나레이션

필수 아님.

다음 조건 중 하나일 때만 1~3문장 사용:
- 화면만으로 story context가 약함
- 캐릭터 성격을 기억시킬 한 줄이 필요함
- 결말의 의미가 영상만으로 약함
- A/B test에서 narration 효용을 검증하려는 경우

42초 기준 총 음성 5~12초 이내. Flow에서 dialogue를 생성하지 않고 후편집에서 사용자가 직접 녹음한다.

---

## 5. 현재 TK-001 실행값

`episodes/TK-001.yaml`은 H30으로 변경됨.

```text
G1 8s: OPEN + PREP
G2 8s: COOK + DANGER
G3 8s: RECOVERY + ASSEMBLY + PAYOFF/RESOLUTION
```

첫 pass:
- 3 Lite generations
- 30 credits non-Ultra / 15 Ultra
- 4 keyframes
- narration none by default
- slow/healing pace

`tools/build_flow_pack.py`와 `tools/build_episode_bundle.py`는 이제 manifest의 scene 수와 budget을 읽으므로 4-generation을 강제하지 않는다.

실행:

```bash
pip install -r tools/requirements.txt
python tools/build_episode_bundle.py episodes/TK-001.yaml
```

이 명령은 LLM/API/Flow를 호출하지 않고:
- originality validation
- Flow pack
- publish pack
- approval bundle

을 생성한다.

---

## 6. 사용자 수동 작업 최소화

사람 승인 지점은 2회만 유지한다.

### Approval A — Production Card
- 일본어 title
- 첫 1초 hook
- 무료 keyframe/contact sheet
- 예상 Flow spend

### Approval B — Final Export
- 첫 1초 시인성
- 고양이/도구/음식 scale continuity
- healing pace 유지
- ending/lore 변화
- AI disclosure / upload metadata

매 scene prompt는 사람이 다시 쓰지 않는다.

---

## 7. Audience-to-Manifest

다음 메뉴를 AI에게 무작정 브레인스토밍시키기 전에 시청자에게 먼저 묻는다.

```text
Poll / Q&A / 구체 댓글
→ audience demand seed
→ originality validation (0 AI tokens)
→ 통과 후보만 Flow spend
```

Poll 승자라도 직전 영상의 goal/conflict/resolution을 그대로 반복하면 폐기한다.

---

## 8. 성과 판단 — 24h와 72h 분리

2026-08-24 이후 public view는 reach 계기판으로 보고, 제작 재투자는 engaged quality로 판단한다.

### 내부 제작 판단
1. Stayed to watch
2. Average percentage viewed
3. Subscribers / 1,000 engaged views
4. Comments / 1,000 engaged views

### 외부 브랜드/협찬
- public views
- 28일/90일 reach
- median reach per Short
- Japan audience share

24h와 72h snapshot은 같은 pool에서 비교하지 않는다.

진단:

```text
STW 약함 + APV 강함 → 첫 0.5~1초만 수정
STW 강함 + APV 약함 → middle pacing/conflict만 수정
둘 다 약함 → 해당 premise에 추가 Flow spend 중단
둘 다 강함 → narration/IP/next episode conversion 실험
```

---

## 9. YPP / AI 원본성 안전

각 episode는 다음이 식별 가능해야 한다.
- unique_goal
- unique_conflict
- unique_ending
- character_motivation
- world_state_change
- callback_or_new_lore

최근 5편과 fingerprint 5개 중 최소 3개를 다르게 유지한다.

YouTube monetization 기준상 동일 캐릭터 시리즈는 가능하지만, AI-generated generic template처럼 보이거나 같은 상황/결말을 반복하는 mass-produced content는 위험하다.

따라서:
- 음식만 바꾸고 같은 사건 복제 금지
- twist 필수 아님
- comedy / proof / emotional / transformation / choice / failure 등 resolution family 순환
- photorealistic synthetic footage는 필요한 altered/synthetic disclosure 사용

---

## 10. 수익화 우선순위

2026 현재:
- Expanded YPP: 500 subscribers + 3M qualified Shorts views/90d 또는 3,000 qualified watch hours
- Full ads/Premium: 1,000 subscribers + 10M qualified Shorts views/90d

2027-02-01 신규 진입:
- 1,000 subscribers + 20M qualified Shorts views/90d 또는 8,000 qualified watch hours

조기 단계부터 준비:
- business contact
- original IP portfolio
- food/gadget 협업 카테고리
- public reach media-kit 데이터
- 실제 Studio에서 활성화된 Creator Partnerships / Shopping / fan funding만 사용

---

## 11. 현재 Loop Engineering

```text
Audience signal / trend / core idea
→ originality validation (0 AI tokens)
→ free image preflight
→ H30: 3 × 8s Lite generations
→ slow editorial holds + reusable ASMR
→ optional 1~3 line user narration only when useful
→ Final Export approval
→ publish
→ 24h / 72h engaged-quality read
→ exact failure stage만 수정
→ H20/H30/H40 중 다음 spend 결정
```

최종 목표:

> **작은 일본 세계에서 고양이가 천천히 한 끼를 완성하는 40초짜리 휴식 — 적은 Flow 크레딧으로 만들고, 시청자 데이터로 다음 편을 결정한다.**
