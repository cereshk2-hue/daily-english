from jfw import *
p = load(22, '22번 · 글의 요지')
VOCAB = words(22, add=[("norm", "기준, 규범"), ("routine", "일상적인; 일과")])
EXAM = [EXQ(22, '22. 다음 글의 요지로 가장 적절한 것은?', p.full(), [
 "시간은 희소한 자원이며 기회비용을 갖는다.", "시간의 절대성은 자연 과학의 전제 조건이다.", "시간의 효율적 활용은 삶에 균형을 가져다준다.",
 "시간의 흐름은 심리 상태에 따라 다르게 인식된다.", "시간을 인식하고 사용하는 방식은 사회적인 산물이다."], 4,
 "정답 ▶ ⑤ 시간을 인식하고 사용하는 방식은 사회적인 산물이다.\n이유: how we perceive and understand time is to a large degree shaped by tradition and cultural norms + 마지막 문장 These numbers and patterns ~ are rather social creations. 일주일·9시~5시 근무·월말 납부·65세 은퇴 모두 사회가 만든 것\n오답 ▶ ① 희소성·기회비용은 경제학 이야기 ② 자연의 기본 속성이 '아니라'고 함 ③ 효율적 활용 이야기 없음 ④ 개인의 심리 현상도 '아니라'고 함(nor are they simply psychological phenomena)\n포인트 ▶ not A nor B, Instead C → C가 요지", v=False),
 EXQ(22, '다음 글의 주제로 가장 적절한 것은?', p.full(), [
 "social and cultural shaping of how we perceive time", "scientific methods for measuring time accurately", "psychological effects of a busy work schedule",
 "historical reasons for the decline of the seven-day week", "benefits of retiring earlier than sixty-five"], 0,
 "정답 ▶ ① 우리가 시간을 인식하는 방식이 사회·문화적으로 형성되는 것\n이유: shaped by tradition and cultural norms / a social invention / social creations\n오답 ▶ ② 정확한 측정법 ✗ ③ 바쁜 일정의 심리 효과 ✗ ④ 일주일이 쇠퇴한다는 말 없음 ⑤ 은퇴 나이는 예시일 뿐\n포인트 ▶ shape = 형성하다 · perceive = 인식하다"),
 EXQ(22, '다음 빈칸에 들어갈 말로 가장 적절한 것은?', p.blank('social creations'), [
 "social creations", "natural laws", "personal feelings", "scientific facts", "biological needs"], 0,
 "정답 ▶ ① social creations (사회적 창조물)\n이유: but are rather ~ 앞에서 '자연이나 인간의 본질적 특성에 의해 좌우되는 게 아니다'라고 했으니, 그 반대인 '사회가 만든 것'. 앞의 a social invention과도 연결\n오답 ▶ ② 자연 법칙 ⑤ 생물학적 필요 → nature와 같은 쪽 ③ 개인적 감정 → 심리 현상(부정됨) ④ 과학적 사실\n포인트 ▶ not A but rather B")]
PICK1 = [PK(p, 'Sociologists argue', 'basic', 'rare', "정답 ▶ basic (기본적인)\n오답 ▶ rare (드문)\n이유: 시계처럼 배경에서 흘러가는 자연의 '기본' 속성이 아니라는 뜻"),
 PK(p, 'Instead, how', 'cultural', 'physical', "정답 ▶ cultural (문화적인)\n오답 ▶ physical (물리적인)\n이유: 전통과 '문화적' 기준에 의해 형성됨 → 사회적 산물이라는 요지"),
 PK(p, 'Eviatar', 'invention', 'discovery', "정답 ▶ invention (발명품)\n오답 ▶ discovery (발견)\n이유: 일주일은 자연에 원래 있던 것을 '발견'한 게 아니라 사회가 '만든' 것"),
 PK(p, 'Eviatar', 'varies', 'remains', "정답 ▶ varies (다르다)\n오답 ▶ remains (그대로이다)\n이유: 사회가 만든 것이라서 문화마다(across cultures) '다르다'"),
 PK(p, 'These numbers', 'essential', 'artificial', "정답 ▶ essential (본질적인)\n오답 ▶ artificial (인위적인)\n이유: 인간의 '본질적' 특성으로 정해진 게 아니라 사회적 창조물이라는 대조"),
 PK(p, 'These numbers', 'internalize', 'reject', "정답 ▶ internalize (내면화하다)\n오답 ▶ reject (거부하다)\n이유: 결국 '정상'으로 받아들이게 되니(come to accept) 우리 안에 '내면화'한 것")]
TF = [TF(p, "Sociologists say our use of time is simply a basic property of nature.", False, "are not just basic properties of nature", "정답 ▶ F\n이유: 단순히 자연의 기본 속성이 아니라고 해요."),
 TF(p, "According to the passage, tradition and cultural norms largely shape how we understand time.", True, "to a large degree shaped by tradition and cultural norms", "정답 ▶ T\n이유: 시간을 이해하는 방식은 상당 부분 전통과 문화적 기준이 형성해요.\n어휘 ▶ largely = to a large degree"),
 TF(p, "Zerubavel’s work shows that the week is the same in every culture.", False, "a social invention that varies across cultures", "정답 ▶ F\n이유: 일주일은 문화마다 다른 사회적 발명품이에요."),
 TF(p, "The week influences how people organize their activities.", True, "influencing how people structure their activities", "정답 ▶ T\n이유: 사람들이 활동과 삶의 리듬을 구조화하는 방식에 영향을 줘요.\n어휘 ▶ organize ≒ structure"),
 TF(p, "The retirement age of sixty-five is decided by human nature.", False, "aren’t really dictated by nature or any essential human characteristic", "정답 ▶ F\n이유: 이런 숫자는 자연이나 인간의 본질적 특성이 정한 게 아니에요."),
 TF(p, "We come to accept social patterns as normal.", True, "come to accept as “normal.”", "정답 ▶ T\n이유: 사회적 창조물을 내면화하여 결국 '정상'으로 받아들이게 돼요.")]
MC = [MC(p, "글의 내용과 일치하지 <u>않는</u> 것은?", [
 "Our perception of time is purely an individual psychological experience.", "Cultural norms play a big role in how we understand time.", "The week is a basic unit of time created by society.",
 "Working from nine to five is a pattern society has made.", "People accept social time patterns as normal."],
 "정답 ▶ Our perception of time is purely an individual psychological experience.\n이유: nor are they simply psychological phenomena of individual experience\n포인트 ▶ purely ≒ simply · created by society = a social invention · basic = fundamental",
 [["시간 인식은 순전히 개인의 심리적 경험이다.", "nor are they simply psychological phenomena of individual experience", "✗ 아님"], ["문화적 기준은 시간 이해에 큰 역할을 한다.", "shaped by tradition and cultural norms", "일치"], ["일주일은 사회가 만든 시간의 기본 단위이다.", "a fundamental unit of time, is a social invention", "basic = fundamental"], ["9시~5시 근무는 사회가 만든 양식이다.", "social creations", "일치"], ["사람들은 사회적 시간 양식을 정상으로 받아들인다.", "come to accept as “normal.”", "일치"]]),
 MC(p, "글의 내용과 <u>일치하는</u> 것은?", ["일주일이라는 단위는 문화마다 다르다.", "시간 인식은 자연이 정한 기본 속성이다.", "월말 납부는 인간의 본능에서 나왔다.", "Zerubavel은 시계의 역사를 연구했다.", "은퇴 나이는 생물학적으로 정해진다."],
 "정답 ▶ 일주일이라는 단위는 문화마다 다르다.\n이유: a social invention that varies across cultures\n오답 ▶ ② 자연의 기본 속성이 아님 ③⑤ 본질적 특성이 정한 게 아님 ④ 일주일의 역사와 의미를 다룬 책",
 [["", "varies across cultures", "일치 ✔"], ["", "not just basic properties of nature", "자연 속성 아님"], ["", "aren’t really dictated by nature", "본능 아님"], ["", "The History and Meaning of the Week", "일주일"], ["", "any essential human characteristic", "생물학 아님"]])]
PICK2 = [PK(p, 'Sociologists argue', 'ticking', 'ticked', "정답 ▶ ticking\n이유: 시계가 '째깍거리며 흘러가는' 능동 → 현재분사가 a clock 수식"),
 PK(p, 'Sociologists argue', 'nor are they', 'nor they are', "정답 ▶ nor are they\n이유: 부정어 nor가 앞에 오면 주어·동사 도치 (nor + 동사 + 주어)"),
 PK(p, 'Instead, how', 'how we perceive', 'the way how we perceive', "정답 ▶ how\n이유: the way와 how는 함께 쓰지 않아요 (the way 또는 how 하나만)"),
 PK(p, 'Instead, how', 'is to a large', 'are to a large', "정답 ▶ is\n이유: 의문사절(how we perceive and understand time) 주어는 단수 취급"),
 PK(p, 'Instead, how', 'shaped', 'shaping', "정답 ▶ shaped\n이유: 방식이 전통에 의해 '형성되는' 수동 → is shaped by"),
 PK(p, 'Eviatar', 'varies', 'vary', "정답 ▶ varies\n이유: 주격 관계대명사 that의 선행사 a social invention(단수) → varies"),
 PK(p, 'These numbers', 'dictated', 'dictating', "정답 ▶ dictated\n이유: 숫자와 양식이 자연에 의해 '좌우되는' 수동 → aren’t dictated by")]
VERB = [VB(p, 'Eviatar', 'influencing', 'influence', "정답 ▶ influencing\n이유: 콤마 뒤 분사구문 — 일주일이 '영향을 주면서'(능동)"),
 VB(p, 'Why don’t', 'work', 'work', "정답 ▶ work\n이유: don’t + 동사원형"),
 VB(p, 'These numbers', 'to accept', 'accept', "정답 ▶ to accept\n이유: come + to부정사(~하게 되다) → to accept")]
VERB = [v for v in VERB if v['v'] != v['a'][0]]
ERR = [ER(p, 'Sociologists argue', ['that', 'ticking', ('are they', 'they are')], 2, 'are they', "틀린 곳 ▶ ③ they are → are they\n이유: 부정어 nor 뒤 도치\n나머지 ▶ ① 명사절 접속사 that ✔ ② 현재분사(능동) ✔"),
 ER(p, 'Instead, how', ['how', 'is', ('shaped', 'shaping')], 2, 'shaped', "틀린 곳 ▶ ③ shaping → shaped\n이유: 형성'되는' 수동 (by tradition)\n나머지 ▶ ① how ✔ ② 명사절 주어 단수 ✔"),
 ER(p, 'These numbers', [('dictated', 'dictating'), 'that', 'accept'], 0, 'dictated', "틀린 곳 ▶ ① dictating → dictated\n이유: 자연에 의해 좌우'되는' 수동\n나머지 ▶ ② 목적격 관계대명사 that ✔ ③ come to + 동사원형 ✔")]
SCR = [0, 1, 2, 7]
ORDER = [[0, 1, 2, 3], [3, 4, 5, 6, 7]]
INSERT = [([0, 1, 2, 3], 1, "정답 ▶ ① (Instead ~ 문장)\n이유: 자연의 속성도, 개인의 심리 현상도 아니다(부정) → Instead(오히려) 전통과 문화가 형성한다(진짜 답) → 그 예로 Zerubavel의 책"),
 ([4, 5, 6, 7], 3, "정답 ▶ ③ (These numbers ~ 문장)\n이유: 질문(주말·월말·65세)들 바로 뒤에 These numbers and patterns(이 숫자와 양식들)로 질문들을 묶어 답해요.")]
ODD = [([1, 2, "Many scientists measure time very precisely using atomic clocks.", 3], 2, "정답 ▶ ③\n이유: 시간 인식이 사회·문화적으로 형성된다는 흐름이에요. 원자시계로 정밀하게 측정한다는 과학 이야기는 관계없어요.")]
BLANK = [BL(p, 'Instead, how', 'tradition', ["gravity", "instinct", "weather"], "정답 ▶ tradition (전통)\n이유: cultural norms와 짝 → 사회적 요인\n오답 ▶ gravity 중력 · instinct 본능 · weather 날씨 → 자연·본능 쪽(부정되는 쪽)"),
 BL(p, 'Eviatar', 'across cultures', ["over the years", "in nature", "by accident"], "정답 ▶ across cultures (문화마다)\n이유: 사회적 발명품이라 문화에 따라 다름\n오답 ▶ over the years 해마다 · in nature 자연에서 · by accident 우연히"),
 BL(p, 'These numbers', 'normal', ["strange", "natural", "unfair"], "정답 ▶ normal (정상, 보통)\n이유: 사회가 만든 것을 내면화해서 결국 '정상'이라 받아들임\n오답 ▶ strange 이상한 · natural 자연스러운(자연이 정한 게 아니라고 했음) · unfair 불공평한")]
GRAM = [{'q': "빈칸에 알맞은 것은?<br><b>It is not a basic property of nature, nor ______ a psychological phenomenon.</b>", 'opts': ["is it", "it is", "it does", "does it"], 'ex': "정답 ▶ is it\n이유: nor + (be)동사 + 주어 도치. 앞이 is이므로 is it"},
 {'q': "빈칸에 알맞은 것은?<br><b>______ we perceive time is shaped by cultural norms.</b>", 'opts': ["How", "The way how", "What", "Which"], 'ex': "정답 ▶ How\n이유: the way how ✗. 뒤가 완전한 절 → How(~하는 방식). What은 불완전한 절"},
 {'q': "빈칸에 알맞은 것은?<br><b>The week is a social invention that ______ across cultures.</b>", 'opts': ["varies", "vary", "varying", "to vary"], 'ex': "정답 ▶ varies\n이유: 관계대명사 that의 선행사 invention(단수)"},
 {'q': "빈칸에 알맞은 것은?<br><b>We internalize these patterns and come ______ them as normal.</b>", 'opts': ["to accept", "accepting", "accept", "accepted"], 'ex': "정답 ▶ to accept\n이유: come + to부정사 = ~하게 되다"}]
SUMQ = [SUM(p, "The way we perceive and use time is not (A) ______ by nature but is a product of society that differs across (B) ______.", [
 "(A) determined – (B) cultures", "(A) determined – (B) individuals", "(A) ignored – (B) cultures", "(A) measured – (B) seasons", "(A) shared – (B) species"],
 "정답 ▶ (A) determined – (B) cultures\n(A) 자연에 의해 '정해지는(dictated)' 게 아니다 → determined\n(B) 문화마다 다르다(varies across cultures) → cultures\n오답 ▶ individuals: 개인의 심리 현상도 아니라고 했어요.",
 ["aren’t really dictated by nature", "varies across cultures"])]
