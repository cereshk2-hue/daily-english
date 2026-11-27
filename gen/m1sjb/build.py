# 11/27 심학중1 족보 OMR 답만 입력 (문제는 종이 족보) → m1-chunjae-so-L6 /* M1SJB-TESTS */
# kind 'exam' → '실전기출' 탭, retry 1 (틀린 번호만 → 한 번 더 → 해설, 점수는 첫 제출)
# 정답: 족보 [정답](그림, 4과 7~9쪽·5과 8~10쪽·6과 7~10쪽) + 60문항 모두 직접 풀어 대조(일치). 6과 19번 해설 본문 '③'은 오타(정답 표시 ② 맞음)
import json, re
path = '/home/claude/proj/data/m1-chunjae-so-L6.js'
C = '①②③④⑤'
SETS = [
 {'id': 'm1sjb-4a', 'title': '족보 OMR · 4과 My Delicious Summer Trip (01) 20문항', 'short': '족보 4과 (01)', 'src': '4.My Delicious Summer Trip(01) 최다오답 공략(교육지대)',
  'key': [
   (2, '동명사', 'enjoy + -ing, 앞에서 말한 그 정원 → the garden'),
   (2, '전치사·접속사', 'ⓐ During(방학 동안) ⓑ After(둘러본 뒤에)'),
   (2, '어법', '(나) fastly → fast (다) are → was (바) liveed → lived'),
   (3, '동명사·현재분사', '③ is drawing은 현재진행형(현재분사), 나머지는 동명사'),
   (5, '추론', '돔베고기: 도마(그릇)와 소스까지 지역 특징으로 느꼈을 것 — 나머지는 근거 없음'),
   (2, '문장 삽입', '피곤해졌다 → However, 돔베고기로 힘을 되찾음 → (B)'),
   (4, '과거 시제', "④ didn't + 동사원형 finish — 나머지: know, were, wrote, go"),
   (4, '과거 시제', '(가) ate·went / (나) eat·go → ⓑ, ⓓ가 다름'),
   (2, '내용 이해', '돔베고기 조리법은 나오지 않음'),
   (5, '영영풀이', 'ⓔ dish는 요리(음식) — 얕고 평평한 그릇 풀이 ✘'),
   (4, '영작', '④ I heard about the history of this food. ✓'),
   (4, '내용 이해', '담양에서 먹은 것 → 대통밥과 떡갈비'),
   (3, '내용 일치', '③ ✘ — 빨리 먹어서가 아니라 쉽게 상하지 않아서'),
   (4, '추론', '옛날 어부들이 충무김밥을 먹기 시작함 → 통영에 어업 인구가 있었음'),
   (1, '어휘·어법', 'ⓐ its(소유격) ⓑ on the side ⓒ in two ways'),
   (5, '과거 시제', '⑤ now → James reads a book now.'),
   (4, '어법', 'ⓒ like → liked, ⓔ It was exciting, ⓖ were → was, ⓗ want to go'),
   (2, '내용 이해', '미나(7월 30일)·수진(낙지 ✘ 오징어)이 틀림 → 2명'),
   (1, '추론', '대통밥의 대나무 향은 대나무 그릇에서 나옴'),
   (3, '요약', 'took(케이블카를 탔다) · past(옛날) · fresh(상하지 않음)')]},
 {'id': 'm1sjb-5a', 'title': '족보 OMR · 5과 Share Your Joys and Worries (01) 20문항', 'short': '족보 5과 (01)', 'src': '5.Share Your Joys and Worries(01) 최다오답 공략(교육지대)',
  'key': [
   (5, '지칭', 'ⓔ It was growing season의 It은 비인칭(시기) — summer를 가리키지 않음'),
   (5, 'be동사', "ⓔ be at my grandma's = ~에 있다(1형식), 나머지는 ~이다(2형식)"),
   ([2, 5], '내용 일치', '② El은 기쁘지 않고 더 작게 느낌 ⑤ El은 꽃 없는 마지막 작은 화분을 가져감 (두 개 고르기)'),
   (2, '비교급·최상급', 'hotter / the hottest / the most comfortable'),
   (5, '심경', '꽃 없는 작은 식물이 자기처럼 작다고 느껴 슬픔'),
   (1, '어휘', '(A) 식물(명사) (B) 심다(동사) → ①'),
   (3, '배열', 'It was the most exciting soccer match ~ → 다섯 번째 단어 exciting'),
   (2, '영영풀이', 'ⓑ reach = 손이 닿다 — 장소에 도착하다 ✘'),
   (3, '비교', '오른쪽으로 달림(사슴 1등) → Ben·Jo·Tom 맞음 → 3명'),
   (5, '추론', "Jo가 '우리처럼 좋은 친구가 될 거야' → 함께 심게 되어 기뻐서 웃음"),
   (5, '내용 이해', 'El이 마지막 화분을 가져갈 때 Jo의 기분은 나오지 않음'),
   (5, '비교급·최상급', 'bigger than / the biggest in ~'),
   (5, '내용 흐름', '자라는 계절 → 두 꽃이 잘 자라고 El도 키가 큼'),
   (4, '비교급', '옳은 것 ⓒⓓⓖ — longer, larger, more expensive, more interesting'),
   ([4, 5], '어법·어휘', 'ⓓ However ✓ ⓔ 상대적으로 작게 느낌 ✓ (두 개 고르기)'),
   (5, '도표', 'Jina 65kg > Kate 60kg → ⑤ ✘'),
   (4, '추론', '④ ✘ — 결국 과꽃에 꽃이 핌'),
   (3, '추론', "'우리처럼 좋은 친구가 될 거야' → 두 식물도 잘 지낼 거라 생각함"),
   ([1, 4], '내용 일치', '① El이 즐거워졌다 ✘ ④ 과꽃이 여전히 초록 ✘ (두 개 고르기)'),
   (2, '감상', 'Jisoo ✘ — Jo는 키가 작아진 게 아니라 커졌음')]},
 {'id': 'm1sjb-6a', 'title': '족보 OMR · 6과 Heroes in Nature (01) 20문항', 'short': '족보 6과 (01)', 'src': '6.Heroes in Nature(01) 최다오답 공략(교육지대)',
  'key': [
   (2, '동명사', 'love diving and spending ~ (and로 같은 형태)'),
   (2, '어법·문맥', '틀린 것 ⓐ work(→ to work/working) ⓑ ever(→ even) ⓓ many(→ much)'),
   (5, '어법', '(가) takes (나) care (라) is (바) bought'),
   (4, '내용 이해', 'Araon은 다른 배보다 강해 두꺼운 얼음을 깸'),
   (1, '추론', '옳은 것은 "세 사람 모두 자연과 조화롭게 일함" 1개'),
   (5, '제목', '옛 직업 지키기 ✘ — 자연을 지키며 일하는 사람들'),
   (5, '어휘·어법', 'care, in, more, look, to → out은 안 들어감'),
   (4, 'to부정사', '④ to cleaning → to clean'),
   (5, '전치사', '[A] care about / [B] keep an eye on → ⓔ가 다름'),
   (5, '내용 일치', 'Jihan은 지리산에서 일함 — 북극 연구 ✘'),
   (1, '접속사 that', '① ✓ — can be, our teacher is from, know, hopes that you'),
   (2, '내용 일치', 'Jihan은 지리산의 야생 동물 관리 센터에서 일함'),
   (3, '추론', '북극해에 기후 위기의 답 → 기후 변화 연구에 도움'),
   (1, '전치사 to', 'ⓔ keep an eye on만 to ✘ → 1개'),
   (5, '영작', '(E) I hope that my work can help the Earth. ✓'),
   (3, '내용 이해', '아침에 조수와 날씨를 확인함'),
   (4, '내용 이해', '맞는 건 민수(노르웨이)뿐 → 틀린 학생 4명'),
   (5, '어휘', 'ⓔ proud = 자랑스러운 ✓'),
   (2, 'to부정사', '못 고치는 것: ⓑ practice + -ing, ⓔⓕ should, ⓗ should not, ⓘ don\'t 뒤 동사원형'),
   (3, '어법', '틀린 것 ⓑ can break ⓒ hopes ⓓ That절 주어 없음 ⓔ want to become')]},
]
tests = []
for S in SETS:
    items = []
    for n, (a, typ, why) in enumerate(S['key'], 1):
        multi = isinstance(a, list); A = [x - 1 for x in a] if multi else a - 1
        mark = ''.join(C[x] for x in A) if multi else C[A]
        items.append({'n': n, 'src': typ, 'stem': '%d번%s' % (n, ' (%d개 고르기)' % len(A) if multi else ''), 'body': '', 'opts': list(C), 'en': False, 'ans': A,
                      'ex': '정답 ▶ %s\n풀이 ▶ %s' % (mark, why), 'ctx': '', 'pts': 5, 'words': [], 'kos': []})
    assert len(items) == 20
    tests.append({'id': S['id'], 'kind': 'exam', 'retry': 1, 'title': S['title'], 'short': S['short'], 'school': '심학중 1학년', 'minutes': 40, 'note': '문제는 종이 족보(%s)로 풀고, 여기엔 답만 입력해요.' % S['src'], 'items': items})
src = open(path, encoding='utf-8').read()
src = re.sub(r'/\* M1SJB-TESTS.*?/\* /M1SJB-TESTS \*/\n?', '', src, flags=re.S)
ids = [t['id'] for t in tests]
src = src.rstrip('\n') + '\n/* M1SJB-TESTS: 족보 OMR 답만 입력 (gen/m1sjb/build.py 로 만듦 · 손으로 고치지 말 것) */\nwindow.PKG.tests = (window.PKG.tests || []).filter(function (t) { return %s.indexOf(t.id) < 0; }).concat(%s);\n/* /M1SJB-TESTS */\n' % (json.dumps(ids), json.dumps(tests, ensure_ascii=False))
open(path, 'w', encoding='utf-8').write(src)
print([(t['id'], len(t['items']), ''.join(C[i['ans']] if not isinstance(i['ans'], list) else '[' + ''.join(C[x] for x in i['ans']) + ']' for i in t['items'])) for t in tests])
