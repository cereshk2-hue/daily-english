# 11/25 중산중2 동아(윤정미) 7·8과 본문 '문장 순서 · 문장 삽입'만 완벽 학습 세트
#  DAY: od7(7과 순서) · oi7(7과 삽입) · od8(8과 순서) · oi8(8과 삽입) 맨 끝 / 시험: m2oi-7 · m2oi-8 (실전 문제 탭, 20문항씩, 종이 시험지)
#  순서 DAY = gen_m1dorder.py 방식(2문장 조각 · 덩이 · tries 3, 본문 한 줄도 안 빠짐) / 삽입 = 단서가 분명한 문장만, 같은 단락 안 6줄 창(①~⑤)
import sys, json, re, subprocess, html, random
sys.path.insert(0, '/home/claude/srcrepo/generators')
from gencommon import write
path = [a for a in sys.argv[1:] if a != 'emit'][0] if [a for a in sys.argv[1:] if a != 'emit'] else '/home/claude/proj/data/m2-donga-yoon-L7.js'
PK = json.loads(subprocess.check_output(['node', '-e', "global.window={};require('%s');process.stdout.write(JSON.stringify(window.PKG))" % path]))
D = {d['id']: d for d in PK['days']}
MARK = re.compile(r'^[❶-❿]$')
HEAD = lambda x: not re.search(r'[.!?]["”’]?$', x.strip())
C = '①②③④⑤'
def sections(keys):
    out = []
    for k in keys:
        for l in D[k]['passage']:
            if l[0] == '#': continue
            if MARK.match(l[1]): out.append((l[1], [])); continue
            out[-1][1].append((l[1], l[2]))
    return out
S7 = dict(sections(('d1', 'd2'))); S8 = dict(sections(('d3', 'd4')))
def body(S, m): return [x for x in S[m] if not HEAD(x[0])]   # 7과 제목 줄 빼고
# ───────── 순서 DAY (본문 전부, 2문장 조각) ─────────
def pairs(sents): return [sents[i:i + 2] for i in range(0, len(sents), 2)]
def join(p, i):
    a = p[0][i]
    for x, y in zip(p, p[1:]): a += (': ' if HEAD(x[0]) else ' ') + y[i]
    return a
def order_day(gid, rng, S, groups, nsent):
    items, passage, n = [], [], 0
    for gi, g in enumerate(groups):
        ps = sum((pairs(S[m]) for m in g), [])
        lines = [join(p, 0) for p in ps]; assert len(lines) >= 3 and len(set(lines)) == len(lines)
        items.append({'lines': lines}); n += sum(len(S[m]) for m in g)
        passage.append(['#', '덩이 %d · 본문 %s' % (gi + 1, ''.join(g)), ''])
        passage += [['', join(p, 0), join(p, 1)] for p in ps]
    assert n == nsent, (n, nsent)
    return {'id': gid, 'name': '', 'range': rng, 'story': rng + ' · 2줄씩 조각, 본문 %d덩이 (본문 %d줄 전부)' % (len(groups), n), 'passage': passage,
            'steps': [{'type': 'order', 'title': '문장 순서', 'tries': 3,
                       'guide': "본문을 %d덩이로 나눴어요. 덩이마다 우리말 조각을 내용 흐름대로, 다음에 영어 조각을 본문 순서대로 놓아요(한 조각 = 2문장). 모두 맞혀야 100점, 하나라도 틀리면 0점! 3번 안에 통과 못 하면 오답 학습을 하고 다시 도전해요." % len(groups),
                       'items': items}]}
# ───────── 삽입: (단락, 몇 번째 문장(제목 빼고 0부터), 단서) ─────────
I7 = [('❶', 1, "This festival(이 축제)이 가리키는 the Fallas festival이 바로 앞에 나와야 해요."),
      ('❶', 3, "fallas(거대한 나무 조각상)를 처음 소개하는 문장 → 뒤의 hundreds of them(그것들 수백 개)의 them이 바로 fallas예요."),
      ('❶', 4, "them = 바로 앞에서 소개한 fallas, giant wooden statues. 소개 뒤, 태우는 이야기(Surprisingly ~) 앞이에요."),
      ('❶', 5, "the fallas are burned(파야들이 태워진다) 다음에 Burning them(그것들을 태우는 것)의 의미가 이어져요."),
      ('❶', 6, "Burning them = 앞 문장의 '파야들을 태우는 것' → 태운다는 말이 먼저 나와야 해요."),
      ('❷', 1, "a special festival을 처음 말하는 문장 → 뒤의 They call it ~(그것을 ~라 부른다)의 it이 이 축제예요."),
      ('❷', 2, "They call it the Midsummer festival.의 it = 앞 문장의 a special festival."),
      ('❷', 4, "축제 날짜(6월 19~25일 사이 금요일 시작) 소개 뒤 → During the festival(축제 기간에) 하는 일. it(장대)이 a tall pole을 받아요."),
      ('❷', 5, "해가 거의 지지 않아서(because the sun hardly sets) 밤새 즐길 수 있다 → 축제 활동 소개 다음, 글의 마지막."),
      ('❸', 1, "this day(이날) = 앞 문장의 once a year(일 년에 한 번) 죽은 사람들이 돌아오는 날."),
      ('❸', 3, "They believe(그들은 믿는다) it is important to remember dead people → 다음 문장 So(그래서) 제단·묘지 파티의 이유예요."),
      ('❸', 4, "So(그래서) → 앞 문장(고인을 기억하는 것이 중요하다고 믿는다)의 결과로 제단을 차리고 파티를 열어요."),
      ('❸', 5, "In some areas(일부 지역에서는) → 모든 사람이 하는 일(제단·파티) 다음에 일부 지역의 특별한 모습(해골 분장)을 덧붙여요."),
      ('❹', 1, "During this festival(이 축제 기간에) → Fur Rondy festival을 소개한 첫 문장 바로 뒤."),
      ('❹', 2, "also(또한)로 앞의 즐길 거리(겨울 스포츠·전통 게임)에 더하고, the Running of the Reindeer가 뒤의 this race(이 경주)로 이어져요."),
      ('❹', 3, "this race(이 경주) = 앞 문장의 the Running of the Reindeer(순록 달리기)."),
      ('❹', 4, "do so(그렇게 하다) = 앞 문장의 run faster than reindeer(순록보다 빨리 달리기). 뒤 Not really(그렇지는 않다)가 이 질문의 대답이에요."),
      ('❹', 5, "Not really(그렇지는 않다)는 앞의 질문 Is it possible to do so?에 대한 대답."),
      ('❹', 6, "앞 문장 but it doesn't matter(중요하지 않다)에 이어 '모두 그저 즐길 뿐이다'로 글을 마무리해요.")]
I8 = [('❶', 3, "Mr. Parker를 처음 소개하는 문장(the founder of Time Travel) → 뒤에서 Eckels가 원하는 것을 말해요. How can we help you?에 대한 대답이 I've always wanted ~."),
      ('❶', 4, "Is it possible?(가능한가요?)에 대한 대답이 뒤의 \"Sure,\"(물론이죠)예요."),
      ('❶', 5, "\"Sure\"는 앞의 질문 Is it possible?에 대한 대답이고, 뒤에서 We can take you back ~으로 설명을 이어요."),
      ('❶', 7, "Can you take me there now?(지금 데려가 줄 수 있나요?) → 뒤의 You're lucky. 10분 후에 출발하는 타임머신이 있다가 대답이에요. there = 6천만 년 전 정글."),
      ('❶', 8, "You're lucky ~ leaves in 10 minutes는 앞의 질문 Can you take me there now?에 대한 대답이에요."),
      ('❶', 9, "Travis를 처음 소개(your travel guide) → 뒤 follow his instructions의 his가 Travis예요. he continued(그는 계속 말했다) = Mr. Parker."),
      ('❶', 10, "his instructions(그의 지시) = 앞에서 소개한 Travis의 지시."),
      ('❷', 2, "자리에 앉아 눈을 감음 → 발밑에서 기계가 움직이는 것을 느낌 → 몇 분 뒤 멈춤. 출발(움직임)은 멈춤 앞이에요."),
      ('❷', 3, "After only a few minutes, the machine stopped. → 바로 뒤 We've just arrived(방금 도착했다)로 이어져요."),
      ('❷', 4, "We've just arrived ~는 기계가 멈춘(stopped) 다음. 뒤의 Do you see the path ~?도 Travis의 말이에요."),
      ('❷', 6, "it = 앞 문장의 the path(저쪽 길). '길을 절대 벗어나지 마라'는 길을 보여 준 직후예요."),
      ('❷', 8, "Do not touch anything(아무것도 만지지 마라)의 이유 → 실수로 무언가를 죽일 수도 있다 → 작은 변화가 미래에 엄청난 일을 일으킬 수 있다."),
      ('❸', 4, "Be careful ~ said Travis → 바로 뒤 \"Just stay calm.도 Travis의 말이 이어지는 것. Eckels의 I'm so excited에 대한 경고예요."),
      ('❸', 7, "I'm not a fool(나는 바보가 아니다)은 앞의 anything foolish(어리석은 행동)에 대한 Eckels의 대답."),
      ('❸', 8, "대화(주의·대답)를 마치고 모두 길을 걷기 시작함 → 단락의 마지막."),
      ('❹', 1, "Travis가 There is a T. rex(티라노가 있다)라고 속삭임 → 100미터 떨어진 곳에 티라노가 서서히 나타남."),
      ('❹', 3, "\"Sh!\"(쉿!)는 Eckels가 말을 꺼내자(\"It ... It ...\") Travis가 조용히 하라고 한 것."),
      ('❹', 5, "Sh ... quiet! You don't want it to see you.는 Eckels가 '너무 무섭다'고 소리 내 말한 뒤 Travis가 화를 내며 한 말."),
      ('❹', 7, "Get me out of here!(여기서 꺼내 줘!) → Don't panic. 돌아서서 기계로 조용히 돌아가라는 Travis의 지시."),
      ('❹', 8, "Turn around(돌아서라)라는 지시대로 돌아섰지만 started to run(뛰기 시작했다) → 뒤에서 겁에 질려 길을 벗어남."),
      ('❹', 9, "he left the path by accident(실수로 길을 벗어났다) → 바로 뒤 Travis의 외침 Don't leave the path!"),
      ('❹', 11, "The T. rex heard Travis → Travis가 외친(shouted) 뒤예요. 뒤에 정적(a moment of silence)이 이어져요."),
      ('❹', 13, "There was a moment of silence. Then(그러고 나서) 갑자기 달려옴 → Run, everybody!"),
      ('❺', 1, "기계 안에서 Eckels를 발견 → 화난 목소리로 '당신이 우리 모두를 위험에 빠뜨렸다' → You left the path.(이유)"),
      ('❺', 3, "I'm sorry, but I didn't kill anything은 앞의 You left the path.(길을 벗어났다)라는 비난에 대한 대답."),
      ('❺', 4, "There's only a little mud on my shoes.는 '아무것도 죽이지 않았다'에 덧붙인 Eckels의 변명. 뒤에서 Travis가 말없이 쳐다봐요."),
      ('❺', 5, "Travis stared ~ without saying anything(아무 말 없이) → 뒤 '집으로 갑시다' said Travis finally(마침내)."),
      ('❻', 1, "The machine stopped. → They all returned to the present safely.(현재로 안전하게 돌아옴)"),
      ('❻', 3, "Fine. Welcome home!은 앞의 질문 Is everything okay here?에 대한 Mr. Parker의 대답."),
      ('❻', 5, "Eckels looked around the room carefully. → Everything looked the same, except the big sign → 뒤 The sign now said ~."),
      ('❻', 6, "The sign now said ~(간판에 이제 이렇게 쓰여 있다) → 앞에서 except the big sign on the wall로 간판을 먼저 말해야 해요."),
      ('❻', 7, "철자가 엉망인 간판을 보고 Eckels was confused(혼란스러웠다) → 뒤 Then, he saw the TV."),
      ('❻', 9, "Then, he saw the TV. → TV 뉴스의 새 대통령이 Keith 씨가 아니었다 → What's going on?"),
      ('❻', 10, "He got more confused(더 혼란스러워졌다) → 간판(confused) 다음에 대통령까지 바뀐 것을 본 뒤예요."),
      ('❻', 11, "He sat down and looked closely at the mud on his shoes. → 진흙을 보고 \"No, it can't be,\"."),
      ('❻', 15, "In the mud on his right shoe, he found a small dead butterfly. → 글의 마지막. 앞의 this little thing(이 작은 것)의 정체예요.")]
CYC = [2, 4, 1, 5, 3, 3, 1, 4, 2, 5]
def ins_items(S, L, tag):
    out = []
    for k, (m, idx, clue) in enumerate(L):
        b = body(S, m); n = min(6, len(b)); assert 1 <= idx < len(b), (m, idx)
        want = CYC[k % len(CYC)]
        feas = [p for p in range(1, n) if 0 <= idx - p and idx - p + n <= len(b)]
        p = min(feas, key=lambda q: (abs(q - want), q))
        s = idx - p; win = b[s:s + n]
        assert win[p] == b[idx]
        pv, nx = win[p - 1], (win[p + 1] if p + 1 < n else None)
        ex = '정답 ▶ %s\n이유 ▶ %s\n앞 문장 ▶ %s (%s)' % (C[p - 1], clue, pv[0], pv[1])
        ex += ('\n뒤 문장 ▶ %s (%s)' % (nx[0], nx[1])) if nx else '\n뒤 문장 ▶ 없음 (단락의 마지막)'
        out.append({'lines': [w[0] for w in win], 'given': p, 'ex': ex, 'm': m, 'ko': b[idx][1], 'clue': clue, 'tag': tag})
    return out
IT7 = ins_items(S7, I7, '7과'); IT8 = ins_items(S8, I8, '8과')
def ins_day(gid, rng, its):
    return {'id': gid, 'name': '', 'range': rng, 'story': rng + ' · 단서가 분명한 문장 %d개 · 같은 단락 6줄 안에서 ①~⑤' % len(its),
            'passage': None, 'steps': [{'type': 'insert', 'title': '문장 삽입', 'guide': "주어진 문장이 들어갈 곳을 고르세요. 대명사(it·them·this)·연결어(So·Then·also)·질문↔대답이 단서예요. 틀리면 해설의 앞뒤 문장을 꼭 읽어요.",
                                        'items': [{'lines': x['lines'], 'given': x['given'], 'ex': x['ex']} for x in its]}]}
DROP = {('7과', '❶', 1), ('7과', '❷', 4), ('7과', '❷', 5), ('8과', '❷', 8)}   # 다른 자리도 말이 되는 것(논쟁 소지) 뺌
def keep(L, IT, tag): return [x for x, y in zip(L, IT) if (tag,) + x[:2] not in DROP], [y for x, y in zip(L, IT) if (tag,) + x[:2] not in DROP]
I7, IT7 = keep(I7, IT7, '7과'); I8, IT8 = keep(I8, IT8, '8과')   # 창(6줄)은 검토한 그대로 두고 뺄 것만 뺌
# ───────── 시험 순서 문항: (단락, 주어진 글, [정답 순서의 조각들], 해설) ─────────
O7 = [('❶', [0, 1, 2], [[3], [4], [5, 6]], "축제의 주인공 fallas 소개 → hundreds of them(them = fallas) → Surprisingly 마지막 날 태워짐 · Burning them의 의미"),
      ('❷', [0], [[1], [2, 3], [4, 5]], "a special festival → They call it(it = 그 축제) the Midsummer festival · 날짜 → During the festival 장대 장식·춤 · 해가 지지 않아 밤새 즐김"),
      ('❸', [0], [[1, 2], [3, 4], [5]], "this day(= 죽은 이가 돌아오는 날) 이름 · 11월 1~2일 축제 → 기억이 중요하다고 믿음 · So 제단·파티 → In some areas 해골 분장"),
      ('❹', [0, 1], [[2, 3], [4, 5], [6]], "also 특별 행사(순록 달리기) · this race 참가자 → do so(순록보다 빨리 달리기)가 가능한가? · Not really → 모두 그저 즐길 뿐")]
O8 = [('❶', [0, 1, 2], [[3], [4], [5, 6]], "Mr. Parker: How can we help you? → Eckels: 공룡을 보고 싶다, 가능한가? → Sure · 6천만 년 전 정글로 데려다줄 수 있다"),
      ('❶', [3, 4], [[5, 6], [7], [8]], "Sure · 데려다줄 수 있다 → Great, 지금(now) 데려가 줄 수 있나? → You're lucky, 10분 후 출발"),
      ('❷', [0, 1], [[2], [3], [4]], "기계가 움직임을 느낌 → 몇 분 뒤 멈춤 → 방금 도착했다(We've just arrived)"),
      ('❷', [4, 5], [[6], [7, 8], [9]], "the path → it(= 길)을 벗어나지 마라 → 아무것도 만지지 마라 · 실수로 죽일 수도 → A little change here(여기서의 작은 변화)가 미래에 큰일"),
      ('❸', [0, 1, 2], [[3], [4, 5, 6], [7, 8]], "Eckels: 신난다 → Travis: 조심, 침착, 어리석은 행동(anything foolish) 하지 마라 → 나는 바보(fool)가 아니다 · 길을 걷기 시작"),
      ('❹', [0, 1], [[2, 3], [4], [5]], "Eckels가 \"It ...\" 속삭이자 \"Sh!\" → 그래도 '거대하다, 무섭다'고 말함 → Sh ... quiet! 화를 냄"),
      ('❹', [6, 7], [[8, 9], [10, 11], [12, 13]], "돌아서서 뛰다가 길을 벗어남 → Travis: 길을 벗어나지 마! · 티라노가 Travis 소리를 들음 → 정적 · Then 갑자기 달려옴"),
      ('❺', [0], [[1, 2], [3, 4], [5, 6]], "당신이 우리를 위험에 빠뜨렸다, 길을 벗어났다 → 미안하지만 아무것도 안 죽였다, 진흙뿐 → 말없이 쳐다보다 마침내 '집에 갑시다'"),
      ('❻', [0, 1, 2, 3], [[4, 5], [6, 7], [8, 9, 10]], "방을 둘러봄, 간판 빼고 같음 → 간판 철자가 이상함 · 혼란 → Then TV, 대통령이 Keith가 아님 · 더 혼란(more confused)")]
T8 = [('❶', 4), ('❶', 8), ('❶', 10), ('❷', 3), ('❷', 6), ('❸', 7), ('❹', 9), ('❹', 11), ('❺', 3), ('❻', 6), ('❻', 7)]
OPT = ['(A) - (C) - (B)', '(B) - (A) - (C)', '(B) - (C) - (A)', '(C) - (A) - (B)', '(C) - (B) - (A)']
def E(s): return html.escape(s, quote=False)
def ord_item(S, o, target):
    m, intro, chunks, clue = o; b = S[m]; b = body(S, m)
    seq = OPT[target].replace(' ', '').split('-')   # 정답 순서에 놓일 이름표들
    lab = {seq[k]: chunks[k] for k in range(3)}
    txt = lambda ix: ' '.join(b[i][0] for i in ix); ko = lambda ix: ' '.join(b[i][1] for i in ix)
    bodyh = '<div class="wbox"><p>%s</p></div>' % E(txt(intro)) + ''.join('<p>%s %s</p>' % (L, E(txt(lab[L]))) for L in ('(A)', '(B)', '(C)'))
    ex = '정답 ▶ %s %s\n이유 ▶ %s\n주어진 글 ▶ %s\n' % (C[target], OPT[target], clue, ko(intro)) + '\n'.join('%s ▶ %s' % (L, ko(lab[L])) for L in seq)
    ex += '\n포인트 ▶ 대명사(it·them·this)가 가리키는 말, 연결어(So·Then·also), 질문 ↔ 대답 짝을 찾아 이어요.'
    return {'src': '%s 본문 %s · 글의 순서' % ('7과' if S is S7 else '8과', m), 'stem': '주어진 글 다음에 이어질 글의 순서로 가장 적절한 것은?', 'body': bodyh, 'opts': OPT[:], 'ans': target, 'ex': ex}
def ins_test(x, lesson):
    g = x['lines'][x['given']]; rest = [l for j, l in enumerate(x['lines']) if j != x['given']]
    bodyh = '<div class="wbox"><p>%s</p></div><p>%s</p>' % (E(g), ' '.join('%s ( %s )' % (E(l), C[j]) for j, l in enumerate(rest)))
    ex = x['ex'] + '\n주어진 문장 해석 ▶ %s\n포인트 ▶ 주어진 문장의 대명사·연결어가 가리키는 말이 바로 앞에, 이어지는 말이 바로 뒤에 오는 곳' % x['ko']
    return {'src': '%s 본문 %s · 문장 삽입' % (lesson, x['m']), 'stem': '글의 흐름으로 보아, 주어진 문장이 들어가기에 가장 적절한 곳은?', 'body': bodyh, 'opts': list(C), 'ans': x['given'] - 1, 'ex': ex}
def test(tid, title, short, items):
    out = []
    for n, it in enumerate(items, 1):
        it = dict(it, n=n, en=True, ctx='', pts=5, words=[], kos=[]); out.append(it)
    assert len(out) == 20
    return {'id': tid, 'title': title, 'short': short, 'school': '중2 동아(윤정미)', 'minutes': 30, 'items': out}
tg7 = [1, 3, 0, 4]; tg8 = [2, 0, 4, 3, 1, 2, 4, 0, 3]
it7 = [ord_item(S7, o, t) for o, t in zip(O7, tg7)] + [ins_test(x, '7과') for x in IT7]
key8 = {(m, i) for m, i in T8}; sel8 = [x for x, (m, i, _) in zip(IT8, I8) if (m, i) in key8]; assert len(sel8) == 11
it8 = [ord_item(S8, o, t) for o, t in zip(O8, tg8)] + [ins_test(x, '8과') for x in sel8]
TESTS = [test('m2oi-7', '순서·삽입 실전 7과 (본문 4개 축제)', '순서·삽입 7과', it7), test('m2oi-8', '순서·삽입 실전 8과 (본문 시간 여행·공룡)', '순서·삽입 8과', it8)]
print('삽입 DAY', len(IT7), len(IT8), '· 시험 정답', [''.join(C[i['ans']] for i in t['items']) for t in TESTS])
if 'emit' in sys.argv:
    od7 = order_day('od7', '7과 본문 · 문장 순서', S7, [['❶', '❷'], ['❸', '❹']], sum(len(S7[m]) for m in S7))
    od8 = order_day('od8', '8과 본문 · 문장 순서', S8, [['❶', '❷'], ['❸', '❹'], ['❺', '❻']], sum(len(S8[m]) for m in S8))
    oi7 = ins_day('oi7', '7과 본문 · 문장 삽입', IT7); oi8 = ins_day('oi8', '8과 본문 · 문장 삽입', IT8)
    oi7['passage'] = D['d1']['passage'] + D['d2']['passage']; oi8['passage'] = D['d3']['passage'] + D['d4']['passage']
    PK['days'] = [d for d in PK['days'] if d['id'] not in ('od7', 'oi7', 'od8', 'oi8')] + [od7, oi7, od8, oi8]
    for i, d in enumerate(PK['days']): d['name'] = 'DAY %d' % (i + 1)
    src = open(path, encoding='utf-8').read(); head = src[:src.index('window.PKG')]
    tail = src[src.index('/* WRAPUP-TESTS'):] if '/* WRAPUP-TESTS' in src else ''
    if '순서·삽입' not in head: head = head.rstrip('\n') + '\n/* 11/25: 7·8과 본문 순서·삽입 완벽 학습 DAY od7·oi7·od8·oi8 맨 끝 + 시험 m2oi-7·8 (gen/m2doi/gen.py) */\n'
    if tail: PK.pop('tests', None)
    write(PK, path, head)
    if tail:
        tail = re.sub(r'/\* M2OI-TESTS.*?/\* /M2OI-TESTS \*/\n?', '', tail, flags=re.S)
        ids = [t['id'] for t in TESTS]
        tail = tail.rstrip('\n') + '\n/* M2OI-TESTS: gen/m2doi/gen.py 로 만듦 (손으로 고치지 말 것) */\nwindow.PKG.tests = (window.PKG.tests || []).filter(function (t) { return %s.indexOf(t.id) < 0; }).concat(%s);\n/* /M2OI-TESTS */\n' % (json.dumps(ids), json.dumps(TESTS, ensure_ascii=False))
        open(path, 'a', encoding='utf-8').write(tail)
    print([d['name'] + ' ' + d['range'] for d in PK['days']][-4:], [len(it['lines']) for it in od7['steps'][0]['items']], [len(it['lines']) for it in od8['steps'][0]['items']])
