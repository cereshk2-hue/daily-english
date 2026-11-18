import re,json
Q=open('q.txt',encoding='utf-8').read().split('\n'); A=open('a.txt',encoding='utf-8').read().split('\n')
ans={}
for l in A:
    m=re.match(r'^\s*(\d+)\s*번\s*-\s*(.*)$',l)
    if m: ans[int(m.group(1))]=m.group(2).strip()
items=[];cur=None;expect=1
for l in Q:
    m=re.match(r'^\s*(\d+)\.\s+(.*)$',l)
    if m and int(m.group(1))==expect:
        cur={'n':expect,'stem':m.group(2),'lines':[]}; items.append(cur); expect+=1; continue
    if cur: cur['lines'].append(l)
for it in items:
    L=it.pop('lines'); opts=[]
    while L and re.match(r'^\s*[①②③④⑤]',L[-1]) and len(opts)<5: opts.insert(0,L.pop().strip())
    it['opts']=opts; it['body']='\n'.join(L); it['ans']=ans.get(it['n'],'?')
json.dump(items,open('items.json','w'),ensure_ascii=False,indent=0)
seen={}
with open('review.txt','w',encoding='utf-8') as f:
  for i in items:
    b=i['body'].strip(); key=re.sub(r'\s+',' ',b)
    if len(key)>250:
        if key in seen: b='[=본문 #%d 와 같음]'%seen[key]
        else: seen[key]=i['n']
    f.write('### %d %s\n'%(i['n'],i['stem']))
    if b: f.write(b+'\n')
    for o in i['opts']: f.write(o+'\n')
    f.write('>> ANS '+i['ans'][:230]+'\n')
print(len(items),[i['n'] for i in items if len(i['opts'])!=5])
