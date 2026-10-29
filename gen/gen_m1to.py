import sys, json, re
sys.path.insert(0, '/tmp/claude-0/-home-claude/a9e3e882-1f02-5d62-8f70-aced81bc59d2/scratchpad')
from gencommon import write
from dlgcommon import ansfirst
# 중1 공통 문법 · to부정사 ① 명사적 용법 (10/29). 동아(윤정미)·천재(소영순) 학생 모두 열림. DAY 고르기(pick)
# 각 DAY의 '본문' 탭 = 개념 노트 + 그날 나온 예문(해석 포함). 문항 문장은 모두 예문 목록에 자동으로 들어간다.

class Day:
    def __init__(s, did, rng, story):
        s.d = {'id': did, 'name': 'DAY', 'range': rng, 'story': story, 'passage': [], 'steps': []}
        s.notes, s.ex, s.seen = [], [], set()
    def note(s, title, rows):  # rows: [(왼쪽, 오른쪽)]
        s.notes.append(['#', title, '']); s.notes += [['', a, b] for a, b in rows]
    def sent(s, en, ko):
        if en not in s.seen: s.seen.add(en); s.ex.append(['', en, ko])
    def step(s, st): s.d['steps'].append(st); return st
    def done(s):
        s.d['passage'] = s.notes + ([['#', '예문', '']] + s.ex if s.ex else [])
        return s.d

def cards(title, items, n=None, guide='카드를 한 번 읽고, 퀴즈에서 짝이 맞는 것을 고르세요.'): return {'type': 'vocab', 'title': title, 'guide': guide, 'quizN': n or len(items), 'items': [list(x) for x in items]}
def TF(title, items, guide='맞으면 T, 틀리면 F를 고르세요.'): return {'type': 'tf', 'title': title, 'guide': guide, 'items': [[a, b, c, None, None] for a, b, c in items]}
def MC(title, items, guide='알맞은 답을 고르세요.'): return {'type': 'mc', 'title': title, 'guide': guide, 'items': [{'q': q, 'opts': o, 'ex': x} for q, o, x in items]}
def PICK(D, title, items, guide='어법상 알맞은 것을 고르세요.'):
    for s, ko, x in items: D.sent(re.sub(r'\{([^|}]*)\|[^}]*\}', r'\1', s), ko)
    return {'type': 'pick', 'title': title, 'guide': guide, 'items': [{'s': s, 'ex': x} for s, ko, x in items]}
def VERB(D, title, items, guide, ph):
    for s, v, a, ko, x in items: D.sent(s.replace('___', a[0]), ko)
    return {'type': 'verb', 'title': title, 'guide': guide, 'free': True, 'ph': ph, 'items': [{'s': s, 'v': v, 'a': a, 'ex': x} for s, v, a, ko, x in items]}
def SCR(D, title, items):
    for en, ko in items: D.sent(en, ko)
    return {'type': 'scramble', 'title': title, 'guide': '우리말에 맞게 단어를 눌러 문장을 완성하세요.', 'items': [{'ko': ko, 'en': en} for en, ko in items]}
def ERR(D, title, items):
    for s, w, f, ko, x in items:
        k = [0]
        def rep(m):
            r = f if k[0] == w else m.group(1); k[0] += 1; return r
        D.sent(re.sub(r'\[\[(.+?)\]\]', rep, s), ko)
    return {'type': 'error', 'title': title, 'guide': '어법상 틀린 곳을 고르세요.', 'items': [{'s': s, 'w': w, 'fix': f, 'ex': x} for s, w, f, ko, x in items]}
U = lambda s, u: s.replace(u, '<u>' + u + '</u>', 1)
def Q(en, u=None): return '<br><b>' + (U(en, u) if u else en) + '</b>'

ROLE = ['주어 (~하는 것은)', '목적어 (~하는 것을)', '보어 (~하는 것이다)']
def role(D, en, u, ko, ans, why):
    D.sent(en, ko)
    opts = [ROLE[ans]] + [r for i, r in enumerate(ROLE) if i != ans]
    return ('밑줄 친 to부정사의 역할은?' + Q(en, u), opts, '정답 ▶ %s\n이유: %s\n해석 ▶ %s' % (ROLE[ans], why, ko))

DAYS = []

# ═════════ DAY 1 · to부정사가 뭐예요? ═════════
D = Day('t1', 'to부정사가 뭐예요?', 'to + 동사원형 알아보기 · to부정사와 전치사 to 구별하기')
D.note('개념 ① to부정사 = to + 동사원형', [
    ('to + 동사원형', '동사 앞에 to를 붙인 모양이 to부정사예요. to 다음에는 꼭 동사원형이 와요.'),
    ('동사원형', '-s, -ed, -ing가 붙지 않은 동사의 원래 모양 (plays ✗ played ✗ playing ✗ → play ✔)'),
    ('play → to play', '놀다 → 노는 것, 놀기'),
    ('read → to read', '읽다 → 읽는 것, 읽기'),
    ('be → to be', '~이다, ~이 되다 → ~이 되는 것 (is·am·are의 원형은 be)'),
])
D.note('개념 ② 전치사 to와 헷갈리지 않기', [
    ('to + 동사원형 = to부정사', 'I want to eat. (먹는 것을 원한다 → 먹고 싶다)'),
    ('to + 명사·대명사 = 전치사 to', 'I go to school. (학교에) / Give it to me. (나에게) → to부정사 아님!'),
    ('구별법', 'to 바로 뒤의 낱말이 동사(~하다)면 to부정사, 장소·사람(명사)이면 전치사예요.'),
])
D.note('개념 ③ 명사적 용법', [
    ('to부정사의 명사적 용법', 'to부정사가 명사처럼 쓰여서 "~하는 것, ~하기"로 해석돼요.'),
    ('to swim', '수영하는 것, 수영하기'),
])
D.step(cards('개념 카드', [
    ('to부정사', 'to + 동사원형'), ('동사원형', '-s·-ed·-ing가 붙지 않은 원래 모양'), ('to play', '노는 것, 놀기'),
    ('to read', '읽는 것, 읽기'), ('to swim', '수영하는 것, 수영하기'), ('to be', '~이 되는 것, ~인 것'),
    ('to learn', '배우는 것, 배우기'), ('to school', '학교에 (전치사 to · to부정사 아님!)')]))
D.step(TF('개념 확인 T/F', [
    ('to 다음에는 동사원형이 온다.', True, '정답 ▶ T\n이유: to부정사 = to + 동사원형. to play, to read, to be처럼 -s·-ed·-ing 없이 써요.'),
    ('to plays는 바른 to부정사이다.', False, '정답 ▶ F\n이유: to 다음에는 동사원형! plays(-s)가 아니라 play → to play'),
    ('go to school의 to는 to부정사이다.', False, '정답 ▶ F\n이유: to 다음이 school(명사)이니 전치사 to예요. "학교에"라는 뜻이에요.\n포인트 ▶ to 뒤가 동사면 to부정사, 명사면 전치사'),
    ('to부정사의 명사적 용법은 "~하는 것, ~하기"로 해석한다.', True, '정답 ▶ T\n이유: 명사처럼 쓰이니 "~하는 것, ~하기"로 해석해요. to swim = 수영하는 것'),
    ('to swimming은 바른 to부정사이다.', False, '정답 ▶ F\n이유: to + 동사원형이므로 swimming(-ing)이 아니라 swim → to swim'),
    ('is의 동사원형은 be이므로, "~이 되는 것"은 to be로 쓴다.', True, '정답 ▶ T\n이유: is·am·are·was·were의 원형은 모두 be → to be (to is ✗)'),
]))
mc1 = [
    ('밑줄 친 to가 to부정사인 것은?', [U('I want to eat pizza.', 'to'), U('I go to school by bus.', 'to'), U('She gave a pen to me.', 'to'), U('We walked to the park.', 'to')],
     '정답 ▶ I want <u>to</u> eat pizza.\n이유: to 다음이 eat(동사원형) → to부정사 (먹는 것을 원한다 = 먹고 싶다)\n오답 ▶ to school(학교에) / to me(나에게) / to the park(공원으로)는 to 다음이 명사·대명사 → 전치사 to'),
    ('to부정사가 쓰인 문장은?', ['I like to read books.', 'I went to the library.', 'Listen to me.', 'He talked to his mom.'],
     '정답 ▶ I like to read books.\n이유: to read = to + 동사원형 (책 읽는 것을 좋아한다)\n오답 ▶ to the library / to me / to his mom은 모두 to + 명사(대명사) → 전치사'),
    ('to부정사가 <b>아닌</b> 것은?', ['to the store', 'to dance', 'to help', 'to be'],
     '정답 ▶ to the store\n이유: to 다음이 the store(가게, 명사) → 전치사 to (가게에)\n오답 ▶ to dance(춤추는 것) / to help(돕는 것) / to be(~이 되는 것)는 to + 동사원형'),
    ('빈칸에 알맞은 것은?' + Q('I want to ______ a movie.'), ['watch', 'watches', 'watched', 'watching'],
     '정답 ▶ watch\n이유: to 다음에는 동사원형 → to watch (영화 보는 것을 원한다 = 영화 보고 싶다)\n오답 ▶ watches(-s) / watched(-ed) / watching(-ing)은 동사원형이 아니에요.'),
    ('to부정사를 바르게 쓴 것은?', ['to be', 'to is', 'to am', 'to being'],
     '정답 ▶ to be\n이유: is·am의 동사원형은 be → to be\n오답 ▶ to is / to am / to being은 모두 동사원형이 아니에요.'),
]
for q, o, x in mc1:
    if '<u>' not in q and '<b>' not in q: pass
D.sent('I want to eat pizza.', '나는 피자를 먹고 싶다. (피자 먹는 것을 원한다)'); D.sent('I go to school by bus.', '나는 버스로 학교에 간다. (전치사 to)')
D.sent('I like to read books.', '나는 책 읽는 것을 좋아한다.'); D.sent('I went to the library.', '나는 도서관에 갔다. (전치사 to)')
D.step(MC('to부정사 찾기', mc1))
D.step(PICK(D, '어법 · to 다음은 동사원형', [
    ('I want to {eat|eats} pizza.', '나는 피자를 먹고 싶다.', '정답 ▶ eat\n이유: to + 동사원형 → to eat\n오답 ▶ eats는 -s가 붙은 모양이라 to 다음에 못 와요.'),
    ('She likes to {read|reading} comic books.', '그녀는 만화책 읽는 것을 좋아한다.', '정답 ▶ read\n이유: to + 동사원형 → to read\n오답 ▶ to 다음에 -ing는 쓰지 않아요.'),
    ('We hope to {visit|visited} Jeju Island.', '우리는 제주도를 방문하기를 바란다.', '정답 ▶ visit\n이유: to + 동사원형 → to visit\n오답 ▶ visited(-ed)는 과거형이라 to 다음에 못 와요.'),
    ('He wants to {be|is} a doctor.', '그는 의사가 되고 싶어 한다.', '정답 ▶ be\n이유: is의 동사원형은 be → to be\n포인트 ▶ to is, to am, to are는 모두 틀린 표현'),
    ('My dream is to {travel|travels} around the world.', '내 꿈은 세계 여행을 하는 것이다.', '정답 ▶ travel\n이유: to + 동사원형 → to travel'),
    ('They need to {study|studies} hard.', '그들은 열심히 공부할 필요가 있다.', '정답 ▶ study\n이유: to + 동사원형 → to study (studies는 -es가 붙은 모양)'),
]))
D.step(VERB(D, 'to부정사로 바꿔 쓰기', [
    ('I want ___ a new bike.', 'buy', ['to buy'], '나는 새 자전거를 사고 싶다.', '정답 ▶ to buy\n이유: to + 동사원형 (buy → to buy)'),
    ('She hopes ___ a singer.', 'be', ['to be'], '그녀는 가수가 되기를 바란다.', '정답 ▶ to be\n이유: be는 이미 동사원형 → to be'),
    ('We plan ___ soccer after school.', 'play', ['to play'], '우리는 방과 후에 축구를 할 계획이다.', '정답 ▶ to play\n이유: to + 동사원형 (play → to play)'),
    ('Tom needs ___ some water.', 'drink', ['to drink'], 'Tom은 물을 좀 마실 필요가 있다.', '정답 ▶ to drink\n이유: to + 동사원형 (drink → to drink)'),
], '( ) 안의 동사를 to부정사(to + 동사원형)로 바꿔 쓰세요.', 'to + 동사원형으로 쓰기'))
DAYS.append(D.done())

# ═════════ DAY 2 · '~하는 것'으로 해석하기 ═════════
D = Day('t2', "'~하는 것'으로 해석하기", "명사적 용법 해석 찾기 · '~하는 것'과 '~하기 위해' 구별")
D.note('개념 ① 명사적 용법은 "~하는 것, ~하기"', [
    ('to play', '노는 것, 놀기'),
    ('like to ~', '~하는 것을 좋아하다'),
    ('want to ~', '~하는 것을 원하다 → 자연스럽게 "~하고 싶다"'),
    ('hope to ~ / decide to ~', '~하기를 바라다 / ~하기로 결심하다'),
    ('To ~ is ...', '~하는 것은 …이다'),
    ('My dream is to ~', '내 꿈은 ~하는 것이다'),
])
D.note('개념 ② "~하기 위해"는 부사적 용법(목적)', [
    ('~하기 위해', 'to부정사가 "왜?"에 대한 이유(목적)를 나타낼 때 → 부사적 용법'),
    ('끊어 보기', 'to 바로 앞에서 끊어 봐요. 앞부분만으로 문장이 끝나면 "~하기 위해"예요.'),
    ('I went to the store / to buy milk.', '"나는 가게에 갔다."로 끝남 → 우유를 사기 위해 (부사적)'),
    ('I want / to buy milk.', '"나는 원한다…" 뭘? 끝나지 않음 → 우유 사는 것을 (명사적)'),
])
D.step(cards('개념 카드', [
    ('to play', '노는 것, 놀기'), ('like to ~', '~하는 것을 좋아하다'), ('want to ~', '~하는 것을 원하다 = ~하고 싶다'),
    ('hope to ~', '~하기를 바라다'), ('decide to ~', '~하기로 결심하다'), ('To ~ is ...', '~하는 것은 …이다'),
    ('My dream is to ~', '내 꿈은 ~하는 것이다'), ('~하기 위해', '부사적 용법(목적) · 명사적 아님!')]))
def tr(en, ko, wrong, why):
    D.sent(en, ko); return ('다음 문장의 해석으로 알맞은 것은?' + Q(en), [ko] + wrong, '정답 ▶ %s\n이유: %s' % (ko, why))
D.step(MC('해석 고르기', [
    tr('I like to swim.', '나는 수영하는 것을 좋아한다.', ['나는 수영하기 위해 좋아한다.', '나는 수영을 했다.', '나는 수영장을 좋아한다.'],
       'like(좋아하다) 뒤의 to swim = "수영하는 것을" (명사적)\n오답 ▶ "수영하기 위해 좋아한다"는 말이 안 돼요. I like만으로는 "뭘 좋아해?"가 남으니 "~하는 것"이에요.'),
    tr('I want to be a teacher.', '나는 선생님이 되고 싶다.', ['나는 선생님이 되기 위해 원한다.', '나는 선생님이었다.', '나는 선생님을 원한다.'],
       'want to be = "되는 것을 원하다" → 자연스럽게 "되고 싶다" (명사적)'),
    tr('To read books is fun.', '책을 읽는 것은 재미있다.', ['책을 읽기 위해 재미있다.', '책은 재미있게 읽힌다.', '나는 재미있는 책을 읽었다.'],
       '문장 맨 앞 To read books = "책을 읽는 것은" (명사적 · 주어)'),
    tr('My plan is to visit Busan.', '나의 계획은 부산을 방문하는 것이다.', ['부산을 방문하기 위해 계획했다.', '나는 부산을 방문했다.', '나의 계획은 부산에 있다.'],
       'is 뒤의 to visit = "방문하는 것이다" (명사적 · 보어)'),
    tr('She decided to study hard.', '그녀는 열심히 공부하기로 결심했다.', ['그녀는 열심히 공부하기 위해 결심했다.', '그녀는 열심히 공부했다.', '그녀는 공부를 그만두기로 했다.'],
       'decide to ~ = "~하기로 결심하다" (명사적 · decide의 목적어)'),
    tr('He hopes to win the game.', '그는 경기에서 이기기를 바란다.', ['그는 경기에서 이기기 위해 바란다.', '그는 경기에서 이겼다.', '그는 경기를 보기를 바란다.'],
       'hope to ~ = "~하기를 바라다" (명사적 · hope의 목적어)'),
    tr('I went to the store to buy milk.', '나는 우유를 사기 위해 가게에 갔다.', ['나는 우유를 사는 것을 가게에 갔다.', '나는 우유를 사는 것을 원했다.', '나는 가게에서 우유를 팔았다.'],
       '끊어 보기 → I went to the store / to buy milk. "나는 가게에 갔다."로 이미 끝나요 → to buy는 "사기 위해" (부사적 · 목적)\n포인트 ▶ 오늘 배우는 명사적 용법과 구별!'),
    tr('She studies hard to pass the test.', '그녀는 시험에 통과하기 위해 열심히 공부한다.', ['그녀는 시험에 통과하는 것을 열심히 공부한다.', '그녀는 시험에 통과했다.', '그녀는 시험 공부를 싫어한다.'],
       '끊어 보기 → She studies hard / to pass the test. "그녀는 열심히 공부한다."로 끝나요 → "통과하기 위해" (부사적 · 목적)'),
]))
for en, ko in [('I want to play outside.', '나는 밖에서 놀고 싶다.'), ('I came here to see you.', '나는 너를 보기 위해 여기에 왔다.'),
               ('He got up early to catch the bus.', '그는 버스를 타기 위해 일찍 일어났다.'), ('We went to the park to run.', '우리는 달리기 위해 공원에 갔다.'),
               ('She saved money to buy a bike.', '그녀는 자전거를 사기 위해 돈을 모았다.'), ('I like to sing.', '나는 노래하는 것을 좋아한다.'),
               ('My dream is to be a pilot.', '내 꿈은 조종사가 되는 것이다.'), ('To swim is fun.', '수영하는 것은 재미있다.')]: D.sent(en, ko)
D.step(MC("'~하는 것' vs '~하기 위해' 가려내기", [
    ("밑줄 친 to부정사가 <b>'~하는 것(~하기)'</b>으로 해석되는 것은?", [U('I want to play outside.', 'to play'), U('I came here to see you.', 'to see'), U('He got up early to catch the bus.', 'to catch'), U('We went to the park to run.', 'to run')],
     "정답 ▶ I want to play outside.\n이유: 끊어 보기 → I want / … '원한다' 뭘? 안 끝남 → '노는 것을' 원한다 (명사적)\n오답 ▶ 나머지는 to 앞에서 '나는 여기에 왔다 / 그는 일찍 일어났다 / 우리는 공원에 갔다'로 문장이 끝나요 → '~하기 위해'(부사적)"),
    ("밑줄 친 to부정사가 <b>'~하기 위해'</b>로 해석되는 것은?", [U('She saved money to buy a bike.', 'to buy'), U('I like to sing.', 'to sing'), U('My dream is to be a pilot.', 'to be'), U('To swim is fun.', 'To swim')],
     "정답 ▶ She saved money to buy a bike.\n이유: She saved money(그녀는 돈을 모았다)로 문장이 끝나고, to buy가 '왜?'에 답해요 → 자전거를 사기 위해\n오답 ▶ to sing(노래하는 것을) / to be(되는 것이다) / To swim(수영하는 것은)은 모두 '~하는 것'"),
    ("두 문장의 to부정사 해석이 <b>같은</b> 것끼리 묶인 것은?", ['I like to dance. / She wants to dance.', 'I like to dance. / I went out to dance.', 'He came to help me. / He wants to help me.', 'To run is fun. / I ran to catch the bus.'],
     "정답 ▶ I like to dance. / She wants to dance.\n이유: 둘 다 동사(like, want) 뒤에서 '춤추는 것을' → 명사적\n오답 ▶ went out to dance(춤추기 위해) / came to help(돕기 위해) / ran to catch(타기 위해)는 부사적"),
]))
for en, ko in [('I like to dance.', '나는 춤추는 것을 좋아한다.'), ('She wants to dance.', '그녀는 춤추고 싶어 한다.')]: D.sent(en, ko)
D.step(TF('끊어 보기 연습', [
    ("'I went to the library / to read books.'에서 to 앞까지만 읽어도 문장이 끝나므로 to read는 '읽기 위해'로 해석한다.", True,
     "정답 ▶ T\n이유: '나는 도서관에 갔다.'로 끝나요 → to read books는 '책을 읽기 위해'(부사적)"),
    ("'I want / to read books.'에서 I want만으로 문장이 끝나므로 '읽기 위해'로 해석한다.", False,
     "정답 ▶ F\n이유: '나는 원한다…' 뭘 원해? → 끝나지 않아요. to read books가 want의 내용(목적어) → '책 읽는 것을 원한다'(명사적)"),
    ("'To learn English is fun.'의 To learn English는 '영어를 배우는 것은'으로 해석한다.", True,
     "정답 ▶ T\n이유: 문장 맨 앞(주어 자리) → '~하는 것은'"),
    ("'He hopes to visit Paris.'는 '그는 파리를 방문하기 위해 바란다.'로 해석한다.", False,
     "정답 ▶ F\n이유: '바란다' 뭘? → to visit Paris(파리를 방문하기를). 바른 해석: 그는 파리를 방문하기를 바란다."),
]))
D.step(SCR(D, '우리말 → 영어 배열', [('I like to dance.', '나는 춤추는 것을 좋아한다.'), ('To read books is fun.', '책을 읽는 것은 재미있다.'),
                                      ('I want to be a teacher.', '나는 선생님이 되고 싶다.')]))
DAYS.append(D.done())

# ═════════ DAY 3 · 주어·보어 역할 ═════════
D = Day('t3', '주어·보어 역할', "문장 맨 앞 '~하는 것은'(주어) · be동사 뒤 '~하는 것이다'(보어)")
D.note('개념 ① 주어 역할 = "~하는 것은"', [
    ('자리', '문장 맨 앞 (동사 앞)'),
    ('To learn English is fun.', '영어를 배우는 것은 재미있다.'),
    ('주어 덩어리 찾기', '동사(is) 앞까지가 한 덩어리 → To learn English'),
    ('동사는 단수', 'to부정사 주어는 하나로 보고 is·was를 써요. (To learn English are ✗)'),
])
D.note('개념 ② 보어 역할 = "~하는 것이다"', [
    ('자리', 'be동사(is·am·are·was) 뒤'),
    ('My dream is to be a singer.', '내 꿈은 가수가 되는 것이다. (My dream = to be a singer)'),
    ('보어 확인법', 'be동사 앞뒤가 "="인지 확인 → 내 꿈 = 가수가 되는 것'),
])
D.note('개념 ③ 주어와 보어 구별', [
    ('be동사 앞(맨 앞)', '주어 · "~하는 것은"'),
    ('be동사 뒤', '보어 · "~하는 것이다"'),
])
D.step(cards('해석 카드', [
    ('To swim is fun.', '수영하는 것은 재미있다.'), ('To learn English is fun.', '영어를 배우는 것은 재미있다.'),
    ('To get up early is hard.', '일찍 일어나는 것은 어렵다.'), ('To help others is important.', '다른 사람을 돕는 것은 중요하다.'),
    ('My dream is to be a singer.', '내 꿈은 가수가 되는 것이다.'), ('His job is to teach English.', '그의 직업은 영어를 가르치는 것이다.'),
    ('My hobby is to draw pictures.', '내 취미는 그림을 그리는 것이다.')], guide='문장을 읽고 알맞은 해석을 골라요. 맨 앞 to부정사는 "~하는 것은", is 뒤 to부정사는 "~하는 것이다"예요.'))
D.step(MC('역할 고르기 (주어 · 보어)', [
    role(D, 'To play soccer is exciting.', 'To play soccer', '축구를 하는 것은 신난다.', 0, '문장 맨 앞, 동사 is 앞 → 주어 "~하는 것은"'),
    role(D, 'My hobby is to draw pictures.', 'to draw pictures', '내 취미는 그림을 그리는 것이다.', 2, 'be동사 is 뒤 → 보어 "~하는 것이다" (내 취미 = 그림 그리는 것)'),
    role(D, 'To get up early is hard.', 'To get up early', '일찍 일어나는 것은 어렵다.', 0, '문장 맨 앞, is 앞 → 주어'),
    role(D, 'Her dream is to become a scientist.', 'to become a scientist', '그녀의 꿈은 과학자가 되는 것이다.', 2, 'is 뒤 → 보어 (그녀의 꿈 = 과학자가 되는 것)'),
    role(D, 'To learn a new language is not easy.', 'To learn a new language', '새로운 언어를 배우는 것은 쉽지 않다.', 0, '맨 앞, is 앞 → 주어'),
    role(D, 'The plan is to meet at the station.', 'to meet at the station', '계획은 역에서 만나는 것이다.', 2, 'is 뒤 → 보어 (계획 = 역에서 만나는 것)'),
    role(D, 'To help others is important.', 'To help others', '다른 사람을 돕는 것은 중요하다.', 0, '맨 앞, is 앞 → 주어'),
    role(D, 'My goal is to read 30 books this year.', 'to read 30 books this year', '내 목표는 올해 책 30권을 읽는 것이다.', 2, 'is 뒤 → 보어 (내 목표 = 책 30권 읽는 것)'),
], '밑줄 친 to부정사가 문장에서 어떤 역할인지 고르세요.'))
D.step(MC('해석 고르기', [
    tr('To get up early is hard.', '일찍 일어나는 것은 어렵다.', ['일찍 일어나기 위해 어렵다.', '일찍 일어나는 것이다.', '나는 일찍 일어나서 힘들었다.'], '맨 앞 To get up early = "일찍 일어나는 것은" (주어)'),
    tr('His job is to teach English.', '그의 직업은 영어를 가르치는 것이다.', ['그는 영어를 가르치기 위해 일한다.', '그의 직업은 영어를 배우는 것이다.', '그는 영어를 가르쳤다.'], 'is 뒤 to teach English = "영어를 가르치는 것이다" (보어)'),
]))
D.step(PICK(D, '어법 선택', [
    ('To learn English {is|are} fun.', '영어를 배우는 것은 재미있다.', '정답 ▶ is\n이유: to부정사 주어는 단수 취급 → is\n포인트 ▶ English가 하나라서가 아니라, "~하는 것" 한 덩어리라서 단수'),
    ('To make new friends {is|are} not difficult.', '새 친구를 사귀는 것은 어렵지 않다.', '정답 ▶ is\n이유: 주어는 To make new friends(새 친구를 사귀는 것) 한 덩어리 → 단수 is\n오답 ▶ friends(복수)에 속지 마세요!'),
    ('{To swim|Swim} in the sea is fun.', '바다에서 수영하는 것은 재미있다.', '정답 ▶ To swim\n이유: 주어 자리에 "~하는 것은"이 와야 하니 to부정사 To swim. 동사원형 Swim은 주어가 될 수 없어요.'),
    ('My dream is {to be|be} a writer.', '내 꿈은 작가가 되는 것이다.', '정답 ▶ to be\n이유: is 뒤 보어 자리 "~하는 것이다" → to be\n오답 ▶ is be처럼 동사 두 개를 나란히 쓸 수 없어요.'),
    ('His job is {to fix|fixes} cars.', '그의 직업은 자동차를 고치는 것이다.', '정답 ▶ to fix\n이유: is 뒤 보어 → to fix (고치는 것이다)\n오답 ▶ is fixes는 동사가 두 개라 틀려요.'),
]))
D.step(VERB(D, 'to부정사로 쓰기', [
    ('___ in the river is dangerous.', 'swim', ['To swim'], '강에서 수영하는 것은 위험하다.', '정답 ▶ To swim\n이유: 문장 맨 앞 주어 자리 → To swim (수영하는 것은)'),
    ('My wish is ___ a puppy.', 'have', ['to have'], '내 소원은 강아지를 갖는 것이다.', '정답 ▶ to have\n이유: is 뒤 보어 자리 → to have (갖는 것이다)'),
    ('___ healthy food is good for you.', 'eat', ['To eat'], '건강한 음식을 먹는 것은 너에게 좋다.', '정답 ▶ To eat\n이유: 맨 앞 주어 자리 → To eat (먹는 것은)'),
    ('Her job is ___ children.', 'teach', ['to teach'], '그녀의 직업은 아이들을 가르치는 것이다.', '정답 ▶ to teach\n이유: is 뒤 보어 → to teach (가르치는 것이다)'),
], '( ) 안의 동사를 to부정사로 바꿔 쓰세요. (맨 앞이면 대문자 To도 정답)', 'to + 동사원형으로 쓰기'))
D.step(SCR(D, '우리말 → 영어 배열', [('To swim is fun.', '수영하는 것은 재미있다.'), ('My dream is to be a singer.', '내 꿈은 가수가 되는 것이다.')]))
DAYS.append(D.done())

# ═════════ DAY 4 · 목적어 역할 · 주목보 구별 ═════════
D = Day('t4', '목적어 역할 · 주·목·보 구별', "일반동사 뒤 '~하는 것을'(목적어) · 세 가지 역할 한 번에 가려내기")
D.note('개념 ① 목적어 역할 = "~하는 것을"', [
    ('자리', '일반동사(like, want, love, decide …) 바로 뒤'),
    ('I like to dance.', '나는 춤추는 것을 좋아한다.'),
    ('She wants to go home.', '그녀는 집에 가는 것을 원한다 → 집에 가고 싶어 한다.'),
])
D.note('개념 ② 주·목·보 3단계 구별법', [
    ('1단계', 'to부정사가 문장 맨 앞(동사 앞)? → 주어 "~하는 것은"'),
    ('2단계', 'be동사(is·am·are·was) 바로 뒤? → 보어 "~하는 것이다"'),
    ('3단계', '일반동사(like, want …) 바로 뒤? → 목적어 "~하는 것을"'),
])
D.step(cards('해석 카드', [
    ('I like to dance.', '나는 춤추는 것을 좋아한다.'), ('She wants to go home.', '그녀는 집에 가고 싶어 한다.'),
    ('We decided to go camping.', '우리는 캠핑을 가기로 결심했다.'), ('I love to sing songs.', '나는 노래 부르는 것을 아주 좋아한다.'),
    ('He started to cry.', '그는 울기 시작했다.'), ('To ride a bike is fun.', '자전거를 타는 것은 재미있다.'),
    ('My dream is to be a chef.', '내 꿈은 요리사가 되는 것이다.')], guide='문장을 읽고 알맞은 해석을 골라요. like·want 뒤의 to부정사는 "~하는 것을"로 해석해요.'))
D.step(MC('역할 고르기 (주어 · 목적어 · 보어)', [
    role(D, 'I love to sing songs.', 'to sing songs', '나는 노래 부르는 것을 아주 좋아한다.', 1, '일반동사 love 바로 뒤 → 목적어 "~하는 것을"'),
    role(D, 'To ride a bike is fun.', 'To ride a bike', '자전거를 타는 것은 재미있다.', 0, '문장 맨 앞 → 주어 "~하는 것은"'),
    role(D, 'My dream is to be a chef.', 'to be a chef', '내 꿈은 요리사가 되는 것이다.', 2, 'be동사 is 뒤 → 보어 "~하는 것이다"'),
    role(D, 'We decided to go camping.', 'to go camping', '우리는 캠핑을 가기로 결심했다.', 1, '일반동사 decided 바로 뒤 → 목적어 (가기로 결심했다)'),
    role(D, 'Her job is to take care of animals.', 'to take care of animals', '그녀의 일은 동물을 돌보는 것이다.', 2, 'is 뒤 → 보어'),
    role(D, 'To eat breakfast is important.', 'To eat breakfast', '아침을 먹는 것은 중요하다.', 0, '맨 앞 → 주어'),
    role(D, 'They want to watch a movie.', 'to watch a movie', '그들은 영화를 보고 싶어 한다.', 1, '일반동사 want 바로 뒤 → 목적어 (보는 것을 원한다)'),
    role(D, 'The best way is to practice every day.', 'to practice every day', '가장 좋은 방법은 매일 연습하는 것이다.', 2, 'is 뒤 → 보어'),
    role(D, 'To be kind to others is good.', 'To be kind to others', '다른 사람에게 친절한 것은 좋다.', 0, '맨 앞 → 주어\n포인트 ▶ others 앞의 to는 전치사(다른 사람에게)'),
    role(D, 'He started to cry.', 'to cry', '그는 울기 시작했다.', 1, '일반동사 started 바로 뒤 → 목적어 (우는 것을 시작했다 = 울기 시작했다)'),
], '3단계 구별법(맨 앞 → 주어 / be동사 뒤 → 보어 / 일반동사 뒤 → 목적어)으로 고르세요.'))
for en, ko in [('To swim in the sea is exciting.', '바다에서 수영하는 것은 신난다.'), ('I want to read books.', '나는 책을 읽고 싶다.'), ('My dream is to read 100 books.', '내 꿈은 책 100권을 읽는 것이다.'),
               ('She likes to read.', '그녀는 읽는 것을 좋아한다.'), ('He hopes to travel to Canada.', '그는 캐나다를 여행하기를 바란다.'), ('To travel is fun.', '여행하는 것은 재미있다.'),
               ('Her wish is to travel to Canada.', '그녀의 소원은 캐나다를 여행하는 것이다.'), ('My plan is to travel.', '내 계획은 여행하는 것이다.'), ('My job is to help people.', '내 일은 사람들을 돕는 것이다.'),
               ('I like to help people.', '나는 사람들을 돕는 것을 좋아한다.'), ('To help people is good.', '사람들을 돕는 것은 좋다.'), ('His dream is to be an actor.', '그의 꿈은 배우가 되는 것이다.'),
               ('To read books is fun.', '책을 읽는 것은 재미있다.')]: D.sent(en, ko)
D.step(MC('쓰임(역할)이 같은 것 고르기', [
    ('밑줄 친 부분과 역할이 <b>같은</b> 것은?' + Q('To read books is fun.', 'To read books'), [U('To swim in the sea is exciting.', 'To swim in the sea'), U('I want to read books.', 'to read books'), U('My dream is to read 100 books.', 'to read 100 books'), U('She likes to read.', 'to read')],
     '정답 ▶ To swim in the sea is exciting.\n이유: 둘 다 문장 맨 앞 → 주어 "~하는 것은"\n오답 ▶ want/likes 뒤(목적어) · is 뒤(보어)'),
    ('밑줄 친 부분과 역할이 <b>같은</b> 것은?' + Q('He hopes to travel to Canada.', 'to travel'), [U('My plan is to travel.', 'to travel') if False else U('She likes to read.', 'to read'), U('To travel is fun.', 'To travel'), U('Her wish is to travel to Canada.', 'to travel to Canada'), U('My plan is to travel.', 'to travel')],
     '정답 ▶ She likes to read.\n이유: 둘 다 일반동사(hopes, likes) 바로 뒤 → 목적어 "~하는 것을"\n오답 ▶ To travel(맨 앞 → 주어) / is 뒤 to travel(보어)'),
    ('밑줄 친 부분과 역할이 <b>같은</b> 것은?' + Q('My job is to help people.', 'to help people'), [U('His dream is to be an actor.', 'to be an actor'), U('I like to help people.', 'to help people'), U('To help people is good.', 'To help people'), U('I want to read books.', 'to read books')],
     '정답 ▶ His dream is to be an actor.\n이유: 둘 다 be동사 is 뒤 → 보어 "~하는 것이다"\n오답 ▶ like/want 뒤(목적어) · 맨 앞(주어)'),
]))
D.step(TF('역할 확인 T/F', [
    ("'I like to dance.'의 to dance는 like의 목적어이다.", True, '정답 ▶ T\n이유: 일반동사 like 바로 뒤 → 목적어 "춤추는 것을"'),
    ("'My dream is to be a pilot.'의 to be a pilot은 주어이다.", False, '정답 ▶ F\n이유: be동사 is 뒤 → 보어 "조종사가 되는 것이다". 주어는 My dream'),
    ("'To swim is fun.'의 To swim은 보어이다.", False, '정답 ▶ F\n이유: 문장 맨 앞(is 앞) → 주어 "수영하는 것은"'),
]))
D.step(PICK(D, '어법 선택', [
    ('I want {to go|go} home.', '나는 집에 가고 싶다.', '정답 ▶ to go\n이유: want의 목적어 자리 → to go\n오답 ▶ want go처럼 동사 두 개를 바로 붙일 수 없어요.'),
    ('We decided {to stay|stayed} at home.', '우리는 집에 머물기로 결심했다.', '정답 ▶ to stay\n이유: decided의 목적어 → to stay (머물기로)\n오답 ▶ decided stayed는 동사가 두 개'),
    ('She loves {to bake|bakes} cookies.', '그녀는 쿠키 굽는 것을 아주 좋아한다.', '정답 ▶ to bake\n이유: loves의 목적어 → to bake (굽는 것을)'),
]))
D.step(SCR(D, '우리말 → 영어 배열', [('I love to sing songs.', '나는 노래 부르는 것을 아주 좋아한다.'), ('We decided to go camping.', '우리는 캠핑을 가기로 결심했다.')]))
DAYS.append(D.done())

# ═════════ DAY 5 · to부정사를 목적어로 쓰는 동사 ═════════
D = Day('t5', 'to부정사를 목적어로 쓰는 동사', 'want · hope · plan · decide · promise · refuse · agree … + to부정사 / 부정은 not to')
D.note('개념 ① 기억법: to부정사 = "앞으로 할 일"', [
    ('to부정사를 목적어로 쓰는 동사', '원하고, 바라고, 계획하고, 결심하고, 약속하는 것은 모두 "앞으로 할 일"이에요 → to부정사와 짝꿍'),
    ('want / would like', '원하다 / ~하고 싶다 (would like to = want to의 공손한 말)'),
    ('hope / wish / expect', '바라다 / 소망하다 / 기대하다·예상하다'),
    ('plan / decide / choose', '계획하다 / 결정하다·결심하다 / 선택하다'),
    ('promise / agree / refuse', '약속하다 / 동의하다 / 거절하다'),
    ('need / learn', '~할 필요가 있다 / ~하는 것을 배우다'),
    ('afford / pretend', '~할 여유가 있다 / ~인 척하다'),
])
D.note('개념 ② to부정사의 부정 = not to + 동사원형', [
    ('I promised not to make a mess.', '나는 어지르지 않겠다고 약속했다. (not은 to 앞에!)'),
    ('We decided not to go to Paris.', '우리는 파리에 가지 않기로 결정했다.'),
])
D.step(cards('동사 카드', [
    ('want to ~', '~하고 싶다 (원하다)'), ('would like to ~', '~하고 싶다 (공손)'), ('hope to ~', '~하기를 바라다'), ('wish to ~', '~하기를 소망하다'),
    ('expect to ~', '~할 것을 기대하다'), ('plan to ~', '~할 계획이다'), ('decide to ~', '~하기로 결정하다'), ('choose to ~', '~하기로 선택하다'),
    ('promise to ~', '~하겠다고 약속하다'), ('agree to ~', '~하기로 동의하다'), ('refuse to ~', '~하기를 거절하다'), ('need to ~', '~할 필요가 있다'),
    ('learn to ~', '~하는 것을 배우다'), ('afford to ~', '~할 여유가 있다'), ('pretend to ~', '~인 척하다'), ('not to + 동사원형', 'to부정사의 부정 (~하지 않기로)')], 12))
D.step(TF('동사 확인 T/F', [
    ('refuse(거절하다)는 목적어로 to부정사를 쓴다.', True, '정답 ▶ T\n이유: refuse to ~ = ~하기를 거절하다 (Carol refused to go out.)'),
    ('"~하지 않기로 결정했다"는 decided to not go보다 decided not to go가 교과서식 표현이다.', True, '정답 ▶ T\n이유: to부정사의 부정은 not을 to 앞에 → not to + 동사원형'),
    ('would like 뒤에는 동명사(-ing)를 쓴다.', False, '정답 ▶ F\n이유: would like to ~ = ~하고 싶다 (Would you like to have something to eat?)'),
    ('"앞으로 할 일"을 원하거나 계획하는 동사는 to부정사와 잘 어울린다.', True, '정답 ▶ T\n이유: want, hope, plan, decide, promise는 모두 미래의 일 → to부정사'),
]))
D.step(PICK(D, '어법 선택 (워크북 Part 1 유형)', [
    ("I don't want {to work|working} when I'm 65.", '나는 65세가 되면 일하고 싶지 않다.', '정답 ▶ to work\n이유: want + to부정사 (부정문이어도 마찬가지)'),
    ('They promised {to pick|picking} us up from the airport.', '그들은 공항에서 우리를 태워 주겠다고 약속했다.', '정답 ▶ to pick\n이유: promise + to부정사'),
    ('She decided {to buy|buying} new clothes.', '그녀는 새 옷을 사기로 결심했다.', '정답 ▶ to buy\n이유: decide + to부정사'),
    ('Would you like {to have|having} something to eat?', '뭐 좀 먹을래요?', '정답 ▶ to have\n이유: would like + to부정사 = ~하고 싶다'),
    ('Mike wants {to have|having} a brother.', 'Mike는 남동생이 있기를 원한다.', '정답 ▶ to have\n이유: want + to부정사'),
    ('Carol refused {to go|going} out with her classmate.', 'Carol은 반 친구와 외출하는 것을 거절했다.', '정답 ▶ to go\n이유: refuse + to부정사'),
    ('She chose {to stay|staying} at home.', '그녀는 집에 있기로 선택했다.', '정답 ▶ to stay\n이유: choose + to부정사'),
    ('She agreed {to be|being} there at 5 p.m.', '그녀는 오후 5시에 그곳에 오기로 동의했다.', '정답 ▶ to be\n이유: agree + to부정사'),
    ('Where did Jake learn {to speak|speaking} French?', 'Jake는 어디에서 프랑스어 하는 것을 배웠니?', '정답 ▶ to speak\n이유: learn + to부정사 (~하는 법을 배우다)'),
    ('The car is too expensive, so I can\'t afford {to buy|buying} it.', '그 차는 너무 비싸서 나는 그것을 살 여유가 없다.', '정답 ▶ to buy\n이유: afford + to부정사 (~할 여유가 있다)'),
    ('He often pretends {to be|being} rich.', '그는 종종 부자인 척한다.', '정답 ▶ to be\n이유: pretend + to부정사 (~인 척하다)'),
]))
D.step(MC('알맞은 동사 · 부정 표현', [
    ('빈칸에 들어갈 수 <b>없는</b> 것은?' + Q('Joe ______ to learn Chinese.'), ['enjoys', 'chooses', 'wants', 'decides'],
     '정답 ▶ enjoys\n이유: 빈칸 뒤 to learn(to부정사) → enjoy는 동명사(-ing)만 써서 못 와요.\n오답 ▶ choose/want/decide + to부정사 ✔'),
    ('우리말과 같도록 바르게 쓴 것은?' + Q('그는 다시는 거짓말을 하지 않겠다고 약속했다.'), ['He promised not to lie again.', 'He promised to lie not again.', 'He promised don\'t lie again.', 'He not promised to lie again.'],
     '정답 ▶ He promised not to lie again.\n이유: to부정사의 부정 = not to + 동사원형\n오답 ▶ He not promised는 "약속하지 않았다"가 되어 뜻이 달라져요(게다가 틀린 어순).'),
]))
D.sent('He promised not to lie again.', '그는 다시는 거짓말을 하지 않겠다고 약속했다.')
D.step(VERB(D, '알맞은 형태로 쓰기 (워크북 Part 3 유형)', [
    ('He wants ___ a doctor.', 'become', ['to become'], '그는 의사가 되고 싶어 한다.', '정답 ▶ to become\n이유: want + to부정사'),
    ('Joe hopes ___ his math exam.', 'pass', ['to pass'], 'Joe는 수학 시험에 통과하기를 바란다.', '정답 ▶ to pass\n이유: hope + to부정사'),
    ('We need ___ a new toaster.', 'buy', ['to buy'], '우리는 새 토스터를 살 필요가 있다.', '정답 ▶ to buy\n이유: need + to부정사'),
    ("I'd like ___ chocolate ice cream.", 'eat', ['to eat'], '나는 초콜릿 아이스크림을 먹고 싶다.', "정답 ▶ to eat\n이유: I'd like = I would like + to부정사"),
    ('I promised ___ a mess in my room.', 'not, make', ['not to make'], '나는 내 방을 어지르지 않겠다고 약속했다.', '정답 ▶ not to make\n이유: to부정사의 부정 → not to + 동사원형'),
    ('We decided ___ to Paris this summer.', 'not, go', ['not to go'], '우리는 이번 여름에 파리에 가지 않기로 결정했다.', '정답 ▶ not to go\n이유: decide + not to + 동사원형'),
], '( ) 안의 말을 이용해 알맞은 형태로 쓰세요.', 'to부정사로 쓰기'))
D.step(SCR(D, '단어 배열 (워크북 Part 5 유형)', [('She promised to call me this evening.', '그녀는 오늘 저녁에 내게 전화하기로 약속했다.'), ("I don't want to waste my money.", '나는 내 돈을 낭비하고 싶지 않다.')]))
DAYS.append(D.done())

# ═════════ DAY 6 · 동명사(-ing)만 쓰는 동사 · 둘 다 쓰는 동사 ═════════
D = Day('t6', '-ing만 쓰는 동사 · 둘 다 쓰는 동사', 'enjoy · finish · mind · avoid · give up · keep · suggest … + -ing / like · love · start · begin은 둘 다')
D.note('개념 ① 동명사(-ing)만 목적어로 쓰는 동사', [
    ('기억법 MEGAFEPS', 'Mind 꺼리다 · Enjoy 즐기다 · Give up 포기하다 · Avoid 피하다 · Finish 끝내다 · Escape 피하다 · Practice 연습하다 · Stop 그만두다 / Suggest 제안하다'),
    ('그 밖에', 'keep 계속하다 · admit 인정하다 · deny 부인하다 · imagine 상상하다 · dislike 싫어하다 · feel like ~하고 싶다'),
    ('느낌', '동명사는 "이미 하고 있거나 해 본 일"과 잘 어울려요. (즐기고, 끝내고, 그만두고, 계속하는 것)'),
    ('enjoy to dance ✗', 'enjoy dancing ✔ / finish to do ✗ → finish doing ✔'),
])
D.note('개념 ② 둘 다 쓰는 동사 · 조심할 동사', [
    ('like · love · hate · start · begin', 'to부정사와 동명사 둘 다 OK, 뜻도 거의 같아요. (I like to walk. = I like walking.)'),
    ('stop -ing', '~하는 것을 그만두다 (She stopped writing. 쓰는 것을 멈췄다)'),
    ('stop to ~', '~하기 위해 멈추다 (뜻이 달라져요! 이건 부사적 용법)'),
    ('feel like -ing vs would like to', '둘 다 "~하고 싶다"지만 feel like 다음은 -ing, would like 다음은 to부정사'),
])
D.step(cards('동사 카드', [
    ('mind -ing', '~하는 것을 꺼리다'), ('enjoy -ing', '~하는 것을 즐기다'), ('give up -ing', '~하는 것을 포기하다'), ('avoid -ing', '~하는 것을 피하다'),
    ('finish -ing', '~하는 것을 끝내다'), ('practice -ing', '~하는 것을 연습하다'), ('stop -ing', '~하는 것을 그만두다'), ('suggest -ing', '~하자고 제안하다'),
    ('keep -ing', '계속 ~하다'), ('admit -ing', '~한 것을 인정하다'), ('imagine -ing', '~하는 것을 상상하다'), ('feel like -ing', '~하고 싶다'),
    ('like · love · start · begin', 'to부정사·-ing 둘 다 OK')], 12))
D.step(TF('동사 확인 T/F', [
    ('enjoy to shop은 바른 표현이다.', False, '정답 ▶ F\n이유: enjoy + 동명사 → enjoy shopping'),
    ('keep은 목적어로 동명사(-ing)를 쓴다.', True, '정답 ▶ T\n이유: keep -ing = 계속 ~하다 (The girls keep talking.)'),
    ('like는 to부정사와 동명사를 모두 목적어로 쓸 수 있다.', True, '정답 ▶ T\n이유: I like to walk. = I like walking.'),
    ('She stopped to write.는 "그녀는 쓰는 것을 그만두었다."라는 뜻이다.', False, '정답 ▶ F\n이유: stop to ~는 "~하기 위해 멈추다". "쓰는 것을 그만두었다"는 She stopped writing.'),
    ('feel like 다음에는 to부정사를 쓴다.', False, '정답 ▶ F\n이유: feel like + -ing (I don\'t feel like going out.) ↔ would like + to부정사'),
]))
D.step(PICK(D, '어법 선택 (워크북 Part 1 유형)', [
    ('Do you enjoy {shopping|to shop} for new things?', '너는 새로운 물건 쇼핑하는 것을 즐기니?', '정답 ▶ shopping\n이유: enjoy + 동명사(-ing)'),
    ("I didn't feel like {going|to go} out last night, so I stayed at home.", '나는 어젯밤 외출하고 싶지 않아서 집에 있었다.', '정답 ▶ going\n이유: feel like + 동명사 (like가 전치사라서 뒤에 -ing)'),
    ('The girls keep {talking|to talk} during lessons.', '그 여자아이들은 수업 중에 계속 떠든다.', '정답 ▶ talking\n이유: keep + 동명사 = 계속 ~하다'),
    ('They avoid {making|to make} mistakes.', '그들은 실수하는 것을 피한다.', '정답 ▶ making\n이유: avoid + 동명사'),
    ('She stopped {writing|to write} a letter because she was too tired.', '그녀는 너무 피곤해서 편지 쓰는 것을 그만두었다.', '정답 ▶ writing\n이유: 너무 피곤해서 → 쓰는 것을 그만두다 = stop + 동명사\n포인트 ▶ stopped to write는 "쓰기 위해 멈췄다"라 뜻이 맞지 않아요.'),
    ('Can you imagine {being|to be} alone all your life?', '평생 혼자인 것을 상상할 수 있니?', '정답 ▶ being\n이유: imagine + 동명사'),
    ('Ted admitted {making|to make} a serious mistake.', 'Ted는 심각한 실수를 한 것을 인정했다.', '정답 ▶ making\n이유: admit + 동명사'),
    ('Do you mind {helping|to help} Ann with her homework?', 'Ann의 숙제를 도와주는 것을 꺼리니? (도와줄 수 있니?)', '정답 ▶ helping\n이유: mind + 동명사'),
    ('My dad gave up {eating|to eat} fast food.', '우리 아빠는 패스트푸드 먹는 것을 포기했다(끊었다).', '정답 ▶ eating\n이유: give up + 동명사'),
]))
D.step(MC('둘 다 쓰는 동사 찾기', [
    ('두 빈칸에 <b>공통으로</b> 들어갈 수 있는 동사는?' + Q('I ______ to read comic books. / I ______ reading comic books.'), ['like', 'want', 'enjoy', 'finish'],
     '정답 ▶ like\n이유: like는 to부정사·동명사 둘 다 OK → like to read = like reading\n오답 ▶ want(to부정사만) / enjoy·finish(-ing만)'),
    ('빈칸에 들어갈 말로 알맞지 <b>않은</b> 것은?' + Q('It started ______ heavily.'), ['rained', 'to rain', 'raining'],
     '정답 ▶ rained\n이유: start는 to부정사(to rain)와 동명사(raining) 둘 다 OK, 하지만 과거형 rained는 목적어가 될 수 없어요.'),
]))
D.step(VERB(D, '알맞은 형태로 쓰기', [
    ('I enjoy ___ a lot.', 'dance', ['dancing'], '나는 춤추는 것을 무척 즐긴다.', '정답 ▶ dancing\n이유: enjoy + 동명사'),
    ('They suggested ___ the train.', 'take', ['taking'], '그들은 기차를 타자고 제안했다.', '정답 ▶ taking\n이유: suggest + 동명사'),
    ('Do you like ___ pictures?', 'draw', ['drawing', 'to draw'], '너는 그림 그리는 것을 좋아하니?', '정답 ▶ drawing / to draw\n이유: like는 둘 다 OK'),
    ('Ricky enjoyed ___ science fiction.', 'read', ['reading'], 'Ricky는 공상 과학 소설 읽는 것을 즐겼다.', '정답 ▶ reading\n이유: enjoy + 동명사'),
    ('Tom suggested ___ for a walk together.', 'go', ['going'], 'Tom은 함께 산책하러 가자고 제안했다.', '정답 ▶ going\n이유: suggest + 동명사'),
    ('Climbing up the mountain is difficult, but we kept ___.', 'go', ['going'], '산을 오르는 것은 힘들지만, 우리는 계속 갔다.', '정답 ▶ going\n이유: keep + 동명사 = 계속 ~하다'),
], '동사에 따라 동명사(-ing) 또는 to부정사로 쓰세요. (둘 다 되면 아무거나)', '-ing 또는 to부정사로 쓰기'))
DAYS.append(D.done())

# ═════════ DAY 7 · 워크북 연습 ① 동사 보고 고르기·쓰기 ═════════
D = Day('t7', '워크북 연습 ① 동사 보고 고르기·쓰기', 'Grammar Build Up Part 1·2·3·4 유형 · 동사를 먼저 보고 to부정사인지 -ing인지')
D.note('푸는 순서 (이것만 기억!)', [
    ('1단계', '빈칸 앞의 동사에 동그라미 → 그 동사가 어느 팀인지 떠올리기'),
    ('to부정사 팀', 'want · would like · hope · wish · expect · plan · decide · choose · promise · agree · refuse · need · learn · afford · pretend'),
    ('-ing 팀', 'mind · enjoy · give up · avoid · finish · practice · stop · suggest · keep · admit · deny · imagine · dislike · feel like'),
    ('둘 다 팀', 'like · love · hate · start · begin'),
    ('2단계', 'to 다음에는 동사원형! not은 to 앞에 (not to go)'),
])
def three(en, opts, ans, ko, why):
    D.sent(en.replace('______', ans), ko)
    return ('빈칸에 알맞은 것은?' + Q(en), [ans] + [o for o in opts if o != ans], '정답 ▶ %s\n이유: %s\n해석 ▶ %s' % (ans, why, ko))
D.step(MC('세 개 중 고르기 (Part 1 유형)', [
    three('Would you like ______ around next Saturday?', ['come', 'to come', 'coming'], 'to come', '다음 주 토요일에 놀러 올래?', 'would like + to부정사'),
    three('Patrick promised ______ back before midnight.', ['to be', 'being', 'be'], 'to be', 'Patrick은 자정 전에 돌아오겠다고 약속했다.', 'promise + to부정사'),
    three('Dan suggested ______ a movie after dinner.', ['watch', 'to watch', 'watching'], 'watching', 'Dan은 저녁 식사 후에 영화를 보자고 제안했다.', 'suggest + 동명사'),
    ('빈칸에 들어갈 수 있는 것을 <b>모두</b> 고른 것은?' + Q('I like ______ early in the morning.'), ['to walk, walking 둘 다', 'to walk만', 'walking만', '둘 다 안 됨'],
     '정답 ▶ to walk, walking 둘 다\n이유: like는 to부정사·동명사 둘 다 OK\n해석 ▶ 나는 아침 일찍 걷는 것을 좋아한다.'),
]))
D.sent('I like to walk early in the morning.', '나는 아침 일찍 걷는 것을 좋아한다.')
D.step(PICK(D, '알맞은 동사 고르기 (Part 2 유형)', [
    ('Joe {chooses|enjoys} to learn Chinese.', 'Joe는 중국어를 배우기로 선택한다.', '정답 ▶ chooses\n이유: 뒤에 to learn(to부정사) → choose 팀. enjoy는 -ing 팀'),
    ('Caroline really {enjoys|refuses} climbing mountains.', 'Caroline은 등산하는 것을 정말 즐긴다.', '정답 ▶ enjoys\n이유: 뒤에 climbing(-ing) → enjoy 팀. refuse는 to부정사 팀'),
    ('Do you {mind|want} helping Ann with her homework?', 'Ann의 숙제를 도와줄 수 있니?', '정답 ▶ mind\n이유: 뒤에 helping(-ing) → mind 팀. want는 to부정사 팀'),
    ('Jeremy {promised|felt like} to phone me before 10 p.m.', 'Jeremy는 밤 10시 전에 나에게 전화하겠다고 약속했다.', '정답 ▶ promised\n이유: 뒤에 to phone(to부정사) → promise 팀. feel like는 -ing 팀'),
    ('Susan {keeps|wants} talking about her problems.', 'Susan은 계속 자기 문제에 대해 이야기한다.', '정답 ▶ keeps\n이유: 뒤에 talking(-ing) → keep 팀. want는 to부정사 팀'),
]))
D.step(VERB(D, '보기의 동사로 쓰기 (Part 4 유형)', [
    ('My sister refused ___ me with my project.', 'help', ['to help'], '내 여동생은 내 과제를 도와주기를 거절했다.', '정답 ▶ to help\n이유: refuse + to부정사'),
    ('Your aunt wished ___ Australia in summer.', 'visit', ['to visit'], '너의 이모는 여름에 호주를 방문하기를 소망했다.', '정답 ▶ to visit\n이유: wish + to부정사'),
    ('Please avoid ___ the wires with wet hands.', 'touch', ['touching'], '젖은 손으로 전선을 만지는 것을 피하세요.', '정답 ▶ touching\n이유: avoid + 동명사'),
    ('All my friends want ___ to the zoo.', 'go', ['to go'], '내 친구들은 모두 동물원에 가고 싶어 한다.', '정답 ▶ to go\n이유: want + to부정사'),
    ('My neighbor enjoys ___ stamps and coins.', 'collect', ['collecting'], '우리 이웃은 우표와 동전을 모으는 것을 즐긴다.', '정답 ▶ collecting\n이유: enjoy + 동명사'),
    ('Excuse me, do you mind ___ the table?', 'clean', ['cleaning'], '실례지만, 테이블을 치워 주시겠어요?', '정답 ▶ cleaning\n이유: mind + 동명사'),
    ("George's father learned ___ the guitar in five years.", 'play', ['to play'], 'George의 아버지는 5년 만에 기타 치는 법을 배웠다.', '정답 ▶ to play\n이유: learn + to부정사'),
    ('You hate ___ for your girlfriend.', 'wait', ['waiting', 'to wait'], '너는 여자 친구를 기다리는 것을 싫어한다.', '정답 ▶ waiting / to wait\n이유: hate는 둘 다 OK'),
    ("I'd like ___ to the Moon soon.", 'fly', ['to fly'], '나는 곧 달에 날아가고 싶다.', "정답 ▶ to fly\n이유: would like + to부정사"),
    ("Anne's plan is ___ in the park on Sunday.", 'take a walk', ['to take a walk', 'taking a walk'], 'Anne의 계획은 일요일에 공원에서 산책하는 것이다.', '정답 ▶ to take a walk / taking a walk\n이유: is 뒤 보어 "~하는 것이다" → to부정사·동명사 둘 다 OK'),
], '( ) 안의 동사를 알맞은 형태로 쓰세요. (둘 다 되면 아무거나)', 'to부정사 또는 -ing로 쓰기'))
DAYS.append(D.done())

# ═════════ DAY 8 · 워크북 연습 ② 주어·목적어·보어 · 배열 ═════════
D = Day('t8', '워크북 연습 ② S·O·C · 배열', 'Grammar Build Up Part 5·6·7 유형 · 주어(S)·목적어(O)·보어(C) 가려내기와 영작 배열')
D.note('S·O·C 가려내는 법', [
    ('S (주어)', 'to부정사가 문장 맨 앞 → "~하는 것은" (To swim is relaxing.)'),
    ('O (목적어)', '일반동사(want, try, began, started …) 바로 뒤 → "~하는 것을"'),
    ('C (보어)', 'be동사(is, was) 바로 뒤 → "~하는 것이다" (The easiest way is to take a taxi.)'),
    ('not to', 'I hoped not to see you again. → hoped 뒤 → O (부정이어도 역할은 같아요)'),
])
SOC = ['S (주어)', 'O (목적어)', 'C (보어)']
def soc(en, u, ko, ans, why):
    D.sent(en, ko)
    return ('밑줄 친 to부정사의 역할은? (S / O / C)' + Q(en, u), [SOC[ans]] + [x for i, x in enumerate(SOC) if i != ans], '정답 ▶ %s\n이유: %s\n해석 ▶ %s' % (SOC[ans], why, ko))
D.step(MC('S · O · C 고르기 (Part 6 유형)', [
    soc('I want to cook this cake for my birthday.', 'to cook', '나는 내 생일을 위해 이 케이크를 요리하고 싶다.', 1, '일반동사 want 바로 뒤 → O'),
    soc('To swim is really relaxing.', 'To swim', '수영하는 것은 정말 마음을 편하게 해 준다.', 0, '문장 맨 앞 → S'),
    soc('To fly a helicopter is very difficult.', 'To fly a helicopter', '헬리콥터를 조종하는 것은 매우 어렵다.', 0, '맨 앞 → S'),
    soc('I try to memorize three expressions every day.', 'to memorize', '나는 매일 세 개의 표현을 외우려고 노력한다.', 1, '일반동사 try 바로 뒤 → O'),
    soc('The easiest way is to take a taxi.', 'to take a taxi', '가장 쉬운 방법은 택시를 타는 것이다.', 2, 'be동사 is 뒤 → C (가장 쉬운 방법 = 택시를 타는 것)'),
    soc('People began to eat bread around 10,000 years ago.', 'to eat bread', '사람들은 약 1만 년 전에 빵을 먹기 시작했다.', 1, '일반동사 began 바로 뒤 → O'),
    soc('My job is to translate English into Korean.', 'to translate', '내 일은 영어를 한국어로 번역하는 것이다.', 2, 'is 뒤 → C'),
    soc('To ride a motorcycle without a helmet is dangerous.', 'To ride a motorcycle without a helmet', '헬멧 없이 오토바이를 타는 것은 위험하다.', 0, '맨 앞 → S (is 앞까지가 주어 덩어리)'),
    soc('My wish is to live in a beautiful house on the hill.', 'to live', '내 소원은 언덕 위의 아름다운 집에서 사는 것이다.', 2, 'is 뒤 → C'),
    soc('To work in the garden was a pleasure.', 'To work in the garden', '정원에서 일하는 것은 즐거움이었다.', 0, '맨 앞, was 앞 → S'),
    soc('Amy thought about her wish and started to write.', 'to write', 'Amy는 자신의 소원에 대해 생각했고 쓰기 시작했다.', 1, '일반동사 started 바로 뒤 → O'),
    soc('I hoped not to see you again.', 'not to see', '나는 너를 다시 보지 않기를 바랐다.', 1, '일반동사 hoped 바로 뒤 → O (not to도 역할은 같아요)'),
], 'S(주어) · O(목적어) · C(보어) 중 하나를 고르세요.'))
D.step(SCR(D, '우리말 → 영어 배열 (Part 5·7 유형)', [
    ('I want to be good at English.', '나는 영어를 잘하고 싶어.'),
    ('Judy likes to play the guitar in the living room.', 'Judy는 거실에서 기타를 연주하는 것을 좋아한다.'),
    ('My plan is to learn Spanish.', '나의 계획은 스페인어를 배우는 것이다.'),
    ('I want to be a painter like him.', '나는 그와 같은 화가가 되고 싶어.'),
    ('I decided to overcome my limitations.', '저는 저의 한계를 극복하기로 결심했습니다.'),
    ('My hobby is to collect stamps.', '내 취미는 우표를 모으는 것이야.'),
    ('He promised not to lie again.', '그는 다시는 거짓말을 하지 않겠다고 약속했다.'),
    ('This year, we plan to visit nursing homes in our town.', '올해, 우리는 우리 마을에 있는 양로원들을 방문할 계획입니다.'),
]))
DAYS.append(D.done())

# ═════════ DAY 6 · 종합 연습 (내신형) ═════════
D = Day('t9', '종합 연습 (내신형)', '해석 · 역할 · 동사 · 어법 · 오류찾기를 섞어서')
D.note('한눈에 정리', [
    ('to부정사', 'to + 동사원형'), ('명사적 용법', '"~하는 것, ~하기"'),
    ('주어', '문장 맨 앞 · "~하는 것은" · 동사는 단수(is)'), ('목적어', '일반동사 바로 뒤 · "~하는 것을"'), ('보어', 'be동사 뒤 · "~하는 것이다"'),
    ('to부정사를 목적어로', 'want · would like · hope · wish · expect · plan · decide · choose · promise · agree · refuse · need · learn'), ('-ing만', 'mind · enjoy · give up · avoid · finish · practice · stop · suggest · keep'),
    ('~하기 위해', '부사적 용법(목적) · to 앞에서 끊어도 문장이 끝남'),
])
D.step(MC('해석 고르기', [
    tr('To keep a diary is a good habit.', '일기를 쓰는 것은 좋은 습관이다.', ['일기를 쓰기 위해 좋은 습관이다.', '나는 매일 일기를 썼다.', '좋은 습관은 일기를 쓰는 것이다.'], '맨 앞 To keep a diary = "일기를 쓰는 것은" (주어)\n오답 ▶ 4번은 주어와 보어를 바꾼 해석이에요.'),
    tr('My wish is to fly in the sky.', '내 소원은 하늘을 나는 것이다.', ['나는 하늘을 날기 위해 소원을 빈다.', '내 소원은 하늘에 있다.', '나는 하늘을 날았다.'], 'is 뒤 to fly = "나는 것이다" (보어)'),
    tr('He woke up early to watch the sunrise.', '그는 해돋이를 보기 위해 일찍 일어났다.', ['그는 해돋이를 보는 것을 일찍 일어났다.', '그는 해돋이를 보고 싶었다.', '그는 늦게 일어나서 해돋이를 못 봤다.'],
       "끊어 보기 → He woke up early / to watch… '그는 일찍 일어났다.'로 끝나요 → '보기 위해' (부사적 · 목적)"),
]))
D.step(MC('역할 고르기', [
    role(D, 'I need to buy a new phone.', 'to buy a new phone', '나는 새 휴대폰을 살 필요가 있다.', 1, '일반동사 need 바로 뒤 → 목적어'),
    role(D, 'To win the race is my goal.', 'To win the race', '경주에서 이기는 것이 내 목표이다.', 0, '맨 앞 → 주어'),
    role(D, 'The important thing is to do your best.', 'to do your best', '중요한 것은 최선을 다하는 것이다.', 2, 'is 뒤 → 보어'),
    role(D, 'She hopes to see the Northern Lights.', 'to see the Northern Lights', '그녀는 오로라를 보기를 바란다.', 1, '일반동사 hopes 바로 뒤 → 목적어'),
]))
for en, ko in [('To swim is fun.', '수영하는 것은 재미있다.'), ('My dream is to be a pilot.', '내 꿈은 조종사가 되는 것이다.'), ('She likes to cook.', '그녀는 요리하는 것을 좋아한다.'),
               ('I went to the park to run.', '나는 달리기 위해 공원에 갔다.')]: D.sent(en, ko)
D.step(MC('쓰임이 다른 것 고르기', [
    ('밑줄 친 to부정사의 쓰임이 나머지와 <b>다른</b> 것은?', [U('I went to the park to run.', 'to run'), U('To swim is fun.', 'To swim'), U('My dream is to be a pilot.', 'to be'), U('She likes to cook.', 'to cook')],
     "정답 ▶ I went to the park to run.\n이유: '나는 공원에 갔다.'로 끝나고 to run은 '달리기 위해'(부사적 · 목적)\n오답 ▶ 나머지는 모두 '~하는 것'(명사적): 주어 / 보어 / 목적어"),
]))
D.step(PICK(D, '어법 선택', [
    ('To learn new things {is|are} exciting.', '새로운 것을 배우는 것은 신난다.', '정답 ▶ is\n이유: to부정사 주어는 단수 취급 (things에 속지 않기!)'),
    ('I want {to visit|visiting} Paris someday.', '나는 언젠가 파리를 방문하고 싶다.', '정답 ▶ to visit\n이유: want + to부정사'),
    ('He finished {cleaning|to clean} his room.', '그는 방 청소를 끝냈다.', '정답 ▶ cleaning\n이유: finish + 동명사(-ing)만'),
    ('Her dream is {to become|becomes} a pianist.', '그녀의 꿈은 피아니스트가 되는 것이다.', '정답 ▶ to become\n이유: is 뒤 보어 → to become'),
]))
D.step(ERR(D, '오류 찾기', [
    ('[[To learn]] English [[are]] [[fun]].', 1, 'is', '영어를 배우는 것은 재미있다.', '틀린 곳 ▶ ② are → is\n이유: to부정사 주어(To learn English)는 단수 취급\n나머지 ▶ ① To learn ✔ ③ fun ✔'),
    ('She [[wants]] [[to buys]] a new [[bag]].', 1, 'to buy', '그녀는 새 가방을 사고 싶어 한다.', '틀린 곳 ▶ ② to buys → to buy\n이유: to + 동사원형\n나머지 ▶ ① wants(주어 She → -s) ✔ ③ bag ✔'),
    ('I [[enjoy]] [[to swim]] in the [[pool]].', 1, 'swimming', '나는 수영장에서 수영하는 것을 즐긴다.', '틀린 곳 ▶ ② to swim → swimming\n이유: enjoy는 동명사(-ing)만\n나머지 ▶ ① enjoy ✔ ③ pool ✔'),
    ('My dream [[is]] [[become]] a [[doctor]].', 1, 'to become', '내 꿈은 의사가 되는 것이다.', '틀린 곳 ▶ ② become → to become\n이유: is 뒤 보어 "~하는 것이다" → to become (is become ✗)\n나머지 ▶ ① is ✔ ③ doctor ✔'),
]))
D.step(VERB(D, '알맞은 형태로 쓰기', [
    ('___ a foreign language is not easy.', 'learn', ['To learn'], '외국어를 배우는 것은 쉽지 않다.', '정답 ▶ To learn\n이유: 맨 앞 주어 → To learn'),
    ('We plan ___ a party.', 'have', ['to have'], '우리는 파티를 열 계획이다.', '정답 ▶ to have\n이유: plan + to부정사'),
    ('My hobby is ___ old coins.', 'collect', ['to collect'], '내 취미는 옛날 동전을 모으는 것이다.', '정답 ▶ to collect\n이유: is 뒤 보어 → to collect'),
    ('She enjoys ___ in the park.', 'walk', ['walking'], '그녀는 공원에서 걷는 것을 즐긴다.', '정답 ▶ walking\n이유: enjoy + 동명사(-ing)만'),
], '( ) 안의 동사를 알맞은 형태로 쓰세요. (맨 앞이면 대문자 To도 정답)', 'to부정사 또는 -ing로 쓰기'))
D.step(SCR(D, '우리말 → 영어 배열', [('To keep a diary is a good habit.', '일기를 쓰는 것은 좋은 습관이다.'), ('She hopes to see the Northern Lights.', '그녀는 오로라를 보기를 바란다.'),
                                      ('We plan to have a party.', '우리는 파티를 열 계획이다.')]))
DAYS.append(D.done())

# ═════════ DAY 7 · 교과서 문장으로 연습 ═════════
D = Day('t10', '우리 교과서 문장으로 연습', '동아(윤정미) · 천재(소영순) 교과서 본문과 대화 속 to부정사')
D.note('교과서 속 to부정사 찾기', [
    ('명사적 (~하는 것)', '동사(want, decide, love, like, start, forget …) 뒤 · is 뒤'),
    ('부사적 (~하기 위해)', 'to 앞에서 끊어도 문장이 끝나는 것'),
    ('조심!', 'be going to(~할 예정이다), thanks to(~ 덕분에)는 to부정사 문제로 나오지 않아요.'),
])
TB = [  # (en, ko, 출처, 밑줄, 용법: n=명사적/a=부사적, 역할)
    ('Do you want to save the Earth?', '여러분은 지구를 구하고 싶나요?', '동아 6과', 'to save the Earth', 'n', 1),
    ('So, I decided to fix it and reuse it.', '그래서 나는 그것을 수선해서 재사용하기로 결심했어.', '동아 6과', 'to fix it', 'n', 1),
    ('I want to be a sports reporter.', '나는 스포츠 기자가 되고 싶어.', '동아 7과', 'to be a sports reporter', 'n', 1),
    ('Yes, I love to make clothes.', '응, 나는 옷 만드는 것을 매우 좋아해.', '동아 7과', 'to make clothes', 'n', 1),
    ("I'm a location manager, and my job is to find perfect places for shooting.", '나는 야외 촬영 관리자이고, 내 일은 촬영을 위한 완벽한 장소를 찾는 거예요.', '동아 7과', 'to find perfect places', 'n', 2),
    ('I like to travel and enjoy challenges.', '나는 여행하는 것을 좋아하고 도전을 즐겨요.', '동아 7과', 'to travel', 'n', 1),
    ('Look. Somebody forgot to turn off the water.', '봐. 누군가 물을 잠그는 걸 깜빡했네.', '동아 6과', 'to turn off the water', 'n', 1),
    ('I want to become an app designer.', '저는 앱 디자이너가 되고 싶어요.', '천재 6과', 'to become an app designer', 'n', 1),
    ('Do you want to protect trees and animals in the forest?', '여러분은 숲속의 나무와 동물을 보호하고 싶나요?', '천재 6과', 'to protect trees and animals', 'n', 1),
    ('Some people love to work in nature.', '어떤 사람들은 자연에서 일하는 것을 아주 좋아한다.', '천재 6과', 'to work in nature', 'n', 1),
    ('A lot of people are working hard to create this movie.', '많은 사람들이 이 영화를 만들기 위해 열심히 일하고 있어요.', '동아 7과', 'to create this movie', 'a', None),
    ('So, I use hand signals to calm him.', '그래서, 나는 그를 진정시키기 위해 수신호를 사용해요.', '동아 7과', 'to calm him', 'a', None),
    ('I wear a diving suit and swimming glasses to work in the water.', '저는 물속에서 일하기 위해 잠수복을 입고 수경을 씁니다.', '천재 6과', 'to work in the water', 'a', None),
    ('Also, I often climb the mountain to look after wild animals like bears.', '또한 저는 곰과 같은 야생 동물을 돌보기 위해 자주 산을 오릅니다.', '천재 6과', 'to look after wild animals', 'a', None),
]
for en, ko, *_ in TB: D.sent(en, ko)
ROLEW = {1: '일반동사 바로 뒤 → 목적어 "~하는 것을"', 2: 'be동사 is 뒤 → 보어 "~하는 것이다"'}
items = []
for en, ko, src, u, k, r in TB:
    if k == 'n':
        items.append(('[%s] 밑줄 친 to부정사의 해석으로 알맞은 것은?' % src + Q(en, u), ["'~하는 것(~하기)'으로 해석 (명사적)", "'~하기 위해'로 해석 (부사적)"],
                      "정답 ▶ '~하는 것(~하기)'으로 해석 (명사적)\n이유: %s\n해석 ▶ %s" % (ROLEW[r], ko)))
    else:
        cut = en.split(' ' + u.split()[0] + ' ' + u.split()[1])[0]
        items.append(('[%s] 밑줄 친 to부정사의 해석으로 알맞은 것은?' % src + Q(en, u), ["'~하기 위해'로 해석 (부사적)", "'~하는 것(~하기)'으로 해석 (명사적)"],
                      "정답 ▶ '~하기 위해'로 해석 (부사적)\n이유: 끊어 보기 → '%s'까지만 읽어도 문장이 끝나요. to부정사가 '왜?'(목적)에 답해요.\n해석 ▶ %s" % (cut, ko)))
D.step(MC("교과서 문장 · '~하는 것' vs '~하기 위해'", items, "to 앞에서 끊어 보세요. 앞부분만으로 문장이 끝나면 '~하기 위해'예요."))
D.step(MC('교과서 문장 · 역할 고르기', [
    role(D, "I'm a location manager, and my job is to find perfect places for shooting.", 'to find perfect places for shooting', '나는 야외 촬영 관리자이고, 내 일은 촬영을 위한 완벽한 장소를 찾는 거예요.', 2, '[동아 7과] be동사 is 뒤 → 보어 (내 일 = 완벽한 장소를 찾는 것)'),
    role(D, 'So, I decided to fix it and reuse it.', 'to fix it', '그래서 나는 그것을 수선해서 재사용하기로 결심했어.', 1, '[동아 6과] 일반동사 decided 바로 뒤 → 목적어 (수선하기로 결심했다)'),
    role(D, 'Some people love to work in nature.', 'to work in nature', '어떤 사람들은 자연에서 일하는 것을 아주 좋아한다.', 1, '[천재 6과] 일반동사 love 바로 뒤 → 목적어'),
]))
D.step(PICK(D, '교과서 문장 · 어법 선택', [
    ('I want to {become|became} an app designer.', '저는 앱 디자이너가 되고 싶어요.', '정답 ▶ become\n이유: [천재 6과] to + 동사원형'),
    ('So, I decided {to fix|fixing} it and reuse it.', '그래서 나는 그것을 수선해서 재사용하기로 결심했어.', '정답 ▶ to fix\n이유: [동아 6과] decide + to부정사'),
    ('I like to travel and {enjoy|enjoying} challenges.', '나는 여행하는 것을 좋아하고 도전을 즐겨요.', '정답 ▶ enjoy\n이유: [동아 7과] and로 이어진 말은 형태를 맞춰요. "여행하는 것을 좋아하고 도전을 즐겨요" → enjoy(동사원형)\n포인트 ▶ and 뒤에는 동사원형 enjoy ("도전을 즐겨요"). enjoying은 올 수 없어요.'),
]))
D.step(SCR(D, '교과서 문장 배열', [('I want to be a sports reporter.', '나는 스포츠 기자가 되고 싶어.'), ('Some people love to work in nature.', '어떤 사람들은 자연에서 일하는 것을 아주 좋아한다.')]))
DAYS.append(D.done())

for i, d in enumerate(DAYS): d['name'] = 'DAY %d' % (i + 1)
for d in DAYS: ansfirst(d['steps'])
PK = {'id': 'm1-grammar-to1', 'school': '중1 동아(윤정미)·중1 천재(소영순)', 'unit': '공통 문법 · to부정사 ①', 'title': 'to부정사 ① 명사적 용법',
      'titleKo': '~하는 것 · 주어 · 목적어 · 보어', 'exam': '2학기 기말고사', 'prose': True, 'pick': True, 'teacherPhone': '', 'days': DAYS}
write(PK, '/home/claude/proj/data/m1-grammar-to1.js', "/* 중1 공통 문법 · to부정사 ① 명사적 용법 (10/29, scratchpad/gen_m1to.py)\n   동아(윤정미)·천재(소영순) 학생 모두 열림(school 문자열에 두 교재 이름). 본문 탭 = 개념 노트 + 예문 */\n")
print('ok', [(d['id'], d['range'], len(d['steps'])) for d in DAYS])
