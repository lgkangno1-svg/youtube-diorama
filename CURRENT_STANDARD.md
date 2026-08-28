# CURRENT STANDARD — Tiny Cat Kitchen

최신 적용 기준: **2026-08-29 Mini Forest-style Paw-Only Miniature Making + Fail-Closed Candidate/Manifest Validation + Planned Keyframe Continuity + Progressive Spend + Runtime Feasibility**

## 0. 문서 거버넌스

이 문서는 현재 실행 규칙이다. 장기 목적/개선 판단은 `PRODUCT_CHARTER.md`, 현재 상태/최근 결정/실패/다음 우선순위는 `PROJECT_HANDOFF.md`가 담당한다.

모든 material 개선 전:

```text
latest explicit user direction
→ latest merged main + PROJECT_HANDOFF.md
→ PRODUCT_CHARTER.md
→ CURRENT_STANDARD.md + specialized docs
→ current manifest / benchmark / backlog / ledger
```

동기화:
- material repository change → `PROJECT_HANDOFF.md`
- production/QC/Flow/selection executable rule change → `CURRENT_STANDARD.md`
- durable purpose/identity/economics philosophy change → `PRODUCT_CHARTER.md`
- true NO-OP → 문서 churn 금지

비용 절감만으로는 개선이 아니다. paws-only miniature-making identity, tactile/healing quality, audience outcome per credit, user control을 함께 보호한다.

## 1. 핵심 경험

> **Mini Forest처럼 아주 작은 음식/물건을 실제로 만드는 미니어처 힐링 영상이며, 사람 손이 들어올 자리를 고양이 앞발이 대신한다.**

필수:
- cream/pale-ginger feline front paws 1~2개만 등장
- face/head/body/full cat 금지
- human hands/fingers/thumbs 금지
- human-like feline tool grip 금지
- hero object 보통 5~20mm, 한 paw 폭의 15~50% 이하
- realistic handcrafted miniature workbench
- process-first making shot
- mostly locked observational camera
- 1 generation = 1 primary tactile action + optional 1 passive micro-payoff
- no rapid montage / no cat character-performance shot

카메라 우선순위:
1. high-oblique maker view
2. top-down macro
3. side/tabletop oblique macro
4. first-person-like angle은 결과가 더 자연스러울 때만

**literal true first-person cat POV는 필수가 아니다.** `POV_PAWS_MICROWORLD_V1` / `first_person_cat_pov` 같은 이름은 현재 tooling compatibility token일 뿐이며 창작 의미를 결정하지 않는다.

## 2. Candidate selection fail-closed gate

`tools/select_next_episode.py`는 legacy enum 값만 보고 production-eligible로 판단하지 않는다.

현재 후보가 통과하려면 최소한:
- compatibility token `POV_PAWS_MICROWORLD_V1` 존재
- `hero_scale`에 paw-width ratio가 명시되어 있고 최대값 `<= 0.50`
- paw action family가 feline-safe allowlist 안에 있음
- runtime prior가 `compact_h30` 또는 `immersive_h40`
- trend/evidence/novelty gate도 기존 규칙대로 통과

현재 feline-safe allowlist:
`nudge / press / pat / roll / steady / slide / tap / push`

`pinch`, `twist`, `grip`, tongs/chopsticks/knife류 human-dexterity action을 후보 metadata에 넣으면 selector가 fail-closed로 거부해야 한다.

중요: legacy enum은 **호환 토큰**이고 maker-view 적합성의 증거가 아니다. 후보 선택 출력도 이를 `visual_grammar_token`으로 표시한다.

## 3. Canonical manifest validation path

정상 사용자 경로 `./tools/make_next_short.ps1`은 `tools/validate_maker_view_manifest.py`를 먼저 실행한다.

필수 semantics:
- `brand_identity.visual_intent = mini_forest_style_paws_only_miniature_making`
- `camera_grammar.semantic_override = mini_forest_style_observational_maker_view`
- `camera_grammar.first_person_required = false`
- `preferred_angles`에 `high_oblique_maker_view`
- `stop_if_maker_view_scale_anatomy_or_premise_fails = true`
- legacy `stop_if_pov...` gate는 active current gate가 아님

그 뒤 구조 validator가 Flow model/output count, H30/H40 scene/credit ceiling, keyframe completeness, actual saved-frame chaining, progressive PASS gates, cut/action limits, runtime feasibility, narration을 검증한다.

## 4. Planned keyframe continuity

Paid Veo 전:

```text
Flow image model + displayed cost 확인
→ no-charge일 때만 free preflight
→ KF0 maker-view master anchor
→ paws / scale / camera / fixed props / lighting QC
→ KF1은 승인 KF0에서 파생
→ KF2는 KF1에서 파생
→ 필요한 마지막 KF까지 순차 파생
→ planned KF chain 전체 PASS
→ G1만 생성
```

KF1+를 independent fresh text-to-image lottery로 만들지 않는다.

planned KF = destination. actual previous PASS frame = next-scene continuity bridge.

## 5. Flow / Veo baseline

생성 직전 실제 UI 확인:

```text
NEW VIDEO GENERATION
Veo 3.1 Lite
9:16
8 seconds
output count = 1
displayed cost = current UI truth
```

2026-08-29 공식 Flow 문서 재확인 기준:
- non-Ultra Veo 3.1 Lite: 10 credits/generation
- Ultra: 5 credits/generation
- non-subscriber: 50 free Flow credits/day, paid plan과 stack되지 않음
- actual UI model/mode/output count/displayed cost가 생성 시점 최종 truth

무료 tier가 있어도 batch/reroll discipline을 느슨하게 하지 않는다.

## 6. Progressive Spend

```text
FREE planned KF chain PASS
→ G1 only
→ QC
→ actual last usable frame native Save frame
→ G2 only after G1 PASS
→ G3 only after G2 PASS
→ G4 only if immersive_h40 + G3 PASS + independent world-resolution value
```

구조적 FAIL 후 다음 paid scene 금지.

## 7. Runtime

H30/H40는 final seconds가 아니라 first-pass credit tier다.

### compact_h30
- 3 × 8s = raw 24s
- current non-Ultra first-pass ceiling 30 credits
- final 보통 24~27s

### immersive_h40
- 4 × 8s = raw 32s
- current non-Ultra first-pass ceiling 40 credits
- final 보통 32~35s
- G4는 serving/world-resolution/afterglow 독립 가치가 있을 때만

runtime padding 금지.

## 8. 8초 scene / paw-action grammar

기본:
> **1 calm tactile primary action + optional 1 passive material payoff**

선호 active action:
`nudge / press / pat / roll / steady / slide / tap / push`

피함:
- thumb-index pinch
- precise twist
- tongs/chopsticks/knife human grip
- 여러 복잡한 active gesture 동시 수행

기본 `max_visual_cuts_per_8s_generation: 0`.

예:
```text
0~1.5s  paw approaches/settles
1.5~6s  one press / roll / slide / nudge / push
6~8s    paw stops; steam/crack/gloss/crumb continues
```

## 9. Audio

기본:
```text
No narration
No generated music
Quiet room tone + close miniature ASMR
```

motion이 좋고 audio만 나쁘면 reroll보다 후편집 교체.

## 10. Research / benchmark

1차 benchmark:
- realistic miniature cooking/making
- handcrafted tiny-food process
- relaxing tactile ASMR

AI-cat 채널은 paw appearance/reliability 같은 보조 근거만 사용한다.

복제 금지:
- exact title
- exact plot
- branded product/package
- distinctive set/dish styling
- exact ending

추출 허용:
- hand-centric maker composition
- tiny scale contrast
- tactile process
- calm pacing
- seasonal timing
- material payoff

Evidence saturation: ranking/timing/mechanics/freshness/Flow assumption/actual production learning을 바꾸지 않는 same-class promo/retail signal은 commit하지 않는다.

## 11. 현재 제작 상태

`production/NEXT_EPISODE.txt` = **TK-005**

`猫の前足で作る、12mmの焼きいも。`

- runtime: `immersive_h40`
- 4 Lite scenes / current non-Ultra first-pass ceiling 40 credits
- final target 32~35s
- Mini Forest-style tiny yakiimo making
- KF0→KF4 planned continuity
- same roasting tray / warmer / serving niche
- G2/G3/G4 First = previous PASS clip native saved frame
- no direct pinch/grab
- zero-cut long take

최우선:
1. current maker-view manifest validation PASS
2. KF0→KF4 continuity PASS
3. G1만 생성
4. maker-view / paws-only / scale / anatomy / fixed props / zero-cut QC
5. PASS → Save frame → G2

## 12. Learning

실제 값만 기록:
- Flow credits / rerolls
- G1~G4 first-pass success
- maker-view/camera failure
- scale/anatomy/continuity failure
- failed action type
- usable motion seconds
- final runtime
- audio replacement
- 24h/72h Stayed to watch / APV / engaged views / subscribers / comments

장기 KPI:
```text
usable motion / credit
engaged views / credit
subscribers / 100 credits
```

## 13. 가장 단순한 사용자 인터페이스

사용자:
```text
다음 영상 준비해줘
```

ChatGPT가 handoff + charter + current standard + production/research/history 확인 → novelty-safe episode 선택 → manifest/NEXT_EPISODE/handoff 준비.

사용자 로컬:
```powershell
./tools/make_next_short.ps1
```

자동화는 Flow 크레딧을 쓰거나 유료 영상을 생성하거나 YouTube에 게시하지 않는다.

## 최종 목표

> **Mini Forest의 사람 손만 자연스러운 고양이 앞발로 바꾼 듯한 초소형 힐링 제작 영상을, 실제 성과와 실패 데이터를 이용해 점점 더 높은 품질/credit 효율로 만든다.**
