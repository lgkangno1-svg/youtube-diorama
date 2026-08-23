# CURRENT STANDARD — Tiny Cat Kitchen

최신 적용 기준: **2026-08-24 Engaged-View Truth Layer + Frame-Lock Credit Reserve**

실제 제작 시 우선순위:

1. `docs/11_engaged_view_truth_layer.md` — **현재 최우선 성과판단 기준**
2. `docs/10_frame_lock_compatibility_credit_reserve_hype.md` — 현재 Flow 제작/비용 기준
3. `docs/09_resolution_diversity_creator_signature.md` — 결말 다양성 + creator signature
4. `docs/08_frame_lock_trend_injection_factory.md` — Frame-Lock + Trend Injection
5. `tools/build_flow_pack.py` — episode YAML → Flow prompt pack
6. `tools/validate_episode_originality.py` — AI token 없이 원본성 사전 검증
7. `tools/score_shorts_experiments.py` — YouTube Studio 수치 → 무료 상대평가/진단
8. `analytics/shorts_metrics.csv` — 최소 수동입력 템플릿
9. `episodes/TK-001.yaml` — 첫 파일럿 / comedy resolution
10. `episodes/TK-002.yaml` — 숫자 제약 / proof resolution
11. `episodes/TK-003.yaml` — 세계관 스토리 / emotional resolution

---

## 1. 2026-08-24 이후 성과 판단 원칙 — 중요

YouTube는 2026-08-24부터 Shorts를 포함한 모든 영상에서 **재생 시작 시점부터 public view를 카운트**한다.

하지만 공식 정책상:

- YPP Shorts 수익은 `engaged views` 기반
- YPP 자격은 `qualified Shorts views` 기반
- `Engaged views` = 초기 몇 초를 넘겨 계속 본 Shorts 횟수, loop 제외
- `Stayed to watch` = 초기 몇 초를 넘겨 본 비율 vs swipe-away
- Average view duration / average percentage viewed는 engaged views 기반

따라서 **public views를 승자선정 KPI 1순위로 사용하지 않는다.**

현재 4대 KPI:

1. `Stayed to watch (%)`
2. `Average percentage viewed (%)`
3. `Engaged views`
4. `Subscribers gained per 1,000 engaged views`

2026-08-24 이전 public views와 이후 public views를 raw 숫자 하나로 직접 비교하지 않는다.

### 진단 → Flow 비용 연결

```text
Stayed to watch 약함 + APV 강함
→ OPEN/첫 0.5~1초만 수정
→ 전체 Flow 4컷 reroll 금지

Stayed to watch 강함 + APV 약함
→ DANGER/PAYOFF 구간만 수정

둘 다 강함 + 구독 전환 약함
→ creator signature / lore / callback 강화

둘 다 약함
→ 해당 가설에 추가 Flow credit 지출 중단
```

Studio 데이터 입력 후:

```bash
python tools/score_shorts_experiments.py analytics/shorts_metrics.csv
```

절대적인 외부 채널 임계값 대신 **같은 채널, 비슷한 길이, 최근 cohort 내 상대 순위**로 판단한다.

---

## 2. 현재 Flow 비용 원칙

초기 탐색 영상:

> Nano Banana 2 Lite 5-keyframe preflight → Veo 3.1 Lite **4 Start+End-frame locked generations** → 35~38초 편집

- Non-Ultra: 40 Flow credits
- Ultra: 20 Flow credits
- output count: 1
- 5 keyframes: OPEN / CONSTRAINT / DANGER / PAYOFF / RESOLUTION
- G1~G4는 인접 keyframe을 First + Last frame으로 고정
- CTA/loop용 별도 video generation 금지
- 5번째 generation은 구조적 실패 1컷 또는 승자 포맷에만 허용
- Quality를 frame-lock 파이프라인의 drop-in upgrade로 보지 않음
- 무료 이미지 preflight에서는 `Nano Banana 2 Lite`를 명시적으로 확인
- Gemini Omni Flash video edit(40 credits)는 4회 이상의 Lite reroll을 대체하거나 고유 편집 기능이 꼭 필요할 때만 검토

### First + Last frame 호환성

2026-08-24 Google Flow 공식 모델 표 기준:

- Veo 3.1 Lite: First + Last frame 지원 (4s / 6s / 8s)
- Veo 3.1 Fast: First + Last frame은 `Coming soon`

따라서 frame-locked 컷은 Lite를 유지한다.

실패 컷 처리 순서:

```text
minor defect
→ editor fix / crop / freeze / keyframe cutaway

frame-locked structural defect
→ Veo 3.1 Lite로 해당 G컷만 1회 reroll

Lite가 반복 실패 + endpoint lock 중요
→ action 단순화 + keyframe 수정 후 Lite reroll

Fast/Quality
→ frame lock을 포기해도 되는 별도 hero insert에서만 검토
```

---

## 3. 무료 계정 50-credit reserve rule

Flow 비구독 사용자는 현재 하루 50 무료 크레딧을 받으며 첫 generation이 refresh cycle을 시작한다. 미사용분은 이월되지 않는다.

```text
G1~G4 Lite = 40 credits
남은 10 credits = contingency reserve
```

- 10크레딧을 처음부터 5번째 장면에 사용하지 않는다.
- 최종 QC 후 가장 치명적인 실패 컷 한 개에만 사용한다.
- 네 컷이 모두 usable이면 억지로 소진하지 않는다.

목표: `하루 1편 초안 + 실패 1회 보험`.

---

## 4. 최소 수동 작업 원칙

사람이 매 scene prompt를 직접 작성하지 않는다.

```bash
pip install -r tools/requirements.txt
python tools/validate_episode_originality.py episodes/TK-003.yaml
python tools/build_flow_pack.py episodes/TK-001.yaml
```

사람 승인 지점은 2회 묶음 승인만 유지한다.

### Approval A — Production Card
한 화면에서:
1. 일본어 title
2. 첫 3초 hook
3. 5-keyframe contact sheet
4. 4-generation 예상 budget

### Approval B — Final Export
1. 첫 0.5초 시인성
2. 고양이/도구 연속성
3. creator signature
4. 결말/세계관 변화
5. 업로드 여부

게시 후에는 24h/72h Studio 수치만 `analytics/shorts_metrics.csv`에 입력한다.

---

## 5. 성장 원칙

첫 3편은 서로 다른 가설과 결말 기능을 검증한다.

- TK-001: 캐릭터 + 미니요리 / `comedy_twist`
- TK-002: 숫자 제약 훅 / `proof_resolution`
- TK-003: 감성 세계관 / `emotional_resolution`

그 다음 기본 편성:

```text
CORE IP / 숫자 도전
→ CORE IP / 생활 세계관
→ TREND INJECTION / 최근 7~30일 일본 음식·계절·생활 트렌드
→ 반복
```

Trend slot은 음식에 한정하지 않는다.

- food trend
- seasonal/cultural moment
- character lifestyle situation

30편을 먼저 생산하지 않는다. **데이터가 확인된 가설만 확장한다.**

### 최근 경쟁군에서 유지할 교훈

- Miniature Cooking Ideas는 2026년 8월에도 높은 업로드 빈도와 큰 일일 조회를 유지하지만 최근 개별 업로드 성과 편차가 크다.
- 일본의 오래된 Miniature Cooking 채널은 2024년 이후 신규 업로드가 멈춰 최근 성장도 정체되어 있다.

따라서 `대량 업로드` 자체가 moat가 아니다.

우리의 moat:

> miniature satisfaction + cat IP + unique conflict + accumulating world state + low-credit iteration

---

## 6. 원본성 원칙

각 episode는 아래 6개가 식별 가능해야 한다.

- unique_goal
- unique_conflict
- unique_ending
- character_motivation
- world_state_change
- callback_or_new_lore

그리고 `episode_fingerprint` 5개를 유지한다.

- hook_mechanic
- dominant_visual
- conflict_mechanic
- emotional_turn
- ending_mechanic

신규 에피소드는 직전 5편과 비교해 fingerprint 5개 중 최소 3개가 달라야 한다.

추가 규칙:

- `twist`는 필수가 아니다.
- 모든 영상은 `KF4_RESOLUTION`을 가진다.
- 최근 5편 안에서 같은 resolution family를 3회 이상 사용하지 않는다.
- `creator_signature.narrator_angle` + `creator_signature.signature_line` 필수.
- 같은 컷 순서와 같은 결말에 음식만 교체하는 방식 금지.

YouTube의 `inauthentic content` 정책 때문에 반복/대량생산처럼 보이는 AI template을 피한다.

---

## 7. AI 표시 / 레이아웃

포토리얼 AI 영상은 YouTube Studio altered/synthetic content disclosure를 기본 `Yes`로 처리한다.

- 첫 0.5초 핵심 물체는 중앙 60% 안에 둔다.
- 화면 최상단 가장자리에만 핵심 정보를 두지 않는다.
- 숫자 제약은 실제 물체 + 후편집 VO/caption으로 중복 전달한다.

AI 공개 자체는 추천이나 수익화 자격을 제한하지 않는다고 YouTube가 명시한다.

---

## 8. 수익화 우선순위

### Phase 0 — YPP 이전

- business contact 공개
- original IP portfolio 축적
- 브랜드가 즉시 이해할 수 있는 `tiny kitchen / food / gadget` 카테고리 정리
- 광고수익을 기다리지 않고 직접 협업 가능성을 준비

### Phase 1 — Expanded YPP

현재 조기 기능 기준:

- 500 subscribers
- 최근 90일 valid public uploads 3개
- 3M qualified Shorts views / 90 days 또는 3,000 qualified watch hours

우선 활용:

- fan funding 자격 확인
- Creator Partnerships
- 실제 Studio에서 활성화된 Shopping 기능
- 지원 지역에서는 중요한 신작에 Hype discovery 실험

### Phase 2 — Full Shorts ads/Premium

2026 현재 신규 진입:

- 1,000 subscribers
- 10M qualified Shorts views / 90 days

2027-02-01부터 신규 진입:

- 1,000 subscribers
- 20M qualified Shorts views / 90 days

### 2027 Shorts 수익 유지에 대한 추가 주의

YouTube가 2026-08-10 발표한 2027 업데이트에 따르면, **2027-02-01부터 Shorts Creator Pool에서 매월 수익을 얻으려면 최근 90일 10M qualified Shorts views를 유지해야 한다.** 이를 놓쳐도 YPP에서 바로 퇴출되는 것은 아니며 다른 YPP 수익에는 직접 영향이 없다고 안내한다.

따라서 장기 목표는 단순 `YPP 입성`이 아니라:

> 500/3M 조기 수익기능 → 1,000/10M 2026 광고 진입 → 반복 가능한 90일 qualified-view 엔진

이다.

또 2027에는 일부 신규 Shorts incentive, Shopping bonus, brand-deal production credits, targeted Shorts ads가 도입될 예정이므로 **브랜드가 안전하게 사용할 수 있는 original character IP + food/gadget format**을 계속 구축한다.

### Shopping 주의

`500명 = 타 브랜드 affiliate 자동 개방`으로 가정하지 않는다.

- Shopping Affiliate는 YPP 가입, subscriber threshold, 지원 국가, audience not Made for Kids 등 별도 조건 적용
- 한국과 일본은 현재 지원 국가지만 Studio의 실제 자격 상태를 기준으로 한다.

---

## 9. 최종 운영 루프

```text
Idea
→ originality validation (0 AI tokens)
→ 5 free keyframes
→ 4 Lite frame-locked generations
→ human Final Export approval
→ publish
→ 24h analytics truth layer
→ 72h cohort comparison
→ diagnose exact failure stage
→ spend credits only on that stage or abandon hypothesis
```

핵심 문장:

> **우리는 public view를 최대화하는 공장이 아니라, 적은 크레딧으로 engaged/qualified view와 재방문을 만드는 IP를 학습하는 시스템을 만든다.**
