# 11/24 21:50 Wrap-up 요약문 짝 문항 10개: 격자 + 1 모양은 그대로(같은 낱말), 정답 자리를 다섯 자리 중 무작위로
# (격자 안일 수도, 혼자 떨어진 짝일 수도) → '한 번만 나온 짝은 오답' 규칙도 없앰. 정답 번호(ans)는 그대로, 나머지 자리만 섞음
# grid_wu.py 다음에 돌림(Wrap-up을 다시 emit하면 grid_wu.py → grid_wu2.py 순서로)
import json, subprocess, random, re
from collections import Counter
D = '/home/claude/proj/data/%s.js'
K = [('h1-mock-2509', 'js2509b', 5), ('h1-mock-2509', 'js2509b', 14), ('h1-mock-2509', 'js2509c', 5), ('h1-mock-2509', 'js2509-3031', 17),
     ('h1-mock-2509', 'js2509-3435', 19), ('h1-ne-min-L3', 'jd-ne-l4', 13), ('h1-ne-min-L3', 'jd-ne-mix2', 3), ('h1-ne-min-L3', 'jd-ne-mix2', 20),
     ('h2-mock-2609-angok', 'ag2609-3034', 9), ('h2-mock-2609-jungsan', 'js2609-2930', 18)]
EXFIX = {('h1-ne-min-L3', 'jd-ne-mix2', 20): None}   # 번호가 든 해설은 아래에서 새로 씀
R = random.Random(2150)
T = [(0, 0), (0, 1), (1, 0), (1, 1), (2, 2)]
def get(path, tid, n):
    return json.loads(subprocess.check_output(['node', '-e', "global.window={};require('%s');const t=window.PKG.tests.find(t=>t.id=='%s');process.stdout.write(JSON.stringify(t.items.find(i=>i.n==%d)))" % (path, tid, n)]))
def lit(arr, q):
    if q == '"': return json.dumps(arr, ensure_ascii=False)
    return '[' + ', '.join("'" + x.replace('\\', '\\\\').replace("'", "\\'") + "'" for x in arr) + ']'
CHOSEN = {(1, 0): 0, (2, 1): 0, (0, 2): 0, (3, 3): 0, (0, 4): 0}
for key in K:
    f, tid, n = key; path = D % f; s = open(path, encoding='utf-8').read()
    it = get(path, tid, n); P = [tuple(o.split(' / ')) for o in it['opts']]; ans = it['ans']; a, b = P[ans]
    if it.get('_wu2'): continue
    ca, cb = Counter(p[0] for p in P), Counter(p[1] for p in P)
    WA = sorted({p[0] for p in P} - {a}, key=lambda w: -ca[w]); WB = sorted({p[1] for p in P} - {b}, key=lambda w: -cb[w])
    assert len(WA) == 2 and len(WB) == 2, (key, P)
    ci = R.randrange(5); cx, cy = T[ci]
    ia = [x for x in (0, 1, 2) if x != cx]; ib = [y for y in (0, 1, 2) if y != cy]
    MA = {cx: a, ia[0]: WA[0], ia[1]: WA[1]}; MB = {cy: b, ib[0]: WB[0], ib[1]: WB[1]}
    new = [(MA[x], MB[y]) for x, y in T]
    wrong = [p for i, p in enumerate(new) if i != ci]; R.shuffle(wrong); wrong.insert(ans, (a, b))
    NO = ['%s / %s' % p for p in wrong]
    assert sorted(set(w for p in wrong for w in p)) == sorted(set(w for p in P for w in p)), key
    # 뜻(okos)
    NK = None
    if it.get('okos'):
        MK = {}
        for p, k in zip(P, it['okos']):
            ka, kb = k.split(' / '); MK[('A', p[0])] = ka; MK[('B', p[1])] = kb
        NK = ['%s / %s' % (MK[('A', p[0])], MK[('B', p[1])]) for p in wrong]
    # 데이터 글자 교체: 이 시험 시작 뒤, 이 문항 해설 앞의 옛 opts 배열
    q = '"' if ('"%s"' % tid) in s else "'"
    st = s.index(q + tid + q)
    exs = json.dumps(it['ex'], ensure_ascii=False)[1:-1] if q == '"' else it['ex'].replace('\\', '\\\\').replace("'", "\\'").replace('\n', '\\n')
    anc = s.index(exs, st)
    old = lit(it['opts'], q); j = s.rfind(old, st, anc); assert j > 0, (key, 'opts')
    s = s[:j] + lit(NO, q) + s[j + len(old):]
    if NK:
        anc = s.index(exs, st); old = lit(it['okos'], q); j = s.find(old, anc); assert j > 0, (key, 'okos')
        s = s[:j] + lit(NK, q) + s[j + len(old):]
    if key in EXFIX:
        C = '①②③④⑤'
        tag = lambda pa: ''.join(C[i] for i, p in enumerate(wrong) if i != ans and pa(p))
        t3 = tag(lambda p: p[0] != a and p[1] != b and not (p[0] in WA and p[1] in WB and False))
        # 3과 제목이 틀린 것 / 4과 제목이 틀린 것으로 다시 씀
        A_wrong = tag(lambda p: p[0] != a and p[1] == b); B_wrong = tag(lambda p: p[0] == a and p[1] != b); both = tag(lambda p: p[0] != a and p[1] != b)
        newex = re.sub(r'\..*$', '', it['ex'].split('/ 4과')[0]) if False else None
        ex2 = re.sub(r'①③ 일부 소재 ③ 두 제목 모두 좁다 ④ 3과 제목이 좁다 ⑤ 4과 제목이 재활용에만 한정|① 일부 소재 ③ 두 제목 모두 좁다 ④ 3과 제목이 좁다 ⑤ 4과 제목이 재활용에만 한정',
                     ('%s 3과 제목이 좁거나 엉뚱함 ' % A_wrong if A_wrong else '') + ('%s 4과 제목이 좁거나 엉뚱함 ' % B_wrong if B_wrong else '') + ('%s 두 제목 모두 틀림' % both if both else ''), it['ex'])
        assert ex2 != it['ex'], it['ex']
        exn = json.dumps(ex2, ensure_ascii=False)[1:-1] if q == '"' else ex2.replace('\\', '\\\\').replace("'", "\\'").replace('\n', '\\n')
        j = s.index(exs, st); s = s[:j] + exn + s[j + len(exs):]
    open(path, 'w', encoding='utf-8').write(s)
    print(key, '정답 자리:', '격자 안' if ci < 4 else '혼자 떨어진 짝', ' '.join('①②③④⑤'[i] + o + ('✓' if i == ans else '') for i, o in enumerate(NO)))
