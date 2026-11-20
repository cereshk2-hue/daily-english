# 11/20 심학중1 천재(소영순) 4과 실전 문법 CS — 동명사 1~4차 (각 20문항, 1차 기본 · 2차 중 · 3차 중상 · 4차 상)
# 원본: 선생님 학습지 동명사(1)·(1-1)·(2)·(2-1).hwp → work_src/m1cto/*.txt + 4과 본문(We enjoyed walking in the garden. / Seeing the blue ocean ... was fantastic!)
# 범위: 동명사 주어(단수)·목적어·보어·전치사의 목적어, 동명사만/to부정사만/둘 다 목적어로 쓰는 동사, 동명사 vs 현재분사, not + -ing, go -ing · How about -ing · look forward to -ing · feel like -ing, remember/forget/stop + -ing / to(3·4차)
# 뺀 것(선생님): 동명사의 의미상 주어. 논쟁 피함: try -ing/to, need -ing, be used to, go to swim처럼 둘 다 되는 표현은 오답으로 안 씀
import sys; sys.path.insert(0, '/home/claude/srcrepo/wrapup')
from wu_m1cg import *
H = ('실전 문법', '중1 영어 천재(소영순) 4과 동명사', '천재(소영순) 4과 동명사 CS', 'm1cg')
B = lambda *ls: BOX('<br>'.join(ls))
NUMS = ['1개', '2개', '3개', '4개', '5개']
t = lambda x: x.replace('[', '<u>').replace(']', '</u>')
R_, V_, K_, I_, L_ = '동명사 역할', '목적어 동사', '쓰임 구별', '관용 표현', '4과 본문'
NOTE = '범위: 동명사(동사원형 + -ing) — 주어 · 목적어 · 보어 · 전치사의 목적어, 동명사 / to부정사를 목적어로 쓰는 동사, 동명사와 현재분사 구별, 동명사 관용 표현.'

# ═══════════════ 1차 (기본) ═══════════════
T = Test('1', '1차', '동명사의 역할과 목적어', '동명사', NOTE, H=H); T.rot0 = 0
T.flex('다음 빈칸에 들어갈 말로 알맞은 것은?', R_, B(BL + ' an English diary is a good study method.'),
 ['Keeping', 'Keep', 'Kept', 'Keeps', 'To keeping'],
 "이유 ▶ 문장의 주어 자리 → 동명사 Keeping(일기를 쓰는 것은).\n오답 ▶ {1}·{2}·{3} 동사로 시작하면 주어가 없음 {4} to 뒤에 -ing ❌\n포인트 ▶ 동명사 주어 = ~하는 것은", [('method', '방법')])
T.flex('다음 빈칸에 들어갈 말로 알맞은 것은?', R_, B('What is your reason for ' + BL + ' late?'),
 ['being', 'be', 'is', 'are', 'to be'],
 "이유 ▶ 전치사 for 뒤 → 동명사 being. 늦은 이유가 뭐니?\n오답 ▶ {1}·{2}·{3} 전치사 뒤에 동사원형·be동사 ❌ {4} 전치사 뒤에 to부정사 ❌\n포인트 ▶ 전치사 + 동명사", [('reason', '이유')])
T.flex('다음 빈칸에 들어갈 말로 알맞은 것은?', V_, B('She enjoys ' + BL + ' tennis.'),
 ['playing', 'play', 'to play', 'played', 'plays'],
 "이유 ▶ enjoy는 동명사만 목적어로 → playing.\n오답 ▶ {1}·{3}·{4} 동사가 이미 있음 {2} enjoy + to부정사 ❌\n포인트 ▶ enjoy · finish · mind · give up · keep + -ing", [])
T.flex('다음 우리말을 영어로 바르게 옮긴 것은?', R_, B('일찍 일어나는 것은 건강에 좋다.'),
 ['Getting up early is good for your health.', 'Get up early is good for your health.', 'Getting up early are good for your health.', 'Got up early is good for your health.', 'To getting up early is good for your health.'],
 "이유 ▶ 동명사 주어 Getting up early + 단수 동사 is.\n오답 ▶ {1}·{3} 동사로 시작 ❌ {2} 동명사 주어는 단수 → is {4} to 뒤에 -ing ❌\n포인트 ▶ 동명사 주어는 단수 취급", [])
T.flex('다음 빈칸에 들어갈 말로 알맞은 것은?', R_, B('My job is ' + BL + ' English.'),
 ['teaching', 'teach', 'teaches', 'taught', 'to teaching'],
 "이유 ▶ be동사 뒤 보어 → 동명사 teaching(가르치는 것). 내 직업은 영어를 가르치는 것이다.\n오답 ▶ {1}·{2}·{3} is 뒤에 동사를 또 쓸 수 없음 {4} to 뒤에 -ing ❌\n포인트 ▶ 주어 + be동사 + 동명사 = ~하는 것이다", [])
T.flex('다음 빈칸에 들어갈 말로 알맞은 것은?', R_, B('Thank you for ' + BL + ' me this present.'),
 ['giving', 'give', 'gave', 'to give', 'gives'],
 "이유 ▶ 전치사 for 뒤 → giving. 이 선물을 주셔서 감사합니다.\n오답 ▶ {1}·{2}·{4} 전치사 뒤에 동사 ❌ {3} 전치사 뒤에 to부정사 ❌\n포인트 ▶ Thank you for + -ing", [])
T.flex('다음 빈칸에 들어갈 말로 알맞지 <u>않은</u> 것은?', V_, B('I ' + BL + ' watching horror movies.'),
 ['want', 'enjoy', 'mind', 'dislike', 'avoid'],
 "이유 ▶ want는 to부정사만 목적어로 → want to watch.\n오답 ▶ {1}·{2}·{3}·{4} 동명사를 목적어로 쓰는 동사 ✔\n포인트 ▶ want · hope · plan · decide + to부정사", [('avoid', '피하다'), ('horror movie', '공포 영화')])
T.flex('다음 중 어법상 <u>틀린</u> 것은?', R_, '',
 ['My hobby is read comic books.', 'Did you finish doing the dishes?', "I'm interested in reading poems.", 'Speaking in English is stressful to me.', 'He likes playing computer games.'],
 "이유 ▶ be동사 뒤 보어 → reading(읽는 것). is 뒤에 동사원형 read ❌\n오답 ▶ {1} finish + -ing {2} 전치사 in + -ing {3} 동명사 주어 + is {4} like + -ing ✔\n포인트 ▶ is 뒤에 동사가 오면 -ing나 to부정사로", [('poem', '시')])
T.flex('다음 빈칸에 들어갈 말로 알맞은 것은?', R_, B('Teaching young kids ' + BL + ' hard for me.'),
 ['is', 'be', 'are', 'were', 'being'],
 "이유 ▶ 주어 Teaching young kids(동명사구)는 단수 → is. (kids를 보고 are를 쓰면 ❌)\n오답 ▶ {1} 동사원형 {2}·{3} 복수 동사 {4} 동사가 없음\n포인트 ▶ 동명사 주어 = 단수", [])
T.flex('다음 빈칸에 들어갈 말로 알맞은 것은?', I_, B('How about ' + BL + ' shopping with me?'),
 ['going', 'go', 'to go', 'went', 'goes'],
 "이유 ▶ How about + -ing = ~하는 게 어때? → going. 나와 쇼핑 가는 것이 어때?\n오답 ▶ {1}·{3}·{4} about은 전치사라 동사 ❌ {2} to부정사 ❌\n포인트 ▶ How about / What about + -ing", [])
T.flex('다음 글의 빈칸에 들어갈 말로 알맞은 것은?', L_, B('We went to Damyang and visited Jungnogwon, a famous bamboo garden. We enjoyed ' + BL + ' in the garden.'),
 ['walking', 'walk', 'to walk', 'walked', 'walks'],
 "이유 ▶ enjoy + 동명사 → walking. 우리는 정원에서 걷는 것을 즐겼다. (교과서)\n오답 ▶ {1}·{3}·{4} 동사를 또 쓸 수 없음 {2} enjoy + to부정사 ❌\n포인트 ▶ enjoy + -ing", [('bamboo', '대나무')])
T.flex('다음 빈칸에 들어갈 말로 알맞은 것은?', V_, B('The children wanted ' + BL + ' baseball in the park.'),
 ['to play', 'play', 'playing', 'to plays', 'to playing'],
 "이유 ▶ want는 to부정사만 목적어로 → to play.\n오답 ▶ {1} 동사원형 ❌ {2} want + -ing ❌ {3}·{4} to 뒤는 동사원형\n포인트 ▶ want + to부정사 / enjoy + 동명사", [])
T.flex('다음 밑줄 친 부분과 바꾸어 쓸 수 있는 것은?', V_, B(t('I like [to swim] in the sea.')),
 ['swimming', 'swim', 'swam', 'to swam', 'to swimming'],
 "이유 ▶ like는 to부정사 · 동명사 둘 다 목적어로 (뜻 같음) → swimming.\n오답 ▶ {1}·{2} 동사 ❌ {3}·{4} to 뒤는 동사원형\n포인트 ▶ like · love · hate · start · begin · continue + to V / -ing", [])
T.flex('다음 중 어법상 <u>틀린</u> 것은?', V_, '',
 ['We enjoyed to have you here with us.', 'My grandfather likes taking naps.', 'Would you mind doing the dishes?', "I'm excited about starting yoga.", 'Swimming is an important survival skill.'],
 "이유 ▶ enjoy + 동명사 → enjoyed having.\n오답 ▶ {1} like + -ing {2} mind + -ing {3} 전치사 about + -ing {4} 동명사 주어 + is ✔\n포인트 ▶ enjoy 뒤 to부정사 ❌", [('take a nap', '낮잠을 자다'), ('survival', '생존')])
T.flex('다음 빈칸에 공통으로 들어갈 말로 알맞은 것은?', R_, B('• She is good at ' + BL + '.', '• Do you enjoy ' + BL + '?'),
 ['singing', 'sing', 'to sing', 'sang', 'sings'],
 "이유 ▶ 전치사 at 뒤 / enjoy 뒤 → 둘 다 동명사 singing.\n오답 ▶ {1}·{3}·{4} 동사 ❌ {2} at · enjoy 뒤 to부정사 ❌\n포인트 ▶ be good at + -ing = ~을 잘하다", [])
T.flex('<보기>의 밑줄 친 동명사와 쓰임(역할)이 같은 것은?', R_, B(t('<보기> [Recycling] paper is a good idea.')),
 [t('[Riding] a bicycle is fun.'), t('I love [studying] wild flowers.'), t('Her job is [selling] flowers.'), t("I'm sorry for [being] late."), t('She kept [crying] all day.')],
 "이유 ▶ <보기>와 정답 모두 문장의 주어(~하는 것은).\n오답 ▶ {1}·{4} 동사의 목적어 {2} 보어 {3} 전치사의 목적어\n포인트 ▶ 동사 앞 = 주어 / 동사 뒤 = 목적어 / be동사 뒤 = 보어", [('recycle', '재활용하다')])
T.flex('다음 글의 빈칸에 들어갈 말로 알맞은 것은?', L_, B('We visited Tongyeong and went up the mountain by cable car. Seeing the blue ocean and the green islands ' + BL + ' fantastic!'),
 ['was', 'were', 'are', 'be', 'being'],
 "이유 ▶ 주어는 Seeing ~(동명사구) → 단수, 과거 → was. (islands를 보고 were ❌) (교과서)\n오답 ▶ {1}·{2} 복수 동사 {3} 동사원형 {4} 동사 없음\n포인트 ▶ 동명사 주어는 뒤가 길어도 단수", [('fantastic', '환상적인')])
T.flex('우리말에 맞게 주어진 단어를 바르게 배열한 것은?', V_, B('그는 그 이야기책을 읽는 것을 마쳤다.', '( the storybook / finished / he / reading )'),
 ['He finished reading the storybook.', 'He reading finished the storybook.', 'He finished the storybook reading.', 'Reading he finished the storybook.', 'He the storybook finished reading.'],
 "이유 ▶ 주어 He + finished + reading(목적어) + the storybook.\n오답 ▶ {1}~{4} 어순 ❌\n포인트 ▶ finish + -ing + 목적어", [])
T.flex('다음 빈칸에 들어갈 말이 바르게 짝지어진 것은?', V_, B('• We decided ' + BL + ' to the beach.', "• I don't mind " + BL + ' the door.'),
 ['to go − opening', 'going − opening', 'to go − to open', 'going − to open', 'go − open'],
 "이유 ▶ decide + to부정사 → to go / mind + 동명사 → opening\n오답 ▶ decide + -ing ❌, mind + to부정사 ❌, 동사원형 ❌\n포인트 ▶ decide(to V) vs mind(-ing)", [])
T.flex('다음 중 어법상 알맞은 것은?', R_, '',
 ['She is interested in learning foreign languages.', 'Send email is easier than writing letters.', 'I often enjoy listen to classical music.', 'Spielberg is good at to create fun characters.', 'I want being a doctor someday.'],
 "이유 ▶ 전치사 in + learning ✔\n오답 ▶ {1} 주어 → Sending {2} enjoy listening {3} 전치사 at + creating {4} want to be\n포인트 ▶ 전치사 뒤 = 동명사", [('foreign', '외국의')])
T.render()

# ═══════════════ 2차 (중) ═══════════════
T = Test('2', '2차', '동명사 · to부정사 목적어 구별', '동명사', NOTE, H=H); T.rot0 = 3
T.flex('다음 밑줄 친 부분의 쓰임이 나머지 넷과 <u>다른</u> 것은?', K_, '',
 [t("I'm [e-mailing] my e-pals these days."), t('She has practiced [swimming] a lot.'), t('I love [listening] to music.'), t('Sora enjoys [spending] time with her parents.'), t('She likes [reading] books.')],
 "이유 ▶ am e-mailing = be + -ing → 진행형(~하는 중이다, 현재분사).\n오답 ▶ {1}~{4} 동사의 목적어로 쓰인 동명사(~하는 것을)\n포인트 ▶ be + -ing = 진행 / 일반동사 + -ing = 동명사 목적어", [])
T.flex('다음 빈칸에 들어갈 말로 알맞지 <u>않은</u> 것은?', V_, B('Julie ' + BL + ' reading books.'),
 ['wanted', 'began', 'loved', 'liked', 'hated'],
 "이유 ▶ want는 to부정사만 → wanted to read.\n오답 ▶ {1}~{4} begin · love · like · hate는 동명사 · to부정사 둘 다 ✔\n포인트 ▶ want + -ing ❌", [])
T.flex("다음 빈칸에 들어갈 수 <u>없는</u> 것은?", R_, B("I'm afraid of " + BL + '.'),
 ['go there at night', 'dogs', 'them', 'meeting him alone', 'sleeping tigers'],
 "이유 ▶ 전치사 of 뒤에는 명사 · 대명사 · 동명사 → go(동사원형) ❌ (going there at night 이면 ✔)\n오답 ▶ {1} 명사 {2} 대명사 목적격 {3} 동명사 {4} 명사(자고 있는 호랑이)\n포인트 ▶ 전치사 뒤에 동사원형 ❌", [('be afraid of', '~을 두려워하다')])
T.flex('다음 중 어법상 <u>어색한</u> 것은?', V_, '',
 ['He gave up to climb a tree.', 'I started exercising.', 'Mary likes talking with me.', 'They continue to study English.', 'She practices playing tennis.'],
 "이유 ▶ give up은 동명사만 → gave up climbing.\n오답 ▶ {1} start + -ing {2} like + -ing {3} continue + to V {4} practice + -ing ✔\n포인트 ▶ give up · practice · finish + -ing", [])
T.flex('(A), (B)에 들어갈 말이 바르게 짝지어진 것은?', V_, B('• Do you mind (A) ' + BL + ' the air conditioner?', '• They decided (B) ' + BL + ' a flea market to sell old things.'),
 ['turning on − to open', 'to turn on − opening', 'turning on − opening', 'to turn on − to open', 'to turning on − to opening'],
 "이유 ▶ (A) mind + 동명사 → turning on (B) decide + to부정사 → to open\n오답 ▶ mind + to부정사 ❌ / decide + -ing ❌ / to 뒤 -ing ❌\n포인트 ▶ Do you mind -ing? = ~해 주시겠어요?", [('flea market', '벼룩시장')])
T.flex('다음 중 어법상 올바른 것은?', V_, '',
 ['Sally began learning English literature.', 'She kept to exercise every morning.', 'Mike promised coming back again someday.', 'He hoped graduating from the university.', 'Jane finished to write her composition.'],
 "이유 ▶ begin은 둘 다 가능 → began learning ✔\n오답 ▶ {1} keep → exercising {2} promise → to come {3} hope → to graduate {4} finish → writing\n포인트 ▶ keep · finish(-ing) / promise · hope(to V)", [('literature', '문학'), ('composition', '작문')])
T.flex('다음 빈칸에 들어갈 말이 순서대로 바르게 짝지어진 것은?', V_, B('• We expected ' + BL + ' to a rock concert.', '• Susan enjoys ' + BL + ' care of animals.'),
 ['to go − taking', 'go − take', 'to go − to take', 'going − taking', 'going − to take'],
 "이유 ▶ expect + to부정사 → to go / enjoy + 동명사 → taking\n오답 ▶ 동사원형 ❌ / expect + -ing ❌ / enjoy + to부정사 ❌\n포인트 ▶ take care of = ~을 돌보다", [('expect', '기대하다')])
T.flex('다음 우리말을 영어로 바르게 옮긴 것은?', R_, B('늦어서 미안해.'),
 ["I'm sorry for being late.", "I'm sorry for be late.", "I'm sorry for to be late.", "I'm sorry being for late.", "I'm sorry for am late."],
 "이유 ▶ 전치사 for + 동명사 being.\n오답 ▶ {1} 동사원형 {2} 전치사 + to부정사 {3} 어순 {4} be동사 ❌\n포인트 ▶ be sorry for + -ing", [])
T.fixed('다음 글의 밑줄 친 ①~⑤ 중 동사의 형태가 바르지 <u>않은</u> 것은?', V_, B('Mina likes ① ' + U('cooking') + ' food. She often ② ' + U('visits') + " children's homes. She loves to ③ " + U('playing') + ' with the children. She also ④ ' + U('makes') + ' a nice meal for them. Her dream is to ⑤ ' + U('be') + ' a great cook.'),
 None, 3,
 "이유 ▶ to 뒤는 동사원형 → loves to play (또는 loves playing)\n오답 ▶ ① like + -ing ② 주어 She → visits ④ 주어 She → makes ⑤ to + 동사원형 be ✔\n포인트 ▶ to + -ing ❌", [('meal', '식사')])
T.flex('다음 빈칸에 들어갈 말로 알맞은 것은?', V_, B('Keep ' + BL + ' on this street, and you will get to the subway station.'),
 ['going', 'go', 'to go', 'went', 'goes'],
 "이유 ▶ keep + 동명사 = 계속 ~하다 → Keep going. 이 길로 계속 가면 지하철역이 나올 거예요.\n오답 ▶ {1}·{3}·{4} keep 뒤에 동사 ❌ {2} keep + to부정사 ❌\n포인트 ▶ keep (on) -ing", [])
T.flex('다음 빈칸에 들어갈 말이 순서대로 바르게 짝지어진 것은?', I_, B('• The noise kept me from ' + BL + '.', '• He spends much time ' + BL + ' with his family.'),
 ['sleeping − talking', 'sleep − talk', 'sleeping − talk', 'sleep − talking', 'slept − talked'],
 "이유 ▶ 전치사 from + sleeping / spend + 시간 + -ing → talking\n오답 ▶ 전치사 뒤 동사원형 ❌, spend 시간 뒤 동사원형 ❌\n포인트 ▶ spend + 시간 + -ing = ~하는 데 시간을 보내다", [('noise', '소음')])
T.flex('다음 빈칸에 들어갈 수 <u>없는</u> 것은?', V_, B('The couple ' + BL + ' to rent a house with a swimming pool.'),
 ['gave up', 'wanted', 'planned', 'agreed', 'hoped'],
 "이유 ▶ give up은 동명사만 → gave up renting. 빈칸 뒤 to rent와 맞지 않음.\n오답 ▶ {1}~{4} want · plan · agree · hope + to부정사 ✔\n포인트 ▶ 빈칸 뒤 to V → to부정사를 쓰는 동사만", [('rent', '빌리다')])
T.flex('다음 밑줄 친 동명사의 쓰임이 같은 것끼리 묶인 것은?', R_, B(t('Ⓐ People began [leaving] the movie theater.'), t('Ⓑ [Reading] gives me great happiness.'), t('Ⓒ Have you finished [typing] that letter?'), t('Ⓓ My dream is [taking] a trip around the world.')),
 ['Ⓐ, Ⓒ', 'Ⓐ, Ⓑ', 'Ⓑ, Ⓒ', 'Ⓒ, Ⓓ', 'Ⓑ, Ⓓ'],
 "이유 ▶ Ⓐ began의 목적어 · Ⓒ finished의 목적어 → 둘 다 동사의 목적어\n오답 ▶ Ⓑ 주어 / Ⓓ 보어\n포인트 ▶ 동명사 자리로 역할 구별", [('happiness', '행복')])
T.fixed('다음 문장의 밑줄 친 ①~⑤ 중 어법상 <u>틀린</u> 것은?', R_, B('① ' + U('Playing') + ' soccer ② ' + U('are') + ' fun, so ③ ' + U('I enjoy') + ' ④ ' + U('playing') + ' soccer every ⑤ ' + U('week') + '.'),
 None, 2,
 "이유 ▶ 주어 Playing soccer는 단수 → is fun (soccer를 보고 are ❌)\n오답 ▶ ① 동명사 주어 ③ 주어 + 동사 ④ enjoy + -ing ⑤ every + 단수 명사 ✔\n포인트 ▶ 동명사 주어 = 단수", [])
T.flex('다음 대화의 빈칸에 공통으로 들어갈 말은?', V_, B('A: How about ' + BL + ' the movie tonight?', "B: I'd love to, but I don't like " + BL + ' horror movies.'),
 ['watching', 'watch', 'watched', 'to watch', 'being watch'],
 "이유 ▶ How about + 동명사 / like + 동명사(to부정사도 가능) → 둘 다 되는 것은 watching.\n오답 ▶ {1}·{2} 동사 ❌ {3} How about 뒤 to부정사 ❌ {4} 형태 ❌\n포인트 ▶ '공통'은 두 빈칸에 모두 맞아야 함", [])
T.flex('<보기>의 밑줄 친 부분과 쓰임이 같은 것은?', K_, B(t('<보기> We enjoyed [walking] in the garden.')),
 [t('My daughter enjoys [helping] me.'), t('[Playing] board games is fun.'), t('Minsu is [swimming] in the pool.'), t("My brother's dream is [going] abroad."), t('[Sitting] down all day is not good for you.')],
 "이유 ▶ <보기>와 정답 모두 enjoy의 목적어(~하는 것을).\n오답 ▶ {1}·{4} 주어 {2} 진행형(현재분사) {3} 보어\n포인트 ▶ 같은 동명사라도 자리에 따라 역할이 다름", [('abroad', '해외로')])
T.flex('다음 중 어법상 <u>틀린</u> 문장을 모두 고른 것은?', V_, B('Ⓐ He wished to buy a new computer.', 'Ⓑ Mom finished to cook Chinese food.', 'Ⓒ She expects leaving tomorrow morning.', 'Ⓓ Jack stopped eating and went to bed.'),
 ['Ⓑ, Ⓒ', 'Ⓐ, Ⓑ', 'Ⓐ, Ⓒ', 'Ⓑ, Ⓒ, Ⓓ', 'Ⓐ, Ⓑ, Ⓒ'],
 "이유 ▶ Ⓑ finish → cooking Ⓒ expect → to leave\n오답 ▶ Ⓐ wish + to V ✔ Ⓓ stop + -ing(먹는 것을 멈추다) ✔\n포인트 ▶ finish(-ing) · expect(to V)", [])
T.flex('다음 빈칸에 들어갈 말이 순서대로 바르게 짝지어진 것은?', V_, B('• We enjoy ' + BL + ' to classical music.', '• He practiced ' + BL + ' English words.', '• She promised ' + BL + ' her best.'),
 ['listening − pronouncing − to do', 'to listen − pronounce − to do', 'listening − to pronounce − doing', 'to listen − pronouncing − doing', 'listening − pronouncing − doing'],
 "이유 ▶ enjoy + -ing / practice + -ing / promise + to V\n오답 ▶ enjoy · practice 뒤 to부정사 ❌, promise 뒤 -ing ❌\n포인트 ▶ 동사마다 뒤에 오는 형태를 외우기", [('pronounce', '발음하다'), ('promise', '약속하다')])
T.flex('두 문장의 의미가 같도록 할 때 빈칸에 알맞은 것은?', R_, B('It is not easy to practice the violin.', '= ' + BL + ' is not easy.'),
 ['Practicing the violin', 'Practice the violin', 'Practiced the violin', 'To practicing the violin', 'The violin practicing'],
 "이유 ▶ 동명사 주어 Practicing the violin = 바이올린을 연습하는 것은\n오답 ▶ {1}·{2} 동사로 시작 ❌ {3} to 뒤 -ing ❌ {4} 어순 ❌\n포인트 ▶ It is ~ to V = 동명사(-ing) 주어 + is ~", [])
T.flex("다음 중 빈칸에 'singing(Singing)'이 들어갈 수 <u>없는</u> 것은?", R_, '',
 ['I ' + BL + ' a song.', 'I like ' + BL + '.', "I'm good at " + BL + '.', 'Do you enjoy ' + BL + '?', BL + ' is exciting.'],
 "이유 ▶ 주어 I 뒤에는 동사가 필요 → I sing a song.\n오답 ▶ {1} like의 목적어 {2} 전치사 at의 목적어 {3} enjoy의 목적어 {4} 주어 ✔\n포인트 ▶ 동명사는 동사 자리에 못 옴", [])
T.render()

# ═══════════════ 3차 (중상) ═══════════════
T = Test('3', '3차', '동명사와 현재분사 · 관용 표현', '동명사', NOTE, H=H); T.rot0 = 4
T.flex('다음 밑줄 친 부분과 쓰임이 <u>다른</u> 것은?', K_, B(t('[Using] shadow puppets is a very old storytelling tradition.')),
 [t('I saw him [running] on the playground.'), t('The baby began [crying].'), t('[Writing] letters is my hobby.'), t('His dream is [teaching] English.'), t('Would you mind [opening] the window?')],
 "이유 ▶ saw him running = 그가 달리고 있는 것을 보았다 → 현재분사(~하고 있는).\n오답 ▶ {1}·{4} 목적어 {2} 주어 {3} 보어 → 모두 동명사\n포인트 ▶ '~하는 것'으로 해석되면 동명사", [('tradition', '전통')])
T.flex('다음 밑줄 친 부분의 쓰임이 나머지 넷과 <u>다른</u> 것은?', K_, '',
 [t('He was good at [playing] baseball.'), t('Look at the girl [singing] in the rain.'), t('She took care of the [crying] baby.'), t('The girl [playing] the piano is my sister.'), t('She was [walking] with a dog.')],
 "이유 ▶ 전치사 at의 목적어 → 동명사(야구하는 것).\n오답 ▶ {1}·{3} 명사를 꾸미는 현재분사 {2} 울고 있는 아기 {4} 진행형\n포인트 ▶ 전치사 뒤 -ing = 동명사", [])
T.flex('다음 중 어법상 <u>어색한</u> 것은?', I_, '',
 ['I feel like to eat pizza.', "I'm looking forward to seeing you again.", 'He is busy doing his homework.', 'Thank you for not telling this to anyone.', 'My dad went fishing yesterday.'],
 "이유 ▶ feel like + 동명사 = ~하고 싶다 → feel like eating.\n오답 ▶ {1} look forward to + -ing(to는 전치사) {2} be busy + -ing {3} not + -ing {4} go + -ing ✔\n포인트 ▶ feel like · be busy · go + -ing", [('look forward to', '~을 고대하다')])
T.flex('다음 우리말을 영어로 바르게 옮긴 것은?', R_, B('그 행사에 참석하지 못해서 미안해.'),
 ["I'm sorry for not attending the ceremony.", "I'm sorry for attending not the ceremony.", "I'm sorry for don't attending the ceremony.", "I'm sorry not for attend the ceremony.", "I'm sorry for not attend the ceremony."],
 "이유 ▶ 동명사의 부정 = not + -ing → for not attending.\n오답 ▶ {1} not 위치 ❌ {2} don't ❌ {3} 위치·형태 ❌ {4} not 뒤 -ing\n포인트 ▶ not은 동명사 바로 앞", [('attend', '참석하다'), ('ceremony', '행사')])
T.flex('다음 짝지어진 두 문장의 의미가 서로 <u>다른</u> 것은?', V_, '',
 ['I should remember to go to the bank.<br>= I should remember going to the bank.', 'My mother begins to collect old coins.<br>= My mother begins collecting old coins.', 'She starts to travel the world.<br>= She starts traveling the world.', 'Jonathan continues to study painting.<br>= Jonathan continues studying painting.', 'I hate to skip breakfast.<br>= I hate skipping breakfast.'],
 "이유 ▶ remember to V = (앞으로) ~할 것을 기억하다 / remember -ing = (전에) ~했던 것을 기억하다 → 뜻이 다름\n오답 ▶ {1}~{4} begin · start · continue · hate는 둘 다 뜻이 같음\n포인트 ▶ remember · forget은 to V(미래) / -ing(과거)", [('skip', '거르다')])
T.flex('다음 빈칸에 들어갈 말이 순서대로 바르게 짝지어진 것은?', V_, B('• Remember ' + BL + " your swimsuit. We'll go to the pool.", '• I remember ' + BL + ' Niagara Falls. It was wonderful.'),
 ['to pack − seeing', 'packing − seeing', 'to pack − to see', 'packing − to see', 'pack − see'],
 "이유 ▶ 앞으로 챙길 것 → Remember to pack / 전에 본 것(It was wonderful) → remember seeing\n오답 ▶ 시간(미래 / 과거)이 반대로 된 보기와 동사원형은 모두 틀림\n포인트 ▶ to V = 할 일 / -ing = 한 일", [('pack', '(짐을) 챙기다')])
T.flex('다음 빈칸에 들어갈 말로 알맞은 것은?', V_, B("Don't forget " + BL + ' the door when you go out.'),
 ['to lock', 'locking', 'lock', 'locked', 'to locking'],
 "이유 ▶ 나갈 때(앞으로) 문 잠글 것을 잊지 마 → forget to lock.\n오답 ▶ {1} forget -ing = 했던 것을 잊다 {2}·{3} 동사 ❌ {4} to 뒤 -ing ❌\n포인트 ▶ Don't forget to V = ~할 것을 잊지 마", [])
T.flex('다음 빈칸에 들어갈 말로 가장 알맞은 것은?', V_, B('Jina was very tired, so she stopped ' + BL + ' under the tree.'),
 ['to rest', 'rest', 'rested', 'resting', 'have rested'],
 "이유 ▶ 피곤해서 → 쉬기 위해 멈췄다 → stopped to rest(목적).\n오답 ▶ {1}·{2}·{4} 형태 ❌ {3} stopped resting = 쉬는 것을 멈췄다 → '피곤해서'와 맞지 않음\n포인트 ▶ stop -ing = ~하던 것을 멈추다 / stop to V = ~하기 위해 멈추다", [('rest', '쉬다')])
T.flex('다음 빈칸에 들어갈 walk의 형태가 같은 것끼리 짝지어진 것은?', V_, B('(A) Did you enjoy ' + BL + ' with me?', '(B) Would you like ' + BL + ' the dog?', '(C) ' + BL + ' and jogging are my mother\'s favorite exercises.', '(D) He needs ' + BL + ' for 30 minutes every day.'),
 ['(A), (C)', '(A), (B)', '(A), (D)', '(B), (C)', '(C), (D)'],
 "이유 ▶ (A) enjoy + walking (C) Walking and jogging(주어) → 둘 다 walking\n오답 ▶ (B) would like + to walk (D) need + to walk\n포인트 ▶ would like · need + to부정사", [('exercise', '운동')])
T.flex('다음 중 어법상 올바른 것은?', I_, '',
 ["We're looking forward to hearing from you.", 'She refused accepting his apology.', 'He complains about not have time to study.', "I can't finish read this book in 5 minutes.", 'Thank you for invite me.'],
 "이유 ▶ look forward to + 동명사(to는 전치사) ✔\n오답 ▶ {1} refuse → to accept {2} not having {3} finish reading {4} for inviting\n포인트 ▶ look forward to 뒤 동사원형 ❌", [('refuse', '거절하다'), ('apology', '사과')])
T.flex('다음 빈칸에 들어갈 말로 알맞지 <u>않은</u> 것은?', V_, B(BL + ' exercising in the morning.'),
 ['George planned', 'Nina gave up', 'They mind', 'We enjoy', 'I kept'],
 "이유 ▶ plan은 to부정사만 → George planned to exercise.\n오답 ▶ {1}~{4} give up · mind · enjoy · keep + -ing ✔\n포인트 ▶ plan + to V", [])
T.flex('다음 빈칸에 들어갈 말로 알맞지 <u>않은</u> 것은?', R_, B('Eating a good breakfast ' + BL + '.'),
 ['becoming my habit', 'is very wise', 'will help you study hard', 'makes you healthy', 'gives you lots of energy'],
 "이유 ▶ 주어 Eating a good breakfast 뒤에는 동사가 필요 → is becoming my habit 이어야 함.\n오답 ▶ {1} is {2} will help {3} makes {4} gives → 단수 동사 ✔\n포인트 ▶ 동명사 주어 + 단수 동사", [])
T.flex('다음 빈칸에 들어갈 말로 어색한 것은?', R_, B(BL + ' makes me happy.'),
 ['Travel around the world', 'The warm sunshine', 'Eating chocolate', 'To learn English', 'Listening to music'],
 "이유 ▶ 주어 자리에 동사원형 Travel ❌ → Traveling around the world\n오답 ▶ {1} 명사 {2}·{4} 동명사 {3} to부정사 주어 ✔\n포인트 ▶ 주어 = 명사 / 동명사 / to부정사", [])
T.flex('다음 대화의 밑줄 친 부분을 바르게 고친 것은?', V_, B(t('A: Would you mind [repeat] your name?'), 'B: Of course not. Andrew Gayle.'),
 ['repeating', 'repeats', 'repeated', 'to repeat', '고칠 필요 없음'],
 "이유 ▶ mind + 동명사 → Would you mind repeating ~? = 다시 말씀해 주시겠어요?\n오답 ▶ {1}·{2} 동사 ❌ {3} mind + to부정사 ❌ {4} 동사원형 repeat ❌\n포인트 ▶ Of course not. = (꺼리지 않으니) 물론이죠", [('repeat', '반복하다')])
T.fixed('다음 글의 밑줄 친 ⓐ~ⓔ 중 어법상 <u>틀린</u> 것은?', L_, B('We went to Damyang and ⓐ ' + U('visited') + ' Jungnogwon. We enjoyed ⓑ ' + U('walking') + ' in the garden. After we ⓒ ' + U('looked') + ' around, we ate two local dishes. On July 30, we visited Tongyeong. ⓓ ' + U('See') + ' the blue ocean and the green islands was fantastic! Long ago, fishermen in this town started ⓔ ' + U('to eat') + ' chungmugimbap.'),
 ['ⓐ', 'ⓑ', 'ⓒ', 'ⓓ', 'ⓔ'], 4,
 "이유 ▶ ⓓ 주어 자리 → 동명사 Seeing (교과서: Seeing the blue ocean and the green islands was fantastic!)\n오답 ▶ ⓐ went와 나란히 과거 ⓑ enjoy + -ing ⓒ 과거 ⓔ start + to V ✔\n포인트 ▶ 동사원형으로 문장의 주어 ❌", [('local', '지역의'), ('fisherman', '어부')])
T.flex('다음 밑줄 친 부분 중 동명사의 개수는?', K_, B(t('ⓐ I need [drinking] water.'), t('ⓑ Christmas is [coming] soon.'), t('ⓒ Bring me some [shopping] bags.'), t('ⓓ His job is [making] bread.'), t('ⓔ Look at the [sleeping] baby.')),
 ['3개', '1개', '2개', '4개', '5개'],
 "이유 ▶ 동명사: ⓐ 마시는 용도의 물 ⓒ 쇼핑용 가방 ⓓ 빵을 만드는 것(보어) → 3개\n현재분사 ▶ ⓑ 다가오고 있다(진행) ⓔ 자고 있는 아기\n포인트 ▶ 용도(~하기 위한) = 동명사 / 상태(~하고 있는) = 현재분사", [])
T.flex('다음 우리말을 영어로 바르게 옮긴 것은?', I_, B('Nami는 일주일에 한 번씩 수영하러 간다.'),
 ['Nami goes swimming once a week.', 'Nami goes swim once a week.', 'Nami goes swims once a week.', 'Nami goes to swimming once a week.', 'Nami go swimming once a week.'],
 "이유 ▶ go + -ing = ~하러 가다, 주어 Nami → goes swimming.\n오답 ▶ {1}·{2} 형태 ❌ {3} go 뒤 to 없이 바로 -ing {4} 3인칭 단수 → goes\n포인트 ▶ go shopping · go fishing · go camping", [('once a week', '일주일에 한 번')])
T.flex('다음 중 어법상 <u>틀린</u> 문장끼리 묶인 것은?', V_, B('Ⓐ It started snowing.', "Ⓑ Don't give up to try.", 'Ⓒ He finished playing the piano.', 'Ⓓ I hope visiting Jejudo someday.'),
 ['Ⓑ, Ⓓ', 'Ⓐ, Ⓑ', 'Ⓐ, Ⓒ', 'Ⓒ, Ⓓ', 'Ⓑ, Ⓒ'],
 "이유 ▶ Ⓑ give up → trying Ⓓ hope → to visit\n오답 ▶ Ⓐ start + -ing ✔ Ⓒ finish + -ing ✔\n포인트 ▶ give up(-ing) · hope(to V)", [])
T.flex('두 문장의 의미가 같도록 할 때 빈칸에 알맞은 것은?', I_, B("Let's meet in front of the stadium.", '= How about ' + BL + ' in front of the stadium?'),
 ['meeting', 'meet', 'to meet', 'met', 'to meeting'],
 "이유 ▶ Let's ~ = How about -ing? → meeting\n오답 ▶ {1}·{3} 동사 ❌ {2}·{4} to ❌\n포인트 ▶ How about -ing? = Let's ~ = Why don't we ~?", [('stadium', '경기장')])
T.flex('다음 우리말을 영어로 바르게 옮긴 것은?', R_, B('새 집으로 이사하는 것은 매우 스트레스 받는 경험이다.'),
 ['Moving to a new house is a very stressful experience.', 'Move to a new house is a very stressful experience.', 'Moving to a new house are a very stressful experience.', 'To moving to a new house is a very stressful experience.', 'Moved to a new house is a very stressful experience.'],
 "이유 ▶ 동명사 주어 Moving to a new house + 단수 동사 is.\n오답 ▶ {1}·{4} 동사로 시작 ❌ {2} 단수 → is {3} to 뒤 -ing ❌\n포인트 ▶ 동명사 주어 = ~하는 것은 + 단수 동사", [('stressful', '스트레스가 많은')])
T.render()

# ═══════════════ 4차 (상) ═══════════════
T = Test('4', '4차', '동명사 종합 심화', '동명사', NOTE, H=H); T.rot0 = 5
T.flex('다음 밑줄 친 부분의 쓰임이 나머지 넷과 <u>다른</u> 것은?', K_, '',
 [t('We are [making] some flowers for our parents.'), t('The soil is needed for [growing] crops.'), t('I stopped [reading] a magazine.'), t('[Writing] in English is not easy.'), t('My grandmother needs a good [walking] stick.')],
 "이유 ▶ are making = 진행형(만드는 중이다) → 현재분사.\n오답 ▶ {1} 전치사 for의 목적어 {2} stop의 목적어 {3} 주어 {4} 용도(걷기 위한 지팡이) → 모두 동명사\n포인트 ▶ a walking stick = a stick for walking(동명사)", [('crop', '농작물'), ('stick', '지팡이')])
T.flex('<보기>의 밑줄 친 부분과 쓰임이 <u>다른</u> 것은?', K_, B(t('<보기> Please go to the [waiting] room and fill out this form.')),
 [t('The man [wearing] a suit is our teacher.'), t('[Reading] a magazine is fun.'), t('Do you mind [using] your cell phone?'), t('[Living] in the country is good for your health.'), t('I bought a new [sleeping] bag.')],
 "이유 ▶ <보기> waiting room = 기다리기 위한 방(용도, 동명사). 정답 wearing은 '양복을 입고 있는' 남자 → 현재분사.\n오답 ▶ {1}·{3} 주어 {2} 목적어 {4} 용도(침낭) → 모두 동명사\n포인트 ▶ 명사를 꾸미는 -ing: 용도면 동명사, 상태·동작이면 현재분사", [('suit', '양복'), ('country', '시골')])
T.flex('다음 중 어법상 <u>어색한</u> 문장의 개수는?', R_, B('ⓐ Thank you for not telling this to anyone.', "ⓑ I'm looking forward to see you.", 'ⓒ He went fishing with his dad.', 'ⓓ My dream is become a pilot.', 'ⓔ Listening to others are important.'),
 ['3개', '1개', '2개', '4개', '5개'],
 "이유 ▶ 어색한 것 ⓑ · ⓓ · ⓔ → 3개\n고치기 ▶ ⓑ to seeing (look forward to + -ing) ⓓ becoming (또는 to become) ⓔ is (동명사 주어 = 단수)\n포인트 ▶ ⓐ not + -ing ✔ ⓒ go + -ing ✔", [('pilot', '조종사')])
T.flex('다음 글의 (A), (B), (C)에서 알맞은 것끼리 짝지은 것은?', V_, B('Last weekend, I went to a cooking class. At first, I was worried about (A) [ make / making ] mistakes. But the teacher was kind, and I really enjoyed (B) [ to cook / cooking ]. Now I want (C) [ to take / taking ] another class.'),
 ['making − cooking − to take', 'make − cooking − to take', 'making − to cook − to take', 'making − cooking − taking', 'make − to cook − taking'],
 "이유 ▶ (A) 전치사 about + making (B) enjoy + cooking (C) want + to take\n오답 ▶ 전치사 뒤 동사원형 ❌ / enjoy + to V ❌ / want + -ing ❌\n포인트 ▶ 한 글 안에서 동사·전치사마다 형태를 따로 확인", [('mistake', '실수')])
T.flex('다음 문장에서 어색한 부분을 바르게 고친 것은?', V_, B('He stopped to smoke for his health.'),
 ['to smoke → smoking', 'stopped → stops', 'for → to', 'his → him', '고칠 필요 없음'],
 "이유 ▶ 건강을 위해 '담배 피우는 것을 끊었다' → stopped smoking. (stopped to smoke = 담배를 피우려고 멈췄다 → 건강을 위해서와 맞지 않음)\n오답 ▶ {1}·{2}·{3} 고칠 곳이 아님 {4} 뜻이 맞지 않으므로 고쳐야 함\n포인트 ▶ stop -ing = 그만두다", [('smoke', '담배를 피우다')])
T.flex('다음 문장의 해석으로 알맞은 것은?', V_, B('I remember meeting Sumi at the store yesterday.'),
 ['나는 어제 가게에서 수미를 만났던 것을 기억한다.', '나는 어제 가게에서 수미를 만날 것을 기억한다.', '나는 어제 가게에서 수미를 만나기 위해 기억했다.', '나는 어제 가게에서 수미를 만나는 것을 잊었다.', '나는 어제 가게에서 수미를 만나는 중이었다.'],
 "이유 ▶ remember + -ing = (전에) ~했던 것을 기억하다, yesterday와도 맞음.\n오답 ▶ {1} remember to V의 뜻 {2} 목적 ❌ {3} forget의 뜻 {4} 진행 ❌\n포인트 ▶ remember -ing(과거) / remember to V(미래)", [], en=False)
T.flex('다음 대화의 빈칸에 들어갈 말로 알맞은 것은?', V_, B("A: Don't forget " + BL + ' your homework tomorrow.', "B: OK. I won't."),
 ['to bring', 'bringing', 'bring', 'brought', 'to bringing'],
 "이유 ▶ 내일(앞으로) 가져올 것을 잊지 마 → forget to bring.\n오답 ▶ {1} 가져왔던 것을 잊다 → tomorrow와 맞지 않음 {2}·{3} 동사 ❌ {4} to 뒤 -ing ❌\n포인트 ▶ forget to V = ~할 것을 잊다", [])
T.flex('다음 중 어법상 올바른 것을 모두 고른 것은?', R_, B('ⓐ She is proud of being a doctor.', "ⓑ I'm sorry for not calling you.", 'ⓒ He is afraid of to swim.', 'ⓓ They talked about join a science club.', 'ⓔ I dream of becoming a vet.'),
 ['ⓐ, ⓑ, ⓔ', 'ⓐ, ⓑ', 'ⓑ, ⓓ', 'ⓐ, ⓒ, ⓔ', 'ⓒ, ⓓ'],
 "이유 ▶ ⓐ of being ⓑ for not calling ⓔ of becoming → 전치사 + 동명사 ✔\n오답 ▶ ⓒ of swimming ⓓ about joining\n포인트 ▶ 전치사 뒤에는 to부정사 · 동사원형 ❌", [('be proud of', '~을 자랑스러워하다'), ('vet', '수의사')])
T.flex('다음 글의 빈칸에 들어갈 말이 순서대로 바르게 짝지어진 것은?', V_, B('Minho likes ' + BL + ' cartoons. He practices ' + BL + ' every day. He hopes ' + BL + ' a cartoonist.'),
 ['drawing − drawing − to become', 'to draw − to draw − becoming', 'drawing − to draw − to become', 'to draw − drawing − becoming', 'draw − drawing − to become'],
 "이유 ▶ like(-ing 가능) → drawing / practice + -ing → drawing / hope + to V → to become\n오답 ▶ practice + to V ❌ / hope + -ing ❌ / like 뒤 동사원형 ❌\n포인트 ▶ like는 to draw도 되지만, 세 칸이 모두 맞는 보기는 하나", [('cartoonist', '만화가')])
T.fixed('다음 글의 밑줄 친 ⓐ~ⓔ 중 어법상 <u>틀린</u> 것은?', V_, B('Yesterday, my family went ⓐ ' + U('camping') + '. ⓑ ' + U('Setting up') + ' the tent was hard, but we finished ⓒ ' + U('to build') + ' it before dark. We enjoyed ⓓ ' + U('cooking') + " dinner together. I'm looking forward to ⓔ " + U('going') + ' camping again.'),
 ['ⓐ', 'ⓑ', 'ⓒ', 'ⓓ', 'ⓔ'], 3,
 "이유 ▶ finish는 동명사만 → finished building\n오답 ▶ ⓐ go + -ing ⓑ 동명사 주어 ⓓ enjoy + -ing ⓔ look forward to + -ing ✔\n포인트 ▶ finish + to V ❌", [('set up', '세우다'), ('before dark', '어두워지기 전에')])
T.flex('다음 밑줄 친 부분 중 동명사로 쓰인 것끼리 바르게 묶은 것은?', K_, B(t('ⓐ My hobby is [collecting] stamps.'), t('ⓑ She is [collecting] stamps now.'), t('ⓒ [Collecting] stamps is fun.'), t('ⓓ The boy [collecting] stamps is my brother.'), t('ⓔ I like [collecting] stamps.')),
 ['ⓐ, ⓒ, ⓔ', 'ⓐ, ⓑ, ⓒ', 'ⓑ, ⓓ', 'ⓐ, ⓓ, ⓔ', 'ⓒ, ⓓ, ⓔ'],
 "이유 ▶ ⓐ 보어(모으는 것) ⓒ 주어 ⓔ 목적어 → 동명사\n오답 ▶ ⓑ 진행형(모으는 중) ⓓ 우표를 모으고 있는 소년(명사 수식) → 현재분사\n포인트 ▶ 'is collecting'은 주어에 따라 동명사도 진행형도 됨 → 주어와 같은 뜻(=)이면 보어", [('collect', '모으다')])
T.flex('다음 우리말을 영어로 바르게 옮긴 것은?', V_, B('Peter는 그녀에게 이야기하는 것을 피했다.'),
 ['Peter avoided talking to her.', 'Peter avoided to talk to her.', 'Peter avoid talking to her.', 'Peter avoided talk to her.', 'Peter avoided talking her.'],
 "이유 ▶ avoid + 동명사, 과거 avoided, talk to + 사람.\n오답 ▶ {1} avoid + to V ❌ {2} 과거·3인칭 → avoided {3} 동사원형 ❌ {4} talk to her (to 빠짐)\n포인트 ▶ avoid + -ing", [('avoid', '피하다')])
T.flex('밑줄 친 work의 알맞은 형태가 바르게 짝지어진 것은?', V_, B(t('I was really excited about [work] with foreigners.'), t('Finally, I went abroad and enjoyed [work] there.')),
 ['working − working', 'to work − to work', 'to work − working', 'working − to work', 'to working − to work'],
 "이유 ▶ 전치사 about + working / enjoy + working\n오답 ▶ 전치사 뒤 to V ❌ / enjoy + to V ❌ / to 뒤 -ing ❌\n포인트 ▶ 전치사 · enjoy 뒤 = 동명사", [('foreigner', '외국인')])
T.flex('다음 중 두 문장의 의미가 같지 <u>않은</u> 것은?', V_, '',
 ['He stopped eating.<br>= He stopped to eat.', 'It started raining.<br>= It started to rain.', 'She loves reading.<br>= She loves to read.', 'They continued talking.<br>= They continued to talk.', 'I hate being alone.<br>= I hate to be alone.'],
 "이유 ▶ stopped eating = 먹는 것을 멈췄다 / stopped to eat = 먹기 위해 멈췄다 → 뜻이 다름\n오답 ▶ {1}~{4} start · love · continue · hate는 둘 다 뜻이 같음\n포인트 ▶ stop 뒤 to V는 목적어가 아니라 '~하기 위해'", [])
T.flex('다음 빈칸에 들어갈 말이 바르게 짝지어진 것은?', R_, B('She came into the room without ' + BL + ' on the door or ' + BL + ' anything.'),
 ['knocking − saying', 'knocking − say', 'knock − saying', 'knocking − to say', 'to knocking − to saying'],
 "이유 ▶ 전치사 without 뒤 두 동명사가 or로 나란히 → knocking − saying\n오답 ▶ or 뒤도 without의 목적어 → say · to say ❌, 전치사 뒤 knock ❌\n포인트 ▶ without + -ing = ~하지 않고", [('knock', '노크하다')])
T.flex('다음 중 어법상 <u>어색한</u> 것은?', V_, '',
 ['I forgot bringing my lunch box this morning, so I was hungry.', 'I remember visiting Paris when I was five.', 'Remember to call your grandma tonight.', "The bird doesn't stop singing until it finds a mate.", "Don't forget to take your umbrella before going out."],
 "이유 ▶ 도시락을 안 가져와서 배고팠다 → 가져올 것을 잊었다 → forgot to bring\n오답 ▶ {1} 다섯 살 때 방문했던 것 {2} 오늘 밤 할 일 {3} 노래하는 것을 멈추지 않는다 {4} 할 일 + before going ✔\n포인트 ▶ 문맥으로 to V / -ing를 정하기", [('mate', '짝')])
T.flex('다음 대화의 ⓐ, ⓑ에 알맞은 형태가 바르게 짝지어진 것은?', I_, B('Jimin: Yunho, can you suggest a hobby for me?', 'Yunho: How about ⓐ (raise) spiders?', "Jimin: Aren't they scary?", "Yunho: Then, why don't you ⓑ (raise) other insects like ants?"),
 ['raising − raise', 'raise − raise', 'to raise − raising', 'raising − raising', 'raises − raising'],
 "이유 ▶ ⓐ How about + -ing → raising ⓑ Why don't you + 동사원형 → raise\n오답 ▶ How about 뒤 동사원형 · to부정사 ❌, Why don't you 뒤 -ing ❌\n포인트 ▶ How about -ing? = Why don't you + 동사원형?", [('raise', '기르다'), ('insect', '곤충')])
T.flex('다음 글의 밑줄 친 부분과 쓰임이 같은 것은?', L_, B('We visited Tongyeong and went up the mountain by cable car. ' + t('[Seeing]') + ' the blue ocean and the green islands was fantastic!'),
 [t('[Raising] insects is an interesting hobby.'), t('My hobby is [raising] spiders.'), t("I'm interested in [raising] spiders."), t('He is [raising] spiders now.'), t('I enjoy [raising] spiders.')],
 "이유 ▶ 본문 Seeing ~ = 문장의 주어. 정답도 주어(곤충을 기르는 것은).\n오답 ▶ {1} 보어 {2} 전치사의 목적어 {3} 진행형(현재분사) {4} 동사의 목적어\n포인트 ▶ 주어 동명사 뒤에는 단수 동사(was · is)", [])
T.flex('다음 글의 밑줄 친 ⓐ~ⓔ 중 어법상 <u>틀린</u> 것의 개수는?', R_, B('I like ⓐ ' + U('to read') + ' books. ⓑ ' + U('Reading books make') + ' me happy. Last night, I finished ⓒ ' + U('reading') + ' a long novel. My dream is ⓓ ' + U('write') + " my own story. I'm good at ⓔ " + U('to imagine') + ' things.'),
 ['3개', '1개', '2개', '4개', '5개'],
 "이유 ▶ 틀린 것 ⓑ makes(동명사 주어 단수) ⓓ writing(또는 to write) ⓔ imagining(전치사 뒤) → 3개\n오답 ▶ ⓐ like + to V ✔ ⓒ finish + -ing ✔\n포인트 ▶ 주어 수 · be동사 뒤 · 전치사 뒤를 모두 확인", [('novel', '소설'), ('imagine', '상상하다')])
T.flex('다음 우리말을 영어로 바르게 옮긴 것은?', R_, B('패스트푸드를 너무 많이 먹지 않는 것은 중요하다.'),
 ['Not eating too much fast food is important.', "Don't eating too much fast food is important.", 'Not eat too much fast food is important.', 'Not eating too much fast food are important.', 'Eating too much fast food not is important.'],
 "이유 ▶ 동명사 부정 Not eating ~ 주어 + 단수 동사 is.\n오답 ▶ {1} Don't ❌ {2} not 뒤 -ing {3} 단수 → is {4} '많이 먹는 것은 중요하지 않다'도 아니고 어순도 ❌\n포인트 ▶ not + -ing = ~하지 않는 것", [])
T.render()
