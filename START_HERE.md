# Tiny Cat Kitchen — START HERE

목표: 사용자가 매번 주제·대본·Flow 프롬프트를 고민하지 않고 **한 문장 → 준비 완료 → planned keyframe 검수 → 필요한 Veo generation만 순차 생성 → 24h/72h 학습**을 반복한다.

## 작업 시작 전

1. 최신 `main` SHA와 최근 PR/commit 확인
2. `AGENTS.md` 확인
3. `PROJECT_HANDOFF.md` 확인
4. `CURRENT_STANDARD.md`, docs/22, docs/23, NEXT_EPISODE, current manifest, research/backlog/ledger 교차 확인
5. 최신 merged state가 오래된 대화/자동화 문구보다 우선

## 사용자가 평소 말할 것

```text
다음 영상 준비해줘
```

소재를 직접 정할 때만 별도 지시한다.

## Source of truth

- `PROJECT_HANDOFF.md`
- `CURRENT_STANDARD.md`
- `docs/22_continuous_episode_learning_engine.md`
- `docs/23_minimum_credit_operator_architecture.md`
- `docs/24_hero_cat_brand_identity.md`
- `docs/25_pov_paws_microworld_grammar.md`
- `docs/26_flow_ui_mode_preflight.md`
- `docs/27_research_evidence_saturation_gate.md`
- `docs/28_episode_novelty_authenticity_gate.md`
- `docs/29_planned_keyframe_continuity_chain.md`
- `research/benchmark_log.csv`
- `ideas/episode_backlog.yaml`
- `analytics/learning_ledger.csv`
- `production/NEXT_EPISODE.txt`

## Tiny Cat Kitchen의 최신 정체성

> **Mini Forest처럼 아주 작은 음식/물건을 실제로 만드는 힐링 미니어처 영상. 사람 손이 나올 자리를 고양이 앞발만 대신한다.**

반드시:
- cream + pale-ginger feline front paws 1~2개만 등장
- face/head/body/full cat 금지
- human hands/fingers/thumbs 금지
- hero object 보통 5~20mm, 한 paw 폭의 15~50%
- real miniature materials / handcrafted diorama look
- process-first making shot
- calm long take / close ASMR

중요:
- **true first-person cat POV는 더 이상 필수 조건이 아니다.**
- 기본은 Mini Forest류의 high-oblique maker view.
- top-down macro / side-oblique macro도 동작과 질감이 더 잘 읽히면 허용.
- 기존 enum `POV_PAWS_MICROWORLD_V1`은 도구 호환을 위해 당분간 유지하지만 실제 의미는 paws-only miniature making이다.

FAIL:
- cat face/full body/character acting
- 고양이가 카운터 뒤에서 사람처럼 요리
- 사람 손/손가락/엄지
- human-like tool grip
- miniature scale가 약함
- making process보다 고양이 캐릭터가 주인공

## 벤치마크 우선순위

1차: Mini Forest류 miniature cooking / handcrafted tiny-food / relaxing ASMR

추출할 것:
- hand-centric making composition
- real miniature craftsmanship
- tactile process
- tiny scale contrast
- calm pacing
- seasonal food timing
- steam/crack/gloss/crumb/sizzle payoff

AI-cat 캐릭터 채널은 1차 제작 방향이 아니다. 필요한 경우 paw appearance/reliability 같은 보조 참고만 한다.

## `다음 영상 준비해줘` 처리

- 최신 일본/글로벌 miniature / ASMR / relaxing-food / adjacent Shorts 확인
- 일본 시즌/기념일/제철 신호 확인
- 실제 production/analytics 확인
- novelty-safe candidate 선택
- Mini Forest-style paw-only making으로 premise 재해석
- H30 vs H40 결정
- manifest 생성/수정
- `production/NEXT_EPISODE.txt` 갱신
- material 변경 시 `PROJECT_HANDOFF.md` 같은 branch/PR에서 갱신

## 사용자가 로컬에서 하는 일

```powershell
./tools/make_next_short.ps1
```

자동 생성 pack은 Flow 크레딧을 쓰지 않는다.

## Gate A — planned keyframe chain

```text
image model + displayed cost 확인
→ KF0 maker-view master anchor 생성
→ paws / scale / camera / props / lighting QC
→ KF1을 KF0에서 edit/reference 파생
→ KF2를 KF1에서 파생
→ 필요한 마지막 KF까지 반복
→ 전체 PASS
→ G1만 생성
```

KF1+를 independent fresh text-to-image로 만들지 않는다.

## Flow 기본 설정

생성 직전 실제 UI 확인:

```text
NEW VIDEO GENERATION
Veo 3.1 Lite
9:16
8 seconds
output count = 1
displayed cost = current UI truth
```

기존 영상 edit/Omni Flash 화면이면 새 generation 화면으로 돌아간다.

## Runtime / Progressive Spend

### compact_h30
- 3×8s raw = 24s
- current first-pass ceiling 30 credits
- final 보통 24~27s

### immersive_h40
- 4×8s raw = 32s
- current first-pass ceiling 40 credits
- final 보통 32~35s
- G4는 독립적인 serving/world-resolution value가 있을 때만

```text
planned KF chain PASS
→ G1
PASS → Flow native Save frame
→ G2
PASS → Save frame
→ G3
→ 필요한 경우만 G4
```

다음 scene First frame은 previous PASS clip의 실제 saved frame이다.

## 한 8초 scene

> **1 calm tactile primary action + optional 1 passive material payoff**

좋은 동작:
- nudge
- press
- pat
- roll
- steady
- slide
- tap
- push

나쁜 동작:
- chopsticks/tongs/knife human grip
- thumb-index pinch
- 여러 복잡한 동작 동시 수행

## 오디오

기본:
```text
No narration
No generated music
Quiet room tone + close tiny ASMR
```

영상이 좋고 소리만 이상하면 후편집 교체.

## 결과 QC

- `MAKER VIEW PASS`
- `SCALE FAIL`
- `CHARACTER FAIL`
- `ANATOMY FAIL`
- `CAMERA FAIL`
- `KEYFRAME DRIFT FAIL`
- `FRAME CHAIN FAIL`
- `PROP CONTINUITY FAIL`
- `PADDING FAIL`

## 학습

실제 값만 기록:
- credits/rerolls
- G1~G4 first-pass success
- maker-view/camera failure
- scale/anatomy/continuity failure
- usable motion seconds
- final runtime
- 24h/72h Stayed to watch / APV / engaged views / subscribers / comments

장기 KPI:
```text
usable motion / credit
engaged views / credit
subscribers / 100 credits
```

## 가장 간단한 실제 사용법

```text
1. ChatGPT: "다음 영상 준비해줘"
2. PowerShell: ./tools/make_next_short.ps1
3. Flow: KF0→KFn maker-view continuity PASS
4. G1만 생성
5. ChatGPT에게 G1 결과 공유
6. PASS면 native Save frame → G2 → G3 → 필요한 경우 G4
7. 업로드 후 성과 기록
```

핵심:

> **Mini Forest의 손-중심 미니어처 제작 감성을 유지하고, 그 손만 고양이 앞발로 바꾼다. 고양이 전체 모습이나 캐릭터 연기는 필요 없다.**
