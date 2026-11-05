import json,sys,os,importlib.util,subprocess
sys.path.insert(0,'/home/claude/work/gen')
from gencommon import write
B=json.load(open('base.json'))
STORY={32:'32 빈칸',33:'33 빈칸',34:'34 빈칸',35:'35 무관한 문장',36:'36 글의 순서',37:'37 글의 순서',38:'38 문장 삽입',39:'39 문장 삽입',40:'40 요약문',41:'41 · 42 장문 (제목 · 어휘)'}
def load(n):
    p='add/a%d.py'%n
    if not os.path.exists(p): return None
    sp=importlib.util.spec_from_file_location('a%d'%n,p); m=importlib.util.module_from_spec(sp); sp.loader.exec_module(m); return m
days=[]; added={}
# 38번에 붙어 있던 'interfere with' 문법은 40번 지문 표현이라 40번으로
g38=next(s for s in B['per']['38']['steps'] if s['title']=='핵심문법'); mv=[x for x in g38['items'] if 'interfere' in x['q']]
g38['items']=[x for x in g38['items'] if x not in mv]
next(s for s in B['per']['40']['steps'] if s['title']=='핵심문법')['items'][:0]=mv
for i,n in enumerate([32,33,34,35,36,37,38,39,40,41]):
    b=B['per'][str(n)]; P=[r for r in b['passage'] if r[0]!='#']; S=[r[1] for r in P]; K=[r[2] for r in P]
    lab=b['passage'][0][1]; steps=b['steps']; st={s['title']:s for s in steps}
    m=load(n); cnt=0
    def put(title,items):
        global cnt
        st[title]['items'].extend(items); cnt+=len(items)
    if m:
        G=lambda k:getattr(m,k,[])
        put('일치·불일치',[dict(n=n,box=[lab],**x) for x in G('MC')])
        put('T/F 내용 확인',[[t[0],t[1],t[2],n,t[3]] for t in G('TF')])
        put('어휘선택',G('PICK1')); put('어법선택',G('PICK2')); put('동사변형',G('VERB')); put('오류찾기',G('ERR'))
        put('본문 스크램블',[{'ko':K[j],'en':S[j]} if isinstance(j,int) else {'ko':j[0],'en':j[1]} for j in G('SCR')])
        put('문장순서',[{'lines':[S[j] for j in o['idx']],'flow':o['flow']} for o in G('ORDER')])
        put('문장삽입',[{'lines':[S[j] for j in o['idx']],'given':o['given'],'flow':o['flow'],'ex':o['ex']} for o in G('INSERT')])
        put('어색한 문장',[{'lines':[S[j] if isinstance(j,int) else j for j in o['lines']],'odd':o['odd'],'ex':o['ex']} for o in G('ODD')])
        put('빈칸추론',G('BLANK'))
        if G('GRAM') and '핵심문법' not in st:
            g=dict(next(s for s in B['per']['32']['steps'] if s['title']=='핵심문법')); g['items']=[]
            steps.insert([s['title'] for s in steps].index('요약문 완성'),g); st['핵심문법']=g
        put('핵심문법',G('GRAM'))
        for extra in getattr(m,'EXTRA',[]): put(extra[0],extra[1])
    VOCTX={32:{'be due to':'due, in part, to'},39:{'think of A as B':'thought of as'},41:{'on -ing':'on hearing'}}
    for w in st['핵심어휘·숙어']['items']:
        if w[0] in VOCTX.get(n,{}): w[3:]=[VOCTX[n][w[0]]]
    added[n]=cnt
    steps=[s for s in steps if s['items']]
    days.append({'id':'q%d'%n,'name':'DAY %d'%(6+i),'range':'41·42번' if n==41 else '%d번'%n,'story':STORY[n],'passage':b['passage'],'steps':steps})
PK=B['pk']; PK.pop('days',None); PK.pop('tests',None)
PK['days']=B['head']+days
src=open('orig_h1-mock-2509.js').read(); tail=src[src.index('/* WRAPUP-TESTS'):]
head='''/* 고1 2025학년도 9월 전국연합학력평가(인천광역시교육청 주관) 영어 18~24 · 26 · 29~42번
   DAY 1~5 는 gen_h1m2509.py / gen_h1m2509b.py, 32~42번은 gen_h1m2509c.py 로 만든 뒤
   gen/regroup_h1m2509 (assign.js → base.js → add/aNN.py → merge.py) 로 32번부터 하루 한 지문(DAY 6~15)으로 나누고 문항을 보강함.
   이 파일이 이제 원본(평평한 JSON). 고칠 때는 이 파일을 직접 고치거나 merge.py 를 다시 돌릴 것.
*/
'''
out=sys.argv[1] if len(sys.argv)>1 else '/home/claude/proj/data/h1-mock-2509.js'
write(PK,out,head); open(out,'a').write(tail)
for d in days: print(d['id'],d['range'],len(d['steps']),sum(len(s['items']) for s in d['steps']),'+%d'%added[int(d['id'][1:])])
