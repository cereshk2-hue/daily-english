# 원본 보기: 긴 줄은 처음만 전체, 이후는 가장 비슷한 앞 줄과 다른 낱말만
import sys, difflib, re
L = open('/home/claude/srcrepo/wrapup/bimi4/u%s.txt' % sys.argv[1]).read().replace('\xad','-').replace('','⟨').replace('','⟩').split('\n')
a, b = (int(sys.argv[2]), int(sys.argv[3])) if len(sys.argv) > 3 else (0, len(L))
seen = []
for i, l in enumerate(L):
    if len(l) < 300:
        if a <= i < b: print(i, l.rstrip()[:400])
        continue
    best = max(seen, key=lambda s: difflib.SequenceMatcher(None, s[1][:600], l[:600]).quick_ratio(), default=None)
    if best and difflib.SequenceMatcher(None, best[1], l).ratio() > .75:
        w1, w2 = best[1].split(), l.split(); out = []
        for op, i1, i2, j1, j2 in difflib.SequenceMatcher(None, w1, w2).get_opcodes():
            if op != 'equal': out.append('[%s → %s]' % (' '.join(w1[i1:i2])[:80], ' '.join(w2[j1:j2])[:200]))
        if a <= i < b: print(i, '≈L%d' % best[0], ' '.join(out)[:1500])
    else:
        if a <= i < b: print(i, l.rstrip())
    seen.append((i, l))
