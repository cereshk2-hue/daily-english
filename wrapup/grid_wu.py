# 11/24 Wrap-up 시험 안의 요약문 (A)/(B) 짝 문항 10개도 '교집합 = 정답' 패턴 제거 (끝판왕과 같은 규칙)
# 데이터 파일의 해당 문항만 손으로 고침(선택지·뜻·해설). Wrap-up을 다시 emit하면 이 스크립트를 다시 돌릴 것(같은 결과, 두 번 돌려도 그대로)
import json, re, subprocess, sys
D = '/home/claude/proj/data/%s.js'
# (파일, 시험 id, 문항 n): (바꿀 선택지 번호 0~4, 새 선택지, 새 뜻 또는 None, [(해설 바꿀 글, 새 글)…])
E = {
 ('h1-mock-2509', 'js2509b', 5): (3, 'weakening / erasing', '약하게 하다 / 지우다',
     [('→ converting 변환하다', '→ converting 변환하다\n오답 ▶ weakening(약하게 하다)은 확장과 반대, erasing(지우다)은 관찰할 수 있게 바꾸는 것과 반대')]),
 ('h1-mock-2509', 'js2509b', 14): (2, 'prohibited / doubt', '금지된 / 의심', [("② doubt는", "doubt는"), ("반대", "반대. prohibited(금지된)는 의무화(prescribes)와 반대")]),
 ('h1-mock-2509', 'js2509c', 5): (3, 'disproved / exploiting', '틀렸음을 증명했다 / 착취하는', [(' · doubted 의심했다', ''), ('assumed 추정했다(직접 보여 준 것과 다름)', 'assumed 추정했다(직접 보여 준 것과 다름) · disproved → exploiting은 두 칸 모두 반대')]),
 ('h1-mock-2509', 'js2509-3031', 17): (2, 'remains stable / rise above', '안정된 채로 있다 / ~보다 위로 올라가다', []),
 ('h1-mock-2509', 'js2509-3435', 19): (3, 'wars / failure', '전쟁 / 실패', [('wars·laws: 본문에 없다', 'wars: 본문에 없다'), ('·rejection(거부)', '')]),
 ('h1-ne-min-L3', 'jd-ne-l4', 13): (3, 'expensive / funding', None, [('funding(자금)은 언급 없음', 'expensive(비싼)는 cost-effective와 반대, funding(자금)은 언급 없음')]),
 ('h1-ne-min-L3', 'jd-ne-mix2', 3): (2, 'indifferent / glorified', None, []),
 ('h1-ne-min-L3', 'jd-ne-mix2', 20): (2, 'Olympic Mascots of Asia / How to Recycle Plastic at Home', None, [('①③ 일부 소재 ④ 3과 제목이 좁다', '① 일부 소재 ③ 두 제목 모두 좁다 ④ 3과 제목이 좁다')]),
 ('h2-mock-2609-angok', 'ag2609-3034', 9): (2, 'afraid / difficult', '두려워하는 / 어려운', [('difficult·slow·costly는', 'difficult·slow는'), (' / forced(강요된)는 스스로 허락한 것과 다름', '')]),
 ('h2-mock-2609-jungsan', 'js2609-2930', 18): (2, 'afraid / difficult', '두려워하는 / 어려운', [('difficult·slow·costly는', 'difficult·slow는'), (' / forced(강요된)는 스스로 허락한 것과 다름', '')]),
}
# 두 번째 고침이 필요한 문항(격자 + 다른 낱말 하나): 선택지 두 개 바꿈
E2 = {
 ('h1-mock-2509', 'js2509-3031', 17): (4, 'accelerates / sink below', '가속한다 / ~ 아래로 가라앉다',
     [('·move away from(멀어지다): 기준선', ': 기준선'), ('remains stable(안정된 채로 있다): 오르내림이 있다는 말과 반대', 'remains stable(안정된 채로 있다)·accelerates(가속한다): 오르내림이 있다는 말과 반대')]),
 ('h1-ne-min-L3', 'jd-ne-mix2', 3): (1, 'hostile / criticized', None, [('consistent 한결같은 · glorify 미화하다', 'glorify 미화하다 · criticize 비판하다')]),
}
def leak(opts, ans):
    pr = [o.split(' / ') for o in opts]
    from collections import Counter
    ca, cb = Counter(p[0] for p in pr), Counter(p[1] for p in pr)
    top = [i for i, p in enumerate(pr) if ca[p[0]] == max(ca.values()) and cb[p[1]] == max(cb.values())]
    return len(top) == 1 and top[0] == ans
def find_items(s, tid, n):
    """데이터 파일 글자에서 그 시험의 n번 문항 객체 글자 범위 찾기 (json 블록 또는 js 리터럴)"""
    i = s.index("'%s'" % tid) if ("id: '%s'" % tid) in s else s.index('"%s"' % tid)
    return i
for f in sorted({k[0] for k in E}):
    path = D % f; s = open(path, encoding='utf-8').read()
    for key in [k for k in E if k[0] == f]:
        _, tid, n = key
        for spec in [E[key]] + ([E2[key]] if key in E2 else []):
            k, new, ko, exs = spec
            st = find_items(s, tid, n)
            data = json.loads(subprocess.check_output(['node', '-e', "global.window={};require('%s');const t=window.PKG.tests.find(t=>t.id=='%s');process.stdout.write(JSON.stringify(t.items.find(i=>i.n==%d)))" % (path, tid, n)]))
            def esc(x, q): return json.dumps(x, ensure_ascii=False)[1:-1] if q == '"' else x.replace('\\', '\\\\').replace("'", "\\'").replace('\n', '\\n')
            q = '"' if s.find(esc(data['ex'], '"'), st) >= 0 and '"%s"' % tid in s else "'"
            anc = s.index(esc(data['ex'], q), st)                   # 이 문항의 해설 위치(고유)
            old = data['opts'][k]
            if old == new: continue
            o1 = q + esc(old, q) + q; j = s.rfind(o1, st, anc); assert j > 0, (key, old)
            s = s[:j] + q + esc(new, q) + q + s[j + len(o1):]
            anc = s.index(esc(data['ex'], q), st)
            if ko and data.get('okos'):
                o1 = q + esc(data['okos'][k], q) + q; j = s.find(o1, anc); assert j > 0, (key, 'okos')
                s = s[:j] + q + esc(ko, q) + q + s[j + len(o1):]
            ex = data['ex']
            for a, b in exs:
                assert a in ex, (key, a); ex = ex.replace(a, b, 1)
            s = s[:anc] + esc(ex, q) + s[anc + len(esc(data['ex'], q)):]
    open(path, 'w', encoding='utf-8').write(s)
    # 검사
    tests = json.loads(subprocess.check_output(['node', '-e', "global.window={};require('%s');process.stdout.write(JSON.stringify(window.PKG.tests))" % path]))
    for key in [k for k in E if k[0] == f]:
        it = next(i for t in tests if t['id'] == key[1] for i in t['items'] if i['n'] == key[2])
        assert not leak(it['opts'], it['ans']) and len(set(it['opts'])) == 5, (key, it['opts'])
        print(key, ' '.join('①②③④⑤'[i] + o + ('✓' if i == it['ans'] else '') for i, o in enumerate(it['opts'])))
