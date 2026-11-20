# 설정 만들기용: 파일의 객관식 문항 요약 (번호 · 줄 · 발문 · 정답 · 보기)
import sys, re, importlib
sys.path.insert(0, '/home/claude/srcrepo/wrapup/bimi4')
import build
fk = sys.argv[1]
try: C = importlib.import_module('cfg_' + fk.replace('-', '')).C
except ModuleNotFoundError: C = {'STEMS': build.cands(fk), 'AUTOW': True}
its, grs = build.parse(fk, C)
for k, it in enumerate(its):
    j = C['STEMS'][k]
    if it.get('kind') == 'write': print('%s [L%d] (서술형) %s' % (it['n'], j, re.sub('<[^>]+>', '', it['stem'])[:90])); continue
    A = it['ans'] if isinstance(it['ans'], list) else [it['ans']]
    print('%s [L%d] %s  ▶ %s' % (it['n'], j, re.sub('<[^>]+>', '', it['stem'])[:110], ''.join('①②③④⑤'[a] for a in A)))
    if '-v' in sys.argv:
        for i, o in enumerate(it['opts']): print('     %s %s' % ('①②③④⑤'[i], re.sub('<[^>]+>', '', o)[:150]))
