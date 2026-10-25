import json, re, sys
def nz(s): 
    s = re.sub(r'<[^>]+>', ' ', str(s)); s = re.sub(r'\{([^}|]*)\|[^}]*\}', r'\1', s); s = re.sub(r'\[\[(.*?)\]\]', r'\1', s)
    s = s.lower().replace('’', "'").replace('‘', "'")
    return re.sub(r'[^a-z0-9\' ]+', ' ', s).split()
def secs_of(d):
    out = []; cur = None
    for l in d['passage']:
        if l[0] == '#': cur = {'label': l[1], 'num': l[1].split('번')[0], 'text': []}; out.append(cur)
        elif cur is not None: cur['text'] += nz(l[1])
    for c in out: c['g3'] = set(tuple(c['text'][i:i+3]) for i in range(len(c['text']) - 2)); c['w'] = set(c['text'])
    return out
def by_num(secs, n):
    n = str(n)
    for c in secs:
        if c['num'] == n or c['num'].split('~')[0] == n.split('~')[0]: return c
    return None
def texts(st, q):
    t = st['type']
    if t == 'pick' or t == 'verb' or t == 'error' or t == 'blank': return [q['s']]
    if t == 'scramble': return [q['en']]
    if t in ('order', 'insert'): return q['lines']
    if t == 'odd': return [x for i, x in enumerate(q['lines']) if i != q['odd']]
    if t == 'mc': return [q['q']] + list(q.get('opts', []))
    return []
def assign(secs, st, q):
    t = st['type']
    if t == 'vocab': return by_num(secs, q[2]), 'n'
    if t == 'tf': return by_num(secs, q[3]), 'n'
    if isinstance(q, dict) and q.get('n') is not None and by_num(secs, q['n']): return by_num(secs, q['n']), 'n'
    words = []
    for x in texts(st, q): words += nz(x)
    g3 = set(tuple(words[i:i+3]) for i in range(len(words) - 2))
    sc = sorted(((len(g3 & c['g3']), len(set(words) & c['w']), c) for c in secs), key=lambda z: (-z[0], -z[1]))
    best = sc[0]; second = sc[1] if len(sc) > 1 else (0, 0, None)
    conf = 'g3' if best[0] > 0 and best[0] > second[0] else ('w?' if best[1] > second[1] else '??')
    return best[2], conf
if __name__ == '__main__':
    P = json.load(open(sys.argv[1]))
    for d in P['days']:
        secs = secs_of(d)
        if len(secs) < 2: continue
        for st in d['steps']:
            for q in st['items']:
                c, how = assign(secs, st, q)
                if how not in ('n', 'g3'):
                    print(d['id'], st['title'], '→', c['label'], how, '|', re.sub(r'<[^>]+>', ' ', str(texts(st, q)[0]))[:110])
