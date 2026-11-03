import sys, json, subprocess, re
sys.path.insert(0, '/home/claude/work/gen')
from gencommon import write
# 고1 능률(민병천) 3과 · 본문 완전정복 DAY 4~6 (11/3)
# ① 주요문장 덩어리 스크램블: 본문 전 문장을 의미 덩어리로 배열 (영작에 가까운 연습)
# ② 오류 사냥: 본문 단락 하나에 틀린 곳 N개 → 찾고(1점) 고쳐 쓰기(1점)

CH = {  # 본문 문장 → 덩어리 ( / 로 나눔)
 '❶': [
  "Children around the world / learned a bit more / about Korean culture / when writer Tae Keller / published her book / When You Trap a Tiger / in 2020.",
  "Its story starts / with a girl / who meets a tiger.",
  "Her grandmother / knows the tiger / as well.",
  "When her grandmother / gets sick, / the girl makes a deal / with the tiger.",
  "Keller's inspiration / for her award-winning book / was an old folktale / that her halmoni (grandmother) / used to tell her.",
  "It is called / \"The Sun and the Moon,\" / and it is about / a brother, a sister, / and a tiger.",
  "Keller wanted / to revive / the public's interest in tigers / by writing / her own book.",
 ],
 '❷': [
  "How is the tiger / related to / Korean culture?",
  "Long ago, / tigers were so abundant / in Korea / that people often called / the country / the \"Land of Tigers.\"",
  "It is estimated / that tigers lived in Korea / for at least / 100,000 years.",
  "The first appearance / of a tiger / in Korean culture / dates back to / the rock art / of the Bronze Age.",
  "It depicts / people hunting / various animals, / including tigers.",
  "Since then, / tigers have appeared / in many aspects / of Korean culture, / from legends / to art and musical instruments.",
  "Some of you / may have heard / Korean folktales / featuring tigers.",
  "In fact, / approximately forty percent / of Korean folktales / about animals / include a tiger.",
  "Tigers in Korean folktales / are sometimes shown / in a positive light / and sometimes / as foolish creatures.",
  "For example, / in one story, / a tiger helps a human / become rich / after the human / saves the tiger's life.",
 ],
 '❸': [
  "In another story, / a tiger hears / a mother tell / her crying baby, / \"Don't cry. / Here's a gotgam.\"",
  "Because the baby / stops crying, / the tiger mistakenly thinks / the gotgam is / a very scary creature / and runs away.",
  "It seems that / people at the time / had conflicting feelings / about tigers.",
  "They had respect / for tigers' / power and courage.",
  "However, / they were also / scared of tigers / because being injured / or even killed by tigers / was common / in the past.",
  "They may have made / tigers / into foolish characters / in order to / be less scared of them.",
  "Tigers in Korea / faced a decline in population / due to hunting / during the Joseon period / and nearly went extinct / during the Japanese colonial era.",
  "With the disappearance / of tigers in Korea, / their use / as a symbol of the nation / faded away.",
  "However, / their symbolism was revived / in modern times / through their selection / as the mascot / for both Olympics / hosted by Korea.",
  "Hodori was / the mascot / for the Seoul Summer Olympics / in 1988.",
  "It was / a Siberian tiger, / which represents / courage.",
  "The PyeongChang Winter Olympics / in 2018 / created Soohorang, / a white tiger, / as its mascot.",
  "White tigers / are considered / sacred guardians.",
 ],
 '❹': [
  "Tigers are also mentioned / in the K-pop song / \"Tiger is Coming.\"",
  "One verse of the song / is a reinterpreted version / of \"Sugungga,\" / which is / a traditional Korean song.",
  "The song drew / worldwide attention, / and its video / was viewed / millions of times / online.",
 ],
 '❺': [
  "These days, / only a few wild tigers / have been reported / to be living / in North Korea.",
  "However, / the history, stories, and cultural meaning / of tigers / still have a place / among modern Korean people.",
  "Who can deny / that the tiger / is a symbol / of Korea?",
  "In 2021, / the National Folk Museum of Korea / published a book / that collects / all the stories / about tigers in Korea.",
  "How about / looking for tigers / around you / now?",
 ],
}

# 오류 사냥: [[틀린 말|바른 말]] · why = 고친 이유 (차례대로)
HUNT = {
 '❶': ("Children around the world learned a bit more about Korean culture when writer Tae Keller [[has published|published]] her book When You Trap a Tiger in 2020. "
       "Its story [[start|starts]] with a girl [[which|who]] meets a tiger. Her grandmother knows the tiger as well. "
       "When her grandmother [[will get|gets]] sick, the girl makes a deal with the tiger. "
       "Keller's inspiration for her award-winning book was an old folktale that her halmoni (grandmother) used to [[telling|tell]] her. "
       "It [[calls|is called]] \"The Sun and the Moon,\" and it is about a brother, a sister, and a tiger. "
       "Keller wanted to revive the public's interest in tigers by [[write|writing]] her own book.",
       ["in 2020(명확한 과거) → 과거시제. 현재완료는 과거 시점 부사와 못 써요.", "주어 Its story(3인칭 단수) → starts", "선행사 a girl(사람) → 주격 관계대명사 who",
        "시간 부사절(When ~)은 미래도 현재시제", "used to + 동사원형 = ~하곤 했다 (be used to -ing와 구별)", "이야기가 '해님 달님'이라고 불린다 → 수동태 is called", "전치사 by 뒤 → 동명사 writing (~함으로써)"]),
 '❷': ("How [[does|is]] the tiger related to Korean culture? "
       "Long ago, tigers were so [[scarce|abundant]] in Korea that people often called the country the \"Land of Tigers.\" "
       "It [[estimates|is estimated]] that tigers lived in Korea for at least 100,000 years. "
       "The first appearance of a tiger in Korean culture [[date|dates]] back to the rock art of the Bronze Age. "
       "It depicts people [[hunted|hunting]] various animals, including tigers. "
       "Since then, tigers [[appeared|have appeared]] in many aspects of Korean culture, from legends to art and musical instruments. "
       "Some of you may have heard Korean folktales [[featured|featuring]] tigers. "
       "In fact, approximately forty percent of Korean folktales about animals [[includes|include]] a tiger. "
       "Tigers in Korean folktales are sometimes [[showing|shown]] in a positive light and sometimes as foolish creatures. "
       "For example, in one story, a tiger helps a human [[becoming|become]] rich after the human saves the tiger's life.",
       ["be related to(~와 관련되다)의 의문문 → How is ~ related", "[어휘] '호랑이의 땅'이라 불릴 만큼 → 많은(abundant). scarce는 '부족한'",
        "가주어 It ~ that: 사람들이 '추정한다' → 수동 It is estimated that", "주어 The first appearance(단수) → dates (of a tiger, in Korean culture는 꾸밈말)",
        "사람들이 '사냥하는' 모습 → 능동 현재분사 hunting", "Since then(그때부터 지금까지) → 현재완료 have appeared", "호랑이가 '등장하는' 설화 → 능동 현재분사 featuring",
        "percent of + 복수명사(folktales) → 복수 동사 include", "호랑이가 '보여지는' 것 → 수동 are shown", "help + 목적어 + (to) 동사원형 → become"]),
 '❸': ("In another story, a tiger hears a mother [[to tell|tell]] her crying baby, \"Don't cry. Here's a gotgam.\" "
       "Because the baby stops [[to cry|crying]], the tiger mistakenly thinks the gotgam is a very [[scared|scary]] creature and runs away. "
       "It seems [[what|that]] people at the time had conflicting feelings about tigers. They had respect for tigers' power and courage. "
       "However, they were also scared of tigers [[because of|because]] being injured or even killed by tigers [[were|was]] common in the past. "
       "They may have [[make|made]] tigers into foolish characters in order to be less scared of them. "
       "Tigers in Korea faced a decline in population due to hunting [[while|during]] the Joseon period and nearly went extinct during the Japanese colonial era. "
       "With the disappearance of tigers in Korea, their use as a symbol of the nation [[emerged|faded away]]. "
       "However, their symbolism was revived in modern times through their selection as the mascot for both Olympics [[hosting|hosted]] by Korea. "
       "Hodori was the mascot for the Seoul Summer Olympics in 1988. It was a Siberian tiger, [[that|which]] represents courage. "
       "The PyeongChang Winter Olympics in 2018 created Soohorang, a white tiger, as its mascot. White tigers are [[considering|considered]] sacred guardians.",
       ["지각동사 hear + 목적어 + 동사원형(tell)", "stop -ing = ~하던 것을 멈추다 (stop to ~ = ~하려고 멈추다)", "곶감이 '무서움을 주는' 존재 → scary (scared는 무서워하는)",
        "It seems that + 완전한 절 (~인 것 같다)", "뒤에 주어(being ~ tigers) + 동사(was)가 있는 절 → 접속사 because", "동명사 주어(being injured ~)는 단수 → was",
        "may have + 과거분사(made) = ~했을지도 모른다", "뒤에 명사(the Joseon period) → 전치사 during (while + 절)",
        "[어휘] 호랑이가 사라지면서(With the disappearance) 상징으로서의 쓰임도 '희미해졌다' → faded away. emerged는 '나타났다'",
        "올림픽이 한국에 의해 '개최된' → 수동 과거분사 hosted", "콤마 뒤 계속적 용법 → which (that은 콤마 뒤 ✗)", "백호가 수호자로 '여겨지는' → 수동 are considered"]),
 '❹': ("Tigers are also [[mentioning|mentioned]] in the K-pop song \"Tiger is Coming.\" "
       "One verse of the song is a [[reinterpreting|reinterpreted]] version of \"Sugungga,\" [[that|which]] is a traditional Korean song. "
       "The song [[drawn|drew]] worldwide attention, and its video was [[viewing|viewed]] millions of times online.",
       ["호랑이가 '언급되는' → 수동 are mentioned", "'재해석된' 버전 → 수동 과거분사 reinterpreted", "콤마 뒤 계속적 용법 → which",
        "and 뒤 was viewed와 같은 과거 → drew (draw - drew - drawn)", "영상이 '시청되는' → 수동 was viewed"]),
 '❺': ("These days, only [[a little|a few]] wild tigers have been [[reporting|reported]] to be living in North Korea. "
       "However, the history, stories, and cultural meaning of tigers still [[has|have]] a place among modern Korean people. "
       "Who can deny that the tiger is a symbol of Korea? "
       "In 2021, the National Folk Museum of Korea published a book that [[collect|collects]] all the stories about tigers in Korea. "
       "How about [[look|looking]] for tigers around you now?",
       ["셀 수 있는 복수명사(tigers) → a few (a little은 셀 수 없는 명사)", "호랑이가 '보고되는' → 수동 have been reported",
        "주어 the history, stories, and cultural meaning(셋, 복수) → have", "선행사 a book(단수) → collects", "How about + 동명사 → looking"]),
}

path = sys.argv[1] if len(sys.argv) > 1 else '/home/claude/proj/data/h1-ne-min-L3.js'
PK = json.loads(subprocess.check_output(['node', '-e', "global.window={};require('%s');process.stdout.write(JSON.stringify(window.PKG))" % path]))
base = [d for d in PK['days'] if not re.match(r'f\d$', d['id'])]
KO = {}
for d in base:
    for l in d['passage']:
        if l[0] != '#' and l[2]: KO[l[1]] = l[2]

def sec_passage(secs):
    out = []
    for d in base:
        on = False
        for l in d['passage']:
            if not l[0] and len(l[1]) == 1 and not l[2]: on = l[1] in secs
            if on: out.append(l)
    return out

def mkday(did, secs, rng):
    scr = []
    for s in secs:
        for c in CH[s]:
            en = c.replace(' / ', ' ')
            assert en in KO, (s, en)
            scr.append({'ko': KO[en], 'en': en, 'chunks': c.split(' / ')})
    hunt = []
    for s in secs:
        txt, why = HUNT[s]
        fixed = re.sub(r'\[\[([^|\]]*)\|([^\]]*)\]\]', r'\2', txt)
        want = ' '.join(c.replace(' / ', ' ') for c in CH[s])
        assert fixed == want, (s, fixed, want)
        n = len(re.findall(r'\[\[', txt)); assert n == len(why), (s, n, len(why))
        hunt.append({'label': '본문 ' + s, 's': txt, 'why': why})
    return {'id': did, 'name': 'DAY', 'range': '본문 완전정복 ' + rng, 'story': '주요문장 덩어리 배열 → 틀린 곳 ' + '·'.join(str(len(HUNT[s][1])) + '개' for s in secs) + ' 찾아 고치기',
            'passage': sec_passage(secs), 'steps': [
        {'type': 'scramble', 'title': '주요문장 덩어리 스크램블', 'guide': '우리말을 보고 의미 덩어리를 순서대로 눌러 문장 전체를 완성하세요. 영작하듯 머릿속으로 먼저 문장을 떠올려 보세요.', 'items': scr},
        {'type': 'hunt', 'title': '오류 사냥 · 틀린 곳 찾아 고치기', 'guide': '단락에서 틀린 곳을 정해진 개수만큼 찾고(1점), 바르게 고쳐 쓰세요(1점).', 'items': hunt}]}

NEW = [mkday('f1', ['❶', '❷'], '❶❷'), mkday('f2', ['❸'], '❸'), mkday('f3', ['❹', '❺'], '❹❺')]
PK['days'] = base + NEW
for i, d in enumerate(PK['days']): d['name'] = 'DAY %d' % (i + 1)
src = open(path, encoding='utf-8').read(); head = src[:src.index('window.PKG')]
tail = src[src.index('/* WRAPUP-TESTS'):] if '/* WRAPUP-TESTS' in src else ''
if '완전정복' not in head: head = head.rstrip('\n') + '\n/* 11/3: DAY 4~6 본문 완전정복(덩어리 스크램블 · 오류 사냥 hunt) gen/gen_h1l3full.py */\n'
tests = PK.pop('tests', None)
write(PK, path, head)
if tail: open(path, 'a', encoding='utf-8').write(tail)
print('ok', [(d['name'], d['range'], [len(s['items']) for s in d['steps']]) for d in PK['days']])
