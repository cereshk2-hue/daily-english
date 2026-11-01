from gramcommon import *
# 중2 비상(황종배) 8과 문법 (11/1): Pattern 1 not only ~ but also … · Pattern 2 간접의문문
# 근거: Grammar Build Up 객관식 8과 유형 + 교과서 8과 본문 문장. 8과 본문(d4) 뒤 DAY 13~18

DAYS = []

# ═════════ 8과 문법 ① not only ~ but also 기본 ═════════
D = Day('h1', '8과 문법 ① not only ~ but also 기본', 'A뿐만 아니라 B도 · 병렬 구조 · B as well as A')
D.note('개념 ① not only A but also B', [
    ('not only A but also B', 'A뿐만 아니라 B도 (but also에서 also는 생략 가능: not only A but B)'),
    ('You need not only strength but also teamwork.', '교과서 8과 · 여러분은 힘뿐만 아니라 팀워크도 필요합니다.'),
    ('This wild journey is not only exciting but also meaningful.', '교과서 8과 · 이 야생의 여정은 흥미진진할 뿐만 아니라 의미도 있을 것입니다.'),
    ('= B as well as A', 'not only A but also B = B as well as A (A와 B의 순서가 바뀌어요!)\nThe girl is not only smart but also beautiful. = The girl is beautiful as well as smart.'),
])
D.note('개념 ② 병렬 구조', [
    ('A와 B는 같은 형태', '명사-명사 / 형용사-형용사 / 동명사-동명사 / to부정사-to부정사 / 동사-동사'),
    ('likes not only dancing but also singing', 'dancing · singing ✔ (sing ✗)'),
    ('not only sings but also dances', '3인칭 단수 동사끼리 ✔ (dance ✗)'),
    ('not only beautiful but also intelligent', '형용사끼리 ✔ (beauty ✗)'),
])
D.step(SCARDS(D, '해석 카드', [
    ('For this race, you need not only strength but also teamwork.', '이 경주를 위해서, 여러분은 힘뿐만 아니라 팀워크도 필요하다. (교과서)'),
    ('This wild journey is not only exciting but also meaningful.', '이 야생의 여정은 흥미진진할 뿐만 아니라 의미도 있다. (교과서)'),
    ('The soup is not only delicious but also healthy.', '그 수프는 맛있을 뿐만 아니라 건강에도 좋다.'),
    ('I like not only reading books but also writing stories.', '나는 책 읽는 것뿐만 아니라 이야기 쓰는 것도 좋아한다.'),
    ('The store sells not only books but also cakes.', '그 가게는 책뿐만 아니라 케이크도 판다.'),
    ('David is not only strong but also fast.', 'David는 힘이 셀 뿐만 아니라 빠르다.'),
    ('He not only plays the guitar but also writes songs.', '그는 기타를 칠 뿐만 아니라 노래도 쓴다.'),
    ('Kate speaks Chinese as well as Korean.', 'Kate는 한국어뿐만 아니라 중국어도 한다.')],
    guide='"A뿐만 아니라 B도"로 해석해요. as well as는 뒤에 있는 말이 A예요.'))
D.step(TF('개념 확인 T/F', [
    ('not only A but also B는 "A가 아니라 B"라는 뜻이다.', False, '정답 ▶ F\n이유: "A뿐만 아니라 B도"예요. "A가 아니라 B"는 not A but B'),
    ('Kate speaks not only Korean but also Chinese. = Kate speaks Chinese as well as Korean.', True, '정답 ▶ T\n이유: not only A but also B = B as well as A (순서가 바뀌어요)'),
    ('He likes not only dancing but also sing.은 바른 문장이다.', False, '정답 ▶ F\n이유: 병렬 구조 → dancing · singing'),
    ('She is not only beauty but also intelligent.는 바른 문장이다.', False, '정답 ▶ F\n이유: intelligent(형용사)와 짝 → beautiful(형용사)'),
    ('Mina not only sings well but plays the piano well.에서 also가 없어도 된다.', True, '정답 ▶ T\n이유: not only A but (also) B → also는 생략 가능'),
    ('Sally bought a pencil as well as an eraser.는 "연필뿐만 아니라 지우개도 샀다"라는 뜻이다.', False, '정답 ▶ F\n이유: B as well as A = A뿐만 아니라 B도 → "지우개뿐만 아니라 연필도 샀다"'),
]))
D.step(PICK(D, '어법 선택', [
    ('You have to study not {only|like} math but also English.', '너는 수학뿐만 아니라 영어도 공부해야 한다.', '정답 ▶ only\n이유: not only A but also B'),
    ('Anne can speak not only English {but|and} also French.', 'Anne은 영어뿐만 아니라 프랑스어도 할 수 있다.', '정답 ▶ but\n이유: not only A but also B (and also ✗)'),
    ('Kevin enjoys not only singing but also {dancing|dance}.', 'Kevin은 노래하는 것뿐만 아니라 춤추는 것도 즐긴다.', '정답 ▶ dancing\n이유: 병렬 → singing · dancing'),
    ('Anne not only sings but also {dances|dancing} on the stage.', 'Anne은 무대에서 노래할 뿐만 아니라 춤도 춘다.', '정답 ▶ dances\n이유: sings와 병렬 → dances'),
    ('The method is not only safe but also {convenient|convenience}.', '그 방법은 안전할 뿐만 아니라 편리하다.', '정답 ▶ convenient\n이유: safe(형용사)와 병렬 → 형용사'),
    ('She is excited as well as {happy|happily}.', '그녀는 행복할 뿐만 아니라 신이 나 있다.', '정답 ▶ happy\n이유: excited(형용사)와 병렬, be동사 뒤 보어 → 형용사'),
    ('We expected you not only to be open-minded but also {to have|have} a love for children.', '우리는 네가 마음이 열려 있을 뿐만 아니라 아이들을 사랑하는 마음도 갖기를 기대했다.', '정답 ▶ to have\n이유: to be와 병렬 → to have'),
    ('The girl is beautiful {as well as|such as} smart.', '그 소녀는 똑똑할 뿐만 아니라 아름답다.', '정답 ▶ as well as\n이유: B as well as A = A뿐만 아니라 B도'),
]))
D.step(MC('같은 뜻 · 우리말', [
    ('주어진 문장과 의미가 같은 것은?' + Q('Shakespeare was not only a writer but also an actor.'), ['Shakespeare was an actor as well as a writer.', 'Shakespeare was not a writer but an actor.', 'Shakespeare was neither a writer nor an actor.', 'Shakespeare was a writer, not an actor.'],
     '정답 ▶ Shakespeare was an actor as well as a writer.\n이유: not only A but also B = B as well as A\n오답 ▶ not A but B(A가 아니라 B) / neither A nor B(A도 B도 아닌) / A, not B(B가 아님)'),
    ('주어진 문장과 의미가 같은 것은?' + Q('He gave not only a doll but also a card to me.'), ['He gave a card as well as a doll to me.', 'He gave a doll as well as a card to me.', 'He gave either a doll or a card to me.', 'He gave not a doll but a card to me.'],
     '정답 ▶ He gave a card as well as a doll to me.\n이유: B(a card) as well as A(a doll)\n오답 ▶ 순서가 바뀌면 "카드뿐만 아니라 인형도"로 강조가 달라져요 / either A or B(둘 중 하나) / not A but B'),
    ('우리말을 바르게 영작한 것은?<br><b>그는 가난할 뿐만 아니라 게으르다.</b>', ['He is not only poor but also lazy.', 'He is not poor but lazy.', 'He is either poor or lazy.', 'He is poor as well as lazy.'],
     '정답 ▶ He is not only poor but also lazy.\n오답 ▶ not A but B(가난한 게 아니라 게으르다) / either A or B(둘 중 하나) / poor as well as lazy(게으를 뿐만 아니라 가난하다 → 순서 반대)'),
    ('우리말을 바르게 영작한 것은?<br><b>Sally는 연필뿐만 아니라 지우개도 샀다.</b>', ['Sally bought not only a pencil but also an eraser.', 'Sally bought not only an eraser but also a pencil.', 'Sally bought a pencil as well as an eraser.', 'Sally bought not a pencil but an eraser.'],
     '정답 ▶ Sally bought not only a pencil but also an eraser.\n이유: A(연필)뿐만 아니라 B(지우개)도\n오답 ▶ A와 B가 바뀜 / as well as 순서 반대 / not A but B'),
]))
D.sent('Shakespeare was not only a writer but also an actor.', '셰익스피어는 작가였을 뿐만 아니라 배우이기도 했다.'); D.sent('Shakespeare was an actor as well as a writer.', '셰익스피어는 작가였을 뿐만 아니라 배우이기도 했다.')
D.sent('He gave not only a doll but also a card to me.', '그는 나에게 인형뿐만 아니라 카드도 주었다.'); D.sent('He is not only poor but also lazy.', '그는 가난할 뿐만 아니라 게으르다.')
D.sent('Sally bought not only a pencil but also an eraser.', 'Sally는 연필뿐만 아니라 지우개도 샀다.')
D.step(SCR(D, '우리말 → 영어 배열', [
    ('For this race, you need not only strength but also teamwork.', '이 경주를 위해서, 여러분은 힘뿐만 아니라 팀워크도 필요하다.'),
    ('This wild journey is not only exciting but also meaningful.', '이 야생의 여정은 흥미진진할 뿐만 아니라 의미도 있다.'),
    ('Jenny can speak not only English but also Chinese.', 'Jenny는 영어뿐만 아니라 중국어도 말할 수 있다.'),
    ('The weather is not only cold but also windy.', '날씨가 추울 뿐만 아니라 바람도 분다.'),
]))
DAYS.append(D.done())

# ═════════ 8과 문법 ② 수 일치 · 비슷한 짝 ═════════
D = Day('h2', '8과 문법 ② 수 일치 · both / either / neither', '주어로 쓰이면 동사는 B에 · 헷갈리는 짝 구별')
D.note('개념 ① 주어 자리의 수 일치', [
    ('Not only A but also B + 동사', '동사는 B에 맞춰요: Not only I but also my brother is good at cooking.'),
    ('B as well as A + 동사', '동사는 앞의 B에 맞춰요: I as well as you am hungry. / Judy as well as I agrees.'),
    ('both A and B + 복수 동사', 'Both Cathy and Mary are planning to help.'),
    ('either A or B / neither A nor B / not A but B', '동사는 B에 맞춰요: Either Anne or you have ~ / Not she but I am good at ~'),
])
D.note('개념 ② 뜻 구별', [
    ('not only A but also B', 'A뿐만 아니라 B도 (둘 다 ✔)'), ('both A and B', 'A와 B 둘 다'),
    ('either A or B', 'A나 B 둘 중 하나'), ('neither A nor B', 'A도 B도 아닌'), ('not A but B', 'A가 아니라 B'),
])
D.step(PICK(D, '수 일치 고르기', [
    ('Not only I but also my brother {is|am} good at cooking.', '나뿐만 아니라 내 남동생도 요리를 잘한다.', '정답 ▶ is\n이유: 동사는 B(my brother)에 맞춰요.'),
    ('Not only the teacher but also the students {want|wants} the best result.', '선생님뿐만 아니라 학생들도 최고의 결과를 원한다.', '정답 ▶ want\n이유: B(the students, 복수)에 맞춰요.'),
    ('I as well as he {am|is} wrong.', '그뿐만 아니라 나도 틀렸다.', '정답 ▶ am\n이유: B as well as A → 앞의 B(I)에 맞춰요.'),
    ('He as well as you {speaks|speak} English.', '너뿐만 아니라 그도 영어를 한다.', '정답 ▶ speaks\n이유: 앞의 B(He)에 맞춰요.'),
    ('My brother as well as you {likes|like} to play soccer.', '너뿐만 아니라 내 남동생도 축구하는 것을 좋아한다.', '정답 ▶ likes\n이유: 앞의 B(My brother)에 맞춰요.'),
    ('Both Cathy and Mary {are|is} planning to help the homeless.', 'Cathy와 Mary 둘 다 노숙자들을 도울 계획이다.', '정답 ▶ are\n이유: both A and B → 복수'),
    ('Not only my parents but also my sister {doesn\'t|don\'t} like him.', '부모님뿐만 아니라 내 여동생도 그를 좋아하지 않는다.', "정답 ▶ doesn't\n이유: B(my sister, 단수)에 맞춰요."),
    ('Not she but I {am|is} good at speaking English.', '그녀가 아니라 내가 영어를 잘한다.', '정답 ▶ am\n이유: not A but B → B(I)에 맞춰요.'),
]))
D.step(MC('빈칸 짝 고르기', [
    ('빈칸 (A), (B)에 알맞은 것은?<br>• Not only I but also my brother (A)____ good at cooking.<br>• Anne not only sings but also (B)____ on the stage.', ['is - dances', 'am - dancing', 'are - dance', 'am - dances', 'is - dance'],
     '정답 ▶ is - dances\n이유: (A) B(my brother)에 맞춰 is (B) sings와 병렬 → dances'),
    ('빈칸 (A), (B)에 알맞은 것은?<br>• Not only the teacher but also the students (A)____ the best result.<br>• My brother likes not only playing soccer but also (B)____ basketball.', ['want - playing', 'wants - playing', 'want - play', 'wants - plays'],
     '정답 ▶ want - playing\n이유: (A) the students(복수) → want (B) playing과 병렬 → playing'),
    ('빈칸에 알맞은 말이 바르게 짝지어진 것은?<br>• Either Anne ____ you have a secret card.<br>• Both Cathy and Mary ____ planning to help the homeless.<br>• Judy as well as I ____ with his opinion.', ['or - are - agrees', 'nor - is - agree', 'or - is - agrees', 'nor - are - agree'],
     '정답 ▶ or - are - agrees\n이유: either A or B / both A and B → 복수 are / B as well as A → Judy에 맞춰 agrees'),
    ('두 문장이 같은 뜻이 되도록 빈칸에 알맞은 것은?<br><b>The 2002 World Cup was held in Korea. It was held in Japan, too.<br>= The 2002 World Cup was held ____ in Korea ____ in Japan.</b>', ['both - and', 'either - or', 'neither - nor', 'not - but'],
     '정답 ▶ both - and\n이유: 한국에서도 일본에서도 → 둘 다\n오답 ▶ either A or B(둘 중 하나) / neither A nor B(둘 다 아님) / not A but B(A가 아니라 B)'),
]))
D.step(MC('뜻 구별', [
    ('우리말을 바르게 영작한 것은?<br><b>Jessica뿐만 아니라 나도 개를 가지고 있다.</b>', ['Not only Jessica but also I have a dog.', 'Not only I but also Jessica has a dog.', 'Either Jessica or I has a dog.', 'Not Jessica but I have a dog.', 'Jessica as well as I has a dog.'],
     '정답 ▶ Not only Jessica but also I have a dog.\n이유: A(Jessica)뿐만 아니라 B(나)도 → 동사는 I에 맞춰 have\n오답 ▶ A·B가 바뀜 / 둘 중 하나 / Jessica가 아니라 나 / Jessica as well as I는 "나뿐만 아니라 Jessica도"'),
    ('주어진 문장과 의미가 같은 것은?' + Q('Girls as well as boys like to play soccer.'), ['Not only boys but also girls like to play soccer.', 'Boys as well as girls like to play soccer.', 'Only girls like to play soccer.', 'Not girls but boys like to play soccer.'],
     '정답 ▶ Not only boys but also girls like to play soccer.\n이유: B(girls) as well as A(boys) = not only A(boys) but also B(girls)'),
    ('짝지어진 두 문장의 의미가 서로 <b>다른</b> 것은?', ['He was a great teacher as well as a great father. = He was not a great teacher but a great father.', 'He is strong and he is smart. = He is not only strong but also smart.', 'Chocolate is enjoyed by adults as well as children. = Chocolate is enjoyed not only by children but also by adults.', 'The hotel room is cheap as well as clean. = The hotel room is not only clean but also cheap.'],
     '정답 ▶ He was a great teacher as well as a great father. = He was not a great teacher but a great father.\n이유: not A but B는 "훌륭한 선생님이 아니라 훌륭한 아버지" → 뜻이 달라요.'),
]))
D.sent('Not only Jessica but also I have a dog.', 'Jessica뿐만 아니라 나도 개를 가지고 있다.'); D.sent('Girls as well as boys like to play soccer.', '남자아이들뿐만 아니라 여자아이들도 축구하는 것을 좋아한다.')
D.step(ERR(D, '오류 찾기', [
    ('Not only my teacher but [[my parents]] [[agrees]] with [[my]] [[plan]].', 1, 'agree', '선생님뿐만 아니라 부모님도 내 계획에 동의하신다.', '정답 ▶ agrees → agree\n이유: 동사는 B(my parents, 복수)에 맞춰요.'),
    ('Not only she but [[also]] I [[is]] a [[singer]] [[too]].', 1, 'am', '그녀뿐만 아니라 나도 가수이다.', '정답 ▶ is → am\n이유: B(I)에 맞춰 am'),
    ('Susie as well as her [[cousins]] [[are]] really good at [[playing]] [[badminton]].', 1, 'is', '사촌들뿐만 아니라 Susie도 배드민턴을 정말 잘 친다.', '정답 ▶ are → is\n이유: B as well as A → 앞의 Susie(단수)에 맞춰요.'),
    ('Sungkyu is good at [[dancing]] as well [[as]] [[sing]] [[songs]].', 2, 'singing', '성규는 노래뿐만 아니라 춤도 잘 춘다.', '정답 ▶ sing → singing\n이유: 병렬 → dancing · singing'),
]))
DAYS.append(D.done())

# ═════════ 8과 문법 ③ not only ~ but also 실전 ═════════
D = Day('h3', '8과 문법 ③ not only ~ but also 실전', '어법상 옳은 문장 · 개수 세기 · 두 문장 잇기 · 도치(Not only did ~)')
D.note('개념 · 더 알아 두기', [
    ('도치', 'Not only가 문장 맨 앞에 오면 의문문 어순: Not only did she win the race, but she also broke the record.'),
    ('두 문장 잇기', 'This book is informative. It is also interesting. → This book is interesting as well as informative.'),
    ('체크리스트', '① 뜻(뿐만 아니라 / 아니라 / 둘 다 / 둘 중 하나) ② A·B 같은 형태 ③ 주어면 동사는 B에(as well as는 앞에)'),
])
D.step(MC('어법상 옳은 문장', [
    ('어법상 <b>옳은</b> 문장은?', ['Not only he but also we were afraid of the dark.', 'I as well as he is wrong.', 'He as well as you speak English.', 'Not only she but also I is a singer.', "Not only my parents but also my sister don't like him."],
     "정답 ▶ Not only he but also we were afraid of the dark.\n이유: B(we)에 맞춰 were\n오답 ▶ is → am / speak → speaks / is → am / don't → doesn't"),
    ('어법상 <b>옳은</b> 문장은?', ['My brother as well as you likes to play soccer.', 'Not only John but also I are tall.', 'Kevin enjoys not only singing but also dance.', 'He not only play tennis but also watch movies.', 'She is excited as well as happily.'],
     '정답 ▶ My brother as well as you likes to play soccer.\n오답 ▶ are → am / dance → dancing / play → plays, watch → watches / happily → happy'),
    ('어법상 <b>어색한</b> 문장은?', ['Ben cannot play not only the piano but also plays the guitar.', 'Bill Gates is not only smart but also rich.', 'They as well as he want to meet the singer.', 'Not only Jisu but also my sisters go to the movies.'],
     '정답 ▶ Ben cannot play not only the piano but also plays the guitar.\n이유: 병렬 → not only the piano but also the guitar (plays ✗)'),
    ('어법상 <b>옳은</b> 문장은?', ['Not only does she speak French, but she cooks well.', 'Not only he is a singer but also an actor.', 'Not only you but also she are pretty.', 'The place is not only wonderful but also a good one to visit.'],
     '정답 ▶ Not only does she speak French, but she cooks well.\n이유: Not only가 맨 앞 → 도치(does she speak)\n오답 ▶ Not only is he ~ / she → is / a good one → good(병렬)'),
]))
D.step(MC('개수 세기 · 고르기', [
    ('어법상 <b>틀린</b> 것을 모두 고른 것은?<br>ⓐ Hana likes not only cake but also cookies.<br>ⓑ Not only the movie but also the book is interesting.<br>ⓒ Not only I but also Mr. Parker want to be a pilot.<br>ⓓ Henry speaks not only English but Korean.<br>ⓔ Sungkyu is good at dancing as well as sing.<br>ⓕ Susie as well as her cousins are good at badminton.', ['ⓒ, ⓔ, ⓕ', 'ⓐ, ⓓ', 'ⓑ, ⓒ, ⓔ', 'ⓒ, ⓓ, ⓕ', 'ⓑ, ⓓ'],
     '정답 ▶ ⓒ, ⓔ, ⓕ\n틀린 것 ▶ ⓒ want → wants(Mr. Parker) / ⓔ sing → singing / ⓕ are → is(Susie)\n맞는 것 ▶ ⓐ ⓑ ⓓ(also 생략 OK)', True),
    ('어법상 <b>옳은</b> 문장의 개수는?<br>ⓐ She enjoys not only singing but also to dance.<br>ⓑ Her language as well as her behavior upsets me.<br>ⓒ Not only Jane but also Eric likes English.<br>ⓓ Not only the students but also the teacher were glad.<br>ⓔ She as well as her friends have similar problems.', ['2개', '1개', '3개', '4개', '5개'],
     '정답 ▶ 2개 (ⓑ, ⓒ)\n틀린 것 ▶ ⓐ to dance → dancing / ⓓ were → was(the teacher) / ⓔ have → has(She)', True),
]))
D.step(MC('두 문장 잇기', [
    ('두 문장을 한 문장으로 만들 때 가장 적절한 것은?', ['This book is informative. It is also interesting. → This book is interesting as well as informative.', 'Leo has gone to America. Kyle has gone, too. → Not only Kyle but also Leo have gone to America.', "Judy's sister is a nurse. She is also a teacher. → Judy's sister is not a teacher but a nurse.", "Sunny doesn't eat vegetables. She doesn't eat fruit either. → Sunny eats not only fruit but also vegetables."],
     '정답 ▶ This book is informative. It is also interesting. → This book is interesting as well as informative.\n오답 ▶ 동사는 Leo(단수)에 → has gone / not A but B(간호사만) / 둘 다 안 먹음 → neither A nor B'),
    ('두 문장을 한 문장으로 만들 때 빈칸에 알맞은 것은?<br><b>Cathy speaks English. She also speaks Japanese.<br>→ Cathy speaks not ____ English ____ also Japanese.</b>', ['only - but', 'but - only', 'only - and', 'simply - and'],
     '정답 ▶ only - but\n이유: not only A but also B'),
]))
D.step(SCR(D, '우리말 → 영어 배열', [
    ('Not only I but also my brother is good at cooking.', '나뿐만 아니라 내 남동생도 요리를 잘한다.'),
    ('The soup is not only delicious but also healthy.', '그 수프는 맛있을 뿐만 아니라 건강에도 좋다.'),
    ('He is interested in arts as well as music.', '그는 음악뿐만 아니라 예술에도 관심이 있다.'),
]))
DAYS.append(D.done())

# ═════════ 8과 문법 ④ 간접의문문 기본 ═════════
D = Day('h4', '8과 문법 ④ 간접의문문 기본', '의문사 + 주어 + 동사 · do / does / did 없애기')
D.note('개념 ① 간접의문문', [
    ('Do you know? + Where is she?', '→ Do you know where she is? (그녀가 어디에 있는지 아니?)'),
    ('어순', '의문사 + 주어 + 동사 (평서문 순서) · 도치 ✗'),
    ('Do you know what the most challenging race in the world is?', '교과서 8과 · 세상에서 가장 도전적인 경주가 무엇인지 아시나요?'),
    ('Do you know when the teams find out the course for the year?', '교과서 8과 · 팀들이 그해의 코스를 언제 알게 되는지 아시나요?'),
])
D.note('개념 ② 바꾸는 법', [
    ('be동사', 'Where is the bus stop? → where the bus stop is'),
    ('조동사', 'Where can I wash my hands? → where I can wash my hands'),
    ('일반동사', 'do/does/did를 없애고 동사에 시제·수를 넣어요.\nWhen does the concert start? → when the concert starts\nWhat did she say? → what she said'),
    ('의문사가 주어', '그대로: Who broke the cup? → who broke the cup / What makes a hero? → what makes a hero'),
    ('how + 형용사', 'How old is his sister? → how old his sister is (how old는 붙어 다녀요)'),
])
D.step(SCARDS(D, '해석 카드', [
    ('Do you know what the most challenging race in the world is?', '세상에서 가장 도전적인 경주가 무엇인지 아니? (교과서)'),
    ('Do you know when the teams find out the course for the year?', '팀들이 그해의 코스를 언제 알게 되는지 아니? (교과서)'),
    ('Can you tell me where the post office is?', '우체국이 어디 있는지 나에게 알려 줄 수 있니?'),
    ('Do you know why the baby is crying?', '그 아기가 왜 우는지 아니?'),
    ('I want to know where the bus stop is.', '나는 버스 정류장이 어디에 있는지 알고 싶다.'),
    ('Do you know what the sign means?', '그 표지판이 무엇을 의미하는지 아니?'),
    ('Can you tell me when the restaurant opens?', '식당이 언제 여는지 말해 줄 수 있니?'),
    ("I'd like to know how much the dishes are.", '나는 그 접시들이 얼마인지 알고 싶다.')],
    guide='간접의문문은 "~인지, ~하는지"로 해석해요.'))
D.step(PICK(D, '어순 고르기', [
    ('Do you know where {she is|is she}?', '그녀가 어디에 있는지 아니?', '정답 ▶ she is\n이유: 의문사 + 주어 + 동사'),
    ('Can you tell me how long {the river is|is the river}?', '그 강이 얼마나 긴지 말해 줄 수 있니?', '정답 ▶ the river is\n이유: how long + 주어 + 동사'),
    ("I don't know what {she did|did she do}.", '나는 그녀가 무엇을 했는지 모른다.', '정답 ▶ she did\n이유: did를 없애고 동사를 과거형(did)으로'),
    ('Ted asks me when the concert {starts|start}.', 'Ted는 나에게 콘서트가 언제 시작하는지 묻는다.', '정답 ▶ starts\n이유: does를 없애고 3인칭 단수 → starts'),
    ('I wonder where Jenny {went|goes} last night.', '나는 Jenny가 어젯밤에 어디에 갔는지 궁금하다.', '정답 ▶ went\n이유: last night → 과거'),
    ('Do you know what time {it is|is it}?', '지금 몇 시인지 아니?', '정답 ▶ it is\n이유: what time + 주어 + 동사'),
    ('You may have different ideas about what {makes|make} a hero.', '여러분은 무엇이 영웅을 만드는지에 대해 다른 생각을 가지고 있을지도 모른다.', '정답 ▶ makes\n이유: 의문사 what이 주어(단수) → makes'),
    ('Do you know how old {his sister is|is his sister}?', '그의 누나가 몇 살인지 아니?', '정답 ▶ his sister is\n이유: how old + 주어 + 동사'),
]))
D.step(MC('두 문장 → 한 문장', [
    ('두 문장을 한 문장으로 만들 때 알맞은 것은?<br><b>Can you tell me? + What did she say?</b>', ['Can you tell me what she said?', 'Can you tell me what did she say?', 'Can you tell me what she says?', 'What can you tell me she said?'],
     '정답 ▶ Can you tell me what she said?\n이유: did를 없애고 said(과거)\n오답 ▶ 어순 ✗ / 시제 ✗ / 의문사 위치 ✗'),
    ('두 문장을 한 문장으로 만들 때 알맞은 것은?<br><b>Could you tell me? + Where does the bus stop next?</b>', ['Could you tell me where the bus stops next?', 'Could you tell me where does the bus stop next?', 'Could you tell me where the bus stopped next?', 'Could you tell me where does the bus stops next?'],
     '정답 ▶ Could you tell me where the bus stops next?\n이유: does를 없애고 stops(현재, 3인칭 단수)'),
    ('두 문장을 한 문장으로 만들 때 알맞은 것은?<br><b>I\'d like to know. + When did she come to the party?</b>', ["I'd like to know when she came to the party.", "I'd like to know when she comes to the party.", "I'd like to know when came she to the party.", "I'd like to know when did she came to the party."],
     "정답 ▶ I'd like to know when she came to the party.\n이유: did를 없애고 came(과거)"),
    ('두 문장을 한 문장으로 연결할 때 <b>어색한</b> 것은?', ['Where can I wash my hands? + Tell me. → Tell me where can I wash my hands.', 'What is she doing? + Do you know? → Do you know what she is doing?', 'Who is she? + Do you know? → Do you know who she is?', 'How tall is he? + I want to know. → I want to know how tall he is.'],
     '정답 ▶ Where can I wash my hands? + Tell me. → Tell me where can I wash my hands.\n이유: 의문사 + 주어 + 동사 → where I can wash my hands'),
]))
D.sent('Can you tell me what she said?', '그녀가 뭐라고 했는지 말해 줄 수 있니?'); D.sent('Could you tell me where the bus stops next?', '버스가 다음에 어디에 서는지 말씀해 주실 수 있나요?')
D.sent("I'd like to know when she came to the party.", '나는 그녀가 언제 파티에 왔는지 알고 싶다.')
D.step(SCR(D, '우리말 → 영어 배열', [
    ('Do you know when the teams find out the course?', '팀들이 언제 코스를 알게 되는지 아니?'),
    ('Do you know what the most challenging race in the world is?', '세상에서 가장 도전적인 경주가 무엇인지 아니?'),
    ('Can you tell me where the post office is?', '우체국이 어디 있는지 나에게 알려 줄 수 있니?'),
    ('I wonder what time we are going to meet.', '나는 우리가 몇 시에 만날 예정인지 궁금하다.'),
]))
DAYS.append(D.done())

# ═════════ 8과 문법 ⑤ if/whether · think 동사 ═════════
D = Day('h5', '8과 문법 ⑤ if / whether · Do you think 순서', '의문사가 없으면 if·whether · think류 동사는 의문사를 맨 앞으로')
D.note('개념 ① 의문사가 없는 의문문', [
    ('Is this bus going to the mall?', '→ Do you know if(whether) this bus is going to the mall? (~인지 아닌지)'),
    ('Did she call you?', '→ Can you tell me if she called you?'),
    ('that ✗', '"~인지"는 if/whether: I wonder that ~ ✗ → I wonder if ~'),
])
D.note('개념 ② think · believe · guess · suppose · imagine', [
    ('의문사가 맨 앞', 'Do you think? + Why did Mina leave early? → Why do you think Mina left early?'),
    ('Do you think why ~? ✗', '"예/아니오"로 답할 수 없는 질문이라 의문사를 맨 앞으로 보내요.'),
    ('know는 그대로', 'Do you know where he lives? ✔ (Where do you know ~? ✗)'),
    ('When do you think he will arrive?', '그가 언제 도착할 거라고 생각하니?'),
])
D.note('개념 ③ if 두 가지', [
    ('if = ~인지 (간접의문문)', 'I am not sure if this answer is right. (이 답이 맞는지 확실하지 않다)'),
    ('if = 만약 ~라면 (조건)', 'You will succeed if you do your best. (최선을 다하면 성공할 것이다)'),
])
D.step(PICK(D, '어법 선택', [
    ("I don't know {if|that} he will succeed.", '나는 그가 성공할지 모르겠다.', '정답 ▶ if\n이유: 의문사가 없는 간접의문문 → if/whether(~인지)'),
    ('Do you know {if|so} this bus is going to the mall?', '이 버스가 쇼핑몰에 가는지 아니?', '정답 ▶ if\n이유: Is this bus ~? → if + 주어 + 동사'),
    ('{Why do you think|Do you think why} Mina left early yesterday?', '너는 미나가 어제 왜 일찍 떠났다고 생각하니?', '정답 ▶ Why do you think\n이유: think는 의문사를 맨 앞으로'),
    ('{Do you know|What do you know} what your parents do for a living?', '부모님이 무슨 일을 하시는지 아니?', '정답 ▶ Do you know\n이유: know는 의문사가 뒤에 그대로'),
    ('{When|Do} do you think his grade will get better?', '너는 그의 성적이 언제 좋아질 거라고 생각하니?', '정답 ▶ When\n이유: When do you think + 주어 + 동사'),
    ('He asked me if I {liked|like} the novel.', '그는 나에게 그 소설을 좋아하는지 물었다.', '정답 ▶ liked\n이유: asked(과거) → 시제 일치 liked'),
    ('Can you tell me if Snow White {loved|did love} the prince?', '백설공주가 왕자를 사랑했는지 말해 줄 수 있니?', '정답 ▶ loved\n이유: Did ~ love? → if + 주어 + loved'),
]))
D.step(MC('if의 쓰임 · 문장 고르기', [
    ('밑줄 친 <i>if</i>의 쓰임이 나머지 넷과 <b>다른</b> 것은?', ['Call me <u>if</u> you need my help.', 'Go and check <u>if</u> she is OK.', "I'm not sure <u>if</u> it is correct.", 'Do you know <u>if</u> Mina can join us?', "He doesn't know <u>if</u> it is a good idea."],
     '정답 ▶ Call me <u>if</u> you need my help.\n이유: "만약 ~라면"(조건). 나머지는 "~인지"(간접의문문)'),
    ('밑줄 친 <i>if</i>의 쓰임이 <보기>와 같은 것은?<br><보기> We\'ll be in trouble <u>if</u> the project isn\'t completed by tomorrow.', ['You\'ll succeed <u>if</u> you do your best.', "I am not sure <u>if</u> this answer is right.", 'Do you know <u>if</u> she has a boyfriend?', 'I wonder <u>if</u> she will come to the party.'],
     '정답 ▶ You\'ll succeed <u>if</u> you do your best.\n이유: <보기>와 같은 "만약 ~라면"(조건). 나머지는 "~인지"'),
    ('두 문장을 한 문장으로 만들 때 알맞은 것은?<br><b>Do you think? + Why did Mina leave early yesterday?</b>', ['Why do you think Mina left early yesterday?', 'Do you think why Mina left early yesterday?', 'Why do you think did Mina leave early yesterday?', 'Do you think why did Mina leave early yesterday?'],
     '정답 ▶ Why do you think Mina left early yesterday?\n이유: think → 의문사 맨 앞 + 주어 + 동사(did 없애고 left)'),
    ('두 문장을 한 문장으로 연결할 때 <b>어색한</b> 것은?', ['Do you suppose? + Who ate my cookies? → Do you suppose who ate my cookies?', 'I asked you. + Why were they angry? → I asked you why they were angry.', 'Tell me. + What did she say? → Tell me what she said.', "I'd like to know. + Where did you go? → I'd like to know where you went."],
     '정답 ▶ Do you suppose? + Who ate my cookies? → Do you suppose who ate my cookies?\n이유: suppose → 의문사 맨 앞: Who do you suppose ate my cookies?'),
]))
D.step(TF('맞을까? T/F', [
    ('Do you think where we should go?는 바른 문장이다.', False, '정답 ▶ F\n이유: think → Where do you think we should go?'),
    ('Where do you know Tom has gone?은 바른 문장이다.', False, '정답 ▶ F\n이유: know는 의문사를 앞으로 보내지 않아요 → Do you know where Tom has gone?'),
    ('Which do you think is better?는 바른 문장이다.', True, '정답 ▶ T\n이유: think → 의문사(Which)가 맨 앞, Which가 주어라 바로 is'),
    ('Everyone wonders that she likes gimchi.는 바른 문장이다.', False, '정답 ▶ F\n이유: "~인지" → if/whether: Everyone wonders if she likes gimchi.'),
    ('I wonder whether Cindy loves me.는 바른 문장이다.', True, '정답 ▶ T\n이유: whether + 주어 + 동사 ✔'),
]))
D.sent('Where do you think we should go?', '너는 우리가 어디로 가야 한다고 생각하니?'); D.sent('Do you know where Tom has gone?', 'Tom이 어디에 갔는지 아니?'); D.sent('Which do you think is better?', '너는 어느 것이 더 낫다고 생각하니?')
D.sent('Everyone wonders if she likes gimchi.', '모두가 그녀가 김치를 좋아하는지 궁금해한다.'); D.sent('I wonder whether Cindy loves me.', '나는 Cindy가 나를 사랑하는지 궁금하다.')
DAYS.append(D.done())

# ═════════ 8과 문법 ⑥ 간접의문문 실전 · 종합 ═════════
D = Day('h6', '8과 문법 ⑥ 간접의문문 실전 · 종합', '영작 · 어법상 옳은/어색한 문장 · 개수 · not only와 섞어서')
D.note('시험 직전 체크리스트', [
    ('① 어순', '의문사 + 주어 + 동사 (where is he ✗ → where he is)'),
    ('② do/does/did', '없애고 동사에 시제·수: what did she do ✗ → what she did'),
    ('③ 의문사가 주어', 'who broke the window ✔ (who the window broke ✗)'),
    ('④ 의문사가 없으면', 'if / whether + 주어 + 동사 (that ✗)'),
    ('⑤ think류', 'Why do you think ~? ✔ / Do you think why ~? ✗'),
])
D.step(MC('우리말 → 영어', [
    ('우리말을 바르게 영작한 것은?<br><b>너는 누가 컴퓨터를 발명했는지 아니?</b>', ['Do you know who invented the computer?', 'Do you know who make the computer?', 'Who invented the computer do you know?', 'Who do you know invented the computer?'],
     '정답 ▶ Do you know who invented the computer?\n이유: 의문사 who가 주어 → who + 동사(invented)'),
    ('우리말을 바르게 영작한 것은?<br><b>저녁 식사가 언제 준비될지 확실히 모르겠어요.</b>', ["I'm not sure when dinner will be ready.", "I'm not sure when will dinner be ready.", "I'm not sure if will dinner be ready.", "I'm not sure where dinner will be ready."],
     "정답 ▶ I'm not sure when dinner will be ready.\n오답 ▶ 어순 ✗ / if 뒤 어순 ✗ / where(어디) 뜻이 다름"),
    ('우리말을 바르게 영작한 것은?<br><b>그가 언제 도착할 거라고 생각하니?</b>', ['When do you think he will arrive?', 'Do you think when he will arrive?', 'When do you think will he arrive?', 'Do you think when will he arrive?'],
     '정답 ▶ When do you think he will arrive?\n이유: think → 의문사 맨 앞 + 주어 + 동사'),
]))
D.sent('Do you know who invented the computer?', '너는 누가 컴퓨터를 발명했는지 아니?'); D.sent("I'm not sure when dinner will be ready.", '저녁 식사가 언제 준비될지 확실히 모르겠어요.')
D.sent('When do you think he will arrive?', '그가 언제 도착할 거라고 생각하니?')
D.step(MC('어법상 옳은 문장 · 어색한 문장', [
    ('어법상 <b>옳은</b> 문장은?', ["I was wondering why we didn't take the train.", "I don't know how old is he.", 'Do you know where is she from?', "I don't know why did he become a doctor."],
     "정답 ▶ I was wondering why we didn't take the train.\n오답 ▶ how old he is / where she is from / why he became"),
    ('어법상 <b>옳은</b> 문장은?', ['Would you tell me whether she lives in Seoul?', 'Do you know how the hotel is far?', 'Can you tell me where is the man?', 'Can you tell me when will the store open?'],
     '정답 ▶ Would you tell me whether she lives in Seoul?\n오답 ▶ how far the hotel is / where the man is / when the store will open'),
    ('어법상 <b>어색한</b> 문장은?', ['Do you know what color is it?', "Can you tell me why he is so upset?", "I don't know what you bought yesterday.", 'I wonder if he will come to my birthday party.'],
     '정답 ▶ Do you know what color is it?\n이유: → what color it is'),
    ('어법상 <b>어색한</b> 문장은?', ['Can you tell me what about your new movie is?', 'I want to test how smart she is.', 'I wonder if there is a father like him.', 'She wants to know why I was late for school.'],
     '정답 ▶ Can you tell me what about your new movie is?\n이유: → what your new movie is about (주어 your new movie + is + about)'),
]))
D.step(MC('개수 세기 · 고르기', [
    ('어법상 <b>어색한</b> 문장의 개수는?<br>ⓐ I wonder whether Cindy loves me.<br>ⓑ Do you remember what time was it?<br>ⓒ How far do you suppose he can run?<br>ⓓ Jessica doesn\'t know if there is a drugstore nearby.<br>ⓔ Please tell me what should I do.', ['2개', '1개', '3개', '4개', '5개'],
     '정답 ▶ 2개 (ⓑ, ⓔ)\n틀린 것 ▶ ⓑ what time it was / ⓔ what I should do\n맞는 것 ▶ ⓐ whether ✔ ⓒ suppose → 의문사 맨 앞 ✔ ⓓ if ✔', True),
    ('어법상 옳은 문장끼리 짝지은 것은?<br>ⓐ Do you know who is she?<br>ⓑ Can you tell me what brought you here?<br>ⓒ Do you know who eat the most hamburgers?<br>ⓓ She didn\'t even tell me what her name was.<br>ⓔ Do you know if Judy can play the guitar?', ['ⓑ, ⓓ, ⓔ', 'ⓐ, ⓒ, ⓓ', 'ⓑ, ⓒ, ⓓ', 'ⓐ, ⓓ, ⓔ'],
     '정답 ▶ ⓑ, ⓓ, ⓔ\n틀린 것 ▶ ⓐ who she is / ⓒ who eats(ate) — 의문사 주어는 단수 취급\n맞는 것 ▶ ⓑ what(주어) brought ✔ ⓓ what her name was ✔ ⓔ if ✔', True),
    ('(A), (B), (C)에서 알맞은 것은?<br>• I have no idea how (A)[they got / did they get] there.<br>• I want to know who (B)[got the message / did the message get] yesterday.<br>• Do you know where (C)[he is / is he] from?', ['they got - got the message - he is', 'they got - got the message - is he', 'did they get - did the message get - he is', 'did they get - got the message - is he'],
     '정답 ▶ they got - got the message - he is\n이유: (A) 주어 + 동사 (B) who가 주어 → who got the message (C) where he is from'),
]))
D.step(MC('not only + 간접의문문 섞어서', [
    ('교과서 8과 문장에 대한 설명으로 <b>틀린</b> 것은?<br>ⓐ Do you know what the most challenging race in the world is?<br>ⓑ For this race, you need not only strength but also teamwork.<br>ⓒ Do you know when the teams find out the course for the year?', ['ⓒ는 when do the teams find out으로 고쳐야 한다.', 'ⓐ는 "의문사 + 주어 + 동사" 순서의 간접의문문이다.', 'ⓑ는 "힘뿐만 아니라 팀워크도"라는 뜻이다.', 'ⓑ는 you need strength as well as teamwork와 강조하는 순서가 다르다.'],
     '정답 ▶ ⓒ는 when do the teams find out으로 고쳐야 한다.\n이유: 간접의문문은 의문사 + 주어 + 동사 → when the teams find out이 맞아요(교과서 그대로).\n포인트 ▶ ⓑ = you need teamwork as well as strength'),
]))
D.step(ERR(D, '오류 찾기', [
    ('I [[don\'t]] [[know]] what [[did she do]] [[yesterday]].', 2, 'she did', '나는 그녀가 어제 무엇을 했는지 모른다.', '정답 ▶ did she do → she did\n이유: 간접의문문은 주어 + 동사, did를 없애고 do를 과거형 did로'),
    ('I [[want]] to know [[where]] [[are you]] [[from]].', 2, 'you are', '나는 네가 어디 출신인지 알고 싶다.', '정답 ▶ are you → you are\n이유: 의문사 + 주어 + 동사'),
    ('[[Do you think]] [[why]] she [[cried]] [[last night]]?', 0, 'Why do you think', '너는 그녀가 어젯밤에 왜 울었다고 생각하니?', '정답 ▶ Do you think why → Why do you think\n이유: think는 의문사를 맨 앞으로'),
    ("I [[don't]] know [[that]] she [[will attend]] the meeting [[or not]].", 1, 'if', '나는 그녀가 회의에 참석할지 안 할지 모른다.', '정답 ▶ that → if(whether)\n이유: "~인지 아닌지" → if/whether'),
]))
DAYS.append(D.done())

for d in DAYS: ansfirst(d['steps'])
path = '/home/claude/proj/data/m2-visang-hwang-L7.js'
PK = json.loads(subprocess.check_output(['node', '-e', "global.window={};require('%s');process.stdout.write(JSON.stringify(window.PKG))" % path]))
base = [d for d in PK['days'] if not re.match(r'h\d', d['id'])]
at = [d['id'] for d in base].index('d4') + 1
PK['days'] = base[:at] + DAYS + base[at:]
for i, d in enumerate(PK['days']): d['name'] = 'DAY %d' % (i + 1)
src = open(path, encoding='utf-8').read(); head = src[:src.index('window.PKG')]
if '8과 문법' not in head: head = head.rstrip('\n') + '\n/* 11/1: 8과 본문 뒤 DAY 13~18 = 8과 문법 not only ~ but also · 간접의문문 (gen/gen_v8gram.py) */\n'
write(PK, path, head)
print('ok', [(d['name'], d['id'], d['range'], len(d['steps']), sum(len(s['items']) for s in d['steps'])) for d in PK['days']][10:])
