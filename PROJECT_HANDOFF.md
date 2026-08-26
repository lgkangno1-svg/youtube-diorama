# Tiny Cat Kitchen — PROJECT HANDOFF

Last handoff update: **2026-08-26 KST**  
Handoff baseline inspected before this update: `main@599d0e26ead1e962e0f47c0d348aad8e65c1f195`  
Repository: `lgkangno1-svg/youtube-diorama`

> 이 문서는 **다른 AI/개발자가 이전 대화를 전혀 보지 않아도 Tiny Cat Kitchen을 이어서 개발·운영할 수 있게 하는 인수인계 source of truth**다.
>
> **Material repository change가 있으면 반드시 같은 branch/PR에서 이 파일도 갱신한다.** 단순 조사 결과가 기존 의사결정 상태를 바꾸지 않아 repo를 NO-OP으로 유지하는 회차에는 이 파일도 억지로 수정하지 않는다.

---

## 1. 개발 의도 — 왜 이 프로젝트가 존재하는가

Tiny Cat Kitchen의 목표는 단순한 `AI 고양이 요리 영상 생성`이 아니다.

사용자가 매번 다음을 직접 하지 않아도 되는 운영체제를 만드는 것이 목적이다.

- 일본 Shorts 트렌드 조사
- 계절/기념일/제철 소재 탐색
- 에피소드 아이디어 발상
- Veo에서 실패하기 쉬운 동작 제거
- Flow 비용 계산
- 장면별 프롬프트 작성
- 캐릭터/카메라/소품 연속성 관리
- 최종 길이와 힐링 pacing 결정
- 업로드 후 24h/72h 성과 학습
- 다음 영상 후보 재평가
- 최근 에피소드와 구조적으로 겹치는 아이디어 자동 차단

사용자의 평소 인터페이스는 최대한 단순해야 한다.

```text
다음 영상 준비해줘
```

이 한 문장을 받으면 시스템이 조사 → 후보 선정 → manifest → `production/NEXT_EPISODE.txt`까지 준비하고, 사용자는 로컬에서 아래 명령만 실행하는 것을 목표로 한다.

```powershell
./tools/make_next_short.ps1
```

Flow에서는 한꺼번에 크레딧을 쓰지 않고 G1부터 순차 생성한다.

---

## 2. 최종 제품 목표

### 시청자에게 보이는 제품

일본 10~20대를 핵심 초기 타깃으로 하는 세로형 힐링 Shorts.

핵심 경험:

> **시청자가 고양이가 된 것처럼 1인칭으로 작업대를 내려다보고, 화면 아래의 고양이 앞발만으로 믿기 어려울 만큼 작은 디오라마 음식/물건을 조심스럽게 만드는 영상.**

귀여움의 핵심은 `고양이 얼굴`이 아니라 **앞발과 초소형 물체의 크기 대비**다.

### 운영자에게 보이는 제품

- 아이디어를 직접 관리하지 않아도 됨
- episode 번호를 외우지 않아도 됨
- Flow prompt를 매번 새로 쓰지 않아도 됨
- 생성 전 0-credit preflight로 큰 실패를 미리 차단
- G1이 틀리면 뒤 generation을 쓰지 않음
- 최근 5개 구조와 같은 conflict/ending 반복을 자동으로 차단
- 실제 성과가 쌓이면 runtime / action / hook / credit 전략이 자동으로 더 좋아짐

---

## 3. 절대 유지해야 하는 영상 정체성

Source of truth:

- `docs/24_hero_cat_brand_identity.md`
- `docs/25_pov_paws_microworld_grammar.md`
- `CURRENT_STANDARD.md`

### POV_PAWS_MICROWORLD_V1

기본 Shorts는 다음을 반드시 만족한다.

- true first-person cat POV
- 화면 아래에 `HERO_CAT_V1`의 cream + pale ginger **앞발 1~2개만** 등장
- 얼굴 / 눈 / 귀 / 머리 / 몸통 / 꼬리 / full cat 금지
- hero food/object는 보통 **5~20mm**
- 화면상 hero object는 한 앞발 폭의 대략 **15~50% 이하**
- macro close-up
- miniature diorama tabletop/workbench
- 카메라는 거의 고정, 아주 미세한 breathing drift만 허용
- 한 8초 generation = **1 primary tactile action + optional 1 micro-payoff**
- no rapid montage
- no meme zoom
- no third-person chef shot

예쁘더라도 다음은 구조적 FAIL이다.

- 고양이가 카운터 뒤에 서서 요리
- 고양이 얼굴/몸통/전신 노출
- 음식이나 팬이 paw와 비슷하거나 더 크게 보임
- 사람 손가락/엄지 발생
- 앞발이 사람처럼 도구를 움켜쥠
- 전체 주방이 주인공이 되어 tiny scale contrast가 약함

### Paw action grammar

Veo reliability를 위해 선호:

- nudge
- press
- pat
- roll
- steady
- slide
- tap

피함:

- chopsticks / tongs / knife를 손가락으로 grip
- thumb-index pinch
- precise twist
- 사람 손목처럼 회전

도구가 꼭 필요하면 넓은 면을 paw pad로 눌러 이동시키는 식으로 재설계한다.

---

## 4. 현재 캐릭터/세계관

### HERO_CAT_V1

프로필/배너에서는 얼굴을 보여줄 수 있지만 기본 Shorts에서는 앞발만 사용한다.

정체성:

- cream fur base
- pale ginger markings
- 실제 feline paw anatomy
- soft premium/healing tone

### KITCHEN_WORLD_V1

- cozy Japanese-inspired miniature environment
- warm wood / ceramic / paper / tiny stall / tiny workbench
- 과도한 장식보다 hero object가 먼저 읽혀야 함
- 계절 장식은 허용하지만 브랜드 제품/패키지 복제 금지

---

## 5. 현재 Flow 제작 전략

Source of truth:

- `docs/23_minimum_credit_operator_architecture.md`
- `docs/26_flow_ui_mode_preflight.md`
- `CURRENT_STANDARD.md`

### 생성 전 UI preflight

Google Flow UI와 가격은 바뀔 수 있으므로 실제 생성 직전 확인한다.

2026-08-26 공식 Google Flow 도움말 재확인 기준:

- Veo 3.1 Lite: 4/6/8s + Extend
- non-Ultra: 10 credits/generation
- output_count = 1을 직접 확인
- First + Last frames: Lite에서 4/6/8s 지원
- Ingredients/References와 Extend는 8s-only일 수 있음
- 1080p upscale: Plus/Pro/Ultra 0 credits
- Gemini Omni Flash 기존 영상 edit는 별도 고비용 경로이므로 G1/G2/G3 생성과 혼동 금지

**실제 UI 표시값이 최종 source of truth**다.

### Progressive Spend

```text
FREE keyframe/reference preflight
→ G1 8s
→ QC
→ actual last usable frame 저장
→ G2 only after PASS
→ QC
→ G3 only after PASS
→ H30 complete 가능
→ G4 only if immersive_h40 + G3 PASS + 독립 beat 존재
```

G2/G3/G4를 미리 생성하지 않는다.

### Sequential Frame Chain

G2는 G1의 실제 마지막 usable frame, G3는 G2, G4는 G3에서 이어간다.

목적:

- 동일 POV 유지
- paw fur/anatomy drift 감소
- hero-object scale 유지
- 음식 상태/소품 연속성 유지
- 조명/작업대 continuity 유지

---

## 6. Runtime 전략 — 몰입과 지루함 사이

현재는 `무조건 60초`를 목표로 하지 않는다.

### compact_h30

- 3 × 8s raw motion = 24s
- first-pass ceiling 약 30 credits
- 최종 약 30~36s
- 3개의 독립 beat로 `scale reveal → making → payoff`가 완결될 때

### immersive_h40

- 4 × 8s raw motion = 32s
- first-pass ceiling 약 40 credits
- 최종 약 38~46s
- G4가 단순 패딩이 아니라 `serving / world-resolution / paws withdraw / afterglow` 같은 독립 가치가 있을 때

### 48~60s

현재 기본값이 아니다.

실제 Tiny Cat Kitchen 24h/72h retention과 engaged-views/credit 데이터가 H40보다 더 긴 길이를 지지할 때만 실험한다.

---

## 7. 오디오 정책

기본:

```text
No narration
No generated music
Quiet room tone + close tiny ASMR
```

적합한 소리:

- tiny ceramic click
- wood scrape
- dry crumb / dough press
- subtle tiny sizzle
- paper rustle
- quiet steam / room ambience

영상이 좋고 생성 오디오만 이상하면 **영상 reroll 금지**. 후편집 SFX 교체를 우선한다.

일본어 사용자 녹음 나레이션은 화면만으로 의미 전달이 부족하거나 character/payoff를 명확히 강화할 때만 0~1문장 정도 검토한다.

---

## 8. 아이디어 선정 구조

Source of truth:

- `ideas/episode_backlog.yaml`
- `ideas/novelty_signatures.yaml`
- `tools/select_next_episode.py`
- `docs/28_episode_novelty_authenticity_gate.md`

현재 9축 base score:

- benchmark evidence — 10
- Japan relevance — 10
- healing fit — 15
- visual satisfaction — 15
- Flow reliability — 20
- originality — 10
- worldbuilding — 5
- audience demand — 5
- expected credit efficiency — 10

Production eligibility hard gate:

- `visual_grammar=POV_PAWS_MICROWORLD_V1`
- tiny-scale 명시
- paw-safe action family
- H30/H40 runtime prior
- 최근 episode fingerprint와 과도한 중복 없음

### Deterministic recent-episode novelty gate

2026-08-26부터 후보 선택 도구는 최근 5개 `episodes/TK-*.yaml`의 `episode_fingerprint`를 읽는다. 게시 전 `planned/ready` manifest도 이미 pipeline에 들어간 이야기이므로 recent window에 포함한다.

`ideas/novelty_signatures.yaml`의 후보 구조와 비교해 다음을 exact hard-block한다.

- 같은 `conflict_mechanic + ending_mechanic` pair
- 같은 `hook + conflict + ending` triple

의도적으로 exact comparison만 사용한다. AI fuzzy similarity를 사실처럼 자동 판정하지 않는다. 그보다 넓은 의미 유사성은 새 manifest 생성 전에 ChatGPT가 추가 검토한다.

현재 이 gate의 중요한 효과:

- `IDEA-009`는 이미 만들어진 TK-005 fingerprint와 동일하므로 **미래 후보로 다시 선택되지 않음**. 현재 `NEXT_EPISODE=TK-005`는 기존 production task이므로 변경하지 않는다.
- `IDEA-002`는 TK-004의 gummy physics tension + measurement proof 구조를 사실상 반복하므로 **최근 window 동안 미래 선택에서 차단**된다. 다시 쓰려면 실제 conflict/resolution을 바꿔야 한다.

### 왜 이 gate가 필요한가

2026-08-26 재확인한 YouTube 공식 channel monetization policy는 repetitive / mass-produced 콘텐츠를 `inauthentic content`로 명확히 다루며, 자동화 도구/템플릿을 사용하더라도 최종 영상에는 original creative vision과 실제 entertainment/educational value가 있어야 한다고 안내한다.

따라서 Tiny Cat Kitchen은 **브랜드 문법은 반복하되 이야기 substance까지 템플릿화하지 않는다.**

### Seasonal Search Lead

일본 계절형 후보는 base score를 덮어쓰지 않고 최대 +8의 bounded boost만 받는다.

기본 prior:

- peak 22~35일 전: early lead
- peak 8~21일 전: strongest lead
- peak 0~7일 전: strong final lead
- peak 기간: 유효하지만 선행 sweet spot보다 약간 낮음
- post-peak: 작은 tail

달력만으로 boost하지 않는다. `research/seasonal_evidence.yaml`의 최신 일본 근거가 있어야 한다.

---

## 9. 연구 정책 — 무엇을 기록하고 무엇을 버리는가

Source of truth:

- `research/benchmark_log.csv`
- `research/seasonal_evidence.yaml`
- `docs/27_research_evidence_saturation_gate.md`

경쟁 콘텐츠에서 복제 금지:

- exact title
- exact plot
- branded product
- package/design
- exact ending

추출하는 것:

- hook mechanic
- scale contrast
- tactile action
- pacing
- visual payoff
- seasonal timing
- worldbuilding mechanic

### Evidence saturation gate

이미 한 후보에 behavioral demand / independent nationwide activation / current survey / culturally dated activation 중 충분한 근거가 있으면, 같은 종류의 PR/상품 출시 뉴스를 계속 저장하지 않는다.

새 commit이 정당화되는 경우:

- candidate score/rank가 실제로 변함
- NEXT_EPISODE 또는 publish timing이 변함
- evidence class가 recognition → behavioral demand처럼 질적으로 변함
- 기존 가설과 충돌하는 근거
- 새 production mechanic 도출
- stale evidence refresh 필요
- 공식 Flow 가격/기능 변화
- 실제 Tiny Cat Kitchen production/performance data 발생
- deterministic tool이 문서상 필수 gate를 실제로 시행하지 못하는 gap 발견

목적은 `뉴스 수집`이 아니라 **의사결정 개선**이다.

---

## 10. 현재 실제 제작 상태

### NEXT_EPISODE

`production/NEXT_EPISODE.txt` = **TK-005**

현재 episode:

**`猫の前足で作る、12mmの焼きいも。`**

Manifest: `episodes/TK-005.yaml`

현재 runtime mode: `immersive_h40`

핵심 4 beat:

1. **Impossible scale reveal** — 12mm 보라색 고구마 + paw 대비
2. **Slow roast / crack** — 같은 tiny tray를 heat 쪽으로 이동, 껍질이 천천히 어두워지고 crack
3. **Golden center reveal** — tray를 불에서 살짝 밀어낸 후 잔열로 기존 crack이 자연스럽게 벌어짐
4. **World resolution** — 같은 tray를 tiny serving niche로 밀고 paws가 빠짐, steam만 남음

연속성 중요사항:

- G1~G4 같은 roasting tray 유지
- 새 접시/도구 갑자기 등장 금지
- 고구마를 paw로 집거나 pinch하지 않음
- G3의 reveal은 passive residual-heat transformation으로 설계

### 현재 실제 실패 데이터

`analytics/learning_ledger.csv`에 `POV-PREFLIGHT-001`이 기록되어 있다.

관찰된 실패:

- third-person full cat
- body visible
- object scale too large
- human-like tool-use risk

이 실패를 음식 소재 실패로 해석하지 않는다.

학습:

- true first-person camera hard gate
- front paws only hard gate
- hero object <= 0.50 paw width
- nudge / press / slide 중심으로 action grammar 강화

현재 실제 24h/72h 게시 성과 데이터는 아직 없다.

---

## 11. 현재 후보 상태 요약

### 현재 production task — IDEA-009 / TK-005 12mm 焼きいも

- 이미 TK-005로 production-ready
- visual satisfaction / Flow reliability / credit efficiency가 강함
- broad autumn season
- novelty gate 도입 후에는 **새 future episode로 다시 선택하지 않음**
- 지금 가장 중요한 것은 추가 연구가 아니라 실제 G1 production result

### 다음 유력 계절 후보 — IDEA-001 8mm 月見だんご

- 일본 relevance와 seasonality 강함
- 2026-09-25 十五夜를 향해 선행 window가 커질 후보
- yolk/customer 같은 복잡한 구조를 버리고 paw-safe roll/slide 형태로 단순화됨
- recent exact conflict/ending duplicate에는 해당하지 않음

### IDEA-002 3mm グミ

- 9/3 グミの日 타이밍과 texture payoff는 강함
- 하지만 현재 abstract conflict + ending이 TK-004와 동일 계열이 아니라 **exact same pair로 선언되어 deterministic gate에서 차단**
- 단순 제목/색상 변경으로 우회 금지. 실제 conflict/resolution을 새로 설계한 뒤 signature를 바꿔야 함

### IDEA-006 10mm 栗ごはん

- 9월 초~가을 recognition 증가
- steam reveal과 tiny clay-pot worldbuilding 적합
- recent exact structural duplicate 없음

현재 NEXT_EPISODE를 매시간 뒤집지 않는다. TK-005를 실제로 만들어 production data를 얻는 것이 더 높은 가치다.

---

## 12. 구현되어 있는 주요 도구

중요 deterministic tools:

- `tools/select_next_episode.py` — backlog / seasonal timing + **recent-five novelty gate** 기반 후보 확인
- `ideas/novelty_signatures.yaml` — backlog 후보의 abstract hook/conflict/ending signature
- `tools/validate_current_standard.py` — stale manifest / POV / runtime 규칙 차단
- `tools/build_flow_pack.py` — episode manifest → 저토큰 Flow prompt pack
- `tools/build_healing_edit_plan.py` — runtime/pacing edit plan
- `tools/score_credit_efficiency.py` — actual production 성과 대비 credits 분석
- `tools/make_next_short.ps1` — `NEXT_EPISODE`를 읽어 사용자용 bundle 생성
- `tools/validate_handoff_update.py` — material change에 `PROJECT_HANDOFF.md`가 빠졌는지 로컬에서 검증

자동 bundle 산출물:

- `generated/TK-XXX_bundle.md`
- `generated/TK-XXX_flow_pack.md`
- `generated/TK-XXX_edit_plan.md`
- `generated/TK-XXX_publish_pack.md`

준비 단계에서는 Flow/LLM/API 크레딧을 쓰지 않아야 한다.

---

## 13. 성과 학습 구조

Source of truth: `analytics/learning_ledger.csv`

가능한 경우 기록:

### Production

- flow strategy
- runtime mode
- actual Flow credits
- rerolls
- G1/G2/G3/G4 first-pass success
- POV failure
- scale failure
- anatomy failure
- continuity failure
- failed action type
- usable motion seconds
- audio replacement
- final length
- beat drop-off note

### Audience 24h / 72h

- Stayed to watch
- APV
- engaged views
- subscribers gained
- comments

장기 최적화 지표:

```text
usable motion / credit
engaged views / credit
subscribers / 100 credits
```

단순히 `credits/video`를 낮추는 것이 목적이 아니다. 더 많은 engaged views와 subscriber conversion을 만드는 영상이면 합리적인 H40은 H30보다 우수할 수 있다.

---

## 14. 개발 완료 상태

현재까지 완료된 핵심 기반:

- [x] 일본 타깃 채널 기본 컨셉
- [x] POV paws-only visual grammar 고정
- [x] tiny-object scale hard gate
- [x] paw-safe action grammar
- [x] H30/H40 adaptive runtime 정책
- [x] Progressive Spend
- [x] sequential actual-frame chaining 정책
- [x] no narration / no generated music 기본 오디오 정책
- [x] seasonal lead-time scoring
- [x] seasonal evidence freshness/saturation 정책
- [x] backlog 9축 scoring
- [x] 최근 5개 conflict/ending exact-duplicate deterministic selection gate
- [x] YouTube authenticity/anti-template 운영 원칙 문서화
- [x] Flow UI generation/edit-mode 혼동 방지 문서
- [x] production manifest validator
- [x] deterministic Flow prompt pack
- [x] deterministic edit plan
- [x] credit-efficiency scorer
- [x] 실제 Flow 실패를 learning ledger에 반영하는 구조
- [x] TK-005 12mm 焼きいも production-ready manifest
- [x] PROJECT_HANDOFF 운영 문서

아직 완료되지 않은 핵심:

- [ ] TK-005의 실제 새 POV G1 생성 및 QC
- [ ] G1→G2→G3→조건부 G4 실제 continuity 검증
- [ ] 실제 final export 편집 검증
- [ ] 첫 YouTube 게시
- [ ] 실제 24h/72h analytics 수집
- [ ] H30 vs H40 실채널 retention 비교
- [ ] paw action type별 first-pass success prior 학습
- [ ] usable motion/credit 실제 baseline 구축
- [ ] engaged views/credit / subscribers/credit baseline 구축
- [ ] season lead timing이 실제 성과에 도움이 되는지 검증
- [ ] novelty gate가 너무 엄격하거나 느슨한지 실제 episode 누적 후 검증

---

## 15. 앞으로의 개발 플랜

### Phase A — Production truth 확보

최우선.

1. TK-005 G1을 현재 POV grammar로 실제 생성
2. `POV / SCALE / ANATOMY / CAMERA / PROP` QC
3. PASS일 때만 G2
4. actual last usable frame chaining 검증
5. G3까지 완결성 확인
6. G4는 world-resolution 가치가 실제로 있을 때만 생성
7. 실제 credits / rerolls / usable seconds 기록

성공 기준:

- full-cat 재등장 없음
- tiny object scale 즉시 읽힘
- paw anatomy 안정
- human grip 없음
- 동일 tray / food state continuity
- 재생성 횟수 최소화

### Phase B — First published Shorts learning

첫 게시 후:

- 24h metrics 기록
- 72h metrics 기록
- STW/APV와 beat별 이탈 가능성 해석
- engaged views/credit
- subscribers/100 credits
- 댓글의 tiny/healing/next-food audience signal 추출

한 편 데이터로 과도한 결론을 내리지 않는다.

### Phase C — Runtime experiment

여러 편 누적 후:

- compact_h30 30~36s
- immersive_h40 38~46s

을 같은 observation horizon에서 비교한다.

### Phase D — Production reliability model

충분한 episode가 생기면 action family별 prior를 만든다.

예:

- nudge first-pass rate
- press first-pass rate
- slide first-pass rate
- passive material transformation success
- liquid pour failure rate
- deformable gummy drift rate

후보 scoring의 `Flow reliability / expected credit efficiency`에 실제 데이터로 반영한다.

### Phase E — Seasonal timing learning

현재 8~21일 pre-peak sweet spot은 초기 prior일 뿐이다.

실제 seasonal episode를 통해 publish date → peak까지 남은 일수와 STW/APV/engaged views/credit/subscriber conversion을 비교한다.

### Phase F — Originality / authenticity learning

현재 novelty gate는 exact structural repeat만 fail-closed한다.

실제 episode가 늘어나면:

- 같은 hook family를 얼마나 자주 반복해도 피로하지 않은지
- world-state change가 subscriber conversion에 도움이 되는지
- seasonal 소재만 바꾼 template episode가 실제로 약한지

를 데이터로 검증한다.

fuzzy AI similarity score를 근거 없이 hard gate로 승격하지 않는다.

### Phase G — 운영 자동화 단순화

장기적으로 사용자 경험을 다음까지 줄인다.

```text
사용자: 다음 영상 준비해줘
AI: 다음 후보 선정 + manifest/NEXT_EPISODE 준비 완료
사용자: ./tools/make_next_short.ps1
사용자: G1 만들었어. 봐줘
AI: PASS / EDITABLE / REROLL / STOP
```

---

## 16. 다음 작업 우선순위

현재 시점의 우선순위:

1. **TK-005 실제 G1 결과 확보** — 가장 가치가 높음
2. G1 first-person/front-paws-only/tiny-scale 재현성 검증
3. 실제 Flow 표시 모델/비용 기록
4. G2 sequential frame chain 검증
5. G3/G4 prop continuity 검증
6. 첫 export 길이 38~46s가 실제로 지루하지 않은지 검토
7. 첫 게시 후 24h/72h 데이터 확보
8. 그 다음 backlog score/runtime prior/novelty prior를 실제 성과로 조정

현재는 추가 계절 PR 수집보다 **실제 production truth**가 더 중요하다.

---

## 17. 사용자가 해야 하는 일

현재 사용자가 직접 해야만 하는 부분은 최소화한다.

당장 필요한 실제 행동:

1. Flow에서 새 video generation 상태인지 확인
2. TK-005 G1만 생성
3. 결과 영상/스크린샷을 ChatGPT에 전달

말은 간단히:

```text
G1 만들었어. 봐줘
```

그 뒤 ChatGPT가 다음 spend 여부를 판단한다.

Flow 크레딧 사용, paid video generation, YouTube publish는 사용자 명시 행동 없이 자동 수행하지 않는다.

---

## 18. 다른 AI/개발자가 작업을 시작할 때 반드시 하는 순서

이전 대화 기억을 최신 상태라고 가정하지 않는다.

1. 최신 `main` SHA 확인
2. 최근 commits / PR 확인
3. `PROJECT_HANDOFF.md` 읽기
4. `START_HERE.md` 읽기
5. `CURRENT_STANDARD.md` 읽기
6. `docs/22_continuous_episode_learning_engine.md` 읽기
7. `docs/23_minimum_credit_operator_architecture.md` 읽기
8. `production/NEXT_EPISODE.txt` + 해당 manifest 확인
9. `analytics/learning_ledger.csv` 확인
10. `ideas/episode_backlog.yaml` + `ideas/novelty_signatures.yaml` + research evidence 확인
11. 다른 AI가 중간에 수정했을 가능성을 전제로 충돌/회귀 위험 확인
12. 그 다음에만 수정 시작

절대 다른 저장소(Cali 등)를 건드리지 않는다.

---

## 19. Material change 후 인수인계 갱신 규칙

**모든 material repository update에서 `PROJECT_HANDOFF.md`도 같은 PR에 포함한다.**

최소 갱신 항목:

- `Last handoff update`
- 현재 main/base 상태 또는 작업 시작 SHA
- `개발 완료 상태`
- `현재 실제 제작 상태`
- `앞으로의 개발 플랜`에서 완료/변경된 항목
- `다음 작업 우선순위`
- 새로운 중요한 의사결정/실패/학습
- Change log

다음은 material change로 본다.

- production standard 변경
- Flow cost/feature assumption 변경
- NEXT_EPISODE 변경
- episode manifest 제작 구조 변경
- backlog score/ranking 의미 있는 변경
- analytics/learning 규칙 변경
- candidate selection algorithm 변경
- originality/novelty gate 변경
- 새로운 실제 production/performance data
- tools 동작 변경
- 중요한 bug fix
- 운영 인터페이스 변경

다음은 handoff 변경을 강제하지 않는 NO-OP 상황이다.

- 의미 없는 동일 종류 PR 기사 하나 추가
- 의사결정에 영향 없는 연구 중복
- repo 자체를 전혀 수정하지 않는 회차

**새 코드/문서만 바꾸고 handoff를 빼먹는 PR은 완료로 보지 않는다.**

---

## 20. 변경 금지 / 안전 규칙

- Flow credits 자동 사용 금지
- paid generation 자동 실행 금지
- YouTube 자동 publish 금지
- 경쟁작 exact title/plot/brand/ending 복제 금지
- food/season/name만 바꾼 동일 conflict+ending 반복 금지
- novelty signature 이름만 바꿔 gate 우회 금지
- full-cat third-person으로 회귀 금지
- 60초를 채우기 위한 padding 금지
- 좋은 영상의 오디오만 문제라고 영상 reroll 금지
- 같은 계절 홍보성 증거를 매시간 commit하는 research churn 금지
- placeholder analytics 0을 실제 실패 데이터처럼 학습 금지
- Cali 또는 unrelated repo 수정 금지
- 이전 assistant memory를 최신 GitHub 상태보다 우선하지 않기

---

## 21. Definition of Done

이 프로젝트의 개발 완료는 단순히 스크립트가 존재하는 상태가 아니다.

최종적으로 다음이 반복 가능해야 한다.

```text
아이디어 조사
→ 일본 타이밍 판단
→ recent-episode novelty gate
→ paw-only/tiny-scale production-safe manifest
→ 0-credit frame preflight
→ progressive Flow generation
→ continuity QC
→ low-friction edit/export
→ upload
→ 24h/72h learning
→ next episode selection
```

그리고 실제 데이터가 쌓일수록:

- first-pass generation 성공률 상승
- usable motion / credit 상승
- engaged views / credit 상승
- subscribers / credit 상승
- 사용자 수동 프롬프트 작업 감소
- 동일 template story 반복 감소

가 나타나는 것이 최종 성공 기준이다.

---

## 22. Change log

### 2026-08-26 — Deterministic recent-episode novelty gate

- 운영 문서에는 최근 5개 fingerprint 중복 제거가 있었지만 실제 `tools/select_next_episode.py`는 이를 자동 수행하지 않고 사람에게 확인을 넘기고 있던 gap을 발견.
- `ideas/novelty_signatures.yaml`을 추가해 backlog 후보의 abstract hook/conflict/ending mechanics를 명시.
- selector가 최근 5개 episode manifest의 `episode_fingerprint`를 읽고 동일 conflict+ending pair 또는 동일 hook+conflict+ending triple을 hard-block하도록 변경.
- 계획/ready manifest도 recent window에 포함해 아직 게시되지 않은 production pipeline story와의 중복도 방지.
- 현재 결과상 IDEA-009는 TK-005의 future repeat이므로 재선택 차단, IDEA-002는 TK-004와 동일 구조라 recent window에서 차단. 현재 NEXT_EPISODE TK-005 자체는 변경 없음.
- `docs/28_episode_novelty_authenticity_gate.md`에 현재 YouTube 공식 inauthentic/repetitive content 정책과 Tiny Cat Kitchen용 anti-template 해석을 기록.
- Flow 공식 가격/기능은 2026-08-26 재확인했고 기존 Veo 3.1 Lite progressive-spend 가정을 바꿀 근거 없음.

### 2026-08-26 — Handoff persistence introduced

- `PROJECT_HANDOFF.md`를 프로젝트 최상위 인수인계 source of truth로 도입.
- 현재 POV paws-only / tiny-scale / adaptive H30-H40 / sequential-frame / seasonal-learning 구조를 한 문서에서 복구 가능하게 정리.
- 현재 NEXT_EPISODE TK-005와 실제 `POV-PREFLIGHT-001` 실패 학습 상태 기록.
- 앞으로 material repo update와 handoff update를 같은 PR에 포함하는 규칙 도입.
- GitHub Actions에 의존하지 않는 handoff-sync 검증을 추가.
