# 41·42번 (장문: "May I help you?"는 최악의 네 단어) — 43~45번은 시험 범위 밖이라 END로 자름
from build import B, V, arrow
_L = open('/home/claude/srcrepo/wrapup/bimi4/u41-45.txt', encoding='utf-8').read().replace('\xad', '-').split('\n')
assert _L[37].startswith('다음 글에서 전체 흐름과 관계') and _L[68].strip() == '① allow' and _L[98].strip() == 'ignoring' and _L[123].startswith('다음 글을 읽고')
C = dict(
 STEMS=[7, 14, 18, 20, 24, 33, 37, 41, 44, 65, 73, 81, 89, 111, 115],
 END=123, AUTOW=True,
 KX={2: [16], 4: [22], 7: [39]},
 LINEFIX={37: '다음 글에서 전체 흐름과 어울리지 않는 문장은? (41-42번)', 68: '① warn', 98: 'welcoming'},
 NOTE={7: '원본은 "관계 없는 문장"이었지만 ⑤는 글과 관련된 내용에서 뜻만 거꾸로 바뀐 문장이라 발문을 "어울리지 않는 문장"으로 바꿨어요. 정답 ⑤ 유지.',
       10: '원본 ① "allow"도 "말하게 허락하지 않는다"로 억지로 읽힐 수 있어 ①을 "warn"으로 바꿨어요. 정답 ② 유지.',
       13: '원본 ① "available – ignoring"(손님을 무시하지 않고)도 요약문으로 말이 돼서 ①의 (B)를 "welcoming"으로 바꿨어요. 정답 ③ 유지.'},
 EXP={
  1: '"May I help you?"는 손님이 말하게 하지 못하고 방어적으로 만들어 판매를 막음 → ③ // ① 항상 써야 X ② 대본 암기 X ④ 손님이 대화를 싫어함 X ⑤ 명함은 일부 내용 // ',
  2: '틀린 것 ❸ what → that(선행사 a rote approach, 주격 관계대명사) · ❹ implying → implies(주어 The very meaning의 동사) · ❺ which → where(뒤 절이 완전, 선행사 situations) → 3개 // ❶ stops(선행사 a negative response) ❷ are(주어 Examples 복수) 맞음 // ',
  4: '❹ isolation → assistance: 실제로 "도움"이 필요해도 "No, thank you"라고 함 // ❶ encourage ❷ negative ❸ defense ❺ accessible 맞음 // ',
  5: '주어진 글(최악의 네 단어) → (C) The four words 부정적 반응, 더 나은 질문 → (A) This line 진부한 접근, 방어적이 됨 → (B) 압박을 느끼면 판매 X, 편안한 환경 // // This line = "May I help you?"',
  6: '"이것은 손님을 방어적으로 만든다" → 손님이 곤경에 처해 구조가 필요하다는 뜻을 담는다는 문장 뒤, 손님의 속마음(도움 필요 없어!) 앞 ① // // This = 질문이 담은 "도움이 필요하다"는 뜻',
  7: '⑤ 손님을 "압박감을 느끼게" 해야 한다는 것은 편안한 환경을 만들라는 흐름과 반대(원문: 명함을 주고) // // ',
  9: '(A) 손님이 "압박감을 느끼면(pressured)" 판매 X (B) 편안한 환경을 "조성해야(promote)" 함 → ① // ② relaxed/prevent ③ annoyed/destroy ④ welcomed/discourage ⑤ defensive/abandon → (B)가 모두 반대 // ',
  10: '"May I help you?"는 손님이 말하도록 "장려하지(encourage)" 못함 → ② // ① 경고하다 ③ 강요하다 ④ 요구하다 ⑤ 상기시키다 // ',
  11: '① 손님은 도움이 필요해도 "No, thank you"라고 부정적으로 반응 // ② 존중받는 느낌 X ③ 고집해서 도우라 X ④ 숙련된 직원은 안 씀 ⑤ 불편함을 자주 느낌 // ',
  12: '① 적절하지 않은 질문 ④ 명함(연락처)을 주라고 함 → 불일치 // ② 구조가 필요하다는 뜻 ③ 더 나은 질문 ⑤ 압박 없는 환경 일치 // ',
  13: '(A) 연락이 닿을 수 있게 "곁에 있고(accessible)" (B) 손님을 "압박하지(pressuring)" 않고 → ③ // ① welcoming(환영하지 않고) ② aggressive ④ distant ⑤ invisible // ',
 },
)
