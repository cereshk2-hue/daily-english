import sys, re
sys.path.insert(0, '/home/claude/work/gen')
from gencommon import write
from dlgcommon import ansfirst
# 중1 동아(윤정미) 6과 문법 · 접속사 that (11/1). 보드에서 to부정사 ① 명사적 용법 바로 아래.
# 근거: Grammar Build Up 객관식 6과 Pattern 2 (접속사 that) 유형 · 교과서 6과 본문 문장. DAY 고르기(pick)

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

def cards(title, items, n=None, guide='카드를 한 번 읽고, 퀴즈에서 짝이 맞는 것을 고르세요.'): return {'type': 'vocab', 'title': title, 'guide': guide, 'quizN': n or len(items), 'items': [list(x) for x in items]}
def SCARDS(D, title, items, n=None, guide=''):
    for en, ko in items: D.sent(en, re.sub(r' \([^)]*\)$', '', ko))
    return cards(title, items, n, guide)
def TF(title, items, guide='맞으면 T, 틀리면 F를 고르세요.'): return {'type': 'tf', 'title': title, 'guide': guide, 'items': [[a, b, c, None, None] for a, b, c in items]}
def MC(title, items, guide='알맞은 답을 고르세요.'):
    return {'type': 'mc', 'title': title, 'guide': guide, 'items': [dict({'q': it[0], 'opts': it[1], 'ex': it[2]}, **({'sort': True} if len(it) > 3 and it[3] else {})) for it in items]}
def PICK(D, title, items, guide='어법상 알맞은 것을 고르세요.'):
    for s, ko, x in items: D.sent(re.sub(r'\{([^|}]*)\|[^}]*\}', r'\1', s), ko)
    return {'type': 'pick', 'title': title, 'guide': guide, 'items': [{'s': s, 'ex': x} for s, ko, x in items]}
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
CIR = '①②③④⑤'
def OL(lines): return '<br>' + '<br>'.join(lines)

ROLE = ['접속사 that (~라고, ~라는 것)', '지시대명사 that (저것, 그것)', '지시형용사 that (저 ~, 그 ~)']
def role(D, en, ko, ans, why, u='that'):
    D.sent(en, ko)
    opts = [ROLE[ans]] + [r for i, r in enumerate(ROLE) if i != ans]
    return ('밑줄 친 <i>that</i>의 쓰임은?' + Q(en, u), opts, '정답 ▶ %s\n이유: %s\n해석 ▶ %s' % (ROLE[ans], why, ko))

DAYS = []

# ═════════ DAY 1 · 접속사 that이 뭐예요? ═════════
D = Day('c1', '접속사 that이 뭐예요?', '문장과 문장을 잇는 that · "~라고 생각하다"로 해석하기')
D.note('개념 ① 접속사 = 잇는 말', [
    ('접속사', '단어와 단어, 문장과 문장을 이어 주는 말이에요. and, but, that, when 등'),
    ('I think. + He is kind.', '두 문장을 that으로 이으면 → I think that he is kind.'),
    ('I think that he is kind.', '나는 그가 친절하다고 생각한다.'),
])
D.note('개념 ② that 뒤에는 "주어 + 동사"', [
    ('think / believe / know / hope / hear / say + that + 주어 + 동사', 'that 뒤에 문장(주어 + 동사)이 통째로 와서, 앞 동사의 목적어가 돼요.'),
    ('해석', '"주어가 ~하다고 / ~라는 것을" + 생각하다 · 믿다 · 알다 · 바라다 · 듣다 · 말하다'),
    ('I know that she is busy.', '나는 그녀가 바쁘다는 것을 안다.'),
    ('I hope that you like it.', '나는 네가 그것을 좋아하기를 바란다.'),
])
D.step(SCARDS(D, '해석 카드', [
    ('I think that he is kind.', '나는 그가 친절하다고 생각한다.'), ('I believe that you can do it.', '나는 네가 그것을 할 수 있다고 믿는다.'),
    ('I know that she is busy.', '나는 그녀가 바쁘다는 것을 안다.'), ('I hope that you like the gift.', '나는 네가 그 선물을 좋아하기를 바란다.'),
    ('I heard that Tom is sick.', '나는 Tom이 아프다고 들었다.'), ('She says that the movie is fun.', '그녀는 그 영화가 재미있다고 말한다.'),
    ('We think that English is easy.', '우리는 영어가 쉽다고 생각한다.'), ('He knows that I like soccer.', '그는 내가 축구를 좋아한다는 것을 안다.')],
    guide='문장을 읽고 알맞은 해석을 골라요. that 뒤 문장은 "~라고, ~라는 것을"로 해석해요.'))
D.step(TF('개념 확인 T/F', [
    ('접속사 that은 문장과 문장을 이어 준다.', True, '정답 ▶ T\n이유: I think. + He is kind. → I think that he is kind. that이 두 문장을 이어 줘요.'),
    ('접속사 that 뒤에는 주어와 동사가 온다.', True, '정답 ▶ T\n이유: that 뒤에 문장(주어 + 동사)이 와요. I know that she(주어) is(동사) busy.'),
    ('I hope that go to Canada.는 바른 문장이다.', False, '정답 ▶ F\n이유: that 뒤에 주어가 없어요. → I hope that I go to Canada. 처럼 주어가 꼭 있어야 해요.\n포인트 ▶ that + 주어 + 동사'),
    ('I think that he is kind.는 "나는 그가 친절하다고 생각한다."로 해석한다.', True, '정답 ▶ T\n이유: that절(he is kind)을 "~라고"로 해석해 think(생각하다) 앞에 붙여요.'),
    ('접속사 that은 "저것"이라는 뜻이다.', False, '정답 ▶ F\n이유: 접속사 that은 뜻이 따로 없이 문장을 이어 줘요. "저것, 그것"은 지시대명사 that이에요. (DAY 4에서 자세히)'),
    ('I know that she is busy.에서 that절은 know의 목적어이다.', True, '정답 ▶ T\n이유: 무엇을 아니? → 그녀가 바쁘다는 것을. that절이 동사 know의 목적어 역할을 해요.'),
]))
D.step(MC('해석 고르기', [
    ('알맞은 해석은?' + Q('I believe that Mr. Kim is a good teacher.'), ['나는 김 선생님이 좋은 선생님이라고 믿는다.', '나는 좋은 선생님인 김 선생님을 믿는다.', '김 선생님은 내가 좋은 선생님이라고 믿는다.', '나는 김 선생님이 좋은 선생님이 되기를 바란다.'],
     '정답 ▶ 나는 김 선생님이 좋은 선생님이라고 믿는다.\n이유: I believe(나는 믿는다) + that Mr. Kim is a good teacher(김 선생님이 좋은 선생님이라고)\n오답 ▶ 믿는 사람은 I(나) / "되기를 바란다"는 hope'),
    ('알맞은 해석은?' + Q('She knows that I like pizza.'), ['그녀는 내가 피자를 좋아한다는 것을 안다.', '나는 그녀가 피자를 좋아한다는 것을 안다.', '그녀는 피자를 좋아하는 나를 안다.', '그녀는 내가 피자를 좋아하기를 바란다.'],
     '정답 ▶ 그녀는 내가 피자를 좋아한다는 것을 안다.\n이유: She knows(그녀는 안다) + that I like pizza(내가 피자를 좋아한다는 것을)\n오답 ▶ 피자를 좋아하는 사람은 I(나), 아는 사람은 She(그녀)'),
    ('알맞은 해석은?' + Q('We hope that you get well soon.'), ['우리는 네가 곧 낫기를 바란다.', '우리는 네가 곧 나았다고 생각한다.', '너는 우리가 곧 낫기를 바란다.', '우리는 곧 나아서 기쁘다.'],
     '정답 ▶ 우리는 네가 곧 낫기를 바란다.\n이유: hope that ~ = ~이기를 바라다. get well = (병이) 낫다'),
    ('알맞은 해석은?' + Q('I heard that the store is closed today.'), ['나는 그 가게가 오늘 문을 닫는다고 들었다.', '나는 오늘 문을 닫은 그 가게에 갔다.', '그 가게는 내가 오늘 들었다고 말했다.', '나는 그 가게가 오늘 문을 열기를 바란다.'],
     '정답 ▶ 나는 그 가게가 오늘 문을 닫는다고 들었다.\n이유: heard that ~ = ~라고 들었다. closed = 문을 닫은'),
    ('우리말과 뜻이 같은 것은?<br><b>나는 그 책이 재미있다고 생각한다.</b>', ['I think that the book is fun.', 'I think the fun book.', 'The book thinks that I am fun.', 'I think that is a fun book.'],
     '정답 ▶ I think that the book is fun.\n이유: 나는 생각한다(I think) + 그 책이 재미있다고(that the book is fun)\n오답 ▶ I think that is a fun book.은 "나는 저것이 재미있는 책이라고 생각한다"(that = 저것)'),
]))
D.step(PICK(D, 'that 뒤에는 주어 + 동사', [
    ('I hope that {we|go} win the game.', '나는 우리가 그 경기에 이기기를 바란다.', '정답 ▶ we\n이유: that 뒤에는 주어 + 동사 → that we(주어) win(동사)'),
    ('I think that {she is|is} very smart.', '나는 그녀가 매우 똑똑하다고 생각한다.', '정답 ▶ she is\n이유: that 뒤에 주어가 꼭 있어야 해요 → that she is ~'),
    ('He knows that {I|me} like music.', '그는 내가 음악을 좋아한다는 것을 안다.', '정답 ▶ I\n이유: that절의 주어 자리 → 주격 I (me는 목적격이라 주어가 될 수 없어요)'),
    ('We believe that {he|him} is honest.', '우리는 그가 정직하다고 믿는다.', '정답 ▶ he\n이유: that절의 주어 자리 → 주격 he'),
    ('I heard that {Mina|to Mina} is sick.', '나는 미나가 아프다고 들었다.', '정답 ▶ Mina\n이유: that + 주어(Mina) + 동사(is)'),
    ('She thinks that {the movie is|the movie} boring.', '그녀는 그 영화가 지루하다고 생각한다.', '정답 ▶ the movie is\n이유: that절에도 동사가 있어야 해요 → the movie(주어) is(동사) boring'),
]))
D.step(SCR(D, '우리말 → 영어 배열', [
    ('I think that he is kind.', '나는 그가 친절하다고 생각한다.'),
    ('I know that she is busy.', '나는 그녀가 바쁘다는 것을 안다.'),
    ('I hope that you like the gift.', '나는 네가 그 선물을 좋아하기를 바란다.'),
    ('We believe that he is honest.', '우리는 그가 정직하다고 믿는다.'),
]))
DAYS.append(D.done())

# ═════════ DAY 2 · that이 들어갈 자리 · 생략 ═════════
D = Day('c2', 'that이 들어갈 자리 · 생략', '동사 바로 뒤, 두 번째 문장 앞 · 목적어 that은 생략 가능')
D.note('개념 ① that이 들어갈 자리', [
    ('찾는 법', '① 주어 + 동사(think, know, hope …)를 찾고 ② 그 뒤에 또 다른 "주어 + 동사"가 시작되는 곳 → 그 앞에 that'),
    ('Jack showed / the new game was interesting.', '→ Jack showed that the new game was interesting. (showed 뒤, the new game 앞)'),
    ('I hope / you have a great time.', '→ I hope that you have a great time.'),
])
D.note('개념 ② 목적어 that은 생략할 수 있어요', [
    ('I think (that) he is kind.', 'that이 없어도 뜻은 같아요. 말할 때는 생략을 더 많이 해요.'),
    ('I guess (that) it\'s all right.', '교과서 6과 본문 · 그래도 괜찮은 것 같아.'),
    ('생략된 that 찾기', 'think, know, hope, guess … 바로 뒤에 "주어 + 동사"가 오면 그 사이에 that이 숨어 있어요.'),
])
D.step(MC('that이 들어갈 곳', [
    ('that이 들어갈 알맞은 곳은?<br><b>Jack ⓐ showed ⓑ the new ⓒ game ⓓ was ⓔ interesting.</b>', ['ⓑ', 'ⓐ', 'ⓒ', 'ⓓ', 'ⓔ'],
     '정답 ▶ ⓑ\n이유: Jack(주어) showed(동사) 뒤에 새 문장 the new game(주어) was(동사)가 시작 → showed that the new game was interesting\n해석 ▶ Jack은 그 새 게임이 재미있다는 것을 보여 주었다.', True),
    ('that이 들어갈 알맞은 곳은?<br><b>I ⓐ hope ⓑ you ⓒ have ⓓ a great ⓔ time.</b>', ['ⓑ', 'ⓐ', 'ⓒ', 'ⓓ', 'ⓔ'],
     '정답 ▶ ⓑ\n이유: I hope 뒤, you(주어) have(동사) 앞 → I hope that you have a great time.\n해석 ▶ 나는 네가 좋은 시간을 보내기를 바란다.', True),
    ('that이 들어갈 알맞은 곳은?<br><b>ⓐ My mom ⓑ knows ⓒ I ⓓ like ⓔ cats.</b>', ['ⓒ', 'ⓐ', 'ⓑ', 'ⓓ', 'ⓔ'],
     '정답 ▶ ⓒ\n이유: My mom(주어) knows(동사) 뒤, I(주어) like(동사) 앞 → My mom knows that I like cats.\n해석 ▶ 엄마는 내가 고양이를 좋아한다는 것을 아신다.', True),
    ('that이 들어갈 알맞은 곳은?<br><b>We ⓐ believe ⓑ our ⓒ team ⓓ will ⓔ win.</b>', ['ⓑ', 'ⓐ', 'ⓒ', 'ⓓ', 'ⓔ'],
     '정답 ▶ ⓑ\n이유: We believe 뒤, our team(주어) will win(동사) 앞 → We believe that our team will win.\n포인트 ▶ our team은 두 단어지만 한 덩어리 주어 → 그 앞에 that\n해석 ▶ 우리는 우리 팀이 이길 거라고 믿는다.', True),
    ('that이 들어갈 알맞은 곳은?<br><b>I ⓐ heard ⓑ plastic ⓒ never ⓓ goes ⓔ away completely.</b>', ['ⓑ', 'ⓐ', 'ⓒ', 'ⓓ', 'ⓔ'],
     '정답 ▶ ⓑ\n이유: 교과서 6과 본문 문장. I heard 뒤, plastic(주어) never goes away(동사) 앞 → I heard that plastic never goes away completely.\n해석 ▶ 나는 플라스틱이 절대로 완전히 없어지지 않는다고 들었다.', True),
]))
D.sent('Jack showed that the new game was interesting.', 'Jack은 그 새 게임이 재미있다는 것을 보여 주었다.')
D.sent('I hope that you have a great time.', '나는 네가 좋은 시간을 보내기를 바란다.')
D.sent('My mom knows that I like cats.', '엄마는 내가 고양이를 좋아한다는 것을 아신다.')
D.sent('We believe that our team will win.', '우리는 우리 팀이 이길 거라고 믿는다.')
D.sent('I heard that plastic never goes away completely.', '나는 플라스틱이 절대로 완전히 없어지지 않는다고 들었다.')
D.step(TF('that이 숨어 있을까? T/F', [
    ('I guess it\'s all right.에는 guess와 it 사이에 that이 생략되어 있다.', True, '정답 ▶ T\n이유: guess(동사) 뒤에 it(주어) is(동사)가 바로 와요 → I guess (that) it\'s all right.\n해석 ▶ 그래도 괜찮은 것 같아.'),
    ('I think she is right.는 that이 없으므로 틀린 문장이다.', False, '정답 ▶ F\n이유: 목적어 자리의 that은 생략할 수 있어요. I think (that) she is right. 둘 다 맞아요.'),
    ('I know you like music.은 "나는 네가 음악을 좋아한다는 것을 안다."로 해석한다.', True, '정답 ▶ T\n이유: know 뒤에 that이 생략 → I know (that) you like music.'),
    ('I hope she gets well soon.에서 that을 생략하면 뜻이 바뀐다.', False, '정답 ▶ F\n이유: that이 있든 없든 뜻은 같아요. "나는 그녀가 곧 낫기를 바란다."'),
    ('I like that song.에는 like와 that 사이에 접속사 that이 생략되어 있다.', False, '정답 ▶ F\n이유: that 뒤가 song(명사) 하나뿐이에요. 주어 + 동사가 없으니 접속사가 아니라 "그 노래"의 that(지시형용사)이에요.'),
    ('He said he was tired.에는 said와 he 사이에 that이 생략되어 있다.', True, '정답 ▶ T\n이유: said(동사) 뒤에 he(주어) was(동사) → He said (that) he was tired.\n해석 ▶ 그는 피곤하다고 말했다.'),
]))
D.sent("I guess it's all right.", '그래도 괜찮은 것 같아.'); D.sent('I know you like music.', '나는 네가 음악을 좋아한다는 것을 안다.'); D.sent('He said he was tired.', '그는 피곤하다고 말했다.')
D.step(MC('that을 생략할 수 있는 것', [
    ('밑줄 친 that을 생략할 수 있는 것은?', [U('I knew that he was right.', 'that'), U('That person is my sister.', 'That'), U('Look at that tall building.', 'that'), U('That is my bike.', 'That')],
     '정답 ▶ I knew that he was right.\n이유: knew 뒤에서 he was right(주어 + 동사)를 이끄는 목적어 접속사 that → 생략 가능\n오답 ▶ That person(저 사람) · that tall building(저 높은 건물) · That is(저것은)의 that은 "저 ~, 저것"이라는 뜻이 있어서 빼면 문장이 이상해져요.'),
    ('밑줄 친 that을 생략할 수 있는 것은?', [U('We hope that you enjoy the trip.', 'that'), U('Who is that girl?', 'that'), U('I want that red cap.', 'that'), U('Do you know that?', 'that')],
     '정답 ▶ We hope that you enjoy the trip.\n이유: hope 뒤 목적어 that절의 접속사 → 생략 가능 (We hope you enjoy the trip.)\n오답 ▶ that girl(저 여자아이) · that red cap(저 빨간 모자) · know that(그것을 알아?)의 that은 뜻이 있어서 생략하면 안 돼요.'),
    ('that이 생략된 문장은?', ['I think you are right.', 'I like this book.', 'She wants to be a nurse.', 'He goes to school by bus.'],
     '정답 ▶ I think you are right.\n이유: think 뒤에 you(주어) are(동사)가 바로 와요 → I think (that) you are right.\n오답 ▶ 나머지는 뒤에 "주어 + 동사"로 된 문장이 따로 없어요.'),
]))
D.sent('I knew that he was right.', '나는 그가 옳다는 것을 알았다.'); D.sent('We hope that you enjoy the trip.', '우리는 네가 여행을 즐기기를 바란다.'); D.sent('I think you are right.', '나는 네가 옳다고 생각한다.')
D.step(SCR(D, 'that 넣어 배열', [
    ('Jack showed that the new game was interesting.', 'Jack은 그 새 게임이 재미있다는 것을 보여 주었다.'),
    ('My mom knows that I like cats.', '엄마는 내가 고양이를 좋아한다는 것을 아신다.'),
    ('We believe that our team will win.', '우리는 우리 팀이 이길 거라고 믿는다.'),
    ('I heard that plastic never goes away completely.', '나는 플라스틱이 절대로 완전히 없어지지 않는다고 들었다.'),
]))
DAYS.append(D.done())

# ═════════ DAY 3 · that과 잘 쓰는 동사 · 어법 ═════════
D = Day('c3', 'that과 잘 쓰는 동사 · 어법', 'think · believe · know · hope · hear · say · guess · remember / 수 일치 · 시제 · don\'t think')
D.note('개념 ① that절을 목적어로 쓰는 동사', [
    ('think that ~', '~라고 생각하다'), ('believe that ~', '~라고 믿다'), ('know that ~', '~라는 것을 알다'),
    ('hope that ~', '~이기를 바라다'), ('hear that ~', '~라고 듣다'), ('say that ~', '~라고 말하다'),
    ('guess that ~', '~라고 짐작하다, ~인 것 같다'), ('remember that ~', '~라는 것을 기억하다'),
    ('want · decide는 ✗', 'want, decide 뒤에는 that절 대신 to부정사를 써요. (I want to go. ✔ / I want that I go. ✗)'),
])
D.note('개념 ② 어법 체크', [
    ('앞 문장 동사', '주어가 3인칭 단수(he, she, Tom)면 -s: She says that ~ / He thinks that ~'),
    ('don\'t / doesn\'t 뒤', '동사원형: I don\'t think ~ (don\'t thought ✗) / She doesn\'t think ~ (doesn\'t thinks ✗)'),
    ('that절 안의 동사', 'that절의 주어에 맞춰요: that something was wrong (were ✗) / that he is kind'),
    ('will, can 뒤', '동사원형: that you will enjoy ~ (will enjoyed ✗)'),
    ('I don\'t think that ~', '"~가 아니라고 생각한다"는 보통 앞의 think를 부정해요. I don\'t think (that) the bag looks perfect. (교과서 6과)'),
])
D.step(SCARDS(D, '해석 카드 · 동사', [
    ('I guess that he is about 20 years old.', '나는 그가 스무 살쯤 되었다고 짐작한다.'), ('I remember that she was kind.', '나는 그녀가 친절했다는 것을 기억한다.'),
    ('He says that time is money.', '그는 시간이 돈이라고 말한다.'), ('I hear that she is a doctor.', '나는 그녀가 의사라고 들었다.'),
    ("I don't think that it is true.", '나는 그것이 사실이 아니라고 생각한다.'), ('She hopes that her son is happy.', '그녀는 아들이 행복하기를 바란다.'),
    ('We believe that he is kind.', '우리는 그가 친절하다고 믿는다.'), ('My mom knew that something was wrong.', '엄마는 뭔가 잘못되었다는 것을 아셨다.')]))
D.step(PICK(D, '어법 선택', [
    ('She {says|say} that it is very useful.', '그녀는 그것이 매우 유용하다고 말한다.', '정답 ▶ says\n이유: 주어 She(3인칭 단수) + 현재 → says'),
    ("I don't {think|thought} there is a toy store in town.", '나는 동네에 장난감 가게가 있다고 생각하지 않는다.', "정답 ▶ think\n이유: don't 뒤에는 동사원형 → don't think"),
    ('My mom knew that something {was|were} wrong.', '엄마는 뭔가 잘못되었다는 것을 아셨다.', '정답 ▶ was\n이유: that절의 주어 something은 단수 → was'),
    ('We hope that you will {enjoy|enjoyed} a taste of Korea.', '우리는 네가 한국의 맛을 즐기기를 바란다.', '정답 ▶ enjoy\n이유: will 뒤에는 동사원형 → will enjoy'),
    ("He doesn't {think|thinks} that the test is easy.", '그는 그 시험이 쉽다고 생각하지 않는다.', "정답 ▶ think\n이유: doesn't 뒤에는 동사원형 → doesn't think"),
    ('I {think|want} that Mina is a good friend.', '나는 미나가 좋은 친구라고 생각한다.', '정답 ▶ think\n이유: that절(Mina is a good friend)을 목적어로 쓰는 동사 → think\n오답 ▶ want는 that절이 아니라 to부정사를 써요.'),
    ('I hope that {we|us} pass the history test.', '나는 우리가 역사 시험에 합격하기를 바란다.', '정답 ▶ we\n이유: that절의 주어 자리 → 주격 we'),
    ('Tom {thinks|think} that his sister is funny.', 'Tom은 여동생이 재미있다고 생각한다.', '정답 ▶ thinks\n이유: 주어 Tom(3인칭 단수) + 현재 → thinks'),
]))
D.step(ERR(D, '오류 찾기', [
    ('She [[say]] that [[it]] [[is]] very [[useful]].', 0, 'says', '그녀는 그것이 매우 유용하다고 말한다.', '정답 ▶ say → says\n이유: 주어 She(3인칭 단수)'),
    ("I [[don't]] [[thought]] [[there]] is a toy store [[in]] town.", 1, 'think', '나는 동네에 장난감 가게가 있다고 생각하지 않는다.', "정답 ▶ thought → think\n이유: don't 뒤는 동사원형"),
    ('My mom [[knew]] [[that]] something [[were]] [[wrong]].', 2, 'was', '엄마는 뭔가 잘못되었다는 것을 아셨다.', '정답 ▶ were → was\n이유: something은 단수 취급'),
    ('I [[hope]] [[that]] [[go]] to [[Canada]].', 2, 'I go', '나는 캐나다에 가기를 바란다.', '정답 ▶ go → I go\n이유: that 뒤에 주어가 없어요 → that I go to Canada\n포인트 ▶ that + 주어 + 동사'),
]))
D.step(MC('어법상 올바른 문장', [
    ('어법상 <b>올바른</b> 문장은?', ["He knows today is his mom's birthday.", 'She say that it is very useful.', "I don't thought there is a toy store in town.", 'My mom knew that something were wrong.', 'We hope that you will enjoyed a taste of Korea.'],
     "정답 ▶ He knows today is his mom's birthday.\n이유: knows 뒤에 that이 생략된 문장 (He knows (that) today is ~) ✔\n오답 ▶ say → says / don't thought → don't think / were → was / will enjoyed → will enjoy"),
    ('어법상 <b>올바른</b> 문장은?', ['I believe that he is honest.', 'I want that I go home.', 'I hope that will be fine.', 'She thinks that him is kind.', "He don't think that it is true."],
     "정답 ▶ I believe that he is honest.\n오답 ▶ want that I go → want to go / that will be → that it will be (주어 필요) / him → he (주어는 주격) / He don't → He doesn't"),
    ('어법상 <b>어색한</b> 문장은?', ['I hope that go to Canada.', 'I hope she lives for a long time.', 'I hope we pass our history test.', 'I hope that we can attend your wedding.'],
     '정답 ▶ I hope that go to Canada.\n이유: that 뒤에 주어가 없어요 → I hope that I go to Canada.\n오답 ▶ 나머지는 that이 생략되었거나(she lives, we pass) 주어 + 동사가 잘 갖춰져 있어요.'),
]))
DAYS.append(D.done())

# ═════════ DAY 4 · 접속사 that vs 지시사 that ═════════
D = Day('c4', '접속사 that vs 지시사 that', '시험에 가장 많이 나오는 유형 · that 바로 뒤를 보면 보여요')
D.note('개념 ① that은 세 가지', [
    ('접속사 that', 'that 뒤에 "주어 + 동사"가 다 있는 문장이 와요. 뜻은 따로 없이 "~라고, ~라는 것"으로 이어 줘요.\nI think that he is kind.'),
    ('지시대명사 that', '"저것, 그것" — that 자체가 주어나 목적어예요. 뒤에 바로 동사가 오거나, 문장이 거기서 끝나요.\nThat is my bag. / I didn\'t know that.'),
    ('지시형용사 that', '"저 ~, 그 ~" — that 바로 뒤에 명사가 와서 그 명사를 꾸며요.\nThat girl is my sister. / I like that song.'),
])
D.note('개념 ② 헷갈리는 함정', [
    ('I think that is your bag.', 'that 뒤에 바로 is → that이 주어(저것) → 지시대명사. (think 뒤 접속사 that은 생략)\n나는 저것이 네 가방이라고 생각한다.'),
    ('I know that book is interesting.', 'that 뒤 book(명사) → 그 책 → 지시형용사. (know 뒤 접속사 that은 생략)\n나는 그 책이 재미있다는 것을 안다.'),
    ('I think that he is kind.', 'that 뒤에 he(주어) is(동사) → 접속사'),
    ('구별 3단계', '① that 바로 뒤가 동사·문장 끝? → 지시대명사 ② that 바로 뒤가 명사이고 뒤에 동사가 이어지지 않음? → 지시형용사 ③ that 뒤가 "주어 + 동사"? → 접속사'),
])
D.step(MC('that의 쓰임 고르기', [
    role(D, 'I think that he is kind.', '나는 그가 친절하다고 생각한다.', 0, 'that 뒤에 he(주어) is(동사)가 다 있는 문장 → 접속사'),
    role(D, 'I think that is your bag.', '나는 저것이 네 가방이라고 생각한다.', 1, 'that 바로 뒤에 is(동사) → that이 주어 "저것" → 지시대명사 (think 뒤 접속사 that은 생략)'),
    role(D, 'That girl is really beautiful.', '저 여자아이는 정말 아름답다.', 2, 'That 바로 뒤에 girl(명사) → "저 여자아이" → 지시형용사', u='That'),
    role(D, "I didn't know that.", '나는 그것을 몰랐다.', 1, 'that 뒤에서 문장이 끝나요 → know의 목적어 "그것" → 지시대명사 (교과서 6과 대화문)'),
    role(D, 'She heard that her class was crowded.', '그녀는 자기 반이 붐빈다고 들었다.', 0, 'that 뒤에 her class(주어) was(동사) → 접속사\n포인트 ▶ 시제 일치: heard(과거)에 맞춰 that절도 was'),
    role(D, 'I know that book is interesting.', '나는 그 책이 재미있다는 것을 안다.', 2, 'that 바로 뒤에 book(명사) → "그 책" → 지시형용사. that book이 생략된 접속사 뒤 문장의 주어예요. (know (that) that book is interesting)'),
    role(D, 'Do you think that is smart?', '너는 저것이 똑똑하다고 생각하니?', 1, 'that 바로 뒤에 is(동사) → that이 주어 "저것, 그것" → 지시대명사'),
    role(D, 'They learned that the Earth moves around the Sun.', '그들은 지구가 태양 주위를 돈다는 것을 배웠다.', 0, 'that 뒤에 the Earth(주어) moves(동사) → 접속사'),
]))
D.step(TF('구별 연습 T/F', [
    ('I saw that picture.의 that은 접속사이다.', False, '정답 ▶ F\n이유: that 뒤에 picture(명사)만 있고 동사가 없어요 → "그 사진" → 지시형용사\n해석 ▶ 나는 그 사진을 보았다.'),
    ('I think that I can fly.의 that은 접속사이다.', True, '정답 ▶ T\n이유: that 뒤에 I(주어) can fly(동사) → 접속사\n해석 ▶ 나는 내가 날 수 있다고 생각한다.'),
    ('They knew that was the right way.의 that은 접속사이다.', False, '정답 ▶ F\n이유: that 바로 뒤에 was(동사) → that이 주어 "그것" → 지시대명사\n해석 ▶ 그들은 그것이 옳은 방법이라는 것을 알았다.'),
    ('Who is that man?의 that은 "저 ~"라는 뜻이다.', True, '정답 ▶ T\n이유: that 뒤에 man(명사) → "저 남자" → 지시형용사\n해석 ▶ 저 남자는 누구니?'),
    ('I hope that everything goes well.의 that은 "저것"이라는 뜻이다.', False, '정답 ▶ F\n이유: that 뒤에 everything(주어) goes(동사) → 접속사. 뜻은 따로 없어요.\n해석 ▶ 나는 모든 것이 잘되기를 바란다.'),
    ('I think that man is my teacher.의 that은 지시형용사이다.', True, '정답 ▶ T\n이유: that 뒤 man(명사) → "저 남자". 접속사 that은 think 뒤에 생략되어 있어요.\n해석 ▶ 나는 저 남자가 우리 선생님이라고 생각한다.'),
]))
D.sent('I saw that picture.', '나는 그 사진을 보았다.'); D.sent('I think that I can fly.', '나는 내가 날 수 있다고 생각한다.'); D.sent('Who is that man?', '저 남자는 누구니?')
D.sent('I hope that everything goes well.', '나는 모든 것이 잘되기를 바란다.'); D.sent('I think that man is my teacher.', '나는 저 남자가 우리 선생님이라고 생각한다.')
D.step(MC('쓰임이 다른 하나', [
    ('밑줄 친 <i>that</i>의 쓰임이 나머지와 <b>다른</b> 것은?', [U('I think that is your bag.', 'that'), U('I believe that he is honest.', 'that'), U('She thinks that they like the story.', 'that'), U('They know that Sarah is always busy.', 'that'), U('I remember that the boy said so.', 'that')],
     '정답 ▶ I think <u>that</u> is your bag.\n이유: that 바로 뒤에 is → "저것"(지시대명사)\n오답 ▶ 나머지는 모두 that 뒤에 주어 + 동사(he is / they like / Sarah is / the boy said) → 접속사'),
    ('밑줄 친 <i>that</i>의 쓰임이 나머지와 <b>다른</b> 것은?', [U('I know that book is interesting.', 'that'), U('I think that he is kind.', 'that'), U('I hope that Jane likes the flowers.', 'that'), U("I don't think that Henry is honest.", 'that'), U('I think that Ella is faster than Susan.', 'that')],
     '정답 ▶ I know <u>that</u> book is interesting.\n이유: that 뒤 book(명사) → "그 책"(지시형용사)\n오답 ▶ 나머지는 that 뒤에 주어 + 동사 → 접속사'),
    ('밑줄 친 <i>that</i>의 쓰임이 나머지와 <b>다른</b> 것은?', [U('I think that I can fly.', 'that'), U('I saw that picture.', 'that'), U('I like that white book.', 'that'), U('I can hear that sound.', 'that'), U('Look at that cute dog.', 'that')],
     '정답 ▶ I think <u>that</u> I can fly.\n이유: 나머지는 that 뒤에 명사(picture, white book, sound, cute dog)가 오는 지시형용사, 이것만 that 뒤에 I(주어) can fly(동사) → 접속사'),
    ('밑줄 친 <i>that</i>의 쓰임이 나머지와 <b>다른</b> 것은?', [U('Do you think that is wrong?', 'that'), U('No one knows that he is honest.', 'that'), U('I believe that you will do your best.', 'that'), U('Jihwan says that he is very handsome.', 'that'), U('My mother knows that I went to the library.', 'that')],
     '정답 ▶ Do you think <u>that</u> is wrong?\n이유: that 바로 뒤 is → "그것"(지시대명사)\n오답 ▶ 나머지는 that 뒤에 주어 + 동사 → 접속사'),
]))
D.sent('I like that white book.', '나는 저 하얀 책이 좋다.'); D.sent('Look at that cute dog.', '저 귀여운 개를 봐.')
DAYS.append(D.done())

# ═════════ DAY 5 · 우리말 → 영어 · 두 문장 잇기 ═════════
D = Day('c5', '우리말 → 영어 · 두 문장 잇기', '"~라고 생각해"를 영어로 · I hope so. / I think so.를 that절로 바꾸기')
D.note('개념 ① 영작 순서', [
    ('나는 / 생각한다 / 그것이 매우 재미있다고', 'I think / that / it is very interesting.'),
    ('순서', '① 주어 + 동사(I think) ② that ③ 주어 + 동사 + 나머지 (it is very interesting)'),
    ('"~가 아니라고 생각해"', '앞의 think를 부정: I don\'t think (that) ~'),
])
D.note('개념 ② 두 문장을 that으로 잇기', [
    ('Ms. Song will get well soon. + I hope so.', '→ I hope that Ms. Song will get well soon. (so가 가리키는 문장을 that 뒤로)'),
    ('She will come tomorrow. + We know it.', '→ We know that she will come tomorrow. (it은 빼요: know it that ✗)'),
    ('You made a mistake. + I think so.', '→ I think that you made a mistake. (think so that ✗)'),
])
D.step(MC('우리말 → 영어', [
    ('우리말을 영어로 바르게 옮긴 것은?<br><b>당신이 좋은 시간을 보내기를 희망합니다.</b>', ['I hope that you have a great time.', 'I hoped that you have a great time.', 'I hope what you have a great time.', 'I will hope you have a great time.', 'I hope that have you a great time.'],
     '정답 ▶ I hope that you have a great time.\n오답 ▶ hoped(과거: 희망했다) / what(✗ → that) / will hope(희망할 것이다) / have you(주어 + 동사 순서가 바뀜)'),
    ('밑줄 친 우리말을 바르게 영작한 것은?<br>A: What do you think of the story?<br>B: <u>나는 그것이 매우 재미있다고 생각해.</u>', ['I think that it is very interesting.', 'That is very interesting I think.', 'I think it is that very interesting.', 'It is very interesting that I think.', 'That I think is very interesting it.'],
     '정답 ▶ I think that it is very interesting.\n이유: 나는 생각해(I think) + that + 그것이 매우 재미있다(it is very interesting)'),
    ('우리말을 영어로 바르게 옮긴 것은?<br><b>나는 그 가방이 완벽해 보인다고 생각하지 않는다.</b>', ["I don't think that the bag looks perfect.", 'I think that the bag not looks perfect.', "I don't thought that the bag looks perfect.", "I don't think that the bag look perfect.", 'I not think that the bag looks perfect.'],
     "정답 ▶ I don't think that the bag looks perfect.\n이유: 교과서 6과 본문 문장. \"~라고 생각하지 않는다\" → don't think + that절\n오답 ▶ not looks(✗) / don't thought(don't 뒤 원형) / the bag look(the bag은 단수 → looks) / I not think(✗ → I don't think)"),
    ('우리말을 영어로 바르게 옮긴 것은?<br><b>나는 그녀가 의사라고 들었다.</b>', ['I heard that she is a doctor.', 'I heard that her is a doctor.', 'I heard she that is a doctor.', 'She heard that I am a doctor.', 'I heard that is a doctor.'],
     '정답 ▶ I heard that she is a doctor.\n오답 ▶ her(주어는 she) / she that(순서: that + 주어) / 주어가 바뀜 / that 뒤 주어 없음'),
]))
D.sent('I think that it is very interesting.', '나는 그것이 매우 재미있다고 생각한다.'); D.sent('I heard that she is a doctor.', '나는 그녀가 의사라고 들었다.')
D.step(MC('두 문장 잇기', [
    ('두 문장을 that으로 바르게 이은 것은?<br><b>Ms. Song will get well soon. + I hope so.</b>', ['I hope that Ms. Song will get well soon.', 'I hope so that Ms. Song will get well soon.', 'Ms. Song hopes that I will get well soon.', 'I hope that so Ms. Song will get well soon.'],
     '정답 ▶ I hope that Ms. Song will get well soon.\n이유: so가 가리키는 내용(Ms. Song will get well soon)을 that 뒤에 넣고 so는 빼요.\n해석 ▶ 나는 송 선생님이 곧 나으시기를 바란다.'),
    ('두 문장을 that으로 바르게 이은 것은?<br><b>She will come here tomorrow. + We know it.</b>', ['We know that she will come here tomorrow.', 'We know it that she will come here tomorrow.', 'She knows that we will come here tomorrow.', 'We know that will come here tomorrow.'],
     '정답 ▶ We know that she will come here tomorrow.\n이유: it이 가리키는 문장을 that 뒤로 → it은 빼요. (know it that ✗)\n오답 ▶ 주어가 바뀜 / that 뒤 주어(she) 없음'),
    ('두 문장을 that으로 바르게 이은 것은?<br><b>You made a stupid mistake. + I think so.</b>', ['I think that you made a stupid mistake.', 'I think so that you made a stupid mistake.', 'You think that I made a stupid mistake.', 'I think that made you a stupid mistake.'],
     '정답 ▶ I think that you made a stupid mistake.\n오답 ▶ think so that(so를 빼야 해요) / 주어가 바뀜 / made you(주어 + 동사 순서 ✗)'),
    ('두 문장을 that으로 바르게 이은 것은?<br><b>We should do something for nature. + We believe so.</b>', ['We believe that we should do something for nature.', 'We believe so that we should do something for nature.', 'We believe that should do something for nature.', 'We believe it that we should do something for nature.'],
     '정답 ▶ We believe that we should do something for nature.\n해석 ▶ 우리는 우리가 자연을 위해 무언가를 해야 한다고 믿는다.'),
]))
D.sent('I hope that Ms. Song will get well soon.', '나는 송 선생님이 곧 나으시기를 바란다.'); D.sent('We know that she will come here tomorrow.', '우리는 그녀가 내일 여기에 올 것을 안다.')
D.sent('I think that you made a stupid mistake.', '나는 네가 어리석은 실수를 했다고 생각한다.'); D.sent('We believe that we should do something for nature.', '우리는 우리가 자연을 위해 무언가를 해야 한다고 믿는다.')
D.step(SCR(D, '우리말 → 영어 배열', [
    ("I don't think that the bag looks perfect.", '나는 그 가방이 완벽해 보인다고 생각하지 않는다.'),
    ('I hope that you have a great time.', '나는 네가 좋은 시간을 보내기를 바란다.'),
    ('We know that she will come here tomorrow.', '우리는 그녀가 내일 여기에 올 것을 안다.'),
    ('Many people say that time is money.', '많은 사람들이 시간은 돈이라고 말한다.'),
    ('I believe that you will do your best.', '나는 네가 최선을 다할 거라고 믿는다.'),
]))
DAYS.append(D.done())

# ═════════ DAY 6 · 우리 교과서 문장으로 ═════════
D = Day('c6', '우리 교과서 문장으로', '동아(윤정미) 6과 Zero-Waste Challenge 본문·대화 속 that')
D.note('교과서 6과 속 that', [
    ("I don't think that the bag looks perfect.", '가방이 완벽해 보인다고 생각하진 않아. → 접속사 that'),
    ('I heard that plastic never goes away completely.', '플라스틱은 절대로 완전히 없어지지 않는다고 들었어. → 접속사 that'),
    ("I guess it's all right.", '그래도 괜찮은 것 같아. → guess 뒤 접속사 that 생략'),
    ("Don't you think that's cool?", "멋지다고 생각하지 않니? → think 뒤 접속사 that 생략, that's(= that is)의 that은 \"그것\"(지시대명사)"),
    ("Oh, I didn't know that.", '아, 몰랐네요. → that = "그것"(지시대명사), 뒤에 문장 없음'),
])
D.step(SCARDS(D, '교과서 문장 카드', [
    ("I don't think that the bag looks perfect.", '나는 가방이 완벽해 보인다고 생각하진 않아.'),
    ('I heard that plastic never goes away completely.', '플라스틱은 절대로 완전히 없어지지 않는다고 들었어.'),
    ("I guess it's all right.", '그래도 괜찮은 것 같아.'),
    ("Don't you think that's cool?", '멋지다고 생각하지 않니?'),
    ("Oh, I didn't know that. I'll close it right away.", '아, 몰랐네요. 즉시 닫을게요.'),
    ('I wanted to buy a new one, but I thought again.', '나는 새것을 사고 싶었지만, 다시 생각해 봤어.')],
    guide='교과서 6과 본문·대화 문장이에요. 해석을 맞혀 보세요.'))
D.step(MC('교과서 문장 · that의 쓰임', [
    role(D, "I don't think that the bag looks perfect.", '나는 가방이 완벽해 보인다고 생각하진 않아.', 0, 'that 뒤에 the bag(주어) looks(동사) → 접속사'),
    role(D, 'I heard that plastic never goes away completely.', '플라스틱은 절대로 완전히 없어지지 않는다고 들었어.', 0, 'that 뒤에 plastic(주어) goes(동사) → 접속사'),
    role(D, "Oh, I didn't know that.", '아, 몰랐네요.', 1, 'that 뒤에서 문장이 끝나요 → "그것"(know의 목적어) → 지시대명사'),
    ("<i>Don't you think that's cool?</i>에 대한 설명으로 알맞은 것은?", ["think 뒤에 접속사 that이 생략되었고, that's의 that은 '그것'이라는 뜻이다.", "that's의 that은 접속사이다.", 'think와 that 사이에는 아무것도 생략되지 않았다.', "that's는 that has를 줄인 말이다."],
     "정답 ▶ think 뒤에 접속사 that이 생략되었고, that's의 that은 '그것'이라는 뜻이다.\n이유: Don't you think (that) that's cool? → that's = that is, 바로 뒤에 is(동사)가 오니 that은 주어 \"그것\"(지시대명사)\n해석 ▶ 멋지다고 생각하지 않니?"),
    ("that이 생략된 곳이 있는 문장은?", ["I guess it's all right.", 'I wanted to buy a new one.', "I'll close it right away.", 'Can you turn off the water?'],
     "정답 ▶ I guess it's all right.\n이유: guess(동사) 뒤에 it(주어) is(동사) → I guess (that) it's all right.\n오답 ▶ 나머지는 뒤에 \"주어 + 동사\"로 된 문장이 따로 오지 않아요."),
]))
D.sent('Can you turn off the water?', '물을 잠가 주겠니?'); D.sent("I'll close it right away.", '즉시 닫을게요.'); D.sent('I wanted to buy a new one.', '나는 새것을 사고 싶었다.')
D.step(PICK(D, '교과서 문장 · 어법 선택', [
    ("I don't think that the bag {looks|look} perfect.", '나는 가방이 완벽해 보인다고 생각하진 않아.', '정답 ▶ looks\n이유: that절의 주어 the bag은 단수 → looks'),
    ("I don't {think|thinks} that the bag looks perfect.", '나는 가방이 완벽해 보인다고 생각하진 않아.', "정답 ▶ think\n이유: don't 뒤에는 동사원형"),
    ('I heard {that|what} plastic never goes away completely.', '플라스틱은 절대로 완전히 없어지지 않는다고 들었어.', '정답 ▶ that\n이유: 뒤에 plastic(주어) goes(동사)가 다 있는 문장 → 접속사 that\n오답 ▶ what은 뒤에 빠진 것이 있을 때 써요.'),
    ('I heard that plastic never {goes|go} away completely.', '플라스틱은 절대로 완전히 없어지지 않는다고 들었어.', '정답 ▶ goes\n이유: plastic은 셀 수 없는 명사 → 단수 취급 → goes'),
    ("I guess {it's|its} all right.", '그래도 괜찮은 것 같아.', "정답 ▶ it's\n이유: it is를 줄인 it's (its는 \"그것의\")\n포인트 ▶ guess 뒤 접속사 that 생략"),
]))
D.step(SCR(D, '교과서 문장 배열', [
    ("I don't think that the bag looks perfect.", '나는 가방이 완벽해 보인다고 생각하진 않아.'),
    ('I heard that plastic never goes away completely.', '플라스틱은 절대로 완전히 없어지지 않는다고 들었어.'),
    ("I guess it's all right.", '그래도 괜찮은 것 같아.'),
]))
DAYS.append(D.done())

# ═════════ DAY 7 · 실전 ① 쓰임이 같은 것 · 다른 것 ═════════
D = Day('c7', '실전 ① 쓰임이 같은 것 · 다른 것', 'Grammar Build Up 객관식 유형 · 접속사 that이 주어·보어 자리에 올 때도')
D.note('개념 · that절은 주어·보어 자리에도 와요 (모두 접속사)', [
    ('목적어', 'I know that he is right. (그가 옳다는 것을 안다) → that 생략 가능'),
    ('보어', 'The problem is that I have no time. (문제는 내가 시간이 없다는 것이다) → be동사 뒤'),
    ('주어', 'That he told a lie is not true. (그가 거짓말했다는 것은 사실이 아니다) → 문장 맨 앞'),
    ('가주어 it', 'It is true that she is kind. (그녀가 친절하다는 것은 사실이다) → It은 가짜 주어, that절이 진짜 주어'),
    ('생략', '목적어 자리 that만 생략할 수 있어요. 주어·보어 자리 that은 생략 ✗'),
])
D.step(MC('주어진 문장과 쓰임이 같은 것', [
    ('밑줄 친 <i>that</i>과 쓰임이 같은 것은?' + Q('My brother believed that I didn\'t take his money.', 'that'), [U('They learned that the Earth moves around the Sun.', 'that'), U("What's that?", 'that'), U('Who is that girl dancing over there?', 'that'), U('I like that red bag.', 'that'), U('I said that already.', 'that')],
     '정답 ▶ They learned <u>that</u> the Earth moves around the Sun.\n이유: 주어진 문장과 같이 동사 뒤 목적어 절을 이끄는 접속사 that\n오답 ▶ What\'s that?(그것, 지시대명사) / that girl(저 여자아이) · that red bag(저 빨간 가방, 지시형용사) / said that already(그것을, 지시대명사)'),
    ('밑줄 친 <i>that</i>과 쓰임이 같은 것은?' + Q('Jack thinks that everything will be fine.', 'that'), [U('I think that Ulsan is a beautiful city.', 'that'), U('That skirt is my favorite.', 'That'), U('I will send that picture to her tomorrow.', 'that'), U('He was a student at that time.', 'that'), U('That little girl is my sister.', 'That')],
     '정답 ▶ I think <u>that</u> Ulsan is a beautiful city.\n이유: 접속사 that (that 뒤에 Ulsan is ~)\n오답 ▶ 나머지는 that 뒤에 명사(skirt, picture, time, little girl) → 지시형용사'),
    ('밑줄 친 <i>that</i>과 쓰임이 같은 것은?' + Q('We still remember that she was a smart student.', 'that'), [U('Please don\'t say that you are very sorry.', 'that'), U('Do you know that boy over there?', 'that'), U('I am not that hungry.', 'that'), U('That is my pencil case.', 'That'), U('You will need to do that.', 'that')],
     '정답 ▶ Please don\'t say <u>that</u> you are very sorry.\n이유: 동사(say) 뒤 목적어 절을 이끄는 접속사 that\n오답 ▶ that boy(저 소년, 지시형용사) / that hungry(그렇게, 부사) / That is(저것은) · do that(그것을, 지시대명사)'),
]))
D.sent('They learned that the Earth moves around the Sun.', '그들은 지구가 태양 주위를 돈다는 것을 배웠다.'); D.sent('I think that Ulsan is a beautiful city.', '나는 울산이 아름다운 도시라고 생각한다.')
D.step(MC('쓰임이 다른 하나', [
    ('밑줄 친 <i>that</i>의 쓰임이 나머지 넷과 <b>다른</b> 것은?', [U('Do you know who that man is?', 'that'), U("I didn't know that he was absent.", 'that'), U('He knows that I enjoy listening to music.', 'that'), U('My hope is that I can make a lot of money.', 'that'), U('It is certain that he will start a new project.', 'that')],
     '정답 ▶ Do you know who <u>that</u> man is?\n이유: that man(저 남자) → 지시형용사\n오답 ▶ 나머지는 모두 접속사 that (목적어 · 목적어 · 보어(is 뒤) · 진주어(It ~ that))'),
    ('밑줄 친 <i>that</i>의 쓰임이 나머지 넷과 <b>다른</b> 것은?', [U('Your dad heard of that story about you.', 'that'), U("I know that I'm not alone any more.", 'that'), U('Many people say that time is money.', 'that'), U('We believe that you can win.', 'that'), U('I hope that a miracle will happen.', 'that')],
     '정답 ▶ Your dad heard of <u>that</u> story about you.\n이유: that story(그 이야기) → 지시형용사\n오답 ▶ 나머지는 that 뒤에 주어 + 동사 → 접속사'),
    ('밑줄 친 <i>that</i>의 쓰임이 나머지 넷과 <b>다른</b> 것은?', [U('She thought that I was busy.', 'that'), U('They knew that was the right way.', 'that'), U('That is not my umbrella.', 'That'), U('I can\'t believe that!', 'that'), U('Who told you that?', 'that')],
     '정답 ▶ She thought <u>that</u> I was busy.\n이유: that 뒤에 I(주어) was(동사) → 접속사\n오답 ▶ 나머지 that은 모두 "그것, 저것"(지시대명사) — that 바로 뒤에 동사가 오거나 문장이 끝나요.'),
]))
D.step(MC('같은 것끼리 묶기', [
    ('<보기>의 밑줄 친 <i>that</i>과 쓰임이 같은 것을 <b>모두</b> 고른 것은?<br><보기> I think <u>that</u> it will rain soon.<br>ⓐ I\'m busy <u>that</u> day.<br>ⓑ I am looking at <u>that</u> man with a dog.<br>ⓒ She knows <u>that</u> Jason is a famous singer.<br>ⓓ You shouldn\'t put <u>that</u> bottle in the trash can.<br>ⓔ It is true <u>that</u> fast food is bad for your health.', ['ⓒ, ⓔ', 'ⓐ, ⓒ', 'ⓑ, ⓓ', 'ⓐ, ⓑ', 'ⓑ, ⓒ, ⓔ'],
     '정답 ▶ ⓒ, ⓔ\n이유: <보기>는 접속사 that. ⓒ knows 뒤 목적어 절 · ⓔ It ~ that(진주어 절) → 접속사\n오답 ▶ ⓐ that day(그날) ⓑ that man(저 남자) ⓓ that bottle(그 병) → 지시형용사', True),
    ('밑줄 친 <i>that</i>의 쓰임이 같은 것끼리 묶인 것은?<br>(A) I believe <u>that</u> he is honest.<br>(B) <u>That</u> bag is very expensive.<br>(C) The truth is <u>that</u> we were late.<br>(D) Look at <u>that</u>!<br>(E) She said <u>that</u> she was hungry.', ['(A), (C), (E)', '(A), (B), (D)', '(B), (D)', '(B), (C), (E)', '(A), (D), (E)'],
     '정답 ▶ (A), (C), (E)\n이유: (A) believe 뒤 목적어 · (C) is 뒤 보어 · (E) said 뒤 목적어 → 모두 접속사\n오답 ▶ (B) That bag(저 가방, 지시형용사) (D) Look at that!(저것, 지시대명사)', True),
]))
D.step(MC('생략 · 빈칸', [
    ('밑줄 친 <i>that</i>을 생략할 수 있는 것은?', [U('I knew that he was right.', 'that'), U('That he is my brother is true.', 'That'), U('The problem is that there is not enough time.', 'that'), U('That person is my sister.', 'That')],
     '정답 ▶ I knew that he was right.\n이유: 목적어 자리의 접속사 that만 생략할 수 있어요.\n오답 ▶ 주어 자리 That(문장 맨 앞) · 보어 자리 that(is 뒤)은 생략 ✗ / That person(저 사람)은 지시형용사'),
    ('빈칸에 들어갈 말이 나머지와 <b>다른</b> 것은?<br>① He knows _____ I like Amy.<br>② _____ Tim is an excellent student is true.<br>③ The problem is _____ I don\'t understand it.<br>④ _____ is true that Jane is very diligent.<br>⑤ The picture shows _____ he is handsome.', ['④', '①', '②', '③', '⑤'],
     '정답 ▶ ④\n이유: ④는 가주어 It (It is true that ~), 나머지는 모두 접속사 that\n포인트 ▶ It ~ that ~: It은 가짜 주어, that 뒤가 진짜 주어', True),
]))
DAYS.append(D.done())

# ═════════ DAY 8 · 실전 ② 어법 · 종합 ═════════
D = Day('c8', '실전 ② 어법 · 종합', 'Grammar Build Up 객관식 유형 · 어법상 옳은 문장 · 틀린 개수 · 두 문장의 쓰임 비교')
D.note('시험 직전 체크리스트', [
    ('① that 뒤에 주어 + 동사가 있나?', 'I hope that go ✗ → I hope that I go'),
    ('② 앞 문장 동사 · that절 동사의 수 · 시제', 'She say ✗ → says / something were ✗ → was / don\'t thought ✗ → don\'t think'),
    ('③ that절을 쓰는 동사인가?', 'think · believe · know · hope · hear · say ✔ / want · decide ✗(to부정사)'),
    ('④ 접속사인가 지시사인가?', 'that 바로 뒤: 주어 + 동사(접속사) / 동사·문장 끝(지시대명사) / 명사(지시형용사)'),
    ('⑤ 두 문장 잇기', 'I think so. → I think that ~ (so 빼기) / We know it. → We know that ~ (it 빼기)'),
])
D.step(MC('어법상 올바른 문장', [
    ('어법상 <b>올바른</b> 문장은?', ['I hope that she lives for a long time.', 'I hope that live for a long time.', 'I want that she lives for a long time.', 'I hope that her lives for a long time.', 'I hopes that she lives for a long time.'],
     '정답 ▶ I hope that she lives for a long time.\n오답 ▶ that 뒤 주어 없음 / want는 that절 ✗ / her → she(주어) / I hopes → I hope'),
    ('어법상 <b>올바른</b> 문장은?', ['Tom thinks that his sister is funny.', 'Tom think that his sister is funny.', 'Tom thinks that his sister are funny.', "Tom doesn't thinks that his sister is funny.", 'Tom thinks so that his sister is funny.'],
     "정답 ▶ Tom thinks that his sister is funny.\n오답 ▶ think → thinks / are → is / doesn't thinks → doesn't think / thinks so that → thinks that"),
    ('어법상 <b>어색한</b> 문장은?', ['We know it that she will come here tomorrow.', 'I hope that Ms. Song will get well soon.', 'We believe that we should save energy.', 'I think that you made a mistake.', 'Did you hear that there was a big fire?'],
     '정답 ▶ We know it that she will come here tomorrow.\n이유: it과 that절이 둘 다 know의 목적어가 되어 버려요 → We know that she will come here tomorrow.'),
]))
D.step(MC('틀린 문장 개수 세기', [
    ('어법상 <b>틀린</b> 문장의 개수는?<br>• I hope that go to Canada.<br>• I hope she lives for a long time.<br>• I hope we pass our history test.<br>• I hope that we can attend your wedding.', ['1개', '0개', '2개', '3개', '4개'],
     '정답 ▶ 1개\n틀린 것 ▶ I hope that go to Canada. (that 뒤 주어 없음 → that I go)\n맞는 것 ▶ that 생략(she lives, we pass) ✔ / that we can attend ✔', True),
    ('어법상 <b>틀린</b> 문장의 개수는?<br>• She say that it is very useful.<br>• He knows today is his mom\'s birthday.<br>• I don\'t thought there is a toy store in town.<br>• My mom knew that something were wrong.<br>• We hope that you will enjoy a taste of Korea.', ['3개', '1개', '2개', '4개', '5개'],
     "정답 ▶ 3개\n틀린 것 ▶ say → says / don't thought → don't think / were → was\n맞는 것 ▶ knows 뒤 that 생략 ✔ / will enjoy ✔", True),
]))
D.step(MC('두 문장의 쓰임 비교', [
    ('두 문장의 밑줄 친 부분의 쓰임이 <b>같은</b> 것은?', [
        'The problem is <u>that</u> I didn\'t bring my phone. / Many people believe <u>that</u> the dragon is a symbol of power.',
        'I think <u>that</u> I can change my phone. / Where did you buy <u>that</u> old vase?',
        'I know <u>that</u> he is kind. / I want <u>that</u> blue cap.',
        'She said <u>that</u> she was tired. / <u>That</u> is my seat.',
        'I hope <u>that</u> you like it. / Who is <u>that</u> boy?'],
     '정답 ▶ The problem is <u>that</u> I didn\'t bring my phone. / Many people believe <u>that</u> the dragon is a symbol of power.\n이유: 둘 다 접속사 that (보어 절 · 목적어 절)\n오답 ▶ 나머지는 모두 [접속사 / 지시사] 짝 — that old vase · that blue cap · that boy(지시형용사), That is(지시대명사)'),
    ('밑줄 친 <i>that</i> 중 접속사인 것의 개수는?<br>ⓐ You will need to do <u>that</u>.<br>ⓑ Do you know <u>that</u> boy over there?<br>ⓒ I think <u>that</u> Joe has too many balls.<br>ⓓ I said <u>that</u> already.<br>ⓔ Jenny knows <u>that</u> you can play the piano well.', ['2개', '1개', '3개', '4개', '5개'],
     '정답 ▶ 2개 (ⓒ, ⓔ)\n이유: ⓒ that Joe has ~ · ⓔ that you can play ~ → that 뒤에 주어 + 동사 → 접속사\n오답 ▶ ⓐ do that(그것을) ⓓ said that(그것을) → 지시대명사 / ⓑ that boy(저 소년) → 지시형용사', True),
]))
D.step(ERR(D, '오류 찾기', [
    ('I [[want]] that [[I]] [[go]] to the [[zoo]].', 0, 'hope', '나는 동물원에 가기를 바란다.', '정답 ▶ want → hope\n이유: want는 that절을 목적어로 쓰지 않아요 (I want to go to the zoo. 는 가능)\n포인트 ▶ that절과 쓰는 동사: think · believe · know · hope · hear · say'),
    ('Many [[people]] [[says]] [[that]] time [[is]] money.', 1, 'say', '많은 사람들이 시간은 돈이라고 말한다.', '정답 ▶ says → say\n이유: 주어 Many people은 복수 → say'),
    ('He [[thinks]] [[that]] [[him]] is [[a good]] singer.', 2, 'he', '그는 그가 좋은 가수라고 생각한다.', '정답 ▶ him → he\n이유: that절의 주어 자리 → 주격 he'),
    ("Mina [[doesn't]] [[believes]] [[that]] the story [[is]] true.", 1, 'believe', '미나는 그 이야기가 사실이라고 믿지 않는다.', "정답 ▶ believes → believe\n이유: doesn't 뒤에는 동사원형"),
]))
DAYS.append(D.done())

RENAME = {'c5': 'that 영작 · 두 문장 잇기', 'c6': 'that · 교과서 6과 문장', 'c7': 'that 실전 ① 쓰임 같은 것·다른 것', 'c8': 'that 실전 ② 어법 · 종합'}
for d in DAYS:
    if d['id'] in RENAME: d['range'] = RENAME[d['id']]
for d in DAYS: ansfirst(d['steps'])
# 11/1 선생님: 따로 링크가 아니라 to부정사 ① 단원 DAY 13부터 이어서
import json, subprocess
path = '/home/claude/proj/data/m1-grammar-to1.js'
PK = json.loads(subprocess.check_output(['node', '-e', "global.window={};require('%s');process.stdout.write(JSON.stringify(window.PKG))" % path]))
base = [d for d in PK['days'] if not d['id'].startswith('c')]
assert len(base) == 12, len(base)
PK['days'] = base + DAYS
for i, d in enumerate(PK['days']): d['name'] = 'DAY %d' % (i + 1)
PK['unit'] = '공통 문법 · to부정사 ① · 접속사 that'
PK['title'] = 'to부정사 ① 명사적 용법 · 접속사 that'
PK['titleKo'] = '~하는 것 · 주어 · 목적어 · 보어 / ~라고 생각하다 · 지시사 that과 구별'
src = open(path, encoding='utf-8').read(); head = src[:src.index('window.PKG')]
if '접속사 that' not in head: head = head.rstrip('\n') + '\n/* 11/1: DAY 13~20 = 동아(윤정미) 6과 문법 · 접속사 that (gen/gen_m1that.py가 이 파일 뒤에 붙임) */\n'
write(PK, path, head)
print('ok', [(d['name'], d['id'], d['range']) for d in PK['days']][10:])
