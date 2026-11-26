# 11/17 저동고1 · 비밀노트(edu-lab) 2026년 고1 10월 변형문제 → h1-mock-2610-jeodong '비밀노트 변형문제' 탭 (bimi/build_bimi.py 일반화)
# 원본 hwp → u<파일>.txt (hwpread_u: 밑줄 …). 파일별 설정은 cfg_<파일>.py (STEMS 줄 번호 0부터, W 서술형, DROP 정답 줄, LINEFIX 줄 통째 교체, FIXT 글자 교체, NOTE 검수, EXP 해설, SRC 번호 고침)
import re, json, sys, html as H, importlib
sys.path.insert(0, '/home/claude/srcrepo/wrapup/bimi2')
DIR = '/home/claude/srcrepo/wrapup/bimi2/'
D = '/home/claude/proj/data/h1-mock-2610-jeodong.js'
CIRC = '①②③④⑤'; ALT = dict(zip('➀➁➂➃➄', CIRC)); ALT.update(zip('❶❷❸❹❺', CIRC))
def nc(s): return ''.join(ALT.get(c, c) for c in s)
SKIP = ('http://edu-lab', '비밀노트', 'edu-lab.kr')
def esc(s): return H.escape(s, quote=False).replace('', '<u>').replace('', '</u>')
def XF(exp, n, ansmark):
    if n not in exp: return ''
    p = [x.strip() for x in exp[n].split('//')] + ['', '']
    out = ['정답 ▶ ' + ansmark] if ansmark else []
    for lb, x in zip(('이유', '오답', '포인트'), p[:3]):
        if x: out.append(lb + ' ▶ ' + x)
    return '\n'.join(out)
def korean(l):
    t = l.strip()
    if not t or '___' in t: return False
    if t.startswith(('원문', '(원문')): return True
    if t[0] in '<[(①②③④⑤ⓐⓑⓒⓓⓔⓕ→※-➠➀➁➂➃➄' or re.match(r'\d\.', t) or t.startswith(('조건', '어색한', '바르게', '<')): return False
    h = len(re.findall('[가-힣]', t)); a = len(re.findall('[A-Za-z]', t))
    return len(t) > 12 and h > 2 * a
def takeexp(seg, skip=None):   # 정답 줄 바로 뒤 우리말 해설 줄 (AUTOEXP 파일)
    out, keep, started, done = [], [], False, False
    for i, l in enumerate(seg):
        if i == skip: keep.append(l); continue
        if not done and korean(l): out.append(re.sub('[\ue000\ue001]', '', l).strip()); started = True; continue
        if l.strip(): done = True
        keep.append(l)
    return out, keep
HDR = re.compile(r'^[\s❖]*다음 글을 읽고 (질문|물음|주어진 문제)에 답하시오')
STEMRE = re.compile(r'^(다음|윗글|글의|주어진|밑줄|Which|본문|위 글|\S+에 관한|\S+에 대한|빈칸|위의|아래)')
def cands(fk):   # 문항 첫 줄 후보 (설정 만들 때 확인용)
    L = open(DIR + 'u%s.txt' % fk, encoding='utf-8').read().split('\n')
    return [i for i, l in enumerate(L) if STEMRE.match(l) and not l.startswith(' ')]
def parse(fk, C):
    raw = open(DIR + 'u%s.txt' % fk, encoding='utf-8').read().replace('\xad', '-')
    for a, b in C.get('REPL', []): raw = raw.replace(a, b)
    L = raw.split('\n')
    for i, t in C.get('LINEFIX', {}).items(): L[i] = t
    raw = '\n'.join(L)
    for a, b in C.get('FIXT', []):
        pat = '[]*'.join(re.escape(ch) for ch in a)
        ms = list(re.finditer(pat, raw)); assert len(ms) == 1, (fk, a, len(ms))
        span = ms[0].group(0); bb = b
        for w in re.findall('(.*?)', span):
            w = w.strip()
            if w and w in bb: bb = bb.replace(w, '' + w + '', 1)
        raw = raw[:ms[0].start()] + bb + raw[ms[0].end():]
    L = raw.split('\n')
    if C.get('END'): L = L[:C['END']]
    S = C['STEMS']; items = []; EXP = C.get('EXP', {}); W = C.get('W', {})
    HS = [i for i, l in enumerate(L) if HDR.match(l)]
    groups = {}
    for h in HS:
        nx = min([x for x in S if x > h] + [len(L)])
        groups[h] = {'head': re.sub(r'\s*\[★+\]\s*', ' ', L[h]).strip(), 'text': '\n'.join(l.rstrip() for l in L[h + 1:nx] if not re.sub('[\ue000\ue001]', '', l).strip().startswith(SKIP)).strip()}
    for n, j in enumerate(S, 1):
        stop = min([x for x in S if x > j] + [h for h in HS if h > j] + [len(L)])
        idx = [k for k in range(j + 1, stop) if not re.sub('[\ue000\ue001]', '', L[k]).strip().startswith(SKIP) and L[k].strip() not in ('/',)]
        kx = C.get('KX', {}).get(n, [])
        drop = set(C.get('DROP', {}).get(n, [])) | set(kx)
        seg = [L[k] for k in C.get('BODYPRE', {}).get(n, [])] + [L[k] for k in idx if k not in drop]
        stem = re.sub(r'\s*\[★+\]\s*', ' ', L[j]).strip()
        hb = [h for h in HS if h < j]; g = hb[-1] if hb else None
        def haspass(lines): return any(len(re.sub(r'[^A-Za-z]', '', l)) > 450 for l in lines)
        it_g = g if g is not None and n in C.get('GRP', {}) else None
        if it_g is None and g is not None and not haspass(seg) and not any(g < x < j and haspass(L[x + 1:min([y for y in S if y > x] + [h for h in HS if h > x] + [len(L)])]) for x in S): it_g = g
        if n in C.get('NOGRP', ()): it_g = None
        m_ = re.search(r'\((\d\d)번?\)', stem)
        it = {'n': str(n), 'src': C.get('SRC', {}).get(n) or (('%s번' % m_.group(1)) if m_ else (('%s번' % C['DEFSRC'](n)) if C.get('DEFSRC') else '')), 'stem': esc(re.sub(r'\s*\(\d\d번?\)\s*', ' ', stem).strip()), 'pts': 2}
        if not it['src'] and it_g is not None and (mg := re.search(r'\((\d\d)번?\)', groups[it_g]['head'])): it['src'] = mg.group(1) + '번'
        BL = lambda l: re.sub(r'(?<=\S)[ \t　]{6,}(?=\S|$)', ' ________ ', l.rstrip()).strip()
        note = C.get('NOTE', {}).get(n)
        kexp = []
        kx_ = [re.sub('[\ue000\ue001]', '', L[k]).strip() for k in kx]
        if C.get('AUTOEXP') and n not in C.get('NOAUTO', ()):
            if n in W: kexp, seg = takeexp(seg)
        if n in W:
            body = [BL(l) for l in seg]
            txt = '\n'.join(body).strip()
            if it_g is not None: it['grp'] = it_g; it['ctx'] = '<b>' + esc(groups[it_g]['head']) + '</b><br>' + esc(groups[it_g]['text']).replace('\n', '<br>')
            bl = W[n]; per = round(2 / len(bl), 2)
            for b in bl: b['pts'] = per
            bl[-1]['pts'] = round(2 - per * (len(bl) - 1), 2)
            ex = XF(EXP, n, '') or (('이유 ▶ ' + ' '.join(kexp)) if kexp else '')
            if note: ex = '[수정] ' + note + ('\n' + ex if ex else '')
            it.update({'kind': 'write', 'blanks': bl, 'body': esc(txt).replace('\n', '<br>'), 'model': ' / '.join(b['ans'][0] for b in bl),
                       'ex': ex + ('\n(여러 가지로 쓸 수 있는 답은 선생님이 확인해요.)' if any(b['review'] for b in bl) else '')})
            items.append(it); continue
        ai = next((i for i, l in enumerate(seg) if re.match(r'\s+[①-⑤➀-➄❶-❺]', l)), None)
        if C.get('AUTOEXP') and n not in C.get('NOAUTO', ()):
            kexp, seg2 = takeexp(seg, ai)
            if kexp: ai = seg2.index(seg[ai]) if ai is not None else None; seg = seg2
        if n in C.get('ANS', {}):
            ans_line = C['ANS'][n]; memo = ''
            body = seg[:ai] + seg[ai + 1:] if ai is not None else seg
        else:
            ans_line = nc(re.sub('[\ue000\ue001]', '', seg[ai]).strip()); body = seg[:ai] + seg[ai + 1:]
            memo = re.sub(r'^[①-⑤,\s]+', '', ans_line).strip()
        m = re.match(r'([①-⑤][①-⑤,\s]*)', ans_line)
        ans = [CIRC.index(c) for c in re.findall('[①-⑤]', m.group(1))]
        opts = [''] * 5; rest = []
        bl_ = [BL(l) if not re.match(r'\s*[①-⑤➀-➄]', l) else l for l in body]; i = 0
        while i < len(bl_):
            l = nc(bl_[i].strip())
            if len(l) == 1 and l in CIRC and i + 2 < len(bl_):
                opts[CIRC.index(l)] = (bl_[i + 1].strip() + ' – ' + bl_[i + 2].strip()); i += 3; continue
            parts = re.split(r'(?=[①-⑤]\s?)', l) if re.match(r'[①-⑤]', l) else None
            if parts and all(re.match(r'[①-⑤]', p) for p in parts if p.strip()) and not opts[CIRC.index(parts[0][0] if parts[0] else parts[1][0])]:
                for p in parts:
                    if p.strip(): opts[CIRC.index(p[0])] = re.sub(r'\s+', ' ', re.sub(r'\s*(\t|\s{3,})\s*', ' – ', p[1:].strip())).strip()
            else: rest.append(bl_[i].rstrip())
            i += 1
        if not all(opts): opts = [o or CIRC[k] for k, o in enumerate(opts)]
        opts = [re.sub(r'\s+–\s+(?=[-…])', ' ', o) for o in opts]   # 11/26 표 모양 선택지 줄바꿈 찌꺼기 ' – -' · ' – ……' 지움
        if n in C.get('OPTS', {}): opts = C['OPTS'][n]
        mk = ''.join(CIRC[a] for a in ans)
        kexp = kx_ + kexp
        if memo and not memo.startswith('*') and C.get('AUTOEXP'): kexp = [memo] + kexp
        exs = [XF(EXP, n, mk) or (('정답 ▶ %s\n이유 ▶ ' % mk + ' '.join(kexp)) if kexp else '')]
        if memo.startswith('*'): exs.append('출제 메모 ▶ ' + memo.lstrip('* ').strip())
        if note: exs.insert(0, '[수정] ' + note)
        it.update({'body': esc('\n'.join(rest).strip()).replace('\n', '<br>'), 'opts': [esc(o) for o in opts], 'en': sum(c.isascii() and c.isalpha() for c in opts[0]) > len(opts[0]) * .5,
                   'ans': ans[0] if len(ans) == 1 else ans, 'ex': '\n'.join(x for x in exs if x)})
        if it_g is not None: it['grp'] = it_g; it['ctx'] = '<b>' + esc(groups[it_g]['head']) + '</b><br>' + esc(groups[it_g]['text']).replace('\n', '<br>')
        it.setdefault('ctx', '')
        items.append(it)
    return items, groups
def V(*xs):
    out = []
    for x in xs:
        for y in (x, x.replace('’', "'"), x.rstrip('.')):
            if y not in out: out.append(y)
    return out
def B(lab, ans, review=False): return {'label': lab, 'ans': ans if isinstance(ans, list) else V(ans), 'review': review}
def arrow(a, b): return [a + s + b for s in (' → ', '→', ' -> ', '->', ' - ', ' ')] + [b]
META = [('20-21', 'jb-2021', '20·21번'), ('22-23', 'jb-2223', '22·23번'), ('24_26', 'jb-24', '24번'), ('29-30', 'jb-2930', '29·30번'), ('31-32', 'jb-3132', '31·32번'),
        ('33-34', 'jb-3334', '33·34번'), ('35-36', 'jb-35', '35번'), ('37-38', 'jb-3738', '37·38번'), ('39-40', 'jb-3940', '39·40번')]
if __name__ == '__main__':
    only = sys.argv[1:]
    tests = []; GR = {}
    for fk, tid, sh in META:
        try: C = importlib.import_module('cfg_' + fk.replace('-', '').replace('_', '')).C
        except ModuleNotFoundError: continue
        its, grs = parse(fk, C)
        GR[tid] = {str(k): v for k, v in grs.items()}
        tests.append({'id': tid, 'kind': 'bimi', 'title': '비밀노트 변형문제 ' + sh, 'short': '비밀노트 ' + sh, 'school': '저동고 1학년', 'minutes': 50, 'items': its})
        mc = [i for i in its if i.get('kind') != 'write']
        print(tid, len(its), '문항 · 객관식', len(mc), '·', ' '.join('%s:%s' % (i['n'], ''.join(CIRC[a] for a in (i['ans'] if isinstance(i['ans'], list) else [i['ans']]))) for i in mc))
        miss = [i['n'] for i in its if not re.search(r'이유 ▶', i['ex'])]
        if miss: print('  해설 없음', miss)
    if 'dry' in only: sys.exit()
    js = open(D, encoding='utf-8').read()
    blk = ('/* BIMI-TESTS: 저동고1 비밀노트 변형문제 (wrapup/bimi2/build.py 로 만듦 · 손으로 고치지 말 것) */\n'
           'window.PKG.tests = (window.PKG.tests || []).filter(function (t) { return t.kind !== "bimi"; }).concat(' + json.dumps(tests, ensure_ascii=False) + ');\n/* /BIMI-TESTS */\n')
    if '/* BIMI-TESTS' in js: js = re.sub(r'/\* BIMI-TESTS.*?/\* /BIMI-TESTS \*/\n', lambda m: blk, js, flags=re.S)
    else: js = js.rstrip('\n') + '\n' + blk
    open(D, 'w', encoding='utf-8').write(js)
    import os; os.makedirs('/home/claude/work/jdbimi', exist_ok=True)
    json.dump({'tests': tests, 'groups': GR}, open('/home/claude/work/jdbimi/tests.json', 'w'), ensure_ascii=False, indent=1)
