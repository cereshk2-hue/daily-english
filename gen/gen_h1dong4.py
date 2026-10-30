import sys, json, subprocess
sys.path.insert(0, '/tmp/claude-0/-home-claude/a9e3e882-1f02-5d62-8f70-aced81bc59d2/scratchpad')
from gencommon import write, js
from dlgcommon import ansfirst
# 고1 공통영어2 동아(이병민) Lesson 4 Explore the World of Art · 본문 Rediscovering Art Through Science ❶~❺ + Link to Art History (10/30)
# 출처: hwp23/art.txt (교재 해석 그대로). 3과 DAY 뒤에 4과 DAY 5~8 추가

B = '빈칸에 알맞은 것은?<br><b>'
def P(label, rows, title=None):
    out = [['', label, '']]
    if title: out.append(['', title[0], title[1]])
    return out + [['', e, k] for e, k in rows]
def e(S, i): return S[i][0]

S1 = [("You might have heard the expression, \"There is more than meets the eye.\"", "여러분은 '눈에 보이는 것이 다가 아니다.'라는 표현을 들어 보았을 것입니다."),
      ("It means that there is more to something than there appears to be at first.", "처음 보이는 것 외에 더 많은 것이 있다는 의미입니다."),
      ("This can apply to art as well.", "이 말은 예술에도 적용될 수 있습니다."),
      ("We appreciate art by looking at its colors, shapes, shadows, as well as the overall beauty presented by the artist.", "우리는 예술가가 표현한 전체적인 아름다움뿐만 아니라 색상, 형태, 음영을 보며 예술을 감상합니다."),
      ("Sometimes, however, there is something more to the images in front of our eyes.", "그러나 때로는 우리 눈앞에 있는 그림에 무언가가 더 있습니다."),
      ("Science, which seems far removed from art, can be the key to seeing beyond what the naked eye can see.", "과학은 예술과 동떨어져 보이지만 맨눈으로 볼 수 있는 것 너머를 보게 해 주는 실마리가 될 수 있습니다."),
      ("Today, I would like to open your eyes and minds through the following paintings.", "오늘 저는 다음 그림들을 통해 여러분의 눈과 마음을 열어보려고 합니다.")]
S2 = [("Look at the portrait of a woman on the next page.", "다음 페이지에 있는 한 여인의 초상화를 보세요."),
      ("What catches your eye?", "무엇이 여러분의 시선을 사로잡나요?"),
      ("What draws most people's attention initially is not the woman but the beautiful white animal in the woman's arms.", "대부분 사람들의 관심을 처음 끌어당기는 것은 여인이 아닌 그녀의 품속에 있는 아름다운 흰 동물입니다."),
      ("In 2014, this painting by Leonardo da Vinci was analyzed by an engineer.", "레오나르도 다빈치가 그린 이 그림은 2014년에 한 기술자에 의해 분석되었습니다."),
      ("He used special equipment to look beneath the surface of the painting and discovered that it had different layers, like those of an onion.", "그는 그림의 표면 아래를 보기 위해 특수 장비를 사용했고 그 그림에 양파처럼 여러 겹의 층이 있다는 것을 발견했습니다."),
      ("After careful examination of the layers, it was revealed that the original painting was just a normal portrait of a woman by herself.", "그 층을 면밀히 조사한 후에 원래 그림은 여인만 있는 평범한 초상화였다는 것이 밝혀졌습니다."),
      ("Then in a second version, a small gray ermine appeared.", "그다음에 두 번째 버전에서 작은 회색 담비가 나타납니다."),
      ("Finally in a third version — the one we know today — the ermine became bigger and its color changed to white.", "마지막으로 오늘날 우리가 알고 있는 세 번째 버전에서 담비가 더 커지고 색깔이 흰색으로 바뀌었습니다."),
      ("Why did Da Vinci add the ermine to this painting?", "다빈치는 왜 이 그림에 담비를 추가했을까요?"),
      ("No one knows for sure.", "그 누구도 (이유를) 확실히 알지 못합니다."),
      ("He might have done it to honor his patron.", "그의 후원자를 기리기 위해 그랬을지도 모릅니다."),
      ("Maybe he just wanted to make the painting look more special.", "그저 그 그림이 좀 더 특별해지기를 원했던 것일 수도 있습니다."),
      ("Whatever the reason, this shows us that even a great master like Leonardo da Vinci, who said, \"Art is never finished,\" made revisions to his paintings over and over again.", "그 이유가 무엇이든, 이것은 \"예술은 결코 완성되지 않는다.\"라고 말했던 레오나르도 다빈치와 같은 거장도 자신의 그림을 계속해서 수정했다는 것을 보여 줍니다.")]
S3 = [("This next piece is by the great Vincent van Gogh.", "다음은 위대한 빈센트 반 고흐의 작품입니다."),
      ("It appears to be just an ordinary painting of a woman wearing a white cap.", "그것은 흰 모자를 쓴 여인의 평범한 그림처럼 보입니다."),
      ("But thanks to technology, another person was discovered on the other side of the canvas.", "그러나 기술 덕분에 캔버스의 다른 면에서 또 다른 사람이 발견되었습니다."),
      ("Who do you think that person was?", "그 사람이 누구였을 거라고 생각하나요?"),
      ("It was Vincent van Gogh himself that was hidden at the back of the painting.", "그 그림 뒤에 숨겨져 있던 것은 바로 빈센트 반 고흐 자신이었습니다."),
      ("In 2022, the National Galleries of Scotland took an X-ray of this painting while preparing for an exhibition.", "2022년에 스코틀랜드 국립 미술관은 전시회를 준비하던 중 이 그림을 엑스레이로 촬영했습니다."),
      ("During this process, a hidden self-portrait of Van Gogh was discovered.", "이 과정에서 숨겨진 반 고흐의 자화상이 발견되었습니다."),
      ("You may be aware that Van Gogh's fame came after his death.", "여러분은 반 고흐의 명성이 그의 죽음 이후에 찾아왔다는 것을 알고 있을 것입니다."),
      ("In fact, he sold only one painting in his lifetime.", "사실, 그는 평생 동안 단 한 점의 그림만을 팔았습니다."),
      ("Being a poor artist, he often reused his canvases to save money, turning them around and painting on the opposite side.", "가난한 화가였기 때문에 그는 돈을 아끼기 위해 캔버스를 뒤집어 반대편에 그림을 그리면서 재사용하는 일이 많았습니다."),
      ("You might also notice that Van Gogh's left ear looks perfectly fine in this painting.", "여러분은 이 그림에서 반 고흐의 왼쪽 귀가 멀쩡하다는 것도 알아차렸을 것입니다."),
      ("Since he cut off part of his ear when he was 35, we can infer that this is one of his early works.", "그가 서른 다섯 살일 때 자신의 귀의 일부를 잘랐기 때문에 우리는 이 그림이 그의 초기 작품 중 하나라는 것을 추론할 수 있습니다."),
      ("It is possible that other hidden paintings of Van Gogh will be revealed to the world with the help of technology.", "과학의 도움으로 반 고흐의 숨겨진 다른 작품들이 세상에 드러나는 것도 가능해 보입니다.")]
S4 = [("Rembrandt's The Night Watch, a huge painting that measures 3.795 meters by 4.535 meters, has had a troubled history.", "높이 3.795m, 너비 4.535m 크기의 거대한 그림인 렘브란트의 '야경'은 문제가 많은 과거사를 겪었습니다."),
      ("It was damaged with a knife twice and sprayed with acid by people who wanted to destroy it.", "그림을 훼손하려는 사람들에 의해 두 차례 칼로 훼손되었고 산성 물질도 뿌려졌습니다."),
      ("Each time, experts miraculously restored the painting to its original state.", "그럴 때마다 전문가들은 기적적으로 이 그림을 원래 상태로 복원했습니다."),
      ("But did you know that this painting was much larger over three centuries ago?", "그런데 이 그림이 300년 전에는 훨씬 더 컸다는 것을 알고 있었나요?"),
      ("In 1715, this monumental painting was trimmed on all four sides to fit on a wall in Amsterdam's town hall.", "1715년에 이 대단히 큰 그림은 암스테르담 시청의 벽에 맞도록 네 면이 잘렸습니다."),
      ("Since then, 60 cm from the left side, 22 cm from the top, 12 cm from the bottom, and 7 cm from the right side have been missing.", "그때 이후로 좌측에서 60cm, 상단에서 22cm, 하단에서 12cm, 우측에서 7cm가 잘려 나간 상태가 되었습니다.")]
S5 = [("However, art lovers can now see The Night Watch as Rembrandt originally intended.", "그러나 미술 애호가들은 이제 렘브란트가 원래 의도한 대로 '야경'을 감상할 수 있습니다."),
      ("It was artificial intelligence (AI) that the museum used to recreate the missing pieces.", "사라진 조각들을 되살리기 위해 박물관에서 사용한 것은 바로 인공 지능(AI)이었습니다."),
      ("Instead of hiring human artists, an AI program was trained to learn Rembrandt's painting style.", "인간 예술가를 고용하는 대신 AI 프로그램이 렘브란트의 화풍을 학습하도록 훈련받았습니다."),
      ("Once the AI program learned to paint like Rembrandt, it was shown a copy of the original painting before it was trimmed.", "AI 프로그램이 렘브란트처럼 그리는 것을 학습한 후에는 잘리기 전 원본 그림의 복사본을 보여 줬습니다."),
      ("Then it reconstructed the missing pieces, which were hung around the painting.", "그런 다음 AI는 소실된 조각을 재구성하였고, 그 조각들은 그림의 둘레에 걸렸습니다."),
      ("For the first time in over three centuries, The Night Watch is complete again.", "300여 년 만에 처음으로 '야경'이 다시 완성된 것입니다."),
      ("Thanks to science, this great masterpiece has been brought back to life for all to see.", "과학 덕분에 이 위대한 걸작이 되살아나 모두가 감상할 수 있게 되었습니다.")]
S6 = [("Rembrandt's painting, widely known as The Night Watch (1642), actually has nothing to do with night.", "'야경'(1642)으로 널리 알려진 렘브란트의 그림은 실은 밤과 아무런 관련이 없다."),
      ("In fact, it was a painting of a daytime event.", "사실 그것은 낮에 일어난 사건을 그린 그림이었다."),
      ("In the late 18th century, however, people began to call it The Night Watch because dust and varnish gathered on the painting and made it look darker.", "그러나 18세기 후반에 사람들은 그 그림을 '야경'이라고 부르기 시작했는데, 그림에 먼지와 광택제가 쌓이면서 어두워 보였기 때문이었다."),
      ("People began to mistakenly believe that the painting was a night scene.", "사람들은 그 그림이 밤의 풍경이라고 잘못 생각하기 시작했다."),
      ("The varnish was removed during the 1940s, but the name remained.", "광택제는 1940년대에 제거되었지만, 그 이름은 그대로 남았다.")]

def steps(vocab, pickv, tf, ilchi, pickg, verb, error, scr, order, insert, odd, blank, gram, summ):
    MCG = "선택지는 본문을 다른 어휘로 바꿔 쓴 문장이에요. 풀고 나서 해설의 어휘를 꼭 확인하세요."
    st = [{'type': 'vocab', 'title': '핵심어휘·숙어', 'quizN': min(15, len(vocab)), 'items': vocab}]
    def add(lst, s):
        if lst: st.append(s)
    add(pickv, {'type': 'pick', 'title': '어휘선택', 'guide': '문맥에 맞는 낱말을 고르세요.', 'items': [{'s': s, 'ex': x} for s, x in pickv]})
    add(tf, {'type': 'tf', 'title': 'T/F 내용 확인', 'guide': '본문 내용과 일치하면 T, 다르면 F를 고르세요.', 'items': tf})
    add(ilchi, {'type': 'mc', 'title': '일치·불일치', 'guide': MCG, 'items': ilchi})
    add(pickg, {'type': 'pick', 'title': '어법선택', 'guide': '어법상 알맞은 것을 고르세요.', 'items': [{'s': s, 'ex': x} for s, x in pickg]})
    add(verb, {'type': 'verb', 'title': '동사변형', 'guide': '( ) 안의 동사를 알맞은 형태로 바꿔 쓰세요.', 'items': [{'s': s, 'v': v, 'a': a, 'ex': x} for s, v, a, x in verb]})
    add(error, {'type': 'error', 'title': '오류찾기', 'guide': '어법상 틀린 곳을 고르세요.', 'items': [{'s': s, 'w': w, 'fix': f, 'ex': x} for s, w, f, x in error]})
    add(scr, {'type': 'scramble', 'title': '본문 스크램블', 'guide': '우리말에 맞게 단어를 눌러 문장을 완성하세요.', 'items': [{'ko': k, 'en': en} for en, k in scr]})
    add(order, {'type': 'order', 'title': '문장순서', 'guide': '문장을 본문 순서대로 눌러서 배열하세요.', 'items': [{'lines': l, 'flow': f} for l, f in order]})
    add(insert, {'type': 'insert', 'title': '문장삽입', 'guide': '주어진 문장이 들어가기에 가장 알맞은 곳을 고르세요.', 'items': [{'lines': l, 'given': g, 'flow': f, 'ex': x} for l, g, f, x in insert]})
    add(odd, {'type': 'odd', 'title': '어색한 문장', 'guide': '글의 흐름과 관계없는 문장을 고르세요.', 'items': [{'lines': l, 'odd': o, 'ex': x} for l, o, x in odd]})
    add(blank, {'type': 'blank', 'title': '빈칸추론', 'guide': '빈칸에 들어갈 말로 가장 알맞은 것을 고르세요.', 'items': [{'s': s, 'opts': o, 'ex': x} for s, o, x in blank]})
    add(gram, {'type': 'mc', 'title': '핵심문법', 'guide': '알맞은 답을 고르세요.', 'items': [{'q': q, 'opts': o, 'ex': x} for q, o, x in gram]})
    add(summ, {'type': 'mc', 'title': '요약문 완성', 'guide': '본문을 읽고 요약문의 빈칸 (A), (B)에 들어갈 말을 고르세요.',
               'items': [{'n': n, 'box': box, 'q': '다음 글의 내용을 한 문장으로 요약할 때, 빈칸 (A), (B)에 들어갈 말로 가장 알맞은 것은?<br><b>' + s + '</b>', 'opts': o, 'ex': x, 'ev': ev} for n, box, s, o, x, ev in summ]})
    return st

# ═════════════ DAY 5 · 4과 본문 ❶❷ ═════════════
d5 = steps(
 vocab=[[w, m, '❶'] for w, m in [('There is more than meets the eye.', '눈에 보이는 것이 다가 아니다.'), ('expression', '표현'), ('apply to', '~에 적용되다'), ('as well', '또한'), ('appreciate', '감상하다, 진가를 알다'),
        ('A as well as B', 'B뿐만 아니라 A도'), ('overall', '전체적인'), ('far removed from', '~와 동떨어진'), ('the key to -ing', '~하는 것의 열쇠[실마리]'), ('the naked eye', '맨눈, 육안'), ('following', '다음의, 이하의')]] +
       [[w, m, '❷'] for w, m in [('portrait', '초상화'), ('catch one\'s eye', '~의 눈길을 끌다'), ('draw attention', '관심을 끌다'), ('initially', '처음에'), ('analyze', '분석하다'), ('equipment', '장비'),
        ('beneath', '~의 아래에'), ('surface', '표면'), ('layer', '층, 겹'), ('examination', '조사, 검사'), ('reveal', '드러내다, 밝히다'), ('by oneself', '혼자'), ('ermine', '담비'),
        ('for sure', '확실히'), ('honor', '기리다, 존경하다'), ('patron', '후원자'), ('make revisions to', '~을 수정하다'), ('over and over again', '계속해서, 되풀이하여')]],
 pickv=[
  ("We {appreciate|depreciate} art by looking at its colors, shapes, shadows, as well as the overall beauty presented by the artist.", "정답 ▶ appreciate (감상하다)\n오답 ▶ depreciate (가치가 떨어지다): 색상·형태·음영을 보며 예술을 '감상한다'"),
  ("Science, which seems far {removed|related} from art, can be the key to seeing beyond what the naked eye can see.", "정답 ▶ removed\n이유: far removed from ~ = ~와 동떨어진. 과학은 예술과 '동떨어져 보이지만' 실마리가 될 수 있다(대조)\n오답 ▶ related는 from과 쓰지 않고 related to(~와 관련된)예요."),
  ("What draws most people's attention {initially|finally} is not the woman but the beautiful white animal in the woman's arms.", "정답 ▶ initially (처음에)\n이유: 그림을 보자마자 '처음' 눈길을 끄는 것\n오답 ▶ finally (마침내)"),
  ("He used special equipment to look {beneath|above} the surface of the painting and discovered that it had different layers, like those of an onion.", "정답 ▶ beneath (~ 아래에)\n이유: 표면 '아래'를 보고 여러 층을 발견했어요."),
  ("After careful examination of the layers, it was {revealed|concealed} that the original painting was just a normal portrait of a woman by herself.", "정답 ▶ revealed (밝혀졌다)\n오답 ▶ concealed (숨겨졌다): 조사 '후에' 사실이 밝혀진 거예요."),
  ("He might have done it to {honor|blame} his patron.", "정답 ▶ honor (기리다)\n오답 ▶ blame (비난하다): 담비를 넣은 이유 → 후원자를 '기리기' 위해"),
  ("Whatever the reason, this shows us that even a great master like Leonardo da Vinci, who said, \"Art is never finished,\" made {revisions|decisions} to his paintings over and over again.", "정답 ▶ revisions (수정)\n이유: \"예술은 결코 완성되지 않는다\" → 계속 '수정했다'"),
 ],
 tf=[
  ["The writer suggests that art has more to it than what we see at first glance.", True, "정답 ▶ T\n이유: There is more than meets the eye가 예술에도 적용된다(This can apply to art as well).\n포인트 ▶ at first glance 처음 봤을 때", '❶', "This can apply to art as well"],
  ["According to the writer, science has nothing to offer the art world.", False, "정답 ▶ F\n이유: 과학은 예술과 동떨어져 보이지만 맨눈 너머를 보는 실마리(the key)가 될 수 있다고 했어요.", '❶', "can be the key to seeing beyond what the naked eye can see"],
  ["Most viewers first notice the woman's face in the portrait.", False, "정답 ▶ F\n이유: 처음 관심을 끄는 것은 여인이 아니라(not the woman) 품속의 흰 동물이에요.", '❷', "is not the woman but the beautiful white animal in the woman's arms"],
  ["An engineer examined the painting with special tools in 2014.", True, "정답 ▶ T\n이유: In 2014 ~ analyzed by an engineer · special equipment = special tools", '❷', "In 2014, this painting by Leonardo da Vinci was analyzed by an engineer"],
  ["The ermine was gray in the version we see today.", False, "정답 ▶ F\n이유: 회색 담비는 두 번째 버전, 오늘날 버전(세 번째)에서는 흰색(white)으로 바뀌었어요.", '❷', "the ermine became bigger and its color changed to white"],
  ["The exact reason why Da Vinci added the ermine is unknown.", True, "정답 ▶ T\n이유: No one knows for sure. → 정확한 이유는 알려지지 않았어요.", '❷', "No one knows for sure"],
 ],
 ilchi=[
  {'n': '❷', 'box': ['❷'], 'q': "글의 내용과 일치하지 <u>않는</u> 것은?",
   'opts': ["The ermine was part of Da Vinci's original plan from the very first version.", "Special equipment showed that the painting had several layers.", "In the second version, the ermine was small and gray.", "The ermine grew larger in the final version.", "The writer offers possible reasons for adding the ermine."],
   'ex': "정답 ▶ The ermine was part of Da Vinci's original plan from the very first version.\n이유: 원래 그림은 여인 혼자(a woman by herself)인 평범한 초상화였고, 담비는 두 번째 버전에서 나타났어요.\n오답 ▶ several layers = different layers · grew larger = became bigger · possible reasons = might have done it to honor ~ / Maybe he just wanted ~",
   'per': [["담비는 처음 버전부터 다빈치의 원래 계획이었다.", "the original painting was just a normal portrait of a woman by herself", "불일치 → 처음엔 여인만 있었음"],
           ["특수 장비로 그림에 여러 층이 있다는 것이 드러났다.", "discovered that it had different layers", "일치"],
           ["두 번째 버전에서 담비는 작고 회색이었다.", "Then in a second version, a small gray ermine appeared", "일치"],
           ["마지막 버전에서 담비가 더 커졌다.", "the ermine became bigger", "일치"],
           ["글쓴이는 담비를 추가한 가능한 이유들을 제시한다.", "He might have done it to honor his patron", "일치"]]},
 ],
 pickg=[
  ("You might {have heard|hear} the expression, \"There is more than meets the eye.\"", "정답 ▶ have heard\n이유: might have p.p. = (과거에) ~했을지도 모른다"),
  ("We appreciate art by looking at its colors, shapes, shadows, as well as the overall beauty {presented|presenting} by the artist.", "정답 ▶ presented\n이유: 아름다움이 예술가에 의해 '표현된' 수동 → 과거분사 presented (by the artist)"),
  ("Sometimes, however, there {is|are} something more to the images in front of our eyes.", "정답 ▶ is\n이유: There is + 단수 주어(something more)"),
  ("Science, {which|that} seems far removed from art, can be the key to seeing beyond what the naked eye can see.", "정답 ▶ which\n이유: 콤마 뒤 계속적 용법 → which (that은 쓸 수 없어요)"),
  ("Science, which seems far removed from art, can be the key to {seeing|see} beyond what the naked eye can see.", "정답 ▶ seeing\n이유: the key to + 동명사 (to는 전치사)"),
  ("{What|That} draws most people's attention initially is not the woman but the beautiful white animal in the woman's arms.", "정답 ▶ What\n이유: 선행사 없이 '~하는 것'의 주어 역할 → 관계대명사 What (What ~ initially가 문장 전체의 주어)"),
  ("In 2014, this painting by Leonardo da Vinci {was analyzed|analyzed} by an engineer.", "정답 ▶ was analyzed\n이유: 그림이 '분석된' 수동 + by an engineer"),
  ("Maybe he just wanted to make the painting {look|to look} more special.", "정답 ▶ look\n이유: 사역동사 make + O + 동사원형"),
 ],
 verb=[
  ("It ___ that there is more to something than there appears to be at first.", 'mean', ['means'], "정답 ▶ means\n이유: 주어 It(3인칭 단수) + 현재 → means"),
  ("We appreciate art by ___ at its colors, shapes, shadows, as well as the overall beauty presented by the artist.", 'look', ['looking'], "정답 ▶ looking\n이유: by + 동명사 (~함으로써)"),
  ("He used special equipment ___ beneath the surface of the painting.", 'look', ['to look'], "정답 ▶ to look\n이유: 목적(~하기 위해) → to부정사"),
  ("Then in a second version, a small gray ermine ___.", 'appear', ['appeared'], "정답 ▶ appeared\n이유: 과거의 일 → appeared (appear는 자동사라 수동태 불가)"),
  ("He might have ___ it to honor his patron.", 'do', ['done'], "정답 ▶ done\n이유: might have + p.p. (do - did - done)"),
  ("Whatever the reason, this shows us that even a great master like Leonardo da Vinci, who said, \"Art is never finished,\" ___ revisions to his paintings over and over again.", 'make', ['made'], "정답 ▶ made\n이유: 과거의 일 (make - made - made)"),
 ],
 error=[
  ("You might [[have heard]] the expression, \"There is more than meets the eye.\" It [[means]] that there is more to something than there [[appear]] to be at [[first]].", 2, 'appears', "정답 ▶ appear → appears\n이유: 주어 there(유도부사) 뒤의 생략된 주어는 단수 something → appears"),
  ("Science, [[that]] seems far [[removed]] from art, can be the key to [[seeing]] beyond [[what]] the naked eye can see.", 0, 'which', "정답 ▶ that → which\n이유: 콤마 뒤 계속적 용법에는 that을 쓸 수 없어요."),
  ("[[What]] draws most people's attention initially [[are]] not the woman but the beautiful white animal [[in]] the woman's [[arms]].", 1, 'is', "정답 ▶ are → is\n이유: What 절(관계대명사절) 주어는 단수 취급 → is"),
  ("Maybe he just [[wanted]] to [[make]] the painting [[to look]] more [[special]].", 2, 'look', "정답 ▶ to look → look\n이유: make + O + 동사원형"),
 ],
 scr=[(e(S1, 2), S1[2][1]), (e(S1, 6), S1[6][1]), (e(S2, 9), S2[9][1]), (e(S2, 10), S2[10][1])],
 order=[
  ([e(S1, 0), e(S1, 1), e(S1, 2), e(S1, 3)], ["'눈에 보이는 게 다가 아니다' 표현", "처음 보이는 것 외에 더 있다는 뜻", "예술에도 적용됨", "우리는 색·형태·음영을 보며 감상"]),
  ([e(S2, 5), e(S2, 6), e(S2, 7), e(S2, 8)], ["원래는 여인 혼자인 초상화", "두 번째 버전: 작은 회색 담비", "세 번째 버전: 커지고 흰색", "왜 담비를 추가했을까?"]),
 ],
 insert=[
  ([e(S1, 4), e(S1, 5), e(S1, 6)], 1, ["눈앞의 그림에 무언가 더 있다", "과학이 맨눈 너머를 보는 열쇠", "다음 그림들로 눈과 마음을 열겠다"], "정답 ▶ 과학 문장은 '무언가 더 있다' 뒤, '다음 그림들' 앞\n이유: 무언가 더 있다 → 그것을 보는 열쇠가 과학 → 그래서 그림들을 소개"),
  ([e(S2, 9), e(S2, 10), e(S2, 11)], 1, ["아무도 확실히 모른다", "후원자를 기리려 했을지도", "그냥 더 특별하게 하고 싶었을지도"], "정답 ▶ '확실히 모른다' 뒤에 추측 1(might have done) → 추측 2(Maybe)"),
 ],
 odd=[
  ([e(S1, 3), e(S1, 4), "Many museums offer discounts to students on weekends.", e(S1, 5)], 2, "정답 ▶ 학생 할인 문장\n이유: 박물관 할인은 '예술을 더 깊이 보는 열쇠로서의 과학'이라는 흐름과 관계없어요."),
  ([e(S2, 3), e(S2, 4), "Onions are widely used in Italian cooking.", e(S2, 5)], 2, "정답 ▶ 양파 요리 문장\n이유: like those of an onion은 비유일 뿐, 양파 요리 이야기는 흐름과 관계없어요."),
 ],
 blank=[
  ("Science, which seems far removed from art, can be the key to seeing beyond ____.", ["what the naked eye can see", "what the artist sold", "the price of the painting", "the walls of the museum"], "정답 ▶ what the naked eye can see\n이유: 과학으로 '맨눈으로 볼 수 있는 것' 너머를 본다 → 첫 문장 There is more than meets the eye와 같은 뜻"),
  ("After careful examination of the layers, it was revealed that the original painting was just ____.", ["a normal portrait of a woman by herself", "a painting of a white ermine", "a landscape with animals", "a portrait of Da Vinci's patron"], "정답 ▶ a normal portrait of a woman by herself\n이유: 담비는 두 번째 버전부터 나타났어요."),
  ("Whatever the reason, this shows us that even a great master like Leonardo da Vinci, who said, \"Art is never finished,\" ____ over and over again.", ["made revisions to his paintings", "sold his paintings", "copied other artists", "gave up painting"], "정답 ▶ made revisions to his paintings\n이유: \"Art is never finished\" → 계속 수정했다"),
 ],
 gram=[
  (B + "You might ______ the expression before.</b>", ['have heard', 'heard', 'hear', 'be heard'], "정답 ▶ have heard\n이유: might have p.p. = ~했을지도 모른다 (과거에 대한 추측)"),
  (B + "______ draws most people's attention is the white animal.</b>", ['What', 'That', 'Which', 'It'], "정답 ▶ What\n이유: 선행사를 포함한 관계대명사 what (= the thing that)"),
  ("다음 문장과 뜻이 같은 것은?<br><b>What draws attention is not the woman but the animal.</b>", ["What draws attention is the animal, not the woman.", "Both the woman and the animal draw attention.", "Neither the woman nor the animal draws attention.", "The woman draws more attention than the animal."], "정답 ▶ What draws attention is the animal, not the woman.\n이유: not A but B = A가 아니라 B (= B, not A)"),
  (B + "It was revealed ______ the original painting was a normal portrait.</b>", ['that', 'what', 'which', 'whether'], "정답 ▶ that\n이유: 가주어 it ~ 진주어 that절 (완전한 절)"),
  (B + "He wanted to make the painting ______ more special.</b>", ['look', 'to look', 'looking', 'looked'], "정답 ▶ look\n이유: make + O + 동사원형"),
 ],
 summ=[
  (None, ['❶'], "Although science seems (A) ______ from art, it can help us see what we cannot (B) ______ with the naked eye.",
   ['(A) far removed – (B) see', '(A) closely related – (B) see', '(A) far removed – (B) sell', '(A) borrowed – (B) touch', '(A) closely related – (B) hide'],
   "정답 ▶ (A) far removed – (B) see\n(A) 과학은 예술과 '동떨어져' 보인다 → far removed\n(B) 맨눈으로 '볼' 수 없는 것을 보게 해 준다 → see",
   ["Science, which seems far removed from art", "can be the key to seeing beyond what the naked eye can see"]),
  (None, ['❷'], "Technical analysis revealed that Da Vinci's portrait had several (A) ______, showing that even a great master kept (B) ______ his work.",
   ['(A) layers – (B) revising', '(A) layers – (B) selling', '(A) colors – (B) revising', '(A) frames – (B) hiding', '(A) owners – (B) copying'],
   "정답 ▶ (A) layers – (B) revising\n(A) 양파처럼 여러 '층' → layers\n(B) 계속해서 '수정했다(made revisions)' → revising",
   ["discovered that it had different layers", "made revisions to his paintings over and over again"]),
 ])

# ═════════════ DAY 6 · 4과 본문 ❸ ═════════════
d6 = steps(
 vocab=[[w, m, '❸'] for w, m in [('piece', '작품'), ('appear to be', '~인 것 같다, ~처럼 보이다'), ('ordinary', '평범한'), ('cap', '(챙 없는) 모자'), ('thanks to', '~ 덕분에'),
        ('canvas', '캔버스, 화폭'), ('hidden', '숨겨진'), ('take an X-ray of', '~을 엑스레이로 촬영하다'), ('prepare for', '~을 준비하다'), ('exhibition', '전시회'),
        ('self-portrait', '자화상'), ('be aware that', '~을 알고 있다'), ('fame', '명성'), ('lifetime', '평생, 생애'), ('reuse', '재사용하다'), ('save money', '돈을 아끼다'),
        ('turn around', '뒤집다, 돌리다'), ('opposite', '반대편의'), ('notice', '알아차리다'), ('cut off', '잘라 내다'), ('infer', '추론하다'), ('early works', '초기 작품'), ('reveal', '드러내다')]],
 pickv=[
  ("It appears to be just an {ordinary|extraordinary} painting of a woman wearing a white cap.", "정답 ▶ ordinary (평범한)\n이유: 겉으로는 '평범해' 보이지만(But) 뒤에 다른 사람이 숨어 있었어요."),
  ("But thanks to technology, another person was {discovered|destroyed} on the other side of the canvas.", "정답 ▶ discovered (발견되었다)\n오답 ▶ destroyed (파괴되었다)"),
  ("In 2022, the National Galleries of Scotland took an X-ray of this painting while preparing for an {exhibition|examination}.", "정답 ▶ exhibition (전시회)\n오답 ▶ examination (조사, 시험): 미술관이 '전시회'를 준비하다가"),
  ("You may be aware that Van Gogh's {fame|failure} came after his death.", "정답 ▶ fame (명성)\n이유: 살아서는 한 점만 팔았다(In fact) → 명성은 죽은 뒤에 왔다"),
  ("Being a poor artist, he often {reused|refused} his canvases to save money, turning them around and painting on the opposite side.", "정답 ▶ reused (재사용했다)\n오답 ▶ refused (거절했다): 돈을 아끼려고 캔버스를 '재사용'"),
  ("Since he cut off part of his ear when he was 35, we can {infer|deny} that this is one of his early works.", "정답 ▶ infer (추론하다)\n이유: 귀가 멀쩡하다 → 귀를 자르기 전 → 초기 작품이라고 '추론'"),
 ],
 tf=[
  ["At first glance, the van Gogh painting looks like an ordinary portrait of a woman.", True, "정답 ▶ T\n이유: It appears to be just an ordinary painting of a woman wearing a white cap.", '❸', "It appears to be just an ordinary painting of a woman wearing a white cap"],
  ["A hidden self-portrait was found on the front of the canvas.", False, "정답 ▶ F\n이유: 캔버스의 다른 면(the other side), 그림 뒤(at the back)에서 발견되었어요.", '❸', "another person was discovered on the other side of the canvas"],
  ["The X-ray was taken while a museum was getting ready for an exhibition.", True, "정답 ▶ T\n이유: while preparing for an exhibition · get ready for = prepare for", '❸', "while preparing for an exhibition"],
  ["Van Gogh became famous while he was alive.", False, "정답 ▶ F\n이유: 명성은 죽은 뒤에(after his death) 찾아왔고, 살아서는 단 한 점만 팔았어요.", '❸', "Van Gogh's fame came after his death"],
  ["Van Gogh painted on both sides of his canvases because he was short of money.", True, "정답 ▶ T\n이유: 가난해서 돈을 아끼려고 캔버스를 뒤집어 반대편에 그렸어요. be short of money = 돈이 부족하다", '❸', "he often reused his canvases to save money"],
  ["The hidden self-portrait shows that it was painted after Van Gogh cut his ear.", False, "정답 ▶ F\n이유: 왼쪽 귀가 멀쩡하다 → 귀를 자르기 전의 초기 작품이라고 추론해요.", '❸', "we can infer that this is one of his early works"],
 ],
 ilchi=[
  {'n': '❸', 'box': ['❸'], 'q': "글의 내용과 일치하지 <u>않는</u> 것은?",
   'opts': ["Van Gogh sold many paintings during his lifetime.", "An X-ray revealed the self-portrait in 2022.", "Van Gogh often turned his canvases around to paint again.", "Van Gogh's left ear appears undamaged in the hidden portrait.", "More hidden works by Van Gogh may be found in the future."],
   'ex': "정답 ▶ Van Gogh sold many paintings during his lifetime.\n이유: 사실 그는 평생 단 한 점만(only one painting) 팔았어요.\n오답 ▶ undamaged = perfectly fine · may be found = will be revealed",
   'per': [["반 고흐는 생전에 많은 그림을 팔았다.", "In fact, he sold only one painting in his lifetime", "불일치 → 단 한 점만 팖"],
           ["2022년에 엑스레이로 자화상이 드러났다.", "a hidden self-portrait of Van Gogh was discovered", "일치"],
           ["반 고흐는 캔버스를 뒤집어 다시 그리는 일이 많았다.", "turning them around and painting on the opposite side", "일치"],
           ["숨겨진 자화상에서 반 고흐의 왼쪽 귀는 다치지 않은 모습이다.", "Van Gogh's left ear looks perfectly fine in this painting", "일치"],
           ["앞으로 반 고흐의 숨겨진 작품이 더 발견될 수 있다.", "other hidden paintings of Van Gogh will be revealed", "일치"]]},
 ],
 pickg=[
  ("It appears to be just an ordinary painting of a woman {wearing|worn} a white cap.", "정답 ▶ wearing\n이유: 여인이 모자를 '쓰고 있는' 능동 → 현재분사 wearing"),
  ("Who do you {think|thinks} that person was?", "정답 ▶ think\n이유: 의문사 + do you think + 주어 + 동사 (간접의문문, do 뒤 동사원형)"),
  ("It was Vincent van Gogh himself {that|what} was hidden at the back of the painting.", "정답 ▶ that\n이유: It was ~ that 강조 구문 (강조 대상: Vincent van Gogh himself)"),
  ("In 2022, the National Galleries of Scotland took an X-ray of this painting while {preparing|prepared} for an exhibition.", "정답 ▶ preparing\n이유: 미술관이 '준비하는' 능동 → while + 현재분사"),
  ("During this process, a hidden self-portrait of Van Gogh {was discovered|discovered}.", "정답 ▶ was discovered\n이유: 자화상이 '발견된' 수동"),
  ("{Being|Been} a poor artist, he often reused his canvases to save money.", "정답 ▶ Being\n이유: 분사구문 (= Because he was a poor artist) → Being"),
  ("Being a poor artist, he often reused his canvases to save money, {turning|turned} them around and painting on the opposite side.", "정답 ▶ turning\n이유: 그가 캔버스를 '뒤집는' 능동 → 분사구문 turning (painting과 병렬)"),
 ],
 verb=[
  ("It appears ___ just an ordinary painting of a woman wearing a white cap.", 'be', ['to be'], "정답 ▶ to be\n이유: appear to be ~ = ~인 것 같다"),
  ("In fact, he ___ only one painting in his lifetime.", 'sell', ['sold'], "정답 ▶ sold\n이유: 과거 (sell - sold - sold)"),
  ("He often reused his canvases ___ money.", 'save', ['to save'], "정답 ▶ to save\n이유: 목적(~하기 위해) → to부정사"),
  ("Since he ___ off part of his ear when he was 35, we can infer that this is one of his early works.", 'cut', ['cut'], "정답 ▶ cut\n이유: 과거 (cut - cut - cut)"),
  ("It is possible that other hidden paintings of Van Gogh will be ___ to the world.", 'reveal', ['revealed'], "정답 ▶ revealed\n이유: 그림들이 '드러나는' 수동 → will be revealed"),
 ],
 error=[
  ("It [[appears]] to be just an ordinary painting of a woman [[worn]] a white cap. But [[thanks to]] technology, another person [[was discovered]].", 1, 'wearing', "정답 ▶ worn → wearing\n이유: 여인이 모자를 '쓰고 있는' 능동 → 현재분사"),
  ("Who [[do you think]] that person [[was]]? It was Vincent van Gogh himself [[what]] was [[hidden]] at the back of the painting.", 2, 'that', "정답 ▶ what → that\n이유: It was ~ that 강조 구문"),
  ("[[Been]] a poor artist, he often [[reused]] his canvases [[to save]] money, [[turning]] them around.", 0, 'Being', "정답 ▶ Been → Being\n이유: 분사구문 Being (= Because he was ~)"),
  ("You might also [[notice]] that Van Gogh's left ear [[looks]] [[perfectly]] [[finely]] in this painting.", 3, 'fine', "정답 ▶ finely → fine\n이유: look + 형용사(보어) → fine (perfectly는 fine을 꾸미는 부사)"),
 ],
 scr=[(e(S3, 3), S3[3][1]), (e(S3, 8), S3[8][1]), (e(S3, 6), S3[6][1])],
 order=[
  ([e(S3, 1), e(S3, 2), e(S3, 3), e(S3, 4)], ["평범한 여인 그림처럼 보임", "기술 덕분에 다른 면에서 다른 사람 발견", "그 사람은 누구일까?", "바로 반 고흐 자신"]),
  ([e(S3, 7), e(S3, 8), e(S3, 9)], ["명성은 죽은 뒤에", "생전에 단 한 점 판매", "가난해서 캔버스를 재사용"]),
 ],
 insert=[
  ([e(S3, 2), e(S3, 3), e(S3, 4)], 1, ["다른 면에서 다른 사람 발견", "그 사람(that person)은 누구일까?", "바로 반 고흐 자신"], "정답 ▶ 질문은 '다른 사람 발견' 뒤, 대답 앞\n이유: that person = another person"),
  ([e(S3, 10), e(S3, 11), e(S3, 12)], 1, ["왼쪽 귀가 멀쩡하다", "그래서 초기 작품이라고 추론", "앞으로 더 발견될 가능성"], "정답 ▶ 추론 문장은 '귀가 멀쩡하다' 바로 뒤\n이유: 귀가 멀쩡하다 → 35세 전 → 초기 작품"),
 ],
 odd=[
  ([e(S3, 5), e(S3, 6), "Scotland is famous for its beautiful lakes and castles.", e(S3, 7)], 2, "정답 ▶ 스코틀랜드 호수·성 문장\n이유: 엑스레이로 자화상을 발견한 이야기와 관계없어요."),
  ([e(S3, 8), e(S3, 9), "Today, many artists sell their works online.", e(S3, 10)], 2, "정답 ▶ 요즘 온라인 판매 문장\n이유: 반 고흐의 가난과 캔버스 재사용 이야기와 관계없어요."),
 ],
 blank=[
  ("It appears to be just an ordinary painting. But thanks to technology, ____ was discovered on the other side of the canvas.", ["another person", "a famous poem", "a hidden letter", "a second signature"], "정답 ▶ another person\n이유: 다음 문장 Who do you think that person was? → '다른 사람'"),
  ("Being a poor artist, he often ____ to save money.", ["reused his canvases", "sold his brushes", "borrowed paintings", "painted on walls"], "정답 ▶ reused his canvases\n이유: 캔버스를 뒤집어 반대편에 그림 → 재사용"),
  ("Since he cut off part of his ear when he was 35, we can infer that this is ____.", ["one of his early works", "his last painting", "a copy by another artist", "a painting of his friend"], "정답 ▶ one of his early works\n이유: 귀가 멀쩡 → 귀를 자르기 전 → 초기 작품"),
 ],
 gram=[
  (B + "It was Van Gogh himself ______ was hidden at the back.</b>", ['that', 'what', 'which', 'when'], "정답 ▶ that\n이유: It was ~ that 강조 구문"),
  ("다음 문장과 뜻이 같은 것은?<br><b>Being a poor artist, he reused his canvases.</b>", ["Because he was a poor artist, he reused his canvases.", "Although he was a poor artist, he reused his canvases.", "If he was a poor artist, he reused his canvases.", "Before he was a poor artist, he reused his canvases."], "정답 ▶ Because he was a poor artist, he reused his canvases.\n이유: 분사구문 Being ~ = 이유(~이기 때문에)"),
  (B + "Who do you think ______?</b>", ['that person was', 'was that person', 'did that person', 'that person did be'], "정답 ▶ that person was\n이유: 의문사 + do you think + 주어 + 동사 (간접의문문 어순)"),
  (B + "a woman ______ a white cap</b>", ['wearing', 'worn', 'wears', 'to wearing'], "정답 ▶ wearing\n이유: 명사를 뒤에서 꾸미는 현재분사(능동)"),
  (B + "It appears ______ an ordinary painting.</b>", ['to be', 'being', 'be', 'been'], "정답 ▶ to be\n이유: appear + to부정사 = ~인 것 같다"),
 ],
 summ=[
  (None, ['❸'], "An X-ray of a van Gogh painting revealed a hidden (A) ______ on the back of the canvas, which he had (B) ______ because he was poor.",
   ['(A) self-portrait – (B) reused', '(A) self-portrait – (B) sold', '(A) letter – (B) reused', '(A) landscape – (B) bought', '(A) signature – (B) destroyed'],
   "정답 ▶ (A) self-portrait – (B) reused\n(A) 숨겨진 '자화상' → self-portrait\n(B) 가난해서 캔버스를 '재사용했다' → reused",
   ["a hidden self-portrait of Van Gogh was discovered", "he often reused his canvases to save money"]),
  (None, ['❸'], "Because Van Gogh's ear looks (A) ______ in the painting, we can guess that it is one of his (B) ______ works.",
   ['(A) fine – (B) early', '(A) injured – (B) early', '(A) fine – (B) last', '(A) injured – (B) final', '(A) small – (B) famous'],
   "정답 ▶ (A) fine – (B) early\n(A) 왼쪽 귀가 '멀쩡해' 보인다 → fine\n(B) 귀를 자르기 전이니 '초기' 작품 → early",
   ["Van Gogh's left ear looks perfectly fine in this painting", "this is one of his early works"]),
 ])

# ═════════════ DAY 7 · 4과 본문 ❹❺ ═════════════
d7 = steps(
 vocab=[[w, m, '❹'] for w, m in [('masterpiece', '걸작'), ('as a whole', '전체로서, 온전한'), ('measure', '(치수가) ~이다'), ('troubled', '문제가 많은, 힘든'), ('damage', '훼손하다'),
        ('spray', '뿌리다'), ('acid', '산(성 물질)'), ('destroy', '파괴하다'), ('miraculously', '기적적으로'), ('restore A to B', 'A를 B로 복원하다'), ('original state', '원래 상태'),
        ('century', '세기, 100년'), ('monumental', '대단히 큰, 기념비적인'), ('trim', '다듬다, 잘라 내다'), ('fit on', '~에 맞다'), ('town hall', '시청'), ('missing', '빠진, 없어진')]] +
       [[w, m, '❺'] for w, m in [('art lover', '미술 애호가'), ('intend', '의도하다'), ('artificial intelligence', '인공 지능'), ('recreate', '되살리다, 재현하다'), ('instead of', '~ 대신에'),
        ('hire', '고용하다'), ('be trained to', '~하도록 훈련받다'), ('once', '일단 ~하면'), ('reconstruct', '재구성하다'), ('complete', '완전한'), ('bring ~ back to life', '~을 되살리다')]],
 pickv=[
  ("Rembrandt's The Night Watch, a huge painting that measures 3.795 meters by 4.535 meters, has had a {troubled|peaceful} history.", "정답 ▶ troubled (문제가 많은)\n이유: 다음 문장에서 칼로 훼손되고 산성 물질이 뿌려졌다고 해요."),
  ("Each time, experts miraculously {restored|removed} the painting to its original state.", "정답 ▶ restored (복원했다)\n이유: restore A to its original state = A를 원래 상태로 복원하다"),
  ("In 1715, this monumental painting was {trimmed|enlarged} on all four sides to fit on a wall in Amsterdam's town hall.", "정답 ▶ trimmed (잘렸다)\n이유: 벽에 맞추려고 네 면을 '잘라 냈다' → 그 뒤로 일부가 없어졌다(missing)"),
  ("It was artificial intelligence (AI) that the museum used to {recreate|remove} the missing pieces.", "정답 ▶ recreate (되살리다)\n오답 ▶ remove (제거하다): 없어진 조각을 '되살렸다'"),
  ("Instead of {hiring|firing} human artists, an AI program was trained to learn Rembrandt's painting style.", "정답 ▶ hiring (고용하기)\n이유: 인간 화가를 '고용하는' 대신 AI를 썼어요."),
  ("Then it {reconstructed|destroyed} the missing pieces, which were hung around the painting.", "정답 ▶ reconstructed (재구성했다)\n이유: 재구성한 조각들을 그림 둘레에 걸었어요."),
 ],
 tf=[
  ["The Night Watch has been attacked more than once.", True, "정답 ▶ T\n이유: 칼로 두 번 훼손되었고(twice) 산성 물질도 뿌려졌어요.", '❹', "It was damaged with a knife twice and sprayed with acid"],
  ["The painting was made bigger in 1715 to fill a wall.", False, "정답 ▶ F\n이유: 1715년에 벽에 맞추려고 네 면을 잘랐어요(trimmed) → 더 작아졌어요.", '❹', "this monumental painting was trimmed on all four sides"],
  ["The largest missing part was cut from the left side.", True, "정답 ▶ T\n이유: 좌측 60cm, 상단 22cm, 하단 12cm, 우측 7cm → 좌측이 가장 커요.", '❹', "60 cm from the left side"],
  ["Human artists painted the missing parts of The Night Watch.", False, "정답 ▶ F\n이유: 인간 화가를 고용하는 대신(Instead of hiring human artists) AI가 재구성했어요.", '❺', "Instead of hiring human artists"],
  ["The AI program was shown a copy of the painting before it was cut.", True, "정답 ▶ T\n이유: it was shown a copy of the original painting before it was trimmed", '❺', "it was shown a copy of the original painting before it was trimmed"],
  ["The recreated pieces were placed around the painting.", True, "정답 ▶ T\n이유: which were hung around the painting · place = hang", '❺', "which were hung around the painting"],
 ],
 ilchi=[
  {'n': '❹', 'box': ['❹', '❺'], 'q': "글의 내용과 일치하지 <u>않는</u> 것은?",
   'opts': ["Experts were unable to repair the damage caused by the attacks.", "The painting was cut to fit on a wall in Amsterdam's town hall.", "AI was used to recreate the missing parts.", "The AI learned Rembrandt's style before rebuilding the missing pieces.", "Today, people can see the painting in its complete form."],
   'ex': "정답 ▶ Experts were unable to repair the damage caused by the attacks.\n이유: 그럴 때마다 전문가들이 기적적으로 원래 상태로 복원했어요(miraculously restored).\n오답 ▶ cut = trimmed · rebuild = reconstruct · in its complete form = complete again",
   'per': [["전문가들은 공격으로 인한 훼손을 고칠 수 없었다.", "experts miraculously restored the painting to its original state", "불일치 → 매번 복원함"],
           ["그림은 암스테르담 시청 벽에 맞추기 위해 잘렸다.", "trimmed on all four sides to fit on a wall in Amsterdam's town hall", "일치"],
           ["사라진 부분을 되살리는 데 AI가 사용되었다.", "It was artificial intelligence (AI) that the museum used to recreate the missing pieces", "일치"],
           ["AI는 사라진 조각을 재구성하기 전에 렘브란트의 화풍을 배웠다.", "an AI program was trained to learn Rembrandt's painting style", "일치"],
           ["오늘날 사람들은 그림을 완전한 형태로 볼 수 있다.", "The Night Watch is complete again", "일치"]]},
 ],
 pickg=[
  ("Rembrandt's The Night Watch, a huge painting that measures 3.795 meters by 4.535 meters, {has had|have had} a troubled history.", "정답 ▶ has had\n이유: 주어는 The Night Watch(단수, 동격 a huge painting ~은 삽입) → has had (현재완료)"),
  ("It was damaged with a knife twice and {sprayed|spraying} with acid by people who wanted to destroy it.", "정답 ▶ sprayed\n이유: was damaged ~ and (was) sprayed → 수동태 병렬"),
  ("But did you know that this painting was {much|very} larger over three centuries ago?", "정답 ▶ much\n이유: 비교급(larger) 강조 → much (very는 비교급을 강조하지 못해요)"),
  ("Since then, 60 cm from the left side, 22 cm from the top, 12 cm from the bottom, and 7 cm from the right side {have been|has been} missing.", "정답 ▶ have been\n이유: 주어가 네 개의 길이(A, B, C, and D) → 복수 → have been"),
  ("It was artificial intelligence (AI) {that|what} the museum used to recreate the missing pieces.", "정답 ▶ that\n이유: It was ~ that 강조 구문 (강조 대상: artificial intelligence)"),
  ("Instead of {hiring|hire} human artists, an AI program was trained to learn Rembrandt's painting style.", "정답 ▶ hiring\n이유: 전치사 of + 동명사"),
  ("Once the AI program learned to paint like Rembrandt, it {was shown|showed} a copy of the original painting before it was trimmed.", "정답 ▶ was shown\n이유: AI가 복사본을 '보여 받은' 수동 (show + 사람 + 사물 → 사람이 주어인 수동태)"),
  ("Then it reconstructed the missing pieces, {which|that} were hung around the painting.", "정답 ▶ which\n이유: 콤마 뒤 계속적 용법 → which"),
 ],
 verb=[
  ("It was ___ with a knife twice and sprayed with acid by people who wanted to destroy it.", 'damage', ['damaged'], "정답 ▶ damaged\n이유: 그림이 '훼손된' 수동 → was damaged"),
  ("In 1715, this monumental painting was trimmed on all four sides ___ on a wall.", 'fit', ['to fit'], "정답 ▶ to fit\n이유: 목적(~하도록) → to부정사"),
  ("However, art lovers can now see The Night Watch as Rembrandt originally ___.", 'intend', ['intended'], "정답 ▶ intended\n이유: 렘브란트가 (과거에) 의도한 대로 → intended"),
  ("An AI program was trained ___ Rembrandt's painting style.", 'learn', ['to learn'], "정답 ▶ to learn\n이유: be trained + to부정사 = ~하도록 훈련받다"),
  ("Then it reconstructed the missing pieces, which were ___ around the painting.", 'hang', ['hung'], "정답 ▶ hung\n이유: (물건을) 걸다 hang - hung - hung, 수동태 were hung"),
  ("Thanks to science, this great masterpiece has been ___ back to life for all to see.", 'bring', ['brought'], "정답 ▶ brought\n이유: 현재완료 수동태 has been + p.p. (bring - brought - brought)"),
 ],
 error=[
  ("Rembrandt's The Night Watch, a huge painting that [[measures]] 3.795 meters by 4.535 meters, [[have had]] a [[troubled]] history.", 1, 'has had', "정답 ▶ have had → has had\n이유: 주어 The Night Watch(단수)"),
  ("But did you know that this painting was [[very]] larger over three centuries ago? In 1715, this [[monumental]] painting [[was trimmed]] on all four sides [[to fit]] on a wall.", 0, 'much', "정답 ▶ very → much\n이유: 비교급 강조는 much, even, far, still, a lot"),
  ("Instead of [[hiring]] human artists, an AI program [[trained]] [[to learn]] Rembrandt's painting [[style]].", 1, 'was trained', "정답 ▶ trained → was trained\n이유: AI 프로그램이 '훈련받은' 수동"),
  ("Then it [[reconstructed]] the missing pieces, [[that]] were [[hung]] [[around]] the painting.", 1, 'which', "정답 ▶ that → which\n이유: 콤마 뒤 계속적 용법"),
 ],
 scr=[(e(S4, 2), S4[2][1]), (e(S5, 0), S5[0][1]), (e(S5, 5), S5[5][1])],
 order=[
  ([e(S4, 1), e(S4, 2), e(S4, 3), e(S4, 4)], ["칼과 산성 물질로 훼손", "매번 전문가가 복원", "300여 년 전엔 훨씬 컸다", "1715년 벽에 맞추려고 잘림"]),
  ([e(S5, 2), e(S5, 3), e(S5, 4), e(S5, 5)], ["AI가 렘브란트 화풍 학습", "원본 복사본을 보여 줌", "사라진 조각 재구성 · 둘레에 걸림", "300여 년 만에 다시 완성"]),
 ],
 insert=[
  ([e(S4, 1), e(S4, 2), e(S4, 3)], 1, ["두 번 칼로 훼손, 산성 물질", "그럴 때마다(Each time) 복원", "그런데 원래 훨씬 컸다"], "정답 ▶ Each time 문장은 훼손 이야기 바로 뒤\n이유: Each time = 훼손될 때마다"),
  ([e(S5, 0), e(S5, 1), e(S5, 2)], 1, ["이제 원래 의도대로 감상 가능", "되살리는 데 쓴 것은 AI", "인간 화가 대신 AI 훈련"], "정답 ▶ 'AI를 사용했다'는 문장이 먼저 와야 '인간 대신 AI 프로그램을 훈련'이 이어져요."),
 ],
 odd=[
  ([e(S4, 3), e(S4, 4), "Amsterdam is well known for its canals and bicycles.", e(S4, 5)], 2, "정답 ▶ 운하·자전거 문장\n이유: 그림이 잘린 이야기와 관계없어요."),
  ([e(S5, 2), e(S5, 3), "Some people worry that AI will replace many jobs in the future.", e(S5, 4)], 2, "정답 ▶ AI 일자리 걱정 문장\n이유: AI로 그림을 복원하는 과정과 관계없어요."),
 ],
 blank=[
  ("In 1715, this monumental painting was trimmed on all four sides ____.", ["to fit on a wall in Amsterdam's town hall", "to make it easier to sell", "to remove the damaged parts", "to hide Rembrandt's signature"], "정답 ▶ to fit on a wall in Amsterdam's town hall\n이유: 시청 벽에 맞추려고 잘랐어요."),
  ("It was ____ that the museum used to recreate the missing pieces.", ["artificial intelligence (AI)", "an old photograph", "a team of human artists", "a famous X-ray machine"], "정답 ▶ artificial intelligence (AI)\n이유: 인간 화가 대신 AI 프로그램을 훈련시켰어요."),
  ("Thanks to science, this great masterpiece ____ for all to see.", ["has been brought back to life", "has been trimmed again", "has been sold to a museum", "has been hidden in a town hall"], "정답 ▶ has been brought back to life\n이유: 300여 년 만에 다시 완성 → 되살아났다"),
 ],
 gram=[
  (B + "This painting was ______ larger three centuries ago.</b>", ['much', 'very', 'many', 'more'], "정답 ▶ much\n이유: 비교급 강조 much"),
  (B + "It was AI ______ the museum used to recreate the pieces.</b>", ['that', 'what', 'who', 'where'], "정답 ▶ that\n이유: It was ~ that 강조 구문"),
  (B + "Rembrandt's The Night Watch, a huge painting, ______ a troubled history.</b>", ['has had', 'have had', 'having', 'to have'], "정답 ▶ has had\n이유: 동격 삽입구를 빼면 주어는 The Night Watch(단수)"),
  ("밑줄 친 <u>it</u>이 가리키는 것은?<br><b>Once the AI program learned to paint like Rembrandt, <u>it</u> was shown a copy of the original painting.</b>", ['the AI program', 'the original painting', 'the copy', 'the museum'], "정답 ▶ the AI program\n이유: 복사본을 '보여 받은' 대상 → AI 프로그램"),
  (B + "Instead of ______ human artists, they used AI.</b>", ['hiring', 'hire', 'to hire', 'hired'], "정답 ▶ hiring\n이유: 전치사(of) + 동명사"),
 ],
 summ=[
  (None, ['❹'], "The Night Watch was not only (A) ______ by attackers but also (B) ______ on all four sides to fit on a wall.",
   ['(A) damaged – (B) trimmed', '(A) damaged – (B) enlarged', '(A) restored – (B) trimmed', '(A) painted – (B) framed', '(A) sold – (B) enlarged'],
   "정답 ▶ (A) damaged – (B) trimmed\n(A) 칼과 산성 물질로 '훼손되었다' → damaged\n(B) 벽에 맞추려고 네 면이 '잘렸다' → trimmed",
   ["It was damaged with a knife twice", "trimmed on all four sides to fit on a wall"]),
  (None, ['❺'], "Instead of hiring human artists, the museum used (A) ______ to recreate the missing pieces, making the painting (B) ______ again.",
   ['(A) AI – (B) complete', '(A) AI – (B) smaller', '(A) X-rays – (B) complete', '(A) photographs – (B) darker', '(A) robots – (B) famous'],
   "정답 ▶ (A) AI – (B) complete\n(A) 인공 지능(AI)을 사용했다 → AI\n(B) 300여 년 만에 다시 '완성'되었다 → complete",
   ["It was artificial intelligence (AI) that the museum used to recreate the missing pieces", "The Night Watch is complete again"]),
 ])

# ═════════════ DAY 8 · Link to Art History ═════════════
d8 = steps(
 vocab=[[w, m, 'L'] for w, m in [('masterpiece', '걸작'), ('wrongly', '잘못'), ('name', '이름을 붙이다'), ('widely known as', '~로 널리 알려진'), ('have nothing to do with', '~와 아무 관련이 없다'),
        ('in fact', '사실'), ('daytime', '낮'), ('event', '사건, 행사'), ('the late 18th century', '18세기 후반'), ('dust', '먼지'), ('varnish', '광택제, 니스'),
        ('gather', '모이다, 쌓이다'), ('mistakenly', '잘못하여, 실수로'), ('scene', '장면, 풍경'), ('remove', '제거하다'), ('remain', '남다, 계속 ~이다')]],
 pickv=[
  ("Rembrandt's painting, widely known as The Night Watch (1642), actually has {nothing|everything} to do with night.", "정답 ▶ nothing\n이유: 다음 문장 In fact, 낮의 사건 → 밤과 '아무 관련이 없다' (have nothing to do with)"),
  ("In fact, it was a painting of a {daytime|nighttime} event.", "정답 ▶ daytime (낮)\n이유: 이름과 달리 실제로는 '낮'의 사건"),
  ("People began to call it The Night Watch because dust and varnish gathered on the painting and made it look {darker|brighter}.", "정답 ▶ darker\n이유: 먼지와 광택제가 쌓여 '더 어두워' 보여서 밤 풍경으로 착각"),
  ("People began to {mistakenly|correctly} believe that the painting was a night scene.", "정답 ▶ mistakenly (잘못)\n이유: 원래 낮의 장면인데 밤이라고 '잘못' 믿었어요."),
  ("The varnish was removed during the 1940s, but the name {remained|changed}.", "정답 ▶ remained (그대로 남았다)\n이유: but → 광택제는 제거됐지만 이름은 '그대로'"),
 ],
 tf=[
  ["The Night Watch actually shows an event that happened at night.", False, "정답 ▶ F\n이유: 실제로는 낮의 사건(a daytime event)을 그린 그림이에요.", 'L', "it was a painting of a daytime event"],
  ["The painting got its famous name in the late 18th century.", True, "정답 ▶ T\n이유: In the late 18th century, people began to call it The Night Watch", 'L', "In the late 18th century, however, people began to call it The Night Watch"],
  ["Dust and varnish made the painting look darker than it really was.", True, "정답 ▶ T\n이유: dust and varnish gathered on the painting and made it look darker", 'L', "made it look darker"],
  ["After the varnish was removed, the painting was given a new name.", False, "정답 ▶ F\n이유: 광택제는 제거됐지만 이름은 그대로 남았어요(the name remained).", 'L', "the name remained"],
 ],
 ilchi=[
  {'n': 'L', 'box': ['Link to Art History'], 'q': "글의 내용과 일치하지 <u>않는</u> 것은?",
   'opts': ["Rembrandt himself named the painting The Night Watch in 1642.", "The painting was completed in 1642.", "People misunderstood the painting as a night scene.", "The varnish was taken off in the 1940s.", "The painting is still called The Night Watch today."],
   'ex': "정답 ▶ Rembrandt himself named the painting The Night Watch in 1642.\n이유: 사람들이 18세기 후반에야 그렇게 부르기 시작했어요(people began to call it ~).\n오답 ▶ misunderstand = mistakenly believe · take off = remove · still called = the name remained",
   'per': [["렘브란트가 직접 1642년에 그림을 '야경'이라고 이름 붙였다.", "In the late 18th century, however, people began to call it The Night Watch", "불일치 → 18세기 후반 사람들이 부름"],
           ["그 그림은 1642년에 완성되었다.", "widely known as The Night Watch (1642)", "일치"],
           ["사람들은 그 그림을 밤 풍경으로 오해했다.", "People began to mistakenly believe that the painting was a night scene", "일치"],
           ["광택제는 1940년대에 제거되었다.", "The varnish was removed during the 1940s", "일치"],
           ["그 그림은 오늘날에도 여전히 '야경'이라 불린다.", "the name remained", "일치"]]},
 ],
 pickg=[
  ("Rembrandt's painting, widely {known|knowing} as The Night Watch (1642), actually has nothing to do with night.", "정답 ▶ known\n이유: 그림이 '알려진' 수동 → 과거분사 known (widely known as ~)"),
  ("In the late 18th century, however, people began {to call|calling to} it The Night Watch.", "정답 ▶ to call\n이유: begin + to부정사(또는 -ing). calling to는 틀린 형태예요."),
  ("Dust and varnish gathered on the painting and made it {look|to look} darker.", "정답 ▶ look\n이유: 사역동사 make + O + 동사원형"),
  ("Dust and varnish gathered on the painting and made it look {darker|more darkly}.", "정답 ▶ darker\n이유: look + 형용사(보어) → darker (비교급 형용사)"),
  ("The varnish {was removed|removed} during the 1940s, but the name remained.", "정답 ▶ was removed\n이유: 광택제가 '제거된' 수동"),
 ],
 verb=[
  ("Rembrandt's painting, widely ___ as The Night Watch (1642), actually has nothing to do with night.", 'know', ['known'], "정답 ▶ known\n이유: 과거분사(수동) widely known as ~"),
  ("Dust and varnish ___ on the painting and made it look darker.", 'gather', ['gathered'], "정답 ▶ gathered\n이유: 과거의 일 (made와 병렬)"),
  ("The varnish was removed during the 1940s, but the name ___.", 'remain', ['remained'], "정답 ▶ remained\n이유: 과거 (remain은 자동사)"),
 ],
 error=[
  ("Rembrandt's painting, widely [[knowing]] as The Night Watch (1642), actually [[has]] nothing [[to do]] with night. In fact, it [[was]] a painting of a daytime event.", 0, 'known', "정답 ▶ knowing → known\n이유: 그림이 '알려진' 수동 → 과거분사"),
  ("People began to call it The Night Watch because dust and varnish [[gathered]] on the painting and [[made]] it [[to look]] [[darker]].", 2, 'look', "정답 ▶ to look → look\n이유: make + O + 동사원형"),
 ],
 scr=[(e(S6, 1), S6[1][1]), (e(S6, 4), S6[4][1])],
 order=[([e(S6, 0), e(S6, 1), e(S6, 2), e(S6, 3), e(S6, 4)], ["'야경'은 밤과 관련 없음", "사실 낮의 사건", "18세기 후반 먼지·광택제로 어두워져 '야경'이라 부름", "밤 풍경이라고 잘못 믿음", "광택제는 제거됐지만 이름은 남음"])],
 insert=[], odd=[],
 blank=[
  ("Rembrandt's painting, widely known as The Night Watch (1642), actually ____.", ["has nothing to do with night", "was painted at midnight", "shows a famous night festival", "was named by Rembrandt himself"], "정답 ▶ has nothing to do with night\n이유: 다음 문장 → 실제로는 낮의 사건"),
  ("The varnish was removed during the 1940s, but ____.", ["the name remained", "the painting was trimmed", "the dust came back", "the name was changed"], "정답 ▶ the name remained\n이유: but → 광택제는 없어졌지만 이름은 그대로"),
 ],
 gram=[
  (B + "The painting, widely ______ as The Night Watch, is famous.</b>", ['known', 'knowing', 'knew', 'to know'], "정답 ▶ known\n이유: 명사를 꾸미는 과거분사(수동)"),
  (B + "Dust made the painting ______ darker.</b>", ['look', 'to look', 'looking', 'looked'], "정답 ▶ look\n이유: make + O + 동사원형"),
  ("밑줄 친 부분과 뜻이 같은 것은?<br><b>The painting actually <u>has nothing to do with</u> night.</b>", ['is not related to', 'is closely connected to', 'is painted at', 'is named after'], "정답 ▶ is not related to\n이유: have nothing to do with ~ = ~와 아무 관련이 없다"),
 ],
 summ=[
  (None, ['Link to Art History'], "Although The Night Watch actually shows a (A) ______ event, it got its name because dust and varnish made it look (B) ______.",
   ['(A) daytime – (B) darker', '(A) nighttime – (B) darker', '(A) daytime – (B) brighter', '(A) nighttime – (B) older', '(A) royal – (B) smaller'],
   "정답 ▶ (A) daytime – (B) darker\n(A) 실제로는 '낮'의 사건 → daytime\n(B) 먼지와 광택제로 '더 어두워' 보였다 → darker",
   ["it was a painting of a daytime event", "made it look darker"]),
  (None, ['Link to Art History'], "People (A) ______ believed that the painting was a night scene, and even after the varnish was removed, the name (B) ______.",
   ['(A) mistakenly – (B) remained', '(A) correctly – (B) remained', '(A) mistakenly – (B) changed', '(A) rarely – (B) disappeared', '(A) correctly – (B) changed'],
   "정답 ▶ (A) mistakenly – (B) remained\n(A) 밤 풍경이라고 '잘못' 믿었다 → mistakenly\n(B) 광택제를 없앤 뒤에도 이름은 '그대로 남았다' → remained",
   ["People began to mistakenly believe that the painting was a night scene", "the name remained"]),
 ])

T4 = ("Rediscovering Art Through Science", "과학을 통한 예술의 재발견")
NEW = [
 {'id': 'e1', 'name': 'DAY', 'range': '4과 본문 ❶❷', 'story': '눈에 보이는 것 너머 · 다빈치 초상화의 담비', 'passage': P('❶', S1, T4) + P('❷', S2, ("Art Is Never Finished", "예술은 결코 완성되지 않는다")), 'steps': d5},
 {'id': 'e2', 'name': 'DAY', 'range': '4과 본문 ❸', 'story': '반 고흐의 숨겨진 자화상', 'passage': P('❸', S3, ("A Hidden Painting Revealed", "드러난 숨겨진 그림")), 'steps': d6},
 {'id': 'e3', 'name': 'DAY', 'range': '4과 본문 ❹❺', 'story': '렘브란트 「야경」과 AI 복원', 'passage': P('❹', S4, ("The Masterpiece as a Whole", "온전한 모습의 걸작")) + P('❺', S5), 'steps': d7},
 {'id': 'e4', 'name': 'DAY', 'range': '4과 Link to Art History', 'story': '이름이 잘못 지어진 걸작 (A Masterpiece Wrongly Named)', 'passage': P('Link to Art History', S6, ("A Masterpiece Wrongly Named", "이름이 잘못 지어진 걸작")), 'steps': d8},
]
path = '/home/claude/proj/data/h1-donga-lee-L3.js'
PK = json.loads(subprocess.check_output(['node', '-e', "global.window={};require('%s');process.stdout.write(JSON.stringify(window.PKG))" % path]))
old = [d for d in PK['days'] if d['id'] in ('d1', 'd2', 'd3', 'd4')]
assert len(old) == 4
days = old + NEW
for i, d in enumerate(days): d['name'] = 'DAY %d' % (i + 1)
for d in NEW: ansfirst(d['steps'])
PK['days'] = days
PK['unit'] = '공통영어2 Lesson 3~4'
PK['title'] = 'Social Media Algorithms · Rediscovering Art Through Science'
PK['pick'] = True
src = open(path).read(); head = src[:src.index('window.PKG')]
if '4과' not in head: head = head.rstrip('\n') + '\n/* 10/30: 4과 본문 ❶~❺ + Link to Art History (scratchpad/gen_h1dong4.py) DAY 5~8 추가 · pick */\n'
write(PK, path, head)
print('ok', [(d['id'], d['name'], d['range'], len(d['steps'])) for d in days])
