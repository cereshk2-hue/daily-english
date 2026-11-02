from gramcommon import *
# 중2 동아(윤정미) 7·8과 문법 (11/2)
# 7과: 가주어 it + to부정사 진주어 · call + 목적어 + 목적격보어 → 7과 본문(d2) 뒤
# 8과: 현재완료 · -thing + 형용사 → 8과 본문(d4) 뒤
# 근거: Grammar Build Up 객관식 7·8과 유형(똑같이 말고 살짝 바꿔서) + 교과서 본문 문장
# 7과 대화문(k7a/k7b)은 10/30에 이미 넣음. 8과 대화문(k8a/k8b)은 파일 받으면 8과 본문 앞에

G7, G8 = [], []

def day(did, rng, story, notes, tf, pick, use, real, err, scr):
    D = Day(did, rng, story)
    D.note('핵심 개념', notes)
    D.step(TF('개념 확인 T/F', tf))
    D.step(PICK(D, '어법 선택', pick))
    D.step(MC('쓰임 구별 · 의미', use))
    D.step(MC('실전 어법', real))
    D.step(ERR(D, '오류 찾기', err))
    D.step(SCR(D, '우리말 → 영어 배열', scr))
    return D.done()

# ═════════ 7과 ① 가주어 it ═════════
G7.append(day('e7a', '7과 문법 ① 가주어 it · 진주어 to부정사', 'It is + 형용사 + to부정사 = ~하는 것은 …하다 · for + 목적격 · it 쓰임 구별',
 [('It(가주어) + be + 형용사 + to부정사(진주어)', '~하는 것은 …하다. It은 "그것"으로 해석하지 않아요.'),
  ('교과서', 'They believe it is important to remember dead people. / Is it possible to do so?'),
  ('의미상 주어', 'It is hard for me to wake up early. (for + 목적격)'),
  ('it 쓰임 구별', '가주어 It(뒤에 to부정사) / 비인칭 it(날씨·시간·요일·거리) / 대명사 it(그것)')],
 [('It is fun to watch a movie with friends.에서 It은 "그것"이라고 해석한다.', False, '정답 ▶ F\n이유: 가주어 It은 해석하지 않아요. → 친구들과 영화를 보는 것은 재미있다.'),
  ('To learn a new language is important. = It is important to learn a new language.', True, '정답 ▶ T\n이유: 긴 to부정사 주어를 뒤로 보내고 그 자리에 가주어 It'),
  ('It is easy for me to swim.에서 for me는 to swim을 하는 사람(의미상 주어)이다.', True, '정답 ▶ T\n이유: for + 목적격 = to부정사의 의미상 주어'),
  ("It's 5 o'clock now.의 It은 가주어이다.", False, '정답 ▶ F\n이유: 시간을 나타내는 비인칭 it. 뒤에 to부정사(진주어)가 없어요.'),
  ('Is it possible to do so?에서 진주어는 to do so이다.', True, '정답 ▶ T\n이유: 그렇게 하는 것(to do so)이 가능할까? (교과서 7과)')],
 [('They believe {it|that} is important to remember dead people.', '그들은 고인을 기억하는 것이 중요하다고 믿는다.', '정답 ▶ it\n이유: 뒤의 to remember ~가 진주어 → 가주어 it (교과서 7과)'),
  ('Is it possible {to do|do} so?', '그렇게 하는 것이 가능할까?', '정답 ▶ to do\n이유: 진주어 자리 → to부정사 (교과서 7과)'),
  ("It isn't easy {to exercise|exercise} every day.", '매일 운동하는 것은 쉽지 않다.', '정답 ▶ to exercise\n이유: 진주어 → to + 동사원형'),
  ('{It|This} is fun to play board games with my family.', '가족과 보드게임을 하는 것은 재미있다.', '정답 ▶ It\n이유: 가주어는 It만 써요. This ✗'),
  ('It is hard {for|of} me to keep a diary every day.', '내가 매일 일기를 쓰는 것은 어렵다.', '정답 ▶ for\n이유: 의미상 주어 for + 목적격'),
  ('It is important {to follow|follows} the class rules.', '학급 규칙을 따르는 것은 중요하다.', '정답 ▶ to follow\n이유: 진주어 → to부정사'),
  ('It {is|are} exciting to watch fireworks.', '불꽃놀이를 보는 것은 신난다.', '정답 ▶ is\n이유: 가주어 It → 단수 동사 (fireworks에 속지 않기)'),
  ('It is dangerous {to swim|swim} in this river.', '이 강에서 수영하는 것은 위험하다.', '정답 ▶ to swim\n이유: 진주어 → to부정사')],
 [('밑줄 친 It의 쓰임이 나머지 넷과 <b>다른</b> 것은?', ['<u>It</u> is cold and windy today.', '<u>It</u> is fun to ride a bike.', '<u>It</u> is important to remember dead people.', '<u>It</u> is not easy to learn Chinese.', '<u>It</u> is exciting to visit festivals.'],
   '정답 ▶ It is cold and windy today.\n이유: 날씨를 나타내는 비인칭 it. 나머지는 뒤에 to부정사가 있는 가주어 It'),
  ('밑줄 친 It의 쓰임이 [보기]와 같은 것은?<br>[보기] <u>It</u> is possible to finish the work today.', ['<u>It</u> is hard to wake up early.', '<u>It</u> is my new bike.', '<u>It</u> is Sunday today.', '<u>It</u> is 2 km from here to the station.', 'I lost my pen. Did you see <u>it</u>?'],
   '정답 ▶ It is hard to wake up early.\n이유: 둘 다 가주어 It\n오답 ▶ 그것(대명사) / 요일·거리(비인칭) / 그것(목적어)'),
  ('두 문장의 의미가 같도록 할 때 알맞은 것은?<br><b>To set up altars at home is important to them.</b>', ['It is important to them to set up altars at home.', 'It is important to them set up altars at home.', 'This is important to them to set up altars at home.', 'It is important to them setting up altars at home.'],
   '정답 ▶ It is important to them to set up altars at home.\n이유: 가주어 It + 진주어 to부정사'),
  ('빈칸 (A), (B)에 알맞은 것은?<br><b>(A)____ is not easy (B)____ a new language.</b>', ['It - to learn', 'That - to learn', 'It - learn', 'This - learning', 'It - learned'],
   '정답 ▶ It - to learn\n이유: 가주어 It + 진주어 to + 동사원형'),
  ('우리말을 바르게 영작한 것은?<br><b>어떤 나이에도 새로운 언어를 배우는 것이 가능한가?</b>', ['Is it possible to learn a new language at any age?', 'Is possible it to learn a new language at any age?', 'Is it possible learn a new language at any age?', 'It is possible to learn a new language at any age?'],
   '정답 ▶ Is it possible to learn a new language at any age?\n이유: 의문문 → Is it + 형용사 + to부정사 ~?')],
 [('어법상 <b>옳은</b> 문장은?', ['It is necessary for you to drink enough water.', 'It is fun play soccer after school.', 'That is important to save energy.', 'It are exciting to travel to new places.', 'It is hard of me to get up early.'],
   '정답 ▶ It is necessary for you to drink enough water.\n오답 ▶ to play / It is / It is / for me'),
  ('어법상 <b>어색한</b> 문장은?', ['It is interesting to learning about other cultures.', 'It is fun to watch a movie with friends.', "It isn't easy to exercise every day.", 'Is it possible to run faster than reindeer?', 'It is good for your health to eat vegetables.'],
   '정답 ▶ It is interesting to learning about other cultures.\n이유: to + 동사원형 → to learn'),
  ('어법상 옳은 문장의 개수는?<br>• It is great to see you again.<br>• It is important remember dead people.<br>• It is not safe to swim here.<br>• This is difficult to solve the puzzle.<br>• It is hard for him to say sorry.', ['3개', '1개', '2개', '4개', '5개'],
   '정답 ▶ 3개\n틀린 것 ▶ remember → to remember / This → It', True),
  ('교과서 7과의 "Is it possible to do so?"에서 do so가 가리키는 것은?', ['run faster than reindeer', 'wear fun costumes', 'enjoy winter sports', 'hold the festival'],
   '정답 ▶ run faster than reindeer\n이유: 바로 앞 문장 People who participate in this race ~ try to run faster than reindeer. → 순록보다 빨리 달리는 것이 가능할까?'),
  ('빈칸에 들어갈 말이 나머지 넷과 <b>다른</b> 것은?<br>① ____ is fun to go camping.<br>② ____ is important to be kind.<br>③ ____ is hard to wake up early.<br>④ ____ is exciting to watch the parade.<br>⑤ ____ girl over there is my sister.', ['⑤', '①', '②', '③', '④'],
   '정답 ▶ ⑤\n이유: ⑤ That girl(저 소녀) / 나머지는 가주어 It', True)],
 [('They believe [[it]] is important [[remember]] [[dead]] people.', 1, 'to remember', '그들은 고인을 기억하는 것이 중요하다고 믿는다.', '정답 ▶ remember → to remember\n이유: 진주어 → to부정사'),
  ('[[That]] is fun [[to watch]] a movie [[with]] friends.', 0, 'It', '친구들과 영화를 보는 것은 재미있다.', '정답 ▶ That → It\n이유: 가주어는 It'),
  ('It is hard [[of]] me [[to keep]] a diary [[every]] day.', 0, 'for', '내가 매일 일기를 쓰는 것은 어렵다.', '정답 ▶ of → for\n이유: 의미상 주어 for + 목적격'),
  ("Is it [[possible]] [[do]] so? Not really, but it [[doesn't]] matter.", 1, 'to do', '그렇게 하는 것이 가능할까? 별로 그렇지 않지만, 그건 중요하지 않다.', '정답 ▶ do → to do'),
  ('It [[are]] exciting [[to watch]] the fireworks [[at]] night.', 0, 'is', '밤에 불꽃놀이를 보는 것은 신난다.', '정답 ▶ are → is\n이유: 가주어 It → 단수')],
 [('They believe it is important to remember dead people.', '그들은 고인을 기억하는 것이 중요하다고 믿는다.'),
  ('Is it possible to do so?', '그렇게 하는 것이 가능할까?'),
  ("It isn't easy to exercise every day.", '매일 운동하는 것은 쉽지 않다.'),
  ('It is fun to watch a movie with friends.', '친구들과 영화를 보는 것은 재미있다.')]))

# ═════════ 7과 ② call + 목적어 + 목적격보어 ═════════
G7.append(day('e7b', '7과 문법 ② call + 목적어 + 목적격보어', 'call A B = A를 B라고 부르다 · 목적어 = 목적격보어 · 4형식과 구별',
 [('call + 목적어 + 명사(목적격보어)', '~을 …라고 부르다. 목적어와 목적격보어는 같은 대상'),
  ('교과서', 'They call it the Midsummer festival. / They call this day the Day of the Dead.'),
  ('주의', 'as · to 넣지 않기: call it as ~ ✗ / call it to ~ ✗'),
  ('4형식과 구별', 'call A B: A = B / give·make A B: A에게 B를 (A ≠ B)')],
 [('They call it the Midsummer festival.에서 it과 the Midsummer festival은 같은 대상이다.', True, '정답 ▶ T\n이유: 목적어(it) = 목적격보어(the Midsummer festival)'),
  ('call + 목적어 + 목적격보어에서 목적격보어 자리에는 주로 명사가 온다.', True, '정답 ▶ T\n이유: 부르는 이름(명사): call me Bob'),
  ('My friends call me Bob.은 "내 친구들은 나에게 Bob을 전화한다"로 해석한다.', False, '정답 ▶ F\n이유: 내 친구들은 나를 Bob이라고 부른다.'),
  ('She calls her robot Clean Master.와 She bought her sister a robot.은 같은 문장 구조이다.', False, '정답 ▶ F\n이유: 로봇 = Clean Master(목적어 = 목적격보어) / 여동생 ≠ 로봇(~에게 …을)'),
  ('People call Chicago as the Windy City.는 바른 문장이다.', False, '정답 ▶ F\n이유: call 뒤에 as를 넣지 않아요. → People call Chicago the Windy City.')],
 [('They call {it|its} the Midsummer festival.', '그들은 그것을 한여름 축제라고 부른다.', '정답 ▶ it\n이유: 목적어 자리 → 목적격 it (교과서 7과)'),
  ('They call this day {the Day of the Dead|to the Day of the Dead}.', '그들은 이날을 죽은 자들의 날이라고 부른다.', '정답 ▶ the Day of the Dead\n이유: call A B (to ✗) (교과서 7과)'),
  ('My name is Robert, but my friends call {me|my} Bob.', '내 이름은 Robert이지만, 친구들은 나를 Bob이라고 부른다.', '정답 ▶ me\n이유: 목적어 자리 → 목적격'),
  ('People call Chicago {the Windy City|as the Windy City}.', '사람들은 시카고를 Windy City라고 부른다.', '정답 ▶ the Windy City\n이유: call A B (as ✗)'),
  ('Her name is Elizabeth, but her friends {call|calls} her Liz.', '그녀의 이름은 Elizabeth이지만, 친구들은 그녀를 Liz라고 부른다.', '정답 ▶ call\n이유: 주어 her friends(복수)'),
  ('We {call|say} our dog Coco.', '우리는 우리 개를 코코라고 부른다.', '정답 ▶ call\n이유: ~을 …라고 부르다 = call A B'),
  ('What {do|are} you call this food in English?', '너는 이 음식을 영어로 뭐라고 부르니?', '정답 ▶ do\n이유: 일반동사 call의 의문문 → do'),
  ('They decided to {call|calling} their daughter Lily.', '그들은 딸을 Lily라고 부르기로 했다.', '정답 ▶ call\n이유: decide + to + 동사원형')],
 [('문장의 구조가 나머지 넷과 <b>다른</b> 것은?', ['My mom made me a sandwich.', 'They call him a hero.', 'We call the cat Nabi.', 'People call the boy a genius.', 'They named the baby Mina.'],
   '정답 ▶ My mom made me a sandwich.\n이유: 나에게 샌드위치를(나 ≠ 샌드위치). 나머지는 목적어 = 목적격보어'),
  ('밑줄 친 call의 쓰임이 [보기]와 같은 것은?<br>[보기] We <u>call</u> him Captain.', ['People <u>call</u> New York the Big Apple.', 'Please <u>call</u> me tonight.', 'I will <u>call</u> you back later.', 'She <u>called</u> a taxi.', 'He <u>called</u> for help.'],
   '정답 ▶ People call New York the Big Apple.\n이유: ~을 …라고 부르다\n오답 ▶ 전화하다 / 다시 전화하다 / (택시를) 부르다 / 도와 달라고 외치다'),
  ('우리말을 바르게 영작한 것은?<br><b>사람들은 시카고를 Windy City라고 부른다.</b>', ['People call Chicago the Windy City.', 'People call the Windy City Chicago.', 'People call Chicago to the Windy City.', 'People call Chicago as the Windy City.', 'People are called Chicago the Windy City.'],
   '정답 ▶ People call Chicago the Windy City.\n이유: call + 목적어(Chicago) + 이름(the Windy City)'),
  ('빈칸 (A), (B)에 알맞은 것은?<br><b>Mexicans believe dead people come back once a year. They call (A)____ day (B)____.</b>', ['this - the Day of the Dead', 'this - to the Day of the Dead', 'these - the Day of the Dead', 'this - as the Day of the Dead'],
   '정답 ▶ this - the Day of the Dead\n이유: this + 단수명사(day) / call A B'),
  ('다음 문장에서 목적어와 목적격보어를 바르게 고른 것은?<br><b>The children call their teacher Ms. Smile.</b>', ['목적어: their teacher / 목적격보어: Ms. Smile', '목적어: The children / 목적격보어: their teacher', '목적어: Ms. Smile / 목적격보어: their teacher', '목적어: their teacher / 목적격보어: 없음'],
   '정답 ▶ 목적어: their teacher / 목적격보어: Ms. Smile\n이유: 선생님(목적어)을 Ms. Smile(보어)이라고 부른다')],
 [('어법상 <b>옳은</b> 문장은?', ['We call the festival Fur Rondy.', 'They call him as a hero.', 'My friends call to me Jay.', 'People call it to the Midsummer festival.', 'She calls her robot is Clean Master.'],
   '정답 ▶ We call the festival Fur Rondy.\n오답 ▶ as ✗ / to ✗ / to ✗ / is ✗'),
  ('어법상 <b>어색한</b> 문장은?', ['They call this day as the Day of the Dead.', 'People call him the king of rock.', 'We call our grandma Halmeoni.', 'They call the giant statues fallas.', 'What do you call this in English?'],
   '정답 ▶ They call this day as the Day of the Dead.\n이유: as를 빼야 해요.'),
  ('어법상 옳은 문장의 개수는?<br>• My classmates call me Smiley.<br>• They call their son to Tom.<br>• People call the city the City of Light.<br>• We call it the Running of the Reindeer.<br>• She calls her cat as Luna.', ['3개', '1개', '2개', '4개', '5개'],
   '정답 ▶ 3개\n틀린 것 ▶ to Tom → Tom / as Luna → Luna', True),
  ('우리말을 바르게 영작한 것은?<br><b>그 소년은 자신의 개를 Max라고 부른다.</b>', ['The boy calls his dog Max.', 'The boy calls Max his dog.', 'The boy his dog calls Max.', 'The boy calls to his dog Max.'],
   '정답 ▶ The boy calls his dog Max.\n이유: call + 목적어(his dog) + 이름(Max). 순서를 바꾸면 "Max를 그의 개라고 부른다"가 돼요.'),
  ('밑줄 친 call의 쓰임이 같은 것끼리 짝지은 것은?<br>ⓐ They <u>call</u> it the Midsummer festival.<br>ⓑ They <u>call</u> this day the Day of the Dead.<br>ⓒ I\'ll <u>call</u> you after the festival.<br>ⓓ Can you <u>call</u> a doctor?', ['ⓐ, ⓑ', 'ⓐ, ⓒ', 'ⓑ, ⓒ', 'ⓐ, ⓓ'],
   '정답 ▶ ⓐ, ⓑ\n이유: ⓐⓑ ~을 …라고 부르다 / ⓒ 전화하다 / ⓓ (의사를) 부르다', True)],
 [('They [[call]] [[its]] the Midsummer [[festival]].', 1, 'it', '그들은 그것을 한여름 축제라고 부른다.', '정답 ▶ its → it\n이유: 목적어 자리 → 목적격'),
  ('People [[call]] [[Chicago]] [[as the Windy City]].', 2, 'the Windy City', '사람들은 시카고를 Windy City라고 부른다.', '정답 ▶ as the Windy City → the Windy City\n이유: call A B (as ✗)'),
  ('My friends [[calls]] [[me]] [[Bob]].', 0, 'call', '내 친구들은 나를 Bob이라고 부른다.', '정답 ▶ calls → call\n이유: 주어 My friends(복수)'),
  ('They decided [[to call]] [[they]] daughter [[Lily]].', 1, 'their', '그들은 딸을 Lily라고 부르기로 했다.', '정답 ▶ they → their\n이유: 명사 앞 → 소유격'),
  ('Mia [[calls]] [[her]] dog [[to Rex]].', 2, 'Rex', 'Mia는 자신의 개를 Rex라고 부른다.', '정답 ▶ to Rex → Rex\n이유: call A B (to ✗)')],
 [('They call it the Midsummer festival.', '그들은 그것을 한여름 축제라고 부른다.'),
  ('They call this day the Day of the Dead.', '그들은 이날을 죽은 자들의 날이라고 부른다.'),
  ('People call Chicago the Windy City.', '사람들은 시카고를 Windy City라고 부른다.'),
  ('My friends call me Bob.', '내 친구들은 나를 Bob이라고 부른다.')]))

# ═════════ 8과 ① 현재완료 ═════════
G8.append(day('e8a', '8과 문법 ① 현재완료', 'have/has + p.p. · 완료/경험/계속 · for/since · 과거 시점과 못 씀',
 [('have/has + p.p.', "I've always wanted to see a dinosaur. / We've just arrived in the jungle. / I've never seen such a huge thing. (교과서)"),
  ('용법', '완료(just, already, yet) · 경험(ever, never, before) · 계속(for + 기간, since + 시점)'),
  ('주의', '명확한 과거(yesterday, last ~, ~ ago, When ~?)와는 못 써요.'),
  ('have been to vs have gone to', '가 본 적 있다(경험) / 가 버렸다(지금 여기 없음)')],
 [("I've never seen such a huge thing.은 경험 용법이다.", True, '정답 ▶ T\n이유: never(한 번도 ~않다) → 본 적이 없다'),
  ('I have visited Jeju-do last year.는 바른 문장이다.', False, '정답 ▶ F\n이유: last year(명확한 과거) → I visited Jeju-do last year.'),
  ('He has gone to Paris.는 "그는 파리에 가 본 적이 있다"는 뜻이다.', False, '정답 ▶ F\n이유: has gone to = 가 버렸다(지금 없음). 가 본 적이 있다 = has been to'),
  ("We've just arrived in the jungle.은 완료 용법이다.", True, '정답 ▶ T\n이유: just(방금) → 방금 도착했다'),
  ('My uncle has lived in Canada since 2010.은 "2010년부터 지금까지 살고 있다"는 뜻이다.', True, '정답 ▶ T\n이유: since + 시점 → 계속')],
 [("I've always {wanted|want} to see a dinosaur.", '저는 항상 공룡을 보고 싶었어요.', '정답 ▶ wanted\n이유: have + p.p. (교과서 8과)'),
  ("We've just {arrived|arrive} in the jungle of 60 million years ago.", '우리는 방금 6천만 년 전의 정글에 도착했습니다.', '정답 ▶ arrived\n이유: have + p.p. (교과서 8과)'),
  ("I've never {seen|saw} such a huge thing.", '나는 저렇게 거대한 것을 본 적이 없다.', '정답 ▶ seen\n이유: see - saw - seen. have + 과거분사 (교과서 8과)'),
  ('My uncle has lived in Canada {since|for} 2010.', '삼촌은 2010년부터 캐나다에 살고 계신다.', '정답 ▶ since\n이유: since + 시점(2010)'),
  ('We have known each other {for|since} five years.', '우리는 5년 동안 서로 알고 지냈다.', '정답 ▶ for\n이유: for + 기간(five years)'),
  ('I {visited|have visited} Jeju-do last summer.', '나는 지난여름에 제주도를 방문했다.', '정답 ▶ visited\n이유: last summer(명확한 과거) → 과거시제'),
  ('{Have|Did} you ever been to Jeju-do?', '너는 제주도에 가 본 적이 있니?', '정답 ▶ Have\n이유: been(p.p.) → Have + 주어 + p.p. ~?'),
  ('She {has|have} already finished her homework.', '그녀는 이미 숙제를 끝냈다.', '정답 ▶ has\n이유: 주어 She(3인칭 단수) → has'),
  ('When {did you meet|have you met} her?', '너는 그녀를 언제 만났니?', '정답 ▶ did you meet\n이유: When(언제)은 현재완료와 못 써요.')],
 [('밑줄 친 부분의 용법이 [보기]와 같은 것은?<br>[보기] I <u>have never seen</u> such a huge thing.', ['<u>Have</u> you ever <u>eaten</u> Mexican food?', 'The concert <u>has already started</u>.', 'He <u>has lived</u> here for ten years.', 'I <u>have just finished</u> my homework.', 'She <u>has been</u> sick since Monday.'],
   '정답 ▶ Have you ever eaten Mexican food?\n이유: [보기]와 같은 경험(ever/never)\n오답 ▶ 완료(already) / 계속(for) / 완료(just) / 계속(since)'),
  ('짝지어진 두 문장의 현재완료 용법이 서로 <b>다른</b> 것은?', ['I have finished the report. / I have been to Busan twice.', 'She has just left. / The train has already arrived.', 'I have lived here for 3 years. / He has been sick since Monday.', 'Have you ever seen a koala? / I have never ridden a horse.'],
   '정답 ▶ I have finished the report. / I have been to Busan twice.\n이유: 완료(끝냈다) / 경험(두 번 가 봤다)'),
  ('대화의 빈칸에 알맞은 것은?<br><b>A: ________<br>B: Yes, I have. I went there last year.</b>', ['Have you been to Gyeongju?', 'Did you go to Gyeongju?', 'Do you go to Gyeongju?', 'Have you gone to Gyeongju?', 'Were you in Gyeongju?'],
   '정답 ▶ Have you been to Gyeongju?\n이유: Yes, I have.로 답했으니 현재완료 경험 질문. have gone to는 "가 버렸다"라 질문으로 어색해요.'),
  ('두 문장을 한 문장으로 바꿀 때 알맞은 것은?<br><b>Tom moved to Seoul in 2020. He still lives there.<br>→ Tom ______ in Seoul since 2020.</b>', ['has lived', 'lived', 'lives', 'is living', 'live'],
   '정답 ▶ has lived\n이유: 2020년부터 지금까지 → 현재완료 계속'),
  ('대화의 빈칸에 알맞은 것은?<br><b>A: Where is Minho?<br>B: He ______ to the library. He isn\'t here now.</b>', ['has gone', 'has been', 'have gone', 'is gone', 'have been'],
   '정답 ▶ has gone\n이유: 도서관에 가 버려서 지금 여기 없다 → has gone to')],
 [('어법상 <b>옳은</b> 문장은?', ['I have never seen such a huge dinosaur.', 'I have seen the movie yesterday.', 'When have you finished your work?', 'She has lived here since three years.', 'Have you ever eat Thai food?'],
   '정답 ▶ I have never seen such a huge dinosaur.\n오답 ▶ yesterday ✗ / When ✗ / since → for / eat → eaten'),
  ('어법상 <b>어색한</b> 문장은?', ['He has met her two days ago.', 'We have just arrived at the station.', 'I have known Mina since 2022.', 'Has the movie started yet?', 'They have already eaten lunch.'],
   '정답 ▶ He has met her two days ago.\n이유: two days ago(명확한 과거) → He met her two days ago.'),
  ('어법상 옳은 문장의 개수는?<br>• I\'ve always wanted to see a dinosaur.<br>• She has gone to London last month.<br>• Have you ever been to Canada?<br>• We have lived here for ten years.<br>• He has went to the store.', ['3개', '1개', '2개', '4개', '5개'],
   '정답 ▶ 3개\n틀린 것 ▶ last month ✗ → She went to London last month. / has went → has gone', True),
  ('우리말을 바르게 영작한 것은?<br><b>우리는 방금 6천만 년 전의 정글에 도착했다.</b>', ["We've just arrived in the jungle of 60 million years ago.", "We've just arrive in the jungle of 60 million years ago.", 'We has just arrived in the jungle of 60 million years ago.', 'We just arrive in the jungle of 60 million years ago.', "We've just arriving in the jungle of 60 million years ago."],
   "정답 ▶ We've just arrived in the jungle of 60 million years ago.\n이유: have + just + p.p. (교과서 8과)"),
  ('교과서 8과 문장과 현재완료 용법이 바르게 연결된 것은?', ["I've never seen such a huge thing. - 경험", "I've always wanted to see a dinosaur. - 완료", "We've just arrived in the jungle. - 계속", "I've never seen such a huge thing. - 계속"],
   "정답 ▶ I've never seen such a huge thing. - 경험\n오답 ▶ always wanted: 계속(늘 보고 싶어 왔다) / just arrived: 완료")],
 [("I've never [[saw]] such a [[huge]] thing. I'm so [[scared]].", 0, 'seen', '나는 저렇게 거대한 것을 본 적이 없다. 너무 무섭다.', '정답 ▶ saw → seen\n이유: have + 과거분사'),
  ('We [[have]] lived in this city [[since]] ten [[years]].', 1, 'for', '우리는 10년 동안 이 도시에 살아 왔다.', '정답 ▶ since → for\n이유: for + 기간'),
  ('I [[have visited]] my grandparents [[last]] [[weekend]].', 0, 'visited', '나는 지난 주말에 조부모님을 방문했다.', '정답 ▶ have visited → visited\n이유: last weekend(명확한 과거)'),
  ('[[Have]] you ever [[be]] to [[Jeju-do]]?', 1, 'been', '너는 제주도에 가 본 적이 있니?', '정답 ▶ be → been'),
  ('She [[have]] [[already]] [[finished]] her homework.', 0, 'has', '그녀는 이미 숙제를 끝냈다.', '정답 ▶ have → has\n이유: 주어 She')],
 [("I've always wanted to see a dinosaur.", '저는 항상 공룡을 보고 싶었어요.'),
  ("We've just arrived in the jungle of 60 million years ago.", '우리는 방금 6천만 년 전의 정글에 도착했습니다.'),
  ("I've never seen such a huge thing.", '나는 저렇게 거대한 것을 본 적이 없다.'),
  ('My uncle has lived in Canada since 2010.', '삼촌은 2010년부터 캐나다에 살고 계신다.')]))

# ═════════ 8과 ② -thing + 형용사 ═════════
G8.append(day('e8b', '8과 문법 ② -thing + 형용사', 'something cold · anything foolish · nothing new · -thing + 형용사 + to부정사',
 [('-thing + 형용사 (뒤에서 꾸밈)', "I don't want you to do anything foolish. (교과서) / something cold / nothing new"),
  ('그냥 명사 thing은 앞에서', "I've never seen such a huge thing. (교과서) → 형용사 + thing"),
  ('something / anything / nothing', '긍정문 something · 부정문·의문문 anything · nothing = not ~ anything'),
  ('+ to부정사', 'something cold to drink (형용사 → to부정사 순서)')],
 [('"차가운 무언가"는 cold something이다.', False, '정답 ▶ F\n이유: -thing은 형용사가 뒤에 → something cold'),
  ("I don't want you to do anything foolish.에서 foolish는 anything을 꾸민다.", True, '정답 ▶ T\n이유: anything + 형용사 → 어리석은 어떤 것 (교과서 8과)'),
  ('"마실 차가운 것"은 something cold to drink 순서로 쓴다.', True, '정답 ▶ T\n이유: -thing + 형용사 + to부정사'),
  ('I saw a strange something.은 바른 문장이다.', False, '정답 ▶ F\n이유: I saw something strange.'),
  ("I've never seen such a huge thing.에서 huge가 thing 앞에 온 것은 틀렸다.", False, '정답 ▶ F\n이유: thing은 그냥 명사라 형용사가 앞에 와요. 뒤로 가는 건 something, anything, nothing 같은 -thing 한 단어')],
 [("I don't want you to do {anything foolish|foolish anything}.", '나는 당신이 어리석은 행동은 아무것도 하지 않기를 바랍니다.', '정답 ▶ anything foolish\n이유: -thing + 형용사 (교과서 8과)'),
  ('I need {something cold|cold something} to drink.', '나는 마실 시원한 것이 필요하다.', '정답 ▶ something cold\n이유: -thing + 형용사 + to부정사'),
  ('Did you hear {anything strange|strange anything} last night?', '어젯밤에 이상한 소리 들었니?', '정답 ▶ anything strange\n이유: -thing + 형용사'),
  ('There is {nothing new|new nothing} in his idea.', '그의 생각에는 새로운 것이 전혀 없다.', '정답 ▶ nothing new\n이유: -thing + 형용사'),
  ("I've never seen such a {huge thing|thing huge}.", '나는 저렇게 거대한 것을 본 적이 없다.', '정답 ▶ huge thing\n이유: thing(그냥 명사)은 형용사가 앞에 (교과서 8과)'),
  ('I want to eat something {sweet|sweetly}.', '나는 단것을 먹고 싶다.', '정답 ▶ sweet\n이유: 명사를 꾸미는 건 형용사. sweetly(부사) ✗'),
  ('I want something {warm to wear|to wear warm}.', '나는 입을 따뜻한 것을 원한다.', '정답 ▶ warm to wear\n이유: 형용사가 먼저, to부정사가 나중'),
  ('The kids are drawing something {funny|funnily}.', '그 아이들은 재미있는 무언가를 그리고 있다.', '정답 ▶ funny\n이유: something을 꾸미는 형용사')],
 [('빈칸에 알맞은 것은?<br><b>Jiho is hot. He wants to drink ______.</b>', ['something cold', 'cold something', 'anything cold to', 'something coldly', 'cold anything'],
   '정답 ▶ something cold\n이유: -thing + 형용사'),
  ('밑줄 친 형용사의 위치가 [보기]와 같은 것은?<br>[보기] I don\'t want you to do anything <u>foolish</u>.', ["There's nothing <u>wrong</u> with his answer.", 'She has a <u>cute</u> dog.', 'It is a <u>huge</u> thing.', 'The weather is <u>nice</u>.', 'He looks <u>tired</u>.'],
   "정답 ▶ There's nothing wrong with his answer.\n이유: -thing 뒤에서 꾸밈\n오답 ▶ 명사 앞(cute dog, huge thing) / 보어 자리(is nice, looks tired)"),
  ('대화의 빈칸에 알맞은 것은?<br><b>A: Mom, I\'m hungry. Is there ________ in the fridge?<br>B: There\'s some cake.</b>', ['anything delicious', 'delicious anything', 'something deliciously', 'delicious something', 'anything deliciously'],
   '정답 ▶ anything delicious\n이유: 의문문 → anything + 형용사'),
  ('우리말을 바르게 영작한 것은?<br><b>나는 어둠 속에서 이상한 무언가를 보았다.</b>', ['I saw something strange in the dark.', 'I saw strange something in the dark.', 'I saw something in the dark strange.', 'I strange saw something in the dark.'],
   '정답 ▶ I saw something strange in the dark.'),
  ('우리말을 바르게 영작한 것은?<br><b>나는 읽을 재미있는 무언가가 필요하다.</b>', ['I need something interesting to read.', 'I need something to read interesting.', 'I need interesting something to read.', 'I need to read something interesting thing.'],
   '정답 ▶ I need something interesting to read.\n이유: -thing + 형용사 + to부정사')],
 [('어법상 <b>옳은</b> 문장은?', ['I want to eat something sweet.', 'Did you see strange anything?', 'There is new nothing here.', 'I need cold something to drink.', 'She bought expensive something.'],
   '정답 ▶ I want to eat something sweet.'),
  ('어법상 <b>어색한</b> 문장은?', ['I have important something to tell you.', "There's nothing wrong with his answer.", 'The kids are drawing something funny.', 'Is there anything interesting on TV?', 'I heard something strange outside.'],
   '정답 ▶ I have important something to tell you.\n이유: something important to tell'),
  ('어법상 옳은 문장의 개수는?<br>• I need something warm to wear.<br>• Let\'s do exciting something.<br>• There is nothing special about it.<br>• I\'ve never seen such a huge thing.<br>• Do you want cold anything?', ['3개', '1개', '2개', '4개', '5개'],
   '정답 ▶ 3개\n틀린 것 ▶ exciting something → something exciting / cold anything → anything cold\n주의 ▶ such a huge thing은 맞아요(thing은 그냥 명사).', True),
  ('교과서 8과 "I don\'t want you to do anything foolish."의 의미로 알맞은 것은?', ['어리석은 행동은 아무것도 하지 않기를 바란다.', '어리석은 행동을 하나만 하길 바란다.', '아무것도 하지 않는 것은 어리석다.', '네가 어리석다고 생각하지 않는다.'],
   '정답 ▶ 어리석은 행동은 아무것도 하지 않기를 바란다.\n이유: Travis가 Eckels에게 한 경고예요.'),
  ('우리말을 바르게 영작한 것은?<br><b>맛있는 냄새가 나지 않니?</b>', ["Don't you smell something delicious?", "Don't you smell delicious something?", "Don't you smell something deliciously?", "Don't you smell deliciously something?"],
   "정답 ▶ Don't you smell something delicious?\n이유: something + 형용사(delicious)")],
 [("I don't want you to do [[foolish anything]]. [[Just]] stay [[calm]].", 0, 'anything foolish', '나는 당신이 어리석은 행동은 아무것도 하지 않기를 바랍니다. 그냥 침착하세요.', '정답 ▶ foolish anything → anything foolish'),
  ('I [[need]] [[cold something]] [[to drink]].', 1, 'something cold', '나는 마실 시원한 것이 필요하다.', '정답 ▶ cold something → something cold'),
  ('Did you [[hear]] [[anything]] [[strangely]] last night?', 2, 'strange', '어젯밤에 이상한 소리 들었니?', '정답 ▶ strangely → strange\n이유: anything을 꾸미는 형용사'),
  ('There [[is]] [[new nothing]] in [[his]] idea.', 1, 'nothing new', '그의 생각에는 새로운 것이 전혀 없다.', '정답 ▶ new nothing → nothing new'),
  ('I want something [[to wear warm]] [[for]] the [[trip]].', 0, 'warm to wear', '나는 여행을 위해 입을 따뜻한 것을 원한다.', '정답 ▶ to wear warm → warm to wear\n이유: 형용사 → to부정사 순서')],
 [("I don't want you to do anything foolish.", '나는 당신이 어리석은 행동은 아무것도 하지 않기를 바랍니다.'),
  ('I saw something strange in the dark.', '나는 어둠 속에서 이상한 무언가를 보았다.'),
  ('Jiho wants to drink something cold.', '지호는 시원한 것을 마시고 싶어 한다.'),
  ("There's nothing wrong with his answer.", '그의 대답에는 잘못된 것이 전혀 없다.')]))

for d in G7 + G8: ansfirst(d['steps'])
path = sys.argv[1] if len(sys.argv) > 1 else '/home/claude/proj/data/m2-donga-yoon-L7.js'
PK = json.loads(subprocess.check_output(['node', '-e', "global.window={};require('%s');process.stdout.write(JSON.stringify(window.PKG))" % path]))
base = [d for d in PK['days'] if not re.match(r'e[78][ab]$', d['id'])]
out = []
for d in base:
    out.append(d)
    if d['id'] == 'd2': out += G7
    if d['id'] == 'd4': out += G8
assert len(out) == len(base) + 4
PK['days'] = out
for i, d in enumerate(PK['days']): d['name'] = 'DAY %d' % (i + 1)
src = open(path, encoding='utf-8').read(); head = src[:src.index('window.PKG')]
if '7·8과 문법' not in head: head = head.rstrip('\n') + '\n/* 11/2: 7·8과 문법 각 과 본문 뒤에 추가(가주어 it·call A B / 현재완료·-thing+형용사) (gen/gen_m2d78gram.py) */\n'
write(PK, path, head)
print('ok', [(d['name'], d['id'], d['range'], len(d['steps'])) for d in PK['days']])
