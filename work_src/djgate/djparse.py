import re
HAN = re.compile('[가-힣]')
def parse(f):
    L = [l.rstrip() for l in open(f, encoding='utf-8')]
    L = L[:next(i for i, l in enumerate(L) if l.strip() == '본문 10단계 워크북')]
    out, ko, en = [], [], []
    skip = lambda s: (not s or s in ('Lesson', '영어II', '교과서 본문', '│본문│', '워크북 6') or re.match(r'^\d+$', s) or '어법 선택형 연습' in s
                      or s.startswith('2022 개정') or s.startswith('NE능률') or s.startswith('◗'))
    for l in L:
        s = l.strip()
        if skip(s): continue
        if l.startswith(' ') and not HAN.search(s) and '[' not in s and en:
            ans = [a.strip() for a in s.split(' / ')]
            sent = ' '.join(en); assert len(re.findall(r'\[', sent)) == len(ans), (sent, ans)
            k = iter(ans)
            def rep(m):
                o = [x.strip() for x in m.group(1).split(' / ')]; a = next(k); assert len(o) == 2 and a in o, (o, a)
                return '{%s|%s}' % (a, o[1 - o.index(a)])
            out.append((re.sub(r'\[([^\]]*)\]', rep, sent), ' '.join(ko))); ko, en = [], []
        elif HAN.search(s): ko.append(s)
        else: en.append(s)
    assert not en, en
    return out
if __name__ == '__main__':
    import sys
    for i, (s, k) in enumerate(parse(sys.argv[1])): print(i, s)
