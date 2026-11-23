# 11/23 중산고1 끝판왕 7~10: 머리 리터럴 안의 boss2509g~j를 제자리 교체(순서·나머지 그대로)
import sys, json, subprocess
sys.path.insert(0, '/home/claude/srcrepo/generators')
from gencommon import js
BEFORE = '/home/claude/work/js1_before_hard.js'; DATA = '/home/claude/proj/data/h1-mock-2509.js'
get = lambda f: json.loads(subprocess.check_output(['node', '-e', "global.window={};require('%s');process.stdout.write(JSON.stringify(window.PKG.tests))" % f]))
old = {t['id']: t for t in get(BEFORE)}; new = {t['id']: t for t in get(DATA)}
s = open(BEFORE, encoding='utf-8').read()
for i in 'ghij':
    tid = 'boss2509' + i
    o = '  ' + js(old[tid], '  ')
    assert s.count(o) == 1, tid
    s = s.replace(o, '  ' + js(new[tid], '  '))
open(DATA, 'w', encoding='utf-8').write(s)
print('ok')
