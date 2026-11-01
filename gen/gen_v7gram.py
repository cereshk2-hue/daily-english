import sys, re, json, subprocess
sys.path.insert(0, '/home/claude/work/gen')
from gencommon import write
from dlgcommon import ansfirst
# 중2 비상(황종배) 7과 문법 (11/1): Pattern 1 so ~ that … · Pattern 2 가주어 it
# 근거: Grammar Build Up 객관식 7과 유형 + 교과서 7과 본문 문장. 7과 본문(d2) 바로 뒤 DAY 5~10으로 끼움

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
            r = f if k[0] == w else m.group(1); k[0] += 1; return r
        D.sent(re.sub(r'\s+', ' ', re.sub(r'\[\[(.+?)\]\]', rep, s)).strip(), ko)
    return {'type': 'error', 'title': title, 'guide': '어법상 틀린 곳을 고르세요.', 'items': [{'s': s, 'w': w, 'fix': f, 'ex': x} for s, w, f, ko, x in items]}
U = lambda s, u: s.replace(u, '<u>' + u + '</u>', 1)
def Q(en, u=None): return '<br><b>' + (U(en, u) if u else en) + '</b>'

DAYS = []

# ═════════ 문법 ① so ~ that 기본 ═════════
D = Day('g1', '7과 문법 ① so ~ that 기본', '매우 ~해서 …하다 · so + 형용사/부사 + that + 주어 + 동사')
D.note('개념 ① so ~ that …', [
    ('so + 형용사/부사 + that + 주어 + 동사', '매우(너무) ~해서 (그 결과) …하다'),
    ('원인 → 결과', 'so 뒤 형용사·부사 = 원인, that 뒤 문장 = 결과'),
    ('He was so nervous that he forgot his lines.', '그는 매우 긴장해서 대사를 잊어버렸다.'),
    ('It is so big that it covers her shoulder.', '교과서 7과 · 그것은 매우 커서 그녀의 어깨를 덮어요.'),
])
D.note('개념 ② 어법 체크', [
    ('so 뒤에는 형용사·부사', 'so kind ✔ / so beauty ✗(명사) → so beautiful'),
    ('very · too ✗', 'very ~ that ✗ / too ~ that ✗ → so ~ that'),
    ('that 뒤에는 주어 + 동사', 'He ate so much that had a stomachache. ✗ → that he had'),
    ('시제 맞추기', '앞이 과거(was)면 that절도 과거: was so tired that he couldn\'t (can\'t ✗)'),
    ('be동사 뒤 형용사 / 일반동사 뒤 부사', 'The bag is so heavy ✔ / It rained so heavily ✔ (rained so heavy ✗)'),
])
D.step(SCARDS(D, '해석 카드', [
    ('He was so nervous that he forgot his lines.', '그는 매우 긴장해서 대사를 잊어버렸다.'),
    ('The movie was so funny that we laughed for ten minutes.', '그 영화는 매우 웃겨서 우리는 10분 동안 웃었다.'),
    ('I was so hungry that I ate a whole pizza.', '나는 매우 배가 고파서 피자 한 판을 다 먹었다.'),
    ('The test was so easy that everyone passed it.', '시험이 매우 쉬워서 모두가 통과했다.'),
    ('The box was so heavy that I couldn\'t carry it.', '그 상자는 너무 무거워서 나는 그것을 옮길 수 없었다.'),
    ('It is so big that it covers her shoulder.', '그것은 매우 커서 그녀의 어깨를 덮는다. (교과서)'),
    ('These centers are so popular that they are always full of people.', '이 센터들은 매우 인기 있어서 늘 사람들로 가득 차 있다. (교과서)'),
    ('The curry was so hot that Jake drank a lot of water.', '그 카레는 매우 매워서 Jake는 물을 많이 마셨다.')],
    guide='so ~ that 문장은 "매우 ~해서 …하다"로 해석해요.'))
D.step(TF('개념 확인 T/F', [
    ('so ~ that …은 "매우 ~해서 …하다"라는 뜻이다.', True, '정답 ▶ T\n이유: so 뒤가 원인, that 뒤가 결과예요.'),
    ('so와 that 사이에는 명사를 쓴다.', False, '정답 ▶ F\n이유: so와 that 사이에는 형용사나 부사가 와요. (so kind ✔ / so beauty ✗)'),
    ('The room was very cold that I put on my jacket.은 바른 문장이다.', False, '정답 ▶ F\n이유: very ~ that ✗ → The room was so cold that I put on my jacket.'),
    ('He was so tired that he can\'t exercise.는 시제가 맞지 않는다.', True, "정답 ▶ T\n이유: 앞이 과거(was)이므로 that절도 과거 → couldn't exercise"),
    ('He ate so much that had a stomachache.는 바른 문장이다.', False, '정답 ▶ F\n이유: that 뒤에 주어가 없어요 → that he had a stomachache'),
    ('It rained so heavily that they put off the game.에서 heavily는 바른 형태이다.', True, '정답 ▶ T\n이유: 일반동사 rained를 꾸미므로 부사 heavily ✔ (heavy ✗)'),
]))
D.step(PICK(D, '어법 선택', [
    ("He was {so|very} excited that he couldn't sleep.", '그는 매우 신이 나서 잠을 잘 수 없었다.', '정답 ▶ so\n이유: so ~ that 구문 (very ~ that ✗)'),
    ('My sister is so {kind|kindness} that everyone likes her.', '내 여동생은 매우 친절해서 모두가 그녀를 좋아한다.', '정답 ▶ kind\n이유: so 뒤에는 형용사 (kindness는 명사)'),
    ('The library is so {noisy|noise} that I can\'t concentrate.', '도서관이 매우 시끄러워서 나는 집중할 수 없다.', '정답 ▶ noisy\n이유: be동사 뒤 보어 → 형용사 noisy (noise는 명사)'),
    ('It rained so {heavily|heavy} that they put off the game.', '비가 매우 많이 와서 그들은 경기를 연기했다.', '정답 ▶ heavily\n이유: 일반동사 rained를 꾸미는 부사'),
    ('This bag is so {heavy|heavily} that she can\'t carry it.', '이 가방은 매우 무거워서 그녀는 그것을 들 수 없다.', '정답 ▶ heavy\n이유: be동사 is 뒤 보어 → 형용사'),
    ('The story was so funny {that|what} everyone laughed.', '그 이야기는 매우 웃겨서 모두가 웃었다.', '정답 ▶ that\n이유: so ~ that (what ✗)'),
    ("Her arms were so short that she {couldn't|can't} reach the shelf.", '그녀의 팔은 너무 짧아서 선반에 닿을 수 없었다.', "정답 ▶ couldn't\n이유: 앞이 과거(were) → that절도 과거"),
    ('The pizza tasted so {delicious|deliciously} that I ate it all.', '그 피자는 매우 맛있어서 나는 그것을 다 먹었다.', '정답 ▶ delicious\n이유: taste(~한 맛이 나다) 뒤에는 형용사'),
]))
D.step(MC('해석 · 우리말 고르기', [
    ('알맞은 해석은?' + Q('These centers are so popular that they are always full of people.'), ['이 센터들은 매우 인기 있어서 늘 사람들로 가득 차 있다.', '이 센터들은 늘 사람들로 가득 차 있어서 인기가 있다.', '이 센터들은 사람들로 가득 차 있지만 인기가 없다.', '이 센터들은 인기를 얻기 위해 늘 사람들을 채운다.'],
     '정답 ▶ 이 센터들은 매우 인기 있어서 늘 사람들로 가득 차 있다.\n이유: so popular(원인) → that they are always full of people(결과). 교과서 7과 본문 문장\n오답 ▶ 원인과 결과가 바뀜 / but 뜻 아님 / 목적(~하기 위해) 아님'),
    ('알맞은 해석은?' + Q("I was so tired that I couldn't do my homework."), ['나는 너무 피곤해서 숙제를 할 수 없었다.', '나는 숙제를 하지 못해서 피곤했다.', '나는 피곤했지만 숙제를 할 수 있었다.', '나는 숙제를 하기 위해 피곤했다.'],
     '정답 ▶ 나는 너무 피곤해서 숙제를 할 수 없었다.\n이유: so tired(원인) → that I couldn\'t do my homework(결과)'),
    ('우리말과 뜻이 같은 것은?<br><b>그 영화는 매우 무서워서 나는 잠을 잘 수 없었다.</b>', ["The movie was so scary that I couldn't sleep.", "The movie was very scary that I couldn't sleep.", "The movie was too scary that I can't sleep.", "The movie was scary enough that I couldn't sleep."],
     "정답 ▶ The movie was so scary that I couldn't sleep.\n오답 ▶ very ~ that ✗ / too ~ that ✗(+ 시제 can't ✗) / enough that ✗"),
    ('우리말과 뜻이 같은 것은?<br><b>날씨가 매우 좋아서 나는 개를 데리고 산책을 나갔다.</b>', ['The weather was so nice that I took a walk with my dog.', 'The weather was nice that I took a walk with my dog.', 'The weather is so nice that I take a walk with my dog.', 'The weather was very nice that I took a walk with my dog.'],
     '정답 ▶ The weather was so nice that I took a walk with my dog.\n오답 ▶ so가 빠짐 / 시제(현재) ✗ / very ~ that ✗'),
]))
D.sent("I was so tired that I couldn't do my homework.", '나는 너무 피곤해서 숙제를 할 수 없었다.'); D.sent("The movie was so scary that I couldn't sleep.", '그 영화는 매우 무서워서 나는 잠을 잘 수 없었다.')
D.sent('The weather was so nice that I took a walk with my dog.', '날씨가 매우 좋아서 나는 개를 데리고 산책을 나갔다.')
D.step(SCR(D, '우리말 → 영어 배열', [
    ('It is so big that it covers her shoulder.', '그것은 매우 커서 그녀의 어깨를 덮는다.'),
    ('These centers are so popular that they are always full of people.', '이 센터들은 매우 인기 있어서 늘 사람들로 가득 차 있다.'),
    ('The room was so cold that Sarah put on her jacket.', '그 방은 매우 추워서 Sarah는 재킷을 입었다.'),
    ('The music was so loud that Jane covered her ears.', '그 음악은 소리가 매우 커서 Jane은 귀를 가렸다.'),
]))
DAYS.append(D.done())

# ═════════ 문법 ② so ~ that ↔ too ~ to / enough to ═════════
D = Day('g2', '7과 문법 ② too ~ to · enough to로 바꾸기', "so ~ that 주어 can't = too ~ to / so ~ that 주어 can = ~ enough to")
D.note('개념 ① 바꿔 쓰기', [
    ("so ~ that + 주어 + can't(couldn't)", '= too + 형용사/부사 + to부정사 → 너무 ~해서 …할 수 없다'),
    ("He is so tired that he can't go camping.", '= He is too tired to go camping.'),
    ('so ~ that + 주어 + can(could)', '= 형용사/부사 + enough + to부정사 → …할 만큼 충분히 ~하다'),
    ('Bora is so clever that she can solve it.', '= Bora is clever enough to solve it.'),
])
D.note('개념 ② 바꿀 때 주의', [
    ('too ~ to에는 not이 없어요', "too 자체에 '~할 수 없다'는 뜻이 있어요. too busy not to eat ✗"),
    ('목적어 it', "The box was so heavy that I couldn't carry it. ↔ The box was too heavy (for me) to carry. (to 뒤에는 it ✗)"),
    ('의미상 주어 for + 목적격', 'that절 주어가 문장 주어와 다르면: The window is too high for Ann to reach.'),
    ('enough의 위치', '형용사 뒤: clever enough ✔ / enough clever ✗'),
])
D.step(MC('같은 뜻 고르기', [
    ('주어진 문장과 의미가 같은 것은?' + Q("I'm too nervous to sleep."), ["I'm so nervous that I can't sleep.", "I'm so nervous that I can sleep.", "I'm so nervous to sleep.", "I'm nervous enough to sleep."],
     "정답 ▶ I'm so nervous that I can't sleep.\n이유: too ~ to = so ~ that 주어 can't\n오답 ▶ can sleep(잘 수 있다 → 반대) / so ~ to ✗ / enough to(잘 수 있을 만큼 → 반대)"),
    ('주어진 문장과 의미가 같은 것은?' + Q('He was kind enough to show me the way.'), ['He was so kind that he could show me the way.', "He was so kind that he couldn't show me the way.", 'He was so kind that he can show me the way.', 'He was too kind to show me the way.'],
     '정답 ▶ He was so kind that he could show me the way.\n이유: enough to = so ~ that 주어 can(could). was(과거) → could\n오답 ▶ couldn\'t(반대) / can(시제 ✗) / too ~ to(반대)'),
    ('주어진 문장과 의미가 같은 것은?' + Q('The box was too heavy for me to move.'), ["The box was so heavy that I couldn't move it.", 'The box was so heavy that I could move it.', 'The box was so heavy for me to move.', 'The box was so heavy that I moved it.'],
     "정답 ▶ The box was so heavy that I couldn't move it.\n이유: for me → that절 주어 I, move의 목적어 it을 살려요."),
    ('주어진 문장과 의미가 같은 것은?' + Q('The woman is rich enough to travel around the world.'), ['The woman is so rich that she can travel around the world.', 'The woman is too rich to travel around the world.', "The woman is so rich that she can't travel around the world.", 'The woman is rich so that she could travel around the world.'],
     '정답 ▶ The woman is so rich that she can travel around the world.\n오답 ▶ too ~ to / can\'t는 반대 뜻 / so that(목적)은 다른 뜻'),
    ('주어진 문장과 의미가 같은 것은?' + Q('Sarang is 4 years old, so she cannot drive a car.'), ['Sarang is too young to drive a car.', 'Sarang is old enough to drive a car.', 'Sarang is so old that she cannot drive a car.', 'Sarang is so young that she can drive a car.'],
     '정답 ▶ Sarang is too young to drive a car.\n이유: 4살 → 너무 어려서 운전할 수 없다\n오답 ▶ old enough(운전할 만큼 나이 듦) / so old(너무 나이 들어서) / can drive(운전할 수 있다)'),
]))
D.sent("I'm too nervous to sleep.", '나는 너무 긴장해서 잘 수 없다.'); D.sent("I'm so nervous that I can't sleep.", '나는 너무 긴장해서 잘 수 없다.')
D.sent('He was kind enough to show me the way.', '그는 친절하게도 나에게 길을 알려 주었다.'); D.sent('The box was too heavy for me to move.', '그 상자는 너무 무거워서 나는 옮길 수 없었다.')
D.sent('Sarang is too young to drive a car.', '사랑이는 너무 어려서 차를 운전할 수 없다.')
D.step(MC('빈칸 짝 고르기', [
    ('두 문장이 같은 뜻이 되도록 빈칸에 알맞은 말은?<br><b>He is so tired that he can\'t go camping.<br>= He is ______ tired ______ go camping.</b>', ['too - to', 'enough - to', 'so - to', 'enough - that'],
     "정답 ▶ too - to\n이유: so ~ that 주어 can't = too ~ to"),
    ('두 문장이 같은 뜻이 되도록 빈칸에 알맞은 말은?<br><b>Bora is clever enough to solve this problem.<br>= Bora is ______ clever ______ she can solve this problem.</b>', ['so - that', 'too - that', 'too - to', 'so - to'],
     '정답 ▶ so - that\n이유: enough to = so ~ that 주어 can'),
    ('빈칸에 알맞은 말은?<br><b>He was ⓐ______ tired ⓑ______ he couldn\'t exercise anymore.</b>', ['so - that', 'too - to', 'so - to', 'too - that'],
     "정답 ▶ so - that\n이유: ⓑ 뒤에 he couldn't(주어 + 동사) → so ~ that"),
    ('빈칸에 알맞은 말은?<br><b>He was ⓐ______ small that he ⓑ______ lift the books.</b>', ["so - couldn't", "too - couldn't", 'so - can', 'too - could'],
     "정답 ▶ so - couldn't\n이유: ~ that → so / was(과거) → couldn't"),
    ('두 문장을 한 문장으로 바르게 이은 것은?<br><b>The coffee is very hot. + I can\'t drink it.</b>', ["The coffee is so hot that I can't drink it.", 'The coffee is too hot that I can\'t drink it.', "The coffee is such hot that I can't drink it.", 'The coffee is so hot that I can drink it.'],
     "정답 ▶ The coffee is so hot that I can't drink it.\n오답 ▶ too ~ that ✗ / such hot ✗ / can drink(반대)"),
]))
D.step(TF('바꿔 쓰기 맞을까? T/F', [
    ("I was so tired that I couldn't walk home. = I was too tired to walk home.", True, "정답 ▶ T\n이유: so ~ that 주어 couldn't = too ~ to"),
    ("She is so busy that she can't meet her boyfriend. = She is not too busy to meet her boyfriend.", False, "정답 ▶ F\n이유: not too busy to meet(만날 수 없을 만큼 바쁘지는 않다)는 반대 뜻 → She is too busy to meet her boyfriend."),
    ('He is so rich that he can buy the car. = He is rich enough to buy the car.', True, '정답 ▶ T\n이유: so ~ that 주어 can = enough to'),
    ("The window is so high that Ann can't reach it. = The window is too high for Ann to reach.", True, '정답 ▶ T\n이유: 주어가 다르면 for + 목적격(for Ann), to reach 뒤 it은 빼요.'),
    ('She worked hard enough to become a lawyer. = She worked so hard that she couldn\'t become a lawyer.', False, "정답 ▶ F\n이유: enough to = so ~ that 주어 could → couldn't는 반대 뜻"),
    ('This room is too small to have 7 people in it. = This room is so small that it can have 7 people in it.', False, "정답 ▶ F\n이유: too ~ to = so ~ that ~ can't → it can't have 7 people in it"),
]))
D.step(PICK(D, '어법 선택', [
    ("She was {too|so} busy to have lunch.", '그녀는 너무 바빠서 점심을 먹을 수 없었다.', '정답 ▶ too\n이유: 뒤에 to have → too ~ to'),
    ('He is tall {enough|too} to reach the top shelf.', '그는 맨 위 선반에 닿을 만큼 키가 크다.', '정답 ▶ enough\n이유: ~할 만큼 충분히 → 형용사 + enough + to'),
    ('This water is too dirty to {drink|drink it}.', '이 물은 너무 더러워서 마실 수 없다.', '정답 ▶ drink\n이유: 주어 This water가 drink의 목적어 → to 뒤에 it을 또 쓰지 않아요.'),
    ("This coffee was so hot that I couldn't {drink it|drink}.", '이 커피는 너무 뜨거워서 나는 그것을 마실 수 없었다.', "정답 ▶ drink it\n이유: that절은 완전한 문장 → drink의 목적어 it이 필요해요."),
    ('The pants are too small {for me|of me} to wear.', '그 바지는 너무 작아서 나는 입을 수 없다.', '정답 ▶ for me\n이유: to부정사의 의미상 주어 → for + 목적격'),
]))
DAYS.append(D.done())

# ═════════ 문법 ③ so ~ that 실전 ═════════
D = Day('g3', '7과 문법 ③ so ~ that 실전', 'so that(~하기 위해)과 구별 · such a ~ that · 영작 · 어법 · 의미가 다른 것')
D.note('개념 · 헷갈리는 짝', [
    ('so + 형용사/부사 + that', '매우 ~해서 …하다 (결과) → He studied so hard that he passed the exam.'),
    ('so that + 주어 + can', '~하기 위해 (목적, so와 that이 붙어 있음) → He studied hard so that he could pass the exam.'),
    ('such + a + 형용사 + 명사 + that', '= so ~ that: Kate is such a kind person that everybody likes her. = Kate is so kind that ~'),
    ('so a fast runner ✗', '명사가 있으면 such: such a fast runner'),
])
D.step(MC('우리말 → 영어', [
    ('우리말을 바르게 영작한 것은?<br><b>Tom은 너무 바빠서 점심도 먹지 못했다.</b>', ["Tom was so busy that he couldn't eat lunch.", 'Tom was too busy not to eat lunch.', "Tom is busy that he didn't eat lunch.", "Tom was so busy that he can't eat lunch."],
     "정답 ▶ Tom was so busy that he couldn't eat lunch.\n오답 ▶ too ~ not to ✗(too에 이미 부정 뜻) / so 빠짐 / 시제 can't ✗"),
    ('우리말을 바르게 영작한 것은?<br><b>그는 매우 열심히 공부해서 그 시험에 합격했다.</b>', ['He studied so hard that he could pass the exam.', 'He studied too hard to pass the exam.', 'He passed the exam so that he could study hard.', "He studied so hard that he couldn't pass the exam."],
     '정답 ▶ He studied so hard that he could pass the exam.\n오답 ▶ too ~ to(합격 못함) / so that(목적, 뜻이 바뀜) / couldn\'t(반대)'),
    ('우리말을 바르게 영작한 것은?<br><b>그 음식은 너무 뜨거워서 나는 먹을 수 없었다.</b>', ["The food was so hot that I couldn't eat it.", 'The food was so hot to eat it.', "The food was too hot that I couldn't eat.", "The food was too hot to I couldn't eat it."],
     "정답 ▶ The food was so hot that I couldn't eat it.\n오답 ▶ so ~ to ✗ / too ~ that ✗ / too ~ to + 문장 ✗"),
    ('우리말을 바르게 영작한 것은?<br><b>Jenny는 너무 어려서 운전을 할 수 없다.</b>', ['Jenny is too young to drive a car.', 'Jenny is so young to drive a car.', "Jenny is so young that I can't drive a car.", 'Jenny is very young to drive a car.'],
     '정답 ▶ Jenny is too young to drive a car.\n오답 ▶ so ~ to ✗ / I(주어가 바뀜) / very ~ to ✗'),
]))
D.sent("Tom was so busy that he couldn't eat lunch.", 'Tom은 너무 바빠서 점심도 먹지 못했다.'); D.sent('He studied so hard that he could pass the exam.', '그는 매우 열심히 공부해서 그 시험에 합격했다.')
D.sent("The food was so hot that I couldn't eat it.", '그 음식은 너무 뜨거워서 나는 먹을 수 없었다.'); D.sent('Jenny is too young to drive a car.', 'Jenny는 너무 어려서 운전을 할 수 없다.')
D.step(MC('어법상 옳은 문장 · 어색한 문장', [
    ('어법상 <b>옳은</b> 문장은?', ['The story was so funny that everyone laughed.', "I am too tired that I can't play soccer today.", 'The water in the river was too dirty to drink it.', 'I was so sick to go to school.'],
     '정답 ▶ The story was so funny that everyone laughed.\n오답 ▶ too ~ that → so ~ that / drink it → drink / so ~ to → too ~ to'),
    ('어법상 <b>어색한</b> 문장은?', ["The library is so noise that I can't concentrate.", 'The book was so boring that she fell asleep.', 'He was so tall that he could reach the tree.', "The desk was so heavy that she couldn't move it."],
     '정답 ▶ The library is so noise that I can\'t concentrate.\n이유: noise(명사) → noisy(형용사)'),
    ('어법상 <b>어색한</b> 문장은?', ['He ate so much that had a stomachache.', 'I was so tired that I fell asleep quickly.', 'Jiho is so funny that he always makes people laugh.', 'I ran so fast that I could catch up with her.'],
     '정답 ▶ He ate so much that had a stomachache.\n이유: that 뒤 주어 없음 → that he had a stomachache'),
    ('어법상 <b>옳은</b> 문장은?', ['The woman is so old that she can\'t swim.', "Kevin is too careful that he can't make mistakes.", 'Sally was so a fast runner that Paul couldn\'t catch her.', "Mom was so sad that she can't eat anything."],
     "정답 ▶ The woman is so old that she can't swim.\n오답 ▶ too ~ that → so ~ that / so a fast runner → such a fast runner / was ~ can't → couldn't"),
]))
D.step(MC('의미 · 용법이 다른 하나', [
    ('의미가 나머지 넷과 <b>다른</b> 것은?', ['She is so nervous that she can sleep.', 'She is too nervous to sleep.', "She is very nervous, so she can't sleep.", "She is so nervous that she can't sleep.", "Because she is very nervous, she can't sleep."],
     '정답 ▶ She is so nervous that she can sleep.\n이유: 이것만 "잘 수 있다", 나머지는 모두 "너무 긴장해서 잘 수 없다"'),
    ('의미가 나머지 넷과 <b>다른</b> 것은?', ["The car was expensive so that I couldn't buy it.", "The car was so expensive that I couldn't buy it.", "The car was very expensive, so I couldn't buy it.", 'The car was too expensive to buy.', "I couldn't buy the car because it was too expensive."],
     '정답 ▶ The car was expensive so that I couldn\'t buy it.\n이유: so that은 "~하기 위해"(목적) → 뜻이 이상해져요. 나머지는 "차가 너무 비싸서 살 수 없었다"'),
    ('밑줄 친 부분의 용법이 <b>다른</b> 것은?', ['He worked hard <u>so that</u> his family could live in comfort.', 'The boat rocked <u>so</u> much <u>that</u> I got sick.', "She was <u>so</u> young <u>that</u> she couldn't enter the contest.", "Jinho is <u>so</u> full <u>that</u> he can't eat anymore."],
     '정답 ▶ He worked hard <u>so that</u> his family could live in comfort.\n이유: so that = ~하기 위해(목적). 나머지는 so + 형용사/부사 + that(매우 ~해서)'),
]))
D.step(ERR(D, '오류 찾기', [
    ('It [[rained]] so [[heavy]] that [[they]] put off [[the game]].', 1, 'heavily', '비가 매우 많이 와서 그들은 경기를 연기했다.', '정답 ▶ heavy → heavily\n이유: 일반동사 rained를 꾸미는 부사'),
    ('I [[was]] so [[sick]] that I [[can\'t]] go to school [[yesterday]].', 2, "couldn't", '나는 어제 너무 아파서 학교에 갈 수 없었다.', "정답 ▶ can't → couldn't\n이유: was, yesterday → 과거"),
    ('She was [[too]] busy [[not]] to [[eat]] lunch [[today]].', 1, '', '그녀는 오늘 너무 바빠서 점심을 먹을 수 없었다.', '정답 ▶ not → 삭제\n이유: too ~ to에 이미 "~할 수 없다"는 뜻 → too busy to eat'),
    ('Kate is [[so]] a kind [[person]] that [[everybody]] [[likes]] her.', 0, 'such', 'Kate는 매우 친절한 사람이어서 모두가 그녀를 좋아한다.', '정답 ▶ so → such\n이유: 뒤에 a + 형용사 + 명사 → such a kind person that ~'),
]))
DAYS.append(D.done())

# ═════════ 문법 ④ 가주어 it 기본 ═════════
D = Day('g4', '7과 문법 ④ 가주어 it 기본', 'It is + 형용사 + to부정사 · 의미상 주어 for / of')
D.note('개념 ① 가주어 it', [
    ('To study hard is important.', '→ It is important to study hard. (열심히 공부하는 것은 중요하다)'),
    ('가주어 It', '긴 to부정사 주어를 뒤로 보내고 주어 자리에 It을 써요. 이 It은 해석하지 않아요.'),
    ('진주어', 'to부정사(구)가 진짜 주어 → "~하는 것은"으로 해석'),
    ('It is always good to get together.', '교과서 7과 · 함께 모이는 것은 언제나 좋아요.'),
    ('It is fun to enjoy the food with good people.', '교과서 7과 · 좋은 사람들과 음식을 즐기는 것은 재미있어요.'),
])
D.note('개념 ② 의미상 주어 for / of', [
    ('It is + 형용사 + for + 목적격 + to부정사', '대부분: It is important for you to get enough sleep.'),
    ('It is + 성격 형용사 + of + 목적격 + to부정사', 'kind, nice, wise, smart, foolish, careless, rude, polite, generous … : It was kind of you to help me.'),
    ('목적격', 'for her ✔ (for she ✗) / of him ✔ (of his ✗)'),
    ('부정', 'not + to부정사: It is important not to be late.'),
    ('It ✔ / That ✗', '가주어 자리에는 It만: That is necessary to ~ ✗'),
])
D.step(SCARDS(D, '해석 카드', [
    ('It is always good to get together.', '함께 모이는 것은 언제나 좋다. (교과서)'),
    ('It is fun to enjoy the food with good people.', '좋은 사람들과 음식을 즐기는 것은 재미있다. (교과서)'),
    ('It is difficult to learn to swim.', '수영을 배우는 것은 어렵다.'),
    ('It is exciting to go to a K-pop concert.', '케이팝 콘서트에 가는 것은 신난다.'),
    ('It is important to exercise regularly.', '규칙적으로 운동하는 것은 중요하다.'),
    ('It is important for you to get enough sleep.', '네가 충분히 잠을 자는 것은 중요하다.'),
    ('It was kind of you to help me.', '나를 도와주다니 너는 친절했다.'),
    ('It is safe to wear a life jacket on a boat.', '배 위에서 구명조끼를 입는 것이 안전하다.')],
    guide='It은 해석하지 않고, 뒤의 to부정사를 "~하는 것은"으로 해석해요.'))
D.step(TF('개념 확인 T/F', [
    ('It is important to study hard.에서 It은 "그것"으로 해석한다.', False, '정답 ▶ F\n이유: 가주어 It은 해석하지 않아요. "열심히 공부하는 것은 중요하다"'),
    ('To get up early is not easy. = It is not easy to get up early.', True, '정답 ▶ T\n이유: to부정사 주어를 뒤로 보내고 가주어 It'),
    ('It is kind for you to say so.는 바른 문장이다.', False, '정답 ▶ F\n이유: kind(성격 형용사) → of you: It is kind of you to say so.'),
    ('It is hard for she to find the building.은 바른 문장이다.', False, '정답 ▶ F\n이유: 전치사 for 뒤는 목적격 → for her'),
    ('It is important not to be late.에서 to부정사의 부정은 not to이다.', True, '정답 ▶ T\n이유: to부정사의 부정은 to 앞에 not'),
    ('That is necessary to wear safety gear.는 가주어 문장으로 바르다.', False, '정답 ▶ F\n이유: 가주어 자리에는 It → It is necessary to wear safety gear.'),
]))
D.step(PICK(D, '어법 선택', [
    ('Is it necessary {to buy|buy} a ticket now?', '지금 표를 사는 것이 필요한가요?', '정답 ▶ to buy\n이유: 진주어 → to부정사'),
    ('{It|That} is important to tell the truth.', '진실을 말하는 것은 중요하다.', '정답 ▶ It\n이유: 가주어 자리에는 It'),
    ('It is foolish {of|for} you to say so.', '그렇게 말하다니 너는 어리석다.', '정답 ▶ of\n이유: foolish(성격) → of + 목적격'),
    ("It's hard {for|of} you to climb the mountain.", '네가 그 산을 오르는 것은 힘들다.', '정답 ▶ for\n이유: hard는 성격 형용사가 아님 → for + 목적격'),
    ('It is impossible for {us|we} to fly in the sky.', '우리가 하늘을 나는 것은 불가능하다.', '정답 ▶ us\n이유: for 뒤 목적격'),
    ('It is {easy|easily} for her to open the window.', '그녀가 그 창문을 여는 것은 쉽다.', '정답 ▶ easy\n이유: be동사 뒤 보어 → 형용사'),
    ('It is good {to be|to} honest.', '정직한 것은 좋다.', '정답 ▶ to be\n이유: honest는 형용사 → to be honest (to honest ✗)'),
    ('It is important {not to bother|to not bother} a guide dog.', '안내견을 방해하지 않는 것이 중요하다.', '정답 ▶ not to bother\n이유: to부정사의 부정은 not to (교재 기준)'),
]))
D.step(MC('for / of 고르기', [
    ('빈칸에 들어갈 말이 나머지와 <b>다른</b> 것은?<br>① It was careless ___ me to tell you my secret.<br>② It is important ___ us to exercise regularly.<br>③ It was easy ___ them to carry the box.<br>④ It is difficult ___ me to read the book.', ['①', '②', '③', '④'],
     '정답 ▶ ①\n이유: careless(부주의한, 성격) → of / 나머지는 for', True),
    ('빈칸에 같은 말이 들어가는 것끼리 짝지은 것은?<br>ⓐ It was nice ___ you to see my son off.<br>ⓑ It is easy ___ us to understand his directions.<br>ⓒ It is impossible ___ him to do push-ups twenty times.<br>ⓓ It is very stupid ___ him to jump from this building.', ['ⓐ, ⓓ', 'ⓐ, ⓑ', 'ⓑ, ⓓ', 'ⓒ, ⓓ'],
     '정답 ▶ ⓐ, ⓓ\n이유: nice · stupid(성격) → of / ⓑ ⓒ → for', True),
    ('빈칸에 알맞은 것은?<br><b>It was very wise ______ you not to spend much money on that.</b>', ['of', 'for', 'to', 'by'],
     '정답 ▶ of\n이유: wise(현명한, 성격) → of + 목적격'),
    ('두 문장을 한 문장으로 바르게 바꾼 것은?<br><b>She was clever. + She guessed the answer.</b>', ['It was clever of her to guess the answer.', 'It was clever for her to guess the answer.', 'That was clever of her to guess the answer.', 'It was clever of her guess the answer.'],
     '정답 ▶ It was clever of her to guess the answer.\n오답 ▶ clever(성격) → of / That ✗ / to guess'),
]))
D.sent('It was very wise of you not to spend much money on that.', '그것에 돈을 많이 쓰지 않다니 너는 매우 현명했다.'); D.sent('It was clever of her to guess the answer.', '답을 맞히다니 그녀는 영리했다.')
D.step(SCR(D, '우리말 → 영어 배열', [
    ('It is always good to get together.', '함께 모이는 것은 언제나 좋다.'),
    ('It is fun to enjoy the food with good people.', '좋은 사람들과 음식을 즐기는 것은 재미있다.'),
    ('It is important for us to understand other cultures.', '우리가 다른 문화를 이해하는 것은 중요하다.'),
    ('It is difficult to get up early.', '일찍 일어나는 것은 어렵다.'),
]))
DAYS.append(D.done())

# ═════════ 문법 ⑤ it 구별 ═════════
ROLE = ['가주어 It (진짜 주어 = 뒤의 to부정사)', '비인칭 주어 It (날씨·시간·거리·명암)', '대명사 It (그것)', '강조 It ~ that']
def role(D, en, ko, ans, why, u='It'):
    D.sent(en, ko)
    opts = [ROLE[ans]] + [r for i, r in enumerate(ROLE) if i != ans]
    return ('밑줄 친 <i>It</i>의 쓰임은?' + Q(en, u), opts, '정답 ▶ %s\n이유: %s\n해석 ▶ %s' % (ROLE[ans], why, ko))
D = Day('g5', '7과 문법 ⑤ It 구별하기', '가주어 · 비인칭 주어 · 대명사 · 강조 It ~ that')
D.note('개념 · It은 네 가지', [
    ('가주어 It', 'It + be + 형용사/명사 + to부정사 → It is easy to swim. (수영하는 것은 쉽다)'),
    ('비인칭 주어 It', '날씨 · 시간 · 요일 · 거리 · 명암: It is cold. / It is 3 o\'clock. / It is two miles to the station. / It is getting dark.'),
    ('대명사 It', '앞에 나온 것을 가리키는 "그것": It is my seat. / It tastes sweet.'),
    ('강조 It ~ that', 'It was Tom that I met yesterday. (내가 어제 만난 사람은 바로 Tom이었다)'),
    ('교과서 7과', 'It is so big that it covers her shoulder. → 이 It은 앞에 나온 빵을 가리키는 대명사(그것), so ~ that 문장이에요.'),
])
D.step(MC('It의 쓰임 고르기', [
    role(D, 'It is always good to get together.', '함께 모이는 것은 언제나 좋다.', 0, '뒤에 to get together(진주어) → 가주어 (교과서 7과)'),
    role(D, 'It is so big that it covers her shoulder.', '그것은 매우 커서 그녀의 어깨를 덮는다.', 2, '앞에 나온 빵을 가리키는 "그것". 뒤의 that은 so ~ that이지 진주어가 아니에요. (교과서 7과)'),
    role(D, 'It is getting dark.', '날이 어두워지고 있다.', 1, '명암 → 비인칭 주어'),
    role(D, 'It is two miles to the station.', '역까지는 2마일이다.', 1, '거리 → 비인칭 주어 (to the station은 to부정사가 아니라 전치사 to)'),
    role(D, 'It was Tom that I met yesterday.', '내가 어제 만난 사람은 바로 Tom이었다.', 3, 'It was + 강조할 말(Tom) + that ~ → 강조 구문'),
    role(D, 'It is fun to enjoy the food with good people.', '좋은 사람들과 음식을 즐기는 것은 재미있다.', 0, '뒤에 to enjoy ~(진주어) → 가주어 (교과서 7과)'),
    role(D, 'It tastes very sweet.', '그것은 맛이 매우 달다.', 2, '어떤 음식을 가리키는 "그것" → 대명사'),
    role(D, 'It takes 3 hours to finish my homework.', '내 숙제를 끝내는 데 3시간이 걸린다.', 1, 'It takes + 시간 + to ~ = ~하는 데 시간이 걸리다 → 시간을 나타내는 비인칭 주어'),
]))
D.step(MC('<보기>와 쓰임이 같은 것', [
    ('밑줄 친 <i>It</i>의 쓰임이 <보기>와 같은 것은?<br><보기> <u>It</u> is not easy to learn Chinese.', [U('It is wonderful to win a soccer game.', 'It'), U('It is my seat.', 'It'), U('It was not so hot yesterday.', 'It'), U('It was in 2000 that I was born.', 'It'), U('It tastes very sweet.', 'It')],
     '정답 ▶ <u>It</u> is wonderful to win a soccer game.\n이유: <보기>와 같은 가주어 It\n오답 ▶ my seat · tastes sweet(대명사) / not so hot(비인칭, 날씨) / in 2000 that ~(강조)'),
    ('밑줄 친 <i>It</i>의 쓰임이 <보기>와 같은 것은?<br><보기> <u>It</u> is good to take a walk with my dog.', [U('It is important to keep promises.', 'It'), U('What time is it now?', 'it'), U('Is it your favorite book?', 'it'), U('How long does it take?', 'it'), U('It was yesterday that I saw her.', 'It')],
     '정답 ▶ <u>It</u> is important to keep promises.\n이유: 가주어 It\n오답 ▶ What time is it(시간, 비인칭) / your favorite book(대명사) / How long does it take(시간, 비인칭) / It was yesterday that(강조)'),
    ('밑줄 친 <i>It</i>의 쓰임이 <보기>와 같은 것은?<br><보기> <u>It</u> is dangerous to cross the street.', [U('It is easy for me to solve this problem.', 'It'), U("It is Yumi's favorite doll.", 'It'), U('It is sunny and windy today.', 'It'), U('It is far from here to Busan.', 'It')],
     '정답 ▶ <u>It</u> is easy for me to solve this problem.\n이유: 가주어 It (for me = 의미상 주어)\n오답 ▶ 대명사 / 날씨(비인칭) / 거리(비인칭)'),
]))
D.step(MC('쓰임이 다른 하나', [
    ('밑줄 친 <i>It</i>의 쓰임이 나머지 넷과 <b>다른</b> 것은?', [U('It takes 3 hours to finish my homework.', 'It'), U('It was impossible to answer the question.', 'It'), U('It is urgent to take him to the hospital.', 'It'), U('Is it fun to play soccer with your friends?', 'it'), U('Is it easy to get up early every day?', 'it')],
     '정답 ▶ <u>It</u> takes 3 hours to finish my homework.\n이유: 시간을 나타내는 비인칭 주어. 나머지는 가주어\n포인트 ▶ to부정사가 뒤에 있어도 It takes + 시간 + to ~는 비인칭!'),
    ('밑줄 친 <i>It</i>의 쓰임이 나머지 넷과 <b>다른</b> 것은?', [U("It's the best book I have read.", "It"), U("Isn't it easy to play the game?", 'it'), U('It will be fun to learn to play tennis.', 'It'), U("It's good to walk for an hour every day.", 'It'), U('I think that it is important to do homework.', 'it')],
     "정답 ▶ <u>It</u>'s the best book I have read.\n이유: 대명사(그것). 나머지는 가주어"),
    ('밑줄 친 <i>It</i>의 쓰임이 나머지 넷과 <b>다른</b> 것은?', [U('It rains heavily during the rainy season.', 'It'), U('It is great to use clean bathrooms.', 'It'), U('It is important to keep the school rules.', 'It'), U('It was so sad to hear the news.', 'It'), U('It is pleasant to visit you.', 'It')],
     '정답 ▶ <u>It</u> rains heavily during the rainy season.\n이유: 날씨 → 비인칭 주어. 나머지는 가주어'),
]))
DAYS.append(D.done())

# ═════════ 문법 ⑥ 가주어 it 실전 · 종합 ═════════
D = Day('g6', '7과 문법 ⑥ 가주어 it 실전 · 종합', '영작 · 배열 · 어법 · 개수 세기 · so ~ that과 가주어 섞어서')
D.note('시험 직전 체크리스트', [
    ('가주어', 'It + is + 형용사 + (for/of + 목적격) + to + 동사원형'),
    ('for / of', '성격 형용사(kind, nice, wise, foolish, careless, rude …) → of / 나머지 → for'),
    ('형태', 'to + 동사원형 (to playing ✗, to diligent ✗ → to be diligent) · It\'s(It is) ✔ / Its ✗'),
    ('so ~ that', 'so + 형용사/부사 + that + 주어 + 동사 · 시제 맞추기 · too ~ to에는 not ✗'),
])
D.step(MC('영작 · 배열', [
    ('우리말과 일치하도록 배열한 것은?<br><b>일찍 일어나는 것은 어렵다. (to, is, early, up, get, it, difficult)</b>', ['It is difficult to get up early.', 'It is early to get up difficult.', 'To get up is difficult it early.', 'It is get up to difficult early.'],
     '정답 ▶ It is difficult to get up early.\n이유: 가주어 It + is + difficult + 진주어 to get up early'),
    ('우리말을 바르게 영작한 것은?<br><b>우리가 다른 문화를 이해하는 것은 중요하다.</b>', ['It is important for us to understand other cultures.', 'It is important for us understand other cultures.', 'It is important we to understand other cultures.', 'It is important of us to understand other cultures.'],
     '정답 ▶ It is important for us to understand other cultures.\n오답 ▶ to 빠짐 / we to ✗ / important는 성격 형용사가 아님 → for'),
    ('우리말을 바르게 영작하지 <b>못한</b> 것은?<br><b>안전 장비를 착용하는 것은 필수적이다.</b>', ['That is necessary to wear safety gear.', 'Wearing safety gear is necessary.', 'To wear safety gear is necessary.', 'It is necessary to wear safety gear.'],
     '정답 ▶ That is necessary to wear safety gear.\n이유: 가주어 자리에는 That ✗ → It'),
    ('우리말을 바르게 영작한 것은?<br><b>나를 도와주다니 너는 정말 친절하구나.</b>', ['It is very kind of you to help me.', 'It is very kind for you to help me.', 'It is very kind of you help me.', 'That is very kind of you to help me.'],
     '정답 ▶ It is very kind of you to help me.\n오답 ▶ kind → of / to 빠짐 / That ✗'),
]))
D.sent('It is very kind of you to help me.', '나를 도와주다니 너는 정말 친절하구나.')
D.step(MC('어법상 옳은 문장', [
    ('어법상 <b>옳은</b> 문장은?', ['It is dangerous for you to swim in this lake.', 'It is kind for you to say so.', 'It is difficult for her to skating on the ice.', 'It is necessary for his to get some fresh air.'],
     '정답 ▶ It is dangerous for you to swim in this lake.\n오답 ▶ kind → of / to skating → to skate / his → him'),
    ('어법상 <b>옳은</b> 문장은?', ["It isn't easy to get a good grade in math.", 'It is important which drink plenty of water.', 'It is fun to playing soccer with friends.', 'Is that useful to learn English grammar?'],
     "정답 ▶ It isn't easy to get a good grade in math.\n오답 ▶ which → to / to playing → to play / Is that → Is it"),
    ('어법상 <b>어색한</b> 문장은?', ['It was rude for him to make a noise in the library.', 'It is exciting to travel around the world.', 'It is difficult for me to express my ideas clearly.', 'It is hard for foreigners to learn Korean.'],
     '정답 ▶ It was rude for him to make a noise in the library.\n이유: rude(무례한, 성격) → of him'),
]))
D.step(MC('개수 세기 · 짝짓기', [
    ('어법상 옳은 것끼리 짝지은 것은?<br>ⓐ Its very important to follow the rules.<br>ⓑ Isn\'t that difficult to learn to fly an airplane?<br>ⓒ It is kind of you to help the disabled.<br>ⓓ It is difficult by me to decide how to fix it.<br>ⓔ It is important to protect the environment.', ['ⓒ, ⓔ', 'ⓐ, ⓒ, ⓔ', 'ⓑ, ⓒ, ⓔ', 'ⓒ, ⓓ, ⓔ'],
     '정답 ▶ ⓒ, ⓔ\n틀린 것 ▶ ⓐ Its → It\'s / ⓑ that → it / ⓓ by me → for me', True),
    ('어법상 옳은 문장의 개수는?<br>ⓐ It was careless of her to break the dishes.<br>ⓑ It is very cruel for him to do such a thing.<br>ⓒ It was wise of you not to spend much money.<br>ⓓ It was impossible to arrive on time.<br>ⓔ It\'s very importantly for teachers to speak clearly.', ['3개', '1개', '2개', '4개', '5개'],
     '정답 ▶ 3개 (ⓐ, ⓒ, ⓓ)\n틀린 것 ▶ ⓑ cruel(성격) → of him / ⓔ importantly → important', True),
]))
D.step(MC('so ~ that + 가주어 섞어서', [
    ('교과서 7과 문장에 대한 설명으로 <b>틀린</b> 것은?<br>ⓐ It is always good to get together.<br>ⓑ It is so big that it covers her shoulder.<br>ⓒ These centers are so popular that they are always full of people.', ['ⓑ의 첫 번째 It은 가주어이다.', 'ⓐ의 It은 가주어이고 to get together가 진주어이다.', 'ⓑ는 "매우 커서 어깨를 덮는다"는 원인과 결과를 나타낸다.', 'ⓒ는 so popular가 원인, that절이 결과이다.'],
     '정답 ▶ ⓑ의 첫 번째 It은 가주어이다.\n이유: ⓑ의 It은 앞에 나온 빵을 가리키는 대명사(그것). 뒤의 that은 so ~ that 구문이에요.'),
    ('밑줄 친 to부정사의 쓰임이 <보기>와 같은 것은?<br><보기> It is impossible <u>to change</u> the decision.', ['It is not easy for me <u>to play</u> the clarinet.', 'They are glad <u>to make</u> the plan.', 'I have something <u>to drink</u>.', 'She studied hard <u>to pass</u> the exam.'],
     '정답 ▶ It is not easy for me <u>to play</u> the clarinet.\n이유: 진주어 → to부정사의 명사적 용법\n오답 ▶ 감정의 원인(부사적) / something을 꾸밈(형용사적) / 목적(부사적)'),
]))
D.step(ERR(D, '오류 찾기', [
    ('It is [[interesting]] [[for]] play [[with]] [[her]].', 1, 'to', '그녀와 노는 것은 재미있다.', '정답 ▶ for → to\n이유: 진주어 to부정사 → It is interesting to play with her.'),
    ('It is [[hard]] to [[diligent]] [[all]] the [[time]].', 1, 'be diligent', '항상 부지런한 것은 어렵다.', '정답 ▶ diligent → be diligent\n이유: to 뒤에는 동사원형 → to be diligent'),
    ('It [[was]] [[careless]] [[for]] you to lose [[your]] umbrella.', 2, 'of', '우산을 잃어버리다니 너는 부주의했다.', '정답 ▶ for → of\n이유: careless(성격) → of + 목적격'),
    ('The sandwiches [[were]] so [[delicious]] that they [[sell]] out in [[one]] hour.', 2, 'sold', '샌드위치가 매우 맛있어서 한 시간 만에 다 팔렸다.', '정답 ▶ sell → sold\n이유: 앞이 과거(were) → that절도 과거 sold out(다 팔렸다)'),
]))
DAYS.append(D.done())

for d in DAYS: ansfirst(d['steps'])
path = '/home/claude/proj/data/m2-visang-hwang-L7.js'
PK = json.loads(subprocess.check_output(['node', '-e', "global.window={};require('%s');process.stdout.write(JSON.stringify(window.PKG))" % path]))
base = [d for d in PK['days'] if not re.match(r'g\d', d['id'])]
at = [d['id'] for d in base].index('d2') + 1
PK['days'] = base[:at] + DAYS + base[at:]
for i, d in enumerate(PK['days']): d['name'] = 'DAY %d' % (i + 1)
src = open(path, encoding='utf-8').read(); head = src[:src.index('window.PKG')]
if '7과 문법' not in head: head = head.rstrip('\n') + '\n/* 11/1: 7과 본문 뒤 DAY 5~10 = 7과 문법 so ~ that · 가주어 it (gen/gen_v7gram.py) */\n'
write(PK, path, head)
print('ok', [(d['name'], d['id'], d['range'], len(d['steps']), sum(len(s['items']) for s in d['steps'])) for d in PK['days']])
