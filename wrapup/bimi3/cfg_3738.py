# 37·38번 (37 언어는 문화의 표출 / 38 밀도와 혼잡감) — 객관식만 (원본 뒤쪽 '서답형·전체적인 복습' 부분은 OMR에서 뺌)
from build import B, V, arrow
C = dict(
 AUTOEXP=True,
 STEMS=[0, 15, 24, 33, 42, 51, 65, 79, 88, 92, 96, 105, 114, 131, 135, 146, 151, 175, 182, 190, 194, 207,
        339, 349, 358, 367, 376, 385, 399, 413, 417, 421, 425, 434, 448, 464, 468, 478, 483, 506, 513, 521, 524, 537],
 END=550,
 LINEFIX={k: 'edu-lab.kr' for k in range(220, 339)},
 REPL=[('are(주의)', 'are')],
 FIXT=[('(t19)', '')],
 ANS={8: '②', 10: '⑤', 12: '①②⑤', 13: '③', 23: '②'},
 KX={8: [81, 82, 83, 84, 85, 86], 12: [117]},
 DROP={1: [1], 12: [107], 13: [116, 117], 23: [341, 342]},
 NOTE={
  8: '원본 정답은 ❸이지만 원본 해설도 ❸(them → themselves)은 틀리고 ❷ linked만 올바르다고 설명해요. "옳은 것"을 고르는 문제라 정답을 ②로 고쳤어요.',
  10: '원본 정답은 ④인데 원본 해설은 independent of → relative to(❺)를 고쳐야 한다고 해요. ❹ counterpart는 맞는 말이라 정답을 ⑤로 고쳤어요.',
  12: '원본은 이 문제와 다음 문제의 정답·해설이 뒤바뀌어 있었어요(이 문제 원본 정답 ②). 빈칸(자신을 가리키는 말이 무엇에 따라 달라지는지)에 맞는 ①②⑤로 고쳤어요.',
  13: '원본 정답 "①, ②, ⑤"와 해설은 앞 문제 것이었어요. 빈칸(직접적 스타일의 단어 예)에 맞지 않는 것은 [C] ambiguous phrasing · [E] tentative statements · [F] vague terms → 정답 ③으로 고쳤어요.',
  23: '원본 정답은 ④(밀도의 물리적 측정을 주관적 감정보다 우선)인데, 붙어 있는 해설과도 글의 주장과도 맞지 않아요. 밀도와 혼잡감을 구분하고 긍정적 공간을 설계하자는 ②로 고쳤어요.',
 },
 EXP={
  42: '[c] degrades → enhances: 기대하던 콘서트라면 혼잡감이 즐거움을 "높임" // [a] impartial(= neutral) [b] escalate [d] highlight [e] relieve 맞음 // ',
  8: '옳은 것은 ❷ linked(단어가 직접적 스타일과 "연관된", 과거분사)뿐 // ❶ enables → enable(선행사 patterns and styles 복수) ❸ them → themselves ❹ which → that(동격, 뒤가 완전한 절) ❺ referring → refer(be used to + 원형) // ',
  10: '❺ independent of → relative to: 청자와 "비교한" 사회적 속성에 따라 자칭어가 달라짐 // ❶ straightforward ❷ ambiguous ❸ exclusive ❹ counterpart 맞음 // ',
  12: '자신을 가리키는 말은 청자와의 관계·상황에 따라 달라짐 → ①·②(같은 뜻) ⑤(원문) // ③ 늘 고정 ④ 모든 상대에게 똑같이 → 반대 // ',
  13: '직접적 스타일의 단어 예(absolutely, certainly) = [A] categorical words [B] definitive expressions [D] assertive vocabulary → 들어갈 수 없는 것 [C] [E] [F](모호·잠정적 표현) // // ',
  23: '② 밀도와 혼잡감을 구분하고 긍정적 경험을 주는 공간을 설계해야(공원·보행 구역) // ① 전면 재건축 ③ 밀도 제한 ④ 물리적 측정 우선 ⑤ 보행 구역 없애기 → 글과 다름 // ',
 },
)
