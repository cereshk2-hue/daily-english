# 11/22 안곡고1 동아(이병민) 3·4과 본문 서술형 10문항 — print/jdsw_make.py 형식 그대로(Q만 교체)
import re, html, sys, os
os.makedirs('/home/claude/out/agsw', exist_ok=True)
OUT = '/home/claude/out/agsw/'
E = html.escape
Q = [
 dict(tag='3과 본문 ❶', gram='수동태 · 계속적 용법 which · 간접의문문', title='다음 우리말을 &lt;조건&gt;에 맞게 영작하시오.',
      box=['이 정보는 알고리즘에 입력되고, 그러면 그 알고리즘이 우리가 무엇을 볼지 결정한다.'],
      cond=['This information으로 시작할 것', 'feed, algorithm, decide, see를 쓰되 필요하면 형태를 바꿀 것', '관계대명사의 계속적 용법을 쓸 것', '14단어로 쓸 것'],
      parts=[('', 2)],
      ans=['This information is fed into an algorithm, which then decides what we will see.'],
      pts=['정보가 \'입력되는\' → is fed(feed-fed-fed) into', '콤마 + which(계속적 용법, that ❌) + 단수 동사 decides', '간접의문문 what + 주어 + 동사(what we will see)']),
 dict(tag='3과 본문 ❷', gram='가목적어 it · 가정법 과거 · have a hard time -ing', title='다음 우리말을 &lt;조건&gt;에 맞게 영작하시오.',
      box=[], cond=[],
      parts=[('(1) 알고리즘은 우리가 필요한 정보를 찾는 것을 더 쉽게 만든다.<br><span class="cond">조건: make, easy, find, information, need를 쓰되 필요하면 형태를 바꿀 것 · 가목적어 it과 의미상 주어를 쓸 것 · 12단어</span>', 2),
             ('(2) 만약 알고리즘이 존재하지 않는다면, 우리는 원하는 것을 찾는 데 더 힘든 시간을 보낼 것이다.<br><span class="cond">조건: 가정법 과거 · exist, have a hard time, search for, what을 쓰되 형태를 바꿀 것 · 16단어(did not은 줄이지 말 것)</span>', 2)],
      ans=['(1) Algorithms make it easier for us to find the information we need.', '(2) If algorithms did not exist, we would have a harder time searching for what we want.'],
      pts=['(1) make + 가목적어 it + 형용사(easier) + for us + to find(진목적어)', '(2) If + 과거(did not exist), would + 동사원형', '(2) have a hard time -ing → harder time searching / 관계대명사 what']),
 dict(tag='3과 본문 ❷', gram='allow + 목적어 + to부정사 · 수 일치 · 주격 관계대명사', title='다음 글에서 어법상 <u>틀린</u> 부분 3개를 찾아 바르게 고쳐 쓰시오.',
      box=['If algorithms did not exist, we would have a harder time searching for what we want. They allow us spending less time searching and more time enjoying what we\'re interested in. '
           'Algorithms help us stay connected to our loved ones and meet new people. Have you ever noticed that posts from your close friends on social media usually appears at the top? This doesn\'t happen by chance. (…) '
           'By showing us posts of users who has similar ideas and interests, social media algorithms can help us find or even form communities with people who share the same interests.'],
      cond=[], parts=[('(1) ________ → ________', 1), ('(2) ________ → ________', 1), ('(3) ________ → ________', 1)],
      ans=['(1) spending → to spend (allow + 목적어 + to부정사)', '(2) appears → appear (주어 posts는 복수)', '(3) has → have (선행사 users는 복수)'],
      pts=['allow/enable/cause + 목적어 + to부정사', 'posts from your close friends on social media — 수식어 빼고 주어 posts', '주격 관계대명사 who의 동사는 선행사(users)에 수 일치']),
 dict(tag='3과 본문 ❸', gram='prevent A from -ing · 동격 that · 관계대명사 what', title='다음 물음에 답하시오.',
      box=[], cond=[],
      parts=[('(1) 다음 우리말을 &lt;조건&gt;에 맞게 영작하시오.<br>이것은 그것들이 우리가 다른 관점을 제공하는 정보를 발견하지 못하게 막는다는 것을 의미한다.<br><span class="cond">조건: This means로 시작 · prevent, discover, offer, point of view를 쓰되 형태를 바꿀 것 · 15단어</span>', 2),
             ('(2) 우리말과 같도록 괄호 안의 말을 바르게 배열하시오.<br>그것은 우리에게 정보 편향, 즉 우리가 생각하는 것이 사회의 표준이라는 잘못된 느낌을 갖게 한다.<br><span class="en">It causes us to have information bias, or ( that / is / a false sense / we think / what / the norm of society ).</span>', 2)],
      ans=['(1) This means they prevent us from discovering information that offers a different point of view.', '(2) a false sense that what we think is the norm of society'],
      pts=['(1) prevent + 목적어 + from -ing(~하지 못하게 막다)', '(1) 주격 관계대명사 that + 단수 동사 offers(선행사 information)', '(2) 동격 that절(a false sense = that ~) 안에서 what we think가 주어 → is']),
 dict(tag='3과 본문 ❸', gram='재구성 빈칸 · 품사 바꾸기', title='다음 글은 본문 ❸을 재구성한 것이다. 빈칸 (A)~(C)에 들어갈 말을 &lt;조건&gt;에 맞게 쓰시오.',
      box=['Because algorithms show us only content that matches our past activity, we can easily become (A) ________ in the information we get. They also keep content flowing (B) ________ on our screens, '
           'so many people end up becoming (C) ________ to social media, which can hurt their studies, work, relationships, and mental health.'],
      cond=['본문 ❸에서 단어를 찾아 문맥에 맞게 형태(품사)를 바꿀 것', '각각 한 단어'],
      parts=[('(A) ____________ &nbsp;&nbsp; (B) ____________ &nbsp;&nbsp; (C) ____________', 1)],
      ans=['(A) biased (← bias)', '(B) continuously (← continuous)', '(C) addicted (← addiction / addictive)'],
      pts=['(A) become + 형용사 biased(편향된)', '(B) 동사 flowing을 꾸미는 부사 continuously', '(C) become addicted to(~에 중독되다)']),
 dict(tag='3과 본문 ❹', gram='분사구문(부정) · whether or not · prevent A from -ing', title='다음 물음에 답하시오.',
      box=[], cond=[],
      parts=[('(1) 다음 우리말을 &lt;조건&gt;에 맞게 영작하시오.<br>사람들은 그 정보가 정확한지 아닌지에 주의를 기울이지 않은 채, 소셜 미디어에 가짜 뉴스를 공유한다.<br><span class="cond">조건: People share로 시작 · 부정 분사구문과 whether or not을 쓸 것 · pay attention to, accurate를 쓸 것 · 18단어</span>', 2),
             ('(2) 다음 질문에 본문 ❹의 내용을 바탕으로 By로 시작하는 영어로 답하시오.<br><span class="en">Q: According to the comment, how can we keep ourselves from having information bias?</span>', 2)],
      ans=['(1) People share fake news on social media, not paying attention to whether or not the information is accurate.',
           '(2) By seeking out different sources (as well), such as books, official news websites, and documentaries.'],
      pts=['(1) 분사구문의 부정: not + -ing(not paying)', '(1) 전치사 to + whether or not + 주어 + 동사', '(2) By + 동명사 seeking out different sources']),
 dict(tag='4과 본문 ❷', gram='관계대명사 what 주어 · not A but B · might have p.p.', title='다음 우리말을 &lt;조건&gt;에 맞게 영작하시오.',
      box=[], cond=[],
      parts=[('(1) 처음에 대부분의 사람들의 관심을 끄는 것은 그 여인이 아니라 그 여인의 팔에 안긴 아름다운 흰 동물이다.<br><span class="cond">조건: What으로 시작 · not A but B · draw, attention, initially를 쓸 것 · 19단어(people\'s, woman\'s는 각 1단어)</span>', 2),
             ('(2) 그는 그의 후원자에게 경의를 표하기 위해 그렇게 했을지도 모른다.<br><span class="cond">조건: He로 시작 · 과거에 대한 추측(조동사 + have p.p.) · do, honor, patron을 쓸 것 · 9단어</span>', 2)],
      ans=['(1) What draws most people\'s attention initially is not the woman but the beautiful white animal in the woman\'s arms.', '(2) He might have done it to honor his patron.'],
      pts=['(1) What + 단수 동사 draws ~ (what절 주어) + is', '(1) not A but B(A가 아니라 B)', '(2) might have p.p.(~했을지도 모른다) / 목적 to honor']),
 dict(tag='4과 본문 ❸', gram='현재분사 수식 · 간접의문문(do you think) · one of + 복수 명사', title='다음 글에서 어법상 <u>틀린</u> 부분 3개를 찾아 바르게 고쳐 쓰시오.',
      box=['This next piece is by the great Vincent van Gogh. It appears to be just an ordinary painting of a woman wore a white cap. But thanks to technology, another person was discovered on the other side of the canvas. '
           'Do you think who that person was? It was Vincent van Gogh himself that was hidden at the back of the painting. (…) You might also notice that Van Gogh\'s left ear looks perfectly fine in this painting. '
           'Since he cut off part of his ear when he was 35, we can infer that this is one of his early work.'],
      cond=[], parts=[('(1) ________ → ________', 1), ('(2) ________ → ________', 1), ('(3) ________ → ________', 1)],
      ans=['(1) wore → wearing (흰 모자를 \'쓰고 있는\' 여인 — 현재분사)', '(2) Do you think who that person was → Who do you think that person was (think류 동사 → 의문사를 맨 앞으로)', '(3) work → works (one of + 복수 명사)'],
      pts=['a woman wearing a white cap: 명사 뒤 분사구', 'Do you think + 간접의문문 → 의문사가 문장 맨 앞', 'one of his early works']),
 dict(tag='4과 본문 ❸', gram='It ~ that 강조 · 분사구문', title='다음 문장을 [ ] 안의 지시대로 바꿔 쓰시오.',
      box=[], cond=[],
      parts=[('(1) Vincent van Gogh himself was hidden at the back of the painting. [Vincent van Gogh himself를 강조하는 It ~ that 구문으로]', 2),
             ('(2) As he was a poor artist, he often reused his canvases to save money. [As절을 분사구문으로]', 2)],
      ans=['(1) It was Vincent van Gogh himself that(who) was hidden at the back of the painting.', '(2) Being a poor artist, he often reused his canvases to save money.'],
      pts=['(1) It was + 강조어 + that ~ (과거 → was)', '(2) 접속사·주어 생략, 동사 was → Being', '(2) 주절의 주어(he)와 같을 때만 생략']),
 dict(tag='4과 본문 ❺', gram='It ~ that 강조(목적어) · 현재완료 수동태', title='다음 우리말을 &lt;조건&gt;에 맞게 영작하시오.',
      box=[], cond=[],
      parts=[('(1) 박물관이 잃어버린 부분들을 재현하기 위해 사용한 것은 바로 인공지능이었다.<br><span class="cond">조건: It ~ that 강조 구문 · artificial intelligence, use, recreate, missing pieces를 쓸 것 · 13단어</span>', 2),
             ('(2) 과학 덕분에, 이 위대한 걸작은 모두가 볼 수 있도록 다시 생명을 얻게 되었다.<br><span class="cond">조건: Thanks to science로 시작 · 현재완료 수동태 · bring back to life, for all to see를 쓸 것 · 16단어</span>', 2)],
      ans=['(1) It was artificial intelligence that the museum used to recreate the missing pieces.', '(2) Thanks to science, this great masterpiece has been brought back to life for all to see.'],
      pts=['(1) 목적어 강조: It was + AI + that + 주어(the museum) + 동사(used) — used 뒤에 목적어 없음', '(1) 목적 to recreate', '(2) has been brought(bring-brought-brought) back to life']),
]
assert len(Q) == 10

CSS = '''
@import url('https://fonts.googleapis.com/css2?family=Noto+Sans+KR:wght@400;500;700;900&family=Noto+Serif:wght@400;700&display=swap');
*{box-sizing:border-box;margin:0;padding:0}
body{font-family:'Noto Sans KR',sans-serif;color:#1d2433;-webkit-print-color-adjust:exact;print-color-adjust:exact}
.en,.box{font-family:'Noto Serif',serif}
.navy{background:#1f3a5f;color:#fff}
'''
A4 = CSS + '''
@page{size:A4;margin:11mm 12mm}
body{font-size:12.5px;line-height:1.6}
.head{display:flex;justify-content:space-between;align-items:flex-end;border-bottom:3px solid #1f3a5f;padding-bottom:6px;margin-bottom:10px}
.head h1{font-size:20px;font-weight:900;color:#1f3a5f}.head .sub{font-size:11.5px;color:#556}
.who{display:flex;gap:6px;font-size:12px}.who span{border:1px solid #99a;padding:3px 10px;min-width:70px}
.note{background:#eef3f9;border-left:4px solid #1f3a5f;padding:6px 10px;margin-bottom:10px;font-size:11.5px}
.q{break-inside:avoid;margin-bottom:12px;border:1px solid #c9d3e0;border-radius:6px;overflow:hidden}
.qh{display:flex;gap:8px;align-items:center;padding:5px 10px;font-weight:700;font-size:13px}
.qh .no{background:#fff;color:#1f3a5f;border-radius:50%;width:22px;height:22px;display:flex;align-items:center;justify-content:center;font-weight:900}
.qh .tag{font-size:10.5px;font-weight:500;opacity:.85;margin-left:auto}
.qb{padding:8px 11px}
.title{font-weight:700;margin-bottom:5px}
.box{border:1px solid #9aa7b8;background:#fafbfd;padding:7px 10px;margin:5px 0;font-size:13px;line-height:1.65}
.condbox{border:1px dashed #1f3a5f;padding:4px 10px;margin:5px 0;font-size:11.5px}
.cond{display:inline-block;font-size:11.5px;color:#1f3a5f;margin-top:2px}
.part{margin-top:6px}.part .en{font-size:13px}
.line{border-bottom:1px solid #8a94a6;height:25px}
.gram{font-size:10.5px;color:#667;margin-top:4px}
.ans{color:#c0262d;font-weight:700;font-family:'Noto Serif',serif;font-size:13px;margin:3px 0}
.pt{font-size:11.5px;color:#334;margin-top:3px}.pt b{color:#1f3a5f}
.pb{break-before:page}
'''
SC = CSS + '''
@page{size:1280px 720px;margin:0}
.s{width:1280px;height:720px;padding:38px 56px;break-after:page;position:relative;overflow:hidden;background:#fff}
.s .top{display:flex;align-items:center;gap:16px;margin-bottom:18px}
.s .no{background:#1f3a5f;color:#fff;font-weight:900;font-size:30px;border-radius:12px;padding:4px 18px}
.s .tag{font-size:20px;color:#1f3a5f;font-weight:700}.s .gram{margin-left:auto;font-size:17px;color:#667}
.s .title{font-size:26px;font-weight:700;margin-bottom:12px}
.s .box{border:2px solid #9aa7b8;background:#fafbfd;padding:14px 20px;font-size:22px;line-height:1.6;margin-bottom:12px}
.s .condbox{border:2px dashed #1f3a5f;padding:8px 18px;font-size:19px;margin-bottom:10px}
.s .part{font-size:22px;line-height:1.55;margin-bottom:12px}.s .part .en{font-size:23px}
.s .cond{font-size:18px;color:#1f3a5f}
.s.a{background:#fff8f8}.s .ans{color:#c0262d;font-weight:700;font-family:'Noto Serif',serif;font-size:27px;line-height:1.5;margin-bottom:10px}
.s .pt{font-size:20px;margin-top:8px;color:#334}.s .pt b{color:#1f3a5f}
.s .foot{position:absolute;bottom:16px;right:56px;font-size:15px;color:#99a}
.cover{display:flex;flex-direction:column;justify-content:center;align-items:center;background:#1f3a5f;color:#fff}
.cover h1{font-size:54px;font-weight:900;margin-bottom:18px}.cover p{font-size:24px;opacity:.9}
'''
def qbody(q, scr=False):
    o = '<div class="title">%s</div>' % q['title']
    for b in q['box']: o += '<div class="box">%s</div>' % b
    if q['cond']: o += '<div class="condbox">&lt;조건&gt; ' + ' · '.join(q['cond']) + '</div>'
    for t, n in q['parts']:
        o += '<div class="part">%s%s</div>' % (t, '' if scr else ''.join('<div class="line"></div>' for _ in range(n)))
    return o

def a4(answer):
    h = '<!doctype html><html><head><meta charset="utf-8"><style>%s</style></head><body>' % A4
    h += '<div class="head"><div><h1>안곡고1 3·4과 본문 서술형%s</h1><div class="sub">동아(이병민) Lesson 3 Social Media Algorithms · Lesson 4 Rediscovering Art Through Science · 10문항</div></div>' % (' — 정답과 채점 포인트' if answer else '')
    h += '<div class="who"><span>번호</span><span>이름</span></div></div>' if not answer else '</div>'
    if not answer: h += '<div class="note">본문에서 문법이 가장 많이 걸린 문장만 골랐어요. 단어 수·형태 변화 조건을 끝까지 지키고, 철자·대소문자·마침표까지 정확히 쓰세요. (하이픈으로 이어진 말은 한 단어)</div>'
    for i, q in enumerate(Q, 1):
        h += '<div class="q"><div class="qh navy"><span class="no">%d</span>%s<span class="tag">%s</span></div><div class="qb">' % (i, q['gram'], q['tag'])
        if answer:
            h += '<div class="title" style="font-weight:500;color:#556">%s</div>' % re.sub('<br>.*', '', q['title'])
            for a in q['ans']: h += '<div class="ans">%s</div>' % a
            h += '<div class="pt"><b>채점 포인트</b> ' + ' / '.join(q['pts']) + '</div>'
        else:
            h += qbody(q)
        h += '</div></div>'
    return h + '</body></html>'

def screen():
    h = '<!doctype html><html><head><meta charset="utf-8"><style>%s</style></head><body>' % SC
    h += '<div class="s cover"><h1>3·4과 본문 서술형</h1><p>안곡고 1학년 · 동아(이병민) Lesson 3·4 · 10문항</p><p style="margin-top:30px;font-size:20px">문제 → 다음 장 정답</p></div>'
    for i, q in enumerate(Q, 1):
        top = '<div class="top"><span class="no">%d</span><span class="tag">%s</span><span class="gram">%s</span></div>' % (i, q['tag'], q['gram'])
        h += '<div class="s">%s%s<div class="foot">서술형 %d / 10</div></div>' % (top, qbody(q, True), i)
        a = ''.join('<div class="ans">%s</div>' % x for x in q['ans'])
        a += '<div class="pt"><b>채점 포인트</b><br>' + '<br>'.join('· ' + p for p in q['pts']) + '</div>'
        h += '<div class="s a">%s<div class="title">정답</div>%s<div class="foot">서술형 %d 정답</div></div>' % (top, a, i)
    return h + '</body></html>'

if __name__ == '__main__':
    from playwright.sync_api import sync_playwright
    files = {'서술형_시험지': a4(False), '서술형_정답': a4(True), '서술형_화면용': screen()}
    with sync_playwright() as p:
        b = p.chromium.launch(); pg = b.new_page()
        for name, doc in files.items():
            hp = '/home/claude/work/agsw_%s.html' % name; open(hp, 'w', encoding='utf-8').write(doc)
            pg.goto('file://' + hp); pg.wait_for_timeout(1200)
            if name == '서술형_화면용': pg.pdf(path=OUT + '안곡고1_3·4과_본문_' + name + '.pdf', width='1280px', height='720px', print_background=True)
            else: pg.pdf(path=OUT + '안곡고1_3·4과_본문_' + name + '.pdf', format='A4', print_background=True, prefer_css_page_size=True)
        b.close()
    print('ok')
