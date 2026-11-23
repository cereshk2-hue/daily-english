# 11/23 안곡고1 추가 시험범위: 2026년 10월 고1 학평 21·22·23·24·29번 + (18:53) 30·31·32번 → h1-donga-lee-L3 맨 뒤 DAY 21~28 (o21 … o32)
# 재료: 저동고1 단원(h1-mock-2610-jeodong)의 같은 번호 DAY(q21…q29)를 그대로 복사 (9월 DAY와 같은 단계 구성). 여러 번 돌려도 같음
import sys, json, re, subprocess
sys.path.insert(0, '/home/claude/srcrepo/generators')
from gencommon import write
D = '/home/claude/proj/data/'
def load(path, head_only=True):
    src = open(path, encoding='utf-8').read()
    ti = min([src.index(m) for m in ('/* WRAPUP-TESTS', '/* BIMI-TESTS', '/* GICHUL-TESTS') if m in src] or [len(src)])
    js = src[:ti] if head_only else src
    pk = json.loads(subprocess.check_output(['node', '-e', "global.window={};eval(require('fs').readFileSync(0,'utf8'));process.stdout.write(JSON.stringify(window.PKG))"], input=js.encode()))
    return src, ti, pk
_, _, JD = load(D + 'h1-mock-2610-jeodong.js')
path = D + 'h1-donga-lee-L3.js'
src, ti, PK = load(path)
HEADJS, TAIL = src[:ti], src[ti:]
NUMS = ['21', '22', '23', '24', '29', '30', '31', '32']
new = []
for n in NUMS:
    d = json.loads(json.dumps(next(x for x in JD['days'] if x['id'] == 'q' + n)))
    d['id'] = 'o' + n; d['range'] = '10월 모고 %s번' % n
    new.append(d)
PK['days'] = [d for d in PK['days'] if not re.match(r'o\d+$', d['id'])] + new
for k, d in enumerate(PK['days']): d['name'] = 'DAY %d' % (k + 1)
PK['titleKo'] = '동아(이병민) 3·4과 본문 + 2026년 9월 고1 학평 30·33~42번 + 10월 21~24·29~32번'
head = HEADJS[:HEADJS.index('window.PKG')]
if '10월 고1 학평 21' not in head:
    head = head.rstrip('\n') + '\n/* 11/23: 2026년 10월 고1 학평 21·22·23·24·29번 DAY o21~o29 맨 뒤 (gen/ag2610/add_oct.py — 저동고1 단원 같은 번호 DAY 복사) */\n'
write(PK, path, head)
open(path, 'a', encoding='utf-8').write(TAIL)
print([(d['name'], d['range']) for d in PK['days'][-6:]])
