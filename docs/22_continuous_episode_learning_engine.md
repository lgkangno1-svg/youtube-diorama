# Continuous Episode Learning Engine

목표: **Mini Forest류 miniature-making benchmark → 일본 시즌/수요 신호 → paw-only 아이디어 → quality-first fast production → 24h/72h 성과 + 제작시간 → 다음 episode**가 한 저장소에서 누적되게 한다.

Source of truth:
- `PROJECT_HANDOFF.md` — current state / decisions / failures / next priorities
- `PRODUCT_CHARTER.md` — durable product intent / priority order / improvement standard
- `CURRENT_STANDARD.md` — executable production rules
- `docs/23_minimum_credit_operator_architecture.md` — legacy filename, current quality-first fast operator architecture
- `docs/27_research_evidence_saturation_gate.md`
- `ideas/episode_backlog.yaml`
- `analytics/learning_ledger.csv`

## 0. Before every loop

1. latest main SHA + recent commits/PRs
2. `PROJECT_HANDOFF.md`
3. `PRODUCT_CHARTER.md`
4. START_HERE / CURRENT_STANDARD / docs/23/27 / NEXT_EPISODE / current manifest / research/backlog/ledger
5. newest explicit user direction + merged state override stale chat/automation/legacy enum
6. material change → same branch/PR `PROJECT_HANDOFF.md`
7. executable production rule change → `CURRENT_STANDARD.md`
8. durable product priority/purpose change only → `PRODUCT_CHARTER.md`

True NO-OP은 문서 churn 금지.

## 1. Improvement priority

현재 우선순위:
1. video/content quality
2. viewer outcome / recognizable channel identity
3. production convenience and speed
4. paid-video reroll/credit efficiency
5. free-image cost policing

사용자의 Nano Banana image access는 현재 무료다. 실제 비용 문제가 다시 생기지 않는 한 free-image cost gate 자체는 연구/개발 우선순위가 아니다.

## 2. Research loop

1. 일본/글로벌 miniature cooking, handcrafted tiny-food, ASMR, relaxing-food, adjacent Shorts 조사
2. Mini Forest류 hand-centric making composition을 1차 제작 benchmark로 사용
3. AI-cat character channels은 paw appearance/reliability 같은 보조 참고만 사용
4. 일본 2–6주 seasonal/cultural/food signals 확인
5. 실제 Tiny Cat Kitchen production/performance 확인
6. Flow 가정 변경이 필요할 때만 공식 Google 기능/가격 재확인
7. decision이 바뀔 때만 repo evidence 갱신

복제 금지: exact title / exact plot / branded package / distinctive set / signature ending.

추출 허용: hook mechanic / hand-centric maker composition / tiny scale / tactile transformation / calm pacing / seasonal timing / material payoff.

## 3. Evidence saturation

이미 충분한 same-class evidence가 있으면 promotional/retail/news row를 더 쌓지 않는다.

새 evidence commit은 ranking, NEXT_EPISODE, timing, evidence class, content mechanic, production mechanic, Flow assumption, freshness, 또는 real production learning 중 하나를 바꿀 때만 정당화한다.

## 4. Backlog scoring

기존 9축을 유지한다.
- benchmark evidence 10
- Japan relevance 10
- healing fit 15
- visual satisfaction 15
- Flow reliability 20
- originality 10
- worldbuilding 5
- audience demand 5
- expected paid-credit efficiency 10

Production prior:
- first 1–2s scale-hook가 강할수록 가점
- hand-centric miniature process가 명확할수록 가점
- feline-safe paw action으로 변환하기 쉬울수록 가점
- 5–20mm hero + paw scale contrast가 강할수록 가점
- visible material transformation과 payoff가 강할수록 가점
- high-oblique/top-down/tabletop macro에서 잘 읽힐수록 가점
- **세 번째 beat에서 이미 만족스러운 core ending을 만들 수 있으면 가점; 네 번째 beat가 없어도 story가 완결되어야 함**

감점:
- full-cat acting
- human-like tool grip / pinch / precise twist
- weak scale
- crowd/multiple characters
- payoff 없는 motion-only scene
- G4가 없으면 결말이 성립하지 않는 H40 설계

Legacy `POV_PAWS_MICROWORLD_V1`은 compatibility token이다.

## 5. Episode creation loop

사용자:
```text
다음 영상 준비해줘
```

ChatGPT/repo:
1. latest state + actual production/analytics 확인
2. fresh evidence는 필요한 만큼만 조사
3. backlog 재평가 + novelty check
4. episode 선택
5. H30/H40 선택
6. HOOK / TRANSFORMATION / SCALE PROOF / PAYOFF / JAPAN FIT 설계
7. manifest 생성/수정
8. exact-order copy/paste `production/<EPISODE>_OPERATOR_CARD.md` 생성/수정
9. NEXT_EPISODE 갱신
10. material handoff sync

Normal user path:
```powershell
./tools/make_next_short.ps1
```

Primary execution surface = Operator Card. Bundle/flow-pack = fallback/reference.

## 6. Content-quality learning

각 episode에서 paid generation 전 다음 hypothesis를 명시한다.
- opening hook hypothesis
- strongest scale-proof frame
- scene-by-scene visible transformation
- core ending hypothesis by G3 when H40 is used
- optional G4 value hypothesis
- Japan timing/relevance hypothesis

영상이 실제로 나온 뒤 이 hypothesis가 output에서 살아남았는지 기록한다. 기술적으로 PASS여도 hook/transform/payoff가 약하면 다음 episode prior에 반영한다.

## 7. Runtime / Progressive Spend

H30/H40는 first-pass paid ceiling.

```text
compact_h30 = 3×8s raw
immersive_h40 = 3 core beats + optional fourth candidate, up to 4×8s raw
```

Adaptive H40 rule:
- G1→G3가 core story를 완결해야 함
- G4는 독립적인 serving/world-resolution/afterglow 가치가 있을 때만
- G4 target KF도 real G3 판단 전에는 만들 필요가 없음
- G3가 이미 완결되면 stop

```text
strong core visual/KF chain
→ G1 only
→ quality + structural QC
→ PASS: native Save frame
→ G2 only after PASS
→ G3 only after PASS
→ watch G1-G3 together
→ complete = STOP
→ only if G4 still adds value: derive optional target from actual G3 saved frame → G4
```

다음 scene First frame = previous PASS clip actual native saved frame.

## 8. Learning ledger

가능하면 실제값 기록:
- paid Flow credits
- rerolls
- G1~G4 first-pass success
- `maker_view_failure`
- `character_failure`
- scale/anatomy/continuity failure
- failed action type
- usable motion seconds / final runtime
- audio replacement
- Stayed to watch / APV / engaged views / subscribers / comments

Operator-efficiency도 가능한 범위로 기록:
- preparation minutes
- manual interventions
- prompt corrections before G1
- time-to-first-valid-G1
- whether optional G4 was planned but correctly skipped after G3

`pov_failure`는 deprecated compatibility field다. Non-first-person maker view 자체를 실패로 기록하지 않는다.

Placeholder zero를 실제 관측값으로 학습하지 않는다.

## 9. Existing production lesson

실제 preflight failure:
- full cat/body visible
- hero too large
- human-like tool-use risk

최신 해석:
- observer maker-view 자체는 문제 아님
- character framing / weak scale / human-like manipulation이 실패

Hard identity gate:
- front paws only
- no face/head/body/full cat
- hero <=0.50 paw width
- miniature making process is subject
- no human-like grip

## 10. Optimization targets

Audience / paid-efficiency:
```text
engaged views / paid credit
subscribers / 100 paid credits
usable motion / paid credit
```

Production speed:
```text
time-to-first-valid-G1
manual interventions / episode
prompt corrections before G1
rerolls / finished episode
unnecessary prebuilt optional targets / episode
```

중요: `credits/video` 또는 `minutes/video`를 단독 최적화하지 않는다. 영상 퀄리티와 audience outcome이 떨어지면 개선이 아니다.

성공한 음식/경쟁 episode 자체를 복제하지 않고 성공한 hook / scale / tactile action / maker-view / pacing / ASMR / payoff mechanics만 다음 prior에 반영한다.

## 11. Final goal

> **Mini Forest의 손-중심 미니어처 제작 감성을 사람 손 대신 자연스러운 고양이 앞발로 구현하면서, 더 좋은 hook·transformation·payoff를 가진 Shorts를 사용자가 점점 더 적은 수동 작업과 재생성으로 빠르게 만들 수 있게 한다.**

## 12. Documentation persistence

Material change:
- always `PROJECT_HANDOFF.md`
- production/QC/operator rule change → `CURRENT_STANDARD.md`
- durable purpose/priority change → `PRODUCT_CHARTER.md`

로컬 git 가능 시:
```powershell
python tools/validate_handoff_update.py --base origin/main
```

로컬 git이 불가능하면 latest main 기반 branch/PR diff에서 same-change handoff 포함 여부를 확인한다.
