# 29·30번 (29 가젤이 가축화되지 않은 이유 / 30 결핍은 나눔을, 풍요는 이기심을)
from build import B, V, arrow
_L = open('/home/claude/srcrepo/wrapup/bimi4/u29-30.txt', encoding='utf-8').read().replace('\xad', '-').split('\n')
assert _L[23].count('tame') == 1 and _L[150].startswith('다음 글에서 전체 흐름과 관계')
C = dict(
 STEMS=[7, 14, 18, 20, 24, 33, 37, 40, 43, 64, 72, 80, 88, 110, 114, 120, 127, 131, 133, 137, 146, 150, 154, 157, 178, 181, 189, 197, 219, 223],
 END=227, AUTOW=True,
 LINEFIX={23: _L[23].replace('tame', 'abandon'), 150: '다음 글에서 전체 흐름과 어울리지 않는 문장은? (30번)'},
 KX={2: [16], 4: [22], 17: [129], 19: [135], 22: [152]},
 NOTE={4: '원본 ❺ "tame"(길들이다)은 domesticate와 뜻이 같아 문맥상 틀리지 않았어요. ❺를 "abandon"(버리다)으로 바꿨어요. 정답 ⑤ 유지.',
       22: '원본은 "관계 없는 문장"이었지만 ⑤는 주제와 관련은 있고 뜻(connection)이 거꾸로 바뀐 문장이라 발문을 "어울리지 않는 문장"으로 바꿨어요. 정답 ⑤ 유지.'},
 EXP={
  1: '겁 많고 빠른 대형 초식동물(가젤)은 갇히면 공황에 빠져 가축화에 맞지 않음 → ③ // ① 식습관 ② 가젤이 가장 쉬움 ④ 모두 가축화 ⑤ 혼자 사는 것 선호 → 글과 다름 // 주제 = 첫 문장 + 가젤 예시',
  2: '틀린 것 ❶ standing → stand(seek, don’t run과 나란한 동사) ❷ them → themselves(주어 they 자신) ❹ having → had(관계절의 동사) → 3개 // ❸ which(계속적 용법, 주격) ❺ has been tamed(수동) 맞음 // 병렬 · 재귀대명사 · 관계절 동사',
  4: '❺ abandon(버리다) → domesticate: 가젤만큼 "가축화할" 기회가 많았던 종은 없었지만 길들여진 적은 없음 // ❶ threatened ❷ run ❸ enclosure(울타리) ❹ escape 맞음 // But no gazelle species has been tamed와 대조',
  5: '주어진 글(겁 많고 빠른 종) → (C) 다른 종은 느림, 겁 많은 종은 가두기 어려움 → (B) 울타리에 넣으면 공황, 가젤이 그 예 → (A) 가젤만큼 기회가 많은 종이 없었지만 길들여지지 않음 // // Other species / That’s true of gazelles 연결 신호',
  6: '"그것은 가젤에게도 사실이다" → 울타리에서 공황에 빠져 죽는다는 문장 바로 뒤 ③, 다음 문장 There is no mammal species ~ than gazelles로 이어짐 // // That’s true = 바로 앞 내용',
  7: '③ 가젤의 서식지(초원·사바나) 설명은 가축화가 어려운 이유라는 흐름과 무관 // // 소재(가젤)가 같아도 주제가 다르면 무관',
  9: '(A) 겁 많은(nervous) 종은 (B) 가둬 두기(captivity) 어렵다 // ② calm ③ slow → 반대 ④ aggressive · enclosure ⑤ wild · habitat → 문맥과 다름 // keep in captivity = 가둬 기르다',
  10: '최초 정착민들이 가젤만큼 "가축화할(domesticate)" 기회가 많았던 종은 없다 → But 길들여진 적 없음과 대조 // ① hunt ② elude(피하다) ③ observe ⑤ conserve → But 뒤 내용과 이어지지 않음 // ',
  11: '② 겁 많은 초식동물은 갇히면 공황에 빠져 스스로를 다치게 함 // ① 차분하고 느림 ❌ ③ 성공적으로 길들임 ❌ ④ 항상 즉시 도망 ❌(어떤 종은 버팀) ⑤ 다루기 쉽고 안전 ❌ // ',
  12: '③ 모든 대형 초식동물이 가두기 쉽다 → 겁 많은 종은 가두기 어려움 // ① ② ④ ⑤ 일치 // ',
  13: '(A) 가젤을 가축화할(domesticate) 기회가 많았지만 길들여지지 않음 (B) 위협을 느끼면(threatened) 격렬하게 반응 // ① hunt ③ observe ④ protect ⑤ capture → 본문의 opportunity to domesticate와 다름 // ',
  16: '③ 결핍은 나눔을, 풍요는 덜 나누게(울타리·보안) 만듦 → ② // ① 유목 생활의 어려움 ③ 체력 ④ 보안 시스템 ⑤ 이주의 역사 → 일부만 다룸 · 무관 // ',
  17: '틀린 것 ❷ which → what(share의 목적어, 선행사 없음) ❺ starting → starts(주어 Our desire의 동사) → 2개 // ❶ when(관계부사) ❸ depends(주어 survival 단수) ❹ sophisticated(the 비교급 구문의 형용사) 맞음 // ',
  19: '❺ increased → reduced: "평범한 사람들"과의 접촉이 "줄어들면서" 현실에 눈멀게 됨 // ❶ share ❷ hospitality ❸ more ❹ less 맞음 // ',
  20: '주어진 글(풍요로울 때 나눔이 복잡해짐) → (C) 가진 게 적을 때 더 나눔, 유목 부족의 환대 → (A) 착해서가 아니라 생존이 나눔에 달림, 아이러니하게 많이 가질수록 덜 나눔 → (B) 더 원하고 접촉이 줄며 현실에 눈멂 // // ',
  21: '"착해서만이 아니라 생존이 나눔에 달려 있어서" → 음식과 환대를 베푼다는 문장 바로 뒤 ④ // // It’s not just because ~ = 앞 문장의 이유',
  22: '⑤ 접촉이 줄면 현실과의 "단절(disconnection)"이 생겨야 하는데 "connection"으로 바뀌어 흐름과 반대 // ① ② ③ ④ 원문 그대로 // ',
  24: '(A) 음식과 환대(hospitality)를 베풂 (B) 현실에 대한 단절(disconnection)이나 눈멂 // ③ connection ⑤ unity → (B) 반대 ④ hostility(적대감) → (A) 반대 ① distance → 원문과 다름 // ',
  26: '① 가진 것이 적을수록 더 기꺼이 나눔 // ② 거의 나누지 않음 ❌ ③ 많이 가질수록 더 나눔 ❌ ④ 나눔이 생존에 불필요 ❌ ⑤ 부유해질수록 접촉 증가 ❌ // ',
  27: '⑤ 부유하고 안전할 때 더 기꺼이 나눔 → 반대(많이 가질수록 덜 나눔) // ① ② ③ ④ 일치 // ',
  28: '(A) 결핍(scarcity)의 시기에 나누도록 진화 (B) 위협이 적을(minimal) 때 복잡해짐 // ① abundance ③ plenty → (A) 반대 ③ ④ ⑤ (B) dangerous · overwhelming · severe → 반대 // ',
 },
)
