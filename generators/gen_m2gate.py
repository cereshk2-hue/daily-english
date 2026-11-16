# 11/16 중2 비상(황종배) 7과 본문 '어법 선택 한 판' DAY (d2 다음) — 선생님 자료(워크북 6 어법 선택형 연습, hwp) 20문장 · 괄호 26개
# 덩이 1 = 본문 ❶❷(괄호 14), 덩이 2 = 본문 ❸(괄호 12). {정답|오답} — 앱이 보기 순서를 섞음
import sys, json, re, subprocess
sys.path.insert(0, '/tmp/claude-0/-home-claude/a9e3e882-1f02-5d62-8f70-aced81bc59d2/scratchpad'); sys.path.insert(0, '/home/claude/srcrepo/generators')
from gencommon import write
path = sys.argv[1] if len(sys.argv) > 1 else '/home/claude/proj/data/m2-visang-hwang-L7.js'
PK = json.loads(subprocess.check_output(['node', '-e', "global.window={};require('%s');process.stdout.write(JSON.stringify(window.PKG))" % path]))
C1 = [
 ("Hello, I'm Minchan! Today, my family and I are at my grandmother's house {to do|do} gimjang.", "안녕하세요, 저는 민찬이에요! 오늘 저희 가족과 저는 김장을 하기 위해 할머니 댁에 있어요.", "'~하기 위해'(목적) → to부정사 to do"),
 ("What is gimjang? It is a Korean cultural tradition to get together and {make|making} a lot of kimchi before winter comes.", "김장은 무엇일까요? 그것은 겨울이 오기 전에 함께 모여 많은 김치를 만드는 한국의 문화적 전통이에요.", "and로 to get과 나란히 → (to) make. making ✗"),
 ("Gimjang is more than making kimchi. It's also about {spending|spend} time with family.", "김장은 김치를 만드는 것 이상이에요. 그것은 또한 가족과 시간을 보내는 것에 관한 것이에요.", "전치사 about 뒤에는 동명사 spending"),
 ("It is always good {to get|get} together. Do you also have any special food traditions?", "함께 모이는 것은 언제나 좋아요. 여러분도 어떤 특별한 음식 전통이 있나요?", "가주어 It ~ 진주어 to부정사 → to get"),
 ("Hi, I'm Emil! We also have this kind of {cultural|culturally} tradition in Azerbaijan.", "안녕하세요, 저는 Emil이에요! 아제르바이잔에도 이런 종류의 문화적 전통이 있어요.", "명사 tradition을 꾸미는 말 → 형용사 cultural"),
 ("Here's a picture from my aunt's wedding. Do you {see|saw} the thing on her shoulder?", "여기 제 이모 결혼식 사진이 있어요. 그녀의 어깨 위에 있는 물건이 보이나요?", "Do + 주어 + 동사원형 → see"),
 ("It's a flatbread. It is so big {that|what} it covers her shoulder.", "그것은 플랫브레드예요. 그것은 매우 커서 그녀의 어깨를 덮어요.", "so + 형용사 + that ~ : 너무 ~해서 …하다"),
 ("We believe {that|what} putting the bread over the shoulder {brings|bring} good luck.", "우리는 그 빵을 어깨 위에 올려두는 것이 행운을 가져온다고 믿어요.", "뒤가 완전한 문장 → 접속사 that / 동명사 주어(putting ~)는 단수 → brings"),
 ("A flatbread is {made|making} only from flour, salt, and water.", "플랫브레드는 밀가루, 소금, 물로만 만들어져요.", "빵이 '만들어지는' 것 → 수동태 is made (from ~로)"),
 ("We eat this bread at every {meal|meals}, but we make {it bigger|bigger it} on special days.", "우리는 매 끼니에 이 빵을 먹지만, 특별한 날에는 더 크게 만들어요.", "every + 단수 명사 meal / make + 목적어 + 보어 → make it bigger"),
 ("So, everyone in the community {gets|get} together and helps out.", "그래서 공동체에 있는 모든 사람이 함께 모여서 도와줘요.", "everyone은 단수 → gets (뒤의 helps와도 짝)"),
 ("Baking the bread together {makes|make} our community stronger.", "함께 빵을 굽는 일은 우리 공동체를 더욱 단단하게 만들어 줘요.", "동명사 주어(Baking ~)는 단수 → makes"),
]
C2 = [
 ("I'm Vivian! Have you {heard|hearing} of hawker centers in Singapore? Hawkers are people {who|which} {sell|sells} food on the street.", "저는 Vivian이에요! 여러분은 싱가포르에 있는 호커 센터에 대해 들어 본 적 있나요? 호커는 길거리에서 음식을 파는 사람들을 말해요.", "현재완료 Have + p.p. → heard / 사람 선행사 → who / 선행사 people(복수) → sell"),
 ("They {formed|were formed} the hawker centers and these centers have {become|became} a huge food community.", "그들이 호커 센터를 만들었고, 이 센터들이 거대한 음식 공동체가 되었어요.", "목적어(the hawker centers)가 있으니 능동 formed / have + p.p. → become"),
 ("These centers are so popular {that|what} they are always full of people.", "이 센터들은 매우 인기 있어서 늘 사람들로 가득 차요.", "so + 형용사 + that ~"),
 ("There {are|is} all kinds of food, from Chinese noodles to Malaysian curry to Indonesian satay.", "중국식 국수부터 말레이시아식 카레, 인도네시아식 사테까지 모든 종류의 음식들이 있어요.", "There + be + 주어: all kinds of food(여러 종류) → are"),
 ("My friends and I are from different countries. We all {have|having} different food tastes.", "제 친구들과 저는 서로 다른 나라 출신이에요. 우리는 모두 음식 취향이 달라요.", "주어 We all 뒤 동사 자리 → have"),
 ("But at the hawker centers, we can always {find|finding} something we {like|like it}.", "하지만 호커 센터에서 우리는 항상 우리가 좋아하는 것을 찾을 수 있어요.", "조동사 can + 동사원형 find / 목적격 관계대명사가 생략된 절이라 목적어(it)를 또 쓰지 않음 → like"),
 ("Sometimes, we share the tables with strangers and end up {becoming|become} friends.", "때때로 우리는 낯선 사람들과 테이블을 함께 쓰다가 친구가 되기도 해요.", "end up + -ing : 결국 ~하게 되다 → becoming"),
 ("It is fun to {enjoy|enjoying} the food with good people. That's why I love this hawker culture.", "좋은 사람들과 함께 음식을 즐기는 건 재미있어요. 그게 제가 이 호커 문화를 사랑하는 이유예요.", "to + 동사원형 → to enjoy"),
]

# 11/16 저녁: 8과 본문 어법 선택 한 판 (선생님 자료: 8과 워크북 6 어법 선택형 연습 hwp) 22문장 · 괄호 34개(13 + 21)
# 덩이 1 = 본문 ❶❷, 덩이 2 = 본문 ❸❹
C3 = [
 ("Do you know {what the most challenging race in the world is|what is the most challenging race in the world}? It is \"The Last Wild Race\"!", "여러분은 세상에서 가장 도전적인 경주가 무엇인지 아시나요? 그것은 '마지막 야생 경주'입니다!", "간접의문문(문장 속 의문문) → 의문사 + 주어 + 동사: what the most challenging race ~ is"),
 ("You should join us in Southern Patagonia, Chile. It is one of the last wild {areas|area} on Earth!", "여러분은 칠레의 남부 파타고니아에서 우리와 함께하셔야 합니다. 이곳은 지구상의 마지막 야생 지역 중 하나입니다!", "one of the + 복수 명사 → areas"),
 ("Every {year|years}, many teams from all over the world {join|joins} the race.", "매년 전 세계에서 온 많은 팀들이 이 경주에 참여합니다.", "every + 단수 명사 → year / 주어 many teams(복수) → join"),
 ("For this race, you {need|needing} not only strength but also teamwork.", "이 경주를 위해서, 여러분은 힘뿐만 아니라 팀워크도 필요합니다.", "주어 you 뒤에 동사가 필요 → need (needing은 동사 자리에 못 옴)"),
 ("The race course is {more|most} than 500 kilometers long and it changes every year.", "경주 코스는 500km 이상 길이가 되고 그것은 매년 바뀝니다.", "more than ~ : ~보다 많이, ~ 이상"),
 ("Do you know {when the teams find|when do the teams find} out the course for the year? Just a day before the race!", "팀들이 그해의 코스를 언제 알게 되는지 아시나요? 바로 경주 하루 전입니다!", "간접의문문 → 의문사 + 주어 + 동사: when the teams find (do를 쓰지 않음)"),
 ("During the race, each team {goes|go} through the wild by {doing|do} different activities.", "경주 동안, 각 팀은 다양한 활동들을 함으로써 야생을 통과합니다.", "each + 단수 명사는 단수 취급 → goes / 전치사 by 뒤 → 동명사 doing"),
 ("They walk on rough ground, ride bikes on tough roads, and {row|rowing} boats on rapid water.", "그들은 거친 땅을 걷고, 험한 길에서 자전거를 타며, 속도가 빠른 물 위에서 배를 젓습니다.", "walk, ride와 and로 나란히(병렬) → row"),
 ("The race is not just about sports. The teams also need {to take|taking} care of nature.", "그 경주는 단지 스포츠에 관한 것만은 아닙니다. 팀들은 또한 자연을 돌볼 필요가 있습니다.", "need + to부정사 : ~할 필요가 있다 → to take"),
 ("They must not make fires or {leave|leaving} trash behind during the race.", "그들은 경주 중에 불을 피우거나 쓰레기를 남기지 말아야 합니다.", "must not 뒤 make와 or로 나란히 → 동사원형 leave"),
 ("Everyone should {protect|protected} the natural environment of Southern Patagonia.", "모두가 남부 파타고니아의 자연환경을 보호해야 합니다.", "조동사 should + 동사원형 → protect"),
]
C4 = [
 ("What {Are|Is} the Rules of the Race?", "경주의 규칙은 무엇인가요?", "주어 the Rules(복수) → Are"),
 ("{To join|Join} the event, all {teams|team} must follow a few rules.", "이 행사에 참가하기 위해 모든 팀들은 몇 가지 규칙을 따라야 합니다.", "'~하기 위해'(목적) → To join / all + 복수 명사 → teams"),
 ("For example, a team of four must {have|had} at least one man and one woman.", "예를 들어, 4명으로 구성된 팀에는 적어도 한 명의 남자와 한 명의 여자가 있어야 합니다.", "조동사 must + 동사원형 → have"),
 ("Every {member|members} must show {that|what} they are healthy.", "모든 팀원은 그들이 건강하다는 것을 보여줘야 합니다.", "every + 단수 명사 → member / 뒤가 완전한 문장 → 접속사 that (what은 뒤가 불완전할 때)"),
 ("Also, each {team|teams} must pass some tests that {check|checks} their skills in using ropes, reading maps, and {giving|give} first aid.", "또한, 각 팀은 로프 사용하기, 지도 읽기, 응급 처치하기에서의 기술들을 확인하는 몇 가지 테스트를 통과해야 합니다.", "each + 단수 명사 → team / 선행사 tests(복수) → check / using, reading과 나란히 → giving"),
 ("This is important {because|because of} the race is very tough, and everyone {needs|need} {to be|being} ready for the challenges.", "이것은 중요한데 왜냐하면 경주가 매우 힘들어서 모든 사람이 도전에 준비되어 있어야 하기 때문입니다.", "뒤에 주어+동사(절) → because (because of + 명사) / everyone은 단수 → needs / need + to부정사 → to be"),
 ("{To finish|Finish} the race, each {team|teams} must reach every checkpoint. The first team {to finish|finish} the race wins.", "경주를 끝내기 위해, 각 팀은 모든 체크포인트에 도달해야 합니다. 가장 먼저 경주를 마치는 팀이 승리합니다.", "'~하기 위해' → To finish / each + 단수 명사 → team / 명사(the first team)를 꾸미는 to부정사 → to finish (동사는 wins)"),
 ("Are you ready {to experience|experiencing} \"The Last Wild Race\"?", "'마지막 야생 경주'를 경험할 준비가 되셨나요?", "be ready + to부정사 : ~할 준비가 되다 → to experience"),
 ("Don't miss out on this {amazing|amazed} adventure!", "이 놀라운 모험을 놓치지 마세요!", "모험이 (사람을) 놀라게 하는 것 → -ing 형용사 amazing (amazed는 사람이 놀란 감정)"),
 ("This wild journey is not only {exciting|excited} but also {meaningful|meaningfully}.", "이 야생의 여정은 흥미진진할 뿐만 아니라 의미도 있을 것입니다.", "여정이 흥미를 주는 것 → exciting / be동사 뒤 보어 자리 → 형용사 meaningful (부사 ✘)"),
 ("Sign up today and {enjoy|enjoying} moments {that|who} will last a lifetime.", "오늘 바로 등록하고 평생 지속될 순간들을 즐겨보세요.", "명령문 Sign up과 and로 나란히 → 동사원형 enjoy / 선행사 moments(사물) → 관계대명사 that (who는 사람)"),
]

D = {d['id']: d for d in PK['days']}
txt = re.sub(r'\s+', ' ', ' '.join(l[1] for d in ('d1', 'd2') for l in D[d]['passage'] if not re.match(r'^[❶-❿]$', l[1])).replace('’', "'"))
nb = 0
for s, ko, ex in C1 + C2:
    full = re.sub(r'\{([^|}]*)\|[^}]*\}', r'\1', s)
    assert full in txt, full
    for m in re.findall(r'\{([^}]*)\}', s): o = m.split('|'); assert len(o) == 2 and o[0] != o[1]; nb += 1
assert nb == 26, nb
mk = lambda C: [{'s': s, 'ko': ko, 'ex': ex} for s, ko, ex in C]
day = {'id': 'gt7', 'name': '', 'range': '7과 본문 · 어법 선택 한 판', 'story': '7과 본문 어법 선택 한 판 · 괄호를 모두 맞혀야 100점 (덩이 2개)',
       'passage': D['d1']['passage'] + D['d2']['passage'],
       'steps': [{'type': 'gate', 'title': '어법 선택 한 판', 'guide': "본문을 두 덩이로 나눴어요. 덩이마다 괄호를 모두 맞혀야 100점, 하나라도 틀리면 0점! 3번 안에 통과 못 하면 틀린 문장만 해설과 함께 연습하고 다시 도전해요.",
                  'items': [{'title': '본문 ❶❷ · 민찬 · Emil (괄호 14개)', 'parts': mk(C1)}, {'title': '본문 ❸ · Vivian (괄호 12개)', 'parts': mk(C2)}]}]}
t8 = re.sub(r'\s+', ' ', ' '.join(l[1] for d in ('d3', 'd4') for l in D[d]['passage'] if not re.match(r'^[❶-❿]$', l[1])).replace('’', "'"))
nb8 = 0
for s_, ko, ex in C3 + C4:
    full = re.sub(r'\{([^|}]*)\|[^}]*\}', r'\1', s_)
    assert full in t8, full
    for m in re.findall(r'\{([^}]*)\}', s_): o = m.split('|'); assert len(o) == 2 and o[0] != o[1]; nb8 += 1
n3 = sum(len(re.findall(r'\{', x[0])) for x in C3); n4 = nb8 - n3
day8 = {'id': 'gt8', 'name': '', 'range': '8과 본문 · 어법 선택 한 판', 'story': '8과 본문 어법 선택 한 판 · 괄호를 모두 맞혀야 100점 (덩이 3개)',
        'passage': D['d3']['passage'] + D['d4']['passage'],
        'steps': [{'type': 'gate', 'title': '어법 선택 한 판', 'guide': day['steps'][0]['guide'].replace('두 덩이', '세 덩이'),
                   'items': [{'title': '본문 ❶❷ · 경주 소개 (괄호 %d개)' % n3, 'parts': mk(C3)}, {'title': '본문 ❸ · 규칙 (괄호 %d개)' % sum(len(re.findall(r'\{', x[0])) for x in C4[:7]), 'parts': mk(C4[:7])}, {'title': '본문 ❹ · 함께하세요 (괄호 %d개)' % sum(len(re.findall(r'\{', x[0])) for x in C4[7:]), 'parts': mk(C4[7:])}]}]}
base = [d for d in PK['days'] if d['id'] not in ('gt7', 'gt8')]
PK['days'] = base + [day, day8]  # 11/16 저녁: 선생님 요청으로 DAY 맨 끝으로 옮김(이름은 '어법 선택 한 판' 유지)
for i, d in enumerate(PK['days']): d['name'] = 'DAY %d' % (i + 1)
src = open(path, encoding='utf-8').read(); head = src[:src.index('window.PKG')]
if '한 판' not in head: head = head.rstrip('\n') + '\n/* 11/16: 7과 본문 어법 한 판 DAY gt7 (generators/gen_m2gate.py) */\n'
write(PK, path, head)
print('괄호 7과', nb, '· 8과', nb8, n3, n4, '·', [d['name'] + ' ' + d['range'] for d in PK['days']][-3:])
