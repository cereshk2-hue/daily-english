import json, re, sys
B = json.load(open('/home/claude/srcrepo/gen/sk27/book_items.json')); K = json.load(open('/home/claude/srcrepo/gen/sk27/key_items.json'))
l = int(sys.argv[1]); c0 = K['CODE0'][str(l)]; n = len(K['ANS'][str(l)])
recs = K['K'][str(l)]
for i in range(n):
    c = c0 + i; b = B[str(c)]
    print('#### %d (%s) ans %s | %s' % (c, 'G' if i == 0 else 'E%d' % i, K['ANS'][str(l)][i], b['stem']))
    print(re.sub(r'\s+', ' ', b['body'])[:3000])
    for o in b['opts']: print('  ', re.sub(r'\s+', ' ', o))
for r in recs:
    print('---- 해설', r['ans'], '|', r['topic']); print('SOL:', re.sub(r'\s+', ' ', r['sol'])[:500])
