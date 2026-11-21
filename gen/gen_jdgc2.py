# 11/21 저동고1 · 영어 기출 시험지 · 공통영어2 능률(민) 3~4과 · 2회 (비타민 영어클리닉, 25개교 기말 본문 출제 25문항) → h1-ne-min-L3 OMR
# 원본 work_src/jdgc2/src.pdf (답지 없음 → 직접 풀어 정답을 정함). 문제는 종이 시험지, 앱은 답 입력·채점·해설
# 배점(원본에 없음): 객관식 20문항 × 3점 = 60, 서술형 2(9)·6(6)·8(10)·18(5)·22(10) = 40 → 100
import json, re
DATA = '/home/claude/proj/data/h1-ne-min-L3.js'
C = '①②③④⑤'
def mc(n, src, stem, opts, ans, ex):
    return {'n': n, 'src': src, 'stem': stem, 'body': '', 'opts': opts, 'en': bool(re.search(r'[A-Za-z]{3}', ''.join(opts))), 'ans': C.index(ans),
            'ex': '정답 ▶ %s\n풀이 ▶ %s' % (ans, ex), 'ctx': '', 'pts': 3, 'words': [], 'kos': []}
def wr(n, src, stem, blanks, ex):
    pts = sum(b['pts'] for b in blanks)
    model = ' '.join(('%s %s' % (b['label'], b['ans'][0])).strip() for b in blanks)
    for b in blanks: b.setdefault('chk', []); b['note'] = False
    return {'kind': 'write', 'n': '서술형 %d' % n, 'src': src, 'pts': pts, 'stem': stem + ' <span class="pt">[%d점]</span>' % pts, 'body': '', 'blanks': blanks,
            'model': model, 'ex': ex, 'kos': []}
D3 = ['ⓐ', 'ⓑ', 'ⓒ', 'ⓓ', 'ⓔ']
items = [
 mc(1, '명일여고 · 3과', '다음 글의 주제로 가장 적절한 것은?',
    ['use of tiger motifs in Korean musical instruments', 'historical and cultural significance of animals in Korea', 'reasons for the historically high tiger population in Korea',
     'long-standing presence of tigers in Korean history and culture', 'different representations of tigers in modern Korean visual arts'], '④',
    '청동기 암각화부터 오늘날의 마스코트·작품까지 호랑이가 한국 문화에 오래 자리해 왔다는 글. ② 동물 전체로 너무 넓음 ①⑤ 일부 내용 ③ 개체 수가 많았던 이유는 없음'),
 wr(2, '명일여고 · 3과', '다음 글 (나)는 (가)를 재구성한 것이다. 문맥의 흐름상 빈칸 (A)~(C)에 들어갈 알맞은 단어를 조건에 맞게 적으시오.',
    [{'label': '(A)', 'pts': 3, 'ans': ['extinction']}, {'label': '(B)', 'pts': 3, 'ans': ['representing']}, {'label': '(C)', 'pts': 3, 'ans': ['emerged']}],
    '(A) drove them close to extinction — (가) nearly went extinct의 extinct를 명사로 (B) a friendly Siberian tiger representing courage — (가) which represents courage를 분사로 (C) Tigers have also recently emerged in popular music — (가) their symbolism emerged again (have + p.p.)\n채점 ▶ 빈칸당 3점. (가)에 쓰인 낱말의 형태만 바꿔 써야 해요(appeared는 (가)에 없어 0점).'),
 mc(3, '수원칠보고 · 3과', '다음 글에서 전체 흐름과 관계없는 문장은?', D3, '③',
    'ⓒ 고대 암각화가 조상의 생활 방식과 당시 날씨 연구에 도움이 된다는 내용은 호랑이와 한국 문화라는 흐름과 무관. ⓓ It = the rock art of the Bronze Age'),
 mc(4, '인천연송고 · 3과', '다음 빈칸에 들어갈 말로 가장 적절한 것은?',
    ['get mixed with the stories of other animals', 'are being forgotten due to rapid modernization', 'show signs of recovery in population worldwide',
     'continue to shape Korean identity and imagination', 'create confusion about the origins of Korean folktales'], '④',
    '야생 호랑이는 거의 없지만 여전히 한국인이 문화를 보는 방식에 영향을 주는 강력한 상징 → 호랑이의 역사·이야기·문화적 의미는 계속 한국인의 정체성과 상상력을 형성한다. 뒤의 "누가 호랑이가 한국의 상징임을 부정하겠는가?"와도 연결'),
 mc(5, '천안불당고 · 3과', '윗글의 밑줄 친 부분 중, 어법상 옳은 것은?', D3, '①',
    'ⓐ (are) sometimes shown ~ and sometimes described as ~ : shown과 병렬인 과거분사 → 옳음. ⓑ becoming → become(help + 목적어 + (to) 동사원형) ⓒ to tell → tell(지각동사 hear + 목적어 + 동사원형) ⓓ to cry → crying(울음을 그치다 stop -ing) ⓔ were → was(동명사구 주어 being injured ~는 단수)'),
 wr(6, '천안불당고 · 3과', '윗글의 빈칸 (A)와 (B)에 들어갈 적절한 연결어를 각각 영어로 순서대로 쓰시오.',
    [{'label': '(A)', 'pts': 3, 'ans': ['For example', 'For instance']}, {'label': '(B)', 'pts': 3, 'ans': ['However', 'But'], 'chk': ['Nevertheless', 'Still', 'On the other hand', 'Yet']}],
    '(A) 앞: 호랑이가 긍정적으로도, 어리석게도 그려짐 → 뒤: 그 예(사람을 부자로 만들어 주는 호랑이) → For example (B) 호랑이의 힘과 용기를 존경했다 ↔ 호랑이를 무서워하기도 했다 → However(교과서 원문은 But)\n채점 ▶ 빈칸당 3점. (A) For example / For instance (B) However / But 정답. Nevertheless·Still·Yet 등은 선생님 확인.'),
 mc(7, '천안여고 · 3과', '윗글의 밑줄 친 ⓐ~ⓔ 중에서 가리키는 대상이 어색한 것은?',
    ['ⓐ: when you trap a tiger', 'ⓑ: Tae Keller', 'ⓒ: Tae Keller', 'ⓓ: the rock art', 'ⓔ: tigers'], '②',
    'ⓑ the girl = 책 속 이야기의 주인공 소녀(호랑이를 만나는 소녀)이지 작가 Tae Keller가 아님. ⓐ Its = 책 When You Trap a Tiger ⓒ her = Keller(할머니가 들려준 대상) ⓓ It = 청동기 암각화 ⓔ they = tigers'),
 wr(8, '천안여고 · 3과', '윗글의 밑줄 친 우리말을 &lt;보기&gt;의 단어들을 활용하여 &lt;조건&gt;에 맞게 완성하시오. (Long ago, 뒤에 이어지는 15단어)',
    [{'label': '', 'pts': 10, 'ans': ['tigers were so abundant in Korea that people called the country the land of tigers', 'tigers were so abundant in Korea that people called the country "the land of tigers"'],
      'chk': ['tigers were so abundant in Korea that people often called the country the land of tigers']}],
    '모범 답안 ▶ (Long ago,) tigers were so abundant in Korea that people called the country the Land of Tigers.\nso + 형용사 + that ~ (너무 ~해서 …하다) · abundance → abundant, be → were, call → called(과거) · call + 목적어 + 목적격보어(the Land of Tigers) · 15단어\n채점 ▶ 10점. 단어 순서·형태가 모범 답안과 같아야 정답. 대소문자는 상관없어요. often을 넣으면 16단어라 선생님 확인.'),
 mc(9, '천안청수고 · 3과', '다음 글의 흐름으로 보아 주어진 문장이 들어가기에 가장 적절한 곳은?', ['(A)', '(B)', '(C)', '(D)', '(E)'], '⑤',
    '사람들은 호랑이에 대해 엇갈린 감정이 있었다 → (D) 뒤 "힘과 용기를 존경했다" → (E) 그러나 호랑이를 무서워하기도 했다(주어진 문장) → 그래서 덜 무서워하려고 호랑이를 어리석은 캐릭터로 만들었을지 모른다. But ~ also가 존경과 대비'),
 mc(10, '청란여고 · 3과', '다음 글의 문장 ⓐ~ⓕ 중, 어법상 어색한 것이 있는 문장을 있는 대로 고른 것은?', ['ⓐ, ⓒ', 'ⓑ, ⓕ', 'ⓓ, ⓔ', 'ⓐ, ⓓ, ⓕ', 'ⓑ, ⓓ, ⓔ'], '④',
    'ⓐ , that → , which(관계대명사 that은 콤마 뒤 계속적 용법 X) ⓓ has → have(주어 the history, stories, and cultural meaning은 복수) ⓕ where → that/which(뒤에 주어가 빠진 불완전한 절 → 관계대명사). ⓑ ⓒ ⓔ 맞음'),
 mc(11, '청란여고 · 3과', '다음 글의 밑줄 친 부분 중, 가리키는 것이 나머지 넷과 다른 하나는?', D3, '②',
    'ⓑ Her grandmother의 Her = 책 속 소녀. 나머지 ⓐ her book ⓒ her award-winning book ⓓ tell her ⓔ her own book은 모두 Tae Keller'),
 mc(12, '충북여고 · 3과', '다음 글의 목적으로 가장 적절한 것은?',
    ['호랑이 관련 전설과 예술 작품을 평가하려고', '호랑이가 한국 문화에 미친 영향을 설명하려고', '한국에서 호랑이 멸종 위기 상황을 경고하려고', '한국의 호랑이 보호 정책의 필요성을 주장하려고', '청동기 시대 암벽화의 예술적 가치를 평가하려고'], '②',
    'How is the tiger related to Korean culture?라고 묻고, 호랑이가 많았던 옛날부터 암각화·전설·예술·악기에 등장해 온 것을 설명함'),
 mc(13, '별가람고 · 4과', '다음 밑줄 친 ⓐ에 해당되는 것만을 &lt;보기&gt;에서 있는 대로 고른 것은?', ['(A), (B)', '(C), (E)', '(A), (C), (D)', '(B), (D), (E)', '(C), (D), (E)'], '③',
    'ⓐ 자연이 문제의 해결책을 주었을 수 있다 → 자연이 환경 문제를 해결해 준 예: (A) 습지가 오염을 가둬 물을 깨끗이 함 (C) 맹그로브가 탄소를 흡수하고 홍수를 막음 (D) 숲이 이산화탄소를 흡수해 공기를 깨끗이 함. (B) 녹는 빙하로 해수면 상승 (E) 가뭄으로 공기가 더러워짐 → 해결책이 아니라 문제'),
 mc(14, '인천연송고 · 4과', '윗글의 빈칸 (A)에 들어갈 말로 가장 적절한 것은?', ['For example', 'In addition', 'In other words', 'On the contrary', 'In the same way'], '②',
    '오염된 흙을 파서 매립지로 옮기는 것은 비싸다 + (게다가) 문제를 다른 곳으로 옮길 뿐 해결하지 못한다 → 단점을 덧붙임: In addition(교과서 원문 Moreover)'),
 mc(15, '인천연송고 · 4과', '윗글의 밑줄 친 this promising area가 의미하는 바로 가장 적절한 것은?',
    ['discovering the major causes of soil pollution in various industries', 'identifying which willow species best remove harmful materials', 'developing fertilizers that improve crop growth in acidic soil',
     'classifying and documenting microorganisms found in soil', 'innovating soil-purifying techniques for various pollutants'], '②',
    '어떤 버드나무 종이 해로운 물질을 더 잘 흡수하는지(some species ~ absorb harmful materials better than others) → 어느 나무가 가장 효과적인지 알아내기 위해 더 연구해야 할 분야'),
 mc(16, '창원남산고 · 4과', '다음 글의 빈칸에 들어갈 말로 가장 적절한 것은?',
    ['Nature continues to contribute', 'Nature barely plays a role in modern approaches', 'The destruction of nature has given rise', 'Nature offers several innovative solutions', 'Human activities continue to pose serious threats'], '④',
    '빈칸 뒤 밀웜(플라스틱 분해)·버드나무(흙 정화)·조류(바이오 연료) 예시 → 자연이 환경 문제에 대한 혁신적인 해결책을 제공한다. ① contribute to environmental issues는 환경 문제를 \'일으킨다\'는 뜻이 됨 ③⑤ 문제 원인 ② 반대'),
 mc(17, '천안불당고 · 4과', '다음 글의 밑줄 친 부분 중, 어법상 옳은 것은?', D3, '④',
    'ⓓ in which(= where) + 완전한 절(it is just dumped or burned) → 옳음. ⓐ discard → discarded(are used ~ and then discarded, 수동) ⓑ reducing → reduce(help + (to) 동사원형) ⓒ has → have(percent of 뒤 the amounts(복수)에 수 일치) ⓔ ends → end(between 8 and 14 million metric tons 복수)'),
 wr(18, '천안불당고 · 4과', '다음 빈칸에 들어갈 말로 가장 적절한 말을 영어 한 단어로 쓰시오.',
    [{'label': '', 'pts': 5, 'ans': ['destruction']}],
    '인간이 자연 \'파괴\'의 주요 원인이다(a major contributor to the destruction of nature). 앞의 해수면 상승·자연재해·쓰레기·플라스틱 오염\n채점 ▶ 5점. destruction만 정답.'),
 mc(19, '천안여고 · 4과', '윗글의 빈칸 (A), (B), (C)에 들어갈 말로 가장 적절한 것은?', ['at / in / into', 'at / on / into', 'from / in / by', 'from / on / by', 'by / in / by'], '④',
    '(A) stop A from -ing(A가 ~하는 것을 막다) (B) feed on(~을 먹고 살다) (C) by -ing(~함으로써)'),
 mc(20, '천안여고 · 4과', '윗글의 밑줄 친 부분 중, 어법상 어색한 것은?', D3, '②',
    'ⓑ dug up and transport → transported(can be dug up and transported, 수동태 병렬). ⓐ ⓒ ⓓ ⓔ 문장은 어법상 맞음'),
 mc(21, '천안여고 · 4과', '윗글의 내용과 일치하는 것은?',
    ['Soil pollution can be addressed at a low cost.', "We're facing serious environmental challenges.", 'Only humans can solve environmental problems.',
     'Less than 8 millions metric tons of plastic are thrown away every year.', '2 billion people drink coffee every day, out of a global population of 8 billion.'], '②',
    'Our environment is in trouble. → 심각한 환경 문제에 직면해 있다. ① 흙을 파서 옮기는 방법은 비싸고, 버드나무는 비용 효율적(cost-effective)이라고만 함 ③ 자연이 해결책을 줌 ④ 매년 800만~1,400만 톤이 바다로 감 ⑤ 세계 인구의 30~40%가 매일 커피를 마심(25%가 아님)\n참고 ▶ 답지가 없어 직접 풀어 정한 답이에요. ①은 버드나무가 cost-effective하다는 말 때문에 맞다고 볼 학생이 있을 수 있어요.'),
 wr(22, '천안여고 · 4과', '윗글의 밑줄 친 우리말과 일치하도록 &lt;보기&gt;의 단어들을 활용하여 &lt;조건&gt;에 맞게 영작하시오. (Often, 뒤에 이어지는 12단어)',
    [{'label': '', 'pts': 10, 'ans': ['plastic waste is moved to places where it is dumped or burned'],
      'chk': ['plastic waste is moved to places where it is burned or dumped', 'often, plastic waste is moved to places where it is dumped or burned', 'plastic waste is moved to places where it is dumped or burnt']}],
    '모범 답안 ▶ (Often,) plastic waste is moved to places where it is dumped or burned.\n관계부사 where(= in which) · move → is moved(수동) · place → places · dump/burn → is dumped or burned · 12단어\n채점 ▶ 10점. 모범 답안과 같아야 정답. 순서를 바꾼 burned or dumped, Often,을 넣은 답, burnt는 선생님 확인.'),
 mc(23, '천안청수고 · 4과', '다음 글의 밑줄 친 ⓐ~ⓔ의 의미로 어색한 것은?',
    ['ⓐ: to go to someone or something for help, advice, or support', 'ⓑ: to separate something into simpler materials', 'ⓒ: to eat a particular food or substance as a regular part of its diet',
     'ⓓ: to prevent something from growing or developing properly', 'ⓔ: a series of actions that produce something or that lead to a particular result'], '④',
    'ⓓ cultivate = 기르다, 배양하다(to grow or raise something). 주어진 풀이(제대로 자라지 못하게 막다)는 반대. ⓐ turn to 의지하다 ⓑ break down 분해하다 ⓒ feed on 먹고 살다 ⓔ process 과정'),
 mc(24, '청원여고 · 4과', '다음 글의 밑줄 친 ⓐ~ⓗ 중, 어법상 옳은 것끼리 짝지어진 것은?', ['ⓐ, ⓑ, ⓒ, ⓔ', 'ⓑ, ⓒ, ⓕ, ⓖ', 'ⓑ, ⓓ, ⓔ, ⓖ', 'ⓒ, ⓓ, ⓕ, ⓗ', 'ⓓ, ⓔ, ⓖ, ⓗ'], '③',
    '옳은 것: ⓑ where these plastic items go(간접의문문) ⓓ in which + 완전한 절 ⓔ With this in mind(이것을 염두에 두고) ⓖ by which + 완전한 절. 틀린 것: ⓐ discard → discarded ⓒ have recycled → has been recycled(waste는 단수, 재활용"되다") ⓕ to be cultivated the bacteria → to cultivate the bacteria ⓗ keeping → keep'),
 mc(25, '충북여고 · 4과', '다음 글의 흐름으로 보아, 주어진 문장이 들어가기에 가장 적절한 곳은?', ['(A)', '(B)', '(C)', '(D)', '(E)'], '④',
    'This ability = 흙에서 다양한 해로운 물질을 자연스럽게 뽑아내는 능력 → (C) 뒤 문장 바로 다음 (D). 뒤의 They can also grow quickly ~가 또 다른 장점(also)으로 이어짐'),
]
assert len(items) == 25 and sum(i['pts'] for i in items) == 100
T = {'id': 'jd-gc2', 'title': '영어 기출 시험지 · 공통영어2 능률(민) 3~4과 · 2회', 'short': '기출 2회', 'school': '저동고 1학년', 'minutes': 50, 'items': items}
js = open(DATA, encoding='utf-8').read()
blk = ('/* GICHUL-TESTS: gen/gen_jdgc2.py 로 만듦 (손으로 고치지 말 것) */\nwindow.PKG.tests = (window.PKG.tests || []).filter(function (t) { return t.id !== %s; }).concat(%s);\n/* /GICHUL-TESTS */\n'
       % (json.dumps(T['id']), json.dumps([T], ensure_ascii=False)))
if '/* GICHUL-TESTS' in js: js = re.sub(r'/\* GICHUL-TESTS.*?/\* /GICHUL-TESTS \*/\n', lambda m: blk, js, flags=re.S)
else: js = js.rstrip('\n') + '\n' + blk
open(DATA, 'w', encoding='utf-8').write(js)
print('OK', ''.join(C[i['ans']] if 'ans' in i else '서' for i in items))
