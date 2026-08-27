# CURRENT STANDARD — Tiny Cat Kitchen

최신 적용 기준: **2026-08-27 POV Paws Microworld + Planned Keyframe Continuity + Progressive Spend + Adaptive H30/H40**

## 1. 핵심 경험

Tiny Cat Kitchen은 고양이를 밖에서 보는 영상이 아니다.

> **시청자가 고양이가 된 것처럼 1인칭 시점에서 앞발만 보며, 터무니없이 작은 디오라마 음식/물건을 조심스럽게 만드는 힐링 ASMR Shorts**다.

필수:
- true first-person cat POV
- 화면 아래쪽 cream + pale ginger 앞발 1~2개만 등장
- 얼굴/머리/몸통/full cat 금지
- hero object 보통 5~20mm, 화면상 한 앞발 폭의 15~50% 이하
- macro miniature diorama workbench
- mostly locked camera
- 한 8초 generation = 1 primary tactile action + optional 1 micro-payoff
- no rapid montage / no meme zoom / no third-person chef shot

구조적 FAIL:
- third-person/full-cat framing
- 음식/도구가 paw와 비슷하거나 더 큼
- human fingers/thumbs
- human-like tool grip
- tiny-scale contrast가 약함

## 2. Paw-action grammar

선호: `nudge / press / pat / roll / steady / slide / tap`

피함:
- chopsticks / knife / tongs를 사람 손처럼 grip
- thumb-index pinch
- precise twist

## 3. Gate A — planned keyframe continuity chain

Paid Veo 전에 planned keyframe을 먼저 만든다.

현재 공식 Flow 문서 기준 `Nano Banana 2 Lite`는 no-charge 이미지 generation/editing 기본 옵션으로 안내되지만, **실제 Flow UI의 모델명과 표시 비용이 최종 source of truth**다.

```text
Flow image generation
→ active image model + displayed cost 확인
→ no-charge일 때만 0-credit preflight로 사용
→ KF0를 master visual anchor로 생성
→ POV / paws / scale / camera / fixed props / lighting QC
→ KF1은 승인된 KF0를 edit/refine 또는 reference/ingredient로 파생
→ KF2는 KF1에서 파생
→ 필요한 KF까지 순차 파생
→ planned KF chain 모두 PASS 후에만 G1
```

**KF1+를 독립 fresh text-to-image로 다시 뽑지 않는다.**

보존 대상:
- paw fur/anatomy
- first-person camera
- hero-object scale
- workbench geometry
- fixed props
- lighting/lens language

planned KF가 drift하면 paid Veo로 넘어가지 않는다. shorthand: `KEYFRAME DRIFT FAIL`.

Canonical: `docs/29_planned_keyframe_continuity_chain.md`.

## 4. Flow/Veo production baseline

생성 직전 실제 UI 확인:

```text
NEW VIDEO GENERATION
Veo 3.1 Lite
9:16
8 seconds
output count = 1
displayed cost = current UI truth
```

2026-08-27 공식 Google Flow 도움말 재확인:
- Veo 3.1 Lite 4/6/8s + Extend = non-Ultra 10 credits/generation
- First + Last frames = Lite 4/6/8s 지원
- Ingredients/References-to-Video = Lite 8s-only 가능
- 1080p upscale = Plus/Pro/Ultra 0 credits

기존 영상 edit/Omni Flash 화면을 G scene generation으로 착각하지 않는다.

## 5. Progressive Spend

```text
FREE planned KF chain PASS
→ G1 only
→ QC
→ actual last usable frame를 Flow native Save frame으로 저장
→ G2 only after G1 PASS
→ QC
→ G3 only after G2 PASS
→ QC
→ G4 only if immersive_h40 + G3 PASS + independent world-resolution beat
```

G2/G3/G4를 미리 생성하지 않는다.

## 6. Actual-frame sequential chain

```text
G1 PASS actual frame
→ Flow Save frame
→ G2 First
→ G2 PASS actual frame
→ Flow Save frame
→ G3 First
→ G3 PASS actual frame
→ G4 First (immersive_h40 only)
```

**planned target KF는 destination이고, actual saved frame은 continuity bridge다.**

다음 scene의 First frame을 prettier planned KF로 대체하지 않는다.

## 7. Runtime policy

### compact_h30
- 정확히 3 × 8s Lite scenes
- 현재 first-pass ceiling 30 credits
- final 약 30~36s
- 3 beat로 scale reveal → making → payoff가 완결될 때

### immersive_h40
- 정확히 4 × 8s Lite scenes
- 현재 first-pass ceiling 40 credits
- final 약 38~46s
- G4가 serving / world-resolution / afterglow의 독립 가치를 가질 때만

48~60s는 실제 24h/72h retention과 engaged-views/credit가 지지할 때만 실험한다.

## 8. 8초 scene grammar

> **1 calm tactile primary action + optional 1 passive micro-payoff**

기본 `max_visual_cuts_per_8s_generation: 0`은 generated prompt에 literal zero-cut constraint로 남아야 한다.

좋은 구조:
```text
0~1.5s  paw approaches absurdly tiny object
1.5~6s  one press / roll / slide / nudge action
6~8s    paw stops; steam/crack/gloss/crumb continues
```

## 9. Audio

기본:
```text
No narration
No generated music
Quiet room tone + close tiny tactile ASMR
```

영상 motion이 좋고 audio만 나쁘면 reroll하지 않고 후편집에서 교체한다.

일본어 사용자 녹음은 comprehension / character voice / payoff를 실제로 강화할 때만 짧게 사용한다.

## 10. Idea / research policy

Score:
- benchmark evidence
- Japan relevance
- healing fit
- visual satisfaction
- Flow reliability
- originality
- worldbuilding
- audience demand
- expected credit efficiency

경쟁작에서 exact title / plot / branded product / package / ending은 복제하지 않는다. hook, scale contrast, tactile action, pacing, payoff, seasonal timing 같은 추상 메커니즘만 가져온다.

최근 fingerprint 중복은 deterministic novelty gate로 차단한다. 시즌 근거가 이미 saturated면 같은 종류의 상품 PR을 추가로 쌓지 않는다.

## 11. 현재 제작 상태

`production/NEXT_EPISODE.txt` = **TK-005**

`猫の前足で作る、12mmの焼きいも。`

- runtime: `immersive_h40`
- 4 Lite scenes / 현재 40-credit first-pass ceiling
- KF0 = master planned anchor
- KF1→KF4 = 이전 approved KF에서 edit/reference 파생
- 같은 roasting tray / tabletop warmer / serving niche 유지
- G2/G3/G4 First = 이전 PASS clip의 Flow-native saved actual frame
- no direct pinch/grab
- zero-cut long take

최우선 실제 단계:
1. TK-005 planned KF0→KF4 continuity PASS
2. G1만 생성
3. POV / scale / anatomy / camera / fixed props / zero-cut QC
4. PASS 시 Save frame → G2

## 12. Learning

실제 데이터만 기록한다:
- Flow credits
- rerolls
- G1/G2/G3/G4 first-pass success
- POV/scale/anatomy/continuity failure
- failed action type
- usable motion seconds
- final runtime
- narration/audio replacement
- 24h/72h Stayed to watch
- APV
- engaged views
- subscribers
- comments

장기 KPI:
```text
usable motion / credit
engaged views / credit
subscribers / 100 credits
```

placeholder 0을 실제 관측값처럼 학습하지 않는다.

## 13. 가장 단순한 사용자 인터페이스

사용자:
```text
다음 영상 준비해줘
```

ChatGPT:
- 최신 research/history 확인
- novelty-safe episode 선택
- manifest/NEXT_EPISODE 준비
- handoff 동기화

사용자 로컬:
```powershell
./tools/make_next_short.ps1
```

자동화는 Flow 크레딧을 쓰거나 유료 영상을 생성하거나 YouTube에 게시하지 않는다.

## 14. 최종 목표

> **고양이 캐릭터를 보여주는 AI 영상이 아니라, 시청자가 고양이의 앞발이 된 듯한 시점에서 믿기 어려울 만큼 작은 세계를 만지는 힐링 경험을, 가능한 적은 실패 generation으로 만든다.**
