# 33·34번 (33 불확실성의 중요성은 상대적 / 34 재생 에너지 전환의 딜레마)
from build import B, V, arrow
_L = open('/home/claude/srcrepo/wrapup/bimi4/u33-34.txt', encoding='utf-8').read().replace('\xad', '-').split('\n')
assert '것은? 것은?' in _L[23]
C = dict(
 STEMS=[1, 10, 23, 32, 39, 53, 63, 69, 74, 86, 91, 97, 102, 106, 119, 130, 141, 150, 159, 163, 177, 183, 190, 197, 220, 227, 233, 241],
 END=251, AUTOW=True,
 LINEFIX={23: _L[23].replace('것은? 것은?', '것은?'), 25: _L[25].replace('\ue000what I’m intending to do with it\ue001', '______________________'),
          132: _L[132].replace('\ue000cannot happen without fossil fuels\ue001', '______________________')},   # 빈칸 문제인데 원본은 정답 부분에 밑줄만 → 빈칸으로
 EXP={
  1: '틀린 이해 ② 태양-지구 거리가 거의 일정해 확실하다(글은 다음 자리가 불확실하다고 함) ③ 태양-지구 거리가 뉴욕-시카고 거리보다 정확하다(불확실성이 뉴욕-시카고 거리보다 크다고 함) // ① 불확실성의 중요성이 상대적이라 이해하기 어려움 ④ 정확한지는 무엇에 쓰느냐에 달림 ⑤ 같은 뜻 → 바른 이해 // ',
  3: '숫자가 "정확한지"는 내가 그것으로 무엇을 하려는지(what I’m intending to do with it)에 달림 → 바로 뒤 일출 시각 · 위성 예시와 이어짐 // ① 자료 모으는 때 ② 계산 방법 ③ 자릿수 ⑤ 측정 장소 → 예시와 이어지지 않음 // ',
  5: '주어진 글(불확실성의 중요성은 상대적) → (C) 예: 태양-지구 거리, 상대적으로 정확해 보임 → (B) 하지만 다음 자리가 불확실하면 오차가 뉴욕-시카고보다 큼, 정확한지는 쓰임에 달림 → (A) 일출 시각이면 충분, 위성이면 더 정확해야 // // Take, for example / However 신호',
  6: 'ⓑ relative(상대적인) ↔ definite(확정된) → 바꿔 쓸 수 없음 // ⓐ appreciate = recognize(인식하다) ⓒ precise = accurate ⓓ quoted = cited(인용된) ⓔ intending = planning // ',
  7: '"정확한지는 쓰임에 달려 있다" → 오차가 뉴욕-시카고 거리보다 크다는 문장 뒤, 일출 시각 · 위성 예시 앞 ④ // // therefore = 앞 내용의 결론',
  8: '③ mean → means: 동명사구 주어(using six significant digits)는 단수 // ① is(주어 One) ② measured(측정된, 수동) ④ is(Whether절 안 주어 number) ⑤ depends(Whether절 주어 = 단수) 맞음 // ',
  10: '③ smaller → larger: 다음 자리가 불확실하면 오차가 뉴욕-시카고 거리보다 "크다"(그래서 정확도는 쓰임에 따라 다름) // ① difficult ② precise ④ fine ⑤ more 맞음 // ',
  14: '숫자의 정확성(불확실성)의 의미는 무엇에 쓰느냐에 따라 상대적 → ② // ① 숫자의 매력 ③ 계산의 정확성 중요 ④ 천문 관측의 어려움 ⑤ 상대성 이론 → 글과 다름 // ',
  15: '재생 에너지 기반을 만들려면 화석 연료가 필요해 오히려 배출 감축을 해친다는 딜레마 → ⑤ // ① 화석 연료 과소평가 ② 태양-풍력 비교 ③ 친환경 에너지 종류 ④ 재생 에너지의 환경 보호 능력 → 글과 다름 // ',
  16: '이 전환은 화석 연료 없이는 일어날 수 없다 → 바로 뒤 For instance(콘크리트 · 강철 · 광물 채굴에 화석 연료) // ①③ 화석 연료 사용 감소 → 반대 ④ ⑤ 무관 // ',
  17: '건설 비용이 거의 고려되지 않고 배출 감축 노력을 해친다고 지적 → critical(비판적인) // ① neutral ③ favorable ④ positive ⑤ hopeful → 글의 지적과 맞지 않음 // ',
  19: '② with → without: 이 전환은 화석 연료 "없이는" 일어날 수 없다(뒤 예시가 모두 화석 연료 사용) // ① stop ③ scarce ④ push ⑤ undermining 맞음 // ',
  22: '③ require → requires: 주어 Production(단수) // ① one of the + 최상급 + 복수 명사 ② is(선행사 energy) ④ the 비교급, the 비교급 ⑤ which(계속적 용법, 선행사 proposals) 맞음 // ',
  24: '(A) 앞 문장의 구체적 예 → For instance (B) 앞 내용의 결과 → Thus // ① ② However · Instead · Yet → 역접 아님 ④ Similarly ⑤ However → 흐름과 다름 // ',
  26: '"이 전환은 화석 연료 없이 일어날 수 없다" → 새로 만들 기반 시설 나열 뒤, For instance(화석 연료가 필요한 예) 앞 ② // // This transformation = 앞의 대규모 변화',
  28: '건설 비용이 전환 계획에서 거의 계산되지 않음 = ① 건설 과정에 화석 연료가 많이 필요 ② 건설 비용을 계산하지 않음 ③ 고려하지 못한 화석 연료 사용 ⑤ 화석 연료가 필요한 역설 // ④ 재생 에너지가 유일한 해결책 → 밑줄의 뜻과 무관 // ',
 },
)
