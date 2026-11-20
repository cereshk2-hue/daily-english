# 학생별 진도표용 단원 지도: daily-english 저장소의 git 기록에서 단원 이름이 바뀐 모든 버전을 모아
# '현황/기록' 탭의 단원 이름(P.unit + ' ' + P.title) → 지금 단원(id)으로 잇고, 지금 단원의 DAY·시험 목록을 담는다.
# 사용: python3 tools/progress_map.py /home/claude/daily-english   → t-iyr3rba2/progress-map.json
import os, re, sys, json, subprocess
REPO = sys.argv[1] if len(sys.argv) > 1 else '/home/claude/daily-english'
BOARD = json.load(open(os.path.join(os.path.dirname(os.path.abspath(__file__)), 'secrets.json')))['board']
SCHOOL = {  # 단원 → 학교·학년 (진도표 검색용 · 모르는 단원은 비워 둠)
    'm1-donga-yoon-L6': '중산중1', 'm1-grammar-to1': '중산중1 · 심학중1', 'm1-chunjae-so-L6': '심학중1', 'm3-jihak-min-L7': '중산중3', 'm2-visang-hwang-L7': '발산중2',
    'h1-mock-2509': '중산고1', 'h2-mock-2609-jungsan': '중산고2', 'h2-mirae-kim-L4': '중산고2', 'h3-suneung-2510': '중산고2 · 고3',
    'h1-ne-min-L3': '저동고1', 'h1-mock-2610-jeodong': '저동고1', 'h2-chunjae-cho-L5': '안곡고2', 'h2-mock-2609-angok': '안곡고2', 'h2-ne-oh-L3': '대진고2', 'h1-donga-lee-L3': '안곡고1', 'm2-donga-yoon-L7': '중산중2'}
def test_label(t):
    # 진도표 시험 칸 머리: (종류, 작은 글씨) — 여기만 고치면 진도표 이름이 바뀜(Code.gs 다시 붙일 필요 없음)
    ti = re.sub(r'\s+', ' ', t.get('title', '') or t.get('short', ''))
    kinds = [('끝판왕', '끝판왕'), ('비밀노트', '비밀노트'), ('Wrap-up', 'Wrap-up'), ('변형기출', '변형기출'), ('기출 마무리', '기출마무리'), ('기출 선별', '기출선별'), ('기출 변형', '기출변형'), ('실전 변형', '실전변형'), ('실전 문제', '실전문제'), ('문법', '문법')]
    kind = next((k for w, k in kinds if w.lower() in ti.lower()), '')
    m = re.search(r'(\d{4})\s*기출', ti)
    if not kind and m: kind = '%s 기출' % m.group(1)
    sub = ti
    for w in ['너른터 ', '끝판왕 ', '비밀노트 ', '변형기출 ', '기출 마무리 ', '기출 선별 ', '기출 변형 ', '실전 변형 ', '실전 문제 ', '요약문 ', '문법 ', '%s 기출 ' % (m.group(1) if m else '@@')]: sub = sub.replace(w, '')
    sub = re.sub(r'(?i)\s*wrap-?up\s*', ' ', sub); sub = re.sub(r'\d+월\s*학평\s*', '', sub); sub = re.sub(r'^(천재|동아|비상|능률|미래엔|지학사)\s*', '', sub)
    sub = re.sub(r'\(([^)]*)\)', r'\1', sub).replace('번', '').replace(' · ', ' ').strip()
    return kind or '시험', sub[:14]
def day_label(d):
    r = str(d.get('range', ''))
    r = re.sub(r'^실전 어휘 뚫기\s*\d+\s*·\s*', '어휘 ', r); r = re.sub(r'^내용 꿰뚫기\s*\d*\s*·\s*', '꿰뚫기 ', r)
    r = re.sub(r'^YBM\s*', 'YBM', r).replace(' · ', ' ').replace('번', '').replace('Lesson ', 'L').replace('본문 ', '본문')
    return re.sub(r'\s+', ' ', r).strip()[:12]
RETIRED = {'h1-ybm-kim-L3': 'h1-mock-2509', 'm1-grammar-that': 'm1-grammar-to1'}  # 합쳐진 단원 → 지금 단원
nz = lambda s: re.sub(r'\s+', '', str(s or '')).replace('변형어휘', '실전어휘뚫기')
def g(*a): return subprocess.check_output(['git', '-C', REPO] + list(a)).decode()
def pkg(src):
    p = subprocess.run(['node', '-e', "global.window={};eval(require('fs').readFileSync(0,'utf8'));process.stdout.write(JSON.stringify(window.PKG||null))"], input=src.encode(), capture_output=True)
    try: return json.loads(p.stdout.decode() or 'null')
    except Exception: return None
uk, cur = {}, {}
olddays = {}   # 11/20 (단원, DAY id) → 예전 DAY 범위 이름들 (이름이 바뀐 예전 기록을 같은 칸에)
paths = sorted(set(x for x in g('log', '--all', '--format=', '--name-only', '--', '*/data/*.js').split('\n') if x.endswith('.js')))
for path in paths:
    for c in [x for x in g('log', '--all', '--format=%h', '--', path).split() if x]:
        try: src = g('show', '%s:%s' % (c, path))
        except subprocess.CalledProcessError: continue
        P = pkg(src)
        if not P: continue
        pid = RETIRED.get(P['id'], P['id'])
        uk.setdefault(nz(P.get('unit', '') + ' ' + P.get('title', '')), pid)
        for x in P.get('days', []): olddays.setdefault((pid, x.get('id')), set()).add(x.get('range', ''))
# 지금 단원
for d in sorted(os.listdir(REPO)):
    dd = os.path.join(REPO, d, 'data')
    if not os.path.isdir(dd): continue
    for f in os.listdir(dd):
        P = pkg(open(os.path.join(dd, f), encoding='utf-8').read())
        if not P: continue
        uk[nz(P.get('unit', '') + ' ' + P.get('title', ''))] = RETIRED.get(P['id'], P['id'])
        if P['id'] in RETIRED: continue
        cur[P['id']] = {'book': P.get('school', ''), 'school': SCHOOL.get(P['id'], ''), 'unit': P.get('unit', ''), 'title': P.get('title', ''), 'folder': d,
                        'days': [[x['id'], x['name'], x.get('range', ''), day_label(x)] + ([al] if (al := sorted(r for r in olddays.get((P['id'], x['id']), ()) if nz(r) != nz(x.get('range', '')) and nz(r) not in {nz(y.get('range', '')) for y in P['days']})) else []) for x in P['days']],
                        'tests': [['w:' + t['id'], t.get('short', ''), t.get('title', '')] + list(test_label(t)) + ([dict(P.get('testReset') or [])[t['id']]] if t['id'] in dict(P.get('testReset') or []) else []) for t in P.get('tests', [])]}  # 11/18 리셋 시각(ms) → 진도표가 그 전 기록을 뺌
# 지금 보드에 없는 예전 단원은 지도에서 빼서(이름 그대로 따로 묶임) 혼동 없게
uk = {k: v for k, v in uk.items() if v in cur}
out = os.path.join(REPO, BOARD, 'progress-map.json')
json.dump({'uk': uk, 'units': cur}, open(out, 'w', encoding='utf-8'), ensure_ascii=False, separators=(',', ':'))
print('단원 이름', len(uk), '→ 지금 단원', len(cur), '·', out)
