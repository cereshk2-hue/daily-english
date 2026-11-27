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
 {'id': 'm1jb-6a', 'title': '족보 OMR · 6과 문법 공략 (01) 25문항', 'short': '족보 6과 (01)', 'src': '6.Good for the Earth, Good for Us(01) 문법 공략(교육지대)',
  'key': [
   (3, 'to부정사', '(가) forgot to turn off(끄는 것을 잊다) (나) and 뒤 동사원형 turn off'),
   (4, 'to부정사', '④ 보어(꿈은 ~하는 것), 나머지는 want·plan·hope·decide의 목적어'),
   (5, '접속사 that', "⑤ ✘ — 주어 자리 that은 생략할 수 없음"),
   (4, '종합', '틀린 것 4개: Play→To play/Playing, his friends (are) kind, To make ~ is, enjoys cooking'),
   (4, '종합', '④ 옳음(today I didn’t 뒤 use ~ 생략) — 나머지: is getting, join, were, goes'),
   (3, 'to부정사', '보어 자리 to부정사 → Our dream is to keep the environment.'),
   (4, 'to부정사', '④ want to be ✓ — decide/hope + to, enjoy + -ing, like to study'),
   (3, '접속사 that', "Ⓐ think 뒤 접속사 that = ③ feels that — 나머지 지시대명사·지시형용사·부사"),
   (2, '종합', '맞는 설명 ⓑⓓ 2개 — ⓐ·ⓒ to 쓰임 다름(ⓒ 전치사), ⓔ in return, ⓕ 생략된 건 접속사 that'),
   ([2, 5], '생략', '생략 불가: ② needs to의 to, ⑤ show A to B의 전치사 to (두 개)'),
   (3, '배열', 'He wants to join the challenge.'),
   (4, 'to부정사', '옳은 것 (1)(2)(3)(4) 4개 — (5) suggested going, (6) hopes'),
   (4, 'to부정사', '보어 자리 → to become'),
   (5, '배열', 'The Earth is getting sicker and sicker. → 4번째 getting'),
   (4, '종합', '④ ✘ — 대명사 those가 아니라 points를 꾸미는 that → those points'),
   (2, '종합', '설명이 옳은 사람 고르기 → ②'),
   (3, '종합', '(A) want to save (B) 명령문 join (C) can + 동사원형 find'),
   (2, 'to부정사·that', '같은 역할끼리: A–D(목적어) / B–F(보어) / C–E(주어)'),
   (3, '종합', '지수·리사 설명 옳음 — 제니(ⓐ to는 전치사 아님 등)·로제(like=~처럼, 전치사) 틀림'),
   (2, '배열', 'I believe that you can do it. → 3번째 that, 6번째 do'),
   (1, '어휘·어법', '① lots of는 셀 수 있는·없는 명사 모두 — waste(셀 수 없음) 앞 가능'),
   (2, 'that 쓰임', '접속사 that(ⓐⓑⓓ) / 지시대명사 that(ⓒⓔ)'),
   (1, '종합', '(A) 동명사 주어 → is (B) looks + 형용사 perfect (C) 과거 got (D) Don’t you'),
   (4, '접속사 that', '④ 옳음 — that절 주어는 단수 취급(means, was), The news is, Her wish is'),
   (2, '종합', '설명이 틀린 사람 → ②(유나 등) — that절 시제 was, 주어 자리 that 생략 불가')]},
 {'id': 'm1jb-7a', 'title': '족보 OMR · 7과 문법 공략 (01) 25문항', 'short': '족보 7과 (01)', 'src': '7.Find Your Dream(01) 문법 공략(교육지대)',
  'key': [
   (4, 'to부정사', '④ want to make ✓ — be동사 빠짐·likes flying/to fly·병렬 fly·try making'),
   (3, '영작', "I'm going to use drones to capture their happy moments. (목적 to)"),
   (2, 'to부정사 부사적', '옳은 것 ⓐⓒ 2개 — ⓑ to receive, ⓓ so as to keep, ⓔ to hear'),
   (2, 'to부정사 부사적', '틀린 것 ⓑⓓ — ⓑ to hear, ⓓ in order to avoid'),
   (1, 'to부정사 부사적', '목적의 to = ① to calm him — 나머지 감정 원인·명사적·형용사 수식'),
   (1, '배열', 'Amy did homework before she watched TV. → 5번째 she'),
   (5, 'to부정사 쓰임', '옳게 설명한 사람: 수빈·다현·지훈'),
   (5, 'when', 'The doorbell rang when we were having dinner.'),
   (2, '시간 부사절', '알맞게 영작한 것 ⓐⓔ 2개'),
   (4, '시간 부사절', '옳은 것끼리 ④ — 부사절은 미래도 현재형(arrive·see), when 뒤 주어+동사'),
   (4, 'when 쓰임', "④는 의문사 when(언제), 나머지는 접속사(~할 때)"),
   (3, 'when', '뒤에 주어+동사가 오는 ③에 접속사 when'),
   (1, '시간 접속사', '(A) After (B) play(현재형) (C) When'),
   (2, 'after·before', '순서가 같은 것: A와 C'),
   (3, 'to부정사 부사적', '목적의 to와 같은 것 3개'),
   (3, '영작', '③ ✘ — before → after (촬영이 끝난 후에)'),
   (2, 'when', '빈칸 뒤 주어+동사 → 접속사 when'),
   (4, '종합', '어법상 틀린 문장 개수 → ④'),
   (4, 'during', 'While I was walking home = during my walk home'),
   (4, '배열', 'To sleep well, Tim drinks tea at night. → 세 번째 drinks'),
   (5, '시간 부사절', 'when he studies(미래도 현재형) → ⑤'),
   (3, 'after 쓰임', '<보기> 접속사 after = ③ when 접속사(뒤에 주어+동사)'),
   (4, 'after', '공통으로 after(~한 후에)'),
   (2, 'to부정사 부사적', '공통 to(~하기 위해) → ② to / To'),
   (1, 'after 쓰임', "① after는 전치사(뒤에 명사), 나머지는 접속사")]},
]
tests = []
for S in SETS:
    items = []
    for n, (a, typ, why) in enumerate(S['key'], 1):
        multi = isinstance(a, list); A = [x - 1 for x in a] if multi else a - 1
        mark = ''.join(C[x] for x in A) if multi else C[A]
        items.append({'n': n, 'src': typ, 'stem': '%d번%s' % (n, ' (%d개 고르기)' % len(A) if multi else ''), 'body': '', 'opts': list(C), 'en': False, 'ans': A,
                      'ex': '정답 ▶ %s\n풀이 ▶ %s' % (mark, why), 'ctx': '', 'pts': 4, 'words': [], 'kos': []})
    tests.append({'id': S['id'], 'kind': 'exam', 'title': S['title'], 'short': S['short'], 'school': '중산중 1학년', 'minutes': 40, 'note': '문제는 종이 족보(%s)로 풀고, 여기엔 답만 입력해요.' % S['src'], 'items': items})
src = open(path, encoding='utf-8').read()
src = re.sub(r'/\* M1JB-TESTS.*?/\* /M1JB-TESTS \*/\n?', '', src, flags=re.S)
ids = [t['id'] for t in tests]
src = src.rstrip('\n') + '\n/* M1JB-TESTS: 족보 OMR 답만 입력 (gen/m1jb/build.py 로 만듦 · 손으로 고치지 말 것) */\nwindow.PKG.tests = (window.PKG.tests || []).filter(function (t) { return %s.indexOf(t.id) < 0; }).concat(%s);\n/* /M1JB-TESTS */\n' % (json.dumps(ids), json.dumps(tests, ensure_ascii=False))
open(path, 'w', encoding='utf-8').write(src)
print([(t['id'], len(t['items']), ''.join(C[i['ans']] if not isinstance(i['ans'], list) else '[' + ''.join(C[x] for x in i['ans']) + ']' for i in t['items'])) for t in tests])
