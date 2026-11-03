import re
BRK = set('that which who whom whose when where because and but so to in on at for with by from about during through as since after before including featuring if while than into like'.split())
def chunks(s, lo=2, hi=4):
    W = s.split()
    out, cur = [], []
    for i, w in enumerate(W):
        lw = re.sub(r'[^a-z]', '', w.lower())
        if cur and lw in BRK and len(cur) >= lo: out.append(cur); cur = []
        cur.append(w)
        if (w.endswith(',') or w.endswith(';')) and len(cur) >= lo: out.append(cur); cur = []
        elif len(cur) >= hi: out.append(cur); cur = []
    if cur:
        if out and len(cur) < lo: out[-1] += cur
        else: out.append(cur)
    # 1단어 덩어리는 뒤(없으면 앞)에 붙인다
    res = []
    for c in out:
        if res and len(res[-1]) < lo: res[-1] += c
        else: res.append(c)
    if len(res) > 1 and len(res[-1]) < lo: res[-2] += res.pop()
    return [' '.join(c) for c in res]
if __name__ == '__main__':
    import sys
    for l in sys.stdin: print(' / '.join(chunks(l.strip())))
