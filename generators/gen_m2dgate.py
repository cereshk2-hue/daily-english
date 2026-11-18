# 11/18 중산중2 동아(윤정미) 7·8과 '어법 선택 한 판' DAY 2개 (맨 끝, 7 → 8) — 선생님 자료: 각 과 워크북 6 어법 선택형 연습 hwp (이그잼포유)
# 과마다 두 덩이 = 본문 DAY 두 개(7과 d1/d2, 8과 d3/d4). {정답|오답} — 앱이 보기 순서를 섞음. gen_m1dgate.py 복사
import sys, json, re, subprocess
sys.path.insert(0, '/home/claude/srcrepo/generators')
from gencommon import write
path = sys.argv[1] if len(sys.argv) > 1 else '/home/claude/proj/data/m2-donga-yoon-L7.js'
PK = json.loads(subprocess.check_output(['node', '-e', "global.window={};require('%s');process.stdout.write(JSON.stringify(window.PKG))" % path]))
L7 = [
 ('People in Valencia {celebrate|celebrates} the coming of spring with the Fallas festival.', '발렌시아 사람들은 파야스 축제로 봄의 시작을 축하한다.', "주어 People(복수) — in Valencia는 수식어 → celebrate"),
 ('This festival takes place from March 15 to 19. {During|While} the festival, people enjoy parades and fireworks.', '이 축제는 3월 15일부터 19일까지 열린다. 축제 기간 동안 사람들은 퍼레이드와 불꽃놀이를 즐긴다.', "뒤에 명사(the festival) → 전치사 During (While은 접속사라 뒤에 주어 + 동사)"),
 ('The stars of the festival {are|is} fallas, giant wooden statues.', '축제의 주인공은 거대한 나무 조각상인 파야들이다.', "주어 The stars(복수) — of the festival은 수식어 → are"),
 ('You can find hundreds of {them|it} all over the city.', '도시 곳곳에서 수백 개의 파야들을 볼 수 있다.', "가리키는 것이 fallas(복수) → them"),
 ('Surprisingly, the fallas are {burned|burn} on the last day of the festival.', '놀랍게도, 축제의 마지막 날에는 이 파야들이 불태워진다.', "파야들이 '태워지는' 수동 → be + 과거분사 burned"),
 ('Burning them {symbolizes|symbolize} saying goodbye to old things and hello to a new start.', '그것들을 태우는 것은 오래된 것들과 작별하고 새로운 시작을 맞이하는 것을 상징한다.', "동명사 주어(Burning them)는 단수 → symbolizes"),
 ('Winter in Sweden {is|are} long and dark, so the people there especially {welcome|welcomes} summer.', '스웨덴의 겨울은 길고 어두워서 그곳 사람들은 여름을 특히 환영한다.', "주어 Winter(단수) → is / 주어 the people(복수) → welcome"),
 ('{To celebrate|Celebrate} the longest day of the year, they have a special festival. They call {it the Midsummer festival|the Midsummer festival it}.', '일 년 중 낮이 가장 긴 날을 기념하기 위해 그들은 특별한 축제를 연다. 이 축제를 한여름 축제라고 부른다.', "'~하기 위해'(목적) → To celebrate / call + 목적어(it) + 목적격보어(the Midsummer festival) 순서"),
 ('The festival starts on the Friday evening between June 19 and 25 and {ends|end} on the Sunday.', '축제는 6월 19일과 25일 사이의 금요일 저녁에 시작하여 일요일에 끝난다.', "starts와 and로 나란히, 주어 The festival(단수) → ends"),
 ('{During|While} the festival, people decorate a tall pole with flowers and green leaves and {enjoy|enjoys} traditional dances around it.', '축제 기간 동안 사람들은 꽃과 초록색 잎으로 장대를 장식하고 그 주위를 돌며 전통 춤을 즐긴다.', "뒤에 명사 → 전치사 During / 주어 people(복수), decorate와 나란히 → enjoy"),
 ('{Because|Because of} the sun hardly sets at this time of year in Sweden, people can {enjoy|enjoyed} the festival all night long.', '스웨덴에서 매년 이맘때면 해가 거의 지지 않기 때문에 사람들은 밤새도록 축제를 즐길 수 있다.', "뒤에 주어 + 동사(the sun hardly sets) → 접속사 Because (Because of + 명사) / can + 동사원형 → enjoy"),
 ('Many Mexicans believe {that|what} once a year dead people come back home {to meet|meet} their family and friends.', '많은 멕시코 사람들은 일 년에 한 번 죽은 사람들이 가족과 친구들을 만나기 위해 집으로 돌아온다고 믿는다.', "believe의 목적어, 뒤가 완전한 절 → 접속사 that / '~하기 위해'(목적) → to meet"),
 ('They call {this day the Day of the Dead|the Day of the Dead this day}. {To welcome|Welcome} dead people, Mexicans hold a festival on November 1 and 2.', '이날을 망자의 날이라고 부른다. 죽은 이들을 맞이하기 위해, 멕시코 사람들은 11월 1일과 2일에 축제를 연다.', "call + 목적어(this day) + 목적격보어(the Day of the Dead) / '~하기 위해' → To welcome"),
 ('They believe it is important {to remember|remember} dead people.', '그들은 고인을 기억하는 것이 중요하다고 믿는다.', "가주어 it — 진주어 to부정사 → to remember"),
 ('So, people set up altars in their homes and {have|has} big parties in cemeteries.', '그래서 사람들은 집에 제단을 차리고, 묘지에서 큰 파티를 연다.', "주어 people(복수), set up과 나란히 → have"),
 ('In some areas, people dress up like skeletons and {hold|holding} big parades.', '일부 지역에서는 사람들이 해골처럼 분장하고 대규모 퍼레이드를 벌인다.', "dress up과 and로 나란히(동사) → hold"),
 ('At the end of February, people in Alaska hold the Fur Rondy festival, one of the biggest winter {festivals|festival} in the world.', '2월 말, 알래스카 사람들은 세계에서 가장 큰 겨울 축제 중 하나인 퍼 론디 축제를 연다.', "one of the + 최상급 + 복수 명사 → festivals"),
 ('During this festival, visitors can {enjoy|enjoyed} various winter sports and Alaskan traditional games.', '이 축제 기간 동안 방문객들은 다양한 겨울 스포츠와 알래스카 전통 게임을 즐길 수 있다.', "can + 동사원형 → enjoy"),
 ('They can also enjoy many special {events|event} such as the Running of the Reindeer.', '또한, 순록 경주 같은 많은 특별한 행사도 즐길 수 있다.', "many + 복수 명사 → events"),
 ('People {who|which} {participate|participates} in this race wear fun costumes and {try|tries} to run {faster|fastest} than reindeer.', '이 경주에 참가하는 사람들은 재미있는 복장을 입고 순록보다 더 빨리 달리려고 애쓴다.', "선행사 People(사람) → who / 선행사 People(복수) → participate / 주어 People, wear와 나란히 → try / than이 있으면 비교급 → faster"),
 ('Is it possible to {do|doing} so? Not really, but it doesn’t matter. Everyone {is|are} just {having|have} fun!', '과연 그럴 수 있을까? 그럴 거 같지는 않지만, 그것은 중요하지 않다. 모두가 그저 즐기고 있을 뿐이다!', "to + 동사원형 → do (가주어 it — 진주어 to부정사) / Everyone은 단수 취급 → is / 현재진행형 is + -ing → having"),
]
L8 = [
 ('Eckels walked into the office of Time Travel. The big sign on the wall {said|saying}, “NAME ANY YEAR IN THE PAST. WE TAKE YOU THERE.”', 'Eckels는 Time Travel의 사무실로 걸어 들어갔다. 벽에 걸린 큰 간판에는 “과거의 어느 연도든 말씀하세요. 우리가 당신을 그곳으로 모시겠습니다.”라고 쓰여 있었다.', "주어 The big sign 뒤 동사 자리(과거) → said ('~라고 쓰여 있다'의 say)"),
 ('There {was|were} a TV on the wall, and Mr. Keith, the new president, {was|were} on the news.', '벽에는 TV가 있었고, 새 대통령인 Keith 씨가 뉴스에 나오고 있었다.', "There + be + 단수(a TV) → was / 주어 Mr. Keith(단수) — 콤마 사이는 설명 → was"),
 ('“How can we help you?” {said|saying} Mr. Parker, the founder of Time Travel.', '“무엇을 도와드릴까요?” Time Travel의 설립자인 Parker 씨가 말했다.', "인용문 뒤 동사 + 주어 어순(said Mr. Parker), 과거 → said"),
 ('“I’ve always {wanted|wanting} {to see|seeing} a dinosaur. {Is|Does} it possible?” asked Eckels.', '“저는 항상 공룡을 보고 싶었어요. 가능한가요?” Eckels가 물었다.', "현재완료 have + 과거분사 → wanted / want + to부정사 → to see / 형용사 possible이 보어 → be동사 의문문 Is"),
 ('“Sure,” said Mr. Parker. “We can take you back to the jungle of 60 million {years|year} ago.”', '“물론이죠.” Parker 씨가 대답했다. “당신을 6천만 년 전의 정글로 데려다줄 수 있습니다.”', "60 million(6천만) + 복수 명사 → years"),
 ('“Great,” said Eckels. “Can you take me there now?” “You’re lucky. There’s a time machine {that|who} {leaves|leave} in 10 minutes,” said Mr. Parker.', '“멋지군요.” Eckels가 말했다. “지금 저를 그곳에 데려가 줄 수 있나요?” “운이 좋으시네요. 10분 후에 출발하는 타임머신이 있습니다.” Parker 씨가 말했다.', "선행사 a time machine(사물) → that (who는 사람) / 선행사 단수 → leaves"),
 ('“This is Travis, your travel guide,” he continued. “To stay {safe|safely}, you must follow his instructions.”', '“이분은 당신의 여행 안내원인 Travis입니다.” 그는 계속 말했다. “안전하려면 그의 지시를 반드시 따라야 합니다.”', "stay + 형용사 보어(~한 상태로 있다) → safe"),
 ('Inside the time machine, there {were|was} two {other|another} travelers. Eckels sat down and {closed|close} his eyes.', '타임머신 안에는 다른 여행자 두 명이 있었다. Eckels는 자리에 앉아 눈을 감았다.', "there + be + 복수(two travelers) → were / 복수 명사 앞 → other (another + 단수) / sat과 나란히(과거) → closed"),
 ('He felt the machine {moving|to move} under his feet. After only a few minutes, the machine stopped.', '그는 발밑에서 타임머신이 움직이는 것을 느꼈다. 불과 몇 분 지나지 않아 타임머신이 멈췄다.', "지각동사 feel + 목적어 + -ing(또는 동사원형) → moving (to부정사는 안 됨)"),
 ('“We’ve just {arrived|arriving} in the jungle of 60 million years ago,” Travis explained.', '“우리는 이제 막 6천만 년 전 정글에 도착했습니다.” Travis가 설명했다.', "현재완료 have just + 과거분사 → arrived"),
 ('“{Do|Are} you see the path over there? You must not leave it at any time. Do not touch anything. You might kill something by accident. A little change here can cause {something unthinkable|unthinkable something} in the future.”', '“저쪽에 길이 보이십니까? 어떤 경우에도 저 길을 절대 벗어나면 안 됩니다. 아무것도 만지지 마세요. 여러분이 실수로 무언가를 죽일 수도 있습니다. 이곳에서의 작은 변화가 미래에 상상할 수 없는 일을 초래할 수 있습니다.”', "일반동사 see의 의문문 → Do / -thing + 형용사 어순 → something unthinkable"),
 ('Slowly, everyone got out of the time machine. The jungle was {covered|cover} in fog. It was very {quiet|quietly}.', '모두 타임머신에서 천천히 내렸다. 정글은 안개로 뒤덮여 있었다. 그곳은 무척 고요했다.', "정글이 '뒤덮인' 수동 → was covered / be동사 보어 → 형용사 quiet"),
 ('“I’m so {excited|exciting},” said Eckels. “Be careful. Some of the dinosaurs {are|is} hungry,” said Travis.', '“정말 신나요.” Eckels가 말했다. “조심하세요. 몇몇 공룡들은 배가 고파요.” Travis가 말했다.', "사람이 '신이 난' 감정 → excited / Some of + 복수 명사(the dinosaurs) → are"),
 ('“Just stay {calm|calmly}. I don’t want you {to do|doing} {anything foolish|foolish anything}.” “Don’t worry. I’m not a fool,” said Eckels. They all began to walk on the path.', '“침착하세요. 당신이 어리석은 어떤 행동도 하지 않기를 바랍니다.” “걱정하지 마세요. 저는 바보가 아니에요.” Eckels가 말했다. 그들은 모두 길을 걷기 시작했다.', "stay + 형용사 보어 → calm / want + 목적어 + to부정사 → to do / -thing + 형용사 → anything foolish"),
 ('After some time, Travis whispered, “Look over there. There {is|are} a T. rex.”', '얼마 후, Travis가 속삭였다. “저기 봐요. 티라노사우루스가 있어요.”', "There + be + 단수(a T. rex) → is"),
 ('One hundred meters away, a T. rex slowly {appeared|appearing}. “It,” whispered Eckels. “It ...” “Sh!”', '100미터 떨어진 곳에서 티라노사우루스가 서서히 나타났다. “저것은,” Eckels가 속삭였다. “저것은 …” “쉿!”', "주어 a T. rex 뒤 동사 자리(과거) → appeared"),
 ('“It ... is huge. I’ve never {seen|saw} such a huge thing. I’m so {scared|scaring},” said Eckels.', '“저건 … 거대해요. 저렇게 거대한 것을 본 적이 없어요. 너무 무서워요.” Eckels가 말했다.', "현재완료 have never + 과거분사 → seen / 사람이 '겁먹은' 감정 → scared"),
 ('“Sh ... quiet!” Travis said angrily. “You don’t want it {to see|seeing} you.”', '“쉿 … 조용히!” Travis가 화를 내며 말했다. “공룡이 당신을 보길 원하는 건 아니겠죠.”', "want + 목적어 + to부정사 → to see"),
 ('“I can’t breathe,” said Eckels. “Get {me out of|out of me} here!” “Don’t panic, Eckels,” said Travis.', '“숨을 쉴 수가 없어요.” Eckels가 말했다. “여기서 나가게 해 줘요!” “겁먹지 마세요, Eckels.” Travis가 말했다.', "get + 목적어(me) + out of + 장소 → Get me out of here"),
 ('“Turn around, and walk quietly back to the machine.” Eckels turned around and {started|start} to run.', '“뒤로 돌아서 조용히 타임머신으로 돌아가세요.” Eckels는 돌아서서 뛰기 시작했다.', "turned와 and로 나란히(과거) → started"),
 ('He was so {terrified|terrifying} {that|what} he left the path by accident. “Eckels!” shouted Travis. “Don’t leave the path!”', '그는 너무 겁에 질려 실수로 길을 벗어나고 말았다. “Eckels!” Travis가 외쳤다. “길을 벗어나지 말아요!”', "사람이 '겁에 질린' 감정 → terrified / so + 형용사 + that ~ (너무 ~해서 …하다) → that"),
 ('The T. rex heard Travis and {turned|turn} its head toward him and the {other|another} travelers.', '티라노사우루스가 Travis의 소리를 듣고 그와 다른 여행자들을 향해 고개를 돌렸다.', "heard와 나란히(과거) → turned / the + 복수 명사 앞 → other"),
 ('There {was|were} a moment of silence. Then, it suddenly started to run toward them with a loud roar. “Run, everybody! Run!” shouted Travis.', '잠시 정적이 흘렀다. 그리고 갑자기 티라노사우루스가 큰 포효와 함께 그들을 향해 달려오기 시작했다. “모두 뛰어요! 뛰어!” Travis가 외쳤다.', "There + be + 단수(a moment) → was"),
 ('Travis and the other travelers returned safely {to the machine|the machine} and {found|find} Eckels inside.', 'Travis와 다른 여행자들은 안전하게 타임머신으로 돌아와서 안에 있는 Eckels를 발견했다.', "return은 '~로 돌아오다'일 때 to와 함께 → to the machine / returned와 나란히(과거) → found"),
 ('“You put all of us in danger,” said Travis to Eckels in an {angry|angrily} voice. “You left the path.”', '“당신이 우리 모두를 위험에 빠뜨렸어요.” Travis가 화난 목소리로 Eckels에게 말했다. “당신이 길을 벗어났잖아요.”', "명사 voice를 꾸미는 말 → 형용사 angry"),
 ('“I’m sorry, but I didn’t kill anything,” said Eckels. “There’s only a {little|few} mud on my shoes.”', '“미안해요, 그렇지만 난 어떤 것도 죽이지 않았어요.” Eckels가 말했다. “신발에 진흙이 조금 묻었을 뿐이에요.”', "mud는 셀 수 없는 명사 → a little (a few + 셀 수 있는 복수)"),
 ('Travis stared at Eckels for a long time without {saying|say} anything. “Let’s go home,” said Travis finally.', 'Travis는 아무 말 없이 Eckels를 오랫동안 응시했다. “집으로 갑시다.” 마침내 Travis가 말했다.', "전치사 without 뒤 동명사 → saying"),
 ('The machine stopped. They all {returned to|returned} the present safely.', '타임머신이 멈췄다. 그들은 모두 안전하게 현재로 돌아왔다.', "'~로 돌아오다'는 return to → returned to"),
 ('“{Is|Does} everything okay here?” asked Travis. “Fine. Welcome home!” said Mr. Parker.', '“이곳은 모든 것이 괜찮나요?” Travis가 물었다. “괜찮아요. 돌아오신 것을 환영합니다!” Parker 씨가 말했다.', "형용사 okay가 보어 → be동사 의문문, everything은 단수 → Is"),
 ('Eckels looked around the room carefully. Everything {looked|were looked} the same, except the big sign on the wall.', 'Eckels는 방을 주의 깊게 둘러보았다. 벽에 걸린 큰 간판만 빼고 모든 것이 똑같아 보였다.', "look(~해 보이다)은 수동태로 쓰지 않음, Everything 단수·과거 → looked"),
 ('The sign now said, “NAIM ANY YEER EN THE PAST. WEE TAEK YU THAIR.” Eckels was {confused|confusing}.', '간판에는 이제 이렇게 쓰여 있었다. “NAIM ANY YEER EN THE PAST. WEE TAEK YU THAIR.” Eckels는 혼란스러웠다.', "사람이 '혼란스러운' 감정 → confused"),
 ('Then, he saw the TV. The new president was on the news, but it was not Mr. Keith. “What’s going on?” He got more {confused|confusing}.', '그리고 그는 TV를 보았다. 뉴스에 새 대통령이 나오고 있었는데, Keith 씨가 아니었다. “이게 대체 무슨 일이지?” 그는 더욱 혼란스러워졌다.', "사람이 '혼란스러워진' 감정 → confused"),
 ('He sat down and {looked|looking} closely at the mud on his shoes.', '그는 앉아서 신발에 묻은 진흙을 유심히 살펴보았다.', "sat과 and로 나란히(과거) → looked"),
 ('“No, it can’t be,” said Eckels. “It’s all {because of|because} this little thing?”', '“안 돼, 이럴 리가 없어.” Eckels가 말했다. “이게 모두 이 작은 것 때문이라고?”', "뒤에 명사구(this little thing) → because of (because + 주어 + 동사)"),
 ('He was {shocked|shocking}. In the mud on his right shoe, he found a small dead butterfly.', '그는 충격을 받았다. 그는 자신의 오른쪽 신발에 묻은 진흙 속에서 죽어 있는 작은 나비 한 마리를 발견했다.', "사람이 '충격받은' 감정 → shocked"),
]
D = {d['id']: d for d in PK['days']}
norm = lambda s: re.sub(r'\s+', ' ', s.replace('’', "'").replace('‘', "'").replace('“', '"').replace('”', '"').replace('—', '-').replace('–', '-').replace('…', '...')).lower()
def build(gid, rng, S, k1, k2, t1, t2):
    TX = {k: norm(' '.join(l[1] for l in D[k]['passage'] if not re.match(r'^[❶-❿]$', l[1]) and l[0] != '#')) for k in (k1, k2)}
    G = {k1: [], k2: []}
    for s, ko, ex in S:
        full = norm(re.sub(r'\{([^|}]*)\|[^}]*\}', r'\1', s))
        where = [k for k in TX if full in TX[k]]; assert len(where) == 1, (full, where)
        for m in re.findall(r'\{([^}]*)\}', s): o = m.split('|'); assert len(o) == 2 and o[0] != o[1], s
        G[where[0]].append({'s': s, 'ko': ko, 'ex': ex})
    nb = {k: sum(len(re.findall(r'\{', p['s'])) for p in v) for k, v in G.items()}
    return {'id': gid, 'name': '', 'range': rng, 'story': rng + ' · 괄호를 모두 맞혀야 100점 (덩이 2개)',
            'passage': D[k1]['passage'] + D[k2]['passage'],
            'steps': [{'type': 'gate', 'title': '어법 선택 한 판', 'guide': "본문을 두 덩이로 나눴어요. 덩이마다 괄호를 모두 맞혀야 100점, 하나라도 틀리면 0점! 3번 안에 통과 못 하면 틀린 문장만 해설과 함께 연습하고 다시 도전해요.",
                       'items': [{'title': '%s (괄호 %d개)' % (t1, nb[k1]), 'parts': G[k1]}, {'title': '%s (괄호 %d개)' % (t2, nb[k2]), 'parts': G[k2]}]}]}, nb
g7, n7 = build('gt7', '7과 본문 · 어법 선택 한 판', L7, 'd1', 'd2', '본문 ❶❷ · 스페인 파야스 · 스웨덴 한여름', '본문 ❸❹ · 멕시코 망자의 날 · 알래스카 퍼 론디')
g8, n8 = build('gt8', '8과 본문 · 어법 선택 한 판', L8, 'd3', 'd4', '본문 ❶❷❸ · Time Travel 사무실 · 정글 도착', '본문 ❹❺❻ · 티라노사우루스 · 돌아온 현재')
PK['days'] = [d for d in PK['days'] if d['id'] not in ('gt7', 'gt8')] + [g7, g8]
for i, d in enumerate(PK['days']): d['name'] = 'DAY %d' % (i + 1)
src = open(path, encoding='utf-8').read(); head = src[:src.index('window.PKG')]
tail = src[src.index('/* WRAPUP-TESTS'):] if '/* WRAPUP-TESTS' in src else ''
if '한 판' not in head: head = head.rstrip('\n') + '\n/* 11/18: 7·8과 본문 어법 선택 한 판 DAY gt7·gt8 맨 끝 (generators/gen_m2dgate.py) */\n'
if tail: PK.pop('tests', None)
write(PK, path, head)
if tail: open(path, 'a', encoding='utf-8').write(tail)
print('괄호', n7, n8, '·', [d['name'] + ' ' + d['range'] for d in PK['days']][-2:])
