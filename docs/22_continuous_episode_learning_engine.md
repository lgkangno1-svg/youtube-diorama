# Continuous Episode Learning Engine

목표: **Mini Forest류 miniature-making benchmark → 일본 시즌 선행 신호 → paw-only 아이디어 → 저실패 Flow 제작 → 24h/72h 성과 → 다음 episode**가 한 저장소에서 누적되게 한다.

Source of truth:
- `PROJECT_HANDOFF.md`
- `CURRENT_STANDARD.md`
- `docs/23_minimum_credit_operator_architecture.md`
- `docs/24_hero_cat_brand_identity.md`
- `docs/25_pov_paws_microworld_grammar.md`
- `docs/27_research_evidence_saturation_gate.md`
- `ideas/episode_backlog.yaml`
- `analytics/learning_ledger.csv`

## 0. Before every loop

1. latest main SHA + recent commits/PRs
2. PROJECT_HANDOFF
3. START_HERE / CURRENT_STANDARD / NEXT_EPISODE / current manifest / analytics
4. latest merged state가 stale chat/automation보다 우선
5. material change면 same branch/PR에서 PROJECT_HANDOFF 업데이트

NO-OP 연구는 handoff를 억지로 수정하지 않는다.

## 1. Research loop

1. 일본/글로벌 miniature cooking, handcrafted tiny-food, ASMR, relaxing-food, adjacent Shorts 조사
2. **Mini Forest류 hand-centric making composition을 1차 제작 benchmark로 사용**
3. AI-cat character channels는 주된 스타일 기준이 아니라 paw appearance/reliability 등 보조 참고만 사용
4. 일본 2~6주 seasonal/cultural/food signals 확인
5. Flow 공식 가격/기능 확인
6. 실제 Tiny Cat Kitchen production/performance 확인
7. 의사결정이 바뀔 때만 repo 갱신

복제 금지:
- exact title
- exact plot
- branded food/package
- exact ending
- exact set/dish presentation

추출 허용:
- hand-centric making composition
- tiny scale contrast
- real miniature craftsmanship
- tactile process
- pacing
- material payoff
- seasonal timing

## 2. Evidence saturation

같은 후보에 behavioral demand / independent nationwide activation / current survey / dated cultural activation 중 충분한 근거가 이미 있으면 same-class PR/retail signal을 더 쌓지 않는다.

새 commit은 ranking, NEXT_EPISODE, timing, evidence class, production mechanic, freshness, Flow assumptions, 실제 production/performance 중 하나를 바꿀 때만 정당화한다.

## 3. Backlog scoring

9축:
- benchmark evidence 10
- Japan relevance 10
- healing fit 15
- visual satisfaction 15
- Flow reliability 20
- originality 10
- worldbuilding 5
- audience demand 5
- expected credit efficiency 10

현재 production prior:
- 사람 손으로 미니어처를 만드는 듯한 process가 명확할수록 가점
- 그 손 역할을 feline-safe paws로 바꿀 수 있을수록 가점
- high-oblique/top-down/tabletop macro에서 동작이 잘 읽힐수록 가점
- 5~20mm hero object와 paw scale contrast가 강할수록 가점
- press/slide/nudge/roll/tap으로 만들 수 있을수록 가점

감점:
- full-cat character acting 필요
- human-like tool grip 필요
- precise pinch/twist 필요
- crowd/multiple characters
- miniature scale가 약함

기존 backlog의 `POV_PAWS_MICROWORLD_V1` label은 legacy compatibility로 해석한다. 새 manifest에서는 CURRENT_STANDARD의 Mini Forest-style paw-only semantics로 재해석한다.

## 4. Episode creation loop

사용자:
```text
다음 영상 준비해줘
```

ChatGPT:
1. benchmark + seasonal signals
2. production + analytics
3. backlog 재평가
4. recent fingerprint 중복 제거
5. Mini Forest-style paw-only making에 맞게 premise 재구성
6. H30/H40 선택
7. manifest 생성/수정
8. NEXT_EPISODE 갱신
9. material change면 handoff 동기화

## 5. Runtime learning

H30/H40 숫자는 first-pass credit ceiling.

```text
compact_h30
3×8s = raw 24s
final 보통 24~27s

immersive_h40
4×8s = raw 32s
final 보통 32~35s
```

G4는 독립적인 serving/world-resolution/afterglow 가치가 있을 때만.

학습 비교:
- Stayed to watch
- APV
- engaged views / credit
- subscribers / 100 credits

## 6. Progressive Spend

생성 직전 공식 docs + 실제 UI 확인.

```text
FREE planned KF chain
→ G1 only
→ maker-view / paw-only / scale / anatomy QC
→ native Save frame
→ G2 only after PASS
→ G3 only after PASS
→ G4 only when manifest/runtime gate justifies it
```

다음 scene First frame = previous PASS clip actual saved frame.

## 7. Learning ledger

가능하면 기록:
- actual Flow credits
- rerolls
- G1~G4 first-pass success
- maker-view/camera failure
- scale failure
- anatomy failure
- continuity issue
- failed action type
- usable motion seconds
- final runtime
- audio replacement
- Stayed to watch
- APV
- engaged views
- subscribers
- comments

placeholder zero를 실제 관측값으로 학습하지 않는다.

## 8. Existing production lesson reinterpretation

2026-08-25 test에서 third-person full-cat + body visible + object scale too large가 실패했다.

이 실패의 최신 해석:
- 문제는 `third-person` 자체가 아니다.
- 문제는 **cat character-performance framing + body reveal + weak miniature scale**이다.
- 허용 third-person/observer camera는 Mini Forest처럼 작업대와 앞발 동작만 보는 maker view다.

Hard gate:
- front paws only
- no face/head/body/full cat
- hero object <=0.50 paw width
- miniature-making process is subject
- no human-like grip

## 9. Long-term optimization

장기 지표:
```text
usable motion / credit
engaged views / credit
subscribers / 100 credits
```

성공한 음식 자체를 복제하지 않고 성공한 scale hook / tactile action / maker-view composition / pacing / ASMR / payoff만 다음 prior에 반영한다.

최종 목표:

> **Mini Forest의 손-중심 미니어처 제작 감성을 유지하면서 사람 손만 고양이 앞발로 바꾼 듯한 Shorts를 가장 적은 실패 generation으로 만든다.**

## 10. Handoff persistence

CURRENT_STANDARD, production mechanics, NEXT_EPISODE/manifest, research decision, analytics, tools, Flow assumption 등 material change가 있으면 같은 branch/PR에서 `PROJECT_HANDOFF.md`를 갱신한다.

로컬 가능 시:
```powershell
python tools/validate_handoff_update.py --base origin/main
```
