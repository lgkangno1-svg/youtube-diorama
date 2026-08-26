# 27 — Research Evidence Saturation Gate

목표: hourly/regular research가 **새 링크를 수집하는 활동**으로 변질되지 않고, Tiny Cat Kitchen의 실제 제작 의사결정을 개선하는 근거만 저장하게 한다.

## Core rule

> **새 정보가 candidate score, ranking, production timing, Flow assumptions, production mechanics, 또는 실제 성과 학습 중 하나도 바꾸지 않으면 GitHub를 수정하지 않는다.**

## Evidence classes

각 seasonal / trend 후보의 근거는 가능한 한 다음 중 어디에 속하는지 구분한다.

1. `behavioral_demand`
   - 방문자 수
   - 실제 투표
   - 예약/사전주문
   - 검색량/검색 추세
   - 실제 판매/품절/구매 행동

2. `current_preference`
   - 표본과 대상이 명시된 현재 설문
   - 현재 소비자 선호 조사

3. `nationwide_activation`
   - 서로 독립적인 전국 단위 사업자/채널의 실제 출시·캠페인
   - category recognition/timing 근거이지 demand proof는 아님

4. `dated_cultural_activation`
   - 행사/기념일의 예약·판매·프로그램이 실제로 열림
   - 달력 날짜만 있는 상태보다 강함

5. `creator_performance`
   - 현재 인접 Shorts/영상의 조회·좋아요·댓글·구독 전환 등
   - 성공 메커니즘만 추상화

6. `production_evidence`
   - Tiny Cat Kitchen 자체 Flow 실패/성공
   - credits, rerolls, usable motion, continuity/anatomy/POV failure
   - 24h/72h Stayed to watch, APV, engaged views, subscribers, comments

7. `platform_cost_or_feature`
   - Google Flow/Veo 공식 가격 또는 기능 변경

## Saturated candidate

같은 candidate의 현재 freshness window 안에 **서로 다른 evidence class 2개 이상**, 또는 아래 중 하나가 충분히 강하게 있으면 saturated로 본다.

- behavioral demand + current preference
- behavioral demand + nationwide activation
- current preference + 2 independent nationwide activations
- dated cultural activation + nationwide activation

saturated 상태에서는 같은 성격의 PR/출시 뉴스가 한 건 더 생겨도 commit하지 않는다.

## Material-update gate

새 research commit은 아래 중 하나를 명확하게 답할 수 있어야 한다.

- 왜 candidate score가 달라져야 하는가?
- 왜 candidate 순위가 달라져야 하는가?
- 왜 NEXT_EPISODE 또는 publish timing이 달라져야 하는가?
- 왜 Flow action/camera/scale/audio/runtime 설계가 달라져야 하는가?
- 기존 가설을 반박하거나 위험을 새로 발견했는가?
- 기존 evidence가 stale해졌는가?
- 공식 Flow 비용/기능이 바뀌었는가?
- 실제 Tiny Cat Kitchen production/performance가 새 prior를 만들었는가?

전부 `아니오`이면 **NO CHANGE**다.

## Same-day anti-churn

같은 candidate에 대해 같은 날 이미 meaningful research commit이 있었다면 추가 commit 기준을 더 높인다.

추가 허용:
- behavioral signal이 처음 등장
- nationwide activation이 처음으로 2개 이상의 독립 채널로 확장
- production timing/score/ranking이 실제 변경
- 새로운 creator-performance benchmark가 production mechanic을 바꿈
- 공식 Flow 변경
- 실제 사용자 production 결과

추가 금지:
- 세 번째/네 번째 유사 브랜드 출시
- 이미 확인된 seasonal flavor의 또 다른 상품
- 이미 확인된 texture story를 반복하는 retailer PR
- source count만 늘고 decision state가 같음

## Benchmark log discipline

`research/benchmark_log.csv`는 링크 저장소가 아니다.

한 row는 최소 하나를 제공해야 한다.
- measurable creator performance
- 새로운 evidence class
- 새로운 production mechanic
- 기존 가설에 대한 반례
- 후보 timing/ranking에 의미 있는 변화

단순 홍보성 공급 신호만 반복되면 기존 `seasonal_evidence.yaml` summary가 이미 충분한지 먼저 본다.

## Scoring discipline

- promotional supply breadth만으로 `audience_demand`를 올리지 않는다.
- candidate가 이미 `benchmark_evidence=20`이면 같은 종류의 근거를 더 추가해도 score는 바뀌지 않는다.
- score가 cap에 도달한 후보는 **contradictory evidence / behavioral demand / production evidence**를 우선 탐색한다.
- 다음 영상이 이미 manifest로 준비돼 있으면 약한 새 seasonal signal 때문에 NEXT_EPISODE를 흔들지 않는다.

## Current application — 2026-08-26

현재 `IDEA-009 さつまいも・焼きいも`는 survey + behavioral event attendance + multiple nationwide activations가 있어 research-saturated 상태다.

현재 `IDEA-001 月見`도 live dated activation + nationwide mass-market activation이 있어 recognition/timing 측면에서는 saturated에 가깝다.

현재 `IDEA-002 グミの日`도 multiple retailer activations가 이미 있으므로, 다음 meaningful update는 **실제 demand/creator-performance/production reliability evidence**가 우선이다.

따라서 같은 종류의 추가 상품 발표는 원칙적으로 repo 변경을 만들지 않는다.

## Flow assumption recheck

2026-08-26 Google Flow 공식 도움말 재확인 기준:
- Google AI Pro: 1,000 credits / billing cycle
- Veo 3.1 Lite 4s/6s/8s: non-Ultra 10 credits per generation
- Veo 3.1 Lite Extend: non-Ultra 10 credits per generation
- Veo 3.1 Lite First + Last frames: 4s/6s/8s 지원
- 1080p upscale: Plus/Pro/Ultra 0 credits

공식 문서나 실제 Flow UI가 바뀌면 이 문서보다 최신 공식값/UI를 우선하고 production assumptions를 재검토한다.
