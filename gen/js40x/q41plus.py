# 11/27 중산고1 DAY 15(41·42번) 내용 문제 보강: '일치·불일치' 단계 뒤에 'T/F 심화' 14 + '내용 일치·불일치 심화' 7 끼워 넣음
# 데이터 본체는 그대로, /* Q41-PLUS */ 꼬리 블록이 불러올 때 q41 단계에 끼움(같은 제목은 먼저 지워서 여러 번 돌려도 하나)
import json, re
path = '/home/claude/proj/data/h1-mock-2509.js'
TF = [
 ("The writer thinks \"May I help you?\" makes customers more willing to talk.", False, "고객이 말하도록 장려하지 않아요(don't encourage the customer to talk).", "they don't encourage the customer to talk"),
 ("\"May I help you?\" often ends a sale before it really begins.", True, "판매 거래를 완전히 멈춰 버리는(stops cold) 부정적 반응을 끌어내요.", "draw out a negative response that stops cold a sales transaction"),
 ("\"Is there anything in particular that you are looking for?\" is suggested as a better opening question.", True, "더 나은 질문의 예로 나와요.", "Examples of better questions to use when approaching customers are \"Is there anything in particular that you are looking for?\""),
 ("Customers usually believe that a salesperson who says \"May I help you?\" really cares about them.", False, "반대예요. 판매원이 관심이 없다고(didn't care) 느낄 거예요.", "chances are you would feel the salesperson didn't care"),
 ("Untrained salespeople rarely use the line \"May I help you?\"", False, "rarely(거의 안 함) ✘ → so overused(너무 남용)예요.", "so overused by untrained and uninterested salespeople"),
 ("The question \"May I help you?\" makes customers feel as if they need to be rescued.", True, "곤경에 처해 구조가 필요하다(needs rescuing)는 것을 암시해요.", "implies that the customer is in trouble of some sort and needs rescuing"),
 ("Customers usually say \"No, thank you\" only after thinking about it for a long time.", False, "오래 생각한 뒤 ✘ → 즉각적인(immediate) 반응이에요.", "\"No, thank you\" is usually the immediate response"),
 ("Customers sometimes refuse help even when they actually need it.", True, "실제로 도움이 필요하더라도(even if) 'No, thank you'라고 해요.", "even if the customer is actually in need of assistance"),
 ("Customers often feel they are not smart enough to decide what they want.", False, "반대예요. 원하는 걸 알아낼 만큼 충분히 똑똑하다고(smart enough) 생각해요.", "I'm smart enough to figure out what I want"),
 ("Making customers feel cornered helps salespeople close more deals.", False, "궁지에 몰리면(cornered) 아무것도 팔지 못해요.", "If customers feel pressured or cornered, then salespeople won't make any sales."),
 ("A good approach lets customers feel that they don't have to hurry.", True, "서두를 필요가 없다고(no rush) 느끼게 하는 편안한 환경이에요.", "makes customers feel there is no rush"),
 ("Salespeople should never answer questions from customers who want to look around alone.", False, "질문이나 걱정거리가 생길 경우에 대비해 다가갈 수 있게(accessible) 있어야 해요.", "keep themselves accessible in case customers have questions or concerns"),
 ("The passage suggests that salespeople should respect customers' wish to browse on their own.", True, "그냥 둘러봐도 괜찮다고 느끼게 하고, 혼자 둘러보려 하면 명함을 건네고 물러나 있어요.", "if customers just want to look around, they should feel that it is all right to do so"),
 ("Business cards are recommended for customers who are in a hurry to buy something.", False, "서두르는 고객 ✘ → 정말 혼자 둘러보고 싶어 하는 고객에게 건네요.", "In situations where customers really do want to look around on their own, salespeople should give customers their business cards"),
]
# (질문, [(선택지, 해석, 근거, 판정)], 정답 index=0, 이유)
MC = [
 ("글의 내용과 일치하는 것은?", [
   ("A salesperson's approach should make customers feel there is no need to hurry.", "판매원의 접근은 고객이 서두를 필요가 없다고 느끼게 해야 한다.", "promote a comfortable environment that makes customers feel there is no rush", "일치"),
   ("\"May I help you?\" helps customers start a conversation easily.", "'도와드릴까요?'는 고객이 쉽게 대화를 시작하게 돕는다.", "they don't encourage the customer to talk", "불일치"),
   ("Customers feel that a salesperson asking \"May I help you?\" is kind.", "고객은 '도와드릴까요?'라고 묻는 판매원이 친절하다고 느낀다.", "you would feel the salesperson didn't care", "불일치"),
   ("\"No, thank you\" means the customer needs no help at all.", "'아뇨, 괜찮아요'는 고객이 도움이 전혀 필요 없다는 뜻이다.", "even if the customer is actually in need of assistance", "불일치"),
   ("Salespeople should stay right next to customers who browse alone.", "판매원은 혼자 둘러보는 고객 바로 옆에 있어야 한다.", "give customers their business cards and keep themselves accessible", "불일치")],
  "편안하고 서두를 필요 없는(no rush) 환경을 만들어야 해요."),
 ("글의 내용과 일치하지 <u>않는</u> 것은?", [
   ("Experienced and enthusiastic salespeople are the ones who mostly use \"May I help you?\"", "경험 많고 열정적인 판매원이 주로 '도와드릴까요?'를 쓴다.", "so overused by untrained and uninterested salespeople", "불일치"),
   ("The question suggests that the customer is in some kind of trouble.", "그 질문은 고객이 어떤 곤경에 처해 있음을 암시한다.", "implies that the customer is in trouble of some sort", "일치"),
   ("Most people react with horror when they hear the question.", "대부분의 사람은 그 질문을 들으면 질겁한다.", "most of us shudder in horror on hearing these words", "일치"),
   ("Customers believe they can figure out what they want by themselves.", "고객은 원하는 것을 스스로 알아낼 수 있다고 믿는다.", "I'm smart enough to figure out what I want", "일치"),
   ("Customers should feel free to just look around.", "고객은 그냥 둘러봐도 괜찮다고 느껴야 한다.", "they should feel that it is all right to do so", "일치")],
  "이 말을 남용하는 건 훈련받지 않고(untrained) 무관심한(uninterested) 판매원이에요."),
 ("필자의 주장으로 가장 적절한 것은?", [
   ("판매원은 고객이 말하게 이끄는 질문으로 다가가고, 편안한 분위기를 만들어야 한다.", None, "better questions … promote a comfortable environment", "정답"),
   ("판매원은 모든 고객에게 곧바로 도움을 제안해야 한다.", None, "곧바로 '도와드릴까요?'는 최악의 접근", "오답"),
   ("고객은 판매원의 질문에 솔직하게 답해야 한다.", None, "고객에게 하는 주장이 아님", "오답"),
   ("매장은 판매원의 수를 줄여야 한다.", None, "본문에 없음", "오답"),
   ("판매원은 명함 대신 할인 쿠폰을 건네야 한다.", None, "명함을 건네라고 했음, 쿠폰 없음", "오답")],
  "'도와드릴까요?' 대신 더 나은 질문 + 서두르지 않는 편안한 환경 = 필자의 주장"),
 ("고객의 잠재의식 속 생각으로 본문에 나온 것은?", [
   ("\"내가 원하는 건 내가 알아서 찾을 수 있어. 도움은 필요 없어!\"", None, "I'm smart enough to figure out what I want, and I don't need your help!", "정답"),
   ("\"판매원이 나를 꼭 도와줬으면 좋겠어.\"", None, "반대 생각", "오답"),
   ("\"이 가게 물건은 너무 비싸.\"", None, "가격 이야기 없음", "오답"),
   ("\"선물 고르기가 너무 어려워.\"", None, "선물 질문은 더 나은 질문의 예일 뿐", "오답"),
   ("\"판매원이 내 이름을 기억해 주면 좋겠어.\"", None, "본문에 없음", "오답")],
  "The subconscious thought by the customer is often ~"),
 ("5번째 문장의 <span class=\"en\">This line</span>이 가리키는 것은?", [
   ("\"May I help you?\"", "도와드릴까요?", "앞 문장 If a fashion salesperson approached you with \"May I help you?\"", "정답"),
   ("\"Is there anything in particular that you are looking for?\"", "특별히 찾으시는 게 있나요?", "더 나은 질문의 예", "오답"),
   ("\"Are you shopping for a gift?\"", "선물을 사러 오셨나요?", "더 나은 질문의 예", "오답"),
   ("\"No, thank you\"", "아뇨, 괜찮아요", "고객의 대답, 판매원의 말이 아님", "오답"),
   ("\"I don't need your help!\"", "당신 도움은 필요 없어!", "고객의 속마음", "오답")],
  "This line은 미숙한 판매원이 남용하는 '기계적인 접근법' = 바로 앞 문장의 \"May I help you?\""),
 ("혼자 둘러보려는 고객에게 판매원이 할 행동으로 글의 내용에 맞는 것끼리 고른 것은?<br>ㄱ. 명함을 건넨다 · ㄴ. 질문이 생기면 다가갈 수 있게 있는다 · ㄷ. 바로 옆에서 상품을 계속 설명한다 · ㄹ. 빨리 결정하라고 재촉한다", [
   ("ㄱ, ㄴ", None, "give customers their business cards and keep themselves accessible", "정답"),
   ("ㄱ, ㄷ", None, "ㄷ 압박·궁지 → 판매 실패", "오답"),
   ("ㄴ, ㄹ", None, "ㄹ no rush와 반대", "오답"),
   ("ㄷ, ㄹ", None, "둘 다 고객을 압박", "오답"),
   ("ㄱ, ㄴ, ㄷ", None, "ㄷ 때문에 오답", "오답")],
  "명함 + 다가갈 수 있는 상태(accessible) = ㄱ, ㄴ"),
 ("4번째 문장 <span class=\"en\"><u>chances are</u> you would feel the salesperson didn't care</span>의 뜻으로 알맞은 것은?", [
   ("아마 ~일 것이다", None, "chances are (that) ~ = 아마 ~일 것이다", "정답"),
   ("~할 기회가 있다", None, "chance를 '기회'로 읽은 함정", "오답"),
   ("~하는 것은 위험하다", None, "뜻이 다름", "오답"),
   ("운이 좋다면 ~할 것이다", None, "뜻이 다름", "오답"),
   ("절대 ~하지 않을 것이다", None, "반대 뜻", "오답")],
  "chances are = probably"),
]
def mc_item(q, opts, why):
    lab = lambda o: o[0] + (' (%s)' % o[1] if o[1] else '')
    ex = '정답 ▶ %s\n이유: %s\n오답 ▶\n%s' % (lab(opts[0]), why, '\n'.join('✘ %s → %s' % (lab(o), o[2]) for o in opts[1:]))
    it = {'n': 41, 'box': ['41~42번 · 내용 일치·불일치 심화'], 'q': q, 'opts': [o[0] for o in opts], 'ex': ex}
    if opts[0][1] and opts[0][3] in ('일치', '불일치'): it['per'] = [[o[1], o[2], o[3]] for o in opts]
    return it
steps = [
 {'type': 'tf', 'title': 'T/F 심화 · 바꿔 말한 문장', 'guide': '본문 표현을 바꿔 말한(paraphrase) 문장이에요. rarely·never·only after·not smart enough처럼 한 단어로 뜻이 뒤집혀요. 해설의 근거 ▶ 문장과 꼭 대조하세요.',
  'items': [[s, b, '정답 ▶ %s\n이유: %s\n근거 ▶ %s' % ('T' if b else 'F', why, ev), 41, ev] for s, b, why, ev in TF]},
 {'type': 'mc', 'title': '내용 일치·불일치 심화', 'guide': '일치·불일치, 주장, 속마음, 지칭, 어구 뜻까지 내용을 꼼꼼히 물어요. 오답이 왜 틀렸는지 해설로 확인하세요.', 'items': [mc_item(*m) for m in MC]},
]
src = open(path, encoding='utf-8').read()
src = re.sub(r'/\* Q41-PLUS.*?/\* /Q41-PLUS \*/\n?', '', src, flags=re.S)
titles = [s['title'] for s in steps]
src = src.rstrip('\n') + '\n/* Q41-PLUS: 11/27 DAY 15(41·42번) 내용 문제 보강 (gen/js40x/q41plus.py 로 만듦 · 손으로 고치지 말 것) */\n(function(){var d=window.PKG.days.filter(function(x){return x.id==="q41"})[0];if(!d)return;var T=%s,S=%s;d.steps=d.steps.filter(function(s){return T.indexOf(s.title)<0});var k=d.steps.map(function(s){return s.title}).indexOf("일치·불일치");k=k<0?d.steps.length:k+1;Array.prototype.splice.apply(d.steps,[k,0].concat(S));})();\n/* /Q41-PLUS */\n' % (json.dumps(titles, ensure_ascii=False), json.dumps(steps, ensure_ascii=False))
open(path, 'w', encoding='utf-8').write(src)
print('ok', len(TF), len(MC))
