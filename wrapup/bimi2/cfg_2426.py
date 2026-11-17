# 24번 (목표를 낭만화하는 긍정적 환상) — 파일 24_26에서 24번만 (25·26번은 범위 밖)
from build import B, V, arrow
C = dict(
 STEMS=[0, 7, 16, 19, 28, 37, 49, 57, 66, 74, 83, 102, 120, 124, 128, 133, 137, 145],
 END=153,
 DEFSRC=lambda n: '24',
 DROP={6: [38], 11: [84], 12: list(range(103, 113)) + list(range(114, 120)), 15: [129]},
 W={
  6: [B('(A)', 'pushing out of mind how different our day-to-day will need to be for us to make it happen', True)],
  11: [B('①', ['romanticize']), B('②', ['intricacy', 'intricacies']), B('③', ['seduce', 'seduces'])],
  12: [B('어법', arrow('to do', 'to be') + arrow('do', 'be')), B('문맥', arrow('more', 'less'))],
  15: [B('(A)', ['seduce']), B('(B)', ['reflecting'])],
 },
 EXP={
  1: '② happened → happen: make + 목적어(it) + 동사원형(사역) // ① what(~하는 것, take의 목적어 빠짐) ③ lead us to put(lead O to V) ④ of + 동명사 integrating ⑤ reflect on + 간접의문문 why // 사역동사 make + O + 원형',
  2: '③ 성공을 상상하면 장애물을 부각해 결심이 늘 강해진다 → 글은 환상이 노력을 줄이고 행동 필요를 못 느끼게 한다고 함 // ① ② ④ ⑤ 일치 // ',
  3: '④ address(다루다) → gloss over(얼버무리다, 대충 넘기다): 목표를 낭만화하는 과정에서 어려움을 "외면"함 // ① disconnected ② different ③ less ⑤ induced 맞음 // ',
  4: '③ 시각화하면 즉각적인 행동이 촉진된다 → 글은 "행동할 필요가 생기지 않는다" // ① ② ④ ⑤ 일치 // ',
  5: '주어진 글(목표의 이상과 일상의 현실 단절) → (C) In fact 환상이 노력을 줄임 → (A) 목표를 낭만화하며 어려움을 외면 → (B) 한 연구의 요약(행동할 필요가 안 생김) // // In fact = 앞 말을 더 강하게',
  6: 'pushing out of mind(분사구문) + how different(간접의문문: how + 형용사 + 주어 + 동사) + our day-to-day will need to be + for us(의미상 주어) to make it happen // // [보기]의 to는 to be 하나뿐이라 make를 to make로 바꿔 써야 해요(형태 변형)',
  7: '환상이 노력을 줄이는 이유 = 이미 원하는 것을 이룬 듯한 "때 이른 성취감"(false and premature sense of accomplishment) // ① 어려움 의식 ③ 계획 재정비 ④ 결심 강화 ⑤ 간극 인식 → 반대 // ',
  8: '긍정적 환상이 목표 달성에 주는 부정적 영향 // ① 스트레스 해소 ② 일상 적응 ③ 습관 실패 이유(범위 넓음) ⑤ 구조적 어려움 → 핵심 아님 // ',
  9: '환상 속에서 미래를 미리 즐기고 현실을 돌아보지 않으니 "실제 행동하려는 충동이 생기지 않는다" // ② 일과 정착 ③ 동기 증폭 ④ 장애물 극복 ⑤ 진전으로 전환 → 반대 // ',
  10: '⑤ 성공을 상상하는 데 그치지 말고 필요한 현실적 변화·실천을 직시해야 // ① 작은 변화 우선 ② 기대가 동력 ③ 단순화 ④ 열망이 필수 → 글과 다름 // ',
  11: '① romanticize(실제보다 좋게 보다) ② intricacy(복잡하게 만드는 세부, 본문 intricacies) ③ seduce(매력으로 끌다) // // ',
  12: '어법: to do → to be(how different our day-to-day will need to be, different는 be의 보어) / 문맥: more → less(환상은 노력을 "덜" 하게 함) // // ',
  13: '① which → what ② making → to make(for us to make) ③ putting → to put(lead O to V) ④ integrated → integrating(of + 동명사) ⑤ summed up it → summed it up(대명사는 동사와 부사 사이) → 5개 // ⑥ desired(원하는, 수동 분사) 맞음 // 이어동사 + 대명사: sum it up',
  14: '① connected → disconnected ④ right → false ⑤ investigate → gloss over ⑥ forbids → seduces ⑦ inhibited → induced → 5개(선지 ④) // ② different ③ less 맞음 // 선지 번호와 개수가 다름 주의(④ = 5개)',
  15: '(A) 환상이 사람들을 때 이른 만족으로 "꾀어낸다(seduce)" (B) 간극을 "곰곰이 생각하는 것(reflecting)"을 막는다(discourage from + 동명사) // // ',
  16: 'In the process(그 과정에서) = 바로 앞 "목표를 낭만화하며 변화라는 생각에 빠진다"의 과정 → ④ // // ',
  17: '"행동할 필요가 생기지 않는다" = 상상한 성공이 구체적으로 노력할 절박함을 줄인다 // ② 목표 수정 ③ 즉각 변화 ④ 실천 루틴 ⑤ 결심 강화 → 반대 // ',
  18: 'gloss over(대충 넘기다) + 새 행동을 삶에 들이는 복잡함과 어려움 = 새 습관을 일상에 들이는 어려움을 간과한다 // ① 피함 ② 장기 효과 무시 ④ 과장 ⑤ 흥미 잃음 → 다름 // ',
 },
)
