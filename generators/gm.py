# 11/18 심학중1 천재(소영순) 4·5·6과 '어법 선택 한 판' DAY 3개 (맨 끝, 4 → 5 → 6) — 선생님 자료: 각 과 워크북 6 어법 선택형 연습 hwp (이그잼포유)
# 과마다 두 덩이 = 본문 DAY 두 개(4과 L4a/L4b, 5과 L5a/L5b, 6과 d1/d2). {정답|오답} — 앱이 보기 순서를 섞음. gen_m1dgate.py(동아) 복사
import sys, json, re, subprocess
sys.path.insert(0, '/home/claude/srcrepo/generators')
from gencommon import write
path = sys.argv[1] if len(sys.argv) > 1 else '/home/claude/proj/data/m1-chunjae-so-L6.js'
PK = json.loads(subprocess.check_output(['node', '-e', "global.window={};require('%s');process.stdout.write(JSON.stringify(window.PKG))" % path]))
L4 = [
 ('During the summer vacation, William {traveled|travel} around Korea with his family.', '여름 방학 동안, William은 가족과 함께 한국 여기저기를 여행했다.', "지난 여름 방학 이야기(과거) → traveled"),
 ('This {is|be} his food diary.', '이것은 그의 음식 일기이다.', "주어 This(단수) 뒤 be동사 현재 → is"),
 ('We {went|gone} to Damyang and visited Jungnogwon, a famous bamboo garden.', '우리는 담양에 갔고 유명한 대나무 정원인 죽녹원을 방문했다.', "과거형 went (gone은 과거분사라 혼자 동사로 못 씀) · visited와 나란히"),
 ('We enjoyed {walking|walk} in the garden.', '우리는 정원에서 걷는 것을 즐겼다.', "enjoy + 동명사 → walking"),
 ('After we {looked|look} around, we ate two local dishes, daetongbap and tteokgalbi.', '주변을 둘러본 후에, 우리는 두 가지 지역 음식인 대통밥과 떡갈비를 먹었다.', "과거 이야기(ate) → looked"),
 ('Daetongbap {is|are} rice in a bamboo bowl.', '대통밥은 대나무 그릇에 담긴 밥이다.', "주어 Daetongbap(단수), 지금도 사실 → is"),
 ('I loved {its|their} unique bamboo smell.', '나는 그것의 독특한 대나무 향이 매우 좋았다.', "가리키는 것이 daetongbap(단수) → its"),
 ('Tteokgalbi, a Korean beef dish, {was|were} soft and sweet.', '한국의 소고기 요리인 떡갈비는 부드럽고 달콤했다.', "주어 Tteokgalbi(단수) — 콤마 사이는 설명 → was"),
 ('The dishes really {went|gone} well together.', '그 요리들은 함께 정말 잘 어울렸다.', "go well together(잘 어울리다)의 과거형 → went"),
 ('We visited Tongyeong and {went|go} up the mountain by cable car.', '우리는 통영을 방문했고 케이블카를 타고 산에 올라갔다.', "visited와 and로 나란히(과거) → went"),
 ('{Seeing|See} the blue ocean and the green islands was fantastic!', '파란 바다와 녹색의 섬들을 보는 것은 환상적이었다!', "문장의 주어 자리 '~하는 것' → 동명사 Seeing (동사는 was)"),
 ('Near the sea, we found a local restaurant and {ate|eat} chungmugimbap.', '바다 근처에서 우리는 현지 식당을 찾았고 충무김밥을 먹었다.', "found와 and로 나란히(과거) → ate"),
 ('It wasn’t like {other|another} types of gimbap.', '그것은 다른 종류의 김밥과는 달랐다.', "뒤에 복수 명사 types → other (another + 단수 명사)"),
 ('There {was|were} only rice inside the seaweed.', '김 안에는 오직 밥만 있었다.', "There + be + 셀 수 없는 명사 rice(단수 취급) → was"),
 ('Kimchi and spicy squid {were|was} on the side.', '김치와 매운 오징어가 옆에 있었다.', "주어가 A and B(두 가지) → 복수 were"),
 ('It {was|were} spicy but really delicious.', '그것은 매웠지만 정말 맛있었다.', "주어 It(단수), 과거 → was"),
 ('I {heard|hearing} about the history of this food.', '나는 이 음식의 역사에 관해 들었다.', "주어 I 뒤 동사 자리(과거) → heard"),
 ('Chungmu {is|are} an old name for Tongyeong.', '충무는 통영의 옛 이름이다.', "주어 Chungmu(단수), 지금도 사실 → is"),
 ('Long ago, fishermen in this town started to eat chungmugimbap because it {did|does} not go bad quickly.', '오래전에, 이 마을의 어부들은 이 음식이 빨리 상하지 않았기 때문에 충무김밥을 먹기 시작했다.', "Long ago(과거) → did not"),
 ('Jeju-do is a {beautiful|beautifully} island in Korea.', '제주도는 한국의 아름다운 섬이다.', "명사 island를 꾸미는 말 → 형용사 beautiful"),
 ('We went there on a very hot day, and we {became|become} tired.', '우리는 매우 더운 날에 거기에 갔고 피곤해졌다.', "went와 이어지는 과거 이야기 → became"),
 ('However, we {got|gets} our energy back thanks to dombegogi.', '그러나 돔베고기 덕분에 우리는 기운을 되찾았다.', "주어 we, 과거 → got (gets는 3인칭 단수 현재)"),
 ('It surprised me in two {ways|way}.', '그것은 두 가지 면으로 나를 놀라게 했다.', "two + 복수 명사 → ways"),
 ('First, it {was|were} pork on a cutting board, not on a plate.', '첫째로, 그것은 접시 위가 아닌 도마 위의 돼지고기였다.', "주어 it(단수), 과거 → was"),
 ('Second, the meat {was|did} so soft!', '둘째로, 고기가 아주 부드러웠다!', "형용사 soft 앞 → be동사 was (did 뒤에는 동사원형이 와야 함)"),
 ('I {had|has} it with a special fish sauce, and the sauce was great, {too|either}.', '나는 그것을 특별한 생선 소스와 함께 먹었는데, 그 소스도 훌륭했다.', "주어 I, 과거 → had / 긍정문의 '~도' → too (either는 부정문)"),
 ('Later, I {learned|learning} about the meaning of dombe.', '나중에 나는 돔베의 의미에 대해 배웠다.', "주어 I 뒤 동사 자리(과거) → learned"),
 ('It {means|mean} a cutting board in Jeju’s language.', '그것은 제주 말로 도마를 의미한다.', "주어 It(3인칭 단수), 지금도 사실 → means"),
]
L5 = [
 ('El and Jo {were|was} the {smallest|smaller} students in the class.', 'El과 Jo는 반에서 가장 작은 학생들이었다.', "주어 El and Jo(복수) → were / in the class(반에서 가장) → the + 최상급 smallest"),
 ('They {were|was} always together.', '그들은 항상 함께였다.', "주어 They(복수) → were"),
 ('They even watered the plants together in the class because they could not {reach|reached} the pots alone.', '그들은 혼자서는 화분에 닿을 수 없었기 때문에 심지어는 교실에서 함께 식물에 물을 주기도 했다.', "could not + 동사원형 → reach"),
 ('However, in the spring, something {was|were} DIFFERENT. Jo grew TALLER!', '하지만 봄에는 무언가가 달라졌다. Jo의 키가 더 커졌다!', "something은 단수 취급 → was"),
 ('Jo was {taller|tall} than El, so Jo could {water|watered} the plants alone.', 'Jo는 El보다 키가 더 컸고, 그래서 Jo는 혼자 식물에 물을 줄 수 있었다.', "than이 있으면 비교급 → taller / could + 동사원형 → water"),
 ('El felt smaller every {day|days}.', 'El은 매일 더 작아지는 기분이었다.', "every + 단수 명사 → day"),
 ('On the last day of school, Mr. Diaz said, “Class, you can take a flower home and {care|cared} for it over the summer.”', '학교 마지막 날에 Diaz 선생님이 말씀하셨다. “여러분, 꽃을 하나 집에 가져가서 여름 동안 돌보세요.”', "can take와 and로 나란히 → 동사원형 care (can이 둘 다에 걸림)"),
 ('All the students {ran|runs} to the window.', '모든 학생이 창문으로 달려갔다.', "주어 All the students(복수), 과거 이야기 → ran"),
 ('El’s classmates {reached|reaches} for the pots over tiny El.', 'El의 학급 친구들은 작은 El 너머 화분에 손을 뻗었다.', "주어 classmates(복수), 과거 → reached"),
 ('They {took|takes} all the pots with colorful flowers.', '그들은 형형색색의 꽃이 있는 화분을 모두 가져갔다.', "주어 They, 과거 이야기 → took"),
 ('El {took|take} the last pot.', 'El은 마지막 화분을 가져갔다.', "과거 이야기 → took"),
 ('It {had|have} the smallest plant with no flowers.', '그것은 꽃이 없는 가장 작은 식물을 가지고 있었다.', "주어 It(그 화분), 과거 → had"),
 ('“I feel just like you, little plant,” {said|saying} El.', '“나도 너와 같은 심정이야, 작은 식물아.” El이 말했다.', "인용문 뒤 동사 + 주어 어순(said El), 과거 → said"),
 ('Mr. Diaz looked at El and {said|say}, “That’s an aster plant. In time, it’ll grow and {have|had} beautiful flowers.”', 'Diaz 선생님이 El을 보며 말씀하셨다. “그것은 과꽃 식물이야. 시간이 지나면, 그것은 자라서 아름다운 꽃을 피울 거야.”', "looked와 나란히(과거) → said / it’ll(will) grow and (will) have → 동사원형 have"),
 ('“But it’s just a little green plant,” {said|saying} El. She was not so sure.', '“하지만 그것은 작은 녹색 식물일 뿐이에요.” El이 말했다. 그녀는 확신이 없었다.', "인용문 뒤 said + 주어, 과거 → said"),
 ('“You can {have|had} my zinnia plant,” Jo said to El, “I’ll be at my grandma’s all summer.”', '“너는 내 백일홍을 가져도 돼.” Jo가 El에게 말했다. “나는 여름 내내 할머니 댁에 있을 거야.”', "can + 동사원형 → have"),
 ('“I’ll {plant|planted} my aster and your zinnia side by side,” El said.', '“내가 내 과꽃과 너의 백일홍을 나란히 심을게.” El이 말했다.', "I’ll(will) + 동사원형 → plant"),
 ('“They’ll {be|do} good friends — just like us!” said Jo. El smiled.', '“그것들은 좋은 친구가 될 거야 — 바로 우리처럼!” Jo가 말했다. El은 미소 지었다.', "will be + 명사(good friends) '~이 되다' → be"),
 ('El {planted|planting} the flowers in her garden.', 'El은 그녀의 정원에 꽃들을 심었다.', "주어 El 뒤 동사 자리(과거) → planted"),
 ('It was growing season. All summer long, she {cared|caring} for them.', '성장하는 시기였다. 여름 내내 그녀는 그것들을 돌보았다.', "주어 she 뒤 동사 자리(과거) → cared"),
 ('On the last day of summer, Jo {came|come} to El’s house.', '여름의 마지막 날, Jo가 El의 집에 왔다.', "과거 이야기 → came"),
 ('El and Jo ran to the garden and suddenly {stopped|stopping}. Something {was|were} DIFFERENT!', 'El과 Jo는 정원으로 달려가다가 갑자기 멈췄다. 무엇인가가 달라졌다!', "ran과 and로 나란히(과거) → stopped / Something(단수) → was"),
 ('There {were|was} flowers on the aster ... and El grew TALLER, {TOO|EITHER}!', '과꽃에 꽃들이 있었다 ... 그리고 El도 키가 더 커졌다!', "There + be + 복수(flowers) → were / 긍정문의 '~도' → TOO"),
]
L6 = [
 ('Some people love {to work|work} in nature.', '어떤 사람들은 자연에서 일하는 것을 아주 좋아한다.', "love + to부정사(또는 동명사) → to work (동사원형은 안 됨)"),
 ('They {work|working} in the sea, mountains, or even in the Arctic.', '그들은 바다, 산, 심지어 북극에서도 일한다.', "주어 They 뒤 동사 자리(현재) → work"),
 ('Let’s meet them and {listen|listening} to their stories.', '그들을 만나 보고 그들의 이야기를 들어 보자.', "Let’s + 동사원형, meet과 and로 나란히 → listen"),
 ('I am Nari. I am a haenyeo in Geoje. I dive in the water and {collect|to collect} seafood.', '저는 나리입니다. 저는 거제의 해녀입니다. 저는 물에 잠수해서 해산물을 채집합니다.', "dive와 and로 나란히(동사) → collect"),
 ('In the morning, I {check|checking} the tide and the weather.', '아침에, 저는 조수와 날씨를 확인합니다.', "주어 I 뒤 동사 자리(현재) → check"),
 ('I wear a diving suit and swimming glasses {to work|work} in the water.', '저는 물속에서 일하기 위해 잠수복을 입고 수경을 씁니다.', "'~하기 위해'(목적) → to work (to부정사 부사적 용법)"),
 ('I love {diving|dive} and {spending|spend} time in the beautiful sea.', '저는 잠수하는 것과 아름다운 바다에서 시간을 보내는 것을 아주 좋아합니다.', "love의 목적어 '~하는 것' → 동명사 diving, and로 나란히 → spending"),
 ('I don’t {collect|collected} too much seafood. This is good for the ocean.', '저는 너무 많은 해산물을 채집하지 않습니다. 이것이 바다에 좋습니다.', "don’t + 동사원형 → collect"),
 ('These days, I see a lot of trash in the water, so I {pick|picked} up the trash.', '요즘은 물속에 쓰레기가 많이 보여서 쓰레기를 줍습니다.', "These days(요즘) · see와 같은 현재 → pick"),
 ('I believe that we should {care|cares} about the ocean.', '저는 우리가 바다에 신경을 써야 한다고 믿습니다.', "should + 동사원형 → care"),
 ('My name {is|are} Jihan. I am a vet at the wild animal care center in Jirisan.', '제 이름은 지한입니다. 저는 지리산 야생 동물 보호 센터의 수의사입니다.', "주어 My name(단수) → is"),
 ('I take care of sick wild animals in the center and {send|sends} {them|it} back to their homes.', '저는 센터의 아픈 야생 동물을 돌보고 그들을 집으로 돌려보냅니다.', "주어 I, take와 나란히 → send / 가리키는 것이 animals(복수) → them"),
 ('Also, I often climb the mountain {to look|look} after wild animals like bears.', '또한 저는 곰과 같은 야생 동물을 돌보기 위해 자주 산을 오릅니다.', "'~하기 위해'(목적) → to look (look after = 돌보다)"),
 ('I’m {proud|proudly} of my job. I think that {protecting|protect} wild animals is important.', '저는 제 직업이 자랑스럽습니다. 저는 야생 동물을 보호하는 것이 중요하다고 생각합니다.', "be동사 뒤 보어 → 형용사 proud (be proud of) / that절의 주어 자리 '~하는 것' → 동명사 protecting"),
 ('We should {keep|keeps} an eye on them and their homes {to live|live} together.', '우리는 함께 살아가기 위해 그들과 그들의 서식처를 계속 지켜보아야 합니다.', "should + 동사원형 → keep / '~하기 위해'(목적) → to live"),
 ('My name {is|are} Eun, and I am an Arctic scientist.', '제 이름은 은이고, 저는 극지 과학자입니다.', "주어 My name(단수) → is"),
 ('I {work|working} at the Arctic Dasan Station in Norway.', '저는 노르웨이의 북극 다산 과학 기지에서 일합니다.', "주어 I 뒤 동사 자리 → work"),
 ('I {study|studying} the soil, seawater, and ice in the Arctic.', '저는 북극의 토양, 바닷물, 얼음을 연구합니다.', "주어 I 뒤 동사 자리 → study"),
 ('I often {travel|travels} on the special ship, Araon.', '저는 특별한 배인 아라온호를 타고 자주 이동합니다.', "주어 I(1인칭) → travel (travels는 3인칭 단수)"),
 ('This ship is {stronger|strong} than other ships.', '이 배는 다른 배보다 더 튼튼합니다.', "than이 있으면 비교급 → stronger"),
 ('It can {break|broke} thick ice across the ocean.', '그것은 바다를 가로질러 두꺼운 얼음을 깰 수 있습니다.', "can + 동사원형 → break"),
 ('Thanks to Araon, I can {collect|collected} seawater samples.', '아라온호 덕분에 저는 바닷물 표본을 채집할 수 있습니다.', "can + 동사원형 → collect"),
 ('The Arctic Ocean {has|have} the answers to the climate crisis.', '북극해는 기후 위기에 대한 해답을 가지고 있습니다.', "주어 The Arctic Ocean(3인칭 단수) → has"),
 ('I hope that my work can {help|helped} the Earth.', '저는 제 일이 지구를 도울 수 있기를 바랍니다.', "can + 동사원형 → help"),
]
D = {d['id']: d for d in PK['days']}
norm = lambda s: re.sub(r'\s+', ' ', s.replace('’', "'").replace('‘', "'").replace('“', '"').replace('”', '"').replace('—', '-').replace('–', '-').replace('…', '...')).lower()
def build(gid, rng, S, k1, k2, t1, t2):
    TX = {k: norm(' '.join(l[1] for l in D[k]['passage'] if not re.match(r'^[❶-❿]$', l[1]))) for k in (k1, k2)}
    G = {k1: [], k2: []}
    for s, ko, ex in S:
        full = norm(re.sub(r'\{([^|}]*)\|[^}]*\}', r'\1', s))
        where = [k for k in TX if full in TX[k]]
        if len(where) != 1:  # 인용 부호·말줄임 등 표기 차이 → 앞 40자로 다시
            where = [k for k in TX if full[:40] in TX[k]]
        assert len(where) == 1, (full, where)
        for m in re.findall(r'\{([^}]*)\}', s): o = m.split('|'); assert len(o) == 2 and o[0] != o[1], s
        G[where[0]].append({'s': s, 'ko': ko, 'ex': ex})
    nb = {k: sum(len(re.findall(r'\{', p['s'])) for p in v) for k, v in G.items()}
    return {'id': gid, 'name': '', 'range': rng, 'story': rng + ' · 괄호를 모두 맞혀야 100점 (덩이 2개)',
            'passage': D[k1]['passage'] + D[k2]['passage'],
            'steps': [{'type': 'gate', 'title': '어법 선택 한 판', 'guide': "본문을 두 덩이로 나눴어요. 덩이마다 괄호를 모두 맞혀야 100점, 하나라도 틀리면 0점! 3번 안에 통과 못 하면 틀린 문장만 해설과 함께 연습하고 다시 도전해요.",
                       'items': [{'title': '%s (괄호 %d개)' % (t1, nb[k1]), 'parts': G[k1]}, {'title': '%s (괄호 %d개)' % (t2, nb[k2]), 'parts': G[k2]}]}]}, nb
g4, n4 = build('gt4', '4과 본문 · 어법 선택 한 판', L4, 'L4a', 'L4b', '본문 ❶❷ · 담양 · 통영', '본문 ❸ · 제주')
g5, n5 = build('gt5', '5과 본문 · 어법 선택 한 판', L5, 'L5a', 'L5b', '본문 ❶❷ · 키 작은 El과 Jo · 화분', '본문 ❸ · 여름 정원')
g6, n6 = build('gt6', '6과 본문 · 어법 선택 한 판', L6, 'd1', 'd2', '본문 ❶❷ · 들어가며 · 해녀 나리', '본문 ❸❹ · 수의사 지한 · 극지 과학자 은')
PK['days'] = [d for d in PK['days'] if d['id'] not in ('gt4', 'gt5', 'gt6')] + [g4, g5, g6]
for i, d in enumerate(PK['days']): d['name'] = 'DAY %d' % (i + 1)
src = open(path, encoding='utf-8').read(); head = src[:src.index('window.PKG')]
tail = src[src.index('/* WRAPUP-TESTS'):] if '/* WRAPUP-TESTS' in src else ''
if '한 판' not in head: head = head.rstrip('\n') + '\n/* 11/18: 4·5·6과 본문 어법 선택 한 판 DAY gt4·gt5·gt6 맨 끝 (generators/gen_m1cgate.py) */\n'
PK.pop('tests', None) if tail else None
write(PK, path, head)
if tail: open(path, 'a', encoding='utf-8').write(tail)
print('괄호', n4, n5, n6, '·', [d['name'] + ' ' + d['range'] for d in PK['days']][-3:])
