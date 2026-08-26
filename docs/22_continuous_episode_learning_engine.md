# Continuous Episode Learning Engine

목표: **벤치마크 → 시즌 선행 신호 → POV paw-only 아이디어 → 저실패 Flow 제작 → 24h/72h 성과 → 다음 episode**가 한 저장소에서 누적되게 한다.

Source of truth:
- handoff/current progress: `PROJECT_HANDOFF.md`
- production: `CURRENT_STANDARD.md`
- operator/credits: `docs/23_minimum_credit_operator_architecture.md`
- character/world: `docs/24_hero_cat_brand_identity.md`
- Shorts framing/scale: `docs/25_pov_paws_microworld_grammar.md`
- research update gate: `docs/27_research_evidence_saturation_gate.md`
- candidates: `ideas/episode_backlog.yaml`
- learning: `analytics/learning_ledger.csv`

## 0. Before every loop — recover current state first

이전 assistant/개발자의 기억을 최신 상태라고 가정하지 않는다.

매 실행 시작 시:
1. 최신 `main` SHA와 최근 commits/PR 확인
2. `PROJECT_HANDOFF.md` 확인
3. START_HERE / CURRENT_STANDARD / NEXT_EPISODE / recent manifest / analytics를 교차 확인
4. 다른 AI/개발자가 중간에 수정한 변경, 충돌, 회귀 위험 확인
5. 그 다음에만 연구 또는 수정 시작

Material repository change가 생기면 **같은 branch/PR에서 `PROJECT_HANDOFF.md`도 반드시 갱신**한다. NO-OP 연구 회차는 handoff를 억지로 건드리지 않는다.

## 1. Research loop

매 회차:
1. 일본/글로벌 AI-cat, miniature, ASMR, relaxing-food, adjacent Shorts의 의미 있는 성공 메커니즘만 확인
2. 경쟁작의 제목/줄거리/브랜드/결말은 복제하지 않음
3. 앞으로 2~6주의 일본 시즌/기념일/제철/문화/소셜 신호를 선행 스캔
4. Flow 공식 가격/기능 재확인
5. 실제 Tiny Cat Kitchen production failures와 24h/72h performance 확인
6. 근거가 있을 때만 backlog/docs/tools/manifests 갱신
7. **repo를 수정했다면 같은 변경 안에서 PROJECT_HANDOFF.md의 현재 상태/다음 우선순위/change log 갱신**

의미 있는 새 근거가 없으면 repo를 바꾸지 않는다.

### 1.1 Evidence saturation / no-churn gate

정기 연구의 목적은 `새 링크 수집`이 아니라 **의사결정 상태가 바뀌는 새 정보**를 찾는 것이다.

같은 후보에 대해 이미 다음 중 2개 이상이 현재 freshness window 안에 있으면 `seasonal evidence saturated`로 본다.
- behavioral demand: 방문/투표/예약/검색/판매 등 실제 행동 신호
- independent nationwide activation: 서로 다른 전국 단위 사업자/채널의 활성화
- current preference/demand survey: 표본과 대상이 명시된 현재 조사
- culturally dated activation: 실제 예약/판매/행사 시작으로 달력 이벤트가 행동 단계에 들어감

saturated 상태에서 **동일 종류의 추가 상품 출시/PR/매장 확대**만 발견되면 기본적으로 commit하지 않는다.

새 commit을 허용하는 조건은 최소 하나다.
- candidate score 또는 ranking이 실제로 바뀜
- NEXT_EPISODE 선택/발행 타이밍이 바뀜
- evidence class가 바뀜: supply/recognition → behavioral demand 등
- 기존 근거와 모순되는 신호가 생김
- 새 production mechanic이 도출되고 Flow reliability/retention 가설에 영향을 줌
- 기존 evidence가 stale해져 freshness를 갱신해야 함
- 공식 Flow 가격/기능이 바뀜
- 실제 Tiny Cat Kitchen 24h/72h production/performance 데이터가 새로 생김

다음은 **repo 변경 사유가 아니다.**
- 이미 강한 고구마 근거가 있는데 또 다른 카페가 고구마 메뉴를 발표
- 이미 전국 月見 activation이 확인됐는데 또 다른 브랜드가 月見 상품을 출시
- 같은 texture story를 반복하는 gummy PR이 하나 더 나옴
- 점수/순위/manifest/production timing에 아무 영향이 없는 홍보성 기사 추가

`research/benchmark_log.csv`는 증거 아카이브가 아니라 **의사결정 메모리**다. 반복 신호는 기존 `seasonal_evidence.yaml`의 source list를 늘리는 것조차 필요하지 않으면 그대로 둔다.

## 2. Backlog scoring

`ideas/episode_backlog.yaml` 9축 base score:
- benchmark evidence 10
- Japan relevance 10
- healing fit 15
- visual satisfaction 15
- Flow reliability 20
- originality 10
- worldbuilding 5
- audience demand 5
- expected credit efficiency 10

계절형 후보에는 bounded `Seasonal Search Lead` boost를 최대 +8만 추가한다. `research/seasonal_evidence.yaml` 근거가 stale/missing이면 boost=0.

기본 seasonal timing prior:
- peak 22~35일 전: early lead
- peak 8~21일 전: strongest lead
- peak 0~7일 전: strong final lead
- peak 기간: valid but lower
- post-peak: small tail

달력만으로 production 우선순위를 올리지 않는다.

## 3. POV_PAWS_MICROWORLD production prior

기본 Shorts는 **고양이를 보는 영상이 아니라 고양이 자신의 1인칭 시점**이다.

후보가 다음에 적합할수록 production prior를 높인다.
- front paws only
- hero object 5~20mm 또는 화면상 paw width의 15~50%
- paw-to-object scale contrast가 첫 1초에 읽힘
- nudge / press / pat / roll / steady / slide / tap으로 만들 수 있음
- 한 8초 clip에 1 primary tactile action
- macro texture/steam/crack/gloss payoff가 있음

다음은 reliability prior를 낮춘다.
- third-person full-cat framing이 필요한 아이디어
- tongs/chopsticks/knife를 사람 손처럼 grip해야 함
- precise pinch/twist
- 다중 캐릭터/군중
- hero object가 커서 miniature 감각이 약함

## 4. Episode creation loop

사용자 입력:

```text
다음 영상 준비해줘
```

ChatGPT 처리:
1. benchmark + Japan seasonal signal 확인
2. production + analytics history 확인
3. backlog 재평가
4. 최근 5개 fingerprint 중복 제거
5. POV paw-only / tiny-scale 적합 후보 우선
6. H30 vs immersive H40 결정
7. episode manifest 생성/수정
8. `production/NEXT_EPISODE.txt` 갱신
9. material 변경이 있으면 `PROJECT_HANDOFF.md` 현재 상태/플랜 동기화

## 5. Runtime learning — H30 vs H40

초기 prior:

```text
compact_h30
3×8s Lite raw motion
→ final 약 30~36s
→ 3개의 독립 beat로 완결

immersive_h40
4×8s Lite raw motion
→ final 약 38~46s
→ 4번째 beat가 world-resolution / serving / afterglow처럼 독립 가치가 있음
```

G4는 단순 runtime padding이면 금지한다. 48~60초는 실제 channel retention data가 지지할 때만 실험한다.

학습 목표는 "긴 게 좋은가"가 아니라:
- stayed-to-watch
- APV
- engaged views / credit
- subscribers / 100 credits

를 H30/H40에서 비교하는 것이다.

## 6. Progressive Spend

생성 직전 official Flow docs + 실제 UI를 확인한다.

현재 2026-08-26 재확인 기준:
- Google AI Pro: 1,000 credits / billing cycle
- Veo 3.1 Lite 4/6/8s + Extend: non-Ultra 10 credits/generation
- output_count=1
- 1080p upscale: Plus/Pro/Ultra 0 credits
- First + Last frames: Veo 3.1 Lite에서 4/6/8s 지원

진행:

```text
FREE frame/reference preflight
→ G1 only
→ POV/SCALE/ANATOMY/QC
→ save actual last usable frame
→ G2 only after PASS
→ QC
→ G3 only after PASS
→ H30 complete if story is complete
→ G4 only if immersive_h40 and G3 PASS
```

## 7. Learning ledger

`analytics/learning_ledger.csv`에 가능한 경우 기록:
- idea origin / benchmark mechanic / hypothesis
- narration mode
- flow strategy + runtime mode
- actual Flow credits
- rerolls
- G1/G2/G3/G4 first-pass success
- POV failure
- scale failure
- anatomy failure
- usable motion seconds
- continuity issue / failed action type
- audio replacement
- final runtime
- beat drop-off note
- 24h/72h Stayed to watch
- APV
- engaged views
- subscribers
- comments

placeholder 0을 실패 데이터처럼 학습하지 않는다.

## 8. Current observed production lesson

2026-08-25 사용자 Flow test에서 **third-person full-cat + body visible + object scale too large**가 실제로 발생했다.

따라서 다음을 hard gate로 승격한다.
- true first-person camera
- front paws only
- hero object <= 0.50 paw width
- human-like tool grip 회피

이 실패는 음식 소재 문제로 보지 않는다. `camera/framing/scale/action grammar` 문제로 학습한다.

## 9. Long-term optimization

장기 지표:

```text
usable motion / credit
engaged views / credit
subscribers / 100 credits
```

성공한 음식 자체는 복제하지 않는다. 성공한 **scale hook / tactile action / pacing / ASMR / world-resolution mechanism**만 다음 episode prior에 반영한다.

최종 목표:

> **시청자가 고양이의 앞발이 된 듯한 시점에서 믿기 어려울 만큼 작은 세계를 조심스럽게 만드는 감각에 빠져드는 Shorts를 가장 적은 실패 generation으로 만든다.**

## 10. Handoff persistence / completion gate

`PROJECT_HANDOFF.md`는 일회성 보고서가 아니라 지속적인 인수인계 상태다.

Material change 예:
- CURRENT_STANDARD/production mechanics 변경
- NEXT_EPISODE 또는 manifest 변경
- backlog score/ranking 의미 있는 변경
- research evidence가 의사결정을 바꿈
- analytics/learning rule 또는 실제 production/performance data 변경
- tools 동작 변경
- Flow 공식 가격/기능 assumption 변경
- 운영 인터페이스 변경

위 변화가 있으면 같은 branch/PR에서 handoff의 다음을 갱신한다.
- 현재 완료 상태
- 현재 제작 상태
- 중요한 결정/실패/학습
- 다음 작업 우선순위
- change log

로컬에서 가능하면 merge 전에:

```powershell
python tools/validate_handoff_update.py --base origin/main
```

을 실행한다. GitHub Actions minutes는 이 gate의 전제조건이 아니다.

**repo가 바뀌었는데 handoff가 바뀌지 않은 material PR은 완료로 간주하지 않는다.**
