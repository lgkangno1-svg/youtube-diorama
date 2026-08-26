# Tiny Cat Kitchen — PROJECT HANDOFF

Last handoff update: **2026-08-27 KST**  
Work-start baseline inspected for this update: `main@fca5266acb7c40176b746d8954a5fef0aa19456d`  
Repository: `lgkangno1-svg/youtube-diorama`

> 다른 AI/개발자가 이전 대화를 전혀 보지 않아도 이 문서와 최신 GitHub만으로 Tiny Cat Kitchen을 이어서 운영·개선할 수 있어야 한다.
>
> **Material repository change가 있으면 반드시 같은 branch/PR에서 이 파일도 갱신한다.** 실제 의사결정이 변하지 않는 NO-OP 조사 회차에는 날짜만 바꾸는 handoff churn을 하지 않는다.

---

## 1. 프로젝트 개발 의도

Tiny Cat Kitchen은 단순한 AI 고양이 영상 생성기가 아니라 **일본 타깃 Shorts 운영체제**다. 사용자가 매번 일본 트렌드 조사, 아이디어 선택, Flow 프롬프트, 장면 길이, 실패 리스크, 크레딧 계산, continuity, 편집, 24h/72h 학습을 직접 관리하지 않아도 되게 하는 것이 목적이다.

정상 사용자 인터페이스는 가능한 한 아래 한 문장에 가까워야 한다.

```text
다음 영상 준비해줘
```

이 요청을 받으면 시스템이:

1. 최신 일본/글로벌 AI-cat, miniature cooking, ASMR, relaxing-food, adjacent Shorts 조사
2. 일본 시즌/문화/음식/소셜 신호 확인
3. 경쟁작의 exact title/plot/brand/ending을 복제하지 않고 성공 메커니즘만 추출
4. production/analytics history 확인
5. 후보를 Japan relevance, healing fit, visual satisfaction, Veo reliability, originality, worldbuilding, audience demand, expected usable-quality-per-credit로 평가
6. 최근 episode fingerprint 중복 차단
7. episode manifest 생성/수정
8. `production/NEXT_EPISODE.txt` 갱신
9. 사용자가 `./tools/make_next_short.ps1`만 실행하면 되는 상태로 준비

까지 담당한다.

Flow credits 사용, paid video generation, YouTube publish는 사용자 명시 행동 없이 자동으로 하지 않는다.

---

## 2. 최종 채널 목표

### 시청자 경험

일본 10~20대를 핵심 초기 타깃으로 하는 세로형 힐링 Shorts.

핵심 경험:

> **시청자가 고양이가 된 것처럼 1인칭으로 작업대를 내려다보고, 화면 아래의 앞발만으로 믿기 어려울 만큼 작은 디오라마 음식/물건을 조심스럽게 만드는 경험.**

브랜드의 핵심 귀여움은 고양이 얼굴이 아니라 **앞발과 초소형 물체의 압도적 크기 대비**다.

### 운영자 경험

- 아이디어를 매번 직접 고르지 않음
- episode 번호를 외우지 않음
- Flow prompt를 직접 조립하지 않음
- 생성 전에 0-credit frame/reference preflight
- G1 실패 시 G2/G3/G4 크레딧 미사용
- 실제 결과가 쌓일수록 runtime/action/hook/seasonality/credit prior 개선
- generated Flow Pack이 scene별 First/Last frame source를 직접 안내
- H30/H40을 스크립트에 고정하지 않고 manifest가 runtime source of truth가 됨

---

## 3. 절대 유지해야 하는 영상 정체성

Canonical source of truth:

- `CURRENT_STANDARD.md`
- `docs/24_hero_cat_brand_identity.md`
- `docs/25_pov_paws_microworld_grammar.md`

### POV_PAWS_MICROWORLD_V1

Hard requirements:

- true first-person cat POV
- 화면 아래 `HERO_CAT_V1` cream + pale ginger 앞발 1~2개만 등장
- 얼굴/눈/귀/머리/몸통/꼬리/full cat 금지
- hero food/object 보통 5~20mm
- 화면상 hero object는 한 앞발 폭의 약 15~50% 이하
- macro close-up
- miniature diorama tabletop/workbench
- mostly locked camera, subtle breathing drift 정도만 허용
- 한 8초 generation = **1 primary tactile action + optional 1 micro-payoff**
- no rapid montage / no meme zoom / no third-person chef shot

구조적 FAIL:

- 고양이가 카운터 뒤에 서서 요리
- 얼굴/몸통/전신 노출
- 음식/팬이 paw와 비슷하거나 더 큼
- 사람 손가락/엄지
- paw가 사람처럼 도구를 움켜쥠
- wide establishing shot 때문에 tiny-scale contrast가 약함

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

- chopsticks/tongs/knife human grip
- thumb-index pinch
- precise twist
- human wrist rotation

도구가 필요하면 넓은 면을 paw pad로 눌러 이동하는 방식으로 재설계한다.

---

## 4. 캐릭터와 세계관

### HERO_CAT_V1

- cream fur base
- pale ginger markings
- real feline paw anatomy
- soft premium/healing tone
- 프로필/배너에서는 얼굴 가능, 기본 Shorts는 front-paws-only

### KITCHEN_WORLD_V1

- cozy Japanese-inspired miniature environment
- warm wood / ceramic / paper / tiny stall / tiny workbench
- hero object가 장식보다 먼저 읽혀야 함
- 계절 장식 허용, branded package/campaign 복제 금지

---

## 5. Flow/Veo 운영 전략

Source of truth:

- `docs/23_minimum_credit_operator_architecture.md`
- `docs/26_flow_ui_mode_preflight.md`
- `CURRENT_STANDARD.md`
- `tools/build_flow_pack.py`

### 2026-08-27 공식 Google Flow 재확인

Production assumption 변경 없음.

- Google AI Pro: 1,000 Flow credits/month
- Veo 3.1 Lite 4s/6s/8s + Extend: non-Ultra 10 credits/generation
- First + Last frames: Lite 4/6/8s 지원
- Ingredients/References 및 Extend는 mode에 따라 8s-only 가능
- 1080p upscale: Plus/Pro/Ultra 0 credits
- output count는 실제 UI에서 1 확인
- 실제 UI displayed cost가 최종 source of truth
- `수정 사항 설명` / Omni Flash video edit는 새 Veo generation과 구분

Official sources rechecked this run:

- Google Flow credit help
- Google Flow models & supported features
- Google Flow create-video help

### Progressive Spend

```text
FREE keyframe/reference preflight
→ G1
→ QC
→ actual last usable frame 저장
→ G2 only after G1 PASS
→ QC
→ G3 only after G2 PASS
→ compact_h30이면 완결 가능
→ G4 only if immersive_h40 + G3 PASS + independent value still real
```

G2/G3/G4를 미리 생성하지 않는다.

### Sequential Frame Chain

```text
G1
↓ actual last usable frame
G2 First frame
↓ actual last usable frame
G3 First frame
↓ actual last usable frame
G4 First frame only when justified
```

중요:

- `KF1_WARM`, `KF2_CRACK` 같은 planned keyframe = 목표 Last-frame state
- `ACTUAL_LAST_USABLE_FRAME_G1` = 실제 G1 PASS 영상에서 저장한 frame

planned target keyframe을 previous actual frame 대신 다음 First frame으로 사용하지 않는다.

`tools/build_flow_pack.py`는 각 scene마다:

- First frame source
- Last frame source
- actual-frame token 의미
- PASS 후 저장 filename 예시
- missing/wrong frame 시 STOP
- `FRAME CHAIN FAIL`

을 출력한다.

---

## 6. Runtime 정책

### compact_h30

- 3 × 8s raw motion
- first-pass ceiling 약 30 credits
- final 약 30~36s
- `scale reveal → tactile making → payoff`가 3 beat로 완결될 때

### immersive_h40

- 4 × 8s raw motion
- first-pass ceiling 약 40 credits
- final 약 38~46s
- G4가 serving / paws withdraw / world-resolution / afterglow 같은 독립 가치를 가질 때

### 48~60s

기본값 아님. 실제 retention/engaged views/credit/subscriber conversion이 지지할 때만 실험.

### 2026-08-27 runtime operator bug fix

발견된 실제 gap:

- `CURRENT_STANDARD.md`와 TK-005 manifest는 adaptive H30/H40 구조이며 TK-005는 `immersive_h40`.
- 그러나 `tools/make_short.ps1`와 `tools/make_next_short.ps1`가 여전히 `H30 = three generations`를 고정 안내.
- `tools/build_episode_bundle.py`도 upload gate에서 `30~36s cut`을 일반 권장해 H40 episode operator를 혼동시킬 수 있었음.

수정:

- PowerShell entrypoints에서 fixed H30 assumption 제거
- episode-specific Flow Pack/manifest가 scene count와 runtime intent의 source of truth가 되도록 변경
- `compact_h30`: G3에서 완결되면 종료, G4 padding 금지
- `immersive_h40`: G3 PASS 후 documented independent G4 value가 실제로 남아 있을 때만 G4
- G4를 단순히 H30에 맞추려고 삭제하지도 않고, 길이 채우려고 유지하지도 않음
- bundle index가 runtime mode와 preferred final range를 직접 출력
- `tools/test_build_episode_bundle_runtime.py`로 H30/H40/custom runtime guidance 회귀 체크 추가

이 변경은 TK-005 story/manifest/credit budget을 바꾸지 않고 **운영 안내가 이미 승인된 adaptive runtime 정책을 정확히 따르게 하는 bug fix**다.

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

영상이 좋고 generated audio만 이상하면 video reroll하지 않고 post SFX 교체.

일본어 사용자 녹음 line은 comprehension/character/payoff를 실질적으로 강화할 때만 짧게 사용.

---

## 8. 아이디어 선정과 originality

Source of truth:

- `ideas/episode_backlog.yaml`
- `ideas/novelty_signatures.yaml`
- `tools/select_next_episode.py`
- `docs/28_episode_novelty_authenticity_gate.md`

9축 base score:

- benchmark evidence — 10
- Japan relevance — 10
- healing fit — 15
- visual satisfaction — 15
- Flow reliability — 20
- originality — 10
- worldbuilding — 5
- audience demand — 5
- expected credit efficiency — 10

Production eligibility:

- `visual_grammar=POV_PAWS_MICROWORLD_V1`
- tiny-scale 명시
- paw-safe action family
- H30/H40 runtime prior
- recent episode fingerprint와 과도한 중복 없음

Recent-five deterministic novelty gate:

- 동일 conflict + ending pair 차단
- 동일 hook + conflict + ending triple 차단
- planned/ready manifests도 recent window 포함
- fuzzy semantic similarity는 근거 없이 hard gate로 만들지 않음

현재 consequence:

- IDEA-009는 future repeat로 재선택 차단되지만 이미 준비된 TK-005는 현재 production task로 계속 진행
- IDEA-002는 TK-004 gummy conflict/ending 구조와 겹쳐 현재 future selection 차단

---

## 9. Research / seasonal policy

Source of truth:

- `research/seasonal_evidence.yaml`
- `research/benchmark_log.csv`
- `docs/27_research_evidence_saturation_gate.md`

계절 후보는 fresh Japanese evidence가 있을 때만 bounded seasonal boost 최대 +8.

Timing prior:

- 22~35일 전: early lead
- 8~21일 전: strongest lead
- 0~7일 전: strong final lead
- peak: valid but lower than pre-peak sweet spot
- post-peak: small tail

Evidence saturation 원칙:

이미 behavioral demand / independent nationwide activation / current survey / culturally dated activation 등 충분한 근거가 있으면 same-class PR/상품 뉴스 추가만으로 commit하지 않는다.

Material research update 조건:

- candidate score/rank 변경
- NEXT_EPISODE/timing 변경
- evidence class 질적 상승
- 기존 가설과 충돌
- 새 production mechanic
- stale evidence refresh
- 공식 Flow feature/price 변경
- 실제 Tiny Cat Kitchen production/performance data

이번 회차 fresh benchmark 참고:

- 일본 `AI猫にゃんこちん Official`은 최근 30일에도 성장 중이며 과거 cooking/job/character routine 계열 인기작이 큰 조회를 유지.
- `黒猫のご飯屋さん`의 2026-08-16 여름축제 콘텐츠도 현재 약 15만 조회 규모로 확인됨.

추출 가능한 abstract lesson은 **고양이 세계관 + 문화적으로 읽히는 일상/행사 맥락**이 character attachment를 강화할 수 있다는 정도다. 이 원리는 기존 cat-job/worldbuilding/seasonal policy와 이미 겹치므로 이번에는 benchmark log나 후보 점수를 추가로 churn하지 않았다.

경쟁작의 exact title/plot/brand/ending은 복제하지 않는다.

---

## 10. 현재 실제 제작 상태

`production/NEXT_EPISODE.txt` = **TK-005**

Episode:

```text
猫の前足で作る、12mmの焼きいも。
```

Manifest: `episodes/TK-005.yaml`  
Runtime mode: `immersive_h40`

4 beats:

1. impossible scale reveal — 12mm purple sweet potato + paw contrast
2. slow roast/crack — same tiny tray toward heat, skin changes
3. golden center reveal — tray slightly away from heat, residual heat widens existing crack
4. world resolution — same tray into tiny serving niche, paws withdraw, steam remains

Continuity:

- G1~G4 same roasting tray
- no sudden new plate/bowl/cookware
- no paw pinch/pickup of potato
- G3 reveal is passive residual-heat transformation

Actual frame workflow:

```text
G1 First = KF0_OPEN
G1 Last  = KF1_WARM
PASS → save actual G1 last usable frame

G2 First = saved actual G1 frame
G2 Last  = KF2_CRACK
PASS → save actual G2 last usable frame

G3 First = saved actual G2 frame
G3 Last  = KF3_OPEN
PASS → save actual G3 last usable frame

G4 First = saved actual G3 frame
G4 Last  = KF4_SERVE
only if G3 PASS + world-resolution value remains real
```

Current actual production learning from `analytics/learning_ledger.csv`:

- third-person full cat occurred
- body visible
- object scale too large
- human-like tool-use risk

Resulting hard gates:

- true first-person camera
- front paws only
- hero object <=0.50 paw width
- nudge/press/slide over grip

아직 published 24h/72h performance data는 없음.

---

## 11. 현재 후보 요약

### TK-005 / IDEA-009 — current production task

- production-ready
- yakiimo seasonal/behavior evidence 충분
- strong visual satisfaction / Flow reliability / credit efficiency
- future exact-repeat selection은 novelty gate가 막음
- 현재 최우선은 실제 G1 생성/QC

### IDEA-010 — 8mm 新米塩むすび

- priority future candidate
- actual rice reservation behavior + early-September new-rice timing
- compact_h30
- triangular mold + one broad paw press + slide-away reveal
- recent exact duplicate 아님

### IDEA-001 — 8mm 月見だんご

- 2026-09-25 十五夜 recognition 강함
- generic moon/roundness/harvest-night mechanic만 사용
- paw-safe roll/slide

### IDEA-006 — 10mm 栗ごはん

- early-autumn recognition
- tiny clay-pot + steam worldbuilding

### IDEA-002 — 3mm グミ

- 9/3 timing/texture interest는 있으나 current novelty signature가 TK-004와 겹쳐 future selection 차단

---

## 12. 주요 deterministic tools

- `tools/select_next_episode.py` — backlog + seasonal timing + recent-five novelty gate
- `tools/test_select_next_episode.py` — selector regression
- `ideas/novelty_signatures.yaml` — candidate novelty signatures
- `tools/validate_current_standard.py` — stale manifest / POV / runtime validation
- `tools/build_flow_pack.py` — manifest → Flow pack + explicit First/Last frame map
- `tools/test_build_flow_pack.py` — frame mapping regression
- `tools/build_episode_bundle.py` — Flow/edit/publish bundle + **manifest-aware runtime guidance**
- `tools/test_build_episode_bundle_runtime.py` — H30/H40/custom runtime guidance regression
- `tools/build_healing_edit_plan.py` — runtime/pacing edit plan
- `tools/build_publish_pack.py` — publish metadata
- `tools/score_credit_efficiency.py` — production outcome vs credits
- `tools/make_short.ps1` — episode bundle entrypoint, no fixed H30 assumption
- `tools/make_next_short.ps1` — NEXT_EPISODE entrypoint, runtime-adaptive progressive-spend guidance
- `tools/validate_handoff_update.py` — material change + handoff sync guard

Generated artifacts:

- `generated/TK-XXX_bundle.md`
- `generated/TK-XXX_flow_pack.md`
- `generated/TK-XXX_edit_plan.md`
- `generated/TK-XXX_publish_pack.md`

Prep stage uses 0 Flow/LLM/API credits.

---

## 13. 성과 학습 구조

Source of truth: `analytics/learning_ledger.csv`

Production fields when available:

- actual Flow credits
- rerolls
- G1/G2/G3/G4 first-pass success
- POV/scale/anatomy failure
- continuity issue
- failed action type
- usable motion seconds
- audio replacement
- final runtime
- beat drop-off note

24h/72h audience fields:

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

`credits/video` 최소화 자체가 목표가 아니다. 더 좋은 engaged views/credit와 subscriber conversion을 만드는 합리적 H40은 H30보다 우수할 수 있다.

Placeholder 0은 실제 failure data로 학습하지 않는다.

---

## 14. 완료된 핵심 기반

- [x] 일본 타깃 Tiny Cat Kitchen 컨셉
- [x] POV paws-only visual grammar
- [x] tiny-object scale hard gate
- [x] paw-safe action grammar
- [x] adaptive H30/H40 runtime
- [x] Progressive Spend
- [x] sequential actual-frame chaining
- [x] explicit First/Last frame operator map
- [x] Flow frame-chain regression tests
- [x] **PowerShell/bundle fixed-H30 operator drift 제거**
- [x] **manifest-aware runtime guidance regression test**
- [x] no narration / no generated music default
- [x] seasonal lead-time scoring
- [x] evidence freshness/saturation gate
- [x] backlog 9-axis scoring
- [x] recent-five deterministic novelty gate
- [x] YouTube anti-template/authenticity rule
- [x] Flow generation/edit-mode preflight
- [x] production manifest validator
- [x] credit-efficiency learning structure
- [x] actual visual failure ledger
- [x] TK-005 production-ready manifest
- [x] persistent `PROJECT_HANDOFF.md`
- [x] new-rice/onigiri future candidate

Still incomplete:

- [ ] TK-005 actual new POV G1 generation/QC
- [ ] G1→G2→G3→conditional G4 real continuity validation
- [ ] final export edit validation
- [ ] first YouTube publish
- [ ] actual 24h/72h analytics
- [ ] H30 vs H40 real-channel retention comparison
- [ ] paw action family first-pass rates
- [ ] usable motion/credit baseline
- [ ] engaged views/credit and subscribers/credit baseline
- [ ] seasonal timing effectiveness
- [ ] novelty gate strictness validation

---

## 15. 앞으로의 개발 플랜

### Phase A — Production truth

최우선.

1. TK-005 G1 실제 생성
2. POV/SCALE/ANATOMY/CAMERA/PROP QC
3. PASS 직후 actual last usable frame 저장
4. Flow Pack대로 G2 연결
5. G2 PASS → actual frame → G3
6. G3 완결성 확인
7. G4는 independent world-resolution value가 실제로 남아 있을 때만
8. actual credits/rerolls/usable seconds 기록

### Phase B — First published learning

첫 게시 후 24h/72h metrics 수집. 한 편으로 과도한 결론 금지.

### Phase C — Runtime experiment

여러 편 누적 후 compact_h30 vs immersive_h40을 같은 horizon에서 비교.

### Phase D — Production reliability model

nudge/press/slide/passive transformation/liquid/deformable object별 first-pass success와 credit cost prior 구축.

### Phase E — Seasonal timing learning

현재 8~21일 pre-peak sweet spot은 initial prior. 실제 publish/performance로 조정.

### Phase F — Originality learning

브랜드 문법은 유지하되 storyline substance 반복 금지. novelty gate strictness는 data 축적 후 조정.

### Phase G — Operator simplification

목표 UX:

```text
사용자: 다음 영상 준비해줘
AI: 조사/선택 + manifest + NEXT_EPISODE 준비
사용자: ./tools/make_next_short.ps1
Flow Pack: scene별 First/Last source + PASS 후 저장 동작
사용자: G1 만들었어. 봐줘
AI: PASS / EDITABLE / REROLL / STOP
```

---

## 16. 다음 작업 우선순위

1. **TK-005 실제 G1 확보**
2. first-person/front-paws-only/tiny-scale 재현성 검증
3. 실제 Flow displayed model/cost 기록
4. G1 PASS 후 actual last usable frame 저장
5. G2 First에 actual G1 frame이 들어갔는지 확인
6. G3/G4 prop continuity
7. first export 38~46s pacing 검토
8. first publish 후 24h/72h data
9. actual data로 runtime/credit/backlog/novelty prior 조정
10. TK-005 완료 후 IDEA-010/IDEA-001 등 재비교

현재는 TK-005를 새 후보로 교체하는 것보다 production truth 확보가 더 중요하다.

---

## 17. 사용자가 직접 해야 하는 최소 행동

1. 로컬에서 `./tools/make_next_short.ps1`
2. generated `TK-005_bundle.md`와 `TK-005_flow_pack.md` 확인
3. Flow에서 NEW VIDEO GENERATION + Veo 3.1 Lite + 9:16 + output 1 + displayed cost 확인
4. **G1만 생성**
5. 결과 영상/스크린샷을 ChatGPT에 전달

```text
G1 만들었어. 봐줘
```

G1 PASS 후 actual last usable frame을 저장한 뒤에만 G2.

---

## 18. 다른 AI/개발자의 시작 순서

1. latest main SHA
2. recent commits/PRs
3. `PROJECT_HANDOFF.md`
4. `START_HERE.md`
5. `CURRENT_STANDARD.md`
6. `docs/22_continuous_episode_learning_engine.md`
7. `docs/23_minimum_credit_operator_architecture.md`
8. `production/NEXT_EPISODE.txt` + current manifest
9. `analytics/learning_ledger.csv`
10. `ideas/episode_backlog.yaml` + novelty signatures
11. `research/seasonal_evidence.yaml` + benchmark log
12. core tools/tests
13. concurrent changes/regression risk check before edits

Latest GitHub state always outranks stale assistant memory.

---

## 19. Handoff persistence rule

Material change examples:

- production standard
- Flow cost/feature assumption
- NEXT_EPISODE/manifest
- meaningful backlog score/ranking
- analytics/learning rule
- selection/originality algorithm
- actual production/performance data
- tool behavior/important bug fix
- operator interface
- meaningful future candidate

NO-OP examples:

- same-class seasonal PR repeat
- score/rank/timing/mechanic unaffected
- repo unchanged

Local git available:

```powershell
python tools/validate_handoff_update.py --base origin/main
```

---

## 20. 안전/금지 규칙

- Flow credits 자동 사용 금지
- paid generation 자동 실행 금지
- YouTube 자동 publish 금지
- competitor exact title/plot/brand/ending 복제 금지
- food/season 이름만 바꾼 동일 conflict+ending 반복 금지
- novelty signature rename으로 gate 우회 금지
- full-cat third-person 회귀 금지
- planned target keyframe을 actual previous frame으로 위장 금지
- previous scene FAIL 상태에서 next spend 금지
- 모든 episode를 H30 또는 H40으로 강제 금지
- 60초 padding 금지
- audio-only 문제로 좋은 video reroll 금지
- same-class seasonal PR churn 금지
- placeholder analytics 0을 failure처럼 학습 금지
- Cali/unrelated repository 수정 금지

---

## 21. Definition of Done

```text
current benchmark/JP signal research
→ candidate scoring + novelty gate
→ paw-only/tiny-scale production-safe manifest
→ 0-credit frame preflight
→ manifest-aware progressive Flow generation
→ actual-last-frame continuity chain
→ continuity QC
→ low-friction edit/export
→ upload
→ 24h/72h learning
→ next episode selection
```

Episode가 쌓일수록:

- first-pass generation success ↑
- usable motion/credit ↑
- engaged views/credit ↑
- subscribers/credit ↑
- operator manual judgment ↓
- continuity reroll ↓
- template story repetition ↓

이 실제 data로 보여야 한다.

---

## 22. Handoff change log

### 2026-08-27 — Runtime-aware operator guidance

Baseline: `main@fca5266acb7c40176b746d8954a5fef0aa19456d`.

Problem:

- adaptive runtime policy와 달리 `tools/make_short.ps1`, `tools/make_next_short.ps1`가 H30/3-generation을 고정 안내.
- TK-005는 `immersive_h40`라서 operator가 G4를 잘못 생략하거나 runtime source of truth를 혼동할 수 있었음.
- bundle index도 30~36s를 일반 권장해 H40 manifest와 충돌 가능.

Changes:

- fixed H30 guidance 제거
- Flow Pack/manifest를 episode-specific source of truth로 명시
- bundle에 runtime mode + preferred runtime 표시
- H30/H40 각각의 stop/continue 조건을 deterministic하게 출력
- `tools/test_build_episode_bundle_runtime.py` 추가

Unchanged:

- NEXT_EPISODE = TK-005
- TK-005 story/manifest/runtime = immersive_h40
- Flow credit assumptions
- candidate scores/ranking
- no paid generation / no publish

Fresh benchmark review found no decision-changing research signal, so no benchmark/backlog churn.

Next highest-value action remains **actual TK-005 G1 generation/QC**.

### 2026-08-27 — Explicit Flow frame-input map

- `tools/build_flow_pack.py` symbolic frame tokens → explicit First/Last operator actions
- PASS 후 actual frame 저장 안내
- frame-chain regression tests
- NEXT_EPISODE TK-005 unchanged

### 2026-08-27 — New-rice onigiri candidate

- IDEA-010 `8mm 新米塩むすび`
- actual rice reservation behavior + early-September timing
- triangular mold + broad paw press + slide-away reveal
- NEXT_EPISODE TK-005 unchanged

### 2026-08-26 — Deterministic novelty gate

- recent-five exact conflict+ending / hook+conflict+ending repeat block
- IDEA-009 future repeat, IDEA-002 recent gummy structure repeat blocked

### 2026-08-26 — Persistent handoff protocol

- root `PROJECT_HANDOFF.md` source of truth
- material change + same-PR handoff update mandatory
- `tools/validate_handoff_update.py`
