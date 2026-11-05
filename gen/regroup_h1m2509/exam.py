# 11/5 저녁: 32번부터 하루 한 지문 DAY 에 실전(내신형 변형) 문항을 3~4개로 늘리고, 문법 단계는 줄인다. 다시 돌려도 같은 결과(변형 문항은 v:1 로 표시해 지우고 다시 넣음).
import json,subprocess,sys,re
sys.path.insert(0,'/home/claude/work/gen'); from gencommon import write
F='/home/claude/proj/data/h1-mock-2509.js'
P=json.loads(subprocess.check_output(['node','-e',"global.window={};require('%s');console.log(JSON.stringify(window.PKG))"%F]))
src=open(F).read(); head=src[:src.index('window.PKG')]; tail=src[src.index('/* WRAPUP-TESTS'):]
P.pop('tests',None)
D={d['id']:d for d in P['days']}
def S(n): return [r[1] for r in D['q%d'%n]['passage'] if r[0]!='#']
def foot(n):
    m=re.search(r'<small>.*?</small>',D['q%d'%n]['steps'][1]['items'][0]['q']); return ('<br>'+m.group(0)) if m else ''
BOX=lambda t:'<span class="exam-box en">'+t+'</span>'
def full(n,txt=None): return BOX((txt if txt is not None else ' '.join(S(n)))+foot(n))
def under(n,pairs):
    t=' '.join(S(n))
    for lab,old,new in pairs:
        assert t.count(old)>=1,(n,old); t=t.replace(old,'%s<u>%s</u>'%(lab,new),1)
    return full(n,t)
def blank(n,old):
    t=' '.join(S(n)); assert old in t,(n,old); return full(n,t.replace(old,'<u>　　　　　　　　　　</u>',1))
def insert(n,given,marks):
    s=S(n); out=[]
    for i,x in enumerate(s):
        if i==given: continue
        if i in marks: out.append('( %s )'%'①②③④⑤'[marks.index(i)])
        out.append(x)
    return BOX('<b>주어진 문장</b> '+s[given])+full(n,' '.join(out))
def order(n,intro,blocks):  # blocks: {'A':[i..],...}
    s=S(n); t='<br>'.join('(%s) %s'%(k,' '.join(s[i] for i in v)) for k,v in sorted(blocks.items()))
    return BOX('<b>주어진 글</b> '+' '.join(s[i] for i in intro))+BOX(t+foot(n))
ORD=["(A)-(C)-(B)","(B)-(A)-(C)","(B)-(C)-(A)","(C)-(A)-(B)","(C)-(B)-(A)"]
def Q(n,title,box,opts,a,ex): return {'n':n,'v':1,'q':'<b>[변형] '+title+'</b>'+box,'opts':opts,'keep':True,'a':a,'ex':ex}
V={
32:[Q(32,'다음 글의 주제로 가장 적절한 것은?',full(32),[
 "the role of adenosine in controlling our need for sleep","the benefits of sleeping less to do more activities","how caffeine blocks the effects of adenosine","ways to recover quickly from a sleepless night","why some people need more sleep than others"],0,
 "정답 ▶ ① 수면 욕구를 조절하는 아데노신의 역할\n이유: 아데노신은 깨어 있으면 쌓이고(builds up) 자면 분해되어(breaks down), 몸이 잃은 잠을 파악하고 잠을 유발하게 해요. 그래서 적게 자는 데 익숙해질 수 없다는 글 → 아데노신이 수면 욕구를 조절\n오답 ▶ ② 적게 자는 것의 '이점'이 아니라 결국 수면 부족이 따라잡는다는 글 ③ 카페인은 언급 없음 ④ 빨리 회복하는 법이 아니라 '더 오래 자서' 갚아야 함 ⑤ 사람마다 다른 수면량은 언급 없음\n포인트 ▶ 주제 = 글 전체에 반복되는 핵심어(adenosine, sleep debt)를 담은 선택지"),
    Q(32,'다음 글의 밑줄 친 부분 중, 문맥상 낱말의 쓰임이 적절하지 <u>않은</u> 것은?',under(32,[('(a)','overwhelming','overwhelming'),('(b)','builds up','builds up'),('(c)','trigger','trigger'),('(d)','longer','shorter'),('(e)','accustomed','accustomed')]),
 ["(a) overwhelming","(b) builds up","(c) trigger","(d) shorter","(e) accustomed"],3,
 "정답 ▶ (d) shorter → longer\n이유: 며칠 밤 잠이 부족하면 수면 빚이 쌓이고, 그 빚은 평소보다 '더 오래(longer)' 자서 갚아야 해요. 더 짧게 자서 갚는다는 건 말이 안 돼요.\n오답 ▶ (a) 결국 잠의 필요가 '압도적'이 됨 ✔ (b) 깨어 있을수록 '쌓임' ✔ (c) 필요할 때 잠을 '유발' ✔ (e) 적게 자는 데 '익숙해질' 수 없음 ✔\n포인트 ▶ make up a sleep debt 수면 빚을 갚다 = sleep longer than normal")],
33:[Q(33,'다음 글의 요지로 가장 적절한 것은?',full(33),[
 "어떤 수치가 정확한지는 그것을 사용하려는 목적에 따라 달라진다.","과학적 측정값에는 항상 유효 숫자가 많이 포함되어야 한다.","지구와 태양 사이의 거리는 정확히 측정하는 것이 불가능하다.","일반 대중은 과학자보다 불확실성을 더 잘 이해한다.","위성을 발사하려면 일출 시각을 정확히 알아야 한다."],0,
 "정답 ▶ ① 어떤 수치가 정확한지는 그것을 사용하려는 목적에 따라 달라진다.\n이유: 첫 문장(불확실성의 중요성은 상대적)과 Whether or not the quoted number is \"precise\" therefore depends on what I'm intending to do with it.이 요지예요. 일출 시각엔 충분, 위성엔 부족이라는 예시가 뒷받침해요.\n오답 ▶ ② 유효 숫자를 늘리라는 주장 없음 ③ 불가능하다고 하지 않음 ④ 대중은 불확실성을 이해하기 '어렵다'(difficult) ⑤ 위성과 일출은 서로 다른 목적의 예시\n포인트 ▶ 요지는 therefore(그러므로)가 있는 문장에 자주 있어요."),
    Q(33,'글의 흐름으로 보아, 주어진 문장이 들어가기에 가장 적절한 곳은?',insert(33,3,[1,2,4,5,6]),["( ① ) 자리","( ② ) 자리","( ③ ) 자리","( ④ ) 자리","( ⑤ ) 자리"],2,
 "정답 ▶ ③\n이유: 주어진 문장은 However(그러나)로 '정확해 보인다(This seems relatively precise)'를 뒤집어요. 그래서 그 문장 바로 뒤예요. 그리고 '오차가 뉴욕-시카고 거리보다 크다' → therefore '정확한지는 목적에 달려 있다'로 이어져요.\n오답 ▶ ① ② 아직 숫자도, '정확해 보인다'는 말도 나오기 전 ④ ⑤ 이미 결론(therefore)과 예시가 나온 뒤\n포인트 ▶ 통념(정확해 보임) → However → 반전 → therefore 결론")],
34:[Q(34,'다음 글의 제목으로 가장 적절한 것은?',full(34),[
 "The Hidden Fossil Fuel Cost of Going Green","Why Solar Panels Are Cheaper Than Ever","Fossil Fuels: An Energy Source of the Past","How Concrete Helps Reduce Global Emissions","A Journalist Who Opposes Renewable Energy"],0,
 "정답 ▶ ① 친환경 전환에 숨겨진 화석 연료 비용\n이유: 재생 에너지 기반 시설을 지으려면 콘크리트·철강·광물 채굴에 화석 연료가 필요하고, 이 비용이 전환 제안서에서 좀처럼 계산되지 않는다(seldom counted)는 글 → hidden cost(숨겨진 비용)\n오답 ▶ ② 태양 전지판은 희귀하고 비싼(scarce and expensive) 광물이 필요 ③ 화석 연료는 오히려 지금 꼭 필요함 ④ 콘크리트 생산은 화석 에너지를 씀 ⑤ Heinberg는 재생 에너지를 반대하는 게 아니라 비용을 지적함\n포인트 ▶ go green 친환경으로 전환하다"),
    Q(34,'다음 글에서 전체 흐름과 관계 <u>없는</u> 문장은?',full(34,' '.join(S(34)[:2])+' ①'+S(34)[2]+' ②'+S(34)[3]+' ③Wind turbines, in particular, have become popular tourist attractions in many countries. ④'+S(34)[4]+' ⑤'+S(34)[5]+' '+' '.join(S(34)[6:])),["①","②","③","④","⑤"],2,
 "정답 ▶ ③\n이유: 글은 '재생 에너지 기반 시설을 짓는 데도 화석 연료가 필요하다'는 흐름이에요(콘크리트·철강 → 태양 전지판 광물). 풍력 터빈이 관광 명소가 됐다는 문장은 이 흐름과 관계없어요.\n오답 ▶ ① 화석 연료 없이는 불가능 ② 콘크리트·철강의 예 ④ 태양 전지판 광물의 예 ⑤ 그러므로 화석 에너지를 더 빨리 씀\n포인트 ▶ 무관한 문장은 글의 핵심어(fossil fuels)를 빼고 소재(wind turbines)만 겹치게 만들어요.")],
35:[Q(35,'다음 글의 주제로 가장 적절한 것은?',full(35),[
 "the long history of the human dream of thinking machines","the dangers of artificial intelligence in modern society","how the Turing test is carried out today","the role of myths in ancient Greek religion","the differences between robots and automatons"],0,
 "정답 ▶ ① 생각하는 기계를 향한 인간의 오랜 꿈의 역사\n이유: 고대 그리스 신화 → 문학 → 1950년 Turing → McCarthy의 '인공지능' 용어 → 오늘날 AI까지 시간 순서로 설명하는 글\n오답 ▶ ② 위험성 언급 없음 ③ 테스트 방법은 설명 안 함 ④ 신화는 예시일 뿐 ⑤ 로봇과 자동 장치의 차이는 언급 없음\n포인트 ▶ 연도·시대 표현(for centuries, since ancient Greece, In 1950, A few years later, Since then)이 이어지면 '역사'가 주제"),
    Q(35,'주어진 글 다음에 이어질 글의 순서로 가장 적절한 것은?',order(35,[0],{'A':[3],'B':[1,2],'C':[4,5]}),ORD,1,
 "정답 ▶ ② (B)-(A)-(C)\n이유: 주어진 글(인간은 수 세기 동안 생각하는 기계를 꿈꿈) → (B) 고대 그리스 신화, 마찬가지로(Likewise) 문학 → (A) 1950년 Turing → (C) 몇 년 후(A few years later) McCarthy, 그 이후(Since then) 오늘날 AI\n포인트 ▶ A few years later는 '1950년'이 앞에 있어야 쓸 수 있어요 → (A) 다음 (C)")],
36:[Q(36,'다음 글의 제목으로 가장 적절한 것은?',full(36),[
 "The Desert Tortoise's Secrets for Surviving Heat and Thirst","Why Desert Tortoises Love the Summer Heat","How to Help Tortoises Cross the Road Safely","The Fastest Animals in Death Valley","Hibernation: A Serious Danger to Desert Reptiles"],0,
 "정답 ▶ ① 사막거북이 더위와 갈증을 이겨 내는 비밀\n이유: 더위는 피하고(동면·굴), 물은 정교한 방광에 저장해 1년을 버틴다는 글\n오답 ▶ ② 더위를 '피함'(avoids) ③ 오히려 돕지 말라(not to stop and help)는 당부 ④ slow-moving(느림보) ⑤ 동면은 생존 방법\n포인트 ▶ 제목은 글 전체(더위 + 물)를 덮어야 해요."),
    Q(36,'글의 흐름으로 보아, 주어진 문장이 들어가기에 가장 적절한 곳은?',insert(36,6,[2,4,5,7,8]),["( ① ) 자리","( ② ) 자리","( ③ ) 자리","( ④ ) 자리","( ⑤ ) 자리"],3,
 "정답 ▶ ④\n이유: 주어진 문장의 the tortoise's bladder는 바로 앞 문장(정교한 방광에 의존한다)에서 처음 나온 방광을 받아요. 그리고 '물을 재흡수한다' → '놀랍게도(Incredibly) 1년 동안 물 없이 지낸다'로 이어져요.\n오답 ▶ ① ② ③ 방광이 아직 나오기 전 ⑤ '1년을 버틴다'는 결과가 이미 나온 뒤\n포인트 ▶ 처음 나오는 대상(its highly sophisticated bladder) → 그 대상 설명(the tortoise's bladder)")],
37:[Q(37,'다음 글의 주제로 가장 적절한 것은?',full(37),[
 "how friction slows down moving objects such as bicycles","the importance of wearing a helmet while cycling","why air resistance helps bicycles move faster","the history of bicycle brakes","how to make a cart move without any friction"],0,
 "정답 ▶ ① 마찰력이 자전거 같은 움직이는 물체를 느리게 하는 방식\n이유: 페달을 멈추면 느려짐 → 브레이크의 마찰 → 브레이크 없이도 바퀴-축 마찰, 공기 저항 → 수레에도 적용. 모두 '마찰력이 느리게 한다'는 이야기\n오답 ▶ ② 헬멧 언급 없음 ③ 공기 저항은 뒤로 밂(backwards) ④ 브레이크의 역사 아님 ⑤ 마찰 없애는 법은 없음\n포인트 ▶ 핵심어 friction이 반복돼요."),
    Q(37,'다음 빈칸에 들어갈 말로 가장 적절한 것은?',blank(37,'opposite to movement'),[
 "opposite to movement","of the wind","the rider chooses","toward the ground","the same as the wheels"],0,
 "정답 ▶ ① 움직임과 반대인\n이유: 빈칸 바로 뒤 that is backwards(즉, 뒤쪽으로)가 결정적 단서. 앞으로 가는 자전거를 '반대 방향'으로 당겨서 느리게 해요. 공기 저항도 pushing you backwards.\n오답 ▶ ② 바람 방향 ③ 타는 사람이 고르는 방향 ④ 땅 쪽 ⑤ 바퀴와 같은 방향 → 모두 '뒤쪽'과 맞지 않아요.\n포인트 ▶ that is(즉) 뒤는 앞말을 다시 풀어 쓴 말")],
38:[Q(38,'다음 글의 제목으로 가장 적절한 것은?',full(38),[
 "Nonlinear Editing: Faster, Easier, and More Flexible","Why Typewriters Are Still Better for Writers","The Decline of Special Effects in Modern Films","How to Rewind Videotape Without Damaging It","Linear Editing: The Future of Video Production"],0,
 "정답 ▶ ① 비선형 편집: 더 빠르고, 쉽고, 유연하다\n이유: 특수 효과, 임의 접근(원하는 장면을 바로 찾음), 장면 추가·삭제와 길이 자동 조정, 워드 프로세서처럼 쉬운 수정 → 비선형 편집의 장점\n오답 ▶ ② 타자기는 '불편한' 선형 편집의 비유 ③ 특수 효과는 장점으로 소개 ④ 되감기는 필요 없어짐 ⑤ 선형 편집은 과거의 방식\n포인트 ▶ flexible 유연한"),
    Q(38,'주어진 글 다음에 이어질 글의 순서로 가장 적절한 것은?',order(38,[0],{'A':[6,7],'B':[1,2,3],'C':[4,5]}),ORD,2,
 "정답 ▶ ③ (B)-(C)-(A)\n이유: 주어진 글(이제 모든 편집은 비선형) → (B) 비선형의 장점들(특수 효과, Another highlight, 추가·삭제) → (C) 선형 편집은 타자기 같았다(과거시제 was) → (A) 반면에(on the other hand) 비선형은 워드 프로세서 같다\n포인트 ▶ on the other hand는 앞에 대조 대상(선형=타자기)이 있어야 해요 → (C) 다음 (A)")],
39:[Q(39,'다음 글의 요지로 가장 적절한 것은?',full(39),[
 "도덕적으로 선한 사람이 되려면 좋은 의도와 함께 실제 결과도 필요하다.","도덕적 판단에서는 행동의 결과가 아니라 의도만이 기준이다.","우연히 해를 막은 사람도 도덕적으로 칭찬받아야 한다.","도덕적 판단의 기준은 사회의 관습에 따라 달라진다.","좋은 행동을 하는 것보다 나쁜 행동을 피하는 것이 더 중요하다."],0,
 "정답 ▶ ① 도덕적으로 선한 사람이 되려면 좋은 의도와 함께 실제 결과도 필요하다.\n이유: 앞부분은 의도와 동기가 중요하다(우연히 해를 막은 사람은 선하지 않음), 뒷부분은 But actual consequences are important(늘 실패하는 사람도 선하다고 여겨지지 않음). 둘 다 필요하다는 글\n오답 ▶ ② 칸트의 입장, 필자는 contrary to Kant ③ is not morally good ④ 관습 이야기 아님 ⑤ 둘을 비교하지 않음\n포인트 ▶ but, contrary to ~ 뒤에 필자의 진짜 생각"),
    Q(39,'다음 빈칸에 들어갈 말로 가장 적절한 것은?',blank(39,'intentions and motives'),[
 "intentions and motives","wealth and status","friends and family","appearance and manners","age and gender"],0,
 "정답 ▶ ① 의도와 동기\n이유: 바로 다음 문장이 '선한 사람은 선을 행하려고 의도해야(intend) 한다', 그다음이 '의도치 않게(unintentionally) 해를 막은 사람은 선하지 않다'예요. 모두 '의도'에 관한 이야기\n오답 ▶ ② 부와 지위 ③ 친구와 가족 ④ 외모와 예절 ⑤ 나이와 성별 → 글에서 다루지 않아요.\n포인트 ▶ 빈칸 뒤 문장들에서 반복되는 말(intend, unintentionally)을 찾기")],
40:[Q(40,'다음 글의 제목으로 가장 적절한 것은?',full(40),[
 "Why We Can't See the World Like a Camera","How to Take Better Photographs of Tools","Cameras: Machines That Understand Our Priorities","The Hammer: The Most Useful Tool in History","Flat Photographs Are Easier to Understand"],0,
 "정답 ▶ ① 우리가 카메라처럼 세상을 보지 못하는 이유\n이유: 우리는 선입견과 사물과의 기능적 관계 때문에 '쓸 준비된' 각도로 보지만, 카메라는 치우침 없이(impartially) 기록해요. 그래서 '카메라처럼 보는 능력'이 방해받는다는 글\n오답 ▶ ② 사진 잘 찍는 법 아님 ③ 카메라는 우선순위를 모름(mechanical indifference) ④ 망치는 예시일 뿐 ⑤ 평면이라 알아볼 수 '없는' 부분이 생김\n포인트 ▶ see \"like a camera\"가 핵심 표현"),
    Q(40,'다음 글의 밑줄 친 부분 중, 문맥상 낱말의 쓰임이 적절하지 <u>않은</u> 것은?',under(40,[('(a)','unconscious','unconscious'),('(b)','profile','profile'),('(c)','interfere','help'),('(d)','impartially','impartially'),('(e)','unrecognizable','unrecognizable')]),
 ["(a) unconscious","(b) profile","(c) help","(d) impartially","(e) unrecognizable"],2,
 "정답 ▶ (c) help → interfere\n이유: 사물과의 기능적 관계가 만든 시각적 기대는 '카메라처럼' 보는 능력을 '방해해요(interfere with)'. 돕는다(help)면 글의 흐름(우리는 카메라처럼 못 본다)과 반대예요.\n오답 ▶ (a) '무의식적' 위계 ✔ (b) '옆모습'으로 떠올림 ✔ (d) 카메라는 '치우침 없이' 기록 ✔ (e) 평면이라 '알아볼 수 없는' 색과 형태 ✔\n포인트 ▶ interfere with ~을 방해하다")],
41:[Q(41,'다음 글의 요지로 가장 적절한 것은?',full(41),[
 "판매원은 고객이 압박감 없이 편안하게 둘러볼 수 있도록 다가가야 한다.","판매원은 고객에게 먼저 \"도와드릴까요?\"라고 물어야 한다.","고객은 판매원의 도움을 거절해서는 안 된다.","판매원은 고객이 매장을 떠날 때까지 곁에 머물러야 한다.","선물을 사는 고객에게는 특별 할인을 해 주어야 한다."],0,
 "정답 ▶ ① 판매원은 고객이 압박감 없이 편안하게 둘러볼 수 있도록 다가가야 한다.\n이유: \"May I help you?\"는 고객을 방어적으로 만들고, 압박을 느끼면 팔 수 없으니(won't make any sales) 서두를 필요 없는 편안한 환경(a comfortable environment that makes customers feel there is no rush)을 만들어야 한다는 글\n오답 ▶ ② 최악의 네 단어라고 함 ③ 거절하는 건 자연스러운 반응으로 설명 ④ 명함을 주고 필요할 때 찾을 수 있게(accessible) ⑤ 할인 언급 없음\n포인트 ▶ has to, should가 있는 문장이 요지"),
    Q(41,'다음 빈칸에 들어갈 말로 가장 적절한 것은?',blank(41,'there is no rush'),[
 "there is no rush","they have no choice","they must buy something today","someone is watching them","a better store is nearby"],0,
 "정답 ▶ ① 서두를 필요가 없다\n이유: 바로 앞 문장 '고객이 압박을 받거나 궁지에 몰렸다고 느끼면 팔 수 없다' → 그러니 '편안한(comfortable)' 환경, 즉 '서두르지 않아도 된다'고 느끼게 해야 해요. 다음 문장의 '그냥 둘러봐도 괜찮다'와도 연결\n오답 ▶ ② ③ ④ 모두 압박감을 주는 말 ⑤ 다른 가게 이야기는 없음\n포인트 ▶ comfortable ↔ pressured, cornered")]}
for n,qs in V.items():
    d=D['q%d'%n]; st=d['steps'][1]; assert st['title']=='실전 문항'
    st['items']=[x for x in st['items'] if not x.get('v')]+qs
    st['guide']='시험지 원문항 + 내신형 변형 문항이에요. 지문을 읽고 답을 고르세요.'
    for s in d['steps']:
        cap={'어법선택':7,'동사변형':4,'오류찾기':4,'핵심문법':4}.get(s['title'])
        if cap: s['items']=s['items'][:cap]
    print(d['id'],len(st['items']),sum(len(s['items']) for s in d['steps']))
write(P,F,head); open(F,'a').write(tail)
