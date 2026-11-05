N="❸"
VOCAB=[[w,m,N]+x for w,m,*x in [
 ["purify","~을 정화하다"],["polluted","오염된"],["mining","광업, 채굴"],["industry","산업"],["across the globe","전 세계에서"],
 ["dig up","~을 파내다 (dig - dug - dug)","dug up"],["transport","~을 운송하다, 옮기다"],["moreover","게다가"],["solve","~을 해결하다"],
 ["fortunately","다행히도"],["eco-friendly","친환경적인"],["cost-effective","비용 효율이 높은, 비용 대비 효과가 좋은"],["restore","~을 회복시키다, 복구하다"],
 ["willow","버드나무"],["extensive","광범위한, 넓게 퍼진"],["well-developed","잘 발달된"],["root system","뿌리 체계"],["as a result","결과적으로"],
 ["extract","~을 추출하다, 뽑아내다"],["a wide range of","매우 다양한, 광범위한"],["harmful","해로운, 유해한"],["material","물질"],
 ["acidity","산성도"],["heavy metal","중금속"],["effectiveness","효과, 유효성"],["purpose","목적"],["in development","개발[진행] 중인"],
 ["absorb","~을 흡수하다"],["promising","유망한, 촉망되는"],["explore","~을 탐구하다, 조사하다"],["find out","~을 알아내다"],
 ["in time","머지않아, 조만간"],["clean up","~을 깨끗이 치우다, 정화하다"]]]
PICK1=[
 {"s":"Mining and other industries are causing soil {pollution|solution} across the globe.","ex":"정답 ▶ pollution (오염)\n오답 ▶ solution (해결책)\n이유: 광업과 다른 산업들이 '일으키는(causing)' 것 → 오염"},
 {"s":"Although polluted soil can be dug up and transported to a landfill, this process is {expensive|inexpensive}.","ex":"정답 ▶ expensive (비싼)\n오답 ▶ inexpensive (저렴한)\n이유: Although(~이긴 하지만)로 '옮길 수는 있지만 비싸다'는 단점. 뒤에 나오는 버드나무는 cost-effective(비용 효율적)라 대조돼요."},
 {"s":"Moreover, it only moves the problem to another area and does not really {solve|cause} it.","ex":"정답 ▶ solve (해결하다)\n오답 ▶ cause (일으키다)\n이유: 문제를 다른 곳으로 '옮길 뿐' 실제로 '해결하지' 못해요. Moreover로 두 번째 단점을 덧붙여요."},
 {"s":"Fortunately, there is an eco-friendly and cost-effective way to {restore|destroy} polluted soil — planting willow trees.","ex":"정답 ▶ restore (회복시키다)\n오답 ▶ destroy (파괴하다)\n이유: Fortunately(다행히) → 오염된 흙을 '되살리는' 방법"},
 {"s":"These amazing trees have {extensive|expensive} and well-developed root systems.","ex":"정답 ▶ extensive (광범위한, 넓게 퍼진)\n오답 ▶ expensive (비싼)\n포인트 ▶ 철자가 비슷해요! extensive = wide-spreading"},
 {"s":"As a result, they naturally {extract|attract} a wide range of harmful materials from the soil.","ex":"정답 ▶ extract (뽑아내다)\n오답 ▶ attract (끌어들이다, 매혹하다)\n이유: 흙'에서(from the soil)' 해로운 물질을 '뽑아내요'. extract A from B"},
 {"s":"They can also grow quickly, even in soil with a high {acidity|activity} level or a lot of heavy metals in it.","ex":"정답 ▶ acidity (산성도)\n오답 ▶ activity (활동)\n이유: 중금속(heavy metals)과 나란히 '나쁜 흙'의 조건 → 산성도가 높은 흙"},
 {"s":"Scientists have found that some species of willow trees are able to {absorb|abandon} harmful materials better than others.","ex":"정답 ▶ absorb (흡수하다)\n오답 ▶ abandon (버리다)\n이유: 해로운 물질을 '더 잘 흡수하는' 종이 있다는 연구 결과"},
 {"s":"Therefore, this {promising|disappointing} area should be further explored to find out which trees are the most effective.","ex":"정답 ▶ promising (유망한)\n오답 ▶ disappointing (실망스러운)\n이유: '더 탐구되어야 한다'는 것은 가능성이 있기 때문 → 유망한 분야"}]
TF=[[a,b,c,N,d] for a,b,c,d in [
 ["Mining is one of the industries that pollute soil around the world.",True,"정답 ▶ T\n이유: 광업과 다른 산업들이 전 세계적으로 토양 오염을 일으키고 있어요.\n어휘 ▶ around the world = across the globe","Mining and other industries are causing soil pollution across the globe"],
 ["Moving polluted soil to a landfill is a cheap solution.",False,"정답 ▶ F\n이유: 그 과정은 비싸요(expensive).\n어휘 ▶ cheap 싼 ↔ expensive","this process is expensive"],
 ["Digging up polluted soil does not truly get rid of the problem.",True,"정답 ▶ T\n이유: 문제를 다른 곳으로 옮길 뿐 진짜로 해결하지 않아요.\n어휘 ▶ get rid of 없애다 ≒ solve · truly = really","does not really solve it"],
 ["Planting willow trees is eco-friendly but costly.",False,"정답 ▶ F\n이유: 친환경적이고 '비용 효율적인(cost-effective)' 방법이에요.\n어휘 ▶ costly 비싼 ↔ cost-effective 비용 대비 효과가 좋은","an eco-friendly and cost-effective way"],
 ["Willow trees have wide-spreading and well-developed roots.",True,"정답 ▶ T\n이유: 광범위하고 잘 발달된 뿌리 체계를 가지고 있어요.\n어휘 ▶ wide-spreading = extensive","extensive and well-developed root systems"],
 ["Willow trees can grow only in clean soil with low acidity.",False,"정답 ▶ F\n이유: 산성도가 높거나 중금속이 많은 흙에서도 빠르게 자라요.\n어휘 ▶ low ↔ high · only ✗ → even","even in soil with a high acidity level"],
 ["Research on using willow trees to clean soil has been completed.",False,"정답 ▶ F\n이유: 연구는 아직 진행 중(in development)이에요.\n어휘 ▶ completed 완료된 ↔ in development","is in development"],
 ["All species of willow trees absorb harmful materials equally well.",False,"정답 ▶ F\n이유: 어떤 종은 다른 종보다 해로운 물질을 더 잘 흡수해요.\n어휘 ▶ equally well 똑같이 잘 ↔ better than others","some species of willow trees are able to absorb harmful materials better than others"],
 ["The writer thinks further study is needed to identify the most effective trees.",True,"정답 ▶ T\n이유: 어떤 나무가 가장 효과적인지 알아내려면 더 탐구해야 한다고 했어요.\n어휘 ▶ identify 찾아내다 = find out · further study = further explored","should be further explored to find out which trees are the most effective"]]]
MC=[
 dict(n=N,box=[N],q="본문 ❸의 내용과 <u>일치하는</u> 것은?",opts=[
  "Willow trees can thrive even in soil that contains many heavy metals.",
  "Soil pollution is a problem found in only a few countries.",
  "Transporting polluted soil to landfills is an inexpensive option.",
  "Willow trees have shallow and poorly developed roots.",
  "Scientists have confirmed that all willow species work equally well."],
  ex="정답 ▶ Willow trees can thrive even in soil that contains many heavy metals.\n이유: They can also grow quickly, even in soil with ~ a lot of heavy metals in it.\n오답 ▶ ② across the globe(전 세계에서) ③ inexpensive ↔ expensive ④ shallow, poorly developed ↔ extensive, well-developed ⑤ 어떤 종이 다른 종보다 더 잘 흡수함\n포인트 ▶ thrive 잘 자라다, 번성하다 ≒ grow quickly · contain 포함하다",
  per=[["버드나무는 중금속이 많은 흙에서도 잘 자랄 수 있다.","a lot of heavy metals in it","thrive ≒ grow quickly ✔"],
       ["토양 오염은 몇몇 나라에서만 발견되는 문제이다.","across the globe","only a few countries ✗ → 전 세계"],
       ["오염된 흙을 매립지로 옮기는 것은 저렴한 방법이다.","this process is expensive","inexpensive ↔ expensive"],
       ["버드나무는 얕고 덜 발달된 뿌리를 가지고 있다.","extensive and well-developed root systems","shallow 얕은 ↔ extensive"],
       ["과학자들은 모든 버드나무 종이 똑같이 효과적이라고 확인했다.","better than others","equally ✗"]]),
 dict(n=N,box=[N],q="본문 ❸의 내용과 일치하지 <u>않는</u> 것은?",opts=[
  "Willow trees remove harmful substances from soil only with human help.",
  "Simply relocating polluted soil just shifts the problem elsewhere.",
  "Planting willows is both environmentally friendly and economical.",
  "Studies on how well willows clean soil are still underway.",
  "The writer hopes that willows may eventually help clean up our land."],
  ex="정답 ▶ Willow trees remove harmful substances from soil only with human help.\n이유: they naturally extract a wide range of harmful materials from the soil. 사람 도움 없이 '자연적으로(naturally)' 뽑아내요.\n오답 ▶ 나머지는 모두 본문을 다른 어휘로 바꿔 쓴 일치 문장\n포인트 ▶ remove = extract · substance = material · relocate = move · elsewhere = to another area · economical = cost-effective · underway = in development · eventually ≒ in time",
  per=[["버드나무는 사람의 도움이 있어야만 흙에서 해로운 물질을 제거한다.","they naturally extract","only with human help ✗ → naturally"],
       ["오염된 흙을 옮기기만 하는 것은 문제를 다른 곳으로 옮길 뿐이다.","it only moves the problem to another area","relocate = move · shift elsewhere = move to another area"],
       ["버드나무 심기는 친환경적이면서 경제적이다.","an eco-friendly and cost-effective way","economical ≒ cost-effective"],
       ["버드나무가 얼마나 흙을 잘 정화하는지에 대한 연구는 아직 진행 중이다.","is in development","underway 진행 중인 = in development"],
       ["필자는 버드나무가 결국 우리 땅을 정화하는 데 도움이 되기를 바란다.","In time, we may be able to clean up our land with willow trees","eventually ≒ in time"]]),
 dict(n=N,box=[N],q="본문 ❸의 내용과 <u>일치하는</u> 것은?",opts=[
  "버드나무는 산성도가 높은 흙에서도 빠르게 자랄 수 있다.",
  "오염된 흙을 파서 매립지로 옮기면 문제가 근본적으로 해결된다.",
  "버드나무를 심는 방법은 친환경적이지만 비용이 많이 든다.",
  "버드나무는 한 가지 해로운 물질만 흡수할 수 있다.",
  "가장 효과적인 버드나무 종은 이미 밝혀졌다."],
  ex="정답 ▶ 버드나무는 산성도가 높은 흙에서도 빠르게 자랄 수 있다.\n이유: They can also grow quickly, even in soil with a high acidity level\n오답 ▶ ② does not really solve it(실제로 해결하지 못함) ③ cost-effective(비용 효율적) ④ a wide range of(매우 다양한) ⑤ 어떤 나무가 가장 효과적인지 더 탐구해야 함\n포인트 ▶ acidity 산성도 · a wide range of 다양한",
  per=[["","even in soil with a high acidity level","일치 ✔"],
       ["","does not really solve it","해결하지 못함"],
       ["","eco-friendly and cost-effective","비용 효율적"],
       ["","a wide range of harmful materials","다양한 물질"],
       ["","to find out which trees are the most effective","아직 찾는 중"]])]
PICK2=[
 {"s":"Mining and other industries {are|is} causing soil pollution across the globe.","ex":"정답 ▶ are\n이유: 주어 Mining and other industries(A and B) → 복수"},
 {"s":"Although polluted soil can be {dug|digging} up and transported to a landfill, this process is expensive.","ex":"정답 ▶ dug\n이유: 흙이 '파내지는' 수동 → can be + p.p. (dig - dug - dug)"},
 {"s":"{Although|Despite} polluted soil can be dug up and transported to a landfill, this process is expensive.","ex":"정답 ▶ Although\n이유: 뒤에 주어+동사(polluted soil can be ~) → 접속사 Although. Despite는 전치사라 뒤에 명사(구)"},
 {"s":"Moreover, it only moves the problem to another area and {does|do} not really solve it.","ex":"정답 ▶ does\n이유: 주어 it(단수), moves와 병렬 → does not"},
 {"s":"Fortunately, there is an eco-friendly and cost-effective way {to restore|restoring} polluted soil — planting willow trees.","ex":"정답 ▶ to restore\n이유: a way to do ~하는 방법 (to부정사가 way를 꾸밈). restoring을 쓰려면 a way of restoring"},
 {"s":"Fortunately, there is an eco-friendly and cost-effective way to restore polluted soil — {planting|planted} willow trees.","ex":"정답 ▶ planting\n이유: 대시(—) 뒤는 앞의 a way를 구체적으로 설명하는 말 → 동명사 '심는 것'"},
 {"s":"As a result, they {naturally|natural} extract a wide range of harmful materials from the soil.","ex":"정답 ▶ naturally\n이유: 동사 extract를 꾸미는 부사 자리"},
 {"s":"They can also grow {quickly|quick}, even in soil with a high acidity level or a lot of heavy metals in it.","ex":"정답 ▶ quickly\n이유: 동사 grow를 꾸미는 부사 (grow + 형용사는 '~해지다'라는 뜻이라 여기선 어색)"},
 {"s":"Research on the effectiveness of using willow trees for this purpose {is|are} in development.","ex":"정답 ▶ is\n이유: 주어 Research(셀 수 없는 명사, 단수). on ~ purpose는 수식어\n포인트 ▶ trees(복수)에 속지 말기!"},
 {"s":"Scientists have found that some species of willow trees are able {to absorb|absorbing} harmful materials better than others.","ex":"정답 ▶ to absorb\n이유: be able to + 동사원형"},
 {"s":"Therefore, this promising area should be further {explored|exploring} to find out which trees are the most effective.","ex":"정답 ▶ explored\n이유: 분야가 '탐구되는' 수동 → should be + p.p."}]
VERB=[
 {"s":"Mining and other industries are ___ soil pollution across the globe.","v":"cause","a":["causing"],"ex":"정답 ▶ causing\n이유: are + -ing 현재진행형"},
 {"s":"Although polluted soil can be dug up and ___ to a landfill, this process is expensive.","v":"transport","a":["transported"],"ex":"정답 ▶ transported\n이유: can be dug up and (be) transported — 수동태 병렬"},
 {"s":"Fortunately, there is an eco-friendly and cost-effective way to restore ___ soil — planting willow trees.","v":"pollute","a":["polluted"],"ex":"정답 ▶ polluted\n이유: 흙이 '오염된' 상태(수동) → 과거분사가 명사 soil 수식"},
 {"s":"These amazing trees have extensive and well-___ root systems.","v":"develop","a":["developed"],"ex":"정답 ▶ developed\n이유: 뿌리가 '잘 발달된' 수동 → well-developed"},
 {"s":"Research on the effectiveness of ___ willow trees for this purpose is in development.","v":"use","a":["using"],"ex":"정답 ▶ using\n이유: 전치사 of 뒤 → 동명사"},
 {"s":"Scientists have ___ that some species of willow trees are able to absorb harmful materials better than others.","v":"find","a":["found"],"ex":"정답 ▶ found\n이유: have + p.p. 현재완료 (find - found - found)"},
 {"s":"Therefore, this promising area should be further ___ to find out which trees are the most effective.","v":"explore","a":["explored"],"ex":"정답 ▶ explored\n이유: should be + p.p. 조동사 수동태"},
 {"s":"In time, we may be able ___ up our land with willow trees.","v":"clean","a":["to clean"],"ex":"정답 ▶ to clean\n이유: be able to + 동사원형"}]
ERR=[
 {"s":"Mining and other industries [[is]] causing soil pollution across the globe. Although polluted soil can be [[dug]] up and [[transported]] to a landfill, this process is expensive.","w":0,"fix":"are","ex":"틀린 곳 ▶ ① is → are\n이유: 주어 Mining and other industries(복수)\n나머지 ▶ ② ③ can be dug up and (be) transported 수동 ✔"},
 {"s":"Moreover, it only [[moves]] the problem to another area and [[do]] not really [[solve]] it.","w":1,"fix":"does","ex":"틀린 곳 ▶ ② do → does\n이유: 주어 it(3인칭 단수)\n나머지 ▶ ① moves ✔ ③ does not + 동사원형 ✔"},
 {"s":"Fortunately, there is an eco-friendly and cost-effective way [[restoring]] polluted soil — [[planting]] willow trees. These [[amazing]] trees have extensive and well-developed root systems.","w":0,"fix":"to restore","ex":"틀린 곳 ▶ ① restoring → to restore\n이유: a way to do ~하는 방법\n나머지 ▶ ② 동명사 '심는 것' ✔ ③ 놀라움을 주는 → amazing ✔"},
 {"s":"As a result, they [[natural]] extract a wide range of [[harmful]] materials from the soil. They can also grow [[quickly]], even in soil with a high acidity level or a lot of heavy metals in it.","w":0,"fix":"naturally","ex":"틀린 곳 ▶ ① natural → naturally\n이유: 동사 extract를 꾸미는 부사\n나머지 ▶ ② 명사 수식 형용사 ✔ ③ 동사 grow 수식 부사 ✔"},
 {"s":"Research on the effectiveness of [[using]] willow trees for this purpose [[are]] in development. Scientists [[have found]] that some species of willow trees are able to absorb harmful materials better than others.","w":1,"fix":"is","ex":"틀린 곳 ▶ ② are → is\n이유: 주어 Research(단수)\n나머지 ▶ ① 전치사 of + 동명사 ✔ ③ 현재완료 ✔"},
 {"s":"Therefore, this promising area should be further [[exploring]] to find out which trees are [[the most effective]]. In time, we may be able [[to clean up]] our land with willow trees.","w":0,"fix":"explored","ex":"틀린 곳 ▶ ① exploring → explored\n이유: 분야가 '탐구되는' 수동 → should be p.p.\n나머지 ▶ ② 최상급 ✔ ③ be able to ✔"}]
SCR=["C3","C4","C6","C7","C9","C11"]
ORDER=[
 (["C1","C2","C3","C4"],["광업 등 산업이 토양 오염을 일으킴","오염된 흙을 파서 옮길 수 있지만 비쌈","게다가(Moreover) 문제를 옮길 뿐 해결 못 함","다행히(Fortunately) 버드나무 심기라는 방법이 있음"]),
 (["C5","C6","C7","C8"],["버드나무는 넓고 잘 발달된 뿌리를 가짐","결과적으로 다양한 해로운 물질을 뽑아냄","또한 산성·중금속 흙에서도 빨리 자람","이 목적의 효과에 대한 연구가 진행 중"]),
 (["C8","C9","C10","C11"],["연구가 진행 중","어떤 종이 다른 종보다 더 잘 흡수함을 발견","그러므로 가장 효과적인 나무를 찾도록 더 탐구해야","머지않아 버드나무로 땅을 정화할 수 있을지도"])]
INSERT=[
 (["C2","C3","C4","C5"],1,["파서 옮길 수 있지만 비쌈","게다가(Moreover) 문제를 옮길 뿐 해결 못 함","다행히(Fortunately) 버드나무","놀라운 나무의 뿌리"],"정답 ▶ ①\n이유: Moreover(게다가)는 앞의 단점(비싸다)에 단점을 하나 더 보태요. 그리고 Fortunately(다행히)로 해결책이 나오기 전에 단점이 다 나와야 해요."),
 (["C4","C5","C6","C7"],2,["버드나무 심기","넓고 잘 발달된 뿌리","결과적으로(As a result) 해로운 물질을 뽑아냄","또한(also) 거친 흙에서도 빨리 자람"],"정답 ▶ ②\n이유: As a result(결과적으로)의 원인은 '뿌리가 넓고 잘 발달됨'이에요. 뿌리 문장 바로 뒤!"),
 (["C8","C9","C10","C11"],2,["연구가 진행 중","어떤 종이 더 잘 흡수함","그러므로(Therefore) 가장 효과적인 나무를 찾도록 더 탐구","머지않아 땅을 정화할 수 있을지도"],"정답 ▶ ②\n이유: '종마다 흡수 능력이 다르다' → 그러므로 '어떤 나무가 가장 효과적인지' 더 탐구해야 해요.")]
ODD=[
 (["C4","C5","Willow wood has long been used to make baskets and furniture.","C6"],2,"정답 ▶ ③\n이유: 글은 버드나무의 뿌리가 흙 속 해로운 물질을 뽑아낸다는 흐름이에요. 바구니·가구를 만드는 목재 이야기는 관계없어요."),
 (["C8","C9","However, scientists agree that willows cannot absorb heavy metals at all.","C10"],2,"정답 ▶ ③\n이유: 앞에서 버드나무가 해로운 물질을 흡수한다고 했고, 다음 문장은 '가장 효과적인 나무를 찾자'예요. 전혀 흡수하지 못한다는 문장은 앞뒤와 모순이에요.")]
BLANK=[
 {"s":"Moreover, it only moves the problem to another area and does not really ____ it.","opts":["solve","cause","notice","describe"],"ex":"정답 ▶ solve (해결하다)\n이유: only moves(옮길 뿐) → 진짜로 '해결하지는' 못해요.\n오답 ▶ cause 일으키다 · notice 알아차리다 · describe 묘사하다"},
 {"s":"Fortunately, there is an eco-friendly and ____ way to restore polluted soil — planting willow trees.","opts":["cost-effective","time-consuming","expensive","dangerous"],"ex":"정답 ▶ cost-effective (비용 효율적인)\n이유: 앞에서 흙을 옮기는 건 비싸다(expensive)고 했어요. Fortunately로 그 단점을 해결 → 비용이 적게 드는 방법\n오답 ▶ time-consuming 시간이 많이 드는 · expensive 비싼 · dangerous 위험한"},
 {"s":"As a result, they naturally ____ a wide range of harmful materials from the soil.","opts":["extract","add","hide","spread"],"ex":"정답 ▶ extract (뽑아내다)\n이유: 잘 발달된 뿌리 → 흙'에서(from)' 해로운 물질을 뽑아내요.\n오답 ▶ add 더하다 · hide 숨기다 · spread 퍼뜨리다"},
 {"s":"Therefore, this ____ area should be further explored to find out which trees are the most effective.","opts":["promising","useless","finished","forbidden"],"ex":"정답 ▶ promising (유망한)\n이유: 더 탐구할 가치가 있다 → 가능성이 큰 분야\n오답 ▶ useless 쓸모없는 · finished 끝난 · forbidden 금지된"}]
GRAM=[
 {"q":"빈칸에 알맞은 것은?<br><b>______ polluted soil can be moved, this process is expensive.</b>","opts":["Although","Despite","Because of","However"],"ex":"정답 ▶ Although (~이긴 하지만)\n이유: 뒤에 주어+동사 → 접속사. Despite·Because of는 전치사, However는 부사라 두 절을 잇지 못해요.\n본문 ▶ Although polluted soil can be dug up and transported"},
 {"q":"빈칸에 알맞은 것은?<br><b>Polluted soil can ______ up and moved to a landfill.</b>","opts":["be dug","dig","be digging","dug"],"ex":"정답 ▶ be dug\n이유: 흙이 '파내지는' 수동 → 조동사 + be + p.p. (dig - dug - dug)"},
 {"q":"밑줄 친 <b>to restore</b>와 쓰임이 같은 것은?<br><b>There is a way <u>to restore</u> polluted soil.</b>","opts":["I have no time to waste.","I went there to meet her.","To learn English is fun.","She was happy to see me."],"ex":"정답 ▶ I have no time to waste.\n이유: 본문의 to restore는 명사 a way를 꾸미는 형용사적 용법(~할). time to waste(낭비할 시간)도 같아요.\n오답 ▶ ② 목적(~하기 위해) ③ 주어(명사적) ④ 감정의 원인"},
 {"q":"빈칸에 알맞은 것은?<br><b>Some willows are able ______ harmful materials better than others.</b>","opts":["to absorb","absorbing","absorb","absorbed"],"ex":"정답 ▶ to absorb\n이유: be able to + 동사원형"},
 {"q":"다음 중 어법상 알맞은 것은?","opts":["I want to know which tree is the most effective.","I want to know which tree the most effective is.","I want to know which is tree the most effective.","I want to know which tree is effectivest."],"ex":"정답 ▶ I want to know which tree is the most effective.\n이유: 간접의문문(의문사 + 주어 + 동사). which tree가 주어 자리라 바로 is가 와요. effective의 최상급은 the most effective\n본문 ▶ to find out which trees are the most effective"},
 {"q":"빈칸에 알맞은 것은?<br><b>This promising area should be further ______.</b>","opts":["explored","exploring","explore","to explore"],"ex":"정답 ▶ explored\n이유: 분야가 '탐구되는' 수동 → should be + p.p."},
 {"q":"빈칸에 알맞은 것은?<br><b>Planting willows is the ______ effective way of all.</b>","opts":["most","more","much","very"],"ex":"정답 ▶ most\n이유: the + most + 형용사 + of all 모든 것 중에서 가장 ~한 (최상급)"}]
