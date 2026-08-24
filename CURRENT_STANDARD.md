# CURRENT STANDARD — Tiny Cat Kitchen

최신 적용 기준: **2026-08-24 Audience-to-Manifest + Dual-Metric Horizon Gate + Frame-Lock Credit Reserve**

실제 제작 시 우선순위:

1. `docs/17_audience_to_manifest_loop.md` — **시청자 반응 → 다음 episode seed / 아이디어 토큰·Flow 낭비 절감**
2. `docs/12_dual_metric_horizon_gate.md` — 현재 최우선 성과판단/브랜드 세일즈 기준
3. `docs/11_engaged_view_truth_layer.md` — engaged-view 중심 내부 최적화
4. `docs/10_frame_lock_compatibility_credit_reserve_hype.md` — Flow 제작/비용 기준
5. `docs/09_resolution_diversity_creator_signature.md` — 결말 다양성 + creator signature
6. `docs/08_frame_lock_trend_injection_factory.md` — Frame-Lock + Trend Injection
7. `tools/build_episode_bundle.py` — originality → Flow pack → publish pack 1-command 준비
8. `tools/build_publish_pack.py` — metadata + Poll/Q&A/Video Reply 지시 자동 생성
9. `tools/validate_episode_originality.py` — AI token 없이 원본성 사전 검증
10. `tools/score_shorts_experiments_v2.py` — 24h/72h horizon-aware 성과평가
11. `analytics/shorts_metrics_v2.csv` — 24h/72h 입력 템플릿
12. `episodes/TK-001.yaml` — 첫 파일럿 / comedy resolution / Poll
13. `episodes/TK-002.yaml` — 숫자 제약 / proof resolution / Q&A
14. `episodes/TK-003.yaml` — 세계관 스토리 / emotional resolution / Video Reply

---

## 1. 새 기본값 — 다음 메뉴를 AI보다 시청자에게 먼저 묻는다

2026-07-07 YouTube 공식 블로그는 Shorts에서 Poll Sticker, Q&A Sticker, Add Yours, Video Replies를 단순 조회수를 팬으로 전환하는 방법으로 권장했다.

따라서 다음 아이디어 생성 기본 순서는:

```text
Poll / Q&A / 구체 댓글
→ 실제 audience demand가 있는 idea seed
→ originality validation (0 LLM tokens)
→ 통과한 후보만 Flow spend
```

첫 3편 interaction rotation:

- TK-001: Poll — `次に3cmで作るなら？ ラーメン / 寿司`
- TK-002: Q&A — `10粒だけで作ってほしい料理は？`
- TK-003: Video Reply — 새로운 손님/메뉴와 사건을 만드는 구체 댓글만 후보

규칙:
- 한 episode에 primary interaction mechanic은 1개만 사용
- Poll 승자나 댓글 요청은 자동 제작하지 않음
- 직전 영상의 goal/conflict/resolution을 바꾸지 못하면 폐기
- generic like/subscribe CTA보다 실제 다음 콘텐츠 결정에 참여시키는 CTA 우선

목표는 아이디어 LLM 토큰을 줄이는 것뿐 아니라 **수요 없는 premise에 40 Flow credits를 쓰는 확률을 낮추는 것**이다.

---

## 2. 2026-08-24 이후 조회수는 두 개의 계기판으로 본다

YouTube는 2026-08-24부터 모든 포맷에서 **영상이 재생되기 시작하는 순간 public view를 카운트**한다.

하지만:
- YPP Shorts 수익은 `engaged views` 기반
- YPP 자격은 `qualified Shorts views` 기반
- `Engaged views` = 초기 몇 초를 넘겨 계속 본 횟수
- `Stayed to watch` = 초기 몇 초를 넘겨 본 비율 vs swipe-away
- APV는 engaged viewers 기반

### Internal Quality Dashboard — Flow 재투자 판단

1. Stayed to watch
2. Average percentage viewed
3. Subscribers per 1,000 engaged views
4. Comments per 1,000 engaged views
5. Audience-loop responses per 1,000 engaged views when available

`raw public views`와 `raw engaged views`는 품질 score에 넣지 않는다.

### External Reach Dashboard — 브랜드/협찬 세일즈

- public views
- 28일/90일 public reach
- median public views per Short
- top public-view Short
- Japan audience share / age bands when available

핵심:

> **제작은 engaged quality로 최적화하고, 협찬은 public reach로 판매한다.**

---

## 3. Observation Horizon Gate

24시간 snapshot과 72시간 snapshot을 같은 percentile pool에서 비교하지 않는다.

- 24h cohort → 첫 훅/리텐션 빠른 진단
- 72h cohort → 소재, IP, 구독 전환 판단
- 모든 analytics row에 `observation_hours` 필수
- 같은 episode의 24h/72h snapshot은 별도 row로 저장

실행:

```bash
python tools/score_shorts_experiments_v2.py analytics/shorts_metrics_v2.csv
```

v2 quality score:

```text
35% Stayed to watch percentile
35% APV percentile
20% subscribers / 1,000 engaged percentile
10% comments / 1,000 engaged percentile
```

절대적인 외부 채널 임계값 대신 **같은 채널 + 같은 관측시간 + 최근 cohort 상대평가**를 사용한다.

---

## 4. 진단 → Flow 비용 연결

```text
STW 약함 + APV 강함
→ OPEN/첫 0.5~1초만 수정
→ 전체 Flow 4컷 reroll 금지

STW 강함 + APV 약함
→ DANGER/PAYOFF 구간만 수정

STW/APV 강함 + 구독 전환 약함
→ creator signature / lore / audience interaction 강화

STW/APV 모두 약함
→ 해당 가설에 추가 Flow credit 지출 중단

public reach 높음 + quality 낮음
→ 브랜드 reach 사례로는 보관
→ 제작 포맷 승자로 지정하지 않음
```

---

## 5. 현재 Flow 비용/기능 원칙

초기 탐색 영상:

> Nano Banana 2 Lite 5-keyframe preflight → Veo 3.1 Lite **4 Start+End-frame locked generations** → 35~38초 편집

공식 Google Flow 기준 재확인:
- Veo 3.1 Lite: 4/6/8초, 비-Ultra 10 credits / Ultra 5 credits
- Veo 3.1 Fast: 비-Ultra 20 / Ultra 10
- Veo 3.1 Quality: 8초 100 credits
- Gemini Omni Flash: 4초 15 / 6초 20 / 8초 25 / 10초 30 credits
- Gemini Omni Flash video edit: 40 credits
- First + Last frame: Lite 지원, Fast는 아직 `Coming soon`
- Ingredients/References: Lite/Fast 8초만 지원
- Extend: Lite/Fast 지원
- 무료 비구독: 하루 50 Flow credits
- 비용은 request가 아니라 generation당 부과
- Nano Banana 2 Lite: 무료 기본 이미지 모델
- 유료 Plus/Pro/Ultra: 1080p upscale 0 credits

현재 budget:

```text
G1~G4 Lite = 40 credits (non-Ultra) / 20 credits (Ultra)
남은 무료 10 credits = contingency reserve
```

규칙:
- output count = 1
- 5번째 generation은 처음부터 쓰지 않음
- 구조적 실패 1컷 또는 검증된 승자 포맷에만 추가 generation 허용
- frame-locked 컷은 Lite 유지
- Fast/Quality는 endpoint lock을 포기해도 되는 별도 Hero insert에서만 검토
- Gemini Omni Flash edit 40 credits는 여러 Lite reroll을 대체할 명확한 이유가 있을 때만 검토

---

## 6. 최소 수동 작업

사람이 매 scene prompt나 upload metadata를 직접 쓰지 않는다.

```bash
pip install -r tools/requirements.txt
python tools/build_episode_bundle.py episodes/TK-001.yaml
```

bundle은 자동으로:
- originality validation
- Flow prompt pack
- YouTube publish pack
- episode별 Poll/Q&A/Video Reply 지시

를 만든다.

사람 승인 지점은 2회만 유지한다.

### Approval A — Production Card
- 일본어 title
- 첫 3초 hook
- 5-keyframe contact sheet
- 4-generation 예상 budget

### Approval B — Final Export
- 첫 0.5초 시인성
- 고양이/도구 연속성
- creator signature
- 결말/세계관 변화
- episode별 audience interaction 1개
- 업로드 여부

게시 후에는 24h/72h Studio 수치만 `analytics/shorts_metrics_v2.csv`에 기록한다.

---

## 7. 성장 편성

첫 3편은 서로 다른 가설과 상호작용 메커니즘을 검증한다.

- TK-001: 캐릭터 + 미니요리 / comedy resolution / Poll
- TK-002: 숫자 제약 훅 / proof resolution / Q&A
- TK-003: 감성 세계관 / emotional resolution / Video Reply candidate

이후:

```text
CORE 숫자 도전
→ CORE 생활 세계관
→ TREND INJECTION
→ Audience-picked candidate
→ 반복
```

30편을 선생산하지 않는다. **데이터와 시청자 수요로 검증된 가설만 확장한다.**

YouTube는 Shorts에 특정 포맷이나 최소 업로드 빈도를 우대하지 않는다고 안내한다. 선택해서 본 비율, 평균 시청시간/평균 시청률, 만족도 신호를 중심으로 평가하므로 업로드 수 자체를 moat로 보지 않는다.

우리 moat:

> miniature satisfaction + cat IP + unique conflict + accumulating world state + audience participation + low-credit iteration

---

## 8. 원본성 / YPP 안전

각 episode는 아래가 식별 가능해야 한다.

- unique_goal
- unique_conflict
- unique_ending
- character_motivation
- world_state_change
- callback_or_new_lore

`episode_fingerprint` 5개:
- hook_mechanic
- dominant_visual
- conflict_mechanic
- emotional_turn
- ending_mechanic

신규 episode는 직전 5편과 비교해 fingerprint 5개 중 최소 3개가 달라야 한다.

추가 규칙:
- twist는 필수가 아님
- 모든 영상은 `KF4_RESOLUTION` 보유
- 최근 5편에서 같은 resolution family 3회 이상 사용 금지
- creator signature 필수
- 음식만 바꿔 같은 컷 순서/갈등/결말 재사용 금지
- audience request라도 독창성 gate를 우회하지 못함

YouTube `inauthentic content` 정책상 반복·대량생산처럼 보이는 AI template을 피한다. 자동화/템플릿 도구 자체가 문제가 아니라 최종 결과물에 창작자의 고유한 관점과 만족스러운 가치가 있어야 한다.

포토리얼 AI 영상은 altered/synthetic content disclosure를 기본 `Yes`로 처리한다. AI 공개 자체는 추천이나 수익화 자격을 제한하지 않는다고 YouTube가 안내한다.

---

## 9. 수익화 우선순위

### Phase 0 — YPP 이전
- business contact 공개
- original IP portfolio 축적
- food/gadget 카테고리 정리
- public reach 사례를 media kit에 축적
- 광고수익 이전부터 직접 협업 가능성 준비

### Phase 1 — Expanded YPP
현재 조기 기능 기준:
- 500 subscribers
- 최근 90일 valid public uploads 3개
- 3M qualified Shorts views / 90 days 또는 3,000 qualified watch hours

활용:
- fan funding
- Creator Partnerships
- 실제 Studio에서 활성화된 Shopping 기능
- 지원 지역에서 Hype 실험

### Phase 2 — Full Shorts ads/Premium
2026 현재 신규 진입:
- 1,000 subscribers
- 10M qualified Shorts views / 90 days

2027-02-01부터 신규 진입:
- 1,000 subscribers
- 20M qualified Shorts views / 90 days

2027-02-01부터 Shorts Creator Pool 월 수익에는 최근 90일 10M qualified Shorts views 유지 요건이 적용된다. Shopping은 `500명 = 타 브랜드 affiliate 자동 개방`으로 가정하지 않고 Studio의 실제 자격 상태를 기준으로 한다.

---

## 10. 최종 Loop Engineering

```text
Audience signal / trend / core idea
→ originality validation (0 AI tokens)
→ 5 free keyframes
→ 4 Lite frame-locked generations
→ Final Export approval
→ publish + 1 primary interaction mechanic
→ 24h quality snapshot
→ 72h quality + IP conversion snapshot
→ Poll/Q&A/comments become next idea seeds
→ exact failure stage만 수정
→ 승자만 fingerprint를 바꿔 확장
```

핵심 문장:

> **적은 크레딧으로 engaged/qualified view를 학습하고, 다음 아이디어는 시청자가 공급하게 만든다.**
