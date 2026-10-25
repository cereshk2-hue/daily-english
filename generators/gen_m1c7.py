import sys, re
sys.path.insert(0, '/tmp/claude-0/-home-claude/a9e3e882-1f02-5d62-8f70-aced81bc59d2/scratchpad')
from gencommon import *

# 중1 천재(소영순) Lesson 7 Love for Art · 본문 Henri's Scissors
S1 = [("In a small town in France, there lived a young boy.", "프랑스의 작은 마을에 어린 소년이 살았다."),
      ("His name was Henri Matisse.", "그의 이름은 Henri Matisse였다."),
      ("He liked to draw pictures.", "그는 그림 그리는 것을 좋아했다."),
      ("He drew pictures in the sand and in his books.", "그는 모래와 그의 책에 그림을 그렸다."),
      ("When Matisse grew up, he left his town and became an artist in Paris.", "Matisse가 어른이 되었을 때, 그는 마을을 떠나 파리에서 화가가 되었다."),
      ("He painted pictures day after day and year after year.", "그는 날마다, 해마다 그림을 그렸다."),
      ("He was happy with his life.", "그는 그의 삶에 행복해했다."),
      ("More and more people began to notice him.", "점점 더 많은 사람들이 그를 알아보기 시작했다."),
      ("They loved his paintings, and soon he became famous.", "그들은 그의 그림을 사랑했고 곧 그는 유명해졌다.")]
S2 = [("When Matisse became an old man, he fell ill.", "Matisse가 노인이 되었을 때, 그는 병에 걸렸다."),
      ("He could only lie in bed and sleep.", "그는 침대에 누워 잠만 잘 수 있었다."),
      ("He couldn't paint at all.", "그는 그림을 전혀 그릴 수 없었다."),
      ("He could only paint in his dreams.", "그는 오직 그의 꿈속에서만 그릴 수 있었다."),
      ("When Matisse opened his eyes, they were full of sadness.", "Matisse가 눈을 떴을 때, 그의 눈은 슬픔으로 가득 차 있었다."),
      ("Luckily, before long, he could sit.", "다행히도, 얼마 지나지 않아 그는 앉을 수 있었다."),
      ("A little later, he started to paint again.", "조금 후에, 그는 다시 그림을 그리기 시작했다."),
      ("However, he realized that he couldn't paint well anymore.", "하지만 그는 더 이상 그림을 잘 그릴 수 없다는 것을 깨달았다.")]
S3 = [("One day, Matisse got a brilliant idea.", "어느 날, Matisse는 멋진 생각을 해냈다."),
      ("He picked up scissors, cut some paper, and made beautiful shapes.", "그는 가위를 집어 들어 종이를 자르고, 아름다운 모양을 만들었다."),
      ("He cut out birds and flowers.", "그는 새와 꽃을 잘라 냈다."),
      ("He was drawing with SCISSORS!", "그는 가위로 그림을 그리고 있었다!"),
      ("He said to himself, \"My pleasure in cutting things grows and grows.", "그는 자기 자신에게 말했다. “무엇인가를 오려 내는 나의 기쁨이 더욱 커지고 있어."),
      ("Scissors gave me another chance.\"", "가위는 내게 또 다른 기회를 주었어.”"),
      ("Matisse cut paper all day.", "Matisse는 하루 종일 종이를 잘랐다.")]
S4 = [("Soon his room was full of shapes and colors.", "곧 그의 방은 모양과 색채로 가득 찼다."),
      ("\"I stay in bed most of the time, but I made a small paper garden all around me.", "“나는 대부분 시간을 침대에 머물러 있지만, 온 주변에 작은 종이 정원을 만들었어."),
      ("There are leaves, fruits, and birds ... I am really happy,\" he thought.", "나뭇잎, 과일, 그리고 새들이 있지 … 난 정말 행복해.”라고 그는 생각했다."),
      ("Perhaps Matisse is still using scissors to cut out stars in heaven.", "아마도 Matisse는 여전히 천국에서 별을 오리기 위해 가위를 사용하고 있을 것이다."),
      ("Look at the night sky.", "밤하늘을 봐."),
      ("Some of the stars may come from his scissors.", "별들 중 일부는 그의 가위에서 나온 것일지도 모른다.")]

# ═════════════ DAY 3 · 7과 본문 ❶❷ ═════════════
d3 = steps(
 vocab=[['scissors', '가위', '❶'], ['town', '마을, 읍', '❶'], ['young', '어린', '❶'], ['draw', '그리다 (과거 drew)', '❶'],
        ['picture', '그림', '❶'], ['sand', '모래', '❶'], ['grow up', '(성인으로) 자라다 (과거 grew up)', '❶'], ['leave', '떠나다 (과거 left)', '❶'],
        ['artist', '화가, 예술가', '❶'], ['day after day', '날마다, 매일매일', '❶'], ['year after year', '해마다, 매년', '❶'], ['be happy with', '~에 만족하다', '❶'],
        ['more and more', '점점 더 많은', '❶'], ['notice', '알아차리다, 주목하다', '❶'], ['famous', '유명한', '❶'], ['fall ill', '병에 걸리다 (과거 fell ill)', '❷'],
        ['lie', '누워 있다', '❷'], ['not ~ at all', '전혀 ~ 아니다', '❷'], ['dream', '꿈', '❷'], ['be full of', '~으로 가득 차다', '❷'],
        ['sadness', '슬픔', '❷'], ['luckily', '다행히도', '❷'], ['before long', '곧, 머지않아', '❷'], ['a little later', '잠시 후, 조금 있다가', '❷'],
        ['however', '그러나', '❷'], ['realize', '깨닫다', '❷'], ['not ~ anymore', '더 이상 ~않다', '❷']],
 pickv=[
  ("In a small town in France, there lived a {young|old} boy.", "어린 소년 → young (old 나이 든)"),
  ("He drew pictures in the {sand|sky} and in his books.", "모래에 그림을 그림 → sand"),
  ("When Matisse grew up, he {left|stayed} his town and became an artist in Paris.", "마을을 '떠나' 파리로 감 → left (stay 머무르다)"),
  ("More and more people began to {notice|forget} him.", "점점 많은 사람들이 '알아보기' 시작함 → notice"),
  ("They loved his paintings, and soon he became {famous|poor}.", "그림을 사랑함 → 곧 '유명해짐' famous"),
  ("When Matisse became an old man, he fell {ill|asleep}.", "fall ill 병에 걸리다"),
  ("When Matisse opened his eyes, they were full of {sadness|happiness}.", "그림을 그릴 수 없었음 → 슬픔(sadness)"),
  ("{Luckily|Sadly}, before long, he could sit.", "다시 앉을 수 있게 됨 → 다행히도(Luckily)"),
  ("However, he {realized|forgot} that he couldn't paint well anymore.", "realize 깨닫다"),
 ],
 tf=[
  ["Henri Matisse lived in a small town in France when he was young.", True, "프랑스의 작은 마을에 살던 어린 소년이었다.", '❶', "In a small town in France, there lived a young boy"],
  ["Henri Matisse liked to write poems when he was a boy.", False, "시가 아니라 그림 그리는 것(to draw pictures)을 좋아했다.", '❶', "He liked to draw pictures"],
  ["Matisse became an artist in his small town.", False, "마을을 떠나 파리(Paris)에서 화가가 되었다.", '❶', "he left his town and became an artist in Paris"],
  ["Matisse painted pictures every day for many years.", True, "날마다, 해마다(day after day and year after year) 그렸다.", '❶', "He painted pictures day after day and year after year"],
  ["More and more people loved Matisse's paintings.", True, "사람들이 그의 그림을 사랑했다.", '❶', "They loved his paintings"],
  ["Matisse fell ill when he was a young artist.", False, "노인이 되었을 때(became an old man) 병에 걸렸다.", '❷', "When Matisse became an old man, he fell ill"],
  ["Matisse's eyes were full of happiness when he opened them.", False, "슬픔(sadness)으로 가득 차 있었다.", '❷', "they were full of sadness"],
  ["Matisse started to paint again, but he couldn't paint well anymore.", True, "다시 그리기 시작했지만 더 이상 잘 그릴 수 없었다.", '❷', "he realized that he couldn't paint well anymore"],
 ],
 ilchi=[
  {'n': '❶', 'box': ['❶'], 'q': "Henri Matisse에 관한 내용과 일치하지 <u>않는</u> 것은?",
   'opts': ["He drew pictures only on paper when he was young.", "He was born and grew up in a small town in France.", "He moved to Paris and became an artist.", "He was satisfied with his life as an artist.", "He gradually gained fame as more people noticed him."],
   'ex': "정답 근거: He drew pictures in the sand and in his books. (종이에만 그린 게 아니라 모래와 책에 그림)\n· be satisfied with = be happy with ~에 만족하다 · gradually 점차 · gain fame 명성을 얻다",
   'per': [["그는 어렸을 때 종이에만 그림을 그렸다.", "He drew pictures in the sand and in his books", "불일치 → 모래와 책에 그림"],
           ["그는 프랑스의 작은 마을에서 자랐다.", "In a small town in France, there lived a young boy", "일치"],
           ["그는 파리로 가서 화가가 되었다.", "he left his town and became an artist in Paris", "일치 (move to 이사하다)"],
           ["그는 화가로서의 삶에 만족했다.", "He was happy with his life", "일치 (be satisfied with = be happy with)"],
           ["더 많은 사람들이 알아보면서 그는 점차 유명해졌다.", "More and more people began to notice him", "일치 (gain fame = become famous)"]]},
  {'n': '❷', 'box': ['❷'], 'q': "글의 내용과 <u>일치하는</u> 것은?",
   'opts': ["When Matisse got sick, he could do nothing but stay in bed and sleep.", "Matisse painted many pictures while he was in bed.", "Matisse felt delighted when he woke up from his dreams.", "Matisse could never sit again after he fell ill.", "Matisse painted better than before when he started again."],
   'ex': "정답 근거: He could only lie in bed and sleep.\n· do nothing but ~ ~만 하다 · delighted 매우 기쁜 · fall ill = get sick 병에 걸리다",
   'per': [["Matisse는 병에 걸렸을 때 침대에 누워 자는 것밖에 할 수 없었다.", "He could only lie in bed and sleep", "일치 (do nothing but ~ = ~만 하다)"],
           ["Matisse는 침대에 있는 동안 많은 그림을 그렸다.", "He couldn't paint at all", "불일치 → 전혀 그릴 수 없었음"],
           ["Matisse는 꿈에서 깼을 때 매우 기뻤다.", "they were full of sadness", "불일치 → 슬픔으로 가득"],
           ["Matisse는 병에 걸린 뒤 다시는 앉을 수 없었다.", "Luckily, before long, he could sit", "불일치 → 곧 앉을 수 있었음"],
           ["Matisse는 다시 그리기 시작했을 때 전보다 더 잘 그렸다.", "he couldn't paint well anymore", "불일치 → 더 이상 잘 그릴 수 없었음"]]},
 ],
 pickg=[
  ("In a small town in France, there {lived|living} a young boy.", "there + 동사 + 주어: ~가 살았다 → lived"),
  ("He {drew|drawed} pictures in the sand and in his books.", "draw - drew - drawn (불규칙)"),
  ("When Matisse grew up, he left his town and {became|becomes} an artist in Paris.", "left(과거)와 병렬 → became"),
  ("He was happy {with|to} his life.", "be happy with ~에 만족하다"),
  ("More and more people began {to notice|noticed} him.", "begin + to부정사"),
  ("He could only lie in bed and {sleep|slept}.", "could + 동사원형 (lie와 병렬)"),
  ("When Matisse opened his eyes, they were full {of|with} sadness.", "be full of ~으로 가득 차다"),
  ("A little later, he started {to paint|painted} again.", "start + to부정사/동명사"),
  ("However, he realized {that|what} he couldn't paint well anymore.", "realize + that절 (목적어)"),
 ],
 verb=[
  ("He liked ___ pictures.", 'draw', ['to draw', 'drawing'], "like + to부정사/동명사 (본문: to draw)"),
  ("He ___ pictures day after day and year after year.", 'paint', ['painted'], "규칙 동사 과거 -ed"),
  ("When Matisse ___ up, he left his town and became an artist in Paris.", 'grow', ['grew'], "grow - grew - grown (과거)"),
  ("When Matisse grew up, he ___ his town and became an artist in Paris.", 'leave', ['left'], "leave - left - left (과거)"),
  ("They ___ his paintings, and soon he became famous.", 'love', ['loved'], "e로 끝나는 동사 + d → loved"),
  ("When Matisse became an old man, he ___ ill.", 'fall', ['fell'], "fall - fell - fallen (과거)"),
  ("He could only ___ in bed and sleep.", 'lie', ['lie'], "could + 동사원형"),
  ("When Matisse ___ his eyes, they were full of sadness.", 'open', ['opened'], "과거의 일 → opened"),
 ],
 error=[
  ("When Matisse [[grew]] up, he [[leaved]] his town and [[became]] an artist [[in]] Paris.", 1, 'left', "leave - left - left (불규칙)"),
  ("He [[painted]] pictures day [[after]] day and year after year. He [[was]] happy [[to]] his life.", 3, 'with', "be happy with ~에 만족하다"),
  ("More and more people [[began]] [[to notice]] him. They [[loved]] his paintings, and soon he became [[fame]].", 3, 'famous', "become + 형용사 → famous"),
  ("He [[couldn't]] paint [[at all]]. He could only [[painted]] in his [[dreams]].", 2, 'paint', "조동사 could + 동사원형"),
  ("A little later, he [[started]] to paint again. However, he [[realized]] [[what]] he couldn't paint [[well]] anymore.", 2, 'that', "realize + that절(~라는 것을)"),
 ],
 scr=[(e(S1, 0), S1[0][1]), (e(S1, 4), S1[4][1]), (e(S1, 7), S1[7][1]), (e(S2, 0), S2[0][1]), (e(S2, 4), S2[4][1]), (e(S2, 7), S2[7][1])],
 order=[
  ([e(S1, 0), e(S1, 1), e(S1, 2), e(S1, 3)], ["프랑스 작은 마을의 어린 소년", "그의 이름은 Henri Matisse", "그림 그리기를 좋아함", "모래와 책에 그림을 그림"]),
  ([e(S1, 4), e(S1, 5), e(S1, 7), e(S1, 8)], ["어른이 되어 파리에서 화가가 됨", "날마다, 해마다 그림을 그림", "점점 많은 사람들이 알아봄", "그림을 사랑했고 곧 유명해짐"]),
  ([e(S2, 0), e(S2, 1), e(S2, 4), e(S2, 5), e(S2, 7)], ["노인이 되어 병에 걸림", "침대에 누워 잠만 잘 수 있었음", "눈을 뜨면 슬픔으로 가득", "다행히 곧 앉을 수 있었음", "더 이상 잘 그릴 수 없다는 걸 깨달음"]),
 ],
 insert=[
  ([e(S1, 1), e(S1, 2), e(S1, 3)], 2, ["그의 이름은 Henri Matisse", "그림 그리기를 좋아함", "모래와 책에 그림(pictures)을 그림"], "그림 그리기를 좋아한다는 내용 뒤에 어디에 그렸는지가 이어진다."),
  ([e(S1, 7), e(S1, 8), e(S2, 0)], 1, ["점점 많은 사람들이 그를 알아봄", "그들(They)은 그의 그림을 사랑했고 곧 유명해짐", "노인이 되어 병에 걸림"], "They는 앞 문장의 More and more people을 가리킨다."),
  ([e(S2, 5), e(S2, 6), e(S2, 7)], 2, ["다행히 곧 앉을 수 있었음", "조금 후 다시 그림을 그리기 시작함", "하지만(However) 더 이상 잘 그릴 수 없었음"], "However는 '다시 그리기 시작했다'는 내용과 반대되는 결과를 이끈다."),
 ],
 odd=[
  ([e(S1, 2), e(S1, 3), "He didn't like drawing at all.", e(S1, 4)], 2, "그림 그리기를 싫어했다 → 그림을 좋아했다는 내용과 반대"),
  ([e(S1, 6), e(S1, 7), "Nobody wanted to see his paintings.", e(S1, 8)], 2, "아무도 그의 그림을 원하지 않았다 → 점점 유명해졌다는 흐름과 반대"),
  ([e(S2, 2), e(S2, 3), "He went to the park and painted every day.", e(S2, 4)], 2, "공원에 가서 매일 그렸다 → 침대에 누워 그릴 수 없었다는 내용과 맞지 않음"),
 ],
 blank=[
  ("When Matisse grew up, he left his town and became ____ in Paris.", ["an artist", "a doctor", "a teacher", "a farmer"], "파리에서 화가가 됨"),
  ("He couldn't paint at all. He could only paint ____.", ["in his dreams", "in the park", "in his school", "with his friends"], "병에 걸려 꿈속에서만 그릴 수 있었음"),
  ("A little later, he started to paint again. However, he realized that ____.", ["he couldn't paint well anymore", "he was a great painter", "he wanted to sleep", "he became famous"], "However → 다시 그렸지만 잘 그릴 수 없었음"),
 ],
 gram=[
  ("우리말과 같도록 할 때 빈칸에 알맞은 것은?<br>마을에 어린 소년이 살았다.<br><b>In a town, ______ lived a young boy.</b>", ['there', 'it', 'he', 'they'], "there + 동사 + 주어: ~가 살았다 (there는 해석하지 않음)"),
  ("우리말과 같도록 할 때 빈칸에 알맞은 것은?<br>그의 눈은 슬픔으로 가득 차 있었다.<br><b>His eyes were full ______ sadness.</b>", ['of', 'with', 'in', 'for'], "be full of ~으로 가득 차다"),
  (B + "When Matisse ______ up, he became an artist.</b>", ['grew', 'grow', 'grows', 'growing'], "과거의 일 → grew (grow - grew - grown)"),
  ("밑줄 친 <b>When</b>의 뜻으로 알맞은 것은?<br><b><u>When</u> Matisse opened his eyes, they were full of sadness.</b>", ['~할 때', '언제', '어디서', '왜'], "접속사 when: ~할 때 (시간의 부사절)"),
  (B + "Soon he became ______.</b>", ['famous', 'fame', 'famously', 'more famous than'], "become + 형용사(보어)"),
  ("두 문장의 뜻이 같도록 할 때 빈칸에 알맞은 것은?<br><b>He could only lie in bed.<br>= He was only ______ to lie in bed.</b>", ['able', 'can', 'could', 'ability'], "could = was/were able to"),
  ("우리말과 같도록 할 때 빈칸에 알맞은 것은?<br>그는 더 이상 그림을 잘 그릴 수 없었다.<br><b>He couldn't paint well ______.</b>", ['anymore', 'at all', 'again', 'already'], "not ~ anymore 더 이상 ~않다"),
 ])

# ═════════════ DAY 4 · 7과 본문 ❸❹ ═════════════
d4 = steps(
 vocab=[['get an idea', '생각이 나다 (과거 got)', '❸'], ['brilliant', '멋진, 훌륭한', '❸'], ['pick ~ up', '~을 집어 들다', '❸'], ['cut', '자르다 (과거 cut)', '❸'],
        ['beautiful', '아름다운', '❸'], ['shape', '모양', '❸'], ['cut ~ out', '~을 오려내다', '❸'], ['say to oneself', '혼잣말을 하다, 마음속으로 생각하다', '❸'],
        ['pleasure', '기쁨, 즐거움', '❸'], ['grow and grow', '점점 더 커지다', '❸'], ['another', '또 다른', '❸'], ['chance', '기회', '❸'],
        ['all day', '하루 종일', '❸'], ['color', '색, 색채', '❹'], ['stay', '머무르다', '❹'], ['most of the time', '대부분의 시간', '❹'],
        ['garden', '정원', '❹'], ['all around ~', '~의 주변 일대에', '❹'], ['leaf', '잎, 나뭇잎 (복수 leaves)', '❹'], ['fruit', '과일', '❹'],
        ['perhaps', '아마, 어쩌면', '❹'], ['still', '아직도, 여전히', '❹'], ['heaven', '천국', '❹'], ['night sky', '밤하늘', '❹'],
        ['some of ~', '~ 중 일부', '❹'], ['come from', '~에서 나오다', '❹']],
 pickv=[
  ("One day, Matisse got a {brilliant|terrible} idea.", "멋진 생각 → brilliant"),
  ("He {picked|put} up scissors, cut some paper, and made beautiful shapes.", "pick ~ up ~을 집어 들다"),
  ("He cut {out|off} birds and flowers.", "cut ~ out ~을 오려내다"),
  ("He said to himself, \"My {pleasure|pain} in cutting things grows and grows.", "오려 내는 '기쁨'이 커짐 → pleasure"),
  ("Scissors gave me another {chance|problem}.", "또 다른 '기회' → chance"),
  ("Soon his room was full of {shapes|books} and colors.", "오려 낸 '모양'과 색채로 가득 → shapes"),
  ("I {stay|work} in bed most of the time, but I made a small paper garden all around me.", "대부분 침대에 '머물러' 있음 → stay"),
  ("{Perhaps|Never} Matisse is still using scissors to cut out stars in heaven.", "아마도 → Perhaps"),
  ("Some of the stars may {come|go} from his scissors.", "come from ~에서 나오다"),
 ],
 tf=[
  ["Matisse got a brilliant idea one day.", True, "어느 날 멋진 생각을 해냈다.", '❸', "One day, Matisse got a brilliant idea"],
  ["Matisse put down scissors and picked up brushes again.", False, "가위를 집어 들었다(picked up scissors).", '❸', "He picked up scissors"],
  ["Matisse made shapes of birds and flowers with scissors.", True, "새와 꽃을 오려 냈다.", '❸', "He cut out birds and flowers"],
  ["Matisse felt happy when he cut things out.", True, "오려 내는 기쁨이 점점 커졌다.", '❸', "My pleasure in cutting things grows and grows"],
  ["Matisse cut paper for only an hour a day.", False, "하루 종일(all day) 종이를 잘랐다.", '❸', "Matisse cut paper all day"],
  ["Matisse was in his garden all day.", False, "대부분 침대에 머물렀다(stay in bed).", '❹', "I stay in bed most of the time"],
  ["Matisse made a paper garden near his bed.", True, "온 주변에 작은 종이 정원을 만들었다.", '❹', "I made a small paper garden all around me"],
  ["Maybe Matisse is still painting with brushes in heaven.", False, "붓이 아니라 가위로 별을 오리고 있을 것이다.", '❹', "Perhaps Matisse is still using scissors to cut out stars in heaven"],
 ],
 ilchi=[
  {'n': '❸', 'box': ['❸'], 'q': "Matisse에 관한 내용과 일치하지 <u>않는</u> 것은?",
   'opts': ["He used scissors only for a short time each day.", "He came up with a creative idea.", "He made beautiful shapes out of paper.", "He thought scissors gave him a new opportunity.", "His joy kept growing as he cut things out."],
   'ex': "정답 근거: Matisse cut paper all day. (짧은 시간이 아니라 하루 종일)\n· come up with ~을 생각해 내다 · opportunity = chance 기회 · creative 창의적인",
   'per': [["그는 하루에 잠깐씩만 가위를 사용했다.", "Matisse cut paper all day", "불일치 → 하루 종일"],
           ["그는 창의적인 생각을 해냈다.", "One day, Matisse got a brilliant idea", "일치 (come up with = get an idea)"],
           ["그는 종이로 아름다운 모양을 만들었다.", "cut some paper, and made beautiful shapes", "일치"],
           ["그는 가위가 새로운 기회를 주었다고 생각했다.", "Scissors gave me another chance", "일치 (opportunity = chance)"],
           ["무엇인가를 오려 낼수록 그의 기쁨이 계속 커졌다.", "My pleasure in cutting things grows and grows", "일치"]]},
  {'n': '❹', 'box': ['❹'], 'q': "글의 내용과 <u>일치하는</u> 것은?",
   'opts': ["Matisse created a garden of paper around his bed.", "Matisse's room was empty and dark.", "Matisse went outside to pick leaves and fruits.", "Matisse felt lonely in his small room.", "The writer says all the stars came from Matisse's scissors."],
   'ex': "정답 근거: I made a small paper garden all around me.\n· create 만들다 · empty 텅 빈 · lonely 외로운",
   'per': [["Matisse는 침대 주변에 종이 정원을 만들었다.", "I made a small paper garden all around me", "일치 (create = make)"],
           ["Matisse의 방은 텅 비고 어두웠다.", "Soon his room was full of shapes and colors", "불일치 → 모양과 색채로 가득"],
           ["Matisse는 밖에 나가 나뭇잎과 과일을 따 왔다.", "I stay in bed most of the time", "불일치 → 대부분 침대에 머묾 (종이로 만든 것)"],
           ["Matisse는 작은 방에서 외로웠다.", "I am really happy", "불일치 → 정말 행복함"],
           ["글쓴이는 모든 별이 Matisse의 가위에서 나왔다고 말한다.", "Some of the stars may come from his scissors", "불일치 → 일부(Some)가 나왔을지도 모름"]]},
 ],
 pickg=[
  ("He picked up scissors, cut some paper, and {made|make} beautiful shapes.", "picked, cut과 병렬 → 과거 made"),
  ("He {was|is} drawing with SCISSORS!", "과거진행형 was + -ing"),
  ("He said to {himself|him}, \"My pleasure in cutting things grows and grows.", "주어 He = 말하는 대상 → 재귀대명사 himself"),
  ("My pleasure in {cutting|cut} things grows and grows.", "전치사 in + 동명사"),
  ("My pleasure in cutting things {grows|grow} and grows.", "주어 My pleasure(단수) → grows"),
  ("Scissors gave {me|to me} another chance.", "give + 간접목적어 + 직접목적어"),
  ("Soon his room was full {of|with} shapes and colors.", "be full of ~으로 가득 차다"),
  ("There {are|is} leaves, fruits, and birds ...", "There + be동사 + 복수 주어 → are"),
  ("Perhaps Matisse is still using scissors {to cut|cut} out stars in heaven.", "목적(~하기 위해) → to부정사"),
  ("Some of the stars may {come|comes} from his scissors.", "조동사 may + 동사원형"),
 ],
 verb=[
  ("One day, Matisse ___ a brilliant idea.", 'get', ['got'], "get - got - got(ten) (과거)"),
  ("He picked up scissors, ___ some paper, and made beautiful shapes.", 'cut', ['cut'], "cut - cut - cut (과거도 cut)"),
  ("He was ___ with SCISSORS!", 'draw', ['drawing'], "과거진행형 was + -ing"),
  ("He ___ to himself, \"My pleasure in cutting things grows and grows.", 'say', ['said'], "say - said - said (과거)"),
  ("Scissors ___ me another chance.", 'give', ['gave'], "give - gave - given (과거)"),
  ("Soon his room ___ full of shapes and colors.", 'be', ['was'], "주어 his room(단수) + 과거 → was"),
  ("Perhaps Matisse is still ___ scissors to cut out stars in heaven.", 'use', ['using'], "현재진행형 is + -ing"),
 ],
 error=[
  ("He [[picked]] up scissors, [[cut]] some paper, and [[make]] beautiful [[shapes]].", 2, 'made', "picked, cut과 병렬 → 과거 made"),
  ("He said to [[him]], \"My pleasure [[in]] [[cutting]] things grows and [[grows]].", 0, 'himself', "주어와 같은 대상 → 재귀대명사 himself"),
  ("My pleasure in cutting things [[grow]] and grows. Scissors [[gave]] [[me]] another [[chance]].", 0, 'grows', "주어 My pleasure(단수) → grows"),
  ("Soon his room was full [[with]] shapes and colors. There [[are]] leaves, fruits, and [[birds]] ... I am [[really]] happy.", 0, 'of', "be full of ~으로 가득 차다"),
  ("Perhaps Matisse [[is]] still using scissors [[to cut]] out stars. Some of the stars may [[comes]] [[from]] his scissors.", 2, 'come', "may + 동사원형 → come"),
 ],
 scr=[(e(S3, 0), S3[0][1]), (e(S3, 1), S3[1][1]), (e(S3, 6), S3[6][1]), (e(S4, 0), S4[0][1]), (e(S4, 3), S4[3][1]), (e(S4, 5), S4[5][1])],
 order=[
  ([e(S3, 0), e(S3, 1), e(S3, 2), e(S3, 3)], ["어느 날 멋진 생각을 해냄", "가위를 집어 종이를 잘라 모양을 만듦", "새와 꽃을 오려 냄", "가위로 그림을 그리고 있었음!"]),
  ([e(S3, 4), e(S3, 5), e(S3, 6), e(S4, 0)], ["오려 내는 기쁨이 점점 커짐", "가위가 또 다른 기회를 줌", "하루 종일 종이를 자름", "곧 방이 모양과 색채로 가득 참"]),
  ([e(S4, 3), e(S4, 4), e(S4, 5)], ["아마 천국에서도 가위로 별을 오리고 있을 것", "밤하늘을 봐", "별 중 일부는 그의 가위에서 나왔을지도"]),
 ],
 insert=[
  ([e(S3, 1), e(S3, 2), e(S3, 3)], 2, ["가위로 종이를 잘라 모양을 만듦", "새와 꽃을 오려 냄", "가위로 그림을 그리고 있었음!"], "새와 꽃을 오려 낸 것을 '가위로 그리고 있었다'고 표현한다."),
  ([e(S3, 6), e(S4, 0), e(S4, 1)], 1, ["하루 종일 종이를 자름", "곧(Soon) 방이 모양과 색채로 가득 참", "침대에 있지만 종이 정원을 만들었다"], "하루 종일 자른 결과 곧 방이 모양으로 가득 찼다."),
  ([e(S4, 3), e(S4, 4), e(S4, 5)], 2, ["천국에서 가위로 별을 오리고 있을 것", "밤하늘을 봐", "별들(the stars) 중 일부는 그의 가위에서"], "밤하늘을 보라는 말 뒤에 별 이야기가 이어진다."),
 ],
 odd=[
  ([e(S3, 1), e(S3, 2), "He didn't like using scissors at all.", e(S3, 3)], 2, "가위 쓰기를 싫어했다 → 가위로 그림을 그렸다는 내용과 반대"),
  ([e(S3, 4), e(S3, 5), "He threw away the scissors and went to sleep.", e(S3, 6)], 2, "가위를 버리고 잤다 → 하루 종일 종이를 잘랐다는 흐름과 맞지 않음"),
  ([e(S4, 0), e(S4, 1), "He was very sad because his room was empty.", e(S4, 2)], 2, "방이 비어 슬펐다 → 모양과 색채로 가득 차 행복했다는 내용과 반대"),
 ],
 blank=[
  ("He picked up scissors, cut some paper, and made ____.", ["beautiful shapes", "a big cake", "a new bed", "a loud sound"], "가위로 종이를 잘라 아름다운 모양을 만듦"),
  ("Scissors gave me ____.", ["another chance", "a big problem", "a lot of money", "a bad dream"], "가위가 또 다른 기회를 줌"),
  ("Perhaps Matisse is still using scissors to cut out ____ in heaven.", ["stars", "flowers", "birds", "leaves"], "밤하늘의 별 → stars"),
 ],
 gram=[
  ("우리말과 같도록 할 때 빈칸에 알맞은 것은?<br>어제 그는 종이를 잘랐다.<br><b>Yesterday he ______ paper.</b>", ['cut', 'cutted', 'cuts', 'cutting'], "cut - cut - cut (과거형도 cut)"),
  ("두 문장의 뜻이 같도록 할 때 빈칸에 알맞은 것은?<br><b>Scissors gave me another chance.<br>= Scissors gave another chance ______ me.</b>", ['to', 'for', 'of', 'with'], "give는 3형식 전환 시 전치사 to"),
  (B + "There ______ leaves, fruits, and birds.</b>", ['are', 'is', 'be', 'was'], "There + be동사 + 복수 주어 → are"),
  ("밑줄 친 부분과 쓰임이 <b>같은</b> 것은?<br><b>He is using scissors <u>to cut</u> out stars.</b>", ["She went to the shop <u>to buy</u> paper.", "I want <u>to buy</u> paper.", "My plan is <u>to buy</u> paper.", "He liked <u>to buy</u> paper."], "목적(~하기 위해)의 부사적 용법"),
  ("밑줄 친 <b>may</b>의 뜻으로 알맞은 것은?<br><b>Some of the stars <u>may</u> come from his scissors.</b>", ['~일지도 모른다', '~해야 한다', '~할 수 있었다', '~하지 않았다'], "may: ~일지도 모른다 (추측)"),
  ("다음 중 어법상 <b>틀린</b> 문장은?", ["He picked up them.", "He picked them up.", "He picked up scissors.", "He picked scissors up."], "목적어가 대명사면 동사 + 대명사 + 부사 → picked them up"),
  (B + "My pleasure in ______ things grows and grows.</b>", ['cutting', 'cut', 'to cut', 'cuts'], "전치사 in 뒤 → 동명사 cutting"),
 ])

SUMQ = '다음 글의 내용을 한 문장으로 요약할 때, 빈칸 (A), (B)에 들어갈 말로 가장 알맞은 것은?'
def SUMSTEP(items):
    return {'type': 'mc', 'title': '요약문 완성', 'guide': '본문을 읽고 요약문의 빈칸 (A), (B)에 들어갈 말을 고르세요.',
            'items': [{'n': n, 'box': box, 'q': SUMQ + '<br><b>' + s + '</b>', 'opts': o, 'ex': x} for n, box, s, o, x in items]}
d3.append(SUMSTEP([
  ('❶', ['❶'], "Henri Matisse loved drawing as a boy, and after he became an artist in Paris, he grew (A) ______ as more and more people (B) ______ his paintings.",
   ['(A) famous – (B) loved', '(A) famous – (B) hated', '(A) poor – (B) loved', '(A) tired – (B) noticed', '(A) poor – (B) forgot'],
   "근거: More and more people began to notice him. They loved his paintings, and soon he became famous.\n(A) famous 유명한 (B) loved 사랑했다"),
  ('❷', ['❷'], "When Matisse became old and sick, his eyes were full of (A) ______, and though he could (B) ______ again later, he couldn't paint well anymore.",
   ['(A) sadness – (B) sit', '(A) happiness – (B) sit', '(A) sadness – (B) run', '(A) pleasure – (B) sleep', '(A) happiness – (B) run'],
   "근거: they were full of sadness / Luckily, before long, he could sit.\n(A) sadness 슬픔 (B) sit 앉다"),
]))
d4.append(SUMSTEP([
  ('❸', ['❸'], "Matisse found a new way to make art: he cut paper with (A) ______, and he felt they gave him another (B) ______.",
   ['(A) scissors – (B) chance', '(A) brushes – (B) chance', '(A) scissors – (B) problem', '(A) pencils – (B) dream', '(A) brushes – (B) problem'],
   "근거: He picked up scissors ... Scissors gave me another chance.\n(A) scissors 가위 (B) chance 기회"),
  ('❹', ['❹'], "Although Matisse stayed in bed most of the time, he made a small paper (A) ______ around him and felt really (B) ______.",
   ['(A) garden – (B) happy', '(A) garden – (B) lonely', '(A) house – (B) happy', '(A) forest – (B) sad', '(A) house – (B) lonely'],
   "근거: I made a small paper garden all around me. ... I am really happy\n(A) garden 정원 (B) happy 행복한"),
]))

def P(n, rows):
    return [['', n, '']] + [['', a, b] for a, b in rows]

D3 = {'id': 'd3', 'name': 'DAY 3', 'range': '7과 본문 ❶❷', 'story': "Lesson 7 · Henri's Scissors · 화가가 된 소년 · 병에 걸린 Matisse",
      'passage': P('❶', S1) + P('❷', S2), 'steps': d3}
D4 = {'id': 'd4', 'name': 'DAY 4', 'range': '7과 본문 ❸❹', 'story': "Lesson 7 · 가위로 그리는 그림 · 종이 정원과 밤하늘의 별",
      'passage': P('❸', S3) + P('❹', S4), 'steps': d4}

path = '/home/claude/proj/data/m1-chunjae-so-L6.js'
src = open(path).read()
assert "id: 'd3'" not in src
tail = '\n  ]\n};\n'
assert src.rstrip().endswith(']\n};') or src.endswith(tail), repr(src[-30:])
i = src.rstrip().rfind(']')  # closing of days array
src = src[:i].rstrip() + ',\n  ' + js(D3, '  ') + ',\n  ' + js(D4, '  ') + '\n  ]\n};\n'
src = src.replace("unit: 'Lesson 6',", "unit: 'Lesson 6~7',", 1).replace("title: 'Heroes in Nature',", "title: 'Heroes in Nature · Love for Art',", 1)
src = src.replace("titleKo: '자연에서 일하는 즐거움',", "titleKo: '자연에서 일하는 즐거움 · 예술에 대한 사랑',", 1)
open(path, 'w').write(src)
print('ok')
