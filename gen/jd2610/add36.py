# 11/23 저동고1 36번 추가: p36.py → DAY q36을 q35와 q37 사이에 넣기 (DAY 이름 다시 매김, 진도는 DAY id·범위로 맞춰져서 안전). 뒤 BIMI/BOSS 블록 보존. 여러 번 돌려도 같음
# 준비: /home/claude/work/jd2610/{prep.json,q.json} 와 gen/ (이 폴더 복사본) — jfw.py가 그 경로를 읽음
import sys, json, subprocess, shutil, os
G = '/home/claude/work/jd2610/gen'
os.makedirs(G, exist_ok=True)
for f in os.listdir('/home/claude/srcrepo/gen/jd2610'):
    if f.endswith(('.py', '.json')): shutil.copy('/home/claude/srcrepo/gen/jd2610/' + f, G)
for f in ('prep.json', 'q.json'): shutil.copy('/home/claude/srcrepo/gen/jd2610/' + f, '/home/claude/work/jd2610/' + f)
sys.path.insert(0, '/home/claude/srcrepo/generators'); sys.path.insert(0, G); os.chdir(G)
from build import build
from gencommon import write
d = build([('p36', '36번', '36 글의 순서 · 소리는 뇌의 산물')])[0]
path = '/home/claude/proj/data/h1-mock-2610-jeodong.js'
src = open(path, encoding='utf-8').read()
ti = min(src.index(m) for m in ('/* BIMI-TESTS', '/* BOSS-TESTS', '/* WRAPUP-TESTS') if m in src)
HEAD, TAIL = src[:ti], src[ti:]
PK = json.loads(subprocess.check_output(['node', '-e', "global.window={};eval(require('fs').readFileSync(0,'utf8'));process.stdout.write(JSON.stringify(window.PKG))"], input=HEAD.encode()))
assert not PK.get('tests')
days = [x for x in PK['days'] if x['id'] != 'q36']
k = [x['id'] for x in days].index('q37')
days.insert(k, d)
for i, x in enumerate(days): x['name'] = 'DAY %d' % (i + 1)
PK['days'] = days
PK['unit'] = PK['unit'].replace('28~35 · 37~40번', '28~40번') if '28~35 · 37~40번' in PK['unit'] else PK['unit']
head = HEAD[:HEAD.index('window.PKG')]
if '36번 DAY' not in head: head = head.rstrip('\n') + '\n/* 11/23: 36번 DAY q36 (35번과 37번 사이) gen/jd2610/p36.py · add36.py */\n'
write(PK, path, head)
open(path, 'a', encoding='utf-8').write(TAIL)
print([(x['name'], x['range']) for x in days[11:16]], PK['unit'])
