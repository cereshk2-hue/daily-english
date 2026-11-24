# 11/24 대진고2 능률(오선영) 3·4과 본문 영작 (우리말 → 영작, 본문 문장 그대로가 정답) — 선생님: "한국어로 해석된 거 영작 문제는 본문에서만 나옴"
# 과마다 10문항 × 10점. 출력: ① 앱 Wrap-up 탭 시험 2개(dj-yj3·dj-yj4, /* YJ-TESTS */ 블록) ② PDF 시험지·정답·화면용(과마다) — print/jdsw_make.py 형식
import re, html, json, subprocess, sys, os
OUT = '/home/claude/out/djyj/'; os.makedirs(OUT, exist_ok=True)
DATA = '/home/claude/proj/data/h2-ne-oh-L3.js'
E = html.escape
def I(tag, gram, ko, words, ans, pts, start='', alt=(), extra=()):
    return dict(tag=tag, gram=gram, ko=ko, words=words, ans=ans, pts=pts, start=start, alt=list(alt), extra=list(extra))
L3 = [
 I('본문 ❶', '원급 비교 not as ~ as · 이유의 접속사 as · 현재분사 수식', '집단 의사 결정은 다른 의견을 가진 수많은 목소리를 수반하기 때문에 우리의 개인적인 선택들만큼 간단하지 않다.',
   ['simple', 'as', 'involve', 'numerous voices', 'differ'], 'Group decision-making is not as simple as our personal choices, as it involves numerous voices with differing opinions.',
   ['not as + 원급 + as(~만큼 …하지 않은)', '이유의 접속사 as + 주어 it + 3인칭 단수 involves', 'differ → differing(현재분사: 서로 다른)'], start='Group decision-making'),
 I('본문 ❶', 'to부정사(목적) · make + 목적어 + 비교급 형용사 · 수동태', '투표는 흔히 집단 의사 결정을 더 공정하고 더 효율적으로 만들기 위해 사용된다.',
   ['use', 'make', 'fair', 'efficient'], 'Voting is often used to make group decisions fairer and more efficient.',
   ['수동태 is often used(빈도부사 위치: be동사 뒤)', 'to부정사 목적 to make', 'make + 목적어 + 형용사 비교급 fairer and more efficient(fair → fairer, efficient → more efficient)']),
 I('본문 ❷', 'encourage + 목적어 + to부정사 · not A but B · -thing + 형용사', '그녀는 그들에게 익숙한 투표 방법을 사용하지 말고, 대신 다른 것을 시도해 보라고 권장했다.',
   ['encourage', 'not', 'use', 'try', 'familiar', 'different', 'instead'], 'She encouraged them not to use the familiar voting method, but to try something different instead.',
   ['encourage + 목적어 + to부정사', 'not to A, but to B(to부정사 병렬)', '-thing 대명사 + 형용사: something different']),
 I('본문 ❷', '명사절 접속사 if(~인지) · 시제 일치(will → would)', '모든 자치회 구성원들은 각각 다른 방법이 서로 다른 결과를 낼지 알아내는 것을 궁금해했다.',
   ['curious', 'find out', 'if', 'will', 'yield'], 'The entire council was curious to find out if the different methods would yield different results.',
   ['be curious + to부정사', 'find out의 목적어 if절(~인지)', '주절이 과거 was → will을 would로(시제 일치)'], start='The entire council'),
 I('본문 ❹', '수동태 · 복합관계대명사 whichever · 수 일치', '투표자들에게는 여러 가지 선택지가 주어지고, 어떤 것이든 가장 많은 1지망 표를 얻은 것이 이긴다.',
   ['give', 'whichever', 'get', 'win', 'most'], 'Voters are given several options, and whichever gets the most first-preference votes wins.',
   ['수여동사 수동태 are given + 직접목적어', 'whichever(~하는 것은 무엇이든) = 단수 취급 → gets', '명사절 주어 whichever ~ votes + 단수 동사 wins'], extra=['first-preference는 1단어']),
 I('본문 ❹', 'neither A nor B · 수 일치 · 수동태', '2지망도 3지망도 둘 다 전혀 중요하지 않으므로, 그것들은 무시된다.',
   ['neither', 'nor', 'matter', 'ignore'], 'Neither the second nor third preference matters at all, so they are ignored.',
   ['neither A nor B(A도 B도 아닌)', 'neither A nor B 주어 → B(third preference, 단수)에 수 일치 → matters', 'ignore → 수동태 are ignored']),
 I('본문 ❺', 'to부정사의 의미상 주어 for + 목적격 · need to · more than', '어떤 선택지가 1차 집계에서 승리하기 위해서는, 1지망 표의 50% 이상을 얻어야 한다.',
   ['for', 'win', 'need', 'get', 'more than'], 'For an option to win in the first round, it needs to get more than 50% of the first-preference votes.',
   ['의미상 주어 for an option + to win(목적)', 'it needs to get(주어 it → needs)', 'more than 50% of ~(~의 50% 이상)'], extra=['50%와 first-preference는 각 1단어']),
 I('본문 ❺', 'allow + 목적어 + to부정사 · 비교급 than', '그것은 때때로 2지망 표가 1지망 표보다 더 큰 영향력을 갖게 하기도 한다.',
   ['allow', 'have', 'great', 'influence'], 'It sometimes allows second-preference votes to have a greater influence than first-preference votes.',
   ['allow + 목적어 + to부정사', 'great → greater(비교급) + than', '빈도부사 sometimes는 일반동사 앞'], extra=['second-preference, first-preference는 각 1단어']),
 I('본문 ❼', '가주어 It ~ that · 동명사 주어 + 단수 동사', '이상적인 투표 방법을 선택하는 것은 복잡하고 도전적인 일이라는 것은 분명하다.',
   ['obvious', 'that', 'choose', 'ideal', 'challenge'], 'It is obvious that choosing an ideal voting method is a complex and challenging task.',
   ['가주어 It + 진주어 that절', '동명사 주어 choosing ~ method → 단수 동사 is', 'challenge → challenging(형용사)']),
 I('본문 ❼', '수동태 · not A but B(to부정사 병렬) · make + 목적어 + 형용사 · help + 목적어 + 동사원형', '이러한 모든 노력은 의사 결정을 어렵고 비효율적으로 만들기 위한 것이 아니라, 우리가 사회로서 더 나은 결정을 내릴 수 있게 돕기 위해 고안된 것이다.',
   ['design', 'not', 'make', 'difficult', 'inefficient', 'help', 'good'], 'All of these efforts are designed not to make decision-making difficult and inefficient, but to help us make better decisions as a society.',
   ['be designed + to부정사', 'not to A, but to B', 'make + 목적어 + 형용사(difficult and inefficient) / help + 목적어 + 동사원형(make)', 'good → better'], start='All of these efforts', extra=['decision-making은 1단어']),
]
L4 = [
 I('본문 ❶', '분사구문(결과) · 부사 수식', '스터디 그룹 모임에 가는 길에, Liz는 실수로 그녀의 노트북을 길에 떨어뜨려 그것을 심각하게 손상시켰다.',
   ['accidentally', 'drop', 'seriously', 'damage'], 'On her way to a study group meeting, Liz accidentally dropped her laptop on the street, seriously damaging it.',
   ['on one\'s way to ~(~로 가는 길에)', '과거 dropped', '결과의 분사구문 , seriously damaging it(그래서 손상시켰다)'], start='On her way to a study group meeting'),
 I('본문 ❶', '사역동사 have + 목적어 + 과거분사 · hesitate to-v · 현재진행', '그녀는 그것을 수리할 수 있지만, 그렇게 하기를 망설이고 있다.',
   ['have', 'repair', 'hesitate', 'do so'], 'She can have it repaired, but she is hesitating to do so.',
   ['have + 목적어(it) + 과거분사(repaired): 노트북이 \'수리되는\' 것', 'hesitate + to부정사', '현재진행 is hesitating']),
 I('본문 ❶', '동명사 주어 병렬 · seem like + 명사 · 비교급', '이 경우에 오래된 노트북은 버리고 새로운 것을 구입하는 것이 더 합리적인 선택처럼 보일 수 있다.',
   ['get rid of', 'purchase', 'seem like', 'reasonable'], 'In this case, getting rid of the old one and purchasing a new one might seem like a more reasonable option.',
   ['동명사 주어 getting rid of ~ and purchasing ~ (병렬)', 'might seem like + 명사(~처럼 보일 수 있다)', 'a more reasonable option(비교급)'], start='In this case'),
 I('본문 ❷', '미래완료 will have p.p. · 과거분사 후치 수식', '전문가들은 2030년에는 매년 발생하는 전자 쓰레기의 양이 단 16년 만에 두 배가 될 것으로 예측한다.',
   ['predict', 'generate', 'annually', 'double'], 'Experts predict that by 2030, the amount of e-waste generated annually will have doubled in just 16 years.',
   ['by 2030(그때까지) → 미래완료 will have doubled', 'e-waste generated annually(과거분사 후치 수식)', '주어 the amount → 단수'], extra=['2030, e-waste는 각 1단어']),
 I('본문 ❸', '목적격 관계대명사 생략 · 보어 that절 · too ~ to', '많은 사람이 그들의 고장 난 장치들을 버리는 한 가지 이유는 그것들이 수리하기 너무 어렵기 때문이다.',
   ['reason', 'dispose of', 'damage', 'too', 'repair'], 'One reason many people dispose of their damaged devices is that they are too difficult to repair.',
   ['One reason (that/why) many people ~: 관계사 생략', '주어 One reason → is + 보어 that절', 'damage → damaged(고장 난) / too difficult to repair']),
 I('본문 ❸', '요구 동사 require + that + (should) 동사원형 · 수동', '그것의 제조사가 그것을 고치려면 공식 수리소로 가져올 것을 요구할 수도 있다.',
   ['require', 'that', 'bring', 'fix'], 'Its manufacturer may require that it be brought to an official service center to be fixed.',
   ['require that + 주어 + (should) 동사원형 → it be brought(is ❌)', '장치가 \'가져와지는\' 것 → 수동 be brought', 'to be fixed(목적, 수동 부정사)'], start='Its manufacturer'),
 I('본문 ❸', '가주어 It ~ for + 의미상 주어 + to부정사 · 의문사 + to부정사 · 과거분사 후치 수식', '소비자들이 그들의 물건을 고치는 방법에 대한 설명이나 수리를 완료하기 위해 필요한 부품들을 얻지 못하는 것은 흔하다.',
   ['common', 'for', 'unable', 'acquire', 'how', 'need'], 'It is common for consumers to be unable to acquire the instructions for how to fix their items or the parts needed to complete repairs.',
   ['가주어 It + 의미상 주어 for consumers + to be unable to', 'how to fix(고치는 방법)', 'the parts needed to complete repairs(과거분사 후치 수식)']),
 I('본문 ❹', 'let + 목적어 + 동사원형 · 간접의문문 how + 부사 · 조동사 수동', '그 지수는 소비자들이 제품을 구입하기 전에 그것이 얼마나 쉽게 수리될 수 있는지 알 수 있게 해 준다.',
   ['let', 'see', 'how', 'easily', 'repair'], 'The index lets consumers see how easily the product can be repaired before they purchase it.',
   ['사역동사 let + 목적어 + 동사원형 see(주어 The index → lets)', '간접의문문 how easily + 주어 + 동사', '조동사 수동 can be repaired']),
 I('본문 ❺', 'with + 목적어 + 현재분사 · expect to-v · 비교급', '더 적은 전자 및 전기 제품들이 쓰레기 매립지에 이르게 되면서, 프랑스는 가까운 미래에 더 지속 가능한 사회로 변화할 것을 기대할 수 있다.',
   ['few', 'end up', 'expect', 'make a transition', 'sustainable'], 'With fewer electronic and electrical items ending up in its landfills, France can expect to make a transition to a more sustainable society in the near future.',
   ['with + 목적어(fewer ~ items) + 현재분사(ending up): ~하면서', 'few → fewer(비교급)', 'expect + to부정사 / a more sustainable society'], start='With'),
 I('본문 ❼', '가정법 과거 · 수동 · 전치사 to + 동명사 병렬', '만약 그랬다면, 그녀의 선택지는 비싼 수리를 위해 비용을 지불하거나 노트북을 버리고 새것을 사는 것으로 제한되지는 않았을 것이다.',
   ['be', 'limit', 'pay for', 'throw away', 'buy'], 'If that were the case, her options wouldn\'t be limited to paying for expensive repairs or throwing away her laptop and buying a new one.',
   ['가정법 과거 If + 주어 + were, 주어 + would + 동사원형', '수동 be limited to + 동명사(to는 전치사)', 'paying ~ or throwing ~ and buying ~(동명사 병렬)'],
   alt=["If that were the case, her options would not be limited to paying for expensive repairs or throwing away her laptop and buying a new one."], extra=["wouldn't는 1단어"]),
]
def wc(s): return len(s.replace(' ,', ',').split())
def cond(q):
    c = []
    if q['start']: c.append('%s(으)로 시작할 것' % q['start'])
    c.append(', '.join(q['words']) + '을(를) 모두 쓰되 필요하면 형태를 바꿀 것')
    c.append('%d단어로 쓸 것' % wc(q['ans']) + (' (' + ' · '.join(q['extra']) + ')' if q['extra'] else ''))
    return c

# ── 검사: 정답은 본문 문장(또는 본문 문장의 한 부분) 그대로 ──
PK = json.loads(subprocess.check_output(['node', '-e', "global.window={};require('%s');process.stdout.write(JSON.stringify(window.PKG))" % DATA]))
BODY = {L: ' '.join(l[1] for d in PK['days'] if d['id'] in ids for l in d['passage']).replace('’', "'").replace('“', '"').replace('”', '"')
        for L, ids in (('3', ('d1', 'd2', 'd3')), ('4', ('p1', 'p2', 'p3', 'p4')))}
for L, QS in (('3', L3), ('4', L4)):
    assert len(QS) == 10
    for q in QS:
        a = q['ans'].rstrip('.')
        assert a in BODY[L] or (a[0].lower() + a[1:]) in BODY[L], (L, q['ans'])
        for w in q['words']: assert w.split()[0][:4].lower() in q['ans'].lower() or w in ('will', 'great', 'good', 'few', 'be', 'fair', 'win', 'buy', 'do so', 'bring', 'give', 'get', 'matter', 'make'), (w, q['ans'])

# ── 앱 시험 ──
def variants(a):
    out = {a}
    out.add(a.replace(',', ''))
    return sorted(x for x in out if x != a)
def app_test(L, QS):
    items = []
    for i, q in enumerate(QS, 1):
        c = cond(q)
        body = ('<div class="wbox"><p>%s</p></div>' % E(q['ko'])) + '<div class="wcond"><b>&lt;조건&gt;</b> ' + ' · '.join(E(x) for x in c) + '</div>'
        ans = [q['ans']] + q['alt']
        items.append({'n': '서술형 %d' % i, 'src': q['tag'], 'pts': 10, 'kind': 'write',
                      'stem': '다음 우리말을 &lt;조건&gt;에 맞게 영작하시오. <span class="pt">[10점]</span>', 'body': body,
                      'blanks': [{'label': '', 'pts': 10, 'ans': ans, 'chk': sorted({v for a in ans for v in variants(a)}), 'note': True,
                                  's': '___', 'v': q['ko'] + ' / ' + ' · '.join(c)}],
                      'model': q['ans'],
                      'ex': '본문 문장 그대로 ▶ %s\n문법 ▶ %s\n채점 ▶ 철자·형태·어순이 모두 맞아야 10점(대소문자·끝 마침표는 상관없음). 쉼표만 빠진 답은 선생님이 확인해요.' % (q['ans'], ' / '.join(q['pts']))})
    return {'id': 'dj-yj%s' % L, 'title': '능률 %s과 본문 영작 (우리말 → 영작)' % L, 'short': '%s과 본문 영작' % L, 'school': '대진고 2학년', 'minutes': 30, 'items': items}

# ── PDF (jdsw_make 형식) ──
sys.path.insert(0, '/home/claude/srcrepo/print')
import jdsw_make as J
def toQ(QS):
    return [dict(tag=q['tag'], gram=q['gram'], title='다음 우리말을 &lt;조건&gt;에 맞게 영작하시오.', box=[E(q['ko'])], cond=[E(x) for x in cond(q)],
                 parts=[('', 2 if wc(q['ans']) > 14 else 1)], ans=[E(q['ans'])] + [E(a) + ' (도 정답)' for a in q['alt']], pts=q['pts']) for q in QS]
LT = {'3': 'Lesson 3 Life Is a Sum of Choices', '4': 'Lesson 4 Create a Greener Tomorrow'}
def pdfs():
    from playwright.sync_api import sync_playwright
    with sync_playwright() as p:
        b = p.chromium.launch(); pg = b.new_page()
        for L, QS in (('3', L3), ('4', L4)):
            J.Q = toQ(QS)
            docs = {'시험지': J.a4(False), '정답': J.a4(True), '화면용': J.screen()}
            for name, doc in docs.items():
                doc = (doc.replace('저동고1 3·4과 본문 서술형', '대진고2 %s과 본문 영작' % L)
                          .replace('공통영어2 능률(민병천) Lesson 3 A Timeless Symbol of Korea · Lesson 4 Looking to Nature for Help · 10문항', '영어Ⅱ 능률(오선영) %s · 우리말 → 영작 10문항 · 정답은 본문 문장 그대로' % LT[L])
                          .replace('본문에서 문법이 가장 많이 걸린 문장만 골랐어요.', '시험에 나오는 영작은 본문에서만 나와요. 본문 문장을 그대로 떠올려 쓰세요.')
                          .replace('3·4과 본문 서술형', '%s과 본문 영작' % L).replace('저동고 1학년 · 능률(민병천) Lesson 3·4 · 10문항', '대진고 2학년 · 능률(오선영) Lesson %s · 10문항' % L)
                          .replace('서술형 ', '영작 '))
                hp = '/home/claude/work/djyj_%s_%s.html' % (L, name); open(hp, 'w', encoding='utf-8').write(doc)
                pg.goto('file://' + hp); pg.wait_for_timeout(1200)
                fn = OUT + '대진고2_%s과_본문영작_%s.pdf' % (L, name)
                if name == '화면용': pg.pdf(path=fn, width='1280px', height='720px', print_background=True)
                else: pg.pdf(path=fn, format='A4', print_background=True, prefer_css_page_size=True)
        b.close()

def emit():
    tests = [app_test('3', L3), app_test('4', L4)]
    ids = [t['id'] for t in tests]
    blk = ('/* YJ-TESTS: print/djyj_make.py 로 만듦 (손으로 고치지 말 것) */\nwindow.PKG.tests = (window.PKG.tests || []).filter(function (t) { return %s.indexOf(t.id) < 0; }).concat(%s);\n/* /YJ-TESTS */\n'
           % (json.dumps(ids), json.dumps(tests, ensure_ascii=False)))
    js = open(DATA, encoding='utf-8').read()
    if '/* YJ-TESTS' in js: js = re.sub(r'/\* YJ-TESTS.*?/\* /YJ-TESTS \*/\n', lambda m: blk, js, flags=re.S)
    else: js = js.rstrip('\n') + '\n\n' + blk
    open(DATA, 'w', encoding='utf-8').write(js)
    print('emit', ids, [len(t['items']) for t in tests])

if __name__ == '__main__':
    for L, QS in (('3', L3), ('4', L4)):
        for i, q in enumerate(QS, 1): print(L, i, wc(q['ans']), q['ans'][:60])
    if 'emit' in sys.argv: emit()
    if 'pdf' in sys.argv: pdfs()
