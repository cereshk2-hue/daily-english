import sys, re
L = open('/home/claude/srcrepo/wrapup/bimi2/u%s.txt' % sys.argv[1]).read().replace('\xad','-').replace('','⟨').replace('','⟩').split('\n')
a, b = (int(sys.argv[2]), int(sys.argv[3])) if len(sys.argv) > 3 else (0, len(L))
for i in range(a, min(b, len(L))):
    l = L[i].rstrip()
    if len(l) > 260:
        u = re.findall(r'(\S{0,3}\s?⟨[^⟩]{0,90}⟩?)', l)
        bl = re.findall(r'.{30}_{5,}.{0,20}|\(\s?[①-⑤]\s?\)|[①-⑤]\s\S+', l)
        print(i, '¶[%d자]' % len(l), ' | '.join(u)[:400] if u else '', ('BL:' + ' '.join(bl)[:200]) if not u else '')
    else: print(i, l[:220])
