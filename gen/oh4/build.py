import sys, importlib
sys.path.insert(0, '/home/claude/work/oh4/gen')
import common
DAYS = [('p1', 'p1', '4과 본문 ❶❷', '고장 난 노트북과 전자 쓰레기 문제', ['❶', '❷']), ('p2', 'p2', '4과 본문 ❸', '수리할 권리 운동', ['❸']),
        ('p3', 'p3', '4과 본문 ❹❺', '프랑스의 수리 가능성 지수', ['❹', '❺']), ('p4', 'p4', '4과 본문 ❻❼', '수리 카페 · 수리가 일상인 지속 가능한 세상', ['❻', '❼'])]
def build(only=None):
    out = []
    for mod, did, rng, story, secs in DAYS:
        if only and mod not in only: continue
        m = importlib.import_module(mod); out.append(common.day(did, 'DAY', rng, story, secs, m))
    return out
if __name__ == '__main__':
    for d in build(sys.argv[1:]): print(d['id'], [(s['title'], len(s['items'])) for s in d['steps']], sum(len(s['items']) for s in d['steps']))
