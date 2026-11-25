import re,sys
HDR = re.compile(r'^[\s❖]*다음 글을 읽고,? (질문|물음|주어진 문제)에 답하시오')
ANS = re.compile(r'^\s+[①-⑤➀-➄❶-❺⓵-⓹]')
Q = re.compile(r'^(다음|윗글|글의|주어진|밑줄|본문|위 글|빈칸|위의|아래|윗 글)')
def stems(f):
    L=open('u%s.txt'%f,encoding='utf-8').read().split('\n')
    out=[]
    for i,l in enumerate(L):
        endnum = re.search(r'\(\d\d(?:[~\-]\d\d)?번?\)\s*$', l)
        if l.startswith(' ') or HDR.match(l) or not (Q.match(l) or (endnum and re.match(r'[A-Z]', l) and len(l) < 200)): continue
        nxt=L[i+1] if i+1<len(L) else ''
        num=re.search(r'\((\d\d)(?:[~\-]\d\d)?번?\)',l)
        if num or ANS.match(nxt) or l.rstrip().endswith(('?','.','시오')):
            w = bool(re.search(r'쓰시오|채우시오|영작|서술', l))
            out.append((i, num.group(1) if num else '-', 'W' if w else 'M', nxt.strip()[:30], l[:50]))
    return L,out
if __name__=='__main__':
    for f in sys.argv[1:]:
        L,o=stems(f); print('==',f,len(o))
        for k,x in enumerate(o,1): print(k,*x)
