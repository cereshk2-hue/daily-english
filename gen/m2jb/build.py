# 11/27 중산중2 족보 OMR 답만 입력 (문제는 종이 족보, 앱엔 번호 + ①~⑤만) → m2-donga-yoon-L7 /* M2JB-TESTS */
# kind 'exam' → '실전기출' 탭, retry 1 (틀린 번호만 → 한 번 더 → 해설, 점수는 첫 제출)
# 정답: 족보 [정답](그림 속 원문자, pdf 6~8쪽을 그림으로 읽음) + 20문항 모두 직접 풀어 대조(일치). 해설은 짧게 내 말로
import json, re
path = '/home/claude/proj/data/m2-donga-yoon-L7.js'
C = '①②③④⑤'
SETS = [
 {'id': 'm2jb-7b', 'title': "족보 OMR · 7과 Let's Enjoy Festivals (02) 20문항", 'short': '족보 7과 (02)', 'src': "7.Let's Enjoy Festivals(02) 최다오답 공략(교육지대)",
  'key': [
   ([1, 3], '대화 내용', '① 할머니 선물을 찾음 ③ 크지만 아주 가볍다고 함 (두 개 고르기)'),
   (5, '내용 이해', 'remember dead people = 세상을 떠난 가족·친구를 기억하기'),
   (1, '어법', '(A) call A B(5형식, as ✘) (B) hardly = 거의 ~않다 (C) can + 동사원형 enjoy'),
   (1, '가주어 it', 'To keep ~ is → It is important to keep ~ (형용사 important, to + 동사원형)'),
   (2, '대화 내용', '불꽃놀이는 저녁 7시 시작 — 아시아 나라는 중국·한국 둘뿐'),
   (4, '가목적어 it', '④만 that절 안의 가주어 it(it was worthwhile to ~), 나머지는 5형식 가목적어 it'),
   (4, '내용 이해', '이기고 지는 것보다 즐기는 것이 중요 → ④'),
   (3, '어법', 'ⓒ to remembering → to remember (to부정사)'),
   ([2, 4], '대화 추론', '② 월요일 시험 준비 ④ 도서관보다 집에서 공부가 좋다 (두 개 고르기)'),
   (4, '어법', '④ 여전히 틀림 — necessary는 for everyone, to 뒤 동사원형 follow'),
   (2, '대화 빈칸', '떡볶이가 더 좋은 이유 → 매운맛 음식을 가장 좋아한다'),
   (3, '내용 이해', '③ ✘ — fallas는 마지막 날 태워 없앰(계속 세워 두지 않음)'),
   (5, '말의 목적', '음식 축제에서 인도 셰프 Kumar의 요리 교실 소개'),
   (1, '빈칸', '순록보다 빨리 달리려 함 → 가능하냐고? 아니지만 상관없음'),
   (4, '내용 일치', '④ ✘ — 기둥 주변에서 전통 춤(민속 노래 ✘)'),
   (3, '어법', '(ㄷ) to drinking → to drink 가 올바른 수정'),
   (4, '대화 내용', '④ 세수를 몇 번 했는지는 나오지 않음'),
   (2, '5형식', 'call it the Midsummer festival = 목적어 + 목적격 보어 → ② named our new puppy Max'),
   (2, '어법', 'ⓒ to saving, ⓔ to finishing → 동사원형이어야 함 (2개)'),
   (4, '내용 일치', '④ ✘ — K-pop 공연 추가 요금은 나오지 않음')]},
 {'id': 'm2jb-8b', 'title': '족보 OMR · 8과 Time Travel (02) 20문항', 'short': '족보 8과 (02)', 'src': '8.Time Travel(02) 최다오답 공략(교육지대)',
  'key': [
   (5, '-thing + 형용사', '⑤ heavy something → something heavy'),
   (5, '어법', "ⓔ didn't killed → didn't kill (did 뒤 동사원형)"),
   (2, '영작', 'Jinsu went to buy something warm for his sister to wear → of 필요 없음'),
   (5, '내용 이해', '10분 뒤 출발하는 기계가 있다고 함 → ⑤만 답할 수 있음'),
   (3, '현재완료', '가 버려서 지금 없음 = has gone to (결과)'),
   (4, '-thing + 형용사', 'ⓐT2 ⓑT0 ⓒF2(nothing special) ⓓT7 ⓔF6(something exciting) → 20276'),
   (5, '어법', 'ⓔ angrily → angry (명사 voice를 꾸미는 형용사)'),
   (1, '함축 의미', "'바보 아니에요' = 규칙을 지킬 수 있다고 자신함"),
   (3, '무관한 문장', '③ 타임머신이 SF에 자주 나온다는 일반 사실 → 흐름과 무관'),
   (4, '주제', '과거의 작은 실수(나비)가 바꾼 미래'),
   (5, '5형식', '⑤ kept everything organized = 목적어 + 목적격 보어, 나머지는 -thing/-one + 형용사(목적어)'),
   (2, '현재완료', '옳은 것 ㄱ·ㄹ 2개 — ㄴ seen, ㄷ eaten, ㅁ Have you'),
   (4, 'for/since', '④ five years(기간) → for, 나머지는 since'),
   (3, '배열', "I didn't find anything special in the box. → 네 번째 anything"),
   (1, '요약', '죽은 나비 때문에 미래가 바뀌어 충격(shocked) — future'),
   (4, '어법', '(A) since 2015 → has lived (B) anything warm (C) have never seen'),
   (4, '빈칸', 'have always wanted = 늘 ~하고 싶었다'),
   (3, '현재완료', 'just arrived = 완료 → ③ already finished'),
   (4, '내용 일치', 'ⓐ 100m 밖 T.rex ⓒ 겁에 질려 실수로 길을 벗어남 ⓔ 나가게 해 달라고 함'),
   (3, '영영풀이', 'returned(돌아왔다)의 풀이는 <보기>에 없음')]},
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
    tests.append({'id': S['id'], 'kind': 'exam', 'retry': 1, 'title': S['title'], 'short': S['short'], 'school': '중산중 2학년', 'minutes': 40, 'note': '문제는 종이 족보(%s)로 풀고, 여기엔 답만 입력해요.' % S['src'], 'items': items})
src = open(path, encoding='utf-8').read()
src = re.sub(r'/\* M2JB-TESTS.*?/\* /M2JB-TESTS \*/\n?', '', src, flags=re.S)
ids = [t['id'] for t in tests]
src = src.rstrip('\n') + '\n/* M2JB-TESTS: 족보 OMR 답만 입력 (gen/m2jb/build.py 로 만듦 · 손으로 고치지 말 것) */\nwindow.PKG.tests = (window.PKG.tests || []).filter(function (t) { return %s.indexOf(t.id) < 0; }).concat(%s);\n/* /M2JB-TESTS */\n' % (json.dumps(ids), json.dumps(tests, ensure_ascii=False))
open(path, 'w', encoding='utf-8').write(src)
print([(t['id'], len(t['items']), ''.join(C[i['ans']] if not isinstance(i['ans'], list) else '[' + ''.join(C[x] for x in i['ans']) + ']' for i in t['items'])) for t in tests])
