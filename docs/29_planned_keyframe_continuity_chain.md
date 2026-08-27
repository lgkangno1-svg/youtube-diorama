# 29 — Planned Keyframe Continuity Chain

목표: paid Veo generation 전에 만드는 무료 planned keyframe 자체가 서로 다른 세계처럼 drift하지 않게 한다.

## 문제

First+Last Frame 생성은 입력 endpoint가 서로 호환될수록 유리하다. 그런데 KF0, KF1, KF2...를 각각 독립적인 text-to-image 요청으로 새로 만들면 다음이 달라질 수 있다.

- 고양이 앞발 털무늬/크기/위치
- first-person camera 높이와 각도
- workbench 재질과 구조
- warmer / tray / serving niche 같은 고정 소품
- hero-object의 paw 대비 scale
- 조명/색온도/DOF

이 상태에서 두 keyframe을 First+Last endpoint로 넣으면 paid Veo가 필요한 음식 상태 변화뿐 아니라 **카메라·캐릭터·세트 변화까지 동시에 보간**해야 한다. 이는 continuity drift와 reroll 위험을 키운다.

## 공식 Flow 기능 근거

2026-08-27 Google Flow 공식 도움말 재확인 기준:

- Flow 이미지 생성은 이미지 ingredient/reference를 prompt에 추가할 수 있다.
- 생성된/기존 이미지를 다시 prompt에 추가할 수 있다.
- Nano Banana 계열은 기존 이미지를 반복적으로 edit/refine할 수 있고 이전 버전은 History/Stack에 보존된다.
- `Nano Banana 2 Lite`는 현재 공식 모델 도움말에서 no-charge 이미지 생성/편집 옵션으로 안내되지만, 실제 UI 표시 비용을 최종 기준으로 한다.

따라서 planned KF는 독립 생성보다 **anchor → edit/reference derivation**을 기본으로 한다.

## 기본 절차

```text
KF0_OPEN
→ 첫 master anchor로 생성/검수
→ POV / paw anatomy / scale / camera / fixed props / lighting PASS

KF1
→ KF0을 열어 edit/refine하거나 KF0을 prompt reference/ingredient로 추가
→ manifest가 요구한 상태만 변경
→ 나머지는 보존

KF2
→ 승인된 KF1에서 같은 방식으로 파생

KF3 / KF4...
→ 바로 이전 승인 KF에서 같은 방식으로 파생
```

### 보존 우선순위

1. true first-person camera
2. visible paw count / fur pattern / feline anatomy
3. hero-object-to-paw scale ratio
4. fixed workbench geometry
5. same major props and their screen positions
6. lighting / lens / depth of field
7. food/object state는 manifest가 요구하는 부분만 변화

## 하지 말 것

- KF1~KF4를 매번 완전히 새로운 text-to-image로 독립 생성
- 더 예쁜 결과라는 이유로 camera angle이 바뀐 KF 채택
- warmer/tray/niche가 KF마다 생성/삭제되는 결과 수용
- paw fur나 paw count가 달라졌는데 paid Veo가 알아서 맞춰줄 것으로 기대
- 무료 이미지 단계에서 해결할 drift를 paid video reroll로 넘김

## QC shorthand

`KEYFRAME DRIFT FAIL`

다음 중 하나면 paid G1 전에 repair한다.

- camera position/angle mismatch
- paw identity/anatomy mismatch
- hero scale mismatch
- fixed prop appears/disappears/moves materially
- workbench/lighting language changes enough to read as another set

## planned KF와 actual saved frame의 역할 차이

두 체인은 섞지 않는다.

### Planned Keyframe Chain

무료 이미지 단계에서 미래 destination frame들이 **같은 세계**인지 보장한다.

```text
KF0 → edit/reference → KF1 → edit/reference → KF2 ...
```

### Actual Video Frame Chain

paid scene 사이의 실제 연속성을 보장한다.

```text
G1 PASS actual last usable frame
→ Flow native Save frame
→ G2 First
→ G2 PASS actual last usable frame
→ G3 First
```

즉:

- planned KF = destination / target state
- actual saved frame = next scene continuity bridge

예쁜 planned KF를 actual bridge 대신 사용하지 않는다.

## TK-005 적용

`TK-005 12mm 焼きいも`에서는 KF0을 master anchor로 잡고, KF1~KF4는 승인된 직전 KF에서 파생한다.

반드시 고정:

- 같은 cream + pale ginger front paws
- 같은 first-person camera
- 같은 12mm급 고구마 scale
- 같은 ceramic roasting tray
- 같은 miniature tabletop warmer
- 같은 upper-right serving niche
- 같은 warm macro lighting

변화는 manifest에 정의된 roasting/crack/golden-center/serving 상태만 허용한다.

## 목적

이 정책은 무료 이미지를 더 많이 만드는 정책이 아니다. **필요한 KF 수는 그대로 유지하면서 endpoint compatibility를 높여 paid Veo reroll 가능성을 낮추는 정책**이다.
