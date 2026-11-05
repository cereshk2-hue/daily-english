N=33
MC=[
 dict(q="글의 내용과 <u>일치하는</u> 것은?",opts=[
  "How important uncertainty is varies from situation to situation.",
  "The public generally finds it easy to grasp the idea of uncertainty.",
  "The Earth-sun distance given was measured throughout the entire year.",
  "Six significant digits guarantee enough accuracy for any purpose.",
  "Launching a satellite near the sun requires less exact figures than predicting sunrise."],
  ex="정답 ▶ How important uncertainty is varies from situation to situation.\n이유: the significance of uncertainty is relative. 불확실성의 중요성은 상대적이에요(상황에 따라 달라요).\n오답 ▶ ② difficult(어렵다) ↔ easy ③ at one point during the year(한 시점) ↔ throughout the entire year(1년 내내) ④ 목적에 따라 달라요 ⑤ 위성은 '더 정확한' 거리가 필요해요\n포인트 ▶ relative 상대적인 = varies(달라지다) · significance = importance · grasp = appreciate 이해하다",
  per=[["불확실성이 얼마나 중요한지는 상황마다 다르다.","the significance of uncertainty is relative","relative(상대적인) = varies from situation to situation ✔"],
       ["대중은 대체로 불확실성 개념을 쉽게 이해한다.","makes uncertainty difficult for members of the public to appreciate","difficult ↔ easy · grasp = appreciate"],
       ["제시된 지구-태양 거리는 1년 내내 측정된 것이다.","as measured at one point during the year","한 시점 ↔ 1년 내내"],
       ["유효 숫자 여섯 자리면 어떤 목적에도 충분히 정확하다.","depends on what I'm intending to do with it","목적에 따라 다름 → any purpose ✗"],
       ["태양 근처로 위성을 쏘는 데는 일출 예측보다 덜 정확한 수치가 필요하다.","I would need to know distances more accurately","more accurately ↔ less exact"]]),
 dict(q="글의 내용과 일치하지 <u>않는</u> 것은?",opts=[
  "The quoted figure is too inexact to tell what minute the sun will rise.",
  "Whether the figure counts as precise is determined by the writer's goal.",
  "Using six significant digits implies an accuracy of roughly one in a million.",
  "An uncertain next digit means an error bigger than the distance between two cities.",
  "Sending a satellite to orbit close to the sun calls for more exact distances."],
  ex="정답 ▶ The quoted figure is too inexact to tell what minute the sun will rise.\n이유: If I care only about what minute the sun will rise tomorrow, then the number quoted here is fine. 일출 시각엔 이 숫자로 '충분'해요.\n오답 ▶ 나머지는 모두 본문을 바꿔 쓴 일치 문장\n포인트 ▶ inexact 부정확한 ↔ precise · fine 괜찮은, 충분한 · roughly = or so 대략 · call for = need 필요로 하다 · goal = what I'm intending to do",
  per=[["인용된 수치는 해가 몇 분에 뜰지 알기에는 너무 부정확하다.","then the number quoted here is fine","fine(충분하다) ↔ too inexact ✗"],
       ["그 수치가 정확하다고 볼 수 있는지는 글쓴이의 목적에 따라 정해진다.","depends on what I'm intending to do with it","is determined by = depends on · goal = intending"],
       ["유효 숫자 여섯 자리는 대략 백만분의 일 정도의 정확도를 뜻한다.","an accuracy of one part in a million or so","roughly = or so · implies = means"],
       ["다음 자리 숫자가 불확실하면 두 도시 사이 거리보다 큰 오차가 생긴다.","is larger than the distance between New York and Chicago","bigger = larger"],
       ["태양 가까이 위성을 보내려면 더 정확한 거리가 필요하다.","I would need to know distances more accurately","call for = need · exact = accurate"]]),
 dict(q="글의 내용과 <u>일치하는</u> 것은?",opts=[
  "같은 숫자라도 무엇에 쓰느냐에 따라 정확한지 아닌지가 달라진다.",
  "지구와 태양 사이의 거리는 1년 내내 같은 값으로 측정된다.",
  "유효 숫자 여섯 자리는 천분의 일 정도의 정확도를 뜻한다.",
  "다음 자리 숫자의 불확실성은 뉴욕과 시카고 사이 거리보다 작다.",
  "내일 해가 몇 분에 뜨는지 알려면 더 정확한 거리가 필요하다."],
  ex="정답 ▶ 같은 숫자라도 무엇에 쓰느냐에 따라 정확한지 아닌지가 달라진다.\n이유: Whether or not the quoted number is \"precise\" therefore depends on what I'm intending to do with it.\n오답 ▶ ② 1년 중 '한 시점'에 측정한 값 ③ one part in a million = 백만분의 일 ④ larger(더 크다) ⑤ 일출 시각엔 이 숫자로 충분(fine), 더 정확해야 하는 건 위성\n포인트 ▶ depend on ~에 달려 있다 · one part in a million 백만분의 일",
  per=[["","depends on what I'm intending to do with it","일치 ✔"],
       ["","as measured at one point during the year","한 시점에 측정"],
       ["","an accuracy of one part in a million or so","백만분의 일"],
       ["","is larger than the distance between New York and Chicago","더 크다"],
       ["","then the number quoted here is fine","일출은 이 숫자로 충분"]])]
TF=[
 ["Ordinary people often struggle to fully understand uncertainty.",True,"정답 ▶ T\n이유: 대중이 불확실성을 제대로 이해하기 어렵다고 했어요.\n어휘 ▶ ordinary people = members of the public · struggle to ~하는 데 애를 먹다 · understand = appreciate","makes uncertainty difficult for members of the public to appreciate"],
 ["The importance of uncertainty is the same in every situation.",False,"정답 ▶ F\n이유: 불확실성의 중요성은 상대적(relative)이에요. 상황마다 달라요.\n어휘 ▶ importance = significance · the same in every situation ↔ relative","the significance of uncertainty is relative"],
 ["The Earth-sun figure in the passage was taken at a single moment in the year.",True,"정답 ▶ T\n이유: 1년 중 한 시점에 측정된 값이에요.\n어휘 ▶ take (측정값을) 얻다 · a single moment = one point","as measured at one point during the year"],
 ["Six significant digits indicate an accuracy of about one part in a thousand.",False,"정답 ▶ F\n이유: 대략 백만분의 일(one part in a million or so)의 정확도예요.\n어휘 ▶ indicate 나타내다 = mean · about = or so","an accuracy of one part in a million or so"],
 ["The writer believes the figure is precise no matter how it is used.",False,"정답 ▶ F\n이유: 정확한지 아닌지는 무엇을 하려는지에 달려 있어요.\n어휘 ▶ no matter how 어떻게 ~하든 상관없이","depends on what I'm intending to do with it"],
 ["At first glance, the Earth-sun figure looks fairly exact.",True,"정답 ▶ T\n이유: 비교적 정확해 보인다(seems relatively precise)고 했어요.\n어휘 ▶ at first glance 언뜻 보기에 · look = seem · fairly = relatively · exact = precise","This seems relatively precise"],
 ["A satellite mission close to the sun would demand more accurate data than a sunrise question.",True,"정답 ▶ T\n이유: 일출 시각은 이 숫자로 충분하지만, 태양 바로 위로 위성을 보내려면 거리를 더 정확히 알아야 해요.\n어휘 ▶ demand 요구하다 = need","I would need to know distances more accurately"]]
PICK1=[
 {"s":"One of the things that makes uncertainty difficult for members of the public to appreciate is that the {significance|signature} of uncertainty is relative.","ex":"정답 ▶ significance (중요성, 의미)\n오답 ▶ signature (서명)\n포인트 ▶ significant 중요한, 의미 있는 → significant digits 유효 숫자"},
 {"s":"One of the things that makes uncertainty difficult for members of the public to appreciate is that the significance of uncertainty is {relative|absolute}.","ex":"정답 ▶ relative (상대적인)\n오답 ▶ absolute (절대적인)\n이유: 같은 숫자도 일출 계산엔 충분하고 위성 발사엔 부족해요. 목적에 따라 달라지니 '상대적'\n포인트 ▶ 이 글의 주제 문장 = 33번 빈칸 정답"},
 {"s":"This seems relatively precise; after all, using six significant digits means I know the distance to an {accuracy|ambiguity} of one part in a million or so.","ex":"정답 ▶ accuracy (정확도)\n오답 ▶ ambiguity (모호함)\n이유: 앞에서 '비교적 정확해 보인다'고 했으니 백만분의 일의 '정확도'\n포인트 ▶ accurate 정확한 · accurately 정확하게"},
 {"s":"If I want to send a {satellite|settlement} to orbit just above the sun, however, then I would need to know distances more accurately.","ex":"정답 ▶ satellite (인공위성)\n오답 ▶ settlement (정착, 합의)\n포인트 ▶ orbit 궤도를 돌다, 궤도"}]
PICK2=[
 {"s":"One of the things that makes uncertainty difficult for members of the public {to appreciate|appreciating} is that the significance of uncertainty is relative.","ex":"정답 ▶ to appreciate\n이유: make + 목적어 + 형용사(difficult) + for 의미상 주어 + to부정사: …가 ~하기 어렵게 만들다\n포인트 ▶ difficult for A to do = A가 ~하기 어려운"},
 {"s":"One of the things that makes uncertainty difficult for members of the public to appreciate is that the significance of uncertainty {is|are} relative.","ex":"정답 ▶ is\n이유: that절의 주어는 the significance(단수). of uncertainty는 수식어\n포인트 ▶ 주어 + 전치사구 → 동사는 앞의 핵심 명사에 맞춰요."},
 {"s":"However, if the next digit is uncertain, that means the uncertainty in knowing the precise Earth-sun distance {is|are} larger than the distance between New York and Chicago!","ex":"정답 ▶ is\n이유: 주어는 the uncertainty(단수). in knowing ~ distance는 수식어"},
 {"s":"This seems relatively precise; after all, using six significant digits {means|mean} I know the distance to an accuracy of one part in a million or so.","ex":"정답 ▶ means\n이유: 동명사구 주어(using six significant digits)는 단수 취급 → means\n포인트 ▶ digits(복수)에 속지 말 것!"}]
VERB=[
 {"s":"However, if the next digit is uncertain, that means the uncertainty in ___ the precise Earth-sun distance is larger than the distance between New York and Chicago!","v":"know","a":["knowing"],"ex":"정답 ▶ knowing\n이유: 전치사 in 뒤 → 동명사\n포인트 ▶ uncertainty in knowing ~ = ~을 아는 데 있어서의 불확실성"},
 {"s":"Whether or not the ___ number is \"precise\" therefore depends on what I'm intending to do with it.","v":"quote","a":["quoted"],"ex":"정답 ▶ quoted\n이유: 숫자가 '인용된' 수동 → 과거분사가 명사 앞에서 수식 (the quoted number = 인용된 숫자)"},
 {"s":"This ___ relatively precise; after all, using six significant digits means I know the distance to an accuracy of one part in a million or so.","v":"seem","a":["seems"],"ex":"정답 ▶ seems\n이유: 주어 This(단수), 현재시제 → seems. seem + 형용사 = ~해 보이다"}]
ERR=[
 {"s":"One of the things that makes uncertainty [[difficultly]] for members of the public [[to appreciate]] [[is]] that the significance of uncertainty is relative.","w":0,"fix":"difficult","ex":"틀린 곳 ▶ ① difficultly → difficult\n이유: make + 목적어 + 목적격보어 → 형용사\n나머지 ▶ ② for 의미상 주어 + to부정사 ✔ ③ 주어 One(of the things) → is ✔"},
 {"s":"This seems relatively precise; after all, [[using]] six significant digits [[mean]] I know the distance to an accuracy of one part in a million [[or so]].","w":1,"fix":"means","ex":"틀린 곳 ▶ ② mean → means\n이유: 동명사구 주어 using six significant digits는 단수\n나머지 ▶ ① 동명사 주어 ✔ ③ or so 대략, ~쯤 ✔"},
 {"s":"If I want to send a satellite to orbit just above the sun, however, then I would need [[knowing]] distances [[more]] [[accurately]].","w":0,"fix":"to know","ex":"틀린 곳 ▶ ① knowing → to know\n이유: need는 to부정사를 목적어로 (need to do ~할 필요가 있다)\n나머지 ▶ ② ③ more accurately 더 정확하게 — 동사 know를 꾸미는 부사 ✔"}]
SCR=[5,6,0,2]
ORDER=[{"idx":[3,4,5,6],"flow":["다음 자리가 불확실하면 오차가 뉴욕-시카고 거리보다 큼","그러므로 정확한지는 목적에 달려 있음","일출 시각만 궁금하면 이 숫자로 충분","하지만(however) 위성을 보내려면 더 정확해야 함"]}]
INSERT=[{"idx":[0,1,2,3],"given":2,"flow":["불확실성의 중요성은 상대적","예: 지구-태양 거리 1.49597 × 10⁸ km","이건 꽤 정확해 보임(유효 숫자 6자리)","하지만(However) 다음 자리가 불확실하면 오차가 엄청 큼"],"ex":"정답 ▶ ②\n이유: 주어진 문장의 This는 바로 앞의 숫자(1.49597 × 10⁸ km)를 가리키고, '정확해 보인다'고 한 뒤에야 However(하지만)로 '사실은 오차가 크다'고 뒤집을 수 있어요.\n포인트 ▶ 통념(정확해 보임) → However → 반전"}]
ODD=[{"lines":[1,2,"In fact, astronomers have now measured this distance without any uncertainty at all.",3],"odd":2,"ex":"정답 ▶ ③\n이유: 바로 다음 문장에서 다음 자리 숫자가 불확실하다고 해요. '불확실성이 전혀 없다'는 문장은 글의 흐름(불확실성의 의미는 상대적)과 맞지 않아요.\n어휘 ▶ astronomer 천문학자"}]
BLANK=[
 {"s":"One of the things that makes uncertainty difficult for members of the public to appreciate is that the significance of uncertainty is ____.","opts":["relative","permanent","negligible","universal"],"ex":"정답 ▶ relative (상대적인)\n이유: 같은 숫자가 일출 계산엔 충분하고 위성 발사엔 부족 → 중요성이 목적에 따라 달라요.\n오답 ▶ permanent 영구적인 · negligible 무시해도 될 만한 · universal 보편적인"},
 {"s":"This seems relatively ____; after all, using six significant digits means I know the distance to an accuracy of one part in a million or so.","opts":["precise","rough","doubtful","misleading"],"ex":"정답 ▶ precise (정확한)\n이유: after all(어쨌든) 뒤에 '백만분의 일의 정확도'라는 근거가 나와요.\n오답 ▶ rough 대략적인 · doubtful 의심스러운 · misleading 오해의 소지가 있는"},
 {"s":"If I want to send a satellite to orbit just above the sun, however, then I would need to know distances more ____.","opts":["accurately","roughly","quickly","cheaply"],"ex":"정답 ▶ accurately (정확하게)\n이유: however로 일출(이 숫자로 충분)과 대조 → 위성은 '더 정확하게' 알아야 해요.\n오답 ▶ roughly 대략 · quickly 빨리 · cheaply 싸게"}]
GRAM=[
 {"q":"빈칸에 알맞은 것은?<br><b>The noise made it difficult ______ me to concentrate.</b>","opts":["for","of","to","with"],"ex":"정답 ▶ for\n이유: to부정사의 의미상 주어 = for + 목적격 (difficult, easy 등 일반 형용사)\n포인트 ▶ 사람의 성격 형용사(kind, wise…)일 때만 of\n본문 ▶ makes uncertainty difficult for members of the public to appreciate"},
 {"q":"빈칸에 알맞은 것은?<br><b>One of my friends ______ in Canada.</b>","opts":["lives","live","living","to live"],"ex":"정답 ▶ lives\n이유: One of + 복수명사 → 주어는 One(단수)\n본문 ▶ One of the things ... is that ~"},
 {"q":"빈칸에 알맞은 것은?<br><b>Using six digits ______ that we know the distance well.</b>","opts":["means","mean","meaning","to mean"],"ex":"정답 ▶ means\n이유: 동명사(구) 주어는 단수 취급\n본문 ▶ using six significant digits means I know the distance"},
 {"q":"다음 중 어법상 알맞은 것은?","opts":["I wonder what time the sun will rise tomorrow.","I wonder what time will the sun rise tomorrow.","I wonder what time does the sun rise tomorrow.","I wonder what time rise the sun tomorrow."],"ex":"정답 ▶ I wonder what time the sun will rise tomorrow.\n이유: 간접의문문 어순 = 의문사 + 주어 + 동사\n본문 ▶ what minute the sun will rise tomorrow"}]
