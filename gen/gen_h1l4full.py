import sys, json, subprocess, re
sys.path.insert(0, '/home/claude/work/gen')
from gencommon import write
# 고1 능률(민병천) 4과 · 본문 완전정복 DAY 10~12 (11/10) — 3과 완전정복(gen_h1l3full.py)과 같은 방식
# ① 주요문장 덩어리 스크램블 ② 오류 사냥(찾기 1점 + 고치기 1점)

CH = {
 '❶': [
  "Our environment / is in trouble.",
  "With the planet / becoming warmer, / sea levels are rising / and natural disasters / such as forest fires and floods / are increasing.",
  "More and more waste / is also being produced.",
  "Plastic, in particular, / is causing problems / with soil and water pollution.",
  "It is clear / that humans are / a major contributor / to the destruction of nature.",
  "Will we be able / to protect the environment / from mountains of plastic?",
  "Can we stop / climate change / from reaching / dangerous levels?",
  "Achieving these goals / seems difficult.",
  "Nature, however, / may have provided us / with solutions / to these problems.",
  "Here are / three areas / where changes / are already happening.",
 ],
 '❷': [
  "About fifty percent of plastic / is produced / for single-use products.",
  "That means / the items are used / just once / and then discarded.",
  "Do you ever stop / to think about / where these plastic items go / after you throw them away?",
  "Recycling can help / reduce the amount of plastic / in our landfills.",
  "However, / less than ten percent / of the world's plastic waste / has been recycled / so far.",
  "Often, / plastic waste is moved / to places / where it is just / dumped or burned.",
  "Furthermore, / between 8 and 14 million metric tons / of plastic / end up in the ocean / every year.",
  "This puts / many marine species / in danger.",
  "With this in mind, / scientists are turning / to mealworms.",
  "Mealworms are / the larvae / of a certain species / of beetle.",
  "Special bacteria / live inside them.",
  "These bacteria / can break down / plastic.",
  "This means / that mealworms / can actually / feed on plastic.",
  "Scientists are now / looking for ways / to cultivate the bacteria / outside of mealworms.",
  "They also want / to speed up the process / by which / the bacteria break down plastic.",
  "This may help us / keep our landfills / plastic-free.",
 ],
 '❸': [
  "Mining and other industries / are causing / soil pollution / across the globe.",
  "Although polluted soil / can be dug up / and transported / to a landfill, / this process is expensive.",
  "Moreover, / it only moves the problem / to another area / and does not / really solve it.",
  "Fortunately, / there is / an eco-friendly and cost-effective way / to restore polluted soil / — planting willow trees.",
  "These amazing trees / have extensive / and well-developed / root systems.",
  "As a result, / they naturally extract / a wide range of / harmful materials / from the soil.",
  "They can also / grow quickly, / even in soil / with a high acidity level / or a lot of heavy metals / in it.",
  "Research / on the effectiveness / of using willow trees / for this purpose / is in development.",
  "Scientists have found / that some species / of willow trees / are able to absorb / harmful materials / better than others.",
  "Therefore, / this promising area / should be further explored / to find out / which trees / are the most effective.",
  "In time, / we may be able to / clean up our land / with willow trees.",
 ],
 '❹': [
  "Statistics show / that about thirty to forty percent / of people in the world / drink coffee / each day.",
  "The coffee-making process, / however, / generates used coffee grounds, / which are normally sent / to landfills.",
  "There, / they can create / a harmful greenhouse gas.",
  "Unfortunately, / there's no way / to stop everyone in the world / from drinking coffee.",
  "However, / we can reduce / greenhouse gas emissions / by turning used coffee grounds / into biofuel.",
  "Biofuel is / a natural fuel / that is made / from plant or animal sources.",
  "Researchers have found / that they can grow algae / on old coffee grounds / without adding / any other nutrients.",
  "If these algae are exposed / to twenty hours of light / and four hours of darkness / each day, / they eventually produce / high-quality biofuel.",
  "The biofuel is / renewable and sustainable, / and it creates / only a small amount / of emissions.",
 ],
 '❺': [
  "These are / just a few solutions / we can find / in nature.",
  "There could be / many more possible solutions / to the problems / we currently face.",
  "It seems / that Mother Nature / has given us / one more chance.",
  "In return, / we need to look for / more ways / to keep the environment / healthy and clean.",
  "If we do, / the future of our planet / may be bright / after all.",
 ],
}

HUNT = {
 '❶': ("Our environment is in trouble. With the planet [[became|becoming]] warmer, sea levels are rising and natural disasters such as forest fires and floods [[is|are]] increasing. "
       "More and more waste is also being [[producing|produced]]. Plastic, in particular, is causing problems with soil and water pollution. "
       "It is clear [[what|that]] humans are a major contributor to the destruction of nature. Will we be able to protect the environment from mountains of plastic? "
       "Can we stop climate change from [[reach|reaching]] dangerous levels? [[Achieve|Achieving]] these goals seems difficult. "
       "Nature, however, may have provided us with solutions to these problems. Here are three areas [[which|where]] changes are already happening.",
       ["with + 명사(the planet) + 분사: 행성이 '더워지는' 능동 진행 → becoming", "주어 natural disasters(복수), such as ~는 예시 → are",
        "쓰레기가 '만들어지는' 수동 진행: be being p.p. → produced", "It is clear that + 완전한 절 (진주어 that절). what 뒤에는 불완전한 절",
        "stop A from -ing (A가 ~하는 것을 막다) → 전치사 from 뒤 동명사 reaching", "주어 자리 → 동명사 Achieving (동사원형은 주어가 될 수 없음)",
        "선행사 areas + 완전한 절(changes are happening) → 관계부사 where"]),
 '❷': ("About fifty percent of plastic [[are|is]] produced for single-use products. That means the items are used just once and then [[discarding|discarded]]. "
       "Do you ever stop [[thinking|to think]] about where these plastic items go after you throw them away? Recycling can help reduce the amount of plastic in our landfills. "
       "However, less than ten percent of the world's plastic waste [[have|has]] been recycled so far. Often, plastic waste is moved to places [[which|where]] it is just dumped or burned. "
       "Furthermore, between 8 and 14 million metric tons of plastic [[ends|end]] up in the ocean every year. This puts many marine species in danger. "
       "With this in mind, scientists are turning to mealworms. Mealworms are the larvae of a certain species of beetle. Special bacteria [[lives|live]] inside them. "
       "These bacteria can break down plastic. This means that mealworms can actually [[feeding|feed]] on plastic. "
       "Scientists are now looking for ways to cultivate the bacteria outside of mealworms. They also want to speed up the process by [[that|which]] the bacteria break down plastic. "
       "This may help us [[keeping|keep]] our landfills plastic-free.",
       ["percent of + 셀 수 없는 명사(plastic) → 단수 동사 is", "are used ~ and (are) discarded: 수동태 병렬 → discarded",
        "stop to think = 생각하기 위해 (하던 일을) 멈추다. stop thinking은 '생각하는 것을 멈추다'로 뜻이 달라짐", "percent of + 셀 수 없는 명사(waste) → has",
        "선행사 places + 완전한 절(it is dumped) → 관계부사 where", "주어 tons(복수) → end", "bacteria는 bacterium의 복수형 → live",
        "조동사 can + 동사원형 → feed", "전치사 + 관계대명사: by which (전치사 뒤 that 불가)", "help + 목적어 + (to) 동사원형 → keep"]),
 '❸': ("Mining and other industries [[is|are]] causing soil pollution across the globe. Although polluted soil can be [[digging|dug]] up and transported to a landfill, this process is expensive. "
       "Moreover, it only moves the problem to another area and [[do|does]] not really solve it. "
       "Fortunately, there [[are|is]] an eco-friendly and cost-effective way to restore polluted soil — planting willow trees. "
       "These amazing trees have extensive and well-developed root systems. As a result, they naturally extract a wide range of [[harmless|harmful]] materials from the soil. "
       "They can also grow quickly, even in soil with a high acidity level or a lot of heavy metals in it. "
       "Research on the effectiveness of using willow trees for this purpose [[are|is]] in development. "
       "Scientists have found that some species of willow trees are able to absorb harmful materials [[good|better]] than others. "
       "Therefore, this promising area should be further [[exploring|explored]] to find out which trees are the most effective. In time, we may be able to clean up our land with willow trees.",
       ["주어 Mining and other industries(A and B, 복수) → are", "흙이 '파내지는' 수동: can be p.p. → dug (dig-dug-dug)",
        "주어 it(3인칭 단수), moves와 병렬 → does not", "there is/are 뒤 진짜 주어 an ~ way(단수) → is",
        "오염된 흙을 정화 → '해로운' 물질을 뽑아낸다 harmful (harmless는 해가 없는)", "주어 Research(단수), on ~ purpose는 수식어 → is",
        "than others가 있으므로 비교급 → better", "분야가 '탐구되어야' 하는 수동: should be p.p. → explored"]),
 '❹': ("Statistics show that about thirty to forty percent of people in the world drink coffee each day. "
       "The coffee-making process, however, generates used coffee grounds, [[that|which]] are normally sent to landfills. There, they can create a harmful greenhouse gas. "
       "Unfortunately, there's no way to stop everyone in the world from [[drink|drinking]] coffee. However, we can reduce greenhouse gas emissions by [[turn|turning]] used coffee grounds into biofuel. "
       "Biofuel is a natural fuel that [[makes|is made]] from plant or animal sources. Researchers have found that they can grow algae on old coffee grounds without [[add|adding]] any other nutrients. "
       "If these algae [[will be|are]] exposed to twenty hours of light and four hours of darkness each day, they eventually produce high-quality biofuel. "
       "The biofuel is renewable and sustainable, and it creates only a small amount of emissions.",
       ["콤마 뒤 계속적 용법 → which (that은 계속적 용법 불가)", "stop A from -ing → drinking", "전치사 by 뒤 동명사 → turning (~함으로써)",
        "연료가 식물·동물로부터 '만들어지는' 수동 → is made", "전치사 without 뒤 동명사 → adding", "조건 부사절(If ~)은 미래라도 현재시제 → are exposed"]),
 '❺': ("These are just a [[little|few]] solutions we can find in nature. There could be [[much|many]] more possible solutions to the problems we currently face. "
       "It seems that Mother Nature has given us one more chance. In return, we need to look for more ways to keep the environment [[healthily|healthy]] and clean. "
       "If we [[will do|do]], the future of our planet may be bright after all.",
       ["셀 수 있는 복수명사 solutions → a few (a little은 셀 수 없는 명사)", "more + 셀 수 있는 복수명사(solutions)를 강조 → many more (much more는 셀 수 없는 명사)",
        "keep + 목적어 + 형용사 보어 → healthy (clean과 병렬)", "조건 부사절(If ~)은 미래라도 현재시제 → do"]),
}

path = sys.argv[1] if len(sys.argv) > 1 else '/home/claude/proj/data/h1-ne-min-L3.js'
PK = json.loads(subprocess.check_output(['node', '-e', "global.window={};require('%s');process.stdout.write(JSON.stringify(window.PKG))" % path]))
base = [d for d in PK['days'] if not re.match(r'g\d$', d['id'])]
L4 = [d for d in base if d['id'].startswith('l4')]
KO = {}
for d in L4:
    for l in d['passage']:
        if l[0] != '#' and l[2]: KO[l[1]] = l[2]

def sec_passage(secs):
    out = []
    for d in L4:
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
    return {'id': did, 'name': 'DAY', 'range': '4과 본문 완전정복 ' + rng, 'story': '주요문장 덩어리 배열 → 틀린 곳 ' + '·'.join(str(len(HUNT[s][1])) + '개' for s in secs) + ' 찾아 고치기',
            'passage': sec_passage(secs), 'steps': [
        {'type': 'scramble', 'title': '주요문장 덩어리 스크램블', 'guide': '우리말을 보고 의미 덩어리를 순서대로 눌러 문장 전체를 완성하세요. 영작하듯 머릿속으로 먼저 문장을 떠올려 보세요.', 'items': scr},
        {'type': 'hunt', 'title': '오류 사냥 · 틀린 곳 찾아 고치기', 'guide': '단락에서 틀린 곳을 정해진 개수만큼 찾고(1점), 바르게 고쳐 쓰세요(1점).', 'items': hunt}]}

# 4과 본문 전 문장이 CH에 다 들어갔는지 (제목 줄 제외)
allen = [l[1] for d in L4 for l in d['passage'] if l[0] != '#' and l[2]]
used = {c.replace(' / ', ' ') for v in CH.values() for c in v}
missing = [e for e in allen if e not in used and len(e.split()) > 5]
assert not missing, missing

NEW = [mkday('g1', ['❶', '❷'], '❶❷'), mkday('g2', ['❸'], '❸'), mkday('g3', ['❹', '❺'], '❹❺')]
PK['days'] = base + NEW
for i, d in enumerate(PK['days']): d['name'] = 'DAY %d' % (i + 1)
src = open(path, encoding='utf-8').read(); head = src[:src.index('window.PKG')]
tail = src[src.index('/* WRAPUP-TESTS'):] if '/* WRAPUP-TESTS' in src else ''
if '4과 본문 완전정복' not in head: head = head.rstrip('\n') + '\n/* 11/10: DAY 10~12 4과 본문 완전정복(덩어리 스크램블 · 오류 사냥) gen/gen_h1l4full.py */\n'
PK.pop('tests', None)
write(PK, path, head)
if tail: open(path, 'a', encoding='utf-8').write(tail)
print('ok', [(d['name'], d['range'], [len(s['items']) for s in d['steps']]) for d in PK['days']])
