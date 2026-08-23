# Google Flow 장면별 생성 프롬프트

## 목적

첫 파일럿 Shorts:

> **猫の手で3cmオムライスは作れる？**

최종 길이: 약 45초  
포맷: 9:16 세로형  
타깃: 일본 10대·20대  
핵심: 고양이 앞발 + 실제 먹을 수 있어 보이는 3cm 오므라이스 + 미니 주방 ASMR + 반전 + 루프

---

## 1. 권장 Flow 제작 방식

Google Flow에서는 전체 45초를 한 번에 생성하지 말고 **8초 클립 6개**를 만든 뒤 Scenebuilder에서 이어 붙이고 필요한 부분을 트리밍한다.

권장 설정:
- Aspect Ratio: 9:16 portrait
- Model: Veo 3.1 Fast로 테스트 → 중요한 컷은 Quality 재생성
- Ingredients/References: 동일 캐릭터·주방·도구를 매 클립 재사용
- Clip length: Ingredients 사용 시 8초 중심
- Audio: 자연스러운 조리 ASMR 위주
- Dialogue/Text: 생성 단계에서는 없음

후편집에서 일본어 내레이션과 자막을 별도로 넣는다. 생성 영상 내부에 일본어 문자를 직접 만들게 하면 깨진 문자가 생길 가능성이 있으므로 피한다.

---

## 2. 먼저 만들어둘 Reference / Ingredient 이미지

### @CatPaws

**Prompt**

```text
Photorealistic orange tabby cat with two small white-socked front paws, warm orange striped fur, soft realistic fur texture, anatomically correct feline paws with no human fingers and no thumbs, cute but not cartoonish, Japanese domestic cat look, clean paws, neutral pose, isolated on a simple light beige background, soft studio lighting, highly consistent character reference, vertical 9:16 composition.
```

### @TinyKitchen

**Prompt**

```text
A photorealistic miniature Japanese home kitchen built at dollhouse scale, warm natural wood counter, tiny cream enamel stove, tiny stainless steel sink, small ceramic bowls, tiny wooden cutting board, subtle Showa-era Japanese cozy atmosphere with modern cleanliness, warm morning window light, extremely detailed miniature craftsmanship, shallow depth of field, macro photography, no people, no animals, no text, vertical 9:16.
```

### @MiniCookware

**Prompt**

```text
A matching set of realistic dollhouse-scale cookware for a miniature Japanese kitchen: a tiny black nonstick frying pan about 4 cm wide, tiny wooden spatula, tiny ceramic mixing bowl, tiny spoon, tiny white plate, all physically plausible, clean and consistent in scale, isolated on a neutral background, photorealistic macro product photography, no text.
```

### @MiniOmurice

**Prompt**

```text
A fully edible-looking 3 cm Japanese omurice on a tiny white ceramic plate, glossy soft yellow omelet wrapped around ketchup fried rice, one very thin neat ketchup line on top, a tiny parsley leaf beside it, realistic steam, realistic food texture, photorealistic macro food photography, no hands, no text, neutral background.
```

---

## 3. 모든 장면에 반복해서 넣을 Consistency 문장

아래 블록은 가능하면 모든 클립 프롬프트 끝에 붙인다.

```text
Use @CatPaws, @TinyKitchen and @MiniCookware as strict visual references. Keep exactly the same orange tabby fur pattern, white sock paws, kitchen layout, frying pan, plate, lighting, scale and lens look across the entire clip. The paws remain anatomically feline at all times: no human fingers, no thumbs, no human hands, no extra limbs. Do not morph or replace utensils. Do not duplicate or vanish ingredients. Keep all object sizes constant. No on-screen text, no subtitles, no logos, no watermark. Photorealistic miniature macro cinematography, shallow depth of field, warm Japanese kitchen atmosphere, realistic physics.
```

---

# SCENE 1 — 0~8초
## 훅: 고양이 발에 작은 달걀을 주면?

### 목표 화면
- 첫 0.5초부터 고양이 앞발 + 아주 작은 달걀 재료 + 미니 팬
- 완성 오므라이스는 보여주지 않음
- `도대체 이걸로 뭘 만들지?`라는 질문 생성

### Flow Prompt

```text
Vertical 9:16 macro cinematic shot inside @TinyKitchen. Start immediately with an extreme close-up of @CatPaws entering frame from the right and gently tapping a tiny pearl-sized egg mixture cup beside the miniature frying pan from @MiniCookware. The tiny pan is already warming on the miniature stove. The cat paw pauses as if deciding whether it can really cook with something this small, then carefully nudges the tiny egg cup toward the pan. The scale difference between the soft cat paw and the extremely tiny cookware should feel surprising and irresistibly cute. Camera slowly pushes in during the first three seconds. End the clip with the paw hovering above the egg cup, about to begin cooking, creating suspense.

Natural audio only: subtle room tone, soft paw tap on wood, tiny ceramic click, very quiet stove sound. No music, no speech.

Use @CatPaws, @TinyKitchen and @MiniCookware as strict visual references. Keep exactly the same orange tabby fur pattern, white sock paws, kitchen layout, frying pan, plate, lighting, scale and lens look across the entire clip. The paws remain anatomically feline at all times: no human fingers, no thumbs, no human hands, no extra limbs. Do not morph or replace utensils. Do not duplicate or vanish ingredients. Keep all object sizes constant. No on-screen text, no subtitles, no logos, no watermark. Photorealistic miniature macro cinematography, shallow depth of field, warm Japanese kitchen atmosphere, realistic physics.
```

### 후편집 일본어 VO

```text
猫の手に卵を渡した結果…
作るのは、3センチのオムライス。
```

---

# SCENE 2 — 8~16초
## 밥 10알 + 케첩 한 방울

### 목표 화면
- 극단적으로 적은 양의 재료
- 계란으로 넘어가기 직전에 새 오픈루프

### Flow Prompt

```text
Continue in the exact same @TinyKitchen. Macro top-down three-quarter angle. @CatPaws gently pushes exactly about ten visible grains of cooked white rice into the tiny frying pan using the miniature wooden spatula from @MiniCookware. Add one tiny glossy drop of ketchup. The paw makes small precise stirring motions with the utensil, creating miniature ketchup fried rice. Show realistic sizzling, tiny steam and glossy rice texture. Halfway through, cut to an extreme macro of the rice turning orange-red. Near the end, reveal the tiny bowl of yellow egg mixture waiting beside the pan. The cat paw stops stirring and slowly turns toward the egg bowl, implying that the hardest part is next.

Natural ASMR audio: tiny sizzling, soft wooden spatula scrape, microscopic ceramic clinks. No music, no speech.

Use @CatPaws, @TinyKitchen and @MiniCookware as strict visual references. Keep exactly the same orange tabby fur pattern, white sock paws, kitchen layout, frying pan, plate, lighting, scale and lens look across the entire clip. The paws remain anatomically feline at all times: no human fingers, no thumbs, no human hands, no extra limbs. Do not morph or replace utensils. Do not duplicate or vanish ingredients. Keep all object sizes constant. No on-screen text, no subtitles, no logos, no watermark. Photorealistic miniature macro cinematography, shallow depth of field, warm Japanese kitchen atmosphere, realistic physics.
```

### 후편집 VO

```text
ごはんは、これだけ。
ケチャップも一滴。
でも問題は…卵。
```

---

# SCENE 3 — 16~24초
## 15초 클리프행어: 계란이 찢어질 듯한 순간

### 목표 화면
- 시청 지속률 핵심 구간
- 계란이 팬에서 찢어질 듯 말 듯
- 해결은 바로 주지 않고 0.3~0.5초 정적 느낌

### Flow Prompt

```text
Extreme macro close-up in the same miniature kitchen. The tiny clean frying pan now contains an ultra-thin layer of soft yellow egg. @CatPaws uses the same tiny wooden spatula to very carefully lift the delicate edge. The omelet membrane stretches and almost tears near one corner. Build visual tension slowly. The paw freezes for a brief moment when a tiny crack begins to form, as if the entire recipe might fail. Hold this dangerous near-tear moment for roughly half a second. Then, only in the final second of the clip, show that the egg is still barely intact, but do not fully resolve the problem yet. Camera remains extremely close to the trembling omelet edge.

Natural audio: gentle egg sizzle that becomes quieter at the freeze, one tiny wooden tap, then near silence for the suspense beat. No music, no speech.

Use @CatPaws, @TinyKitchen and @MiniCookware as strict visual references. Keep exactly the same orange tabby fur pattern, white sock paws, kitchen layout, frying pan, plate, lighting, scale and lens look across the entire clip. The paws remain anatomically feline at all times: no human fingers, no thumbs, no human hands, no extra limbs. Do not morph or replace utensils. Do not duplicate or vanish ingredients. Keep all object sizes constant. No on-screen text, no subtitles, no logos, no watermark. Photorealistic miniature macro cinematography, shallow depth of field, warm Japanese kitchen atmosphere, realistic physics.
```

### VO

```text
ここで破れたら…全部やり直し。
あっ…。
これ、ヤバい。
```

---

# SCENE 4 — 24~32초
## 계란 올리기 + 30초 두 번째 오픈루프

### 목표 화면
- 계란 위기 해결
- 밥에 올리면서 또 실패 가능성
- 30초 즈음 `이건 고양이가 먹으려고 만든 게 아니다` VO 삽입

### Flow Prompt

```text
Continue seamlessly. The delicate miniature omelet survives. @CatPaws carefully slides the intact yellow omelet from the tiny pan onto a tiny oval mound of ketchup rice on the same white plate from @MiniCookware. The omelet lands slightly off-center and begins to slip. The cat paw reacts quickly, gently nudging the plate and using the same spatula to rescue the alignment without touching the food directly with the paw. Build a second suspense beat around whether the omelet will fall apart. By the end, the omelet sits perfectly centered over the rice. The cat paw pauses proudly, but the ketchup bottle remains just outside the frame, suggesting one final step.

Natural ASMR audio: tiny plate scrape, soft spatula tap, faint sizzling fading away, cat paw tap. No music, no speech.

Use @CatPaws, @TinyKitchen and @MiniCookware as strict visual references. Keep exactly the same orange tabby fur pattern, white sock paws, kitchen layout, frying pan, plate, lighting, scale and lens look across the entire clip. The paws remain anatomically feline at all times: no human fingers, no thumbs, no human hands, no extra limbs. Do not morph or replace utensils. Do not duplicate or vanish ingredients. Keep all object sizes constant. No on-screen text, no subtitles, no logos, no watermark. Photorealistic miniature macro cinematography, shallow depth of field, warm Japanese kitchen atmosphere, realistic physics.
```

### VO

```text
ギリギリ成功。
でも、本当に難しいのはここから。
一回でもズレたら終わり。
でも実は…これ、猫が食べるためじゃありません。
```

---

# SCENE 5 — 32~40초
## 완성 공개 + 먹을 것 같은 페이크

### 목표 화면
- 시각적 보상
- 완성 오므라이스를 가장 예쁘게 보여줌
- 고양이가 먹으려는 듯 다가가며 다음 반전 준비

### Flow Prompt

```text
Hero reveal shot in the same @TinyKitchen. A tiny squeeze bottle releases one impossibly thin but realistic line of ketchup across the 3 cm omurice. Match the final food appearance to @MiniOmurice. Tiny steam rises gently. The camera makes a smooth slow macro orbit of the finished omurice for a beautiful satisfying reveal. A tiny fresh parsley leaf sits beside the omurice. In the second half of the clip, @CatPaws slowly enters frame and approaches the omurice as if the cat is about to steal or eat it. The paw gets very close to the plate. End before the paw touches anything.

Natural ASMR audio: tiny ketchup squeeze, delicate plate click, soft room tone, subtle paw steps. No music, no speech.

Use @CatPaws, @TinyKitchen, @MiniCookware and @MiniOmurice as strict visual references. Keep exactly the same orange tabby fur pattern, white sock paws, kitchen layout, plate, lighting, scale, food appearance and lens look. The paws remain anatomically feline: no human fingers, no thumbs, no human hands, no extra limbs. No object morphing, no ingredient duplication, no scale changes. No on-screen text, no subtitles, no logos, no watermark. Photorealistic miniature macro cinematography, shallow depth of field, warm Japanese kitchen atmosphere, realistic physics.
```

### VO

```text
じゃあ、誰が食べるの？
その前に、完成。
猫が選んだのは…
```

---

# SCENE 6 — 40~48초 생성 후 45초까지 트림
## 반전 + CTA + 완벽한 루프

### 목표 화면
- 고양이가 오므라이스를 지나침
- 파슬리만 가져감
- 마지막에 작은 달걀/계란볼을 처음 위치에 놓아 SCENE 1과 연결

### Flow Prompt

```text
Start with the finished 3 cm omurice exactly as in @MiniOmurice on the tiny white plate inside the same @TinyKitchen. @CatPaws approaches confidently as if it will take the omurice, pauses above the plate, then unexpectedly moves past the omurice and gently taps and takes only the tiny parsley leaf beside it. The omurice remains completely untouched. Create a small comedic pause after the parsley disappears. Then the same paw returns holding the same tiny pearl-sized egg mixture cup from Scene 1 and places it in the exact original position beside the miniature frying pan. Finish on a composition that closely matches the opening frame of Scene 1: cat paw, tiny egg cup, miniature frying pan. The final frame must be visually loopable into Scene 1 with no noticeable jump.

Natural ASMR audio: soft paw tap, tiny leaf rustle, small comedic half-second silence, ceramic click when the egg cup is placed down. No music, no speech.

Use @CatPaws, @TinyKitchen, @MiniCookware and @MiniOmurice as strict visual references. Keep exactly the same orange tabby fur pattern, white sock paws, kitchen layout, frying pan, plate, lighting, scale and lens look across the entire clip. The paws remain anatomically feline at all times: no human fingers, no thumbs, no human hands, no extra limbs. Do not morph or replace utensils. Do not duplicate or vanish ingredients except for the parsley being intentionally carried out of frame. Keep all object sizes constant. No on-screen text, no subtitles, no logos, no watermark. Photorealistic miniature macro cinematography, shallow depth of field, warm Japanese kitchen atmosphere, realistic physics.
```

### VO

```text
そっち！？
オムライス、完全無視。
次は何を作る？
ラーメン？寿司？
猫の手に卵を渡した結果…
```

마지막 문장은 첫 장면 첫 문장과 겹치도록 편집해 자연스럽게 반복 재생되게 한다.

---

## 4. 컷 편집 권장 타임라인

| 구간 | 사용할 장면 | 핵심 기능 |
|---|---|---|
| 0.0~7.0 | Scene 1 | 첫 훅 / 스케일 충격 |
| 7.0~14.0 | Scene 2 | 쌀 10알 / 계란 오픈루프 |
| 14.0~21.5 | Scene 3 | 첫 클리프행어 |
| 21.5~30.5 | Scene 4 | 실패 가능성 / 두 번째 오픈루프 |
| 30.5~38.5 | Scene 5 | 완성 보상 / 먹는 척 |
| 38.5~45.0 | Scene 6 | 파슬리 반전 / CTA / 루프 |

---

## 5. 생성 실패 시 수정 프롬프트

### 고양이 발이 사람 손처럼 변할 때

```text
The cat paws must remain fully anatomical feline paws. Remove all human-like fingers, thumbs and grasping hands. The utensil should be moved by gentle paw pressure and nudging rather than a human grip.
```

### 팬/도구가 컷 중 바뀔 때

```text
Lock the exact frying pan and wooden spatula design from the reference image for the entire clip. No utensil transformation, replacement or spontaneous object changes.
```

### 음식이 갑자기 커질 때

```text
Maintain strict miniature scale. The finished omurice remains exactly 3 cm long relative to the same plate and cat paw throughout the clip. No scale drift.
```

### 재료가 증식할 때

```text
Preserve ingredient count and continuity. No new rice, egg, ketchup, parsley or cookware may appear unless explicitly introduced in the prompt.
```

### 카메라가 너무 정신없을 때

```text
Use one controlled macro camera move only. No handheld shake, no sudden zoom, no fast orbit, no unnecessary angle changes.
```

---

## 6. 이 스타일을 다음 영상에 재활용하는 공식

```text
[같은 CatPaws + 같은 TinyKitchen]
+
[일본인이 0.5초 안에 알아볼 음식]
+
[극단적 크기 또는 숫자 규칙]
+
[중간 실패 가능성]
+
[고양이의 예상 밖 선택]
+
[첫 장면과 연결되는 마지막 프레임]
```

예:
- 쌀 10알 볶음밥
- 계란 한 방울 계란말이
- 1cm 초밥 vs 3cm 초밥
- 10엔 라멘
- 비 오는 날 작은 우동집
- 고양이의 심야 편의점 라멘
