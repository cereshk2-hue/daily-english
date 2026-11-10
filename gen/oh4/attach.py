# 11/11 고2 능률(오선영) 4과 본문 DAY p1~p4 를 h2-ne-oh-L3 끝(3과 어휘 DAY 다음)에 붙임 → 이어서 gen_h2oh4full.py 로 k1~k3
import sys, json, subprocess, re
sys.path.insert(0, '/home/claude/work/gen'); sys.path.insert(0, '/home/claude/work/oh4/gen')
from gencommon import write
from build import build
path = '/home/claude/proj/data/h2-ne-oh-L3.js'
PK = json.loads(subprocess.check_output(['node', '-e', "global.window={};require('%s');process.stdout.write(JSON.stringify(window.PKG))" % path]))
base = [d for d in PK['days'] if not re.match(r'[pk]\d$', d['id'])]
PK['days'] = base + build()
for i, d in enumerate(PK['days']): d['name'] = 'DAY %d' % (i + 1)
PK.update({'unit': '영어Ⅱ Lesson 3 · 4', 'title': 'Life Is a Sum of Choices · Create a Greener Tomorrow', 'titleKo': '삶은 선택의 합 · 더 푸른 내일 만들기'})
src = open(path, encoding='utf-8').read(); head = src[:src.index('window.PKG')]
tail = src[src.index('/* WRAPUP-TESTS'):] if '/* WRAPUP-TESTS' in src else ''
if 'Lesson 4' not in head: head = head.rstrip('\n') + '\n/* 11/11: Lesson 4 Create a Greener Tomorrow 본문 DAY p1~p4 (❶❷ · ❸ · ❹❺ · ❻❼) gen/oh4 (raw.json ← 이그잼포유 hwp) attach.py, 이어서 gen_h2oh4full.py = 완전정복 k1~k3 */\n'
PK.pop('tests', None)
write(PK, path, head)
if tail: open(path, 'a', encoding='utf-8').write(tail)
print([(d['name'], d['range']) for d in PK['days']])
