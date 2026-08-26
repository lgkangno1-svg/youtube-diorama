# Tiny Cat Kitchen — PROJECT HANDOFF

Last handoff update: **2026-08-27 KST**  
Work-start baseline inspected for this update: `main@3acb910ace84eb22c5f37b7f0c46c7117d951630`  
Repository: `lgkangno1-svg/youtube-diorama`

> 이 파일은 다른 AI/개발자가 이전 대화 없이도 프로젝트를 이어갈 수 있게 하는 인수인계 source of truth다.
>
> **모든 material repository change는 같은 branch/PR에서 이 파일도 갱신해야 완료로 본다.** 실제 의사결정이 바뀌지 않는 NO-OP 연구 회차에는 날짜만 바꾸지 않는다.

---

## 1. 개발 의도

Tiny Cat Kitchen은 단순한 AI 고양이 영상 생성기가 아니라 **일본 타깃 Shorts 운영체제**다.

사용자가 매번 다음을 직접 하지 않아도 되게 하는 것이 목적이다.

- 일본/글로벌 AI-cat, miniature cooking, ASMR, relaxing-food 트렌드 조사
- 일본 계절/문화/음식/소셜 신호 탐색
- 경쟁작 복제 없이 성공 메커니즘만 추출
- 다음 episode 후보 발상/점수화
- Veo 실패 가능성이 높은 동작 제거
- Flow generation 수와 크레딧 계획
- POV/scale/paw anatomy/continuity 설계
- 장면별 prompt/frame chain 생성
- H30/H40 runtime 선택
- 업로드 후 24h/72h 성과 기록과 다음 episode 학습

정상 사용자 인터페이스는 최대한 단순해야 한다.

```text
다음 영상 준비해줘
```

ChatGPT가 research → candidate selection → episode manifest → `production/NEXT_EPISODE.txt` → handoff 동기화까지 준비하고, 사용자는 로컬에서:

```powershell
./tools/make_next_short.ps1
```

을 실행하는 구조가 목표다.

**Flow credits 사용, paid video generation, YouTube publish는 사용자 명시 행동 없이 자동 실행하지 않는다.**

---

## 2. 최종 채널 목표

초기 핵심 타깃은 일본 10~20대.

시청자 경험:

> **시청자가 고양이가 된 것처럼 1인칭으로 작업대를 내려다보고, 화면 아래의 고양이 앞발만으로 믿기 어려울 만큼 작은 디오라마 음식/물건을 조심스럽게 만드는 힐링 Shorts.**

핵심 귀여움은 고양이 얼굴이 아니라 **앞발과 초소형 물체의 압도적 크기 대비**다.

운영자 관점 최종 목표:

- episode 번호/프롬프트/Flow 순서를 외울 필요 없음
- 0-credit frame/reference preflight로 구조적 실패 선차단
- G1 실패 시 G2/G3/G4 비용 미사용
- manifest가 runtime/scene count/spend source of truth
- generated Flow Pack이 First/Last frame input을 직접 안내
- 실제 production + YouTube data가 쌓일수록 engaged views/credit와 subscribers/credit가 개선

---

## 3. 절대 유지할 영상 정체성

Canonical docs:

- `CURRENT_STANDARD.md`
- `docs/24_hero_cat_brand_identity.md`
- `docs/25_pov_paws_microworld_grammar.md`

### POV_PAWS_MICROWORLD_V1

Hard requirements:

- true first-person cat POV
- 화면 아래 `HERO_CAT_V1` cream + pale ginger 앞발 1~2개만 등장
- 얼굴/눈/귀/머리/몸통/꼬리/full cat 금지
- hero food/object 보통 5~20mm
- hero object는 화면상 한 앞발 폭의 약 15~50% 이하
- macro miniature diorama workbench
- mostly locked camera, subtle breathing drift 정도만 허용
- 한 8초 generation = **1 primary tactile action + optional 1 micro-payoff**
- no rapid montage / no meme zoom / no third-person chef shot

구조적 FAIL:

- 고양이가 카운터 뒤에 서서 요리
- 얼굴/몸통/전신 노출
- 음식/팬이 paw와 비슷하거나 더 큼
- human fingers/thumbs
- paw가 사람처럼 chopsticks/tongs/knife를 grip
- wide shot 때문에 tiny-scale contrast가 약함

Paw-safe actions:

- nudge
- press
- pat
- roll
- steady
- slide
- tap

피할 것:

- thumb-index pinch
- precise twist
- human wrist rotation
- human-like tool grip

---

## 4. 캐릭터/세계관

### HERO_CAT_V1

- cream fur base
- pale ginger markings
- realistic feline paw anatomy
- soft premium/healing tone
- profile/banner에서는 얼굴 가능, 기본 Shorts에서는 front-paws-only

### KITCHEN_WORLD_V1

- cozy Japanese-inspired miniature environment
- warm wood / ceramic / paper / tiny stall / tiny workbench
- hero object가 장식보다 먼저 읽혀야 함
- 계절 요소는 허용하지만 브랜드 제품/패키지/캠페인 복제 금지

---

## 5. Flow/Veo 운영 기준

Source of truth:

- `docs/23_minimum_credit_operator_architecture.md`
- `docs/26_flow_ui_mode_preflight.md`
- `CURRENT_STANDARD.md`
- `tools/validate_current_standard.py`
- `tools/build_flow_pack.py`

### 2026-08-27 공식 Google Flow 재확인

Production assumption 변경 없음.

- Veo 3.1 Lite 4s/6s/8s + Extend: non-Ultra 10 credits/generation
- First + Last frames: Lite 4/6/8s 지원
- output count = 1
- 1080p upscale: Plus/Pro/Ultra 0 credits
- Ingredients/References 및 Extend는 mode에 따라 8s-only 가능
- actual UI displayed cost를 생성 직전 최종 확인
- `수정 사항 설명` / Omni Flash edit 화면을 새 Veo generation으로 착각하지 않음

공식 확인 출처:

- Google Flow credit help
- Google Flow models & supported features
- Google Flow create-video help

### Progressive Spend

```text
FREE keyframe/reference preflight
→ G1 only
→ QC
→ actual last usable frame 저장
→ G2 only after G1 PASS
→ QC
→ G3 only after G2 PASS
→ compact_h30이면 종료 가능
→ G4 only if immersive_h40 + G3 PASS + independent value still exists
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

- planned `KF*` = 목표 상태
- `ACTUAL_LAST_USABLE_FRAME_Gn` = 실제 PASS clip에서 저장한 frame
- planned target frame을 previous actual frame 대신 쓰지 않는다.

---

## 6. Runtime 정책

### compact_h30

- 정확히 3개 first-pass Lite scenes
- raw motion 24s
- first-pass ceiling 30 credits
- final 약 30~36s
- scale reveal → making → payoff가 3 beat로 완결될 때

### immersive_h40

- 정확히 4개 first-pass Lite scenes
- raw motion 32s
- first-pass ceiling 40 credits
- final 약 38~46s
- G4가 serving / paws withdraw / world-resolution / afterglow 같은 독립 가치가 있을 때

48~60s는 기본값이 아니다. 실제 Tiny Cat Kitchen retention과 engaged-views/credit가 지지할 때만 실험한다.

### 2026-08-27 runtime operator fix

이미 반영 완료:

- `make_short.ps1` / `make_next_short.ps1`의 hardcoded H30 안내 제거
- bundle/Flow Pack이 manifest runtime을 따름
- compact_h30은 G3에서 종료
- immersive_h40은 G3 PASS 후 documented G4 value가 있을 때만 진행
- `tools/test_build_episode_bundle_runtime.py` 회귀 테스트 존재

---

## 7. 이번 회차 추가된 Manifest Spend Consistency Gate

### 발견한 문제

`tools/validate_current_standard.py`가 visual/POV/scene 길이는 검사했지만 다음 모순은 완전히 차단하지 못했다.

- manifest scenes는 3개인데 `max_lite_generations_first_pass=4`
- 3 generations인데 first-pass credit budget이 40으로 남아 있음
- `compact_h30`인데 G4가 조용히 추가됨
- `immersive_h40`인데 실제 scenes가 3개뿐임
- scene ID가 G1/G2/G3 순서와 다름
- first+last scene인데 required frame이 비어 있음

이런 stale manifest는 **Flow Pack 자체는 정상 생성되면서 operator에게 잘못된 spend ceiling/scene count를 보여줄 수 있어 실제 크레딧 낭비로 연결될 수 있는 운영 버그**다.

### 수정

`tools/validate_current_standard.py`가 이제 fail-closed로 검사한다.

- `max_lite_generations_first_pass == len(scenes)` 필수
- 현재 non-Ultra Lite 기준 `first_pass_credit_budget == generations × 10`
- `compact_h30 == 정확히 3 scenes / 30 credits`
- `immersive_h40 == 정확히 4 scenes / 40 credits`
- immersive_h40의 `minimum_distinct_motion_beats >= 4`
- G4 사용 시 `fourth_beat_value` 필수
- scene IDs는 G1..Gn 순서
- generation type은 `first_plus_last` 또는 `extend`
- first+last는 start/end frame 필수
- extend는 source_scene 필수
- G2/G3/G4 sequential actual-frame chain 유지

새 회귀 테스트:

- `tools/test_validate_current_standard.py`

이 gate는 Flow를 호출하지 않으며 **0 credits**다.

### 가격 변경 시 주의

validator의 `CURRENT_NON_ULTRA_LITE_CREDITS_PER_GENERATION = 10`은 현재 공식 Flow 가격을 반영한 값이다. Google이 가격을 바꾸면 공식 문서/UI 확인 후 이 값과 관련 docs/manifests를 같은 변경에서 갱신해야 한다.

---

## 8. 오디오 정책

기본:

```text
No narration
No generated music
Quiet room tone + close tiny ASMR
```

영상 motion이 좋고 generated audio만 나쁘면 video reroll하지 않는다. post SFX 교체를 우선한다.

일본어 사용자 녹음 line은 화면만으로 comprehension/payoff가 부족할 때만 짧게 사용한다.

---

## 9. Research / idea policy

Source of truth:

- `research/benchmark_log.csv`
- `research/seasonal_evidence.yaml`
- `ideas/episode_backlog.yaml`
- `ideas/novelty_signatures.yaml`
- `docs/27_research_evidence_saturation_gate.md`
- `docs/28_episode_novelty_authenticity_gate.md`

후보 9축:

- benchmark evidence
- Japan relevance
- healing fit
- visual satisfaction
- Veo reliability
- originality
- worldbuilding
- audience demand
- expected credit efficiency

원칙:

- 경쟁작 exact title/plot/brand/package/ending 복제 금지
- 성공한 hook/scale/action/pacing/payoff/worldbuilding mechanic만 추출
- 최근 5 episode의 동일 conflict+ending 또는 hook+conflict+ending exact repeat 차단
- same-class seasonal PR가 이미 포화면 repo churn 금지
- actual behavioral demand / contradictory evidence / ranking change / new production mechanic / Flow change / actual production data가 생길 때 우선 갱신

현재 알려진 후보 상태:

- IDEA-009 yakiimo: TK-005로 이미 production 준비됨; future repeat selection은 novelty gate로 차단
- IDEA-001 8mm 月見だんご: priority future candidate
- IDEA-010 8mm 新米塩むすび: behavioral rice-reservation evidence 기반 future candidate
- IDEA-002 gummy: TK-004 recent structure와 conflict/ending이 겹쳐 현재 future selection 차단

이번 회차 fresh research에서 기존 의사결정을 바꿀 만큼 새로운 benchmark/seasonal evidence는 확인되지 않아 benchmark/backlog는 변경하지 않았다.

---

## 10. 현재 실제 제작 상태

`production/NEXT_EPISODE.txt` = **TK-005**

Episode:

```text
猫の前足で作る、12mmの焼きいも。
```

Manifest: `episodes/TK-005.yaml`

Runtime: `immersive_h40`

4 beats:

1. impossible scale reveal — 12mm purple sweet potato + paws
2. slow roast / skin crack
3. tray slide away + residual-heat golden center reveal
4. same tray → tiny serving niche, paws withdraw, steam remains

Continuity hard rules:

- same roasting tray G1~G4
- no surprise new plate/cookware
- paw never pinches sweet potato
- G3 reveal is passive residual-heat transformation
- G2 First = actual last usable frame from G1
- G3 First = actual last usable frame from G2
- G4 First = actual last usable frame from G3

**현재 다음 가장 가치 있는 실전 단계는 TK-005 G1을 실제로 생성하고 QC하는 것**이다. 자동화가 Flow credit를 대신 쓰지는 않는다.

---

## 11. 현재 실제 production learning

`analytics/learning_ledger.csv`에 실제 preflight 실패가 기록되어 있다.

관찰된 실패:

- third-person full-cat
- body visible
- scale too large
- human-like tool use risk

따라서 hard gate:

- true first-person camera
- front paws only
- hero object <= 0.50 paw width
- nudge/press/slide 중심

아직 충분한 24h/72h public performance sample은 없다. placeholder 0을 실제 failure/zero performance처럼 학습하지 않는다.

장기 KPI:

```text
usable motion / credit
engaged views / credit
subscribers / 100 credits
```

---

## 12. 완료된 주요 구축

- PROJECT_HANDOFF persistence protocol
- START_HERE source-of-truth ordering
- HERO_CAT_V1 / KITCHEN_WORLD_V1
- POV_PAWS_MICROWORLD_V1
- Progressive Spend
- Sequential actual-frame chaining
- Flow UI generation-vs-edit preflight
- adaptive H30/H40 runtime
- deterministic novelty/authenticity gate
- seasonal evidence saturation/no-churn gate
- Japanese seasonal candidate scoring
- generated Flow Pack explicit First/Last frame mapping
- runtime-aware PowerShell operator guidance
- manifest spend consistency fail-closed validation
- local tests for frame chain/runtime/novelty/manifest consistency

---

## 13. 앞으로의 플랜

### Phase A — 실제 TK-005 production truth 확보

1. free opening/target frame preflight
2. G1 only
3. POV / scale / anatomy / camera / action QC
4. PASS 시 actual last usable frame 저장
5. G2 → G3 → 조건 충족 시 G4
6. actual credits/rerolls/usable seconds/failure type 기록

### Phase B — 첫 공개 Shorts 성과 학습

24h/72h:

- Stayed to watch
- APV
- engaged views
- subscribers
- comments
- final runtime
- credits
- rerolls

을 `analytics/learning_ledger.csv`에 기록.

### Phase C — H30 vs H40 학습

실제 episodes가 쌓이면 compact_h30과 immersive_h40의:

- engaged views/credit
- subscribers/100 credits
- APV
- beat drop-off

비교.

### Phase D — 반복 가능한 operator automation 강화

- 실제 Flow UI 변화가 생기면 docs/tooling 갱신
- manifest validation을 production history와 연결
- user input을 가능한 `다음 영상 준비해줘` 한 문장으로 축소

### Phase E — worldbuilding 확대

성과가 지지할 때만 tiny stall / rainy shop / after-hours bakery / seasonal ritual 등을 확장. 동일 template story 반복 금지.

---

## 14. 다음 작업 우선순위

현재 우선순위:

1. **TK-005 실제 G1 production/QC 데이터**
2. actual last usable frame chain 검증
3. actual credits/rerolls/usable seconds 기록
4. 첫 공개 episode 24h/72h data 확보
5. 이후에만 runtime/action/idea prior 재조정

추가 retail/PR 기사 수집은 지금 우선순위가 아니다.

---

## 15. 작업 시작 규칙

다른 AI/개발자는 항상:

1. 최신 main SHA 확인
2. recent commits/PRs 확인
3. `PROJECT_HANDOFF.md` 읽기
4. `START_HERE.md`
5. `CURRENT_STANDARD.md`
6. `docs/22_continuous_episode_learning_engine.md`
7. `docs/23_minimum_credit_operator_architecture.md`
8. `production/NEXT_EPISODE.txt`
9. current episode manifest
10. research/backlog/learning ledger

순으로 교차검증하고 작업한다.

이전 대화나 오래된 automation prompt를 최신 상태로 가정하지 않는다.

---

## 16. Handoff persistence gate

Material repository change:

```text
code/docs/tool/manifest/backlog/research/analytics change
→ PROJECT_HANDOFF.md same branch/PR update
→ local validation when available
→ PR review
→ merge
```

로컬 git 사용 가능 시:

```powershell
python tools/validate_handoff_update.py --base origin/main
```

NO-OP 연구는 handoff를 억지로 변경하지 않는다.

---

## 17. 안전/금지 규칙

- Flow credits 자동 사용 금지
- paid video generation 자동 실행 금지
- YouTube 자동 publish 금지
- competitor exact title/plot/brand/ending 복제 금지
- same story를 food 이름만 바꿔 반복 금지
- full-cat third-person 회귀 금지
- planned target frame을 actual previous frame으로 위장 금지
- previous scene FAIL 상태에서 next spend 금지
- scene count / runtime / credit budget 불일치 허용 금지
- 모든 episode를 무조건 H30/H40/60초로 강제 금지
- audio-only 문제로 좋은 video reroll 금지
- placeholder analytics 0을 실제 성과로 학습 금지
- Cali 또는 unrelated repo 수정 금지

---

## 18. Definition of Done

```text
current benchmark/JP signal research
→ scored + novelty-safe candidate
→ POV/tiny-scale production-safe manifest
→ manifest spend consistency PASS
→ 0-credit frame preflight
→ progressive Flow generation
→ actual-last-frame continuity chain
→ edit/export
→ upload
→ 24h/72h learning
→ next episode prior update
```

프로젝트가 좋아지고 있다는 증거는 단순 commit 수가 아니라:

- first-pass success ↑
- usable motion/credit ↑
- engaged views/credit ↑
- subscribers/credit ↑
- continuity rerolls ↓
- operator manual judgment ↓
- repetitive story fingerprints ↓

여야 한다.

---

## 19. Change log

### 2026-08-27 — Manifest spend consistency fail-closed gate

Baseline: `main@3acb910ace84eb22c5f37b7f0c46c7117d951630`.

Problem:

- validator가 scenes/runtime/spend metadata의 모순을 일부 허용할 수 있었음.
- stale manifest가 Flow Pack의 scene count/credit ceiling을 잘못 안내하면 실제 크레딧 낭비 가능.

Changes:

- exact scene-count ↔ declared generation-count gate
- exact current non-Ultra Lite first-pass budget gate
- compact_h30=3 / immersive_h40=4 deterministic consistency
- scene IDs / required frame/source validation
- `tools/test_validate_current_standard.py` 추가

Unchanged:

- NEXT_EPISODE = TK-005
- TK-005 story/runtime/manifest
- candidate ranking
- Flow official pricing assumption
- no paid generation / no publish

Fresh benchmark/seasonal review found no decision-changing signal, so research/backlog remained unchanged.

### 2026-08-27 — Runtime-aware operator guidance

- hardcoded H30 guidance 제거
- manifest runtime source-of-truth 강화
- runtime regression test 추가

### 2026-08-27 — Explicit Flow frame-input map

- symbolic actual-frame tokens를 operator actions로 변환
- PASS 후 actual frame 저장 안내
- frame-chain regression test 추가

### 2026-08-27 — New-rice onigiri future candidate

- IDEA-010 `8mm 新米塩むすび`
- behavioral rice-reservation evidence 기반
- NEXT_EPISODE 변경 없음

### 2026-08-26 — Deterministic novelty gate

- recent-five exact conflict+ending / hook+conflict+ending repeat 차단

### 2026-08-26 — Persistent handoff protocol

- root `PROJECT_HANDOFF.md`
- material change + same-PR handoff update mandatory
- `tools/validate_handoff_update.py`
