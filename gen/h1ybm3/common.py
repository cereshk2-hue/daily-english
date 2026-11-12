import json,re
import sents
S,K,SEC=sents.S,sents.K,sents.SEC
TITLES={'❶':('Katherine Johnson, a "Computer" Who Looked Beyond Numbers',"숫자 너머를 본 '컴퓨터' 캐서린 존슨"),'❷':None,'❸':None,'❹':None,'❺':None}
def passage(secs):
    rows=[]
    for sec in secs:
        rows.append(['',sec,''])
        if TITLES[sec]: rows.append(['',TITLES[sec][0],TITLES[sec][1]])
        es,ks=SEC[sec]; rows+= [['',e,k] for e,k in zip(es,ks)]
    return rows
G={'vocab':'', 'pick1':'문맥에 맞는 낱말을 고르세요.','tf':'본문 내용과 일치하면 T, 다르면 F를 고르세요.',
   'mc':'선택지는 본문을 다른 어휘로 바꿔 쓴 문장이에요. 풀고 나서 해설의 어휘를 꼭 확인하세요.','pick2':'어법상 알맞은 것을 고르세요.',
   'verb':'( ) 안의 동사를 알맞은 형태로 바꿔 쓰세요.','error':'어법상 틀린 곳을 고르세요.','scramble':'우리말에 맞게 단어를 눌러 문장을 완성하세요.',
   'order':'문장을 본문 순서대로 눌러서 배열하세요.','insert':'주어진 문장이 들어가기에 가장 알맞은 곳을 고르세요.','odd':'글의 흐름과 관계없는 문장을 고르세요.',
   'blank':'빈칸에 들어갈 말로 가장 알맞은 것을 고르세요.','gram':'알맞은 답을 고르세요.',
   'content':'주제·제목·지칭·심경·추론·요약까지, 본문 내용을 여러 각도로 물어요.','abc':'주어진 글 다음에 이어질 순서를 고르세요. 연결어·지시어(This, There, That)가 열쇠예요.'}
def sx(c): return S[c] if isinstance(c,str) and re.fullmatch(r'[A-E]\d+',c) else c
def day(id,name,rng,story,secs,m):
    st=[]
    st.append({'type':'vocab','title':'핵심어휘·숙어','quizN':15,'items':m.VOCAB})
    st.append({'type':'pick','title':'어휘선택','guide':G['pick1'],'items':m.PICK1})
    st.append({'type':'tf','title':'T/F 내용 확인','guide':G['tf'],'items':m.TF})
    st.append({'type':'mc','title':'일치·불일치','guide':G['mc'],'items':m.MC})
    # 11/12 중산고: 문법(어법선택·동사변형·오류찾기·핵심문법)·스크램블 뺌 → 내용 다각도 + 순서·삽입 강화 (content.py)
    import content; C={'y1':content.D1,'y2':content.D2,'y3':content.D3}[id]
    st.append({'type':'mc','title':'내용 다각도','guide':G['content'],'items':C['CONTENT']})
    st.append({'type':'order','title':'문장순서','guide':G['order'],'items':[{'lines':[S[c] for c in o[0]],'flow':o[1]} for o in m.ORDER+C['ORDER']]})
    st.append({'type':'mc','title':'순서 실전','guide':G['abc'],'items':C['ABC']})
    st.append({'type':'insert','title':'문장삽입','guide':G['insert'],'items':[{'lines':[S[c] for c in o[0]],'given':o[1],'flow':o[2],'ex':o[3]} for o in m.INSERT+C['INSERT']]})
    st.append({'type':'odd','title':'어색한 문장','guide':G['odd'],'items':[{'lines':[sx(c) for c in o[0]],'odd':o[1],'ex':o[2]} for o in m.ODD+C['ODD']]})
    st.append({'type':'blank','title':'빈칸추론','guide':G['blank'],'items':m.BLANK})
    return {'id':id,'name':name,'range':rng,'story':story,'passage':passage(secs),'steps':st}
