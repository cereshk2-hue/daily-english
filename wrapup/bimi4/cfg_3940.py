# 39·40번 (39 도덕적으로 선한 사람: 의도와 결과 / 40 시각과 선입견, 카메라)
# (원본 머리글은 "2023년 9월"이지만 지문은 2025년 9월 고1 39·40번과 같음)
from build import B, V, arrow
_L = open('/home/claude/srcrepo/wrapup/bimi4/u39-40.txt', encoding='utf-8').read().replace('\xad', '-').split('\n')
assert _L[13].count('❸ confront') == 1 and _L[13].count('❶ connected') == 1 and _L[292].startswith('④ Functional Expectations')
C = dict(
 STEMS=[0, 7, 11, 14, 23, 27, 30, 33, 50, 58, 64, 67, 72, 80, 88, 110, 114, 118, 121, 129, 148, 152, 158, 161, 165, 168, 177, 182, 185, 188, 205, 213, 221, 224, 232, 240, 262, 266, 270, 278, 286, 294, 313, 316],
 END=318, AUTOW=True,
 LINEFIX={13: _L[13].replace('❸ confront', '❸ reinforce').replace('❶ connected', '❶ considered'),
          292: '④ Functional Expectations as the Key to Accurate Vision'},
 W={20: [B('', 'x')], 42: [B('', 'x')]},   # 영영 풀이 단어 쓰기(서술형)
 NOTE={3: '원본 ❸ "confront"(맞서다)는 "잘못된 인상에 맞서려고"로 읽혀 틀렸다고 하기 어렵고, ❶ "connected"도 뜻이 애매해서 ❸은 "reinforce"(강화하다), ❶은 "considered"로 바꿨어요. 정답 ③ 유지.',
       41: '원본 ④ "Functional Expectations and the Limits of Human Vision"도 제목으로 말이 돼서 ④를 "Functional Expectations as the Key to Accurate Vision"(정확한 시각의 열쇠)으로 바꿨어요. 정답 ③ 유지.'},
 EXP={
  1: '❺ being → is: 주어 A person(who ~ never does)의 동사 자리 // ❶ does(does morally bad ~와 병렬) ❷ are(not only A but also B → B인 intentions and motives에 수 일치) ❸ them(= others) ❹ that(동격절) 맞음 // ',
  2: '틀린 것 counts → count(It is ~ that 강조, consequences 복수) · what → that(it may be said that ~ 가주어-진주어) → 2개 // significantly(비교급 수식 부사) · to do(intend to) · because(+절) 맞음 // ',
  3: '❸ reinforce → avoid: 잘못된 인상을 "피하려고" 언급할 가치가 있음 // ❶ considered ❷ involuntarily(의도하지 않게) ❹ significant ❺ required 맞음 // ',
  4: '주어진 글(도덕적으로 선한 사람의 정의) → (B) Furthermore 행동뿐 아니라 의도와 동기도 중요, 의도 없이 해를 막은 사람은 선하지 않음 → (A) this kind of situation(그런 상황)은 슬랩스틱 영화에서나 → (C) But 실제 결과도 중요 // // this kind of situation = (B)의 우연히 해를 막은 상황',
  5: '"그러나 실제 결과도 중요하다" → 결과가 판단 기준이라는 잘못된 인상을 피하려 한다는 문장 뒤, 해를 막으려 하지만 못 막는 사람 예시 앞 ④ // // But: 의도 강조 → 결과도 중요로 전환',
  6: '③ 일상 행동과 동기를 다룬 영화가 재미있다는 내용은 도덕적 판단(의도와 결과)과 무관 // // ',
  9: '선한 의도만으로는 부족하고 칸트와 달리 "어떤 결과가 필요하다" → ② // ① 의도만 중요 ③ 결과 불필요 ④ 동기로만 판단 ⑤ 결과 고려 X → 모두 반대 // ',
  10: '바로 뒤 "해를 막으려 하지만 결코 못 막는 사람은 선하다고 여겨지지 않는다" → 실제 결과는 "중요하다" ④ // ① 재미있는 ② 피할 수 있는 ③ 우연한 ⑤ 무의미한 // ',
  13: '⑤ 의도하지 않은 좋은 결과로는 도덕적으로 선한 사람이 되지 않음 // ① 행동과 의도 모두 중요 ② 칸트와 달리 결과 필요 ③ 대부분보다 선행 많이 ④ 결과 없는 선의는 불충분 일치 // ',
  14: '③ 칸트와 달리 결과 필요 ⑤ 선한 행동 의도·악한 행동 회피 의도 → 일치 // ① 결과도 중요 ② 결과도 필요 ④ 의도 없이 해를 막은 사람은 선하지 않음 // ',
  15: '(A) 도덕적 가치의 "평가(evaluation)"에는 행동과 내적 목적이 모두 포함 (B) "구체적인(concrete)" 성과가 필요 → ① // ② abstract(추상적) ③ avoidance(회피) ④⑤ imagination(상상) // ',
  19: '도덕적으로 선한 사람은 의도와 결과 둘 다로 판단 → ④ // ② 의도만 ③⑤ 결과만 → 일부 ① 우연히 해를 막은 예시만 // ',
  23: '❹ creating → creates: 주어 The functional relationship(we have with objects)의 동사 자리 // ❶ that(주격 관계대명사) ❷ visualizing(when + 분사) ❸ seen(망치가 "보여진") ❺ them(= confusing details) 맞음 // ',
  24: '틀린 것 them → it(= a hammer) · confused → confusing(혼란을 "주는" 세부) · are appeared → appear(자동사는 수동태 X) → 3개 // is hidden(손잡이가 "가려지는") · to see(ability to) 맞음 // ',
  25: '❹ dissimilar → similar: 카메라도 눈처럼 형태와 색만 보므로 눈과 "비슷한" 렌즈 // ❶ unconscious ❷ hidden ❸ interfere with ❺ unrecognizable 맞음 // ',
  26: '주어진 글(시각은 선입견의 영향, 기능적 관계를 반영하는 위계) → (C) For example 망치 → (A) 기능적 관계가 카메라처럼 보는 능력을 방해, 카메라는 형태와 색만 봄 → (B) 사진은 혼란스러운 세부를 그대로 보여줌 // // ',
  27: '"카메라는 인간의 눈처럼 형태와 색만 본다" → "카메라처럼 보는 능력"이 처음 나온 뒤, It documents(It = the camera) 앞 ④ // // It = The camera',
  28: '⑤ 그림이 화가의 선입견을 드러낸다는 내용은 인간 시각과 카메라(사진) 비교라는 흐름과 무관 // // ',
  31: '사진이 놀라운 이유: 혼란스러운 세부를 해석하지 않고 기계적 무관심으로 그대로 보여줌 → ③ // ① 기능적 관계를 대체 X ② 낯선 것 제거 X ④ 마음의 눈과 같은 각도 X ⑤ 사진가의 선입견 X // ',
  32: '시각은 "현실에 대한 선입견"의 영향을 받음 → 뒤의 무의식적 위계, 기능적 관계 → ② // ① 사진의 평면성 ③ 카메라 렌즈 ④ 기능적 관계의 부재 ⑤ 눈이 기록한 형태와 색 // ',
  34: '② 카메라는 혼란스러운 세부를 해석하지 "않고" 그대로 보여줌 // ① 선입견 ③ 기능적 관계 ④ 기계적 무관심 ⑤ 사용 준비 각도 일치 // ',
  35: '② 사진은 혼란스러운 세부를 "그대로" 보여줌 ⑤ 시각은 무의식적 위계를 "세움" → 불일치 // ① 공평하게 기록 ③ 옆모습·사용 각도 ④ 평면성 일치 // ',
  36: '(A) 선입견과 실용적 필요가 중립적 관찰을 "왜곡함(distort)" (B) 사진은 "편견 없는(unbiased)" 무심함으로 기록 → ① // ② emotional(감정적) ③ promote/biased ④ support/common ⑤ support/subjective // ',
  39: '기능적 관계 = 사물을 쓰임(실용적 용도)에 따라 지각함 → ③ // ① 목적 없는 중립적 이미지 X ② 경험과 무관 X ④ 기계적 기록은 카메라 ⑤ 사진 X // ',
  40: '실용적 필요와 기대가 인간의 시각을 카메라와 다르게 만듦 → ⑤ // ① 카메라 개발 ② 사진의 세부 제거 X ③ 위에서 상상 X ④ 평면과 입체 X // ',
  41: '인간의 선입견 vs 중립적 관찰(카메라) → ③ // ① 카메라만 ② 평면성만 ④ 기대는 정확한 시각을 방해함 ⑤ 망치 예시만 // ',
 },
)
