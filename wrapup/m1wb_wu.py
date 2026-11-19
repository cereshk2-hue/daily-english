# 11/19 중산중1 동아(윤정미) 실전 문법 — 시간 접속사 when · before · after 1·2·3차 (각 20문항) · 출처 표시 CS
# 원본: 선생님 학습지 ______1.hwp(when, 시간 접속사) · ______2.hwp(접속사 When) · ______2-1.hwp(while 두 가지 의미) · _____.hwp(when/while) → work/wba/*.txt
# 범위(선생님: when before after): 접속사 when(~할 때) / 의문사 when(언제) 구별, before(~하기 전에) · after(~한 후에) 뜻과 문장 바꾸기,
#   시간 부사절은 미래라도 현재 시제(주절은 will), 부사절이 앞에 오면 콤마. 7과 본문: gets too excited when ~ / when recording ~ / My work begins after the shooting is over
# 뺀 것: while · as · until · since · as soon as(답으로 안 냄), when to부정사
import sys; sys.path.insert(0, '/home/claude/srcrepo/wrapup')
from wu_m1to import *
H = ('실전 문법', '중1 영어 동아(윤정미) 접속사 when · before · after', '동아(윤정미) when · before · after CS', 'm1wb')
B = lambda *ls: BOX('<br>'.join(ls))
NUMS = ['1개', '2개', '3개', '4개', '5개']
W_, BA, TN, K_ = '접속사 when', 'before · after', '시제', '쓰임 구별'
NOTE = '범위: 시간 접속사 when(~할 때) · before(~하기 전에) · after(~한 후에), 의문사 when(언제)과 구별, 시간 부사절의 현재 시제. 문장 전체를 끝까지 읽고 고르세요.'
t = lambda x: x.replace('[', '<u>').replace(']', '</u>')

# ═══════════════ 1차 (기본) ═══════════════
T = Test('1', '1차', '접속사 when · before · after', 'when · before · after', NOTE, H=H); T.rot0 = 1
T.flex('다음 빈칸에 들어갈 말로 알맞은 것은?', W_, B('Call me ' + BL + ' you get home.'),
 ['when', 'but', 'so', 'or', 'and'],
 "이유 ▶ 집에 도착하면(도착할 때) 전화해 → when + 주어 + 동사.\n오답 ▶ {1}·{2}·{3}·{4} '~할 때'의 뜻이 없음\n포인트 ▶ when + 주어 + 동사 = ~할 때", [])
T.flex('다음 우리말을 영어로 바르게 옮긴 것은?', W_, B('내가 어렸을 때, 나는 수영을 할 수 없었다.'),
 ["When I was young, I couldn't swim.", "When was I young, I couldn't swim.", "I was young when, I couldn't swim.", "After I was young, I couldn't swim.", "Before I was young, I couldn't swim."],
 "이유 ▶ ~할 때 → When + 주어 + 동사(I was young), 앞에 오면 콤마.\n오답 ▶ {1} 접속사 뒤는 '주어 + 동사' 순서 {2} when의 자리 ❌ {3} 어린 후에 ❌ {4} 어리기 전에 ❌\n포인트 ▶ When + 주어 + 동사, 주절", [])
T.flex('다음 빈칸에 들어갈 말로 알맞은 것은?', BA, B('Brush your teeth ' + BL + ' you go to bed.'),
 ['before', 'after', 'but', 'so', 'because'],
 "이유 ▶ 자러 가기 전에 이를 닦아라 → before.\n오답 ▶ {1} 자러 간 후에 닦는 건 어색 {2}·{3}·{4} 시간의 뜻이 아님\n포인트 ▶ before = ~하기 전에", [])
T.flex('다음 빈칸에 들어갈 말로 알맞은 것은?', BA, B('He felt full ' + BL + ' he ate three hamburgers.'),
 ['after', 'before', 'but', 'or', 'so'],
 "이유 ▶ 햄버거를 세 개 먹은 후에 배가 불렀다 → after.\n오답 ▶ {1} 먹기 전에 배가 부른 건 어색 {2}·{3}·{4} 시간의 뜻이 아님\n포인트 ▶ after = ~한 후에", [])
T.flex('다음 밑줄 친 When이 접속사(~할 때)로 쓰인 것은?', K_, '',
 [t('[When] he saw me, he ran away.'), t('[When] did you get up today?'), t('[When] is your birthday?'), t('I wonder [when] she will come back.'), t('[When] will you come?')],
 "이유 ▶ When + 주어 + 동사, 주절 → ~할 때(접속사).\n오답 ▶ {1}·{2}·{4} 의문문 '언제' {3} '언제 돌아올지'(의문사)\n포인트 ▶ 물음표 의문문의 When = 언제", [])
T.flex('다음 빈칸에 들어갈 말로 알맞은 것은?', TN, B('When I ' + BL + " home, I'll call you."),
 ['get', 'will get', 'got', 'getting', 'to get'],
 "이유 ▶ 시간을 나타내는 when절은 미래의 일이라도 현재 시제 → get.\n오답 ▶ {1} when절에 will ❌ {2} 과거 ❌(주절은 미래) {3}·{4} 동사 자리\n포인트 ▶ When I get home, I'll call you.", [])
T.flex('다음 중 어법상 <u>틀린</u> 것은?', TN, '',
 ['My mother will pick you up when she will finish her work.', 'When school is over, we will go to the gym.', 'He came when I was not at home.', 'My father died when I was a small boy.', 'When I am tired, I get some sleep.'],
 "이유 ▶ 시간 부사절은 현재 시제 → when she finishes her work.\n오답 ▶ {1} is ✔ {2}·{3} 과거 일은 과거 ✔ {4} 늘 하는 일은 현재 ✔\n포인트 ▶ when절 안에 will ❌", [])
T.flex('두 문장을 when을 써서 한 문장으로 바르게 바꾼 것은?', W_, B('I was on my way home. I met him.'),
 ['I met him when I was on my way home.', 'I met him when was I on my way home.', 'I met when him I was on my way home.', 'I met him after I was on my way home.', 'When I met him I was, on my way home.'],
 "이유 ▶ 집에 오는 길에 그를 만났다 → I met him + when I was on my way home.\n오답 ▶ {1} 주어 + 동사 순서 {2} when의 자리 ❌ {3} 뜻이 달라짐 {4} 콤마 자리 ❌\n포인트 ▶ 주절 + when + 주어 + 동사", [])
T.flex('다음 중 빈칸에 when을 쓸 수 <u>없는</u> 것은?', W_, '',
 ['I hope ' + BL + ' you will get better soon.', BL + ' I prepared dinner, he was watering the plants.', "I'll help you " + BL + ' I finish doing the dishes.', 'I was happy ' + BL + ' I got a birthday present.', 'We went to Disneyland ' + BL + ' we traveled to America.'],
 "이유 ▶ '네가 곧 나아지기를' 바란다 → hope의 목적어 that절. when(~할 때)은 쓸 수 없음.\n오답 ▶ {1}·{2}·{3}·{4} '~할 때'로 자연스러움\n포인트 ▶ that = ~라는 것(~하기를) / when = ~할 때", [])
T.flex('다음 빈칸에 들어갈 말로 알맞은 것은?', W_, B(BL + ' Jane was a student, she studied English hard.'),
 ['When', 'Before', 'After', 'But', 'So'],
 "이유 ▶ Jane이 학생이었을 때 영어를 열심히 공부했다 → When.\n오답 ▶ {1} 학생이기 전에 {2} 학생이었던 후에 → 어색 {3}·{4} 문장 맨 앞에서 두 문장을 이을 수 없음\n포인트 ▶ When + 주어 + 동사, 주절", [])
T.flex('다음 우리말을 영어로 바르게 옮긴 것은?', BA, B('그는 숙제를 끝낸 후에 TV를 봤다.'),
 ['He watched TV after he finished his homework.', 'He watched TV before he finished his homework.', 'He finished his homework after he watched TV.', 'He watched TV when he will finish his homework.', 'After he watched TV, he finished his homework.'],
 "이유 ▶ 숙제를 끝낸 후에 → after he finished his homework.\n오답 ▶ {1} 끝내기 전에 {2}·{4} TV를 먼저 봄(순서 반대) {3} 과거 일에 will ❌\n포인트 ▶ A after B = B 하고 나서 A", [])
T.flex('다음 중 어법상 <u>옳은</u> 것은?', TN, '',
 ['When you feel sad, cry loudly.', "I'll take a good rest when I'll have a cold.", 'When Mom will come home, I will leave.', 'He felt surprised when the accident happens.', 'When I will be free, I will call you.'],
 "이유 ▶ When + 현재 시제, 명령문 ✔\n오답 ▶ {1}·{2}·{4} when절에 will ❌ {3} 과거 일 → happened\n포인트 ▶ 시간 부사절: 미래라도 현재 시제", [])
T.flex('다음 밑줄 친 When과 쓰임이 같은 것은?', K_, B(t('[When] Mom came home, I was talking on the phone.')),
 [t('I listened to music [when] I was lonely.'), t("[When] is Jenny's birthday?"), t('[When] do you think she is coming?'), t('[When] is Joe going to move to Daegu?'), t('Do you know [when] the store opens?')],
 "이유 ▶ 보기와 정답 모두 '~할 때'(접속사).\n오답 ▶ {1}·{2}·{3} '언제'(의문문) {4} '언제 문을 여는지'(의문사)\n포인트 ▶ when 뒤에 '주어 + 동사'가 오고 '~할 때'로 해석되면 접속사", [])
T.flex('다음 밑줄 친 when의 의미가 나머지 넷과 <u>다른</u> 것은?', K_, '',
 [t('I was playing tennis [when] you called me.'), t('[When] is your birthday?'), t('Do you know [when] the movie begins?'), t('[When] did you start piano lessons?'), t("I don't know [when] he will come.")],
 "이유 ▶ 네가 전화했을 때 → '~할 때'(접속사).\n오답 ▶ {1}~{4} 모두 '언제'(의문사)\n포인트 ▶ 언제 vs ~할 때", [])
T.flex('다음 우리말과 같도록 빈칸에 들어갈 말로 알맞은 것은?', BA, B('그들은 영화가 끝나기 전에 잠들었다.', 'They fell asleep ' + BL + ' the movie ended.'),
 ['before', 'after', 'but', 'so', 'because'],
 "이유 ▶ 끝나기 전에 → before.\n오답 ▶ {1} 끝난 후에 {2}·{3}·{4} 시간의 뜻이 아님\n포인트 ▶ before + 주어 + 동사 = ~하기 전에", [])
T.flex('다음 빈칸에 공통으로 들어갈 말로 알맞은 것은?', W_, B("• I wasn't here " + BL + ' you called.', '• ' + BL + ' I first met him, he was a little boy.'),
 ['when', 'before', 'after', 'because', 'but'],
 "이유 ▶ 네가 전화했을 때 / 내가 그를 처음 만났을 때 → when.\n오답 ▶ {1}·{2} 둘째 문장의 뜻이 어색 {3} 이유 {4} 문장 앞에 못 옴\n포인트 ▶ when = ~할 때", [])
T.flex('다음 문장의 밑줄 친 부분을 바르게 고친 것은?', TN, B(t("After you [will take] a piano lesson, you'll have to go to the dentist.")),
 ['take', 'took', 'taking', 'to take', 'will be taken'],
 "이유 ▶ after가 이끄는 시간 부사절 → 미래라도 현재 시제 take.\n오답 ▶ {1} 과거 ❌ {2}·{3} 동사 자리 ❌ {4} 수동 ❌\n포인트 ▶ before · after · when 절 안에 will ❌", [])
T.flex('다음 빈칸에 들어갈 말로 알맞은 것은?', W_, B('Turn off the lights ' + BL + ' you leave the room.'),
 ['when', 'because', 'but', 'or', 'so'],
 "이유 ▶ 방을 나갈 때 불을 꺼라 → when.\n오답 ▶ {1} 이유 {2}·{3}·{4} 시간의 뜻이 아님\n포인트 ▶ 명령문 + when + 주어 + 현재 시제", [])
T.flex('다음 두 문장과 뜻이 같은 것은?', BA, B('I did my homework. Then I went to bed.'),
 ['After I did my homework, I went to bed.', 'Before I did my homework, I went to bed.', 'After I went to bed, I did my homework.', 'I did my homework after I went to bed.', 'When I go to bed, I did my homework.'],
 "이유 ▶ 숙제를 하고 나서(then) 잤다 → After I did my homework, I went to bed.\n오답 ▶ {1}·{2}·{3} 순서가 반대 {4} 시제가 맞지 않음\n포인트 ▶ 먼저 한 일 앞에 after / 나중 일 앞에 before", [])
T.flex('다음 빈칸에 들어갈 말로 알맞은 것은?', W_, B('Max is a great actor, but he sometimes gets too excited ' + BL + ' a lot of people are around.'),
 ['when', 'but', 'or', 'so', 'than'],
 "이유 ▶ 주변에 사람이 많을 때 너무 흥분한다 → when. (7과 본문)\n오답 ▶ {1}·{2}·{3}·{4} '~할 때'의 뜻이 없음\n포인트 ▶ 주절 + when + 주어 + 동사", [])
T.render()

# ═══════════════ 2차 (중상) ═══════════════
T = Test('2', '2차', '접속사 when · before · after', 'when · before · after', NOTE, H=H); T.rot0 = 3
T.flex('다음 문장과 뜻이 같은 것은?', BA, B('The movie ended after they fell asleep.'),
 ['They fell asleep before the movie ended.', 'They fell asleep after the movie ended.', 'The movie ended before they fell asleep.', 'After the movie ended, they fell asleep.', 'They fell asleep when the movie will end.'],
 "이유 ▶ 잠든 후에 영화가 끝났다 = 영화가 끝나기 전에 잠들었다.\n오답 ▶ {1}·{2}·{3} 순서가 반대 {4} 과거 일에 will ❌\n포인트 ▶ A after B = B before A", [])
T.flex('다음 빈칸에 들어갈 말로 알맞은 것은?', BA, B('My work begins ' + BL + ' the shooting is over.'),
 ['after', 'before', 'but', 'or', 'so'],
 "이유 ▶ 편집자의 일은 촬영이 끝난 후에 시작된다 → after. (7과 본문)\n오답 ▶ {1} 촬영이 끝나기 전에 → 편집할 수 없음 {2}·{3}·{4} 시간의 뜻이 아님\n포인트 ▶ after + 주어 + 동사 = ~한 후에", [])
T.flex('다음 중 어법상 <u>틀린</u> 것은?', TN, '',
 ['When he will grow up, he wants to be a rock star.', 'When school is over, I go home.', 'I will be 16 when I graduate from middle school.', 'Before you go out, close the windows.', 'After she had lunch, she took a walk.'],
 "이유 ▶ when절은 현재 시제, 늘 그렇게 바라는 일 → When he grows up.\n오답 ▶ {1} 현재 ✔ {2} 주절 will + when절 현재 ✔ {3} before + 현재, 명령문 ✔ {4} 과거 일 ✔\n포인트 ▶ when · before · after 절 안에 will ❌", [])
T.flex('다음 빈칸에 들어갈 말로 알맞은 것은?', TN, B('I will call you after I ' + BL + ' my homework.'),
 ['finish', 'will finish', 'finished', 'finishing', 'to finish'],
 "이유 ▶ after 시간 부사절 → 미래라도 현재 시제 finish.\n오답 ▶ {1} will ❌ {2} 과거 ❌ {3}·{4} 동사 자리\n포인트 ▶ 주절 will + after/when절 현재", [])
T.flex('다음 밑줄 친 when의 쓰임이 나머지 넷과 <u>다른</u> 것은?', K_, '',
 [t('Do you know [when] the next meeting is?'), t('I feel so happy [when] it snows.'), t('You must visit us [when] you come to Seoul.'), t('[When] I looked at the sky, I saw a bird.'), t('I drink a glass of water [when] I get up.')],
 "이유 ▶ 다음 회의가 언제인지 → 의문사(언제).\n오답 ▶ {1}~{4} 모두 '~할 때'(접속사)\n포인트 ▶ know · wonder · remember + when ~ = 언제 ~인지", [])
T.flex('두 문장을 when을 써서 한 문장으로 바르게 바꾼 것은?', W_, B('Ryan was absent. The class had a test.'),
 ['When Ryan was absent, the class had a test.', 'When was Ryan absent, the class had a test.', 'Ryan was absent when, the class had a test.', 'When Ryan was absent the class, had a test.', 'Ryan when was absent, the class had a test.'],
 "이유 ▶ When + 주어 + 동사, 주절 → When Ryan was absent, the class had a test.\n오답 ▶ {1} 의문문 어순 ❌ {2}·{3}·{4} when · 콤마 자리 ❌\n포인트 ▶ 부사절이 앞에 오면 부사절 끝에 콤마", [])
T.flex('다음 우리말을 영어로 바르게 옮긴 것은?', W_, B('한수가 컴퓨터 게임을 시작했을 때 그의 엄마가 들어오셨다.'),
 ['When Hansu started to play computer games, his mom came in.', 'When did Hansu start to play computer games, his mom came in.', 'Hansu started to play computer games when, his mom came in.', 'When his mom came in, Hansu will start to play computer games.', 'Before Hansu started to play computer games, his mom came in.'],
 "이유 ▶ ~했을 때 → When + 주어 + 동사(과거), 주절(과거).\n오답 ▶ {1} 의문문 어순 ❌ {2} when 자리 ❌ {3} 과거 일에 will ❌ {4} 시작하기 전에 ❌\n포인트 ▶ 과거 일은 when절 · 주절 모두 과거", [])
T.table('(A), (B)에 들어갈 말이 바르게 짝지어진 것은?', BA, B('• Look both ways <b>(A)</b> ______ you cross the street.', '• I felt much better <b>(B)</b> ______ I took the medicine.'),
 ['(A)', '(B)'], [['before', 'after'], ['after', 'before'], ['after', 'after'], ['before', 'before'], ['when', 'before']],
 "이유 ▶ (A) 길을 건너기 전에 양쪽을 봐라 → before (B) 약을 먹은 후에 나아졌다 → after\n오답 ▶ 건넌 후에 양쪽을 보는 건 어색 / 약을 먹기 전에 나아진 건 어색\n포인트 ▶ 일의 순서를 따져 before / after 고르기", [])
T.fixed('다음 <보기>에서 when이 접속사(~할 때)로 쓰인 문장의 개수는?', K_, B(
 '(a) When did your class finish?', '(b) I wonder when he will move into his new house.', "(c) I'll call you when I get back.", '(d) What do you usually do when you have free time?', '(e) I was taking a shower when she knocked on my door.'),
 NUMS, 3,
 "이유 ▶ 접속사: (c)·(d)·(e) 3개.\n오답 ▶ (a) 언제 끝났니(의문사) (b) 언제 이사할지(의문사)\n포인트 ▶ '~할 때'로 해석되면 접속사", [])
T.table('다음 빈칸에 들어갈 말이 바르게 짝지어진 것은?', TN, B('When you ' + BL + ' Jeju-do next year, you ' + BL + ' the beautiful beaches.'),
 ['첫째 빈칸', '둘째 빈칸'], [['visit', 'will see'], ['will visit', 'will see'], ['visited', 'will see'], ['will visit', 'saw'], ['visiting', 'see']],
 "이유 ▶ when절은 미래라도 현재 visit, 주절은 미래 will see (next year).\n오답 ▶ when절에 will ❌ / 미래 일에 과거 ❌ / visiting은 동사가 아님\n포인트 ▶ When + 현재, 주어 + will + 동사원형", [])
T.flex('다음 중 문맥상 <u>어색한</u> 것은?', BA, '',
 ['I got wet before it started to rain.', 'She ate breakfast after she woke up.', 'Take off your shoes before you enter the room.', 'He was tired after he ran 10 km.', 'Think carefully before you answer.'],
 "이유 ▶ 비가 오기 시작하기 전에 젖었다 → 어색. after it started to rain이 자연스러움.\n오답 ▶ {1}·{2}·{3}·{4} 일의 순서가 자연스러움\n포인트 ▶ 먼저 일어난 일 → after 뒤 / 나중 일 → before 뒤", [])
T.flex('다음 중 콤마(,)가 바르게 쓰인 것은?', W_, '',
 ['When I was young, I lived in Busan.', 'When I was young I, lived in Busan.', 'I lived in Busan, when I was, young.', 'When, I was young I lived in Busan.', 'I lived, in Busan when I was young.'],
 "이유 ▶ 부사절(When I was young)이 앞에 오면 그 끝에 콤마.\n오답 ▶ {1}·{2}·{3}·{4} 콤마 자리 ❌\n포인트 ▶ When + 주어 + 동사, 주어 + 동사", [])
T.flex('다음 빈칸에 들어갈 말이 나머지 넷과 <u>다른</u> 것은?', W_, '',
 ['I missed the bus ' + BL + ' I got up late.', 'Jisu smiled ' + BL + ' she saw the puppy.', "I couldn't swim at all " + BL + ' I was young.', BL + ' we arrived at the station, it was dark.', 'My father rides his bike ' + BL + ' he goes to work.'],
 "이유 ▶ 늦게 일어나서 버스를 놓쳤다 → 이유 because. 나머지는 when.\n오답 ▶ {1}·{2}·{3}·{4} '~할 때' → when\n포인트 ▶ when(때) vs because(이유)", [])
T.flex('두 문장을 after를 써서 한 문장으로 바르게 바꾼 것은?', BA, B('I ate dinner. Then I took a shower.'),
 ['After I ate dinner, I took a shower.', 'After I took a shower, I ate dinner.', 'I ate dinner after I took a shower.', 'Before I ate dinner, I took a shower.', 'After I ate dinner I, took a shower.'],
 "이유 ▶ 먼저 한 일(저녁 식사) 앞에 after → After I ate dinner, I took a shower.\n오답 ▶ {1}·{2}·{3} 순서가 반대 {4} 콤마 자리 ❌\n포인트 ▶ After + 먼저 한 일, 나중 일", [])
T.flex('다음 빈칸에 들어갈 말로 알맞은 것은?', W_, B('I create sound effects in my studio ' + BL + ' recording on location is not easy.'),
 ['when', 'before', 'after', 'but', 'so'],
 "이유 ▶ 야외 촬영장에서 녹음하는 것이 쉽지 않을 때 작업실에서 만든다 → when. (7과 본문)\n오답 ▶ {1}·{2} 뜻이 어색 {3}·{4} '~할 때'의 뜻이 없음\n포인트 ▶ when + 주어 + 동사 = ~할 때", [])
T.fixed('다음 <보기>에서 어법상 <u>옳은</u> 문장의 개수는?', TN, B(
 '(a) When it will rain tomorrow, I will stay home.', '(b) Before you leave, turn off the TV.', '(c) After he came home, he took a nap.', "(d) I'll tell her when she comes back.", "(e) When I will grow up, I'll be a doctor."),
 NUMS, 3,
 "이유 ▶ 옳은 것 (b)·(c)·(d) 3개.\n오답 ▶ (a) When it rains tomorrow (e) When I grow up\n포인트 ▶ when · before · after 절 안에 will ❌", [])
T.flex('대화의 빈칸에 들어갈 말로 알맞은 것은?', W_, B('A: What do you want to be ' + BL + ' you grow up?', 'B: I want to be a pilot.'),
 ['when', 'before', 'after', 'but', 'so'],
 "이유 ▶ 커서(자랐을 때) 뭐가 되고 싶니? → when you grow up.\n오답 ▶ {1} 자라기 전에 {2} 자란 후에 → 어색 {3}·{4} 뜻이 없음\n포인트 ▶ What do you want to be when you grow up?", [])
T.flex('다음 우리말을 영어로 바르게 옮긴 것은?', BA, B('나는 밖에 나가기 전에 엄마에게 전화했다.'),
 ['I called my mom before I went out.', 'I called my mom after I went out.', 'I went out before I called my mom.', 'Before I called my mom, I went out.', 'I called my mom when I will go out.'],
 "이유 ▶ 나가기 전에 → before I went out.\n오답 ▶ {1} 나간 후에 {2}·{3} 순서 반대 {4} 과거 일에 will ❌\n포인트 ▶ before 뒤에는 나중에 한 일", [])
T.flex('다음 밑줄 친 when의 의미가 나머지 넷과 <u>다른</u> 것은?', K_, '',
 [t('[When] does the game begin?'), t('What do you do [when] you are free?'), t('I was sleeping [when] you called.'), t('[When] I hold the baby, she smiles.'), t('Call me [when] you arrive.')],
 "이유 ▶ 경기가 언제 시작하니? → 의문사(언제).\n오답 ▶ {1}~{4} '~할 때'(접속사)\n포인트 ▶ 의문문 맨 앞 When = 언제", [])
T.flex('다음 빈칸에 들어갈 말로 알맞은 것은?', W_, B("Don't forget to lock the door " + BL + ' you go out.'),
 ['when', 'because', 'but', 'or', 'so'],
 "이유 ▶ 나갈 때 문 잠그는 것을 잊지 마 → when.\n오답 ▶ {1} 이유 {2}·{3}·{4} 시간의 뜻이 아님\n포인트 ▶ when + 주어 + 현재 시제", [])
T.render()

# ═══════════════ 3차 (상) ═══════════════
T = Test('3', '3차', '접속사 when · before · after', 'when · before · after', NOTE, H=H); T.rot0 = 2
T.fixed('다음 <보기>에서 어법상 <u>어색한</u> 문장의 개수는?', TN, B(
 '(a) After Betty will do her homework, she will go shopping.', '(b) When Tim is sick, he goes to a hospital.', "(c) I'll help you when I'll finish my homework.", '(d) He came home after the sun set.', '(e) When will the next bus leave?'),
 NUMS, 2,
 "이유 ▶ 어색한 것 (a)·(c) 2개.\n오답 ▶ (a) After Betty does (c) when I finish / (b) 현재 ✔ (d) 과거 ✔ (e) 의문사 When + will ✔\n포인트 ▶ 의문문의 when(언제)은 will을 쓸 수 있다", [])
T.flex('다음 문장과 뜻이 같은 것은?', BA, B('I had dinner before I watched TV.'),
 ['I watched TV after I had dinner.', 'I had dinner after I watched TV.', 'I watched TV before I had dinner.', 'Before I had dinner, I watched TV.', 'After I watched TV, I had dinner.'],
 "이유 ▶ 저녁을 먹고 나서 TV를 봤다 = TV를 본 것은 저녁 먹은 후.\n오답 ▶ {1}~{4} 모두 TV를 먼저 본 뜻(순서 반대)\n포인트 ▶ A before B = B after A", [])
T.flex('다음 문장의 밑줄 친 부분을 바르게 고친 것은?', TN, B(t('When the cat [will be] away, the mice will play.')),
 ['is', 'are', 'was', 'were', 'will'],
 "이유 ▶ 시간 부사절(When ~) → 현재 시제, 주어 the cat(단수) → is.\n오답 ▶ {1} 복수 {2}·{3} 과거 {4} 동사 be 빠짐\n포인트 ▶ When + 현재 시제, 주절 will", [])
SC = '<table style="border-collapse:collapse;margin:4px 0;font-size:12.5px"><tr>' + ''.join('<th style="border:1px solid #9aa3b5;padding:2px 8px">%s</th>' % h for h in ('7:00', '7:30', '8:00')) + '</tr><tr>' + ''.join('<td style="border:1px solid #9aa3b5;padding:2px 8px">%s</td>' % h for h in ('get up', 'have breakfast', 'go to school')) + '</tr></table>'
T.flex('다음은 Mina의 아침 일과표이다. 내용과 일치하지 <u>않는</u> 것은?', BA, B(SC),
 ['Mina gets up after she has breakfast.', 'Mina has breakfast before she goes to school.', 'Mina goes to school after she has breakfast.', 'Mina gets up before she goes to school.', 'Mina has breakfast after she gets up.'],
 "이유 ▶ 일어나고(7:00) 나서 아침을 먹으므로 → gets up before she has breakfast.\n오답 ▶ {1} 7:30 → 8:00 ✔ {2} 8:00이 7:30 뒤 ✔ {3} 7:00 → 8:00 ✔ {4} 7:00 → 7:30 ✔\n포인트 ▶ 시간표 순서로 before / after 따지기", [])
T.flex('다음 밑줄 친 When과 쓰임이 같은 것은?', K_, B(t('[When] I feel lonely, I listen to music.')),
 [t('Where did you live [when] you were a kid?'), t('[When] does the library close?'), t('Do you know [when] the concert starts?'), t("She couldn't remember [when] she lost it."), t('[When] are you going to do your homework?')],
 "이유 ▶ 보기와 정답 모두 '~할 때'(접속사). 정답 문장은 Where가 의문사, when은 접속사!\n오답 ▶ {1}·{4} 의문문 '언제' {2}·{3} '언제 ~인지'(의문사)\n포인트 ▶ 문장 맨 앞 의문사에 속지 말 것", [])
T.table('(A)~(C)의 각 네모 안에서 알맞은 말을 바르게 짝지은 것은?', BA, B(
 '• <b>(A)</b> [ When / Before ] I was a child, I lived in Jeju.', '• Wash the fruit <b>(B)</b> [ before / after ] you eat it.', '• <b>(C)</b> [ After / Before ] the rain stopped, we went out to play.'),
 ['(A)', '(B)', '(C)'], [['When', 'before', 'After'], ['Before', 'before', 'After'], ['When', 'after', 'After'], ['When', 'before', 'Before'], ['Before', 'after', 'Before']],
 "이유 ▶ (A) 어렸을 때 → When (B) 먹기 전에 씻어라 → before (C) 비가 그친 후에 놀러 나갔다 → After\n오답 ▶ 어리기 전에 ❌ / 먹은 후에 씻기 ❌ / 비가 그치기 전에 놀러 나감 ❌\n포인트 ▶ 문맥으로 때 · 전 · 후 고르기", [])
T.table('다음 빈칸에 들어갈 말이 바르게 짝지어진 것은?', TN, B('When he ' + BL + ' the news tomorrow, he ' + BL + ' surprised.'),
 ['첫째 빈칸', '둘째 빈칸'], [['hears', 'will be'], ['will hear', 'will be'], ['hears', 'is'], ['heard', 'will be'], ['will hear', 'was']],
 "이유 ▶ tomorrow(미래): when절은 현재 hears, 주절은 will be.\n오답 ▶ when절에 will ❌ / 주절이 현재·과거 ❌ / when절 과거 ❌\n포인트 ▶ When + 현재, 주어 + will + 동사원형", [])
T.flex('다음 중 어법상 <u>옳은</u> 것은?', TN, '',
 ['I will be eighteen when I graduate.', 'I will be eighteen when I met her last year.', 'When will I be free, I will call you.', 'After he will finish lunch, he will rest.', 'Before you will go to bed, brush your teeth.'],
 "이유 ▶ 주절 will + when절 현재(graduate) ✔\n오답 ▶ {1} 작년 일 → I was eighteen when I met her {2} When I am free {3} After he finishes {4} Before you go\n포인트 ▶ 시간 부사절 현재 / 과거 일은 둘 다 과거", [])
T.flex('다음 우리말을 영어로 바르게 옮긴 것은?', TN, B('나는 숙제를 끝낸 후에 친구들과 축구를 할 것이다.'),
 ['I will play soccer with my friends after I finish my homework.', 'I will play soccer with my friends after I will finish my homework.', 'I will play soccer with my friends before I finish my homework.', 'I played soccer with my friends after I will finish my homework.', 'After I will play soccer with my friends, I finish my homework.'],
 "이유 ▶ 주절 will play + after + 현재(finish).\n오답 ▶ {1} after절에 will ❌ {2} 끝내기 전에 {3}·{4} 시제·순서 ❌\n포인트 ▶ 주어 + will ~ after + 주어 + 현재", [])
T.flex('다음 빈칸에 공통으로 들어갈 말로 알맞은 것은? (대 · 소문자 무시)', K_, B('• ' + BL + ' is the school festival?', '• I was cooking ' + BL + ' the phone rang.'),
 ['when', 'before', 'after', 'what', 'where'],
 "이유 ▶ 학교 축제가 언제니?(의문사) / 전화가 울렸을 때(접속사) → when.\n오답 ▶ {1}·{2} 첫 문장 불가 {3}·{4} 둘째 문장 불가\n포인트 ▶ when = 언제(의문사) / ~할 때(접속사)", [])
T.fixed('다음 글의 밑줄 친 ⓐ~ⓔ 중 어법상 <u>틀린</u> 것은?', TN, B(
 'Every morning, I get up ⓐ <u>when the alarm rings</u>. I wash my face ⓑ <u>before I eat breakfast</u>. ⓒ <u>After I eat breakfast</u>, I go to school. Tomorrow, ⓓ <u>when I will get up</u>, I ⓔ <u>will go</u> jogging.'),
 ['ⓐ', 'ⓑ', 'ⓒ', 'ⓓ', 'ⓔ'], 4,
 "이유 ▶ 내일 일이라도 when절은 현재 시제 → when I get up.\n오답 ▶ ⓐ·ⓑ·ⓒ 매일 하는 일 현재 ✔ ⓔ 주절은 will ✔\n포인트 ▶ when절 will ❌, 주절 will ✔", [])
T.table('글의 흐름상 (A)~(C)에 들어갈 말이 바르게 짝지어진 것은?', BA, B(
 '<b>(A)</b> ______ I got home, I was very hungry. So I ate some bread <b>(B)</b> ______ I did my homework. <b>(C)</b> ______ I finished my homework, I went to bed.'),
 ['(A)', '(B)', '(C)'], [['When', 'before', 'After'], ['Before', 'after', 'When'], ['After', 'after', 'Before'], ['When', 'after', 'Before'], ['Before', 'before', 'After']],
 "이유 ▶ (A) 집에 왔을 때 배고팠다 → When (B) 배고파서 숙제하기 전에 빵을 먹었다 → before (C) 숙제를 끝낸 후에 잤다 → After\n오답 ▶ 집에 오기 전에 ❌ / 숙제를 끝내기 전에 잠 ❌\n포인트 ▶ 글의 시간 순서 따라가기", [])
T.flex('다음 밑줄 친 when의 쓰임이 <보기>와 <u>다른</u> 것은?', K_, B(t("I'm not sure [when] Tom will arrive.")),
 [t('Call me [when] you get there.'), t("Do you know [when] Hye-jin's birthday is?"), t('I wonder [when] he will move.'), t('I forgot [when] the party starts.'), t('[When] did you meet her?')],
 "이유 ▶ 보기는 '언제 도착할지'(의문사). 정답은 '거기 도착하면(할 때)'(접속사).\n오답 ▶ {1}·{2}·{3} '언제 ~인지' {4} '언제'\n포인트 ▶ 의문사 when 뒤에는 미래 will 가능 / 접속사 when 절은 현재", [])
T.table('(A), (B)에 들어갈 말이 바르게 짝지어진 것은?', TN, B("• I don't know when he <b>(A)</b> ______ back.", "• I'll call you when he <b>(B)</b> ______ back."),
 ['(A)', '(B)'], [['will come', 'comes'], ['comes', 'will come'], ['comes', 'comes'], ['will come', 'will come'], ['came', 'will come']],
 "이유 ▶ (A) 언제 돌아올지(의문사, know의 목적어) → 미래 will come (B) 그가 돌아오면(때, 시간 부사절) → 현재 comes\n오답 ▶ 시간 부사절에 will ❌ / 의문사절은 미래면 will\n포인트 ▶ 같은 when이라도 '언제'면 will, '~할 때'면 현재", [])
T.flex('두 문장을 before를 써서 한 문장으로 바르게 바꾼 것은?', BA, B('Think carefully. Then answer the question.'),
 ['Think carefully before you answer the question.', 'Think carefully after you answer the question.', 'Answer the question before you think carefully.', 'Before you think carefully, answer the question.', 'Think carefully when you will answer the question.'],
 "이유 ▶ 먼저 생각하고 그다음 답하라 → 답하기 전에 생각해라.\n오답 ▶ {1}·{2}·{3} 순서 반대 {4} when절에 will ❌\n포인트 ▶ before 뒤에는 나중에 할 일", [])
T.flex('다음 문장과 뜻이 같은 것은?', BA, B('My work begins after the shooting is over.'),
 ['The shooting is over before my work begins.', 'My work begins before the shooting is over.', 'The shooting is over after my work begins.', 'After my work begins, the shooting is over.', 'My work began before the shooting will be over.'],
 "이유 ▶ 촬영이 끝난 뒤 내 일이 시작 = 내 일이 시작되기 전에 촬영이 끝난다. (7과 본문)\n오답 ▶ {1}·{2}·{3} 순서 반대 {4} 시제 ❌\n포인트 ▶ A after B = B before A", [])
T.flex('대화의 빈칸에 들어갈 말로 알맞은 것은?', BA, B('A: Mom, can I play games now?', 'B: Yes, but only ' + BL + ' you finish your homework.'),
 ['after', 'before', 'because', 'or', 'so'],
 "이유 ▶ 숙제를 끝낸 후에만 → after.\n오답 ▶ {1} 숙제 끝내기 전에만 → 어색 {2}·{3}·{4} 시간의 뜻이 아님\n포인트 ▶ only after ~ = ~한 후에야", [])
T.flex('다음 중 어법상 <u>틀린</u> 것은?', TN, '',
 ['He was reading a book when I will enter the room.', 'I was taking a shower when she knocked on the door.', 'When I got home, he was playing badminton.', 'What did you do when you were in Busan?', 'She was surprised when I told her the news.'],
 "이유 ▶ 과거 일(was reading) → when I entered the room.\n오답 ▶ {1}~{4} 과거 일은 when절 · 주절 모두 과거 ✔\n포인트 ▶ 주절과 when절의 때를 맞추기", [])
T.flex('다음 우리말을 영어로 바르게 옮긴 것은?', TN, B('네가 서울에 오면 우리를 먼저 보러 와야 해.'),
 ['You must come and see us first when you visit Seoul.', 'You must come and see us first when you will visit Seoul.', 'You must come and see us first before you visit Seoul.', 'When you must visit Seoul, come and see us first.', 'You must come and see us first when did you visit Seoul.'],
 "이유 ▶ 서울에 올 때(오면) → when you visit Seoul(현재).\n오답 ▶ {1} when절에 will ❌ {2} 오기 전에 ❌ {3} 뜻이 달라짐 {4} 의문문 어순 ❌\n포인트 ▶ 미래 일이라도 when절은 현재", [])
T.flex('다음 중 빈칸에 when을 쓸 수 <u>없는</u> 것은?', W_, '',
 ['I think ' + BL + ' he is honest.', BL + ' the bell rang, I opened the door.', 'I was happy ' + BL + ' I heard the news.', 'Tell me ' + BL + ' you are ready.', 'It was snowing ' + BL + ' I woke up.'],
 "이유 ▶ '그가 정직하다고' 생각한다 → think + that절. when은 어색.\n오답 ▶ {1}·{2}·{3}·{4} '~할 때'로 자연스러움\n포인트 ▶ think · know · hope + that절", [])
T.render()
