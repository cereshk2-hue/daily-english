# 41·42번 (알고리즘과 선택 설계 — 인간 주체성 지키기) — 파일 41-45에서 41·42번만 (43~45번은 범위 밖)
from build import B, V, arrow
_L = open('/home/claude/srcrepo/wrapup/bimi3/u41-45.txt', encoding='utf-8').read().replace('\xad', '-').split('\n')
C = dict(
 STEMS=[6, 13, 16, 19, 22, 31, 35, 38, 41, 49, 57, 65, 73, 95, 99],
 END=105,
 DEFSRC=lambda n: '41·42',
 LINEFIX={34: _L[34].replace('( ① ) (By curating', '( ① ) By curating').replace('paths.  ② )', 'paths. ( ② )').replace('T( ③ ) he question', '( ③ ) The question')},
 DROP={3: [17], 8: [39], 14: [96], 15: [100, 101]},
 W={
  3: [B('', ['curating'])],
  8: [B('[a]', V('how the design of the environment in which choices are made can significantly influence the decisions people make.', '[a] how the design of the environment in which choices are made can significantly influence the decisions people make.'), True)],
  14: [B('1', ['Algorithms']), B('2', ['curating']), B('3', ['nudging']), B('4', ['critical'])],
  15: [B('(A)', 'how the design of the environment in which choices are made can significantly influence the decisions people make', True),
       B('(B)', 'cultivating a healthy skepticism towards the seemingly objective outputs of algorithms', True)],
 },
 NOTE={6: '원본 지문의 ( ② ) · ( ③ ) 괄호 위치가 깨져 있어서 바로잡았어요. 정답 ④ 유지.'},
 EXP={
  1: '알고리즘이 만든 선택 환경에 비판적으로 참여해 인간의 주체성을 지키기 // ① 알고리즘이 스스로 결정 ② 인간 개입 최소화 ③ 추천을 따르기 ④ 넛지 완전 제거 → 반대 // ',
  2: '틀린 것 ❶ is popularized → popularized(“choice architecture”를 꾸미는 분사, 동사는 highlights) → 1개 // ❷ in which ❸ aligned(be aligned with) ❹ challenging(seeking과 병렬) ❺ necessarily 맞음 // ',
  3: 'By curating(동명사, 큐레이션함으로써) what we see ~ → 알고리즘이 특정 방향으로 슬쩍 이끔 // // ',
  4: '❸ passive → critical: 우리가 쓰는 기술과 "비판적인" 관계를 유지하려는 의식적 노력이 필요 // ❶ curating ❷ nudge ❹ challenging ❺ cultivating 맞음 // ',
  5: '주어진 글(선택 설계: 환경이 결정에 영향) → (C) 알고리즘은 디지털 환경의 설계자, 넛지 → (B) 넛지는 유익할 수도 조작이 될 수도 → (A) 그렇다면 주체성을 어떻게 지킬까, 비판적 참여 // // ',
  6: '"기술과 비판적 관계를 유지하려는 의식적 노력이 필요하다" = 주체성을 어떻게 지킬까 질문의 답, 뒤 It means(그것은 ~을 뜻한다)로 이어짐 → ④ // // ',
  7: '⑤ 알고리즘 결과를 "맹목적으로 받아들이기" → 건전한 회의(healthy skepticism)를 기르라는 흐름과 반대 // // ',
  8: '[a] the environment which choices are made → the environment in which choices are made(뒤가 완전한 절 → 전치사 + 관계대명사) // // ',
  9: '① 알고리즘의 영향을 비판적으로 살피고 의도적으로 선택해 자율성을 지켜야 // ② 추천에 의존 ③ 넛지 모두 없애기 ④ 알고리즘에 맡기기 ⑤ 개인 판단 불필요 → 반대 // ',
  10: '알고리즘의 겉보기에 객관적인 결과에 대한 건전한 "회의(skepticism)" // ① confidence ② compliance ④ dependence ⑤ acceptance → 반대 // ',
  11: '① 선택이 일어나는 환경이 결정에 큰 영향 // ② 정보만 보여 줌 → 특정 방향으로 이끔 ③ 늘 조작 → 유익할 수도 ④ 따르기 → 비판적으로 ⑤ 과거 데이터가 믿을 만한 청사진 → 아님 // ',
  12: '② 알고리즘은 사용자를 특정 선택지로 이끌 수 "없다" → 이끈다(nudge) // ① ③ ④ ⑤ 일치 // ',
  13: '(A) 행동을 슬쩍 "이끌다(steer)" (B) 기계의 결과를 "검토하다(examine)" // ① avoid ⑤ overlook → (B) 반대 ② ignore ④ restrain → (A) 다름 // ',
  14: 'Algorithms · curating · nudging · critical // // ',
  15: '(A) how the design of the environment in which choices are made(be → are) can significantly(significant → significantly) influence the decisions people make (B) cultivating(동명사) a healthy skepticism towards ~ outputs of algorithms // // ',
 },
)
