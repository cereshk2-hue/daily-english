from wu import *
# 38·39번
I1 = "All editing systems are now nonlinear computer-based systems that allow random access to any video shot or scene without having to fast forward or fast reverse to find it."
I2 = "Nonlinear systems can create a range of special effects, such as slow motion, wipes and dissolves."
I3 = "Another highlight of a digital nonlinear system is its random access process that makes it easy for an editor to find desired shots or scenes without having to spend time fast forwarding or rewinding videotape."
I4 = "With nonlinear editing, shots or scenes can be easily added or removed anywhere in the program, and the computer adjusts the program length automatically."
I5 = "Linear editing was like composing a paper on a typewriter."
I6 = "If a mistake was made or new information needed to be added the whole piece had to be retyped."
I7 = "Nonlinear editing, on the other hand, is like using a word processing program."
I8 = "If a mistake is made, it is easily deleted and fixed with a few keystrokes, and new information can be added easily."
P38 = ' '.join([I1, I2, I3, I4, I5, I6, I7, I8])
J1 = "A morally good person is one who does morally bad actions significantly less often than most and does morally good ones significantly more often than most."
J2 = "In judging a person not only her actions but also her intentions and motives are relevant."
J3 = "A morally good person must intend to do morally good actions and intend to avoid morally bad ones."
J4 = "A person who unintentionally prevents harm to others and does not harm them simply because things do not turn out as she intends is not morally good."
J5 = "Although this kind of situation generally occurs only in slapstick movies, it is worth mentioning to avoid the false impression that it is the actual consequences of a person's actions that count toward her being judged morally good or bad."
J6 = "But actual consequences are important."
J7 = "A person who always tries to prevent harm but never does, is not generally thought of as morally good."
J8 = "Of such a person, it may be said that she means well; but, contrary to Kant, some results are necessary before she is regarded as morally good."
P39 = ' '.join([J1, J2, J3, J4, J5, J6, J7, J8])

T = Test('3839', '38·39번', '비선형 편집 · 도덕적으로 선한 사람', '38·39번',
         '범위: 38번(타자기 같은 선형 편집 vs. 워드 프로그램 같은 비선형 편집) · 39번(선한 사람: 의도도 결과도 중요하다). 지문은 원문을 일부 바꾼 것이 있어요. 선택지는 본문 표현을 다른 말로 바꿔 썼으니 뜻을 정확히 따져 보세요.')

# ── 38번 ──
T.flex('다음 글의 주제로 가장 적절한 것은?', '38번', BOX(P38), [
    ('the advantages of nonlinear editing over linear editing', '선형 편집에 비해 비선형 편집이 가진 장점'),
    ('the history of the typewriter and its decline', '타자기의 역사와 쇠퇴'),
    ('how to create slow-motion effects on videotape', '비디오테이프로 슬로 모션 효과를 만드는 방법'),
    ('why editors still prefer to rewind videotape', '편집자들이 여전히 비디오테이프 되감기를 선호하는 이유'),
    ('the difficulty of learning word processing programs', '워드 프로그램을 배우는 것의 어려움')],
    "이유 ▶ 비선형 편집은 원하는 장면을 바로 찾고(random access), 특수 효과를 만들고, 장면을 쉽게 넣고 빼며 길이도 자동 조정 — 타자기 같은 선형 편집과 달리 워드 프로그램처럼 편하다 → 비선형 편집의 장점.\n오답 ▶ {1} 타자기는 비유일 뿐 {2} 특수 효과는 장점 중 하나, 비디오테이프로 만드는 방법이 아니다 {3} 되감는 시간을 쓰지 않아도 된다(without having to spend time ~ rewinding)고 했다 {4} 워드 프로그램은 쉬운 쪽의 비유\n포인트 ▶ 비교·대조 글(on the other hand)의 주제 = 두 대상의 차이와 그 장점.",
    [['nonlinear', '비선형의'], ['advantage', '장점'], ['rewind', '되감다'], ['decline', '쇠퇴']])

T.flex('다음 글의 내용과 일치하지 <u>않는</u> 것은?', '38번', BOX(P38), [
    ('In linear editing, a mistake could be fixed with just a few keystrokes.', '선형 편집에서는 실수를 키 몇 번만 눌러 고칠 수 있었다.'),
    ('Nonlinear systems let editors go directly to any shot or scene.', '비선형 시스템은 편집자가 어떤 장면으로든 바로 가게 해 준다.'),
    ('Effects such as slow motion can be produced with nonlinear systems.', '슬로 모션 같은 효과를 비선형 시스템으로 만들 수 있다.'),
    ('In nonlinear editing, the computer changes the program length on its own.', '비선형 편집에서는 컴퓨터가 프로그램 길이를 스스로 바꾼다.'),
    ('Linear editing is compared to writing a paper on a typewriter.', '선형 편집은 타자기로 글을 쓰는 것에 비유된다.')],
    "이유 ▶ 키 몇 번으로 고치는 것(fixed with a few keystrokes)은 비선형 편집(워드 프로그램). 선형 편집은 전체를 다시 쳐야 했다(the whole piece had to be retyped) ✗\n오답 ▶ {1} random access to any video shot or scene ✔ {2} special effects, such as slow motion ✔ {3} the computer adjusts the program length automatically ✔ (on its own = 스스로) {4} Linear editing was like composing a paper on a typewriter ✔\n포인트 ▶ 대조 글의 일치 문제: 어느 쪽(선형/비선형)의 특징인지 짝을 바꾼 선택지를 조심.",
    [['keystroke', '키를 누름'], ['directly', '바로'], ['on its own', '스스로'], ['compare A to B', 'A를 B에 비유하다']])

T.flex('다음 빈칸에 들어갈 말로 가장 적절한 것은?', '38번 변형', BOX(
    I4 + ' ' + I5 + ' If a mistake was made or new information needed to be added, ' + BL + '. ' + I7 + ' ' + I8), [
    ('the entire work had to be done over again', '작업 전체를 처음부터 다시 해야 했다'),
    ('it could easily be inserted anywhere', '어디에든 쉽게 끼워 넣을 수 있었다'),
    ('the computer corrected it automatically', '컴퓨터가 자동으로 그것을 고쳤다'),
    ('a few keystrokes were enough to fix it', '키 몇 번이면 고치기에 충분했다'),
    ('special effects could be used to hide it', '그것을 감추는 데 특수 효과를 쓸 수 있었다')],
    "이유 ▶ 원문: the whole piece had to be retyped(전체를 다시 쳐야 했다). 타자기로 쓴 글은 중간을 고칠 수 없어 처음부터 다시 해야 한다 → the entire work had to be done over again.\n오답 ▶ {1}·{2}·{3} 모두 비선형 편집(워드 프로그램)의 특징 {4} 특수 효과로 실수를 감춘다는 말은 없다\n포인트 ▶ on the other hand(반면에) 앞뒤는 정반대: 선형(다시 해야 함) ↔ 비선형(쉽게 고침).",
    [['entire', '전체의'], ['do over', '다시 하다'], ['insert', '끼워 넣다'], ['retype', '다시 타자 치다']])

T.fixed('다음 글의 밑줄 친 부분 중, 문맥상 낱말의 쓰임이 적절하지 <u>않은</u> 것은?', '38번 변형', BOX(
    "All editing systems are now nonlinear computer-based systems that allow " + CN(1, 'random') + " access to any video shot or scene without having to fast forward or fast reverse to find it. " + I2 + " Another highlight of a digital nonlinear system is its random access process that makes it easy for an editor to find " + CN(2, 'desired') + " shots or scenes without having to spend time fast forwarding or rewinding videotape. With nonlinear editing, shots or scenes can be easily added or " + CN(3, 'removed') + " anywhere in the program, and the computer adjusts the program length " + CN(4, 'manually') + ". " + I5 + ' ' + I6 + ' ' + I7 + " If a mistake is made, it is easily deleted and fixed with a few keystrokes, and new information can be added " + CN(5, 'easily') + "."),
    ['random', 'desired', 'removed', 'manually', 'easily'], 4,
    "이유 ▶ 컴퓨터가 프로그램 길이를 조정하는 것은 '자동으로' <i>automatically</i>. manually(손으로, 수동으로)는 컴퓨터가 하는 일과 맞지 않고, 비선형 편집이 편리하다는 흐름에도 어긋난다.\n오답 ▶ ① '임의' 접근(어떤 장면이든 바로) ✔ ② 편집자가 '원하는' 장면 ✔ ③ 장면을 쉽게 넣거나 '뺀다' ✔ ⑤ 새 정보도 '쉽게' 더할 수 있다 ✔\n포인트 ▶ automatically ↔ manually 반의어 짝.",
    [['random access', '임의 접근'], ['desired', '원하는'], ['manually', '수동으로'], ['automatically', '자동으로']])

T.fixed('다음 글의 밑줄 친 부분 중, 어법상 <u>틀린</u> 것은?', '38번 변형', BOX(
    "All editing systems are now nonlinear computer-based systems that " + CN(1, 'allow') + " random access to any video shot or scene without " + CN(2, 'having') + " to fast forward or fast reverse to find it. … Another highlight of a digital nonlinear system is its random access process that makes " + CN(3, 'it') + " easy for an editor " + CN(4, 'finding') + " desired shots or scenes. With nonlinear editing, shots or scenes can be easily " + CN(5, 'added') + " or removed anywhere in the program."),
    ['allow', 'having', 'it', 'finding', 'added'], 4,
    "이유 ▶ make + 가목적어 it + 형용사 + for 의미상 주어 + <i>to부정사</i>(진목적어) → to find.\n오답 ▶ ① 선행사 systems(복수) → allow ✔ ② 전치사 without + 동명사 ✔ ③ 뒤의 to부정사를 대신하는 가목적어 it ✔ ⑤ 장면이 '더해지는' 수동 can be added ✔\n포인트 ▶ make it easy(hard, possible) for A to V: 가목적어-진목적어 구문.",
    [['fast forward', '빨리 감다'], ['highlight', '가장 좋은 점'], ['make it easy to V', '~하는 것을 쉽게 하다']])

T.table('(A), (B), (C)의 각 네모 안에서 어법에 맞는 표현으로 가장 적절한 것은?', '38번', BOX(
    "All editing systems are now nonlinear computer-based systems that <b>(A)</b> [ allow / allows ] random access to any video shot or scene. … Linear editing was like composing a paper on a typewriter. If a mistake was made or new information needed <b>(B)</b> [ to be added / to add ], the whole piece had to be retyped. Nonlinear editing, on the other hand, is like using a word processing program. If a mistake is made, it <b>(C)</b> [ is easily deleted / easily deletes ] and fixed with a few keystrokes."),
    ['(A)', '(B)', '(C)'], [['allow', 'to be added', 'is easily deleted'], ['allows', 'to be added', 'is easily deleted'], ['allow', 'to add', 'is easily deleted'], ['allow', 'to be added', 'easily deletes'], ['allows', 'to add', 'easily deletes']],
    "이유 ▶ (A) 주격 관계대명사 that의 선행사 computer-based systems(복수) → <i>allow</i> (B) 정보가 '더해질' 필요 → 수동 <i>to be added</i> (C) 실수가 '삭제되는' 수동, 뒤의 and fixed와도 병렬 → <i>is easily deleted</i>\n오답 ▶ allows: 선행사를 단수로 착각 / to add: 정보가 직접 무언가를 더하는 게 아니다 / easily deletes: 실수가 스스로 지우는 게 아니고 목적어도 없다\n포인트 ▶ need to be p.p. (~될 필요가 있다), 주어가 동작을 받으면 수동.",
    [['compose', '(글을) 쓰다'], ['need to be p.p.', '~될 필요가 있다'], ['delete', '삭제하다']])

T.fixed('글의 흐름으로 보아, 주어진 문장이 들어가기에 가장 적절한 곳은?', '38번', GIV(I7) + '\n' + BOX(
    I1 + ' ' + I2 + GP(1) + I3 + GP(2) + I4 + GP(3) + I5 + GP(4) + I6 + GP(5) + I8),
    None, 5,
    "이유 ▶ on the other hand(반면에) → 앞의 선형 편집 = 타자기(I5·I6)와 대조되는 비선형 편집 = 워드 프로그램. 뒤 문장 '실수하면 키 몇 번으로 지우고 고친다'(I8)는 워드 프로그램의 특징이므로 주어진 문장 바로 뒤에 와야 한다 → ⑤.\n오답 ▶ ①②③ 아직 선형 편집(타자기)이 나오기 전이라 대조할 대상이 없다 ④ 타자기 비유와 그 설명(I6) 사이를 끊는다\n포인트 ▶ on the other hand 앞뒤 대조 + 뒤 문장의 is made(현재) ↔ was made(과거) 시제 차이도 단서.",
    [['on the other hand', '반면에'], ['word processing program', '워드 프로그램']])

T.fixed('주어진 글 다음에 이어질 글의 순서로 가장 적절한 것은?', '38번', GIV(I1) + '\n' + BOX(
    '<b>(A)</b> ' + I2 + ' ' + I3 + ' ' + I4 + '</p><p><b>(B)</b> ' + I7 + ' ' + I8 + '</p><p><b>(C)</b> ' + I5 + ' ' + I6),
    ['(A) − (C) − (B)', '(B) − (A) − (C)', '(B) − (C) − (A)', '(C) − (A) − (B)', '(C) − (B) − (A)'], 1,
    "이유 ▶ 주어진 글: 모든 편집 시스템이 이제 비선형, 임의 접근 가능 → (A) Nonlinear systems ~ 특수 효과, Another highlight(또 다른 장점), 장면 추가·삭제 → (C) Linear editing은 타자기 같았다, 실수하면 전부 다시 → (B) on the other hand 비선형 편집은 워드 프로그램 같다.\n오답 ▶ (B)의 on the other hand는 (C)의 선형 편집과 대조하므로 (C) 뒤 / (A)의 Another highlight는 주어진 글의 장점(임의 접근)을 이어받는다\n포인트 ▶ Another(또 하나의)와 on the other hand(반면에)로 순서 잡기.",
    [['another', '또 다른'], ['linear', '선형의'], ['typewriter', '타자기']], en=False)

T.table('다음 글의 내용을 한 문장으로 요약할 때, 빈칸 (A), (B)에 들어갈 말로 가장 적절한 것은?', '38번', BOX(P38) + '\n' + SUM(
    'Unlike linear editing, which was as <b>(A)</b> ' + BL + ' as typing on a typewriter, nonlinear editing makes it <b>(B)</b> ' + BL + ' to find, add, or remove scenes.'),
    ['(A)', '(B)'], [['inconvenient', 'easy'], ['convenient', 'easy'], ['inconvenient', 'impossible'], ['creative', 'costly'], ['convenient', 'difficult']],
    "이유 ▶ (A) 타자기처럼 실수하면 전부 다시 쳐야 했다 → <i>inconvenient</i>(불편한) (B) 원하는 장면을 쉽게 찾고 쉽게 넣고 뺀다 → <i>easy</i>\n오답 ▶ convenient(편리한): 선형 편집과 반대 / impossible(불가능한)·difficult(어려운)·costly(비용이 많이 드는): 비선형 편집의 장점과 반대 / creative: 근거 없음\n포인트 ▶ Unlike A, B: A와 B는 반대 성질.",
    [['inconvenient', '불편한'], ['convenient', '편리한'], ['costly', '비용이 많이 드는']],
    ko=['불편한 / 쉬운', '편리한 / 쉬운', '불편한 / 불가능한', '창의적인 / 비용이 많이 드는', '편리한 / 어려운'])

T.flex('글에서 선형 편집과 비선형 편집을 각각 무엇에 비유했는지 바르게 짝지은 것은?', '38번', BOX(P38), [
    '타자기로 글쓰기 – 워드 프로그램 쓰기',
    '워드 프로그램 쓰기 – 타자기로 글쓰기',
    '비디오테이프 되감기 – 슬로 모션 만들기',
    '손으로 편지 쓰기 – 이메일 보내기',
    '타자기로 글쓰기 – 손으로 다시 쓰기'],
    "이유 ▶ Linear editing was like composing a paper on a typewriter(선형 편집 = 타자기로 글쓰기). Nonlinear editing, on the other hand, is like using a word processing program(비선형 편집 = 워드 프로그램 쓰기).\n오답 ▶ {1} 순서를 거꾸로 바꾼 함정 {2} 되감기와 슬로 모션은 비유가 아니라 실제 편집 이야기 {3} 편지·이메일은 나오지 않는다 {4} 비선형 편집은 다시 쓰지 않아도 된다\n포인트 ▶ like(~와 같은)로 연결된 비유 대상을 정확히 짝짓기.",
    [['be like', '~와 같다'], ['compose', '쓰다, 작성하다']], en=False)

# ── 39번 ──
T.flex('다음 글의 요지로 가장 적절한 것은?', '39번', BOX(P39), [
    '도덕적으로 선한 사람으로 여겨지려면 선한 의도뿐 아니라 실제 결과도 어느 정도 필요하다.',
    '사람을 판단할 때는 오직 행동의 결과만이 중요하다.',
    '선한 의도만 있으면 결과와 상관없이 선한 사람이다.',
    '슬랩스틱 영화는 사람들의 도덕적 판단에 큰 영향을 준다.',
    '칸트의 주장은 결과의 중요성에 대해 완전히 옳다.'],
    "이유 ▶ 의도와 동기가 중요하다(intentions and motives are relevant) + But actual consequences are important(하지만 실제 결과도 중요하다) → 선하다고 여겨지려면 어느 정도 결과가 필요하다(some results are necessary).\n오답 ▶ {1} 우연히 해를 막은 사람은 선하지 않다 — 결과만으로는 안 된다 {2} 늘 노력만 하고 한 번도 못 막은 사람은 선하다고 여겨지지 않는다 {3} 슬랩스틱 영화는 그런 상황이 드물다는 예 {4} contrary to Kant(칸트와 달리)\n포인트 ▶ 양쪽(의도만 X, 결과만 X)을 모두 부정하고 '둘 다'로 가는 글.",
    [['morally', '도덕적으로'], ['intention', '의도'], ['consequence', '결과'], ['contrary to', '~와 달리']], en=False)

T.flex('다음 빈칸에 들어갈 말로 가장 적절한 것은?', '39번 변형', BOX(
    J3 + ' ' + J4 + ' ' + J5 + ' But ' + BL + '. ' + J7 + ' ' + J8), [
    ('what our actions actually bring about also matters', '우리 행동이 실제로 가져오는 것도 중요하다'),
    ('intentions are all that count in moral judgment', '도덕적 판단에서는 의도만이 중요하다'),
    ('slapstick movies reflect real life accurately', '슬랩스틱 영화는 현실을 정확히 반영한다'),
    ('harm to others can never be prevented', '다른 사람에게 가는 해는 결코 막을 수 없다'),
    ('motives have nothing to do with being good', '동기는 선한 것과 아무 관계가 없다')],
    "이유 ▶ 원문: actual consequences are important. 앞에서 '결과만 중요하다는 잘못된 인상을 피하자'고 한 뒤 But으로 방향을 돌려 그래도 실제 결과는 중요하다 → 뒤 문장(노력만 하고 한 번도 못 막은 사람은 선하다고 여겨지지 않는다)이 근거.\n오답 ▶ {1} But 뒤에는 앞(의도가 중요)과 다른 내용이 와야 하고, 뒤 예시와도 반대 {2} 슬랩스틱 영화에서만 생기는 상황이라고 했다 {3} 해를 막지 못한 사람의 예일 뿐 일반화가 아니다 {4} 동기는 중요하다(relevant)고 했다\n포인트 ▶ bring about(가져오다) = 결과(consequences).",
    [['bring about', '가져오다, 일으키다'], ['count', '중요하다'], ['have nothing to do with', '~와 관계가 없다']])

T.flex('다음 글의 내용과 일치하지 <u>않는</u> 것은?', '39번', BOX(P39), [
    ('The writer believes good intentions alone make a person morally good.', '글쓴이는 선한 의도만으로 사람이 도덕적으로 선해진다고 믿는다.'),
    ('A morally good person does bad actions far less often than most people.', '도덕적으로 선한 사람은 대부분의 사람보다 나쁜 행동을 훨씬 덜 한다.'),
    ('Both actions and motives matter when we judge a person.', '사람을 판단할 때는 행동과 동기가 모두 중요하다.'),
    ('Someone who prevents harm only by accident is not morally good.', '우연히 해를 막았을 뿐인 사람은 도덕적으로 선하지 않다.'),
    ('The writer disagrees with Kant about whether results are needed.', '글쓴이는 결과가 필요한지에 대해 칸트와 생각이 다르다.')],
    "이유 ▶ 늘 해를 막으려 하지만 한 번도 막지 못한 사람은 선하다고 여겨지지 않고, 어느 정도 결과가 필요하다(some results are necessary) → 의도만으로 충분하다 ✗\n오답 ▶ {1} does morally bad actions significantly less often than most ✔ {2} not only her actions but also her intentions and motives are relevant ✔ {3} unintentionally prevents harm ~ is not morally good ✔ {4} contrary to Kant, some results are necessary ✔\n포인트 ▶ contrary to Kant → 칸트는 의도만으로 충분하다고 본다는 뜻(글쓴이와 반대).",
    [['far less often', '훨씬 덜 자주'], ['by accident', '우연히'], ['disagree with', '~와 의견이 다르다']])

T.fixed('다음 글의 밑줄 친 부분 중, 문맥상 낱말의 쓰임이 적절하지 <u>않은</u> 것은?', '39번 변형', BOX(
    "A morally good person is one who does morally bad actions significantly " + CN(1, 'less') + " often than most and does morally good ones significantly more often than most. In judging a person not only her actions but also her intentions and motives are " + CN(2, 'irrelevant') + ". " + J3 + " A person who " + CN(3, 'unintentionally') + " prevents harm to others and does not harm them simply because things do not turn out as she intends is not morally good. Although this kind of situation generally occurs only in slapstick movies, it is worth mentioning to avoid the " + CN(4, 'false') + " impression that it is the actual consequences of a person's actions that count toward her being judged morally good or bad. " + J6 + ' ' + J7 + " Of such a person, it may be said that she means well; but, contrary to Kant, some results are " + CN(5, 'necessary') + " before she is regarded as morally good."),
    ['less', 'irrelevant', 'unintentionally', 'false', 'necessary'], 2,
    "이유 ▶ 바로 다음 문장에서 선한 사람은 선한 행동을 '의도해야' 한다고 하므로, 의도와 동기는 판단에 '관련 있다(중요하다)' → <i>relevant</i>. irrelevant(관련 없는)는 반대.\n오답 ▶ ① 나쁜 행동을 대부분보다 '덜' 한다 ✔ ③ '의도치 않게' 해를 막은 사람은 선하지 않다 ✔ ④ 결과만 중요하다는 것은 '잘못된' 인상 ✔ ⑤ 선하다고 여겨지려면 어느 정도 결과가 '필요하다' ✔\n포인트 ▶ not only A but also B 구문의 주장(행동뿐 아니라 의도도)과 다음 문장(must intend)이 연결.",
    [['relevant', '관련 있는'], ['irrelevant', '관련 없는'], ['unintentionally', '의도치 않게'], ['impression', '인상']])

T.fixed('다음 글의 밑줄 친 부분 중, 어법상 <u>틀린</u> 것은?', '39번 변형', BOX(
    "In " + CN(1, 'judging') + " a person not only her actions but also her intentions and motives are relevant. A morally good person must intend to do morally good actions and intend " + CN(2, 'to avoid') + " morally bad ones. A person who unintentionally prevents harm to others and does not harm them simply because things do not turn out as she intends " + CN(3, 'are') + " not morally good. Although this kind of situation generally occurs only in slapstick movies, it is worth " + CN(4, 'mentioning') + ". … A person who always tries to prevent harm but never does, is not generally " + CN(5, 'thought') + " of as morally good."),
    ['judging', 'to avoid', 'are', 'mentioning', 'thought'], 3,
    "이유 ▶ 주어는 A person(단수), who ~ intends까지는 관계절 수식어 → <i>is</i>.\n오답 ▶ ① 전치사 In + 동명사(사람을 판단할 때) ✔ ② intend to V(~할 작정이다) ✔ ④ be worth -ing(~할 가치가 있다) ✔ ⑤ think of A as B의 수동태 be thought of as ✔\n포인트 ▶ 긴 관계절(who ~ intends)이 끼어도 주어(A person)를 찾아 수 일치.",
    [['intend to V', '~할 작정이다'], ['turn out', '(결과가) ~이 되다'], ['be worth -ing', '~할 가치가 있다']])

T.table('(A), (B), (C)의 각 네모 안에서 어법에 맞는 표현으로 가장 적절한 것은?', '39번', BOX(
    "A morally good person is one who does morally bad actions significantly <b>(A)</b> [ less / fewer ] often than most and does morally good ones significantly more often than most. … Although this kind of situation generally occurs only in slapstick movies, it is worth <b>(B)</b> [ mentioning / to mention ] to avoid the false impression that it is the actual consequences of a person's actions that count toward her being judged morally good or bad. … Of such a person, it may be said that she means well; but, contrary to Kant, some results are necessary before she <b>(C)</b> [ is regarded / regards ] as morally good."),
    ['(A)', '(B)', '(C)'], [['less', 'mentioning', 'is regarded'], ['fewer', 'mentioning', 'is regarded'], ['less', 'to mention', 'is regarded'], ['less', 'mentioning', 'regards'], ['fewer', 'to mention', 'regards']],
    "이유 ▶ (A) 부사 often을 꾸미는 비교급 → <i>less</i> often (fewer는 셀 수 있는 명사 앞) (B) be worth -ing → <i>mentioning</i> (C) 그녀가 선하다고 '여겨지는' 수동 regard A as B → <i>is regarded</i> as\n오답 ▶ fewer: 명사가 아니라 부사(often)를 꾸민다 / to mention: worth 뒤에는 동명사 / regards: 목적어가 없으므로 수동\n포인트 ▶ less often(덜 자주) ↔ more often(더 자주).",
    [['fewer + 복수명사', '더 적은 수의'], ['less', '덜'], ['regard A as B', 'A를 B로 여기다']])

T.fixed('글의 흐름으로 보아, 주어진 문장이 들어가기에 가장 적절한 곳은?', '39번', GIV(J6) + '\n' + BOX(
    J2 + GP(1) + J3 + GP(2) + J4 + GP(3) + J5 + GP(4) + J7 + GP(5) + J8),
    None, 4,
    "이유 ▶ 앞에서 '결과만 중요하다는 잘못된 인상을 피하자'(J5)고 한 뒤, But(하지만) 실제 결과도 중요하다 → 그 예로 늘 노력하지만 한 번도 해를 막지 못한 사람은 선하다고 여겨지지 않는다(J7). ④.\n오답 ▶ ①②③ 아직 의도의 중요성을 설명하는 중이라 But으로 뒤집을 내용(결과만 중요하다는 잘못된 인상)이 나오기 전 ⑤ J7의 예시가 근거 없이 먼저 나온다\n포인트 ▶ 의도 강조(J2~J5) → But 결과도 중요(주어진 문장) → 예시(J7·J8).",
    [['actual', '실제의'], ['consequence', '결과']])

T.flex('밑줄 친 <u>she means well</u>이 의미하는 바로 가장 적절한 것은?', '39번', BOX(P39.replace('she means well', U('she means well'))), [
    ('She has good intentions.', '그녀는 좋은 의도를 가지고 있다.'),
    ('She always succeeds in helping others.', '그녀는 늘 다른 사람을 돕는 데 성공한다.'),
    ('She is skilled at preventing harm.', '그녀는 해를 막는 데 능숙하다.'),
    ('She intends to hurt others.', '그녀는 다른 사람을 해칠 작정이다.'),
    ('She explains her ideas clearly.', '그녀는 자기 생각을 분명하게 설명한다.')],
    "이유 ▶ mean well = 선의를 가지다(좋은 뜻으로 하다). such a person = 늘 해를 막으려 하지만(always tries) 한 번도 못 막는 사람 → 의도는 좋다.\n오답 ▶ {1}·{2} 한 번도 막지 못했다(never does) {3} 반대 {4} mean을 '설명하다, 의미하다'로 직역한 함정\n포인트 ▶ she means well; but ~ (의도는 좋지만, 결과도 필요하다).",
    [['mean well', '선의를 가지다'], ['skilled', '능숙한'], ['intend', '의도하다']])

T.table('다음 글의 내용을 한 문장으로 요약할 때, 빈칸 (A), (B)에 들어갈 말로 가장 적절한 것은?', '39번', BOX(P39) + '\n' + SUM(
    'Judging whether a person is morally good requires considering both her <b>(A)</b> ' + BL + ' and the actual <b>(B)</b> ' + BL + ' of her actions.'),
    ['(A)', '(B)'], [['intentions', 'results'], ['appearance', 'results'], ['intentions', 'speed'], ['wealth', 'costs'], ['appearance', 'speed']],
    "이유 ▶ (A) 의도와 동기도 중요하다 → <i>intentions</i>(의도) (B) 실제 결과도 중요하다 → <i>results</i>(결과)\n오답 ▶ appearance(외모)·wealth(재산): 본문에 없다 / speed(속도)·costs(비용): 행동의 '결과'와 다르다\n포인트 ▶ 의도(intentions, motives) + 결과(consequences, results) — 이 글의 두 기준.",
    [['consider', '고려하다'], ['appearance', '외모'], ['result', '결과']],
    ko=['의도 / 결과', '외모 / 결과', '의도 / 속도', '재산 / 비용', '외모 / 속도'])

# ── 종합 ──
T.fixed('다음 (a)~(g) 중 어법상 <u>틀린</u> 것의 개수는?', '종합', BOX(
    "(a) Nonlinear systems allow random access to any scene without " + U('having') + " to fast forward.<br>(b) Its random access process makes " + U('it') + " easy for an editor to find desired shots.<br>(c) If a mistake was made, the whole piece had to " + U('retype') + ".<br>(d) Not only her actions but also her intentions " + U('are') + " relevant.<br>(e) A person who always tries to prevent harm but never does " + U('is') + " not thought of as morally good.<br>(f) It is the actual consequences of a person's actions that " + U('counts') + ".<br>(g) Nonlinear editing is like " + U('use') + " a word processing program."),
    ['1개', '2개', '3개', '4개', '5개'], 3,
    "이유 ▶ 틀린 것 (c) (f) (g) 3개. (c) 글이 '다시 쳐져야' 하는 수동 → <i>be retyped</i> (f) It is ~ that 강조 구문, 강조된 주어 the actual consequences(복수) → <i>count</i> (g) 전치사 like 뒤 → 동명사 <i>using</i>\n오답 ▶ (a) without + 동명사 ✔ (b) 가목적어 it ✔ (d) not only A but also B → B(intentions)에 일치 ✔ (e) 주어 A person → is ✔\n포인트 ▶ It is A that ~ 강조 구문: that 뒤 동사는 A에 수 일치.",
    [['have to be p.p.', '~되어야 한다'], ['It is A that ~', 'A가 바로 ~이다 (강조)'], ['be like -ing', '~하는 것과 같다']], en=False)

T.render()
