# 11/15 중2 동아(윤정미) 6과 대화문 (The Greatest Love for All) → m2-donga-yoon-L7.js 맨 앞 k6a·k6b
# 원문·해석: 선생님 hwp(2022 개정 2026 중2 동아 6과 01 대화문). 8과는 대화문 없음.
# 7과 대화문(k7a/k7b) 12단계 + 외우기 단계(추천한 것/누가 한 말, 표현 직접 쓰기, 대화 전체 순서)
import sys, json, re, subprocess
sys.path.insert(0, '/home/claude/srcrepo/generators')
sys.path.insert(0, '/tmp/claude-0/-home-claude/a9e3e882-1f02-5d62-8f70-aced81bc59d2/scratchpad')
from gencommon import write

def H(t): return ['#', t, '']

D1 = [H('6과 대화 1 · 공상 과학 소설 추천 (Watch and Check)'),
 ['B', 'What kinds of books do you usually read?', '너는 주로 어떤 종류의 책을 읽니?'],
 ['G', 'I usually read sci-fi novels.', '나는 보통 공상 과학 소설을 읽어.'],
 ['B', 'Then, can you recommend a good sci-fi novel for me?', '그럼, 좋은 공상 과학 소설 하나 추천해 줄래?'],
 ['G', "How about The Time Machine? I think it's the best.", '‘The Time Machine’은 어때? 나는 그것이 최고라고 생각해.']]
D2 = [H('6과 대화 2 · 새 탄산음료 추천 (Watch and Check)'),
 ['G', 'What kinds of soft drinks do you usually have?', '너는 주로 어떤 종류의 탄산음료를 마시니?'],
 ['B', 'I usually drink apple soda, but today, I want to try something else. Can you recommend some new soft drinks?', '나는 보통 사과 소다를 마시는데, 오늘은 다른 것을 마셔 보고 싶어. 새로운 탄산음료를 추천해 줄래?'],
 ['G', 'Try a cherry soda. The cherry soda here is good.', '체리 소다를 마셔 봐. 여기 체리 소다가 맛있어.'],
 ['B', "OK. I'll give it a try, then.", '알았어. 그럼, 한번 마셔 볼게.']]
D3 = [H('6과 대화 3 · 액션 영화 추천 (Watch and Check)'),
 ['B', 'What kinds of movies do you like?', '너는 어떤 종류의 영화를 좋아하니?'],
 ['G', 'I like action movies. Spider-Man is my favorite.', '나는 액션 영화를 좋아해. ‘스파이더맨’이 가장 좋아하는 영화야.'],
 ['B', "Oh, I didn't see it.", '오, 나는 그거 안 봤어.'],
 ['G', "You didn't? It's really fun. I strongly recommend it.", '안 봤다고? 정말 재미있어. 강력히 추천해.']]
D4 = [H('6과 대화 4 · 과학 잡지 추천 (Watch and Check)'),
 ['B', 'What kinds of magazines do you have?', '어떤 종류의 잡지가 있니?'],
 ['G', 'We have all kinds of magazines.', '모든 종류의 잡지가 있어.'],
 ['B', "I'm really interested in science. Can you recommend a science magazine for me?", '나는 과학에 정말 관심이 있어. 과학 잡지 하나 추천해 줄래?'],
 ['G', "Sure. You'll love this one, Teen's Science.", '그럼. ‘Teen’s Science’가 아주 마음에 들 거야.']]
D5 = [H('6과 대화 5 · 소미의 에세이 (Watch, Answer, and Role-play)'),
 ['G', 'Liam, can you please help me? I need to find some books for my homework.', 'Liam, 나 좀 도와줄래? 숙제를 위해 책을 몇 권 찾아야 해.'],
 ['B', 'What kinds of books are you looking for, Somi?', '어떤 종류의 책을 찾고 있니, 소미야?'],
 ['G', "I'm looking for books on famous people who helped others. I need to write an essay.", '다른 사람들을 도운 유명인들에 관한 책을 찾고 있어. 에세이를 써야 하거든.'],
 ['B', 'Who do you want to write about?', '너는 누구에 대해 쓰고 싶니?'],
 ['G', 'I was thinking about Dr. Schweitzer, but can you recommend someone else for me?', 'Schweitzer 박사를 생각하고 있었는데, 다른 사람을 추천해 줄 수 있어?'],
 ['B', 'What about Audrey Hepburn?', 'Audrey Hepburn은 어때?'],
 ['G', 'I know she was a famous actor, but what did she do to help others?', '그녀가 유명한 배우였다는 건 알지만, 다른 사람들을 돕기 위해 무엇을 했는데?'],
 ['B', 'She did a lot of volunteer work, especially for children.', '그녀는 특히 아이들을 위해서 많은 자원봉사를 했어.'],
 ['G', 'Really? Then, I can write about her. Thank you!', '정말? 그럼 그녀에 대해 쓸 수 있겠다. 고마워!']]
D6 = [H('6과 Listen Up · 영화 소개 The Song of Love'),
 ['W', 'Hello, everyone.', '여러분, 안녕하세요.'],
 ['W', "The movie I'm going to introduce today is The Song of Love.", '제가 오늘 소개할 영화는 ‘The Song of Love’입니다.'],
 ['W', "It's a movie about a pianist who loses his love for music.", '이것은 음악에 대한 사랑을 잃어버린 한 피아니스트에 관한 영화입니다.'],
 ['W', 'He moves to a small town for a new start.', '그는 새출발을 위해 작은 마을로 이사합니다.'],
 ['W', 'There, he begins teaching music to children and finds his love for music again.', '그곳에서 그는 아이들에게 음악을 가르치기 시작하며 음악에 대한 사랑을 되찾게 됩니다.'],
 ['W', 'This movie has great music and a touching story, so I strongly recommend it.', '이 영화는 훌륭한 음악과 감동적인 이야기를 담고 있어 강력히 추천합니다.']]

def L(D): return [r[1] for r in D[1:]]
BOX_A = [d[0][1] for d in (D1, D2, D3, D4)]
BOX_B = [D5[0][1], D6[0][1]]

def ST(t, title, items, **kw):
    s = {'type': t, 'title': title}; s.update(kw); s['items'] = items; return s
G_PICKV = '문맥에 맞는 낱말을 고르세요.'; G_TF = '본문 내용과 일치하면 T, 다르면 F를 고르세요.'
G_RESP = '대화의 흐름에 맞는 응답을 고르세요.'; G_IL = '선택지는 본문을 다른 말로 바꿔 쓴 문장이에요. 풀고 나서 해설의 어휘를 꼭 확인하세요.'
G_GRAM = '어법상 알맞은 것을 고르세요.'; G_SCR = '우리말에 맞게 단어를 눌러 문장을 완성하세요.'
G_ORD = '대화(문장)를 순서대로 눌러서 배열하세요. 대화 전체 순서를 통째로 외워요!'; G_BL = '빈칸에 들어갈 말로 가장 알맞은 것을 고르세요.'
G_ODD = '짝지어진 대화 중 어색한 것을 고르세요.'; G_FN = '상황에 맞는 표현을 고르세요.'; G_SUM = '본문을 읽고 요약문의 빈칸 (A), (B)에 들어갈 말을 고르세요.'
G_WR = '대화 속 빈칸에 들어갈 말을 직접 쓰세요. 우리말 뜻과 첫 글자가 힌트예요. 철자까지 정확히!'

def W(line, word, ko, ex, alts=()):
    assert line.count(word) == 1, (line, word)
    return {'s': line.replace(word, '___'), 'v': ko + ' · ' + word[0] + '…', 'a': [word] + list(alts), 'ex': ex}

# ─────────── k6a 대화 1~4 ───────────
A_ = L(D1) + L(D2) + L(D3) + L(D4)
k6a = {'id': 'k6a', 'name': '', 'range': '6과 대화문 ① 대화 1~4',
 'story': 'Lesson 6 · 종류 묻고 답하기 (What kinds of ~?) · 추천 요청하고 답하기 (Can you recommend ~?)',
 'passage': D1 + D2 + D3 + D4,
 'steps': [
  ST('vocab', '핵심어휘·숙어', [
     ['What kinds of ~ do you like?', '어떤 종류의 ~을 좋아하니? (종류 묻기)'], ['I usually ~.', '나는 주로[보통] ~해. (종류 답하기)'],
     ['Can you recommend ~ for me?', '나에게 ~을 추천해 줄래? (추천 요청하기)'], ['How about ~?', '~은 어때? (추천하기)'],
     ['Try + 명사', '~을 먹어[마셔] 봐 (추천하기)'], ['I strongly recommend ~.', '나는 ~을 강력히 추천해. (추천하기)'],
     ["You'll love ~.", '너는 ~을 아주 좋아하게 될 거야. (추천하기)'], ['sci-fi novel', '공상 과학 소설'], ['recommend', '추천하다'],
     ['soft drink', '탄산음료'], ['try something else', '다른 것을 시도하다[마셔 보다]'], ['give it a try', '한번 해 보다, 시도해 보다'],
     ['action movie', '액션 영화'], ['favorite', '가장 좋아하는 것'], ['magazine', '잡지'], ['all kinds of ~', '모든 종류의 ~'],
     ['be interested in ~', '~에 관심이 있다'], ['I think (that) ~.', '나는 ~라고 생각해.']], quizN=12),
  ST('pick', '어휘선택', [
     {'s': 'I usually drink apple soda, but today, I want to try something {else|again}.', 'ex': "정답 ▶ else (그 밖의 다른)\n이유: 평소엔 사과 소다를 마시지만 오늘은 '다른 것'을 마셔 보고 싶다 → something else. 그래서 새 탄산음료를 추천해 달라고 해요.\n오답 ▶ again (다시): 평소 마시던 것을 다시 마시면 추천을 부탁할 이유가 없어요."},
     {'s': 'We have all {kinds|sizes} of magazines.', 'ex': "정답 ▶ kinds (종류)\n이유: What kinds of magazines do you have?(어떤 종류의 잡지가 있니?)에 대한 답 → 모든 '종류'의 잡지가 있다\n오답 ▶ sizes (크기): 질문이 종류를 물었어요."},
     {'s': "You didn't? It's really fun. I strongly {recommend|forget} it.", 'ex': "정답 ▶ recommend (추천하다)\n이유: 상대가 안 봤다고 하자 정말 재미있다며 '강력히 추천한다'\n오답 ▶ forget (잊다): 흐름과 맞지 않아요."},
     {'s': 'I usually read {sci-fi|history} novels.', 'ex': "정답 ▶ sci-fi (공상 과학의)\n이유: 바로 뒤에 소년이 a good sci-fi novel을 추천해 달라고 해요. 그래서 소녀가 공상 과학 소설 The Time Machine을 추천하죠.\n오답 ▶ history (역사): 대화 내용과 달라요."}], guide=G_PICKV),
  ST('tf', 'T/F 내용 확인', [
     ['In Dialog 1, the girl usually reads sci-fi novels.', True, '정답 ▶ T\n이유: I usually read sci-fi novels.라고 했어요.', None, 'I usually read sci-fi novels'],
     ['In Dialog 1, the girl thinks The Time Machine is the best.', True, "정답 ▶ T\n이유: How about The Time Machine? I think it's the best.", None, "I think it's the best"],
     ['In Dialog 2, the boy wants to drink apple soda again today.', False, '정답 ▶ F\n이유: 평소엔 사과 소다를 마시지만 오늘은 다른 것(something else)을 마셔 보고 싶어 해요.', None, 'I want to try something else'],
     ['In Dialog 2, the boy will try a cherry soda.', True, "정답 ▶ T\n이유: 소녀가 체리 소다를 추천하자 OK. I'll give it a try, then.이라고 했어요.", None, "I'll give it a try, then"],
     ['In Dialog 3, the boy has already seen Spider-Man.', False, "정답 ▶ F\n이유: Oh, I didn't see it.(나는 그거 안 봤어)라고 했어요.", None, "Oh, I didn't see it"],
     ['In Dialog 4, the boy is really interested in science.', True, "정답 ▶ T\n이유: I'm really interested in science.라고 했어요.", None, "I'm really interested in science"]], guide=G_TF),
  ST('mc', '무엇을 추천했을까?', [
     {'q': '대화 1에서 소녀가 추천한 것은?', 'opts': ['The Time Machine (공상 과학 소설)', 'Spider-Man (액션 영화)', "Teen's Science (과학 잡지)", 'a cherry soda (체리 소다)'], 'ex': '정답 ▶ The Time Machine\n이유: 공상 과학 소설을 추천해 달라는 말에 How about The Time Machine?이라고 했어요.\n외우기 ▶ 대화 1 책 → The Time Machine'},
     {'q': '대화 2에서 소녀가 추천한 것은?', 'opts': ['a cherry soda', 'an apple soda', 'The Time Machine', "Teen's Science"], 'ex': '정답 ▶ a cherry soda\n이유: Try a cherry soda. The cherry soda here is good.\n오답 ▶ an apple soda: 소년이 평소에 마시는 것이에요.\n외우기 ▶ 대화 2 탄산음료 → 체리 소다'},
     {'q': '대화 3에서 소녀가 강력히 추천한 것은?', 'opts': ['Spider-Man', 'The Time Machine', 'a cherry soda', 'The Song of Love'], 'ex': "정답 ▶ Spider-Man\n이유: Spider-Man is my favorite. ~ I strongly recommend it.\n외우기 ▶ 대화 3 영화 → 스파이더맨"},
     {'q': '대화 4에서 소녀가 추천한 것은?', 'opts': ["Teen's Science", 'Spider-Man', 'The Time Machine', 'a cherry soda'], 'ex': "정답 ▶ Teen's Science\n이유: 과학 잡지를 추천해 달라는 말에 You'll love this one, Teen's Science.라고 했어요.\n외우기 ▶ 대화 4 잡지 → Teen's Science"}], guide='대화마다 무엇을 추천했는지 떠올려 보세요.'),
  ST('mc', '알맞은 응답 고르기', [
     {'q': '다음 말에 이어질 응답으로 가장 알맞은 것은?<br><b>A: What kinds of books do you usually read?</b>', 'opts': ['I usually read sci-fi novels.', 'Yes, I read books.', "I'll give it a try, then.", 'You will love this one.'], 'ex': '정답 ▶ I usually read sci-fi novels.\n이유: What kinds of ~?(어떤 종류?)에는 구체적인 종류로 답해요.\n오답 ▶ Yes, I read books.는 Do you ~?에 대한 대답이에요.'},
     {'q': '다음 말에 이어질 응답으로 가장 알맞은 것은?<br><b>A: Can you recommend some new soft drinks?</b>', 'opts': ['Try a cherry soda.', 'I usually drink apple soda.', "No, I didn't see it.", 'We have all kinds of magazines.'], 'ex': '정답 ▶ Try a cherry soda.\n이유: 추천을 요청하는 말(Can you recommend ~?)에는 Try ~. / How about ~? / I recommend ~.로 답해요.'},
     {'q': '다음 말에 이어질 응답으로 가장 알맞은 것은?<br><b>A: Oh, I didn\'t see it.</b>', 'opts': ["You didn't? It's really fun. I strongly recommend it.", "Sure. You'll love this one.", 'I like action movies.', 'What kinds of movies do you like?'], 'ex': "정답 ▶ You didn't? It's really fun. I strongly recommend it.\n이유: 안 봤다는 말에 놀라며(You didn't?) 재미있다고 강력히 추천해요. (대화 3의 마지막 말)"}], guide=G_RESP),
  ST('mc', '일치·불일치', [
     {'box': BOX_A, 'q': '대화의 내용과 일치하지 <u>않는</u> 것은?',
      'opts': ['The boy in Dialog 2 decides to drink apple soda as usual.', 'The girl in Dialog 1 regards The Time Machine as the best sci-fi novel.', 'In Dialog 3, Spider-Man is the girl\'s favorite movie.', 'The girl in Dialog 4 offers a science magazine to the boy.', 'The boy in Dialog 4 is fascinated by science.'],
      'ex': "정답 ▶ The boy in Dialog 2 decides to drink apple soda as usual.\n이유: 소년은 평소(as usual)처럼 사과 소다를 마시는 게 아니라, 다른 것을 원해서 체리 소다를 마셔 보기로 해요.\n어휘 ▶ as usual 평소처럼 · regard A as B A를 B로 여기다 · offer 제공하다 · be fascinated by ~에 매료되다(= be really interested in)",
      'per': [['대화 2 소년은 평소처럼 사과 소다를 마시기로 한다.', "I want to try something else / I'll give it a try", '불일치 → 체리 소다를 마셔 봄'], ['대화 1 소녀는 The Time Machine을 최고로 여긴다.', "I think it's the best", '일치'],
              ['대화 3 스파이더맨은 소녀가 가장 좋아하는 영화', 'Spider-Man is my favorite', '일치'], ['대화 4 소녀는 소년에게 과학 잡지를 권한다.', "You'll love this one, Teen's Science", '일치'], ['대화 4 소년은 과학에 매료되어 있다.', "I'm really interested in science", '일치']]}], guide=G_IL),
  ST('pick', '어법선택', [
     {'s': 'What kinds of books {do|are} you usually read?', 'ex': '정답 ▶ do\n이유: 일반동사 read의 의문문 → do + 주어 + 동사원형. (usually = 습관)'},
     {'s': 'Then, can you recommend a good sci-fi novel {for|to} me?', 'ex': '정답 ▶ for\n이유: Can you recommend ~ for me? = 나에게(나를 위해) ~을 추천해 줄래?'},
     {'s': 'I usually drink apple soda, but today, I want {to try|trying} something else.', 'ex': '정답 ▶ to try\n이유: want + to부정사(~하고 싶다). want는 동명사를 목적어로 쓰지 않아요.'},
     {'s': "I'm really interested {in|on} science.", 'ex': '정답 ▶ in\n이유: be interested in ~ = ~에 관심이 있다'},
     {'s': 'We have all kinds of {magazines|magazine}.', 'ex': '정답 ▶ magazines\n이유: all kinds of + 복수명사 = 모든 종류의 ~'}], guide=G_GRAM),
  ST('scramble', '본문 스크램블', [
     {'ko': '그럼, 좋은 공상 과학 소설 하나 추천해 줄래?', 'en': 'Then, can you recommend a good sci-fi novel for me?'},
     {'ko': '너는 주로 어떤 종류의 탄산음료를 마시니?', 'en': 'What kinds of soft drinks do you usually have?'},
     {'ko': '알았어. 그럼, 한번 마셔 볼게.', 'en': "OK. I'll give it a try, then."},
     {'ko': '나는 과학에 정말 관심이 있어.', 'en': "I'm really interested in science."}], guide=G_SCR),
  ST('verb', '표현 직접 쓰기', [
     W('What kinds of books do you usually read?', 'kinds', '종류', '정답 ▶ kinds\n이유: What kinds of + 명사 ~? = 어떤 종류의 ~? (종류 묻기)'),
     W('Then, can you recommend a good sci-fi novel for me?', 'recommend', '추천하다', '정답 ▶ recommend\n이유: Can you recommend ~ for me? = ~을 추천해 줄래? (추천 요청)'),
     W("How about The Time Machine? I think it's the best.", 'How', '~은 어때?', '정답 ▶ How\n이유: How about ~? = ~은 어때? (추천하기)'),
     W("OK. I'll give it a try, then.", 'try', '시도', '정답 ▶ try\n이유: give it a try = 한번 해 보다'),
     W("You didn't? It's really fun. I strongly recommend it.", 'strongly', '강력히', '정답 ▶ strongly\n이유: I strongly recommend ~. = 나는 ~을 강력히 추천해.'),
     W("Sure. You'll love this one, Teen's Science.", 'love', '아주 좋아하다', "정답 ▶ love\n이유: You'll love ~. = 너는 ~이 아주 마음에 들 거야. (추천하기)")], guide=G_WR, ph='빈칸에 들어갈 말 쓰기'),
  ST('order', '문장순서', [
     {'lines': L(D1), 'flow': ['B: 어떤 종류의 책을 읽니?', 'G: 공상 과학 소설', 'B: 하나 추천해 줄래?', 'G: The Time Machine 어때?']},
     {'lines': L(D2), 'flow': ['G: 어떤 탄산음료를 마시니?', 'B: 보통 사과 소다, 오늘은 다른 것 추천해 줘', 'G: 체리 소다를 마셔 봐', 'B: 한번 마셔 볼게']},
     {'lines': L(D3), 'flow': ['B: 어떤 영화를 좋아해?', 'G: 액션 영화, 스파이더맨', 'B: 그거 안 봤어', 'G: 안 봤어? 강력 추천!']},
     {'lines': L(D4), 'flow': ['B: 어떤 잡지가 있어?', 'G: 모든 종류가 있어', 'B: 과학 잡지 추천해 줘', "G: Teen's Science가 마음에 들 거야"]}], guide=G_ORD),
  ST('blank', '빈칸추론', [
     {'s': 'I like action movies. Spider-Man is my ____.', 'opts': ['favorite', 'problem', 'homework', 'secret'], 'ex': "정답 ▶ favorite (가장 좋아하는 것)\n이유: 액션 영화를 좋아한다 → 스파이더맨이 '가장 좋아하는' 영화. 그래서 강력히 추천해요."},
     {'s': 'Try a cherry soda. The cherry soda here is ____.', 'opts': ['good', 'expensive', 'terrible', 'old'], 'ex': "정답 ▶ good (맛있는)\n이유: 체리 소다를 추천하는 이유 → 여기 체리 소다가 '맛있다'\n오답 ▶ terrible(형편없는): 추천하는 이유가 될 수 없어요."}], guide=G_BL),
  ST('mc', '어색한 대화 고르기', [
     {'q': '다음 중 짝지어진 대화가 <b>어색한</b> 것은?', 'opts': ['A: What kinds of movies do you like? B: Yes, I like movies.', 'A: Can you recommend a book for me? B: How about The Time Machine?', "A: Oh, I didn't see it. B: You didn't? I strongly recommend it.", "A: Can you recommend a science magazine? B: Sure. You'll love this one."],
      'ex': "정답 ▶ A: What kinds of movies do you like? B: Yes, I like movies.\n이유: What kinds of ~?(어떤 종류?)에는 Yes/No로 답할 수 없어요. → I like action movies.처럼 종류를 말해요."}], guide=G_ODD),
  ST('mc', '의사소통 기능', [
     {'q': '추천을 <b>요청하는</b> 표현이 <b>아닌</b> 것은?', 'opts': ['I strongly recommend it.', 'Can you recommend a good sci-fi novel for me?', 'Can you suggest some new soft drinks?', 'What do you recommend?'],
      'ex': '정답 ▶ I strongly recommend it.\n이유: 이것은 추천을 요청하는 말이 아니라, 추천하는(답하는) 말이에요.\n포인트 ▶ 추천 요청: Can you recommend ~? = Can you suggest ~? = What do you recommend? / 추천하기: How about ~? · Try ~. · I recommend ~. · You\'ll love ~.'},
     {'q': '밑줄 친 말의 의도로 알맞은 것은?<br><b>B: <u>What kinds of magazines do you have?</u></b>', 'opts': ['종류 묻기', '추천하기', '감사하기', '거절하기'], 'ex': '정답 ▶ 종류 묻기\n이유: What kinds of ~?는 구체적인 종류를 묻는 표현이에요. (어떤 종류의 잡지가 있니?)'}], guide=G_FN),
  ST('mc', '요약문 완성', [
     {'n': None, 'box': [D2[0][1]], 'q': '다음 글의 내용을 한 문장으로 요약할 때, 빈칸 (A), (B)에 들어갈 말로 가장 알맞은 것은?<br><b>The boy usually drinks (A) ______ soda, but today he decides to try a (B) ______ soda.</b>',
      'opts': ['(A) apple – (B) cherry', '(A) cherry – (B) apple', '(A) apple – (B) lemon', '(A) orange – (B) cherry', '(A) cherry – (B) cherry'],
      'ex': '정답 ▶ (A) apple – (B) cherry\n(A) I usually drink apple soda → 평소엔 사과\n(B) Try a cherry soda. → I\'ll give it a try → 오늘은 체리\n오답 ▶ (A)(B)를 바꾼 ②가 함정이에요.', 'ev': ['I usually drink apple soda', 'Try a cherry soda']},
     {'n': None, 'box': [D4[0][1]], 'q': '다음 글의 내용을 한 문장으로 요약할 때, 빈칸 (A), (B)에 들어갈 말로 가장 알맞은 것은?<br><b>The boy is interested in (A) ______, so the girl recommends a (B) ______ called Teen\'s Science.</b>',
      'opts': ['(A) science – (B) magazine', '(A) science – (B) novel', '(A) movies – (B) magazine', '(A) music – (B) book', '(A) sports – (B) magazine'],
      'ex': "정답 ▶ (A) science – (B) magazine\n(A) I'm really interested in science\n(B) Can you recommend a science magazine ~? → Teen's Science", 'ev': ["I'm really interested in science", "You'll love this one, Teen's Science"]}], guide=G_SUM),
 ]}

# ─────────── k6b 대화 5 · Listen Up ───────────
k6b = {'id': 'k6b', 'name': '', 'range': '6과 대화문 ② 대화 5·Listen Up',
 'story': 'Lesson 6 · 소미의 에세이(Audrey Hepburn) · 영화 소개 The Song of Love',
 'passage': D5 + D6,
 'steps': [
  ST('vocab', '핵심어휘·숙어', [
     ['Can you (please) help me?', '나 좀 도와줄래? (도움 요청)'], ['need to + 동사원형', '~해야 한다'], ['look for', '~을 찾다'],
     ['What kinds of ~ are you looking for?', '어떤 종류의 ~을 찾고 있니? (종류 묻기)'], ['books on ~', '~에 관한 책'], ['famous', '유명한'],
     ['help others', '다른 사람들을 돕다'], ['essay', '에세이, 글'], ['write about ~', '~에 대해 쓰다'], ['someone else', '다른 누군가'],
     ['What about ~?', '~은 어때? (추천하기) = How about ~?'], ['actor', '배우'], ['volunteer work', '자원봉사 (활동)'], ['especially', '특히'],
     ['introduce', '소개하다'], ['pianist', '피아니스트'], ['lose one\'s love for ~', '~에 대한 사랑을 잃다'], ['for a new start', '새 출발을 위해'],
     ['begin -ing', '~하기 시작하다'], ['touching', '감동적인'], ['strongly', '강력히']], quizN=12),
  ST('pick', '어휘선택', [
     {'s': 'I need to find some books for my {homework|vacation}.', 'ex': "정답 ▶ homework (숙제)\n이유: 바로 뒤에 I need to write an essay.(에세이를 써야 해) → 숙제를 위해 책을 찾음"},
     {'s': "I'm looking for books on famous people who {helped|hated} others.", 'ex': "정답 ▶ helped (도왔다)\n이유: 소미는 '다른 사람들을 도운' 유명인에 대해 써요. Audrey Hepburn도 자원봉사를 했죠.\n오답 ▶ hated (싫어했다): 흐름과 반대"},
     {'s': 'She did a lot of volunteer work, especially for {children|animals}.', 'ex': "정답 ▶ children (아이들)\n이유: Audrey Hepburn은 특히 '아이들'을 위해 자원봉사를 했어요. 소미의 메모에도 children에 표시해요."},
     {'s': 'This movie has great music and a {touching|boring} story, so I strongly recommend it.', 'ex': "정답 ▶ touching (감동적인)\n이유: so I strongly recommend it(그래서 강력히 추천한다) → 추천하는 이유는 '감동적인' 이야기\n오답 ▶ boring (지루한): 추천 이유가 될 수 없어요."},
     {'s': "It's a movie about a pianist who {loses|finds} his love for music.", 'ex': "정답 ▶ loses (잃다)\n이유: 처음엔 음악에 대한 사랑을 '잃고', 아이들을 가르치며 다시 찾아요(finds ~ again).\n오답 ▶ finds: 뒤의 finds his love for music again과 흐름이 맞지 않아요."}], guide=G_PICKV),
  ST('tf', 'T/F 내용 확인', [
     ['Somi needs books for her homework.', True, '정답 ▶ T\n이유: I need to find some books for my homework.', None, 'I need to find some books for my homework'],
     ['Somi first thought about writing about Audrey Hepburn.', False, '정답 ▶ F\n이유: 처음에는 Schweitzer 박사를 생각했고, Liam이 Audrey Hepburn을 추천했어요.', None, 'I was thinking about Dr. Schweitzer'],
     ['Somi already knew Audrey Hepburn was a famous actor.', True, '정답 ▶ T\n이유: I know she was a famous actor라고 했어요.', None, 'I know she was a famous actor'],
     ['Somi decides to write about Dr. Schweitzer.', False, '정답 ▶ F\n이유: Then, I can write about her.(her = Audrey Hepburn)라고 했어요.', None, 'Then, I can write about her'],
     ['In the movie, the pianist moves to a big city.', False, '정답 ▶ F\n이유: a small town(작은 마을)으로 이사해요.', None, 'He moves to a small town for a new start'],
     ['The pianist finds his love for music again by teaching children.', True, '정답 ▶ T\n이유: he begins teaching music to children and finds his love for music again', None, 'he begins teaching music to children and finds his love for music again']], guide=G_TF),
  ST('mc', '누가 한 말일까?', [
     {'q': '대화 5에서 다음 말을 한 사람은?<br><b>"What kinds of books are you looking for?"</b>', 'opts': ['Liam', 'Somi'], 'ex': '정답 ▶ Liam\n이유: 소미의 도움 요청에 Liam이 어떤 종류의 책을 찾는지 물어요. (What kinds of books are you looking for, Somi?)'},
     {'q': '대화 5에서 다음 말을 한 사람은?<br><b>"Can you recommend someone else for me?"</b>', 'opts': ['Somi', 'Liam'], 'ex': '정답 ▶ Somi\n이유: Schweitzer 박사를 생각하던 소미가 다른 사람을 추천해 달라고 해요.'},
     {'q': '대화 5에서 다음 말을 한 사람은?<br><b>"What about Audrey Hepburn?"</b>', 'opts': ['Liam', 'Somi'], 'ex': '정답 ▶ Liam\n이유: 추천을 요청받은 Liam이 Audrey Hepburn을 추천해요.'},
     {'q': '대화 5에서 다음 말을 한 사람은?<br><b>"She did a lot of volunteer work, especially for children."</b>', 'opts': ['Liam', 'Somi'], 'ex': "정답 ▶ Liam\n이유: 소미가 '그녀가 다른 사람들을 돕기 위해 무엇을 했는지' 묻자 Liam이 대답해요."},
     {'q': '소미가 도서관에 온 이유로 알맞은 것은?', 'opts': ['to look for books for her homework', 'to return some books', 'to research places to volunteer', 'to watch a movie about a pianist'], 'ex': '정답 ▶ to look for books for her homework (숙제를 위한 책을 찾으려고)\n이유: I need to find some books for my homework.\n오답 ▶ 책 반납 / 자원봉사 할 곳 조사 → 교과서 Watch, Answer 1번의 오답이에요.'}], guide='대화 속 인물과 상황을 떠올려 보세요.'),
  ST('mc', '알맞은 응답 고르기', [
     {'q': '다음 말에 이어질 응답으로 가장 알맞은 것은?<br><b>A: Who do you want to write about?</b>', 'opts': ['I was thinking about Dr. Schweitzer.', 'I need to write an essay.', 'Yes, I want to write.', 'She was a famous actor.'], 'ex': '정답 ▶ I was thinking about Dr. Schweitzer.\n이유: Who ~?(누구?)에는 사람으로 답해요. 대화 5에서 소미의 대답이에요.'},
     {'q': '다음 말에 이어질 응답으로 가장 알맞은 것은?<br><b>A: I know she was a famous actor, but what did she do to help others?</b>', 'opts': ['She did a lot of volunteer work, especially for children.', 'What about Audrey Hepburn?', 'I can write about her.', 'She moves to a small town.'], 'ex': '정답 ▶ She did a lot of volunteer work, especially for children.\n이유: 다른 사람을 돕기 위해 무엇을 했는지 → 아이들을 위한 자원봉사'},
     {'q': '다음 말에 이어질 응답으로 가장 알맞은 것은?<br><b>A: Liam, can you please help me?</b>', 'opts': ['Sure. What do you need?', 'Yes, I helped others.', 'No, I am not a pianist.', 'What about you?'], 'ex': "정답 ▶ Sure. What do you need?\n이유: 도움을 요청하는 말에는 Sure.(그럼) 등으로 수락하고 무엇이 필요한지 물어요.\n오답 ▶ Yes, I helped others.는 과거 경험을 말하는 것이라 어색해요."}], guide=G_RESP),
  ST('mc', '일치·불일치', [
     {'box': BOX_B, 'q': '대화와 담화의 내용과 일치하지 <u>않는</u> 것은?',
      'opts': ['Liam suggests that Somi write about Dr. Schweitzer.', 'Somi has to write an essay about famous people who helped others.', 'Audrey Hepburn did volunteer work mainly for children.', 'The pianist relocates to a small town to make a fresh start.', 'The speaker highly recommends The Song of Love.'],
      'ex': "정답 ▶ Liam suggests that Somi write about Dr. Schweitzer.\n이유: Schweitzer 박사는 소미가 처음 생각한 사람이고, Liam이 추천한 사람은 Audrey Hepburn이에요.\n어휘 ▶ suggest 제안하다 · mainly 주로(= especially) · relocate 이전하다(= move) · a fresh start 새 출발(= a new start) · highly 매우(= strongly)",
      'per': [['Liam이 Schweitzer 박사에 대해 쓰라고 제안', 'What about Audrey Hepburn?', '불일치 → Audrey Hepburn 추천'], ['소미는 남을 도운 유명인에 대한 에세이를 써야 함', "I'm looking for books on famous people who helped others", '일치'],
              ['Audrey Hepburn은 주로 아이들을 위해 봉사', 'especially for children', '일치'], ['피아니스트는 새 출발을 위해 작은 마을로 이사', 'He moves to a small town for a new start', '일치'], ['화자는 영화를 강력히 추천', 'I strongly recommend it', '일치']]}], guide=G_IL),
  ST('pick', '어법선택', [
     {'s': 'I need {to find|finding} some books for my homework.', 'ex': '정답 ▶ to find\n이유: need + to부정사 = ~해야 한다, ~할 필요가 있다'},
     {'s': 'What kinds of books are you {looking|look} for, Somi?', 'ex': '정답 ▶ looking\n이유: are you + -ing ~? = 현재진행형 의문문(지금 ~하고 있니?)'},
     {'s': "I'm looking for books on famous people {who|which} helped others.", 'ex': '정답 ▶ who\n이유: 선행사 famous people(사람) → 주격 관계대명사 who'},
     {'s': 'I know she was a famous actor, but what did she do {to help|helping} others?', 'ex': '정답 ▶ to help\n이유: ~하기 위해(목적) → to부정사'},
     {'s': "It's a movie about a pianist who {loses|lose} his love for music.", 'ex': '정답 ▶ loses\n이유: 주격 관계대명사절의 동사는 선행사 a pianist(단수)에 맞춰요 → loses'},
     {'s': 'There, he begins teaching music to children and {finds|finding} his love for music again.', 'ex': '정답 ▶ finds\n이유: 주어 he에 이어지는 동사 begins와 and로 병렬 → finds'}], guide=G_GRAM),
  ST('scramble', '본문 스크램블', [
     {'ko': '다른 사람들을 도운 유명인들에 관한 책을 찾고 있어.', 'en': "I'm looking for books on famous people who helped others."},
     {'ko': '다른 사람을 추천해 줄 수 있어?', 'en': 'can you recommend someone else for me?'},
     {'ko': '그녀는 특히 아이들을 위해서 많은 자원봉사를 했어.', 'en': 'She did a lot of volunteer work, especially for children.'},
     {'ko': '제가 오늘 소개할 영화는 ‘The Song of Love’입니다.', 'en': "The movie I'm going to introduce today is The Song of Love."}], guide=G_SCR),
  ST('verb', '표현 직접 쓰기', [
     W('Liam, can you please help me? I need to find some books for my homework.', 'help', '돕다', '정답 ▶ help\n이유: can you please help me? = 나 좀 도와줄래? (도움 요청)'),
     W('What kinds of books are you looking for, Somi?', 'looking', '찾고 있는', '정답 ▶ looking\n이유: look for = ~을 찾다 → are you looking for ~? (현재진행)'),
     W('I was thinking about Dr. Schweitzer, but can you recommend someone else for me?', 'else', '다른', '정답 ▶ else\n이유: someone else = 다른 누군가'),
     W('What about Audrey Hepburn?', 'about', '~은 어때?', '정답 ▶ about\n이유: What about ~? = ~은 어때? (= How about ~?) (추천하기)'),
     W('She did a lot of volunteer work, especially for children.', 'volunteer', '자원봉사', '정답 ▶ volunteer\n이유: volunteer work = 자원봉사 (활동)'),
     W('She did a lot of volunteer work, especially for children.', 'especially', '특히', '정답 ▶ especially\n이유: especially for children = 특히 아이들을 위해'),
     W("The movie I'm going to introduce today is The Song of Love.", 'introduce', '소개하다', '정답 ▶ introduce\n이유: The movie (that) I\'m going to introduce today = 내가 오늘 소개할 영화'),
     W('This movie has great music and a touching story, so I strongly recommend it.', 'touching', '감동적인', '정답 ▶ touching\n이유: a touching story = 감동적인 이야기')], guide=G_WR, ph='빈칸에 들어갈 말 쓰기'),
  ST('order', '문장순서', [
     {'lines': L(D5), 'flow': ['G: 도와줄래? 숙제용 책', 'B: 어떤 종류의 책?', 'G: 남을 도운 유명인, 에세이', 'B: 누구에 대해?', 'G: Schweitzer 박사… 다른 사람 추천해 줘', 'B: Audrey Hepburn 어때?', 'G: 배우인 건 알지만 뭘 했어?', 'B: 아이들을 위한 자원봉사', 'G: 그녀에 대해 쓸게, 고마워!']},
     {'lines': L(D5)[3:8], 'flow': ['B: 누구에 대해 쓰고 싶어?', 'G: Schweitzer 박사… 다른 사람 추천해 줘', 'B: Audrey Hepburn 어때?', 'G: 남을 돕기 위해 뭘 했어?', 'B: 특히 아이들을 위해 자원봉사']},
     {'lines': L(D6), 'flow': ['인사', '소개할 영화 제목', '음악에 대한 사랑을 잃은 피아니스트', '새 출발을 위해 작은 마을로', '아이들을 가르치며 사랑을 되찾음', '훌륭한 음악·감동적 이야기 → 강력 추천']}], guide=G_ORD),
  ST('blank', '빈칸추론', [
     {'s': 'He moves to a small town for a new ____.', 'opts': ['start', 'job', 'piano', 'house'], 'ex': '정답 ▶ start (시작)\n이유: for a new start = 새 출발을 위해. 음악에 대한 사랑을 잃은 뒤 새로 시작하려고 이사해요.'},
     {'s': "Really? Then, I can write ____ her. Thank you!", 'opts': ['about', 'for', 'with', 'to'], 'ex': '정답 ▶ about\n이유: write about ~ = ~에 대해 쓰다. Who do you want to write about?와 짝이에요.'}], guide=G_BL),
  ST('mc', '어색한 대화 고르기', [
     {'q': '다음 중 짝지어진 대화가 <b>어색한</b> 것은?', 'opts': ['A: Can you recommend someone else for me? B: Yes, I can write about her.', 'A: What kinds of books are you looking for? B: Books on famous people who helped others.', 'A: Who do you want to write about? B: I was thinking about Dr. Schweitzer.', 'A: What did she do to help others? B: She did a lot of volunteer work.'],
      'ex': '정답 ▶ A: Can you recommend someone else for me? B: Yes, I can write about her.\n이유: 추천을 요청했으니 What about Audrey Hepburn?처럼 추천할 사람을 말해야 해요.'}], guide=G_ODD),
  ST('mc', '의사소통 기능', [
     {'q': '밑줄 친 말과 바꾸어 쓸 수 <b>없는</b> 것은?<br><b>B: <u>What about</u> Audrey Hepburn?</b>', 'opts': ['Why did you choose', 'How about', 'I recommend', 'Why don\'t you write about'],
      'ex': "정답 ▶ Why did you choose\n이유: What about ~?(~은 어때?)은 추천하는 말이에요. How about ~? / I recommend ~. / Why don't you write about ~?으로 바꿔 쓸 수 있어요. Why did you choose ~?는 이유를 묻는 말이에요."},
     {'q': '밑줄 친 말의 의도로 알맞은 것은?<br><b>G: I was thinking about Dr. Schweitzer, but <u>can you recommend someone else for me?</u></b>', 'opts': ['추천 요청하기', '감사하기', '종류 묻기', '거절하기'], 'ex': '정답 ▶ 추천 요청하기\n이유: Can you recommend ~ for me? = 나에게 ~을 추천해 줄래? (someone else = 다른 누군가)'}], guide=G_FN),
  ST('mc', '요약문 완성', [
     {'n': None, 'box': [D5[0][1]], 'q': '다음 글의 내용을 한 문장으로 요약할 때, 빈칸 (A), (B)에 들어갈 말로 가장 알맞은 것은?<br><b>Somi decides to write about Audrey Hepburn, who did a lot of (A) ______ work, especially for (B) ______.</b>',
      'opts': ['(A) volunteer – (B) children', '(A) volunteer – (B) sick people', '(A) acting – (B) children', '(A) music – (B) children', '(A) writing – (B) teachers'],
      'ex': '정답 ▶ (A) volunteer – (B) children\n(A)(B) She did a lot of volunteer work, especially for children.\n오답 ▶ sick people(아픈 사람들): 교과서 메모 문제의 오답 / acting(연기): 배우였던 건 맞지만 남을 도운 일이 아니에요.', 'ev': ['She did a lot of volunteer work, especially for children']},
     {'n': None, 'box': [D6[0][1]], 'q': '다음 글의 내용을 한 문장으로 요약할 때, 빈칸 (A), (B)에 들어갈 말로 가장 알맞은 것은?<br><b>In The Song of Love, a pianist who (A) ______ his love for music gets it back after he begins teaching music to (B) ______.</b>',
      'opts': ['(A) loses – (B) children', '(A) finds – (B) children', '(A) loses – (B) adults', '(A) shows – (B) pianists', '(A) loses – (B) his friends'],
      'ex': '정답 ▶ (A) loses – (B) children\n(A) a pianist who loses his love for music\n(B) he begins teaching music to children and finds his love for music again', 'ev': ['a pianist who loses his love for music', 'he begins teaching music to children']}], guide=G_SUM),
 ]}

def ansfirst_ok(steps):
    for s in steps:
        if s['type'] == 'mc':
            for q in s['items']: assert len(set(q['opts'])) == len(q['opts'])

for d in (k6a, k6b): ansfirst_ok(d['steps'])
path = sys.argv[1] if len(sys.argv) > 1 else '/home/claude/proj/data/m2-donga-yoon-L7.js'
PK = json.loads(subprocess.check_output(['node', '-e', "global.window={};require('%s');process.stdout.write(JSON.stringify(window.PKG))" % path]))
base = [d for d in PK['days'] if d['id'] not in ('k6a', 'k6b')]
PK['days'] = [k6a, k6b] + base
for i, d in enumerate(PK['days']): d['name'] = 'DAY %d' % (i + 1)
PK['unit'] = 'Lesson 6~8'
src = open(path, encoding='utf-8').read(); head = src[:src.index('window.PKG')]
if '6과 대화문' not in head: head = head.rstrip('\n') + '\n/* 11/15: 6과 대화문 k6a·k6b 맨 앞에 추가 (generators/gen_m2d6dlg.py). 8과는 대화문 없음 */\n'
write(PK, path, head)
print('ok', [(d['name'], d['id'], d['range'], len(d['steps'])) for d in PK['days']])
