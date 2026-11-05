N=35
MC=[
 dict(q="글의 내용과 <u>일치하는</u> 것은?",opts=[
  "The term \"artificial intelligence\" took the place of an earlier expression.",
  "Interest in thinking machines began only in the 20th century.",
  "Alan Turing was an American physicist.",
  "John McCarthy developed a test to measure machine intelligence.",
  "Mary Shelley wrote the myth of Pandora."],
  ex="정답 ▶ The term \"artificial intelligence\" took the place of an earlier expression.\n이유: replacing the previously used expression \"automata studies.\" 예전 표현을 대신했어요.\n오답 ▶ ② for centuries(수 세기 동안), since ancient Greece ③ British mathematician(영국의 수학자) ④ 테스트를 만든 건 Turing ⑤ Pandora는 고대 그리스 신화, Mary Shelley는 Frankenstein\n포인트 ▶ take the place of = replace 대신하다 · earlier = previously used",
  per=[["'인공지능'이라는 용어가 이전 표현을 대신했다.","replacing the previously used expression","take the place of = replace ✔"],
       ["생각하는 기계에 대한 관심은 20세기에야 시작되었다.","since ancient Greece","for centuries · ancient Greece ✗"],
       ["Alan Turing은 미국의 물리학자였다.","British mathematician Alan Turing","British mathematician"],
       ["John McCarthy가 기계 지능을 측정하는 테스트를 개발했다.","developed the Turing test to measure a machine's intelligence","테스트 개발 = Turing"],
       ["Mary Shelley가 판도라 신화를 썼다.","Mary Shelley's Frankenstein","Shelley = Frankenstein"]]),
 dict(q="글의 내용과 일치하지 <u>않는</u> 것은?",opts=[
  "AI machines are designed to think in ways completely unlike humans.",
  "Legends of man-made beings have existed since ancient Greek times.",
  "Writers throughout history have imagined creating human-like creatures.",
  "Turing wanted to find out whether machines could think independently.",
  "The phrase \"automata studies\" was in use before \"artificial intelligence.\""],
  ex="정답 ▶ AI machines are designed to think in ways completely unlike humans.\n이유: programmed to think like humans 인간'처럼' 생각하도록 프로그래밍돼요.\n오답 ▶ 나머지는 모두 본문을 바꿔 쓴 일치 문장\n포인트 ▶ unlike ~와 달리 ↔ like · legend 전설 ≒ myth · man-made 인공의 = artificial · independently = autonomously 자율적으로",
  per=[["AI 기계는 인간과 완전히 다르게 생각하도록 설계된다.","programmed to think like humans","unlike ↔ like ✗"],
       ["인공 존재에 관한 전설은 고대 그리스 시대부터 있었다.","artificial beings since ancient Greece","legends ≒ myths · man-made = artificial"],
       ["역사 속 작가들은 인간 같은 생명체를 만드는 것을 상상해 왔다.","literature throughout history has dreamed of creating human-like creatures","writers ≒ literature · imagine ≒ dream of"],
       ["Turing은 기계가 독립적으로 생각할 수 있는지 알아내고 싶었다.","whether the machines can think autonomously","independently = autonomously"],
       ["'automata studies'라는 말은 '인공지능'보다 먼저 쓰였다.","replacing the previously used expression","in use before = previously used"]]),
 dict(q="글의 내용과 <u>일치하는</u> 것은?",opts=[
  "튜링 테스트는 기계가 스스로 생각할 수 있는지도 측정하려 했다.",
  "판도라 신화는 세상에 행복을 가져다준 이야기이다.",
  "'인공지능'이라는 말은 Turing이 처음 만들었다.",
  "McCarthy는 1950년보다 앞서 '인공지능'이라는 말을 만들었다.",
  "인공지능 기계는 학습 능력 없이 정해진 일만 하도록 만들어진다."],
  ex="정답 ▶ 튜링 테스트는 기계가 스스로 생각할 수 있는지도 측정하려 했다.\n이유: to measure a machine's intelligence and whether the machines can think autonomously\n오답 ▶ ② ills = 불행, 재앙 ③ coined는 McCarthy ④ A few years later(1950년 몇 년 후) ⑤ endowed with reasoning and learning 추론과 학습 능력을 부여받음\n포인트 ▶ autonomously 자율적으로, 스스로 · ills 불행 · coin (새 말을) 만들다",
  per=[["","whether the machines can think autonomously","일치 ✔"],
       ["","the myth of Pandora, who released ills upon the world","ills = 불행"],
       ["","MIT professor John McCarthy coined","만든 사람 = McCarthy"],
       ["","A few years later, MIT professor John McCarthy coined","1950년 몇 년 '후'"],
       ["","endowed by their creators with reasoning and learning","학습 능력을 부여받음"]])]
TF=[
 ["People have long imagined machines capable of making decisions like humans.",True,"정답 ▶ T\n이유: 인간은 수 세기 동안 인간 같은 결정을 내리는 기계를 꿈꿔 왔어요.\n어휘 ▶ long 오랫동안 = for centuries · imagine ≒ dream of · capable of ~할 수 있는","make human-like decisions"],
 ["In the myth, Pandora brought misfortunes into the world.",True,"정답 ▶ T\n이유: 판도라는 세상에 온갖 불행(ills)을 풀어놓았어요.\n어휘 ▶ misfortune 불행 = ills · bring into = release upon","who released ills upon the world"],
 ["Frankenstein is given as an example of ancient Greek mythology.",False,"정답 ▶ F\n이유: Frankenstein은 '문학(literature)'의 예예요. 고대 그리스 신화의 예는 판도라.\n어휘 ▶ mythology 신화","Mary Shelley's Frankenstein"],
 ["Turing came up with a test to evaluate how intelligent a machine is.",True,"정답 ▶ T\n이유: 기계의 지능을 측정하려고 튜링 테스트를 개발했어요.\n어휘 ▶ come up with = develop 생각해 내다 · evaluate = measure","developed the Turing test to measure a machine's intelligence"],
 ["John McCarthy was a British mathematician.",False,"정답 ▶ F\n이유: 영국의 수학자는 Turing, McCarthy는 MIT 교수예요.","MIT professor John McCarthy"],
 ["The phrase \"artificial intelligence\" was invented several years after 1950.",True,"정답 ▶ T\n이유: 1950년 Turing 이후 몇 년 뒤(A few years later) McCarthy가 만들었어요.\n어휘 ▶ invent = coin (새 말을) 만들다","A few years later, MIT professor John McCarthy coined"],
 ["Today's AI aims to give machines the ability to reason and learn.",True,"정답 ▶ T\n이유: 창조자가 추론과 학습 능력을 부여한(endowed) 기계를 만드는 것이에요.\n어휘 ▶ endow A with B A에게 B를 부여하다","endowed by their creators with reasoning and learning"]]
PICK1=[
 {"s":"There have been myths about robots, automatons, and artificial beings since ancient Greece (e.g., the myth of Pandora, who {released|relieved} ills upon the world).","ex":"정답 ▶ released (풀어놓다)\n오답 ▶ relieved (덜어 주다, 안심시키다)\n포인트 ▶ release A upon B = B에 A를 풀어놓다 · ills 불행, 재앙"},
 {"s":"{Likewise|Otherwise}, literature throughout history has dreamed of creating human-like creatures and thinking machines (e.g., Mary Shelley's Frankenstein).","ex":"정답 ▶ Likewise (마찬가지로)\n오답 ▶ Otherwise (그렇지 않으면)\n이유: 앞의 '신화'에 이어 '문학'도 같은 꿈을 꿨다 → 비슷한 예를 덧붙이는 Likewise"},
 {"s":"A few years later, MIT professor John McCarthy coined \"artificial intelligence,\" replacing the {previously|presently} used expression \"automata studies.\"","ex":"정답 ▶ previously (이전에)\n오답 ▶ presently (현재)\n이유: 새 용어가 '이전에 쓰이던' 표현을 대신했어요."},
 {"s":"Since then, artificial intelligence has become the study and practice of \"making intelligent machines\" that are programmed to think like humans — {endowed|endangered} by their creators with reasoning and learning.","ex":"정답 ▶ endowed (부여받은)\n오답 ▶ endangered (멸종 위기의)\n포인트 ▶ endow A with B = A에게 B를 부여하다 → (A is) endowed with B"}]
PICK2=[
 {"s":"Humans for centuries have dreamed of machines that could become intelligent and {make|making} human-like decisions.","ex":"정답 ▶ make\n이유: could에 become과 make가 and로 병렬 → 동사원형"},
 {"s":"Likewise, literature throughout history has dreamed of {creating|create} human-like creatures and thinking machines (e.g., Mary Shelley's Frankenstein).","ex":"정답 ▶ creating\n이유: 전치사 of 뒤 → 동명사 (dream of -ing ~하는 것을 꿈꾸다)"},
 {"s":"There {have|has} been myths about robots, automatons, and artificial beings since ancient Greece (e.g., the myth of Pandora, who released ills upon the world).","ex":"정답 ▶ have\n이유: There + be 뒤의 명사(myths, 복수)가 진짜 주어 → have been\n포인트 ▶ since(~ 이래로) → 현재완료"},
 {"s":"In 1950, British mathematician Alan Turing asked whether machines could think and reason like humans and then {developed|developing} the Turing test to measure a machine's intelligence and whether the machines can think autonomously.","ex":"정답 ▶ developed\n이유: 주어 Alan Turing의 동사 asked와 and then으로 병렬 → 과거형 developed"}]
VERB=[
 {"s":"There have been myths about robots, automatons, and artificial beings since ancient Greece (e.g., the myth of Pandora, who ___ ills upon the world).","v":"release","a":["released"],"ex":"정답 ▶ released\n이유: 신화 속 과거의 일 → 과거시제"},
 {"s":"A few years later, MIT professor John McCarthy ___ \"artificial intelligence,\" replacing the previously used expression \"automata studies.\"","v":"coin","a":["coined"],"ex":"정답 ▶ coined\n이유: A few years later(1950년 몇 년 후), 과거의 일 → 과거시제\n포인트 ▶ coin (새 말을) 만들다"},
 {"s":"Since then, artificial intelligence has become the study and practice of \"making intelligent machines\" that are programmed to think like humans — ___ by their creators with reasoning and learning.","v":"endow","a":["endowed"],"ex":"정답 ▶ endowed\n이유: 기계가 추론·학습 능력을 '부여받은' 수동 → 과거분사 (be endowed with)"}]
ERR=[
 {"s":"Humans for centuries [[have dreamed]] of machines that could become [[intelligently]] and [[make]] human-like decisions.","w":1,"fix":"intelligent","ex":"틀린 곳 ▶ ② intelligently → intelligent\n이유: become 뒤 보어 → 형용사\n나머지 ▶ ① for centuries → 현재완료 ✔ ③ could + make 병렬 ✔"},
 {"s":"There [[has]] been myths about robots, automatons, and artificial beings since ancient Greece (e.g., the myth of Pandora, [[who]] [[released]] ills upon the world).","w":0,"fix":"have","ex":"틀린 곳 ▶ ① has → have\n이유: 진짜 주어 myths(복수)\n나머지 ▶ ② 사람(Pandora) + 콤마 → who ✔ ③ 과거의 일 ✔"},
 {"s":"Since then, artificial intelligence [[has become]] the study and practice of \"making intelligent machines\" that [[is]] programmed to think like humans — [[endowed]] by their creators with reasoning and learning.","w":1,"fix":"are","ex":"틀린 곳 ▶ ② is → are\n이유: that의 선행사 intelligent machines(복수)\n나머지 ▶ ① Since then → 현재완료 ✔ ③ 부여받은(수동) ✔"}]
SCR=[3,5,("고대 그리스 이래로 로봇, 자동 장치, 인공 존재에 관한 신화가 있어 왔다.","There have been myths about robots, automatons, and artificial beings since ancient Greece."),("마찬가지로 역사를 통틀어 문학은 인간과 같은 생명체와 생각하는 기계를 만드는 것을 꿈꿔 왔다.","Likewise, literature throughout history has dreamed of creating human-like creatures and thinking machines.")]
ORDER=[{"idx":[2,3,4,5],"flow":["문학도 인간 같은 생명체·생각하는 기계를 꿈꿈","1950년 Turing: 기계가 생각할 수 있나? → 튜링 테스트","몇 년 후 McCarthy가 '인공지능'이라는 말을 만듦","그 이후 AI = 지능적인 기계를 만드는 연구·실천"]}]
INSERT=[{"idx":[0,1,2,3],"given":2,"flow":["인간은 수 세기 동안 지능 있는 기계를 꿈꿈","고대 그리스 이래 인공 존재 신화(판도라)","마찬가지로(Likewise) 문학도(프랑켄슈타인)","1950년 Turing"],"ex":"정답 ▶ ②\n이유: Likewise(마찬가지로)는 앞에 비슷한 예가 있어야 해요. '신화' 다음에 '문학'을 덧붙이고, 그다음 1950년 Turing으로 시대순으로 이어져요.\n포인트 ▶ 신화(고대) → 문학(역사 전체) → 1950년 → 몇 년 후: 시간 흐름"}]
ODD=[{"lines":[0,1,"However, ancient people never imagined that non-human beings could think.",2],"odd":2,"ex":"정답 ▶ ③\n이유: 바로 앞 문장이 고대 그리스 이래 인공 존재 신화가 있었다는 내용이에요. 고대인이 그런 상상을 한 적 없다는 문장은 앞뒤와 모순이에요."}]
BLANK=[
 {"s":"In 1950, British mathematician Alan Turing asked whether machines could think and reason like humans and then developed the Turing test to measure a machine's intelligence and whether the machines can think ____.","opts":["autonomously","slowly","randomly","collectively"],"ex":"정답 ▶ autonomously (자율적으로, 스스로)\n이유: '인간처럼 생각하고 추론할 수 있는지' → 스스로 생각할 수 있는지를 측정\n오답 ▶ slowly 천천히 · randomly 무작위로 · collectively 집단으로"},
 {"s":"A few years later, MIT professor John McCarthy coined \"artificial intelligence,\" replacing the ____ used expression \"automata studies.\"","opts":["previously","currently","rarely","officially"],"ex":"정답 ▶ previously (이전에)\n이유: 새 용어가 그 전에 쓰이던 표현을 대신(replacing)했어요.\n오답 ▶ currently 현재 · rarely 드물게 · officially 공식적으로"},
 {"s":"Likewise, literature throughout history has dreamed of creating human-like creatures and ____ machines (e.g., Mary Shelley's Frankenstein).","opts":["thinking","sewing","farming","vending"],"ex":"정답 ▶ thinking (생각하는)\n이유: 글 전체가 '인간처럼 생각하는 기계(AI)'의 역사예요.\n오답 ▶ sewing machine 재봉틀 · farming machine 농기계 · vending machine 자판기"}]
GRAM=[
 {"q":"빈칸에 알맞은 것은?<br><b>I asked him ______ he could help me.</b>","opts":["whether","that","what","which"],"ex":"정답 ▶ whether (~인지 아닌지)\n이유: ask의 목적어로 '~인지'를 묻는 명사절 → whether(= if)\n본문 ▶ Alan Turing asked whether machines could think"},
 {"q":"빈칸에 알맞은 것은?<br><b>She has always dreamed of ______ a pilot.</b>","opts":["becoming","become","to become","became"],"ex":"정답 ▶ becoming\n이유: dream of + 동명사\n본문 ▶ has dreamed of creating human-like creatures"},
 {"q":"빈칸에 알맞은 것은?<br><b>He coined a new term, ______ the old one.</b>","opts":["replacing","replaced","replace","to replacing"],"ex":"정답 ▶ replacing\n이유: 분사구문. 주어 He가 옛 용어를 '대신하는' 능동 → 현재분사\n본문 ▶ coined \"artificial intelligence,\" replacing the previously used expression"},
 {"q":"빈칸에 알맞은 것은?<br><b>This is the myth of Pandora, ______ released ills upon the world.</b>","opts":["who","which","that","whose"],"ex":"정답 ▶ who\n이유: 선행사 Pandora(사람) + 콤마(계속적 용법) → who. that은 콤마 뒤에 못 써요.\n본문 ▶ the myth of Pandora, who released ills upon the world"}]
