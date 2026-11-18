# 9월 모평 DAY 26~33 : 18 목적 → 20 주장 → 19 심경 → 22 요지 → 26 인물 불일치 → 23 주제 → 27 안내문 → 24 제목  (gen_h3s9.py 안에서 exec)

# ═══ 18번 목적 ═══
T18 = [
 ("Dear Mr. Steve Carter,", "Steve Carter 씨께,"),
 ("Congratulations on the 60th graduation ceremony of Yuoralis High School.", "Yuoralis 고등학교의 제60회 졸업식을 축하합니다."),
 ("As a former student, I am extremely proud that the school has become one of the best schools in the local community.", "졸업생으로서, 저는 우리 학교가 지역 사회에서 가장 훌륭한 학교 중 하나가 된 것이 대단히 자랑스럽습니다."),
 ("I felt honored when I received your kind invitation to deliver a speech at the ceremony.", "졸업식에서 연설을 해 달라는 귀하의 친절한 초청을 받았을 때 저는 영광스러웠습니다."),
 ("However, I am deeply sorry to say that I will not be able to give a speech because I have a very important overseas business trip scheduled during that time.", "하지만, 그 기간에 아주 중요한 해외 출장이 예정되어 있어서 연설을 할 수 없을 것이라는 말씀을 드리게 되어 진심으로 죄송합니다."),
 ("I would have loved to speak to the graduating students, but I must decline your invitation to this meaningful celebration.", "졸업하는 학생들에게 연설을 정말 하고 싶었지만, 이 의미 있는 축하 행사에 대한 귀하의 초청을 거절할 수밖에 없습니다."),
 ("I wish you a memorable graduation ceremony.", "기억에 남는 졸업식이 되기를 기원합니다."),
 ("Sincerely, Jane Whittmore", "Jane Whittmore 드림"),
]
day(18, 'q18', '목적', '글의 목적 · However 뒤의 본론 찾기', '다음 글의 목적으로 가장 적절한 것은?', T18,
 ['졸업식 일정을 문의하려고', '졸업식 연설 초청을 거절하려고', '졸업식 자원 봉사를 지원하려고', '졸업식의 미흡했던 점을 지적하려고', '졸업식에서 공연할 팀을 추천하려고'], 1,
 '앞부분은 졸업식 축하와 초청을 받아 영광이라는 인사예요. However(하지만)로 본론이 시작돼요: 해외 출장 때문에 연설을 할 수 없다(I will not be able to give a speech) → 초청을 거절할 수밖에 없다(I must decline your invitation). 그래서 정답은 ② 졸업식 연설 초청을 거절하려고.',
 ['① 졸업식 일정을 묻는 말은 없어요. (during that time은 이미 아는 일정이에요)',
  '③ 자원 봉사 이야기는 나오지 않아요.',
  '④ 졸업식의 미흡한 점을 지적하지 않아요. 오히려 학교가 자랑스럽다고 해요.',
  '⑤ 공연 팀 추천은 나오지 않아요.'],
 '목적 문제는 앞의 인사·칭찬은 건너뛰고 However, Unfortunately 같은 전환어 뒤를 보세요. decline(거절하다), be unable to 같은 말이 목적을 그대로 알려 줘요.',
 [(T18[3][0], T18[3][1], "feel honored 영광스럽게 느끼다 · invitation to + 동사원형 ~해 달라는 초청 (to부정사가 invitation을 꾸밈)"),
  (T18[4][0], T18[4][1], "be sorry to say that ~ ~라고 말씀드리게 되어 죄송하다 · have + O + p.p.(a trip scheduled) 출장이 예정되어 있다"),
  (T18[5][0], T18[5][1], "would have loved to ~ ~하고 싶었다(하지만 못 함, 가정법 과거완료 느낌) · must decline 거절할 수밖에 없다")],
 [('graduation ceremony', '졸업식'), ('former student', '졸업생, 이전 학생'), ('extremely', '대단히, 매우'), ('proud', '자랑스러운'), ('local community', '지역 사회'),
  ('honored', '영광스러운'), ('invitation', '초대(장), 초청'), ('deliver a speech', '연설하다'), ('deeply', '진심으로, 깊이'), ('overseas business trip', '해외 출장'),
  ('scheduled', '예정된'), ('graduating', '졸업하는'), ('decline', '거절하다'), ('meaningful', '의미 있는'), ('celebration', '축하 행사'), ('memorable', '기억에 남는')],
 ['extremely', 'proud', 'honored', 'invitation', 'deeply', 'scheduled', 'graduating', 'decline', 'meaningful', 'celebration', 'memorable'],
 paras=[esc(T18[0][0]), ' '.join(esc(e) for e, k in T18[1:7]), 'Sincerely,<br>Jane Whittmore'])

# ═══ 20번 주장 ═══
T20 = [
 ("Current social changes driven by technological advancements demand a fundamental rethinking in our approach to education.", "기술 발전에 따른 현재의 사회 변화는 교육에 대한 우리의 접근 방식에 있어서 근본적인 재고를 요구한다."),
 ("In particular, lifelong learning is no longer optional; it is essential.", "특히, 평생학습은 더 이상 선택적인 것이 아니라 필수적이다."),
 ("We must recognize that the rapidly evolving socioeconomic ecology requires individuals to engage in constant upskilling and self-transformation.", "우리는 빠르게 변화하고 있는 사회경제적 생태계가 개인들에게 끊임없는 기술 향상과 자기 혁신에 참여할 것을 요구한다는 점을 인식해야 한다."),
 ("If we can enhance lifelong learning initiatives, we will not only promote personal growth and well-being but also sustain national productivity and global competitiveness.", "만일 우리가 평생학습 계획을 강화할 수 있다면, 우리는 개인의 성장과 행복을 증진할 뿐만 아니라 국가 생산성과 글로벌 경쟁력을 유지할 것이다."),
 ("Furthermore, our efforts will support social integration by providing opportunities for people from various backgrounds to connect and move on together.", "게다가, 우리의 노력은 다양한 배경을 가진 사람들이 연결되고 함께 나아갈 수 있는 기회를 제공함으로써 사회적 통합을 지원할 것이다."),
 ("Investing in lifelong education thus is not simply an extra expense; we must consider it a necessity for survival and success as we encounter significant changes in the years ahead.", "따라서 평생교육에 투자하는 것은 단순한 추가 비용이 아니며, 우리는 앞으로 다가올 수년간 중대한 변화에 직면하면서 그것을 생존과 성공을 위한 필수 요소로 여겨야 한다."),
 ("By prioritizing lifelong education, we will be able to navigate this changing world with confidence and a sense of fulfillment.", "평생교육을 우선시함으로써, 우리는 자신감과 성취감을 가지고 이 변화하는 세상을 헤쳐 나갈 수 있을 것이다."),
]
day(20, 'q20', '주장', '필자의 주장 · must가 반복되는 말을 묶기', '다음 글에서 필자가 주장하는 바로 가장 적절한 것은?', T20,
 ['변화하는 사회에 대응하기 위해 평생교육을 강화해야 한다.', '융합 교육을 통해 미래 사회의 인재를 적극 육성해야 한다.', '경제 교육을 강화하여 투자에 대한 바른 인식을 갖도록 해야 한다.', '기술 발전을 위해 특정 분야의 전문 지식 습득을 장려해야 한다.', '평생교육 기관을 설립하여 사회의 균형 발전을 도모해야 한다.'], 0,
 '첫 문장: 기술 발전에 따른 사회 변화가 교육에 대한 재고를 요구한다. 바로 다음: 평생학습은 더 이상 선택이 아니라 필수다(no longer optional; it is essential). 이어서 must recognize, enhance lifelong learning initiatives, must consider it a necessity, prioritizing lifelong education이 계속 반복돼요. → 변화하는 사회에 대응하려면 평생교육을 강화해야 한다 = ①.',
 ['② 융합(통합) 교육은 나오지 않아요. social integration(사회적 통합)은 평생교육의 ‘효과’일 뿐이에요.',
  '③ Investing(투자)이 나오지만 ‘평생교육에 투자하는 것’이지 경제·투자 교육이 아니에요. (단어 함정)',
  '④ 특정 분야의 전문 지식이 아니라 평생 동안 계속 배우는 것(constant upskilling)이에요.',
  '⑤ 평생교육 ‘기관 설립’은 나오지 않아요. 글에 없는 구체적인 방법을 덧붙인 오답이에요.'],
 '주장 문제는 must, should, need to가 붙은 문장을 모아 보세요. 여러 번 반복되는 핵심어(lifelong learning/education)가 들어간 선택지 중, 글에 없는 내용(기관 설립)을 덧붙이지 않은 것을 고르세요.',
 [(T20[1][0], T20[1][1], "no longer 더 이상 ~이 아닌 · 세미콜론(;) 뒤에 반대되는 말(optional ↔ essential)"),
  (T20[3][0], T20[3][1], "not only A but also B A뿐만 아니라 B도 (A = promote ~, B = sustain ~ 동사끼리 병렬)"),
  (T20[5][0], T20[5][1], "동명사 주어 Investing ~ is · consider + O + 명사(a necessity) ~을 …로 여기다 · as ~하면서")],
 [('advancement', '발전'), ('demand', '요구하다'), ('fundamental', '근본적인'), ('rethinking', '재고, 다시 생각함'), ('lifelong learning', '평생학습'), ('optional', '선택적인'),
  ('essential', '필수적인'), ('evolving', '변화하는, 진화하는'), ('socioeconomic', '사회경제적인'), ('engage in', '~에 참여하다'), ('upskilling', '기술 향상'), ('enhance', '강화하다'),
  ('initiative', '계획, 제도'), ('sustain', '유지하다'), ('productivity', '생산성'), ('competitiveness', '경쟁력'), ('integration', '통합'), ('expense', '비용'),
  ('necessity', '필수 요소'), ('prioritize', '우선시하다'), ('navigate', '헤쳐 나가다'), ('fulfillment', '성취감')],
 ['fundamental', 'optional', 'essential', 'evolving', 'enhance', 'initiative', 'sustain', 'productivity', 'integration', 'necessity', 'prioritize', 'navigate'])

# ═══ 19번 심경 변화 ═══
T19 = [
 ("On her way to school, Katie thought of the argument she had with Sarah the day before and wiped tears from her eyes.", "학교로 가는 길에, Katie는 전날 Sarah와 했던 다툼을 떠올리며 눈물을 닦았다."),
 ("“I can’t believe I fought with my best friend,” she cried.", "“내가 가장 친한 친구와 싸웠다니 믿을 수 없어.”라고 그녀는 울먹였다."),
 ("“I just want things to go back to normal.”", "“난 그저 모든 게 예전으로 돌아가길 바랄 뿐이야.”"),
 ("It seemed that nothing could help her overcome this painful moment.", "어떤 것도 그녀가 이 고통스러운 순간을 극복하도록 도울 수 없을 것 같았다."),
 ("As she walked into her classroom, she heard a familiar voice.", "교실로 걸어 들어갔을 때, 그녀는 익숙한 목소리를 들었다."),
 ("Sarah was calling her name.", "Sarah가 그녀의 이름을 부르고 있었다."),
 ("“Katie, I’m sorry for the things I said yesterday.”", "“Katie, 어제 내가 했던 말들에 대해 미안해.”"),
 ("A big smile spread across Katie’s face.", "Katie의 얼굴에 환한 미소가 번졌다."),
 ("“I’m sorry, too. Let’s never fight again.”", "“나도 미안해. 우리 다시는 싸우지 말자.”"),
 ("Katie and Sarah hugged each other tightly and laughed the way they always did before.", "Katie와 Sarah는 서로를 꽉 껴안고 예전에 늘 그랬던 것처럼 함께 웃었다."),
]
day(19, 'q19', '심경 변화', '심경 변화 · 눈물(tears) → 미소(smile) 행동 묘사 잡기', '다음 글에 드러난 Katie의 심경 변화로 가장 적절한 것은?', T19,
 ['nervous → frustrated', 'sad → delighted', 'excited → calm', 'bored → happy', 'hopeful → disappointed'], 1,
 '앞: 친구와의 다툼을 떠올리며 눈물을 닦고(wiped tears) 울먹임(cried), 고통스러운 순간(painful moment) → 슬픔(sad). 뒤: Sarah가 사과하자 환한 미소가 번지고(A big smile spread) 꽉 껴안고 웃음(hugged, laughed) → 기쁨(delighted). 그래서 ② sad → delighted.',
 ['① nervous(긴장한) → frustrated(좌절한): 끝에 화해하고 웃으니 좌절이 아니에요.',
  '③ excited(신난) → calm(차분한): 처음에 울고 있었으니 신난 상태가 아니에요.',
  '④ bored(지루한) → happy(행복한): 뒤는 맞지만, 앞은 지루함이 아니라 슬픔이에요. (반만 맞는 함정)',
  '⑤ hopeful(희망에 찬) → disappointed(실망한): 흐름이 정반대예요.'],
 '심경 변화는 앞과 뒤를 나누어 각각 감정 단어로 바꾸고, 두 개가 모두 맞는 선택지를 고르세요. 한쪽만 맞는 선택지(④)가 늘 함정이에요.',
 [(T19[0][0], T19[0][1], "the argument (that) she had with Sarah (목적격 관계대명사 생략) · the day before 그 전날"),
  (T19[3][0], T19[3][1], "It seemed that ~ ~인 것 같았다 · help + O + 동사원형(overcome) ~가 …하도록 돕다"),
  (T19[9][0], T19[9][1], "the way (that) they always did before 예전에 늘 그랬던 방식으로 · did = laughed (대동사)")],
 [('on one’s way to', '~로 가는 길에'), ('argument', '다툼, 논쟁'), ('wipe', '닦다'), ('tear', '눈물'), ('fight', '싸우다'), ('go back to normal', '예전으로 돌아가다'),
  ('overcome', '극복하다'), ('painful', '고통스러운'), ('familiar', '익숙한, 친숙한'), ('spread', '퍼지다, 번지다'), ('hug', '껴안다'), ('tightly', '꽉, 단단히'),
  ('nervous', '긴장한'), ('frustrated', '좌절한'), ('delighted', '기쁜'), ('disappointed', '실망한')],
 ['argument', 'wipe', 'overcome', 'painful', 'familiar', 'spread', 'tightly', 'nervous', 'frustrated', 'delighted', 'disappointed'])

# ═══ 22번 요지 ═══
T22 = [
 ("Studies show that people who sit in the front row learn and retain more than others in the audience, partially because those in the front row are more eager to learn, and they show more attention to the speaker in order to avoid being called on.", "연구에 따르면 앞줄에 앉은 사람들은 청중의 다른 사람들보다 더 많이 배우고 기억하는데, 이는 부분적으로 앞줄에 있는 사람들이 배우기를 더 열망하며, 지적받는 것을 피하기 위해 강연자에게 더 집중하기 때문이다."),
 ("Those in the middle sections are the next most attentive and ask the most questions, as the middle section is considered a safe area, surrounded by others.", "중간 구역에 있는 사람들은 그다음으로 집중력이 높고 가장 많은 질문을 하는데, 중간 구역이 다른 사람들에게 둘러싸여 안전한 영역으로 간주되기 때문이다."),
 ("The side areas and back are the least responsive and attentive.", "가장자리 구역과 뒷줄은 반응하고 집중하는 정도가 가장 낮다."),
 ("In one experiment we conducted, we placed name cards on participants’ seats so they could not take their usual positions.", "우리가 실시한 한 실험에서, 우리는 참가자들이 평소의 자리를 잡지 못하도록 그들의 자리에 이름표를 두었다."),
 ("We intentionally sat enthusiastic people to the sides and rear of the room, and well-known back-row hermits sat in the front.", "우리는 열의가 있는 사람들을 의도적으로 방의 가장자리와 뒤쪽에 앉게 했고, 뒷줄 은둔자로 잘 알려진 사람들을 앞에 앉혔다."),
 ("We found that this strategy not only increased the participation and recall of the normally negative participants who sat up front, it also decreased the participation and recall of the usually positive participants who had been sent to the back.", "우리는 이 전략이 앞에 앉은 보통 소극적인 참가자들의 참여와 기억을 증가시켰을 뿐만 아니라, 뒤쪽으로 보내진 보통 적극적인 참가자들의 참여와 기억을 감소시켰다는 것을 알게 되었다."),
]
day(22, 'q22', '요지', '요지 · 연구 결과 + 실험 결과의 공통점 찾기', '다음 글의 요지로 가장 적절한 것은?', T22,
 ['개인의 성향을 고려한 좌석 배정이 업무의 효율성을 높인다.', '앉은 위치가 학습 참여와 배운 내용의 기억에 영향을 준다.', '학습자들의 적극적인 참여는 생산적인 토론에 필수적이다.', '자유로운 질의응답은 강연 분위기를 결정하는 요인이다.', '수업 집중도와 기억력은 긍정적 상관관계를 보인다.'], 1,
 '앞부분(연구): 앞줄은 더 많이 배우고 기억함 → 중간은 그다음 → 가장자리·뒤는 가장 낮음. 뒷부분(실험): 자리를 강제로 바꿨더니, 앞에 앉힌 소극적인 사람은 참여와 기억(participation and recall)이 늘고, 뒤로 보낸 적극적인 사람은 줄었다. → 성격이 아니라 ‘앉은 위치’가 참여와 기억에 영향을 준다 = ②.',
 ['① ‘업무 효율성’이 아니라 학습 참여와 기억이에요. 또 성향을 고려해 배정한 것이 아니라 일부러 반대로 앉혔어요.',
  '③ 적극적인 참여가 토론에 필수라는 말은 없어요.',
  '④ 질문은 중간 구역의 특징으로만 나와요.',
  '⑤ 집중도와 기억력의 관계를 말하는 글이 아니라, 위치가 둘 다에 영향을 준다는 글이에요. (그럴듯한 일반론 함정)'],
 '요지 문제에서 연구·실험이 나오면 “무엇을 바꿨더니(위치) 무엇이 달라졌는가(참여·기억)”를 한 문장으로 정리하세요. 그 두 요소가 모두 들어간 선택지가 정답이에요.',
 [(T22[0][0], T22[0][1], "people who sit ~ 주어 / learn and retain 동사 · in order to avoid being called on 지적받는 것을 피하려고 (동명사 수동 being p.p.)"),
  (T22[3][0], T22[3][1], "In one experiment (that) we conducted · so (that) they could not ~ ~하지 못하도록"),
  (T22[5][0], T22[5][1], "not only A, (but) it also B 구조 · who had been sent 과거완료 수동(보내진)")],
 [('front row', '앞줄'), ('retain', '기억하다, 보유하다'), ('partially', '부분적으로'), ('eager', '열망하는'), ('call on', '지명하다'), ('attentive', '집중하는'),
  ('section', '구역'), ('surround', '둘러싸다'), ('responsive', '반응하는'), ('conduct', '실시하다'), ('participant', '참가자'), ('intentionally', '의도적으로'),
  ('enthusiastic', '열의가 있는'), ('rear', '뒤쪽'), ('hermit', '은둔자'), ('strategy', '전략'), ('participation', '참여'), ('recall', '기억, 회상')],
 ['retain', 'partially', 'eager', 'attentive', 'surround', 'responsive', 'conduct', 'participant', 'intentionally', 'enthusiastic', 'participation', 'recall'],
 notes='* hermit: 은둔자')

# ═══ 26번 내용 불일치 ═══
T26 = [
 ("Chuck Jones was an influential director and artist whose work shaped animated films and cartoon production.", "Chuck Jones는 그의 작품이 애니메이션 영화와 만화 제작의 틀을 형성한 영향력 있는 감독이자 예술가였다."),
 ("He was born in Spokane, Washington, in 1912, though he grew up in Los Angeles.", "그는 1912년에 Washington 주의 Spokane에서 태어났지만, Los Angeles에서 자랐다."),
 ("As a child, Jones had many opportunities to draw.", "Jones는 어린아이였을 때 그림을 그릴 기회가 많았다."),
 ("He used the leftover pencils and paper that his father brought him from work.", "그는 아버지가 직장에서 그에게 가져다준 남은 연필과 종이를 사용했다."),
 ("Jones began his career in animation in 1930 and was quickly promoted.", "Jones는 1930년에 애니메이션 분야에서 경력을 시작하여 빠르게 승진했다."),
 ("In the 1940s, he created famous characters such as Wile E. Coyote and the Road Runner.", "1940년대에 그는 Wile E. Coyote와 Road Runner 같은 유명한 캐릭터들을 만들었다."),
 ("He directed the famous cartoon film How the Grinch Stole Christmas, which is still enjoyed by many people today.", "그는 유명한 만화 영화 How the Grinch Stole Christmas를 감독했는데, 그 영화는 오늘날에도 많은 사람이 여전히 즐긴다."),
 ("Jones started his own company, Chuck Jones Enterprises, in 1970.", "Jones는 1970년에 자신의 회사인 Chuck Jones Enterprises를 시작했다."),
 ("For his contribution to the field of animation, he received an Honorary Academy Award in 1996.", "그는 애니메이션 분야에 기여한 공로로 1996년에 아카데미 공로상을 받았다."),
 ("Late in his life, he established a non-profit organization supporting art education and other creative skills.", "말년에 그는 예술 교육과 다른 창의적인 능력을 지원하는 비영리 기구를 설립했다."),
]
day(26, 'q26', '내용 불일치', '인물 내용 일치 · 연도(1970 / 1996)를 사건과 짝짓기', 'Chuck Jones에 관한 다음 글의 내용과 일치하지 <u>않는</u> 것은?', T26,
 ['어렸을 때 그림을 그릴 기회가 많았다.', 'Wile E. Coyote와 같은 유명한 캐릭터를 만들었다.', '많은 사람들이 여전히 즐기는 만화 영화를 감독했다.', '애니메이션 분야에 기여한 공로로 1970년에 상을 받았다.', '예술 교육을 지원하는 비영리 기구를 설립했다.'], 3,
 '1970년은 자신의 회사(Chuck Jones Enterprises)를 시작한 해예요. 애니메이션에 기여한 공로로 상(Honorary Academy Award)을 받은 해는 1996년이에요. 연도와 사건을 바꿔 놓은 ④가 불일치.',
 ['① As a child, Jones had many opportunities to draw → 일치',
  '② he created famous characters such as Wile E. Coyote → 일치',
  '③ How the Grinch Stole Christmas, which is still enjoyed by many people today → 일치',
  '⑤ he established a non-profit organization supporting art education → 일치'],
 '인물 일치 문제는 연도가 여러 개 나오면 “연도–사건”을 짝지어 표시하세요. 선택지는 본문 순서대로 나오니, 하나씩 본문에서 위치를 찾아 대조하면 돼요.',
 [(T26[0][0], T26[0][1], "소유격 관계대명사 whose + 명사(work) ~의 작품이 … · shape 틀을 형성하다"),
  (T26[3][0], T26[3][1], "the leftover pencils and paper that his father brought him (목적격 관계대명사 that) · bring + 사람 + 물건"),
  (T26[9][0], T26[9][1], "a non-profit organization supporting ~ (현재분사구가 명사를 뒤에서 꾸밈: ~을 지원하는)")],
 [('influential', '영향력 있는'), ('director', '감독'), ('shape', '틀을 형성하다'), ('animated film', '애니메이션 영화'), ('production', '제작'), ('opportunity', '기회'),
  ('leftover', '(쓰고) 남은'), ('career', '경력'), ('promote', '승진시키다'), ('direct', '감독하다'), ('contribution', '공로, 기여'), ('field', '분야'),
  ('Honorary Academy Award', '아카데미 공로상'), ('establish', '설립하다'), ('non-profit organization', '비영리 기구'), ('creative', '창의적인')],
 ['influential', 'director', 'production', 'opportunity', 'leftover', 'career', 'promote', 'contribution', 'field', 'establish', 'creative'])

# ═══ 23번 주제 ═══
T23 = [
 ("Popular culture loves to label dopamine as the “pleasure molecule,” yet science reveals a richer, more nuanced reality.", "대중문화에서는 도파민에 ‘쾌락 분자’라는 딱지를 붙이기를 좋아하지만, 과학은 더 풍부하고 더 미묘한 현실을 드러낸다."),
 ("Dopamine’s true role is found not simply in the thrill of reward, but in the dance of anticipation, striving, and imagining what could be.", "도파민의 진정한 역할은 단순히 보상의 황홀감에서가 아니라, 기대와 노력, 그리고 무엇이 될 수 있을지를 상상하는 것의 역동적 과정에서 발견된다."),
 ("The rush of motivation that energizes you at the start of a new day, the focus that allows you to solve complex problems, and the curiosity that fuels ambition are all orchestrated by dopamine.", "새로운 하루를 시작할 때 여러분에게 활력을 주는 동기 부여의 급증, 복잡한 문제를 해결할 수 있게 해 주는 집중력, 그리고 야망에 기름을 붓는 호기심은 모두 도파민에 의해 조율된다."),
 ("Dopamine doesn’t give contentment; it delivers possibility.", "도파민은 만족감을 주는 것이 아니라 가능성을 전달한다."),
 ("It sets the stage for new challenges, frames future goals as attainable, and propels you to ask “What if?” about new opportunities, relationships, or aspirations.", "그것은 새로운 도전을 위한 무대를 마련하고, 미래의 목표를 달성 가능한 것으로 그리며, 새로운 기회, 인간관계 또는 열망에 대해 “~라면 어떨까?”라고 묻도록 이끈다."),
 ("The anticipation of a meaningful conversation, the excitement for a fresh project, and even just the temptation of a delicious meal are all sparked by dopamine’s drive for future reward.", "의미 있는 대화에 대한 기대, 새로운 프로젝트에 대한 설렘, 심지어 그저 맛있는 식사에 대한 유혹까지도 모두 미래의 보상을 향한 도파민의 작용으로 촉발된다."),
 ("Critically, dopamine rewards the process, not just the finished result.", "결정적으로, 도파민은 단지 완료된 결과만이 아니라 과정 자체에 보상한다."),
 ("It’s what sharpens focus and fills ordinary moments with potential.", "바로 그것이 집중력을 더 날카롭게 하고 평범한 순간들을 가능성으로 채우는 것이다."),
]
day(23, 'q23', '주제', '주제 · not A but B에서 B(가능성)를 잡기', '다음 글의 주제로 가장 적절한 것은?', T23,
 ['limitation of dopamine as a chemical reaction orchestrator', 'impact of dopamine on sparking intense pleasure', 'usefulness of dopamine in improving cognitive skills', 'importance of rewards in sustaining motivation', 'force of dopamine as a facilitator of realizing possibilities'], 4,
 '대중문화는 도파민을 ‘쾌락 분자’라 부르지만(통념), 과학은 다르다(yet). 도파민의 진짜 역할은 쾌락이 아니라(not simply in the thrill of reward) 기대·노력·상상 속에 있고, 만족감이 아니라 가능성을 전달한다(doesn’t give contentment; it delivers possibility). 결과가 아니라 과정에 보상한다. → 가능성을 실현하도록 돕는 촉진제로서 도파민의 힘 = ⑤.',
 ['① 도파민의 ‘한계’를 말하는 글이 아니에요. orchestrate(조율하다)라는 단어만 빌려 온 오답이에요.',
  '② 강렬한 쾌락은 글이 부정하는 통념(pleasure molecule)이에요. 정반대 오답!',
  '③ 집중력·문제 해결이 예로 나오지만 ‘인지 능력 향상’ 자체가 주제는 아니에요. (부분 정보)',
  '④ 주어가 도파민이 아니라 ‘보상’이에요. 글은 결과로서의 보상보다 과정·가능성을 강조해요.'],
 '주제 문제에서 “통념(Popular culture …) + yet/but + 진짜 내용”이 나오면, but 뒤가 주제예요. not A but B, doesn’t A; it B 구조에서 B에 해당하는 말(possibility, process)을 담은 선택지를 고르세요.',
 [(T23[1][0], T23[1][1], "not simply in A, but in B 단순히 A에서가 아니라 B에서 · what could be 무엇이 될 수 있을지(관계대명사 what)"),
  (T23[3][0], T23[3][1], "doesn’t A; it B → A가 아니라 B (세미콜론으로 대조) · contentment 만족감 ↔ possibility 가능성"),
  (T23[4][0], T23[4][1], "동사 3개 병렬: sets ~, frames ~, and propels ~ · frame A as B A를 B로 그리다 · propel + O + to부정사 ~하도록 이끌다")],
 [('popular culture', '대중문화'), ('label', '딱지를 붙이다'), ('molecule', '분자'), ('nuanced', '미묘한'), ('thrill', '황홀감, 전율'), ('anticipation', '기대'),
  ('strive', '노력하다'), ('energize', '활력을 주다'), ('fuel', '부채질하다, 연료를 공급하다'), ('ambition', '야망'), ('orchestrate', '조율하다'), ('contentment', '만족감'),
  ('attainable', '달성 가능한'), ('propel', '이끌다, 나아가게 하다'), ('aspiration', '열망'), ('temptation', '유혹'), ('spark', '촉발하다'), ('critically', '결정적으로'),
  ('ordinary', '평범한'), ('potential', '가능성, 잠재력'), ('facilitator', '촉진제, 촉진하는 것')],
 ['label', 'molecule', 'nuanced', 'anticipation', 'ambition', 'orchestrate', 'contentment', 'attainable', 'aspiration', 'temptation', 'ordinary', 'potential'],
 notes='* strive: 노력하다')

# ═══ 27번 안내문 불일치 ═══
T27 = [
 ("RCQ High School Food Waste Reduction Competition", "RCQ 고등학교 음식물 쓰레기 줄이기 대회"),
 ("Our school is holding a food waste reduction competition to promote sustainable living.", "우리 학교는 지속 가능한 삶을 장려하기 위해 음식물 쓰레기 줄이기 대회를 개최합니다."),
 ("This competition has been held every year since 2023.", "이 대회는 2023년 이래로 매년 개최되어 왔습니다."),
 ("Your effort makes a difference!", "여러분의 노력이 변화를 만듭니다!"),
 ("When: October 1 to October 31, 2026", "일시: 2026년 10월 1일부터 10월 31일까지"),
 ("Who: All classes of RCQ High School will participate.", "대상: RCQ 고등학교의 모든 학급이 참가할 것입니다."),
 ("How", "방법"),
 ("Every lunch, we will give a point to each student who doesn’t leave food on their tray.", "매 점심에, 식판에 음식을 남기지 않은 학생 각각에게 점수를 줄 것입니다."),
 ("Students’ points will be combined by class.", "학생들의 점수는 학급별로 합해질 것입니다."),
 ("Winning classes will be decided by each class’s points.", "수상 학급은 각 학급의 점수로 결정될 것입니다."),
 ("Prizes", "시상"),
 ("1st prize: 1 class — Snacks worth $200", "1등상: 1개 학급 — 200달러어치의 간식"),
 ("2nd prize: 1 class — Snacks worth $150", "2등상: 1개 학급 — 150달러어치의 간식"),
 ("3rd prize: 2 classes — Snacks worth $100", "3등상: 2개 학급 — 100달러어치의 간식 (학급당)"),
]
H27 = {"RCQ High School Food Waste Reduction Competition", "How", "Prizes"}
TB27 = ('<table style="border-collapse:collapse;width:100%;font-size:12px;margin:6px 0">'
        '<tr>' + ''.join('<th %s>%s</th>' % (TD, h) for h in ('', 'Number of Winners', 'Reward (per class)')) + '</tr>'
        + ''.join('<tr>' + ''.join('<td %s>%s</td>' % (TD, v) for v in r) + '</tr>' for r in
                  [('1st prize', '1 class', 'Snacks worth $200'), ('2nd prize', '1 class', 'Snacks worth $150'), ('3rd prize', '2 classes', 'Snacks worth $100')]) + '</table>')
day(27, 'q27', '안내문 불일치', '안내문 · 표의 숫자(1 class / 2 classes) 대조', 'RCQ High School Food Waste Reduction Competition에 관한 다음 안내문의 내용과 일치하지 <u>않는</u> 것은?', T27,
 ['2023년 이래로 매년 개최되고 있다.', '한 달간 진행된다.', 'RCQ 고등학교의 모든 학급이 참가할 것이다.', '수상 학급은 각 학급의 점수로 결정될 것이다.', '2등상은 두 학급에 주어진다.'], 4,
 '시상 표에서 2nd prize는 1 class(한 학급)예요. 두 학급(2 classes)에 주어지는 것은 3등상이에요. 줄을 바꿔 읽은 ⑤가 불일치.',
 ['① This competition has been held every year since 2023 → 일치',
  '② October 1 to October 31 → 10월 한 달간 진행 → 일치',
  '③ All classes of RCQ High School will participate → 일치',
  '④ Winning classes will be decided by each class’s points → 일치'],
 '안내문에 표가 있으면 선택지의 숫자가 표의 “어느 줄”인지 손가락으로 짚어 확인하세요. 옆 줄의 숫자로 바꿔 놓는 것이 단골 함정이에요.',
 [(T27[1][0], T27[1][1], "be holding 개최할 예정이다(가까운 미래) · to promote ~ 장려하기 위해 (목적의 to부정사)"),
  (T27[2][0], T27[2][1], "has been held 현재완료 수동(계속 개최되어 왔다) · since + 과거 시점"),
  (T27[7][0], T27[7][1], "each student who doesn’t ~ (each + 단수 명사 → 단수 동사 doesn’t) · leave food 음식을 남기다")],
 [('food waste', '음식물 쓰레기'), ('reduction', '줄이기, 감축'), ('competition', '대회'), ('promote', '장려하다'), ('sustainable', '지속 가능한'), ('make a difference', '변화를 만들다'),
  ('participate', '참가하다'), ('tray', '식판, 쟁반'), ('combine', '합하다'), ('decide', '결정하다'), ('prize', '상'), ('reward', '부상, 보상'), ('worth', '~의 가치가 있는')],
 ['reduction', 'competition', 'promote', 'sustainable', 'participate', 'tray', 'combine', 'reward', 'worth'],
 paras=[lines_html(T27[:11], H27), TB27])

# ═══ 24번 제목 ═══
T24 = [
 ("The new views about and questions being asked about aging could be detected across society.", "노화에 관한 새로운 관점과 제기되는 질문들이 사회 전반에서 감지될 수 있었다."),
 ("“Something strange is happening in America,” wrote Marj Jackson Levin for the St. Louis Post-Dispatch in 1988, finding that what she called “the former boundaries of age” were being expanded or relaxed in many arenas.", "Marj Jackson Levin은 1988년 St. Louis Post-Dispatch에 “미국에서 뭔가 이상한 일이 일어나고 있다.”라고 썼는데, 그녀가 ‘과거의 연령 경계’라 부른 것이 많은 활동 무대에서 확장되거나 완화되고 있다는 것을 발견했다."),
 ("Whether it was fortysomething baseball players, midlife women having babies, or the oldest president in the nation’s history, it did indeed appear that the preconceptions surrounding aging were weakening.", "40대 야구 선수든, 아이를 가진 중년 여성이든, 국가 역사상 가장 나이가 많은 대통령이든, 노화를 둘러싼 선입견들이 약해지고 있다는 것은 정말 분명해 보였다."),
 ("As baby boomers entered midlife, the idea of oldness was being pushed back, and the expectations for what people should or should not be doing at a particular age broadened.", "베이비붐 세대가 중년에 접어들면서, 노년이라는 개념은 뒤로 밀려나고 있었고, 특정 연령에 무엇을 해야 하고 하지 말아야 하는지에 대한 기대는 넓어졌다."),
 ("Turning fifty had only recently been commonly viewed as the unofficial turning of the corner into one’s senior years, for example, but now that number did not automatically mean one could not start a new career or family.", "예를 들어, 50세가 되는 것은 최근까지만 해도 노년기로 접어드는 비공식적인 전환점으로 흔히 여겨졌지만, 이제 그 숫자가 새 직업을 시작하거나 새 가정을 꾸릴 수 없다는 것을 자동으로 의미하지는 않았다."),
 ("In a good number of cases, at least, age was becoming less significant, a clear victory for those lobbying for a less age-centric society.", "적어도 상당히 많은 경우에 나이는 덜 중요해지고 있었는데, 이는 연령 중심성이 덜한 사회를 위해 운동하는 사람들에게 분명한 승리였다."),
]
day(24, 'q24', '제목', '제목 · 반복되는 말(boundaries, weakening, less significant) 묶기', '다음 글의 제목으로 가장 적절한 것은?', T24,
 ['Fading Boundaries: Evolving Views of Aging', 'Forever Young! The Rise of the Anti-aging Industry', 'How Multiple Perspectives Narrow Generation Gaps', 'Older and Wiser: What the Elderly Can Teach Us', 'Do Modern Lifestyles Really Slow Aging?'], 0,
 '노화에 대한 새로운 관점(new views about aging)이 사회 전반에 나타남 → 과거의 연령 경계가 확장·완화됨(boundaries of age were being expanded or relaxed) → 선입견이 약해짐(weakening) → 나이가 덜 중요해짐(less significant). → 희미해지는 경계: 변화하는 노화에 대한 관점 = ①.',
 ['② ‘영원히 젊게!’ 항노화 산업은 나오지 않아요. 나이 드는 것을 막는 이야기가 아니라 나이에 대한 ‘생각’이 바뀐 이야기예요.',
  '③ 세대 차이를 좁히는 이야기는 없어요.',
  '④ 노인이 가르쳐 줄 지혜는 나오지 않아요.',
  '⑤ 현대 생활 방식이 노화를 늦추는지(신체적 노화)는 다루지 않아요.'],
 '제목 문제는 글에서 반복되는 핵심어를 찾아 그것을 비유적으로 바꾼 말을 고르세요. boundaries were relaxed → Fading Boundaries, new views → Evolving Views.',
 [(T24[1][0], T24[1][1], "인용문 + wrote + 주어 (도치) · 분사구문 finding that ~ · what she called “~” 그녀가 ‘~’라 부른 것 · were being expanded 과거진행 수동"),
  (T24[2][0], T24[2][1], "Whether it was A, B, or C A든 B든 C든 · did indeed appear (did = 강조의 조동사)"),
  (T24[5][0], T24[5][1], "콤마 뒤 명사구 a clear victory ~ = 앞 문장 전체를 다시 설명 (동격) · those lobbying for ~ ~을 위해 운동하는 사람들")],
 [('detect', '감지하다'), ('aging', '노화'), ('former', '이전의'), ('boundary', '경계'), ('expand', '확장하다'), ('relax', '완화하다'),
  ('arena', '활동 무대, 경기장'), ('fortysomething', '40대'), ('midlife', '중년(의)'), ('preconception', '선입견'), ('surround', '둘러싸다'), ('weaken', '약해지다'),
  ('push back', '뒤로 미루다, 밀어내다'), ('broaden', '넓어지다'), ('unofficial', '비공식적인'), ('automatically', '자동으로'), ('significant', '중요한'), ('lobby', '(정치·사회적) 운동을 하다'),
  ('age-centric', '연령 중심의'), ('fade', '희미해지다')],
 ['detect', 'former', 'boundary', 'expand', 'arena', 'preconception', 'weaken', 'broaden', 'unofficial', 'automatically', 'significant', 'fade'])
