# 11/13 중산고2 9월 학평 31~42번 DAY 6~16 붙이기 (gen_js2609c.py → new_3142.json). 기존 DAY 1~5·시험 블록(Wrap-up·끝판왕)은 그대로 둠
import json, subprocess, sys
sys.path.insert(0, '/home/claude/srcrepo/generators')
from gencommon import write
F = '/home/claude/proj/data/h2-mock-2609-jungsan.js'
NUMS = ['31', '32', '33', '34', '35', '36', '37', '38', '39', '40', '41~42']
src = open(F, encoding='utf-8').read()
cut = src.index('/* WRAPUP-TESTS')
head, tail = src[:cut], src[cut:]
P = json.loads(subprocess.check_output(['node', '-e', 'global.window={};eval(require("fs").readFileSync(0,"utf8"));process.stdout.write(JSON.stringify(window.PKG))'], input=head.encode()))
new = {str(x['num']): x for x in json.load(open('/home/claude/work/js2d/new_3142.json', encoding='utf-8'))}
ONLY = sys.argv[1:] == ['--partial']
days = [d for d in P['days'] if int(d['id'][1:]) <= 5]
for i, n in enumerate(NUMS):
    if n not in new:
        assert ONLY, '아직 없는 번호: ' + n
        continue
    x = new[n]
    days.append({'id': 'd%d' % (i + 6), 'name': 'DAY %d' % (i + 6), 'range': n + '번', 'story': '%s번 · %s' % (n, x['kind']), 'passage': x['passage'], 'steps': x['steps']})
P['days'] = days
P['unit'] = '19~24 · 26~27 · 29~42번'
P['titleKo'] = '2026년 9월 고2 학력평가 · 중산고 내신 범위'
for d in days[5:]:
    for n in [d['range'].replace('번', '')]: P['legacy']['map'].setdefault('q' + n.split('~')[0], [d['id']])
write(P, F, "/* 고2 2026년 9월 학력평가 · 중산고 내신 범위 19~24 · 26~27 · 29~42번\n"
      "   DAY 1~5: 두 문항씩(split/combine2.py) · DAY 6~16: 31~42번 한 문항씩(gen_js2609c.py → split/add_3142.py, 대의 파악·어휘 비틀기 중심, 서술형 없음) */\n")
open(F, 'a', encoding='utf-8').write(tail)
print([(d['name'], d['range'], len(d['steps'])) for d in days])
