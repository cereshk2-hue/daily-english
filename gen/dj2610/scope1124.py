# 11/24 대진고2 시험범위 수정: 10월 모고 26번 제외(DAY q26 삭제) + 우리말→영작(본문 스크램블)은 교과서 본문에서만 → 모고 DAY(q*)에서 scramble 단계 삭제
import sys, json, subprocess, re
sys.path.insert(0, '/home/claude/work/gen'); sys.path.insert(0, '/home/claude/srcrepo/generators')
from gencommon import write
path = '/home/claude/proj/data/h2-ne-oh-L3.js'
PK = json.loads(subprocess.check_output(['node', '-e', "global.window={};require('%s');process.stdout.write(JSON.stringify(window.PKG))" % path]))
PK.pop('tests', None)
PK['days'] = [d for d in PK['days'] if d['id'] != 'q26']
for d in PK['days']:
    if re.match(r'q\d+$', d['id']): d['steps'] = [s for s in d['steps'] if s['type'] != 'scramble']
for i, d in enumerate(PK['days']): d['name'] = 'DAY %d' % (i + 1)
PK['unit'] = PK['unit'].replace('20~24·26·29~42번', '20~24·29~42번')
src = open(path, encoding='utf-8').read(); head = src[:src.index('window.PKG')]
tail = src[src.index('/* WRAPUP-TESTS'):]
if '11/24' not in head: head = head.rstrip('\n') + '\n/* 11/24: 시험범위 수정 — 26번 제외(q26 삭제), 모고 DAY 본문 스크램블(우리말→영작) 삭제(영작은 교과서 본문에서만). gen/dj2610/scope1124.py */\n'
write(PK, path, head)
open(path, 'a', encoding='utf-8').write(tail)
print(len(PK['days']), PK['unit'])
