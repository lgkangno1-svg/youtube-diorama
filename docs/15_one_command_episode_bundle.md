# One-command episode bundle

작성 기준: 2026-08-24

## 왜 바꿨나

기존 zero-LLM 파이프라인은 비용은 낮았지만 한 에피소드마다 아래 명령을 따로 실행해야 했다.

```bash
python tools/validate_episode_originality.py episodes/TK-001.yaml
python tools/build_flow_pack.py episodes/TK-001.yaml
python tools/build_publish_pack.py episodes/TK-001.yaml
```

반복 제작에서는 이 운영 마찰 자체가 사람 시간을 잡아먹고, 검사 하나를 빼먹을 위험도 만든다.

## 현재 권장 명령

```bash
pip install -r tools/requirements.txt
python tools/build_episode_bundle.py episodes/TK-001.yaml
```

한 번 실행하면 순서대로:

1. 원본성 검사
2. Google Flow prompt pack 생성
3. YouTube publish pack 생성
4. 두 번의 human approval만 모은 production bundle index 생성

원본성 검사가 실패하면 뒤 단계를 즉시 중단한다. API, LLM, Google Flow 생성, YouTube 업로드는 실행하지 않는다.

생성물:

```text
generated/TK-001_bundle.md
generated/TK-001_flow_pack.md
generated/TK-001_publish_pack.md
```

## Approval A — Flow 크레딧 사용 전

사람은 다음만 확인한다.

- 제목
- 첫 3초 훅
- creator signature
- 무료 Nano Banana 2 Lite 5-keyframe contact sheet
- Flow의 video output count가 반드시 1인지

현재 공식 Google Flow 기준으로 Nano Banana 2 Lite는 Flow에서 무료 기본 이미지 모델이며, 비구독자에게 제공되는 일일 50 무료 Flow 크레딧은 Veo 3.1 Lite/Fast/Quality 동영상 생성에 사용된다. 따라서 keyframe 검수를 먼저 하고 동영상 크레딧을 쓰는 현재 구조를 유지한다.

## Approval B — 업로드 전

- 첫 0.5~1초에 핵심 시각 요소가 바로 읽히는지
- 고양이 발/도구/음식 크기가 장면 사이에서 유지되는지
- creator signature와 해당 에피소드만의 resolution이 남아 있는지
- 포토리얼 합성 영상의 AI disclosure가 올바른지
- 실제 광고 관계가 없는데 paid promotion/Shopping tag를 켜지 않았는지

## 현재 비용 원칙 재검증

2026-08-24 Google 공식 Flow 문서 기준:

- Veo 3.1 Lite: 4/6/8초, 비-Ultra 10 credits / Ultra 5 credits
- Veo 3.1 Fast: 비-Ultra 20 / Ultra 10
- Veo 3.1 Quality: 8초 100 credits
- Gemini Omni Flash: 4초 15 / 6초 20 / 8초 25 / 10초 30 credits
- Omni video edit: 길이 무관 40 credits
- Nano Banana 2 Lite: 무료 기본 image model
- First + Last frame: Lite 지원, Fast는 아직 Coming soon

따라서 기본 탐색은 계속:

```text
5 free keyframes
→ 4 × Lite First+Last generations
→ 편집
→ 실패한 한 장면만 reroll
```

으로 유지한다.

## 중요한 운영 원칙

`build_episode_bundle.py`는 제작을 자동 실행하는 도구가 아니라 **실수하기 쉬운 준비 작업을 deterministic하게 묶는 도구**다.

Google Flow 크레딧 사용과 YouTube 업로드는 계속 사람 승인 뒤에만 수행한다.
