VOCAB=[[w,m,n]+x for w,m,n,*x in [
 ["remarkable","놀라운, 주목할 만한","❹"],["by hand","손으로","❹"],["trust","~을 신뢰하다","❹"],["digital","디지털의","❹"],
 ["pioneering","선구적인","❹"],["astronaut","우주 비행사","❹"],["orbit","~의 궤도를 돌다","❹"],["electronic","전자의","❹"],
 ["introduce","~을 도입하다","❹"],["calculate","~을 계산하다","❹"],["trajectory","궤적, 궤도","❹"],["minor","사소한, 작은","❹"],
 ["error","오류","❹"],["be concerned about","~을 걱정하다","❹"],["accuracy","정확성","❹"],["double-check","~을 재확인하다","❹"],
 ["figure","수치, 숫자","❹"],["be good to go","준비가 다 되다","❹"],["slide rule","계산자","❹"],
 ["spend 시간 -ing","~하는 데 시간을 쓰다","❹","spent a day and a half checking"],["make sure of","~을 확인하다, 확실히 하다","❹","made sure of"],
 ["perform","~을 수행하다","❹"],["work on","~에 공을 들이다, 작업하다","❹"],
 ["retire","은퇴하다","❺"],["dedicate A to B","A를 B에 바치다","❺","dedicated the rest of her life to"],["the rest of","~의 나머지","❺"],
 ["champion","~을 옹호하다, 지지하다","❺"],["access","접근(권), 이용 기회","❺"],["STEM","과학·기술·공학·수학 (분야)","❺"],["award","(상을) 수여하다","❺"],
 ["refuse to","~하기를 거부하다","❺"],["be limited by","~에 의해 제한되다","❺"],["expectation","기대","❺"],["gender","성별","❺"],["race","인종","❺"],
 ["expand","~을 확장하다, 넓히다","❺"],["boundary","경계, 한계","❺"],["humanity","인류","❺"],["in one's honor","~을 기리기 위해","❺"],
 ["facility","시설","❺"],["legacy","유산, 업적","❺"]]]
PICK1=[
 {"s":"Katherine's {remarkable|regrettable} calculations by hand were trusted more than digital computers.","ex":"정답 ▶ remarkable (놀라운)\n오답 ▶ regrettable (유감스러운)\n이유: 컴퓨터보다 더 신뢰받은 계산 → 놀라운 계산"},
 {"s":"NASA used an electronic computer, first {introduced|reduced} into the space program a year earlier, to calculate the spaceship's trajectory, but it made many minor errors.","ex":"정답 ▶ introduced (도입된)\n오답 ▶ reduced (줄어든)\n포인트 ▶ introduce A into B A를 B에 도입하다"},
 {"s":"Glenn, who was concerned about its {accuracy|appearance}, asked Katherine Johnson to double-check the machine's figures by hand.","ex":"정답 ▶ accuracy (정확성)\n오답 ▶ appearance (외모, 출현)\n이유: 컴퓨터가 사소한 오류(minor errors)를 많이 냈으니 '정확성'을 걱정했어요."},
 {"s":"Glenn, who was concerned about its accuracy, asked Katherine Johnson to {double-check|ignore} the machine's figures by hand.","ex":"정답 ▶ double-check (재확인하다)\n오답 ▶ ignore (무시하다)\n이유: 정확성이 걱정되니 손으로 '다시 확인'해 달라고 했어요."},
 {"s":"{Eventually|Previously}, Glenn became the first American astronaut to orbit the Earth.","ex":"정답 ▶ Eventually (결국)\n오답 ▶ Previously (이전에)\n이유: 캐서린의 확인 '후에' 비행에 성공 → 결국"},
 {"s":"Katherine {retired|returned} in 1986 after thirty-three years at NASA.","ex":"정답 ▶ retired (은퇴했다)\n오답 ▶ returned (돌아왔다)\n이유: 33년을 일한 '후' → 은퇴. 다음 문장 After that(그 후) 여생을 교육에 바쳐요."},
 {"s":"After that, she dedicated the rest of her life to championing {access|excess} to STEM education for Black girls.","ex":"정답 ▶ access (접근, 이용 기회)\n오답 ▶ excess (초과)\n포인트 ▶ access to ~에 대한 접근(기회)"},
 {"s":"For her contributions, President Barack Obama awarded her the Presidential Medal of Freedom in 2015 and said, \"Katherine G. Johnson refused to be {limited|liberated} by society's expectations of her gender and race while expanding the boundaries of humanity's reach.\"","ex":"정답 ▶ limited (제한된)\n오답 ▶ liberated (해방된)\n이유: refused to be limited = 사회의 기대에 '갇히기를' 거부했다"},
 {"s":"For her contributions, President Barack Obama awarded her the Presidential Medal of Freedom in 2015 and said, \"Katherine G. Johnson refused to be limited by society's expectations of her gender and race while {expanding|shrinking} the boundaries of humanity's reach.\"","ex":"정답 ▶ expanding (넓히는)\n오답 ▶ shrinking (줄이는)\n이유: 우주 비행 계산으로 인류가 갈 수 있는 범위를 '넓혔어요'."},
 {"s":"She died on February 24, 2020, at the age of 101, but her pioneering legacy will never be {forgotten|remembered}.","ex":"정답 ▶ forgotten (잊힌)\n오답 ▶ remembered (기억된)\n이유: but으로 '세상을 떠났다'와 대조 + never → 결코 '잊히지' 않을 것"}]
TF=[
 ["People trusted Katherine's hand calculations more than those of computers.",True,"정답 ▶ T\n이유: 그녀의 손 계산은 디지털 컴퓨터보다 더 신뢰받았어요.\n어휘 ▶ hand calculations = calculations by hand","❹","were trusted more than digital computers"],
 ["John Glenn was getting ready to be the first American to orbit the Earth.",True,"정답 ▶ T\n이유: 미국 역사상 처음으로 지구 궤도를 돌 준비를 하고 있었어요.\n어휘 ▶ get ready to = prepare to","❹","to orbit the Earth for the first time in American history"],
 ["The electronic computer NASA used made no mistakes at all.",False,"정답 ▶ F\n이유: 사소한 오류를 많이 냈어요(made many minor errors).","❹","it made many minor errors"],
 ["Glenn asked Katherine to check the computer's numbers by hand.",True,"정답 ▶ T\n이유: 기계의 수치를 손으로 다시 확인해 달라고 했어요.\n어휘 ▶ check = double-check · numbers = figures","❹","to double-check the machine's figures by hand"],
 ["Katherine checked all the calculations in just one hour.",False,"정답 ▶ F\n이유: 하루 반(a day and a half) 동안 확인했어요.","❹","spent a day and a half checking the calculations"],
 ["Katherine also did calculations for the mission that first sent people to the Moon.",True,"정답 ▶ T\n이유: 1969년 처음으로 세 사람을 달에 보낸 아폴로 11호의 계산팀이었어요.","❹","performed calculations for Apollo 11"],
 ["Katherine worked at NASA for more than forty years.",False,"정답 ▶ F\n이유: NASA에서 33년(thirty-three years) 일했어요.","❺","after thirty-three years at NASA"],
 ["After retiring, Katherine worked to give Black girls access to STEM education.",True,"정답 ▶ T\n이유: 흑인 소녀들의 STEM 교육 기회를 옹호하는 데 여생을 바쳤어요.","❺","championing access to STEM education for Black girls"],
 ["Katherine received the Presidential Medal of Freedom from President Obama.",True,"정답 ▶ T\n이유: 2015년 오바마 대통령이 대통령 자유 훈장을 수여했어요.\n어휘 ▶ receive A from B ↔ B award A","❺","awarded her the Presidential Medal of Freedom"],
 ["NASA named a building after Katherine only after she died.",False,"정답 ▶ F\n이유: 2017년에 건물을 헌정했고, 그녀는 2020년에 세상을 떠났어요. 살아 있을 때예요.\n어휘 ▶ name A after B B의 이름을 따서 A를 짓다","❺","In 2017, NASA dedicated a building in her honor"]]
MC=[
 dict(n="❹",box=["❹"],q="본문 ❹의 내용과 <u>일치하는</u> 것은?",opts=[
  "Glenn wanted Katherine to verify the computer's results before his flight.",
  "The electronic computer had been used in the space program for many years.",
  "Katherine used a modern digital calculator to check the numbers.",
  "Glenn refused to fly unless the computer approved Katherine's work.",
  "Katherine's work ended with the Apollo 11 mission."],
  ex="정답 ▶ Glenn wanted Katherine to verify the computer's results before his flight.\n이유: asked Katherine Johnson to double-check the machine's figures by hand\n오답 ▶ ② a year earlier(1년 전) 처음 도입 ③ only a pencil and a slide rule(연필과 계산자만) ④ 반대: 그녀가 괜찮다고 하면 출발 ⑤ 화성 계획(Mars)까지\n포인트 ▶ verify 검증하다 = double-check · results ≒ figures",
  per=[["글렌은 비행 전에 캐서린이 컴퓨터 결과를 검증해 주길 원했다.","to double-check the machine's figures by hand","verify = double-check ✔"],
       ["그 전자 컴퓨터는 우주 프로그램에서 수년간 쓰였다.","first introduced into the space program a year earlier","many years ✗ → 1년 전 처음"],
       ["캐서린은 최신 디지털 계산기로 수치를 확인했다.","Using only a pencil and a slide rule","연필과 계산자만"],
       ["글렌은 컴퓨터가 캐서린의 계산을 승인해야만 비행하겠다고 했다.","If she says the numbers are good","거꾸로: 캐서린이 확인"],
       ["캐서린의 일은 아폴로 11호로 끝났다.","even the plan to put people on Mars","화성 계획까지"]]),
 dict(n="❺",box=["❺"],q="본문 ❺의 내용과 일치하지 <u>않는</u> 것은?",opts=[
  "Katherine stopped caring about education after she left NASA.",
  "Katherine left NASA in 1986 after more than three decades there.",
  "Obama praised Katherine for not letting social expectations hold her back.",
  "A NASA facility in Virginia was named after Katherine.",
  "Katherine lived to be over one hundred years old."],
  ex="정답 ▶ Katherine stopped caring about education after she left NASA.\n이유: she dedicated the rest of her life to championing access to STEM education for Black girls. 여생을 교육에 바쳤어요.\n오답 ▶ 나머지는 모두 본문을 다른 어휘로 바꿔 쓴 일치 문장\n포인트 ▶ leave = retire from · three decades 30년 (33년은 30년 이상) · hold back 막다 ≒ limit · be named after ~의 이름을 따서 짓다",
  per=[["캐서린은 NASA를 떠난 후 교육에 관심을 끊었다.","she dedicated the rest of her life to championing access to STEM education","stopped caring ✗ → 여생을 바침"],
       ["캐서린은 30년 넘게 일한 뒤 1986년에 NASA를 떠났다.","Katherine retired in 1986 after thirty-three years at NASA","three decades = 30년 · 33년 → more than"],
       ["오바마는 캐서린이 사회적 기대에 발목 잡히지 않은 것을 칭찬했다.","refused to be limited by society's expectations","hold back ≒ limit"],
       ["버지니아의 NASA 시설은 캐서린의 이름을 따서 지어졌다.","named it the Katherine G. Johnson Computational Research Facility","be named after"],
       ["캐서린은 100세 넘게 살았다.","at the age of 101","101세"]]),
 dict(n="❹",box=["❹"],q="본문 ❹의 내용과 <u>일치하는</u> 것은?",opts=[
  "캐서린은 하루 반 동안 연필과 계산자만으로 계산을 확인했다.",
  "존 글렌은 1962년 달에 처음 착륙한 미국인이다.",
  "NASA의 전자 컴퓨터는 오류 없이 우주선의 궤적을 계산했다.",
  "글렌은 캐서린의 계산보다 컴퓨터의 계산을 더 믿었다.",
  "화성에 사람을 보내는 계획은 이미 끝났다."],
  ex="정답 ▶ 캐서린은 하루 반 동안 연필과 계산자만으로 계산을 확인했다.\n이유: Using only a pencil and a slide rule, Katherine spent a day and a half checking the calculations\n오답 ▶ ② 지구 궤도(orbit the Earth)를 돈 최초의 미국인 ③ many minor errors ④ 캐서린이 괜찮다고 해야 출발 ⑤ still being worked on today(지금도 진행 중)\n포인트 ▶ slide rule 계산자 · trajectory 궤적",
  per=[["","spent a day and a half checking the calculations","일치 ✔"],
       ["","the first American astronaut to orbit the Earth","지구 궤도 비행"],
       ["","it made many minor errors","오류 많음"],
       ["","If she says the numbers are good","캐서린을 더 신뢰"],
       ["","which is still being worked on today","아직 진행 중"]])]
PICK2=[
 {"s":"Katherine's remarkable calculations by hand {were|was} trusted more than digital computers.","ex":"정답 ▶ were\n이유: 주어 calculations(복수). by hand는 수식어"},
 {"s":"In early 1962, John Glenn, one of the pioneering American {astronauts|astronaut}, was preparing to orbit the Earth for the first time in American history.","ex":"정답 ▶ astronauts\n이유: one of the + 복수명사"},
 {"s":"In early 1962, John Glenn, one of the pioneering American astronauts, was preparing {to orbit|orbiting} the Earth for the first time in American history.","ex":"정답 ▶ to orbit\n이유: prepare + to부정사 ~할 준비를 하다"},
 {"s":"NASA used an electronic computer, first {introduced|introducing} into the space program a year earlier, to calculate the spaceship's trajectory, but it made many minor errors.","ex":"정답 ▶ introduced\n이유: 컴퓨터가 '도입된' 수동 → 과거분사구가 앞의 명사를 꾸밈 (= which was first introduced)"},
 {"s":"Glenn, {who|which} was concerned about its accuracy, asked Katherine Johnson to double-check the machine's figures by hand.","ex":"정답 ▶ who\n이유: 사람 선행사(Glenn) + 콤마 → 계속적 용법 who"},
 {"s":"Glenn, who was concerned about its accuracy, asked Katherine Johnson {to double-check|double-check} the machine's figures by hand.","ex":"정답 ▶ to double-check\n이유: ask + 목적어 + to부정사 ~에게 …해 달라고 요청하다"},
 {"s":"{Using|Used} only a pencil and a slide rule, Katherine spent a day and a half checking the calculations and finally made sure of them.","ex":"정답 ▶ Using\n이유: 분사구문. 캐서린이 연필을 '사용하는' 능동 → 현재분사"},
 {"s":"Using only a pencil and a slide rule, Katherine spent a day and a half {checking|to check} the calculations and finally made sure of them.","ex":"정답 ▶ checking\n이유: spend + 시간 + -ing ~하는 데 시간을 쓰다"},
 {"s":"Katherine was also part of the team that performed calculations for Apollo 11, {which|that} sent the first three men to the Moon in 1969, and even the plan to put people on Mars, which is still being worked on today.","ex":"정답 ▶ which\n이유: 콤마 뒤 계속적 용법 → which (that 불가)"},
 {"s":"Katherine was also part of the team that performed calculations for Apollo 11, which sent the first three men to the Moon in 1969, and even the plan to put people on Mars, which is still being {worked|working} on today.","ex":"정답 ▶ worked\n이유: 계획이 '진행되고 있는' 수동 + 진행 → is being p.p. (work on ~에 공을 들이다 → be worked on)"},
 {"s":"After that, she dedicated the rest of her life to {championing|champion} access to STEM education for Black girls.","ex":"정답 ▶ championing\n이유: dedicate A to -ing — 여기서 to는 전치사 → 동명사"},
 {"s":"For her contributions, President Barack Obama awarded her the Presidential Medal of Freedom in 2015 and said, \"Katherine G. Johnson refused {to be limited|being limited} by society's expectations of her gender and race while expanding the boundaries of humanity's reach.\"","ex":"정답 ▶ to be limited\n이유: refuse는 to부정사를 목적어로. 그녀가 '제한되는' 수동 → to be p.p."},
 {"s":"She died on February 24, 2020, at the age of 101, but her pioneering legacy will never {be forgotten|forget}.","ex":"정답 ▶ be forgotten\n이유: 유산이 '잊히는' 수동 → will be p.p. (forget - forgot - forgotten)"}]
VERB=[
 {"s":"Katherine's remarkable calculations by hand were ___ more than digital computers.","v":"trust","a":["trusted"],"ex":"정답 ▶ trusted\n이유: were + p.p. 수동태"},
 {"s":"In early 1962, John Glenn, one of the pioneering American astronauts, was ___ to orbit the Earth for the first time in American history.","v":"prepare","a":["preparing"],"ex":"정답 ▶ preparing\n이유: was + -ing 과거진행형"},
 {"s":"NASA used an electronic computer, first ___ into the space program a year earlier, to calculate the spaceship's trajectory, but it made many minor errors.","v":"introduce","a":["introduced"],"ex":"정답 ▶ introduced\n이유: '도입된' 컴퓨터 → 과거분사"},
 {"s":"Using only a pencil and a slide rule, Katherine spent a day and a half ___ the calculations and finally made sure of them.","v":"check","a":["checking"],"ex":"정답 ▶ checking\n이유: spend + 시간 + -ing"},
 {"s":"Eventually, Glenn ___ the first American astronaut to orbit the Earth.","v":"become","a":["became"],"ex":"정답 ▶ became\n이유: 과거의 일 (become - became - become)"},
 {"s":"Katherine ___ in 1986 after thirty-three years at NASA.","v":"retire","a":["retired"],"ex":"정답 ▶ retired\n이유: in 1986 과거 → 과거형"},
 {"s":"For her contributions, President Barack Obama ___ her the Presidential Medal of Freedom in 2015 and said, \"Katherine G. Johnson refused to be limited by society's expectations of her gender and race while expanding the boundaries of humanity's reach.\"","v":"award","a":["awarded"],"ex":"정답 ▶ awarded\n이유: in 2015 과거, said와 병렬 → 과거형\n포인트 ▶ award A B A에게 B를 수여하다"},
 {"s":"For her contributions, President Barack Obama awarded her the Presidential Medal of Freedom in 2015 and said, \"Katherine G. Johnson refused to be limited by society's expectations of her gender and race while ___ the boundaries of humanity's reach.\"","v":"expand","a":["expanding"],"ex":"정답 ▶ expanding\n이유: 접속사 while + 분사(주어 생략) — 그녀가 '넓히는' 능동"},
 {"s":"She died on February 24, 2020, at the age of 101, but her pioneering legacy will never be ___.","v":"forget","a":["forgotten"],"ex":"정답 ▶ forgotten\n이유: will be + p.p. 수동 (forget - forgot - forgotten)"}]
ERR=[
 {"s":"Katherine's remarkable calculations by hand [[was]] trusted more than digital computers. In early 1962, John Glenn, one of the [[pioneering]] American astronauts, was preparing [[to orbit]] the Earth for the first time in American history.","w":0,"fix":"were","ex":"틀린 곳 ▶ ① was → were\n이유: 주어 calculations(복수)\n나머지 ▶ ② 선구적인(능동) ✔ ③ prepare to ✔"},
 {"s":"NASA used an electronic computer, first [[introducing]] into the space program a year earlier, [[to calculate]] the spaceship's trajectory, but it [[made]] many minor errors.","w":0,"fix":"introduced","ex":"틀린 곳 ▶ ① introducing → introduced\n이유: 컴퓨터가 '도입된' 수동\n나머지 ▶ ② 목적의 to부정사 ✔ ③ 과거형 ✔"},
 {"s":"Glenn, [[which]] was concerned about its accuracy, asked Katherine Johnson [[to double-check]] the machine's figures [[by hand]].","w":0,"fix":"who","ex":"틀린 곳 ▶ ① which → who\n이유: 선행사 Glenn(사람)\n나머지 ▶ ② ask O to-v ✔ ③ 손으로 ✔"},
 {"s":"[[Used]] only a pencil and a slide rule, Katherine spent a day and a half [[checking]] the calculations and finally [[made]] sure of them.","w":0,"fix":"Using","ex":"틀린 곳 ▶ ① Used → Using\n이유: 캐서린이 '사용하는' 능동 → 현재분사\n나머지 ▶ ② spend 시간 -ing ✔ ③ spent와 병렬 ✔"},
 {"s":"Katherine was also part of the team that performed calculations for Apollo 11, [[that]] sent the first three men to the Moon in 1969, and even the plan [[to put]] people on Mars, which is still [[being worked]] on today.","w":0,"fix":"which","ex":"틀린 곳 ▶ ① that → which\n이유: 콤마 뒤 계속적 용법에는 that 불가\n나머지 ▶ ② the plan을 꾸미는 to부정사 ✔ ③ 진행 수동 ✔"},
 {"s":"Katherine [[retired]] in 1986 after thirty-three years at NASA. After that, she [[dedicated]] the rest of her life to [[champion]] access to STEM education for Black girls.","w":2,"fix":"championing","ex":"틀린 곳 ▶ ③ champion → championing\n이유: dedicate A to -ing (to는 전치사)\n나머지 ▶ ① ② 과거형 ✔"},
 {"s":"She died on February 24, 2020, [[at the age of]] 101, but her [[pioneering]] legacy will never [[forget]].","w":2,"fix":"be forgotten","ex":"틀린 곳 ▶ ③ forget → be forgotten\n이유: 유산이 '잊히는' 수동\n나머지 ▶ ① ~의 나이에 ✔ ② 선구적인 ✔"}]
SCR=["D1","D4","D6","D7","E1","E2","E5"]
ORDER=[
 (["D2","D3","D4","D5"],["1962년 글렌이 지구 궤도 비행을 준비","NASA 전자 컴퓨터가 궤적 계산, 하지만 오류가 많음","정확성을 걱정한 글렌이 캐서린에게 재확인 부탁","'그녀가 맞다고 하면 출발하겠다'"]),
 (["D4","D5","D6","D7"],["글렌이 손으로 재확인 부탁","'그녀가 맞다고 하면 갈 준비 완료'","연필과 계산자로 하루 반 동안 확인","결국 글렌이 지구 궤도를 돈 첫 미국인이 됨"]),
 (["E1","E2","E3","E4"],["1986년 33년 만에 은퇴","그 후 흑인 소녀들의 STEM 교육을 옹호","2015년 오바마가 대통령 자유 훈장 수여","2017년 NASA가 그녀를 기려 건물 헌정"])]
INSERT=[
 (["D1","D2","D3","D4"],3,["손 계산이 컴퓨터보다 신뢰받음","1962년 글렌의 궤도 비행 준비","컴퓨터가 궤적 계산, 하지만 오류가 많음","그 정확성(its accuracy)을 걱정한 글렌이 재확인 부탁"],"정답 ▶ ③\n이유: its는 바로 앞의 '전자 컴퓨터'를 가리켜요. 오류가 많았으니 정확성을 걱정한 거예요."),
 (["D5","D6","D7","D8"],2,["'그녀가 맞다고 하면 출발'","하루 반 동안 확인","결국(Eventually) 글렌이 첫 궤도 비행 성공","아폴로 11호·화성 계획에도 참여"],"정답 ▶ ②\n이유: 캐서린의 확인이 끝난 '뒤에' 결국 비행에 성공했어요. 그다음 also로 다른 업적이 이어져요."),
 (["E2","E3","E4","E5"],1,["은퇴 후 흑인 소녀 STEM 교육 옹호","그 공헌으로(For her contributions) 오바마가 훈장 수여","2017년 NASA 건물 헌정","2020년 별세, 유산은 잊히지 않을 것"],"정답 ▶ ①\n이유: 시간 순서(1986 은퇴 → 2015 훈장 → 2017 건물 → 2020 별세)대로예요. For her contributions가 앞의 공헌을 받아요.")]
ODD=[
 (["D2","D3","Personal computers became common in American homes in the 1960s.","D4"],2,"정답 ▶ ③\n이유: 글렌의 비행과 NASA 컴퓨터의 오류 이야기예요. 가정용 컴퓨터 이야기는 관계없고, 다음 문장의 its(컴퓨터의)가 가리킬 대상도 흐려져요."),
 (["E3","E4","Many people today still prefer paper maps to GPS.","E5"],2,"정답 ▶ ③\n이유: 캐서린이 받은 훈장·헌정 건물·유산 이야기의 흐름이에요. 종이 지도 이야기는 관계없어요.")]
BLANK=[
 {"s":"Katherine's remarkable calculations by hand were ____ more than digital computers.","opts":["trusted","feared","ignored","doubted"],"ex":"정답 ▶ trusted (신뢰받은)\n이유: 글렌이 컴퓨터 대신 캐서린에게 재확인을 부탁할 만큼 '믿었어요'.\n오답 ▶ feared 두려워진 · ignored 무시된 · doubted 의심받은"},
 {"s":"NASA used an electronic computer, first introduced into the space program a year earlier, to calculate the spaceship's trajectory, but it made many minor ____.","opts":["errors","friends","profits","decisions"],"ex":"정답 ▶ errors (오류)\n이유: but 뒤의 단점 → 그래서 글렌이 정확성을 걱정했어요.\n오답 ▶ friends 친구 · profits 이익 · decisions 결정"},
 {"s":"Glenn, who was concerned about its ____, asked Katherine Johnson to double-check the machine's figures by hand.","opts":["accuracy","size","color","price"],"ex":"정답 ▶ accuracy (정확성)\n이유: 오류가 많았으니 '정확성'을 걱정 → 다시 확인 부탁\n오답 ▶ size 크기 · color 색 · price 가격"},
 {"s":"After that, she dedicated the rest of her life to championing ____ to STEM education for Black girls.","opts":["access","resistance","opposition","limits"],"ex":"정답 ▶ access (접근, 기회)\n이유: 자신이 겪은 교육 차별을 겪지 않도록 흑인 소녀들의 교육 '기회'를 옹호\n오답 ▶ resistance 저항 · opposition 반대 · limits 제한"},
 {"s":"She died on February 24, 2020, at the age of 101, but her pioneering ____ will never be forgotten.","opts":["legacy","mistake","failure","debt"],"ex":"정답 ▶ legacy (유산, 업적)\n이유: but으로 '세상을 떠났지만 그녀의 업적은 잊히지 않는다'\n오답 ▶ mistake 실수 · failure 실패 · debt 빚"}]
GRAM=[
 {"q":"빈칸에 알맞은 것은?<br><b>Her calculations were trusted ______ than digital computers.</b>","opts":["more","most","much","many"],"ex":"정답 ▶ more\n이유: than이 있으면 비교급 → more"},
 {"q":"빈칸에 알맞은 것은?<br><b>NASA used a computer, first ______ a year earlier.</b>","opts":["introduced","introducing","introduce","to introduce"],"ex":"정답 ▶ introduced\n이유: 컴퓨터가 '도입된' 수동 → 과거분사가 명사를 꾸밈"},
 {"q":"빈칸에 알맞은 것은?<br><b>Glenn asked Katherine ______ the figures.</b>","opts":["to check","checking","check","checked"],"ex":"정답 ▶ to check\n이유: ask + 목적어 + to부정사"},
 {"q":"빈칸에 알맞은 것은?<br><b>She spent a day and a half ______ the calculations.</b>","opts":["checking","to check","check","checked"],"ex":"정답 ▶ checking\n이유: spend + 시간 + -ing ~하는 데 시간을 쓰다"},
 {"q":"빈칸에 알맞은 것은?<br><b>Glenn became the first American astronaut ______ the Earth.</b>","opts":["to orbit","orbits","orbited","orbit"],"ex":"정답 ▶ to orbit\n이유: the first + 명사 + to부정사 ~한 첫 번째 …"},
 {"q":"빈칸에 알맞은 것은?<br><b>The plan to put people on Mars is still ______ on today.</b>","opts":["being worked","working","worked","been worked"],"ex":"정답 ▶ being worked\n이유: 계획이 '진행되고 있는' 진행 수동 → is being p.p."},
 {"q":"빈칸에 알맞은 것은?<br><b>She dedicated her life to ______ others.</b>","opts":["helping","help","helped","to help"],"ex":"정답 ▶ helping\n이유: dedicate A to -ing (to는 전치사)\n본문 ▶ dedicated the rest of her life to championing"},
 {"q":"빈칸에 알맞은 것은?<br><b>She refused ______ by society's expectations.</b>","opts":["to be limited","to limit","limiting","being limit"],"ex":"정답 ▶ to be limited\n이유: refuse + to부정사, 그녀가 '제한되는' 수동 → to be p.p."},
 {"q":"빈칸에 알맞은 것은?<br><b>Her legacy will never ______.</b>","opts":["be forgotten","forget","be forgetting","forgotten"],"ex":"정답 ▶ be forgotten\n이유: 조동사 + be + p.p. 수동"}]
