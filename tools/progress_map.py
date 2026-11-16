# 학생별 진도표용 단원 지도: daily-english 저장소의 git 기록에서 단원 이름이 바뀐 모든 버전을 모아
# '현황/기록' 탭의 단원 이름(P.unit + ' ' + P.title) → 지금 단원(id)으로 잇고, 지금 단원의 DAY·시험 목록을 담는다.
# 사용: python3 tools/progress_map.py /home/claude/daily-english   → t-iyr3rba2/progress-map.json
import os, re, sys, json, subprocess
REPO = sys.argv[1] if len(sys.argv) > 1 else '/home/claude/daily-english'
BOARD = json.load(open(os.path.join(os.path.dirname(os.path.abspath(__file__)), 'secrets.json')))['board']
SCHOOL = {  # 단원 → 학교·학년 (진도표 검색용 · 모르는 단원은 비워 둠)
    'm1-donga-yoon-L6': '중산중1', 'm1-grammar-to1': '중산중1', 'm3-jihak-min-L7': '중산중3', 'm2-visang-hwang-L7': '발산중2',
    'h1-mock-2509': '중산고1', 'h2-mock-2609-jungsan': '중산고2', 'h2-mirae-kim-L4': '중산고2', 'h3-suneung-2510': '중산고2 · 고3',
    'h1-ne-min-L3': '저동고1', 'h1-mock-2610-jeodong': '저동고1', 'h2-chunjae-cho-L5': '안곡고2', 'h2-mock-2609-angok': '안곡고2', 'h2-ne-oh-L3': '대진고2'}
RETIRED = {'h1-ybm-kim-L3': 'h1-mock-2509', 'm1-grammar-that': 'm1-grammar-to1'}  # 합쳐진 단원 → 지금 단원
nz = lambda s: re.sub(r'\s+', '', str(s or '')).replace('변형어휘', '실전어휘뚫기')
def g(*a): return subprocess.check_output(['git', '-C', REPO] + list(a)).decode()
def pkg(src):
    p = subprocess.run(['node', '-e', "global.window={};eval(require('fs').readFileSync(0,'utf8'));process.stdout.write(JSON.stringify(window.PKG||null))"], input=src.encode(), capture_output=True)
    try: return json.loads(p.stdout.decode() or 'null')
    except Exception: return None
uk, cur = {}, {}
paths = sorted(set(x for x in g('log', '--all', '--format=', '--name-only', '--', '*/data/*.js').split('\n') if x.endswith('.js')))
for path in paths:
    for c in [x for x in g('log', '--all', '--format=%h', '--', path).split() if x]:
        try: src = g('show', '%s:%s' % (c, path))
        except subprocess.CalledProcessError: continue
        P = pkg(src)
        if not P: continue
        pid = RETIRED.get(P['id'], P['id'])
        uk.setdefault(nz(P.get('unit', '') + ' ' + P.get('title', '')), pid)
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
                        'days': [[x['id'], x['name'], x.get('range', '')] for x in P['days']],
                        'tests': [['w:' + t['id'], t.get('short', ''), t.get('title', '')] for t in P.get('tests', [])]}
# 지금 보드에 없는 예전 단원은 지도에서 빼서(이름 그대로 따로 묶임) 혼동 없게
uk = {k: v for k, v in uk.items() if v in cur}
out = os.path.join(REPO, BOARD, 'progress-map.json')
json.dump({'uk': uk, 'units': cur}, open(out, 'w', encoding='utf-8'), ensure_ascii=False, separators=(',', ':'))
print('단원 이름', len(uk), '→ 지금 단원', len(cur), '·', out)
