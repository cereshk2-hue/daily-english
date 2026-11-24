# 11/24 모든 고등 끝판왕 '교집합=정답' 패턴 제거 → 데이터 파일 안 끝판왕 시험만 제자리 교체 (순서·다른 시험 그대로)
# 각 *_build.py의 app_tests()(gridfix 적용) 결과를 BOSS-TESTS 블록(json) 또는 머리 리터럴(js 형식, 중산고1)에 넣음
import sys, json, re, subprocess, importlib
sys.path.insert(0, '/home/claude/srcrepo/wrapup'); sys.path.insert(0, '/home/claude/srcrepo/generators')
from gencommon import js
D = '/home/claude/proj/data/%s.js'
P = {'boss_build': 'h1-mock-2509', 'boss4_build': 'h1-mock-2509', 'boss2_build': 'h2-mock-2609-jungsan', 'boss5_build': 'h2-mock-2609-jungsan',
     'boss3_build': 'h2-mock-2609-angok', 'boss6_build': 'h2-ne-oh-L3', 'bossjd_build': 'h1-mock-2610-jeodong'}
sys.argv = ['x']
NEW = {}
for b, f in P.items():
    for t in importlib.import_module(b).app_tests(): NEW.setdefault(f, {})[t['id']] = t
for f, nt in NEW.items():
    path = D % f; s = open(path, encoding='utf-8').read()
    cur = {t['id']: t for t in json.loads(subprocess.check_output(['node', '-e', "global.window={};require('%s');process.stdout.write(JSON.stringify(window.PKG.tests))" % path]))}
    m = re.search(r'(/\* BOSS-TESTS[^\n]*\n.*?\.concat\()(.*?)(\);\n/\* /BOSS-TESTS \*/)', s, re.S)
    if m:
        arr = json.loads(m.group(2)); arr = [nt.get(t['id'], t) for t in arr]
        assert {t['id'] for t in arr} >= set(nt)
        s = s[:m.start(2)] + json.dumps(arr, ensure_ascii=False) + s[m.end(2):]
    else:
        for tid, t in nt.items():
            o = '  ' + js(cur[tid], '  ')
            assert s.count(o) == 1, tid
            s = s.replace(o, '  ' + js(t, '  '))
    open(path, 'w', encoding='utf-8').write(s)
    print(f, len(nt), 'tests')
