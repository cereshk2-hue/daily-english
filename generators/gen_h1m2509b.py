import sys, html
sys.path.insert(0, '/tmp/claude-0/-home-claude/a9e3e882-1f02-5d62-8f70-aced81bc59d2/scratchpad')
from gencommon import *

# 고1 2025년 9월 학평 26 · 29 · 30 · 31번 → 기존 h1-mock-2509 (18~24번) 뒤에 DAY 4 · 5로 이어 붙임
def esc(s): return html.escape(s, quote=False)
def box(t): return '<span class="exam-box en">' + t + '</span>'
def exam(no, stem, body_html, extra=''):
    return '<b>' + str(no) + '. ' + stem + '</b>' + extra + box(body_html)
def body(T): return ' '.join(esc(r[0]) for r in T)
def sec(t): return [['#', t, '']]
def rows(T): return [['', a, b] for a, b in T]
def L(T, i): return T[i][0]

H26, H29, H30, H31 = '26번 · 내용 불일치', '29번 · 어법', '30번 · 어휘', '31번 · 빈칸'

T26 = [
 ("Roger Payne was born in Manhattan in 1935.", "Roger Payne은 1935년 맨해튼에서 태어났다."),
 ("He studied biology at Harvard University and eventually earned his Ph.D. from Cornell University in 1961.", "그는 하버드 대학교에서 생물학을 공부했고, 마침내 1961년 코넬 대학교에서 박사 학위를 받았다."),
 ("In 1967, he discovered that humpback whales make long and complex sounds.", "1967년, 그는 혹등고래가 길고 복잡한 소리를 낸다는 것을 발견했다."),
 ("They're known as \"whale songs,\" and he showed that whales use them to communicate.", "그 소리는 '고래의 노래'로 알려져 있으며, 그는 고래가 의사소통하기 위해 그것을 사용한다는 것을 보여 주었다."),
 ("Then in 1970, he released an album Songs of the Humpback Whale, which became a surprise hit and helped start the global \"Save the Whales\" movement.", "그리고 1970년, 그는 'Songs of the Humpback Whale'이라는 앨범을 발매했는데, 그것은 뜻밖의 히트작이 되었고 전 세계적인 '고래를 구하자' 운동이 시작되는 데 도움을 주었다."),
 ("The following year, he founded Ocean Alliance to protect whales and the earth's oceans, and he used new, safe methods to study whales without harming them.", "그다음 해, 그는 고래와 지구의 바다를 보호하기 위해 Ocean Alliance를 설립했고, 고래에게 해를 끼치지 않고 고래를 연구하는 새롭고 안전한 방법을 사용했다."),
 ("Over his career, he led more than 100 research trips worldwide, including the Voyage of the Odyssey from 2000 to 2005, which studied ocean pollution.", "경력 전반에 걸쳐, 그는 해양 오염을 연구한 2000년부터 2005년까지의 Voyage of the Odyssey를 포함하여 전 세계에서 100회가 넘는 연구 여행을 이끌었다."),
 ("His work helped make laws that protect marine mammals, which finally led to the global ban on commercial whaling in 1986.", "그의 연구는 해양 포유류를 보호하는 법을 만드는 데 도움이 되었고, 이는 마침내 1986년 상업적 포경의 전 세계적 금지로 이어졌다."),
]
T29 = [
 ("Big mammalian herbivore species react to danger from predators or humans in different ways.", "큰 포유류 초식동물 종들은 포식자나 인간으로부터의 위험에 서로 다른 방식으로 반응한다."),
 ("Some species are nervous, fast, and programmed for instant flight when they perceive a threat.", "어떤 종들은 예민하고, 빠르며, 위협을 감지하면 즉시 달아나도록 (본능적으로) 프로그램되어 있다."),
 ("Other species are slower, less nervous, seek protection in herds, stand their ground when threatened, and don't run until necessary.", "다른 종들은 더 느리고, 덜 예민하며, 무리 속에서 보호를 구하고, 위협을 받으면 물러서지 않고 버티며, 필요할 때까지 달아나지 않는다."),
 ("Naturally, the nervous species are difficult to keep in captivity.", "당연히 예민한 종들은 가두어 기르기가 어렵다."),
 ("If put into an enclosure, they are likely to panic, and either die of shock or hit themselves repeatedly to death against the fence in their attempts to escape.", "울타리 안에 넣어지면, 그것들은 겁에 질려서 충격으로 죽거나, 탈출하려다 울타리에 스스로를 거듭 부딪쳐 죽을 가능성이 크다."),
 ("That's true, for example, of gazelles, which for thousands of years were the most frequently hunted game species in some parts of the Fertile Crescent.", "예를 들어 가젤이 그런데, 가젤은 수천 년 동안 비옥한 초승달 지대의 일부 지역에서 가장 자주 사냥된 사냥감 종이었다."),
 ("There is no mammal species that the first settled peoples of that area had more opportunity to domesticate than gazelles.", "그 지역에 처음 정착한 민족들에게 가젤보다 길들일 기회가 더 많았던 포유류 종은 없다."),
 ("But no gazelle species has ever been domesticated.", "하지만 어떤 가젤 종도 길들여진 적이 없다."),
 ("Just imagine trying to herd an animal that runs away, blindly hits itself against walls, can leap up to nearly 30 feet, and can run at a speed of 50 miles per hour!", "달아나고, 앞뒤 가리지 않고 벽에 몸을 부딪치며, 거의 30피트 높이까지 뛰어오를 수 있고, 시속 50마일로 달릴 수 있는 동물을 무리 지어 몰려고 한다고 상상해 보라!"),
]
T30 = [
 ("For a species born in a time when resources were limited and dangers were great, our natural tendency to share and cooperate is complicated when resources are plenty and outside dangers are few.", "자원이 한정되고 위험이 컸던 시대에 태어난 종이기에, 나누고 협력하려는 우리의 타고난 경향은 자원이 풍부하고 외부의 위험이 적을 때 복잡해진다."),
 ("When we have less, we tend to be more open to sharing what we have.", "우리는 가진 것이 적을 때 가진 것을 나누는 데 더 열려 있는 경향이 있다."),
 ("Certain nomadic tribes don't have much, yet they are happy to share because it is in their interest to do so.", "어떤 유목 부족들은 가진 것이 많지 않지만, 그렇게 하는 것이 자신들에게 이익이 되기 때문에 기꺼이 나눈다."),
 ("If you happen upon them in your travels, they will open up their homes and give you their food and hospitality.", "여행 중에 우연히 그들을 만나면, 그들은 집을 열어 주고 음식과 환대를 베풀 것이다."),
 ("It's not just because they are nice people; it's because their survival depends on sharing, for they know that they may be the travelers in need of food and shelter another day.", "그것은 단지 그들이 친절한 사람들이기 때문이 아니라 그들의 생존이 나눔에 달려 있기 때문인데, 그들은 언젠가 자신들이 음식과 쉼터가 필요한 여행자가 될 수도 있다는 것을 알기 때문이다."),
 ("Ironically, the more we have, the bigger our fences, the more sophisticated our security to keep people away and the less we want to share.", "아이러니하게도 우리가 더 많이 가질수록, 우리의 울타리는 더 커지고, 사람들을 멀리하기 위한 보안은 더 정교해지며, 우리는 덜 나누고 싶어 한다."),
 ("Our desire for more, combined with our decreased physical interaction with the \"common folk,\" starts to create a disconnection or blindness to reality.", "더 많이 가지려는 욕망은 '평범한 사람들'과의 줄어든 물리적 교류와 결합되어, 현실과의 단절 또는 현실에 대한 무지를 만들어 내기 시작한다."),
]
T31 = [
 ("Whether we feel happy or sad, content or discontent, is not determined merely by each individual successive moment of life experience — a good thing happens and I'm happy, a bad thing happens and I'm sad.", "우리가 행복하다고 느끼는지 슬프다고 느끼는지, 만족하는지 불만족하는지는 삶의 경험이 이어지는 각각의 순간에 의해서만 결정되지 않는다. 즉, 좋은 일이 생기면 행복하고, 나쁜 일이 생기면 슬픈 식이 아니다."),
 ("While our experiences affect our mood, we are not blown in a completely new direction by each gust of wind.", "경험이 우리의 기분에 영향을 미치기는 하지만, 우리는 바람이 한 번 불 때마다 완전히 새로운 방향으로 날려 가지는 않는다."),
 ("As humans, we adjust — to new information and events both good and bad — and return to our personal default level of well-being.", "인간으로서 우리는 좋든 나쁘든 새로운 정보와 사건에 적응하고, 각자의 기본 행복 수준으로 돌아간다."),
 ("There will be highs and lows, but over time, like water seeking its own level, we are pulled toward our baseline — back up after bad news and back down after good.", "기복은 있겠지만, 시간이 지나면 물이 제 수위를 찾아가듯 우리는 기준선 쪽으로 끌려간다. 즉, 나쁜 소식 뒤에는 다시 올라가고 좋은 소식 뒤에는 다시 내려간다."),
 ("The euphoria of first love fades, and so does the despair of a break-up.", "첫사랑의 황홀감은 사라지고, 이별의 절망도 마찬가지이다."),
 ("This tendency is best seen with little kids and their toy joy: When they get what they've longed for, they believe they will be happy for the rest of their lives.", "이 경향은 어린아이들과 그들이 장난감을 받고 느끼는 기쁨에서 가장 잘 드러난다. 아이들은 간절히 바라던 것을 얻으면 남은 평생 행복할 거라고 믿는다."),
 ("And for the first few minutes of the rest of their lives, they are.", "그리고 남은 평생 중 처음 몇 분 동안은 실제로 그렇다(행복하다)."),
 ("But then the kids — like adults — adapt.", "하지만 그러고 나면 아이들은, 어른들처럼, 적응한다."),
]

# ───── 실전 문항 원문 (시험지 그대로: 밑줄·빈칸) ─────
Q29 = ("Big mammalian herbivore species react to danger from predators or humans in different ways. Some species are nervous, fast, and programmed for instant flight when they perceive a threat. "
       "Other species are slower, less nervous, seek protection in herds, ①<u>stand</u> their ground when threatened, and don't run until necessary. Naturally, the nervous species are difficult to keep in captivity. "
       "If ②<u>putting</u> into an enclosure, they are likely to panic, and either die of shock or hit themselves repeatedly to death against the fence in their attempts to escape. "
       "That's true, for example, of gazelles, ③<u>which</u> for thousands of years were the most frequently hunted game species in some parts of the Fertile Crescent. "
       "There is no mammal species that the first settled peoples of that area had more opportunity ④<u>to domesticate</u> than gazelles. But no gazelle species has ever been domesticated. "
       "Just imagine trying to herd an animal that runs away, blindly hits ⑤<u>itself</u> against walls, can leap up to nearly 30 feet, and can run at a speed of 50 miles per hour!<br><small>* herbivore: 초식동물 ** herd: 무리</small>")
Q30 = ("For a species born in a time when resources were limited and dangers were great, our natural tendency to share and cooperate is ①<u>complicated</u> when resources are plenty and outside dangers are few. "
       "When we have less, we tend to be more open to sharing what we have. Certain nomadic tribes don't have much, yet they are happy to share because it is in their ②<u>interest</u> to do so. "
       "If you happen upon them in your travels, they will open up their homes and give you their food and hospitality. It's not just because they are nice people; it's because their ③<u>survival</u> depends on sharing, "
       "for they know that they may be the travelers in need of food and shelter another day. Ironically, the ④<u>more</u> we have, the bigger our fences, the more sophisticated our security to keep people away and the less we want to share. "
       "Our desire for more, combined with our ⑤<u>increased</u> physical interaction with the \"common folk,\" starts to create a disconnection or blindness to reality.<br><small>* nomadic: 유목의 ** hospitality: 환대</small>")
Q31 = body(T31[:7]) + ' But then the kids — like adults — <u>　　　　　　　　</u>.<br><small>* euphoria: (극도의) 행복감</small>'

def day(vocab, real, summ, **kw):
    st = steps(vocab=vocab, **kw)
    st.insert(1, {'type': 'mc', 'title': '실전 문항', 'guide': '시험지 원문항이에요. 지문을 읽고 답을 고르세요.', 'items': real})
    st.append({'type': 'mc', 'title': '요약문 완성', 'guide': '지문을 읽고 요약문의 빈칸 (A), (B)에 들어갈 말을 고르세요.',
               'items': [{'n': n, 'box': bx, 'q': '다음 글의 내용을 한 문장으로 요약할 때, 빈칸 (A), (B)에 들어갈 말로 가장 알맞은 것은?<br><b>' + s + '</b>', 'opts': o, 'ex': x, 'ev': ev} for n, bx, s, o, x, ev in summ]})
    return st

def mc(n, bx, q, opts, ex, per):
    return {'n': n, 'box': bx, 'q': q, 'opts': opts, 'ex': ex, 'per': per}

# ═════════════ DAY 4 · 26 · 29번 ═════════════
d4 = day(
 vocab=[['biology', '생물학', 26], ['eventually', '결국, 마침내', 26], ['Ph.D.', '박사 학위', 26], ['humpback whale', '혹등고래', 26],
        ['complex', '복잡한', 26], ['communicate', '의사소통하다', 26], ['release', '(음반 등을) 발매하다', 26], ['surprise hit', '뜻밖의 히트작', 26],
        ['global', '전 세계적인', 26], ['movement', '(사회적) 운동', 26], ['found', '설립하다 (found - founded - founded)', 26], ['method', '방법', 26],
        ['harm', '해를 끼치다', 26], ['career', '경력, 생애', 26], ['worldwide', '전 세계적으로', 26], ['voyage', '항해, 여행', 26],
        ['pollution', '오염', 26], ['marine mammal', '해양 포유류', 26], ['ban', '금지', 26], ['commercial whaling', '상업적 포경(고래잡이)', 26],
        ['mammalian', '포유류의', 29], ['herbivore', '초식동물', 29], ['predator', '포식자', 29], ['instant', '즉각적인', 29],
        ['flight', '도주, 달아남', 29], ['perceive', '감지하다, 인식하다', 29], ['threat', '위협', 29], ['herd', '무리; (가축을) 몰다', 29],
        ['stand one\'s ground', '물러서지 않다, 버티다', 29], ['captivity', '감금, 사육 상태', 29], ['enclosure', '울타리를 친 곳', 29], ['panic', '겁에 질리다', 29],
        ['die of', '~으로 죽다', 29], ['attempt', '시도', 29], ['game', '사냥감', 29], ['settled', '정착한', 29],
        ['domesticate', '(동물을) 길들이다, 가축화하다', 29], ['blindly', '앞뒤 가리지 않고, 무턱대고', 29], ['leap', '뛰어오르다', 29]],
 real=[
  {'n': 26, 'q': exam(26, 'Roger Payne에 관한 다음 글의 내용과 일치하지 <u>않는</u> 것은?', body(T26) + '<br><small>* humpback whale: 혹등고래</small>'),
   'opts': ['그의 앨범 Songs of the Humpback Whale은 인기를 얻지 못했다.', '하버드 대학교에서 생물학을 공부했다.', '혹등고래가 길고 복잡한 소리를 낸다는 것을 발견했다.', '고래와 지구의 해양을 보호하기 위해 Ocean Alliance를 설립했다.', '그의 연구는 해양 포유류를 보호하는 법 제정에 도움을 주었다.'],
   'ex': "정답 ▶ ③ 그의 앨범은 인기를 얻지 못했다.\n이유: 앨범은 뜻밖의 히트작(a surprise hit)이 되었고 '고래를 구하자' 운동이 시작되는 데까지 도움을 줬어요. 인기를 얻지 못한 게 아니라 큰 인기를 얻었어요.\n포인트 ▶ 인물 내용 일치는 선택지 순서 = 본문 순서. 연도·숫자·부정 표현(못했다, 없다)을 본문과 하나씩 대조하세요.",
   'per': [['그의 앨범은 인기를 얻지 못했다.', 'which became a surprise hit', '불일치 → 뜻밖의 히트작'],
           ['하버드 대학교에서 생물학을 공부했다.', 'He studied biology at Harvard University', '일치'],
           ['혹등고래가 길고 복잡한 소리를 낸다는 것을 발견했다.', 'he discovered that humpback whales make long and complex sounds', '일치'],
           ['Ocean Alliance를 설립했다.', 'he founded Ocean Alliance to protect whales and the earth\'s oceans', '일치'],
           ['해양 포유류 보호법 제정에 도움을 주었다.', 'His work helped make laws that protect marine mammals', '일치']]},
  {'n': 29, 'q': exam(29, '다음 글의 밑줄 친 부분 중, 어법상 <u>틀린</u> 것은? [3점]', Q29),
   'opts': ['② putting', '① stand', '③ which', '④ to domesticate', '⑤ itself'],
   'ex': "정답 ▶ ② putting → put\n이유: If (they are) put into an enclosure에서 '주어 + be동사'가 생략된 형태예요. 주어 they(= 예민한 종들)는 울타리 안에 '넣어지는' 대상이라 수동 → 과거분사 put. putting이면 '스스로 넣는다'는 능동이 돼요.\n나머지 ▶ ① stand: are, seek, stand, don't run이 주어 Other species에 걸리는 병렬 동사 ✔ ③ which: 콤마 뒤 계속적 용법, 선행사 gazelles ✔ ④ to domesticate: opportunity를 꾸미는 형용사적 to부정사 ✔ ⑤ itself: 주어 an animal(= that)과 목적어가 같은 대상 → 재귀대명사 ✔",
   'per': [['', 'If put into an enclosure, they are likely to panic', '수동 분사 put (If they are put)'],
           ['', 'seek protection in herds, stand their ground when threatened', '병렬 동사 ✔'],
           ['', 'gazelles, which for thousands of years were the most frequently hunted game species', '계속적 용법 which ✔'],
           ['', 'had more opportunity to domesticate than gazelles', 'opportunity to부정사 ✔'],
           ['', 'blindly hits itself against walls', '재귀대명사 ✔']]},
 ],
 pickv=[
  ("He studied biology at Harvard University and {eventually|eventfully} earned his Ph.D. from Cornell University in 1961.",
   "정답 ▶ eventually (결국, 마침내)\n오답 ▶ eventfully (다사다난하게): 하버드에서 공부한 뒤 '마침내' 박사 학위를 받았다는 흐름이에요. 철자가 비슷한 혼동어!"),
  ("In 1967, he discovered that humpback whales make long and {complex|compact} sounds.",
   "정답 ▶ complex (복잡한)\n오답 ▶ compact (소형의, 촘촘한): '길고 복잡한' 소리라서 '노래'처럼 들려요."),
  ("Then in 1970, he released an album Songs of the Humpback Whale, which became a surprise hit and helped start the global \"Save the Whales\" {movement|moment}.",
   "정답 ▶ movement ((사회적) 운동)\n오답 ▶ moment (순간): '고래를 구하자' 운동. 철자 혼동 주의!"),
  ("The following year, he founded Ocean Alliance to protect whales and the earth's oceans, and he used new, safe methods to study whales without {harming|helping} them.",
   "정답 ▶ harming (해를 끼치는)\n오답 ▶ helping (돕는): '안전한 방법'으로 연구했으니 고래에게 '해를 끼치지 않고' 연구한 거예요."),
  ("His work helped make laws that protect {marine|marital} mammals, which finally led to the global ban on commercial whaling in 1986.",
   "정답 ▶ marine (해양의)\n오답 ▶ marital (결혼의): marine mammals = 해양 포유류(고래, 물개 등)"),
  ("His work helped make laws that protect marine mammals, which finally led to the global {ban|boom} on commercial whaling in 1986.",
   "정답 ▶ ban (금지)\n오답 ▶ boom (호황): 고래 보호법이 이어져 상업적 포경이 '금지'되었어요. ban on ~ = ~에 대한 금지"),
  ("Some species are nervous, fast, and programmed for {instant|constant} flight when they perceive a threat.",
   "정답 ▶ instant (즉각적인)\n오답 ▶ constant (끊임없는): 위협을 감지하면 '즉시' 달아나요. 여기서 flight는 '비행'이 아니라 '도주'!"),
  ("Other species are slower, less nervous, seek {protection|production} in herds, stand their ground when threatened, and don't run until necessary.",
   "정답 ▶ protection (보호)\n오답 ▶ production (생산): 덜 예민한 종들은 무리 속에서 '보호'를 구해요."),
  ("Naturally, the nervous species are difficult to keep in {captivity|creativity}.",
   "정답 ▶ captivity (감금, 사육 상태)\n오답 ▶ creativity (창의성): 예민한 종은 '가두어 기르기' 어렵다 → 길들이기(가축화)가 어려운 이유"),
  ("There is no mammal species that the first settled peoples of that area had more opportunity to {domesticate|dominate} than gazelles.",
   "정답 ▶ domesticate (길들이다, 가축화하다)\n오답 ▶ dominate (지배하다): 바로 뒤 'no gazelle species has ever been domesticated'와 연결돼요."),
 ],
 tf=[
  ["Payne obtained his doctorate before he identified whale songs.", True, "정답 ▶ T\n이유: 박사 학위는 1961년, 고래 소리 발견은 1967년이에요.\n어휘 ▶ obtain 얻다 · doctorate 박사 학위(= Ph.D.) · identify 확인하다, 밝혀내다", 26, "earned his Ph.D. from Cornell University in 1961"],
  ["Payne demonstrated that whales use their songs as a means of communication.", True, "정답 ▶ T\n이유: he showed that whales use them to communicate.\n어휘 ▶ demonstrate 보여 주다(= show) · a means of ~의 수단", 26, "he showed that whales use them to communicate"],
  ["Payne's album failed to attract public attention.", False, "정답 ▶ F\n이유: 앨범은 뜻밖의 히트작(a surprise hit)이 되었어요.\n어휘 ▶ fail to ~하지 못하다 · attract attention 관심을 끌다", 26, "which became a surprise hit"],
  ["Payne's research methods involved injuring whales.", False, "정답 ▶ F\n이유: 고래에게 해를 끼치지 않는(without harming) 안전한 방법을 썼어요.\n어휘 ▶ involve 포함하다 · injure 다치게 하다(= harm)", 26, "without harming them"],
  ["The global ban on commercial whaling came before Payne discovered whale songs.", False, "정답 ▶ F\n이유: 고래 노래 발견은 1967년, 상업적 포경 금지는 1986년이에요. 순서가 반대예요.", 26, "the global ban on commercial whaling in 1986"],
  ["Some herbivores flee immediately upon sensing danger.", True, "정답 ▶ T\n이유: 위협을 감지하면 즉시 달아나도록 되어 있는 종이 있어요.\n어휘 ▶ flee 달아나다 · upon -ing ~하자마자 · sense 감지하다(= perceive)", 29, "programmed for instant flight when they perceive a threat"],
  ["Nervous species easily get used to life in enclosures.", False, "정답 ▶ F\n이유: 예민한 종은 가두어 기르기 어렵고, 울타리에 넣으면 겁에 질려 죽기도 해요.\n어휘 ▶ get used to ~에 익숙해지다", 29, "the nervous species are difficult to keep in captivity"],
  ["Gazelles were rarely hunted in the Fertile Crescent.", False, "정답 ▶ F\n이유: 가젤은 가장 자주 사냥된(the most frequently hunted) 사냥감이었어요.\n어휘 ▶ rarely 거의 ~ 않는", 29, "the most frequently hunted game species"],
 ],
 ilchi=[
  mc(26, [H26], "글의 내용과 일치하지 <u>않는</u> 것은?",
     ["His album went largely unnoticed by the public.", "He studied biology at Harvard.", "He revealed that humpback whales produce lengthy, intricate sounds.", "He established an organization dedicated to marine conservation.", "His research contributed to legislation safeguarding marine mammals."],
     "정답 ▶ His album went largely unnoticed by the public.\n이유: 앨범은 뜻밖의 히트작이었어요.\n어휘 ▶ go unnoticed 주목받지 못하다 · lengthy 긴 · intricate 복잡한(= complex) · dedicated to ~에 전념하는 · conservation 보호 · legislation 법률 제정 · safeguard 보호하다",
     [["그의 앨범은 대중에게 거의 주목받지 못했다.", "which became a surprise hit", "불일치"],
      ["하버드에서 생물학을 공부했다.", "He studied biology at Harvard University", "일치"],
      ["혹등고래가 길고 복잡한 소리를 낸다는 것을 밝혀냈다.", "humpback whales make long and complex sounds", "일치 (intricate = complex)"],
      ["해양 보호에 전념하는 단체를 설립했다.", "he founded Ocean Alliance to protect whales and the earth's oceans", "일치"],
      ["그의 연구는 해양 포유류를 보호하는 법률 제정에 기여했다.", "His work helped make laws that protect marine mammals", "일치"]]),
  mc(26, [H26], "글의 내용과 <u>일치하는</u> 것은?",
     ["He led over a hundred research expeditions around the globe.", "He was born in Cornell in 1935.", "The Voyage of the Odyssey focused on whale migration.", "He founded Ocean Alliance before releasing his album.", "He was against the ban on commercial whaling."],
     "정답 ▶ He led over a hundred research expeditions around the globe.\n이유: he led more than 100 research trips worldwide\n어휘 ▶ expedition 탐험, 원정(= trip) · around the globe 전 세계에서(= worldwide) · migration 이동",
     [["전 세계에서 100회 넘는 연구 원정을 이끌었다.", "he led more than 100 research trips worldwide", "일치"],
      ["1935년 코넬에서 태어났다.", "Roger Payne was born in Manhattan in 1935", "불일치 → 맨해튼"],
      ["Voyage of the Odyssey는 고래 이동을 연구했다.", "which studied ocean pollution", "불일치 → 해양 오염"],
      ["앨범을 내기 전에 Ocean Alliance를 설립했다.", "The following year, he founded Ocean Alliance", "불일치 → 앨범(1970) 다음 해"],
      ["상업적 포경 금지에 반대했다.", "which finally led to the global ban on commercial whaling", "불일치 → 금지로 이어지게 도움"]]),
  mc(29, [H29], "글의 내용과 일치하지 <u>않는</u> 것은?",
     ["Gazelles were among the first animals to be domesticated in the region.", "Calmer species tend to rely on herds for safety.", "Nervous animals may injure themselves fatally when confined.", "Gazelles were hunted frequently for thousands of years.", "Gazelles can jump almost 30 feet."],
     "정답 ▶ Gazelles were among the first animals to be domesticated in the region.\n이유: 어떤 가젤 종도 길들여진 적이 없어요.\n어휘 ▶ rely on ~에 의지하다 · fatally 치명적으로 · confined 갇힌",
     [["가젤은 그 지역에서 가장 먼저 길들여진 동물 중 하나였다.", "no gazelle species has ever been domesticated", "불일치"],
      ["덜 예민한 종은 안전을 위해 무리에 의지한다.", "seek protection in herds", "일치"],
      ["예민한 동물은 갇히면 스스로를 치명적으로 다치게 할 수 있다.", "hit themselves repeatedly to death against the fence", "일치"],
      ["가젤은 수천 년 동안 자주 사냥되었다.", "for thousands of years were the most frequently hunted game species", "일치"],
      ["가젤은 거의 30피트를 뛰어오를 수 있다.", "can leap up to nearly 30 feet", "일치"]]),
  mc(29, [H29], "글의 내용과 <u>일치하는</u> 것은?",
     ["Early settlers had many chances to domesticate gazelles but never succeeded.", "All large herbivores respond to danger in the same way.", "Slower species run away at the first sign of a threat.", "Nervous species are easy to raise in captivity.", "Gazelles can run at about 30 miles per hour."],
     "정답 ▶ Early settlers had many chances to domesticate gazelles but never succeeded.\n이유: 가젤보다 길들일 기회가 많았던 종은 없었지만, 어떤 가젤 종도 길들여진 적이 없어요.\n어휘 ▶ settler 정착민 · at the first sign of ~의 기미가 보이자마자",
     [["초기 정착민은 가젤을 길들일 기회가 많았지만 성공하지 못했다.", ["There is no mammal species that the first settled peoples", "But no gazelle species has ever been domesticated"], "일치"],
      ["모든 큰 초식동물은 위험에 같은 방식으로 반응한다.", "react to danger from predators or humans in different ways", "불일치 → 서로 다른 방식"],
      ["느린 종은 위협의 기미가 보이면 바로 달아난다.", "don't run until necessary", "불일치 → 필요할 때까지 안 달아남"],
      ["예민한 종은 가두어 기르기 쉽다.", "the nervous species are difficult to keep in captivity", "불일치 → 어렵다"],
      ["가젤은 시속 약 30마일로 달린다.", "can run at a speed of 50 miles per hour", "불일치 → 50마일 (30은 점프 높이)"]]),
 ],
 pickg=[
  ("They're known {as|for} \"whale songs,\" and he showed that whales use them to communicate.",
   "정답 ▶ as\n이유: be known as + 이름·자격 = ~로(라고) 알려져 있다. 그 소리 = '고래의 노래'\n비교 ▶ be known for + 이유 = ~로 유명하다 (Seoul is known for its food.)"),
  ("Then in 1970, he released an album Songs of the Humpback Whale, {which|that} became a surprise hit and helped start the global \"Save the Whales\" movement.",
   "정답 ▶ which\n이유: 콤마(,) 뒤에서 앞말을 보충 설명하는 계속적 용법에는 which. that은 콤마 뒤에 쓸 수 없어요."),
  ("Then in 1970, he released an album Songs of the Humpback Whale, which became a surprise hit and helped {start|starting} the global \"Save the Whales\" movement.",
   "정답 ▶ start\n이유: help + (to) 동사원형 = ~하는 것을 돕다. helped start / helped to start ✔, helped starting ✘"),
  ("The following year, he founded Ocean Alliance to protect whales and the earth's oceans, and he used new, safe methods to study whales without {harming|harm} them.",
   "정답 ▶ harming\n이유: 전치사 without 뒤에는 동명사(-ing). without harming = 해를 끼치지 않고"),
  ("If {put|putting} into an enclosure, they are likely to panic, and either die of shock or hit themselves repeatedly to death against the fence in their attempts to escape.",
   "정답 ▶ put\n이유: If (they are) put ~ → 주어 they(동물)가 울타리에 '넣어지는' 수동 → 과거분사 put\n오답 ▶ putting(능동: 스스로 넣다) ✘ — 29번 실전 문항의 정답 포인트!"),
  ("Other species are slower, less nervous, seek protection in herds, stand their ground when {threatened|threatening}, and don't run until necessary.",
   "정답 ▶ threatened\n이유: when (they are) threatened → 동물이 '위협을 받을 때'(수동) → 과거분사\n오답 ▶ threatening이면 '위협할 때'(능동)가 돼요."),
  ("If put into an enclosure, they are likely to panic, and either die of shock or hit {themselves|them} repeatedly to death against the fence in their attempts to escape.",
   "정답 ▶ themselves\n이유: 부딪치는 주체(they)와 부딪치는 대상이 같으니 재귀대명사 themselves\n오답 ▶ them이면 '다른 동물들'을 부딪친다는 뜻이 돼요."),
  ("There is no mammal species that the first settled peoples of that area had more opportunity {to domesticate|domesticating} than gazelles.",
   "정답 ▶ to domesticate\n이유: opportunity(기회)를 뒤에서 꾸미는 형용사적 to부정사 = 길들일 기회\n포인트 ▶ chance/opportunity/time + to부정사"),
  ("But no gazelle species has ever {been domesticated|domesticated}.",
   "정답 ▶ been domesticated\n이유: 가젤은 '길들여지는' 대상 → 수동. 현재완료 수동 = have/has been + p.p.\n오답 ▶ has domesticated(능동: 가젤이 무언가를 길들였다) ✘"),
  ("Just imagine {trying|to try} to herd an animal that runs away, blindly hits itself against walls, can leap up to nearly 30 feet, and can run at a speed of 50 miles per hour!",
   "정답 ▶ trying\n이유: imagine은 목적어로 동명사(-ing)만 써요.\n포인트 ▶ 동명사만 목적어로: imagine, enjoy, avoid, finish, mind, consider, give up"),
 ],
 verb=[
  ("Roger Payne ___ born in Manhattan in 1935.", 'be', ['was'], "정답 ▶ was\n이유: be born = 태어나다(수동 형태). 1935년 과거 → was born"),
  ("He studied biology at Harvard University and eventually ___ his Ph.D. from Cornell University in 1961.", 'earn', ['earned'], "정답 ▶ earned\n이유: studied(과거)와 and로 이어진 병렬 → 과거형 earned"),
  ("The following year, he ___ Ocean Alliance to protect whales and the earth's oceans, and he used new, safe methods to study whales without harming them.", 'found', ['founded'], "정답 ▶ founded\n이유: found(설립하다)의 과거형은 founded!\n주의 ▶ find(찾다) - found - found 와 헷갈리지 마세요. 'found'를 넣으면 '찾았다'가 돼요."),
  ("Over his career, he ___ more than 100 research trips worldwide, including the Voyage of the Odyssey from 2000 to 2005, which studied ocean pollution.", 'lead', ['led'], "정답 ▶ led\n이유: lead - led - led (불규칙). 지난 경력 → 과거"),
  ("Some species are nervous, fast, and ___ for instant flight when they perceive a threat.", 'program', ['programmed'], "정답 ▶ programmed\n이유: are nervous, (are) fast, and (are) programmed → 동물은 '프로그램된' 대상이라 수동 be + p.p. (m을 겹쳐 -med)"),
  ("Naturally, the nervous species are difficult ___ in captivity.", 'keep', ['to keep'], "정답 ▶ to keep\n이유: difficult/easy/hard + to부정사 = ~하기 어렵다/쉽다"),
  ("That's true, for example, of gazelles, which for thousands of years were the most frequently ___ game species in some parts of the Fertile Crescent.", 'hunt', ['hunted'], "정답 ▶ hunted\n이유: 가젤은 '사냥된' 대상 → 과거분사가 명사 game species를 꾸며요. the most frequently hunted = 가장 자주 사냥된"),
 ],
 error=[
  ("Then in 1970, he released an album Songs of the Humpback Whale, [[that]] became a surprise hit and [[helped]] start the global \"Save the Whales\" [[movement]].", 0, 'which',
   "틀린 곳 ▶ ① that → which\n이유: 콤마 뒤 계속적 용법에는 that을 쓸 수 없어요.\n나머지 ▶ ② helped start(help + 동사원형) ✔ ③ movement(운동) ✔"),
  ("His work [[helped]] make laws that [[protects]] marine mammals, [[which]] finally led to the global ban on commercial whaling in 1986.", 1, 'protect',
   "틀린 곳 ▶ ② protects → protect\n이유: 관계대명사 that의 선행사는 laws(복수) → 동사도 복수형 protect\n나머지 ▶ ① helped make ✔ ③ which(앞 내용을 받는 계속적 용법) ✔"),
  ("Over his career, he led more than 100 research trips worldwide, [[including]] the Voyage of the Odyssey from 2000 to 2005, [[which]] [[studying]] ocean pollution.", 2, 'studied',
   "틀린 곳 ▶ ③ studying → studied\n이유: 관계대명사 which 뒤에는 동사가 와야 해요(which가 주어 역할). 지난 일이라 과거형 studied\n나머지 ▶ ① including(~을 포함하여) ✔ ② which ✔"),
  ("Naturally, the nervous species [[are]] difficult to keep in [[captive]]. If put into an enclosure, they are [[likely]] to panic.", 1, 'captivity',
   "틀린 곳 ▶ ② captive → captivity\n이유: 전치사 in 뒤에는 명사 → captivity(감금, 사육 상태). captive는 '사로잡힌'(형용사)/'포로'(사람)\n나머지 ▶ ① are(species 복수) ✔ ③ be likely to(~할 가능성이 크다) ✔"),
  ("That's true, for example, of gazelles, [[which]] for thousands of years [[was]] the most frequently [[hunted]] game species in some parts of the Fertile Crescent.", 1, 'were',
   "틀린 곳 ▶ ② was → were\n이유: which의 선행사는 gazelles(복수) → were. 사이에 낀 for thousands of years에 속지 마세요.\n나머지 ▶ ① which ✔ ③ hunted(사냥된, 수동) ✔"),
  ("Just imagine trying to herd an animal that [[runs]] away, blindly hits [[themselves]] against walls, can [[leap]] up to nearly 30 feet, and can run at a speed of 50 miles per hour!", 1, 'itself',
   "틀린 곳 ▶ ② themselves → itself\n이유: 주어는 an animal(단수) → 재귀대명사도 단수 itself\n나머지 ▶ ① runs(an animal 단수) ✔ ③ leap(can + 동사원형) ✔"),
 ],
 scr=[(L(T26, 0), T26[0][1]), (L(T26, 2), T26[2][1]), (L(T29, 1), T29[1][1]), (L(T29, 3), T29[3][1]), (L(T29, 7), T29[7][1])],
 order=[
  ([L(T26, 0), L(T26, 1), L(T26, 2), L(T26, 3)], ["1935년 맨해튼 출생", "하버드 생물학 → 1961년 코넬 박사", "1967년 혹등고래의 복잡한 소리 발견", "그 소리 = 고래의 노래, 의사소통 수단"]),
  ([L(T26, 4), L(T26, 5), L(T26, 6), L(T26, 7)], ["1970년 앨범 발매 → 히트, 고래 보호 운동", "다음 해 Ocean Alliance 설립", "100회 넘는 연구 여행", "해양 포유류 보호법 → 1986년 포경 금지"]),
  ([L(T29, 0), L(T29, 1), L(T29, 2), L(T29, 3)], ["초식동물은 위험에 다르게 반응", "어떤 종: 예민, 즉시 도주", "다른 종: 느림, 무리, 버팀", "당연히 예민한 종은 가두기 어려움"]),
  ([L(T29, 5), L(T29, 6), L(T29, 7), L(T29, 8)], ["가젤: 가장 자주 사냥된 동물", "길들일 기회가 가장 많았음", "하지만 길들여진 적 없음", "달아나고 부딪치고 뛰는 동물을 몰아 보라!"]),
 ],
 insert=[
  ([L(T26, 2), L(T26, 3), L(T26, 4)], 1, ["혹등고래의 길고 복잡한 소리 발견", "그것들(They) = 고래의 노래, 의사소통", "1970년 앨범 발매"],
   "정답 ▶ ①\n이유: They는 바로 앞의 long and complex sounds를 가리켜요. 그 소리를 '고래의 노래'라고 부른다는 설명이 이어지고, 그다음에 그 노래를 담은 앨범 이야기가 나와요."),
  ([L(T29, 1), L(T29, 2), L(T29, 3)], 1, ["어떤(Some) 종: 예민, 즉시 도주", "다른(Other) 종: 느림, 버팀", "당연히 예민한 종은 가두기 어려움"],
   "정답 ▶ ①\n이유: Some species ~ / Other species ~ 짝으로 두 종류를 비교한 뒤, '예민한 종'으로 돌아와 결론을 내려요."),
  ([L(T29, 6), L(T29, 7), L(T29, 8)], 1, ["가젤보다 길들일 기회가 많았던 종은 없음", "하지만(But) 길들여진 적 없음", "그런 동물을 몰아 보라!"],
   "정답 ▶ ①\n이유: '기회가 가장 많았다' ↔ '하지만 한 번도 길들여지지 않았다'의 역접(But). 마지막 문장은 왜 불가능했는지를 보여 줘요."),
 ],
 odd=[
  ([L(T26, 3), L(T26, 4), "Payne later regretted releasing the album because it sold poorly.", L(T26, 5)], 2,
   "정답 ▶ ③\n이유: 앨범은 '뜻밖의 히트작'이었어요. '잘 안 팔려서 후회했다'는 내용과 정반대예요."),
  ([L(T29, 2), L(T29, 3), "Nervous species usually calm down quickly in small enclosures.", L(T29, 4)], 2,
   "정답 ▶ ③\n이유: 예민한 종은 울타리에 넣으면 겁에 질려 죽기도 해요. '좁은 울타리에서 금방 진정한다'는 흐름과 반대예요."),
  ([L(T29, 5), L(T29, 6), "As a result, gazelles became the most common farm animals in the area.", L(T29, 7)], 2,
   "정답 ▶ ③\n이유: 바로 뒤에 '어떤 가젤 종도 길들여진 적 없다'가 와요. '가장 흔한 가축이 되었다'는 모순이에요."),
 ],
 blank=[
  ("Then in 1970, he released an album Songs of the Humpback Whale, which became a surprise ____ and helped start the global \"Save the Whales\" movement.", ["hit", "failure", "secret", "debt"],
   "정답 ▶ hit\n이유: 앨범이 고래 보호 운동을 시작하는 데 도움을 줄 만큼 '히트'했어요. failure(실패)면 운동을 일으킬 수 없어요."),
  ("His work helped make laws that protect ____, which finally led to the global ban on commercial whaling in 1986.", ["marine mammals", "endangered birds", "ocean plants", "fishing companies"],
   "정답 ▶ marine mammals\n이유: 결과가 '상업적 포경(고래잡이) 금지'예요. 고래 = 해양 포유류"),
  ("Naturally, the nervous species are difficult to keep in ____.", ["captivity", "the wild", "herds", "mind"],
   "정답 ▶ captivity\n이유: 바로 뒤에 울타리(enclosure)에 넣는 상황이 나와요. '가두어 기르기' 어렵다는 뜻이에요."),
  ("But no gazelle species has ever been ____.", ["domesticated", "hunted", "studied", "seen"],
   "정답 ▶ domesticated\n이유: 앞 문장에서 '길들일 기회'가 가장 많았다고 했고, But으로 반전돼요. hunted는 '가장 자주 사냥되었다'와 모순이에요."),
 ],
 gram=[
  ("다음 중 어법상 <b>틀린</b> 것은?", ["His work helped making laws.", "His work helped make laws.", "His work helped to make laws.", "His work helped us make laws."],
   "정답 ▶ His work helped making laws.\n이유: help 뒤에는 동사원형 또는 to부정사. 동명사(-ing)는 쓰지 않아요.\n포인트 ▶ help (+ 목적어) + (to) 동사원형"),
  (B + 'Seoul is known ______ its delicious street food.</b>', ['for', 'as', 'to', 'by'],
   "정답 ▶ for\n이유: be known for + 이유 = ~로 유명하다\n비교 ▶ be known as + 이름·자격 (They're known as \"whale songs.\") / be known to + 대상 (~에게 알려져 있다)"),
  ("다음 문장의 의미로 알맞은 것은?<br><b>There is no mammal species that the first settled peoples had more opportunity to domesticate than gazelles.</b>", ['가젤은 길들일 기회가 가장 많았던 동물이었다.', '가젤은 길들일 기회가 전혀 없었다.', '다른 동물들이 가젤보다 길들이기 쉬웠다.', '가젤보다 길들일 기회가 많았던 동물이 여럿 있었다.'],
   "정답 ▶ 가젤은 길들일 기회가 가장 많았던 동물이었다.\n이유: no ~ more ... than A = A보다 더 ~한 것은 없다 → A가 가장 ~하다 (비교급으로 최상급 의미)"),
  ("밑줄 친 <b>That</b>이 가리키는 내용으로 알맞은 것은?<br><b><u>That</u>'s true, for example, of gazelles.</b>", ['예민한 종은 갇히면 겁에 질려 죽을 수 있다는 것', '느린 종은 무리 속에서 보호를 구한다는 것', '가젤이 가장 자주 사냥되었다는 것', '가젤이 길들여졌다는 것'],
   "정답 ▶ 예민한 종은 갇히면 겁에 질려 죽을 수 있다는 것\n이유: That은 바로 앞 문장(울타리에 넣으면 겁에 질려 죽는다)을 가리켜요. be true of ~ = ~에 해당되다"),
  (B + 'They either die of shock ______ hit themselves against the fence.</b>', ['or', 'nor', 'and', 'but'],
   "정답 ▶ or\n이유: either A or B = A이거나 B (둘 중 하나)\n비교 ▶ neither A nor B (둘 다 아닌) / both A and B (둘 다)"),
  ("다음 중 목적어로 동명사(-ing)<b>만</b> 쓰는 동사가 <b>아닌</b> 것은?", ['want', 'imagine', 'enjoy', 'avoid'],
   "정답 ▶ want\n이유: want는 to부정사를 목적어로 써요(want to go). imagine, enjoy, avoid는 동명사만!\n본문 ▶ Just imagine trying to herd an animal ~"),
  ("밑줄 친 부분의 뜻으로 알맞은 것은?<br><b>If put into an enclosure, they <u>are likely to</u> panic.</b>", ['~할 가능성이 크다', '~하는 것을 좋아한다', '~하지 않으려 한다', '~한 적이 있다'],
   "정답 ▶ ~할 가능성이 크다\n이유: be likely to + 동사원형 = ~할 것 같다, ~할 가능성이 크다"),
 ],
 summ=[
  (26, [H26], "Roger Payne discovered that humpback whales (A) ______ through songs and devoted his life to (B) ______ whales and the oceans.",
   ['(A) communicate – (B) protecting', '(A) communicate – (B) hunting', '(A) migrate – (B) protecting', '(A) migrate – (B) hunting', '(A) sleep – (B) selling'],
   "정답 ▶ (A) communicate – (B) protecting\n(A) 고래가 노래로 '의사소통한다'는 것을 보여 줌 → communicate\n(B) Ocean Alliance 설립, 보호법 제정 → 고래와 바다를 '보호하는' 데 일생을 바침 → protecting\n오답 ▶ migrate(이동하다)는 본문에 없고, hunting(사냥)·selling(판매)은 반대 방향이에요.\n어휘 ▶ devote A to -ing A를 ~하는 데 바치다",
   ["whales use them to communicate", "he founded Ocean Alliance to protect whales"]),
  (29, [H29], "Nervous herbivores like gazelles tend to (A) ______ when confined, which explains why they have never been (B) ______.",
   ['(A) panic – (B) domesticated', '(A) panic – (B) hunted', '(A) relax – (B) domesticated', '(A) relax – (B) hunted', '(A) adapt – (B) studied'],
   "정답 ▶ (A) panic – (B) domesticated\n(A) 울타리에 갇히면 '겁에 질린다' → panic\n(B) 그래서 가젤은 한 번도 '길들여지지' 않았다 → domesticated\n오답 ▶ relax(긴장을 풀다)·adapt(적응하다)는 반대이고, hunted는 '가장 자주 사냥되었다'와 모순이에요.\n어휘 ▶ confined 갇힌",
   ["they are likely to panic", "But no gazelle species has ever been domesticated"]),
 ])

# ═════════════ DAY 5 · 30 · 31번 ═════════════
d5 = day(
 vocab=[['resource', '자원', 30], ['limited', '한정된', 30], ['tendency', '경향', 30], ['cooperate', '협력하다', 30],
        ['complicated', '복잡한', 30], ['plenty', '풍부한, 많은', 30], ['be open to -ing', '~하는 데 열려 있다', 30], ['nomadic', '유목의', 30],
        ['tribe', '부족', 30], ['in one\'s interest', '~에게 이익이 되는', 30], ['happen upon', '우연히 만나다', 30], ['hospitality', '환대', 30],
        ['survival', '생존', 30], ['depend on', '~에 달려 있다', 30], ['shelter', '쉼터, 피난처', 30], ['in need of', '~이 필요한', 30],
        ['ironically', '아이러니하게도, 역설적으로', 30], ['sophisticated', '정교한', 30], ['security', '보안', 30], ['combined with', '~과 결합된', 30],
        ['interaction', '상호작용, 교류', 30], ['common folk', '평범한 사람들', 30], ['disconnection', '단절', 30], ['blindness', '무지, 맹목', 30],
        ['content', '만족하는', 31], ['discontent', '불만족한', 31], ['determine', '결정하다', 31], ['merely', '단지, 그저', 31],
        ['successive', '연속적인', 31], ['mood', '기분', 31], ['gust', '(바람이) 한 차례 휙 불기', 31], ['adjust', '적응하다', 31],
        ['default', '기본(값)의', 31], ['well-being', '행복, 안녕', 31], ['highs and lows', '기복, 좋을 때와 나쁠 때', 31], ['baseline', '기준선', 31],
        ['euphoria', '극도의 행복감', 31], ['fade', '사라지다, 희미해지다', 31], ['despair', '절망', 31], ['long for', '간절히 바라다', 31], ['adapt', '적응하다', 31]],
 real=[
  {'n': 30, 'q': exam(30, '다음 글의 밑줄 친 부분 중, 문맥상 낱말의 쓰임이 적절하지 <u>않은</u> 것은?', Q30),
   'opts': ['⑤ increased', '① complicated', '② interest', '③ survival', '④ more'],
   'ex': "정답 ▶ ⑤ increased → decreased (줄어든)\n이유: 더 많이 가질수록 울타리를 높이고 보안을 강화해 '사람들을 멀리한다(keep people away)'고 했어요. 그러니 평범한 사람들과의 교류는 '늘어난' 게 아니라 '줄어든' 거예요. 교류가 줄어야 현실과 '단절'된다는 결론과도 맞아요.\n나머지 ▶ ① complicated: 풍족할 때 나눔 본능이 '복잡해진다' ✔ ② interest: 나누는 것이 자신들에게 '이익' ✔ ③ survival: '생존'이 나눔에 달려 있음 ✔ ④ more: '더 많이' 가질수록 덜 나눔 ✔",
   'per': [['', 'combined with our decreased physical interaction', '사람들을 멀리하니 교류는 줄어듦 → decreased'],
           ['', 'our natural tendency to share and cooperate is complicated when resources are plenty', '풍족할 때 나눔 본능이 흐려짐 ✔'],
           ['', 'because it is in their interest to do so', '나누는 게 이익 ✔'],
           ['', 'their survival depends on sharing', '생존이 나눔에 달림 ✔'],
           ['', 'the more we have, the bigger our fences', '더 많이 가질수록 ✔']]},
  {'n': 31, 'q': exam(31, '다음 빈칸에 들어갈 말로 가장 적절한 것은?', Q31),
   'opts': ['adapt', 'regret', 'explore', 'struggle', 'celebrate'],
   'ex': "정답 ▶ ① adapt (적응한다)\n이유: 글의 핵심은 '좋은 일이든 나쁜 일이든 우리는 적응해서(adjust) 원래의 행복 수준(baseline)으로 돌아간다'예요. 장난감을 받은 아이도 처음 몇 분만 행복하고, 어른처럼 곧 '적응해서' 원래 상태로 돌아가요. adjust = adapt\n오답 ▶ regret(후회하다): 후회 이야기는 없음 / explore(탐험하다) / struggle(애쓰다) / celebrate(축하하다): 행복이 계속된다는 쪽이라 반대",
   'per': [['적응한다', 'As humans, we adjust', '정답 (adjust = adapt)'], ['후회한다', '', '✘'], ['탐험한다', '', '✘'], ['힘겹게 애쓴다', '', '✘'], ['축하한다', '', '✘ (기쁨이 지속되는 쪽)']]},
 ],
 pickv=[
  ("For a species born in a time when resources were limited and dangers were great, our natural tendency to share and {cooperate|corporate} is complicated when resources are plenty and outside dangers are few.",
   "정답 ▶ cooperate (협력하다)\n오답 ▶ corporate (기업의, 법인의): share and cooperate = 나누고 협력하다 (동사 병렬). 철자 혼동 주의!"),
  ("Certain {nomadic|nominal} tribes don't have much, yet they are happy to share because it is in their interest to do so.",
   "정답 ▶ nomadic (유목의)\n오답 ▶ nominal (명목상의): 여행자를 맞이하는 '유목' 부족 이야기예요."),
  ("If you happen upon them in your travels, they will open up their homes and give you their food and {hospitality|hostility}.",
   "정답 ▶ hospitality (환대)\n오답 ▶ hostility (적대감): 집을 열어 주고 음식을 주는 것 = 환대. 반대말 혼동 주의!"),
  ("It's not just because they are nice people; it's because their survival depends on sharing, for they know that they may be the travelers in need of food and {shelter|shatter} another day.",
   "정답 ▶ shelter (쉼터, 피난처)\n오답 ▶ shatter (산산이 부수다): food and shelter = 먹을 것과 잘 곳"),
  ("Ironically, the more we have, the bigger our fences, the more sophisticated our security to keep people {away|together} and the less we want to share.",
   "정답 ▶ away\n오답 ▶ together: 울타리를 높이고 보안을 강화하는 이유는 사람들을 '멀리하기(keep away)' 위해서예요."),
  ("Our desire for more, combined with our decreased physical interaction with the \"common folk,\" starts to create a {disconnection|connection} or blindness to reality.",
   "정답 ▶ disconnection (단절)\n오답 ▶ connection (연결): 사람들과의 교류가 줄면 현실과 '단절'되고, 현실을 보지 못하게(blindness) 돼요."),
  ("Whether we feel happy or sad, content or discontent, is not determined merely by each individual {successive|successful} moment of life experience — a good thing happens and I'm happy, a bad thing happens and I'm sad.",
   "정답 ▶ successive (연속적인)\n오답 ▶ successful (성공적인): 계속 이어지는 각각의 순간. succeed의 두 뜻(뒤를 잇다/성공하다)에서 나온 혼동어!"),
  ("While our experiences affect our {mood|mode}, we are not blown in a completely new direction by each gust of wind.",
   "정답 ▶ mood (기분)\n오답 ▶ mode (방식, 모드): 경험이 '기분'에 영향을 준다"),
  ("There will be highs and lows, but over time, like water seeking its own level, we are pulled toward our {baseline|deadline} — back up after bad news and back down after good.",
   "정답 ▶ baseline (기준선)\n오답 ▶ deadline (마감 기한): 원래의 기본 행복 수준(= default level)으로 끌려간다"),
  ("The euphoria of first love {fades|grows}, and so does the despair of a break-up.",
   "정답 ▶ fades (사라지다)\n오답 ▶ grows (커지다): 좋은 감정도 나쁜 감정도 시간이 지나면 '사라져' 기준선으로 돌아가요."),
 ],
 tf=[
  ["People tend to share more readily when they have fewer resources.", True, "정답 ▶ T\n이유: 가진 것이 적을 때 나눔에 더 열려 있어요.\n어휘 ▶ readily 선뜻, 기꺼이", 30, "When we have less, we tend to be more open to sharing what we have"],
  ["Nomadic tribes share solely out of kindness.", False, "정답 ▶ F\n이유: 단지 친절해서가 아니라(not just because they are nice people) 생존이 나눔에 달려 있기 때문이에요.\n어휘 ▶ solely 오로지 · out of kindness 친절함에서", 30, "It's not just because they are nice people"],
  ["Nomads realize that they themselves might someday need help from others.", True, "정답 ▶ T\n이유: 언젠가 자신들이 도움이 필요한 여행자가 될 수 있다는 걸 알아요.", 30, "they may be the travelers in need of food and shelter another day"],
  ["Greater wealth tends to make people more eager to share.", False, "정답 ▶ F\n이유: 더 많이 가질수록 덜 나누고 싶어 해요(the less we want to share).\n어휘 ▶ wealth 부 · eager to ~하고 싶어 하는", 30, "the less we want to share"],
  ["Our mood is shaped entirely by each individual experience.", False, "정답 ▶ F\n이유: 각 순간의 경험'만으로' 결정되지 않아요(not determined merely by).\n어휘 ▶ shape 형성하다 · entirely 전적으로", 31, "is not determined merely by each individual successive moment"],
  ["Over time, people tend to return to their usual level of happiness.", True, "정답 ▶ T\n이유: 각자의 기본 행복 수준으로 돌아가요.\n어휘 ▶ usual level = default level · happiness = well-being", 31, "return to our personal default level of well-being"],
  ["The despair of a break-up lasts forever.", False, "정답 ▶ F\n이유: 'so does the despair of a break-up' → 이별의 절망도 첫사랑의 행복감처럼 사라져요.", 31, "and so does the despair of a break-up"],
  ["Children's delight over a new toy does not last long.", True, "정답 ▶ T\n이유: 처음 몇 분 동안만 행복하고, 그다음엔 적응해요.\n어휘 ▶ delight 기쁨", 31, "And for the first few minutes of the rest of their lives, they are"],
 ],
 ilchi=[
  mc(30, [H30], "글의 내용과 일치하지 <u>않는</u> 것은?",
     ["Abundance strengthens our natural tendency to share.", "Scarcity makes people more willing to share.", "Nomads offer hospitality to travelers they meet.", "Nomads' generosity is partly based on self-interest.", "Wealth tends to come with tighter security."],
     "정답 ▶ Abundance strengthens our natural tendency to share.\n이유: 자원이 풍부하면 나눔 본능은 강해지는 게 아니라 '복잡해지고(complicated)' 덜 나누게 돼요.\n어휘 ▶ abundance 풍부 · scarcity 부족 · generosity 너그러움 · self-interest 자기 이익",
     [["풍족함은 나누려는 타고난 경향을 강화한다.", "is complicated when resources are plenty", "불일치"],
      ["부족함은 사람들을 더 나누게 만든다.", "When we have less, we tend to be more open to sharing", "일치"],
      ["유목민은 만나는 여행자에게 환대를 베푼다.", "they will open up their homes and give you their food and hospitality", "일치"],
      ["유목민의 너그러움은 부분적으로 자기 이익에 바탕을 둔다.", "because it is in their interest to do so", "일치"],
      ["부유할수록 보안이 더 철저해진다.", "the more sophisticated our security to keep people away", "일치"]]),
  mc(30, [H30], "글의 내용과 <u>일치하는</u> 것은?",
     ["Wanting more can cut us off from reality.", "Our tendency to cooperate developed in times of plenty.", "Nomads share only with their own tribe members.", "The writer believes nomads are simply kinder than others.", "Wealthy people interact more with ordinary people."],
     "정답 ▶ Wanting more can cut us off from reality.\n이유: 더 많이 가지려는 욕망이 현실과의 단절을 만들어 내기 시작해요.\n어휘 ▶ cut A off from B A를 B로부터 단절시키다 · in times of plenty 풍족한 시대에",
     [["더 많이 원하는 것은 우리를 현실과 단절시킬 수 있다.", "starts to create a disconnection or blindness to reality", "일치"],
      ["협력하려는 경향은 풍족한 시대에 생겼다.", "born in a time when resources were limited", "불일치 → 자원이 부족한 시대"],
      ["유목민은 자기 부족 사람들과만 나눈다.", "If you happen upon them in your travels", "불일치 → 여행자에게도 나눔"],
      ["필자는 유목민이 그저 더 친절하다고 믿는다.", "It's not just because they are nice people", "불일치 → 생존 때문"],
      ["부유한 사람들은 평범한 사람들과 더 많이 교류한다.", "our decreased physical interaction", "불일치 → 교류가 줄어듦"]]),
  mc(31, [H31], "글의 내용과 일치하지 <u>않는</u> 것은?",
     ["Each new experience permanently changes our level of happiness.", "Our experiences influence how we feel.", "People adjust to both positive and negative events.", "Our happiness rises and falls but returns to a baseline.", "Children's joy over a toy is short-lived."],
     "정답 ▶ Each new experience permanently changes our level of happiness.\n이유: 경험이 기분에 영향은 주지만, 우리는 결국 기본 행복 수준으로 돌아가요. '영구적으로' 바뀌지 않아요.\n어휘 ▶ permanently 영구적으로 · short-lived 오래가지 않는",
     [["새로운 경험마다 행복 수준이 영구적으로 바뀐다.", "return to our personal default level of well-being", "불일치"],
      ["경험은 우리의 기분에 영향을 준다.", "While our experiences affect our mood", "일치"],
      ["사람은 좋은 일과 나쁜 일 모두에 적응한다.", "we adjust — to new information and events both good and bad", "일치"],
      ["행복은 오르내리지만 기준선으로 돌아간다.", "There will be highs and lows, but over time", "일치"],
      ["장난감으로 인한 아이의 기쁨은 오래가지 않는다.", "And for the first few minutes of the rest of their lives, they are", "일치"]]),
  mc(31, [H31], "글의 내용과 <u>일치하는</u> 것은?",
     ["The joy of first love eventually fades away.", "Bad news permanently lowers our well-being.", "Children stay happy longer than adults do.", "Adults rarely adapt to new situations.", "A break-up causes lifelong despair."],
     "정답 ▶ The joy of first love eventually fades away.\n이유: The euphoria of first love fades\n어휘 ▶ eventually 결국 · lifelong 평생 동안의",
     [["첫사랑의 기쁨은 결국 사라진다.", "The euphoria of first love fades", "일치"],
      ["나쁜 소식은 행복을 영구적으로 떨어뜨린다.", "back up after bad news", "불일치 → 다시 올라감"],
      ["아이들은 어른보다 더 오래 행복하다.", "But then the kids — like adults — adapt", "불일치 → 어른처럼 적응"],
      ["어른들은 새 상황에 거의 적응하지 않는다.", "As humans, we adjust", "불일치"],
      ["이별은 평생의 절망을 가져온다.", "and so does the despair of a break-up", "불일치 → 절망도 사라짐"]]),
 ],
 pickg=[
  ("For a species born in a time {when|which} resources were limited and dangers were great, our natural tendency to share and cooperate is complicated when resources are plenty and outside dangers are few.",
   "정답 ▶ when\n이유: 선행사 a time(시간) + 뒤에 완전한 절(resources were limited) → 관계부사 when\n오답 ▶ which 뒤에는 주어나 목적어가 빠진 불완전한 절이 와요."),
  ("When we have less, we tend to be more open to {sharing|share} what we have.",
   "정답 ▶ sharing\n이유: be open to의 to는 전치사! 전치사 뒤에는 동명사\n포인트 ▶ to가 전치사인 표현: be open to -ing, look forward to -ing, be used to -ing"),
  ("Certain nomadic tribes don't have much, yet they are happy to share because it is in their interest {to do|doing} so.",
   "정답 ▶ to do\n이유: it(가주어) ~ to부정사(진주어). it is in their interest to do so = 그렇게 하는 것이 그들에게 이익이다"),
  ("It's not just because they are nice people; it's because their survival depends on sharing, {for|during} they know that they may be the travelers in need of food and shelter another day.",
   "정답 ▶ for\n이유: 뒤에 '주어 + 동사(they know)'가 오므로 접속사가 필요해요. 콤마 뒤 for = 왜냐하면 ~이니까(이유)\n오답 ▶ during은 전치사라 뒤에 명사만 와요."),
  ("Ironically, the more we have, the {bigger|biggest} our fences, the more sophisticated our security to keep people away and the less we want to share.",
   "정답 ▶ bigger\n이유: the 비교급 ~, the 비교급 … = ~할수록 더 …하다. 최상급 biggest ✘"),
  ("Whether we feel happy or sad, content or discontent, {is|are} not determined merely by each individual successive moment of life experience — a good thing happens and I'm happy, a bad thing happens and I'm sad.",
   "정답 ▶ is\n이유: 주어는 Whether ~ discontent라는 명사절 하나 → 단수 취급 → is\n함정 ▶ 바로 앞 discontent나 happy or sad에 속지 마세요."),
  ("While our experiences affect our mood, we are not {blown|blowing} in a completely new direction by each gust of wind.",
   "정답 ▶ blown\n이유: 우리가 바람에 '날려 가는' 것 → 수동 be + p.p. (blow - blew - blown). 뒤의 by each gust of wind가 힌트"),
  ("There will be highs and lows, but over time, like water {seeking|sought} its own level, we are pulled toward our baseline — back up after bad news and back down after good.",
   "정답 ▶ seeking\n이유: 물이 스스로 제 수위를 '찾아가는'(능동) → 현재분사 seeking이 water를 꾸며요."),
  ("The euphoria of first love fades, and so {does|is} the despair of a break-up.",
   "정답 ▶ does\n이유: so + 동사 + 주어 = ~도 그렇다. 앞 동사 fades(일반동사, 현재, 단수)를 받으니 does\n포인트 ▶ be동사면 so is, 조동사면 so can"),
  ("This tendency is best seen with little kids and their toy joy: When they get {what|that} they've longed for, they believe they will be happy for the rest of their lives.",
   "정답 ▶ what\n이유: get의 목적어 자리 + 뒤 절에 목적어가 빠짐(longed for ___) + 앞에 선행사 없음 → what(~하는 것)\n오답 ▶ that은 선행사가 필요해요."),
 ],
 verb=[
  ("For a species ___ in a time when resources were limited and dangers were great, our natural tendency to share and cooperate is complicated when resources are plenty and outside dangers are few.", 'bear', ['born'], "정답 ▶ born\n이유: a species (which was) born ~ → '태어난' 종. 과거분사 born이 앞의 명사를 꾸며요. bear - bore - born"),
  ("Certain nomadic tribes don't have much, yet they are happy ___ because it is in their interest to do so.", 'share', ['to share'], "정답 ▶ to share\n이유: be happy to + 동사원형 = 기꺼이 ~하다"),
  ("The euphoria of first love ___, and so does the despair of a break-up.", 'fade', ['fades'], "정답 ▶ fades\n이유: 주어 The euphoria(단수), 일반적인 사실 → 현재형 3인칭 단수 fades. 뒤의 so does와도 짝이 맞아요."),
  ("This tendency is best ___ with little kids and their toy joy: When they get what they've longed for, they believe they will be happy for the rest of their lives.", 'see', ['seen'], "정답 ▶ seen\n이유: 경향이 '보이는' 것 → 수동 is seen. best는 '가장 잘'(부사)"),
  ("This tendency is best seen with little kids and their toy joy: When they get what they've ___ for, they believe they will be happy for the rest of their lives.", 'long', ['longed'], "정답 ▶ longed\n이유: they've(they have) + p.p. → 현재완료 longed. long for = 간절히 바라다"),
 ],
 error=[
  ("When we have less, we tend to be more open to [[share]] [[what]] we [[have]].", 0, 'sharing',
   "틀린 곳 ▶ ① share → sharing\n이유: be open to의 to는 전치사 → 동명사\n나머지 ▶ ② what(~하는 것, 선행사 없음) ✔ ③ have ✔"),
  ("Certain nomadic tribes don't have much, [[yet]] they are happy to share because [[it]] is in their interest [[doing]] so.", 2, 'to do',
   "틀린 곳 ▶ ③ doing → to do\n이유: 가주어 it ~ 진주어 to부정사\n나머지 ▶ ① yet(그렇지만, 접속사) ✔ ② it(가주어) ✔"),
  ("If you [[happen]] upon them in your travels, they will open up their homes and [[gave]] you their food and [[hospitality]].", 1, 'give',
   "틀린 곳 ▶ ② gave → give\n이유: will open up ~ and (will) give → 조동사 뒤 병렬은 동사원형\n나머지 ▶ ① happen upon(우연히 만나다) ✔ ③ hospitality(명사) ✔"),
  ("Ironically, the [[more]] we have, the [[biggest]] our fences, the more sophisticated our security to keep people away and the [[less]] we want to share.", 1, 'bigger',
   "틀린 곳 ▶ ② biggest → bigger\n이유: the 비교급, the 비교급 구문 → 모두 비교급\n나머지 ▶ ① more ✔ ③ less(little의 비교급) ✔"),
  ("As humans, we adjust — to new information and events both good and bad — and [[returning]] to our personal [[default]] level of [[well-being]].", 0, 'return',
   "틀린 곳 ▶ ① returning → return\n이유: we adjust ~ and return ~ → 주어 we의 동사 두 개가 and로 병렬. 대시(— —) 사이의 삽입구를 빼고 보면 쉬워요.\n나머지 ▶ ② default(기본의) ✔ ③ well-being(명사) ✔"),
  ("This tendency is best [[seen]] with little kids and their toy joy: When they get [[that]] they've longed for, they [[believe]] they will be happy for the rest of their lives.", 1, 'what',
   "틀린 곳 ▶ ② that → what\n이유: 선행사가 없고 longed for의 목적어가 빠져 있어요 → 관계대명사 what\n나머지 ▶ ① seen(수동) ✔ ③ believe ✔"),
 ],
 scr=[(L(T30, 1), T30[1][1]), (L(T30, 2), T30[2][1]), (L(T31, 1), T31[1][1]), (L(T31, 4), T31[4][1]), (L(T31, 6), T31[6][1])],
 order=[
  ([L(T30, 1), L(T30, 2), L(T30, 3), L(T30, 4)], ["가진 게 적을수록 나눔에 열려 있음", "유목 부족: 적게 가졌지만 기꺼이 나눔", "여행자에게 집과 음식을 내줌", "친절해서가 아니라 생존 때문"]),
  ([L(T30, 4), L(T30, 5), L(T30, 6)], ["유목민: 생존이 나눔에 달려 있음", "역설: 많이 가질수록 울타리·보안↑, 나눔↓", "욕망 + 교류 감소 → 현실과 단절"]),
  ([L(T31, 0), L(T31, 1), L(T31, 2), L(T31, 3)], ["행복은 각 순간으로만 정해지지 않음", "경험이 기분에 영향은 주지만 휩쓸리진 않음", "적응하고 기본 수준으로 돌아감", "기복이 있어도 기준선으로 끌려감"]),
  ([L(T31, 4), L(T31, 5), L(T31, 6), L(T31, 7)], ["첫사랑의 황홀감도, 이별의 절망도 사라짐", "아이들: 바라던 걸 얻으면 평생 행복할 거라 믿음", "처음 몇 분은 정말 행복함", "하지만 어른처럼 적응함"]),
 ],
 insert=[
  ([L(T30, 2), L(T30, 3), L(T30, 4)], 1, ["유목 부족: 적게 가졌지만 기꺼이 나눔", "그들(them)을 만나면 집과 음식을 내줌", "그것(It)은 친절해서가 아니라 생존 때문"],
   "정답 ▶ ①\n이유: them은 nomadic tribes를 가리켜요. 마지막 문장의 It은 '집과 음식을 내주는 행동'을 가리키니, 그 행동이 먼저 나와야 해요."),
  ([L(T30, 4), L(T30, 5), L(T30, 6)], 1, ["유목민: 생존이 나눔에 달려 있음", "아이러니하게도 많이 가질수록 덜 나눔", "욕망 + 교류 감소 → 단절"],
   "정답 ▶ ①\n이유: Ironically(아이러니하게도)는 앞 내용(적게 가진 사람들은 기꺼이 나눔)과 반대되는 상황을 이끌어요."),
  ([L(T31, 5), L(T31, 6), L(T31, 7)], 1, ["아이들은 평생 행복할 거라 믿음", "그리고 처음 몇 분은 정말 그렇다(they are)", "하지만(But) 곧 적응함"],
   "정답 ▶ ①\n이유: they are 뒤에는 앞 문장의 happy가 생략되어 있어요. 그래서 '평생 행복할 거라 믿는다' 바로 뒤에 와야 하고, But으로 반전돼요."),
 ],
 odd=[
  ([L(T30, 2), L(T30, 3), "Nomadic tribes usually refuse to let strangers into their homes.", L(T30, 4)], 2,
   "정답 ▶ ③\n이유: 유목민은 여행자에게 집을 열어 주고 음식을 내줘요. '낯선 사람을 들이지 않는다'는 정반대예요."),
  ([L(T30, 4), L(T30, 5), "Wealthy people are usually the most eager to share with strangers.", L(T30, 6)], 2,
   "정답 ▶ ③\n이유: 많이 가질수록 덜 나누고 싶어 한다고 했어요. '부자가 가장 나누고 싶어 한다'는 흐름과 맞지 않아요."),
  ([L(T31, 4), L(T31, 5), "Children usually stay happy with a new toy for many years.", L(T31, 6)], 2,
   "정답 ▶ ③\n이유: 아이들의 기쁨은 처음 몇 분뿐이고 곧 적응해요. '몇 년 동안 행복하다'는 내용과 반대예요."),
 ],
 blank=[
  ("When we have ____, we tend to be more open to sharing what we have.", ["less", "more", "plenty", "everything"],
   "정답 ▶ less\n이유: 이어지는 예가 '가진 것이 많지 않은(don't have much)' 유목 부족이에요. 적게 가질 때 더 나눠요."),
  ("It's not just because they are nice people; it's because their ____ depends on sharing, for they know that they may be the travelers in need of food and shelter another day.", ["survival", "reputation", "religion", "wealth"],
   "정답 ▶ survival\n이유: 언젠가 자신들도 음식과 쉼터가 필요한 여행자가 될 수 있으니, 나눔은 '생존'의 문제예요."),
  ("As humans, we ____ — to new information and events both good and bad — and return to our personal default level of well-being.", ["adjust", "resist", "overreact", "give up"],
   "정답 ▶ adjust\n이유: 좋은 일이든 나쁜 일이든 '적응해서' 원래 수준으로 돌아간다. 31번 정답 adapt와 같은 뜻이에요."),
  ("The euphoria of first love fades, and so does the ____ of a break-up.", ["despair", "excitement", "euphoria", "hope"],
   "정답 ▶ despair\n이유: 좋은 감정(첫사랑의 황홀감)과 나쁜 감정(이별의 '절망')이 모두 사라진다는 대비예요."),
 ],
 gram=[
  (B + 'Tom likes pizza, and so ______ his sister.</b>', ['does', 'is', 'likes', 'do'],
   "정답 ▶ does\n이유: so + 동사 + 주어 = ~도 그렇다. likes(일반동사, 현재, 3인칭 단수 his sister) → does\n본문 ▶ The euphoria of first love fades, and so does the despair of a break-up."),
  ("밑줄 친 <b>Whether</b>의 뜻으로 알맞은 것은?<br><b><u>Whether</u> we feel happy or sad is not determined merely by each moment.</b>", ['~인지 (아닌지)', '~이든 아니든 (양보)', '~할 때', '~이기 때문에'],
   "정답 ▶ ~인지 (아닌지)\n이유: Whether절이 문장의 주어(명사절)로 쓰였어요. '우리가 행복한지 슬픈지는 ~ 결정되지 않는다'\n비교 ▶ 부사절이면 '~이든 아니든' (Whether you like it or not, ...)"),
  ("밑줄 친 <b>for</b>와 쓰임이 <b>같은</b> 것은?<br><b>Their survival depends on sharing, <u>for</u> they know that they may need help.</b>", ["He felt no fear, <u>for</u> he was brave.", "This gift is <u>for</u> you.", "I waited <u>for</u> an hour.", "She is famous <u>for</u> her voice."],
   "정답 ▶ He felt no fear, for he was brave.\n이유: 콤마 뒤 for + 주어 + 동사 = 왜냐하면 ~이니까 (접속사)\n오답 ▶ 나머지는 모두 전치사 for (~을 위해, ~ 동안, ~로)"),
  ("밑줄 친 <b>they are</b> 뒤에 생략된 말은?<br><b>They believe they will be happy for the rest of their lives. And for the first few minutes, <u>they are</u>.</b>", ['happy', 'children', 'sad', 'adults'],
   "정답 ▶ happy\n이유: 앞 문장과 겹치는 말(happy)을 생략했어요. they are (happy) = 처음 몇 분 동안은 정말 행복하다"),
  ("밑줄 친 <b>While</b>의 뜻으로 알맞은 것은?<br><b><u>While</u> our experiences affect our mood, we are not blown in a new direction.</b>", ['~이긴 하지만', '~하는 동안', '~ 때문에', '~하자마자'],
   "정답 ▶ ~이긴 하지만 (양보)\n이유: '경험이 기분에 영향을 주긴 하지만, 완전히 휩쓸리지는 않는다'. 앞뒤 내용이 대조돼요.\n비교 ▶ while이 '~하는 동안'(시간)일 때도 있어요."),
  ("밑줄 친 부분의 뜻으로 알맞은 것은?<br><b>If you <u>happen upon</u> them in your travels, they will open up their homes.</b>", ['우연히 만나다', '찾아 나서다', '공격하다', '피하다'],
   "정답 ▶ 우연히 만나다\n이유: happen upon(on) = come across = 우연히 마주치다"),
  (B + 'I still remember the day ______ I first met her.</b>', ['when', 'which', 'where', 'what'],
   "정답 ▶ when\n이유: 선행사 the day(시간) + 뒤에 완전한 절 → 관계부사 when\n본문 ▶ a time when resources were limited"),
 ],
 summ=[
  (30, [H30], "People with (A) ______ resources tend to share more, while having more makes us (B) ______ to share.",
   ['(A) fewer – (B) less willing', '(A) fewer – (B) more eager', '(A) more – (B) less willing', '(A) more – (B) more eager', '(A) no – (B) afraid'],
   "정답 ▶ (A) fewer – (B) less willing\n(A) 가진 것이 '적을' 때 더 나눈다 → fewer\n(B) 많이 가질수록 '덜 나누고 싶어' 한다 → less willing\n오답 ▶ more eager(더 나누고 싶어 하는)는 반대예요.\n어휘 ▶ willing to ~할 의향이 있는",
   ["When we have less, we tend to be more open to sharing what we have", "the less we want to share"]),
  (31, [H31], "Although experiences (A) ______ our mood for a while, we eventually (B) ______ to our usual level of happiness.",
   ['(A) affect – (B) return', '(A) affect – (B) never return', '(A) fix – (B) return', '(A) fix – (B) never return', '(A) ignore – (B) rise'],
   "정답 ▶ (A) affect – (B) return\n(A) 경험은 기분에 '영향을 준다' → affect\n(B) 결국 기본 행복 수준으로 '돌아간다' → return\n오답 ▶ fix(고정하다)는 '휩쓸리지 않는다'와 맞지 않고, never return은 글의 핵심과 반대예요.",
   ["While our experiences affect our mood", "return to our personal default level of well-being"]),
 ])

D4 = {'id': 'd4', 'name': 'DAY 4', 'range': '26·29번', 'story': '26 내용 불일치(인물) · 29 어법',
      'passage': sec(H26) + rows(T26) + sec(H29) + rows(T29), 'steps': d4}
D5 = {'id': 'd5', 'name': 'DAY 5', 'range': '30·31번', 'story': '30 어휘 · 31 빈칸',
      'passage': sec(H30) + rows(T30) + sec(H31) + rows(T31), 'steps': d5}

path = '/home/claude/proj/data/h1-mock-2509.js'
src = open(path).read()
assert "id: 'd4'" not in src
tail = "\n  ]\n};\n})();"
i = src.rstrip().rfind(tail.strip()[:3])  # 마지막 '  ]'
i = src.rstrip().rfind('\n  ]\n};')
assert i > 0
src = src[:i].rstrip() + ',\n  ' + js(D4, '  ') + ',\n  ' + js(D5, '  ') + src[i:]
for a, b in [("unit: '18~24번',", "unit: '18~24 · 26 · 29~31번',")]:
    assert src.count(a) == 1, a
    src = src.replace(a, b, 1)
src = src.replace("영어 18~24번\n", "영어 18~24 · 26 · 29~31번 (26~31번은 scratchpad/gen_h1m2509b.py 로 추가)\n", 1)
open(path, 'w').write(src)
print('ok')
