import sys, re, html, json, subprocess
sys.path.insert(0, '/home/claude/srcrepo/gen')
from gencommon import write
# 고3 수능실전반 (11/18) · 2027학년도 9월 모의평가(평가원) 18~45번 → 기존 10월 학평 DAY 1~25 뒤에 DAY 26~50으로 이어 붙임
# 3등급 학생 기준 순서: 쉬운 유형으로 시작 → 3등급이 약한 유형(빈칸·순서·삽입·어휘) 사이사이 → 고난도(33·34·37·39)는 뒤쪽에 흩어 배치
# 18 → 20 → 19 → 22 → 26 → 23 → 27 → 24 → 25 → 36 → 28 → 29 → 31 → 35 → 40 → 30 → 43~45 → 21 → 38 → 32 → 41·42 → 37 → 33 → 39 → 34
# 정답: 18② 19② 20① 21② 22② 23⑤ 24① 25③ 26④ 27⑤ 28⑤ 29③ 30⑤ 31① 32⑤ 33③ 34④ 35④ 36③ 37④ 38⑤ 39③ 40① 41③ 42④ 43④ 44④ 45②
# 실행: python3 gen_h3s9.py  → /home/claude/proj/data/h3-suneung-2510.js 의 기존 DAY(10월)를 읽어 제목 붙이고, 9월 DAY를 뒤에 붙여 다시 씀
#       (10월 DAY는 다시 만들지 않음. 이미 9월이 붙어 있으면 10월 25개만 남기고 새로 붙임)
GEN = '/home/claude/srcrepo/gen/'
_s = open(GEN + 'gen_h3sn.py').read()
exec(_s[_s.index('def esc'):_s.index('# ═══ DAY 1 ')])
_m = open(GEN + 'gen_h3sn_more.py').read()
exec(_m[_m.index('def multi'):_m.index('# ═══ DAY 11')])
exec(_m[_m.index('def ul('):_m.index('P43 = ')])

TD = 'style="border:1px solid var(--line);padding:4px 2px;text-align:center;white-space:nowrap"'
ANS = {18: 1, 19: 1, 20: 0, 21: 1, 22: 1, 23: 4, 24: 0, 25: 2, 26: 3, 27: 4, 28: 4, 29: 2, 30: 4, 31: 0, 32: 4, 33: 2, 34: 3, 35: 3, 36: 2, 37: 3, 38: 4, 39: 2, 40: 0,
       41: 2, 42: 3, 43: 3, 44: 3, 45: 1}

for part in ('gen_h3s9_a.py', 'gen_h3s9_b.py', 'gen_h3s9_c.py'):
    exec(open(GEN + part).read())

# 정답 대조 (정답표)
for d in DAYS:
    for it in d['steps'][0]['items']:
        assert it['a'] == ANS[it['n']], (it['n'], it['a'])
assert len(DAYS) == 25, len(DAYS)
assert sorted(it['n'] for d in DAYS for it in d['steps'][0]['items']) == list(range(18, 46))

T9, T10 = '9월 모평 ', '10월 학평 '
for d in DAYS:
    d['id'] = 's' + d['id'][1:]
    d['range'] = T9 + d['range']
    d['passage'][0][1] = T9 + d['passage'][0][1]
    d['steps'][0]['guide'] = '2027학년도 9월 모의평가 기출이에요. ' + d['steps'][0]['guide']

DATA = '/home/claude/proj/data/h3-suneung-2510.js'
PKG = json.loads(subprocess.check_output(['node', '-e', "global.window={};require(%r);process.stdout.write(JSON.stringify(window.PKG))" % DATA]))
old = [d for d in PKG['days'] if d['id'].startswith('q')]
assert len(old) == 25, len(old)
for d in old:
    if not d['range'].startswith(T10):
        d['range'] = T10 + d['range']
        d['passage'][0][1] = T10 + d['passage'][0][1]
    for it in d['steps'][0]['items']:
        it['q'] = it['q'].replace(' [3점] [3점]', ' [3점]')  # 10월 42번 [3점] 중복 표시 수정
    g = d['steps'][0]['guide']
    if not g.startswith('2026학년도 10월'):
        d['steps'][0]['guide'] = '2026학년도 10월 학평 기출이에요. ' + g
ids = [d['id'] for d in old] + [d['id'] for d in DAYS]
assert len(set(ids)) == len(ids)
PKG['unit'] = '하루 한 문제 · 2026학년도 10월 학평 + 2027학년도 9월 모평'
PKG['days'] = old + DAYS
for i, d in enumerate(PKG['days']): d['name'] = 'DAY %d' % (i + 1)
head = open(DATA).read().split('window.PKG')[0]
if '9월 모의평가' not in head:
    head = head.replace('2026학년도 10월 고3 전국연합학력평가', '2026학년도 10월 고3 전국연합학력평가 (DAY 1~25) + 2027학년도 9월 모의평가 (DAY 26~50, srcrepo/gen/gen_h3s9.py)')
write(PKG, DATA, head)
print('ok', len(PKG['days']))
