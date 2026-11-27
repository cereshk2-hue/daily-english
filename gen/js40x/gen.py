# 11/27 중산고1 9월 모고 40번·41~42번 '내용 정밀 독해' 학습 강화 (선생님: 40-41 내용 자세히 보라고 하심)
#  DAY x40 · x41 (h1-mock-2509 맨 끝): 문장별 정밀 T/F 16 + 한글 오지선다 세부 내용 6~8
#  11/27 선생님: 40번은 범위 아님(실수) → DAY는 x41만, 시험은 js2509-x4142 '41~42번 내용 심화'로 바꿈 (x40·js2509-x4042 지움)
#  시험 (원래) js2509-x4042 '40·41~42번 내용 심화' 20문항 OMR (/* X4042-TESTS */ 블록) — 해설에 선택지마다 ✔/✘ 이유(영어 선택지는 해석까지)
import sys, json, re, subprocess
sys.path.insert(0, '/home/claude/srcrepo/generators')
from gencommon import write
path = sys.argv[1] if len(sys.argv) > 1 else '/home/claude/proj/data/h1-mock-2509.js'
src = open(path, encoding='utf-8').read()
cut = src.index('/* BIMI-TESTS'); head, tail = src[:src.index('window.PKG')], src[cut:]
PK = json.loads(subprocess.check_output(['node', '-e', "global.window={};eval(require('fs').readFileSync(0,'utf8'));process.stdout.write(JSON.stringify(window.PKG))"], input=src[:cut].encode()))
D = {d['id']: d for d in PK['days']}
# ── T/F: (문장, 참/거짓, 이유, 근거 원문)
TF40 = [
 ("Vision is shaped by our preconceptions about reality.", True, "시각은 현실에 대한 선입견에 영향을 받아요(첫 문장).", "Vision is influenced by our preconceptions about reality."),
 ("We consciously build hierarchies when we view a scene.", False, "consciously(의식적으로) ✘ → unconscious(무의식적인) 위계예요.", "we establish unconscious hierarchies"),
 ("The hierarchies we set up reflect our functional relationship to objects.", True, "위계는 사물과의 기능적 관계를 반영해요.", "hierarchies that reflect our functional relationship to objects"),
 ("The hierarchies reflect our long-term priorities rather than momentary ones.", False, "long-term(장기적) ✘ → momentary priorities(그 순간의 우선순위)예요.", "and our momentary priorities"),
 ("When we picture a hammer in our mind, we usually see it from the top.", False, "위에서 본 모습 ✘ → 옆모습(in profile)이나 '바로 쓸 수 있는' 각도로 떠올려요.", "we tend to \"see\" it in profile or at some other \"ready for use\" angle"),
 ("We tend to imagine a hammer at an angle in which it is ready to be used.", True, "'ready for use' angle = 바로 쓸 수 있는 각도.", "at some other \"ready for use\" angle"),
 ("Seen from the top, a hammer's head is hidden by its handle.", False, "거꾸로예요. 위에서 보면 손잡이(handle)가 머리(head)에 가려져요.", "the handle is hidden by the hammer's head"),
 ("Our visual expectations help us see \"like a camera.\"", False, "help(돕다) ✘ → interfere with(방해하다)예요.", "visual expectations that interfere with our ability to see \"like a camera.\""),
 ("Our visual expectations come from the functional relationship we have with objects.", True, "기능적 관계가 시각적 기대를 만들어 내요(creates).", "The functional relationship we have with objects creates visual expectations"),
 ("Unlike the human eye, the camera sees only shapes and colors.", False, "Unlike(~와 달리) ✘ → like the human eye(인간의 눈처럼)예요.", "The camera, like the human eye, sees only shapes and colors."),
 ("The camera records the world without taking sides.", True, "impartially = 치우침 없이, 공정하게 = without taking sides.", "It documents the world impartially"),
 ("The camera's lens works in a completely different way from the eye.", False, "완전히 다르다 ✘ → 눈과 비슷한(similar to the eye) 렌즈예요.", "through a lens that is similar to the eye"),
 ("Photographs interpret confusing details for us.", False, "해석해 준다 ✘ → 해석하지 않고(don't interpret) 그냥 내놓아요.", "they don't interpret confusing details"),
 ("Photographs show us details with a mechanical indifference.", True, "기계적인 무관심으로(with a mechanical indifference) 그저 내놓아요.", "simply serve them up to us with a mechanical indifference"),
 ("Photographs are often surprising only when we glance at them quickly.", False, "빨리 훑어볼 때 ✘ → 주의 깊게 볼 때(look at them carefully) 놀라워요.", "When we look at them carefully, photographs are often surprising"),
 ("Because photographs are flat, some areas look like unrecognizable colors and shapes.", True, "평면성(flatness) 때문에 알아볼 수 없는 색·형태로 보이는 부분이 있어요.", "because of their flatness, photographs often contain areas that appear as unrecognizable colors and shapes"),
]
TF41 = [
 ("\"May I help you?\" is the best way to begin talking with customers.", False, "best ✘ → the worst four words(최악의 네 단어)예요.", "are the worst four words that a retail salesperson can utter"),
 ("\"May I help you?\" puts customers on the defensive.", True, "고객을 방어적으로 만들어요(put them on the defensive).", "put them on the defensive"),
 ("The four words usually draw out a positive response that helps the sale.", False, "positive ✘ → negative response(부정적 반응), 거래를 멈춰 버려요(stops cold).", "draw out a negative response that stops cold a sales transaction"),
 ("\"Are you shopping for a gift?\" is given as an example of a better question.", True, "더 나은 질문의 예로 나와요.", "Examples of better questions ... \"Are you shopping for a gift?\""),
 ("Hearing \"May I help you?\", customers may feel the salesperson doesn't care.", True, "chances are(아마) 판매원이 관심 없다고 느낄 거예요.", "chances are you would feel the salesperson didn't care"),
 ("The line is used mostly by well-trained salespeople.", False, "well-trained ✘ → untrained and uninterested(훈련받지 않고 무관심한) 판매원이 남용해요.", "so overused by untrained and uninterested salespeople"),
 ("Most people feel pleased when they hear \"May I help you?\"", False, "pleased ✘ → shudder in horror(질겁하며 몸서리친다)예요.", "most of us shudder in horror on hearing these words"),
 ("The question implies that the customer is in some kind of trouble.", True, "곤경에 처해 구조가 필요하다는 것을 암시해요(implies).", "implies that the customer is in trouble of some sort and needs rescuing"),
 ("Customers say \"No, thank you\" only when they need no help at all.", False, "only when ✘ → 실제로 도움이 필요하더라도(even if) 그렇게 답해요.", "even if the customer is actually in need of assistance"),
 ("Deep down, customers think they can figure out what they want by themselves.", True, "잠재의식 속 생각: 내가 원하는 건 내가 알아낼 만큼 똑똑하다.", "I'm smart enough to figure out what I want"),
 ("Salespeople can make more sales by putting pressure on customers.", False, "압박하면 ✘ → 압박·궁지에 몰리면 아무것도 못 팔아요(won't make any sales).", "If customers feel pressured or cornered, then salespeople won't make any sales."),
 ("The approach should create a comfortable environment where customers feel no rush.", True, "서두를 필요 없다고 느끼게 하는 편안한 환경을 조성해야 해요.", "promote a comfortable environment that makes customers feel there is no rush"),
 ("Customers who just want to look around should feel it is all right to do so.", True, "그냥 둘러봐도 괜찮다고 느껴야 해요.", "they should feel that it is all right to do so"),
 ("Salespeople should follow closely behind customers who want to look around alone.", False, "따라다닌다 ✘ → 명함을 건네고 필요할 때 다가갈 수 있게(accessible) 있어야 해요.", "salespeople should give customers their business cards and keep themselves accessible"),
 ("Salespeople should hand their business cards to customers who prefer to look around on their own.", True, "혼자 둘러보려는 고객에게 명함을 건네요.", "salespeople should give customers their business cards"),
 ("Salespeople should stay available in case customers have questions.", True, "in case = ~할 경우에 대비해, accessible = 다가갈 수 있는.", "keep themselves accessible in case customers have questions or concerns"),
]
# ── 한글/영어 오지선다: (문항, 상자 머리, [(선택지, 해석 또는 None, ✔/✘ 이유)] — 첫 번째가 정답)
MC40 = [
 ("글의 내용과 <u>일치하는</u> 것은?", None, [
   ("우리는 장면을 볼 때 무의식적인 위계를 세운다.", None, "2번째 문장 unconscious hierarchies와 일치"),
   ("시각은 현실에 대한 선입견과 관계가 없다.", None, "첫 문장: 선입견에 영향을 받는다(is influenced by)"),
   ("우리는 망치를 주로 위에서 본 모습으로 떠올린다.", None, "옆모습·바로 쓸 수 있는 각도로 떠올린다"),
   ("카메라는 인간의 눈과 달리 형태와 색만 본다.", None, "like the human eye = 인간의 눈'처럼'"),
   ("사진은 혼란스러운 세부 사항을 해석해서 보여 준다.", None, "don't interpret = 해석하지 '않는다'")]),
 ("글의 내용과 <u>일치하지 않는</u> 것은?", None, [
   ("카메라는 사물과의 기능적 관계에 따라 세상을 기록한다.", None, "기능적 관계에 영향을 받는 건 '사람의 시각'. 카메라는 치우침 없이(impartially) 기록"),
   ("사물과의 기능적 관계는 시각적 기대를 만들어 낸다.", None, "5번째 문장 creates visual expectations와 일치"),
   ("시각적 기대는 '카메라처럼' 보는 능력을 방해한다.", None, "interfere with와 일치"),
   ("사진은 평면성 때문에 알아볼 수 없는 부분을 담기도 한다.", None, "마지막 문장과 일치"),
   ("사진을 주의 깊게 보면 놀라운 경우가 많다.", None, "When we look at them carefully, ~ often surprising과 일치")]),
 ("망치(hammer)의 예가 보여 주는 것으로 가장 적절한 것은?", None, [
   ("우리는 사물을 쓰임새에 맞는 모습으로 떠올린다.", None, "'ready for use' angle → 기능적 관계가 보는 방식을 정함"),
   ("도구는 위에서 볼 때 가장 잘 보인다.", None, "위에서 본 모습은 오히려 떠올리지 않는다"),
   ("마음의 눈은 카메라보다 더 정확하다.", None, "오히려 기대 때문에 카메라처럼 보지 못한다"),
   ("망치의 손잡이는 머리보다 덜 중요하다.", None, "부품의 중요도 이야기가 아님"),
   ("사람마다 망치를 떠올리는 방식이 전혀 다르다.", None, "대부분 비슷하게(tend to) 옆모습으로 떠올린다")]),
 ("사진이 종종 놀랍게 느껴지는 이유로 가장 적절한 것은?", None, [
   ("혼란스러운 세부 사항을 해석하지 않고 그대로 내놓기 때문에", None, "don't interpret ~ but simply serve them up과 일치"),
   ("사진이 현실을 더 아름답게 꾸며 주기 때문에", None, "꾸미지 않고 기계적인 무관심으로 보여 줌"),
   ("우리의 우선순위에 맞게 장면을 골라 주기 때문에", None, "우선순위를 반영하는 건 사람의 시각"),
   ("사진이 장면의 입체감을 살려 주기 때문에", None, "오히려 평면성(flatness) 때문에 알아보기 힘든 부분이 생김"),
   ("사진이 우리의 선입견을 그대로 담기 때문에", None, "선입견에 영향받는 건 사람의 시각, 카메라는 impartially")]),
 ("8번째 문장 <span class=\"en\">simply serve <u>them</u> up to us</span>의 them이 가리키는 것은?", None, [
   ("confusing details", "혼란스러운 세부 사항", "don't interpret confusing details but simply serve them up → 해석하지 않고 '그것들(세부 사항)'을 내놓음"),
   ("photographs", "사진", "사진이 주어(they)이고 them은 목적어 → 사진 자신이 아님"),
   ("we", "우리", "us(우리에게)가 따로 있음"),
   ("shapes and colors", "형태와 색", "앞 문장의 말, 이 문장에는 없음"),
   ("objects", "사물", "앞 단락의 말, 이 문장과 무관")]),
 ("글의 내용을 한 문장으로 요약할 때 (A), (B)에 들어갈 말로 가장 적절한 것은?", "Unlike the camera, which records the world (A)________, human vision is influenced by (B)________ formed through our functional relationship with objects.", [
   ("impartially …… expectations", "치우침 없이 …… 기대", "(A) documents the world impartially (B) creates visual expectations"),
   ("selectively …… expectations", "선택적으로 …… 기대", "(A) 카메라는 가리지 않고 기록 → selectively ✘"),
   ("impartially …… instincts", "치우침 없이 …… 본능", "(B) 본능 ✘ → 기능적 관계가 만든 '기대'"),
   ("emotionally …… memories", "감정적으로 …… 기억", "(A)(B) 모두 본문에 없음"),
   ("selectively …… colors", "선택적으로 …… 색", "(A) ✘, (B) 색은 카메라·눈이 보는 것이지 시각에 영향 주는 것이 아님")]),
]
MC41 = [
 ("글의 제목으로 가장 적절한 것은?", None, [
   ("Why \"May I Help You?\" Hurts Sales", "왜 '도와드릴까요?'가 판매를 해치는가", "이 말이 고객을 방어적으로 만들어 판매를 멈춘다는 글 전체 내용"),
   ("How to Train Polite Salespeople", "예의 바른 판매원을 훈련하는 법", "훈련 방법 이야기가 아님"),
   ("The Secret of Giving Business Cards", "명함을 건네는 비결", "명함은 마지막 문장의 일부 내용일 뿐"),
   ("Customers Prefer Fast Service", "고객은 빠른 서비스를 좋아한다", "오히려 서두르지 않는(no rush) 환경이 중요"),
   ("Shopping Alone Is Always Better", "혼자 쇼핑하는 것이 언제나 더 낫다", "always ✘, 혼자 쇼핑이 낫다는 주장 아님")]),
 ("글의 내용과 <u>일치하지 않는</u> 것은?", None, [
   ("고객이 둘러보길 원하면 판매원은 곧바로 다른 상품을 추천해야 한다.", None, "둘러봐도 괜찮다고 느끼게 하고, 명함을 건넨 뒤 필요할 때 다가갈 수 있게 있어야 함"),
   ("'특별히 찾으시는 게 있나요?'는 더 나은 질문의 예이다.", None, "3번째 문장과 일치"),
   ("'May I help you?'는 판매 거래를 멈추게 할 수 있다.", None, "stops cold a sales transaction과 일치"),
   ("훈련받지 않은 판매원들이 이 말을 남용한다.", None, "overused by untrained and uninterested salespeople과 일치"),
   ("고객이 압박을 느끼면 판매가 이루어지지 않는다.", None, "won't make any sales와 일치")]),
 ("'May I help you?'가 고객을 방어적으로 만드는 이유로 가장 적절한 것은?", None, [
   ("고객이 곤경에 처해 도움이 필요하다는 뜻을 담고 있어서", None, "implies that the customer is in trouble ~ and needs rescuing → This almost always puts the customer on the defense"),
   ("질문이 너무 길고 복잡해서", None, "네 단어짜리 짧은 질문"),
   ("판매원이 명함을 주지 않아서", None, "명함은 둘러보는 고객에 대한 조언"),
   ("고객에게 선물을 사라고 강요해서", None, "'선물을 사러 오셨나요?'는 오히려 더 나은 질문의 예"),
   ("고객의 이름을 묻지 않아서", None, "본문에 없는 내용")]),
 ("고객이 혼자 둘러보고 싶어 할 때 판매원이 해야 할 일로 가장 적절한 것은?", None, [
   ("명함을 건네고 필요할 때 다가갈 수 있게 있는다.", None, "give customers their business cards and keep themselves accessible과 일치"),
   ("고객 곁을 따라다니며 상품을 설명한다.", None, "압박·궁지에 몰리게 하면 판매 실패"),
   ("고객이 원할 때까지 매장 밖에서 기다린다.", None, "밖에 나가라는 말은 없음, accessible(다가갈 수 있게)"),
   ("'May I help you?'라고 다시 묻는다.", None, "최악의 네 단어"),
   ("빨리 결정하라고 부드럽게 재촉한다.", None, "no rush(서두를 필요 없는) 환경이어야 함")]),
 ("\"No, thank you\"에 대한 설명으로 가장 적절한 것은?", None, [
   ("고객이 실제로 도움이 필요해도 곧바로 나오는 대답이다.", None, "usually the immediate response, even if ~ in need of assistance"),
   ("고객이 도움이 전혀 필요 없을 때만 하는 대답이다.", None, "even if(~라도) → 필요할 때도 이렇게 답함"),
   ("판매원에게 고마움을 표현하는 대답이다.", None, "방어적인 반응, 잠재의식은 '도움 필요 없어!'"),
   ("고객이 선물을 찾을 때 하는 대답이다.", None, "본문에 없는 연결"),
   ("판매원을 오래 기다린 뒤에 하는 대답이다.", None, "immediate(즉각적인) 대답")]),
 ("<span class=\"en\">most of us <u>shudder in horror</u> on hearing these words</span>의 뜻으로 가장 알맞은 것은?", None, [
   ("질겁하며 몸서리치다", None, "shudder 몸서리치다 + in horror 공포에 질려 → 그만큼 싫다"),
   ("기뻐서 웃음을 터뜨리다", None, "반대 감정"),
   ("놀라서 박수를 치다", None, "shudder ≠ 박수"),
   ("지루해서 하품하다", None, "horror(공포)와 무관"),
   ("감동해서 눈물을 흘리다", None, "반대 감정")]),
 ("<span class=\"en\">a negative response that <u>stops cold</u> a sales transaction</span>의 뜻으로 가장 알맞은 것은?", None, [
   ("거래를 그 자리에서 완전히 멈춰 버리다", None, "stop ~ cold = 갑자기·완전히 멈추게 하다"),
   ("거래를 차갑고 정중하게 마무리하다", None, "cold를 '차가운'으로 읽은 함정"),
   ("거래 속도를 조금 늦추다", None, "조금 ✘, 완전히 멈춤"),
   ("거래를 다음 날로 미루다", None, "미루는 것이 아님"),
   ("거래 가격을 낮추다", None, "가격 이야기 없음")]),
]
def mc_ex(opts):
    ok = opts[0]
    lab = lambda o: o[0] + (' (%s)' % o[1] if o[1] else '')
    return '정답 ▶ %s\n이유 ▶ %s\n오답 ▶\n%s' % (lab(ok), ok[2], '\n'.join('✘ %s → %s' % (lab(o), o[2]) for o in opts[1:]))
def tf_items(T, n):
    return [[s, b, '정답 ▶ %s\n이유: %s\n근거 ▶ %s' % ('T' if b else 'F', why, ev), n, ev] for s, b, why, ev in T]
def mc_items(M, n, tag):
    out = []
    for q, sub, opts in M:
        qq = q + ('<br><span class="en">%s</span>' % sub if sub else '')
        out.append({'n': n, 'box': ['%s · 세부 내용' % tag], 'q': qq, 'opts': [o[0] for o in opts], 'ex': mc_ex(opts)})
    return out
def day(gid, q, tag, n, T, M):
    return {'id': gid, 'name': '', 'range': '내용 정밀 독해 · %s' % tag, 'story': '9월 모고 %s · 내용 정밀 독해 (문장마다 T/F %d → 세부 내용 오지선다 %d)' % (tag, len(T), len(M)),
            'passage': D[q]['passage'],
            'steps': [{'type': 'tf', 'title': '문장마다 정밀 T/F', 'guide': '본문 한 문장 한 문장을 비튼 T/F예요. not·only·always·like/unlike·주어 바꾸기에 속지 말고 근거 문장을 찾아 대조하세요. 해설의 근거 ▶ 문장을 꼭 다시 읽어요.', 'items': tf_items(T, n)},
                      {'type': 'mc', 'title': '세부 내용 오지선다', 'guide': '실제 시험처럼 세부 내용·이유·지칭·제목·요약을 물어요. 해설에서 오답이 왜 틀렸는지까지 읽어요.', 'items': mc_items(M, n, tag)}]}
x40 = day('x40', 'q40', '40번', 40, TF40, MC40); x41 = day('x41', 'q41', '41~42번', 41, TF41, MC41)
# ── OMR 시험 20문항: 오지선다 13 + <보기> 일치 개수 4 + 빈칸 2 + 답할 수 없는 질문 1
C = '①②③④⑤'
def boxcount(T, idx):
    sts = [T[i] for i in idx]; k = sum(1 for s in sts if s[1])
    body = '<div class="wbox"><p>&lt;보기&gt;</p>' + ''.join('<p>(%s) %s</p>' % ('abcdef'[j], s[0]) for j, s in enumerate(sts)) + '</div>'
    ex = '일치하는 것 %d개\n' % k + '\n'.join('(%s) %s %s → %s\n    해석: %s' % ('abcdef'[j], '✔' if s[1] else '✘', s[0], s[2], '') for j, s in enumerate(sts))
    return body, k, ex
KO = {}   # 보기 문장 해석
for s, b, why, ev in TF40 + TF41: KO[s] = ''
import html as _h
PASS = {t: '<div class="wbox"><p>%s</p></div>' % _h.escape(' '.join(l[1] for l in D[q]['passage'] if l[0] != '#'), quote=False) for t, q in (('40번', 'q40'), ('41~42번', 'q41'))}
EXTRA = []
def add_box(T, idx, tag, kos):
    sts = [T[i] for i in idx]; k = sum(1 for s in sts if s[1])
    body = '<div class="wbox"><p>&lt;보기&gt;</p>' + ''.join('<p>(%s) %s</p>' % ('abcdef'[j], s[0]) for j, s in enumerate(sts)) + '</div>'
    ex = '이유 ▶ 일치하는 것은 %s → %d개\n' % (', '.join('(%s)' % 'abcdef'[j] for j, s in enumerate(sts) if s[1]), k) + '\n'.join('(%s) %s %s\n    해석: %s\n    → %s' % ('abcdef'[j], '✔' if s[1] else '✘', s[0], kos[j], s[2]) for j, s in enumerate(sts))
    return ('%s · 내용 일치' % tag, '다음 &lt;보기&gt; 중 글의 내용과 <u>일치하는</u> 것의 개수는?', body, ['1개', '2개', '3개', '4개', '5개'], k - 1, ex)
EXTRA.append(add_box(TF40, [0, 2, 10, 15, 1, 7], '40번', ['시각은 현실에 대한 선입견에 의해 형성된다.', '우리가 세우는 위계는 사물과의 기능적 관계를 반영한다.', '카메라는 한쪽 편을 들지 않고 세상을 기록한다.', '사진은 평면이라 일부가 알아볼 수 없는 색과 형태로 보인다.', '우리는 장면을 볼 때 의식적으로 위계를 세운다.', '시각적 기대는 우리가 카메라처럼 보도록 돕는다.']))
EXTRA.append(add_box(TF40, [4, 5, 6, 9, 11, 13], '40번', ['마음속으로 망치를 떠올릴 때 보통 위에서 본 모습을 본다.', '우리는 망치를 바로 쓸 수 있는 각도로 떠올리는 경향이 있다.', '위에서 보면 망치 머리가 손잡이에 가려진다.', '인간의 눈과 달리 카메라는 형태와 색만 본다.', '카메라 렌즈는 눈과 완전히 다른 방식으로 작동한다.', '사진은 기계적인 무관심으로 세부를 보여 준다.']))
EXTRA.append(add_box(TF41, [1, 2, 5, 7, 9, 13], '41~42번', ["'May I help you?'는 고객을 방어적으로 만든다.", '이 네 단어는 보통 판매에 도움이 되는 긍정적 반응을 끌어낸다.', '이 말은 주로 잘 훈련된 판매원이 쓴다.', '이 질문은 고객이 어떤 곤경에 처해 있음을 암시한다.', '고객은 속으로 자기가 원하는 것을 스스로 알아낼 수 있다고 생각한다.', '판매원은 혼자 둘러보려는 고객을 바짝 따라다녀야 한다.']))
EXTRA.append(add_box(TF41, [3, 11, 12, 14, 15, 6], '41~42번', ["'선물을 사러 오셨나요?'는 더 나은 질문의 예로 나온다.", '접근 방식은 고객이 서두를 필요가 없다고 느끼는 편안한 환경을 만들어야 한다.', '그냥 둘러보고 싶은 고객은 그래도 괜찮다고 느껴야 한다.', '판매원은 혼자 둘러보길 원하는 고객에게 명함을 건네야 한다.', '판매원은 고객에게 질문이 생길 경우에 대비해 다가갈 수 있게 있어야 한다.', "대부분의 사람은 'May I help you?'를 들으면 기뻐한다."]))
def blank(tag, sent, opts, why):
    ex = '이유 ▶ %s\n' % why + '\n'.join('%s %s (%s)' % ('✔' if j == 0 else '✘', o, k) for j, (o, k) in enumerate(opts))
    return ('%s · 세부 어휘' % tag, '글의 내용으로 보아 빈칸에 들어갈 말로 가장 적절한 것은?', '<div class="wbox"><p>%s</p></div>' % sent, [o for o, _ in opts], 0, ex)
EXTRA.append(blank('40번', 'The camera documents the world ________ through a lens that is similar to the eye.',
  [('impartially', '치우침 없이'), ('selectively', '선택적으로'), ('emotionally', '감정적으로'), ('creatively', '창의적으로'), ('partially', '부분적으로·편파적으로')],
  '카메라는 형태와 색만 보고, 사진은 세부를 해석 없이 기계적인 무관심으로 내놓음 → 치우침 없이 기록 = impartially'))
EXTRA.append(blank('41~42번', 'The approach has to promote a ________ environment that makes customers feel there is no rush.',
  [('comfortable', '편안한'), ('competitive', '경쟁적인'), ('crowded', '붐비는'), ('formal', '격식을 차린'), ('tense', '긴장된')],
  '고객이 압박받으면 판매 실패 → 서두를 필요 없다고 느끼는 편안한(comfortable) 환경'))
EXTRA.append(('41~42번 · 세부 내용', '글을 읽고 답할 수 <u>없는</u> 질문은?', PASS['41~42번'], [
  '판매원 교육에 드는 비용은 얼마인가?', '고객에게 다가갈 때 쓸 수 있는 더 나은 질문은 무엇인가?', "'May I help you?'에 대한 고객의 흔한 즉각적 반응은 무엇인가?", '혼자 둘러보려는 고객에게 판매원이 건네야 할 것은 무엇인가?', '고객이 압박을 느끼면 어떤 결과가 생기는가?'], 0,
  "이유 ▶ 교육 비용은 본문에 전혀 없음\n✘ 더 나은 질문 → 'Is there anything in particular ~?' / 'Are you shopping for a gift?'\n✘ 즉각적 반응 → \"No, thank you\"\n✘ 건넬 것 → 명함(business cards)\n✘ 압박 결과 → 아무것도 팔지 못함(won't make any sales)"))
def mc_test(M, tag):
    out = []
    for q, sub, opts in M:
        body = PASS[tag] + ('<div class="wbox"><p class="en">%s</p></div>' % sub if sub else '')
        out.append(('%s · 세부 내용' % tag, q, body, [o[0] for o in opts], 0, mc_ex(opts).split('\n', 1)[1]))
    return out
_q = open('/home/claude/srcrepo/gen/js40x/q41plus.py', encoding='utf-8').read(); _ns = {}
exec(_q[_q.index('TF = ['):_q.index('def mc_item')], _ns)   # DAY 15 보강(q41plus.py)의 T/F·오지선다를 같이 씀
TFQ = _ns['TF']; MCQ = _ns['MC']
X2 = [add_box(TFQ, [0, 1, 2, 3, 4, 5], '41~42번', ["필자는 '도와드릴까요?'가 고객이 더 말하고 싶게 만든다고 생각한다.", "'도와드릴까요?'는 판매가 제대로 시작되기도 전에 끝내 버리곤 한다.", "'특별히 찾으시는 게 있나요?'는 더 나은 첫 질문으로 제시된다.", "고객은 보통 '도와드릴까요?'라고 말하는 판매원이 자기에게 진심으로 관심이 있다고 믿는다.", "훈련받지 않은 판매원은 '도와드릴까요?'를 거의 쓰지 않는다.", "'도와드릴까요?'는 고객이 마치 구조가 필요한 사람처럼 느끼게 한다."]),
      add_box(TFQ, [7, 10, 12, 1, 2, 11], '41~42번', ["고객은 실제로 도움이 필요할 때도 도움을 거절하곤 한다.", "좋은 접근은 고객이 서두를 필요가 없다고 느끼게 한다.", "글은 판매원이 혼자 둘러보려는 고객의 바람을 존중해야 한다고 말한다.", "'도와드릴까요?'는 판매가 제대로 시작되기도 전에 끝내 버리곤 한다.", "'특별히 찾으시는 게 있나요?'는 더 나은 첫 질문으로 제시된다.", "판매원은 혼자 둘러보려는 고객의 질문에 절대 답하지 말아야 한다."])]
def mcq_test(m):
    q, opts, why = m
    lab = lambda o: o[0] + (' (%s)' % o[1] if o[1] else '')
    ex = '이유 ▶ %s\n오답 ▶\n%s' % (why, '\n'.join('✘ %s → %s' % (lab(o), o[2]) for o in opts[1:]))
    if opts[0][1]: ex = '정답 해석 ▶ %s\n' % opts[0][1] + ex
    return ('41~42번 · 내용 일치·불일치', q, PASS['41~42번'], [o[0] for o in opts], 0, ex)
GIST = ('41~42번 · 요지', '글의 요지로 가장 적절한 것은?', PASS['41~42번'], [
  "'May I help you?' 같은 판에 박힌 질문 대신, 고객이 편하게 둘러볼 수 있게 다가가야 판매에 성공한다.", '판매원은 고객이 도움을 요청할 때까지 기다리기만 하면 된다.', '친절한 인사 한마디가 판매의 전부이다.', '고객은 판매원에게 먼저 도움을 청하는 것이 예의이다.', '명함은 판매원의 신뢰를 높이는 가장 좋은 도구이다.'], 0,
  "이유 ▶ 최악의 질문(May I help you?) → 더 나은 질문 → 압박하지 말고 편안한 환경·혼자 둘러볼 자유 → 판매 성공\n오답 ▶\n✘ 기다리기만 → 더 나은 질문으로 다가가라고 함\n✘ 친절한 인사가 전부 → '도와드릴까요?'도 인사지만 최악\n✘ 고객의 예의 → 고객에게 하는 말이 아님\n✘ 명함이 최고의 도구 → 명함은 마지막 조언의 일부")
RAW = mc_test(MC41, '41~42번') + EXTRA[2:4] + X2 + [EXTRA[5], EXTRA[6], GIST] + [mcq_test(MCQ[i]) for i in (0, 1, 2, 3, 4, 5)]
RAW = RAW[:20]
assert len(RAW) == 20, len(RAW)
# 정답 자리를 ①~⑤ 4개씩: 선택지를 돌려 정답을 원하는 자리로 (개수형은 순서 고정이라 그대로 두고 나머지로 맞춤)
fixed = [i for i, r in enumerate(RAW) if r[3][0] == '1개']
need = {k: 4 for k in range(5)}
for i in fixed: need[RAW[i][4]] -= 1
want = []
for k in range(5): want += [k] * need[k]
order = [2, 0, 4, 1, 3, 3, 1, 0, 4, 2, 1, 4, 0, 3, 2, 2, 0, 3, 1, 4]
pool = list(want); items = []
for i, (src_, stem, body, opts, ans, ex) in enumerate(RAW):
    if i in fixed: tgt = ans; o = opts
    else:
        tgt = next(k for k in order[i:] + order + list(range(5)) if k in pool); pool.remove(tgt)
        o = list(opts); right = o.pop(ans); o.insert(tgt, right)
    items.append({'n': i + 1, 'src': src_, 'stem': stem, 'body': body, 'opts': o, 'en': any(re.search(r'[A-Za-z]{4}', x) for x in o), 'ans': tgt,
                  'ex': '정답 ▶ %s %s\n' % (C[tgt], o[tgt]) + ex, 'ctx': '', 'pts': 5, 'words': [], 'kos': []})
from collections import Counter
cnt = Counter(it['ans'] for it in items); assert all(cnt[k] == 4 for k in range(5)), cnt
TEST = {'id': 'js2509-x4142', 'title': '9월 학평 41~42번 내용 심화', 'short': '41~42 내용 심화', 'school': '중산고 1학년', 'minutes': 30, 'items': items}
# DAY는 HV-DAYS 블록(끝에서 다시 번호 매김) 뒤에 붙여야 기존 DAY 번호가 안 바뀜 → 데이터 파일은 그대로, 꼬리 블록으로만 추가
tail = re.sub(r'/\* X4042-TESTS.*?/\* /X4042-TESTS \*/\n?', '', tail, flags=re.S)
tail = re.sub(r'/\* X40-DAYS.*?/\* /X40-DAYS \*/\n?', '', tail, flags=re.S)
tail = tail.rstrip('\n') + '\n/* X40-DAYS: 11/27 41~42번 내용 정밀 독해 DAY x41 맨 끝 (40번 x40은 범위 아니라 뺌) (gen/js40x/gen.py 로 만듦 · 손으로 고치지 말 것) */\n(function(){var P=window.PKG,N=%s;P.days=P.days.filter(function(d){return d.id!=="x40"&&d.id!=="x41"}).concat(N);P.days.forEach(function(d,i){d.name="DAY "+(i+1)});})();\n/* /X40-DAYS */\n' % json.dumps([x41], ensure_ascii=False)
tail = tail.rstrip('\n') + '\n/* X4042-TESTS: gen/js40x/gen.py 로 만듦 (손으로 고치지 말 것) */\nwindow.PKG.tests = (window.PKG.tests || []).filter(function (t) { return t.id !== "js2509-x4042" && t.id !== "js2509-x4142"; }).concat([%s]);\n/* /X4042-TESTS */\n' % json.dumps(TEST, ensure_ascii=False)
open(path, 'w', encoding='utf-8').write(src[:cut] + tail)
print(dict(cnt), ''.join(C[it['ans']] for it in items))
