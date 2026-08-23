# CURRENT STANDARD — Tiny Cat Kitchen

최신 적용 기준: **2026-08-24 Frame-Lock Compatibility + Credit Reserve Loop**

실제 제작 시 우선순위:

1. `docs/10_frame_lock_compatibility_credit_reserve_hype.md` — **현재 최우선 기준**
2. `docs/09_resolution_diversity_creator_signature.md` — 결말 다양성 + creator signature
3. `docs/08_frame_lock_trend_injection_factory.md` — Frame-Lock + Trend Injection 기준
4. `tools/build_flow_pack.py` — episode YAML에서 Flow prompt pack 자동 생성
5. `tools/validate_episode_originality.py` — AI token 없이 원본성 사전 검증
6. `episodes/TK-001.yaml` — 첫 파일럿 / comedy resolution
7. `episodes/TK-002.yaml` — 숫자 제약 / proof resolution
8. `episodes/TK-003.yaml` — 세계관 스토리 / emotional resolution
9. `docs/07_4gen_exploration_and_ip_moat.md` — 4-generation 비용 기준 참고
10. `docs/06_zero_waste_flow_factory.md` — 5-generation 승격형 참고
11. `docs/02_google_flow_scene_prompts.md` — 장면 연출 라이브러리 참고

## 현재 비용 원칙

초기 탐색 영상:

> Nano Banana 2 Lite 5-keyframe preflight → Veo 3.1 Lite **4 Start+End-frame locked generations** → 35~38초 편집

- Non-Ultra: 40 Flow credits
- Ultra: 20 Flow credits
- output count: 1
- 5개 keyframe: OPEN / CONSTRAINT / DANGER / PAYOFF / RESOLUTION
- G1~G4는 인접 keyframe을 First + Last frame으로 고정
- CTA/loop용 별도 video generation 금지
- 5번째 generation은 승자 포맷 또는 구조적 실패 1컷에만 허용
- Quality는 frame-lock 파이프라인의 drop-in upgrade로 간주하지 않음
- 이미지 preflight는 `Nano Banana 2 Lite`를 명시적으로 확인
- Gemini Omni Flash video edit(40 credits)는 **4회 이상의 Lite reroll을 대체하거나 고유 편집 기능이 꼭 필요할 때만** 사용

### 중요: First + Last frame 호환성

2026-08-24 Google Flow 공식 모델 표 기준:

- Veo 3.1 Lite: First + Last frame 지원 (4s / 6s / 8s)
- Veo 3.1 Fast: First + Last frame은 `Coming soon`
- 따라서 현재 frame-locked 컷을 Fast로 바꾸는 것은 **동일한 제작 모드의 품질 승격이 아니다.**

실패 컷 처리 순서:

```text
minor defect
→ editor fix / crop / freeze / keyframe cutaway

frame-locked structural defect
→ Veo 3.1 Lite로 해당 G컷만 1회 reroll

Lite가 반복 실패하지만 endpoint lock이 중요
→ prompt/action 단순화 + keyframe 수정 후 Lite reroll

Fast/Quality 사용
→ frame lock을 포기해도 되는 별도 hero insert / first-frame-only shot / reference shot에서만 검토
```

핵심은 40 credits보다 더 싸게 보이게 만드는 것이 아니라 **reroll을 줄여 실제 총비용을 낮추면서 endpoint continuity를 유지하는 것**이다.

## 무료 계정 50-credit reserve rule

구독이 없는 Flow 계정은 현재 하루 50 무료 크레딧을 받고, 첫 generation이 그날의 refresh cycle을 트리거한다. 남은 무료 크레딧은 이월되지 않는다.

따라서 무료 계정에서는:

```text
G1~G4 Lite = 40 credits
남은 10 credits = contingency reserve
```

- 10크레딧을 처음부터 5번째 장면에 쓰지 않는다.
- 최종 QC 후 가장 치명적인 실패 컷 한 개에만 사용한다.
- 네 컷이 모두 usable이면 10크레딧은 억지로 소진하지 않는다.
- 다음날 새 50-credit cycle에서 다음 episode를 시작한다.

이 구조는 `하루 1편 초안 + 실패 1회 보험`으로 이해한다.

## 현재 자동화 원칙

사람이 매 scene prompt를 직접 작성하지 않는다.

```bash
pip install -r tools/requirements.txt
python tools/validate_episode_originality.py episodes/TK-003.yaml
python tools/build_flow_pack.py episodes/TK-001.yaml
```

그러면 원본성을 먼저 무료로 검사하고 `generated/TK-001_flow_pack.md`를 생성한다.

사람 승인 지점은 실질적으로 **2회 묶음 승인**으로 줄인다.

### Approval A — Production Card
한 화면에서 한 번에 확인:
1. 일본어 title
2. 첫 3초 hook
3. 5-keyframe contact sheet
4. 4-generation 예상 budget

### Approval B — Final Export
1. 첫 0.5초 시인성
2. 고양이/도구 연속성
3. creator signature
4. 결말/루프
5. 업로드 여부

중간 scene prompt 문장은 사람이 승인하지 않는 것을 기본값으로 한다.

## 현재 성장 원칙

첫 3편은 서로 다른 가설과 서로 다른 결말 기능을 검증한다.

- TK-001: 캐릭터 + 미니요리 / `comedy_twist`
- TK-002: 숫자 제약 훅 / `proof_resolution`
- TK-003: 감성 세계관 / `emotional_resolution`

그 다음부터 게시 비율 기본값:

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

30편을 먼저 생산하지 않는다.

## 현재 원본성 원칙

각 episode는 기존 6개 항목이 식별 가능해야 한다.

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
- `creator_signature.narrator_angle` + `creator_signature.signature_line`을 필수로 둔다.
- 같은 컷 순서와 같은 결말에 음식만 교체하는 방식은 금지한다.

## 현재 AI 표시/레이아웃 원칙

포토리얼 AI 영상은 YouTube Studio AI use disclosure를 기본 `Yes`로 처리한다.

- 첫 0.5초 핵심 물체는 중앙 60% 안에 둔다.
- 화면 최상단 가장자리에만 핵심 정보를 두지 않는다.
- 숫자 제약은 실제 물체 + 후편집 VO/caption으로 중복 전달한다.

AI 공개 자체는 추천이나 수익화 자격을 제한하지 않는다고 YouTube가 명시한다.

## 현재 수익화 우선순위

### Phase 0 — YPP 이전
- business contact 공개
- original IP portfolio 축적
- 브랜드가 바로 이해할 수 있는 `tiny kitchen / food / gadget` 카테고리 정리
- 광고수익을 기다리지 말고 직접 협업 가능성을 준비

### Phase 1 — Expanded YPP
현재 기준: 500 subscribers + 최근 90일 valid public uploads 3개 + 3M qualified Shorts views(90일) 또는 3,000 qualified watch hours.

우선 활용:
- memberships / Super Thanks 등 fan funding 자격 확인
- own-product Shopping 등 실제 Studio에서 활성화된 기능 확인
- **Hype**: YPP에 들어온 500~500,000 subscriber 채널은 지원 지역에서 신작 공개 후 7일 동안 Hype discovery를 활용할 수 있으므로, 팬에게 일반적인 `좋아요` 대신 중요한 신작에서 Hype를 안내하는 실험 가능

### Phase 2 — Full Shorts ads/Premium
2026 현재: 1,000 subscribers + 10M qualified Shorts views / 90 days.

2027-02-01부터 신규 진입 기준은 1,000 subscribers + 20M qualified Shorts views / 90 days로 변경 예정.

### Shopping 주의
`500명 = 다른 브랜드 상품 affiliate 자동 개방`으로 가정하지 않는다.

- Expanded YPP의 조기 Shopping 설명은 own merchandise/store 중심이다.
- 다른 브랜드 상품 태깅/affiliate는 별도 Shopping Affiliate eligibility 및 국가/파일럿 조건을 적용한다.
- 한국·일본은 현재 지원 국가 목록에 포함되지만 Studio에서 실제 자격/초대 상태를 확인한 뒤 운영한다.

브랜드 수익은 YouTube 내부 기능만 기다리지 않고 `business contact + original IP portfolio`를 병행한다.
