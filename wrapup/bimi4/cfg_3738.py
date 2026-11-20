# 37·38번 (37 자전거와 마찰력 / 38 비선형 편집 시스템)
from build import B, V, arrow
_L = open('/home/claude/srcrepo/wrapup/bimi4/u37-38.txt', encoding='utf-8').read().replace('\xad', '-').split('\n')
assert _L[0].startswith('밑줄 친 부분 중 어법상')
C = dict(
 STEMS=[0, 15, 22, 27, 34, 41, 52, 63, 74, 92, 102, 107, 119, 124, 129, 134, 147, 158, 169, 180, 197, 207, 219],
 END=226, AUTOW=True,
 W={10: [B('', 'x')], 21: [B('', 'x')]},   # 요약문 <보기> 쓰기(서술형) — 정답 줄이 ①로 시작해 객관식으로 읽힘
 LINEFIX={0: '밑줄 친 ⓐ~ⓔ를 어법상 바르게 고친 것으로 옳지 \ue000않은\ue001 것은? (37번)'},
 NOTE={1: '원본 발문은 "밑줄 친 부분 중 어법상 틀린 것"이었지만 ⓐ~ⓔ가 모두 틀린 표현이고 선택지가 "고친 것"이라 발문을 "바르게 고친 것으로 옳지 않은 것"으로 바꿨어요. 정답 ④ 유지.'},
 EXP={
  1: 'ⓓ pushes → pushing: air resistance를 설명하는 분사구문(~하면서 밀어내는) // ① make → making(분사구문) ② it → which(콤마 두 절 연결) ③ and which → and they(접속사+대명사) ⑤ that → what(see의 목적어, could be generating의 주어) 모두 바르게 고침 // 접속사 없이 두 절 X',
  2: '틀린 것 ⓒ exerted → exerting(브레이크가 힘을 "가하는", 능동 진행) · ⓖ slows → slow(선행사 forces 복수) · ⓗ which you can feel it → it 삭제 · ⓙ generated → generating(마찰을 "발생시키는") → 4개 // ⓐ to move ⓑ making ⓓ called ⓔ tends ⓕ opposite ⓘ pushing 맞음 // ',
  3: '❹ assistance → resistance: 뒤로 미는 "공기 저항" // ❶ affect ❷ decelerate ❸ off(브레이크를 안 잡아도) ❺ causing 맞음 // assistance 도움 ↔ resistance 저항',
  4: '"이것이 마찰력이다" → 브레이크가 바퀴 테두리를 잡고 문지르며 힘을 가한다는 문장 바로 뒤 ② // // This = 브레이크가 가하는 힘',
  5: '"브레이크를 안 잡아도 다른 마찰력이 있다" → 바로 뒤 One of these(그중 하나는 축의 마찰), Another(공기 저항)가 이어지는 ③ // // these = other friction forces',
  6: '페달을 멈추면 서서히, 브레이크를 잡으면 갑자기 느려지는 것 모두 마찰력 때문 → ① // ② 브레이크만이 유일 X ③ 공기 저항 미미 X ④ 수레와 자전거 구조 같음 X ⑤ 중력 X // ',
  7: '마찰력이 일상의 물체에서 움직임을 늦추도록 작용하는 방식 → ② // ① 도로 손상 X ③ 페달 없이 못 감은 일부 ④ 공기 저항 증가 X ⑤ 브레이크 역사 X // ',
  8: '⑤ 마찰력은 움직임과 "반대" 방향으로 작용해 속도를 줄임 // ① 테두리를 잡아 힘 ② 수레는 축 마찰 ③ 브레이크 없이도 축 마찰·공기 저항 ④ 뒤로 작용 일치 // ',
  9: '틀린 것 ②(공기 저항은 반대 방향) ⑤(브레이크 없어도 서서히 느려짐) ⑨(페달을 밟아도 마찰은 계속) → 3개 // 나머지 일치 // ',
  14: '⑤ add → be added: 새 정보가 "추가되어야" 함(수동) // ① it(= any video shot or scene) ② makes it easy(가목적어) ③ rewinding(fast forwarding과 병렬) ④ adjusts(주어 the computer) 맞음 // need to be p.p.',
  15: '❹ partial → whole: 실수하면 "전체"를 다시 타이핑해야 함 // ❶ enable ❷ simple ❸ adjusts ❺ keystrokes 맞음 // ',
  16: '주어진 글(비선형 편집, 임의 접근, 특수 효과) → (B) Another highlight(또 다른 장점) → (C) 장면 추가·삭제, 선형 편집은 타자기 같음 → (A) on the other hand, 비선형은 워드 프로그램 같음 // // on the other hand → 앞에 선형 편집 설명',
  17: '임의 접근·자유로운 수정·쉬운 오류 수정으로 비선형 편집이 영상 편집을 바꿈 → ⑤ // ① 선형 편집 우세 X ② 기능 비슷 X ③ 특수 효과 실패 X ④ 관련 없음 X // ',
  18: '편집 방식의 변화와 비선형 시스템의 우수성 → ③ // ① 공통점 X ② 단점 X ④ 워드 프로그램 소멸 X ⑤ 빨리 감기 기능 지속 X // ',
  19: '④ 컴퓨터가 프로그램 길이를 "자동으로" 조정함 // ① 컴퓨터 기반, 임의 접근 ② 선형은 전체 다시 ③ 와이프·디졸브 ⑤ 워드 프로그램 비유 일치 // ',
  20: '틀린 것 ②(특수 효과 만들 수 있음) ④(선형은 타자기, 비선형은 워드 프로그램) ⑧(역사적 발전은 언급 없음) → 3개 // 나머지 일치 // ',
 },
)
