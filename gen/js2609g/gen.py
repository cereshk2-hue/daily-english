# 11/28 중산고2 9월 모고 본문 어법 종합 35 (학교: 문법은 본문에서만 출제, 서술형 없음) → h2-mock-2609-jungsan 맨 끝 DAY g35
# 지문 19~24·26·29~42번(27번 안내문 제외) 문장만으로 6가지 각도: ①밑줄 틀린 곳 10 ②네모 (A)(B)(C) 6 ③옳은/틀린 문장 5 ④옳은 것 개수 4 ⑤같은 쓰임 5 ⑥바꿔 쓰기·영작·고친 것 5
# 바뀐 곳 말고는 원문 그대로 — 아래 assert로 확인(밑줄 표시를 뗀 문장 / 정답으로 고친 문장이 원문에 들어 있는지)
import json, re, subprocess, sys
sys.path.insert(0, '/home/claude/srcrepo/generators')
from gencommon import write
path = sys.argv[1] if len(sys.argv) > 1 else '/home/claude/proj/data/h2-mock-2609-jungsan.js'
PK = json.loads(subprocess.check_output(['node', '-e', "global.window={};require('%s');process.stdout.write(JSON.stringify(window.PKG))" % path]))
SRC = ' '.join(l[1] for d in PK['days'][:16] for l in d['passage'] if l[0] != '#').replace('’', "'")
C5 = ['①', '②', '③', '④', '⑤']; CNT = ['1개', '2개', '3개', '4개', '5개']
U = lambda n, w: '%s<u>%s</u>' % (C5[n - 1], w)
def P(*xs): return '<div class="wbox en">' + ''.join('<p>%s</p>' % x for x in xs) + '</div>'
# ① 밑줄 ①~⑤ 중 틀린 것: (번호, 본문(밑줄), 틀린 번호, 고친 말, 원문 확인용 고친 문장들, 해설)
S1 = [
 ('19번', "I ran into the music room, %s heavily. The rest of the band %s sitting with long faces. I sank into a chair. I had truly believed we would make it; our audition %s flawless. My chest felt %s as I asked, \"So, who won?\" I was %s back my tears." % (U(1, 'breathing'), U(2, 'were'), U(3, 'had been'), U(4, 'heavily'), U(5, 'holding')),
  4, 'heavy', ['My chest felt heavy as I asked'], "④ 감각동사 feel + 형용사 → heavy\n① 동시 동작 분사구문 ② 밴드 구성원들 → were(원문) ③ 믿었던 것보다 앞선 일 → 과거완료 ⑤ 과거진행형"),
 ('20번', "Only when you're happy that you've done the best you can for your story %s you show it to someone else. The most valuable feedback is likely %s from other sources. Fellow writers are ideal, but don't imagine that any writer %s. If you are part of a writers' circle or class, you'll know %s writing you admire, and if you've had feedback in the past you'll know whose opinions %s helpful." % (U(1, 'should'), U(2, 'to come'), U(3, 'will do'), U(4, 'whose'), U(5, 'has been')),
  5, 'have been', ["whose opinions have been helpful"], "⑤ 주어 opinions(복수) → have been\n① Only when ~ 부정어구가 앞에 → 도치 should you ② be likely to + 동사원형 ③ any writer will do(아무 작가나 괜찮다) ④ 뒤에 명사 writing → 소유격 관계사 whose"),
 ('21번', "An agenda with a meeting start time and a topic will probably %s before the meeting. This will serve as the trunk of the tree. But there's no expectation %s the meeting will progress in a linear manner. %s seemed like a priority last week when the agenda was crafted %s not necessarily the priority right now. Other branches may sprout as some members have urgent phone calls that %s them in and out of the meeting." % (U(1, 'be circulated'), U(2, 'which'), U(3, 'What'), U(4, 'is'), U(5, 'take')),
  2, 'that', ["there's no expectation that the meeting will progress"], "② 뒤에 빠진 것 없는 완전한 절 + expectation의 내용 → 동격 that (which ✘)\n① 안건이 '돌려지다' 수동 ③ ~한 것(선행사 없음) What ④ What절 주어는 단수 is ⑤ calls(복수) → take"),
 ('22번', "When we are \"always on\" we are constantly %s content. If we do it while we are eating, our multi-tasking %s us. It's easy %s a sandwich in a minute while %s on the phone. Some people are skilled at %s both at the same time." % (U(1, 'ingesting'), U(2, 'are overloading'), U(3, 'to eat'), U(4, 'talking'), U(5, 'doing')),
  2, 'is overloading', ["our multi-tasking is overloading us"], "② 주어 multi-tasking(단수) → is overloading\n① 진행형 ③ 가주어 It ~ 진주어 to eat ④ while (we are) talking ⑤ be skilled at + 동명사"),
 ('23번', "Music can bring us into a very comfortable rhythm, and it can be %s in and of itself. There needs to be a process that %s tension and drives the movement towards something in particular. The excitement %s arises in this process creates satisfaction and pleasure. Therefore, the fluid movement in the prelude usually creates a tension that can %s in the subsequent movement with a set rhythm. This, in turn, creates new and other types of tensions, %s the rhythm is unambiguous and predictable." % (U(1, 'satisfied'), U(2, 'creates'), U(3, 'that'), U(4, 'be released'), U(5, 'where')),
  1, 'satisfying', ["it can be satisfying in and of itself"], "① 음악이 만족감을 '주는' 것 → satisfying (satisfied는 사람이 만족한)\n② a process(단수) → creates ③ 주격 관계대명사 ④ 긴장이 '해소되다' 수동 ⑤ 뒤에 완전한 절 → 관계부사 where"),
 ('24번', "This means helping students %s how the architecture of a social media feed or a news site %s deliberately designed to distract or provoke them. Classes in media literacy traditionally cover how %s the credibility of sources. A student might be tasked with %s how many times they switch tasks or check their phone in an hour of homework. By treating these as deliberate design choices, young people become more critical users %s passive consumers." % (U(1, 'recognize'), U(2, 'are'), U(3, 'to evaluate'), U(4, 'tracking'), U(5, 'rather than')),
  2, 'is', ["or a news site is deliberately designed"], "② 주어 the architecture(단수) → is\n① help + 목적어 + (to) 동사원형 ③ how to + 동사원형 ④ 전치사 with + 동명사 ⑤ A rather than B"),
 ('26번', "Frederick Law Olmsted, %s as the father of American landscape architecture, was born in 1822. When Olmsted was young, he often went on trips to the countryside with his father, %s loved scenery. At age 14, he could not enter Yale College %s a severe sumac poisoning that damaged his eyesight. Instead of %s a college, he gained experience %s as a clerk, a sailor, and a farmer." % (U(1, 'known'), U(2, 'who'), U(3, 'due to'), U(4, 'attend'), U(5, 'working')),
  4, 'attending', ["Instead of attending a college"], "④ 전치사 of 뒤 → 동명사 attending\n① ~로 '알려진' 과거분사 ② 사람(father) + 계속적 용법 who ③ due to + 명사구 ⑤ gain experience (in) -ing"),
 ('29번', "Capitalism is not a system %s cash is everywhere but rather one %s islands of cash exchange exist within oceans of cheap natures. Reproducing life within the cash nexus %s expensive, and it grows more expensive over time. Workers' wages can be frozen, even %s back. Frontiers are so important in these processes because they offer places where the new cheap things can %s." % (U(1, 'where'), U(2, 'in which'), U(3, 'are'), U(4, 'rolled'), U(5, 'be seized')),
  3, 'is', ["Reproducing life within the cash nexus is expensive"], "③ 동명사구 주어(Reproducing life ~)는 단수 → is\n① 완전한 절 → 관계부사 where ② 전치사 + 관계대명사 ④ can be frozen, (be) rolled back 수동 병렬 ⑤ '빼앗기다' 수동"),
 ('31번', "As people find themselves regularly on the move, we are experiencing a phase shift: molecules heat up and loosen from one another, %s more rapidly. One might even say that humans are becoming like particles in quantum physics, %s velocity and location always in flux. It would be nice %s to some form of stability, but that's not %s things work in a quantum world. Instead, the complexity of today's world makes it increasingly difficult %s permanently anywhere." % (U(1, 'vibrating'), U(2, 'their'), U(3, 'to return'), U(4, 'what'), U(5, 'to settle')),
  4, 'how', ["but that's not how things work in a quantum world"], "④ 뒤에 완전한 절(things work) + '방식' → how (what ✘)\n① 분사구문 ② 독립분사구문(their velocity ~ (being) in flux) ③ 가주어 It ~ 진주어 to return ⑤ 가목적어 it ~ 진목적어 to settle"),
 ('34번', "When we focus on the obvious aspects of media, we miss the changes that %s over time but %s not apparent day to day. It %s in the early 1980s and revolutionized food preparation. Now, it was possible to prepare foods very quickly, and this shortening of preparation time was liberating for the cooks in the family, most of %s tended to be women. The effects of the microwave oven on family life were not anticipated and would have been difficult %s." % (U(1, 'accumulates'), U(2, 'are'), U(3, 'was introduced'), U(4, 'whom'), U(5, 'to foresee')),
  1, 'accumulate', ["the changes that accumulate over time"], "① 선행사 the changes(복수) → accumulate\n② that절 동사 병렬 are ③ 전자레인지가 '소개되다' 수동 ④ most of + 관계대명사 whom(접속사 역할) ⑤ 형용사 difficult를 꾸미는 to부정사"),
]
# ② 네모 (A)(B)(C): (번호, 본문, [정답 조합, 오답 조합 4], 해설, 원문 확인 문장들)
S2 = [
 ('32번', "Of the cognitive motivations, the most fundamental one encourages people (A)[to understand / understanding] their environment to predict what is going to happen in case of uncertainties. Most important, people prefer to develop meanings that (B)[are / is] shared with other people. It is easy to understand why living in the lounge (C)[is / being] problematic.",
  ['to understand – are – is', 'understanding – are – is', 'to understand – is – is', 'to understand – are – being', 'understanding – is – being'],
  "(A) encourage + 목적어 + to부정사 (B) 선행사 meanings(복수) → are (C) why절의 주어 living in the lounge(동명사구, 단수) + 동사 is", []),
 ('33번', "Grief is a dynamic emotional process (A)[essential / essentially] to consciousness. Grief work honours the loss, the sadness and the experience of diminishment or absence, while also (B)[setting / set] up the ground for self-transformation and the continuation of life. When we grieve for (C)[what / that] is lost, it clears the way towards a strengthening of love and commitment for what remains.",
  ['essential – setting – what', 'essentially – setting – what', 'essential – set – what', 'essential – setting – that', 'essentially – set – that'],
  "(A) 명사 process를 뒤에서 꾸미는 형용사 essential (B) while (it is) also setting — 능동 분사 (C) 전치사 for의 목적어 + 선행사 없음 → what", []),
 ('35번', "Digital twins are digital replicas of assets or activities (A)[using / used] modeling and sensors to create digital representations. However, faster wireless networks and the resulting availability of real-time data (B)[enable / enables] much more detailed and dynamic digital representations. When sensors collect data from a connected device, the sensor data can (C)[be used / use] to continuously update the digital twin.",
  ['using – enable – be used', 'used – enable – be used', 'using – enables – be used', 'using – enable – use', 'used – enables – use'],
  "(A) 복제본이 모델링·센서를 '사용하는' 능동 → using (B) 주어 networks and availability(복수) → enable (C) 데이터가 '사용되다' 수동", []),
 ('36번', "Many studies have shown that not only (A)[do animals have / animals have] a remarkable ability to seek out the best available locations for the necessities of life, but that they are able to anticipate how a setting will serve their future needs. The warbler establishes territories preferentially among the red spruce trees early in the summer months, (B)[even though / despite] these trees offer less food than the neighboring white spruce trees. Later, though, when nests are built and hungry baby birds need nourishment, it is the red spruce forest (C)[that / what] offers the easier pickings.",
  ['do animals have – even though – that', 'animals have – even though – that', 'do animals have – despite – that', 'do animals have – even though – what', 'animals have – despite – what'],
  "(A) 부정어 not only가 절 앞 → 도치 do animals have (B) 뒤에 절(these trees offer ~) → 접속사 even though (despite + 명사) (C) It is ~ that 강조 구문", []),
 ('37번', "They develop a culture-specific communication style (A)[that / what] is, for example, direct and explicit in individualistic cultures or indirect and implicit in collectivistic cultures. By contrast, the cultural assumptions of interdependence and harmony require that collectivists limit (B)[themselves / them] to implicit and even ambiguous use of words. The English language is the only language in the world (C)[that / who] spells I with a capital letter.",
  ['that – themselves – that', 'what – themselves – that', 'that – them – that', 'that – themselves – who', 'what – them – who'],
  "(A) 선행사 style이 있음 → 관계대명사 that (B) 주어 collectivists 자신을 제한 → 재귀대명사 themselves (C) 선행사 the only language(사물) → that", []),
 ('38번', "Usually, high density is needed for the phenomenon of crowding, (A)[which / that] makes people experience sensory overload, a lack of control, and rising stress and anxiety. However, some psychologists see crowding as neutral rather than invariably negative, and believe that people's moods and behaviors (B)[intensify / intensifies] as density increases. So if an individual is looking forward to a concert, say, the feeling of crowding (C)[enhances / enhance] their enjoyment of the performance.",
  ['which – intensify – enhances', 'that – intensify – enhances', 'which – intensifies – enhances', 'which – intensify – enhance', 'that – intensifies – enhance'],
  "(A) 콤마 뒤 계속적 용법 → which (that ✘) (B) 주어 moods and behaviors(복수) → intensify (C) 주어 the feeling(단수) → enhances", []),
]
# ③ 옳은/틀린 문장 고르기: (발문, [정답, 오답4], 해설)
S3 = [
 ('본문 문장 중 어법상 <u>옳은</u> 것은?', ["Interruptions, agenda changes, and frequent shifts in direction are seen as natural and necessary.", "It's easy eat a sandwich in a minute while talking on the phone.",
   "There need to be a process that creates tension and drives the movement.", "Olmsted could not enter Yale due to a severe sumac poisoning that damaged him eyesight.", "Workers' wages can be freezing, even rolled back."],
  "① 21번 원문 그대로 ✓\n② 가주어 It ~ 진주어 to eat ③ a process(단수) → There needs ④ 소유격 his eyesight ⑤ 임금이 '동결되다' → can be frozen"),
 ('본문 문장 중 어법상 <u>틀린</u> 것은?', ["The ability to select a set of surroundings suitable for foraging are one of the most important determinants of biological success.", "Grief can make us both very sad and very motivated to act.",
   "As time went on, fewer and fewer families sat down together to eat dinner.", "There is no Japanese equivalent for the English I.", "Positive social behaviors develop belonging and self-respect."],
  "① 주어 The ability(단수) → is (36번)\n② make + 목적어 + 형용사 ③ fewer and fewer + 복수 명사 ④⑤ 원문 그대로"),
 ('본문 문장 중 어법상 <u>틀린</u> 것은?', ["Exclusion is a state what is ignored by the organization psychologists.", "Individuals react to organizational exclusion by trying to strengthen their basic needs, which are threatened.",
   "However, individuals may be faced with more exclusion when they cannot adapt to a group.", "Precautions need to be taken regarding organizational exclusion, which is very important for business.", "When this situation is not avoided, exclusion increases even more."],
  "① 선행사 a state가 있음 → that(which) (39번)\n② 선행사 basic needs(복수) → are ③ be faced with ④ 계속적 용법 which ⑤ 원문 그대로"),
 ('본문 문장 중 어법상 <u>옳은</u> 것은?', ["Simply perceiving ourselves as people who do good deeds and behaving accordingly motivates us to do greater good in the future.", "Our adult brains retain a preference for perpetuate good, fair behavior.",
   "Subjects gave almost twice as much as those who had instructed to recall previous bad deeds.", "People who seemed concerned about appearances were less generously than those who cared more about doing good.", "Subjects who'd taken pains to describe how they'd been nice to others was likely to donate less."],
  "① 40번 원문 — 동명사구 주어(A and B를 하나의 행동으로) + motivates ✓\n② 전치사 for + 동명사 perpetuating ③ '지시받은' → had been instructed ④ be동사 뒤 형용사 generous ⑤ 주어 Subjects(복수) → were"),
 ('본문 문장 중 어법상 <u>틀린</u> 것은?', ["By curate what we see, algorithms subtly nudge us towards particular paths.", "The design of the environment in which choices are made can significantly influence the decisions people make.",
   "It requires a conscious effort to maintain critical engagement with the technologies we use.", "It means actively seeking out diverse perspectives and challenging algorithmic recommendations.", "These systems are designed by humans with specific goals."],
  "① 전치사 By + 동명사 curating (41~42번)\n② 전치사 + 관계대명사 in which ③ effort를 꾸미는 to부정사 ④ mean + 동명사 병렬 ⑤ 수동태"),
]
# ④ 옳은 것 개수: (본문 줄들, 정답 개수 a(0=1개), 해설)
S4 = [
 (["ⓐ Immy looked up at me and shook her head.", "ⓑ A band calling A Happy Accident won.", "ⓒ Since you were late, we decided to play a joke on you!", "ⓓ My heart was racing with excite.", "ⓔ You may well wanting to show it to your nearest and dearest."], 1,
  "옳은 것 ⓐⓒ → 2개\nⓑ '~라고 불리는' → called ⓓ 전치사 with + 명사 excitement ⓔ may well + 동사원형 want"),
 (["ⓐ Progressive educators and librarians are developing curricula to teach attention literacy.", "ⓑ Why does an app use infinite scrolling instead of pages?", "ⓒ Why do notifications appearing with specific colors and sounds?", "ⓓ In 1858, he worked with Calvert Vaux and won the design competition.", "ⓔ Although he passed away in 1903, his sons and successors continued his design philosophy."], 3,
  "옳은 것 ⓐⓑⓓⓔ → 4개\nⓒ do + 주어 + 동사원형 appear"),
 (["ⓐ Some people are more likely to cheat after purchase eco-friendly products.", "ⓑ People who experience eco-guilt seek pro-environmental actions to compensate for this guilt.", "ⓒ People are inclined to believing in quick-fixes.", "ⓓ When people are reminded of deeds they have done, they might be left with a feeling of eco-guilt.", "ⓔ People are more likely signing a petition after viewing evidence of environmental damage."], 1,
  "옳은 것 ⓑⓓ → 2개\nⓐ 전치사 after + 동명사 purchasing ⓒ be inclined to + 동사원형 believe ⓔ be likely to + 동사원형 sign"),
 (["ⓐ Quite a few students end up living in dorm lounges or campus hotels.", "ⓑ Students in a hotel get private bathrooms, their own TV, and larger rooms.", "ⓒ They must wait in uncertainty before find their social niche.", "ⓓ Most of us notice the obvious aspects of a new medium while missing the more subtle aspects.", "ⓔ Meals that took a long time to prepare was a luxury of the past."], 2,
  "옳은 것 ⓐⓑⓓ → 3개\nⓒ 전치사 before + 동명사 finding ⓔ 주어 Meals(복수) → were (원문 became)"),
]
# ⑤ 같은 쓰임: (발문, 주어진 문장, [정답, 오답4], 해설)
S5 = [
 ('밑줄 친 that과 쓰임이 같은 것은?', "But there's no expectation <u>that</u> the meeting will progress in a linear manner.",
  ["The news that he won the prize surprised everyone.", "Some members have urgent phone calls that take them in and out of the meeting.", "It is the red spruce forest that offers the easier pickings.", "I think that she is honest.", "This is the music that we played at the audition."],
  "주어진 that = 앞 명사(expectation)의 내용을 설명하는 동격 that → ① The news = 그가 상을 받았다는 것\n② ⑤ 관계대명사 ③ 강조 구문 ④ 목적어절 접속사"),
 ('밑줄 친 It과 쓰임이 같은 것은?', "<u>It</u>'s easy to eat a sandwich in a minute while talking on the phone.",
  ["It would be nice to return to some form of stability.", "It was introduced in the early 1980s.", "It is the red spruce forest that offers the easier pickings.", "Eat your sandwich. Taste it.", "It requires a conscious effort."],
  "주어진 It = 가주어(진주어 to eat ~) → ① 진주어 to return ~\n② ④ ⑤ 앞에 나온 것을 가리키는 대명사 ③ 강조 구문 It"),
 ('밑줄 친 to부정사와 쓰임이 같은 것은?', "It requires a conscious effort <u>to maintain</u> critical engagement with the technologies we use.",
  ["The ability to select a set of surroundings is one of the most important determinants.", "Volunteers will plant native tree seedlings to help restore the local environment.", "People prefer to develop meanings that are shared with other people.",
   "A student might track the time to raise self-awareness about fragmentation.", "It would be nice to return to some form of stability."],
  "주어진 to maintain = 앞 명사 effort를 꾸미는 형용사적 용법 → ① ability를 꾸밈\n② ④ 목적(~하기 위해) ③ prefer의 목적어(명사적) ⑤ 진주어(명사적)"),
 ('밑줄 친 -ing와 쓰임이 같은 것은?', "I ran into the music room, <u>breathing</u> heavily.",
  ["Collectivists limit themselves to implicit use of words, using terms like maybe, perhaps, or probably.", "Reproducing life within the cash nexus is expensive.", "Some people are skilled at doing both at the same time.",
   "Classes in media literacy now include recognizing clickbait.", "Instead of attending a college, he gained experience."],
  "주어진 breathing = 동시 동작을 나타내는 분사구문 → ① using ~\n②~⑤ 모두 동명사(주어·전치사 목적어·동사 목적어)"),
 ('밑줄 친 부분처럼 주어와 동사의 어순이 바뀐(도치) 것은?', "Only when you're happy that you've done the best you can for your story <u>should you show</u> it to someone else.",
  ["Not only do animals have a remarkable ability to seek out the best locations.", "Why does an app use infinite scrolling instead of pages?", "So, who won?", "Don't imagine that any writer will do.", "Eat your sandwich. Taste it."],
  "주어진 문장 = 부정어구(Only when ~)가 앞에 와서 생긴 도치 → ① Not only가 앞 → do animals have\n② 의문문 어순 ③ 의문사 주어 ④ ⑤ 명령문"),
]
# ⑥ 바꿔 쓰기·영작·고친 것: (발문, [정답, 오답4], 해설)
S6 = [
 ('다음 문장과 뜻이 같고 어법상 옳은 것은?<br><span class="en">Only when you\'re happy that you\'ve done the best you can should you show it to someone else.</span>',
  ["You should show it to someone else only when you're happy that you've done the best you can.", "Only when you're happy that you've done the best you can you should show it to someone else.",
   "You should not show it to anyone when you're happy that you've done the best you can.", "Only when should you be happy that you've done the best you can.", "When you're happy that you've done the best you can, you should never show it to anyone."],
  "도치를 풀면 You should show it ~ only when ~ ✓\n② Only when ~이 앞이면 도치 필수 ③ ⑤ 뜻이 반대 ④ 문장이 성립하지 않음"),
 ('밑줄 친 부분을 바꿔 쓸 때 가장 알맞은 것은?<br><span class="en">Most of us notice the obvious aspects of a new medium or technology <u>while missing</u> the more subtle aspects.</span>',
  ['while we miss', 'while we are missed', 'while missed', 'because we miss', 'while to miss'],
  "while missing = while we miss (분사구문 앞 접속사 남김, 주어가 같아 생략)\n② ③ 수동은 뜻이 다름 ④ 이유로 바뀜 ⑤ while + to부정사 ✘"),
 ('다음 문장과 뜻이 같고 어법상 옳은 것은?<br><span class="en">The effects of the microwave oven on family life would have been difficult to foresee.</span>',
  ["It would have been difficult to foresee the effects of the microwave oven on family life.", "The effects of the microwave oven on family life would have been difficult to foresee them.",
   "It would have been difficult to be foreseen the effects of the microwave oven.", "The effects of the microwave oven would have difficult to foresee.", "It would be difficult to foresee the effects of the microwave oven now."],
  "가주어 It ~ to foresee + 목적어 ✓\n② 주어가 이미 foresee의 목적어 → them 중복 ✘ ③ to be foreseen 뒤 목적어 ✘ ④ have been 빠짐 ⑤ 시제·뜻이 다름"),
 ('다음 우리말을 영어로 바르게 옮긴 것은?<br>학생은 숙제하는 한 시간 동안 몇 번이나 과제를 바꾸는지 기록하는 일을 맡을 수도 있다.',
  ["A student might be tasked with tracking how many times they switch tasks in an hour of homework.", "A student might be tasked with track how many times they switch tasks in an hour of homework.",
   "A student might be tasked to tracking how many times they switch tasks in an hour of homework.", "A student might be tasked with tracking how many times do they switch tasks in an hour of homework.",
   "A student might be tasked with tracking how much times they switch tasks in an hour of homework."],
  "be tasked with + 동명사, 간접의문문 어순 how many times + 주어 + 동사 ✓\n② 동명사 tracking ③ with ④ 간접의문문은 do 없이 평서문 어순 ⑤ times(셀 수 있음) → many"),
 ('밑줄 친 부분 중 어법상 틀린 곳을 바르게 고친 것은?<br><span class="en">In their search for such a balance, people are inclined to <u>believe</u> in "quick-fixes," because they want to <u>re-establish</u> the moral balance and <u>escape</u> the guilt as <u>quick</u> and easily as possible.</span>',
  ['quick → quickly', 'believe → believing', 're-establish → re-establishing', 'escape → escaping', 'are inclined → inclined'],
  "as ~ as possible 사이, 동사 escape를 꾸미고 easily와 병렬 → 부사 quickly\nbe inclined to + 동사원형 / want to re-establish ~ and (to) escape 병렬 — 모두 옳음"),
]
# ── 원문 확인: 정답으로 고친 본문을 문장으로 쪼개 원문에 있는지 (줄인 문장은 목록으로 보여 주고 눈으로 확인) ──
MISS = []
def chk_in(s, strict=True):
    t = re.sub(r'<[^>]+>', '', s).replace('&nbsp;', ' ').strip().rstrip('.')
    if t not in SRC:
        assert not strict, t
        MISS.append(t)
def sents(x): return [y for y in re.split(r'(?<=[.?!"])\s+', x) if y]
for no, body, w, fix, oks, ex in S1:
    for o in oks: chk_in(o)
    k = [0]
    def rp(m):
        k[0] += 1; return fix if k[0] == w else m.group(1)
    full = re.sub(r'[①②③④⑤]<u>(.*?)</u>', rp, body)
    for x in sents(full): chk_in(x, False)
for no, body, opts, ex, _ in S2:
    plain = re.sub(r'\(([ABC])\)\[([^/\]]+?) / [^\]]+\]', lambda m: m.group(2), body)
    for x in sents(plain): chk_in(x, False)
for q, opts, ex in S3:
    if '원문' in ex.split('\n')[0]: chk_in(opts[0])
items = []
def mc(q, opts, ex, a=None, keep=False, step=''):
    assert len(opts) == 5 and len(set(opts)) == 5, q
    d = {'q': q, 'opts': opts, 'ex': ex}
    if keep: d['keep'] = True; d['a'] = a
    return d
st1 = [mc('다음 글(%s)의 밑줄 친 ①~⑤ 중 어법상 <u>틀린</u> 것은?' % no + P(body), C5, '정답 ▶ %s (%s)\n%s' % (C5[w - 1], fix, ex), w - 1, True) for no, body, w, fix, oks, ex in S1]
st2 = [mc('다음 글(%s)의 (A), (B), (C)에서 어법에 맞는 것끼리 짝지은 것은?' % no + P(re.sub(r'\(([ABC])\)\[([^\]]+)\]', r'(\1) [ \2 ]', body)), opts, '정답 ▶ %s\n%s' % (opts[0], ex)) for no, body, opts, ex, _ in S2]
st3 = [mc(q, opts, '정답 ▶ %s\n%s' % (opts[0][:40] + ('…' if len(opts[0]) > 40 else ''), ex)) for q, opts, ex in S3]
st4 = [mc('다음 중 어법상 옳은 문장의 <b>개수</b>는?' + P(*lines), CNT, '정답 ▶ %s\n%s' % (CNT[a], ex), a, True) for lines, a, ex in S4]
st5 = [mc(q + P(given), opts, '정답 ▶ %s\n%s' % (opts[0][:40] + '…', ex)) for q, given, opts, ex in S5]
st6 = [mc(q, opts, '정답 ▶ %s\n%s' % (opts[0][:40] + ('…' if len(opts[0]) > 40 else ''), ex)) for q, opts, ex in S6]
assert len(st1) + len(st2) + len(st3) + len(st4) + len(st5) + len(st6) == 35
day = {'id': 'g35', 'name': '', 'range': '9월 모고 본문 어법 종합 35 (다양한 각도)', 'story': '19~24·26·29~42번 본문 문장만으로 — 밑줄 틀린 곳 · 네모 어법 · 옳은/틀린 문장 · 개수 · 같은 쓰임 · 바꿔 쓰기',
       'passage': [['#', '본문 어법 종합 — 각 문제 안에 본문이 들어 있어요 (바른 본문은 해설에서)', '']],
       'steps': [
        {'type': 'mc', 'title': '① 밑줄 틀린 곳 (10)', 'guide': '지문의 밑줄 친 ①~⑤ 중 어법상 틀린 것을 고르세요. 바뀐 곳 말고는 본문 그대로예요.', 'items': st1},
        {'type': 'mc', 'title': '② 네모 (A)(B)(C) 어법 (6)', 'guide': '(A), (B), (C) 각 네모에서 어법에 맞는 표현을 골라 짝지은 것을 고르세요.', 'items': st2},
        {'type': 'mc', 'title': '③ 옳은 문장 · 틀린 문장 (5)', 'guide': '본문 문장을 살짝 바꿨어요. 어법상 옳은(틀린) 문장을 고르세요.', 'items': st3},
        {'type': 'mc', 'title': '④ 옳은 문장 개수 (4)', 'guide': 'ⓐ~ⓔ 중 어법상 옳은 문장이 몇 개인지 고르세요.', 'items': st4},
        {'type': 'mc', 'title': '⑤ 같은 쓰임 (5)', 'guide': '밑줄 친 부분과 쓰임(문법 기능)이 같은 것을 고르세요.', 'items': st5},
        {'type': 'mc', 'title': '⑥ 바꿔 쓰기 · 영작 · 고친 것 (5)', 'guide': '뜻이 같은 문장, 바른 영작, 바르게 고친 것을 고르세요.', 'items': st6}]}
src = open(path, encoding='utf-8').read()
cut = re.search(r'\n/\* [A-Z0-9]+-TESTS', src).start() + 1
head, tail = src[:cut], src[cut:]
PK2 = json.loads(subprocess.check_output(['node', '-e', "global.window={};eval(require('fs').readFileSync(0,'utf8'));process.stdout.write(JSON.stringify(window.PKG))"], input=head.encode()))
head = head[:head.index('window.PKG')]
PK2['days'] = [d for d in PK2['days'] if d['id'] != 'g35'] + [day]
for i, d in enumerate(PK2['days']): d['name'] = 'DAY %d' % (i + 1)
if 'js2609g' not in head: head = head.rstrip('\n') + '\n/* 11/28: 본문 어법 종합 35 DAY g35 (gen/js2609g/gen.py) */\n'
write(PK2, path, head)
open(path, 'a', encoding='utf-8').write(tail)
from collections import Counter
print('원문과 다른(줄인) 문장:', *MISS, sep='\n  ')
print(len(PK2['days']), PK2['days'][-1]['name'], 'keep 정답 분포', Counter(x['a'] for s in day['steps'] for x in s['items'] if x.get('keep')))
