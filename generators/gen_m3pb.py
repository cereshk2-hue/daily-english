# 11/20 11:14 중산중3 외부지문 2 「Picture Bride」(Cathy Song, 1983 — 저작권 있음) → 앱 DAY (맨 끝, id pb1), 내용 비중 크게
# 시 원문은 싣지 않음: 본문 탭 = 칸별 장면 요약(내가 쓴 쉬운 영어 + 우리말), 원문은 학교 프린트 2·3쪽. 시와 4단어 이상 겹치는 문장 없는지 assert
import sys, json, re, subprocess
sys.path.insert(0, '/home/claude/srcrepo/generators')
from gencommon import write
path = sys.argv[1] if len(sys.argv) > 1 else '/home/claude/proj/data/m3-jihak-min-L7.js'
PK = json.loads(subprocess.check_output(['node', '-e', "global.window={};require('%s');process.stdout.write(JSON.stringify(window.PKG))" % path]))
SUM = [  # (칸, 쉬운 영어 요약, 우리말)
 (1, "The speaker's grandmother was only twenty-three at the time she moved away from Korea, just one year younger than the speaker is now.", '화자의 할머니는 스물셋에 한국을 떠났는데, 지금의 화자보다 겨우 한 살 어린 나이였다.'),
 (2, 'The speaker wonders if leaving her father\'s home was really that easy for her grandmother.', '화자는 아버지의 집을 떠나는 일이 할머니에게 정말 그렇게 쉬웠을지 궁금해한다.'),
 (3, 'She walked past the tailor shops in Pusan to reach the port.', '할머니는 부산의 양복점들을 지나 항구까지 갔다.'),
 (4, 'A ship was going to carry her across the sea to Hawaii, a place she barely knew.', '배는 할머니를 거의 알지 못하는 곳, 하와이의 한 섬으로 데려갈 예정이었다.'),
 (5, 'On that island, a man was holding her picture up to the light while he waited for her.', '그 섬에서는 한 남자가 할머니의 사진을 빛에 비춰 보며 그녀를 기다리고 있었다.'),
 (6, 'He lived in a workers\' camp near the Waialua Sugar Mill, where lamps came on in the evening.', '그는 와이알루아 설탕 공장 근처의 노동자 숙소에 살았고, 저녁이면 그곳에 등불이 켜졌다.'),
 (7, 'Moths from the sugarcane fields made his small room seem to glow.', '사탕수수 밭에서 날아온 나방들 때문에 그의 작은 방이 빛나는 것처럼 보였다.'),
 (8, 'The speaker cannot know what her grandmother packed for the trip.', '화자는 할머니가 여행을 위해 무엇을 챙겼는지 알 수 없다.'),
 (9, 'When she arrived, she met her husband for the first time. He was a stranger, and he was 13 years her senior.', '도착했을 때 할머니는 남편을 처음 만났다. 그는 낯선 사람이었고, 열세 살이나 많았다.'),
 (10, 'Perhaps she carefully loosened the ribbon on her Korean jacket in front of him.', '아마도 할머니는 그 앞에서 한복 저고리의 고름을 조심스럽게 풀었을 것이다.'),
 (11, 'Hot, dry wind from the burning sugarcane fields blew her long skirt out like a tent.', '사탕수수를 태우는 들판에서 불어온 뜨겁고 건조한 바람이 그녀의 긴 치마를 텐트처럼 부풀렸다.'),
]
POEM = """She was a year younger than I, twenty-three when she left Korea. Did she simply close the door of her father's house and walk away. And was it a long way through the tailor shops of Pusan to the wharf where the boat waited to take her to an island whose name she had only recently learned, on whose shore a man waited, turning her photograph to the light when the lanterns in the camp outside Waialua Sugar Mill were lit and the inside of his room grew luminous from the wings of moths migrating out of the cane stalks? What things did my grandmother take with her? And when she arrived to look into the face of the stranger who was her husband, thirteen years older than she, did she politely untie the silk bow of her jacket, her tent-shaped dress filling with the dry wind that blew from the surrounding fields where the men were burning the cane?"""
_w = lambda t: re.findall(r"[a-z'\-]+", t.lower().replace('’', "'"))
_pw = _w(POEM); _G = set(tuple(_pw[i:i + 4]) for i in range(len(_pw) - 3))
def nocopy(t):
    w = _w(t); bad = [' '.join(w[i:i + 4]) for i in range(len(w) - 3) if tuple(w[i:i + 4]) in _G]
    assert not bad, (t, bad)
passage = [['#', '외부지문 「Picture Bride」 · Cathy Song (학교 프린트)', ''],
           ['', 'Story summary — 원문은 학교 프린트 2쪽(시)·3쪽(해석)을 보세요', '아래는 프린트 3쪽 표 칸 순서대로 정리한 장면 요약이에요']]
for n, e, k in SUM:
    if n in (1, 5, 8): passage.append(['', {1: 'Part 1. Leaving Korea', 5: 'Part 2. A Man with Her Photograph', 8: 'Part 3. Meeting Her Husband'}[n], {1: '한국을 떠나다', 5: '사진을 든 남자', 8: '남편을 만나다'}[n]])
    passage.append(['', '(%d) %s' % (n, e), k])
VOC = [('picture bride', '사진신부'), ('wharf', '부두, 선창'), ('shore', '해안가'), ('tailor shop', '양복점'), ('island', '섬'), ('recently', '최근에'),
       ('lantern', '등불'), ('sugar mill', '설탕 공장'), ('light – lit – lit', '불을 켜다'), ('luminous', '빛나는'), ('moth', '나방'), ('migrate', '이동하다'),
       ('cane stalk', '사탕수수 줄기'), ('stranger', '낯선 사람'), ('politely', '예의 바르게'), ('untie', '풀다'), ('silk', '비단'), ('bow', '매듭, 고름'),
       ('tent-shaped', '텐트 모양의'), ('surrounding', '주변의'), ('immigrate', '이민 가다'), ('plantation', '대농장')]
TF = [  # (문장, 정답, 친절한 해설, 근거(본문 탭 요약 문장 일부)) — 11/20 선생님: 왜 그런지 친절한 설명
 ("The grandmother was twenty-three at the time of leaving Korea.", True,
  "정답 T ✔\n문장 해석 ▶ 할머니는 한국을 떠날 때 스물세 살이었다.\n시의 첫 부분(칸 1)에서 할머니가 한국을 떠날 때 스물셋이었다고 했어요.\n→ 그대로 맞는 내용이라 T예요. 학교 프린트 Activity 3의 1번 정답(23세)과 같아요.", "only twenty-three"),
 ("The speaker is younger than her grandmother was at the time of leaving Korea.", False,
  "정답 F ✘\n문장 해석 ▶ 화자는 한국을 떠날 때의 할머니보다 나이가 어리다.\n칸 1에서 할머니는 화자보다 한 살 어렸다고 했어요. 즉 화자가 할머니보다 한 살 많아요.\n→ 할머니가 23세였으니 화자는 24세예요. 화자가 더 어리다는 건 반대라서 F예요.", "just one year younger"),
 ("The grandmother got on the ship in Seoul.", False,
  "정답 F ✘\n문장 해석 ▶ 할머니는 서울에서 배를 탔다.\n칸 3에서 할머니는 부산(Pusan)의 양복점 거리를 지나 부두까지 갔다고 했어요.\n→ 배를 탄 곳은 서울이 아니라 부산이라서 F예요. (프린트 Activity 3의 2번 정답: 부산)", "tailor shops in Pusan"),
 ("The grandmother had known the island's name for many years.", False,
  "정답 F ✘\n문장 해석 ▶ 할머니는 그 섬의 이름을 여러 해 동안 알고 있었다.\n칸 4에서 할머니가 그 섬의 이름을 최근에야(only recently) 알게 되었다고 했어요.\n→ 오래전부터 알았던 게 아니라 얼마 전에야 안 낯선 곳이라 F예요. 할머니가 느꼈을 불안함을 보여 주는 부분이에요.", "a place she barely knew"),
 ("The man on the island had a photo of the grandmother.", True,
  "정답 T ✔\n문장 해석 ▶ 섬에 있는 남자는 할머니의 사진을 가지고 있었다.\n칸 5에서 섬의 해안에서 한 남자가 할머니의 사진을 빛에 비춰 보며 기다렸다고 했어요.\n→ 사진을 가지고 있었으니 T예요. 사진만 보고 결혼을 약속한 '사진신부'라는 제목과 연결돼요.", "holding her picture up to the light"),
 ("The man worked near a sugar mill.", True,
  "정답 T ✔\n문장 해석 ▶ 그 남자는 설탕 공장 근처에서 일했다.\n칸 6에서 남자는 와이알루아 설탕 공장(Sugar Mill) 밖의 숙소에서 지냈다고 했어요.\n→ 사탕수수 농장에서 일하는 노동자였다는 뜻이라 T예요.", "Waialua Sugar Mill"),
 ("The man's room became bright because of fireflies.", False,
  "정답 F ✘\n문장 해석 ▶ 남자의 방은 반딧불이 때문에 환해졌다.\n칸 7에서 방을 환하게 만든 것은 사탕수수 줄기에서 날아온 나방(moths)의 날개라고 했어요.\n→ 반딧불이(fireflies)가 아니라 나방이라서 F예요. 빛나는 방은 신부를 기다리는 남자의 설렘을 보여 줘요.", "Moths from the sugarcane fields"),
 ("The speaker knows exactly what her grandmother took with her.", False,
  "정답 F ✘\n문장 해석 ▶ 화자는 할머니가 무엇을 가지고 갔는지 정확히 알고 있다.\n칸 8에서 화자는 할머니가 어떤 물건들을 가지고 갔을지 묻기만 해요(질문).\n→ 화자는 답을 모르기 때문에 상상하며 묻는 거예요. '정확히 안다'는 건 반대라서 F예요.", "cannot know what her grandmother packed"),
 ("The grandmother and her husband had met many times before the wedding.", False,
  "정답 F ✘\n문장 해석 ▶ 할머니와 남편은 결혼 전에 여러 번 만난 적이 있었다.\n칸 9에서 할머니가 도착해 들여다본 남편의 얼굴은 낯선 사람(stranger)의 얼굴이었어요.\n→ 사진으로만 알던 사이라 그날 처음 만났어요. 여러 번 만났다는 건 반대라서 F예요. (프린트 Activity 3 B-2도 X)", "met her husband for the first time"),
 ("The grandmother was thirteen years younger than her husband.", True,
  "정답 T ✔\n문장 해석 ▶ 할머니는 남편보다 열세 살 어렸다.\n칸 9에서 남편은 할머니보다 열세 살 많았다고 했어요.\n→ 남편이 13살 많다 = 할머니가 13살 어리다, 같은 뜻이라 T예요. (3살·23살과 헷갈리지 않기)", "13 years her senior"),
 ("The grandmother was wearing Korean clothes when she met him.", True,
  "정답 T ✔\n문장 해석 ▶ 할머니는 그를 만났을 때 한복을 입고 있었다.\n칸 10에서 할머니가 저고리(jacket)의 비단 고름(silk bow)을 예의 바르게 풀었을까 하고 물어요.\n→ 고름이 있는 저고리, 즉 한복을 입고 있었으니 T예요.", "ribbon on her Korean jacket"),
 ("A cold, wet wind was blowing when she arrived.", False,
  "정답 F ✘\n문장 해석 ▶ 할머니가 도착했을 때 차갑고 축축한 바람이 불고 있었다.\n칸 11에서 남자들이 사탕수수를 태우던 들판에서 건조한(dry) 바람이 불어와 치마를 부풀렸다고 했어요.\n→ 차갑고 축축한 바람이 아니라 뜨겁고 건조한 바람이라 F예요. 앞으로 살아갈 거친 노동 현실을 암시해요.", "Hot, dry wind"),
 ("Most of the poem is made up of questions.", True,
  "정답 T ✔\n문장 해석 ▶ 시의 대부분은 질문으로 이루어져 있다.\n시는 '그저 떠났을까?', '먼 길이었을까?', '무엇을 가져갔을까?', '고름을 풀었을까?'처럼 거의 다 질문이에요.\n→ 화자가 직접 볼 수 없었던 할머니의 과거를 상상하며 궁금해하기 때문이에요. 그래서 T예요.", None),
]
MC = [
 {'q': '시의 내용과 일치하지 <u>않는</u> 것은?', 'opts': ['The man had never seen the grandmother\'s photo.', 'The grandmother left Korea from Pusan.', 'The man waited for her on an island.', 'The husband was much older than the grandmother.', 'Men were burning sugarcane in the fields.'],
  'ex': '정답 근거: 칸 5 — 남자는 그녀의 사진을 빛에 비춰 보며 기다렸다.\n· 나머지: 부산 출발(칸 3) · 섬에서 기다림(칸 5) · 13살 연상(칸 9) · 사탕수수를 태움(칸 11)'},
 {'q': '시의 내용과 일치하는 것은?', 'opts': ['The grandmother met a stranger who became her husband.', 'The grandmother traveled to Hawaii with her father.', 'The man worked in a tailor shop in Pusan.', 'The grandmother arrived on a cold winter night.', 'The speaker asked her grandmother many questions in person.'],
  'ex': '정답 근거: 칸 9 — 남편인 낯선 사람을 처음 만남.\n· 오답: 아버지의 집을 떠남(칸 2) / 양복점은 부산 거리(칸 3) · 남자는 설탕 공장 노동자 / 건조한 바람(칸 11) / 화자는 상상하며 물을 뿐 직접 묻지 않음'},
 {'q': '시의 화자는 누구인가?', 'opts': ['할머니의 손녀', '할머니의 남편', '할머니의 아버지', '설탕 공장 주인', '부산의 양복점 주인'], 'ex': '칸 8에서 my grandmother — 화자는 손녀, 할머니보다 한 살 많은 24세'},
 {'q': '시의 대부분이 의문문인 이유로 가장 알맞은 것은?', 'opts': ['화자가 직접 볼 수 없었던 할머니의 과거를 상상하며 궁금해하기 때문에', '할머니가 화자에게 퀴즈를 냈기 때문에', '남편이 할머니를 의심했기 때문에', '화자가 할머니를 비판하기 위해서', '독자에게 정답을 알려 주기 위해서'], 'ex': '화자는 답을 모르는 채 상상하며 묻는다 — 시에 답이 나오지 않음, 궁금증과 공감'},
 {'q': '\'그저(simply) 아버지 집의 문을 닫고 떠났을까?\'라는 물음에 담긴 화자의 생각은?', 'opts': ['그렇게 쉽게 떠날 수 있었을 리 없다', '할머니는 가족을 싫어했다', '할머니는 문을 잠그는 것을 잊었다', '아버지가 할머니를 쫓아냈다', '떠나는 일은 아주 신나는 일이었다'], 'ex': '칸 2 · \'그저\' — 이별이 그렇게 간단했을 리 없다는 마음, 이별의 무게'},
 {'q': '남자가 사진을 빛에 비춰 보는 모습에서 알 수 있는 것은?', 'opts': ['남자도 그녀를 사진으로만 알고 있고, 만남을 기대하며 설렌다', '남자는 사진가이다', '남자는 사진 속 여자를 싫어한다', '남자는 이미 그녀를 여러 번 만났다', '남자는 사진을 팔려고 한다'], 'ex': '칸 5 · 사진신부 — 서로 사진으로만 아는 사이, 기대·설렘'},
 {'q': '\'남편인 낯선 사람\'이라는 표현이 보여 주는 것은?', 'opts': ['남편이지만 처음 보는 사람이라는 아이러니', '남편이 외국인이라는 사실', '남편이 이름을 숨겼다는 사실', '두 사람이 어릴 때부터 친구였다는 사실', '남편이 할머니를 싫어했다는 사실'], 'ex': '칸 9 · 사진만 보고 결혼을 약속해 첫 만남의 날 남편은 아직 낯선 사람'},
 {'q': '마지막 장면의 건조한 바람과 불타는 사탕수수가 암시하는 것은?', 'opts': ['할머니가 앞으로 살아갈 거친 노동 현실', '할머니 고향의 아름다운 풍경', '행복한 결혼식 축제', '남편의 부유한 생활', '화자가 사는 도시의 모습'], 'ex': '칸 11 · 뜨겁고 힘든 사탕수수 농장의 노동 환경이 할머니를 맞이함'},
 {'q': '할머니가 한국을 떠날 때의 마음으로 가장 알맞은 것은? (학교 프린트 Activity 5)', 'opts': ['sad and nervous', 'happy and relaxed', 'bored and sleepy', 'proud and angry', 'excited and calm'], 'ex': '가족·고향을 떠나 처음 보는 사람과 결혼하러 낯선 나라로 감 → 슬프고 긴장됨 (scared, lonely도 근거가 맞으면 가능)'},
 {'q': '「Picture Bride(사진신부)」라는 제목의 뜻으로 알맞은 것은?', 'opts': ['사진만 보고 결혼을 약속해 먼 나라로 간 신부', '사진을 찍는 일을 하는 신부', '결혼식 사진 속의 신부', '사진관을 운영한 신부', '사진을 모으는 취미를 가진 신부'], 'ex': '1910~1924년 하와이로 간 한국 여성들 — 남자들이 보낸 사진만 보고 결혼을 약속'},
]
ORD = [[SUM[0][1], SUM[2][1], SUM[3][1], SUM[4][1]], [SUM[4][1], SUM[5][1], SUM[6][1], SUM[8][1]], [SUM[7][1], SUM[8][1], SUM[9][1], SUM[10][1]]]
SCENE = ["The grandmother leaves her home in Korea.", "She takes a ship to an island she hardly knows.", "A man waits for her, looking at her photo.", "She finally meets the stranger who is her husband."]
ORD.append(SCENE)
FLOW = ['23세에 한국을 떠남 → 부산 양복점 거리 지나 항구로 → 배 타고 낯선 하와이로 → 섬에서 사진 든 남자가 기다림',
        '사진을 빛에 비춰 보며 기다리는 남자 → 설탕 공장 숙소, 저녁 등불 → 나방 날개로 빛나는 방 → 도착: 낯선 남편과 첫 만남',
        '무엇을 챙겼을까? (질문) → 도착: 13살 많은 낯선 남편 → 예의 바르게 고름을 풂 → 건조한 바람에 부푼 치마',
        '집을 떠남 → 배·이름도 낯선 섬 → 사진 든 남자의 기다림 → 낯선 남편과의 만남']
ODD = [([SUM[2][1], SUM[3][1], "The grandmother had visited Hawaii many times as a child.", SUM[4][1]], 2, '섬은 이름도 최근에 안 낯선 곳 — 어릴 때 여러 번 갔다는 말은 흐름과 맞지 않아요.'),
       ([SUM[8][1], SUM[9][1], "Her husband gave her a big birthday party that night.", SUM[10][1]], 2, '첫 만남의 어색함·거친 바람 장면에 생일 파티는 관계없어요.')]
BL = [("The grandmother was a ____ who married a man she knew only from a photo.", ['picture bride', 'tailor', 'sugar worker', 'teacher'], '사진만 보고 결혼한 신부 = picture bride'),
      ("The man lived and worked near a ____ in Hawaii.", ['sugar mill', 'tailor shop', 'school', 'hospital'], '칸 6 · 와이알루아 설탕 공장(sugar mill)'),
      ("The husband was a ____ to her when she first saw his face.", ['stranger', 'brother', 'neighbor', 'classmate'], '칸 9 · 남편이지만 처음 보는 낯선 사람'),
      ("Because the speaker can only imagine the past, most of the poem is written as ____.", ['questions', 'orders', 'jokes', 'letters'], '시 전체가 의문문 — 화자가 상상하며 묻는다'),
      ("The speaker was ____ years old when she wrote about her grandmother.", ['twenty-four', 'twenty-two', 'thirteen', 'thirty-six'], '칸 1 · 할머니(23세)보다 한 살 많음 → 24세')]
PICK = [("The ship sat at the {wharf|forest}, ready to leave for the island.", 'wharf: 부두 — 배가 기다리는 곳'),
        ("The man stood on the {shore|roof} of the island and waited.", 'shore: 해안가'),
        ("The lanterns were {lit|dark} in the evening.", 'lit: 불이 켜진 (light – lit – lit)'),
        ("The room looked {luminous|empty} because of the moths' wings.", 'luminous: 빛나는'),
        ("Her new husband was really a {stranger|friend} to her.", 'stranger: 낯선 사람 — 처음 보는 남편'),
        ("She {politely|rudely} untied the ribbon on her Korean top.", 'politely: 예의 바르게 — 조심스러운 첫 만남'),
        ("Moths flew from the {sugarcane|tailor shops} around the camp.", 'sugarcane: 사탕수수')]
GM = [{'q': '빈칸에 알맞은 것은?<br><b>I visited a town ______ name I had never heard before.</b>', 'opts': ['whose', 'who', 'where', 'what'], 'ex': '명사(name) 앞 소유격 관계대명사 whose — 시 칸 4·5에도 섬을 꾸미는 whose가 두 번 나옴'},
      {'q': '빈칸에 알맞은 것은?<br><b>This is the port ______ the ship was waiting for us.</b>', 'opts': ['where', 'which', 'whose', 'what'], 'ex': '장소 + 완전한 문장 → 관계부사 where (시 칸 4: 부두를 꾸미는 where)'},
      {'q': '빈칸에 알맞은 것은?<br><b>He waited by the door, ______ her photo in his hand.</b>', 'opts': ['holding', 'held', 'to hold', 'holds'], 'ex': '분사구문(동시동작) -ing — 시 칸 5: 사진을 돌려 보며 기다림'},
      {'q': '빈칸에 알맞은 것은?<br><b>She walked on, her skirt ______ with the wind.</b>', 'opts': ['filling', 'filled', 'to fill', 'fills'], 'ex': '독립분사구문 명사 + -ing — 시 칸 11: 바람에 부푼 치마'}]
for s_ in [e for _, e, _ in SUM] + [t[0] for t in TF] + FLOW + [o for m in MC for o in m['opts']] + SCENE + [l for l, _, _ in ODD for l in l] + [b[0] for b in BL] + [p[0] for p in PICK] + [g['q'] for g in GM]:
    nocopy(re.sub(r'\{([^|}]*)\|[^}]*\}', r'\1', s_))
def tfx(c, b):  # 정답 / 문장 해석 / 본문 ▶ / 왜 T·F? ▶ 로 줄 이름 붙이기
    L = c.split('\n'); L[2] = '본문 ▶ ' + (L[2][3:] if L[2].startswith('본문 ') else L[2])
    return '\n'.join(L).replace('\n→ ', '\n왜 %s일까? ▶ ' % ('T' if b else 'F'))

day = {'id': 'pb1', 'name': '', 'range': '외부지문 2 · Picture Bride (사진신부, 시)', 'story': '학교 프린트 외부지문 시 · 내용·숨은 뜻·이야기 흐름 중심 (원문은 프린트 2·3쪽)',
       'passage': passage, 'steps': [
  {'type': 'vocab', 'title': '핵심어휘', 'quizN': 15, 'items': [list(v) for v in VOC]},
  {'type': 'tf', 'title': 'T/F 내용 확인', 'guide': '시의 내용과 일치하면 T, 다르면 F를 고르세요. (칸 번호 = 학교 프린트 3쪽 표 순서)', 'items': [[a, b, tfx(c, b), None, d] if d else [a, b, tfx(c, b)] for a, b, c, d in TF]},
  {'type': 'mc', 'title': '내용 일치 · 숨은 뜻', 'guide': '시의 내용과 숨은 뜻을 생각하며 답을 고르세요.', 'items': MC},
  {'type': 'order', 'title': '이야기 순서', 'guide': '장면을 이야기 순서대로 눌러서 배열하세요.', 'items': [{'lines': l, 'flow': [f]} for l, f in zip(ORD, FLOW)]},
  {'type': 'odd', 'title': '흐름과 관계없는 문장', 'guide': '이야기 흐름과 관계없는 문장을 고르세요.', 'items': [{'lines': l, 'odd': o, 'ex': e} for l, o, e in ODD]},
  {'type': 'blank', 'title': '내용 빈칸', 'guide': '시의 내용에 맞게 빈칸에 들어갈 말을 고르세요.', 'items': [{'s': s, 'opts': o, 'ex': e} for s, o, e in BL]},
  {'type': 'pick', 'title': '어휘선택', 'guide': '시의 장면에 맞는 낱말을 고르세요.', 'items': [{'s': s, 'ex': e} for s, e in PICK]},
  {'type': 'mc', 'title': '구조 확인 (새 문장)', 'guide': '시에 나온 구조를 새 문장으로 확인해요.', 'items': GM},
]}
PK['days'] = [d for d in PK['days'] if d['id'] != 'pb1'] + [day]
for i, d in enumerate(PK['days']): d['name'] = 'DAY %d' % (i + 1)
src = open(path, encoding='utf-8').read(); head = src[:src.index('window.PKG')]
tail = src[src.index('/* WRAPUP-TESTS'):] if '/* WRAPUP-TESTS' in src else ''
if 'pb1' not in head: head = head.rstrip('\n') + '\n/* 11/20: 외부지문 2 Picture Bride DAY pb1 맨 끝 (generators/gen_m3pb.py, 원문 없이 장면 요약) */\n'
if tail: PK.pop('tests', None)
write(PK, path, head)
if tail: open(path, 'a', encoding='utf-8').write(tail)
print(day['name'] if False else PK['days'][-1]['name'], [len(s['items']) for s in day['steps']])
