# 11/21 안곡고1 · 2026년 9월 고1 학평(인천) 30·33~42번 → h1-donga-lee-L3(동아 이병민 L3·4) 끝에 DAY로 붙임 (선생님: 합치되 동아 먼저)
#  한 지문 = 하루, id q30 q33…q41, range '9월 모고 30번' … (gen/dj2610/mkattach.py 방식). 지문 문항은 p30 p33~p41.py
import sys, json, subprocess, re, importlib
sys.path.insert(0, '/home/claude/srcrepo/gen'); sys.path.insert(0, '/home/claude/srcrepo/gen/ag2609')
from gencommon import write
import jfw
from mkunit_mods import MODS
def build():
    out = []
    for mod, n, story in MODS:
        m = importlib.import_module(mod)
        d = jfw.spread(jfw.jday(m.p.n, 'DAY', '9월 모고 %s번' % n, story, m.p, m), re.match(r'\d+', n).group())
        d['id'] = 'q' + re.match(r'\d+', n).group()
        out.append(d)
    return out
if __name__ == '__main__':
    path = '/home/claude/proj/data/h1-donga-lee-L3.js'
    PK = json.loads(subprocess.check_output(['node', '-e', "global.window={};require('%s');process.stdout.write(JSON.stringify(window.PKG))" % path]))
    base = [d for d in PK['days'] if not re.match(r'q\d+$', d['id'])]
    PK['days'] = base + build()
    for i, d in enumerate(PK['days']): d['name'] = 'DAY %d' % (i + 1)
    PK['unit'] = '공통영어2 Lesson 3~4 + 9월 학평 30·33~42번'
    PK['title'] = '안곡고1'   # 11/21 선생님: 타이틀은 안곡고1
    PK['titleKo'] = '동아(이병민) 3·4과 본문 + 2026년 9월 고1 학평 30·33~42번'
    src = open(path, encoding='utf-8').read(); head = src[:src.index('window.PKG')]
    tail = src[src.index('/* WRAPUP-TESTS'):] if '/* WRAPUP-TESTS' in src else ''
    if '9월 고1 학평' not in head: head = head.rstrip('\n') + '\n/* 11/21: 2026년 9월 고1 학평(인천, 안곡고 범위) 30·33~42번 DAY q30~q41 (한 지문 = 하루) gen/ag2609/mkattach.py — 지문분석 hwp → extract*.py·prep.py → p30 p33~p41.py */\n'
    if not PK.get('tests'): PK.pop('tests', None)
    write(PK, path, head)
    if tail: open(path, 'a', encoding='utf-8').write(tail)
    print([(d['name'], d['id'], d['range'], sum(len(s['items']) for s in d['steps'])) for d in PK['days']])
