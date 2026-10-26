import json, sys
sys.path.insert(0, '/tmp/claude-0/-home-claude/a9e3e882-1f02-5d62-8f70-aced81bc59d2/scratchpad')
sys.path.insert(0, '/tmp/claude-0/-home-claude/a9e3e882-1f02-5d62-8f70-aced81bc59d2/scratchpad/split')
from gencommon import write
from combine import split_pkg
D = '/tmp/claude-0/-home-claude/a9e3e882-1f02-5d62-8f70-aced81bc59d2/scratchpad/split/'
ORDER = ['핵심어휘·숙어', '실전 문항', '어휘선택', 'T/F 내용 확인', '일치·불일치', '어법선택', '동사변형', '오류찾기', '본문 스크램블', '문장순서', '문장삽입', '어색한 문장', '빈칸추론', '핵심문법', '요약문 완성']
P = json.load(open(D + 'h2-mock-2609-angok.json'))
old, _ = split_pkg(P)
num = {x['name'].replace('번', ''): x for x in old}
for x in json.load(open(D + 'new_h2.json')):
    num[str(x['num'])] = {'name': '%d번' % x['num'], 'range': x['kind'], 'passage': x['passage'], 'steps': x['steps']}
def merge(a, b):
    st = []
    for t in ORDER:
        parts = [s for s in num[a]['steps'] + num[b]['steps'] if s['title'] == t]
        if not parts: continue
        m = dict(parts[0]); m['items'] = [q for s in parts for q in s['items']]
        if m['type'] == 'vocab': m['quizN'] = min(15, len(m['items']))
        st.append(m)
    extra = [s['title'] for s in num[a]['steps'] + num[b]['steps'] if s['title'] not in ORDER]
    assert not extra, extra
    return st
PAIRS = [('19', '20'), ('21', '22'), ('23', '24'), ('26', '27'), ('29', '30')]
days = []
for i, (a, b) in enumerate(PAIRS):
    days.append({'id': 'd%d' % (i + 1), 'name': 'DAY %d' % (i + 1), 'range': '%s·%s번' % (a, b),
                 'story': '%s %s · %s %s' % (a, num[a]['range'], b, num[b]['range']),
                 'passage': num[a]['passage'] + num[b]['passage'], 'steps': merge(a, b)})
leg = {}
for i, (a, b) in enumerate(PAIRS):
    for n in (a, b): leg['q' + n] = ['d%d' % (i + 1)]
PK = {'id': 'h2-mock-2609-jungsan', 'school': '고2 모의고사(2026년 9월 학평·중산고)', 'unit': '19~24 · 26~27 · 29~30번', 'title': 'September 2026 Mock Test',
      'titleKo': '2026년 9월 고2 학력평가 · 중산고 내신 범위', 'exam': '내신·모의고사', 'prose': True, 'teacherPhone': '',
      'legacy': {'v': 2, 'key': 'daily:h2-mock-2609', 'map': leg}, 'days': days}
write(PK, '/home/claude/proj/data/h2-mock-2609-jungsan.js',
      "/* 고2 2026년 9월 학력평가 · 중산고 내신 범위 19~24 · 26~27 · 29~30번 (두 문항씩 DAY 5개, 순서대로)\n"
      "   만든 곳: gen_m2609b.py(19~23·26·27) + gen_m2609.py(24·29·30, 안곡고 파일에서 번호별로 떼어 옴) → split/combine2.py */\n")
print([(d['name'], d['range'], len(d['steps']), sum(len(s['items']) for s in d['steps'])) for d in days])
