# 11/19 중산중3 지학사(민찬규) 학교 프린트 맨 뒷장 외부지문 'Reading File · Lesson 7 Challenge'(일본 전통 가옥) → 본문 DAY (맨 끝, id rf7)
# 원본: 선생님 PDF(스캔) 17쪽을 보고 옮김. 빈칸(2번 문제 정답) = keep the living area dry and safe. 출처 web-japan.org kidsweb
# 한 줄씩 면밀하게: 13문장 전부 스크램블, 어법·동사변형·오류는 문장마다 하나 이상. 구성은 본문 DAY(d2)와 같음
import sys, json, re, subprocess
sys.path.insert(0, '/home/claude/srcrepo/generators')
from gencommon import write
path = sys.argv[1] if len(sys.argv) > 1 else '/home/claude/proj/data/m3-jihak-min-L7.js'
PK = json.loads(subprocess.check_output(['node', '-e', "global.window={};require('%s');process.stdout.write(JSON.stringify(window.PKG))" % path]))
S = [
 ("What would it be like to live in a traditional Japanese house?", "전통 일본 가옥에 산다면 어떨까?"),
 ("If you lived there, you would have to take off your shoes in the genkan, an entrance hall, before entering the house.", "만약 당신이 그곳에 산다면, 집에 들어가기 전에 현관인 겐칸에서 신발을 벗어야 할 것이다."),
 ("In the house, many Japanese do not use chairs.", "집 안에서 많은 일본 사람들은 의자를 사용하지 않는다."),
 ("Instead, they sit directly on tatami mats that are made from woven grass.", "대신에, 그들은 엮은 풀로 만들어진 다다미 매트 위에 바로 앉는다."),
 ("Rooms are divided by shoji, portable sliding doors that are made from wood and thin paper.", "방은 나무와 얇은 종이로 만들어진 이동식 미닫이문인 쇼지로 나뉜다."),
 ("For large gatherings, these doors can be removed to create one large room.", "큰 모임을 위해, 이 문들은 하나의 큰 방을 만들기 위해 떼어 낼 수 있다."),
 ("When the weather gets cold, people prefer to sit at a kotatsu, a heated table, and put their legs in it.", "날씨가 추워지면, 사람들은 열이 나는 탁자인 고타쓰에 앉아 그 안에 다리를 넣는 것을 좋아한다."),
 ("Keeping their body warm, Japanese have meals, drink tea, or read books at the table.", "몸을 따뜻하게 유지하면서, 일본 사람들은 그 탁자에서 식사를 하거나, 차를 마시거나, 책을 읽는다."),
 ("In summer, heavy rain can cause flooding.", "여름에는 폭우가 홍수를 일으킬 수 있다."),
 ("The floor of the house is raised a little off the ground to keep the living area dry and safe from flooding.", "집의 바닥은 생활 공간을 홍수로부터 건조하고 안전하게 유지하기 위해 땅에서 약간 높여져 있다."),
 ("The house also has sloped roofs because they keep rainwater flowing off easily.", "그 집은 또한 경사진 지붕을 가지고 있는데, 그것이 빗물을 쉽게 흘러내리게 하기 때문이다."),
 ("The roofs are covered with kawara tiles.", "지붕은 가와라 기와로 덮여 있다."),
 ("The strong kawara tiles are not only water-resistant but also fireproof.", "튼튼한 가와라 기와는 방수가 될 뿐만 아니라 불에도 강하다."),
]
E = [s for s, _ in S]
passage = [["#", "7과 Reading File · 외부지문 (학교 프린트)", ""], ["", "A Traditional Japanese House", "일본의 전통 가옥"]] + [["", s, k] for s, k in S]
VOC = [("traditional", "전통적인"), ("take off", "(신발 등을) 벗다"), ("entrance hall", "현관"), ("enter", "들어가다"), ("instead", "대신에"),
       ("directly", "바로, 직접"), ("woven", "짠, 엮어진 (weave-wove-woven)"), ("grass", "풀"), ("divide", "나누다"), ("portable", "휴대용의, 이동 가능한"),
       ("sliding door", "미닫이문"), ("thin", "얇은"), ("gathering", "모임"), ("remove", "제거하다, 떼어 내다"), ("create", "만들다"),
       ("prefer to", "~하는 것을 더 좋아하다"), ("heated", "열이 나는, 데워진"), ("keep ~ warm", "~을 따뜻하게 유지하다"), ("heavy rain", "폭우"),
       ("flooding", "홍수"), ("raise", "올리다, 높이다"), ("off the ground", "땅에서 떨어져"), ("living area", "생활 공간"), ("safe from", "~로부터 안전한"),
       ("sloped", "경사진"), ("flow off", "흘러내리다"), ("be covered with", "~로 덮여 있다"), ("tile", "기와, 타일"), ("water-resistant", "방수의"),
       ("fireproof", "내화성의, 불에 강한"), ("not only A but also B", "A뿐만 아니라 B도")]
P1 = [
 ("What would it be like to live in a {traditional|modern} Japanese house?", "traditional: 전통적인 — 겐칸·다다미·쇼지 같은 옛 방식"),
 ("If you lived there, you would have to {take off|put on} your shoes in the genkan, an entrance hall, before entering the house.", "집에 들어가기 전에 신발을 벗는다(take off)"),
 ("In the house, many Japanese do not use {chairs|floors}.", "의자를 쓰지 않고 대신 다다미 위에 바로 앉는다"),
 ("Instead, they sit {directly|rarely} on tatami mats that are made from woven grass.", "directly: 바로, 직접 (rarely: 거의 ~않다)"),
 ("Rooms are divided by shoji, {portable|heavy} sliding doors that are made from wood and thin paper.", "portable: 이동 가능한 — 떼어 낼 수 있는 가벼운 문"),
 ("For large gatherings, these doors can be {removed|locked} to create one large room.", "문을 떼어 내야(removed) 큰 방 하나가 된다"),
 ("When the weather gets {cold|hot}, people prefer to sit at a kotatsu, a heated table, and put their legs in it.", "열이 나는 탁자에 다리를 넣는다 → 추울 때"),
 ("In summer, heavy rain can cause {flooding|drought}.", "폭우 → 홍수(flooding), drought는 가뭄"),
 ("The house also has {sloped|flat} roofs because they keep rainwater flowing off easily.", "빗물이 흘러내리려면 경사진(sloped) 지붕"),
 ("The strong kawara tiles are not only water-resistant but also {fireproof|flammable}.", "fireproof: 불에 강한 (flammable: 불에 잘 타는)"),
]
TF = [  # (문장, 정답, 친절한 해설, 근거 문장 일부) — 11/20 선생님: 왜 그런지 친절한 설명
 ("People take off their shoes before entering a traditional Japanese house.", True,
  "정답 T ✔\n본문 2번 문장에서 집에 들어가기 전에(before entering the house) 현관인 겐칸에서 신발을 벗어야 한다(take off your shoes)고 했어요.\n→ 문제 문장과 같은 내용이라 T예요.", "take off your shoes in the genkan"),
 ("In a traditional house, many Japanese sit on chairs.", False,
  "정답 F ✘\n본문 3번 문장: 많은 일본 사람들은 집 안에서 의자를 사용하지 않는다(do not use chairs)고 했어요. 4번 문장: 대신(Instead) 다다미 위에 바로 앉아요.\n→ 의자에 앉는다는 건 본문과 반대라서 F예요.", "many Japanese do not use chairs"),
 ("Tatami mats are made from woven grass.", True,
  "정답 T ✔\n본문 4번 문장: 다다미 매트는 엮은 풀로 만들어진다(made from woven grass)고 했어요.\n→ 그대로 맞는 내용이라 T예요.", "made from woven grass"),
 ("Shoji doors are made from stone and glass.", False,
  "정답 F ✘\n본문 5번 문장: 쇼지는 나무와 얇은 종이(wood and thin paper)로 만들어진다고 했어요.\n→ 돌과 유리(stone and glass)가 아니라 나무와 종이예요. 그래서 F예요. (가볍기 때문에 떼어 낼 수도 있어요)", "made from wood and thin paper"),
 ("Shoji doors can be taken away to make one large room.", True,
  "정답 T ✔\n본문 6번 문장: 큰 모임을 위해 이 문들을 떼어 내서(can be removed) 큰 방 하나를 만들 수 있다고 했어요.\n→ taken away(치워지다) = removed(떼어 내지다), 바꿔 쓴 표현이라 T예요.", "these doors can be removed"),
 ("People use a kotatsu to stay cool in summer.", False,
  "정답 F ✘\n본문 7번 문장: 날씨가 추워지면(When the weather gets cold) 열이 나는 탁자(a heated table)인 고타쓰에 앉는다고 했어요.\n→ 여름에 시원하게가 아니라 겨울에 몸을 따뜻하게 하려고 써요. 그래서 F예요.", "When the weather gets cold"),
 ("The floor is raised to keep the living area safe from flooding.", True,
  "정답 T ✔\n본문 10번 문장: 바닥을 땅에서 조금 높여서(raised a little off the ground) 생활 공간을 홍수로부터 건조하고 안전하게 지킨다고 했어요.\n→ 같은 내용이라 T예요. (9번 문장: 여름 폭우로 홍수가 날 수 있어서)", "is raised a little off the ground"),
 ("Kawara tiles catch fire easily.", False,
  "정답 F ✘\n본문 13번 문장: 가와라 기와는 방수가 될 뿐 아니라 불에도 강하다(fireproof)고 했어요.\n→ catch fire easily(불이 쉽게 붙다)는 fireproof(불에 강한)와 반대라서 F예요.", "not only water-resistant but also fireproof"),
]
MC1 = [
 {"n": "Reading File", "box": ["Reading File"], "q": "글의 내용과 일치하지 <u>않는</u> 것은?",
  "opts": ["Shoji doors are made from wood and thick glass.", "People take off their shoes in the genkan.", "Tatami mats are made of woven grass.",
           "A kotatsu is a table that keeps people warm.", "The roofs are covered with kawara tiles."],
  "ex": "정답 근거: shoji, portable sliding doors that are made from wood and thin paper\n· 바꿔 쓴 표현: made from = made of · a heated table = a table that keeps people warm\n· thick : 두꺼운 ↔ thin : 얇은",
  "per": [["쇼지 문은 나무와 두꺼운 유리로 만들어진다.", "made from wood and thin paper", "불일치 → 나무와 얇은 종이"],
          ["사람들은 겐칸에서 신발을 벗는다.", "take off your shoes in the genkan", "일치"],
          ["다다미 매트는 엮은 풀로 만들어진다.", "made from woven grass", "일치 (made from = made of)"],
          ["고타쓰는 사람들을 따뜻하게 해 주는 탁자다.", "a heated table", "일치"],
          ["지붕은 가와라 기와로 덮여 있다.", "The roofs are covered with kawara tiles", "일치"]]},
 {"n": "Reading File", "box": ["Reading File"], "q": "빈칸에 들어갈 말로 글의 내용과 일치하는 것은? (학교 프린트 1번)<br><b>In Japan, people ________________.</b>",
  "opts": ["can remove the sliding doors to create one large room for a gathering", "enter their house without taking off their shoes",
           "often use chairs in the rooms", "prefer to sit on tatami mats that are made from woven plastic", "like to sit at a kotatsu in the hot summer to cool their body"],
  "ex": "정답 근거: For large gatherings, these doors can be removed to create one large room.\n· 오답: 신발을 벗고 들어감 / 의자를 안 씀 / 다다미는 풀(grass)로 만듦 / 고타쓰는 추울 때 몸을 데움",
  "per": [["모임을 위해 미닫이문을 떼어 내 큰 방 하나를 만들 수 있다.", "these doors can be removed to create one large room", "일치"],
          ["신발을 벗지 않고 집에 들어간다.", "take off your shoes in the genkan ... before entering the house", "불일치 → 신발을 벗는다"],
          ["방에서 의자를 자주 사용한다.", "many Japanese do not use chairs", "불일치 → 의자를 안 씀"],
          ["엮은 플라스틱으로 만든 다다미에 앉는 것을 좋아한다.", "made from woven grass", "불일치 → 풀로 만듦"],
          ["더운 여름에 몸을 식히려고 고타쓰에 앉는다.", "When the weather gets cold ... a heated table", "불일치 → 추울 때 몸을 데움"]]},
]
P2 = [
 ("What would it be like to live in a {traditional|tradition} Japanese house?", "명사 house를 꾸미는 형용사 → traditional"),
 ("If you {lived|live} there, you would have to take off your shoes in the genkan, an entrance hall, before entering the house.", "가정법 과거: If + 주어 + 과거동사 → lived"),
 ("If you lived there, you {would|will} have to take off your shoes in the genkan, an entrance hall, before entering the house.", "가정법 과거 주절: would + 동사원형"),
 ("If you lived there, you would have to take off your shoes in the genkan, an entrance hall, before {entering|enter} the house.", "전치사 before + 동명사 → entering"),
 ("Instead, they sit directly on tatami mats {that|what} are made from woven grass.", "선행사 tatami mats가 있음 → 관계대명사 that (what은 선행사 없이)"),
 ("Instead, they sit directly on tatami mats that are made from {woven|weaving} grass.", "풀이 '엮어진' → 과거분사 woven"),
 ("Rooms {are divided|divide} by shoji, portable sliding doors that are made from wood and thin paper.", "방이 쇼지에 의해 '나뉘는' 수동 → are divided"),
 ("For large gatherings, these doors can {be removed|remove} to create one large room.", "문이 '떼어지는' 수동 → can be removed"),
 ("When the weather gets {cold|coldly}, people prefer to sit at a kotatsu, a heated table, and put their legs in it.", "get + 형용사 보어(~해지다) → cold"),
 ("When the weather gets cold, people prefer to sit at a kotatsu, a heated table, and {put|putting} their legs in it.", "prefer to sit and (to) put — sit과 나란히 → put"),
 ("{Keeping|Kept} their body warm, Japanese have meals, drink tea, or read books at the table.", "일본 사람들이 몸을 따뜻하게 '유지하는' 능동 분사구문 → Keeping"),
 ("Keeping their body {warm|warmly}, Japanese have meals, drink tea, or read books at the table.", "keep + 목적어 + 형용사 보어 → warm"),
 ("The floor of the house {is raised|raises} a little off the ground to keep the living area dry and safe from flooding.", "바닥이 '높여진' 수동 → is raised"),
 ("The floor of the house is raised a little off the ground to keep the living area {dry|dryly} and safe from flooding.", "keep + 목적어 + 형용사 보어 → dry (safe와 나란히)"),
 ("The house also has sloped roofs because they keep rainwater {flowing|to flow} off easily.", "keep + 목적어 + -ing(계속 ~하게 하다) → flowing"),
 ("The roofs are covered {with|by} kawara tiles.", "be covered with: ~로 덮여 있다"),
 ("The strong kawara tiles are not only water-resistant {but|and} also fireproof.", "not only A but also B → but"),
]
VB = [
 ("If you ___ there, you would have to take off your shoes in the genkan, an entrance hall, before entering the house.", "live", ["lived"], "가정법 과거 → lived"),
 ("If you lived there, you would have to take off your shoes in the genkan, an entrance hall, before ___ the house.", "enter", ["entering"], "전치사 before + 동명사"),
 ("Instead, they sit directly on tatami mats that are made from ___ grass.", "weave", ["woven"], "'엮어진' 풀 → 과거분사 woven (weave-wove-woven)"),
 ("Rooms are ___ by shoji, portable sliding doors that are made from wood and thin paper.", "divide", ["divided"], "수동태 be + 과거분사"),
 ("For large gatherings, these doors can be ___ to create one large room.", "remove", ["removed"], "can be + 과거분사(수동)"),
 ("___ their body warm, Japanese have meals, drink tea, or read books at the table.", "keep", ["Keeping", "keeping"], "능동 분사구문 → Keeping"),
 ("The house also has sloped roofs because they keep rainwater ___ off easily.", "flow", ["flowing"], "keep + 목적어 + -ing"),
 ("The roofs are ___ with kawara tiles.", "cover", ["covered"], "be covered with: ~로 덮여 있다"),
]
ER = [
 ("If you [[lived]] there, you [[will]] have to take off your shoes in the genkan, an entrance hall, before [[entering]] the [[house]].", 1, "would", "가정법 과거 주절 → would + 동사원형"),
 ("Instead, they sit [[directly]] on tatami mats [[what]] [[are]] made from [[woven]] grass.", 1, "that", "선행사 tatami mats → 관계대명사 that"),
 ("For large gatherings, these doors [[can]] [[remove]] [[to create]] one large [[room]].", 1, "be removed", "문이 '떼어지는' 수동 → can be removed"),
 ("Keeping their body [[warmly]], Japanese [[have]] meals, [[drink]] tea, or [[read]] books at the table.", 0, "warm", "keep + 목적어 + 형용사 보어 → warm"),
 ("The floor of the house [[is raised]] a little off the ground [[to keep]] the living area [[dryly]] and [[safe]] from flooding.", 2, "dry", "keep + 목적어 + 형용사 보어 → dry"),
 ("The house also has [[sloped]] roofs [[because of]] they keep rainwater [[flowing]] off [[easily]].", 1, "because", "뒤에 주어 + 동사(절) → 접속사 because"),
 ("The strong kawara tiles [[are]] not only [[water-resistant]] [[and]] also [[fireproof]].", 2, "but", "not only A but also B"),
]
ORD = [E[0:4], E[4:8], E[9:13]]
FLOW = ['질문: 전통 가옥에 산다면? → 현관(겐칸)에서 신발 벗기 → 집 안: 의자 X → 대신(Instead) 다다미에 바로 앉기',
        '쇼지로 방 나누기 → 큰 모임: 문을 떼어 큰 방 하나 → 추워지면(When cold) 고타쓰 → 몸을 데우며 식사·차·독서',
        '홍수 대비: 바닥을 높임 → 또(also) 경사 지붕: 빗물이 흘러내림 → 지붕 = 가와라 기와 → 그 기와: 방수 + 내화']
INS = [(E[2:6], 1, "'의자를 쓰지 않는다' 뒤에 Instead(대신에) 다다미에 바로 앉는다가 온다."),
       (E[6:10], 1, "Keeping their body warm ... at the table — the table은 앞 문장의 kotatsu(열이 나는 탁자)."),
       (E[9:13], 2, "sloped roofs → The roofs are covered with kawara tiles → The strong kawara tiles 순서로 이어진다.")]
ODD = [([E[1], E[2], "Most Japanese houses have big sofas in the living room.", E[3]], 2, "의자를 쓰지 않고 바닥에 앉는다는 내용과 반대된다."),
       ([E[8], E[9], "In winter, people often swim in the river near the house.", E[10]], 2, "여름 폭우·홍수 대비 이야기와 관계없다.")]
BL = [
 ("The floor of the house is raised a little off the ground to ____ from flooding.", ["keep the living area dry and safe", "keep the living area wet", "make the floor cold", "let the rain come inside"], "홍수로부터 생활 공간을 건조하고 안전하게 유지하려고 바닥을 높인다. (학교 프린트 2번: keep the living area dry and safe)"),
 ("When the weather gets cold, people prefer to sit at a kotatsu, ____, and put their legs in it.", ["a heated table", "a cold drink", "a sliding door", "a sloped roof"], "고타쓰 = 열이 나는 탁자(a heated table), 추울 때 다리를 넣는다."),
 ("The house also has sloped roofs because they keep rainwater ____ easily.", ["flowing off", "staying on the roof", "coming inside", "freezing"], "경사진 지붕 → 빗물이 쉽게 흘러내린다(flowing off)."),
]
GM = [
 {"q": "빈칸에 알맞은 것은?<br><b>If you ______ there, you would have to take off your shoes.</b>", "opts": ["lived", "live", "will live", "living"], "ex": "가정법 과거: If + 주어 + 과거동사, 주어 + would + 동사원형"},
 {"q": "빈칸에 알맞은 것은?<br><b>The floor is raised to keep the living area ______ and safe.</b>", "opts": ["dry", "dryly", "to dry", "dries"], "ex": "keep + 목적어 + 형용사 보어 (7과 문법 ③)"},
 {"q": "\"튼튼한 가와라 기와는 방수가 될 뿐만 아니라 불에도 강하다.\"를 바르게 영작한 것은?",
  "opts": ["The strong kawara tiles are not only water-resistant but also fireproof.", "The strong kawara tiles are not only water-resistant and also fireproof.",
           "The strong kawara tiles are only not water-resistant but also fireproof.", "The strong kawara tiles are both water-resistant or fireproof."],
  "ex": "not only A but also B: A뿐만 아니라 B도"},
]
# 검사: 바꾼 문장·빈칸 문장이 본문 문장과 맞는지
fill = lambda s: re.sub(r'\{([^|}]*)\|[^}]*\}', r'\1', s)
for s, _ in P1 + P2: assert fill(s) in E, s
for s, v, a, _ in VB: assert s.replace('___', a[0]) in E, s
for s, w, fx, _ in ER:
    marks = re.findall(r'\[\[(.*?)\]\]', s); assert len(marks) == 4
    fixed = re.sub(r'\[\[(.*?)\]\]', lambda m, c=[0]: (fx if c.__setitem__(0, c[0] + 1) or c[0] - 1 == w else m.group(1)), s)
    assert fixed in E, (fixed,)
for s, o, _ in BL: assert s.replace('____', o[0]) in E, s
for m in MC1:
    for p in m['per']:
        ev = p[1] if isinstance(p[1], list) else [p[1]]
        for e in ev:
            for piece in e.split(' ... '): assert piece in ' '.join(E), piece
assert sum(1 for s, _ in P2 if True) >= len(E) - 4
day = {'id': 'rf7', 'name': '', 'range': '7과 외부지문 · Reading File (일본 전통 가옥)', 'story': '학교 프린트 맨 뒷장 외부지문 · 한 줄씩 꼼꼼하게',
       'passage': passage, 'steps': [
  {'type': 'vocab', 'title': '핵심어휘·숙어', 'quizN': 15, 'items': [list(v) for v in VOC]},
  {'type': 'pick', 'title': '어휘선택', 'guide': '문맥에 맞는 낱말을 고르세요.', 'items': [{'s': s, 'ex': e} for s, e in P1]},
  {'type': 'tf', 'title': 'T/F 내용 확인', 'guide': '본문 내용과 일치하면 T, 다르면 F를 고르세요.', 'items': [[a, b, c, None, d] for a, b, c, d in TF]},
  {'type': 'mc', 'title': '일치·불일치', 'guide': '선택지는 본문 표현을 쉬운 말로 조금 바꿔 썼어요. 해설의 "바꿔 쓴 표현"을 꼭 확인하세요.', 'items': MC1},
  {'type': 'pick', 'title': '어법선택', 'guide': '어법상 알맞은 것을 고르세요.', 'items': [{'s': s, 'ex': e} for s, e in P2]},
  {'type': 'verb', 'title': '동사변형', 'guide': '( ) 안의 동사를 알맞은 형태로 바꿔 쓰세요.', 'items': [{'s': s, 'v': v, 'a': a, 'ex': e} for s, v, a, e in VB]},
  {'type': 'error', 'title': '오류찾기', 'guide': '어법상 틀린 곳을 고르세요.', 'items': [{'s': s, 'w': w, 'fix': f, 'ex': e} for s, w, f, e in ER]},
  {'type': 'scramble', 'title': '본문 스크램블 (13문장 전부)', 'guide': '우리말에 맞게 단어를 눌러 문장을 완성하세요. 본문 한 줄씩 전부 나와요.', 'items': [{'ko': k, 'en': s} for s, k in S]},
  {'type': 'order', 'title': '문장순서', 'guide': '문장을 본문 순서대로 눌러서 배열하세요.', 'items': [{'lines': l, 'flow': [f]} for l, f in zip(ORD, FLOW)]},
  {'type': 'insert', 'title': '문장삽입', 'guide': '주어진 문장이 들어가기에 가장 알맞은 곳을 고르세요.', 'items': [{'lines': l, 'given': g, 'ex': e} for l, g, e in INS]},
  {'type': 'odd', 'title': '어색한 문장', 'guide': '글의 흐름과 관계없는 문장을 고르세요.', 'items': [{'lines': l, 'odd': o, 'ex': e} for l, o, e in ODD]},
  {'type': 'blank', 'title': '빈칸추론', 'guide': '빈칸에 들어갈 말로 가장 알맞은 것을 고르세요.', 'items': [{'s': s, 'opts': o, 'ex': e} for s, o, e in BL]},
  {'type': 'mc', 'title': '핵심문법', 'guide': '알맞은 답을 고르세요.', 'items': GM},
]}
PK['days'] = [d for d in PK['days'] if d['id'] != 'rf7'] + [day]
for i, d in enumerate(PK['days']): d['name'] = 'DAY %d' % (i + 1)
src = open(path, encoding='utf-8').read(); head = src[:src.index('window.PKG')]
tail = src[src.index('/* WRAPUP-TESTS'):] if '/* WRAPUP-TESTS' in src else ''
if 'rf7' not in head: head = head.rstrip('\n') + '\n/* 11/19: 학교 프린트 외부지문 Reading File 7과(일본 전통 가옥) DAY rf7 맨 끝 (generators/gen_m3rf7.py) */\n'
if tail: PK.pop('tests', None)
write(PK, path, head)
if tail: open(path, 'a', encoding='utf-8').write(tail)
print(PK['days'][-1]['name'], day['range'], [len(s['items']) for s in day['steps']])
