import re
JUNK = re.compile(r'^\s*(Part|I|II|III|유형편|\d{1,3}|Gateway|Exercise)\s*$')
def parse_struct(s):
    out = []
    for x in [x for x in re.split(r'■■', s) if x.strip()]:
        x = re.sub(r'\n\s*본문.*$', '', x, flags=re.S)
        ls = [l.strip() for l in x.split('\n') if l.strip() and not JUNK.match(l)]
        en, note, mode = [], [], 0
        for l in ls:
            if mode == 0 and (re.match(r'(\[ ?\]|\{ ?\}|< ?>|\( ?\)|「|‘)', l) or re.search(r'[가-힣]', l)): mode = 1
            (en if mode == 0 else note).append(l)
        e = re.sub(r'\s+', ' ', re.sub(r'[\[\]{}<>]', '', ' '.join(en))).strip()
        out.append((e, '\n'.join(note)))
    return out
CIRS = '①②③④⑤'
def split_opts(opts):
    s = re.sub(r'\s+', ' ', ' '.join(opts))
    parts = re.split(r'([①②③④⑤])', s)
    out = {}
    for k in range(1, len(parts) - 1, 2):
        t = parts[k + 1]
        t = re.split(r'\s+(?:정답과 해설|\d\d\s+(?:다음|[가-힣A-Za-z])|\d\d\s*$|Part\b|유형편)', t)[0]
        out[parts[k]] = t.strip()
    return [out.get(c, '') for c in CIRS] if len(out) == 5 else None
