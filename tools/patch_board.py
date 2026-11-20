# 배포 보드(t-iyr3rba2) UNITS 중 지정 폴더만 dist 값으로 갱신 — 순서·link 유지 (사용: patch_board.py <folder>...)
import json, sys
dst = '/home/claude/daily-english/t-iyr3rba2/index.html'; src = '/home/claude/proj/dist/github/t-iyr3rba2/index.html'
dec = json.JSONDecoder()
def units(s):
    i = s.index('window.UNITS = ') + len('window.UNITS = ')
    v, e = dec.raw_decode(s[i:]); return v, i, i + e
S = open(src, encoding='utf-8').read(); D = open(dst, encoding='utf-8').read()
new, _, _ = units(S); old, a, b = units(D); N = {u['folder']: u for u in new}
for f in sys.argv[1:]:
    k = [i for i, u in enumerate(old) if u['folder'] == f]
    u = dict(N[f])
    if k: u['link'] = old[k[0]].get('link') or u.get('link'); old[k[0]] = u
    else: u.setdefault('link', 'https://cereshk2-hue.github.io/daily-english/%s/' % f); old.append(u)
    print(f, 'updated' if k else 'added', [d['name'] for d in u.get('days', [])][-3:], u.get('tests', '')[:0] if isinstance(u.get('tests'), str) else '')
D = D[:a] + json.dumps(old, ensure_ascii=False, indent=2) + D[b:]
open(dst, 'w', encoding='utf-8').write(D)
