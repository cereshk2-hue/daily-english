# 11/24 대진고2 기출예상문제 본문 (능률 오선영 3과 · 4과) — 선생님: "대진고는 학교 어휘프린트(유·반의어)를 본문에 다 녹여서 서술형을 만들기로 유명. 지난 시험지처럼, OMR로 입력, 제목 '기출예상문제 본문'"
# 지난 시험지(2026 1학기 1·2차) 유형: 본문을 유의어로 바꿔 쓴 글 + 첫 철자 빈칸 / 요약문 첫 철자 빈칸 / <보기>로 영작(so~that, the+비교급) / 어법 틀린 문장 찾아 문장 전체 고쳐 쓰기 / <보기> 배열
# 객관식 12 × 4점 + 서술형 5 (10·10·10·12·10) = 100점. 어휘는 gen/daejin_tables.json(3과)·gen/oh4v/table.py(4과) 학교 프린트 유·반의어만 씀
# emit → h2-ne-oh-L3 /* GC-TESTS */ 블록(맨 끝, id dj-gc3·dj-gc4) — Wrap-up 탭(답안지 OMR) / 시험지 PDF는 pdf.py
import json, re, sys, subprocess
DATA = '/home/claude/proj/data/h2-ne-oh-L3.js'
U = lambda s: '<u>%s</u>' % s
def BOX(*ps): return '<div class="wbox">' + ''.join('<p>%s</p>' % p for p in ps) + '</div>'
NUM = '①②③④⑤'
def mc(src, stem, body, opts, ans, ex, en=True):
    assert len(opts) == 5 and len(set(opts)) == 5 and 0 <= ans < 5
    return {'src': src, 'stem': stem, 'body': body, 'opts': opts, 'en': en, 'ans': ans, 'ex': ex, 'ctx': '', 'pts': 4, 'words': [], 'kos': []}
def wr(src, stem, body, blanks, model, ex):
    pts = sum(b[1] for b in blanks)
    for lab, p, a, c in blanks:   # 첫 철자 빈칸 밑줄 수 = 글자 수 - 1 로 맞춤
        if re.match(r'\([A-E]\) [a-z]+$', lab) and len(a) == 1:
            body = re.sub(re.escape(lab[:3]) + r' ' + a[0][0] + r'_+', lambda m: lab[:3] + ' ' + a[0][0] + '_' * (len(a[0]) - 1), body)
    bl = [{'label': lab, 'pts': p, 'ans': list(a), 'chk': list(c), 'note': False} for lab, p, a, c in blanks]
    return {'kind': 'write', 'src': src, 'pts': pts, 'stem': stem + ' <span class="pt">[%d점]</span>' % pts, 'body': body, 'blanks': bl, 'model': model, 'ex': ex, 'kos': []}
def first(w): return '%s%s' % (w[0], '_' * (len(w) - 1))
def B(lab, w, extra=()): return (lab, 2, [w], list(extra), )
def nocomma(s): return [s.replace(',', '')] if ',' in s else []
SYM = lambda c: [c, '(%s)' % c, 'ⓐⓑⓒⓓⓔ'['abcde'.index(c)]]

# ══════════════ 3과 Life Is a Sum of Choices ══════════════
L3 = [
 mc('본문 ❶', '다음 글의 밑줄 친 부분 중, 문맥상 낱말의 쓰임이 적절하지 <u>않은</u> 것은?',
    BOX("We make many personal choices in our lives, from who to have lunch with to what career to ① " + U('strive for') + ". However, there are many situations where we must make decisions as a group. Group decision-making is not as ② " + U('straightforward') + " as our personal choices, as it involves numerous voices with ③ " + U('diverging') + " opinions. Voting is often used to make group decisions more ④ " + U('partial') + " and more ⑤ " + U('economical') + ", and various voting methods have been developed over time."),
    ['①', '②', '③', '④', '⑤'], 3,
    '정답 ▶ ④ partial(불공정한)은 fair(공정한)의 반의어 → impartial / unbiased / just 여야 함\n①strive for = pursue ②straightforward = simple ③diverging = differing ⑤economical = efficient (모두 어휘프린트 유의어)', en=False),
 mc('본문 ❷', '다음 글의 밑줄 친 (a), (b), (c)와 의미가 가장 가까운 것끼리 짝지어진 것은?',
    BOX("Their three options were an art show, a bake sale, and a charity concert, but there were (a) " + U('conflicting') + " opinions. So they decided to put it to a vote. When they asked for advice from Ms. Akers, the council's advisor, she (b) " + U('encouraged') + " them not to use the familiar voting method, but to try something different instead. (…) The entire council was curious to find out if the different methods would (c) " + U('yield') + " different results."),
    ['clashing – fostered – generate', 'harmonizing – fostered – render', 'clashing – dissuaded – produce', 'colliding – discouraged – bear', 'according – motivated – generate'], 0,
    '정답 ▶ ① conflict = clash·collide / encourage = foster·promote·motivate / yield = produce·generate·render·bear\n함정: harmonize·accord는 conflict의 반의어, dissuade·discourage는 encourage의 반의어'),
 mc('본문 ❸', '(A), (B), (C)의 각 네모 안에서 문맥에 맞는 낱말로 가장 적절한 것은?',
    BOX("On the day of the vote, each possible event was given a letter: \"art show\" was (A) [ <b>symbolized</b> / <b>concealed</b> ] by the letter A, the letter B (B) [ <b>signified</b> / <b>disregarded</b> ] \"bake sale,\" and C stood for \"charity concert.\" Each of the 20 council members was given a voting slip and (C) [ <b>directed</b> / <b>dissuaded</b> ] to write down the options in order of preference."),
    ['symbolized – signified – directed', 'symbolized – disregarded – directed', 'concealed – signified – dissuaded', 'concealed – disregarded – directed', 'symbolized – signified – dissuaded'], 0,
    '정답 ▶ ① represent = symbolize·depict / indicate = signify·show(↔ hide) / instruct = direct·order·command\nconceal(숨기다)·disregard(무시하다)·dissuade(단념시키다)는 문맥과 반대'),
 mc('본문 ❹', '다음 글의 밑줄 친 ⓐ~ⓔ 중, 어법상 <u>틀린</u> 것끼리 짝지어진 것은?',
    BOX("Voters are given several options, and ⓐ " + U('whichever gets') + " the most first-preference votes wins. Neither the second nor third preference ⓑ " + U('matter') + " at all, so they are ignored. This method ⓒ " + U('is commonly used') + " in political elections around the world. (…) It is possible ⓓ " + U('to win') + " a vote without the support of the majority. That ⓔ " + U('were') + " the case here."),
    ['ⓐ, ⓒ', 'ⓑ, ⓔ', 'ⓑ, ⓓ', 'ⓒ, ⓔ', 'ⓐ, ⓓ'], 1,
    '정답 ▶ ② ⓑ matter → matters (neither A nor B는 B인 third preference(단수)에 수 일치) / ⓔ were → was (주어 That 단수)\nⓐ 복합관계대명사 whichever + 단수 동사 ⓒ 수동태 ⓓ 가주어 It ~ 진주어 to win', en=False),
 mc('본문 ❹', '다음 글의 밑줄 친 ⓐ~ⓓ와 바꿔 쓸 수 있는 말로 바르게 짝지어진 것은?',
    BOX("The FPTP method is ⓐ " + U('uncomplicated') + " and easy to understand, but it has a ⓑ " + U('significant') + " ⓒ " + U('weakness') + ". It is possible to win a vote without the support of the ⓓ " + U('majority') + "."),
    ['straightforward – substantial – drawback – bulk', 'intricate – substantial – drawback – bulk', 'straightforward – trivial – shortcoming – minority', 'complex – considerable – strength – lion\'s share', 'simple – insignificant – flaw – minority'], 0,
    '정답 ▶ ① uncomplicated = straightforward·simple / significant = substantial·considerable / weakness = drawback·flaw·shortcoming / majority = bulk·lion\'s share\n함정: intricate·complex(복잡한), trivial·insignificant(사소한), strength(장점), minority(소수)는 반의어'),
 mc('본문 ❺', '다음 글의 내용과 일치하지 <u>않는</u> 것은?',
    BOX("The AV method can potentially include more than one round of counting. For an option to win in the first round, it needs to get more than 50% of the first-preference votes. As the charity concert only received 40% of the total votes, a second round of counting was required. Option A, the art show, received the fewest first-preference votes, with only 5 council members voting for it. Therefore, option A was eliminated, and the 5 council members' votes were redistributed based on their second preferences. As a result, 4 votes for option B (ABC) and 1 for option C (ACB) were added to the total."),
    ['AV 방식은 집계가 두 차례 이상 이루어질 수 있다.', '1차 집계에서 이기려면 1지망 표의 과반을 얻어야 한다.', '자선 콘서트는 1차 집계에서 과반을 얻지 못했다.', '미술 전시회는 1지망 표를 가장 적게 받아 제외되었다.', '제외된 5표는 모두 빵 바자회로 옮겨졌다.'], 4,
    '정답 ▶ ⑤ 5표 중 4표는 B(빵 바자회), 1표는 C(자선 콘서트)로 재분배됨(4 votes for option B and 1 for option C)', en=False),
 mc('본문 ❺', '다음 글의 밑줄 친 부분 중, 문맥상 낱말의 쓰임이 적절하지 <u>않은</u> 것은?',
    BOX("Next, the council members ① " + U('scrutinized') + " the votes using the AV method, and they soon realized that there would be a different result. The AV method can ② " + U('conceivably') + " include more than one round of counting. (…) Therefore, option A was ③ " + U('retained') + ", and the 5 council members' votes were ④ " + U('reallocated') + " based on their second preferences. (…) Unfortunately, the AV method is not ⑤ " + U('impeccable') + " either."),
    ['①', '②', '③', '④', '⑤'], 2,
    '정답 ▶ ③ 가장 적은 표를 받은 A는 eliminated(제거된) → remove·eradicate 의미여야 함. retain(유지하다)은 eliminate의 반의어\n①scrutinize = examine ②conceivably = potentially ④reallocate = redistribute ⑤impeccable = perfect(not perfect either)', en=False),
 mc('본문 ❻', '다음 빈칸 (A), (B)에 들어갈 말로 가장 적절한 것은?',
    BOX("The Condorcet method's weakness is that, along with being (A) ________, it sometimes fails to select a winner. This is especially true in elections that (B) ________ numerous options. It is possible that no option will be clearly preferred over the others."),
    ['intricate – encompass', 'straightforward – encompass', 'intricate – omit', 'uncomplicated – exclude', 'complicated – leave out'], 0,
    '정답 ▶ ① complex = intricate·complicated / contain = encompass·include·hold\n함정: straightforward·uncomplicated(단순한)는 complex의 반의어, omit·exclude·leave out은 contain의 반의어'),
 mc('본문 ❻', '다음 글의 밑줄 친 부분 중, 어법상 <u>틀린</u> 것은?',
    BOX("This method involves ① " + U('comparing') + " the voters' preferences between each possible pair of options. In this case, there were three pairs ② " + U('to consider') + ": A vs. B, B vs. C, and A vs. C. Through this method, the student council discovered that its members ③ " + U('preferred option A than option B') + " by a count of 11 to 9. In other words, 11 people preferred A to B, ④ " + U('voting') + " either ABC, ACB, or CAB. (…) As option A, the art show, ⑤ " + U('was preferred') + " to both of the other options, it would be considered the winner."),
    ['①', '②', '③', '④', '⑤'], 2,
    '정답 ▶ ③ prefer A to B(B보다 A를 선호하다) → preferred option A to option B (than ❌)\n① involve + 동명사 ② to부정사 형용사적 용법 ④ 분사구문 ⑤ 수동태(be preferred to)', en=False),
 mc('본문 ❼', '다음 글의 내용을 한 문장으로 요약할 때, 빈칸 (A), (B)에 들어갈 말로 가장 적절한 것은?',
    BOX("It is obvious that choosing an ideal voting method is a complex and challenging task. No voting system is flawless or clearly superior to another. Whichever we choose will have pros and cons. (…) Ultimately, understanding all of the possible voting methods and weighing their pros and cons allows us to better understand the process of decision-making.")
    + BOX('→ Since no voting system is (A) ________, we need to (B) ________ the pros and cons of each method to become better decision-makers.'),
    ['impeccable – ponder', 'defective – ponder', 'impeccable – overlook', 'inferior – disregard', 'obscure – neglect'], 0,
    '정답 ▶ ① flawless = impeccable·faultless·perfect / weigh = ponder·evaluate·deliberate\n함정: defective(↔flawless), overlook·disregard·neglect(무시하다)는 weigh와 반대'),
 mc('본문 ❼', '다음 글의 밑줄 친 부분 중, 문맥상 낱말의 쓰임이 적절하지 <u>않은</u> 것은?',
    BOX("After a long, ① " + U('fervent') + " discussion with Ms. Akers, the student council members decided to choose the Condorcet method, as they liked the idea of ② " + U('straight') + " comparing each option with the others. (…) It is ③ " + U('evident') + " that choosing an ideal voting method is a complex and ④ " + U('effortless') + " task. (…) Others continue to develop and test new ways of voting, ⑤ " + U('contending') + " that more complex methods deliver more accurate results."),
    ['①', '②', '③', '④', '⑤'], 3,
    '정답 ▶ ④ complex and challenging task → effortless(힘들지 않은)는 challenging의 반의어. demanding이어야 함\n①fervent = intense ②straight = directly ③evident = obvious ⑤contend = argue', en=False),
 mc('본문 ❶~❼', '본문의 요지로 가장 적절한 것은?',
    BOX("Instead of all methods pointing toward a single option and making the council's choice easier, the winner differed with each method. (…) No voting system is flawless or clearly superior to another. (…) When we understand decision-making better, we are more likely to become better decision-makers ourselves."),
    ['투표 방식마다 장단점이 있으므로, 이를 이해하는 것이 더 나은 의사 결정으로 이어진다.', '단순 다수결 방식이 가장 공정하므로 정치 선거에 널리 쓰여야 한다.', '콩도르세 방식은 언제나 승자를 정해 주므로 가장 우수한 방식이다.', '집단 의사 결정은 개인의 선택보다 언제나 더 정확한 결과를 낳는다.', '복잡한 투표 방식은 의사 결정을 어렵게 하므로 피해야 한다.'], 0,
    '정답 ▶ ① 어떤 방식도 완벽하지 않고(no voting system is flawless) 장단점을 따져 이해하면 더 나은 의사 결정자가 된다는 내용\n③ 콩도르세 방식은 때때로 승자를 정하지 못함(fails to select a winner)', en=False),
 wr('본문 ❹', '다음은 본문 ❹의 일부를 어휘프린트의 유의어로 바꿔 쓴 글이다. 빈칸 (A)~(E)에 들어갈 말을 주어진 철자로 시작하여 한 단어로 쓰시오. (문맥에 맞는 형태로)',
    BOX("The FPTP method is the most (A) s______________ (= simplest) of the three methods. Voters are given several options, and whichever gets the most first-preference votes wins. Neither the second nor third preference (B) c_____ (= matters) at all, so they are (C) d__________ (= ignored). This method is (D) f_________ (= commonly) used in political elections around the world. The student council quickly (E) a__________ (= determined) that the winner would be option C, the charity concert."),
    [('(A) s', 2, ['straightforward'], []), ('(B) c', 2, ['counts'], []), ('(C) d', 2, ['disregarded'], []), ('(D) f', 2, ['frequently'], []), ('(E) a', 2, ['ascertained'], [])],
    '(A) straightforward (B) counts (C) disregarded (D) frequently (E) ascertained',
    '어휘프린트: uncomplicated·simple = straightforward / matter = count / ignore = disregard·neglect·overlook / commonly = frequently·usually·generally / determine = ascertain·identify\n형태: (B) 주어가 neither A nor B(단수) → counts (C) are + 과거분사 → disregarded (E) 과거 → ascertained. 빈칸당 2점'),
 wr('본문 ❶~❼', '다음은 본문 전체를 요약한 글이다. 빈칸 (A)~(E)에 들어갈 말을 주어진 철자로 시작하여 한 단어로 쓰시오. (어휘프린트 유의어, 문맥에 맞는 형태로)',
    BOX("When a group must make a decision, voting can make the process more (A) i________ and more (B) e_________. However, each voting method may (C) y____ a different winner, as the student council discovered. Because no voting system is (D) i_________, we should (E) p_____ the pros and cons of each method to become better decision-makers."),
    [('(A) i', 2, ['impartial'], []), ('(B) e', 2, ['economical'], []), ('(C) y', 2, ['yield'], []), ('(D) i', 2, ['impeccable'], []), ('(E) p', 2, ['ponder'], [])],
    '(A) impartial (B) economical (C) yield (D) impeccable (E) ponder',
    '본문: make group decisions fairer and more efficient → fair = impartial / efficient = economical · would yield different results → yield / No voting system is flawless → flawless = impeccable / weighing their pros and cons → weigh = ponder. 빈칸당 2점'),
 wr('본문 ❼', '다음 우리말을 &lt;조건&gt;에 맞게 영작하시오.',
    BOX('우리가 의사 결정을 더 잘 이해할수록, 우리는 스스로 더 나은 의사 결정자가 될 가능성이 더 높다.') +
    '<div class="wcond"><b>&lt;조건&gt;</b> ① the + 비교급 ~, the + 비교급 … 구문을 쓸 것 · ② &lt;보기&gt;의 단어를 모두 쓰되 필요하면 형태를 바꿀 것 · ③ 15단어로 쓸 것 (decision-making, decision-makers는 각 1단어)<br>&lt;보기&gt; well / understand / decision-making / likely / become / good / decision-makers / ourselves</div>',
    [('', 10, ['The better we understand decision-making, the more likely we are to become better decision-makers ourselves.'],
      nocomma('The better we understand decision-making, the more likely we are to become better decision-makers ourselves.'))],
    'The better we understand decision-making, the more likely we are to become better decision-makers ourselves.',
    '본문: When we understand decision-making better, we are more likely to become better decision-makers ourselves.\n→ the better(well의 비교급) + 주어 + 동사, the more likely + 주어 + be동사 + to부정사 / good → better. 지난 기출 논술형 5(the less you use it, the more likely you are ~)와 같은 유형\n채점 ▶ 문장 전체가 맞아야 10점(대소문자·끝 마침표 무관), 쉼표만 빠지면 선생님 확인'),
 wr('본문 ❷', '다음 글의 밑줄 친 ⓐ~ⓔ 중 어법상 <u>틀린</u> 문장 두 개를 찾아 기호를 쓰고, 틀린 부분을 고쳐 문장 전체를 다시 쓰시오.',
    BOX("ⓐ " + U('So they decided to put it to a vote.') + " ⓑ " + U("When they asked for advice from Ms. Akers, she encouraged them not using the familiar voting method, but to try something different instead.") + " ⓒ " + U('After doing some research, the council members decided to try three different voting systems.') + " ⓓ " + U('The entire council was curious to find out if the different methods will yield different results.') + " ⓔ " + U('Each of the 20 council members was given a voting slip.')),
    [('기호 1', 2, SYM('b'), []), ('고친 문장 1', 4, ["When they asked for advice from Ms. Akers, she encouraged them not to use the familiar voting method, but to try something different instead."], nocomma("When they asked for advice from Ms. Akers, she encouraged them not to use the familiar voting method, but to try something different instead.")),
     ('기호 2', 2, SYM('d'), []), ('고친 문장 2', 4, ['The entire council was curious to find out if the different methods would yield different results.'], [])],
    "ⓑ When they asked for advice from Ms. Akers, she encouraged them not to use the familiar voting method, but to try something different instead. / ⓓ The entire council was curious to find out if the different methods would yield different results.",
    'ⓑ encourage + 목적어 + to부정사 → not using ❌ not to use ⭕ (뒤의 but to try와 병렬)\nⓓ 주절이 과거(was curious) → 시제 일치 will ❌ would ⭕\n채점 ▶ 기호 각 2점 + 고친 문장 각 4점(문장 전체가 맞아야). 기호 순서는 ⓑ → ⓓ 순으로 쓰기'),
 wr('본문 ❼', '다음 우리말과 같도록 &lt;보기&gt;의 말을 배열하여 문장을 완성하시오.',
    BOX('모든 방식이 하나의 선택지를 가리키고 자치회의 선택을 더 쉽게 만드는 대신, 각 방식마다 승자는 달랐다.') +
    '<div class="wcond"><b>&lt;조건&gt;</b> ① &lt;보기&gt;의 말을 모두 한 번씩 쓸 것 · ② 본문의 differed는 어휘프린트 유의어 <b>v_____</b>로 바꿔 쓸 것(과거형) · ③ 쉼표(,)를 알맞은 곳에 쓸 것<br>&lt;보기&gt; and / the winner / making / instead of / pointing toward / with each method / all methods / easier / the council\'s choice / a single option</div>',
    [('', 10, ["Instead of all methods pointing toward a single option and making the council's choice easier, the winner varied with each method."],
      nocomma("Instead of all methods pointing toward a single option and making the council's choice easier, the winner varied with each method."))],
    "Instead of all methods pointing toward a single option and making the council's choice easier, the winner varied with each method.",
    '본문: … the winner differed with each method. → differ = vary·diverge (어휘프린트 3번) → varied\ninstead of + 의미상 주어(all methods) + 동명사(pointing ~ and making ~) / make + 목적어 + 형용사(easier)\n채점 ▶ 문장 전체 10점, 쉼표만 빠지면 선생님 확인'),
]

# ══════════════ 4과 Create a Greener Tomorrow ══════════════
L4 = [
 mc('본문 ❶', '다음 글의 밑줄 친 부분 중, 문맥상 낱말의 쓰임이 적절하지 <u>않은</u> 것은?',
    BOX("On her way to a study group meeting, Liz ① " + U('unintentionally') + " dropped her laptop on the street, seriously ② " + U('impairing') + " it. Although it still turns on, the screen is ③ " + U('fractured') + ", and some keys are not working. She can have it ④ " + U('restored') + ", but she is ⑤ " + U('standing firm') + " to do so. Sometimes repairs are expensive, and they often take a long time."),
    ['①', '②', '③', '④', '⑤'], 4,
    '정답 ▶ ⑤ 수리를 \'망설이고\' 있는 상황 → hesitate = waver·falter. stand firm(단호하다)은 hesitate의 반의어\n①unintentionally = accidentally ②impair = damage ③fracture = crack ④restore = repair', en=False),
 mc('본문 ❷', '다음 글의 밑줄 친 (a)~(d)와 의미가 가장 가까운 것끼리 짝지어진 것은?',
    BOX("The term refers to (a) " + U('discarded') + " electronic devices and electrical appliances. Due to toxic materials contained in these products, such as lead, e-waste is a serious health and environmental (b) " + U('hazard') + ". To make matters worse, the amount of e-waste produced each year is increasing at an (c) " + U('alarming') + " rate. (…) For this reason, efforts are being made to (d) " + U('address') + " this problem."),
    ['thrown away – peril – disturbing – confront', 'retained – peril – reassuring – tackle', 'dumped – threat – comforting – handle', 'kept – danger – shocking – overlook', 'disposed of – safety – worrying – deal with'], 0,
    '정답 ▶ ① discard = throw away·dump·dispose of / hazard = peril·danger·threat / alarming = disturbing·worrying·shocking / address = confront·tackle·handle·deal with\n함정: retain·keep(↔discard), reassuring·comforting(↔alarming), safety, overlook'),
 mc('본문 ❷', '다음 글의 밑줄 친 ⓐ~ⓔ 중, 어법상 <u>틀린</u> 것끼리 짝지어진 것은?',
    BOX("In 2021, a total of 57.4 million metric tons of e-waste ⓐ " + U('was generated') + " worldwide, which was a 37% increase from 2014, the year ⓑ " + U('which') + " data about e-waste was first collected. Experts predict that by 2030, the amount of e-waste ⓒ " + U('generated') + " annually ⓓ " + U('will have doubled') + " in just 16 years. For this reason, efforts are being made to address this problem, ⓔ " + U('most of them') + " are focused on making products easier to repair."),
    ['ⓐ, ⓒ', 'ⓑ, ⓔ', 'ⓒ, ⓓ', 'ⓐ, ⓓ', 'ⓑ, ⓒ'], 1,
    '정답 ▶ ② ⓑ the year + 완전한 절 → which ❌ when ⭕ / ⓔ 두 절을 잇는 접속사가 없음 → most of them ❌ most of which ⭕\nⓐ 수동태(쓰레기가 \'발생된\') ⓒ 과거분사 후치 수식 ⓓ by 2030 → 미래완료', en=False),
 mc('본문 ❸', '(A), (B), (C)의 각 네모 안에서 문맥에 맞는 낱말로 가장 적절한 것은?',
    BOX("For example, a device may be difficult to (A) [ <b>dismantle</b> / <b>fabricate</b> ], or its manufacturer may require that it be brought to an official service center to be fixed. (…) What is more, some products are (B) [ <b>deliberately</b> / <b>coincidentally</b> ] designed to be difficult to repair. It is common for consumers to be unable to (C) [ <b>procure</b> / <b>forfeit</b> ] the instructions for how to fix their items or the parts needed to complete repairs."),
    ['dismantle – deliberately – procure', 'dismantle – coincidentally – procure', 'fabricate – deliberately – forfeit', 'fabricate – coincidentally – procure', 'dismantle – deliberately – forfeit'], 0,
    '정답 ▶ ① disassemble = dismantle·take apart(↔ fabricate·assemble) / intentionally = deliberately·on purpose(↔ coincidentally) / acquire = procure·attain(↔ forfeit)'),
 mc('본문 ❸', '수리할 권리 운동이 요구하는 것으로 본문에서 언급되지 <u>않은</u> 것은?',
    BOX("To protect the rights of consumers, the right-to-repair movement demands four things. First, companies must make information about their products available to everyone. Second, third parties, including individuals, should be able to obtain the parts and tools required to make repairs. Third, the practice of preventing consumers from installing custom software on their own devices should be prohibited by law. Finally, it demands that manufacturers design devices in a way that makes repairs as easy as possible."),
    ['제품에 대한 정보를 모두가 이용할 수 있게 할 것', '개인을 포함한 제삼자가 수리 부품과 도구를 구할 수 있게 할 것', '소비자가 자기 기기에 맞춤형 소프트웨어를 설치하지 못하게 막는 행위를 법으로 금지할 것', '수리를 최대한 쉽게 만드는 방식으로 기기를 설계할 것', '고장 난 기기는 반드시 공식 수리소에서만 고치게 할 것'], 4,
    '정답 ▶ ⑤ 오히려 운동은 공식 수리소만 고집하는 회사 관행을 문제로 봄(you have the right to fix it yourself or bring it to a technician of your choice)', en=False),
 mc('본문 ❸', '다음 글의 밑줄 친 부분 중, 문맥상 낱말의 쓰임이 적절하지 <u>않은</u> 것은?',
    BOX("Second, third parties, including individuals, should be able to ① " + U('secure') + " the parts and tools required to make repairs. Third, the practice of preventing consumers from ② " + U('embedding') + " ③ " + U('personalized') + " software on their own devices should be ④ " + U('sanctioned') + " by law. (…) ⑤ " + U('Proponents') + " of the movement say that if all these goals are accomplished, far less e-waste will be generated."),
    ['①', '②', '③', '④', '⑤'], 3,
    '정답 ▶ ④ 막는 행위는 법으로 \'금지\'되어야 함 → prohibit = forbid·ban·bar. sanction(허가하다)은 prohibit의 반의어\n①secure = obtain ②embed = install ③personalized = customized ⑤proponent = advocate', en=False),
 mc('본문 ❹', '다음 글의 밑줄 친 부분 중, 어법상 <u>틀린</u> 것은?',
    BOX("In January 2021, the French government passed a bill ① " + U('that requires') + " that every manufacturer ② " + U('include') + " a \"repairability index\" on five categories of electronic devices and electrical appliances. Using a score ③ " + U('ranging') + " from 0 to 10, as well as a color-coded system, the index lets consumers ④ " + U('to see') + " how easily the product can be repaired before they purchase it. A high number on a green label ⑤ " + U('indicates') + " that the product is easy to repair."),
    ['①', '②', '③', '④', '⑤'], 3,
    '정답 ▶ ④ 사역동사 let + 목적어 + 동사원형 → to see ❌ see ⭕\n② require that + 주어 + (should) 동사원형 ③ 현재분사 후치 수식 ⑤ 주어 A high number(단수)', en=False),
 mc('본문 ❹', '다음 글의 밑줄 친 ⓐ~ⓓ와 바꿔 쓸 수 있는 말로 바르게 짝지어진 것은?',
    BOX("The index ⓐ " + U('takes into account') + " several ⓑ " + U('elements') + ", including the availability of repair information, the ease of disassembly, and the price of ⓒ " + U('spare') + " parts. A low number on a bright red ⓓ " + U('label') + " means that repairing the product will be difficult."),
    ['considers – components – extra – tag', 'ignores – components – extra – tag', 'considers – factors – essential – glance', 'overlooks – parts – reserved – index', 'considers – substances – original – sticker'], 0,
    '정답 ▶ ① take into account = consider / element = component·factor / spare = extra·additional·reserved / label = tag·sticker\n함정: ignore·overlook(↔고려하다), essential·original(여분이 아님)'),
 mc('본문 ❺', '다음 빈칸 (A), (B)에 들어갈 말로 가장 적절한 것은?',
    BOX("Firstly, it allows consumers to make (A) ________ decisions when purchasing new devices and appliances. Secondly, it encourages manufacturers to make their products easier to repair. As a result, with fewer electronic and electrical items ending up in its landfills, France can expect to make a (B) ________ to a more sustainable society in the near future."),
    ['knowledgeable – shift', 'ignorant – shift', 'knowledgeable – halt', 'hasty – return', 'uninformed – delay'], 0,
    '정답 ▶ ① informed = knowledgeable·educated / transition = shift·change·transformation\n함정: ignorant·uninformed(↔informed), halt·delay(멈춤·지연)'),
 mc('본문 ❺~❻', '다음 글의 밑줄 친 부분 중, 문맥상 낱말의 쓰임이 적절하지 <u>않은</u> 것은?',
    BOX("If the index is successful, we can ① " + U('foresee') + " more countries around the world following France's ② " + U('ground-breaking') + " lead. (…) When consumers are given the right tools and materials, they can repair much of the damage that ③ " + U('arises') + " in electronic products by themselves. (…) It was such a success that the idea soon spread to ④ " + U('adjacent') + " countries. (…) These cafés also encourage people to share their ⑤ " + U('worthless') + " skills and knowledge about the repair and maintenance of electronics."),
    ['①', '②', '③', '④', '⑤'], 4,
    '정답 ▶ ⑤ invaluable(매우 귀중한) 자리 → priceless·extremely valuable. worthless(가치 없는)는 invaluable의 반의어\n①foresee = anticipate ②ground-breaking = innovative ③arise = occur ④adjacent = neighboring', en=False),
 mc('본문 ❻', '다음 글의 밑줄 친 ⓐ~ⓔ 중, 어법상 <u>틀린</u> 것끼리 짝지어진 것은?',
    BOX("They are free meeting places ⓐ " + U('where') + " people can gather together and fix their broken devices. The cafés are staffed by volunteer experts who can give technical advice and teach people ⓑ " + U('how to fix') + " things. It was ⓒ " + U('so a success') + " that the idea soon spread to neighboring countries. Along with preventing damaged items from ⓓ " + U('become') + " e-waste, these cafés also encourage people ⓔ " + U('to share') + " their invaluable skills."),
    ['ⓐ, ⓑ', 'ⓑ, ⓔ', 'ⓒ, ⓓ', 'ⓐ, ⓒ', 'ⓓ, ⓔ'], 2,
    '정답 ▶ ③ ⓒ such + a + 명사 + that → so a success ❌ such a success ⭕ / ⓓ 전치사 from + 동명사 → become ❌ becoming ⭕\nⓐ 관계부사 where ⓑ how to부정사 ⓔ encourage + 목적어 + to부정사', en=False),
 mc('본문 ❼', '다음 글의 내용을 한 문장으로 요약할 때, 빈칸 (A), (B)에 들어갈 말로 가장 적절한 것은?',
    BOX("Imagine she lived in a world where repairing damaged devices and appliances was simply part of everyday life. If that were the case, her options wouldn't be limited to paying for expensive repairs or throwing away her laptop and buying a new one. (…) Even more importantly, it is a future in which people will generate far less e-waste.")
    + BOX('→ In a world where repair is part of daily life, consumers\' options would not be (A) ________ to costly repairs or replacement, and far less e-waste would be (B) ________.'),
    ['confined – engendered', 'unconstrained – engendered', 'confined – depleted', 'extended – exhausted', 'circumscribed – curtailed'], 0,
    '정답 ▶ ① limit = confine·restrict·circumscribe / generate = engender·yield·spawn\n함정: unconstrain(↔limit), deplete·exhaust(↔generate), curtail(줄이다)는 \'발생하다\'가 아님'),
 wr('본문 ❻', '다음은 본문 ❻의 일부를 어휘프린트의 유의어로 바꿔 쓴 글이다. 빈칸 (A)~(E)에 들어갈 말을 주어진 철자로 시작하여 한 단어로 쓰시오. (문맥에 맞는 형태로)',
    BOX("When consumers are given the right tools and materials, they can repair much of the damage that (A) a_____ (= occurs) to electronic products by themselves. (…) The first Repair Café was such a success that the idea soon spread to (B) a_______ (= neighboring) countries. These cafés also encourage people to share their (C) p_______ (= invaluable) skills and knowledge about the repair and (D) u_____ (= maintenance) of electronics. By providing spaces where people can learn, Repair Cafés enable individuals to maintain their devices and (E) p______ (= extend) their life spans."),
    [('(A) a', 2, ['arises'], []), ('(B) a', 2, ['adjacent'], []), ('(C) p', 2, ['priceless'], []), ('(D) u', 2, ['upkeep'], []), ('(E) p', 2, ['prolong'], [])],
    '(A) arises (B) adjacent (C) priceless (D) upkeep (E) prolong',
    '어휘프린트: occur = arise·happen / neighboring = adjacent·nearby / invaluable = priceless / maintenance = upkeep·preservation / extend = prolong·lengthen\n형태: (A) 주어 damage(단수) 현재 → arises (E) enable ~ to maintain and (to) prolong → 동사원형. 빈칸당 2점'),
 wr('본문 ❶~❼', '다음은 본문 전체를 요약한 글이다. 빈칸 (A)~(E)에 들어갈 말을 주어진 철자로 시작하여 한 단어로 쓰시오. (어휘프린트 유의어, 문맥에 맞는 형태로)',
    BOX("Because e-waste contains (A) l_____ materials such as lead and is increasing at a (B) d_________ rate, efforts are being made to make products easier to (C) r______. These include the right-to-repair movement, France's repairability (D) i________, and Repair Cafés, which (E) c________ a sustainable perspective in local communities."),
    [('(A) l', 2, ['lethal'], []), ('(B) d', 2, ['disturbing'], []), ('(C) r', 2, ['restore'], []), ('(D) i', 2, ['indicator'], []), ('(E) c', 2, ['cultivate'], [])],
    '(A) lethal (B) disturbing (C) restore (D) indicator (E) cultivate',
    '본문: toxic materials → toxic = lethal·hazardous / at an alarming rate → alarming = disturbing / easier to repair → repair = restore·fix·mend / repairability index → index = indicator·gauge / foster a sustainable perspective → foster = cultivate·nurture. 빈칸당 2점'),
 wr('본문 ❻', '다음 우리말을 &lt;조건&gt;에 맞게 영작하시오.',
    BOX('그것(첫 번째 수리 카페)은 매우 성공적이어서 그 아이디어는 곧 이웃 나라들로 퍼졌다.') +
    '<div class="wcond"><b>&lt;조건&gt;</b> ① so ~ that 구문을 쓸 것 · ② &lt;보기&gt;의 단어를 모두 쓰되 필요하면 형태를 바꿀 것 · ③ 12단어로 쓸 것<br>&lt;보기&gt; it / success / idea / soon / spread / neighboring / countries</div>',
    [('', 10, ['It was so successful that the idea soon spread to neighboring countries.'], [])],
    'It was so successful that the idea soon spread to neighboring countries.',
    '본문: It was such a success that the idea soon spread to neighboring countries.\n→ so + 형용사 + that: such a success(명사) → so successful(형용사로 바꾸기) / spread(과거형도 spread)\n지난 기출 논술형 4(so ~ that 구문)와 같은 유형. 채점 ▶ 문장 전체 10점'),
 wr('본문 ❸', '다음 글의 밑줄 친 ⓐ~ⓔ 중 어법상 <u>틀린</u> 문장 두 개를 찾아 기호를 쓰고, 틀린 부분을 고쳐 문장 전체를 다시 쓰시오.',
    BOX("ⓐ " + U('One reason many people dispose of their damaged devices is that they are too difficult to repair.') + " ⓑ " + U('Many companies do not allow their customers taking their damaged items to third-party repair shops.') + " ⓒ " + U('What is more, some products are intentionally designed to be difficult to repair.') + " ⓓ " + U('It is common for consumers to be unable to acquire the instructions for how to fix their items or the parts needing to complete repairs.') + " ⓔ " + U('To protect the rights of consumers, the right-to-repair movement demands four things.')),
    [('기호 1', 2, SYM('b'), []), ('고친 문장 1', 4, ['Many companies do not allow their customers to take their damaged items to third-party repair shops.'], []),
     ('기호 2', 2, SYM('d'), []), ('고친 문장 2', 4, ['It is common for consumers to be unable to acquire the instructions for how to fix their items or the parts needed to complete repairs.'], [])],
    'ⓑ Many companies do not allow their customers to take their damaged items to third-party repair shops. / ⓓ It is common for consumers to be unable to acquire the instructions for how to fix their items or the parts needed to complete repairs.',
    'ⓑ allow + 목적어 + to부정사 → taking ❌ to take ⭕\nⓓ 부품은 수리를 완료하는 데 \'필요한(필요해지는)\' 것 → 과거분사 needed ⭕ (needing ❌)\n채점 ▶ 기호 각 2점 + 고친 문장 각 4점. 기호 순서는 ⓑ → ⓓ'),
 wr('본문 ❻', '다음 우리말과 같도록 &lt;보기&gt;의 말을 배열하여 문장을 완성하시오.',
    BOX('사람들이 배울 수 있는 공간을 제공함으로써, 수리 카페들은 개인이 자신들의 장치를 유지하고 그것들의 수명을 연장할 수 있게 한다.') +
    '<div class="wcond"><b>&lt;조건&gt;</b> ① &lt;보기&gt;의 말을 모두 한 번씩 쓸 것 · ② 본문의 extend는 어휘프린트 유의어 <b>p______</b>로 바꿔 쓸 것 · ③ 쉼표(,)를 알맞은 곳에 쓸 것<br>&lt;보기&gt; Repair Cafés / their devices / enable / where people can learn / by providing spaces / their life spans / individuals / and / to maintain</div>',
    [('', 10, ['By providing spaces where people can learn, Repair Cafés enable individuals to maintain their devices and prolong their life spans.'],
      nocomma('By providing spaces where people can learn, Repair Cafés enable individuals to maintain their devices and prolong their life spans.'))],
    'By providing spaces where people can learn, Repair Cafés enable individuals to maintain their devices and prolong their life spans.',
    '본문: … enable individuals to maintain their devices and extend their life spans. → extend = prolong·lengthen (어휘프린트 57번)\nby + 동명사(~함으로써) / 관계부사 where / enable + 목적어 + to부정사(to maintain ~ and (to) prolong ~)\n채점 ▶ 문장 전체 10점, 쉼표만 빠지면 선생님 확인'),
]

TGT = {'3': [0, 1, 4, 0, 1, 4, 1, 0], '4': [0, 1, 2, 0, 1, 2, 0, 2]}   # 옮길 수 있는 객관식의 정답 자리(①~⑤ 고르게)
def place(L, items):
    tg = iter(TGT[L])
    for it in items:
        if it.get('kind') == 'write' or it['opts'] == list(NUM): continue
        t = next(tg); a = it['ans']
        if t != a:
            o = it['opts']; o[a], o[t] = o[t], o[a]
            assert it['ex'].startswith('정답 ▶ ' + NUM[a]), it['ex'][:12]
            it['ex'] = '정답 ▶ ' + NUM[t] + it['ex'][len('정답 ▶ ') + 1:]
            it['ans'] = t
    assert next(tg, None) is None
    return items
def number(items):
    k = w = 0
    for it in items:
        if it.get('kind') == 'write': w += 1; it['n'] = '서술형 %d' % w
        else: k += 1; it['n'] = k
    return items

# ── 검사 ──
def vocab_words():
    d = json.load(open('/home/claude/srcrepo/gen/daejin_tables.json'))
    s3 = ' '.join(re.sub(r'[*°]', '', ' '.join(r)) for r in d[0][1:]).lower()
    src4 = open('/home/claude/srcrepo/gen/oh4v/table.py', encoding='utf-8').read().lower()
    return s3, src4
def check():
    s3, s4 = vocab_words()
    PK = json.loads(subprocess.check_output(['node', '-e', "global.window={};require('%s');process.stdout.write(JSON.stringify(window.PKG))" % DATA]))
    body = {L: ' '.join(l[1] for d in PK['days'] if d['id'] in ids for l in d['passage']).replace('’', "'") for L, ids in (('3', ('d1', 'd2', 'd3')), ('4', ('p1', 'p2', 'p3', 'p4')))}
    for L, QS, voc in (('3', L3, s3), ('4', L4, s4)):
        assert sum(it['pts'] for it in QS) == 100, (L, sum(it['pts'] for it in QS))
        assert sum(1 for it in QS if it.get('kind') != 'write') == 12
        for it in QS:
            if it.get('kind') == 'write':
                for b in it['blanks']:
                    if b['label'][:1] == '(' and len(b['ans']) == 1 and ' ' not in b['ans'][0]:   # 첫 철자 빈칸: 어휘프린트에 있는 말
                        w = b['ans'][0]; root = w[:5]
                        assert root in voc, (L, w)
                        assert b['label'].endswith(w[0]) or b['label'].endswith(w[:2]), (b['label'], w)
                        m = re.search(re.escape(b['label'][:3]) + r' (\w)(_+)', it['body'])
                        assert m and m.group(1) == w[0] and len(m.group(2)) == len(w) - 1, (L, w, m and m.group(0))
    print('check ok')

def tests():
    return [{'id': 'dj-gc3', 'title': '기출예상문제 본문 · 능률(오선영) 3과', 'short': '기출예상 3과', 'school': '대진고 2학년', 'minutes': 50, 'items': number(place('3', L3))},
            {'id': 'dj-gc4', 'title': '기출예상문제 본문 · 능률(오선영) 4과', 'short': '기출예상 4과', 'school': '대진고 2학년', 'minutes': 50, 'items': number(place('4', L4))}]
def emit():
    T = tests(); ids = [t['id'] for t in T]
    blk = ('/* GC-TESTS: gen/djgc/mk.py 로 만듦 (손으로 고치지 말 것) */\nwindow.PKG.tests = (window.PKG.tests || []).filter(function (t) { return %s.indexOf(t.id) < 0; }).concat(%s);\n/* /GC-TESTS */\n'
           % (json.dumps(ids), json.dumps(T, ensure_ascii=False)))
    js = open(DATA, encoding='utf-8').read()
    if '/* GC-TESTS' in js: js = re.sub(r'/\* GC-TESTS.*?/\* /GC-TESTS \*/\n', lambda m: blk, js, flags=re.S)
    else: js = js.rstrip('\n') + '\n\n' + blk
    open(DATA, 'w', encoding='utf-8').write(js); print('emit', ids)

if __name__ == '__main__':
    check()
    if 'emit' in sys.argv: emit()
