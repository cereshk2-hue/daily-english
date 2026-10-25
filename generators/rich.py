import json, re
P = '/home/claude/proj/data/h1-mock-2509.js'
J = lambda x: json.dumps(x, ensure_ascii=False)

ORDER = {
1: [
 ['학생회장으로서 도서관 운영 시간 문제로 연락함', '현재 5시 마감 → 자료 이용이 제한됨', '입시·학업 프로젝트 학생에게 특히 힘듦', '그래서 7시까지 연장을 요청함', '연장하면 학업 목표에 집중할 시간이 생김'],
 ['벽시계를 힐끗 봄', '10시', '곧 오디션 결과 전화가 올 시간', '온몸이 떨리고 손톱을 물어뜯음'],
 ['마침내 전화가 울림', '내가 오는 사이 아빠가 받음', '아빠가 "알려 줄게요"라고 말함', '계단 아래 오니 아빠가 전화를 내려놓음', '아빠: "먼치킨 역에 붙었어"'],
 ['비효율적인 교사는 수업 첫 몇 분을 간과함', '수업 시작 전 10분 넘게 사라지기도 함', '그러니 학생들이 늦는 건 당연함', '처음 10분을 잘 쓸 수도, 낭비할 수도 있음', '처음 몇 분이 수업 분위기를 정함'],
 ['처음 몇 분이 수업 분위기를 정함', '시작 루틴이 있으면 학생들이 전환·집중 준비를 함', '결론: 시작 루틴을 만들어라'],
],
2: [
 ['몸속 원자는 우주만큼 오래됨', '숨 쉴 때 일부만 내쉼', '나머지는 몸의 일부가 됐다가 나중에 떠남', '원자는 소유가 아니라 빌리는 것'],
 ['모두 같은 원자 저장소를 공유함', '호흡·땀으로 사람 사이를 순환함', '대규모로 원자를 재활용함', '가벼운 원자는 우주의 기원, 무거운 원자는 태양·지구보다 오래됨', '시간의 시작부터 존재하며 무한한 형태로 순환함'],
 ['정원 가꾸기는 훌륭한 신체 활동', '파기·심기·물 주기·수확 등 다양한 동작', '근력·유연성·지구력 향상', '잡초 뽑기 같은 작은 일도 칼로리 소모', '전통 운동이 힘든 사람에게 특히 좋음'],
 ['신체 외에 정신 건강에도 이점', '식물 돌보기는 마음을 진정시킴', '현재에 집중 → 스트레스·불안 감소', '반복 작업이 마음 챙김 상태를 만듦', '연구: 기분·인지 향상, 우울 감소'],
],
3: [
 ['인간은 감각으로 못 느끼는 현상을 도구로 지각해 옴', '① 감각 신호를 확장하는 도구 (예: 망원경)', '② 지각 못 하는 신호를 관찰 가능한 신호로 바꾸는 도구', '그 예: 자외선 이미지, 가청 범위 밖 소리 변환', '③ 감각이 아예 없는 속성을 측정해 바꾸는 도구'],
 ['반대자: 의학 발전은 동물 실험의 결과가 아니었다', '옹호자: 상관관계가 있으니 동물 실험이 발전을 일으켰다', '반대자는 이 추론을 거부함', '상관관계가 생길 별개의 이유가 있음'],
 ['상관관계가 생길 별개의 이유가 있음', '법이 모든 신약 등을 먼저 동물에게 시험하게 함', '따라서 상관관계는 법적 필요성의 결과일 뿐'],
 ['법이 동물 시험을 의무화함', '상관관계는 법적 필요성의 결과', '게다가 의사들이 역사적 반대 증거를 제시함', '임상적 발견이 더 큰 역할을 했다고 주장함'],
]}
INSERT = {
1: [
 ['현재 5시 마감 → 이용이 제한됨', '입시 준비 학생들에게 특히 힘듦', '그래서 7시까지 연장을 요청함', '이 변화(연장)가 학생들에게 도움이 됨'],
 ['전화가 울림', '아빠가 전화를 받음', '아빠가 "알려 줄게요"라고 말함', '아빠가 전화를 내려놓음'],
 ['시계를 봄', '10시', '그것(10시)은 곧 결과 전화가 온다는 뜻', '긴장해서 온몸이 떨림'],
 ['학생들이 늦는 건 당연함', '첫 10분을 쓸지 낭비할지는 선택', '첫 몇 분이 분위기를 정함', '루틴이 있으면 이 짧은 시간을 전환에 씀'],
],
2: [
 ['숨 쉴 때 일부만 내쉼', '나머지 원자는 몸의 일부가 됨', '원자는 소유가 아니라 빌리는 것', '모두 같은 원자 저장소를 공유함'],
 ['원자의 기원은 우주·태양보다 오래됨', '시간의 시작부터 순환해 온 원자', '나는 원자의 현재 관리인', '내 뒤를 이을 이들이 많을 것'],
 ['다양한 동작을 포함함', '이런 활동들이 근력·유연성·지구력 향상', '작은 일도 칼로리 소모', '전통 운동이 힘든 사람에게 좋음'],
 ['정신 건강에도 이점이 있음', '식물 돌보기는 마음을 진정시킴', '그것이 현재에 집중하게 해 스트레스 감소', '반복 작업 → 마음 챙김 상태'],
],
3: [
 ['인간은 도구로 못 느끼는 현상을 지각해 옴', '어떤 경우엔 이것이 신호를 단순히 확장하는 것 (망원경)', '다른 도구는 지각 못 하는 신호를 바꿈', '그중 일부는 감각 범위를 넓힘'],
 ['신호를 확장하는 도구', '지각 못 하는 신호를 바꾸는 도구', '이것들 중 일부는 감각 범위를 넓히는 형태', '또는 감각이 전혀 없는 속성을 측정'],
 ['옹호자: 동물 실험이 발전을 일으켰다', '반대자는 이 추론을 거부함', '상관관계가 생길 별개의 이유가 있음', '법이 동물 시험을 의무화함'],
 ['법이 동물 시험을 의무화함', '상관관계는 법적 필요성의 결과', '게다가 의사들이 역사적 반대 증거를 제시함', '그들은 임상적 발견이 더 중요했다고 주장함'],
]}
TFEV = {
1: ["As student council president, I am reaching out", "At present, the library closes at 5 p.m.", "extend the library's operating hours to 7 p.m.", "the results of my first audition", "While I was coming round, Dad answered", "While I was coming round, Dad answered", "You're second senior munchkin", "The first minutes set the tone", "prepare to focus on learning new material"],
2: ["only some of the atoms that you inhale are exhaled", "you borrow them", "Atoms cycle from person to person", "most heavier atoms are older than the Sun and Earth", "It involves a range of motions", "can burn many calories", "accessible for people of all ages", "even in a small garden"],
3: ["telescopes can bring into clear view", "some instruments measure properties for which we have no sensory capacity at all", "changing sounds that are normally outside the range", "some instruments measure properties for which we have no sensory capacity at all", "the former caused the latter", "Opponents of research reject this inference", "the law prescribes that all new drugs", "clinical discoveries played a more substantial role"],
}
# 실전 문항: [선택지 해석, 근거, 이유] — opts 순서(첫 번째가 정답)
REAL = {
1: [
 [['', "Therefore, I'd like to ask you to extend the library's operating hours to 7 p.m.", '"Therefore, I\'d like to ask you to ~"가 요청의 핵심 문장 → 운영 시간 연장 요청'],
  ['', '', '새 책 구입 이야기는 없음'],
  ['', '', '도서관 프로그램은 언급되지 않음'],
  ['', "I hope you will consider this proposal", '감사 편지가 아니라 제안·요청하는 편지'],
  ['', 'a quiet and resourceful environment', '조용한 환경 언급은 있지만, 공간이 아니라 "시간" 연장을 요청함']],
 [['긴장한 → 기쁜', ["I felt shaky all over", "I got a little rush of excitement"], '손톱을 물어뜯고 발을 떪(긴장) → 합격 소식에 흥분(기쁨)'],
  ['어리둥절한 → 차분한', '', '어리둥절할 상황이 아니고, 마지막엔 흥분함'],
  ['지루한 → 혼란스러운', '', '지루해하지 않고 초조해함'],
  ['만족한 → 후회하는', '', '후회할 일이 없음, 합격함'],
  ['자신감 있는 → 실망한', "I felt shaky all over", '처음부터 떨렸고, 결과도 합격']],
 [['', "In summary, you should establish an opening routine", '"In summary, you should ~" 결론 문장이 주장'],
  ['', '', '포용적 분위기 이야기는 없음'],
  ['', '', '수업 자료 개발 이야기는 없음'],
  ['', '', '학습량 조절 이야기는 없음'],
  ['', "have taught your students an opening routine", '루틴은 교사가 가르쳐 주는 것 → "학생 스스로"가 틀림']],
],
2: [
 [['원자는 당신 이후에 다른 형태의 일부가 될 것이다', ["recycling throughout the universe among limitless forms", "You're the present caretaker of the atoms"], '나는 "현재" 관리인일 뿐, 원자는 계속 다른 형태로 순환함'],
  ['원자는 고유하게 남아 공유될 수 없을 것이다', "We all share from the same atom pool", '같은 원자 저장소를 공유한다고 함'],
  ['원자는 원래의 형태를 따를 것이다', '', '원래 형태로 돌아간다는 내용은 없음'],
  ['원자는 결코 새로운 형태에 받아들여지지 않을 것이다', "among limitless forms", '무한한 형태 사이를 순환함 → 반대'],
  ['원자는 당신의 생이 끝나면 완전히 사라질 것이다', "have existed since the first moments of time", '시간의 시작부터 존재해 온 원자는 사라지지 않음']],
 [['', ["The act of gardening itself is a fantastic form of physical activity", "Besides physical health, gardening has profound mental health benefits"], '앞부분은 신체 건강, Besides 이후는 정신 건강 → 둘 다 이로움'],
  ['', "boost self-esteem", '자존감은 나오지만 협동심·야외 활동 이야기는 없음'],
  ['', '', '취미의 동기 이야기는 없음'],
  ['', "It allows you to focus on the present moment", '집중은 나오지만 "실내" 식물 이야기가 아님'],
  ['', "accessible for people of all ages", '글에 있는 내용이지만 세부 사항일 뿐 요지가 아님']],
],
3: [
 [['인간 감각의 능력을 높여 주는 도구', ["humans have taken advantage of tools", "expanding the reach of our current senses"], '글 전체가 감각으로 못 느끼는 것을 느끼게 해 주는 도구 이야기'],
  ['인간의 감각을 도구로 대체하는 것의 어려움', '', '어려움은 언급되지 않음'],
  ['과학 도구 발명에 영감을 주는 인간의 감각', '', '감각이 발명의 영감이라는 내용은 없음'],
  ['인간의 시각과 청각의 차이', "changing sounds", '시각·청각 예시가 나오지만 차이를 비교하는 글이 아님'],
  ['우주 발견에서 인간 상상력의 힘', '', '상상력 이야기는 없음']],
 [['의학은 동물 실험으로 발전하는가?', ["Opponents of research reject this inference", "the correlation between animal experimentation and medical discovery is the result of legal necessity"], '동물 실험 → 의학 발전이라는 주장에 의문을 제기하는 글'],
  ['생의학: 의료의 새로운 영역을 열다', '', '새 영역 개척 이야기가 아님'],
  ['의료 문제 해결을 위해 역사적 증거를 참고하라', "several influential physicians have offered historical evidence", '역사적 증거는 근거 중 하나일 뿐, 의료 문제 해결 이야기가 아님'],
  ['왜 동물 입양에 대한 엄격한 법은 없을까?', "the law prescribes", '입양 이야기는 없음, 법은 실험을 의무화하는 법'],
  ['인간 수명 연장을 위한 의학적 진보', "the decline in mortality", '사망률 감소 언급은 있지만 수명 연장 방법 이야기가 아님']],
]}
# 일치·불일치: [선택지 해석, 근거, 판정]
M = {
1: [
 [['필자는 도서관의 현재 일정에 만족하며 변경을 원하지 않는다.', "Therefore, I'd like to ask you to extend", '불일치 → 연장을 요청함'],
  ['필자는 학생회장의 자격으로 교장에게 연락한다.', "As student council president, I am reaching out", '일치'],
  ['이른 마감 시간이 학생들의 도서관 자료 이용을 제한한다.', "limits their ability to fully use its resources", '일치'],
  ['대학 입시를 준비하는 학생들이 특히 불편을 겪는다.', "particularly challenging for those preparing for college entrance exams", '일치'],
  ['필자는 도서관 운영 시간을 2시간 더 연장할 것을 제안한다.', ["the library closes at 5 p.m.", "extend the library's operating hours to 7 p.m."], '일치 (5시 → 7시 = 2시간)']],
 [['필자는 연장이 학생들에게 학업 목표를 추구할 시간을 더 줄 것이라고 믿는다.', "This change would greatly benefit students by providing additional time", '일치'],
  ['이 편지는 교사가 학생들을 대신해 썼다.', "As student council president", '불일치 → 학생회장 Eric Park가 씀'],
  ['도서관이 시끄럽고 시설이 부족하다고 비판받는다.', '', '불일치 → 언급 없음'],
  ['필자는 도서관이 주말에 문을 열 것을 요구한다.', '', '불일치 → 주말이 아니라 저녁 7시까지 연장'],
  ['필자는 요청이 거절되면 시위를 조직하겠다고 위협한다.', "I hope you will consider this proposal", '불일치 → 정중하게 고려를 부탁할 뿐']],
 [['화자는 캐스팅 감독에게서 직접 전화로 소식을 들었다.', ["Dad answered", "he announced"], '불일치 → 아빠가 받아서 전해 줌'],
  ['화자는 오디션 결과를 기다리며 불안해했다.', "I felt shaky all over", '일치'],
  ['화자는 안절부절못하는 등 불안한 몸짓을 보였다.', "chewing my thumbnail and jiggling my feet", '일치'],
  ['아빠는 전화를 끊고 나서 소식을 전했다.', ["he was just putting the phone down", "he announced"], '일치'],
  ['화자는 배역을 따냈다는 것을 알고 크게 기뻐했다.', "I got a little rush of excitement, knowing I was in", '일치']],
 [['화자는 오즈의 마법사에서 먼치킨 역을 맡았다.', "You're second senior munchkin", '일치'],
  ['화자는 이번 오디션 전에 여러 뮤지컬에 출연했었다.', "my first audition", '불일치 → 첫 오디션이었음'],
  ['전화가 울렸을 때 화자가 직접 받았다.', "Dad answered", '불일치 → 아빠가 받음'],
  ['화자는 결과를 듣고 무덤덤했다.', "I got a little rush of excitement", '불일치 → 흥분함'],
  ['캐스팅 감독은 결과 발표를 미뤘다.', "the casting director would call very soon", '불일치 → 10시에 바로 전화가 옴']],
 [['늦게 오는 학생은 시간 엄수를 위해 벌을 받아야 한다.', "they have little reason to be on time", '불일치 → 벌 이야기는 없음. 늦는 건 일찍 올 이유가 없어서라고 함'],
  ['비효율적인 교사는 처음 몇 분의 중요성을 간과하는 경향이 있다.', "Inefficient teachers overlook the potential power", '일치'],
  ['실제 수업이 시작되기 전에 10분 넘게 흘러갈 수 있다.', "more than ten minutes can disappear before class starts", '일치'],
  ['처음 몇 분이 수업 전체의 분위기를 결정한다.', "The first minutes set the tone", '일치'],
  ['잘 만든 루틴은 학생들이 새 내용으로 초점을 전환하도록 돕는다.', "make mental and emotional transitions", '일치']],
 [['수업이 늦게 시작되면 학생들은 시간을 지킬 이유가 거의 없다.', "they have little reason to be on time", '일치'],
  ['필자는 수업 시작 몇 분이 사소하다고 주장한다.', "The first minutes set the tone", '불일치 → 오히려 중요하다고 함'],
  ['교사는 처음 10분을 숙제 검토에 써야 한다.', '', '불일치 → 숙제 이야기는 없음'],
  ['시작 루틴은 이미 성실한 학생에게만 효과가 있다.', '', '불일치 → 그런 조건은 없음'],
  ['필자는 즉흥성을 위해 루틴을 없앨 것을 권한다.', "you should establish an opening routine", '불일치 → 루틴을 만들라고 함']],
],
2: [
 [['우리가 들이마신 모든 원자는 바로 다음 숨에 내보내진다.', "only some of the atoms that you inhale are exhaled", '불일치 → 일부(only some)만 내쉼'],
  ['우리 몸속 원자의 상당 부분은 거의 우주만큼 오래되었다.', "Many atoms in your body are nearly as old as the universe itself", '일치'],
  ['우리는 원자를 소유하지 않고 단지 빌릴 뿐이다.', "you borrow them", '일치'],
  ['원자는 호흡과 땀을 통해 사람들 사이에서 교환된다.', "Atoms cycle from person to person as we breathe and as our sweat is evaporated", '일치'],
  ['가장 가벼운 원자는 우주의 기원으로 거슬러 올라간다.', "The origin of the lightest atoms goes back to the origin of the universe", '일치']],
 [['많은 무거운 원자는 태양과 지구가 생기기 전부터 있었다.', "most heavier atoms are older than the Sun and Earth", '일치'],
  ['몸에 들어온 원자는 영원히 그곳에 머문다.', "they later leave your body by various means", '불일치 → 나중에 몸을 떠남'],
  ['사람마다 따로 쓰는 독점적인 원자 저장소가 있다.', "We all share from the same atom pool", '불일치 → 같은 저장소를 공유함'],
  ['원자는 살아 있는 생물 사이에서만 순환한다.', "both nonliving and living", '불일치 → 무생물과 생물 모두'],
  ['원자 재활용은 아주 작은 규모로만 일어난다.', "We recycle atoms on a grand scale", '불일치 → 대규모로 일어남']],
 [['정원 가꾸기는 전통적인 운동을 힘들어하는 사람에게 맞지 않는다.', "Gardening is particularly beneficial for those who find traditional exercise challenging", '불일치 → 오히려 특히 이로움'],
  ['정원 가꾸기는 땅 파기부터 수확까지 다양한 동작을 포함한다.', "It involves a range of motions, from digging and planting to watering and harvesting", '일치'],
  ['잡초 뽑기 같은 작은 일도 상당한 칼로리를 소모할 수 있다.', "small tasks like weeding or turning compost can burn many calories", '일치'],
  ['식물을 돌보는 것은 마음을 달래 주는 명상적 효과가 있다.', "Tending to plants can be incredibly calming and meditative", '일치'],
  ['식물이 잘 자라는 것을 보면 자존감이 높아질 수 있다.', "watching your plants grow and thrive can also boost self-esteem", '일치']],
 [['정원 가꾸기는 몸에 무리가 적어 나이에 상관없이 할 수 있다.', "making it accessible for people of all ages", '일치'],
  ['정원 가꾸기의 이점은 신체 건강에 국한된다.', "Besides physical health, gardening has profound mental health benefits", '불일치 → 정신 건강에도 이로움'],
  ['반복적인 정원 일은 불안을 높이는 경향이 있다.', "reducing stress and anxiety", '불일치 → 불안을 줄여 줌'],
  ['연구에 따르면 큰 정원만 우울증을 완화한다.', "even in a small garden", '불일치 → 작은 정원도 효과가 있음'],
  ['정원 가꾸기는 단조로워서 인지 기능을 해친다.', "improve cognition", '불일치 → 인지 능력을 향상함']],
],
3: [
 [['모든 도구는 우리 감각이 이미 감지할 수 있는 신호를 단지 확대할 뿐이다.', "some instruments measure properties for which we have no sensory capacity at all", '불일치 → 감각이 전혀 없는 속성을 재는 도구도 있음'],
  ['망원경은 맨눈으로 보기에 너무 먼 물체를 알아볼 수 있게 해 준다.', "telescopes can bring into clear view that which is too far away", '일치'],
  ['어떤 장치는 지각할 수 없는 신호를 관찰할 수 있는 신호로 바꾼다.', "Other instruments turn signals that we cannot perceive into ones that we can observe", '일치'],
  ['어떤 도구는 자외선을 눈에 보이는 이미지로 나타낸다.', "creating visible images based on the ultraviolet spectrum of light", '일치'],
  ['어떤 도구는 인간에게 감각 능력이 전혀 없는 속성을 측정한다.', "measure properties for which we have no sensory capacity at all", '일치']],
 [['어떤 도구는 사람이 들을 수 있는 범위를 넘는 소리를 들리는 신호로 바꾼다.', "changing sounds that are normally outside the range of what human ears can hear into audible signals", '일치'],
  ['인간은 최근 수십 년 사이에야 이런 도구에 의존하기 시작했다.', "For many centuries", '불일치 → 수 세기 동안 써 왔음'],
  ['과학 도구가 인간의 감각을 쓸모없게 만들었다.', "expanding the reach of our current senses", '불일치 → 감각을 대체한 게 아니라 넓혀 줌'],
  ['망원경은 먼 빛의 세기를 줄여서 작동한다.', "simply amplifying signals", '불일치 → 신호를 확장함'],
  ['어떤 도구도 인간의 지각 범위 밖의 현상을 감지할 수 없다.', "natural phenomena that we can't perceive with our senses", '불일치 → 바로 그런 현상을 지각하게 하는 게 도구'],],
 [['반대자들은 상관관계가 인과관계를 증명한다는 추론을 지지한다.', "Opponents of research reject this inference", '불일치 → 추론을 거부함'],
  ['옹호자들은 동물 실험이 의학 발전을 가져왔다고 주장한다.', "the former caused the latter", '일치 (the former = 동물 실험, the latter = 의학 발전)'],
  ['법은 신약을 사람에게 쓰기 전에 동물에게 시험하도록 의무화한다.', "the law prescribes that all new drugs", '일치'],
  ['그 상관관계는 진짜 인과관계가 아니라 법적 요구에서 비롯된다.', "is the result of legal necessity, not evidence", '일치'],
  ['몇몇 저명한 의사들은 옹호자들을 반박하는 역사적 증거를 제시한다.', "several influential physicians have offered historical evidence", '일치']],
 [['몇몇 의사들은 동물 연구자들이 인정하는 것보다 임상적 발견이 더 중요한 역할을 했다고 본다.', "clinical discoveries played a more substantial role than animal researchers have led us to believe", '일치'],
  ['반대자들은 현대 의학이 사망률 감소의 유일한 요인이라고 주장한다.', "modern medicine not the only cause for the decline in mortality", '불일치 → "유일한 원인이 아니다"라고 함'],
  ['법에 따라 보철 장치는 동물 실험에서 면제된다.', "all new drugs, prosthetic devices, and surgical techniques be tried on animals", '불일치 → 보철 장치도 동물 시험 대상'],
  ['의사들의 증거는 옹호자들의 주장을 뒷받침한다.', "has not been as responsible for biomedical discovery as defenders suggest", '불일치 → 오히려 반박함'],
  ['반대자들은 동물 실험이 법으로 금지되어 있다고 믿는다.', "the law prescribes that all new drugs", '불일치 → 법은 오히려 동물 실험을 요구함']],
]}

s = open(P, encoding='utf-8').read()
days = s.split("id: 'd")
for di in (1, 2, 3):
    b = days[di]
    # order / insert: flow
    it = iter(ORDER[di])
    b, n = re.subn(r"(\{ lines: \[.*\]) \}", lambda m: m.group(1) + ', flow: ' + J(next(it)) + ' }', b); assert n == len(ORDER[di]), (di, 'order', n)
    it = iter(INSERT[di])
    b, n = re.subn(r"given: (\d+), ex:", lambda m: 'given: ' + m.group(1) + ', flow: ' + J(next(it)) + ', ex:', b); assert n == len(INSERT[di]), (di, 'insert', n)
    # tf ev: 4th element n ] → , ev ]
    a = b.index("type: 'tf'"); e = b.index("]},", a); blk = b[a:e]
    it = iter(TFEV[di])
    blk, n = re.subn(r", (\d\d)\](,?)\n", lambda m: ', ' + m.group(1) + ', ' + J(next(it)) + ']' + m.group(2) + '\n', blk); assert n == len(TFEV[di]), (di, 'tf', n)
    b = b[:a] + blk + b[e:]
    # 실전 / 일치: per
    for title, DATA in (("'실전 문항'", REAL), ("'일치·불일치'", M)):
        a = b.index("title: " + title); e = b.index("]},", a); blk = b[a:e]
        lines = blk.split('\n'); it = iter(DATA[di]); n = 0
        for k, ln in enumerate(lines):
            if ln.lstrip().startswith('{ n: '):
                assert ln.rstrip().endswith('}') or ln.rstrip().endswith('},')
                tail = ',' if ln.rstrip().endswith(',') else ''
                core = ln.rstrip()[:-1] if tail else ln.rstrip()
                lines[k] = core[:-1].rstrip() + ', per: ' + J(next(it)) + ' }' + tail; n += 1
        assert n == len(DATA[di]), (di, title, n)
        b = b[:a] + '\n'.join(lines) + b[e:]
    days[di] = b
open(P, 'w', encoding='utf-8').write("id: 'd".join(days))
print('ok')
