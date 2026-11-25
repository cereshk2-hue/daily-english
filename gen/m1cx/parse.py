# 11/25 심학중1 천재(소영순) 기출(m1gc parse 복사 + 'Read the following and answer' 묶음 머리) · 원래: 11/24 중1 동아(윤정미) 2학기 중간 기출 7개교 hwp 텍스트 → 문항 구조(JSON). work/m1gc/*.txt (hwpread_u.py 출력)
import re, json, glob, os
import sys
W = sys.argv[1] if len(sys.argv) > 1 else '/home/claude/work/m1gc/'
C = '①②③④⑤'
def school(t): return re.search(r'(?:중간|기말)기출 (\S+)', t).group(1)
def split_opts(lines):
    s = '\n'.join(lines)
    parts = re.split(r'([①②③④⑤])', s)
    opts = {}
    for i in range(1, len(parts) - 1, 2): opts[parts[i]] = parts[i + 1].strip()
    return [opts.get(c, '') for c in C]
out = []
for f in sorted(glob.glob(W + '[0-9a-f]'*8 + '.txt')):
    t = open(f, encoding='utf-8').read()
    sc = school(t); L = t.split('\n')
    i = next(k for k, l in enumerate(L) if l.startswith('부교재')) + 1
    end = next((k for k in range(len(L) - 1, 0, -1) if L[k].strip() == '정답'), len(L)) - 1
    L = L[i:end]
    # 문항 시작: '다음'/'윗글'/'위 글'/영어 물음 + 물음표/것은/쓰시오/고르시오 줄
    qstart0 = re.compile(r'^\s*((다음|윗글|위 |위의|밑줄|빈칸|주어진|아래|대화|글의|본문).*(\?|것은|쓰시오|고르시오|답하시오|완성하시오|하시오)|Read the following and answer)')
    qen = re.compile(r'^[A-Z][^.:]{8,}\?\s*$')
    class Q:
        @staticmethod
        def match(l, nxt=''):
            return qstart0.match(l) or (qen.match(l) and re.match(r'^\s*[①②③④⑤]+\s*$', nxt))
    qstart = Q
    blocks = []; cur = None
    for li, l in enumerate(L):
        if qstart.match(l, L[li + 1] if li + 1 < len(L) else '') and len(l) < 160:
            cur = {'head': l.strip(), 'lines': []}; blocks.append(cur)
        elif cur is not None: cur['lines'].append(l.rstrip())
    grp = None; tag = None
    for b in blocks:
        m = re.search(r'\[([\d과, ]+)\]', b['head']); tg = m.group(1) if m else None
        if '물음에 답하시오' in b['head'] or b['head'].startswith('Read the following') or (b['head'].startswith('다음') and not any(re.match(r'^\s*[①②③④⑤]+\s*$', x) for x in b['lines'][:2]) and '물음' in b['head']):
            grp = {'head': b['head'], 'text': '\n'.join(b['lines']).strip(), 'tag': tg}; tag = tg; continue
        if tg is None and grp is not None and (b['head'].startswith('윗글') or b['head'].startswith('위 ') or re.match(r'^[A-Z]', b['head'])):
            g = grp; tg = grp['tag']
        else:
            g = None
            if tg is not None: grp = None
        ls = b['lines']; ans = None
        k = 0
        while k < len(ls) and not ls[k].strip(): k += 1
        if k < len(ls) and re.match(r'^\s*[①②③④⑤]+\s*$', ls[k]): ans = ls[k].strip(); ls = ls[k + 1:]
        oi = next((j for j, x in enumerate(ls) if x.strip().startswith('①')), None)
        body = '\n'.join(ls[:oi] if oi is not None else ls).strip('\n')
        opts = split_opts(ls[oi:]) if oi is not None else []
        out.append({'file': os.path.basename(f)[:8], 'school': sc, 'tag': tg, 'stem': b['head'], 'ans': ans, 'body': body, 'opts': opts, 'group': g})
json.dump(out, open(W + 'items.json', 'w'), ensure_ascii=False, indent=1)
from collections import Counter
print(len(out), Counter(o['school'] for o in out), sum(1 for o in out if not o['ans']), 'no-ans')
