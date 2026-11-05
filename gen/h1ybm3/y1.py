VOCAB=[[w,m,n]+x for w,m,n,*x in [
 ["prodigy","영재, 신동","❶"],["early childhood","유년기, 어린 시절","❶"],["reflect on","~을 되돌아보다, 회상하다","❶"],["youth","어린 시절, 젊은 시절","❶"],
 ["excitedly","신이 나서, 흥분하여","❶"],["can't wait to","~하기를 몹시 기다리다, 빨리 ~하고 싶다","❶","couldn't wait to"],["algebra","대수학","❶"],["geometry","기하학","❶"],
 ["hometown","고향","❷"],["segregated","(인종 등에 따라) 분리된, 차별하는","❷"],["education system","교육 제도","❷"],["so that","~할 수 있도록","❷"],
 ["graduate from","~을 졸업하다","❷"],["be admitted to","~에 입학 허가를 받다","❷"],["junior year","(4년제 대학의) 3학년","❷"],["offer","~을 제공하다","❷"],
 ["mentor","멘토, 조언자","❷"],["gladly","기꺼이","❷"],["outstanding","뛰어난","❷"],["career opportunity","직업 기회","❷"],
 ["make","(자질이 있어) ~이 되다","❷"],["research mathematician","연구 수학자","❷"],["prepare A for B","A가 B를 준비하게 하다","❷"],
 ["reply","대답하다","❷"],["path","길","❷"],["unclear","불확실한, 분명하지 않은","❷"],["full of","~로 가득 찬","❷"],["obstacle","장애물","❷"],
 ["strength","힘, 강인함","❷"],["make one's way","나아가다, 길을 헤쳐 나가다","❷"],["with highest honors","최우등으로","❷"],["public school","공립 학교","❷"],
 ["option","선택(지)","❷"],["available","이용할 수 있는, 얻을 수 있는","❷"]]]
PICK1=[
 {"s":"Katherine was a math {prodigy|product} from early childhood.","ex":"정답 ▶ prodigy (영재, 신동)\n오답 ▶ product (제품)\n이유: 어릴 때부터 모든 것을 세고, 대수학·기하학을 빨리 배우고 싶어 함 → 수학 영재"},
 {"s":"She {excitedly|reluctantly} added, \"I couldn't wait to get to high school to take algebra and geometry.\"","ex":"정답 ▶ excitedly (신이 나서)\n오답 ▶ reluctantly (마지못해)\n이유: couldn't wait to(빨리 ~하고 싶었다) → 들뜬 마음"},
 {"s":"But Katherine's hometown had a {segregated|integrated} education system, and black students could not enter high school.","ex":"정답 ▶ segregated (분리된, 차별하는)\n오답 ▶ integrated (통합된)\n이유: 흑인 학생들이 고등학교에 들어갈 수 없었다 → 인종에 따라 나뉜 제도"},
 {"s":"After graduating from high school in 1932, she was {admitted|omitted} to a black college at the age of fifteen.","ex":"정답 ▶ admitted (be admitted to ~에 입학 허가를 받다)\n오답 ▶ omitted (생략된)"},
 {"s":"Her mentor {gladly|unwillingly} offered special classes just for her, but he was not happy when he had to tell his outstanding student about her career opportunities.","ex":"정답 ▶ gladly (기꺼이)\n오답 ▶ unwillingly (마지못해)\n이유: but 뒤의 '기쁘지 않았다(was not happy)'와 대조 → 수업은 '기꺼이' 해 줬어요."},
 {"s":"Her mentor gladly offered special classes just for her, but he was not happy when he had to tell his {outstanding|ordinary} student about her career opportunities.","ex":"정답 ▶ outstanding (뛰어난)\n오답 ▶ ordinary (평범한)\n이유: 3학년 때 이미 모든 수학 과정을 다 들은 학생 → 뛰어난 학생"},
 {"s":"The path ahead was {unclear|bright} and full of obstacles, but Katherine knew she had the strength to make her own way.","ex":"정답 ▶ unclear (불확실한)\n오답 ▶ bright (밝은)\n이유: full of obstacles(장애물로 가득한)와 나란히, but 뒤의 '그래도 힘이 있었다'와 대조 → 앞길이 불확실"},
 {"s":"The path ahead was unclear and full of {obstacles|opportunities}, but Katherine knew she had the strength to make her own way.","ex":"정답 ▶ obstacles (장애물)\n오답 ▶ opportunities (기회)\n이유: 일자리 문제는 '너의 문제'라는 말 뒤 → 장애물 가득한 길"},
 {"s":"The path ahead was unclear and full of obstacles, but Katherine knew she had the {strength|weakness} to make her own way.","ex":"정답 ▶ strength (힘, 강인함)\n오답 ▶ weakness (약함)\n이유: but으로 어려움과 대조 → 스스로 길을 헤쳐 나갈 '힘'"},
 {"s":"At that time, teaching was the only {option|opinion} available to her.","ex":"정답 ▶ option (선택지)\n오답 ▶ opinion (의견)\n이유: 당시 흑인 여성에게 열린 '유일한 선택지'가 교사였어요."}]
TF=[
 ["Katherine was the oldest child in her family.",False,"정답 ▶ F\n이유: 네 자녀 중 막내(the youngest)였어요.\n어휘 ▶ oldest ↔ youngest","❶","was the youngest of four children"],
 ["Katherine showed an exceptional talent for math from a young age.",True,"정답 ▶ T\n이유: 어릴 때부터 수학 영재였어요.\n어휘 ▶ exceptional talent 뛰어난 재능 ≒ prodigy · from a young age = from early childhood","❶","a math prodigy from early childhood"],
 ["As a child, Katherine counted things around her, such as steps and dishes.",True,"정답 ▶ T\n이유: 계단, 접시, 숟가락, 포크까지 모든 것을 셌다고 회상했어요.","❶","I counted everything"],
 ["Katherine was not looking forward to studying algebra in high school.",False,"정답 ▶ F\n이유: 대수학과 기하학을 배우러 빨리 고등학교에 가고 싶었어요.\n어휘 ▶ look forward to ~을 고대하다 ≒ can't wait to","❶","I couldn't wait to get to high school to take algebra and geometry"],
 ["Black students in Katherine's hometown were not allowed to attend high school.",True,"정답 ▶ T\n이유: 흑인 학생들은 고등학교에 들어갈 수 없었어요.\n어휘 ▶ attend 다니다 ≒ enter","❷","black students could not enter high school"],
 ["Katherine's family moved so that she could go to high school.",True,"정답 ▶ T\n이유: 아버지가 가족을 데리고 200킬로미터 떨어진 곳으로 이사했어요.","❷","so that she could enter high school"],
 ["Katherine entered college at the age of eighteen.",False,"정답 ▶ F\n이유: 15세에 대학에 입학했어요. 18세는 대학을 '졸업'한 나이예요.","❷","at the age of fifteen"],
 ["Katherine's mentor refused to give her extra lessons.",False,"정답 ▶ F\n이유: 멘토는 그녀만을 위한 특별 수업을 기꺼이 해 줬어요.\n어휘 ▶ refuse 거절하다 ↔ gladly offered","❷","Her mentor gladly offered special classes just for her"],
 ["Katherine's mentor promised to find her a job.",False,"정답 ▶ F\n이유: 일자리는 '네 문제가 될 것'이라고 했어요.\n어휘 ▶ promise 약속하다","❷","will be your problem"],
 ["When Katherine graduated, teaching was the only job she could get.",True,"정답 ▶ T\n이유: 당시 그녀가 할 수 있는 유일한 선택은 가르치는 일이었어요.\n어휘 ▶ the only job she could get = the only option available to her","❷","teaching was the only option available to her"]]
MC=[
 dict(n="❷",box=["❷"],q="본문 ❷의 내용과 <u>일치하는</u> 것은?",opts=[
  "Katherine finished college with the highest academic distinction.",
  "Black and white students attended the same schools in Katherine's hometown.",
  "Katherine had taken only a few math courses by her junior year.",
  "Katherine's mentor was delighted to talk about her job prospects.",
  "Katherine started working as a teacher at a private school for white students."],
  ex="정답 ▶ Katherine finished college with the highest academic distinction.\n이유: Katherine graduated from college with highest honors\n오답 ▶ ② segregated(분리된) 교육 제도 ③ all the math courses(모든 수학 과정) ④ was not happy(기쁘지 않았음) ⑤ a black public school(흑인 공립 학교)\n포인트 ▶ academic distinction 우등 = honors · job prospects 취업 전망 = career opportunities · delighted ↔ not happy",
  per=[["캐서린은 최우등으로 대학을 마쳤다.","graduated from college with highest honors","distinction = honors ✔"],
       ["캐서린의 고향에서는 흑인과 백인 학생이 같은 학교에 다녔다.","had a segregated education system","segregated 분리된 ✗"],
       ["캐서린은 3학년까지 수학 과목을 몇 개만 들었다.","she had taken all the math courses the college could offer","only a few ✗ → all"],
       ["멘토는 그녀의 취업 전망에 대해 기쁘게 이야기했다.","he was not happy when he had to tell","delighted ↔ not happy"],
       ["캐서린은 백인 사립학교에서 교사로 일하기 시작했다.","a teacher at a black public school","private ✗ public · white ✗ black"]]),
 dict(n="❷",box=["❷"],q="본문 ❷의 내용과 일치하지 <u>않는</u> 것은?",opts=[
  "Katherine's mentor assured her that she would easily find a research job.",
  "Katherine's father relocated the family for the sake of her education.",
  "By her third year, Katherine had completed every math course her college offered.",
  "Her mentor believed she had what it takes to be a research mathematician.",
  "Despite an uncertain future, Katherine believed in her own strength."],
  ex="정답 ▶ Katherine's mentor assured her that she would easily find a research job.\n이유: \"That,\" he replied, \"will be your problem.\" 일자리는 네가 해결할 문제라고 했어요.\n오답 ▶ 나머지는 모두 본문을 다른 어휘로 바꿔 쓴 일치 문장\n포인트 ▶ assure 장담하다 · relocate 이전하다 = move · for the sake of ~을 위해 · third year = junior year · complete = take · what it takes 필요한 자질 · uncertain = unclear",
  per=[["멘토는 그녀가 연구직을 쉽게 찾을 거라고 장담했다.","will be your problem","assure ✗ → 네 문제"],
       ["캐서린의 아버지는 그녀의 교육을 위해 가족을 이주시켰다.","her father moved the family 200 kilometers away","relocate = move"],
       ["3학년까지 캐서린은 대학이 제공하는 모든 수학 과정을 마쳤다.","she had taken all the math courses the college could offer","third year = junior year · complete ≒ take"],
       ["멘토는 그녀에게 연구 수학자가 될 자질이 있다고 믿었다.","You would make a good research mathematician","what it takes = 필요한 자질"],
       ["불확실한 미래에도 캐서린은 자신의 힘을 믿었다.","Katherine knew she had the strength to make her own way","uncertain = unclear"]]),
 dict(n="❷",box=["❶","❷"],q="본문 ❶❷의 내용과 <u>일치하는</u> 것은?",opts=[
  "캐서린은 대수학과 기하학을 배우러 고등학교에 가기를 몹시 기다렸다.",
  "캐서린은 1918년 한 백인 가정의 맏이로 태어났다.",
  "캐서린의 가족은 20킬로미터 떨어진 곳으로 이사했다.",
  "캐서린은 17세에 대학을 졸업했다.",
  "캐서린은 대학 졸업 후 바로 연구 수학자가 되었다."],
  ex="정답 ▶ 캐서린은 대수학과 기하학을 배우러 고등학교에 가기를 몹시 기다렸다.\n이유: I couldn't wait to get to high school to take algebra and geometry.\n오답 ▶ ② a black family의 막내(the youngest) ③ 200 kilometers ④ 18세(at the age of eighteen) ⑤ 흑인 공립 학교 교사로 시작\n포인트 ▶ 숫자·나이(1918, 200km, 15세 입학, 18세 졸업) 정확히!",
  per=[["","to take algebra and geometry","일치 ✔"],
       ["","the youngest of four children in a black family","흑인 가정의 막내"],
       ["","200 kilometers away","200킬로미터"],
       ["","at the age of eighteen, Katherine graduated from college","18세 졸업"],
       ["","began her career as a teacher","교사로 시작"]])]
PICK2=[
 {"s":"Katherine Johnson was born on August 26, 1918, in West Virginia, in the U.S., and {was|were} the youngest of four children in a black family.","ex":"정답 ▶ was\n이유: 주어 Katherine Johnson(단수). was born ~ and was ~ 병렬"},
 {"s":"{Reflecting|Reflected} on her youth, Katherine once said, \"I counted everything — the steps to the road, the steps up to church, the number of dishes, spoons, and forks I washed.\"","ex":"정답 ▶ Reflecting\n이유: 분사구문. 주어 Katherine이 '회상하는' 능동 → 현재분사\n포인트 ▶ = As she reflected on her youth"},
 {"s":"She excitedly added, \"I couldn't wait to get to high school {to take|taking} algebra and geometry.\"","ex":"정답 ▶ to take\n이유: '대수학과 기하학을 배우기 위해' → 목적의 to부정사"},
 {"s":"So her father moved the family 200 kilometers away {so that|such that} she could enter high school.","ex":"정답 ▶ so that\n이유: so that + 주어 + can/could ~ = ~할 수 있도록 (목적)"},
 {"s":"After {graduating|graduated} from high school in 1932, she was admitted to a black college at the age of fifteen.","ex":"정답 ▶ graduating\n이유: 여기서 After는 전치사 → 동명사\n포인트 ▶ = After she graduated from ~"},
 {"s":"After graduating from high school in 1932, she {was admitted|admitted} to a black college at the age of fifteen.","ex":"정답 ▶ was admitted\n이유: 그녀가 대학에 '입학 허가를 받은' 수동 → be admitted to"},
 {"s":"By her junior year, she {had taken|has taken} all the math courses the college could offer.","ex":"정답 ▶ had taken\n이유: By her junior year(과거의 한 시점)까지 이미 완료 → 과거완료 had p.p."},
 {"s":"\"You would make a good research mathematician,\" he told his {seventeen-year-old|seventeen-years-old} student, \"and I'm going to prepare you for this career.\"","ex":"정답 ▶ seventeen-year-old\n이유: 하이픈으로 연결해 명사 앞에서 꾸미는 복합형용사 → 단위명사는 단수(year)"},
 {"s":"Katherine asked, \"Where {will I find|I will find} a job?\"","ex":"정답 ▶ will I find\n이유: 따옴표 안은 직접의문문 → 의문사 + 조동사 + 주어 + 동사\n포인트 ▶ 간접의문문이면 Katherine asked where she would find a job."},
 {"s":"The path ahead was unclear and full of obstacles, but Katherine knew she had the strength {to make|making} her own way.","ex":"정답 ▶ to make\n이유: the strength를 꾸미는 to부정사(형용사적 용법) = 길을 헤쳐 나갈 힘"},
 {"s":"At that time, teaching was the only option {available|availably} to her.","ex":"정답 ▶ available\n이유: 명사 option을 뒤에서 꾸미는 형용사 (= the only option that was available to her)"}]
VERB=[
 {"s":"Katherine Johnson was ___ on August 26, 1918, in West Virginia, in the U.S., and was the youngest of four children in a black family.","v":"bear","a":["born"],"ex":"정답 ▶ born\n이유: be born 태어나다 (bear - bore - born)"},
 {"s":"___ on her youth, Katherine once said, \"I counted everything — the steps to the road, the steps up to church, the number of dishes, spoons, and forks I washed.\"","v":"reflect","a":["Reflecting","reflecting"],"ex":"정답 ▶ Reflecting\n이유: 분사구문, 주어가 '회상하는' 능동 → 현재분사"},
 {"s":"So her father ___ the family 200 kilometers away so that she could enter high school.","v":"move","a":["moved"],"ex":"정답 ▶ moved\n이유: 과거의 일 → 과거형"},
 {"s":"After ___ from high school in 1932, she was admitted to a black college at the age of fifteen.","v":"graduate","a":["graduating"],"ex":"정답 ▶ graduating\n이유: 전치사 After + 동명사"},
 {"s":"After graduating from high school in 1932, she was ___ to a black college at the age of fifteen.","v":"admit","a":["admitted"],"ex":"정답 ▶ admitted\n이유: be admitted to ~에 입학 허가를 받다 (t를 겹쳐 admitted)"},
 {"s":"By her junior year, she had ___ all the math courses the college could offer.","v":"take","a":["taken"],"ex":"정답 ▶ taken\n이유: had + p.p. 과거완료 (take - took - taken)"},
 {"s":"Her mentor gladly ___ special classes just for her, but he was not happy when he had to tell his outstanding student about her career opportunities.","v":"offer","a":["offered"],"ex":"정답 ▶ offered\n이유: 과거의 일 → 과거형"},
 {"s":"In 1935, at the age of eighteen, Katherine graduated from college with highest honors and ___ her career as a teacher at a black public school.","v":"begin","a":["began"],"ex":"정답 ▶ began\n이유: graduated와 and로 병렬 → 과거형 (begin - began - begun)"}]
ERR=[
 {"s":"[[Reflected]] on her youth, Katherine once said, \"I [[counted]] everything — the steps to the road, the steps up to church, the number of dishes, spoons, and forks I [[washed]].\"","w":0,"fix":"Reflecting","ex":"틀린 곳 ▶ ① Reflected → Reflecting\n이유: 주어 Katherine이 '회상하는' 능동 → 현재분사\n나머지 ▶ ② ③ 과거의 일 ✔"},
 {"s":"But Katherine's hometown had a [[segregating]] education system, and black students [[could not]] enter high school. So her father moved the family 200 kilometers away [[so that]] she could enter high school.","w":0,"fix":"segregated","ex":"틀린 곳 ▶ ① segregating → segregated\n이유: 교육 제도가 '분리된' 상태(수동) → 과거분사형 형용사\n나머지 ▶ ② ③ ✔"},
 {"s":"After [[graduated]] from high school in 1932, she [[was admitted]] to a black college [[at the age of]] fifteen.","w":0,"fix":"graduating","ex":"틀린 곳 ▶ ① graduated → graduating\n이유: 전치사 After + 동명사\n나머지 ▶ ② 입학 허가를 받은 수동 ✔ ③ ~의 나이에 ✔"},
 {"s":"By her junior year, she [[has taken]] all the math courses the college [[could]] offer. Her mentor [[gladly]] offered special classes just for her.","w":0,"fix":"had taken","ex":"틀린 곳 ▶ ① has taken → had taken\n이유: 과거의 한 시점(By her junior year)까지 완료 → 과거완료\n나머지 ▶ ② 과거 문맥의 could ✔ ③ 동사 수식 부사 ✔"},
 {"s":"\"You would make a good research mathematician,\" he told his [[seventeen-years-old]] student, \"and I'm going [[to prepare]] you [[for]] this career.\"","w":0,"fix":"seventeen-year-old","ex":"틀린 곳 ▶ ① seventeen-years-old → seventeen-year-old\n이유: 하이픈 복합형용사 안의 단위명사는 단수\n나머지 ▶ ② be going to ✔ ③ prepare A for B ✔"},
 {"s":"Katherine asked, \"Where [[I will find]] a job?\" \"That,\" he [[replied]], \"[[will be]] your problem.\"","w":0,"fix":"will I find","ex":"틀린 곳 ▶ ① I will find → will I find\n이유: 직접의문문 어순 = 의문사 + 조동사 + 주어\n나머지 ▶ ② ③ ✔"},
 {"s":"The path ahead was unclear and full of obstacles, but Katherine knew she had the strength [[making]] her own way. In 1935, at the age of eighteen, Katherine [[graduated]] from college with highest honors and [[began]] her career as a teacher at a black public school.","w":0,"fix":"to make","ex":"틀린 곳 ▶ ① making → to make\n이유: 명사 the strength를 꾸미는 to부정사\n나머지 ▶ ② ③ 과거형 병렬 ✔"}]
SCR=["A2","A4","B2","B3","B4","B9","B11"]
ORDER=[
 (["A1","A2","A3","A4"],["1918년 흑인 가정의 막내로 태어남","어릴 때부터 수학 영재","어린 시절 모든 것을 셌다고 회상","고등학교에서 대수학·기하학을 빨리 배우고 싶었음"]),
 (["B1","B2","B3","B4"],["그러나 고향은 흑인이 고등학교에 못 가는 차별적 제도","그래서(So) 아버지가 200km 떨어진 곳으로 이사","고등학교 졸업 후 15세에 흑인 대학 입학","3학년 때 모든 수학 과정을 다 들음"]),
 (["B6","B7","B8","B9"],["멘토: 훌륭한 연구 수학자가 될 거야","캐서린: 어디서 일자리를 찾죠?","멘토: 그건 네 문제가 될 거야","앞길은 불확실했지만 스스로 헤쳐 나갈 힘이 있음"])]
INSERT=[
 (["B1","B2","B3","B4"],1,["흑인 학생은 고등학교에 못 감","그래서(So) 아버지가 이사함","고등학교 졸업 후 대학 입학","3학년 때 모든 과정 수강"],"정답 ▶ ①\n이유: So(그래서)는 '고등학교에 갈 수 없었다'는 문제의 결과예요. 이사한 뒤에야 고등학교를 졸업했다는 내용이 이어질 수 있어요."),
 (["B4","B5","B6","B7"],2,["모든 수학 과정 수강","멘토가 특별 수업, 하지만 직업 기회 이야기는 기쁘지 않음","멘토: 훌륭한 연구 수학자가 될 거야(he told)","캐서린: 어디서 일자리를?"],"정답 ▶ ②\n이유: 주어진 문장의 he는 멘토, this career는 '연구 수학자'예요. 멘토가 직업 이야기를 꺼낸 뒤, 캐서린이 '어디서 일자리를 찾죠?'라고 묻는 흐름이에요."),
 (["B8","B9","B10","B11"],3,["그건 네 문제가 될 거야","앞길은 불확실했지만 힘이 있었음","1935년 최우등 졸업, 흑인 공립 학교 교사로 시작","그 당시(At that time) 가르치는 일이 유일한 선택"],"정답 ▶ ③\n이유: At that time(그 당시)은 1935년 교사가 된 때를 가리켜요. 교사로 시작했다는 문장 바로 뒤, 단락의 마지막이에요.")]
ODD=[
 (["A1","A2","Her older brothers and sisters also became famous mathematicians.","A3"],2,"정답 ▶ ③\n이유: 단락은 캐서린 '자신'의 어린 시절 수학 재능을 이야기해요. 형제자매 이야기는 흐름과 관계없어요."),
 (["B9","B10","Many students at her college chose to study history instead of math.","B11"],2,"정답 ▶ ③\n이유: 캐서린이 졸업 후 교사가 된 과정과 당시 선택지가 없었다는 흐름이에요. 다른 학생들의 전공 선택은 관계없어요.")]
BLANK=[
 {"s":"Katherine was a math ____ from early childhood.","opts":["prodigy","teacher","critic","beginner"],"ex":"정답 ▶ prodigy (영재)\n이유: 모든 것을 세고, 고등학교 수학을 빨리 배우고 싶어 한 아이\n오답 ▶ teacher 교사 · critic 비평가 · beginner 초보자"},
 {"s":"So her father moved the family 200 kilometers away so that she could ____ high school.","opts":["enter","avoid","build","close"],"ex":"정답 ▶ enter (입학하다)\n이유: 고향에서는 흑인 학생이 고등학교에 '들어갈' 수 없어서 이사했어요.\n오답 ▶ avoid 피하다 · build 짓다 · close 닫다"},
 {"s":"By her junior year, she had taken ____ the math courses the college could offer.","opts":["all","none of","few of","half of"],"ex":"정답 ▶ all (모든)\n이유: 다음 문장에서 멘토가 '그녀만을 위한' 특별 수업을 해 줘요 → 들을 수업을 이미 '다' 들었기 때문\n오답 ▶ none of 하나도 ~ 않는 · few of 거의 없는 · half of 절반의"},
 {"s":"The path ahead was unclear and full of ____, but Katherine knew she had the strength to make her own way.","opts":["obstacles","rewards","friends","choices"],"ex":"정답 ▶ obstacles (장애물)\n이유: unclear(불확실한)와 나란히, but 뒤 '헤쳐 나갈 힘'과 대조 → 어려움\n오답 ▶ rewards 보상 · friends 친구 · choices 선택지"},
 {"s":"At that time, teaching was the ____ option available to her.","opts":["only","best","easiest","newest"],"ex":"정답 ▶ only (유일한)\n이유: 멘토가 '일자리는 네 문제'라고 했을 만큼, 당시 흑인 여성에게는 교사 말고 길이 없었어요.\n오답 ▶ best 최고의 · easiest 가장 쉬운 · newest 가장 새로운"}]
GRAM=[
 {"q":"빈칸에 알맞은 것은?<br><b>______ on her youth, Katherine once said, \"I counted everything.\"</b>","opts":["Reflecting","Reflected","Reflect","To reflecting"],"ex":"정답 ▶ Reflecting\n이유: 분사구문, 주어 Katherine이 '회상하는' 능동 → 현재분사\n본문 ▶ Reflecting on her youth, Katherine once said"},
 {"q":"빈칸에 알맞은 것은?<br><b>I couldn't wait ______ high school.</b>","opts":["to start","starting","start","started"],"ex":"정답 ▶ to start\n이유: can't[couldn't] wait to + 동사원형 = 빨리 ~하고 싶다\n본문 ▶ I couldn't wait to get to high school"},
 {"q":"빈칸에 알맞은 것은?<br><b>He moved away ______ his daughter could go to school.</b>","opts":["so that","such that","in order to","because of"],"ex":"정답 ▶ so that (~할 수 있도록)\n이유: 뒤에 주어 + 동사(his daughter could go) → so that\n오답 ▶ in order to + 동사원형 · because of + 명사"},
 {"q":"빈칸에 알맞은 것은?<br><b>By the time she was seventeen, she ______ all the courses.</b>","opts":["had taken","has taken","takes","was taking"],"ex":"정답 ▶ had taken\n이유: 과거 시점(By the time she was seventeen)까지 완료 → 과거완료\n본문 ▶ By her junior year, she had taken all the math courses"},
 {"q":"다음 중 어법상 알맞은 것은?","opts":["He has a seven-year-old son.","He has a seven-years-old son.","He has a seven-year-olds son.","He has a seven-years-olds son."],"ex":"정답 ▶ He has a seven-year-old son.\n이유: 하이픈 복합형용사(숫자-단위명사-형용사)에서 단위명사는 단수\n본문 ▶ his seventeen-year-old student"},
 {"q":"빈칸에 알맞은 것은?<br><b>She took all the courses ______ the college could offer.</b>","opts":["that","what","who","whose"],"ex":"정답 ▶ that\n이유: 선행사 all the courses + offer의 목적어가 빠진 절 → 목적격 관계대명사 that (생략 가능)\n포인트 ▶ 선행사에 all이 있으면 주로 that\n본문 ▶ all the math courses (that) the college could offer"},
 {"q":"밑줄 친 <b>make</b>의 뜻으로 알맞은 것은?<br><b>You would <u>make</u> a good research mathematician.</b>","opts":["(자질이 있어) ~이 되다","~을 만들다","~하게 하다","(돈을) 벌다"],"ex":"정답 ▶ (자질이 있어) ~이 되다\n이유: make + 명사(보어) = ~이 될 자질이 있다. You would make a good teacher. (너는 좋은 선생님이 될 거야)"},
 {"q":"빈칸에 알맞은 것은?<br><b>Katherine asked, \"Where ______ a job?\"</b>","opts":["will I find","I will find","I find will","will find I"],"ex":"정답 ▶ will I find\n이유: 직접의문문 = 의문사 + 조동사 + 주어 + 동사원형"},
 {"q":"빈칸에 알맞은 것은?<br><b>Teaching was the only option ______ to her.</b>","opts":["available","availability","availably","avail"],"ex":"정답 ▶ available\n이유: 형용사구(available to her)가 명사 option을 뒤에서 꾸밈"}]
