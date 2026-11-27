# 11/27 중산중1 족보 OMR 답만 입력 (문제는 종이 족보, 앱엔 번호 + ①~⑤만) → m1-donga-yoon-L6 /* M1JB-TESTS */
# kind 'exam' → 앱의 '실전기출' 탭에 따로(다른 Wrap-up과 섞이지 않게)
# 정답: 족보 자체 [정답](그림 속 원문자, pdf 7·8쪽을 그림으로 읽음) + 문항마다 직접 풀어 대조. 해설은 짧게 내 말로(문제 원문 옮기지 않음)
import json, re
path = '/home/claude/proj/data/m1-donga-yoon-L6.js'
C = '①②③④⑤'
SETS = [
 {'id': 'm1jb-5a', 'title': '족보 OMR · 5과 문법 공략 (01) 25문항', 'short': '족보 5과 (01)', 'src': '5.Think like Sherlock Holmes!(01) 문법 공략(교육지대)',
  'key': [   # (정답 번호(1~5, 여러 개면 리스트), 유형, 짧은 해설)
   (3, '영작', '말을 걸다 speak to의 과거 spoke to + 목적어 him + in Spanish'),
   (3, '영작', '과거 부정 didn’t + 동사원형 understand, 타동사라 바로 목적어 me'),
   (4, 'There is/are', '옳은 것 ⓐⓑⓒ — ⓓ last Sunday → Were, ⓔ two books → were'),
   (4, '비교급', 'Mike의 자전거가 더 빠르다 = 내 자전거가 더 느리다'),
   (4, 'There is/are', '바르게 고친 것 (가)(나)(마) — (다)는 과거·단수라 Was, (라)는 과거·복수라 were여야 함'),
   (4, 'There is/are', "'~가 있다'의 there: ⓐⓒⓔ — ⓑⓓ는 '그곳에(부사)'"),
   (3, 'There is/are', 'ⓒ pieces of cake(복수) → were'),
   (5, '종합', '틀린 것 (c) some cookies → are, (d) big → bigger, (e) the hottest → hotter'),
   (1, 'There is/are', '(A) pieces(복수)·과거 → were (B) was 뒤 단수 a wheelchair (C) next to'),
   (3, '비교급·최상급', '옳은 것 ⓐⓓⓔ 3개 — ⓑ the biggest, ⓒ more delicious'),
   (1, '최상급', '최상급 앞 the 필요 → the most expensive car'),
   (4, 'that 쓰임', "지시형용사 '그 ~': ⓐⓒⓔ — ⓑⓓ는 접속사"),
   (2, '비교급·최상급', '(A) in the class → the best (B) than → longer (C) than + 3음절 → more delicious'),
   (4, '비교급', 'difficult는 3음절 → more difficult'),
   (4, '-er 쓰임', '④만 ~하는 사람(명사 runner), 나머지는 비교급 -er'),
   (4, '배열', 'There is not much water in the desert. → 네 번째 much'),
   (3, 'There is/are', 'two windows(복수) → Are there'),
   (4, 'There is/are', '그림과 맞는 문장 ④(책상 위 컴퓨터)'),
   (2, 'There is/are', '옳은 것 ⓒⓓ 2개 — ⓐ water → is, ⓑ a cat → was, ⓔ yesterday → wasn’t'),
   (2, 'There is/are', 'any apples(복수) → Are'),
   (2, 'There is/are', '재현 ✘ — Is there ~?의 대답은 Yes, there is. / No, there isn’t.'),
   (2, 'so 쓰임', "② so = '매우'(부사), 나머지는 '그래서'(접속사)"),
   (2, '-ing 쓰임', 'ⓐ following(다음 것)·ⓒ painting(그림)은 명사, 나머지는 과거진행형'),
   ([3, 4], '비교 추론', '③ Yena가 셋 중 가장 작다 ④ 남동생은 나보다 일찍 오지 않았다 (두 개 고르기)'),
   (5, '종합', "지훈 ✘ — a little은 '조금, 약간'(조금 더 크다)")]},
]
tests = []
for S in SETS:
    items = []
    for n, (a, typ, why) in enumerate(S['key'], 1):
        multi = isinstance(a, list); A = [x - 1 for x in a] if multi else a - 1
        mark = ''.join(C[x] for x in A) if multi else C[A]
        items.append({'n': n, 'src': typ, 'stem': '%d번%s' % (n, ' (두 개 고르기)' if multi else ''), 'body': '', 'opts': list(C), 'en': False, 'ans': A,
                      'ex': '정답 ▶ %s\n풀이 ▶ %s' % (mark, why), 'ctx': '', 'pts': 4, 'words': [], 'kos': []})
    tests.append({'id': S['id'], 'kind': 'exam', 'title': S['title'], 'short': S['short'], 'school': '중산중 1학년', 'minutes': 40, 'note': '문제는 종이 족보(%s)로 풀고, 여기엔 답만 입력해요.' % S['src'], 'items': items})
src = open(path, encoding='utf-8').read()
src = re.sub(r'/\* M1JB-TESTS.*?/\* /M1JB-TESTS \*/\n?', '', src, flags=re.S)
ids = [t['id'] for t in tests]
src = src.rstrip('\n') + '\n/* M1JB-TESTS: 족보 OMR 답만 입력 (gen/m1jb/build.py 로 만듦 · 손으로 고치지 말 것) */\nwindow.PKG.tests = (window.PKG.tests || []).filter(function (t) { return %s.indexOf(t.id) < 0; }).concat(%s);\n/* /M1JB-TESTS */\n' % (json.dumps(ids), json.dumps(tests, ensure_ascii=False))
open(path, 'w', encoding='utf-8').write(src)
print([(t['id'], len(t['items']), ''.join(C[i['ans']] if not isinstance(i['ans'], list) else '[' + ''.join(C[x] for x in i['ans']) + ']' for i in t['items'])) for t in tests])
