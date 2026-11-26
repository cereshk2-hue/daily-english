import re
HAN = re.compile('[가-힣]')
def parse(f):
    L = [l.rstrip('\n') for l in open(f, encoding='utf-8')]
    Q, cur, ko, en = {}, None, [], []
    for l in L:
        s = l.strip()
        m = re.match(r'^(\d+(?:~\d+)?)번$', s)
        if m:
            if m.group(1) != cur: cur = m.group(1); Q.setdefault(cur, [])
            continue
        if not s or 'WORKBOOK' in s or '학력평가' in s or s in ('단계별', 'Learning Guide', '어법·어휘 고르기', '고2') : continue
        if cur is None: continue
        if l.startswith(' ') and not HAN.search(s) and '[' not in s and en:
            ans = [a.strip() for a in s.split(' / ')] if ' / ' in s or True else None
            sent = ' '.join(en); nb = len(re.findall(r'\[', sent))
            assert nb == len(ans), (cur, sent, ans)
            k = iter(ans)
            def rep(mm):
                o = [x.strip() for x in mm.group(1).split(' / ')]; a = next(k); assert len(o) == 2 and a in o, (cur, o, a)
                return '{%s|%s}' % (a, o[1 - o.index(a)])
            Q[cur].append([re.sub(r'\[([^\]]*)\]', rep, sent), ' '.join(ko)]); ko, en = [], []
        elif HAN.search(s): ko.append(s)
        else: en.append(s)
    return Q
if __name__ == '__main__':
    Q = parse('/home/claude/srcrepo/work_src/djmock/oct_wb6.txt')
    for k, v in Q.items(): print(k, len(v), sum(s.count('{') for s, _ in v))
