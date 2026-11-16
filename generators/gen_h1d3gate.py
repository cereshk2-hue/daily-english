# 11/16 저녁 안곡고1 공통영어2 동아(이병민) 3과·4과 본문 '어법 선택 한 판' DAY (맨 끝) — 선생님 자료: 3과 워크북 6 어법 선택형 연습 hwp
# 덩이 1 = 본문 ❶❷(도입 · PROS), 덩이 2 = 본문 ❸❹(CONS · COMMENTS). {정답|오답} — 앱이 보기 순서를 섞음
import sys, json, re, subprocess
sys.path.insert(0, '/tmp/claude-0/-home-claude/a9e3e882-1f02-5d62-8f70-aced81bc59d2/scratchpad'); sys.path.insert(0, '/home/claude/srcrepo/generators')
from gencommon import write
path = sys.argv[1] if len(sys.argv) > 1 else '/home/claude/proj/data/h1-donga-lee-L3.js'
PK = json.loads(subprocess.check_output(['node', '-e', "global.window={};require('%s');process.stdout.write(JSON.stringify(window.PKG))" % path]))
C1 = [
 ("Social media algorithms {play|playing} a huge role in our everyday lives.", "소셜 미디어 알고리즘은 우리의 일상생활에서 큰 역할을 한다.", "주어 algorithms 뒤 동사 자리 → play (playing은 동사가 못 됨)"),
 ("They make our lives {easier|more easily} by presenting us with options {that|what} we may be interested in.", "그것은 우리가 흥미를 느낄 만한 선택지들을 제시함으로써 우리의 삶을 더 편하게 만들어 준다.", "make + 목적어 + 형용사 보어 → easier / 선행사 options가 있음 → 관계대명사 that (what은 선행사 없이)"),
 ("Algorithms decide which content {is shown|to show} to us.", "알고리즘은 어떤 콘텐츠가 우리에게 보여질지 결정한다.", "간접의문문 which content + 동사, 콘텐츠가 '보여지는' 것 → 수동태 is shown"),
 ("They also determine the order of the content {that|what} appears on our social media feed.", "그것은 우리의 소셜 미디어 피드에 뜨는 콘텐츠의 순서도 결정한다.", "선행사 the content → 관계대명사 that"),
 ("If we are using an app {to watch|watch} videos, for example, we may see suggestions for related videos.", "예를 들어, 영상을 보려고 앱을 사용한다면 연관 영상에 대한 제안을 보게 될 수 있다.", "'~하기 위해'(목적) → to watch"),
 ("These recommendations are not random. They are based on our previous activity — {what|that} we've watched or clicked on in the past.", "이러한 추천은 무작위가 아니다. 그것은 우리의 이전 활동, 즉 과거에 시청한 것이나 클릭한 것들을 토대로 한다.", "선행사 없이 '~한 것' + 뒤가 불완전(watched의 목적어 없음) → what"),
 ("This information is fed into an algorithm, {which|that} then decides {what|which} we will see.", "이러한 정보는 알고리즘에 입력되고 그것은 우리가 무엇을 보게 될지 결정한다.", "콤마 뒤 계속적 용법 → which (that ✘) / '무엇을' 볼지 → what"),
 ("Social media algorithms are all around us, but they are a double-edged sword {that|what} can bring both benefits and problems.", "소셜 미디어 알고리즘은 우리 주변 어디에나 있는데, 그것은 이점과 문제점을 둘 다 가져올 수 있는 양날의 검이다.", "선행사 a double-edged sword → that"),
 ("Let's {look|looked} at some pros and cons of social media algorithms.", "소셜 미디어 알고리즘에 대한 찬반양론을 살펴보자.", "Let's + 동사원형 → look"),
 ("Algorithms make it easier for us {to find|finding} the information we need.", "알고리즘은 우리가 필요한 정보를 찾는 것을 더 쉽게 해 준다.", "가목적어 it ~ (for 의미상 주어) 진목적어 to부정사 → to find"),
 ("There is a lot of information {available|availably} on social media.", "소셜 미디어에는 이용할 수 있는 많은 정보가 있다.", "명사 information을 뒤에서 꾸미는 형용사 → available"),
 ("To find {what|that} we're looking for, we must sort through a lot of irrelevant information. Algorithms do this job for us.", "우리가 찾고 있는 것을 발견하려면 많은 양의 관련 없는 정보를 살펴보아야 한다. 알고리즘은 우리를 위해 이 일을 해 준다.", "선행사 없이 '~하는 것' + 뒤가 불완전(looking for의 목적어 없음) → what"),
 ("If we're trying {to decide|decide} on an item to buy, for example, they remember {which|that} brands we looked at or purchased in the past.", "예를 들어, 우리가 어떤 물건을 살지 정하려고 한다면 알고리즘은 우리가 과거에 보았거나 구매했던 브랜드를 기억한다.", "try + to부정사 : ~하려고 애쓰다 → to decide / '어떤' 브랜드 + 명사 → 의문형용사 which"),
 ("They also show us stories {related|relate} to topics we've clicked on.", "우리가 클릭했던 주제와 관련된 이야기들도 보여 준다.", "명사 stories를 꾸미는 과거분사(관련된) → related"),
 ("If algorithms did not exist, we {would|will} have a harder time {searching|search} for {what|that} we want.", "알고리즘이 존재하지 않는다면 우리는 원하는 것을 찾느라 더 어려움을 겪을 것이다.", "가정법 과거(If + 과거) → would / have a hard time + -ing → searching / '~하는 것' + want의 목적어 없음 → what"),
 ("They allow us {to spend|spending} less time searching and more time {enjoying|enjoy} {what|which} we're interested in.", "그것은 우리가 검색하는 데 드는 시간을 줄여주고 관심 있는 것을 즐길 수 있는 시간이 더 많아지도록 해 준다.", "allow + 목적어 + to부정사 → to spend / spend time + -ing (searching과 나란히) → enjoying / 선행사 없이 '~한 것' → what"),
 ("Algorithms help us stay {connected|connecting} to our loved ones and meet new people.", "알고리즘은 사랑하는 이들과의 관계를 유지하고 새로운 사람들을 만날 수 있게 돕는다.", "stay connected : 연결된 상태로 있다 (우리가 '연결되는' 것 → 과거분사)"),
 ("Have you ever noticed that posts from your close friends on social media usually {appear|appearing} at the top?", "소셜 미디어에서 친한 친구들의 게시물이 가장 상단에 뜨는 것을 알고 있었는가?", "that절 주어 posts 뒤 동사 자리 → appear"),
 ("This doesn't {happen|happen to} by chance. It is the work of algorithms.", "이것은 우연히 일어나지 않는다. 그것은 알고리즘이 한 일이다.", "happen은 자동사 → happen by chance (to ✘)"),
 ("They keep track of the people we {interact|interacting} with the most on social media.", "알고리즘은 우리가 소셜 미디어에서 가장 많이 소통하는 사람들을 계속 파악한다.", "목적격 관계대명사 생략: the people (whom) we interact with → 주어 we 뒤 동사 interact"),
 ("This allows us {to stay|staying} in touch with the people we {care|caring} about. They can also connect us with new people.", "이를 통해 우리가 관심을 기울이는 사람들과 연락을 유지할 수 있게 해 준다. 알고리즘은 우리를 새로운 사람들과 연결해 줄 수도 있다.", "allow + 목적어 + to부정사 → to stay / (whom) we care about → 동사 care"),
 ("By showing us posts of users {who|what} have similar ideas and interests, social media algorithms can help us {find|finding} or even form communities with people who share the same interests.", "비슷한 생각과 관심사를 가진 사용자들의 게시물을 보여줌으로써 소셜 미디어 알고리즘은 우리가 같은 관심사를 공유하는 사람들의 커뮤니티를 찾거나 심지어 형성하는 것을 도울 수 있다.", "선행사 users(사람) → who / help + 목적어 + (to) 동사원형, form과 나란히 → find"),
]
C2 = [
 ("Algorithms {promote|promoting} information bias.", "알고리즘은 정보 편향을 촉진한다.", "주어 Algorithms 뒤 동사 자리 → promote"),
 ("Social media algorithms organize content {based|base} on our previous activities — likes, dislikes, and search history.", "소셜 미디어 알고리즘은 좋아요, 싫어요, 검색 기록과 같은 우리의 이전 활동을 기반으로 콘텐츠를 구성한다.", "based on ~ : ~을 바탕으로 (과거분사)"),
 ("If you {like|liked} an article or a post, algorithms will show you similar content.", "만약 당신이 어떤 기사나 게시물을 좋아하면, 알고리즘은 이와 유사한 콘텐츠를 보여 줄 것이다.", "조건(If)절은 현재가 미래를 대신 → like (주절 will show)"),
 ("This means they prevent us from {discovering|discover} information {that|what} offers a different point of view.", "이는 우리가 다른 관점을 제공하는 정보를 발견하는 것을 막는다는 뜻이다.", "prevent A from -ing → discovering / 선행사 information → that"),
 ("It causes us {to have|have} information bias, or a false sense that {what|that} we think is the norm of society.", "그것은 우리로 하여금 정보 편향 또는 우리가 생각하는 것이 사회의 표준이라는 잘못된 인식을 갖게 한다.", "cause + 목적어 + to부정사 → to have / '우리가 생각하는 것'(주어 자리, think의 목적어 없음) → what"),
 ("As a result, our range of knowledge remains {narrow|narrowly} and our opinions don't change.", "결과적으로 우리의 지식 범위는 좁은 채로 남고 우리의 의견은 변하지 않게 된다.", "remain + 형용사 보어 → narrow (부사 ✘)"),
 ("This is especially {dangerous|danger} when it comes to controversial topics.", "이는 논쟁적인 주제에 있어서 특히 위험하다.", "be동사 + 보어, especially(부사)의 꾸밈을 받는 형용사 → dangerous"),
 ("Algorithms can {contribute to|contribute} social media addiction.", "알고리즘은 소셜 미디어 중독의 원인이 될 수 있다.", "contribute to ~ : ~의 원인이 되다, ~에 기여하다 (to 필요)"),
 ("As we all know, social media can be very {addictive|addict}.", "모두 알다시피 소셜 미디어는 매우 중독적일 수 있다.", "be + 형용사 보어(very의 꾸밈) → addictive (addict는 명사·동사)"),
 ("It presents us with posts, articles, and information {that|what} look important or interesting.", "그것은 우리에게 중요해 보이거나 흥미로워 보이는 게시물, 기사, 정보를 제공한다.", "선행사 posts, articles, and information → that"),
 ("Social media algorithms ensure {that|what} we have a continuous stream of content on our screens, {which|and} makes {it|them} hard for us to look away.", "소셜 미디어 알고리즘은 끊임없는 콘텐츠를 화면에 띄워서 우리가 눈을 떼기 어렵게 만든다.", "뒤가 완전한 문장(목적어절) → that / 콤마 뒤 앞 내용 전체를 받아 주어 역할 → which (and는 주어가 없어 ✘) / 가목적어 it ~ to look away → it"),
 ("So we end up {spending|to spend} hours and hours online.", "그렇게 우리는 몇 시간이고 온라인에서 시간을 보내게 된다.", "end up + -ing : 결국 ~하게 되다 → spending"),
 ("Social media addiction is a serious issue for some people. It can have a harmful effect on their studies, work, personal relationships, and even {mental|mentally} health.", "소셜 미디어 중독은 어떤 사람들에게는 심각한 문제이다. 그것은 학업, 업무, 대인 관계, 그리고 심지어 정신 건강에도 해로운 영향을 미칠 수 있다.", "명사 health를 꾸미는 형용사 → mental"),
 ("I think social media algorithms make my life {easier|more easily}.", "난 소셜 미디어 알고리즘이 내 삶을 더 편하게 만들어 준다고 생각해요.", "make + 목적어 + 형용사 보어 → easier"),
 ("They help me a lot when I'm looking for songs or movies {that|what} suit my taste.", "내 취향에 맞는 노래나 영화를 찾을 때 큰 도움을 주거든요.", "선행사 songs or movies → that"),
 ("I've {discovered|discovering} some of my favorite directors and musical artists thanks to algorithms.", "알고리즘 덕분에 내가 좋아하는 감독과 음악가를 알게 되었어요.", "현재완료 have + p.p. → discovered"),
 ("It feels like algorithms know me better {than|to} I know myself!", "알고리즘이 나 자신보다 나를 더 잘 아는 것처럼 느껴져요!", "비교급 better + than"),
 ("We can't {ignore|be ignored} the negative aspects of social media algorithms.", "우리는 소셜 미디어 알고리즘의 부정적인 측면을 무시할 수 없어요.", "우리가 '무시하는' 것, 뒤에 목적어 있음 → 능동 ignore"),
 ("People share fake news on social media, not {paying|pay} attention to whether or not the information {is|being} accurate.", "사람들은 정보가 정확한지에 대해 신경 쓰지 않고 소셜 미디어에서 가짜 뉴스를 공유해요.", "분사구문(부정은 not + -ing) → paying / whether절의 주어 the information 뒤 동사 → is"),
 ("Fake news spreads rapidly through algorithms and {impacts|impact} our society.", "가짜 뉴스는 알고리즘을 통해 빠르게 확산되어 우리 사회에 영향을 미쳐요.", "주어 Fake news(단수), spreads와 and로 나란히 → impacts"),
 ("It is a bad idea {to depend|depend} on social media for all of our information.", "모든 정보를 소셜 미디어에 의존하는 것은 좋은 생각이 아니에요.", "가주어 It ~ 진주어 to부정사 → to depend"),
 ("We need to {seek|seeking} out different sources as well, such as books, official news websites, and documentaries.", "우리는 책, 공식 뉴스 웹사이트, 다큐멘터리와 같은 여러 다른 출처를 찾아봐야 해요.", "need to + 동사원형 → seek"),
 ("This will prevent us from {having|have} information bias by {exposing|expose} us to fresh and different perspectives.", "이는 우리에게 새롭고 다양한 관점을 접하게 함으로써 정보 편향을 갖게 되는 것을 막아 줄 거예요.", "prevent A from -ing → having / 전치사 by 뒤 동명사 → exposing"),
]

# 4과 (선생님 자료: 4과 워크북 6 어법 선택형 연습 hwp) 덩이 1 = 본문 ❶❷(도입 · 다빈치), 덩이 2 = 본문 ❸❹❺(반 고흐 · 야경)
C3 = [
 ("You might have heard the expression, \"There is more than {meets|meet} the eye.\"", "여러분은 '눈에 보이는 것이 다가 아니다.'라는 표현을 들어 보았을 것입니다.", "주어 역할의 than(유사관계대명사) 뒤 동사, 단수 취급 → meets (관용 표현 There is more than meets the eye)"),
 ("It means that there {is|are} more to something than there {appears|appear} to be at first. This can apply to art as well.", "처음 보이는 것 외에 더 많은 것이 있다는 의미입니다. 이 말은 예술에도 적용될 수 있습니다.", "there is + 단수 주어 more → is / there appears to be (단수) → appears"),
 ("We appreciate art by looking at its colors, shapes, shadows, as well as the overall beauty {presented|presenting} by the artist.", "우리는 예술가가 표현한 전체적인 아름다움뿐만 아니라 색상, 형태, 음영을 보며 예술을 감상합니다.", "아름다움이 예술가에 의해 '표현된' → 과거분사 presented (by the artist)"),
 ("Sometimes, however, there {is|are} something more to the images in front of our eyes.", "그러나 때로는 우리 눈앞에 있는 그림에 무언가가 더 있습니다.", "주어 something(단수) → is"),
 ("Science, {which|that} seems far removed from art, can be the key to {seeing|see} beyond {what|which} the naked eye can see.", "과학은 예술과 동떨어져 보이지만 맨눈으로 볼 수 있는 것 너머를 보게 해 주는 실마리가 될 수 있습니다.", "콤마 사이 계속적 용법 → which (that ✘) / the key to + 동명사(to는 전치사) → seeing / 선행사 없이 '~하는 것' → what"),
 ("Today, I would like {to open|open} your eyes and minds through the following paintings.", "오늘 저는 다음 그림들을 통해 여러분의 눈과 마음을 열어보려고 합니다.", "would like + to부정사 → to open"),
 ("Look at the portrait of a woman on the next page. What {catches|catching} your eye?", "다음 페이지에 있는 한 여인의 초상화를 보세요. 무엇이 여러분의 시선을 사로잡나요?", "의문사 주어 What(단수) + 동사 → catches"),
 ("{What|That} draws most people's attention initially {is|are} not the woman but the beautiful white animal in the woman's arms.", "대부분 사람들의 관심을 처음 끌어당기는 것은 여인이 아닌 그녀의 품속에 있는 아름다운 흰 동물입니다.", "'~하는 것'(주어절, draws의 주어 없음) → What / What절 주어는 단수 → is"),
 ("In 2014, this painting by Leonardo da Vinci was {analyzed|analyzing} by an engineer.", "레오나르도 다빈치가 그린 이 그림은 2014년에 한 기술자에 의해 분석되었습니다.", "그림이 '분석된' 것 → 수동태 was analyzed"),
 ("He used special equipment to look beneath the surface of the painting and discovered {that|what} it had different layers, like {those|that} of an onion.", "그는 그림의 표면 아래를 보기 위해 특수 장비를 사용했고 그 그림에 양파처럼 여러 겹의 층이 있다는 것을 발견했습니다.", "뒤가 완전한 문장(목적어절) → that / 앞의 복수 명사 layers를 받음 → those"),
 ("After careful examination of the layers, it was revealed {that|what} the original painting was just a normal portrait of a woman by herself.", "그 층을 면밀히 조사한 후에 원래 그림은 여인만 있는 평범한 초상화였다는 것이 밝혀졌습니다.", "가주어 it ~ 진주어 that절(뒤가 완전) → that"),
 ("Then in a second version, a small gray ermine {appeared|appearing}.", "그다음에 두 번째 버전에서 작은 회색 담비가 나타납니다.", "주어 a small gray ermine 뒤 동사 자리 → appeared"),
 ("Finally in a third version — the one we know today — the ermine {became|becoming} bigger and its color changed to white.", "마지막으로 오늘날 우리가 알고 있는 세 번째 버전에서 담비가 더 커지고 색깔이 흰색으로 바뀌었습니다.", "주어 the ermine 뒤 동사 자리, changed와 나란히 → became"),
 ("Why did Da Vinci add the ermine to this painting? No one {knows|know} for sure.", "다빈치는 왜 이 그림에 담비를 추가했을까요? 그 누구도 (이유를) 확실히 알지 못합니다.", "No one은 단수 → knows"),
 ("He might have done it {to honor|honor} his patron. Maybe he just wanted to make the painting look more {special|specially}.", "그의 후원자를 기리기 위해 그랬을지도 모릅니다. 그저 그 그림이 좀 더 특별해지기를 원했던 것일 수도 있습니다.", "'~하기 위해'(목적) → to honor / look + 형용사 보어 → special"),
 ("{Whatever|What} the reason, this shows us {that|which} even a great master like Leonardo da Vinci, who said, \"Art is never finished,\" {made|make} revisions to his paintings over and over again.", "그 이유가 무엇이든, 이것은 '예술은 결코 완성되지 않는다.'라고 말했던 레오나르도 다빈치와 같은 거장도 자신의 그림을 계속해서 수정했다는 것을 보여 줍니다.", "'무엇이든' → Whatever / 뒤가 완전한 문장(목적어절) → that / 과거의 일 → made"),
]
C4 = [
 ("This next piece is by the great Vincent van Gogh. It appears {to be|being} just an ordinary painting of a woman {wearing|worn} a white cap.", "다음은 위대한 빈센트 반 고흐의 작품입니다. 그것은 흰 모자를 쓴 여인의 평범한 그림처럼 보입니다.", "appear + to부정사 : ~인 것 같다 → to be / 여인이 모자를 '쓰고 있는' → 현재분사 wearing"),
 ("But thanks to technology, another person {was|were} discovered on the other side of the canvas.", "그러나 기술 덕분에 캔버스의 다른 면에서 또 다른 사람이 발견되었습니다.", "주어 another person(단수) → was"),
 ("Who do you think that person was? It was Vincent van Gogh himself {that|what} was hidden at the back of the painting.", "그 사람이 누구였을 거라고 생각하나요? 그 그림 뒤에 숨겨져 있던 것은 바로 빈센트 반 고흐 자신이었습니다.", "It was ~ that … 강조 구문 → that"),
 ("In 2022, the National Galleries of Scotland took an X-ray of this painting while {preparing|prepare} for an exhibition.", "2022년에 스코틀랜드 국립 미술관은 전시회를 준비하던 중 이 그림을 엑스레이로 촬영했습니다.", "접속사 while + 분사(주어 생략) → preparing"),
 ("During this process, a {hidden|hiding} self-portrait of Van Gogh was discovered.", "이 과정에서 숨겨진 반 고흐의 자화상이 발견되었습니다.", "자화상이 '숨겨진' 것 → 과거분사 hidden"),
 ("You may be aware {that|what} Van Gogh's fame came after his death. In fact, he sold only one painting in his lifetime.", "여러분은 반 고흐의 명성이 그의 죽음 이후에 찾아왔다는 것을 알고 있을 것입니다. 사실, 그는 평생 동안 단 한 점의 그림만을 팔았습니다.", "be aware that + 완전한 문장 → that"),
 ("{Being|Be} a poor artist, he often reused his canvases to save money, turning them around and {painting|painted} on the opposite side.", "가난한 화가였기 때문에 그는 돈을 아끼기 위해 캔버스를 뒤집어 반대편에 그림을 그리면서 재사용하는 일이 많았습니다.", "분사구문(이유) → Being / turning과 and로 나란히 → painting"),
 ("You might also notice {that|what} Van Gogh's left ear looks {perfectly|perfect} fine in this painting.", "여러분은 이 그림에서 반 고흐의 왼쪽 귀가 멀쩡하다는 것도 알아차렸을 것입니다.", "뒤가 완전한 문장 → that / 형용사 fine을 꾸미는 부사 → perfectly"),
 ("{Since|Due to} he cut off part of his ear when he was 35, we can infer {that|what} this is one of his early {works|work}.", "그가 서른다섯 살일 때 자신의 귀의 일부를 잘랐기 때문에 우리는 이 그림이 그의 초기 작품 중 하나라는 것을 추론할 수 있습니다.", "뒤에 주어+동사(절) → 접속사 Since (Due to + 명사) / 뒤가 완전 → that / one of + 복수 명사 → works"),
 ("It is possible {that|which} other {hidden|hiding} paintings of Van Gogh will be revealed to the world with the help of technology.", "과학의 도움으로 반 고흐의 숨겨진 다른 작품들이 세상에 드러나는 것도 가능해 보입니다.", "가주어 It ~ 진주어 that절 → that / 그림이 '숨겨진' → hidden"),
 ("Rembrandt's The Night Watch, a huge painting {that|what} measures 3.795 meters by 4.535 meters, {has|have} had a troubled history.", "높이 3.795m, 너비 4.535m 크기의 거대한 그림인 렘브란트의 '야경'은 문제가 많은 과거사를 겪었습니다.", "선행사 a huge painting → that / 주어 The Night Watch(단수) → has"),
 ("It was damaged with a knife twice and {sprayed|spraying} with acid by people {who|what} wanted to destroy it.", "그림을 훼손하려는 사람들에 의해 두 차례 칼로 훼손되었고 산성 물질도 뿌려졌습니다.", "was damaged와 나란히 수동(was) sprayed / 선행사 people(사람) → who"),
 ("Each time, experts miraculously {restored|restoring} the painting to its original state. But did you know {that|what} this painting was {much|very} larger over three centuries ago?", "그럴 때마다 전문가들은 기적적으로 이 그림을 원래 상태로 복원했습니다. 그런데 이 그림이 300년 전에는 훨씬 더 컸다는 것을 알고 있었나요?", "주어 experts 뒤 동사 → restored / 뒤가 완전 → that / 비교급 강조 → much (very ✘)"),
 ("In 1715, this monumental painting was trimmed on all four sides {to fit|fit} on a wall in Amsterdam's town hall.", "1715년에 이 대단히 큰 그림은 암스테르담 시청의 벽에 맞도록 네 면이 잘렸습니다.", "'~하기 위해'(목적) → to fit"),
 ("Since then, 60 cm from the left side, 22 cm from the top, 12 cm from the bottom, and 7 cm from the right side have been {missing|miss}.", "그때 이후로 좌측에서 60cm, 상단에서 22cm, 하단에서 12cm, 우측에서 7cm가 잘려 나간 상태가 되었습니다.", "have been + 형용사(사라진) → missing"),
 ("However, art lovers can now see The Night Watch as Rembrandt originally {intended|intending}.", "그러나 미술 애호가들은 이제 렘브란트가 원래 의도한 대로 '야경'을 감상할 수 있습니다.", "as + 주어 + 동사: Rembrandt 뒤 동사 → intended"),
 ("{It|That} was artificial intelligence (AI) {that|what} the museum used to recreate the missing pieces.", "사라진 조각들을 되살리기 위해 박물관에서 사용한 것은 바로 인공 지능(AI)이었습니다.", "It was ~ that … 강조 구문 → It / that"),
 ("Instead of {hiring|hire} human artists, an AI program was trained {to learn|learning} Rembrandt's painting style.", "인간 예술가를 고용하는 대신 AI 프로그램이 렘브란트의 화풍을 학습하도록 훈련받았습니다.", "전치사 Instead of + 동명사 → hiring / be trained + to부정사 → to learn"),
 ("Once the AI program {learned|learning} to paint like Rembrandt, it was shown a copy of the original painting before it was trimmed.", "AI 프로그램이 렘브란트처럼 그리는 것을 학습한 후에는 잘리기 전 원본 그림의 복사본을 보여 줬습니다.", "접속사 Once + 주어 + 동사 → learned"),
 ("Then it reconstructed the missing pieces, {which|that} {were|was} hung around the painting.", "그런 다음 AI는 소실된 조각을 재구성하였고, 그 조각들은 그림의 둘레에 걸렸습니다.", "콤마 뒤 계속적 용법 → which / 선행사 pieces(복수) → were"),
 ("For the first time in over three centuries, The Night Watch is complete again. Thanks to science, this great masterpiece has {been brought|brought} back to life for all {to see|see}.", "300여 년 만에 처음으로 '야경'이 다시 완성된 것입니다. 과학 덕분에 이 위대한 걸작이 되살아나 모두가 감상할 수 있게 되었습니다.", "걸작이 '되살려진' 것 → 현재완료 수동 has been brought / for all to see : 모두가 볼 수 있도록 → to see"),
]

D = {d['id']: d for d in PK['days']}
txt = re.sub(r'\s+', ' ', ' '.join(l[1] for d in ('d1', 'd2', 'd3', 'd4', 'e1', 'e2', 'e3') for l in D[d]['passage'] if not re.match(r'^[❶-❿]$', l[1])).replace('’', "'"))
nbs = []
for C in (C1, C2, C3, C4):
    nb = 0
    for s, ko, ex in C:
        full = re.sub(r'\{([^|}]*)\|[^}]*\}', r'\1', s)
        assert full in txt, full
        for m in re.findall(r'\{([^}]*)\}', s): o = m.split('|'); assert len(o) == 2 and o[0] != o[1], s; nb += 1
    nbs.append(nb)
mk = lambda C: [{'s': s, 'ko': ko, 'ex': ex} for s, ko, ex in C]
chunk = lambda t, C: {'title': '%s (괄호 %d개)' % (t, sum(len(re.findall(r'\{', x[0])) for x in C)), 'parts': mk(C)}
day = {'id': 'gt3', 'name': '', 'range': '3과 본문 · 어법 선택 한 판', 'story': '3과 본문 어법 선택 한 판 · 괄호를 모두 맞혀야 100점 (덩이 4개)',
       'passage': D['d1']['passage'] + D['d2']['passage'] + D['d3']['passage'] + D['d4']['passage'],
       'steps': [{'type': 'gate', 'title': '어법 선택 한 판', 'guide': "본문을 네 덩이로 나눴어요. 덩이마다 괄호를 모두 맞혀야 100점, 하나라도 틀리면 0점! 3번 안에 통과 못 하면 틀린 문장만 해설과 함께 연습하고 다시 도전해요.",
                  'items': [chunk('본문 ❶ · 도입', C1[:9]), chunk('본문 ❷ · PROS', C1[9:]), chunk('본문 ❸ · CONS', C2[:13]), chunk('본문 ❹ · COMMENTS', C2[13:])]}]}
day4 = {'id': 'gt4', 'name': '', 'range': '4과 본문 · 어법 선택 한 판', 'story': '4과 본문 어법 선택 한 판 · 괄호를 모두 맞혀야 100점 (덩이 4개)',
        'passage': D['e1']['passage'] + D['e2']['passage'] + D['e3']['passage'],
        'steps': [{'type': 'gate', 'title': '어법 선택 한 판', 'guide': day['steps'][0]['guide'],
                   'items': [chunk('본문 ❶ · 도입', C3[:6]), chunk('본문 ❷ · 다빈치', C3[6:]), chunk('본문 ❸ · 반 고흐', C4[:10]), chunk('본문 ❹❺ · 야경', C4[10:])]}]}
PK['days'] = [d for d in PK['days'] if d['id'] not in ('gt3', 'gt4')] + [day, day4]
for i, d in enumerate(PK['days']): d['name'] = 'DAY %d' % (i + 1)
src = open(path, encoding='utf-8').read(); head = src[:src.index('window.PKG')]
if '한 판' not in head: head = head.rstrip('\n') + '\n/* 11/16: 3과 본문 어법 선택 한 판 DAY gt3 맨 끝 (generators/gen_h1d3gate.py) */\n'
write(PK, path, head)
print('괄호', nbs, sum(nbs), '·', [d['name'] + ' ' + d['range'] for d in PK['days']][-2:])
