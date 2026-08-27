# Tiny Cat Kitchen — START HERE

목표: 사용자가 매번 주제·대본·Flow 프롬프트를 고민하지 않고 **한 문장 → 준비 완료 → planned keyframe 연속성 검수 → 필요한 Veo generation만 순차 생성 → 24h/72h 학습**을 반복한다.

## 작업 시작 전 가장 먼저

다른 AI/개발자가 중간에 수정했을 수 있으므로 이전 대화 기억을 최신 상태라고 가정하지 않는다.

1. 최신 `main` SHA와 최근 PR/commit 확인
2. `AGENTS.md` 확인 — 저장소 개발 실행 정책
3. **`PROJECT_HANDOFF.md`를 읽어 개발 의도·완료 상태·NEXT 작업 복구**
4. 아래 source of truth 교차 확인
5. 충돌/회귀 위험 확인 후에만 수정 시작

## 사용자가 평소 말할 것

```text
다음 영상 준비해줘
```

소재를 직접 정하고 싶을 때만:

```text
이번엔 미니 라멘으로 만들어줘
```

그 외 조사·선정·대본·Flow 설계·기록은 시스템이 담당한다.

## Source of truth

- `AGENTS.md` — 저장소 개발 실행 정책
- `PROJECT_HANDOFF.md` — **개발 의도 / 목표 / 현재 완료 상태 / 앞으로의 플랜 / 인수인계 change log**
- `CURRENT_STANDARD.md` — 최신 production 기준
- `docs/22_continuous_episode_learning_engine.md` — 연구/학습 루프
- `docs/23_minimum_credit_operator_architecture.md` — 최소 조작/크레딧 구조
- `docs/24_hero_cat_brand_identity.md` — 고양이/주방 identity
- `docs/25_pov_paws_microworld_grammar.md` — **Shorts 1인칭 앞발-only / 초소형 scale 문법**
- `docs/26_flow_ui_mode_preflight.md` — **Flow 새 생성 vs 기존 영상 수정 상태 / 모델·길이·비용 preflight**
- `docs/27_research_evidence_saturation_gate.md` — research no-churn / evidence saturation
- `docs/28_episode_novelty_authenticity_gate.md` — 최근 episode fingerprint 반복 방지
- `docs/29_planned_keyframe_continuity_chain.md` — **planned KF0→KFn 연속성 체인**
- `research/benchmark_log.csv` — 성공 메커니즘 기억
- `ideas/episode_backlog.yaml` — 후보와 점수
- `analytics/learning_ledger.csv` — 실제 제작비/성과/학습
- `production/NEXT_EPISODE.txt` — 지금 만들 episode

## Tiny Cat Kitchen의 영상은 이렇게 보여야 함

> **시청자가 고양이가 된 것처럼 작업대를 내려다본다. 화면 아래에는 앞발만 보이고, 발보다 훨씬 작은 5~20mm 음식/물건을 조심스럽게 만든다.**

반드시:
- true first-person cat POV
- cream + pale ginger 앞발 1~2개만 등장
- 얼굴/머리/몸통/full cat 금지
- hero object가 한 앞발 폭의 절반 이하로 보임
- macro miniature diorama
- 고양이 발은 nudge / press / roll / slide / tap 위주
- human fingers/thumbs/grip 금지

예쁘더라도 다음이면 FAIL:
- 고양이가 카운터 뒤에 서서 요리함
- 정면에서 고양이를 바라보는 third-person shot
- 음식/팬이 paw와 비슷하거나 더 큼
- full kitchen establishing shot 때문에 tiny scale가 안 읽힘

## ChatGPT가 `다음 영상 준비해줘`를 받으면

- 최신 일본/글로벌 AI-cat / miniature / ASMR / relaxing Shorts 확인
- 앞으로 2~6주 일본 시즌/기념일/제철 신호 확인
- 경쟁작을 복제하지 않고 성공 원리만 추출
- production/24h/72h 기록 확인
- POV paw-only와 tiny-scale에 맞는 후보만 우선
- 최근 fingerprint 중복 제거
- 다음 episode 선택
- H30 vs H40 runtime gate 선택
- 일본어 title/hook
- narration 필요 여부
- episode manifest 생성/수정
- `production/NEXT_EPISODE.txt` 갱신
- **material repo 변경이 있으면 `PROJECT_HANDOFF.md`도 같은 branch/PR에서 갱신**

후보만 확인:

```powershell
python tools/select_next_episode.py --top 3
```

## 사용자가 로컬에서 하는 일

```powershell
./tools/make_next_short.ps1
```

자동 생성:
- `generated/TK-XXX_bundle.md`
- `generated/TK-XXX_flow_pack.md`
- `generated/TK-XXX_edit_plan.md`
- `generated/TK-XXX_publish_pack.md`

이 단계는 Flow/LLM/API 크레딧을 쓰지 않는다.

## Gate A — planned keyframe chain 먼저

**Paid Veo 전에 현재 episode가 요구하는 planned keyframe을 모두 만들고 연속성을 검수한다.**

현재 공식 Flow 문서에서 no-charge 이미지 경로가 안내되더라도, 실제 UI에서 **active image model + displayed cost**를 먼저 확인한다. 0-credit/no-charge로 표시될 때만 무료 preflight로 사용한다.

```text
KF0 = master visual anchor
↓ approved KF0를 edit/refine/reference로 사용
KF1
↓ approved KF1에서 파생
KF2
↓
필요한 마지막 KF까지 순차 파생
↓
planned KF chain 전체 PASS
↓
G1만 생성
```

**KF1+를 각각 독립적인 fresh text-to-image로 다시 뽑지 않는다.** 그러면 paw fur, 카메라, hero-object scale, fixed props, 조명과 workbench geometry가 바뀔 수 있다.

각 KF 체크:
- true first-person인가?
- 앞발만 보이는가?
- 얼굴/몸통이 안 보이는가?
- hero object가 paw보다 압도적으로 작은가?
- human fingers/thumbs가 없는가?
- paw fur/anatomy가 이전 승인 KF와 같은가?
- camera/lens/workbench/fixed props 위치가 유지되는가?
- 바뀌어야 할 food/material state만 의도대로 바뀌었는가?

구조적 drift가 있으면 `KEYFRAME DRIFT FAIL`이고 **paid G1으로 넘어가지 않는다.**

중요:
- planned KF = 각 scene이 도달할 **destination**
- 이전 PASS 영상에서 Flow `Save frame`으로 저장한 actual frame = 다음 scene의 **continuity bridge**

둘을 혼동하지 않는다.

## Flow 기본 설정

생성 직전 실제 UI에서 확인:

```text
새 영상 generation 상태
Veo 3.1 Lite
9:16
8 seconds 또는 현재 mode가 8s-only임을 확인
output count = 1
표시 비용 = 현재 공식표/실제 UI와 일치
```

**기존 영상을 열어둔 수정 화면은 G1/G2/G3/G4 생성 화면이 아니다.** `수정 사항 설명` 계열 입력창이나 `Omni Flash` video-edit 상태가 보이면 standard 새 동영상 generation 화면으로 돌아간다.

4s/6s/8s selector가 안 보인다고 바로 오류로 판단하지 않는다. mode에 따라 8s-only일 수 있으므로 **duration selector 자체보다 active model + generation mode + output count + displayed cost 확인을 우선한다.** 자세한 절차는 `docs/26_flow_ui_mode_preflight.md`.

## Runtime / credit 선택

### compact_h30

```text
planned KF chain PASS
→ G1 8s = 10
PASS → G2 = +10
PASS → G3 = +10
first-pass ceiling = 30 credits
final ≈ 30~36s
```

3개 독립 beat로 완결될 때 사용.

### immersive_h40

```text
planned KF chain PASS
→ G1 → G2 → G3 모두 PASS
독립적인 4번째 world-resolution beat가 있을 때만 G4 = +10
first-pass ceiling = 40 credits
final ≈ 38~46s
```

4번째 scene은 길이 패딩이 아니라 작은 세계의 여운/serving/resolution이어야 한다.

48~60초는 실제 retention 데이터가 지지하기 전에는 기본 목표가 아니다.

## Actual-frame Sequential Chain

```text
planned KF0→KFn 전체 PASS
↓
G1
↓ QC PASS
Flow native Save frame — actual last usable frame
↓
G2 First frame
↓ QC PASS
Flow native Save frame
↓
G3 First frame
↓ QC PASS
Flow native Save frame
↓
G4 First frame (immersive_h40 only)
```

다음 scene의 First frame은 **이전 PASS clip의 실제 saved frame**을 사용한다. 더 예쁜 planned target KF로 대체하지 않는다.

## 한 8초 scene

> **1 calm tactile primary action + optional 1 passive micro-payoff**

좋은 동작:
- paw nudges a tiny cup
- paw presses a tiny dough ball
- paw rolls one tiny ingredient
- paw slides a miniature plate
- paw taps one garnish

나쁜 동작:
- paw grips chopsticks/tongs like a hand
- 여러 도구를 동시에 사용
- 준비→조리→완성→먹기 전부 한 번에

기본 long-take episode에서 manifest가 `max_visual_cuts_per_8s_generation: 0`을 선언하면 generated paid prompt에도 literal zero-cut 지시가 남아야 한다.

## 오디오

기본:

```text
No narration
No generated music
Quiet room tone + close tiny ASMR
```

영상 motion이 좋고 소리만 이상하면 영상 재생성 금지. 후편집 SFX로 교체한다.

## 생성 결과를 다시 보여줄 때

```text
G1 만들었어. 봐줘
```

영상/스크린샷만 첨부.

ChatGPT 판단:
- `PASS`
- `EDITABLE`
- `REROLL`
- `STOP`

구조적 실패 shorthand:
- `POV FAIL`
- `SCALE FAIL`
- `ANATOMY FAIL`
- `CAMERA FAIL`
- `KEYFRAME DRIFT FAIL`
- `FRAME CHAIN FAIL`
- `PADDING FAIL`

## 업로드 후 학습

24h/72h에 가능한 범위에서 기록:
- Stayed to watch
- APV
- engaged views
- subscribers
- comments
- actual Flow credits
- rerolls
- G1/G2/G3/G4 first-pass success
- POV/scale/anatomy failure
- continuity failure
- failed action type
- usable motion seconds
- final duration

장기 목표:

```text
usable motion / credit
engaged views / credit
subscribers / 100 credits
```

특히 `30~36s compact_h30`과 `38~46s immersive_h40`을 비교해 실제 채널에 맞는 몰입 길이를 학습한다.

## Handoff persistence gate

repo를 실제로 수정하는 모든 material 작업은 `PROJECT_HANDOFF.md`를 같은 branch/PR에서 갱신해야 완료로 본다.

로컬 검증:

```powershell
python tools/validate_handoff_update.py --base origin/main
```

의미 있는 개선이 없어 repo를 NO-OP으로 유지한 회차는 handoff도 억지로 수정하지 않는다.

# 가장 간단한 실제 사용법

```text
1. ChatGPT: "다음 영상 준비해줘"
2. PowerShell: ./tools/make_next_short.ps1
3. Flow: image model/cost 확인 → KF0 생성/QC
4. KF1→필요한 마지막 KF까지 이전 승인 KF에서 순차 파생/QC
5. planned KF chain 전체 PASS 후 새 동영상 generation 상태 확인
6. G1만 생성
7. ChatGPT: "G1 만들었어. 봐줘"
8. PASS면 Flow native Save frame → 그 실제 frame으로 G2
9. G2 PASS → Save frame → G3 → 필요하면 정당한 G4
10. 업로드 후 Studio 수치/스크린샷 공유
```

핵심:

> **고양이를 보여주는 영상이 아니라, 고양이의 앞발이 된 시점에서 믿기 어려울 만큼 작은 것을 만드는 경험을 판다.**
