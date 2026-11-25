import json,sys,re,html
T={t['id']:t for t in json.load(open('/home/claude/work/agb2_dry.json'))}
C='①②③④⑤'
def tx(s): return re.sub(r'\s+',' ',html.unescape(re.sub(r'<br>','\n',re.sub(r'<(?!br)[^>]+>','',s or '')).replace('<u>','_').replace('</u>','_'))).strip()
for tid in sys.argv[1:]:
    t=T[tid]; seen=set()
    for i in t['items']:
        a=i['ans'] if isinstance(i['ans'],list) else [i['ans']]
        print('### %s n%s [%s] %s'%(tid,i['n'],''.join(C[x] for x in a),tx(i['stem'])))
        c=tx(i.get('ctx',''))
        if c and c not in seen: print('CTX:',c[:1500]); seen.add(c)
        print('BODY:',tx(re.sub('</?u>','_',i['body']))[:1600])
        for k,o in enumerate(i['opts']): print('  ',C[k],tx(o)[:160])
        print('  EX:',i['ex'][:200].replace('\n',' | '))
