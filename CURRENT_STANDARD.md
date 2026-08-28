# CURRENT STANDARD — Tiny Cat Kitchen

최신 적용 기준: **2026-08-29 Mini Forest-style Paw-Only Miniature Making + Maker-View Fail-Closed Validation + Planned Keyframe Continuity + Progressive Spend + Runtime Feasibility**

## 0. 문서 거버넌스

이 문서는 **현재 실행 규칙**이다. 장기 제품 목적과 개선 판단 기준은 `PRODUCT_CHARTER.md`, 현재 상태/최근 결정/실패/다음 우선순위는 `PROJECT_HANDOFF.md`를 따른다.

모든 material 개선 전에 최소한 다음을 함께 확인한다.

```text
latest explicit user direction
→ latest merged repository state + PROJECT_HANDOFF.md
→ PRODUCT_CHARTER.md
→ CURRENT_STANDARD.md + specialized docs
→ current manifest / benchmark / backlog / ledger
```

변경 시 동기화 원칙:
- material repository change → `PROJECT_HANDOFF.md` 같은 branch/PR에서 갱신
- production/QC/Flow 실행 규칙 변경 → 이 `CURRENT_STANDARD.md` 갱신
- durable purpose / creative identity / economics / improvement philosophy 변경 → `PRODUCT_CHARTER.md`도 갱신
- true NO-OP → 문서 churn 금지

비용 절감만으로는 개선이 아니다. `PRODUCT_CHARTER.md`의 판단 기준에 따라 paws-only miniature-making identity, tactile/healing quality, audience outcome per credit, user control을 함께 보호한다.

### Canonical manifest validation path

정상 사용자 경로 `./tools/make_next_short.ps1`은 이제 `tools/validate_maker_view_manifest.py`를 먼저 실행한다.

이 adapter가 현재 의미를 fail-closed로 확인한다.
- `brand_identity.visual_intent = mini_forest_style_paws_only_miniature_making`
- `camera_grammar.semantic_override = mini_forest_style_observational_maker_view`
- `camera_grammar.first_person_required = false`
- `preferred_angles`에 `high_oblique_maker_view` 포함
- `stop_if_maker_view_scale_anatomy_or_premise_fails = true`
- legacy `stop_if_pov_scale_anatomy_or_premise_fails`를 현재 manifest의 active gate로 사용하지 않음

그 다음 기존 `validate_current_standard.py`의 성숙한 구조 검증을 재사용한다: Flow model/output count, H30/H40 scene/credit ceiling, keyframe completeness, actual saved-frame chaining, progressive PASS gates, cut/action limits, runtime feasibility, narration 등.

중요: legacy `camera_grammar.mode: first_person_cat_pov`와 `POV_PAWS_MICROWORLD_V1`은 호환 필드일 뿐이다. **검증기가 이 이름을 근거로 literal first-person을 다시 강제해서는 안 된다.**

## 1. 핵심 경험

Tiny Cat Kitchen은 AI 고양이 캐릭터를 보여주는 채널이 아니다.

> **Mini Forest처럼 아주 작은 음식/물건을 실제로 만드는 미니어처 힐링 영상이며, 사람 손이 들어올 자리를 고양이 앞발이 대신한다.**

필수:
- cream + pale-ginger 실제 고양이 앞발 1~2개만 등장
- 얼굴/머리/몸통/full cat 금지
- 사람 손/손가락/엄지 금지
- hero object 보통 5~20mm, 한 앞발 폭의 15~50% 이하
- realistic handcrafted miniature workbench
- process-first making shot
- mostly locked observational camera
- 1 generation = 1 primary tactile action + optional 1 passive micro-payoff
- no rapid montage / no cat character-performance shot

중요한 변경:
- **true first-person cat POV는 더 이상 필수 조건이 아니다.**
- 기본 카메라는 Mini Forest류의 `high-oblique maker view`다.
- top-down macro / side-oblique macro / tabletop close-up도 동작과 질감이 더 잘 읽히면 허용한다.
- 기존 enum `POV_PAWS_MICROWORLD_V1`은 현재 도구/manifest 호환을 위해 당분간 유지하지만 의미는 `paws-only miniature making`으로 해석한다.

구조적 FAIL:
- cat face/head/body/full-cat
- 고양이가 카운터 뒤에서 사람처럼 요리하는 캐릭터 연기
- human hands/fingers/thumbs
- human-like tool grip
- 음식/도구가 paw와 비슷하거나 더 커서 tiny scale가 약함
- making process보다 넓은 세트/고양이 캐릭터가 주인공이 됨

## 2. Camera / Paw-action grammar

기본 카메라 우선순위:
1. high-oblique maker view
2. top-down macro
3. side/low oblique macro
4. first-person-like angle은 결과가 자연스러울 때만 조건부

선호 paw actions:
`nudge / press / pat / roll / steady / slide / tap / push`

피함:
- chopsticks / knife / tongs를 사람 손처럼 grip
- thumb-index pinch
- precise twist

Mini Forest에서 사람 손이 하는 동작을 그대로 복제하지 않는다. **동작 목적만 유지하고 feline-safe 동작으로 재설계**한다.

## 3. Gate A — planned keyframe continuity chain

Paid Veo 전에 planned keyframe을 먼저 만든다.

```text
Flow image generation
→ active image model + displayed cost 확인
→ no-charge일 때만 0-credit preflight
→ KF0 master visual anchor
→ maker-view / paws / scale / camera / fixed props / lighting QC
→ KF1은 승인 KF0에서 edit/refine/reference 파생
→ KF2는 KF1에서 파생
→ 필요한 KF까지 순차 파생
→ planned KF chain 전체 PASS
→ G1만 생성
```

KF1+를 독립 fresh text-to-image로 다시 뽑지 않는다.

보존 대상:
- paw fur/anatomy/count
- maker-view camera angle/height/lens
- hero-object scale
- workbench geometry
- fixed props
- lighting

## 4. Flow/Veo baseline

생성 직전 실제 UI 확인:

```text
NEW VIDEO GENERATION
Veo 3.1 Lite
9:16
8 seconds
output count = 1
displayed cost = current UI truth
```

2026-08-29 재확인 기준:
- Flow의 no-charge image option은 실제 UI에서 0 credits/no charge인지 매번 확인
- repository의 현행 production assumption은 non-Ultra Veo 3.1 Lite 10 credits/generation
- 실제 Flow UI 모델/모드/output count/표시 비용이 생성 시점 최종 source of truth

기존 영상 edit/Omni Flash 화면을 새 G scene generation으로 착각하지 않는다.

## 5. Progressive Spend

```text
FREE planned KF chain PASS
→ G1 only
→ QC
→ actual last usable frame를 Flow native Save frame으로 저장
→ G2 only after G1 PASS
→ G3 only after G2 PASS
→ G4 only if immersive_h40 + G3 PASS + independent world-resolution value
```

planned KF = destination. actual saved frame = continuity bridge.

## 6. Runtime policy

H30/H40 숫자는 final seconds가 아니라 현재 first-pass credit tier다.

### compact_h30
- 3 × 8s = raw 24s
- current first-pass ceiling 30 credits
- 기본 final 약 24~27s

### immersive_h40
- 4 × 8s = raw 32s
- current first-pass ceiling 40 credits
- 기본 final 약 32~35s
- G4는 serving/world-resolution/afterglow의 독립 가치가 있을 때만

자연스러운 slowdown만 manifest 허용 범위에서 사용한다. 명시되지 않은 still/loop/hold로 길이를 채우지 않는다.

## 7. 8초 scene grammar

> **1 calm tactile primary action + optional 1 passive material payoff**

기본 `max_visual_cuts_per_8s_generation: 0`.

예:
```text
0~1.5s  paw approaches or settles near tiny workpiece
1.5~6s  one press / roll / slide / nudge / push
6~8s    paw stops; steam/crack/gloss/crumb continues
```

## 8. Audio

기본:
```text
No narration
No generated music
Quiet room tone + close miniature ASMR
```

motion이 좋고 audio만 나쁘면 영상 reroll 대신 후편집 교체.

## 9. Research / benchmark policy

1차 제작 벤치마크는 **Mini Forest류 miniature cooking / handcrafted tiny-food / relaxing ASMR**이다.

AI-cat 채널은 고양이 캐릭터 스토리 구조의 1차 기준이 아니다. 필요한 경우 paw appearance/reliability 같은 보조 신호만 참고한다.

경쟁작 exact title / plot / branded product / package / ending은 복제하지 않는다. 다음 추상 메커니즘만 추출한다.
- hand-centric making composition
- real miniature craftsmanship
- tactile process
- seasonal food recognition
- tiny-scale contrast
- calm pacing
- material payoff

연구량 자체가 목표가 아니다. 이미 포화된 evidence class는 ranking/timing/mechanics/freshness/production learning을 실제로 바꾸지 않는 한 추가 commit하지 않는다.

## 10. 현재 제작 상태

`production/NEXT_EPISODE.txt` = **TK-005**

`猫の前足で作る、12mmの焼きいも。`

- runtime: `immersive_h40`
- 4 Lite scenes / current 40-credit first-pass ceiling
- final target 32~35s
- visual intent: Mini Forest-style tiny yakiimo making, human hands replaced by feline front paws
- KF0→KF4 sequential planned-frame continuity
- same roasting tray / warmer / serving niche
- G2/G3/G4 First = previous PASS clip native saved frame
- no direct pinch/grab
- zero-cut long take

최우선 실제 단계:
1. `validate_maker_view_manifest.py` 기준 TK-005 current semantics PASS
2. TK-005 KF0→KF4 maker-view continuity PASS
3. G1만 생성
4. maker-view / paws-only / scale / anatomy / fixed props / zero-cut QC
5. PASS → Save frame → G2

## 11. Learning

실제 데이터만 기록:
- Flow credits / rerolls
- G1~G4 first-pass success
- camera/maker-view failure
- scale/anatomy/continuity failure
- failed action type
- usable motion seconds
- final runtime
- 24h/72h Stayed to watch / APV / engaged views / subscribers / comments

장기 KPI:
```text
usable motion / credit
engaged views / credit
subscribers / 100 credits
```

## 12. 가장 단순한 사용자 인터페이스

사용자:
```text
다음 영상 준비해줘
```

ChatGPT가 `PROJECT_HANDOFF.md` + `PRODUCT_CHARTER.md` + 현재 production/research/history 확인 → novelty-safe episode 선택 → manifest/NEXT_EPISODE/handoff 준비.

사용자 로컬:
```powershell
./tools/make_next_short.ps1
```

이 명령은 current maker-view manifest validator를 먼저 통과한 뒤 production pack을 만든다. 자동화는 Flow 크레딧을 쓰거나 유료 영상을 생성하거나 YouTube에 게시하지 않는다.

## 최종 목표

> **Mini Forest를 고양이 캐릭터 영상으로 바꾸는 것이 아니라, Mini Forest의 사람 손만 자연스러운 고양이 앞발로 바꾼 듯한 초소형 힐링 제작 영상을 만든다.**
