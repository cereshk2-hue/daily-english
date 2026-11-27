# 11/27 선생님: 중산고1 비밀노트 22·23 — 아이들이 너무 어려워함 → 해설에 영어 선지 + 해석 + 다른 선지가 왜 답이 아닌지까지
# build_bimi.py가 key ('3', n) 문항의 해설 앞부분(정답·이유·오답)을 이걸로 바꾸고, 원래 출제 메모·포인트는 뒤에 그대로 둠
EX = {
1: """정답 ▶ ② The Gift of Heightened Physical and Psychic Well-Being Cultivated by the Gardens
    (정원이 길러 주는, 높아진 신체적·정신적 행복이라는 선물)
이유 ▶ 앞부분은 정원 가꾸기의 신체적 이점(근력·칼로리·저강도 운동), 뒷부분은 정신적 이점(스트레스 감소·마음 챙김·자존감) → 몸과 마음 둘 다 = Physical and Psychic
✘ ① Better Emotional Fitness That Can Definitely Translates Into Better Physical Health (더 나은 정서적 건강이 확실히 더 나은 신체 건강으로 이어진다) → 정서가 신체를 좋게 만든다는 '인과'는 없음. 두 이점을 나란히 말할 뿐 (Translates도 어법 오류)
✘ ③ The Spiritual Serenity That Comes From Fulfilling the Repetitive Chores of Everyday Life (일상의 반복적 허드렛일을 해내는 데서 오는 영적 평온) → '일상의 허드렛일' 전반이 아니라 정원 가꾸기, 신체 이점이 빠짐
✘ ④ The Positive Impacts of Physical Exercises Through Gardening on Both Nature and Humans (정원 가꾸기 운동이 자연과 인간 모두에 주는 긍정적 영향) → 자연(Nature)에 주는 영향은 글에 없음
✘ ⑤ The Superiority of Activities Through Gardening Compared to Traditional Exercise Routines (전통적 운동보다 정원 가꾸기 활동이 우월함) → 전통 운동이 힘든 사람에게 좋다고 했을 뿐, 더 낫다(우월)고 비교하지 않음""",
2: """정답 ▶ ④ Man has qualitatively extended the capacity of his finite senses by employing various aids.
    (인간은 다양한 보조 도구를 써서 유한한 감각의 능력을 질적으로 넓혀 왔다.)
이유 ▶ 첫 문장(도구가 감각으로 못 느끼는 현상을 지각하게 해 줌) + 증폭·변환·측정 예시 → 도구로 감각의 한계를 넘어섰다
✘ ① The supplement of sensory powers through devices predicts a human in the future. (도구를 통한 감각 능력 보충이 미래의 인간을 예측한다) → 미래 예측 이야기 없음
✘ ② Reliance on the machines causes the unique power of the human senses to dissipate. (기계 의존이 인간 감각 고유의 힘을 사라지게 한다) → 감각이 약해진다는 부정적 내용 없음
✘ ③ Fragile humans rose to mastery over nature through the invention of various machines. (연약한 인간이 다양한 기계 발명으로 자연을 지배하게 되었다) → '지배'가 아니라 '지각(perception)'을 넓힌 것
✘ ⑤ Devices to compensate for the limits of human sensors have caused a loss of human faculties. (인간 감각의 한계를 보완하는 도구가 인간 능력의 상실을 불러왔다) → 능력 상실 내용 없음, 오히려 확장""",
3: """정답 ▶ ⑤ the plants you nurture with care return the favor by tending to your body and mind in kind
    (네가 정성껏 키우는 식물이 똑같이 네 몸과 마음을 돌봄으로써 보답한다)
이유 ▶ 글 전체가 정원 가꾸기의 신체적 이점 + 정신적 이점 → 내가 식물을 돌보면 식물이 몸과 마음을 돌봐 준다
✘ ① the rewards of gardening can extend beyond the gardener to the whole community (정원 가꾸기의 보상은 정원사를 넘어 공동체 전체로 퍼질 수 있다) → 공동체 이야기 없음, 개인의 몸과 마음
✘ ② sticking to traditional workouts can make you miss multiple benefits of gardening activities (전통 운동만 고집하면 정원 가꾸기의 여러 이점을 놓칠 수 있다) → 전통 운동과 비교·경고하는 글이 아님
✘ ③ the repetitive nature of activities that gardening requires leads to increased mental fatigue (정원 가꾸기의 반복적 활동이 정신적 피로를 늘린다) → 반대. 반복 작업은 마음 챙김(mindfulness)을 유도
✘ ④ the simplicity of the gardening practice can be a cozy refuge to those tired of a hard life (정원 가꾸기의 단순함이 고된 삶에 지친 이들의 안락한 도피처가 될 수 있다) → 정신적 이점 일부만, 신체적 이점이 빠짐. '도피처'도 글의 초점이 아님""",
4: """정답 ▶ ③ they extended our senses, letting objects that existed apart from us step into our territory
    (그것들(도구)은 우리 감각을 확장해, 우리와 동떨어져 있던 대상이 우리 영역 안으로 들어오게 했다)
이유 ▶ 첫 문장 '감각으로 지각할 수 없는 자연 현상을 우리 지각 안으로 가져다준다'를 바꿔 쓴 말
✘ ① our deficient abilities were complemented by their support, allowing us to rule over nature (부족한 능력이 도구의 도움으로 보완되어 자연을 지배하게 되었다) → '자연 지배'는 글에 없음
✘ ② the greater our capacities grew with them, the more objects needed to observe only expanded (도구와 함께 능력이 커질수록 관찰해야 할 대상만 더 늘어났다) → 관찰 대상이 '늘어나 부담'이라는 내용 없음
✘ ④ their dramatic advances brought us benefits, but they also caused equal amounts of pain to us (극적인 발전이 이익을 주었지만 같은 만큼의 고통도 주었다) → 부정적 측면 없음
✘ ⑤ with our dependence on them increased came a corresponding decline in our inherent capacity (도구 의존이 커지면서 타고난 능력도 그만큼 줄었다) → 능력 감소 내용 없음""",
5: """정답 ▶ ① (A) - (C) - (B)
이유 ▶ 주어진 글: 정원 가꾸기 = 훌륭한 신체 활동(근력·유연성·지구력)
→ (A) 칼로리 소모·저강도 운동 (신체 이점 계속)
→ (C) Besides physical health(신체 건강 말고도) → 정신 건강 이점 시작
→ (B) 연구 결과(기분·인지·우울 증상) + 성취감·자존감 (정신 이점 마무리, also)
✘ (B)로 시작(②③) → 주어진 글이 신체 이야기인데 바로 연구·성취감으로 갈 수 없음
✘ (C)로 시작(④⑤) → Besides physical health는 신체 이점이 다 나온 뒤((A) 뒤)여야 함""",
6: """정답 ▶ ② (B) - (A) - (C)
이유 ▶ 주어진 글: 도구가 감각으로 못 느끼는 현상을 지각하게 해 줌
→ (B) In some cases 신호 증폭(망원경) + Other instruments 지각 못 하는 신호를 관찰 가능한 것으로 바꿈
→ (A) Some of these(= Other instruments 중 일부) 현재 감각 범위 확장(자외선 이미지·들을 수 없는 소리)
→ (C) Alternatively 감각 능력이 전혀 없는 속성을 측정
✘ (A)로 시작(①) → Some of these의 these가 가리킬 말(Other instruments)이 앞에 없음
✘ (C)로 시작(④⑤) → Alternatively(그 대신, 또 다른 방법으로)는 다른 방법들이 먼저 나온 뒤
✘ ③ (B)-(C)-(A) → (A)의 Some of these는 (B)의 Other instruments 바로 뒤에 와야 함""",
7: """정답 ▶ ④ (C) - (A) - (B)
이유 ▶ 주어진 글: 정원 가꾸기 = 신체 활동(근력·유연성·지구력)
→ (C) That is(즉) 불필요한 체지방이 쌓일 틈이 없음 + 저강도 운동 (신체 이점 이어서)
→ (A) However 이점은 근력 이상 → 정신 건강 이점
→ (B) 전문가 연구(기분·인지·우울) + also 자신감·삶의 질
✘ (A)로 시작(①) → 주어진 글 바로 뒤에 However로 정신 건강을 꺼내면 (C)의 신체 이야기가 끊김
✘ (B)로 시작(②③) → 연구 결과·also는 정신 건강 이야기가 먼저 나와야 함
✘ ⑤ (C)-(B)-(A) → (B)의 also·정신 이점이 However(A)보다 먼저 올 수 없음""",
8: """정답 ▶ ⑤ (C) - (B) - (A)
이유 ▶ 주어진 글: 도구가 감각 밖 현상을 지각하게 해 줌
→ (C) For example 망원경 = 신호를 단순히 증폭하는 전형적 사례
→ (B) Instead of enlarging the image(이미지를 확대하는 대신) 지각 못 하는 신호를 관찰 가능한 것으로 바꾸는 도구 + 자외선 이미지
→ (A) This process of conversion(이 변환 과정) 소리도 마찬가지 + Additionally 감각 없는 속성 측정
✘ (A)로 시작(①) → This process of conversion이 가리킬 '변환' 이야기가 앞에 없음
✘ (B)로 시작(②③) → Instead of enlarging the image는 '확대(망원경)' 이야기 (C) 뒤에 와야 함
✘ ④ (C)-(A)-(B) → (A)의 This process of conversion은 변환을 소개하는 (B) 뒤""",
9: """정답 ▶ ①
이유 ▶ 주어진 문장: 정원 가꾸기는 전통적 운동이 힘든 사람에게 특히 좋다
→ ① 뒤 It's a low-impact way(저강도 방법이다) ~ accessible for people of all ages: 주어진 문장을 이어 설명
✘ ② 뒤는 Besides physical health 이후 정신 건강 이야기라 '운동' 문장이 들어갈 수 없음
✘ ③④⑤ 모두 정신 건강(차분함·마음 챙김·연구·성취감) 흐름 한가운데""",
10: """정답 ▶ ③
이유 ▶ 주어진 문장: Other instruments(다른 도구들)는 지각 못 하는 신호를 관찰 가능한 것으로 바꾼다
→ ③ 앞 = 증폭하는 도구(망원경) / ③ 뒤 = Some of these(그중 일부)가 감각 범위 확장 → these = Other instruments
✘ ①② → 아직 첫 번째 방법(증폭)과 망원경 예시가 나오기 전
✘ ④⑤ → Some of these가 가리킬 말이 그 앞에 없게 되고, Specifically·Alternatively 흐름이 끊김""",
11: """정답 ▶ ④
이유 ▶ 주어진 문장: 그 진정 효과(That appeasing effect)는 처음엔 이해가 안 될 수 있다, 정원 가꾸기는 일상적 허드렛일 같으니까
→ ④ 앞 = 차분하고 명상적, 스트레스·불안 감소(= appeasing effect) / ④ 뒤 = However 전문가들이 보여 줬다(의심 → 반박)
✘ ①② → 아직 신체 이점 이야기, 진정 효과가 나오기 전
✘ ③ → 진정 효과(calming)가 나오기 바로 전이라 That appeasing effect가 가리킬 말이 없음
✘ ⑤ → However 뒤라 '의심 → 그러나 연구는'의 흐름이 거꾸로 됨""",
12: """정답 ▶ ④
이유 ▶ 주어진 문장: 그런 도구(such a device)의 대표적 예는 보이지 않는 적외선 신호를 볼 수 있는 이미지로 바꾸는 것
→ ④ 앞 = Some of these expand the range of our existing senses(감각 범위 확장) / ④ 뒤 = The same is true of 소리 변환(마찬가지로 소리도)
✘ ①② → 망원경(확대·증폭) 이야기, 적외선 '변환'과 다름
✘ ③ → 아직 '감각 범위 확장'이 나오기 전이라 such a device가 가리킬 말이 없음
✘ ⑤ → The same is true of(소리도 마찬가지) 앞에 시각 예가 먼저 와야 함""",
13: """정답 ▶ ③
이유 ▶ ③ 명상의 이점은 잘 알려져 있고, 오래 명상한 사람은 대인 관계가 더 좋다 → 정원 가꾸기가 아닌 '명상' 자체와 '대인 관계' 이야기
✔ ① 현재에 집중, 스트레스·불안 감소 = 정원 가꾸기의 정신적 이점
✔ ② 반복 작업이 마음 챙김을 유도 = 정원 가꾸기
✔ ④ 정원에서 보내는 시간이 기분·인지·우울 증상 개선 = 정원 가꾸기
✔ ⑤ 식물이 자라는 걸 보는 성취감 → 자존감 = 정원 가꾸기""",
14: """정답 ▶ ②
이유 ▶ ② 도구의 발전이 실용성을 넘어 과학 발전의 원동력이 되었다 → '감각을 넓혀 주는 도구의 종류' 흐름과 무관(과학 발전 이야기)
✔ ① 신호 증폭(망원경) = 첫 번째 종류
✔ ③ 지각 못 하는 신호를 관찰 가능한 것으로 바꿈 = 두 번째 종류
✔ ④ 그중 일부는 감각 범위 확장(자외선·소리)
✔ ⑤ Alternatively 감각이 전혀 없는 속성 측정 = 세 번째 종류""",
15: """정답 ▶ ⑤
이유 ▶ ⑤ 네 '회사(firms)'가 자라고 번창하는 걸 보는 성취감 → 정원 가꾸기 글인데 회사가 나옴 (원문 plants를 firms로 바꾼 함정)
✔ ① 나이·체력 상관없이 할 수 있는 운동 = 신체 이점
✔ ② What is better 정신 건강 이점, 차분하고 명상적
✔ ③ It means 반복 작업 → 마음 챙김
✔ ④ Also 연구: 인지 향상·우울 완화 → 자신감·행복""",
16: """정답 ▶ ④
이유 ▶ ④ 들을 수 없는 소리를 바꾸는 것이 청각 기관에 해로울 수 있다 → 도구가 감각을 '넓혀 준다'는 흐름에 '해롭다'는 엉뚱한 내용
✔ ① 지각 못 하는 신호를 관찰 가능한 것으로 바꾸는 도구
✔ ② 그중 일부는 감각 범위 확장
✔ ③ 대표적 예: 자외선 기반 이미지
✔ ⑤ Alternatively 감각이 없는 속성 측정""",
17: """정답 ▶ ③ (3개: ⓒ ⓓ ⓕ)
✔ ⓐ It involves a range of motions, from A to B → 맞음 (It = gardening, involves 단수)
✔ ⓑ small tasks ~ can burn many calories → 맞음 (작은 일들이 칼로리를 '태우는' 능동)
✘ ⓒ making them accessible → making it accessible (it = a low-impact way/gardening, 단수)
✘ ⓓ similar to meditate → similar to meditation (전치사 to 뒤에는 명사)
✔ ⓔ spending time ~ can elevate, improve, and reduce → 맞음 (동명사 주어 + 동사원형 병렬)
✘ ⓕ watching your plants grow and to thrive → grow and thrive (지각동사 watch + 목적어 + 동사원형, 병렬)""",
18: """정답 ▶ ⑤ (5개 모두)
✘ ⓐ natural phenomena where we can't perceive → that (perceive의 목적어가 빠진 불완전한 절 → 관계대명사, where ✘)
✘ ⓑ this is consisted of → this consists of (consist는 자동사, 수동 ✘)
✘ ⓒ ones what we can observe → ones that (선행사 ones가 있으면 what ✘)
✘ ⓓ the range of which human ears can hear → the range of what (of의 목적어 + hear의 목적어가 없는 절 → 선행사를 품은 what)
✘ ⓔ that which we can be observed → that which we can observe (주어 we가 관찰하는 능동)""",
19: """정답 ▶ ④ (4개: ⓑ ⓒ ⓔ ⓕ)
✔ ⓐ improve(향상시키다) strength → 맞음
✘ ⓑ burp(트림하다) → burn(태우다) many calories
✘ ⓒ accessory(액세서리, 부속물) → accessible(이용하기 쉬운)
✔ ⓓ focus on(~에 집중하다) the present moment → 맞음
✘ ⓔ indulge(빠지다, 탐닉하다) → induce(유도하다) a state of mindfulness
✘ ⓕ boast(자랑하다) → boost(높이다) self-esteem
포인트 ▶ 철자가 비슷한 단어 짝(burp/burn, accessory/accessible, indulge/induce, boast/boost)""",
20: """정답 ▶ ③ (3개: ⓑ ⓒ ⓔ)
✔ ⓐ natural(자연의) phenomena → 맞음
✘ ⓑ amputating(절단하는) → amplifying(증폭하는) signals
✘ ⓒ object(반대하다) → observe(관찰하다)
✔ ⓓ outside(~ 밖의) the range of what human ears can hear → 맞음 (들을 수 있는 범위 밖)
✘ ⓔ sensible(분별 있는) → sensory(감각의) capacity""",
21: """정답 ▶ ① (1개: ⓑ)
✔ ⓐ , which involves ~ → 맞음 (계속적 용법, 선행사 a fantastic form of physical activity)
✘ ⓑ many calories can burn → can be burned (칼로리는 '태워지는' 것, by small tasks가 행위자)
✔ ⓒ , which makes it accessible → 맞음 (it = gardening)
✔ ⓓ allows you to focus ~ and reduce ~ → 맞음 (to focus와 (to) reduce 병렬)
✔ ⓔ The repetitive tasks that are involved in → 맞음 (that are 생략 전 형태)
✔ ⓕ can elevate mood and improve cognition, reducing ~ → 맞음 (분사구문)
✔ ⓖ watching your plants growing and thriving → 맞음 (지각동사 + 목적어 + -ing 가능)""",
22: """정답 ▶ ④ (4개: ⓐ ⓒ ⓔ ⓖ)
✘ ⓐ natural phenomena what we can't perceive → that (선행사 phenomena가 있으면 what ✘)
✔ ⓑ any signal that feeds into → 맞음 (any signal 단수 → feeds)
✘ ⓒ bring into clear view which is too far away → what (선행사 that이 빠졌으므로 선행사를 품은 what)
✔ ⓓ turn signals ~ into what we can observe → 맞음 (into의 목적어 + observe의 목적어 = what)
✘ ⓔ sounds that are normal outside → normally (형용사 outside 앞, 부사로 꾸밈)
✔ ⓕ properties we have no sensory capacity at all for → 맞음 (for which에서 which 생략, for는 뒤로)
✘ ⓖ change it into → change them (them = properties, 복수)""",
23: """정답 ▶ ⑤ (5개: ⓐ ⓓ ⓔ ⓕ ⓖ)
✘ ⓐ improve the decline(감소를 향상시키다) → prevent(막다) the decline
✔ ⓑ help lose some weight → 맞음 (= burn many calories)
✔ ⓒ demanding(힘든) → 맞음 (= challenging)
✘ ⓓ incredulously(믿지 못하겠다는 듯이) → incredibly(엄청나게) calming
✘ ⓔ reducing(줄이는) vitality and relaxation(활력과 휴식) → enhancing(높이는)
✘ ⓕ induce(유도하다) a state of dullness(둔함) → 정원 가꾸기는 둔함이 아니라 마음 챙김을 유도 (block 등으로 바꿔야)
✘ ⓖ elevate(높이다) insensibility(무감각) → 무감각을 높인다 ✘ (lessen 등)""",
24: """정답 ▶ ③ (3개: ⓐ ⓓ ⓕ)
✘ ⓐ we are perceptible of(지각할 수 있는) → imperceptible(지각할 수 없는) (감각으로 못 느끼는 현상이어야 함)
✔ ⓑ enlarging(확대하는) signals → 맞음 (= amplifying)
✔ ⓒ transform(바꾸다) → 맞음 (= turn ~ into)
✘ ⓓ visionary(공상적인, 선견지명 있는) images → visible(눈에 보이는) images
✔ ⓔ belong inside the range of what human ears can't hear → 맞음 (들을 수 '없는' 범위 안에 있는 소리)
✘ ⓕ for which we have sensory capacity at all → lack(없다) (at all = 전혀, 감각 능력이 전혀 '없는' 속성)""",
25: """정답 ▶ ② Specifically(구체적으로) – Furthermore(게다가)
이유 ▶ (A) 앞: 정원 가꾸기의 신체 활동 설명 → (A) 뒤: 그중 특히 전통 운동이 힘든 사람에게 좋다(구체화) → Specifically
         (B) 앞: 연구로 본 정신 건강 이점 → (B) 뒤: 성취감이 자존감을 높인다(이점 추가) → Furthermore
✘ ① Particularly(특히) – In contrast(대조적으로) → (A)는 가능하지만 (B) 뒤는 대조가 아니라 추가
✘ ③ Therefore(그러므로) – Even so(그렇다 하더라도) → (A) 결과가 아님, (B) 양보 아님
✘ ④ In fact(사실) – Nevertheless(그럼에도 불구하고) → (B) 앞뒤가 반대 내용이 아님
✘ ⑤ Hence(따라서) – For instance(예를 들어) → (A) 결과 아님, (B) 성취감은 앞 연구 결과의 예가 아님""",
26: """정답 ▶ ⑤ Watching the growth of your plants creates a sense of achievement, enhancing overall well-being.
    (식물이 자라는 것을 지켜보면 성취감이 생겨 전반적인 행복이 높아진다.) → 마지막 문장과 일치
✘ ① Gardening needs a variety of physical activities as well as rigorous mental planning. (정원 가꾸기는 다양한 신체 활동뿐 아니라 엄격한 정신적 계획이 필요하다) → '엄격한 계획'은 없음
✘ ② Heavy manual labor, such as weeding or mixing compost, is effective for weight control. (잡초 뽑기·퇴비 섞기 같은 '힘든' 육체노동이 체중 조절에 효과적이다) → 본문은 small tasks(작은 일)이고 low-impact(저강도)
✘ ③ Those who struggle with conventional exercise take time to get used to the gardening. (전통 운동이 힘든 사람은 정원 가꾸기에 익숙해지는 데 시간이 걸린다) → 오히려 그런 사람에게 특히 좋다
✘ ④ Gardening allows for mentality to distract from the present distress and concentrate on future. (정원 가꾸기는 현재 고통에서 벗어나 미래에 집중하게 한다) → 본문은 현재 순간(present moment)에 집중""",
27: """정답 ▶ ① ㉠ benefit → beneficent ✘ (beneficial이어야 함)
이유 ▶ be동사 뒤 보어 자리 형용사 '이로운' = beneficial. beneficent는 '자선을 베푸는, 친절한'이라 문맥에 안 맞음
✔ ② ㉡ access → accessible (make it + 형용사 보어 '이용하기 쉬운')
✔ ③ ㉢ credit → incredibly (형용사 calming을 꾸미는 부사 '엄청나게')
✔ ④ ㉣ mind → mindfulness (a state of + 명사 '마음 챙김')
✔ ⑤ ㉤ thrive → thrive 그대로 (watching your plants grow and thrive: 지각동사 + 목적어 + 동사원형 grow와 병렬)
[수정] 원본 선지 ③ incredible(형용사)·⑤ thriving(grow와 병렬이 깨짐)도 틀린 고침이라 답이 셋이 됨 → ③ incredibly, ⑤ thrive 그대로로 바로잡음. 종이 시험지(원본)에서 ③·⑤를 고른 학생은 선생님 판단으로 정답 처리해 주세요.
""",
28: """정답 ▶ ③ focus on anything but an object ✘
이유 ▶ anything but = '~ 말고는 무엇이든', 즉 그 대상에는 집중하지 않는다는 뜻 → 반복 작업은 '한 가지에 집중'하게 해 명상과 비슷 (focus on only one object 등이어야 함)
✔ ① repeating simple tasks constantly (단순한 일을 계속 반복) = The repetitive tasks
✔ ② pay attention to the task at hand and block out distractions (지금 하는 일에 집중하고 방해 요소를 차단) = focus on the present moment
✔ ④ Spending time in nature can help improve your emotional capacity (자연 속 시간이 정서 능력 향상에 도움) = elevate mood, reduce depression
✔ ⑤ make you feel accomplished (성취감을 느끼게 함) = The sense of accomplishment""",
29: """정답 ▶ ② moderate(적당한) – distract from(~에서 벗어나다) – favorable(호의적인, 긍정적인)
요약문 해석 ▶ 정원 가꾸기는 다양한 (A)적당한 강도의 신체 활동을 꾸준히 하게 해 신체 건강에 필요한 요소를 주고, 정서적으로는 현재의 걱정에서 (B)벗어나 더 (C)긍정적인 자기 평가를 기르게 한다.
✘ ① serious(진지한, 심한) – deviate from(벗어나다, 일탈하다) – positive → (A) low-impact(저강도)와 반대
✘ ③ vigorous(격렬한) – engage in(참여하다) – realistic(현실적인) → (A) 격렬 ✘, (B) 걱정에 '참여' ✘
✘ ④ light(가벼운) – obsess with(집착하다) – optimistic(낙관적인) → (B) 걱정에 집착 ✘
✘ ⑤ dynamic(역동적인) – absorb in(몰두하다) – pessimistic(비관적인) → (B)(C) 반대""",
30: """정답 ▶ ④ To illustrate(예를 들어 설명하면) – Furthermore(게다가)
이유 ▶ (A) 앞: 신호를 증폭하는 경우 / 뒤: 망원경 = 그 예 → To illustrate
         (B) 앞: 감각 범위를 넓히는 도구 / 뒤: 감각이 전혀 없는 속성도 측정하는 도구(또 하나 추가) → Furthermore
✘ ① For instance(예를 들어) – In other words(다시 말해) → (A)는 맞지만 (B)는 앞말을 바꿔 말하는 게 아니라 새 종류 추가
✘ ② For example – Therefore(그러므로) → (B) 결과가 아님
✘ ③ However(그러나) – Likewise(마찬가지로) → (A) 대조 아님
✘ ⑤ In addition(게다가) – As a result(그 결과) → (A) 추가가 아니라 예시, (B) 결과 아님""",
31: """정답 ▶ ⑤ What we can't detect at all can be turned into what we can observe with the help of tools.
    (우리가 전혀 감지할 수 없는 것도 도구의 도움으로 관찰할 수 있는 것으로 바뀔 수 있다.) → 마지막 문장과 일치
✘ ① No natural occurrence is beyond the reach of our perception, due to the invention of tools. (도구 발명 덕분에 우리 지각 범위를 넘는 자연 현상은 하나도 없다) → '하나도 없다'는 지나친 일반화
✘ ② A telescope allows us to enlarge the invisible image so that we can see, whatever the distance. (망원경은 거리에 상관없이 보이지 않는 이미지를 확대해 보게 해 준다) → '거리에 상관없이'는 없음, 너무 멀어 안 보이는 것을 보게 할 뿐
✘ ③ Some of the tools can reinvent our sensory scopes to make the previously undetectable visible. (일부 도구는 감각 범위를 '새로 만들어' 감지 못 하던 것을 보이게 한다) → 본문은 reach를 expanding(넓힘), reinvent(재발명) ✘
✘ ④ Our ears only bring what we need into our perceptual field from the signals they hear. (귀는 들리는 신호 중 필요한 것만 지각 영역에 가져온다) → 본문에 없는 내용""",
32: """정답 ▶ ② ⓑ에 대한 설명이 틀림
이유 ▶ ⓑ which는 주격 관계대명사가 맞지만, 선행사 that은 전치사 into의 목적어가 아니라 동사 bring의 목적어 (bring A into clear view에서 A = that이 뒤로 간 형태)
✔ ① ⓐ bring은 translate와 병렬, 목적어는 natural phenomena
✔ ③ ⓒ take는 문장의 동사, 주어 Some of these(복수) → take
✔ ④ ⓓ what은 전치사 of의 목적어, 선행사를 품은 관계대명사
✔ ⑤ ⓔ for which, 선행사 properties, 뒤에 완전한 문장(we have no sensory capacity at all)""",
33: """정답 ▶ ③ ㉢ expand → expansion ✘ (expanding이어야 함)
이유 ▶ 전치사 of 뒤 + 뒤에 목적어 the reach가 있으므로 목적어를 받을 수 있는 동명사 expanding. 명사 expansion은 목적어를 바로 못 받음
✔ ① ㉠ ample → amplifying (simply 뒤 동명사, '증폭하는')
✔ ② ㉡ one → ones (signals를 받는 복수 대명사)
✔ ④ ㉣ norm → normally (형용사 outside를 꾸미는 부사)
✔ ⑤ ㉤ sense → sensory (capacity를 꾸미는 형용사 '감각의')""",
34: """정답 ▶ ④ supplement(보충하다) – extensive(넓은) – beyond(~을 넘어서는)
요약문 해석 ▶ 인간은 감각 기관의 부족을 다양한 도구로 (A)보충해, (B)넓은 범위의 외부 신호를 감지할 수 있게 되었고, 그중 일부는 우리 감각의 범위를 (C)넘어선다.
✘ ① compensate(보상하다) – broad – inside(안에) → compensate는 for가 필요(compensate for), (C) 감각 범위 '안' ✘
✘ ② intensify(강화하다) – constrained(제한된) – within(안에) → (A) 부족을 강화 ✘, (B)(C) 반대
✘ ③ make up for(보충하다) – restrictive(제한적인) – outside → (B) 제한적 ✘
✘ ⑤ aggravate(악화시키다) – comprehensible(이해할 수 있는) – out of → (A) 악화 ✘""",
}
