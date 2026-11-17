# 11/17 중산중1 동아(윤정미) 5·6·7과 '어법 선택 한 판' DAY 3개 (맨 끝, 단원 순서 6 → 7 → 5) — 선생님 자료: 각 과 워크북 6 어법 선택형 연습 hwp
# 과마다 두 덩이(선생님 지정) = 본문 DAY 두 개(6과 d1/d2, 7과 d3/d4, 5과 L5a/L5b). {정답|오답} — 앱이 보기 순서를 섞음
import sys, json, re, subprocess
sys.path.insert(0, '/home/claude/srcrepo/generators')
from gencommon import write
path = sys.argv[1] if len(sys.argv) > 1 else '/home/claude/proj/data/m1-donga-yoon-L6.js'
PK = json.loads(subprocess.check_output(['node', '-e', "global.window={};require('%s');process.stdout.write(JSON.stringify(window.PKG))" % path]))
L6 = [
 ("Every day, we produce lots of waste, and the Earth is {getting|get} sicker and sicker.", "매일 우리는 많은 쓰레기를 만들고, 지구는 점점 더 병들고 있습니다.", "현재진행형 is + -ing → getting"),
 ("Do you want {to save|saving} the Earth?", "여러분은 지구를 구하고 싶나요?", "want + to부정사 : ~하고 싶다 → to save"),
 ("Then, join the zero-waste challenge, and {share|sharing} your stories.", "그렇다면 제로 웨이스트 챌린지에 동참하고 여러분의 이야기를 공유해 주세요.", "명령문 join과 and로 나란히 → 동사원형 share"),
 ("My birthday {was|is} last Saturday, and my family and I {ate|eat} out.", "내 생일은 지난 토요일이었고, 가족들과 나는 외식을 했어.", "last Saturday(과거) → was / ate"),
 ("There {were|was} lots of leftovers, but we brought them home.", "남은 음식이 많아서 우리는 그것들을 집으로 가져왔어.", "There + be + 복수 명사(leftovers), 과거 → were"),
 ("The next day, I made a nice lunch out of {them|it}.", "그다음 날, 나는 그것들로 맛있는 점심을 만들었어.", "가리키는 말이 leftovers(복수) → them"),
 ("FYI, you can {find|found} great cooking ideas for leftovers on the Internet.", "참고로, 인터넷에서 남은 음식을 위한 멋진 요리 아이디어를 찾을 수 있어.", "조동사 can + 동사원형 → find"),
 ("My dog {tore|to tear} my bag.", "내 개가 내 가방을 찢었어.", "주어 My dog 뒤 동사(과거) → tore"),
 ("I wanted {to buy|buying} a new one, but I thought again.", "나는 새것을 사고 싶었지만, 다시 생각해 봤어.", "want + to부정사 → to buy"),
 ("I learned that {reusing|reuse} is important for zero-waste living.", "나는 재사용이 제로 웨이스트 생활에 중요하다고 배웠어.", "that절의 주어 자리 → 동명사 reusing"),
 ("So, I decided {to fix|fixing} it and reuse it.", "그래서 나는 그것을 수선해서 재사용하기로 결심했어.", "decide + to부정사 → to fix"),
 ("I'm not very good at {sewing|sew}, and I don't think that the bag looks {perfect|perfectly}.", "나는 바느질을 아주 잘하지 못하고, 가방이 완벽해 보인다고 생각하진 않아.", "전치사 at 뒤 → 동명사 sewing / look + 형용사 보어 → perfect"),
 ("I often use food delivery services, but today I {didn't|wasn't}.", "나는 종종 음식 배달 서비스를 이용하는데, 오늘은 이용하지 않았어.", "일반동사 use를 받는 부정 → didn't (use 생략)"),
 ("Instead, I walked to my favorite restaurant with a reusable container and {picked|picking} up the food.", "대신, 재사용할 수 있는 용기를 가지고 내가 가장 좋아하는 식당에 걸어가서 음식을 가져왔어.", "walked와 and로 나란히(과거) → picked"),
 ("I heard that plastic never {goes|go} away completely.", "플라스틱은 절대로 완전히 없어지지 않는다고 들었어.", "주어 plastic(단수), 현재 → goes"),
 ("I didn't {use|used} any single-use plastic today.", "나는 오늘 어떤 일회용 플라스틱도 사용하지 않았어.", "didn't + 동사원형 → use"),
 ("Yesterday, I {took|take} some plastic and glass bottles to a recycling machine near my house.", "어제 나는 플라스틱과 유리병 몇 개를 집 근처에 있는 재활용 기계에 가져갔어.", "Yesterday(과거) → took"),
 ("I put them into the machine one by one, and I {got|get} some points in return.", "나는 그것들을 하나씩 기계에 집어넣었고, 대가로 포인트를 받았어.", "과거 이야기(put = 과거) → got"),
 ("What can I {do|does} with those points?", "그 포인트로 무엇을 할 수 있냐고?", "조동사 can + 동사원형 → do"),
 ("Well, I can {use|used} them like money.", "음, 나는 그것들을 돈처럼 사용할 수 있어.", "can + 동사원형 → use"),
 ("Don't you {think|thought} that's cool?", "멋지다고 생각하지 않니?", "Don't + 주어 + 동사원형 → think"),
]
L7 = [
 ("It's a movie about the friendship between Tom {and|or} his dog Max.", "이것은 Tom과 그의 개 Max의 우정에 관한 영화예요.", "between A and B : A와 B 사이 → and"),
 ("A lot of people are {working|work} hard {to create|create} this movie.", "많은 사람들이 이 영화를 만들기 위해 열심히 일하고 있어요.", "현재진행형 are + -ing → working / '~하기 위해'(목적) → to create"),
 ("Do you want {to meet|meeting} some of them?", "그들 중 몇 명을 만나 보고 싶나요?", "want + to부정사 → to meet"),
 ("I'm a location manager, and my job is {to find|find} perfect places for shooting.", "나는 야외 촬영 관리자이고, 내 일은 촬영을 위한 완벽한 장소를 찾는 거예요.", "be동사 뒤 보어 '~하는 것' → to find"),
 ("Of course, it is not {easy|easily}, but I love my job.", "물론, 이 일은 쉽지 않지만, 나는 내 일을 정말 좋아해요.", "be동사 뒤 보어 → 형용사 easy"),
 ("I like to travel and {enjoy|enjoying} challenges.", "나는 여행하는 것을 좋아하고 도전을 즐겨요.", "주어 I의 동사 like와 and로 나란히 → enjoy"),
 ("I'm in charge of all the {cameras|camera}.", "나는 모든 카메라를 담당하고 있어요.", "all the + 복수 명사 → cameras"),
 ("Today, Tom and Max are going to {play|playing} together with a ball on the beach.", "오늘, Tom과 Max는 해변에서 공을 가지고 함께 놀 예정이에요.", "be going to + 동사원형 → play"),
 ("{To capture|Capture} their happy moments, I'm going to {use|using} drones.", "그들의 행복한 순간을 포착하기 위해, 나는 드론을 사용할 거예요.", "'~하기 위해'(목적) → To capture / be going to + 동사원형 → use"),
 ("I trained and {took|taking} care of Max for a long time.", "나는 Max를 오랫동안 훈련하고 돌봤어요.", "trained와 and로 나란히(과거) → took"),
 ("Max is a great actor, but he sometimes {gets|get} too excited when a lot of people {are|to be} around.", "Max는 훌륭한 배우이지만, 주변에 사람들이 많을 때 가끔 너무 흥분해요.", "주어 he(3인칭 단수) → gets / when절 주어 people 뒤 동사 → are"),
 ("So, I use hand signals {to calm|calm} him.", "그래서, 나는 그를 진정시키기 위해 수신호를 사용해요.", "'~하기 위해'(목적) → to calm"),
 ("Who {am|is} I? I'm an animal wrangler.", "나는 누구일까요? 나는 동물 조련사예요.", "주어 I → am"),
 ("My work {begins|beginning} after the shooting is over.", "내 일은 촬영이 끝나고 나서 시작돼요.", "주어 My work 뒤 동사(3인칭 단수 현재) → begins"),
 ("{To create|Create} a better story, I can {change|changed} the order of scenes or delete some of them.", "더 좋은 이야기를 만들기 위해서, 나는 장면의 순서를 바꾸거나 장면 중 일부를 삭제할 수도 있어요.", "'~하기 위해'(목적) → To create / can + 동사원형 → change"),
 ("Storytelling skills are {important|importantly} for my job, so I read a lot.", "내 직업상 스토리텔링 기술이 중요해서 나는 책을 많이 읽어요.", "be동사 뒤 보어 → 형용사 important"),
 ("I create sound effects in my studio when recording on location {is|are} not easy.", "나는 야외 촬영장에서 녹음하는 게 쉽지 않을 때 내 작업실에서 음향 효과를 만들어요.", "동명사 주어(recording)는 단수 → is"),
 ("Do you {hear|hearing} the sound of waves?", "파도 소리가 들리나요?", "Do + 주어 + 동사원형 → hear"),
 ("I {made|making} that sound with rice and a plastic container.", "나는 쌀과 플라스틱 통으로 그 소리를 만들었어요.", "주어 I 뒤 동사(과거) → made"),
 ("Doesn't it {sound|sounds} real?", "진짜처럼 들리지 않나요?", "Doesn't + 주어 + 동사원형 → sound"),
]
L5 = [
 ("Last Saturday, someone {threw|throw} a cake at the Monalisa in the Botero Museum in Bogota, Colombia.", "지난 토요일, 누군가 콜롬비아 보고타의 보테로 박물관에 있는 '모나리자'에 케이크를 던졌다.", "Last Saturday(과거) → threw"),
 ("There {were|was} four eyewitnesses. What did they {say|said}?", "네 명의 목격자가 있었다. 그들은 뭐라고 말했을까?", "There + be + 복수(four eyewitnesses) → were / did + 동사원형 → say"),
 ("Read the following, and {find|finding} the criminal.", "다음을 읽고, 범인을 찾아보자.", "명령문 Read와 and로 나란히 → find"),
 ("I was looking at the Monalisa, and someone {threw|throw} a cake at the painting.", "저는 '모나리자'를 보고 있었는데, 누군가 그 그림을 향해 케이크를 던졌어요.", "과거 이야기 → threw"),
 ("I turned around and {saw|see} an old man.", "저는 뒤로 돌았고 한 노인을 봤어요.", "turned와 and로 나란히(과거) → saw"),
 ("He was {standing|stand} in front of a wheelchair.", "그는 휠체어 앞에 서 있었어요.", "과거진행형 was + -ing → standing"),
 ("I'm about 170 cm tall, and he was a little {taller|tallest} than me.", "저는 키가 170cm 정도인데, 그는 저보다 조금 더 컸어요.", "than이 있으면 비교급 → taller"),
 ("An old man with gray hair was {running|run} away, and something {fell|fall} off his head.", "회색 머리의 한 노인이 도망가고 있었는데, 그의 머리에서 무언가 떨어졌어요.", "과거진행형 was + -ing → running / 과거 → fell"),
 ("I ran after him, but I couldn't {catch|caught} him.", "저는 그를 뒤쫓았지만, 잡을 수 없었어요.", "couldn't + 동사원형 → catch"),
 ("He was {faster|fastest} than me.", "그는 저보다 더 빨랐거든요.", "than → 비교급 faster"),
 ("In fact, the old man {was|were} not old.", "사실, 그 노인은 나이 든 사람이 아니었어요.", "주어 the old man(단수) → was"),
 ("He {was|were} a young man with long brown hair.", "그는 긴 갈색 머리의 젊은 남자였어요.", "주어 He → was"),
 ("I went to the crime scene, and there {were|was} pieces of cake all over the painting.", "저는 범죄 현장에 갔는데, 그림 곳곳에 케이크 조각들이 있었어요.", "There + be + 복수(pieces) → were"),
 ("There {was|were} also a wheelchair near the painting, and I {found|find} a cake box next to the wheelchair.", "그림 근처에 휠체어도 있었는데, 저는 휠체어 옆에서 케이크 상자를 발견했어요.", "There + be + 단수(a wheelchair) → was / 과거 → found"),
 ("The box {was|were} from Camila's Bakery.", "그 상자는 Camila 빵집의 것이었어요.", "주어 The box(단수) → was"),
 ("Last Friday, a young man {came|comes} in.", "지난 금요일, 한 젊은 남자가 들어왔어요.", "Last Friday(과거) → came"),
 ("I spoke to him in Spanish, but he didn't {understand|understood} me.", "저는 그에게 스페인어로 말했지만, 그는 제 말을 이해하지 못했어요.", "didn't + 동사원형 → understand"),
 ("We had a lot of different {cakes|cake}, but he just wanted the {smallest|smaller} one.", "우리 가게에는 다양한 케이크가 많이 있었지만, 그는 단지 가장 작은 것을 원했어요.", "a lot of different + 복수 명사 → cakes / the + 최상급(여럿 중 가장) → smallest"),
 ("We {sold|sell} only one cake that day, so I remember him clearly.", "우리는 그날 케이크를 한 개만 팔아서, 저는 그를 똑똑히 기억해요.", "that day(과거) → sold"),
 ("Now, {look|looking} at the information about the suspects. Who {threw|throw} the cake at the Monalisa?", "이제, 용의자들에 대한 정보를 보자. 누가 '모나리자'에 케이크를 던졌을까?", "명령문 → 동사원형 look / 과거 사건 → threw"),
]
D = {d['id']: d for d in PK['days']}
norm = lambda s: re.sub(r'\s+', ' ', s.replace('’', "'"))
def build(gid, rng, S, k1, k2, t1, t2):
    TX = {k: norm(' '.join(l[1] for l in D[k]['passage'] if not re.match(r'^[❶-❿]$', l[1]))) for k in (k1, k2)}
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
g6, n6 = build('gt6', '6과 본문 · 어법 선택 한 판', L6, 'd1', 'd2', '본문 ❶❷❸ · 음식물 · 재사용', '본문 ❹❺ · 일회용 플라스틱 · 재활용')
g7, n7 = build('gt7', '7과 본문 · 어법 선택 한 판', L7, 'd3', 'd4', '본문 ❶❷❸ · 감독 · Anna · Peter', '본문 ❹❺❻ · Jennifer · Emma · Chris')
g5, n5 = build('gt5', '5과 본문 · 어법 선택 한 판', L5, 'L5a', 'L5b', '본문 ❶❷ · 사건 · 목격자 1·2', '본문 ❸❹ · 목격자 3·4 · 용의자')
PK['days'] = [d for d in PK['days'] if d['id'] not in ('gt6', 'gt7', 'gt5')] + [g6, g7, g5]
for i, d in enumerate(PK['days']): d['name'] = 'DAY %d' % (i + 1)
src = open(path, encoding='utf-8').read(); head = src[:src.index('window.PKG')]
if '한 판' not in head: head = head.rstrip('\n') + '\n/* 11/17: 6·7·5과 본문 어법 선택 한 판 DAY gt6·gt7·gt5 맨 끝 (generators/gen_m1dgate.py) */\n'
write(PK, path, head)
print('괄호', n6, n7, n5, '·', [d['name'] + ' ' + d['range'] for d in PK['days']][-3:])
