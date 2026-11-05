N=36
MC=[
 dict(q="글의 내용과 <u>일치하는</u> 것은?",opts=[
  "The tortoise deals with intense heat simply by staying out of it.",
  "The tortoise is active for most of its life.",
  "The tortoise comes out of its tunnel mainly during dry periods.",
  "The tortoise gets water only by drinking from streams.",
  "The tortoise's bladder works the same way as that of most animals."],
  ex="정답 ▶ The tortoise deals with intense heat simply by staying out of it.\n이유: a simple solution for coping with Death Valley's extreme heat: It avoids it.\n오답 ▶ ② 생의 90% 이상을 움직이지 않음(immobile) ③ 비가 충분히 온 뒤(after a good rain)에 나옴 ④ 식물을 먹고 구멍을 파서 빗물을 모음 ⑤ Unlike most animals 대부분의 동물과 달리\n포인트 ▶ deal with = cope with 대처하다 · intense = extreme 극심한 · stay out of = avoid 피하다",
  per=[["거북은 그저 더위를 피하는 것으로 극심한 더위에 대처한다.","It avoids it","deal with = cope with · stay out of = avoid ✔"],
       ["거북은 생의 대부분을 활발히 움직인다.","more than 90 percent of its life immobile","active ↔ immobile"],
       ["거북은 주로 건조한 시기에 굴에서 나온다.","the tortoise usually only surfaces after a good rain","dry ↔ after a good rain"],
       ["거북은 오직 개울물을 마셔서 물을 얻는다.","by eating plants and digging holes to collect rain","only drinking ✗"],
       ["거북의 방광은 대부분의 동물과 같은 방식으로 작동한다.","Unlike most animals","the same ↔ unlike"]]),
 dict(q="글의 내용과 일치하지 <u>않는</u> 것은?",opts=[
  "Being picked up calms tortoises so much that they hold on to their water.",
  "The tortoise digs holes in order to gather rainwater.",
  "During its long hibernation, the tortoise depends on its bladder for water.",
  "The tortoise can survive a whole year without consuming any fresh water.",
  "The tortoise spends the winter in an inactive, sleep-like state."],
  ex="정답 ▶ Being picked up calms tortoises so much that they hold on to their water.\n이유: Tortoises become so terrified when people pick them up that they empty their bladders. 진정되는 게 아니라 겁에 질려 물을 쏟아 버려요.\n오답 ▶ 나머지는 모두 본문을 바꿔 쓴 일치 문장\n포인트 ▶ calm 진정시키다 ↔ terrified 겁에 질린 · hold on to 붙잡아 두다 ↔ empty 비우다 · gather = collect · depend on = rely on · consume = take in · inactive, sleep-like state = hibernation",
  per=[["들어 올려지면 거북은 아주 차분해져서 물을 그대로 지킨다.","they empty their bladders, losing their precious water reserves","calm ↔ terrified · hold on to ↔ empty ✗"],
       ["거북은 빗물을 모으려고 구멍을 판다.","digging holes to collect rain","gather = collect"],
       ["긴 동면 기간 동안 거북은 물을 방광에 의존한다.","to stay supplied with water through its extended hibernation, the reptile relies on","depend on = rely on · long = extended"],
       ["거북은 민물을 전혀 섭취하지 않고 1년을 버틸 수 있다.","can go a full year without taking in any freshwater","consume = take in · survive ≒ go"],
       ["거북은 겨울을 활동하지 않는 잠과 비슷한 상태로 보낸다.","hibernates during the winter","hibernate 동면하다 = 겨울잠"]]),
 dict(q="글의 내용과 <u>일치하는</u> 것은?",opts=[
  "사람이 거북을 들어 올리면 거북은 저장해 둔 물을 잃을 수 있다.",
  "사막거북은 더위를 견디려고 낮에 더 활발하게 움직인다.",
  "사막거북은 여름 내내 굴 밖에서 먹이를 찾는다.",
  "거북의 방광은 물을 몸 밖으로 빨리 내보내는 역할을 한다.",
  "공원 관리원들은 길을 건너는 거북을 도와주라고 당부한다."],
  ex="정답 ▶ 사람이 거북을 들어 올리면 거북은 저장해 둔 물을 잃을 수 있다.\n이유: they empty their bladders, losing their precious water reserves\n오답 ▶ ② 더위를 피함(avoids) ③ 여름 대부분을 굴속(in its tunnel)에서 지냄 ④ 저장 탱크(holding tank) + 재흡수(reabsorb) ⑤ 멈춰서 돕지 말라고(not to stop and help) 당부\n포인트 ▶ water reserves 저장 수분 · reabsorb 재흡수하다",
  per=[["","losing their precious water reserves","일치 ✔"],
       ["","It avoids it","더위를 피함"],
       ["","stays in its tunnel for much of the summer","여름 대부분 굴속"],
       ["","the tortoise's bladder acts as a holding tank","저장 탱크"],
       ["","remind visitors not to stop and help the slow-movers across the road","돕지 말라고 당부"]])]
TF=[
 ["The tortoise handles the heat by staying away from it.",True,"정답 ▶ T\n이유: 더위에 대처하는 간단한 방법은 그것을 피하는 거예요.\n어휘 ▶ handle = cope with · stay away from = avoid","It avoids it"],
 ["The tortoise sleeps through the winter.",True,"정답 ▶ T\n이유: 겨울 동안 동면해요(hibernates).\n어휘 ▶ sleep through the winter 겨울잠을 자다 = hibernate","hibernates during the winter"],
 ["The tortoise usually appears above ground after a heavy rain.",True,"정답 ▶ T\n이유: 대개 비가 충분히 온 뒤에야 밖으로 나와요.\n어휘 ▶ appear above ground = surface (동사) 수면·지면 위로 나오다 · a good rain = 비가 넉넉히 옴","only surfaces after a good rain"],
 ["The tortoise stores up water partly by eating plants.",True,"정답 ▶ T\n이유: 식물을 먹어서 물을 비축해요.\n어휘 ▶ store up = stock up on 비축하다","stocks up on water by eating plants"],
 ["The tortoise's bladder is a simple organ, just like most animals'.",False,"정답 ▶ F\n이유: 매우 정교한(highly sophisticated) 방광이고, 대부분의 동물과 달라요(Unlike most animals).\n어휘 ▶ simple ↔ sophisticated 정교한","its highly sophisticated bladder"],
 ["The tortoise's bladder allows it to take water back into its body.",True,"정답 ▶ T\n이유: 물을 몸속으로 재흡수할 수 있게 해 줘요.\n어휘 ▶ take back into = reabsorb 재흡수하다","allowing it to reabsorb water back into its body"],
 ["Frightened tortoises keep their water safe by holding it in their bladders.",False,"정답 ▶ F\n이유: 겁에 질리면 방광을 비워 소중한 물을 잃어요.\n어휘 ▶ frightened = terrified · keep ~ safe ↔ lose","they empty their bladders, losing their precious water reserves"]]
PICK1=[
 {"s":"The desert tortoise has a simple solution for {coping|copying} with Death Valley's extreme heat: It avoids it.","ex":"정답 ▶ coping (cope with ~에 대처하다)\n오답 ▶ copying (베끼기)\n포인트 ▶ cope with = deal with = handle"},
 {"s":"The slow-moving creature {hibernates|hesitates} during the winter and stays in its tunnel for much of the summer, meaning that it spends more than 90 percent of its life immobile.","ex":"정답 ▶ hibernates (동면하다)\n오답 ▶ hesitates (망설이다)\n이유: during the winter + 생의 90%를 움직이지 않음 → 겨울잠\n포인트 ▶ hibernation 동면"},
 {"s":"In fact, the tortoise usually only {surfaces|suffers} after a good rain.","ex":"정답 ▶ surfaces (밖으로 나오다)\n오답 ▶ suffers (고통받다)\n이유: 굴속에 있다가 비가 온 뒤에야 '밖으로 나와' 일을 시작해요(Then, it gets to work).\n포인트 ▶ surface는 명사 '표면' 말고 동사 '떠오르다, 나타나다'로도 써요."},
 {"s":"The tortoise {stocks|stalks} up on water by eating plants and digging holes to collect rain.","ex":"정답 ▶ stocks (stock up on ~을 비축하다)\n오답 ▶ stalks (몰래 뒤쫓다)\n포인트 ▶ stock 재고, 비축"},
 {"s":"But to stay supplied with water through its extended hibernation, the reptile {relies|relieves} on something else — its highly sophisticated bladder.","ex":"정답 ▶ relies (rely on ~에 의존하다)\n오답 ▶ relieves (덜어 주다)\n포인트 ▶ rely on = depend on · the reptile(파충류) = the tortoise"}]
PICK2=[
 {"s":"The desert tortoise has a simple solution for {coping|cope} with Death Valley's extreme heat: It avoids it.","ex":"정답 ▶ coping\n이유: 전치사 for 뒤 → 동명사\n포인트 ▶ a solution for -ing ~하는 해결책"},
 {"s":"Unlike most animals, the tortoise's bladder acts as a holding tank, {allowing|allowed} it to reabsorb water back into its body.","ex":"정답 ▶ allowing\n이유: 분사구문. 방광이 거북에게 물을 재흡수하게 '해 주는' 능동 → 현재분사 (allow + 목적어 + to부정사)"},
 {"s":"And {because|because of} its bladder is so important to a tortoise's survival, park rangers often remind visitors not to stop and help the slow-movers across the road.","ex":"정답 ▶ because\n이유: 뒤에 주어+동사(its bladder is) → 접속사 because. because of 뒤엔 명사(구)"},
 {"s":"And because its bladder is so important to a tortoise's survival, park rangers often remind visitors not to stop and {help|helping} the slow-movers across the road.","ex":"정답 ▶ help\n이유: not to stop and (to) help — to부정사 병렬 → 동사원형\n포인트 ▶ help + 목적어 + across ~가 건너도록 돕다"},
 {"s":"Tortoises become so terrified when people pick them up {that|which} they empty their bladders, losing their precious water reserves.","ex":"정답 ▶ that\n이유: so + 형용사 + that ~ = 너무 ~해서 …하다\n포인트 ▶ so 뒤에 when절이 끼어 있어도 that으로 이어져요."}]
VERB=[
 {"s":"The tortoise stocks up on water by eating plants and ___ holes to collect rain.","v":"dig","a":["digging"],"ex":"정답 ▶ digging\n이유: by eating과 and로 병렬 → 동명사. dig는 g를 한 번 더 써서 digging"},
 {"s":"And because its bladder is so important to a tortoise's survival, park rangers often ___ visitors not to stop and help the slow-movers across the road.","v":"remind","a":["remind"],"ex":"정답 ▶ remind\n이유: 주어 park rangers(복수), 일반적 사실 → 현재시제 remind\n포인트 ▶ remind + 목적어 + (not) to부정사 ~에게 …하라고(하지 말라고) 상기시키다"},
 {"s":"The slow-moving creature ___ during the winter and stays in its tunnel for much of the summer, meaning that it spends more than 90 percent of its life immobile.","v":"hibernate","a":["hibernates"],"ex":"정답 ▶ hibernates\n이유: 주어 The slow-moving creature(단수), stays와 병렬 → hibernates"}]
ERR=[
 {"s":"The desert tortoise has a simple solution for [[cope]] with Death Valley's [[extreme]] heat: It [[avoids]] it.","w":0,"fix":"coping","ex":"틀린 곳 ▶ ① cope → coping\n이유: 전치사 for 뒤 → 동명사\n나머지 ▶ ② 형용사 extreme이 heat 수식 ✔ ③ 주어 It(단수) ✔"},
 {"s":"But [[to stay]] supplied with water through its [[extending]] hibernation, the reptile [[relies]] on something else — its highly sophisticated bladder.","w":1,"fix":"extended","ex":"틀린 곳 ▶ ② extending → extended\n이유: 동면이 '연장된, 긴' 상태 → 과거분사 (extended 긴, 장기간의)\n나머지 ▶ ① ~하기 위해(목적) ✔ ③ 주어 the reptile(단수) ✔"},
 {"s":"And because its bladder is so important to a tortoise's survival, park rangers often remind visitors [[not to stop]] and [[helping]] the slow-movers [[across]] the road.","w":1,"fix":"help","ex":"틀린 곳 ▶ ② helping → help\n이유: not to stop and (to) help — to부정사 병렬\n나머지 ▶ ① 부정사의 부정 not to ✔ ③ across the road 길 건너편으로 ✔"}]
SCR=[0,4,6,9]
ORDER=[{"idx":[0,1,2,3],"flow":["사막거북의 더위 해결책 = 피하기","겨울엔 동면, 여름엔 굴속 → 생의 90% 이상 움직이지 않음","사실 비가 넉넉히 온 뒤에야 밖으로 나옴","그러고 나서(Then) 일을 시작함"]}]
INSERT=[{"idx":[6,7,8,9],"given":3,"flow":["방광 = 저장 탱크, 물 재흡수","놀랍게도 민물 없이 1년을 버팀","그래서 관리원들은 거북을 돕지 말라고 당부","사람이 들면 겁에 질려 방광을 비워 물을 잃음"],"ex":"정답 ▶ ③\n이유: 주어진 문장은 '왜 돕지 말라고 하는지'에 대한 이유예요. 관리원 당부 문장 바로 뒤, 글의 맨 끝!\n포인트 ▶ 당부(돕지 마세요) → 이유(들면 물을 잃어요)"}]
ODD=[{"lines":[5,6,"Because of this, the tortoise must drink fresh water every day.",7],"odd":2,"ex":"정답 ▶ ③\n이유: 바로 다음 문장에서 민물 없이도 꼬박 1년을 지낼 수 있다고 해요. 매일 물을 마셔야 한다는 문장은 정반대예요."}]
BLANK=[
 {"s":"The slow-moving creature hibernates during the winter and stays in its tunnel for much of the summer, meaning that it spends more than 90 percent of its life ____.","opts":["immobile","hunting","underwater","awake"],"ex":"정답 ▶ immobile (움직이지 않는)\n이유: 겨울엔 동면, 여름 대부분은 굴속 → 생의 대부분을 '움직이지 않고' 보내요.\n오답 ▶ hunting 사냥하며 · underwater 물속에서 · awake 깨어 있는"},
 {"s":"Unlike most animals, the tortoise's bladder acts as a ____ tank, allowing it to reabsorb water back into its body.","opts":["holding","leaking","fuel","fish"],"ex":"정답 ▶ holding (저장하는)\n이유: 물을 담아 두었다가 다시 몸속으로 재흡수 → 저장 탱크(holding tank)\n오답 ▶ leaking 새는 · fuel tank 연료 탱크 · fish tank 수조"},
 {"s":"Tortoises become so terrified when people pick them up that they empty their bladders, losing their precious water ____.","opts":["reserves","tunnels","plants","rangers"],"ex":"정답 ▶ reserves (비축분, 저장량)\n이유: 방광을 비우면 모아 둔 '소중한 저장 수분'을 잃어요.\n포인트 ▶ reserve 비축(분); 동사로는 '예약하다'"}]
GRAM=[
 {"q":"빈칸에 알맞은 것은?<br><b>The tortoise was ______ scared that it emptied its bladder.</b>","opts":["so","such","very","too"],"ex":"정답 ▶ so\n이유: so + 형용사 + that ~ 너무 ~해서 …하다. such는 뒤에 (a) + 형용사 + 명사\n본문 ▶ Tortoises become so terrified when people pick them up that they empty their bladders"},
 {"q":"빈칸에 알맞은 것은?<br><b>You can save money by ______ your own lunch.</b>","opts":["making","make","made","to make"],"ex":"정답 ▶ making\n이유: by + 동명사 ~함으로써\n본문 ▶ stocks up on water by eating plants and digging holes"},
 {"q":"빈칸에 알맞은 것은?<br><b>______ most animals, the tortoise can go a year without water.</b>","opts":["Unlike","Although","Despite of","Because"],"ex":"정답 ▶ Unlike (~와 달리, 전치사)\n오답 ▶ Although·Because는 접속사라 뒤에 주어+동사 · Despite of는 틀린 표현(despite 또는 in spite of)\n본문 ▶ Unlike most animals, the tortoise's bladder acts as a holding tank"},
 {"q":"빈칸에 알맞은 것은?<br><b>The tortoise can go a full year without ______ any freshwater.</b>","opts":["drinking","drink","drank","to drink"],"ex":"정답 ▶ drinking\n이유: 전치사 without 뒤 → 동명사\n본문 ▶ without taking in any freshwater at all"}]
