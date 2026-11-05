# 안곡고 고2 모의고사 추가분(10월 모평 · 고3 6월 모평) 한 지문 = 하루 DAY. 문항 헬퍼: 본문 문장에서 바로 만들어 오타를 막는다.
import re
CIR='①②③④⑤'
def box(t): return '<span class="exam-box en">'+t+'</span>'
class P:
    def __init__(s,n,label,sents,foot=''):
        s.n=n; s.label=label; s.E=[a for a,b in sents]; s.K=[b for a,b in sents]; s.foot=foot
    def text(s,ex=None): return ' '.join(s.E if ex is None else ex)
    def sent(s,frag):
        m=[x for x in s.E if frag in x]; assert len(m)>=1,(s.n,frag); return m[0]
    def full(s,t=None): return box((t or s.text())+('<br><small>'+s.foot+'</small>' if s.foot else ''))
    def blank(s,old):
        t=s.text(); assert old in t,(s.n,old); return s.full(t.replace(old,'<u>　　　　　　　　　　</u>',1))
    def under(s,pairs):
        t=s.text()
        for lab,old,new in pairs: assert old in t,(s.n,old); t=t.replace(old,'%s<u>%s</u>'%(lab,new),1)
        return s.full(t)
    def insert_q(s,given,marks):
        out=[]
        for i,x in enumerate(s.E):
            if i==given: continue
            if i in marks: out.append('( %s )'%CIR[marks.index(i)])
            out.append(x)
        return box('<b>주어진 문장</b> '+s.E[given])+s.full(' '.join(out))
    def order_q(s,intro,blocks):
        t='<br>'.join('(%s) %s'%(k,' '.join(s.E[i] for i in v)) for k,v in sorted(blocks.items()))
        return box('<b>주어진 글</b> '+' '.join(s.E[i] for i in intro))+box(t+('<br><small>'+s.foot+'</small>' if s.foot else ''))
ORD=["(A)-(C)-(B)","(B)-(A)-(C)","(B)-(C)-(A)","(C)-(A)-(B)","(C)-(B)-(A)"]
SLOT=["( ① ) 자리","( ② ) 자리","( ③ ) 자리","( ④ ) 자리","( ⑤ ) 자리"]
def EXQ(n,title,boxhtml,opts,a,ex,v=True): return {'n':n,'q':'<b>'+('[변형] ' if v else '')+title+'</b>'+boxhtml,'opts':opts,'keep':True,'a':a,'ex':ex}
def PK(p,frag,right,wrong,ex):
    s=p.sent(frag); assert s.count(right)>=1,(right,s); return {'s':s.replace(right,'{%s|%s}'%(right,wrong),1),'ex':ex}
def VB(p,frag,form,base,ex,alt=()):
    s=p.sent(frag); assert form in s,(form,s); return {'s':s.replace(form,'___',1),'v':base,'a':[form,*alt],'ex':ex}
def ER(p,frag,marks,w,fix,ex):
    """marks: 원문 조각 3개(순서대로). w번째는 틀린 형태 wrong 으로 바꿔 보여 준다: marks[w]=(원문, 틀린형)"""
    s=p.sent(frag); out=s; pos=0
    for i,m in enumerate(marks):
        orig,shown=(m if isinstance(m,tuple) else (m,m))
        j=out.index(orig,pos); out=out[:j]+'[['+shown+']]'+out[j+len(orig):]; pos=j+len(shown)+4
    assert fix==(marks[w][0] if isinstance(marks[w],tuple) else marks[w])
    return {'s':out,'w':w,'fix':fix,'ex':ex}
def BL(p,frag,ans,dis,ex):
    s=p.sent(frag); assert ans in s,(ans,s); return {'s':s.replace(ans,'____',1),'opts':[ans]+dis,'ex':ex}
def TF(p,en,b,ev,ex): assert ev in p.text(),(p.n,ev); return [en,b,ex,p.n,ev]
def MC(p,q,opts,ex,per):
    for x in per: assert not x[1] or x[1] in p.text(),(p.n,x[1])
    return {'n':p.n,'box':[p.label],'q':q,'opts':opts,'ex':ex,'per':per}
G={'pick1':'문맥에 맞는 낱말을 고르세요.','tf':'본문 내용과 일치하면 T, 다르면 F를 고르세요.','mc':'선택지는 본문을 다른 어휘로 바꿔 쓴 문장이에요. 풀고 나서 해설의 어휘를 꼭 확인하세요.',
   'pick2':'어법상 알맞은 것을 고르세요.','verb':'( ) 안의 동사를 알맞은 형태로 바꿔 쓰세요.','error':'어법상 틀린 곳을 고르세요.','scramble':'우리말에 맞게 단어를 눌러 문장을 완성하세요.',
   'order':'문장을 본문 순서대로 눌러서 배열하세요.','insert':'주어진 문장이 들어가기에 가장 알맞은 곳을 고르세요.','odd':'글의 흐름과 관계없는 문장을 고르세요.','blank':'빈칸에 들어갈 말로 가장 알맞은 것을 고르세요.','gram':'알맞은 답을 고르세요.'}
def short(k): return k if len(k)<=34 else k[:32]+'…'
def day(id,name,rng,story,p,m):
    st=[{'type':'vocab','title':'핵심어휘·숙어','quizN':15,'items':[[w,mm,p.n]+x for w,mm,*x in m.VOCAB]},
        {'type':'mc','title':'실전 문항','guide':'시험지 원문항 + 내신형 변형 문항이에요. 지문을 읽고 답을 고르세요.','items':m.EXAM},
        {'type':'pick','title':'어휘선택','guide':G['pick1'],'items':m.PICK1},
        {'type':'tf','title':'T/F 내용 확인','guide':G['tf'],'items':m.TF},
        {'type':'mc','title':'일치·불일치','guide':G['mc'],'items':m.MC},
        {'type':'pick','title':'어법선택','guide':G['pick2'],'items':m.PICK2},
        {'type':'verb','title':'동사변형','guide':G['verb'],'items':m.VERB},
        {'type':'error','title':'오류찾기','guide':G['error'],'items':m.ERR},
        {'type':'scramble','title':'본문 스크램블','guide':G['scramble'],'items':[{'ko':p.K[i],'en':p.E[i]} for i in m.SCR]},
        {'type':'order','title':'문장순서','guide':G['order'],'items':[{'lines':[p.E[i] for i in o],'flow':[short(p.K[i]) for i in o]} for o in m.ORDER]},
        {'type':'insert','title':'문장삽입','guide':G['insert'],'items':[{'lines':[p.E[i] for i in o[0]],'given':o[1],'flow':[short(p.K[i]) for i in o[0]],'ex':o[2]} for o in m.INSERT]},
        {'type':'odd','title':'어색한 문장','guide':G['odd'],'items':[{'lines':[p.E[i] if isinstance(i,int) else i for i in o[0]],'odd':o[1],'ex':o[2]} for o in m.ODD]},
        {'type':'blank','title':'빈칸추론','guide':G['blank'],'items':m.BLANK},
        {'type':'mc','title':'핵심문법','guide':G['gram'],'items':m.GRAM}]
    st=[s for s in st if s['items']]
    return {'id':id,'name':name,'range':rng,'story':story,'passage':[['#',p.label,'']]+[['',e,k] for e,k in zip(p.E,p.K)],'steps':st}
