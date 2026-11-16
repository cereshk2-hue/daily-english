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
D = {d['id']: d for d in PK['days']}
txt = re.sub(r'\s+', ' ', ' '.join(l[1] for d in ('d1', 'd2') for l in D[d]['passage'] if not re.match(r'^[❶-❿]$', l[1])).replace('’', "'"))
nb = 0
for s, ko, ex in C1 + C2:
    full = re.sub(r'\{([^|}]*)\|[^}]*\}', r'\1', s)
    assert full in txt, full
    for m in re.findall(r'\{([^}]*)\}', s): o = m.split('|'); assert len(o) == 2 and o[0] != o[1]; nb += 1
assert nb == 26, nb
mk = lambda C: [{'s': s, 'ko': ko, 'ex': ex} for s, ko, ex in C]
day = {'id': 'gt7', 'name': '', 'range': '7과 본문 어법 한 판', 'story': '7과 본문 어법 선택 한 판 · 괄호를 모두 맞혀야 100점 (덩이 2개)',
       'passage': D['d1']['passage'] + D['d2']['passage'],
       'steps': [{'type': 'gate', 'title': '어법 선택 한 판', 'guide': "본문을 두 덩이로 나눴어요. 덩이마다 괄호를 모두 맞혀야 100점, 하나라도 틀리면 0점! 3번 안에 통과 못 하면 틀린 문장만 해설과 함께 연습하고 다시 도전해요.",
                  'items': [{'title': '본문 ❶❷ · 민찬 · Emil (괄호 14개)', 'parts': mk(C1)}, {'title': '본문 ❸ · Vivian (괄호 12개)', 'parts': mk(C2)}]}]}
base = [d for d in PK['days'] if d['id'] != 'gt7']
k = next(i for i, d in enumerate(base) if d['id'] == 'd2') + 1
PK['days'] = base[:k] + [day] + base[k:]
for i, d in enumerate(PK['days']): d['name'] = 'DAY %d' % (i + 1)
src = open(path, encoding='utf-8').read(); head = src[:src.index('window.PKG')]
if '한 판' not in head: head = head.rstrip('\n') + '\n/* 11/16: 7과 본문 어법 한 판 DAY gt7 (generators/gen_m2gate.py) */\n'
write(PK, path, head)
print('괄호', nb, '·', [d['name'] + ' ' + d['range'] for d in PK['days']][3:6])
