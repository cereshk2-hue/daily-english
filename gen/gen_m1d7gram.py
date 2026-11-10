import sys, re, json, subprocess
sys.path.insert(0, '/home/claude/work/gen')
from gencommon import write
from dlgcommon import ansfirst
# 11/10 중1 동아(윤정미) 7과 문법 2가지 → 공통 문법(m1-grammar-to1) DAY 21~40
#   a1~a12 to부정사 ② 부사적 용법 · w1~w8 시간 접속사 when · before · after
# 근거: Grammar Build Up 워크북·객관식 7과 Pattern 1 / Pattern 2·3, 교과서 7과 본문 문장

class Day:
    def __init__(s, did, rng, story):
        s.d = {'id': did, 'name': 'DAY', 'range': rng, 'story': story, 'passage': [], 'steps': []}
        s.notes, s.ex, s.seen = [], [], set()
    def note(s, title, rows):
        s.notes.append(['#', title, '']); s.notes += [['', a, b] for a, b in rows]
    def sent(s, en, ko):
        en = re.sub(r'<[^>]+>', '', en)
        if en not in s.seen: s.seen.add(en); s.ex.append(['', en, ko])
    def step(s, st): s.d['steps'].append(st); return st
    def done(s):
        s.d['passage'] = s.notes + ([['#', '예문', '']] + s.ex if s.ex else [])
        return s.d

def CARDS(D, title, items, guide='문장을 읽고 알맞은 해석을 골라요.'):
    for en, ko in items: D.sent(en, ko)
    return {'type': 'vocab', 'title': title, 'guide': guide, 'quizN': len(items), 'items': [list(x) for x in items]}
def TF(title, items, guide='맞으면 T, 틀리면 F를 고르세요.'): return {'type': 'tf', 'title': title, 'guide': guide, 'items': [[a, b, c, None, None] for a, b, c in items]}
def MC(title, items, guide='알맞은 답을 고르세요.'):
    return {'type': 'mc', 'title': title, 'guide': guide, 'items': [dict({'q': it[0], 'opts': it[1], 'ex': it[2]}, **({'sort': True} if len(it) > 3 and it[3] else {})) for it in items]}
def PICK(D, title, items, guide='어법상 알맞은 것을 고르세요.'):
    for s, ko, x in items: D.sent(re.sub(r'\{([^|}]*)\|[^}]*\}', r'\1', s), ko)
    return {'type': 'pick', 'title': title, 'guide': guide, 'items': [{'s': s, 'ex': x} for s, ko, x in items]}
def VERB(D, title, items, guide, ph='알맞은 말 쓰기'):
    for s, v, a, ko, x in items: D.sent(s.replace('___', a[0]), ko)
    return {'type': 'verb', 'title': title, 'guide': guide, 'free': True, 'ph': ph, 'items': [{'s': s, 'v': v, 'a': a, 'ex': x} for s, v, a, ko, x in items]}
def SCR(D, title, items, guide='우리말에 맞게 단어를 눌러 문장을 완성하세요.'):
    for en, ko in items: D.sent(en, ko)
    return {'type': 'scramble', 'title': title, 'guide': guide, 'items': [{'ko': ko, 'en': en} for en, ko in items]}
def ERR(D, title, items):
    for s, w, f, ko, x in items:
        k = [0]
        def rep(m):
            r = ('' if f == '(삭제)' else f) if k[0] == w else m.group(1); k[0] += 1; return r
        D.sent(re.sub(r'\s+', ' ', re.sub(r'\[\[(.+?)\]\]', rep, s)).strip(), ko)
    return {'type': 'error', 'title': title, 'guide': '어법상 틀린 곳을 고르세요.', 'items': [{'s': s, 'w': w, 'fix': f, 'ex': x} for s, w, f, ko, x in items]}
U = lambda s, u: s.replace(u, '<u>' + u + '</u>', 1)
def Q(en, u=None): return '<br><b>' + (U(en, u) if u else en) + '</b>'

USE = ['목적 (~하기 위해)', '감정의 원인 (~해서)', '결과 ((…해서) ~하다)', '형용사 수식 (~하기에)']
def use(D, en, ko, ans, why, u):
    D.sent(en, ko)
    return ('밑줄 친 부분의 쓰임은?' + Q(en, u), [USE[ans]] + [x for i, x in enumerate(USE) if i != ans], '정답 ▶ %s\n이유: %s\n해석 ▶ %s' % (USE[ans], why, ko))
AN = ['부사적 용법 (~하기 위해 등)', '명사적 용법 (~하는 것)']
def an(D, en, ko, ans, why, u):
    D.sent(en, ko)
    return ('밑줄 친 to부정사의 용법은?' + Q(en, u), [AN[ans], AN[1 - ans]], '정답 ▶ %s\n이유: %s\n해석 ▶ %s' % (AN[ans], why, ko))

DAYS = []
# ═════════════════ to부정사 ② 부사적 용법 ═════════════════
D = Day('a1', 'to부정사 ② 부사적 용법이 뭐예요?', '"~하기 위해" · 왜 했는지 이유(목적)를 붙이는 to부정사')
D.note('개념 ① 부사적 용법 = 문장에 "왜?"를 붙여요', [
    ('I went to the library.', '나는 도서관에 갔다. → 왜 갔어?'),
    ('I went to the library to read books.', '나는 책을 읽기 위해 도서관에 갔다. (to read books = 왜 갔는지)'),
    ('to + 동사원형', '문장 뒤(또는 앞)에 붙어 "~하기 위해(서)"라는 목적을 나타내요.'),
])
D.note('개념 ② 명사적 용법과 비교', [
    ('I want to read books.', '명사적: 나는 책 읽는 것을 원한다. (want의 목적어 = ~하는 것)'),
    ('I went there to read books.', '부사적: 나는 책을 읽기 위해 그곳에 갔다. (없어도 문장이 완성됨 + "왜?")'),
    ('구별 요령', 'to부정사를 빼도 문장이 말이 되면 → 부사적 용법일 가능성이 커요.'),
])
D.step(CARDS(D, '해석 카드', [
    ('I went to the library to read books.', '나는 책을 읽기 위해 도서관에 갔다.'), ('She saved money to go to Portugal.', '그녀는 포르투갈에 가기 위해 돈을 모았다.'),
    ('He sat on a chair to get some rest.', '그는 휴식을 취하기 위해 의자에 앉았다.'), ('I came home early to do my homework.', '나는 숙제를 하기 위해 집에 일찍 왔다.'),
    ('Olivia came to Seoul to study Korean.', 'Olivia는 한국어를 공부하기 위해 서울에 왔다.'), ('Tom exercises every day to be healthy.', 'Tom은 건강해지기 위해 매일 운동한다.'),
    ('I got up early to prepare breakfast.', '나는 아침을 준비하기 위해 일찍 일어났다.'), ('We use a camera to take photographs.', '우리는 사진을 찍기 위해 카메라를 사용한다.')],
    guide='to + 동사원형을 "~하기 위해"로 해석해요.'))
D.step(TF('개념 확인 T/F', [
    ('부사적 용법의 to부정사는 "~하기 위해"라는 목적을 나타낼 수 있다.', True, '정답 ▶ T\n이유: I went to the library to read books. → 책을 읽기 위해(목적)'),
    ('to 다음에는 동사원형이 온다.', True, '정답 ▶ T\n이유: to read(○), to reads(×), to reading(×)'),
    ('She saved money to go to Portugal.에서 to go는 "가는 것"으로 해석한다.', False, '정답 ▶ F\n이유: 돈을 모은 이유(목적) → "가기 위해"로 해석해요.'),
    ('I want to read books.의 to read는 부사적 용법이다.', False, '정답 ▶ F\n이유: want의 목적어(읽는 것) → 명사적 용법이에요.'),
    ('He went to the park to play soccer.에서 to play soccer를 빼도 문장이 된다.', True, '정답 ▶ T\n이유: He went to the park. 만으로도 완전한 문장 → to play soccer는 "왜?"를 더해 주는 부사적 용법'),
    ('Tom exercises every day to be healthy.는 "Tom은 건강해지기 위해 매일 운동한다."이다.', True, '정답 ▶ T\n이유: to be healthy = 건강해지기 위해(목적)'),
]))
D.step(MC('"왜?"에 해당하는 부분 찾기', [
    ('밑줄 친 부분 중 "왜 했는지"를 나타내는 것은?<br><b>I ①went ②to the store ③to buy some milk ④yesterday ⑤with my mom.</b>', ['③ to buy some milk', '① went', '② to the store', '④ yesterday', '⑤ with my mom'],
     '정답 ▶ ③ to buy some milk\n이유: 가게에 간 이유 = 우유를 사기 위해\n포인트 ▶ to the store의 to는 전치사(~로), to buy의 to는 to부정사'),
    ('to부정사(to + 동사원형)가 <b>아닌</b> 것은?', ['I went <u>to the bakery</u>.', 'I went out <u>to buy</u> bread.', 'He studies <u>to pass</u> the test.', 'We met <u>to talk</u>.', 'She called me <u>to say</u> sorry.'],
     '정답 ▶ I went <u>to the bakery</u>.\n이유: to + 명사(the bakery) → 전치사 to(~로)\n포인트 ▶ to 뒤가 동사원형이면 to부정사, 명사면 전치사'),
    ('빈칸에 알맞은 것은?<br><b>Jane went to the library ______ books.</b>', ['to read', 'read', 'reads', 'reading', 'to reads'],
     '정답 ▶ to read\n이유: "책을 읽기 위해" → to + 동사원형\n해석 ▶ Jane은 책을 읽기 위해 도서관에 갔다.'),
    ('우리말과 같은 뜻이 되도록 할 때 빈칸에 알맞은 것은?<br>나는 너를 만나기 위해 여기에 왔다.<br><b>I came here ______ you.</b>', ['to meet', 'meet', 'met', 'meeting', 'to meeting'],
     '정답 ▶ to meet\n이유: ~하기 위해 = to + 동사원형'),
    ('해석이 바른 것은?<br><b>He sat on a chair to get some rest.</b>', ['그는 휴식을 취하기 위해 의자에 앉았다.', '그는 의자에 앉는 것을 좋아했다.', '그는 휴식을 취한 후에 의자에 앉았다.', '그는 의자에 앉아서 휴식을 취하고 싶었다.', '그는 휴식을 취하는 것이 의자라고 말했다.'],
     '정답 ▶ 그는 휴식을 취하기 위해 의자에 앉았다.\n이유: to get some rest = 휴식을 취하기 위해(목적)'),
]))
D.step(PICK(D, '어법 · to 다음은 동사원형', [
    ('She saved money to {go|goes} to Portugal.', '그녀는 포르투갈에 가기 위해 돈을 모았다.', '정답 ▶ go\n이유: to 다음에는 동사원형'),
    ('I came home early to {do|did} my homework.', '나는 숙제를 하기 위해 집에 일찍 왔다.', '정답 ▶ do\n이유: 과거 문장이어도 to 다음은 동사원형(did ×)'),
    ('He went to the shop to {buy|buying} some bread.', '그는 빵을 좀 사기 위해 가게에 갔다.', '정답 ▶ buy\n이유: to + 동사원형 (to buying ×)'),
    ('Tom exercises every day to {be|is} healthy.', 'Tom은 건강해지기 위해 매일 운동한다.', '정답 ▶ be\n이유: is의 원형은 be → to be'),
    ('We use a camera {to take|take} photographs.', '우리는 사진을 찍기 위해 카메라를 사용한다.', '정답 ▶ to take\n이유: 동사 use가 이미 있으므로 "찍기 위해"는 to take'),
    ('Olivia came to Seoul {to study|studies} Korean.', 'Olivia는 한국어를 공부하기 위해 서울에 왔다.', '정답 ▶ to study\n이유: 목적(공부하기 위해) → to + 동사원형'),
]))
D.step(VERB(D, 'to부정사로 쓰기', [
    ('I went to the bakery ___ some bread.', 'buy', ['to buy'], '나는 빵을 좀 사기 위해 빵집에 갔다.', '정답 ▶ to buy\n이유: 빵을 사기 위해 → to + 동사원형'),
    ('I went to the park ___ my dog.', 'walk', ['to walk'], '나는 개를 산책시키기 위해 공원에 갔다.', '정답 ▶ to walk'),
    ('I went to the gym ___ out.', 'work', ['to work'], '나는 운동하기 위해 체육관에 갔다.', '정답 ▶ to work (work out = 운동하다)'),
    ('I went to the store ___ a T-shirt.', 'buy', ['to buy'], '나는 티셔츠를 사기 위해 가게에 갔다.', '정답 ▶ to buy'),
], '괄호 속 동사를 "~하기 위해"가 되도록 to부정사로 써요.', 'to + 동사원형'))
DAYS.append(D.done())

D = Day('a2', '목적 ① "~하기 위해" 해석 · 배열', '문장 뒤에 붙은 to부정사를 "왜?"로 읽고 우리말 순서 바꿔 보기')
D.note('해석 순서', [
    ('I went to the market / to buy some fish.', '① 나는 시장에 갔다 / ② 생선을 사기 위해 → 나는 생선을 사기 위해 시장에 갔다.'),
    ('요령', 'to부정사(목적)를 먼저 해석하고 앞 문장을 붙이면 자연스러워요.'),
])
D.step(CARDS(D, '해석 카드', [
    ('I went to the market to buy some fish.', '나는 생선을 사기 위해 시장에 갔다.'), ('I bought some fruit to make juice.', '나는 주스를 만들기 위해 과일을 좀 샀다.'),
    ('I jumped rope every day to lose some weight.', '나는 살을 좀 빼기 위해 매일 줄넘기를 했다.'), ('I went to the library to find a book about iguanas.', '나는 이구아나에 관한 책을 찾기 위해 도서관에 갔다.'),
    ('You use a watch to tell the time.', '너는 시간을 알기 위해 손목시계를 사용한다.'), ('You use a knife to cut things.', '너는 물건을 자르기 위해 칼을 사용한다.'),
    ('I turned on the radio to listen to some music.', '나는 음악을 좀 듣기 위해 라디오를 켰다.'), ('They put on sun cream to protect their skin.', '그들은 피부를 보호하기 위해 선크림을 발랐다.')]))
D.step(MC('짝 맞추기 (워크북 Warm-up)', [
    ('빈칸에 가장 알맞은 것은?<br><b>I went to the market ______.</b>', ['to buy some fish', 'to lose some weight', 'to make juice from the fish', 'to find a book about iguanas', 'to tell the time'],
     '정답 ▶ to buy some fish\n이유: 시장에 간 목적 = 생선을 사기 위해'),
    ('빈칸에 가장 알맞은 것은?<br><b>I jumped rope every day ______.</b>', ['to lose some weight', 'to buy some fish', 'to find a book', 'to make juice', 'to cut things'],
     '정답 ▶ to lose some weight\n이유: 매일 줄넘기를 한 목적 = 살을 빼기 위해'),
    ('빈칸에 가장 알맞은 것은?<br><b>You use a microwave ______.</b>', ['to heat up food', 'to tell the time', 'to take photographs', 'to write things', 'to wake up in the morning'],
     '정답 ▶ to heat up food\n이유: 전자레인지 = 음식을 데우기 위해'),
    ('빈칸에 가장 알맞은 것은?<br><b>You use an alarm clock ______.</b>', ['to wake up in the morning', 'to heat up food', 'to cut things', 'to write things', 'to take photographs'],
     '정답 ▶ to wake up in the morning\n이유: 알람시계 = 아침에 일어나기 위해'),
    ('빈칸에 가장 알맞은 것은?<br><b>They went to the airport ______ Ben\'s sister.</b>', ['to meet', 'to send', 'to learn', 'to listen', 'to watch'],
     '정답 ▶ to meet\n이유: 공항에 간 목적 = Ben의 여동생을 만나기 위해'),
]))
D.step(MC('해석 고르기', [
    ('해석이 바른 것은?<br><b>I bought some fruit to make juice.</b>', ['나는 주스를 만들기 위해 과일을 좀 샀다.', '나는 과일을 사서 주스를 마셨다.', '나는 주스를 만드는 것을 좋아한다.', '나는 주스를 만든 후에 과일을 샀다.', '나는 과일로 주스를 만들고 싶다.'], '정답 ▶ 나는 주스를 만들기 위해 과일을 좀 샀다.'),
    ('해석이 바른 것은?<br><b>They put on sun cream to protect their skin.</b>', ['그들은 피부를 보호하기 위해 선크림을 발랐다.', '그들은 피부를 보호하는 것을 잊었다.', '그들은 선크림을 바른 후 피부가 좋아졌다.', '그들은 피부를 보호하는 선크림을 샀다.', '그들은 선크림을 바르는 것을 싫어했다.'], '정답 ▶ 그들은 피부를 보호하기 위해 선크림을 발랐다.'),
    ('해석이 바른 것은?<br><b>He went to England to learn English.</b>', ['그는 영어를 배우기 위해 영국에 갔다.', '그는 영국에서 영어를 배우는 것을 원했다.', '그는 영어를 배운 후 영국에 갔다.', '그는 영국에 가는 것을 배웠다.', '그는 영어를 배우러 갈 계획이다.'], '정답 ▶ 그는 영어를 배우기 위해 영국에 갔다.'),
    ('우리말을 영어로 바르게 옮긴 것은?<br>나는 뉴스를 보기 위해 TV를 켰다.', ['I turned on the TV to watch the news.', 'I turned on the TV watch the news.', 'I turned on the TV to watched the news.', 'I watched the news to turn on the TV.', 'I turned on the TV for watch the news.'],
     '정답 ▶ I turned on the TV to watch the news.\n오답 ▶ to 빠짐 / to watched(과거형 ×) / 순서가 바뀜 / for watch(×)'),
]))
D.step(SCR(D, '우리말 → 영어 배열', [
    ('He went to Paris to visit his mother.', '그는 엄마를 찾아뵙기 위해 파리로 갔다.'), ('Jane went to the library to read books.', 'Jane은 책을 읽기 위해 도서관에 갔다.'),
    ('I study very hard to pass the exam.', '나는 시험에 합격하기 위해 매우 열심히 공부한다.'), ('She went to the park to take a walk.', '그녀는 산책하기 위해 공원에 갔다.'),
    ('He called his friend to ask for help.', '그는 도움을 청하기 위해 친구에게 전화했다.')]))
DAYS.append(D.done())

D = Day('a3', '목적 ② 문장 맨 앞 To ~, · 두 문장 잇기', 'To부정사가 맨 앞에 오면 콤마(,) · 워크북 Part 2 두 문장 합치기')
D.note('개념 ① 목적의 to부정사는 문장 앞에도 와요', [
    ('To stay healthy, eat fruits.', '건강을 유지하기 위해, 과일을 먹어라.'),
    ('To capture their happy moments, I\'m going to use drones.', '그들의 행복한 순간을 포착하기 위해, 나는 드론을 사용할 거예요. (교과서)'),
    ('규칙', '맨 앞에 오면 to부정사구 끝에 콤마(,)를 찍어요. 뜻은 똑같이 "~하기 위해".'),
])
D.note('개념 ② 두 문장 잇기', [
    ('Judy went by bus. + She wanted to save money.', '→ Judy went by bus to save money. (버스를 탄 목적 = 돈을 아끼기 위해)'),
    ('요령', '두 번째 문장의 wanted to / had to / needed to를 빼고 to + 동사원형만 붙여요.'),
])
D.step(CARDS(D, '해석 카드', [
    ('To stay healthy, eat fruits.', '건강을 유지하기 위해, 과일을 먹어라.'), ('To capture their happy moments, I\'m going to use drones.', '그들의 행복한 순간을 포착하기 위해, 나는 드론을 사용할 거예요.'),
    ('To create a better story, I can change the order of scenes.', '더 좋은 이야기를 만들기 위해, 나는 장면의 순서를 바꿀 수 있어요.'), ('To catch the first train, she got up early.', '첫 기차를 타기 위해, 그녀는 일찍 일어났다.'),
    ('Judy went by bus to save money.', 'Judy는 돈을 아끼기 위해 버스를 탔다.'), ('Mary stayed late to finish her homework.', 'Mary는 숙제를 끝내기 위해 늦게까지 남아 있었다.')]))
D.step(TF('콤마 · 위치 T/F', [
    ('To stay healthy, eat fruits.는 바른 문장이다.', True, '정답 ▶ T\n이유: 목적의 to부정사가 맨 앞 + 콤마'),
    ('To capture their happy moments에서 To capture는 "포착하는 것"으로 해석한다.', False, '정답 ▶ F\n이유: 뒤에 주절(I\'m going to use drones)이 있으므로 "포착하기 위해"(목적)'),
    ('Judy went by bus to save money.는 Judy went by bus. + She wanted to save money.를 합친 것이다.', True, '정답 ▶ T'),
    ('To catch the first train, she got up early.와 She got up early to catch the first train.은 뜻이 같다.', True, '정답 ▶ T\n이유: to부정사구의 위치만 다르고 뜻은 같아요.'),
]))
D.step(MC('두 문장 잇기 (워크북 Part 2)', [
    ('두 문장을 한 문장으로 바르게 바꾼 것은?<br>My mother went to the post office. + She had to post some letters.', ['My mother went to the post office to post some letters.', 'My mother went to the post office to posted some letters.', 'My mother went to the post office post some letters.', 'My mother had to post the post office.', 'My mother went to post the post office some letters.'],
     '정답 ▶ My mother went to the post office to post some letters.\n이유: had to를 빼고 to post만 붙여요.'),
    ('두 문장을 한 문장으로 바르게 바꾼 것은?<br>Paul did some exercises. + He wanted to lose weight.', ['Paul did some exercises to lose weight.', 'Paul did some exercises to losing weight.', 'Paul wanted some exercises to lose weight.', 'Paul did some exercises lose weight.', 'Paul did to lose some exercises.'],
     '정답 ▶ Paul did some exercises to lose weight.'),
    ('두 문장을 한 문장으로 바르게 바꾼 것은?<br>Daisy is studying hard. + She wants to be a doctor.', ['Daisy is studying hard to be a doctor.', 'Daisy is studying hard to is a doctor.', 'Daisy is studying hard be a doctor.', 'Daisy wants studying hard a doctor.', 'Daisy is a doctor to study hard.'],
     '정답 ▶ Daisy is studying hard to be a doctor.\n이유: wants to를 빼고 to be를 붙여요.'),
    ('같은 뜻이 되도록 할 때 빈칸에 알맞은 것은?<br>She got up early to catch the first train.<br>= ______ the first train, she got up early.', ['To catch', 'Catch', 'Caught', 'To catching', 'For catch'],
     '정답 ▶ To catch\n이유: 목적의 to부정사를 맨 앞으로 → To catch ~, (콤마)'),
]))
D.step(SCR(D, '우리말 → 영어 배열', [
    ('To stay healthy, eat fruits.', '건강을 유지하기 위해, 과일을 먹어라.'), ('Sam went to the supermarket to buy some sugar.', 'Sam은 설탕을 좀 사기 위해 슈퍼마켓에 갔다.'),
    ('We are on a diet to get thinner.', '우리는 더 날씬해지기 위해 다이어트 중이다.'), ('To catch the train, he left early.', '기차를 타기 위해, 그는 일찍 떠났다.')]))
DAYS.append(D.done())

D = Day('a4', 'in order to · so as to · not to', '"~하기 위해" 다른 표현 2개 · "~하지 않기 위해"는 not to')
D.note('개념 ① 목적 = in order to = so as to', [
    ('We used the computer to save time.', '우리는 시간을 절약하기 위해 컴퓨터를 사용했다.'),
    ('= We used the computer in order to save time.', 'in order to + 동사원형 (뜻 같음)'),
    ('= We used the computer so as to save time.', 'so as to + 동사원형 (뜻 같음)'),
])
D.note('개념 ② 부정: not을 to 바로 앞에', [
    ('Jake put on a warm jacket not to catch a cold.', 'Jake는 감기에 걸리지 않기 위해 따뜻한 재킷을 입었다.'),
    ('They\'re going to study hard not to fail again.', '그들은 다시 실패하지 않기 위해 열심히 공부할 것이다.'),
    ('주의', 'to not catch(×) → not to catch(○) / in order not to · so as not to 도 가능'),
])
D.step(CARDS(D, '해석 카드', [
    ('We used the computer in order to save time.', '우리는 시간을 절약하기 위해 컴퓨터를 사용했다.'), ('I went to a bookstore so as to buy a book.', '나는 책을 사기 위해 서점에 갔다.'),
    ('We eat in order to live.', '우리는 살기 위해 먹는다.'), ('He left early in order to catch the train.', '그는 기차를 타기 위해 일찍 떠났다.'),
    ('Jake put on a warm jacket not to catch a cold.', 'Jake는 감기에 걸리지 않기 위해 따뜻한 재킷을 입었다.'), ('They\'re going to study hard not to fail again.', '그들은 다시 실패하지 않기 위해 열심히 공부할 것이다.')]))
D.step(PICK(D, '어법 선택', [
    ('We used the computer in order {to save|save} time.', '우리는 시간을 절약하기 위해 컴퓨터를 사용했다.', '정답 ▶ to save\n이유: in order to + 동사원형 (to를 빼면 ×)'),
    ('I went to a bookstore so as {to buy|buy} a book.', '나는 책을 사기 위해 서점에 갔다.', '정답 ▶ to buy\n이유: so as to + 동사원형'),
    ('Jake put on a warm jacket {not to|to not} catch a cold.', 'Jake는 감기에 걸리지 않기 위해 따뜻한 재킷을 입었다.', '정답 ▶ not to\n이유: to부정사의 부정은 not을 to 앞에'),
    ('She didn\'t eat dinner {to lose|to losing} weight.', '그녀는 살을 빼기 위해 저녁을 먹지 않았다.', '정답 ▶ to lose'),
    ('He left early in {order|ordering} to catch the train.', '그는 기차를 타기 위해 일찍 떠났다.', '정답 ▶ order\n이유: in order to는 한 덩어리'),
    ('I study hard {not to|not} fail the test.', '나는 시험에 떨어지지 않기 위해 열심히 공부한다.', '정답 ▶ not to\n이유: not만 쓰면 ×, not + to + 동사원형'),
]))
D.step(MC('같은 뜻 · 부정 표현', [
    ('밑줄 친 부분과 바꿔 쓸 수 있는 것은?<br><b>I went to a bookstore <u>to buy</u> a book.</b>', ['in order to buy', 'buying', 'for buy', 'to bought', 'not to buy'],
     '정답 ▶ in order to buy\n이유: 목적의 to부정사 = in order to = so as to\n오답 ▶ not to buy는 "사지 않기 위해"로 뜻이 반대'),
    ('우리말과 같도록 빈칸에 알맞은 것은?<br>그녀는 늦지 않기 위해 택시를 탔다.<br><b>She took a taxi ______ late.</b>', ['not to be', 'to not be', 'not be', 'to be not', 'be not to'],
     '정답 ▶ not to be\n이유: ~하지 않기 위해 = not to + 동사원형'),
    ('다음 중 뜻이 <b>나머지와 다른</b> 것은?', ['We used the computer not to save time.', 'We used the computer to save time.', 'We used the computer in order to save time.', 'We used the computer so as to save time.', 'To save time, we used the computer.'],
     '정답 ▶ We used the computer not to save time.\n이유: not to = ~하지 않기 위해 (나머지는 모두 "시간을 절약하기 위해")'),
]))
D.step(SCR(D, '우리말 → 영어 배열', [
    ('We eat in order to live.', '우리는 살기 위해 먹는다.'), ('I went to a bookstore so as to buy a book.', '나는 책을 사기 위해 서점에 갔다.'),
    ("They're going to study hard not to fail again.", '그들은 다시 실패하지 않기 위해 열심히 공부할 것이다.'), ('He left early in order to catch the train.', '그는 기차를 타기 위해 일찍 떠났다.')]))
DAYS.append(D.done())

D = Day('a5', '워크북 연습 ① 박스의 동사로 쓰기', 'Part 1 · Part 3 유형: 알맞은 동사를 골라 to부정사로')
D.note('풀이 순서', [('① 문장의 "왜?"를 생각한다', 'We use a camera ______ photographs. → 사진을 찍기 위해'), ('② 알맞은 동사를 골라 to + 동사원형', 'take → to take')])
D.step(VERB(D, '박스 동사로 쓰기 ① (watch · take · send · meet · listen · learn)', [
    ('We use a camera ___ photographs.', 'take', ['to take'], '우리는 사진을 찍기 위해 카메라를 사용한다.', '정답 ▶ to take'),
    ('I turned on the radio ___ to some music.', 'listen', ['to listen'], '나는 음악을 좀 듣기 위해 라디오를 켰다.', '정답 ▶ to listen'),
    ("They went to the airport ___ Ben's sister.", 'meet', ['to meet'], '그들은 Ben의 여동생을 만나기 위해 공항에 갔다.', '정답 ▶ to meet'),
    ('Tom used the computer ___ an email.', 'send', ['to send'], 'Tom은 이메일을 보내기 위해 컴퓨터를 사용했다.', '정답 ▶ to send'),
    ('Jack and Carol went to the cinema ___ a film.', 'watch', ['to watch'], 'Jack과 Carol은 영화를 보기 위해 영화관에 갔다.', '정답 ▶ to watch'),
    ('They went to the museum ___ about the natural world.', 'learn', ['to learn'], '그들은 자연 세계에 대해 배우기 위해 박물관에 갔다.', '정답 ▶ to learn'),
], '괄호 속 동사를 to부정사로 써요.', 'to + 동사원형'))
D.step(VERB(D, '박스 동사로 쓰기 ② (find · pass · protect · keep · give · buy)', [
    ('He went to the shop ___ some bread.', 'buy', ['to buy'], '그는 빵을 좀 사기 위해 가게에 갔다.', '정답 ▶ to buy'),
    ("She's studying ___ her exam.", 'pass', ['to pass'], '그녀는 시험에 합격하기 위해 공부하고 있다.', '정답 ▶ to pass'),
    ('She goes to the gym ___ fit.', 'keep', ['to keep'], '그녀는 건강을 유지하기 위해 체육관에 간다.', '정답 ▶ to keep (keep fit = 건강을 유지하다)'),
    ("He's buying the CD ___ to his brother.", 'give', ['to give'], '그는 남동생에게 주기 위해 그 CD를 사고 있다.', '정답 ▶ to give'),
    ('They put on sun cream ___ their skin.', 'protect', ['to protect'], '그들은 피부를 보호하기 위해 선크림을 발랐다.', '정답 ▶ to protect'),
    ('We looked at the map ___ the way.', 'find', ['to find'], '우리는 길을 찾기 위해 지도를 보았다.', '정답 ▶ to find'),
], '괄호 속 동사를 to부정사로 써요.', 'to + 동사원형'))
D.step(VERB(D, '표현 넣어 쓰기 (Part 3)', [
    ('I phoned the dentist ___ an appointment.', 'make', ['to make'], '나는 예약을 하기 위해 치과에 전화했다.', '정답 ▶ to make (make an appointment = 예약하다)'),
    ('I went to a job agency ___ for a job.', 'look', ['to look'], '나는 일자리를 찾기 위해 직업소개소에 갔다.', '정답 ▶ to look (look for = 찾다)'),
    ('You need this key ___ the door.', 'open', ['to open'], '너는 문을 열기 위해 이 열쇠가 필요하다.', '정답 ▶ to open'),
    ('I need more money ___ my bills.', 'pay', ['to pay'], '나는 청구서를 내기 위해 돈이 더 필요하다.', '정답 ▶ to pay'),
    ('He went to Paris ___ the Eiffel Tower.', 'see', ['to see'], '그는 에펠탑을 보기 위해 파리에 갔다.', '정답 ▶ to see'),
    ('He washes Dad\'s car every Sunday ___ extra pocket money.', 'get', ['to get'], '그는 용돈을 더 받기 위해 일요일마다 아빠의 차를 세차한다.', '정답 ▶ to get'),
], '괄호 속 동사를 to부정사로 써요.', 'to + 동사원형'))
DAYS.append(D.done())

D = Day('a6', '워크북 연습 ② 틀린 곳 고치기', 'Part 4 유형: for to · for · to + -ing · to 빠짐 · in order 뒤 to 빠짐')
D.note('자주 틀리는 5가지', [
    ('for to learn ✗ · for learn ✗', '→ to learn (for를 쓰지 않아요)'), ('keep fit ✗ (목적인데 to 없음)', '→ to keep fit'),
    ('to learning ✗ · to had ✗', '→ to learn · to have (to + 동사원형)'), ('in order getting ✗ · in order see ✗', '→ in order to get · in order to see'),
    ('playing ✗ (목적인데 -ing)', 'She went to the park playing ✗ → to play'),
])
D.step(ERR(D, '오류 찾기 ①', [
    ('I [[go]] to school [[for to]] learn [[English]].', 1, 'to', '나는 영어를 배우기 위해 학교에 간다.', '정답 ▶ for to → to\n이유: 목적은 to + 동사원형만'),
    ('I [[went]] to town [[for]] meet my [[friends]].', 1, 'to', '나는 친구들을 만나기 위해 시내에 갔다.', '정답 ▶ for → to'),
    ('I [[go]] jogging every day [[keep]] [[fit]].', 1, 'to keep', '나는 건강을 유지하기 위해 매일 조깅을 한다.', '정답 ▶ keep → to keep\n이유: 동사가 두 개(go, keep) → 목적은 to keep'),
    ("I'm [[calling]] my friend [[invited]] her to [[come]] to my house.", 1, 'to invite', '나는 친구를 우리 집에 초대하기 위해 전화하고 있다.', '정답 ▶ invited → to invite'),
    ('She [[went]] to the park [[playing]] with her [[friends]].', 1, 'to play', '그녀는 친구들과 놀기 위해 공원에 갔다.', '정답 ▶ playing → to play'),
]))
D.step(ERR(D, '오류 찾기 ②', [
    ('I [[watch]] TV in English [[to learning]] more [[words]].', 1, 'to learn', '나는 더 많은 단어를 배우기 위해 영어로 TV를 본다.', '정답 ▶ to learning → to learn'),
    ('I [[practice]] the piano [[in order getting]] [[better]].', 1, 'in order to get', '나는 더 잘하기 위해 피아노를 연습한다.', '정답 ▶ in order getting → in order to get'),
    ('I [[cleaned]] the kitchen [[for]] help my [[mom]].', 1, 'to', '나는 엄마를 돕기 위해 부엌을 청소했다.', '정답 ▶ for → to'),
    ("We're [[going]] to Egypt [[in order see]] the [[Pyramids]].", 1, 'in order to see', '우리는 피라미드를 보기 위해 이집트에 갈 것이다.', '정답 ▶ in order see → in order to see'),
    ('I [[visit]] the website [[to had]] fun [[learning]] English.', 1, 'to have', '나는 영어를 재미있게 배우기 위해 그 웹사이트를 방문한다.', '정답 ▶ to had → to have\n이유: to 뒤에는 동사원형'),
]))
D.step(PICK(D, '빠르게 어법 고르기', [
    ('I go to school {to|for to} learn English.', '나는 영어를 배우기 위해 학교에 간다.', '정답 ▶ to'),
    ('She went to the park {to play|playing} with her friends.', '그녀는 친구들과 놀기 위해 공원에 갔다.', '정답 ▶ to play'),
    ('I practice the piano in order {to get|getting} better.', '나는 더 잘하기 위해 피아노를 연습한다.', '정답 ▶ to get'),
    ('I go jogging every day {to keep|keep} fit.', '나는 건강을 유지하기 위해 매일 조깅을 한다.', '정답 ▶ to keep'),
    ('I watch TV in English to {learn|learning} more words.', '나는 더 많은 단어를 배우기 위해 영어로 TV를 본다.', '정답 ▶ learn'),
]))
DAYS.append(D.done())

D = Day('a7', '감정의 원인 "~해서"', 'glad · happy · sad · sorry · surprised + to부정사 = 그 감정이 생긴 이유')
D.note('개념 감정 형용사 + to부정사', [
    ("I'm so glad to meet you.", '나는 너를 만나서 정말 기쁘다. (기쁜 이유 = 만나서)'),
    ('She was sad to hear the news.', '그녀는 그 소식을 들어서 슬펐다.'),
    ('해석 요령', 'glad, happy, sad, sorry, surprised, excited 같은 감정 뒤의 to부정사 → "~해서, ~하게 되어"'),
])
D.step(CARDS(D, '해석 카드', [
    ("I'm so glad to meet you.", '나는 너를 만나서 정말 기쁘다.'), ('She was sad to hear the news.', '그녀는 그 소식을 들어서 슬펐다.'),
    ("I'm sorry to hear that.", '그 말을 들으니 유감이야.'), ('We were happy to win the game.', '우리는 경기에 이겨서 행복했다.'),
    ('He was surprised to see the snake.', '그는 그 뱀을 보고 놀랐다.'), ('They were excited to go to the beach.', '그들은 해변에 가게 되어 신이 났다.')],
    guide='감정 뒤의 to부정사는 "~해서"로 해석해요.'))
D.step(MC('해석 · 쓰임 고르기', [
    ('해석이 바른 것은?<br><b>He was surprised to see the snake.</b>', ['그는 그 뱀을 보고 놀랐다.', '그는 그 뱀을 보기 위해 놀랐다.', '그는 그 뱀을 보는 것을 좋아했다.', '그는 놀라서 뱀을 찾았다.', '그는 뱀을 보러 가는 것에 놀랐다.'],
     '정답 ▶ 그는 그 뱀을 보고 놀랐다.\n이유: surprised(감정) + to see → "보고(봐서) 놀랐다"'),
    ('밑줄 친 부분이 "~해서"로 해석되는 것은?', ["I'm glad <u>to meet</u> you.", 'I went out <u>to meet</u> you.', 'I want <u>to meet</u> you.', 'I hope <u>to meet</u> you.', 'I called you <u>to meet</u> you.'],
     "정답 ▶ I'm glad <u>to meet</u> you.\n이유: glad(감정) 뒤 → 만나서 기쁘다\n오답 ▶ went out to meet(목적) / want·hope to meet(명사적)"),
    ('빈칸에 알맞은 것은?<br><b>We were happy ______ the game.</b>', ['to win', 'win', 'won', 'winning', 'to won'], '정답 ▶ to win\n해석 ▶ 우리는 경기에 이겨서 행복했다.'),
    ('우리말을 영어로 바르게 옮긴 것은?<br>나는 그 소식을 들어서 슬펐다.', ['I was sad to hear the news.', 'I was sad hear the news.', 'I was sad to heard the news.', 'I heard the news to be sad.', 'I was sad for hear the news.'], '정답 ▶ I was sad to hear the news.'),
]))
D.step(PICK(D, '어법 선택', [
    ("I'm so glad {to meet|meeting} you.", '나는 너를 만나서 정말 기쁘다.', '정답 ▶ to meet\n이유: 감정의 원인 → to + 동사원형'),
    ('She was sad {to hear|to heard} the news.', '그녀는 그 소식을 들어서 슬펐다.', '정답 ▶ to hear\n이유: 과거 문장이어도 to 다음은 동사원형'),
    ('They were excited {to go|go} to the beach.', '그들은 해변에 가게 되어 신이 났다.', '정답 ▶ to go'),
    ("I'm sorry {to hear|hear} that.", '그 말을 들으니 유감이야.', '정답 ▶ to hear'),
]))
D.step(SCR(D, '우리말 → 영어 배열', [
    ("I'm so glad to meet you.", '나는 너를 만나서 정말 기쁘다.'), ('He was surprised to see the snake.', '그는 그 뱀을 보고 놀랐다.'),
    ('We were happy to win the game.', '우리는 경기에 이겨서 행복했다.')]))
DAYS.append(D.done())

D = Day('a8', '결과 "(…해서) ~하다" · 형용사 수식 "~하기에"', 'grew up to be ~ · fun to solve · easy to read')
D.note('개념 ① 결과', [
    ('The boy grew up to be a great musician.', '그 소년은 자라서 훌륭한 음악가가 되었다.'),
    ('He lived to be 100 years old.', '그는 100세까지 살았다. (살아서 100세가 되었다)'),
    ('요령', 'grow up to be, live to be 처럼 "그 결과 ~하게 되었다"로 앞에서부터 해석해요.'),
])
D.note('개념 ② 형용사 수식', [
    ('The quiz is fun to solve.', '그 퀴즈는 풀기에 재미있다.'),
    ('This book is easy to read.', '이 책은 읽기에 쉽다.'),
    ('요령', 'easy, hard, fun, difficult 같은 형용사 뒤 → "~하기에 (쉽다·어렵다·재미있다)"'),
])
D.step(CARDS(D, '해석 카드', [
    ('The boy grew up to be a great musician.', '그 소년은 자라서 훌륭한 음악가가 되었다.'), ('He lived to be 100 years old.', '그는 100세까지 살았다.'),
    ('She grew up to be a famous scientist.', '그녀는 자라서 유명한 과학자가 되었다.'), ('The quiz is fun to solve.', '그 퀴즈는 풀기에 재미있다.'),
    ('This book is easy to read.', '이 책은 읽기에 쉽다.'), ('The question is hard to answer.', '그 질문은 대답하기에 어렵다.')]))
D.step(MC('쓰임 고르기 (목적 · 감정 · 결과 · 형용사 수식)', [
    use(D, 'The boy grew up to be a great musician.', '그 소년은 자라서 훌륭한 음악가가 되었다.', 2, 'grow up to be = 자라서 (그 결과) ~가 되다', 'to be'),
    use(D, 'This book is easy to read.', '이 책은 읽기에 쉽다.', 3, '형용사 easy 뒤 → 읽기에 쉽다', 'to read'),
    use(D, "I'm so glad to meet you.", '나는 너를 만나서 정말 기쁘다.', 1, '감정 glad 뒤 → 만나서 기쁘다', 'to meet'),
    use(D, 'I got up early to prepare breakfast.', '나는 아침을 준비하기 위해 일찍 일어났다.', 0, '일찍 일어난 이유(목적) → 준비하기 위해', 'to prepare'),
    use(D, 'The quiz is fun to solve.', '그 퀴즈는 풀기에 재미있다.', 3, '형용사 fun 뒤 → 풀기에 재미있다', 'to solve'),
    use(D, 'She was surprised to see him there.', '그녀는 거기서 그를 보고 놀랐다.', 1, '감정 surprised 뒤 → 보고 놀랐다', 'to see'),
    use(D, 'He lived to be 100 years old.', '그는 100세까지 살았다.', 2, 'live to be = 살아서 (그 결과) ~이 되다', 'to be'),
    use(D, 'Tom exercises every day to be healthy.', 'Tom은 건강해지기 위해 매일 운동한다.', 0, '매일 운동하는 이유(목적)', 'to be'),
]))
D.step(MC('해석 고르기', [
    ('해석이 바른 것은?<br><b>She grew up to be a famous scientist.</b>', ['그녀는 자라서 유명한 과학자가 되었다.', '그녀는 유명한 과학자가 되기 위해 자랐다.', '그녀는 유명한 과학자가 되는 것을 원했다.', '그녀는 과학자가 되어서 기뻤다.', '그녀는 과학자가 되기에 어렸다.'], '정답 ▶ 그녀는 자라서 유명한 과학자가 되었다.\n이유: grow up to be = 자라서 ~가 되다(결과)'),
    ('해석이 바른 것은?<br><b>The question is hard to answer.</b>', ['그 질문은 대답하기에 어렵다.', '그 질문에 대답하기 위해 열심히 했다.', '그 질문에 대답해서 힘들었다.', '그 질문은 대답하는 것이다.', '그는 질문에 대답하기 위해 어려웠다.'], '정답 ▶ 그 질문은 대답하기에 어렵다.'),
]))
DAYS.append(D.done())

D = Day('a9', '부사적 vs 명사적 구별 (A / N)', 'Part 5 유형: want·hope·plan·like 뒤 = 명사적 · "왜?"·감정 뒤 = 부사적')
D.note('구별 표', [
    ('명사적 N (~하는 것)', 'want · hope · plan · like · love · decide + to부정사 / 주어 · 보어 자리 (My dream is to ~)'),
    ('부사적 A (~하기 위해 · ~해서)', '완전한 문장 + to부정사(왜?) / 감정 형용사 + to부정사'),
    ('빼 보기', 'to부정사를 빼도 문장이 완전하면 A, 빼면 문장이 망가지면 N'),
])
D.step(MC('A · N 고르기', [
    an(D, 'I came to see you.', '나는 너를 보기 위해 왔다.', 0, 'I came. + 보기 위해(목적)', 'to see'),
    an(D, "I'm saving my money to buy a new car.", '나는 새 차를 사기 위해 돈을 모으고 있다.', 0, '돈을 모으는 목적', 'to buy'),
    an(D, 'Paul arrived in New York to study physics.', 'Paul은 물리학을 공부하기 위해 뉴욕에 도착했다.', 0, '도착한 목적', 'to study'),
    an(D, 'I want to see him again.', '나는 그를 다시 보고 싶다.', 1, 'want의 목적어(보는 것)', 'to see'),
    an(D, 'I went to a store to buy some milk.', '나는 우유를 좀 사기 위해 가게에 갔다.', 0, '가게에 간 목적', 'to buy'),
    an(D, 'My dream is to be a pilot.', '내 꿈은 조종사가 되는 것이다.', 1, 'is 뒤 보어(되는 것)', 'to be'),
    an(D, 'We decided to travel together.', '우리는 함께 여행하기로 결정했다.', 1, 'decide의 목적어(여행하는 것)', 'to travel'),
    an(D, 'She was happy to get the gift.', '그녀는 그 선물을 받아서 행복했다.', 0, '감정 happy의 원인 → 부사적', 'to get'),
    an(D, 'To learn English is fun.', '영어를 배우는 것은 재미있다.', 1, '문장의 주어(배우는 것)', 'To learn'),
    an(D, 'To learn English, he watches movies.', '영어를 배우기 위해, 그는 영화를 본다.', 0, '콤마 뒤에 주절 → 목적(배우기 위해)', 'To learn'),
]))
D.step(TF('빼 보기 T/F', [
    ('I want to see him again.에서 to see him again을 빼도 문장이 완전하다.', False, '정답 ▶ F\n이유: I want. 만으로는 무엇을 원하는지 없어 불완전 → 명사적'),
    ('I went to a store to buy some milk.에서 to buy some milk를 빼도 문장이 완전하다.', True, '정답 ▶ T\n이유: I went to a store. → 완전 → 부사적'),
    ('To learn English, he watches movies.의 To learn은 주어이다.', False, '정답 ▶ F\n이유: 주어는 he. To learn English, 는 목적(배우기 위해)'),
    ('To learn English is fun.의 To learn은 주어이다.', True, '정답 ▶ T\n이유: 동사 is 앞의 주어 → 명사적'),
]))
DAYS.append(D.done())

D = Day('a10', '우리 교과서 7과 문장으로 연습', "Let's Make a Movie! 본문 속 to부정사 · 명사적 vs 부사적")
D.note('교과서 7과의 to부정사', [
    ('A lot of people are working hard to create this movie.', '부사적(목적): 이 영화를 만들기 위해'),
    ('To capture their happy moments, I\'m going to use drones.', '부사적(목적): 포착하기 위해 (맨 앞 + 콤마)'),
    ('So, I use hand signals to calm him.', '부사적(목적): 그를 진정시키기 위해'),
    ('my job is to find perfect places for shooting.', '명사적(보어): 찾는 것'),
    ('I like to travel and enjoy challenges.', '명사적(목적어): 여행하는 것'),
])
D.step(CARDS(D, '교과서 문장 카드', [
    ('A lot of people are working hard to create this movie.', '많은 사람들이 이 영화를 만들기 위해 열심히 일하고 있어요.'),
    ("To capture their happy moments, I'm going to use drones.", '그들의 행복한 순간을 포착하기 위해, 나는 드론을 사용할 거예요.'),
    ('So, I use hand signals to calm him.', '그래서, 나는 그를 진정시키기 위해 수신호를 사용해요.'),
    ('To create a better story, I can change the order of scenes.', '더 좋은 이야기를 만들기 위해, 나는 장면의 순서를 바꿀 수 있어요.'),
    ('My job is to find perfect places for shooting.', '내 일은 촬영을 위한 완벽한 장소를 찾는 거예요.'), ('I like to travel and enjoy challenges.', '나는 여행하는 것을 좋아하고 도전을 즐겨요.')]))
D.step(MC('교과서 문장 · A / N', [
    an(D, 'A lot of people are working hard to create this movie.', '많은 사람들이 이 영화를 만들기 위해 열심히 일하고 있어요.', 0, '열심히 일하는 목적', 'to create'),
    an(D, "To capture their happy moments, I'm going to use drones.", '그들의 행복한 순간을 포착하기 위해, 나는 드론을 사용할 거예요.', 0, '콤마 뒤 주절 → 목적', 'To capture'),
    an(D, 'So, I use hand signals to calm him.', '그래서, 나는 그를 진정시키기 위해 수신호를 사용해요.', 0, '수신호를 쓰는 목적', 'to calm'),
    an(D, 'My job is to find perfect places for shooting.', '내 일은 촬영을 위한 완벽한 장소를 찾는 거예요.', 1, 'is 뒤 보어', 'to find'),
    an(D, 'I like to travel and enjoy challenges.', '나는 여행하는 것을 좋아하고 도전을 즐겨요.', 1, 'like의 목적어', 'to travel'),
    an(D, 'Do you want to meet some of them?', '그들 중 몇 명을 만나 보고 싶나요?', 1, 'want의 목적어', 'to meet'),
]))
D.step(PICK(D, '교과서 문장 · 어법', [
    ('A lot of people are working hard to {create|creating} this movie.', '많은 사람들이 이 영화를 만들기 위해 열심히 일하고 있어요.', '정답 ▶ create'),
    ('{To capture|Capture} their happy moments, I\'m going to use drones.', '그들의 행복한 순간을 포착하기 위해, 나는 드론을 사용할 거예요.', '정답 ▶ To capture\n이유: 콤마 뒤에 주절이 있으므로 목적의 To부정사'),
    ('So, I use hand signals {to calm|calm} him.', '그래서, 나는 그를 진정시키기 위해 수신호를 사용해요.', '정답 ▶ to calm'),
]))
D.step(SCR(D, '교과서 문장 배열', [
    ('A lot of people are working hard to create this movie.', '많은 사람들이 이 영화를 만들기 위해 열심히 일하고 있어요.'),
    ('So, I use hand signals to calm him.', '그래서, 나는 그를 진정시키기 위해 수신호를 사용해요.'),
    ('To create a better story, I can change the order of scenes.', '더 좋은 이야기를 만들기 위해, 나는 장면의 순서를 바꿀 수 있어요.')]))
DAYS.append(D.done())

D = Day('a11', '실전 ① 쓰임이 같은 것 · 다른 것', 'Grammar Build Up 객관식 유형 · 주어진 문장과 쓰임이 같은 to부정사')
D.note('3초 판별', [('want/hope/plan/like + to ~', '명사적'), ('완전한 문장 + to ~ (왜?)', '부사적 · 목적'), ('glad/sad/sorry + to ~', '부사적 · 감정의 원인'), ('My dream is to ~ / To ~ is ...', '명사적 · 보어/주어')])
D.step(MC('주어진 문장과 쓰임이 같은 것', [
    ('밑줄 친 부분과 쓰임이 <b>같은</b> 것은?<br><b>I went to the library <u>to borrow</u> some books.</b>', ['She called me <u>to say</u> thank you.', 'I hope <u>to see</u> you soon.', 'His plan is <u>to travel</u> to Busan.', 'We decided <u>to stay</u> home.', '<u>To read</u> books is fun.'],
     '정답 ▶ She called me <u>to say</u> thank you.\n이유: 주어진 문장 = 목적(빌리기 위해) / 정답 = 목적(말하기 위해)\n오답 ▶ hope·decided의 목적어, is 뒤 보어, 주어 → 모두 명사적'),
    ('밑줄 친 부분과 쓰임이 <b>같은</b> 것은?<br><b>I want <u>to be</u> a movie director.</b>', ['My job is <u>to find</u> perfect places.', 'I use hand signals <u>to calm</u> him.', "I'm glad <u>to meet</u> you.", 'He studied hard <u>to pass</u> the test.', 'She went out <u>to buy</u> milk.'],
     '정답 ▶ My job is <u>to find</u> perfect places.\n이유: 주어진 문장 = 명사적(want의 목적어) / 정답 = 명사적(is 뒤 보어)\n오답 ▶ 나머지는 부사적(목적·감정)'),
    ('밑줄 친 부분과 쓰임이 <b>같은</b> 것은?<br><b>We were happy <u>to win</u> the game.</b>', ['She was sad <u>to hear</u> the news.', 'I went there <u>to win</u> the game.', 'We want <u>to win</u> the game.', 'Our goal is <u>to win</u> the game.', 'He tried <u>to win</u> the game.'],
     '정답 ▶ She was sad <u>to hear</u> the news.\n이유: 둘 다 감정의 원인(~해서)'),
]))
D.step(MC('쓰임이 다른 하나', [
    ('밑줄 친 to부정사 중 쓰임이 <b>다른</b> 하나는?', ['I like <u>to dance</u>.', 'He went to Paris <u>to see</u> the Eiffel Tower.', 'She saved money <u>to buy</u> a bike.', 'I turned on the TV <u>to watch</u> the news.', 'We met <u>to talk</u> about the project.'],
     '정답 ▶ I like <u>to dance</u>.\n이유: like의 목적어(춤추는 것) = 명사적, 나머지는 모두 목적(~하기 위해)'),
    ('밑줄 친 to부정사 중 쓰임이 <b>다른</b> 하나는?', ['She went to the park <u>to take</u> a walk.', 'My hobby is <u>to take</u> pictures.', 'I plan <u>to visit</u> Jeju.', 'He wants <u>to be</u> a chef.', '<u>To exercise</u> every day is good.'],
     '정답 ▶ She went to the park <u>to take</u> a walk.\n이유: 목적(산책하기 위해) = 부사적, 나머지는 명사적(보어·목적어·주어)'),
    ('밑줄 친 to부정사 중 쓰임이 <b>다른</b> 하나는?', ['I need some money <u>to pay</u> my bills.', 'I was surprised <u>to see</u> the snake.', "I'm sorry <u>to hear</u> that.", 'We were excited <u>to go</u> camping.', 'She was glad <u>to get</u> a letter.'],
     '정답 ▶ I need some money <u>to pay</u> my bills.\n이유: 목적(내기 위해) / 나머지는 감정의 원인(~해서)'),
]))
D.step(MC('같은 것끼리 묶기', [
    ('밑줄 친 부분의 쓰임이 같은 것끼리 바르게 묶은 것은?<br>ⓐ I came here <u>to help</u> you.<br>ⓑ I want <u>to help</u> you.<br>ⓒ She studies hard <u>to be</u> a doctor.<br>ⓓ My dream is <u>to be</u> a doctor.', ['ⓐ, ⓒ', 'ⓐ, ⓑ', 'ⓑ, ⓒ', 'ⓒ, ⓓ', 'ⓐ, ⓓ'],
     '정답 ▶ ⓐ, ⓒ\n이유: ⓐ·ⓒ 목적(~하기 위해) / ⓑ want의 목적어 · ⓓ 보어 → 명사적', True),
]))
DAYS.append(D.done())

D = Day('a12', '실전 ② 어법 종합', '어법상 옳은 문장 · 틀린 문장 · 개수 세기 · 영작')
D.note('시험 직전 체크리스트', [
    ('① to + 동사원형', 'to buying ✗ · to bought ✗ · to is ✗ → to buy · to be'), ('② for를 쓰지 않는다', 'for learn ✗ · for to learn ✗ → to learn'),
    ('③ in order to / so as to', 'in order see ✗ → in order to see'), ('④ 부정은 not to', 'to not catch ✗ → not to catch'), ('⑤ 맨 앞이면 콤마', 'To stay healthy, eat fruits.'),
])
D.step(MC('어법상 올바른 · 어색한 문장', [
    ('어법상 <b>올바른</b> 문장은?', ['I went to the bakery to buy some bread.', 'I went to the bakery for buy some bread.', 'I went to the bakery to buying some bread.', 'I went to the bakery buy some bread.', 'I went to the bakery to bought some bread.'], '정답 ▶ I went to the bakery to buy some bread.'),
    ('어법상 <b>올바른</b> 문장은?', ['She took a taxi not to be late.', 'She took a taxi to not be late.', 'She took a taxi not be late.', 'She took a taxi in order not be late.', 'She took a taxi to be not late.'], '정답 ▶ She took a taxi not to be late.\n이유: 부정은 not to + 동사원형'),
    ('어법상 <b>어색한</b> 문장은?', ["We're going to Egypt in order see the Pyramids.", 'I went to a bookstore so as to buy a book.', 'To stay healthy, eat fruits.', "I'm glad to meet you.", 'He grew up to be a great musician.'],
     "정답 ▶ We're going to Egypt in order see the Pyramids.\n이유: in order 뒤에 to가 빠짐 → in order to see"),
    ('어법상 <b>어색한</b> 문장은?', ['She went to the park playing with her friends.', 'He called his friend to ask for help.', 'This book is easy to read.', 'We eat in order to live.', 'I study hard not to fail the test.'],
     '정답 ▶ She went to the park playing with her friends.\n이유: 목적 → to play'),
]))
D.step(MC('틀린 문장 개수 세기', [
    ('어법상 <b>틀린</b> 문장의 개수는?<br>• I go jogging every day keep fit.<br>• I cleaned the kitchen to help my mom.<br>• I watch TV in English to learning more words.<br>• She was sad to hear the news.<br>• They put on sun cream to protect their skin.', ['2개', '1개', '3개', '4개', '5개'],
     '정답 ▶ 2개\n틀린 것 ▶ keep → to keep / to learning → to learn\n맞는 것 ▶ to help ✔ · to hear ✔ · to protect ✔', True),
]))
D.step(MC('빈칸 · 영작', [
    ('우리말과 같도록 할 때 빈칸에 알맞은 것은?<br>나는 건강을 유지하기 위해 매일 걷는다.<br><b>I walk every day ______ healthy.</b>', ['to stay', 'stay', 'for stay', 'staying', 'to staying'], '정답 ▶ to stay'),
    ('다음 우리말을 영어로 옮길 때 5번째로 오는 단어는?<br>그는 사진을 찍기 위해 카메라를 샀다.<br>(bought / to / a camera / he / take / pictures)', ['take', 'to', 'a camera', 'pictures', 'bought'],
     '정답 ▶ take\n이유: He(1) bought(2) a camera(3) to(4) take(5) pictures(6).', True),
]))
D.step(SCR(D, '종합 배열', [
    ('She had to hurry to get there in time.', '그녀는 제시간에 거기에 도착하기 위해 서둘러야 했다.'), ('You should eat less to lose weight.', '너는 살을 빼기 위해 덜 먹어야 한다.'),
    ('Why don\'t we visit those places to learn more about Korean history?', '한국 역사에 대해 더 배우기 위해 그 장소들을 방문해 보는 게 어때?')]))
DAYS.append(D.done())

# ═════════════════ 시간 접속사 when · before · after ═════════════════
D = Day('w1', '시간 접속사 when "~할 때"', 'when + 주어 + 동사 = 언제 그 일이 일어나는지')
D.note('개념 ① when = ~할 때', [
    ('I listen to music when I\'m free.', '나는 한가할 때 음악을 듣는다.'),
    ('when + 주어 + 동사', 'when 뒤에도 문장(주어 + 동사)이 와요. when I\'m free'),
    ('When I was young, I learned Chinese.', '나는 어렸을 때 중국어를 배웠다.'),
])
D.note('개념 ② when절만으로는 문장이 안 돼요', [('When I was young.', '✗ (어렸을 때 → 무엇을 했는지가 없음)'), ('When I was young, I learned Chinese.', '○ 주절(I learned Chinese)이 꼭 있어야 해요.')])
D.step(CARDS(D, '해석 카드', [
    ("I listen to music when I'm free.", '나는 한가할 때 음악을 듣는다.'), ('When I was young, I learned Chinese from my dad.', '나는 어렸을 때 아빠에게 중국어를 배웠다.'),
    ('I smile when I am happy.', '나는 행복할 때 웃는다.'), ('I liked bugs when I was a child.', '나는 어렸을 때 벌레를 좋아했다.'),
    ('Raise your hand when you have a question.', '질문이 있을 때 손을 들어라.'), ('Minji drinks tea when she has a cold.', '민지는 감기에 걸렸을 때 차를 마신다.')],
    guide='when + 주어 + 동사는 "~할 때"로 해석해요.'))
D.step(TF('개념 확인 T/F', [
    ('when은 "~할 때"라는 뜻의 접속사로 쓸 수 있다.', True, '정답 ▶ T'),
    ('접속사 when 뒤에는 주어와 동사가 온다.', True, '정답 ▶ T\n이유: when I(주어) am(동사) happy'),
    ('When I was young.은 혼자서 완전한 문장이다.', False, '정답 ▶ F\n이유: when절은 주절이 있어야 해요. When I was young, I learned Chinese.'),
    ('I smile when I am happy.는 "나는 웃을 때 행복하다."이다.', False, '정답 ▶ F\n이유: when 뒤가 "~할 때" → 나는 행복할 때 웃는다.'),
]))
D.step(MC('해석 고르기', [
    ('해석이 바른 것은?<br><b>I liked bugs when I was a child.</b>', ['나는 어렸을 때 벌레를 좋아했다.', '나는 벌레를 좋아할 때 어렸다.', '나는 어린아이였지만 벌레를 좋아했다.', '나는 벌레를 좋아하는 아이를 알았다.', '나는 언제 벌레를 좋아했니?'], '정답 ▶ 나는 어렸을 때 벌레를 좋아했다.'),
    ('해석이 바른 것은?<br><b>Raise your hand when you have a question.</b>', ['질문이 있을 때 손을 들어라.', '손을 들 때 질문을 해라.', '질문이 있으면 손을 들지 마라.', '언제 질문이 있니?', '손을 들고 질문을 기다려라.'], '정답 ▶ 질문이 있을 때 손을 들어라.'),
    ('우리말과 같도록 빈칸에 알맞은 것은?<br>나는 한가할 때 음악을 듣는다.<br><b>I listen to music ______ I\'m free.</b>', ['when', 'what', 'where', 'that', 'to'], '정답 ▶ when\n이유: ~할 때 = when'),
    ('빈칸에 알맞은 것은?<br><b>______ I have enough money, I will buy you a new phone.</b>', ['When', 'What', 'Who', 'To', 'Because of'], '정답 ▶ When\n해석 ▶ 돈이 충분히 있을 때, 너에게 새 휴대폰을 사 줄게.'),
]))
D.step(SCR(D, '우리말 → 영어 배열', [
    ('I smile when I am happy.', '나는 행복할 때 웃는다.'), ('When I was a child, I liked bugs.', '나는 어렸을 때 벌레를 좋아했다.'),
    ("I listen to music when I'm free.", '나는 한가할 때 음악을 듣는다.'), ('Raise your hand when you have a question.', '질문이 있을 때 손을 들어라.')]))
DAYS.append(D.done())

D = Day('w2', 'before "~하기 전에" · after "~한 후에"', '시간 순서를 나타내는 접속사 두 개')
D.note('개념 before · after', [
    ('I read a book before I go to bed.', '나는 잠자리에 들기 전에 책을 읽는다. (책 → 잠)'),
    ('After Kevin did his homework, he played outside.', 'Kevin은 숙제를 한 후에 밖에서 놀았다. (숙제 → 놀기)'),
    ('Before you eat, you should wash your hands.', '먹기 전에 손을 씻어야 한다.'),
    ('요령', 'before 뒤 일이 나중, after 뒤 일이 먼저 일어나요.'),
])
D.step(CARDS(D, '해석 카드', [
    ('I read a book before I go to bed.', '나는 잠자리에 들기 전에 책을 읽는다.'), ('After Kevin did his homework, he played outside.', 'Kevin은 숙제를 한 후에 밖에서 놀았다.'),
    ('Before you eat, you should wash your hands.', '먹기 전에 손을 씻어야 한다.'), ('Amy did her homework before she watched TV.', 'Amy는 TV를 보기 전에 숙제를 했다.'),
    ('Suho went to bed after he took a shower.', '수호는 샤워를 한 후에 잠자리에 들었다.'), ('My work begins after the shooting is over.', '내 일은 촬영이 끝난 후에 시작된다.')]))
D.step(MC('무엇이 먼저 일어났을까?', [
    ('먼저 일어난 일은?<br><b>Amy did her homework before she watched TV.</b>', ['숙제를 했다', 'TV를 봤다', '둘이 동시에 일어났다', '알 수 없다', 'TV를 본 뒤 숙제를 했다'], '정답 ▶ 숙제를 했다\n이유: before she watched TV = TV를 보기 전에 → 숙제가 먼저'),
    ('먼저 일어난 일은?<br><b>Suho went to bed after he took a shower.</b>', ['샤워를 했다', '잠자리에 들었다', '둘이 동시에 일어났다', '알 수 없다', '잠자리에 든 뒤 샤워했다'], '정답 ▶ 샤워를 했다\n이유: after he took a shower = 샤워를 한 후에 → 샤워가 먼저'),
    ('먼저 일어난 일은?<br><b>After Kevin did his homework, he played outside.</b>', ['숙제를 했다', '밖에서 놀았다', '둘이 동시에 일어났다', '알 수 없다', '논 뒤 숙제를 했다'], '정답 ▶ 숙제를 했다'),
    ('해석이 바른 것은?<br><b>Before you eat, you should wash your hands.</b>', ['먹기 전에 손을 씻어야 한다.', '먹은 후에 손을 씻어야 한다.', '손을 씻을 때 먹어야 한다.', '손을 씻기 전에 먹어야 한다.', '먹을 때 손을 씻지 마라.'], '정답 ▶ 먹기 전에 손을 씻어야 한다.'),
]))
D.step(PICK(D, '뜻에 맞는 접속사 고르기', [
    ('I read a book {before|after} I go to bed.', '나는 잠자리에 들기 전에 책을 읽는다.', '정답 ▶ before\n이유: ~하기 전에'),
    ('Suho went to bed {after|before} he took a shower.', '수호는 샤워를 한 후에 잠자리에 들었다.', '정답 ▶ after\n이유: ~한 후에'),
    ('{Before|After} you eat, you should wash your hands.', '먹기 전에 손을 씻어야 한다.', '정답 ▶ Before'),
    ('My work begins {after|before} the shooting is over.', '내 일은 촬영이 끝난 후에 시작된다.', '정답 ▶ after'),
    ('Amy did her homework {before|after} she watched TV.', 'Amy는 TV를 보기 전에 숙제를 했다.', '정답 ▶ before'),
]))
D.step(SCR(D, '우리말 → 영어 배열', [
    ('I read a book before I go to bed.', '나는 잠자리에 들기 전에 책을 읽는다.'), ('Suho went to bed after he took a shower.', '수호는 샤워를 한 후에 잠자리에 들었다.'),
    ('Before you eat, you should wash your hands.', '먹기 전에 손을 씻어야 한다.')]))
DAYS.append(D.done())

D = Day('w3', 'when · before · after 골라 쓰기', '그림처럼 장면을 떠올리며 알맞은 접속사 고르기')
D.note('세 가지 한눈에', [('when', '~할 때 (같은 때)'), ('before', '~하기 전에 (뒤 일이 나중)'), ('after', '~한 후에 (뒤 일이 먼저)')])
D.step(MC('알맞은 접속사 고르기', [
    ('빈칸에 알맞은 것은?<br><b>Peter usually eats fried chicken ______ he doesn\'t feel good.</b><br>(Peter는 기분이 안 좋을 때 대개 프라이드치킨을 먹는다.)', ['when', 'before', 'after', 'that', 'to'], '정답 ▶ when'),
    ('빈칸에 알맞은 것은?<br><b>Brush your teeth ______ you go to bed.</b><br>(잠자리에 들기 전에 이를 닦아라.)', ['before', 'after', 'when', 'that', 'to'], '정답 ▶ before'),
    ('빈칸에 알맞은 것은?<br><b>______ the movie ended, we went home.</b><br>(영화가 끝난 후에 우리는 집에 갔다.)', ['After', 'Before', 'That', 'To', 'What'], '정답 ▶ After'),
    ('빈칸에 알맞은 것은?<br><b>Put on your coat ______ you go out.</b><br>(밖에 나가기 전에 코트를 입어라.)', ['before', 'after', 'that', 'to', 'what'], '정답 ▶ before'),
    ('빈칸에 알맞은 것은?<br><b>I was very happy ______ I heard the news.</b><br>(그 소식을 들었을 때 나는 매우 기뻤다.)', ['when', 'before', 'that', 'to', 'what'], '정답 ▶ when'),
    ('빈칸에 알맞은 것은?<br><b>You can watch TV ______ you finish your homework.</b><br>(숙제를 끝낸 후에 TV를 봐도 된다.)', ['after', 'before', 'that', 'to', 'what'], '정답 ▶ after'),
]))
D.step(PICK(D, '빠르게 고르기', [
    ('Look both ways {before|after} you cross the street.', '길을 건너기 전에 양쪽을 살펴라.', '정답 ▶ before'),
    ('{When|Before} I feel tired, I take a nap.', '나는 피곤할 때 낮잠을 잔다.', '정답 ▶ When'),
    ('We had lunch {after|before} we finished the class.', '우리는 수업을 마친 후에 점심을 먹었다.', '정답 ▶ after'),
    ("Max gets too excited {when|before} a lot of people are around.", '주변에 사람들이 많을 때 Max는 너무 흥분한다.', '정답 ▶ when'),
]))
DAYS.append(D.done())

D = Day('w4', '부사절의 위치와 콤마(,)', '앞에 오면 콤마 · 뒤에 오면 콤마 없음 · 뜻은 같음')
D.note('개념 위치 바꾸기', [
    ('When I feel tired, I take a nap.', 'when절이 앞 → 절 끝에 콤마(,)'), ('I take a nap when I feel tired.', 'when절이 뒤 → 콤마 없음 (뜻은 같아요)'),
    ('After Kevin did his homework, he played outside.', '= Kevin played outside after he did his homework.'),
])
D.step(TF('콤마 T/F', [
    ('When I feel tired, I take a nap.은 바르다.', True, '정답 ▶ T'), ('I take a nap, when I feel tired.처럼 when절이 뒤에 올 때도 꼭 콤마를 찍는다.', False, '정답 ▶ F\n이유: 뒤에 올 때는 보통 콤마를 쓰지 않아요.'),
    ('When I was young I learned Chinese.는 콤마가 빠졌다.', True, '정답 ▶ T\n이유: when절이 앞에 오면 절 끝에 콤마 → When I was young, I learned Chinese.'),
    ('I smile when I am happy.와 When I am happy, I smile.은 뜻이 같다.', True, '정답 ▶ T'),
]))
D.step(MC('위치 바꿔 쓰기', [
    ('같은 뜻의 문장은?<br><b>I take a nap when I feel tired.</b>', ['When I feel tired, I take a nap.', 'When I take a nap, I feel tired.', 'I feel tired when I take a nap.', 'When I feel tired I take, a nap.', 'I take a nap, when I feel, tired.'],
     '정답 ▶ When I feel tired, I take a nap.\n오답 ▶ 두 절의 내용을 바꾸면 뜻이 달라져요.'),
    ('같은 뜻의 문장은?<br><b>After Kevin did his homework, he played outside.</b>', ['Kevin played outside after he did his homework.', 'Kevin did his homework after he played outside.', 'Kevin played outside before he did his homework.', 'After Kevin played outside, he did his homework.', 'Kevin did his homework when he played outside.'],
     '정답 ▶ Kevin played outside after he did his homework.'),
    ('콤마(,)가 들어갈 자리로 알맞은 곳은?<br><b>Before you ① eat ② you ③ should ④ wash ⑤ your hands.</b>', ['②', '①', '③', '④', '⑤'], '정답 ▶ ②\n이유: Before you eat(부사절) 끝 → Before you eat, you should wash your hands.', True),
]))
D.step(SCR(D, '두 가지 순서로 배열', [
    ('When I am happy, I smile.', '나는 행복할 때 웃는다. (when절을 앞에)'), ('I smile when I am happy.', '나는 행복할 때 웃는다. (when절을 뒤에)'),
    ('When you have a question, raise your hand.', '질문이 있을 때 손을 들어라. (when절을 앞에)'), ('Kevin played outside after he did his homework.', 'Kevin은 숙제를 한 후에 밖에서 놀았다. (after절을 뒤에)')]))
DAYS.append(D.done())

D = Day('w5', '미래 일이어도 현재형으로', 'when · before · after 절 안에서는 will 대신 현재형')
D.note('개념 시간 부사절의 현재 시제', [
    ('When Amy arrives, we will have dinner.', 'Amy가 도착하면 우리는 저녁을 먹을 것이다. (will arrive ✗)'),
    ('Give me a call after you arrive.', '도착한 후에 나에게 전화해 줘.'),
    ('He will call her when he leaves the house.', '그는 집을 나설 때 그녀에게 전화할 것이다. (will leave ✗)'),
    ('규칙', '주절은 will 그대로, when/before/after 절만 현재형'),
])
D.step(PICK(D, '어법 선택', [
    ('When Amy {arrives|will arrive}, we will have dinner.', 'Amy가 도착하면 우리는 저녁을 먹을 것이다.', '정답 ▶ arrives\n이유: 시간 부사절은 미래라도 현재형'),
    ('He will call her when he {leaves|will leave} the house.', '그는 집을 나설 때 그녀에게 전화할 것이다.', '정답 ▶ leaves'),
    ("I'll pick you up when you {are|will be} ready.", '네가 준비되면 데리러 갈게.', '정답 ▶ are'),
    ("I'll show you my photos when I {see|will see} you tomorrow.", '내일 너를 만나면 사진을 보여 줄게.', '정답 ▶ see'),
    ('When I {have|will have} enough money, I will buy you a new phone.', '돈이 충분히 있을 때 너에게 새 휴대폰을 사 줄게.', '정답 ▶ have'),
    ('Give me a call after you {arrive|will arrive}.', '도착한 후에 나에게 전화해 줘.', '정답 ▶ arrive'),
]))
D.step(VERB(D, '알맞은 형태로 쓰기 (Part 2 유형)', [
    ('When Judy ___ ready, I will come to take her.', 'be', ['is'], 'Judy가 준비되면 내가 데리러 갈 것이다.', '정답 ▶ is\n이유: 미래 일이지만 시간 부사절 → 현재형, 주어 Judy(3인칭 단수)'),
    ('We will go out when it ___ raining.', 'stop', ['stops'], '비가 그치면 우리는 나갈 것이다.', '정답 ▶ stops\n이유: 현재형 + 3인칭 단수 -s'),
    ('I will call you after I ___ my homework.', 'finish', ['finish'], '숙제를 끝낸 후에 너에게 전화할게.', '정답 ▶ finish\n이유: after절은 미래 일이라도 현재형 (will finish ✗), 주어 I'),
    ('When I was a child, my grandfather ___.', 'die', ['died'], '내가 어렸을 때 할아버지가 돌아가셨다.', '정답 ▶ died\n이유: was(과거) → 과거의 일은 과거형'),
    ('When she ___ up, she starts the day with yoga.', 'get', ['gets'], '그녀는 일어나면 요가로 하루를 시작한다.', '정답 ▶ gets\n이유: 습관(현재) + 3인칭 단수'),
], '괄호 속 동사를 알맞은 형태로 써요. 시간·주어를 꼭 확인!', '알맞은 형태'))
D.step(ERR(D, '오류 찾기', [
    ('When [[she]] [[will come]] home, we [[will]] [[eat]] dinner.', 1, 'comes', '그녀가 집에 오면 우리는 저녁을 먹을 것이다.', '정답 ▶ will come → comes\n이유: 시간 부사절은 미래라도 현재형'),
    ("I [[will]] [[call]] you after I [[will finish]] my [[homework]].", 2, 'finish', '숙제를 끝낸 후에 너에게 전화할게.', '정답 ▶ will finish → finish'),
    ('We [[will]] [[go]] on a picnic when the weather [[will be]] [[nice]].', 2, 'is', '날씨가 좋으면 우리는 소풍을 갈 것이다.', '정답 ▶ will be → is'),
]))
DAYS.append(D.done())

D = Day('w6', '두 문장 잇기 (Part 3)', 'when · before · after로 두 문장을 하나로')
D.note('잇는 요령', [
    ('They\'ll give us a call. + They\'ll get home tonight.', '→ They\'ll give us a call when they get home tonight. (when절 안은 현재형)'),
    ('Sam was four. + He learned to kick a ball.', '→ When Sam was four, he learned to kick a ball.'),
])
D.step(MC('두 문장 잇기', [
    ('두 문장을 when으로 바르게 이은 것은?<br>I\'ll pick you up. + You will be ready.', ["I'll pick you up when you are ready.", "I'll pick you up when you will be ready.", "I'll pick you up when are you ready.", "When I'll pick you up, you are ready.", "I'll pick you up, when ready you are."],
     "정답 ▶ I'll pick you up when you are ready.\n이유: when절 안은 현재형(are)"),
    ('두 문장을 when으로 바르게 이은 것은?<br>The dog barked. + It noticed the cat.', ['The dog barked when it noticed the cat.', 'The dog noticed when it barked the cat.', 'When the dog barked, it noticed.', 'The dog barked when noticed the cat.', 'The dog barked when the cat it noticed.'],
     '정답 ▶ The dog barked when it noticed the cat.\n이유: when + 주어(it) + 동사(noticed)'),
    ('두 문장을 after로 바르게 이은 것은?<br>She finished dinner. + Then she washed the dishes.', ['After she finished dinner, she washed the dishes.', 'After she washed the dishes, she finished dinner.', 'She finished dinner after she washed the dishes.', 'After finished dinner she, washed the dishes.', 'She washed after the dishes she finished dinner.'],
     '정답 ▶ After she finished dinner, she washed the dishes.\n이유: 저녁 먹기가 먼저 → after 뒤에'),
    ('두 문장을 before로 바르게 이은 것은?<br>I did my homework. + Then I played games.', ['I did my homework before I played games.', 'I played games before I did my homework.', 'Before I did my homework, I played games.', 'I did before my homework I played games.', 'I did my homework before played games.'],
     '정답 ▶ I did my homework before I played games.\n이유: 게임이 나중 → before 뒤에'),
]))
D.step(SCR(D, '우리말 → 영어 배열', [
    ("I'll show you my photos when I see you tomorrow.", '내일 너를 만나면 사진을 보여 줄게.'), ('When Sam was four, he learned to kick a ball.', 'Sam은 네 살 때 공 차는 법을 배웠다.'),
    ('Buy some bread when you do the shopping.', '장을 볼 때 빵을 좀 사 와라.'), ('After she finished dinner, she washed the dishes.', '그녀는 저녁을 먹은 후에 설거지를 했다.')]))
DAYS.append(D.done())

D = Day('w7', '교과서 7과 문장 · 접속사 when vs 의문사 when', '"~할 때"(접속사)와 "언제?"(의문사) 구별')
D.note('구별 표', [
    ('When is your birthday?', '의문사 when = 언제? (물음표로 끝나는 질문, 뒤에 동사가 먼저)'),
    ('I was happy when I got the gift.', '접속사 when = ~할 때 (주어 + 동사가 이어짐)'),
])
D.note('교과서 7과의 시간 접속사', [
    ('Max is a great actor, but he sometimes gets too excited when a lot of people are around.', '주변에 사람들이 많을 때'),
    ('My work begins after the shooting is over.', '촬영이 끝난 후에'),
    ('I create sound effects in my studio when recording on location is not easy.', '야외 촬영장에서 녹음하는 게 쉽지 않을 때'),
])
D.step(CARDS(D, '교과서 문장 카드', [
    ('Max gets too excited when a lot of people are around.', '주변에 사람들이 많을 때 Max는 너무 흥분해요.'), ('My work begins after the shooting is over.', '내 일은 촬영이 끝난 후에 시작돼요.'),
    ('I create sound effects in my studio when recording on location is not easy.', '야외 촬영장에서 녹음하는 게 쉽지 않을 때 나는 내 작업실에서 음향 효과를 만들어요.')]))
D.step(MC('접속사 when · 의문사 when', [
    ('밑줄 친 when의 쓰임이 <b>나머지와 다른</b> 것은?', ['<u>When</u> is your birthday?', 'I was happy <u>when</u> I got the gift.', '<u>When</u> I feel tired, I take a nap.', 'Max gets excited <u>when</u> people are around.', 'Call me <u>when</u> you arrive.'],
     '정답 ▶ <u>When</u> is your birthday?\n이유: 의문사(언제?) / 나머지는 접속사(~할 때)'),
    ('밑줄 친 when이 "~할 때"로 쓰인 것은?', ['I create sound effects <u>when</u> recording on location is not easy.', '<u>When</u> did you get up?', '<u>When</u> do you play soccer?', 'Do you know <u>when</u> the movie starts?', '<u>When</u> will you come back?'],
     '정답 ▶ I create sound effects <u>when</u> recording on location is not easy.\n이유: 주어(recording on location) + 동사(is) → 접속사\n오답 ▶ 나머지는 "언제"를 묻는 의문사'),
    ('교과서 문장과 같은 뜻은?<br><b>My work begins after the shooting is over.</b>', ['촬영이 끝난 후에 내 일이 시작된다.', '내 일이 끝난 후에 촬영이 시작된다.', '촬영이 끝나기 전에 내 일이 시작된다.', '촬영할 때 내 일이 끝난다.', '내 일은 촬영을 끝내는 것이다.'], '정답 ▶ 촬영이 끝난 후에 내 일이 시작된다.'),
]))
D.step(SCR(D, '교과서 문장 배열', [
    ('My work begins after the shooting is over.', '내 일은 촬영이 끝난 후에 시작돼요.'), ('Max gets too excited when a lot of people are around.', '주변에 사람들이 많을 때 Max는 너무 흥분해요.')]))
DAYS.append(D.done())

D = Day('w8', '실전 시간 접속사 종합', '어법상 옳은 문장 · 틀린 개수 · 뜻 고르기')
D.note('시험 직전 체크리스트', [
    ('① 뜻', 'when ~할 때 · before ~하기 전에 · after ~한 후에'), ('② 접속사 뒤 주어 + 동사', 'when tired ✗ → when I am tired'),
    ('③ 앞에 오면 콤마', 'When I feel tired, I take a nap.'), ('④ 미래라도 현재형', 'when he will leave ✗ → when he leaves'), ('⑤ 의문사 when과 구별', 'When is ~? = 언제'),
])
D.step(MC('어법상 올바른 · 어색한 문장', [
    ('어법상 <b>올바른</b> 문장은?', ['When Amy arrives, we will have dinner.', 'When Amy will arrive, we will have dinner.', 'When Amy arrive, we will have dinner.', 'When arrives Amy, we will have dinner.', 'Amy arrives when, we will have dinner.'], '정답 ▶ When Amy arrives, we will have dinner.'),
    ('어법상 <b>어색한</b> 문장은?', ["I'll call you after I will get home.", 'Before you eat, you should wash your hands.', 'I read a book before I go to bed.', 'I liked bugs when I was a child.', 'After Kevin did his homework, he played outside.'],
     "정답 ▶ I'll call you after I will get home.\n이유: after절은 현재형 → after I get home"),
    ('어법상 <b>어색한</b> 문장은?', ['Raise your hand when have a question.', 'When I am happy, I smile.', 'My work begins after the shooting is over.', 'Look both ways before you cross the street.', "I'll pick you up when you are ready."],
     '정답 ▶ Raise your hand when have a question.\n이유: when 뒤에 주어(you)가 빠짐 → when you have a question'),
]))
D.step(MC('틀린 문장 개수 세기', [
    ('어법상 <b>틀린</b> 문장의 개수는?<br>• When I will see you tomorrow, I\'ll show you my photos.<br>• I take a nap when I feel tired.<br>• Before I go to bed, I read a book.<br>• He will call her when he leaves the house.<br>• When I was young I learned Chinese.', ['2개', '1개', '3개', '4개', '0개'],
     "정답 ▶ 2개\n틀린 것 ▶ When I will see → When I see / When I was young 뒤 콤마 빠짐\n맞는 것 ▶ 나머지 3개 ✔", True),
]))
D.step(MC('뜻 고르기 · 영작', [
    ('우리말과 같도록 빈칸에 알맞은 것끼리 짝지은 것은?<br>나는 샤워를 한 후에 잠자리에 든다. / 나는 아침을 먹기 전에 운동한다.<br>I go to bed (A) ______ I take a shower. / I exercise (B) ______ I eat breakfast.', ['after – before', 'before – after', 'when – before', 'after – when', 'before – before'], '정답 ▶ after – before', True),
    ('우리말을 영어로 바르게 옮긴 것은?<br>그 소식을 들었을 때 나는 놀랐다.', ['When I heard the news, I was surprised.', 'When I was surprised, I heard the news.', 'I heard the news when surprised.', 'When heard I the news, I was surprised.', 'I was surprised, when I will hear the news.'], '정답 ▶ When I heard the news, I was surprised.'),
]))
D.step(SCR(D, '종합 배열', [
    ('When Amy arrives, we will have dinner.', 'Amy가 도착하면 우리는 저녁을 먹을 것이다.'), ('Give me a call after you arrive.', '도착한 후에 나에게 전화해 줘.'),
    ('Look both ways before you cross the street.', '길을 건너기 전에 양쪽을 살펴라.')]))
DAYS.append(D.done())

for d in DAYS: ansfirst(d['steps'])
path = '/home/claude/proj/data/m1-grammar-to1.js'
PK = json.loads(subprocess.check_output(['node', '-e', "global.window={};require('%s');process.stdout.write(JSON.stringify(window.PKG))" % path]))
base = [d for d in PK['days'] if not d['id'][0] in 'aw']
assert len(base) == 20, len(base)
PK['days'] = base + DAYS
for i, d in enumerate(PK['days']): d['name'] = 'DAY %d' % (i + 1)
PK['unit'] = '공통 문법 · to부정사 ①② · 접속사 that · 시간 접속사'
PK['title'] = 'to부정사 · 접속사 that · when / before / after'
PK['titleKo'] = '~하는 것 · ~하기 위해 · ~라고 · ~할 때 / 전에 / 후에'
src = open(path, encoding='utf-8').read(); head = src[:src.index('window.PKG')]
if '시간 접속사' not in head: head = head.rstrip('\n') + '\n/* 11/10: DAY 21~40 = 동아(윤정미) 7과 문법 · to부정사 부사적 용법(a1~a12) · 시간 접속사 when/before/after(w1~w8) (gen/gen_m1d7gram.py) */\n'
write(PK, path, head)
print('ok', len(PK['days']), [(d['name'], d['id'], sum(len(s['items']) for s in d['steps'])) for d in DAYS])
