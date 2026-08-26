# Tiny Cat Kitchen — PROJECT HANDOFF

Last handoff update: **2026-08-27 KST**  
Work-start baseline inspected for this update: `main@d85cb29c94f76cc9c1f8c1d0efbe406b7e452e34`  
Repository: `lgkangno1-svg/youtube-diorama`

> 이 문서는 이전 대화를 모르는 다른 AI/개발자도 Tiny Cat Kitchen을 바로 이어서 운영·개선할 수 있게 하는 인수인계 source of truth다.
>
> **Material repository change가 있으면 반드시 같은 branch/PR에서 이 파일도 갱신한다.** 실제 의사결정이 바뀌지 않는 NO-OP 조사 회차에는 이 문서도 억지로 수정하지 않는다.

---

## 1. 프로젝트 개발 의도

Tiny Cat Kitchen은 단순한 `AI 고양이 요리 영상 생성기`가 아니다. 사용자가 매번 아이디어, 일본 트렌드, Flow 프롬프트, 장면 길이, 실패 리스크, 크레딧 효율, 업로드 후 학습까지 직접 관리하지 않아도 되는 **일본 타깃 Shorts 운영체제**를 만드는 것이 목표다.

사용자의 정상 인터페이스는 가능한 한 아래 한 문장에 가까워야 한다.

```text
다음 영상 준비해줘
```

이 요청을 받으면 시스템이:

1. 최신 일본/글로벌 AI-cat, miniature cooking, ASMR, relaxing-food, adjacent Shorts 조사
2. 일본 시즌/문화/음식/소셜 신호 확인
3. 경쟁작의 exact title/plot/brand/ending을 복제하지 않고 성공 메커니즘만 추출
4. production/analytics history 확인
5. 후보를 Japan relevance, healing fit, visual satisfaction, Veo reliability, originality, worldbuilding, audience demand, expected usable-quality-per-credit로 재평가
6. 최근 episode fingerprint와 구조 중복 차단
7. 다음 episode manifest 생성/수정
8. `production/NEXT_EPISODE.txt` 갱신
9. 사용자가 `./tools/make_next_short.ps1`만 실행하면 되는 상태로 준비

까지 담당한다.

Flow 크레딧 사용, paid video generation, YouTube publish는 사용자 명시 행동 없이 자동으로 하지 않는다.

---

## 2. 최종 채널 목표

### 시청자 경험

일본 10~20대를 핵심 초기 타깃으로 하는 세로형 힐링 Shorts.

핵심 경험:

> **시청자가 고양이가 된 것처럼 1인칭으로 작업대를 내려다보고, 화면 아래의 앞발만으로 믿기 어려울 만큼 작은 디오라마 음식/물건을 조심스럽게 만드는 경험.**

브랜드의 핵심 귀여움은 고양이 얼굴 자체보다 **앞발과 초소형 물체의 압도적 크기 대비**다.

### 운영자 경험

- 아이디어를 매번 직접 고르지 않아도 됨
- episode 번호를 외우지 않아도 됨
- Flow prompt를 직접 조립하지 않아도 됨
- 생성 전에 0-credit frame/reference preflight로 큰 실패를 차단
- G1이 실패하면 G2/G3/G4 크레딧을 쓰지 않음
- 실제 결과가 쌓일수록 runtime/action/hook/seasonality/credit prior 개선
- generated Flow Pack이 실제 UI에서 어떤 First/Last frame을 넣어야 하는지 장면별로 알려줌

---

## 3. 절대 유지해야 하는 영상 정체성

Canonical source of truth:

- `CURRENT_STANDARD.md`
- `docs/24_hero_cat_brand_identity.md`
- `docs/25_pov_paws_microworld_grammar.md`

### POV_PAWS_MICROWORLD_V1

기본 Shorts hard requirements:

- true first-person cat POV
- 화면 아래에 `HERO_CAT_V1`의 cream + pale ginger 앞발 1~2개만 등장
- 얼굴 / 눈 / 귀 / 머리 / 몸통 / 꼬리 / full cat 금지
- hero food/object는 보통 5~20mm
- 화면상 hero object는 한 앞발 폭의 약 15~50% 이하
- macro close-up
- miniature diorama tabletop/workbench
- 카메라는 mostly locked, subtle breathing drift 정도만 허용
- 한 8초 generation = **1 primary tactile action + optional 1 micro-payoff**
- no rapid montage / no meme zoom / no third-person chef shot

예쁘더라도 다음은 구조적 FAIL:

- 고양이가 카운터 뒤에 서서 요리
- 얼굴/몸통/전신이 보임
- 음식/팬이 paw와 비슷하거나 더 큼
- 사람 손가락/엄지 생성
- paw가 사람처럼 도구를 움켜쥠
- 전체 주방이 주인공이 되어 tiny-scale contrast가 약함

### Paw-safe action grammar

선호:

- nudge
- press
- pat
- roll
- steady
- slide
- tap

회피:

- chopsticks / tongs / knife를 사람 손처럼 grip
- thumb-index pinch
- precise twist
- human wrist rotation

도구가 필요하면 넓은 면을 paw pad로 눌러 움직이는 방식으로 재설계한다.

---

## 4. 캐릭터와 세계관

### HERO_CAT_V1

- cream fur base
- pale ginger markings
- real feline paw anatomy
- soft premium/healing tone
- 프로필/배너에서는 얼굴 사용 가능하지만 기본 Shorts는 front-paws-only

### KITCHEN_WORLD_V1

- cozy Japanese-inspired miniature environment
- warm wood / ceramic / paper / tiny stall / tiny workbench
- hero object가 장식보다 먼저 읽혀야 함
- 계절 장식은 허용하되 브랜드 제품/패키지/캠페인 복제 금지

---

## 5. Flow/Veo 운영 전략

Source of truth:

- `docs/23_minimum_credit_operator_architecture.md`
- `docs/26_flow_ui_mode_preflight.md`
- `CURRENT_STANDARD.md`
- `tools/build_flow_pack.py`

### 2026-08-27 공식 Google Flow 도움말 재확인 결과

현재 production assumption을 바꿀 새 근거 없음.

- Google AI Pro monthly credits: 1,000
- Veo 3.1 Lite 4s / 6s / 8s + Extend: non-Ultra 10 credits per generation
- output count = 1을 실제 UI에서 확인
- First + Last frames는 Lite에서 4/6/8s 지원
- Ingredients/References 또는 Extend는 mode에 따라 8s-only일 수 있음
- 1080p upscale은 Plus/Pro/Ultra에서 0 credits
- 실제 Flow UI 표시 비용이 최종 source of truth
- 기존 영상의 `수정 사항 설명` / Omni Flash video edit 화면은 새 Veo generation 화면과 구분

공식 확인 source:

- Google Flow credit help
- Google Flow models & supported features

### Progressive Spend

```text
FREE keyframe/reference preflight
→ G1 8s
→ POV/SCALE/ANATOMY/CAMERA/PROP QC
→ actual last usable frame 저장
→ G2 only after G1 PASS
→ QC
→ G3 only after G2 PASS
→ H30 complete 가능
→ G4 only if immersive_h40 + G3 PASS + 독립 world-resolution beat 존재
```

G2/G3/G4를 미리 생성하지 않는다.

### Sequential Frame Chain — 핵심 운영 규칙

```text
G1
↓ actual last usable frame
G2 First frame
↓ actual last usable frame
G3 First frame
↓ actual last usable frame
G4 First frame only when justified
```

중요한 구분:

- `KF1_WARM`, `KF2_CRACK` 같은 무료 planned keyframe = **목표 상태 / Last frame destination**
- `ACTUAL_LAST_USABLE_FRAME_G1` = **G1이 실제로 생성된 뒤 QC PASS한 영상에서 저장한 실제 마지막 usable frame**

둘은 같은 것이 아니다.

**planned target keyframe을 actual previous frame 대신 다음 First frame에 넣지 않는다.** 그렇게 하면 paw 위치, 카메라, 음식 상태, tray 위치 등이 순간이동할 수 있고 continuity reroll 비용이 증가한다.

이번 2026-08-27 개선에서 `tools/build_flow_pack.py`가 이 구분을 generated Flow Pack 안에서 장면별로 명시하도록 변경됐다.

예:

```text
G1 First frame → approved FREE KF0_OPEN
G1 Last frame  → approved FREE KF1_WARM
G1 PASS 후     → 실제 G1 마지막 usable frame을 G1_last_usable.png로 저장
G2 First frame → 그 실제 G1_last_usable.png 업로드
G2 Last frame  → approved FREE KF2_CRACK
```

이제 generated pack은:

- 각 scene의 First frame source
- 각 scene의 Last frame source
- previous actual frame token의 의미
- PASS 후 바로 저장해야 하는 실제 frame filename 예시
- 잘못된 planned-frame substitution 금지
- `FRAME CHAIN FAIL` QC shorthand

를 출력한다.

목적:

- 같은 first-person camera 유지
- paw fur/anatomy drift 감소
- hero-object scale 유지
- food/cookware state continuity 유지
- lighting/workbench consistency 유지
- 잘못된 frame source로 인한 10-credit reroll 감소

---

## 6. Runtime 정책

### compact_h30

- 3 × 8s raw motion
- first-pass ceiling 약 30 credits
- 최종 약 30~36s
- 3개의 독립 beat로 `scale reveal → tactile making → payoff`가 완결될 때

### immersive_h40

- 4 × 8s raw motion
- first-pass ceiling 약 40 credits
- 최종 약 38~46s
- G4가 단순 패딩이 아니라 serving / paws withdraw / world-resolution / afterglow 같은 독립 가치가 있을 때

### 48~60s

기본값이 아니다. 실제 Tiny Cat Kitchen 24h/72h retention, engaged views/credit, subscriber conversion 데이터가 지지할 때만 실험한다.

---

## 7. 오디오 정책

기본:

```text
No narration
No generated music
Quiet room tone + close tiny ASMR
```

좋은 소리:

- tiny ceramic click
- wood scrape
- crumb/dough press
- soft tiny sizzle
- paper rustle
- faint steam/room ambience

영상이 좋고 generated audio만 이상하면 영상 reroll하지 않는다. 후편집 SFX 교체가 기본이다.

일본어 사용자 녹음 line은 화면만으로 이해가 어렵거나 character voice/payoff가 실질적으로 강화될 때만 짧게 사용한다.

---

## 8. 아이디어 선정과 novelty gate

Source of truth:

- `ideas/episode_backlog.yaml`
- `ideas/novelty_signatures.yaml`
- `tools/select_next_episode.py`
- `docs/28_episode_novelty_authenticity_gate.md`

### 9축 base score

- benchmark evidence — 10
- Japan relevance — 10
- healing fit — 15
- visual satisfaction — 15
- Flow reliability — 20
- originality — 10
- worldbuilding — 5
- audience demand — 5
- expected credit efficiency — 10

### Production eligibility hard gate

- `visual_grammar=POV_PAWS_MICROWORLD_V1`
- tiny-scale 명시
- paw-safe action family
- H30/H40 runtime prior
- 최근 episode fingerprint와 과도한 중복 없음

### Recent-five deterministic novelty gate

`tools/select_next_episode.py`는 최근 5개 `episodes/TK-*.yaml`의 `episode_fingerprint`를 읽는다. planned/ready manifest도 pipeline 중복 방지를 위해 recent window에 포함한다.

Exact hard blocks:

- 동일 `conflict_mechanic + ending_mechanic` pair
- 동일 `hook + conflict + ending` triple

Fuzzy semantic similarity를 근거 없이 hard gate로 만들지 않는다. broader similarity는 새 manifest 생성 전 ChatGPT가 별도 검토한다.

현재 중요한 결과:

- IDEA-009는 TK-005와 동일 future structure라 새로운 episode로 재선택 차단. 단, 이미 준비된 현재 TK-005 production task는 그대로 진행.
- IDEA-002는 TK-004의 gummy tension/measurement 구조와 겹쳐 recent window에서 차단.

---

## 9. Seasonal Search Lead / research policy

Source of truth:

- `research/seasonal_evidence.yaml`
- `research/benchmark_log.csv`
- `docs/27_research_evidence_saturation_gate.md`

계절 후보는 fresh Japanese evidence가 있을 때만 bounded seasonal boost 최대 +8을 받는다.

초기 timing prior:

- 22~35일 전: early lead
- 8~21일 전: strongest lead
- 0~7일 전: strong final lead
- peak 기간: valid but lower than pre-peak sweet spot
- post-peak: small tail

### Evidence saturation

목적은 링크 수집이 아니라 **의사결정 상태를 바꾸는 정보**다.

이미 충분한 behavioral demand / nationwide activation / current survey / culturally dated activation이 있으면 같은 종류의 상품 PR을 계속 commit하지 않는다.

새 commit을 정당화하는 대표 조건:

- candidate score/rank 변경
- NEXT_EPISODE 또는 timing 변경
- evidence class가 질적으로 상승
- 기존 가설과 충돌
- 새 production mechanic 도출
- stale evidence refresh
- 공식 Flow 기능/가격 변경
- 실제 Tiny Cat Kitchen production/performance data 발생
- deterministic tool과 문서 정책 사이 실제 gap 발견

경쟁작에서 exact title / plot / branded product / packaging / exact ending은 복제하지 않는다.

---

## 10. 현재 계절/후보 연구 상태

### IDEA-010 — 新米塩むすび

2026-08-27 추가된 future candidate.

근거 유형:

- 일본 onigiri category의 현재 일상식 수요/트렌드
- 2026 예약쌀 실제 registration behavior
- 9월 초 신미 배송/판매 timing

Working title:

```text
猫の前足で作る、8mmの新米塩むすび。
```

Flow-safe mechanic:

- true first-person POV
- 8mm new-rice salt onigiri
- tiny triangular mold
- broad paw press 1회
- mold slide-away → shape reveal
- glossy individual rice grains + faint steam payoff
- tiny wooden board를 dawn breakfast shelf로 nudge

직접 손처럼 삼각형을 빚거나 김을 정교하게 감싸는 동작은 피한다.

Novelty signature:

```text
hook: new_rice_micro_scale_reveal
conflict: single_press_mold_shape_reveal
ending: dawn_breakfast_shelf_resolution
```

현재 NEXT_EPISODE를 교체하지 않는다.

### 포화된 근거

고구마 / 月見 / gummy 일부 후보는 이미 same-class 홍보 신호를 더 쌓을 필요가 없는 상태다. 새 evidence class나 실제 행동/성과 변화가 없으면 repo churn 금지.

---

## 11. 현재 실제 제작 상태

### NEXT_EPISODE

`production/NEXT_EPISODE.txt` = **TK-005**

현재 episode:

```text
猫の前足で作る、12mmの焼きいも。
```

Manifest: `episodes/TK-005.yaml`
Runtime mode: `immersive_h40`

핵심 4 beat:

1. impossible scale reveal — 12mm 보라색 고구마 + paw 대비
2. slow roast/crack — 같은 tiny tray를 heat 쪽으로 이동, 껍질 상태 변화
3. golden-center reveal — tray를 불에서 살짝 밀어낸 후 잔열로 기존 crack이 자연스럽게 벌어짐
4. world resolution — 같은 tray를 tiny serving niche로 밀고 paws가 빠지며 steam 유지

Continuity rules:

- G1~G4 same roasting tray
- 새 plate/bowl/cookware 갑작스러운 등장 금지
- paw가 고구마를 집거나 pinch하지 않음
- G3 reveal은 passive residual-heat transformation

### TK-005 actual frame workflow

G1:

```text
First = KF0_OPEN
Last  = KF1_WARM
PASS → save G1 actual last usable frame
```

G2:

```text
First = actual saved last usable frame from G1
Last  = KF2_CRACK
PASS → save G2 actual last usable frame
```

G3:

```text
First = actual saved last usable frame from G2
Last  = KF3_OPEN
PASS → save G3 actual last usable frame
```

G4 only if still justified:

```text
First = actual saved last usable frame from G3
Last  = KF4_SERVE
```

### 현재 actual production learning

`analytics/learning_ledger.csv`의 `POV-PREFLIGHT-001`에서 관찰된 실패:

- third-person full cat
- body visible
- object scale too large
- human-like tool-use risk

학습:

- true first-person camera hard gate
- front paws only
- hero object <=0.50 paw width
- nudge / press / slide 중심

현재 아직 실제 published 24h/72h 성과 데이터는 없다.

---

## 12. 현재 후보 상태 요약

### TK-005 / IDEA-009 — 현재 production task

- production-ready
- sweet-potato seasonal/behavior evidence 충분
- high visual satisfaction / Flow reliability / credit efficiency
- novelty gate상 future repeat은 막히지만 현재 준비된 production task는 진행
- 지금 가장 가치 있는 다음 행동은 실제 G1 생성/QC

### IDEA-010 — 新米塩むすび

- priority future candidate
- actual rice reservation behavior + early-September new-rice timing
- compact H30
- one mold press + slide reveal
- recent exact duplicate 아님

### IDEA-001 — 8mm 月見だんご

- 2026-09-25 十五夜 recognition 강함
- moon/roundness/harvest-night만 generic하게 사용
- paw-safe roll/slide
- recent exact duplicate 아님

### IDEA-006 — 10mm 栗ごはん

- 9월 초 이후 recognition 증가
- tiny clay-pot + steam worldbuilding
- recent exact duplicate 없음

### IDEA-002 — 3mm グミ

- 9/3 timing/texture interest는 좋음
- 현재 conflict+ending signature가 TK-004와 겹쳐 future selection 차단
- 제목/색만 바꿔 gate 우회 금지

---

## 13. 주요 deterministic tools

- `tools/select_next_episode.py` — backlog + seasonal timing + recent-five novelty gate
- `tools/test_select_next_episode.py` — selector regression tests
- `ideas/novelty_signatures.yaml` — candidate hook/conflict/ending signatures
- `tools/validate_current_standard.py` — stale manifest / POV / runtime rules validation
- `tools/build_flow_pack.py` — manifest → Flow prompt pack + **scene별 explicit First/Last frame operator map**
- `tools/test_build_flow_pack.py` — actual-frame token / free keyframe / fail-closed / save-gate regression tests
- `tools/build_healing_edit_plan.py` — runtime/pacing edit plan
- `tools/build_publish_pack.py` — publish metadata pack
- `tools/score_credit_efficiency.py` — actual production 성과 대비 credits 분석
- `tools/score_shorts_experiments.py` / `v2` — experiment scoring
- `tools/make_next_short.ps1` — `NEXT_EPISODE` 기반 사용자 bundle 생성
- `tools/validate_handoff_update.py` — material change에 handoff 누락 여부 검증

Generated artifacts:

- `generated/TK-XXX_bundle.md`
- `generated/TK-XXX_flow_pack.md`
- `generated/TK-XXX_edit_plan.md`
- `generated/TK-XXX_publish_pack.md`

준비 단계에서는 Flow/LLM/API 크레딧을 쓰지 않는다.

---

## 14. 성과 학습 구조

Source of truth: `analytics/learning_ledger.csv`

가능한 경우 기록:

### Production

- actual Flow credits
- rerolls
- G1/G2/G3/G4 first-pass success
- POV / scale / anatomy failure
- continuity issue
- failed action type
- usable motion seconds
- audio replacement
- final runtime
- beat drop-off note

### Audience 24h / 72h

- Stayed to watch
- APV
- engaged views
- subscribers gained
- comments

Long-term optimization:

```text
usable motion / credit
engaged views / credit
subscribers / 100 credits
```

`credits/video` 최소화 자체가 목표가 아니다. 더 높은 engaged views/credit 또는 subscriber conversion을 만드는 합리적 H40은 H30보다 우수할 수 있다.

Placeholder 0을 실제 실패 데이터처럼 학습하지 않는다.

---

## 15. 완료된 핵심 기반

- [x] 일본 타깃 채널 기본 컨셉
- [x] POV paws-only visual grammar
- [x] tiny-object scale hard gate
- [x] paw-safe action grammar
- [x] H30/H40 adaptive runtime
- [x] Progressive Spend
- [x] sequential actual-frame chaining policy
- [x] generated Flow Pack의 explicit First/Last frame operator map
- [x] actual-frame token regression tests
- [x] no narration / no generated music 기본 정책
- [x] seasonal lead-time scoring
- [x] evidence freshness/saturation gate
- [x] backlog 9축 scoring
- [x] recent-five deterministic novelty gate
- [x] YouTube anti-template/authenticity 운영 원칙
- [x] Flow UI generation/edit-mode preflight
- [x] production manifest validator
- [x] deterministic Flow/edit/publish pack tools
- [x] credit-efficiency learning 구조
- [x] actual Flow visual failure ledger 구조
- [x] TK-005 production-ready manifest
- [x] persistent `PROJECT_HANDOFF.md`
- [x] 2026 new-rice/onigiri future candidate + current Japanese behavioral evidence

아직 미완료:

- [ ] TK-005 실제 새 POV G1 생성/QC
- [ ] G1→G2→G3→조건부 G4 real continuity 검증
- [ ] final export 실제 편집 검증
- [ ] 첫 YouTube 게시
- [ ] 실제 24h/72h analytics
- [ ] H30 vs H40 실채널 retention 비교
- [ ] paw action family별 first-pass rate
- [ ] usable motion/credit baseline
- [ ] engaged views/credit 및 subscribers/credit baseline
- [ ] season lead timing 실효성 검증
- [ ] novelty gate strictness 실데이터 검증

---

## 16. 앞으로의 개발 플랜

### Phase A — Production truth

최우선.

1. TK-005 G1 실제 생성
2. POV/SCALE/ANATOMY/CAMERA/PROP QC
3. PASS 직후 실제 last usable frame 저장
4. generated Flow Pack의 explicit frame map대로 G2 First frame 연결
5. G2 PASS 후 actual frame 저장 → G3 연결
6. G3 완결성 확인
7. G4는 독립 world-resolution 가치가 있을 때만 생성
8. actual credits / rerolls / usable seconds 기록

### Phase B — First published Shorts learning

첫 게시 후 24h/72h metrics 수집. 한 편으로 과도한 결론을 내리지 않는다.

### Phase C — Runtime experiment

여러 편 누적 후 compact_h30(30~36s) vs immersive_h40(38~46s)을 같은 observation horizon에서 비교.

### Phase D — Production reliability model

충분한 episode가 쌓이면 nudge/press/slide/passive transformation/liquid/deformable object별 first-pass success와 credit cost prior를 만든다.

### Phase E — Seasonal timing learning

현재 8~21일 pre-peak sweet spot은 초기 prior다. 실제 publish date와 STW/APV/engaged views/credit/subscriber conversion을 비교해 조정.

### Phase F — Originality learning

브랜드 문법은 유지하되 story substance는 반복하지 않는다. exact novelty gate가 너무 엄격/느슨한지는 episode 누적 후 판단.

### Phase G — Operator simplification

장기 UX:

```text
사용자: 다음 영상 준비해줘
AI: 후보 조사/선택 + manifest + NEXT_EPISODE 준비
사용자: ./tools/make_next_short.ps1
Flow Pack: 각 scene에 First/Last frame source와 PASS 후 저장 동작까지 표시
사용자: G1 만들었어. 봐줘
AI: PASS / EDITABLE / REROLL / STOP
```

---

## 17. 다음 작업 우선순위

1. **TK-005 실제 G1 결과 확보**
2. first-person/front-paws-only/tiny-scale 재현성 검증
3. 실제 Flow 표시 model/cost 기록
4. G1 PASS 후 실제 last usable frame 저장 여부 확인
5. G2 First frame에 planned KF가 아니라 G1 actual frame이 실제로 들어갔는지 검증
6. G3/G4 prop continuity 검증
7. first export 38~46s pacing 검토
8. 첫 게시 후 24h/72h data 확보
9. 그 다음 actual data로 backlog/runtime/credit/novelty prior 조정
10. TK-005 완료 후 IDEA-010 / IDEA-001 등 future candidate를 current Japanese evidence로 재비교

현재는 TK-005를 중간에 바꾸는 것보다 production truth 확보가 더 중요하다.

---

## 18. 사용자가 직접 해야 하는 최소 행동

현재 필요한 실제 행동:

1. 로컬에서 `./tools/make_next_short.ps1` 실행
2. generated `TK-005_flow_pack.md` 확인
3. Flow에서 NEW VIDEO GENERATION + Veo 3.1 Lite + 9:16 + output 1 + 표시 cost 확인
4. **G1만 생성**
5. 결과 영상/스크린샷을 ChatGPT에 전달

```text
G1 만들었어. 봐줘
```

G1이 PASS하면 generated Flow Pack 안내대로 실제 마지막 usable frame을 저장한 뒤에만 G2로 진행한다.

---

## 19. 다른 AI/개발자의 시작 순서

1. 최신 main SHA 확인
2. recent commits/PRs 확인
3. `PROJECT_HANDOFF.md` 읽기
4. `START_HERE.md`
5. `CURRENT_STANDARD.md`
6. `docs/22_continuous_episode_learning_engine.md`
7. `docs/23_minimum_credit_operator_architecture.md`
8. `production/NEXT_EPISODE.txt` + 해당 manifest
9. `analytics/learning_ledger.csv`
10. `ideas/episode_backlog.yaml` + `ideas/novelty_signatures.yaml`
11. `research/seasonal_evidence.yaml` + benchmark log
12. core tools와 tests 확인
13. concurrent changes/회귀 위험 확인 후 수정 시작

최신 GitHub 상태를 이전 assistant memory보다 우선한다.

---

## 20. Handoff persistence rule

Material change라면 반드시 같은 branch/PR에서 `PROJECT_HANDOFF.md`를 갱신한다.

Material examples:

- production standard 변경
- Flow cost/feature assumption 변경
- NEXT_EPISODE/manifest 변경
- meaningful backlog score/ranking change
- analytics/learning rule 변경
- selection/originality algorithm 변경
- actual production/performance data
- tool behavior change / important bug fix
- operator interface 변경
- 새로운 후보가 future ranking/production decision을 의미 있게 바꿈

NO-OP examples:

- 같은 계절 PR 기사 반복
- score/rank/timing/mechanic에 영향 없는 research duplicate
- repo 자체 무변경

Local git이 가능하면:

```powershell
python tools/validate_handoff_update.py --base origin/main
```

또는 동등한 valid base로 확인한다.

---

## 21. 안전/금지 규칙

- Flow credits 자동 사용 금지
- paid generation 자동 실행 금지
- YouTube 자동 publish 금지
- 경쟁작 exact title/plot/brand/ending 복제 금지
- food/season 이름만 바꾼 동일 conflict+ending 반복 금지
- novelty signature rename으로 gate 우회 금지
- full-cat third-person 회귀 금지
- planned target keyframe을 actual previous-scene frame으로 위장해 continuity 진행 금지
- previous scene FAIL 상태에서 next generation spend 금지
- 60초 padding 금지
- audio-only 문제 때문에 좋은 영상 reroll 금지
- same-class seasonal PR churn 금지
- placeholder analytics 0을 실제 failure처럼 학습 금지
- Cali 또는 unrelated repository 수정 금지

---

## 22. Definition of Done

반복 가능한 전체 loop:

```text
current benchmark/JP signal research
→ candidate scoring + novelty gate
→ paw-only/tiny-scale production-safe manifest
→ 0-credit frame preflight
→ progressive Flow generation
→ actual-last-frame continuity chain
→ continuity QC
→ low-friction edit/export
→ upload
→ 24h/72h learning
→ next episode selection
```

그리고 episode가 쌓일수록:

- first-pass generation success 상승
- usable motion/credit 상승
- engaged views/credit 상승
- subscribers/credit 상승
- 사용자 수동 prompt/frame-source 판단 감소
- continuity reroll 감소
- template story 반복 감소

가 실제 데이터로 보여야 한다.

---

## 23. Handoff change log

### 2026-08-27 — Explicit Flow frame-input map

Baseline inspected: `main@d85cb29c94f76cc9c1f8c1d0efbe406b7e452e34`.

Problem found:

- manifest와 문서는 sequential actual-frame chaining을 요구했지만 generated Flow Pack은 `ACTUAL_LAST_USABLE_FRAME_G1` 같은 symbolic token을 그대로 보여주어, 실제 Flow에서 어떤 이미지를 First frame에 넣어야 하는지 초보 운영자가 혼동할 수 있었음.
- planned target keyframe을 previous actual frame 대신 사용하면 camera/paw/food/tray continuity가 깨지고 reroll cost가 늘어날 수 있음.

Changes:

- `tools/build_flow_pack.py`가 symbolic frame token을 explicit operator action으로 변환
- scene별 First frame / Last frame input 안내 추가
- PASS 후 actual last usable frame 즉시 저장 안내 및 filename 예시 추가
- next scene이 actual frame을 요구하면 visual continuity 확인 전 다음 spend 금지
- `FRAME CHAIN FAIL` QC shorthand 추가
- `tools/test_build_flow_pack.py` 신규 추가로 actual token, free KF, missing-frame fail-closed, sequential save gate를 회귀 테스트

Unchanged:

- NEXT_EPISODE = TK-005
- TK-005 story/runtime/manifest
- Flow cost assumptions
- candidate scores/ranking
- no paid generation / no publish

Next highest-value action remains: **사용자가 TK-005 G1을 실제 생성해 production truth를 확보하는 것.**

### 2026-08-27 — New-rice onigiri candidate

- IDEA-010 `8mm 新米塩むすび` 추가
- actual rice reservation behavior + early-September new-rice timing 반영
- triangular mold + one broad paw press + slide-away reveal로 human-like shaping 회피
- NEXT_EPISODE TK-005 유지

### 2026-08-26 — Deterministic novelty gate

- recent-five fingerprint exact conflict+ending / hook+conflict+ending repeat 차단
- IDEA-009 future repeat, IDEA-002 recent gummy structure repeat 차단
- current TK-005 task 유지

### 2026-08-26 — Persistent handoff protocol

- root `PROJECT_HANDOFF.md`를 프로젝트 인수인계 source of truth로 추가
- material repo change와 같은 PR에서 handoff 갱신 의무화
- `tools/validate_handoff_update.py` 추가
