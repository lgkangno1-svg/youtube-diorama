# Motion-Dense Healing H30 — Tiny Cat Kitchen

작성 기준: 2026-08-24
상태: H30 보완 기준

## 핵심 교정

`힐링 = 정지화면이 많음`으로 해석하지 않는다.

Tiny Cat Kitchen의 기본값은 **느린 움직임이 계속 이어지는 힐링**이다. Veo 3.1 Lite 8초 × 3회 = 30 credits 구조는 유지하되, 최종 영상의 moving-footage density를 높이고 정지 keyframe으로 러닝타임을 억지로 채우지 않는다.

## 왜 바꾸는가

YouTube monetization policy는 최소한의 narrative/commentary/value만 있는 image slideshow나 반복 template을 inauthentic content 위험 예시로 든다. 우리 H30은 원래 24초 motion + 10~20초 keyframe/slow zoom으로 35~45초를 만들 수 있게 설계했지만, 이를 과용하면 힐링보다 `AI slideshow`로 느껴질 수 있다.

따라서 목표는:

```text
calm ≠ static
calm = continuous small motion + long shot duration + sound continuity
```

## H30-M 기본값

```text
Veo 3.1 Lite 8s × 3 = 24s raw generated motion
final runtime = 30~36s 권장
motion density >= 80%
static/keyframe holds <= 5s total
```

40초를 채우기 위해 10초 이상의 still/zoom을 붙이지 않는다.

### 허용되는 느린 움직임

- paw slowly enters / nudges / pauses
- one or two gentle stirs
- tiny steam continuously rises
- sauce slowly spreads
- rain moves on window
- cloth or curtain subtly moves
- plate gently slides into position
- cat paw rests but fur/steam/environment still has living motion

### 피할 것

- 3~5초 완전 정지 image 반복
- 여러 still을 Ken Burns로만 연결
- 같은 hero image를 다른 crop으로 재활용해 러닝타임 증가
- 40초를 맞추기 위한 의미 없는 pause

## Playback-speed rule

원본 motion이 충분히 자연스럽고 이미 느린 경우에만 **0.90~1.00x** 안에서 소폭 조정한다.

- 0.90x: 24s raw motion → 약 26.7s
- 여기에 3~5s의 micro-hold/hero/loop를 더하면 약 30~32s
- 더 긴 영상이 필요하면 억지 slowdown보다 story action 자체를 늘리는 편이 낫다.

0.8x 이하를 기본으로 쓰지 않는다. AI-generated paw/fur/steam은 과도한 slowdown이나 optical-flow interpolation에서 부자연스러움이 커질 수 있다.

## Audio

속도를 늦춘 source의 native audio를 그대로 쓰지 않는다. pitch/tempo artifact가 생길 수 있으므로:

1. native ASMR이 깨끗하고 1.00x면 유지 가능
2. speed change가 있으면 reusable ASMR library로 교체 우선
3. room tone / sizzle bed를 컷 사이 계속 유지해 sound bridge 생성
4. narration은 기본 없음

## 30 vs 40 credits

H30은 러닝타임이 부족해서 실패한 것으로 판정하지 않는다.

4번째 Lite generation 10 credits를 쓰는 조건:

- G1~G3 중 한 scene에 구조적 continuity 오류가 있음
- story의 이해에 필수적인 action이 누락됨
- 24h/72h 데이터로 이미 검증된 winning format의 production quality를 올리는 경우

쓰지 않는 조건:

- 40초를 채우고 싶어서
- 컷 수를 늘리고 싶어서
- static footage가 심심해 보여서

이 경우에는 먼저 final runtime을 30~36초로 줄인다.

## 일본 healing benchmark 보완

일본 AI cat cooking 계열에서도 `ゆっくり丁寧にごはんをつくる`, `心あたたまる`, `癒し` 같은 포지셔닝이 실제로 존재한다. 여기서 배울 점은 장면을 멈추는 것이 아니라 **작은 행동을 천천히 끝까지 보여주는 것**이다.

반면 최근 AI猫にゃんこちん 계열은 강한 사건/생활 상황으로 캐릭터 IP를 확장하고 있다. 따라서 Tiny Cat Kitchen은:

```text
first 1s = immediately legible premise
next 25~30s = calm continuous action
ending = one satisfying or emotional resolution
```

을 기본 문법으로 한다.

## 자동화

`tools/build_healing_edit_plan.py`가 episode YAML의 scene length, static-hold budget, playback-speed range를 읽어 deterministic edit plan을 생성한다.

```bash
python tools/build_healing_edit_plan.py episodes/TK-001.yaml
```

또는 전체 bundle:

```bash
python tools/build_episode_bundle.py episodes/TK-001.yaml
```

이제 bundle은 originality validation + Flow pack + healing edit plan + publish pack을 한 번에 만든다.

## 최종 원칙

> **크레딧을 아끼기 위해 정지화면을 늘리지 않는다. 같은 30 credits 안에서 느리지만 계속 움직이는 30~36초를 만든다.**
