N=39
MC=[
 dict(q="글의 내용과 <u>일치하는</u> 것은?",opts=[
  "A morally good person commits bad acts considerably less frequently than most people.",
  "Only a person's actions should be considered when judging her.",
  "Preventing harm by accident is enough to make someone morally good.",
  "The writer believes results have nothing to do with moral goodness.",
  "The writer fully agrees with Kant's view of moral goodness."],
  ex="정답 ▶ A morally good person commits bad acts considerably less frequently than most people.\n이유: one who does morally bad actions significantly less often than most\n오답 ▶ ② not only her actions but also her intentions and motives(의도·동기도) ③ unintentionally(의도치 않게) 막은 사람은 선하지 않음 ④ But actual consequences are important ⑤ contrary to Kant(칸트와 달리)\n포인트 ▶ commit (나쁜 일을) 저지르다 = do · considerably = significantly 상당히 · frequently = often",
  per=[["도덕적으로 선한 사람은 대부분의 사람보다 나쁜 행동을 상당히 덜 자주 한다.","does morally bad actions significantly less often than most","considerably = significantly · frequently = often ✔"],
       ["사람을 판단할 때는 오직 행동만 고려해야 한다.","not only her actions but also her intentions and motives are relevant","only ✗ → not only ~ but also"],
       ["우연히 해를 막은 것만으로도 도덕적으로 선해진다.","A person who unintentionally prevents harm","by accident = unintentionally → not morally good"],
       ["필자는 결과가 도덕적 선함과 아무 관계가 없다고 믿는다.","But actual consequences are important","nothing to do with ✗"],
       ["필자는 칸트의 도덕적 선함에 대한 견해에 전적으로 동의한다.","contrary to Kant","contrary to ~와 반대로"]]),
 dict(q="글의 내용과 일치하지 <u>않는</u> 것은?",opts=[
  "Accidentally preventing harm is a common event in everyday life.",
  "A morally good person aims to do good and to steer clear of bad actions.",
  "A person's intentions and motives matter when we judge her.",
  "Someone whose attempts to prevent harm always fail is not usually seen as morally good.",
  "We might say that such a person has good intentions."],
  ex="정답 ▶ Accidentally preventing harm is a common event in everyday life.\n이유: this kind of situation generally occurs only in slapstick movies. 이런 일은 대개 슬랩스틱 영화에서나 일어나요.\n오답 ▶ 나머지는 모두 본문을 바꿔 쓴 일치 문장\n포인트 ▶ aim to = intend to · steer clear of = avoid 피하다 · matter = are relevant · be seen as = be thought of as · have good intentions = mean well",
  per=[["의도치 않게 해를 막는 일은 일상에서 흔하다.","generally occurs only in slapstick movies","common in everyday life ✗ → 영화에서나"],
       ["선한 사람은 선을 행하고 나쁜 행동은 피하려고 한다.","intend to do morally good actions and intend to avoid morally bad ones","aim to = intend to · steer clear of = avoid"],
       ["사람을 판단할 때 의도와 동기가 중요하다.","her intentions and motives are relevant","matter ≒ are relevant"],
       ["해를 막으려는 시도가 늘 실패하는 사람은 대개 선하다고 여겨지지 않는다.","is not generally thought of as morally good","be seen as = be thought of as"],
       ["그런 사람은 선의를 가지고 있다고 말할 수 있다.","it may be said that she means well","have good intentions = mean well"]]),
 dict(q="글의 내용과 <u>일치하는</u> 것은?",opts=[
  "늘 해를 막으려 하지만 한 번도 막지 못하는 사람은 대개 선하다고 여겨지지 않는다.",
  "도덕적으로 선한 사람은 나쁜 행동을 전혀 하지 않는 사람이다.",
  "의도치 않게 해를 막은 사람도 도덕적으로 선하다.",
  "필자는 행동의 실제 결과는 전혀 중요하지 않다고 본다.",
  "필자는 칸트의 생각에 전적으로 동의한다."],
  ex="정답 ▶ 늘 해를 막으려 하지만 한 번도 막지 못하는 사람은 대개 선하다고 여겨지지 않는다.\n이유: A person who always tries to prevent harm but never does, is not generally thought of as morally good.\n오답 ▶ ② 전혀 안 하는 게 아니라 '상당히 덜 자주'(significantly less often) ③ is not morally good ④ actual consequences are important ⑤ contrary to Kant\n포인트 ▶ 의도(intention)도 결과(result)도 둘 다 필요하다는 글",
  per=[["","is not generally thought of as morally good","일치 ✔"],
       ["","significantly less often than most","전혀 ✗ → 덜 자주"],
       ["","is not morally good","선하지 않음"],
       ["","But actual consequences are important","결과도 중요"],
       ["","contrary to Kant","칸트와 반대"]])]
TF=[
 ["A morally good person never does anything morally bad.",False,"정답 ▶ F\n이유: 나쁜 행동을 대부분의 사람보다 '상당히 덜 자주' 하는 사람이에요. 전혀 안 하는 게 아니에요.\n어휘 ▶ never 전혀 ~ 않다 ↔ less often 덜 자주","does morally bad actions significantly less often than most"],
 ["A morally good person does good deeds much more often than most people.",True,"정답 ▶ T\n이유: 좋은 행동을 대부분의 사람보다 상당히 더 자주 해요.\n어휘 ▶ deed 행위 = action · much = significantly","does morally good ones significantly more often than most"],
 ["A morally good person must aim to steer clear of bad actions.",True,"정답 ▶ T\n이유: 나쁜 행동을 피하려고 의도해야 해요.\n어휘 ▶ aim to = intend to · steer clear of = avoid","intend to avoid morally bad ones"],
 ["Harm being avoided purely by chance mostly happens in comedy films.",True,"정답 ▶ T\n이유: 이런 상황은 대개 슬랩스틱 영화(몸개그 코미디)에서나 일어나요.\n어휘 ▶ by chance 우연히 = unintentionally · slapstick 슬랩스틱(과장된 몸짓 코미디)","generally occurs only in slapstick movies"],
 ["The writer warns against believing that only actual results matter in moral judgment.",True,"정답 ▶ T\n이유: 실제 결과만이 중요하다는 잘못된 인상을 피하려고 언급한다고 했어요.\n어휘 ▶ warn against ~하지 말라고 경고하다 · false impression 잘못된 인상","to avoid the false impression"],
 ["According to the writer, actual consequences do not matter at all.",False,"정답 ▶ F\n이유: 하지만 실제 결과도 중요하다(But actual consequences are important)고 했어요.\n어휘 ▶ not ~ at all 전혀 ~ 않다","But actual consequences are important."],
 ["We may say that a person who never succeeds in preventing harm means well.",True,"정답 ▶ T\n이유: 그런 사람에 대해 선의를 가지고 있다(means well)고 말할 수는 있어요. 다만 선하다고 여겨지진 않아요.\n어휘 ▶ mean well 선의를 갖다","it may be said that she means well"]]
PICK1=[
 {"s":"In judging a person not only her actions but also her intentions and {motives|motors} are relevant.","ex":"정답 ▶ motives (동기)\n오답 ▶ motors (모터)\n포인트 ▶ intention 의도 · motive 동기 — 둘 다 '마음속 이유'"},
 {"s":"Although this kind of situation generally occurs only in {slapstick|lipstick} movies, it is worth mentioning to avoid the false impression that it is the actual consequences of a person's actions that count toward her being judged morally good or bad.","ex":"정답 ▶ slapstick (슬랩스틱, 과장된 몸개그 코미디)\n오답 ▶ lipstick (립스틱)\n이유: 의도와 반대로 일이 꼬여 우연히 해를 막는 상황은 현실보다 코미디 영화에서나 나와요."},
 {"s":"Although this kind of situation generally occurs only in slapstick movies, it is worth mentioning to avoid the false {impression|expression} that it is the actual consequences of a person's actions that count toward her being judged morally good or bad.","ex":"정답 ▶ impression (인상)\n오답 ▶ expression (표현)\n포인트 ▶ the false impression that ~ = ~라는 잘못된 인상(that은 동격)"},
 {"s":"Of such a person, it may be said that she means well; but, contrary to Kant, some results are necessary before she is {regarded|rewarded} as morally good.","ex":"정답 ▶ regarded (여겨지다)\n오답 ▶ rewarded (보상받다)\n포인트 ▶ regard A as B = A를 B로 여기다 → A is regarded as B"}]
PICK2=[
 {"s":"A person who unintentionally prevents harm to others and does not harm them simply because things do not turn out as she {intends|intend} is not morally good.","ex":"정답 ▶ intends\n이유: as절의 주어 she(3인칭 단수), 현재시제"},
 {"s":"A person who unintentionally prevents harm to others and does not harm them simply because things do not turn out as she intends {is|are} not morally good.","ex":"정답 ▶ is\n이유: 문장의 주어는 A person(단수). who ~ intends 전체가 수식어\n포인트 ▶ 긴 주어 → 핵심 명사 찾기!"},
 {"s":"Although this kind of situation generally occurs only in slapstick movies, it is worth mentioning to avoid the false impression that it is the actual consequences of a person's actions that {count|counts} toward her being judged morally good or bad.","ex":"정답 ▶ count\n이유: It is ~ that 강조 구문. 강조된 주어 the actual consequences(복수)에 맞춰 count"},
 {"s":"Although this kind of situation generally occurs only in slapstick movies, it is worth mentioning to avoid the false impression that it is the actual consequences of a person's actions that count toward her being {judged|judging} morally good or bad.","ex":"정답 ▶ judged\n이유: 그녀가 '판단되는' 수동 → being + p.p.(동명사의 수동). her는 동명사의 의미상 주어"},
 {"s":"A person who always tries to prevent harm but never {does|do}, is not generally thought of as morally good.","ex":"정답 ▶ does\n이유: 주격 관계대명사 who의 선행사 A person(단수) → tries ~ but never does. does는 prevents harm을 대신하는 대동사\n포인트 ▶ but never does = but never prevents harm"}]
VERB=[
 {"s":"A morally good person must intend to do morally good actions and ___ to avoid morally bad ones.","v":"intend","a":["intend"],"ex":"정답 ▶ intend\n이유: 조동사 must 뒤에 intend ~ and intend로 병렬 → 동사원형"},
 {"s":"A person who unintentionally prevents harm to others and does not harm them simply because things do not ___ out as she intends is not morally good.","v":"turn","a":["turn"],"ex":"정답 ▶ turn\n이유: do not + 동사원형\n포인트 ▶ turn out (일이) ~하게 되다, 결과가 ~로 드러나다"},
 {"s":"A person who always tries to prevent harm but never does, is not generally ___ of as morally good.","v":"think","a":["thought"],"ex":"정답 ▶ thought\n이유: 사람이 '여겨지는' 수동 → is thought of as\n포인트 ▶ think of A as B = A를 B로 여기다 (think - thought - thought)"}]
ERR=[
 {"s":"A person who unintentionally [[prevents]] harm to others and does not harm them simply because things do not turn out as she [[intend]] [[is]] not morally good.","w":1,"fix":"intends","ex":"틀린 곳 ▶ ② intend → intends\n이유: 주어 she(3인칭 단수)\n나머지 ▶ ① 선행사 A person(단수) → prevents ✔ ③ 문장 주어 A person → is ✔"},
 {"s":"Although this kind of situation generally occurs only in slapstick movies, it is worth mentioning to avoid the false impression that it is the actual consequences of a person's actions that [[counts]] toward her [[being]] [[judged]] morally good or bad.","w":0,"fix":"count","ex":"틀린 곳 ▶ ① counts → count\n이유: 강조된 주어 the actual consequences(복수)\n나머지 ▶ ② 전치사 toward + 동명사 ✔ ③ 판단'되는' 수동 ✔"},
 {"s":"Of such a person, it may be [[said]] that she means well; but, [[contrary]] to Kant, some results are necessary before she [[regards]] as morally good.","w":2,"fix":"is regarded","ex":"틀린 곳 ▶ ③ regards → is regarded\n이유: 그녀가 선하다고 '여겨지는' 수동 (regard A as B → A is regarded as B)\n나머지 ▶ ① it may be said that ~라고 말할 수 있다 ✔ ② contrary to ~와 반대로 ✔"}]
SCR=[2,5,0,7]
ORDER=[{"idx":[0,1,2,3],"flow":["선한 사람 = 나쁜 일은 덜, 좋은 일은 더 자주","판단할 때 행동뿐 아니라 의도·동기도 중요","선한 사람은 선을 행하고 악을 피하려 의도해야","의도치 않게 해를 막은 사람은 선하지 않음"]}]
INSERT=[{"idx":[4,5,6,7],"given":1,"flow":["(우연한 경우를 든 건) 결과만 중요하다는 오해를 피하려고","하지만(But) 실제 결과도 중요","늘 막으려 하지만 못 막는 사람은 선하다고 안 여겨짐","그런 사람은 선의는 있지만, 결과도 필요"],"ex":"정답 ▶ ①\n이유: 앞 문장은 '결과만 중요하다는 건 오해'라는 말이고, But으로 '그래도 결과는 중요하다'고 균형을 잡아요. 그 뒤에 '늘 실패하는 사람' 예시가 이어져요.\n포인트 ▶ 의도 강조 → But → 결과도 중요 → 예시"}]
ODD=[{"lines":[5,6,"Most people who try to prevent harm usually succeed in the end.",7],"odd":2,"ex":"정답 ▶ ③\n이유: 앞뒤 문장은 '늘 막으려 하지만 결코 못 막는 사람(such a person)'에 대한 이야기예요. 대부분 결국 성공한다는 일반론은 흐름에서 벗어나고, 다음 문장의 such a person이 가리킬 대상도 끊어 버려요."}]
BLANK=[
 {"s":"A morally good person is one who does morally bad actions significantly ____ often than most and does morally good ones significantly more often than most.","opts":["less","more","as","so"],"ex":"정답 ▶ less\n이유: 나쁜 행동은 '덜' 자주, 좋은 행동은 '더' 자주 — 대비 구조예요. than이 있으니 비교급(less/more)\n오답 ▶ more: 나쁜 일을 더 자주 하면 선한 사람이 아니죠."},
 {"s":"Although this kind of situation generally occurs only in ____ movies, it is worth mentioning to avoid the false impression.","opts":["slapstick","horror","documentary","war"],"ex":"정답 ▶ slapstick (슬랩스틱 코미디)\n이유: 의도와 반대로 일이 꼬여 '우연히' 해를 막는 황당한 상황 → 몸개그 코미디 영화에서나 나와요.\n오답 ▶ horror 공포 · documentary 다큐멘터리 · war 전쟁"},
 {"s":"Of such a person, it may be said that she means well; but, contrary to Kant, some ____ are necessary before she is regarded as morally good.","opts":["results","excuses","intentions","rules"],"ex":"정답 ▶ results (결과)\n이유: 선의(means well)는 이미 있으니, 선하다고 여겨지려면 '결과'도 필요해요. 앞의 actual consequences are important와 연결\n오답 ▶ intentions 의도 — 이미 있는 것이라 답이 될 수 없어요."}]
GRAM=[
 {"q":"빈칸에 알맞은 것은?<br><b>She always tries ______ harm to others.</b>","opts":["to prevent","prevent","prevented","to preventing"],"ex":"정답 ▶ to prevent\n이유: try to do ~하려고 애쓰다\n포인트 ▶ try -ing 시험 삼아 ~해 보다\n본문 ▶ A person who always tries to prevent harm"},
 {"q":"빈칸에 알맞은 것은?<br><b>Nobody likes ______ judged by others.</b>","opts":["being","to","be","been"],"ex":"정답 ▶ being\n이유: like의 목적어 동명사, 내가 '판단되는' 수동 → being + p.p.\n본문 ▶ count toward her being judged morally good or bad"},
 {"q":"밑줄 친 <b>contrary to</b>의 뜻으로 알맞은 것은?<br><b><u>Contrary to</u> Kant, some results are necessary.</b>","opts":["~와는 반대로","~에 따르면","~ 덕분에","~와 마찬가지로"],"ex":"정답 ▶ ~와는 반대로\n이유: 칸트는 의도만 중요하다고 봤지만, 필자는 '그와 달리' 결과도 필요하다고 해요.\n오답 ▶ according to ~에 따르면 · thanks to ~ 덕분에 · like ~와 마찬가지로"}]
