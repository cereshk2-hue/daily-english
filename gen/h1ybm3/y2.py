N="❸"
VOCAB=[[w,m,N]+x for w,m,*x in [
 ["it was not until A that B","A가 되어서야 비로소 B하다","It was not until 1953 that"],["field center","현장 연구소"],["complex","복잡한"],["calculation","계산"],["manually","손으로, 수동으로"],
 ["support","~을 지원하다"],["contribute to","~에 기여하다"],["endure","~을 견디다, 참다"],["discrimination","차별"],["segregation","(인종) 분리, 차별"],
 ["be referred to","~로 불리다, 언급되다"],["term","용어, 말"],["despite","~에도 불구하고"],["professional","전문직의, 전문적인"],["reassign","~을 재배치하다"],
 ["elite","엘리트의, 정예의"],["division","부서"],["enormous","엄청난, 막대한"],["contribution","공헌, 기여"],["permission","허락, 허가"],
 ["attend","~에 참석하다"],["colleague","동료"],["embarrassed","당황한"],["have no choice but to","~할 수밖에 없다","had no choice but to"],
 ["let ~ in","~을 들여보내다"],["discriminatory","차별적인"],["custom","관습"],["face","~에 직면하다"],["barrier","장벽"],["overcome","~을 극복하다"],
 ["pay off","결실을 맺다, 성공하다","paid off"],["courage","용기"],["research paper","연구 논문"],["spacecraft","우주선"],["orbit","궤도"],
 ["receive credit","인정받다, 공로를 인정받다"],["author","저자"]]]
PICK1=[
 {"s":"There, she worked as one of the \"Black computers\" who did complex calculations {manually|automatically} to support white male engineers.","ex":"정답 ▶ manually (손으로, 수동으로)\n오답 ▶ automatically (자동으로)\n이유: '흑인 컴퓨터'는 기계가 아니라 계산을 '손으로' 하던 사람들이에요. ❹의 by hand와 같은 뜻"},
 {"s":"Though they greatly contributed to the space project, they {endured|enjoyed} a lot of discrimination, including segregation in the office and being referred to with terms like \"girl\" despite being professional women.","ex":"정답 ▶ endured (견뎠다)\n오답 ▶ enjoyed (즐겼다)\n이유: Though(~했지만)로 '크게 기여했다'와 대조 → 차별을 '견뎌야' 했어요."},
 {"s":"Though they greatly contributed to the space project, they endured a lot of discrimination, including {segregation|integration} in the office and being referred to with terms like \"girl\" despite being professional women.","ex":"정답 ▶ segregation (분리, 차별)\n오답 ▶ integration (통합)\n이유: 차별(discrimination)의 예 → 사무실 안에서도 인종에 따라 '분리'"},
 {"s":"Two weeks into the job, Katherine was {reassigned|resigned} to NASA's elite space research division.","ex":"정답 ▶ reassigned (재배치된)\n오답 ▶ resigned (사직한)\n이유: 다음 문장 There(그 부서에서) 유일한 흑인 여성이었다 → 그 부서로 '옮겨졌어요'."},
 {"s":"Despite her {enormous|minor} contributions, the important research meetings were held only among white staff members.","ex":"정답 ▶ enormous (엄청난)\n오답 ▶ minor (사소한)\n이유: Despite(~에도 불구하고)로 '회의에서 빠졌다'와 대조 → 공헌이 '엄청났는데도'"},
 {"s":"When she asked for {permission|admission} to attend the meetings, her male colleagues said that \"the girls\" didn't usually go.","ex":"정답 ▶ permission (허락)\n오답 ▶ admission (입학, 입장)\n포인트 ▶ ask for permission to do ~할 허락을 구하다"},
 {"s":"The {embarrassed|encouraged} male workers had no choice but to let her in.","ex":"정답 ▶ embarrassed (당황한)\n오답 ▶ encouraged (격려받은)\n이유: '갈 수 없다는 법이 있나요?'라는 질문에 할 말이 없어진 남자 직원들"},
 {"s":"By asking questions no one had ever asked, Katherine ended a {discriminatory|democratic} custom.","ex":"정답 ▶ discriminatory (차별적인)\n오답 ▶ democratic (민주적인)\n이유: 흑인 여성을 회의에서 빼던 관습 → 차별적인 관습"},
 {"s":"She had faced barriers, but her efforts to {overcome|overlook} them paid off.","ex":"정답 ▶ overcome (극복하다)\n오답 ▶ overlook (간과하다, 못 본 척하다)\n이유: 장벽(barriers)은 '극복'하는 것. 그 노력이 결실을 맺었어요(paid off)."},
 {"s":"She felt proud and continued her work with {courage|fear}.","ex":"정답 ▶ courage (용기)\n오답 ▶ fear (두려움)\n이유: 차별을 끝내고 자부심을 느낀 뒤 → 용기 있게 일을 이어 감"},
 {"s":"That was the first time a woman in her division received {credit|blame} as an author of a research report.","ex":"정답 ▶ credit (인정, 공로)\n오답 ▶ blame (비난)\n포인트 ▶ receive credit as ~로 인정받다"}]
TF=[[a,b,c,N,d] for a,b,c,d in [
 ["Katherine got a job at NASA right after college.",False,"정답 ▶ F\n이유: 1953년이 되어서야 NASA에서 일자리를 찾았어요. 대학 졸업은 1935년이에요.\n어휘 ▶ It was not until A that B A가 되어서야 B하다","It was not until 1953 that Katherine found a job"],
 ["The \"Black computers\" performed complicated calculations by hand.",True,"정답 ▶ T\n이유: 복잡한 계산을 손으로 했어요.\n어휘 ▶ complicated = complex · by hand = manually","did complex calculations manually"],
 ["Although they were professionals, the women were sometimes called \"girls.\"",True,"정답 ▶ T\n이유: 전문직 여성인데도 '여자애'라는 말로 불렸어요.\n어휘 ▶ be called = be referred to with terms like","being referred to with terms like"],
 ["Katherine stayed in her first position at NASA for many years.",False,"정답 ▶ F\n이유: 일을 시작한 지 2주 만에 엘리트 우주 연구 부서로 재배치됐어요.\n어휘 ▶ position 직위, 자리","Two weeks into the job, Katherine was reassigned"],
 ["Katherine was one of many black women in the elite research division.",False,"정답 ▶ F\n이유: 그 부서에서 유일한(the only) 흑인 여성 직원이었어요.","she was the only black female member of the staff"],
 ["At first, only white staff members attended the important research meetings.",True,"정답 ▶ T\n이유: 중요한 연구 회의는 백인 직원들끼리만 열렸어요.","the important research meetings were held only among white staff members"],
 ["Katherine's male colleagues invited her to the meetings right away.",False,"정답 ▶ F\n이유: 허락을 구하자 '여자들은 보통 안 간다'고 말했어요.\n어휘 ▶ invite 초대하다 · right away 즉시","her male colleagues said that"],
 ["Katherine's question left the men no option but to let her into the meetings.",True,"정답 ▶ T\n이유: 당황한 남자 직원들은 그녀를 들여보낼 수밖에 없었어요.\n어휘 ▶ leave A no option but to ~ A가 ~할 수밖에 없게 하다 = have no choice but to","had no choice but to let her in"],
 ["Katherine gave up her work because of the barriers she faced.",False,"정답 ▶ F\n이유: 자부심을 느끼며 용기 있게 일을 계속했어요.\n어휘 ▶ give up 포기하다 ↔ continue","continued her work with courage"],
 ["Katherine was the first woman in her division to be credited as an author of a research report.",True,"정답 ▶ T\n이유: 부서에서 여성이 연구 보고서 저자로 인정받은 건 처음이었어요.\n어휘 ▶ be credited as = receive credit as","the first time a woman in her division received credit as an author"]]]
MC=[
 dict(n=N,box=[N],q="본문 ❸의 내용과 <u>일치하는</u> 것은?",opts=[
  "Katherine co-wrote a paper on how to put a spacecraft into orbit.",
  "Katherine was hired by NASA in the 1930s.",
  "The Black computers were treated as equals by white engineers.",
  "Katherine attended the important meetings from her very first day.",
  "Katherine's question angered her colleagues, so they kept her out."],
  ex="정답 ▶ Katherine co-wrote a paper on how to put a spacecraft into orbit.\n이유: she wrote a research paper with another engineer about how to place a spacecraft into orbit\n오답 ▶ ② 1953년 ③ endured a lot of discrimination ④ 허락을 구해야 했음 ⑤ had no choice but to let her in(들여보낼 수밖에 없었음)\n포인트 ▶ co-write 공동 집필하다 = write with another · put = place · keep ~ out 들이지 않다",
  per=[["캐서린은 우주선을 궤도에 올리는 방법에 관한 논문을 공동 집필했다.","with another engineer about how to place a spacecraft into orbit","co-write = write with another ✔"],
       ["캐서린은 1930년대에 NASA에 고용되었다.","It was not until 1953","1930년대 ✗ → 1953년"],
       ["흑인 컴퓨터들은 백인 엔지니어와 동등하게 대우받았다.","they endured a lot of discrimination","equals ✗ → 차별"],
       ["캐서린은 첫날부터 중요한 회의에 참석했다.","When she asked for permission to attend the meetings","허락을 구해야 했음"],
       ["캐서린의 질문에 동료들이 화가 나서 그녀를 들이지 않았다.","had no choice but to let her in","kept her out ✗ → let her in"]]),
 dict(n=N,box=[N],q="본문 ❸의 내용과 일치하지 <u>않는</u> 것은?",opts=[
  "Katherine accepted without question the custom of keeping women out of meetings.",
  "The Black computers made a significant contribution to the space project.",
  "Soon after starting, Katherine was transferred to an elite research team.",
  "Katherine's efforts to overcome barriers eventually proved worthwhile.",
  "Katherine went on working bravely and with pride."],
  ex="정답 ▶ Katherine accepted without question the custom of keeping women out of meetings.\n이유: By asking questions no one had ever asked, Katherine ended a discriminatory custom. 질문을 던져 그 관습을 끝냈어요.\n오답 ▶ 나머지는 모두 본문을 다른 어휘로 바꿔 쓴 일치 문장\n포인트 ▶ significant = great(ly) · transfer 전근시키다 = reassign · prove worthwhile 보람 있다 ≒ pay off · go on -ing = continue · bravely = with courage",
  per=[["캐서린은 여성을 회의에서 빼는 관습을 의문 없이 받아들였다.","Katherine ended a discriminatory custom","accept ✗ → ended"],
       ["흑인 컴퓨터들은 우주 프로젝트에 크게 기여했다.","they greatly contributed to the space project","significant contribution = greatly contributed"],
       ["일을 시작하자마자 캐서린은 엘리트 연구팀으로 옮겨졌다.","Two weeks into the job, Katherine was reassigned","transfer = reassign · soon after starting = two weeks into the job"],
       ["장벽을 극복하려는 캐서린의 노력은 결국 보람이 있었다.","her efforts to overcome them paid off","prove worthwhile ≒ pay off"],
       ["캐서린은 용감하게, 자부심을 갖고 일을 계속했다.","She felt proud and continued her work with courage","bravely = with courage · go on = continue"]]),
 dict(n=N,box=[N],q="본문 ❸의 내용과 <u>일치하는</u> 것은?",opts=[
  "캐서린은 아무도 하지 않았던 질문을 해서 차별적인 관습을 끝냈다.",
  "캐서린은 대학을 졸업하자마자 NASA에 들어갔다.",
  "'흑인 컴퓨터'는 계산을 하는 전자 기계를 가리킨다.",
  "엘리트 연구 부서에는 흑인 여성 직원이 여러 명 있었다.",
  "캐서린은 1960년에 혼자서 연구 논문을 썼다."],
  ex="정답 ▶ 캐서린은 아무도 하지 않았던 질문을 해서 차별적인 관습을 끝냈다.\n이유: By asking questions no one had ever asked, Katherine ended a discriminatory custom.\n오답 ▶ ② 1953년이 되어서야 ③ 손으로 계산하던 '사람들' ④ the only black female member(유일한 흑인 여성) ⑤ with another engineer(다른 엔지니어와 함께)\n포인트 ▶ It was not until ~ that … ~이 되어서야 …했다",
  per=[["","Katherine ended a discriminatory custom","일치 ✔"],
       ["","It was not until 1953","1953년이 되어서야"],
       ["","did complex calculations manually","손으로 계산한 사람들"],
       ["","the only black female member of the staff","유일한 흑인 여성"],
       ["","with another engineer","공동 집필"]])]
PICK2=[
 {"s":"It was not until 1953 {that|which} Katherine found a job at a NASA field center in Virginia.","ex":"정답 ▶ that\n이유: It was not until A that B = A가 되어서야 비로소 B했다 (강조 구문)"},
 {"s":"There, she worked as one of the \"Black computers\" {who|which} did complex calculations manually to support white male engineers.","ex":"정답 ▶ who\n이유: '흑인 컴퓨터'는 계산하던 '사람들' → 사람 선행사 + 주격 → who"},
 {"s":"{Though|Despite} they greatly contributed to the space project, they endured a lot of discrimination, including segregation in the office and being referred to with terms like \"girl\" despite being professional women.","ex":"정답 ▶ Though\n이유: 뒤에 주어+동사(they greatly contributed) → 접속사 Though. Despite는 전치사"},
 {"s":"Though they greatly contributed to the space project, they endured a lot of discrimination, including segregation in the office and {being referred|referring} to with terms like \"girl\" despite being professional women.","ex":"정답 ▶ being referred\n이유: 그들이 '불리는' 수동 + 전치사 including 뒤 동명사 → being p.p.\n포인트 ▶ refer to A with B → A is referred to with B"},
 {"s":"Though they greatly contributed to the space project, they endured a lot of discrimination, including segregation in the office and being referred to with terms like \"girl\" despite {being|they were} professional women.","ex":"정답 ▶ being\n이유: despite는 전치사 → 동명사 (절 X)"},
 {"s":"Two weeks into the job, Katherine {was reassigned|reassigned} to NASA's elite space research division.","ex":"정답 ▶ was reassigned\n이유: 캐서린이 '재배치된' 수동 (reassign A to B → A is reassigned to B)"},
 {"s":"{Despite|Although} her enormous contributions, the important research meetings were held only among white staff members.","ex":"정답 ▶ Despite\n이유: 뒤에 명사구(her enormous contributions)만 → 전치사 Despite"},
 {"s":"Despite her enormous contributions, the important research meetings {were held|held} only among white staff members.","ex":"정답 ▶ were held\n이유: 회의가 '열리는' 수동 (hold - held - held)"},
 {"s":"Katherine asked, \"Is there a law that {says|say} I can't go?\"","ex":"정답 ▶ says\n이유: 주격 관계대명사 that의 선행사 a law(단수)"},
 {"s":"The embarrassed male workers had no choice but {to let|letting} her in.","ex":"정답 ▶ to let\n이유: have no choice but to + 동사원형 ~할 수밖에 없다"},
 {"s":"By {asking|asked} questions no one had ever asked, Katherine ended a discriminatory custom.","ex":"정답 ▶ asking\n이유: 전치사 By + 동명사 ~함으로써"},
 {"s":"She felt {proud|proudly} and continued her work with courage.","ex":"정답 ▶ proud\n이유: feel + 형용사(보어) ~하게 느끼다"},
 {"s":"In 1960, she wrote a research paper with another engineer about how {to place|placing} a spacecraft into orbit.","ex":"정답 ▶ to place\n이유: how to + 동사원형 ~하는 방법"}]
VERB=[
 {"s":"There, she worked as one of the \"Black computers\" who did complex calculations manually ___ white male engineers.","v":"support","a":["to support"],"ex":"정답 ▶ to support\n이유: '지원하기 위해' 목적의 to부정사"},
 {"s":"Though they greatly contributed to the space project, they ___ a lot of discrimination, including segregation in the office and being referred to with terms like \"girl\" despite being professional women.","v":"endure","a":["endured"],"ex":"정답 ▶ endured\n이유: 과거의 일, contributed와 같은 시제 → 과거형"},
 {"s":"Two weeks into the job, Katherine was ___ to NASA's elite space research division.","v":"reassign","a":["reassigned"],"ex":"정답 ▶ reassigned\n이유: was + p.p. 수동태"},
 {"s":"Despite her enormous contributions, the important research meetings were ___ only among white staff members.","v":"hold","a":["held"],"ex":"정답 ▶ held\n이유: were + p.p. 수동태 (hold - held - held)"},
 {"s":"When she asked for permission ___ the meetings, her male colleagues said that \"the girls\" didn't usually go.","v":"attend","a":["to attend"],"ex":"정답 ▶ to attend\n이유: permission to do ~할 허락 (명사를 꾸미는 to부정사)"},
 {"s":"The ___ male workers had no choice but to let her in.","v":"embarrass","a":["embarrassed"],"ex":"정답 ▶ embarrassed\n이유: 사람이 '당황한' 감정 → 과거분사형 형용사 (embarrassing은 '당황하게 만드는')"},
 {"s":"By asking questions no one had ever ___, Katherine ended a discriminatory custom.","v":"ask","a":["asked"],"ex":"정답 ▶ asked\n이유: had + p.p. 과거완료 (그때까지 아무도 묻지 않았던)"},
 {"s":"She had ___ barriers, but her efforts to overcome them paid off.","v":"face","a":["faced"],"ex":"정답 ▶ faced\n이유: had + p.p. 과거완료"},
 {"s":"That was the first time a woman in her division ___ credit as an author of a research report.","v":"receive","a":["received"],"ex":"정답 ▶ received\n이유: 과거의 일 → 과거형"}]
ERR=[
 {"s":"It was not until 1953 [[what]] Katherine found a job at a NASA field center in Virginia. There, she worked as one of the \"Black computers\" [[who]] did complex calculations [[manually]] to support white male engineers.","w":0,"fix":"that","ex":"틀린 곳 ▶ ① what → that\n이유: It was not until A that B 구문\n나머지 ▶ ② 사람 선행사 → who ✔ ③ 동사 수식 부사 ✔"},
 {"s":"Though they greatly contributed to the space project, they endured a lot of discrimination, including segregation in the office and [[referring]] to with terms like \"girl\" [[despite]] [[being]] professional women.","w":0,"fix":"being referred","ex":"틀린 곳 ▶ ① referring → being referred\n이유: 그들이 '불리는' 수동 → 동명사 수동 being p.p.\n나머지 ▶ ② 전치사 despite ✔ ③ 전치사 뒤 동명사 ✔"},
 {"s":"Two weeks into the job, Katherine [[reassigned]] to NASA's elite space research division. There, she [[was]] the only black female member [[of]] the staff.","w":0,"fix":"was reassigned","ex":"틀린 곳 ▶ ① reassigned → was reassigned\n이유: 캐서린이 '재배치된' 수동\n나머지 ▶ ② ③ ✔"},
 {"s":"[[Although]] her enormous contributions, the important research meetings [[were held]] only [[among]] white staff members.","w":0,"fix":"Despite","ex":"틀린 곳 ▶ ① Although → Despite\n이유: 뒤에 명사구만 → 전치사\n나머지 ▶ ② 회의가 열리는 수동 ✔ ③ among ~ 사이에서 ✔"},
 {"s":"Katherine asked, \"Is there a law that [[say]] I can't go?\" The [[embarrassed]] male workers had no choice but [[to let]] her in.","w":0,"fix":"says","ex":"틀린 곳 ▶ ① say → says\n이유: 선행사 a law(단수)\n나머지 ▶ ② 당황한(감정) ✔ ③ have no choice but to ✔"},
 {"s":"By [[ask]] questions no one [[had ever asked]], Katherine ended a [[discriminatory]] custom.","w":0,"fix":"asking","ex":"틀린 곳 ▶ ① ask → asking\n이유: 전치사 By + 동명사\n나머지 ▶ ② 과거완료 ✔ ③ 명사 수식 형용사 ✔"},
 {"s":"She had faced barriers, but her efforts [[to overcome]] them paid off. She felt [[proudly]] and continued her work [[with courage]].","w":1,"fix":"proud","ex":"틀린 곳 ▶ ② proudly → proud\n이유: feel + 형용사 보어\n나머지 ▶ ① efforts to do ✔ ③ with courage = courageously ✔"}]
SCR=["C1","C4","C5","C8","C9","C10","C12"]
ORDER=[
 (["C1","C2","C3","C4"],["1953년에야 NASA 필드 센터에 취직","'흑인 컴퓨터'로 손 계산","크게 기여했지만 많은 차별을 견딤","2주 만에 엘리트 우주 연구 부서로"]),
 (["C6","C7","C8","C9"],["공헌에도 중요한 회의는 백인끼리만","허락을 구하자 '여자들은 안 간다'","'갈 수 없다는 법이 있나요?'","당황한 남자 직원들은 들여보낼 수밖에"]),
 (["C11","C12","C13","C14"],["장벽에 맞섰고 노력이 결실을 맺음","자부심과 용기로 일을 계속","1960년 우주선 궤도 논문을 공동 집필","부서에서 여성이 저자로 인정받은 첫 사례"])]
INSERT=[
 (["C3","C4","C5","C6"],2,["많은 차별을 견딤","2주 만에 엘리트 연구 부서로 재배치","그곳에서(There) 유일한 흑인 여성","공헌에도 회의는 백인끼리"],"정답 ▶ ②\n이유: There는 바로 앞의 '엘리트 우주 연구 부서'를 가리켜요."),
 (["C7","C8","C9","C10"],2,["'여자들은 보통 안 간다'","'갈 수 없다는 법이 있나요?'","당황한(embarrassed) 남자 직원들이 들여보냄","질문으로 차별 관습을 끝냄"],"정답 ▶ ②\n이유: 남자 직원들이 '당황한' 이유는 캐서린의 날카로운 질문이에요. 질문 바로 뒤!"),
 (["C11","C12","C13","C14"],3,["노력이 결실을 맺음","용기로 일을 계속","1960년 논문 집필","그것(That)이 여성이 저자로 인정받은 첫 사례"],"정답 ▶ ③\n이유: That은 1960년에 쓴 연구 논문을 가리켜요. 논문 문장 바로 뒤, 단락의 끝이에요.")]
ODD=[
 (["C1","C2","Many engineers at NASA preferred to work alone at night.","C3"],2,"정답 ▶ ③\n이유: 흑인 컴퓨터가 한 일과 그들이 겪은 차별 이야기예요. 엔지니어들의 근무 습관은 관계없어요."),
 (["C12","C13","Today, most spacecraft are controlled by artificial intelligence.","C14"],2,"정답 ▶ ③\n이유: 1960년 논문 → 그것이 여성 최초의 저자 인정이라는 흐름이에요. 오늘날 우주선 조종 방식은 관계없고, 다음 문장 That이 가리킬 대상도 끊어 버려요.")]
BLANK=[
 {"s":"There, she worked as one of the \"Black computers\" who did complex calculations ____ to support white male engineers.","opts":["manually","digitally","carelessly","silently"],"ex":"정답 ▶ manually (손으로)\n이유: 사람이 하던 계산 → 손으로. ❹에서도 calculations by hand가 나와요.\n오답 ▶ digitally 디지털 방식으로 · carelessly 부주의하게 · silently 조용히"},
 {"s":"Though they greatly contributed to the space project, they endured a lot of ____, including segregation in the office.","opts":["discrimination","praise","money","free time"],"ex":"정답 ▶ discrimination (차별)\n이유: Though로 '크게 기여했다'와 대조, including segregation(분리)이 예시\n오답 ▶ praise 칭찬 · money 돈 · free time 여가"},
 {"s":"Despite her enormous ____, the important research meetings were held only among white staff members.","opts":["contributions","mistakes","complaints","absences"],"ex":"정답 ▶ contributions (공헌)\n이유: Despite + 좋은 점 → 그런데도 회의에서 제외. 실수였다면 Despite가 어색해요.\n오답 ▶ mistakes 실수 · complaints 불평 · absences 결석"},
 {"s":"By asking questions no one had ever asked, Katherine ended a ____ custom.","opts":["discriminatory","fair","friendly","modern"],"ex":"정답 ▶ discriminatory (차별적인)\n이유: 여성(흑인 여성)을 회의에서 빼던 관습 → 차별적\n오답 ▶ fair 공정한 · friendly 친근한 · modern 현대적인"},
 {"s":"She had faced barriers, but her efforts to ____ them paid off.","opts":["overcome","create","ignore","accept"],"ex":"정답 ▶ overcome (극복하다)\n이유: 장벽에 맞서 '극복하려는' 노력이 결실을 맺음\n오답 ▶ create 만들다 · ignore 무시하다 · accept 받아들이다"}]
GRAM=[
 {"q":"다음 문장과 뜻이 같은 것은?<br><b>It was not until 1953 that Katherine found a job at NASA.</b>","opts":["Katherine found a job at NASA only in 1953.","Katherine found a job at NASA before 1953.","Katherine lost her job at NASA in 1953.","Katherine never found a job at NASA."],"ex":"정답 ▶ Katherine found a job at NASA only in 1953.\n이유: It was not until A that B = A가 되어서야 비로소 B했다 = Only in A did B ~\n포인트 ▶ 1953년 '전에는' 못 찾았다는 뜻"},
 {"q":"빈칸에 알맞은 것은?<br><b>______ being professional women, they were called \"girls.\"</b>","opts":["Despite","Though","Because","Unless"],"ex":"정답 ▶ Despite\n이유: 뒤에 동명사구(being ~) → 전치사. Though·Because·Unless는 접속사"},
 {"q":"빈칸에 알맞은 것은?<br><b>She didn't like ______ to as a \"girl.\"</b>","opts":["being referred","referring","to refer","referred"],"ex":"정답 ▶ being referred\n이유: 그녀가 '불리는' 수동 + like의 목적어 동명사 → being p.p."},
 {"q":"빈칸에 알맞은 것은?<br><b>They had no choice but ______ her in.</b>","opts":["to let","letting","let","lets"],"ex":"정답 ▶ to let\n이유: have no choice but to + 동사원형 ~할 수밖에 없다"},
 {"q":"빈칸에 알맞은 것은?<br><b>The teacher let us ______ home early.</b>","opts":["go","to go","going","went"],"ex":"정답 ▶ go\n이유: 사역동사 let + 목적어 + 동사원형\n본문 ▶ to let her in (let + 목적어 + 부사)"},
 {"q":"빈칸에 알맞은 것은?<br><b>______ asking questions, she ended a discriminatory custom.</b>","opts":["By","For","To","With"],"ex":"정답 ▶ By\n이유: by + -ing ~함으로써 (수단)"},
 {"q":"빈칸에 알맞은 것은?<br><b>She asked questions that no one ______ before.</b>","opts":["had ever asked","has ever asked","ever asks","was ever asking"],"ex":"정답 ▶ had ever asked\n이유: 그녀가 물은 과거 시점보다 '이전'까지의 경험 → 과거완료"},
 {"q":"빈칸에 알맞은 것은?<br><b>She wrote a paper about ______ to place a spacecraft into orbit.</b>","opts":["how","what","why","that"],"ex":"정답 ▶ how\n이유: how to + 동사원형 ~하는 방법"}]
