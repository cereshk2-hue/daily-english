# 11/20 중산중2 동아(윤정미) 8과 실전 문법 — 현재완료 1~6차 (각 20문항, 1·2차 기본 · 3·4차 중~중상 · 5·6차 상)
# 원본: 선생님 학습지 현재완료(1)~(5).hwp → work_src/m2pp/*.txt + 8과 본문(I've always wanted to see a dinosaur. / We've just arrived in the jungle ... / I've never seen such a huge thing.)
# 범위: have/has + p.p.(불규칙 과거분사), 부정·의문·대답, 용법 4가지(경험·완료·계속·결과), been to / gone to / been in, for / since / ago, 명확한 과거 표현(yesterday · ~ ago · last · in 연도 · just now · When)과 못 씀, 과거 vs 현재완료 뜻, already · yet · just, 조동사 have vs 일반동사 have
# 뺀 것: 현재완료 진행 · 과거완료 · 미래완료(8과 범위 밖). 논쟁 피함: I/you have gone to(미국 영어에서 '가 본 적' 뜻으로도 씀)를 정답 근거로 안 씀, didn't ~ yet · Did you ever ~? 를 틀린 보기로 안 씀, 표지어 없는 '결과/완료' 구별 안 냄
import sys; sys.path.insert(0, '/home/claude/srcrepo/wrapup')
from wu_m2it import *
H = ('실전 문법', '중2 영어 동아(윤정미) 8과 현재완료', '동아(윤정미) 8과 현재완료', 'm2pp')
B = lambda *ls: BOX('<br>'.join(ls))
NUMS = ['1개', '2개', '3개', '4개', '5개']
t = lambda x: x.replace('[', '<u>').replace(']', '</u>')
F, Y, K, P, R = '현재완료 형태', '용법 구별', '현재완료 vs 과거', 'for · since', '8과 본문'
NOTE = '범위: 현재완료(have/has + 과거분사) — 형태 · 부정문 · 의문문, 경험 · 완료 · 계속 · 결과, been to / gone to, for / since, 과거 시제와의 구별.'
def S(no, title, rot):
    T = Test(no, '%s차' % no, title, '현재완료', NOTE, H=H); T.rot0 = rot; return T

# ═══════════════ 1차 (기본) ═══════════════
T = S('1', '현재완료의 형태와 쓰임', 0)
T.flex('다음 빈칸에 들어갈 말로 알맞은 것은?', F, B('Have you ever ' + BL + ' a koala?'),
 ['seen', 'saw', 'see', 'seeing', 'sees'],
 "이유 ▶ Have + 주어 + 과거분사 → seen (see-saw-seen). 코알라를 본 적 있니?\n오답 ▶ {1} 과거형 {2}·{3}·{4} 과거분사가 아님\n포인트 ▶ 현재완료 = have/has + 과거분사(p.p.)", [('koala', '코알라')])
T.flex('다음 빈칸에 들어갈 말로 알맞은 것은?', F, B('Yuri ' + BL + ' learned to play the guitar.'),
 ['has', 'have', 'is', 'did', 'was'],
 "이유 ▶ 주어 Yuri(3인칭 단수) + has + learned.\n오답 ▶ {1} 복수·I·you 주어 {2}·{4} be동사 + p.p.는 수동태 {3} did + p.p. ❌\n포인트 ▶ 3인칭 단수 → has + p.p.", [])
T.flex('다음 빈칸에 들어갈 말로 알맞은 것은?', F, B('I ' + BL + ' eaten Indian food.'),
 ['have never', 'never have', 'not have', 'am never', 'did never'],
 "이유 ▶ 부정 = have + never(not) + p.p. → I have never eaten ~. 인도 음식을 먹어 본 적이 없다.\n오답 ▶ {1}·{2} 어순 ❌ {3}·{4} be동사·did ❌\n포인트 ▶ never / not은 have와 p.p. 사이", [])
T.flex('다음 우리말을 영어로 바르게 옮긴 것은?', F, B('나는 이미 기차표를 샀다.'),
 ['I have already bought a train ticket.', 'I have already buyed a train ticket.', 'I already have buy a train ticket.', 'I has already bought a train ticket.', 'I am already bought a train ticket.'],
 "이유 ▶ have + already + bought(buy-bought-bought).\n오답 ▶ {1} buyed ❌ {2} have + 동사원형 ❌ {3} I → have {4} be동사 ❌\n포인트 ▶ already는 have와 p.p. 사이", [])
T.flex('다음 문장을 의문문으로 바르게 바꾼 것은?', F, B('You have thought about your future.'),
 ['Have you thought about your future?', 'Do you have thought about your future?', 'Have you think about your future?', 'Did you have thought about your future?', 'Are you thought about your future?'],
 "이유 ▶ 현재완료 의문문 = Have + 주어 + p.p. ~?\n오답 ▶ {1}·{3} do · did ❌ {2} p.p. thought로 {4} be동사 ❌\n포인트 ▶ have를 주어 앞으로", [('future', '미래')])
T.flex('다음 대화의 빈칸에 들어갈 말로 알맞은 것은?', F, B('A: Have you ever been to Jejudo?', 'B: Yes, ' + BL + '. It was beautiful.'),
 ['I have', 'I do', 'I did', 'I am', 'I was'],
 "이유 ▶ Have you ~? → Yes, I have. / No, I haven't.\n오답 ▶ {1}·{2}·{3}·{4} 질문의 조동사 have와 맞지 않음\n포인트 ▶ 현재완료 질문엔 have / has로 대답", [])
T.flex('다음 빈칸에 들어갈 말로 알맞은 것은?', P, B('I have lived in Daejeon ' + BL + ' two years.'),
 ['for', 'since', 'ago', 'when', 'at'],
 "이유 ▶ two years(기간) 앞 → for.\n오답 ▶ {1} since + 시점 {2} ago는 과거 시제와 {3}·{4} 기간 앞에 쓰지 않음\n포인트 ▶ for + 기간 / since + 시점", [])
T.flex('다음 빈칸에 들어갈 말로 알맞은 것은?', P, B('She has been sick ' + BL + ' last Friday.'),
 ['since', 'for', 'ago', 'from', 'at'],
 "이유 ▶ last Friday(시작 시점) 앞 → since. 지난 금요일 이후로 계속 아프다.\n오답 ▶ {1} for + 기간 {2} ago는 과거 시제 {3} 현재완료 계속엔 since {4} 시점 앞 at ❌\n포인트 ▶ since + 시점", [])
T.flex('다음 빈칸에 들어갈 수 <u>없는</u> 것은?', K, B('I have been there ' + BL + '.'),
 ['yesterday', 'twice', 'once', 'three times', 'before'],
 "이유 ▶ yesterday는 명확한 과거 → 현재완료와 못 씀 (I was there yesterday.)\n오답 ▶ {1}~{4} 횟수 · before → 경험 ✔\n포인트 ▶ yesterday · ~ ago · last ~ · in 연도 + 현재완료 ❌", [])
T.flex('다음 중 어법상 <u>틀린</u> 것은?', K, '',
 ['She has visited him last Friday.', 'Jane has been to Switzerland twice.', "I've just finished my work.", 'I have read the book before.', 'He has lived here since 2010.'],
 "이유 ▶ last Friday(명확한 과거) → 과거 시제 visited.\n오답 ▶ {1} 경험 {2} 완료 {3} 경험 {4} 계속 ✔\n포인트 ▶ last ~ 와 현재완료는 함께 못 씀", [])
T.flex('다음 밑줄 친 문장의 해석으로 알맞은 것은?', R, B('After only a few minutes, the machine stopped. ' + t('["We\'ve just arrived in the jungle of 60 million years ago,"]') + ' Travis explained.'),
 ['우리는 이제 막 6천만 년 전의 정글에 도착했습니다.', '우리는 6천만 년 전의 정글에 도착할 것입니다.', '우리는 6천만 년 전의 정글에 도착하지 못했습니다.', '우리는 6천만 년 전의 정글에 가 본 적이 있습니다.', '우리는 6천만 년 전의 정글에 도착하는 중입니다.'],
 "이유 ▶ have just + p.p. = 이제 막 ~했다(완료). (교과서)\n오답 ▶ {1} 미래 {2} 부정 {3} 경험 {4} 진행 → 모두 just arrived와 맞지 않음\n포인트 ▶ just · already · yet = 완료", [('arrive', '도착하다'), ('jungle', '정글')], en=False)
T.flex('다음 우리말을 영어로 가장 바르게 옮긴 것은?', Y, B('그는 일본에 가고 없다.'),
 ['He has gone to Japan.', 'He has been to Japan.', 'He went to Japan.', 'He goes to Japan.', 'He is going to Japan.'],
 "이유 ▶ 가 버려서 지금 여기 없다 → has gone to(결과).\n오답 ▶ {1} 가 본 적이 있다(경험) {2} 갔다(지금 있는지는 모름) {3} 간다 {4} 갈 것이다\n포인트 ▶ has gone to = 가고 없다 / has been to = 가 본 적 있다", [])
T.flex('다음 두 문장을 한 문장으로 바르게 나타낸 것은?', Y, B('Alice began to work with us two years ago. Alice still works with us.'),
 ['Alice has worked with us for two years.', 'Alice has worked with us for two years ago.', 'Alice has worked with us two years ago.', 'Alice has begun to work with us for two years.', 'Alice worked with us for two years.'],
 "이유 ▶ 2년 전에 시작해서 지금도 일함 → 계속: has worked ~ for two years.\n오답 ▶ {1}·{2} ago는 현재완료와 ❌ {3} begin은 한 번 시작하는 일이라 for와 ❌ {4} 과거 시제는 지금 일하는지 알 수 없음\n포인트 ▶ 과거에 시작 + 지금도 → 현재완료 계속", [])
T.flex('다음 질문에 대한 응답으로 <u>어색한</u> 것은?', K, B('How long have you been in Korea?'),
 ['I have been here three years ago.', 'I came here last summer.', 'I have been here since last March.', 'I have been here for almost 10 years.', 'I have just arrived here from Chicago.'],
 "이유 ▶ three years ago(명확한 과거)와 현재완료 ❌\n오답 ▶ {1} 과거 시제 + last summer ✔ {2} since ✔ {3} for ✔ {4} 방금 도착 ✔\n포인트 ▶ ago는 과거 시제와만", [])
T.flex('<보기>의 밑줄 친 have와 쓰임이 <u>다른</u> 것은?', F, B(t('<보기> I [have] never seen him before.')),
 [t('I [have] many games to play with.'), t('She [has] left for Paris.'), t('I [have] just come home.'), t('She [has] stayed here for one hour.'), t('I [have] been to Brazil once.')],
 "이유 ▶ 정답의 have는 '가지고 있다'(일반동사). <보기>는 현재완료의 조동사 have(뒤에 p.p.).\n오답 ▶ {1}~{4} 뒤에 과거분사(left · come · stayed · been) → 현재완료\n포인트 ▶ have 뒤에 p.p.가 오면 현재완료", [])
T.flex('다음 대화의 빈칸에 공통으로 들어갈 말은?', Y, B('Tom: Where have you ' + BL + ', Julia?', 'Julia: I have ' + BL + ' to Europe.'),
 ['been', 'gone', 'went', 'were', 'be'],
 "이유 ▶ 지금 눈앞의 Julia → 어디 갔다 왔니? / 유럽에 갔다 왔어 → been\n오답 ▶ {1} Julia가 여기 있으므로 '가고 없다'(gone to)는 맞지 않음 {2}·{3}·{4} 과거분사가 아님\n포인트 ▶ have been (to) = 갔다 왔다 · 가 본 적 있다", [])
T.flex('다음 중 어법상 올바른 것은?', K, '',
 ['He has worn glasses since he was a kid.', 'They have gone to New York last winter.', 'When have you taught him?', 'She has met him yesterday.', 'They have been happy a week ago.'],
 "이유 ▶ since + 과거 시점(절) → 현재완료 계속 ✔ (since 뒤 절은 과거 was)\n오답 ▶ {1} last winter {3} yesterday {4} a week ago → 과거 시제 {2} When은 현재완료와 ❌\n포인트 ▶ since 뒤 절은 과거, 주절은 현재완료", [('wear glasses', '안경을 쓰다')])
T.flex('우리말에 맞게 주어진 단어를 배열할 때 알맞은 문장은? (필요하면 형태를 바꿀 것)', F, B('그는 지금 막 독서를 끝냈다.', '( have / reading / book / he / just / a / finish )'),
 ['He has just finished reading a book.', 'He have just finished reading a book.', 'He has finished just reading a book.', 'He just has finished reading a book.', 'He has just finish reading a book.'],
 "이유 ▶ He + has(3인칭 단수) + just + finished + reading a book.\n오답 ▶ {1} He → has {2}·{3} just 위치 ❌ {4} has + 동사원형 ❌\n포인트 ▶ 주어에 따라 have → has로 바꿈", [])
T.flex('다음 글의 밑줄 친 부분과 현재완료의 용법이 같은 것은?', R, B(t('"It ... is huge. [I\'ve never seen] such a huge thing. I\'m so scared," said Eckels.')),
 ['Have you ever ridden a horse?', 'I have just finished my homework.', 'She has lived here for ten years.', 'He has gone to America.', 'We have known each other since 2015.'],
 "이유 ▶ 본문 have never seen = 본 적이 없다(경험). 정답도 ever → 경험.\n오답 ▶ {1} just → 완료 {2} for → 계속 {3} gone to → 결과 {4} since → 계속\n포인트 ▶ ever · never · before · ~ times = 경험", [('huge', '거대한')])
T.flex('다음 밑줄 친 부분이 <u>잘못</u> 쓰인 것은?', F, '',
 [t('Have you ever [became] a leader?'), t('Have you ever [read] a fantasy novel?'), t('She has just [heard] the news.'), t('He has never [sent] a letter abroad.'), t("I haven't [eaten] Italian food before.")],
 "이유 ▶ become-became-become → Have you ever become ~?\n오답 ▶ {1} read-read-read {2} hear-heard-heard {3} send-sent-sent {4} eat-ate-eaten ✔\n포인트 ▶ 과거형과 과거분사가 다른 동사 조심", [('novel', '소설')])
T.render()

# ═══════════════ 2차 (기본) ═══════════════
T = S('2', '현재완료의 부정 · 의문 · 시간 표현', 2)
T.flex('다음 빈칸에 들어갈 말로 알맞은 것은?', F, B('Pep Torres ' + BL + ' made a new vending machine.'),
 ['has', 'have', 'is', 'were', 'did'],
 "이유 ▶ 주어 Pep Torres(한 사람) → has + made.\n오답 ▶ {1} 3인칭 단수엔 has {2}·{3} be동사 + p.p.는 수동태 {4} did + p.p. ❌\n포인트 ▶ 주어 수에 맞춰 have / has", [('vending machine', '자판기')])
T.flex('동사원형과 과거분사가 <u>잘못</u> 연결된 것은?', F, '',
 ['become − became', 'buy − bought', 'bring − brought', 'read − read', 'be − been'],
 "이유 ▶ become의 과거분사는 become (become-became-become). became는 과거형.\n오답 ▶ {1}~{4} 바르게 연결됨\n포인트 ▶ come · become · run은 원형 = 과거분사", [])
T.flex('다음 대화의 빈칸에 들어갈 말로 알맞은 것은?', F, B('A: Have you already finished the report?', 'B: No, I ' + BL + ' it yet.'),
 ["haven't finished", "don't finish", 'finished', "wasn't finished", "haven't finish"],
 "이유 ▶ Have you ~? → No, I haven't finished it yet. (아직 못 끝냈어)\n오답 ▶ {1} 현재 시제 {2} No와 맞지 않음 {3} 수동태 {4} have + 동사원형 ❌\n포인트 ▶ yet(아직) + 부정 현재완료", [('report', '보고서')])
T.flex('다음 우리말을 영어로 바르게 옮긴 것은?', F, B('그녀는 아직 숙제를 끝내지 않았다.'),
 ["She hasn't finished her homework yet.", 'She has finished her homework yet.', "She hasn't finished her homework already.", "She didn't have finished her homework yet.", "She hasn't finish her homework yet."],
 "이유 ▶ hasn't + finished + yet(아직).\n오답 ▶ {1} 긍정문 ❌ {2} 부정문의 '아직'은 yet {3} didn't have ❌ {4} p.p. finished\n포인트 ▶ already(긍정, 이미) / yet(부정, 아직)", [])
T.flex('다음 빈칸에 들어갈 말이 바르게 짝지어진 것은?', F, B('I have ' + BL + ' written a letter. I haven\'t sent it to him ' + BL + '.'),
 ['already − yet', 'already − just', 'just − already', 'yet − just', 'yet − already'],
 "이유 ▶ 긍정문 '이미 썼다' → already / 부정문 '아직 안 보냈다' → yet\n오답 ▶ 부정문 끝에 just · already ❌, 긍정문 have 뒤 yet ❌\n포인트 ▶ already = 긍정문 / yet = 부정문 · 의문문", [])
T.flex('다음 빈칸에 들어갈 말이 차례대로 바르게 짝지어진 것은?', P, B('• He has been in the army ' + BL + ' two years.', '• He has learned Japanese ' + BL + ' he was a boy.'),
 ['for − since', 'for − for', 'since − for', 'since − since', 'for − ago'],
 "이유 ▶ two years(기간) → for / he was a boy(시점) → since\n오답 ▶ 기간 앞 since ❌, 절(주어 + 동사) 앞 for ❌, ago ❌\n포인트 ▶ since 뒤에는 시점 · 절 둘 다", [('army', '군대')])
T.flex('다음 빈칸에 들어갈 말로 알맞은 것은?', Y, B('Ralph and I ' + BL + ' close friends since we were little.'),
 ['have been', 'are', 'were', 'was', 'be'],
 "이유 ▶ since we were little(어릴 때부터) → 지금까지 계속 → have been.\n오답 ▶ {1} 현재 {2}·{3} 과거 {4} 동사원형 → since와 함께 못 씀\n포인트 ▶ since가 보이면 현재완료", [])
T.flex('다음 중 어법상 <u>어색한</u> 것은?', F, '',
 ['He has already drank the juice.', 'The train has not left yet.', 'I have never met such a kind man.', 'I have seen a rainbow many times.', 'Have you ever worked on a farm?'],
 "이유 ▶ drink-drank-drunk → has already drunk.\n오답 ▶ {1} leave-left-left {2} meet-met-met {3} see-saw-seen {4} work-worked-worked ✔\n포인트 ▶ 과거형(drank)과 과거분사(drunk) 구별", [])
T.flex('두 문장의 의미가 같도록 할 때 빈칸에 알맞은 것은?', K, B("I lost my bag, and I don't have it now.", '= I ' + BL + ' my bag.'),
 ['have lost', 'lose', 'am lost', 'was lost', 'have losing'],
 "이유 ▶ 잃어버려서 지금도 없다 → have lost(결과).\n오답 ▶ {1} 현재 {2}·{3} 수동 {4} have + -ing ❌\n포인트 ▶ 과거의 일 + 현재 상태 = 현재완료", [])
T.flex('다음 중 현재완료의 용법이 나머지 넷과 <u>다른</u> 것은?', Y, '',
 ["I haven't finished the game yet.", "I've seen a lion before.", 'She has been to Jeju Island.', 'Have you ever had a terrible dream?', 'He has never heard such a wonderful story.'],
 "이유 ▶ yet → 아직 끝내지 못했다(완료).\n오답 ▶ {1} before {2} been to {3} ever {4} never → 모두 경험\n포인트 ▶ yet은 완료, ever · never · before는 경험", [('terrible', '끔찍한')])
T.flex('다음 빈칸에 들어갈 수 <u>없는</u> 것은?', P, B('The store has been here ' + BL + '.'),
 ['last week', 'since 1988', 'for ten years', 'since I was born', 'for many years'],
 "이유 ▶ last week(명확한 과거)는 현재완료와 ❌\n오답 ▶ {1}·{3} since + 시점 {2}·{4} for + 기간 ✔\n포인트 ▶ 계속 = for / since", [])
T.flex('다음 두 문장을 한 문장으로 바르게 나타낸 것은?', Y, B('Sumi went to the library one hour ago. She is still there.'),
 ['Sumi has been at the library for one hour.', 'Sumi was at the library for one hour.', 'Sumi has been at the library one hour ago.', 'Sumi is at the library since one hour.', 'Sumi has been at the library since one hour.'],
 "이유 ▶ 한 시간 전부터 지금까지 도서관에 있다 → has been at ~ for one hour.\n오답 ▶ {1} 과거 → 지금 있는지 모름 {2} ago ❌ {3} is + since ❌ {4} one hour(기간) 앞엔 for\n포인트 ▶ 지금도 있다 → 현재완료 계속", [])
T.fixed('다음 대화의 밑줄 친 ①~⑤ 중 어법상 <u>어색한</u> 것은?', F, B('A: Have you ever ① ' + U('been') + ' to Jejudo?', 'B: ② ' + U('Yes, I did') + '.', 'A: Then ③ ' + U('have you ever stayed') + ' late at night ④ ' + U("at your friend's house") + '?', "B: ⑤ " + U("No, I haven't") + '.'),
 None, 2,
 "이유 ▶ Have you ~? 에는 have로 대답 → Yes, I have.\n오답 ▶ ① been to ③ 현재완료 의문문 ④ 장소 ⑤ No, I haven't ✔\n포인트 ▶ 질문의 조동사로 대답", [])
T.flex('다음 대화의 빈칸에 들어갈 질문으로 알맞은 것은?', F, B('A: ' + BL + '?', "B: Yes, I've been there once."),
 ['Have you ever been to Alaska', 'When did you go to Alaska', 'How did you go to Alaska', 'Where have you been during the vacation', 'Will you go to Alaska'],
 "이유 ▶ Yes, I've been there once. → 가 본 적 있니?(경험) 질문.\n오답 ▶ {1} 언제 {2} 어떻게 {3} 어디에 → Yes로 답할 수 없음 {4} 미래 질문엔 Yes, I will.\n포인트 ▶ Yes / No 대답 → 의문사 없는 질문", [])
T.flex('다음 문장과 의미가 같은 것은?', K, B('I have lost my key.'),
 ["I lost my key, and I don't have it now.", 'I lost my key, but I found it.', 'I lost my key, but I have it now.', 'I have my key in my pocket.', "I didn't have a key from the beginning."],
 "이유 ▶ 결과 용법 = 잃어버려서 지금도 없다.\n오답 ▶ {1}·{2}·{3} 지금 열쇠가 있음 {4} 처음부터 없었음\n포인트 ▶ have lost = 잃어버려서 지금 없다", [])
T.flex('다음 우리말을 영어로 바르게 옮긴 것은?', F, B('너는 콘서트에 가 본 적이 있니?'),
 ['Have you ever been to a concert?', 'Did you ever been to a concert?', 'Have you ever be to a concert?', 'Have ever you been to a concert?', 'Do you ever been to a concert?'],
 "이유 ▶ Have + you + ever + been to ~? = ~에 가 본 적 있니?\n오답 ▶ {1}·{4} did · do + been ❌ {2} be → been {3} ever 위치 ❌\n포인트 ▶ ever는 주어 뒤, p.p. 앞", [])
T.flex('다음 대화의 빈칸에 들어갈 말로 알맞은 것은?', F, B('A: How is the weather in London today?', 'B: It started raining this morning and ' + BL + ' yet.'),
 ["hasn't stopped", "doesn't stop", "hasn't stop", "isn't stopped", "wasn't stopping"],
 "이유 ▶ 아침에 시작해서 아직 안 그쳤다 → hasn't stopped yet.\n오답 ▶ {1} 현재 시제 + yet 어색 {2} has + 동사원형 ❌ {3} 수동 ❌ {4} 과거 진행 ❌\n포인트 ▶ 아직 ~하지 않았다 = haven't / hasn't + p.p. + yet", [])
T.flex('다음 중 어법상 옳은 것은?', K, '',
 ['He has arrived at the station already.', 'I have eaten breakfast just now.', 'I have bought a bicycle last week.', 'She has moved here two years ago.', 'When have you finished the work?'],
 "이유 ▶ already(이미)는 현재완료와 ✔ (문장 끝에도 옴)\n오답 ▶ {1} just now(방금 전) {2} last week {3} two years ago → 과거 시제 {4} When ❌\n포인트 ▶ just(현재완료) / just now(과거)", [])
T.fixed('다음 글의 밑줄 친 ①~⑤ 중 어법상 <u>어색한</u> 것은?', R, B('Eckels walked into the office. "I ① ' + U('have always wanted') + ' to see a dinosaur," he said. After a few minutes, the time machine ② ' + U('stopped') + '. "We ③ ' + U('have just arrived') + ' in the jungle," Travis explained. An hour later, Eckels ④ ' + U('has seen') + ' a T. rex. "I ⑤ ' + U('have never seen') + ' such a huge thing," he said.'),
 None, 4,
 "이유 ▶ An hour later(과거의 한 시점) → 과거 시제 saw\n오답 ▶ ① 지금까지 계속 원해 왔다 ② 과거 ③ 막 도착(완료) ⑤ 본 적 없다(경험) ✔ (교과서 문장)\n포인트 ▶ 과거의 특정 때 → 과거 시제", [('dinosaur', '공룡')])
T.flex('다음 빈칸에 since가 들어갈 수 <u>없는</u> 것은?', P, '',
 ['John has worked here ' + BL + ' ten years.', 'I have lived in this house ' + BL + ' I was a child.', 'Mary has known Jack ' + BL + ' 2003.', "I've never met him " + BL + ' last year.', 'She has done ballet ' + BL + ' the age of five.'],
 "이유 ▶ ten years(기간) → for.\n오답 ▶ {1} 절 {2} 연도 {3} last year {4} the age of five → 모두 시점이라 since\n포인트 ▶ 숫자 + 기간(ten years) → for", [('ballet', '발레')])
T.render()

# ═══════════════ 3차 (중) ═══════════════
T = S('3', '용법 구별 · 과거와 현재완료', 4)
T.flex('<보기>의 밑줄 친 부분과 용법이 같은 것은?', Y, B(t('<보기> She [has lived] in Australia since 2003.')),
 ['I have learned Chinese for 2 years.', 'Jenny has read the story twice.', 'She has gone to Paris.', 'I have met her before.', 'Kevin has been to America.'],
 "이유 ▶ <보기> since 2003 → 계속. 정답 for 2 years → 계속.\n오답 ▶ {1}·{3}·{4} 경험(twice · before · been to) {2} 결과(gone to)\n포인트 ▶ for · since · How long = 계속", [])
T.flex('<보기>의 밑줄 친 부분과 용법이 같은 것은?', Y, B(t('<보기> Mark [has just arrived] in Korea.')),
 ['My sister has already come home.', 'I have read about the rumor before.', 'He has been angry since yesterday.', 'She has gone to Paris.', 'Mary has lived here since she was young.'],
 "이유 ▶ <보기> just → 완료. 정답 already → 완료.\n오답 ▶ {1} 경험 {2}·{4} 계속 {3} 결과\n포인트 ▶ just · already · yet = 완료", [('rumor', '소문')])
T.flex('다음 빈칸에 들어갈 말이 순서대로 바르게 짝지어진 것은?', P, B('• He had a car accident three years ' + BL + '.', '• She has studied for the exam ' + BL + ' last Monday.'),
 ['ago − since', 'ago − for', 'since − for', 'for − since', 'since − ago'],
 "이유 ▶ 과거 시제(had) + three years ago / 현재완료 + since last Monday\n오답 ▶ 과거 시제 문장 끝 since · for ❌, last Monday 앞 for · ago ❌\n포인트 ▶ ago = 과거 시제 / since = 현재완료", [('accident', '사고')])
T.flex('다음 빈칸에 들어갈 말이 순서대로 바르게 짝지어진 것은?', K, B('• My teacher ' + BL + ' her pen, so she has to buy a new one.', '• My teacher ' + BL + ' her pen, but found it later.'),
 ['has lost − lost', 'lost − has lost', 'has lost − has lost', 'lost − loses', 'has lost − loses'],
 "이유 ▶ 잃어버려서 지금 새로 사야 함 → has lost / 잃어버렸지만 나중에 찾음(지금은 있음) → lost\n오답 ▶ 둘째 문장에 has lost를 쓰면 '지금도 없다'가 되어 found it과 맞지 않음, loses는 시제 ❌\n포인트 ▶ 현재완료 결과 = 지금도 그 상태", [])
T.flex('다음 중 어법상 바르지 <u>않은</u> 것은?', K, '',
 ['When have you come back from Tokyo?', 'I have studied Japanese for three years.', 'I sold my old car the day before yesterday.', 'She has been busy since last Friday.', 'I have had this bike since I was ten.'],
 "이유 ▶ 의문사 When은 현재완료와 ❌ → When did you come back ~?\n오답 ▶ {1} for {3} since + 시점 {4} since + 절 → 계속 ✔ {2} 명확한 과거 + 과거 시제 ✔\n포인트 ▶ When / What time + 과거 시제", [])
T.flex('다음 문장을 현재완료로 바르게 바꾼 것은?', F, B('Did they forget his address?'),
 ['Have they forgotten his address?', 'Did they have forgotten his address?', 'Have they forget his address?', 'Has they forgotten his address?', 'Are they forgotten his address?'],
 "이유 ▶ Have + they + forgotten(forget-forgot-forgotten) ~?\n오답 ▶ {1} did ❌ {2} 동사원형 ❌ {3} they → Have {4} be동사 ❌\n포인트 ▶ 의문문 = Have/Has + 주어 + p.p.", [('address', '주소')])
T.flex('밑줄 친 부분을 묻는 의문문으로 알맞은 것은?', F, B(t('Tom has written [a letter] in English.')),
 ['What has Tom written in English?', 'What has Tom write in English?', 'What did Tom has written in English?', 'What Tom has written in English?', 'What have Tom written in English?'],
 "이유 ▶ 의문사 + has + 주어 + p.p. ~? → What has Tom written ~?\n오답 ▶ {1} p.p. written {2} did ❌ {3} has가 주어 앞으로 {4} Tom → has\n포인트 ▶ 의문사 의문문도 has를 주어 앞에", [])
T.flex('다음 빈칸에 들어갈 말이 순서대로 바르게 짝지어진 것은?', P, B('• I have played chess ' + BL + ' I was ten.', '• My friend has never ' + BL + ' to Paris.', '• She has been sick ' + BL + ' three days.'),
 ['since − been − for', 'for − gone − since', 'since − gone − for', 'for − been − since', 'since − been − since'],
 "이유 ▶ I was ten(시점) → since / 가 본 적 없다 → been / three days(기간) → for\n오답 ▶ 절 앞 for ❌, 기간 앞 since ❌, never gone to는 경험의 뜻과 맞지 않음\n포인트 ▶ 경험 = have been to", [])
T.flex('괄호 안 wear의 알맞은 형태가 순서대로 바르게 짝지어진 것은?', K, B('• I ' + BL + ' glasses when I went to school.', '• I ' + BL + ' contact lenses since I graduated from school.'),
 ['wore − have worn', 'have worn − wore', 'wore − wore', 'have worn − have worn', 'wear − have worn'],
 "이유 ▶ when I went to school(과거의 때) → wore / since ~ → have worn\n오답 ▶ when절(과거)과 현재완료 ❌, since와 과거 시제 ❌, 현재 wear ❌\n포인트 ▶ when 과거절 = 과거 / since = 현재완료", [('graduate', '졸업하다')])
T.flex('다음 중 대화가 <u>어색한</u> 것은?', K, '',
 ['A: Why are you coughing so much?<br>B: I\'ve caught a cold last week.', 'A: Where is your book?<br>B: I left it at home.', 'A: Have you sent the letter to him?<br>B: No, not yet.', 'A: How long have you known Jake?<br>B: For over three years.', 'A: Where is Jim?<br>B: He has left already.'],
 "이유 ▶ last week(명확한 과거) → I caught a cold last week.\n오답 ▶ {1} 과거 ✔ {2} 아직 안 보냄 ✔ {3} 기간 ✔ {4} 이미 떠났다 ✔\n포인트 ▶ 대화 속에서도 last ~ 와 현재완료 ❌", [('cough', '기침하다')])
T.flex('다음 중 현재완료의 용법이 나머지 넷과 <u>다른</u> 것은?', Y, '',
 ['Have you ever played the piano?', 'Have you finished the work already?', 'I have just finished the project.', "They've just arrived.", "My mom hasn't cooked dinner yet."],
 "이유 ▶ ever → 경험.\n오답 ▶ {1} already {2}·{3} just {4} yet → 모두 완료\n포인트 ▶ 같이 쓰인 부사로 용법 찾기", [])
T.flex('다음 문장의 의미로 알맞은 것은?', K, B('He has broken his leg.'),
 ['그는 다리가 부러졌고, 지금도 다친 상태이다.', '그는 다리가 부러졌지만, 지금은 다 나았다.', '그는 다리가 부러질 것이다.', '그는 다리가 부러진 적이 한 번도 없다.', '그는 지금 다리가 부러지고 있다.'],
 "이유 ▶ 현재완료(결과) = 과거의 일이 지금까지 이어짐 → 지금도 다친 상태\n오답 ▶ {1} He broke his leg.(지금 상태는 모름) {2} 미래 {3} 경험 부정 {4} 진행\n포인트 ▶ 현재완료 = 과거 + 현재", [], en=False)
T.flex('다음 밑줄 친 have의 쓰임이 나머지 넷과 <u>다른</u> 것은?', F, '',
 [t('Did you [have] dinner last evening?'), t('I [have] been to Jejudo three times.'), t('[Have] you finished your homework yet?'), t('I [have] never played such a game.'), t('[Have] you ever heard the news?')],
 "이유 ▶ have dinner = 저녁을 먹다(일반동사).\n오답 ▶ {1}~{4} 뒤에 p.p.(been · finished · played · heard) → 현재완료의 조동사\n포인트 ▶ Did ~ have + 명사 = 일반동사", [])
T.flex('다음 두 문장을 한 문장으로 바르게 나타낸 것은?', Y, B('Miriam watched <i>The Incredibles</i> five years ago. She watched the movie again last year.'),
 ['Miriam has watched <i>The Incredibles</i> twice.', 'Miriam was watching <i>The Incredibles</i> twice.', 'Miriam watched <i>The Incredibles</i> many years ago.', 'Miriam will watch <i>The Incredibles</i> twice.', 'Miriam has watched <i>The Incredibles</i> last year.'],
 "이유 ▶ 두 번 본 경험 → has watched ~ twice.\n오답 ▶ {1} 진행 {2} 두 번 본 내용이 빠짐 {3} 미래 {4} last year와 현재완료 ❌\n포인트 ▶ 횟수(twice) = 경험", [])
T.flex('다음 우리말을 영어로 바르게 옮긴 것은?', P, B('그녀는 6월 이래로 중국에 있다.'),
 ['She has been in China since June.', 'She is in China since June.', 'She was in China since June.', 'She has been in China for June.', 'She has been in China since in June.'],
 "이유 ▶ 6월부터 지금까지 계속 있다 → has been in ~ since June.\n오답 ▶ {1} 현재 {2} 과거 + since ❌ {3} June(시점) 앞 for ❌ {4} since in ❌\n포인트 ▶ have been in = 계속 ~에 있다", [])
T.flex('다음 중 어법상 <u>틀린</u> 문장의 개수는?', F, B('• I have swam in the river.', '• I have traveled to China.', '• I have win a singing contest.', '• I have not rode a bike.', '• I have danced in the street.'),
 ['3개', '1개', '2개', '4개', '5개'],
 "이유 ▶ 틀린 것: swam → swum, win → won, rode → ridden → 3개\n오답 ▶ traveled · danced(규칙 변화) ✔\n포인트 ▶ swim-swam-swum / ride-rode-ridden / win-won-won", [])
T.flex('다음 빈칸에 들어갈 수 <u>없는</u> 것은?', P, B("I've had the same bicycle " + BL + '. I need a new one.'),
 ['ten years ago', 'for ages', 'for five years', 'since I was 11', 'since my childhood'],
 "이유 ▶ ago는 과거 시제와만 → 현재완료 문장에 ❌\n오답 ▶ {1}·{2} for + 기간 {3}·{4} since + 시점 ✔\n포인트 ▶ ~ ago + 현재완료 ❌", [('for ages', '아주 오랫동안')])
T.flex('다음 글의 밑줄 친 부분과 현재완료의 용법이 같은 것은?', R, B(t('After only a few minutes, the machine stopped. "We [\'ve just arrived] in the jungle of 60 million years ago," Travis explained.')),
 ['The train has already left.', 'I have never seen a dinosaur.', 'He has lived here for a year.', 'She has gone to Busan.', 'We have known him since 2020.'],
 "이유 ▶ 본문 have just arrived → 완료. 정답 already → 완료.\n오답 ▶ {1} 경험 {2}·{4} 계속 {3} 결과\n포인트 ▶ just · already = 완료", [])
T.flex('다음 우리말을 영어로 바르게 옮긴 것은?', P, B('그는 2000년 이래로 가수이다.'),
 ['He has been a singer since 2000.', 'He is a singer since 2000.', 'He was a singer since 2000.', 'He has been a singer for 2000.', 'He has been a singer in 2000.'],
 "이유 ▶ 2000년부터 지금까지 → has been + since 2000.\n오답 ▶ {1} 현재 {2} 과거 + since ❌ {3} 연도(시점) 앞 for ❌ {4} in 2000은 과거의 한 때\n포인트 ▶ since + 연도", [])
T.flex('다음 빈칸에 공통으로 들어갈 말로 알맞은 것은?', Y, B('• I have not ' + BL + ' to Russia.', '• She has ' + BL + ' at home all day.'),
 ['been', 'gone', 'be', 'being', 'went'],
 "이유 ▶ 가 본 적 없다(have not been to) / 하루 종일 집에 있었다(has been at home) → been\n오답 ▶ {1} has gone at home ❌ {2}·{3}·{4} 과거분사가 아님\n포인트 ▶ be의 과거분사 been", [])
T.render()

# ═══════════════ 4차 (중상) ═══════════════
T = S('4', '현재완료 종합 (중상)', 7)
T.flex('다음 중 어법상 옳은 것끼리 짝지은 것은?', K, B("ⓐ John's grandfather has died in 2000.", 'ⓑ Where have you been last night?', "ⓒ I've lost my cell phone. I can't find it now.", "ⓓ I've finished my homework at 2 o'clock.", 'ⓔ Maria has just arrived at the subway station.'),
 ['ⓒ, ⓔ', 'ⓐ, ⓒ', 'ⓑ, ⓔ', 'ⓒ, ⓓ', 'ⓓ, ⓔ'],
 "이유 ▶ ⓒ 결과(지금도 없음) ⓔ 완료(just) ✔\n오답 ▶ ⓐ in 2000 → died ⓑ last night → were ⓓ at 2 o'clock → finished\n포인트 ▶ 시점 표현이 있으면 과거 시제", [])
T.fixed('다음 대화의 밑줄 친 ①~⑤ 중 어법상 <u>틀린</u> 것은?', K, B('A: ① ' + U('Have') + ' you ② ' + U('gone') + ' downtown ③ ' + U('yet') + '?', 'B: Yes, I ④ ' + U('have gone') + ' downtown ⑤ ' + U('three days ago') + '.'),
 None, 4,
 "이유 ▶ three days ago(명확한 과거) → I went downtown three days ago.\n오답 ▶ ① 의문문 Have ② p.p. ③ 의문문 yet(벌써) ⑤ 시간 표현 자체는 바름\n포인트 ▶ 대답에 ago가 있으면 과거 시제", [('downtown', '시내에')])
T.flex('다음 빈칸에 들어갈 말이 순서대로 바르게 짝지어진 것은?', P, B('• My sister has lived in Busan ' + BL + ' 20 years.', '• I have studied English ' + BL + ' last year.', '• We graduated from elementary school ' + BL + ' 2023.'),
 ['for − since − in', 'in − since − at', 'for − for − in', 'since − for − in', 'for − since − since'],
 "이유 ▶ 20 years(기간) → for / last year(시점) + 현재완료 → since / 과거 시제 + 연도 → in\n오답 ▶ 과거 시제 문장에 since ❌, last year 앞 for ❌, 기간 앞 in ❌\n포인트 ▶ 동사의 시제도 함께 보기", [('graduate from', '~을 졸업하다')])
T.flex('다음 문장에서 어법상 <u>어색한</u> 부분을 바르게 고친 것은?', K, B('Yumi has been born in Gwangju.'),
 ['has been → was', 'born → bear', 'in → at', 'has → have', '고칠 필요 없음'],
 "이유 ▶ 태어난 것은 과거의 한 사건 → Yumi was born in Gwangju.\n오답 ▶ {1}·{2}·{3} 고칠 곳이 아님 {4} 현재완료로 쓸 수 없는 문장\n포인트 ▶ be born은 과거 시제", [])
T.flex('괄호 안 study의 알맞은 형태가 순서대로 바르게 짝지어진 것은?', K, B('• Bill ' + BL + ' science two hours ago.', '• Bill ' + BL + ' science since 2010.'),
 ['studied − has studied', 'has studied − studied', 'studied − studied', 'has studied − has studied', 'studies − has studied'],
 "이유 ▶ two hours ago → 과거 studied / since 2010 → 현재완료 has studied\n오답 ▶ ago + 현재완료 ❌, since + 과거 ❌, 현재 studies ❌\n포인트 ▶ 시간 표현이 시제를 정함", [])
T.flex('다음 우리말을 영어로 바르게 옮긴 것은?', P, B('나는 여러 날 동안 그를 보지 못하고 있다.'),
 ["I haven't seen him for several days.", "I haven't seen him since several days.", "I haven't saw him for several days.", "I don't have seen him for several days.", 'I have not see him for several days.'],
 "이유 ▶ haven't + seen + for several days(기간).\n오답 ▶ {1} 기간 앞 since ❌ {2} saw → seen {3} don't have ❌ {4} see → seen\n포인트 ▶ 부정 = haven't + p.p.", [('several', '여러')])
T.flex('다음 짝지어진 두 문장의 의미가 서로 <u>다른</u> 것은?', Y, '',
 ['He has been to Busan.<br>= He went to Busan, and he is still there.', "He has gone to Busan.<br>= He went to Busan, so he isn't here now.", "I have lost my key.<br>= I lost my key, and I don't have it now.", 'It has rained for two hours.<br>= It began to rain two hours ago, and it is still raining.', 'She has lived here for 5 years.<br>= She began to live here 5 years ago, and she still lives here.'],
 "이유 ▶ has been to = 가 본 적 있다(경험) → 지금 거기 있다는 뜻이 아님. '가서 지금 거기 있다'는 has gone to.\n오답 ▶ {1} 결과 {2} 결과 {3}·{4} 계속 → 뜻이 같음\n포인트 ▶ been to(경험) / gone to(결과)", [])
T.flex('다음 중 경험 용법끼리 바르게 묶은 것은?', Y, B('ⓐ Have you ever heard of the koala?', 'ⓑ We have lived here since 1990.', 'ⓒ She has been to Canada twice.', 'ⓓ He has just come back.', 'ⓔ How long have you known her?'),
 ['ⓐ, ⓒ', 'ⓑ, ⓔ', 'ⓐ, ⓓ', 'ⓒ, ⓓ', 'ⓑ, ⓓ'],
 "이유 ▶ ⓐ ever · ⓒ twice → 경험\n오답 ▶ ⓑ · ⓔ 계속(since · How long) ⓓ 완료(just)\n포인트 ▶ ever · never · before · ~ times = 경험", [])
T.flex('다음 중 어법상 <u>틀린</u> 것끼리 짝지은 것은?', K, B('ⓐ Kevin has visited the country several times.', 'ⓑ He has never learned to play tennis.', 'ⓒ I have visited him last Friday.', 'ⓓ Bell has invented the telephone in 1876.'),
 ['ⓒ, ⓓ', 'ⓐ, ⓒ', 'ⓑ, ⓓ', 'ⓐ, ⓑ', 'ⓑ, ⓒ'],
 "이유 ▶ ⓒ last Friday → visited ⓓ in 1876 → invented\n오답 ▶ ⓐ several times(경험) ⓑ never(경험) ✔\n포인트 ▶ 역사적 사실(in + 연도) = 과거 시제", [('invent', '발명하다')])
T.flex('다음 표를 보고 Mr. Han이 한 대답으로 표와 일치하지 <u>않는</u> 것은?', Y, B('<b>Mr. Han\'s trips</b>', '2021 Kenya · 2022 China · 2023 Egypt · 2024 China · 2025 China'),
 ['Q: How many times have you been to China?<br>A: I have been there twice.', "Q: Have you ever been to Japan?<br>A: No, I haven't.", 'Q: Have you ever been to Africa?<br>A: Yes, I have. I have been to Kenya and Egypt.', 'Q: When did you go to Egypt?<br>A: I went there in 2023.', "Q: Have you been to Asia?<br>A: Yes, I have. I've been to China."],
 "이유 ▶ 중국은 2022 · 2024 · 2025년 → 세 번(three times)\n오답 ▶ {1} 일본 없음 {2} 케냐 · 이집트 = 아프리카 {3} When → 과거 시제 went {4} 중국 = 아시아 ✔\n포인트 ▶ How many times have you ~? = 몇 번 ~해 봤니?", [])
T.flex('다음 빈칸에 gone이 들어가야 하는 것은?', Y, '',
 ['Where is my daughter? Has she ' + BL + ' out?', "This place looks familiar. I've " + BL + ' here before.', 'She has ' + BL + ' busy since Monday.', 'My dad has ' + BL + ' a teacher for ten years.', 'I have ' + BL + ' in Seoul for two years.'],
 "이유 ▶ 딸이 안 보인다 → 나가고 없니? → has gone out(결과)\n오답 ▶ {1} 와 본 적 있다(been) {2}·{3}·{4} 계속 '~이다 · ~에 있다'(been)\n포인트 ▶ 지금 여기 없음 → gone", [('familiar', '익숙한')])
T.flex('다음 대화의 빈칸에 들어갈 질문으로 알맞은 것은?', P, B('A: ' + BL + '?', 'B: For three weeks.'),
 ['How long have you been in Korea', 'Have you ever driven a car', 'How often do you meet her', 'When did you come to Korea', 'Have you been in Korea'],
 "이유 ▶ For three weeks(기간) → How long ~? 질문\n오답 ▶ {1}·{4} Yes / No 질문 {2} 횟수 질문 {3} When엔 시점으로 대답\n포인트 ▶ How long have you ~? → for / since로 대답", [])
T.flex('다음 우리말을 영어로 바르게 옮긴 것은?', P, B('내 여동생은 어젯밤부터 감기로 앓아누워 있다.'),
 ['My little sister has been in bed with a cold since last night.', 'My little sister has been in bed with a cold for last night.', 'My little sister was in bed with a cold since last night.', 'My little sister has in bed been with a cold since last night.', 'My little sister has been in bed with a cold last night.'],
 "이유 ▶ has been in bed + with a cold + since last night.\n오답 ▶ {1} last night(시점) 앞 for ❌ {2} 과거 + since ❌ {3} 어순 ❌ {4} last night만 쓰면 과거의 한 때라 현재완료와 ❌\n포인트 ▶ since + 시점", [('cold', '감기')])
T.flex('다음 대화의 밑줄 친 부분을 바르게 고친 것은?', K, B('A: Have you ever heard of Nelson Mandela?', 'B: No. Who is that?', 'A: He ' + U('has fought') + ' for equality for black people in South Africa. He died in 2013.'),
 ['has fought → fought', 'has fought → fights', 'has fought → has been fought', 'has fought → is fighting', '고칠 필요 없음'],
 "이유 ▶ 2013년에 세상을 떠난 사람 → 지금과 이어지지 않음 → 과거 시제 fought\n오답 ▶ {1}·{3} 현재 {2} 수동 {4} 현재완료는 지금까지 이어지는 일에만\n포인트 ▶ 이미 끝난 일(돌아가신 분의 일) = 과거", [('equality', '평등')])
T.flex('다음 두 문장을 한 문장으로 바르게 나타낸 것은?', Y, B('She came to Seoul in 2000. She still lives in Seoul.'),
 ['She has lived in Seoul since 2000.', 'She has lived in Seoul for 2000.', 'She lived in Seoul since 2000.', 'She has come to Seoul since 2000.', 'She has lived in Seoul in 2000.'],
 "이유 ▶ 2000년부터 지금까지 살고 있다 → has lived ~ since 2000.\n오답 ▶ {1} 연도 앞 for ❌ {2} 과거 + since ❌ {3} come은 한 번 오는 일이라 since와 어색 {4} in 2000 ❌\n포인트 ▶ 계속 = live · know · be 같은 동사 + for/since", [])
T.flex('다음 중 현재완료의 용법이 나머지 넷과 <u>다른</u> 것은?', Y, '',
 ['He has gone to America.', 'I have seen him once.', 'I have never flown before.', 'Have you ever met Mike before?', 'He has eaten Chinese food twice.'],
 "이유 ▶ has gone to → 가고 없다(결과).\n오답 ▶ {1} once {2} never · before {3} ever · before {4} twice → 모두 경험\n포인트 ▶ gone to · lost = 결과", [])
T.flex('다음 중 의미상 <u>어색한</u> 것은?', K, '',
 ['Mr. Lee has closed the window, and it is open again.', 'Jenny has lost weight, and she is very slim now.', 'Jane has gone to Japan, and she is in Japan now.', "I have lost my notebook, and I don't have it now.", "Somebody has taken my purse, so I can't find it."],
 "이유 ▶ 창문을 닫아 둔 결과가 지금까지 → 창문은 지금 닫혀 있어야 함. '다시 열려 있다'와 맞지 않음 → closed\n오답 ▶ {1}~{4} 과거의 일이 지금 상태로 이어짐 ✔\n포인트 ▶ 현재완료 = 결과가 지금도 남아 있음", [('purse', '지갑')])
T.flex('다음 빈칸에 들어갈 말이 순서대로 바르게 짝지어진 것은?', F, B("• She hasn't worn the new clothes " + BL + '.', '• Have you ' + BL + ' brushed your teeth? (벌써 이 닦았니?)', '• The plane has ' + BL + ' arrived. (막 도착했다)'),
 ['yet − already − just', 'already − yet − just', 'yet − just − already', 'just − already − yet', 'already − just − yet'],
 "이유 ▶ 부정문 끝 '아직' → yet / '벌써' → already / '막' → just\n오답 ▶ 부정문 끝 already · just ❌, '막'의 뜻은 just\n포인트 ▶ yet(부정 · 의문 끝) · already · just(have와 p.p. 사이)", [('brush one\'s teeth', '이를 닦다')])
T.flex('다음 문장을 어법에 맞게 고친 것은?', K, B('When has the Civil War broken out?'),
 ['When did the Civil War break out?', 'When has the Civil War break out?', 'When was the Civil War broken out?', 'When does the Civil War break out?', 'When the Civil War broke out?'],
 "이유 ▶ When(의문사) → 과거 시제 의문문 did + 주어 + 동사원형.\n오답 ▶ {1} 현재완료 + When ❌ {2} 수동 ❌ {3} 현재 ❌ {4} 의문문 어순 ❌\n포인트 ▶ When + did ~?", [('break out', '(전쟁이) 일어나다')])
T.flex('다음 글의 밑줄 친 문장의 의미로 알맞은 것은?', R, B(t('"It ... is huge. [I\'ve never seen such a huge thing.] I\'m so scared," said Eckels.')),
 ['Eckels는 지금까지 그렇게 거대한 것을 본 적이 없다.', 'Eckels는 그렇게 거대한 것을 여러 번 본 적이 있다.', 'Eckels는 그렇게 거대한 것을 보러 갈 것이다.', 'Eckels는 어제 그렇게 거대한 것을 보았다.', 'Eckels는 그렇게 거대한 것을 보고 싶지 않다.'],
 "이유 ▶ have never seen = 지금까지 한 번도 본 적이 없다(경험). (교과서)\n오답 ▶ {1} 반대 {2} 미래 {3} 과거의 한 때 {4} 바람\n포인트 ▶ never + 현재완료 = 한 번도 ~한 적 없다", [], en=False)
T.render()

# ═══════════════ 5차 (상) ═══════════════
T = S('5', '현재완료 심화 ①', 3)
T.flex('다음 중 어법상 옳은 것은?', K, '',
 ['Steven has never flown across the Atlantic.', "She hasn't won the contest three years ago.", 'Last week, my uncle has driven a new car.', 'When have you woken up this morning?', 'I have knew her for a long time.'],
 "이유 ▶ never + has flown(fly-flew-flown) → 경험 ✔\n오답 ▶ {1} three years ago {2} Last week → 과거 시제 {3} When ❌ {4} know-knew-known → have known\n포인트 ▶ 시간 표현 · 의문사 · 과거분사를 모두 확인", [('Atlantic', '대서양')])
T.fixed('다음 문장의 밑줄 친 ①~⑤ 중 어법상 <u>어색한</u> 것은?', P, B('Chinese ① ' + U('has become') + ' ② ' + U('one of') + ' ③ ' + U('the most popular courses') + ' ④ ' + U('at the university') + ' ⑤ ' + U('for last year') + '.'),
 None, 5,
 "이유 ▶ last year(시점) 앞에는 since → since last year\n오답 ▶ ① 현재완료 ② one of + 복수 ③ 최상급 + 복수 명사 ④ 장소 ✔\n포인트 ▶ for + 기간 / since + 시점", [('course', '강좌')])
T.flex('다음 빈칸에 들어갈 말이 순서대로 바르게 짝지어진 것은?', P, B('• Have you ' + BL + ' lived abroad?', '• She has had her cell phone ' + BL + ' 10 months.', '• My aunt has lived in San Diego ' + BL + ' 2001.'),
 ['ever − for − since', 'ever − for − in', 'just − in − for', 'just − during − for', 'before − during − since'],
 "이유 ▶ 살아 본 적 있니? → ever / 10 months(기간) → for / 2001(시점) + 현재완료 → since\n오답 ▶ 현재완료 + in 2001 ❌, 10 months 앞 in · during ❌, Have you before lived ❌\n포인트 ▶ ever는 주어와 p.p. 사이", [('abroad', '해외에서')])
T.flex('다음 문장에서 밑줄 친 부분을 바르게 고친 것은?', P, B('Sumi ' + U('studies') + ' English since she was 7 years old.'),
 ['has studied', 'is studied', 'was studied', 'has to study', '고칠 필요 없음'],
 "이유 ▶ since + 과거 시점 → 지금까지 계속 → has studied\n오답 ▶ {1}·{2} 수동 {3} 의무(~해야 한다) {4} 현재 시제는 since와 ❌\n포인트 ▶ since가 있으면 주절은 현재완료", [])
T.flex('다음 중 대화가 <u>어색한</u> 것은?', K, '',
 ['A: Have you ever eaten Mexican food?<br>B: Yes, I have eaten it last week.', 'A: Have you ever seen a koala?<br>B: No, I have never seen a koala.', 'A: How long have you been here?<br>B: I came here three weeks ago.', 'A: Where have you been?<br>B: I have just walked around the village.', 'A: Have you finished your homework yet?<br>B: Yes, I finished it yesterday.'],
 "이유 ▶ last week → I ate it last week.\n오답 ▶ {1} 경험 ✔ {2} 과거 시제 + ago ✔ {3} 방금 산책함(완료) ✔ {4} yesterday엔 과거 시제 finished ✔\n포인트 ▶ 현재완료로 물어도 대답에 시점이 있으면 과거 시제", [])
T.flex('다음 중 어법상 옳은 문장의 개수는?', K, B("ⓐ It's been a long time since I met her.", 'ⓑ I have lost my bag on the street 3 days ago.', 'ⓒ She has gone shopping when I called her.', 'ⓓ They have just had lunch.', 'ⓔ He has listened to the song twice.'),
 ['3개', '1개', '2개', '4개', '5개'],
 "이유 ▶ 옳은 것 ⓐ(It's = It has) · ⓓ · ⓔ → 3개\n틀린 것 ▶ ⓑ 3 days ago → lost ⓒ when I called her(과거의 때) → went\n포인트 ▶ It's been ~ since … = …한 지 ~ 되었다", [])
T.flex('다음 문장과 의미가 같은 것은?', Y, B('It has been ten years since they got married.'),
 ['They got married ten years ago.', 'They will get married in ten years.', 'They have been married for twenty years.', 'They got married ten years later.', 'They are getting married now.'],
 "이유 ▶ 결혼한 지 10년이 되었다 = 10년 전에 결혼했다\n오답 ▶ {1} 미래 {2} 20년 ❌ {3} 10년 후 {4} 지금 결혼하는 중\n포인트 ▶ It has been + 기간 + since + 과거", [('get married', '결혼하다')])
T.flex('다음 두 문장을 한 문장으로 바르게 나타낸 것은?', Y, B('My mother was sick last Sunday, and she is still sick.'),
 ['My mother has been sick since last Sunday.', 'My mother has been sick for last Sunday.', 'My mother was sick since last Sunday.', 'My mother has been sick last Sunday.', 'My mother is sick since last Sunday.'],
 "이유 ▶ 지난 일요일부터 지금까지 아프다 → has been sick since last Sunday.\n오답 ▶ {1} 시점 앞 for ❌ {2}·{4} since와 과거 · 현재 ❌ {3} last Sunday만 쓰면 현재완료와 ❌\n포인트 ▶ 과거 + still → 현재완료 계속", [])
T.flex('다음 빈칸에 들어갈 말이 순서대로 바르게 짝지어진 것은?', K, B('• He ' + BL + ' dead for two years. (be)', '• He ' + BL + ' two years ago. (die)'),
 ['has been − died', 'has died − died', 'was − has died', 'has been − has died', 'died − has been'],
 "이유 ▶ 2년째 죽은 상태 → has been dead for two years / 2년 전에 죽었다 → died\n오답 ▶ die는 한 번에 끝나는 일이라 has died for ❌, ago + 현재완료 ❌\n포인트 ▶ 상태(be dead)는 for와 현재완료 / 사건(die)은 ago와 과거", [('dead', '죽은')])
T.flex('다음 중 현재완료의 용법과 예문이 <u>잘못</u> 연결된 것은?', Y, '',
 ['경험: I have already finished my report.', '경험: I have been to Rome.', "계속: We've lived together for 5 years.", '완료: My teacher has just called the roll.', '결과: Selina has gone to Spain.'],
 "이유 ▶ already → 완료 (경험 ❌)\n오답 ▶ {1} been to = 경험 {2} for = 계속 {3} just = 완료 {4} gone to = 결과 ✔\n포인트 ▶ 부사로 용법을 확인", [('call the roll', '출석을 부르다')], en=False)
T.flex('다음 중 우리말을 영어로 바르게 옮긴 것은?', K, '',
 ['그녀는 지금 미국에 가고 없다.<br>⇒ She has gone to America.', '너는 미국에 가 본 적이 있니?<br>⇒ Did you go to America?', '나는 작년에 이곳에 살았었다.<br>⇒ I have lived here last year.', '언제 너희 담임선생님을 만났니?<br>⇒ When have you met your homeroom teacher?', '나는 그를 3년 동안 알아 왔다.<br>⇒ I have known him since three years.'],
 "이유 ▶ 가고 없다 → has gone to ✔\n오답 ▶ {1} 경험 → Have you ever been to ~? {2} last year → lived {3} When → did you meet {4} 기간 → for three years\n포인트 ▶ 우리말 뜻에 맞는 시제 고르기", [('homeroom teacher', '담임 선생님')])
T.flex('다음 대화의 빈칸에 들어갈 말로 가장 알맞은 것은?', F, B("A: Have you heard about Hera's new action movie?", 'B: ' + BL + ' She plays a police officer.'),
 ['Yes, I have.', "No, I haven't.", 'Of course, I do.', "No, I didn't.", 'I hear the news.'],
 "이유 ▶ B가 영화 내용(경찰 역)을 알고 있음 → Yes, I have.\n오답 ▶ {1} 들은 적 없다면 내용을 말할 수 없음 {2} do로 대답 ❌ {3} didn't ❌ {4} 시제 ❌\n포인트 ▶ 뒤 문장으로 Yes / No 정하기", [])
T.fixed('다음 글의 밑줄 친 ⓐ~ⓔ 중 어법상 <u>어색한</u> 것은?', K, B('I ⓐ ' + U('have known') + ' Minho since we ⓑ ' + U('were') + ' in elementary school. We ⓒ ' + U('have played') + ' soccer together every weekend for five years. Last month, he ⓓ ' + U('has moved') + ' to Busan, so I ⓔ ' + U('miss') + ' him a lot.'),
 ['ⓐ', 'ⓑ', 'ⓒ', 'ⓓ', 'ⓔ'], 4,
 "이유 ▶ Last month(명확한 과거) → he moved to Busan\n오답 ▶ ⓐ since → 계속 ⓑ since 뒤 절은 과거 ⓒ for → 계속 ⓔ 지금 그리워함(현재) ✔\n포인트 ▶ since 뒤 절은 과거, last ~ 는 과거", [('elementary school', '초등학교')])
T.flex('다음 빈칸에 들어갈 말이 순서대로 바르게 짝지어진 것은?', Y, B('• My parents ' + BL + ' Australia, so they are not home now.', '• I ' + BL + ' Australia twice. I loved it.', '• My uncle ' + BL + ' Australia for three years. He still lives there.'),
 ['have gone to − have been to − has been in', 'have been to − have gone to − has been in', 'have gone to − have been in − has been to', 'have been in − have been to − has gone to', 'have gone to − have been to − has gone to'],
 "이유 ▶ 가고 없다 → have gone to / 두 번 가 봤다 → have been to / 3년째 거기 있다 → has been in\n오답 ▶ 각 빈칸의 뜻(결과 · 경험 · 계속)이 뒤바뀌면 틀림\n포인트 ▶ gone to(가고 없음) · been to(가 본 적) · been in(계속 있음)", [])
T.flex("'He has gone to America yesterday.'가 틀린 이유로 알맞은 것은?", K, '',
 ['yesterday처럼 명확한 과거를 나타내는 말은 현재완료와 함께 쓸 수 없기 때문', '3인칭 단수 주어에는 has를 쓸 수 없기 때문', 'go의 과거분사는 gone이 아니기 때문', 'to 뒤에 나라 이름을 쓸 수 없기 때문', 'yesterday는 문장 맨 앞에만 쓸 수 있기 때문'],
 "이유 ▶ yesterday → He went to America yesterday.\n오답 ▶ {1} 3인칭 단수 = has ✔ {2} go-went-gone ✔ {3}·{4} 사실이 아님\n포인트 ▶ yesterday · ago · last ~ · in 연도 · just now + 과거 시제", [], en=False)
T.flex('다음 질문과 대답이 <u>어울리지 않는</u> 것은?', F, '',
 ['Q: When have you arrived?<br>A: Ten minutes ago.', 'Q: How long have you lived here?<br>A: Since 2015.', 'Q: Have you ever ridden a horse?<br>A: No, never.', 'Q: How many times have you been to Jeju?<br>A: Twice.', 'Q: Has he finished the work yet?<br>A: Yes, he has.'],
 "이유 ▶ When은 현재완료와 ❌ → When did you arrive?\n오답 ▶ {1} since {2} never {3} 횟수 {4} has로 대답 ✔\n포인트 ▶ 질문 자체가 틀린 것도 찾기", [])
T.flex('다음 중 어법상 옳은 것끼리 묶인 것은?', K, B('ⓐ Have you ever tried Thai food?', "ⓑ I've been to the museum when I was ten.", "ⓒ She hasn't called me since Monday.", 'ⓓ We have known each other for a long time.', 'ⓔ He has met her the other day.'),
 ['ⓐ, ⓒ, ⓓ', 'ⓐ, ⓑ, ⓒ', 'ⓑ, ⓓ, ⓔ', 'ⓒ, ⓓ, ⓔ', 'ⓐ, ⓓ, ⓔ'],
 "이유 ▶ ⓐ 경험 ⓒ since ⓓ for ✔\n오답 ▶ ⓑ when I was ten → went ⓔ the other day(며칠 전) → met\n포인트 ▶ when절 · the other day = 과거", [])
T.flex('두 문장을 한 문장으로 바꾼 것 중 <u>틀린</u> 것은?', Y, '',
 ['Peter went to Japan. He is back home now.<br>→ Peter has gone to Japan.', 'Liz started to study Japanese two years ago. She still studies it.<br>→ Liz has studied Japanese for two years.', 'Mark started to play tennis in 2000. He still plays it.<br>→ Mark has played tennis since 2000.', "Jack arrived here four days ago. He's still here.<br>→ Jack has been here for four days.", 'My mom bought the house last year. She still has it.<br>→ My mom has had the house since last year.'],
 "이유 ▶ 지금 집에 돌아와 있음 → '가고 없다'(has gone to) ❌ → Peter has been to Japan.\n오답 ▶ {1} for {2} since {3} for {4} since → 계속 ✔\n포인트 ▶ 돌아왔으면 been to, 아직 거기 있으면 gone to", [])
T.flex('다음 글의 밑줄 친 문장의 의미로 알맞은 것은?', R, B(t('"How can we help you?" said Mr. Parker. "[I\'ve always wanted to see a dinosaur.] Is it possible?" asked Eckels.')),
 ['Eckels는 전부터 지금까지 줄곧 공룡을 보고 싶어 했다.', 'Eckels는 공룡을 한 번 본 적이 있다.', 'Eckels는 방금 공룡을 보았다.', 'Eckels는 공룡을 보러 가 버렸다.', 'Eckels는 공룡을 보고 싶었지만 지금은 아니다.'],
 "이유 ▶ have always wanted = (예전부터 지금까지) 항상 ~하고 싶었다(계속). (교과서)\n오답 ▶ {1} 경험 {2} 완료 {3} 결과 {4} 지금도 원하므로 Is it possible?\n포인트 ▶ always + 현재완료 = 지금까지 늘", [('possible', '가능한')], en=False)
T.flex('다음 우리말을 영어로 바르게 옮긴 것은?', F, B('여기서 얼마나 오래 일하셨나요?'),
 ['How long have you worked here?', 'How long have you work here?', 'How long you have worked here?', 'How long has you worked here?', 'When have you worked here?'],
 "이유 ▶ How long + have + 주어 + p.p. ~? (계속)\n오답 ▶ {1} p.p. worked {2} 어순 ❌ {3} you → have {4} When ❌\n포인트 ▶ How long have you ~? = 얼마나 오래 ~해 왔니?", [])
T.render()

# ═══════════════ 6차 (상) ═══════════════
T = S('6', '현재완료 심화 ②', 5)
T.flex('<보기>의 밑줄 친 부분과 용법이 같은 것은?', Y, B(t('<보기> I [have known] him for three years.')),
 ['Mrs. Black has lived in Korea for ten years.', 'She has already left for Paris.', 'I have never heard about the project.', 'Mr. Smith has just bought this sweater.', 'He has gone to London.'],
 "이유 ▶ <보기>와 정답 모두 for + 기간 → 계속.\n오답 ▶ {1}·{3} 완료(already · just) {2} 경험(never) {4} 결과(gone to)\n포인트 ▶ for + 기간 = 계속", [('project', '프로젝트')])
T.flex('다음 글의 밑줄 친 ⓐ~ⓔ 중 어법상 <u>틀린</u> 것의 개수는?', K, B('I ⓐ ' + U('have lived') + ' in this town since I ⓑ ' + U('was born') + '. I ⓒ ' + U('have visited') + ' the town museum many times. Last Sunday, I ⓓ ' + U('have gone') + ' there with my cousin. She liked it a lot, so we ⓔ ' + U('have gone') + ' there again yesterday.'),
 ['2개', '1개', '3개', '4개', '5개'],
 "이유 ▶ 틀린 것 ⓓ Last Sunday → went ⓔ yesterday → went → 2개\n오답 ▶ ⓐ since → 계속 ⓑ since 뒤 과거 ⓒ many times → 경험 ✔\n포인트 ▶ 같은 글 안에서도 시간 표현마다 시제가 달라짐", [('cousin', '사촌')])
T.flex('다음 빈칸에 since가 들어갈 수 <u>없는</u> 것은?', P, '',
 ['She moved to Seoul three years ' + BL + '.', 'We have been friends ' + BL + ' we were children.', 'It has been three years ' + BL + ' I last saw her.', 'He has worked here ' + BL + ' last spring.', 'I have lived here ' + BL + ' 2018.'],
 "이유 ▶ 과거 시제 moved + three years ago(~ 전에)\n오답 ▶ {1}·{2} since + 절 {3} since + last spring {4} since + 연도 ✔\n포인트 ▶ 기간 + ago = 과거 시제", [])
T.flex('다음 대화의 빈칸에 들어갈 말로 알맞은 것은?', Y, B('A: Where is Jisu? I need her help.', "B: She " + BL + " to the library. She'll be back soon."),
 ['has gone', 'has been', 'have gone', 'has go', 'has went'],
 "이유 ▶ 도서관에 가서 지금 여기 없음 → has gone to(결과)\n오답 ▶ {1} 갔다 왔다 → 지금 여기 있어야 함 {2} 주어 She → has {3} has + 동사원형 ❌ {4} went는 과거형\n포인트 ▶ 지금 없다 = has gone to", [])
T.flex('두 문장의 의미가 같도록 할 때 빈칸에 알맞은 것은?', F, B('Do you have an experience of visiting Italy?', '= ' + BL + ' Italy?'),
 ['Have you ever visited', 'Did you visit yesterday', 'Are you visiting', 'Have you ever visit', 'Do you ever visited'],
 "이유 ▶ 경험이 있니? = Have you ever + p.p. ~?\n오답 ▶ {1} 과거의 한 때 {2} 진행 {3} p.p. visited {4} do + p.p. ❌\n포인트 ▶ 경험 = Have you ever ~?", [('experience', '경험')])
T.flex('다음 중 어법상 <u>틀린</u> 것끼리 짝지은 것은?', F, B("ⓐ Tom hasn't met his uncle for four years.", 'ⓑ They have played tennis since 2009.', 'ⓒ Have you seen the movie?', 'ⓓ She has never be to Africa.', "ⓔ He doesn't have finished his homework yet."),
 ['ⓓ, ⓔ', 'ⓐ, ⓓ', 'ⓑ, ⓔ', 'ⓐ, ⓒ', 'ⓒ, ⓓ'],
 "이유 ▶ ⓓ be → been ⓔ doesn't have finished → hasn't finished\n오답 ▶ ⓐ 부정 + for ⓑ since ⓒ 의문문 ✔\n포인트 ▶ 부정 = haven't / hasn't + p.p.", [])
T.flex('다음 중 현재완료와 함께 쓸 수 있는 것만 모두 고른 것은?', K, B('ⓐ just', 'ⓑ just now', 'ⓒ since Monday', 'ⓓ two days ago', 'ⓔ ever'),
 ['ⓐ, ⓒ, ⓔ', 'ⓐ, ⓑ, ⓒ', 'ⓑ, ⓓ', 'ⓒ, ⓓ, ⓔ', 'ⓐ, ⓑ, ⓔ'],
 "이유 ▶ just(막) · since Monday · ever ✔\n오답 ▶ ⓑ just now(방금 전) · ⓓ two days ago → 과거 시제\n포인트 ▶ just ✔ / just now ❌", [])
T.flex('다음 글의 내용과 일치하지 <u>않는</u> 것은?', Y, B('Jiho started to learn the guitar in 2022, and he still plays it every day. He visited Japan in 2023. He visited Japan again in 2025.'),
 ['Jiho has never been to Japan.', 'Jiho has learned the guitar since 2022.', 'Jiho has been to Japan twice.', 'Jiho visited Japan in 2023.', 'Jiho has played the guitar for some years.'],
 "이유 ▶ 2023년, 2025년 두 번 일본에 감 → 가 본 적이 없다 ❌\n오답 ▶ {1} since 2022 ✔ {2} twice ✔ {3} 2023년 + 과거 ✔ {4} 몇 년째 ✔\n포인트 ▶ 글의 사실을 현재완료로 바꿔 보기", [])
T.flex('다음 중 어법상 옳은 것은?', K, '',
 ['Since when have you lived in this city?', 'I have seen her at the party two days ago.', 'How long ago have you met him?', 'He has come back just now.', 'I have finished it when you called.'],
 "이유 ▶ Since when ~? = 언제부터 ~? → 현재완료와 ✔\n오답 ▶ {1} two days ago {2} How long ago {3} just now {4} when you called → 모두 과거의 한 때라 과거 시제\n포인트 ▶ since when ✔ / when · ago ❌", [])
T.flex('다음 밑줄 친 have의 쓰임이 나머지 넷과 <u>다른</u> 것은?', F, '',
 [t('We [have] lunch at noon.'), t('She [has] been to Paris.'), t('[Have] you finished it?'), t('He [has] lost his key.'), t('They [have] known each other since 2010.')],
 "이유 ▶ have lunch = 점심을 먹다(일반동사, 뒤에 명사).\n오답 ▶ {1}~{4} 뒤에 p.p.(been · finished · lost · known) → 현재완료 조동사\n포인트 ▶ have 바로 뒤가 p.p.인지 명사인지", [])
T.flex('두 문장의 의미가 같도록 할 때 빈칸에 알맞은 것은?', P, B('They got married ten years ago.', '= Ten years ' + BL + ' since they got married.'),
 ['have passed', 'pass', 'have pass', 'was passed', 'passing'],
 "이유 ▶ 결혼한 이후로 10년이 지났다 → Ten years have passed since ~.\n오답 ▶ {1} 현재 {2} p.p. passed {3} 수동 · 수 ❌ {4} 동사가 없음\n포인트 ▶ 기간 + have passed + since + 과거", [('pass', '(시간이) 지나다')])
T.flex('다음 중 대화가 <u>어색한</u> 것은?', K, '',
 ['A: Did you see Jina yesterday?<br>B: Yes, I have seen her at the mall.', 'A: I have lost weight.<br>B: You look great!', "A: Where's Ben?<br>B: He has gone home.", 'A: How long has it rained?<br>B: Since this morning.', 'A: Have you ever been to Busan?<br>B: Yes, twice.'],
 "이유 ▶ yesterday에 대한 대답 → Yes, I saw her at the mall.\n오답 ▶ {1} 결과 {2} 가고 없음 {3} since {4} 횟수 ✔\n포인트 ▶ 과거로 물으면 과거로 대답", [])
T.flex('다음 우리말을 영어로 바르게 옮긴 것은?', P, B('나는 10살 때부터 피아노를 쳐 왔지만, 아직 이 곡을 연주해 보지 않았다.'),
 ["I have played the piano since I was ten, but I haven't played this song yet.", "I have played the piano since I am ten, but I haven't played this song yet.", "I have played the piano for I was ten, but I haven't played this song yet.", "I have played the piano since I was ten, but I haven't played this song already.", "I have played the piano since I was ten, but I haven't play this song yet."],
 "이유 ▶ since + 과거절(I was ten) / 부정문 '아직' → yet\n오답 ▶ {1} since 뒤 절은 과거 {2} 절 앞 for ❌ {3} 부정문의 아직 = yet {4} p.p. played\n포인트 ▶ since 절 · yet 위치 · p.p. 세 가지", [('song', '곡')])
T.flex('다음 글의 (A), (B), (C)에서 알맞은 것끼리 짝지은 것은?', K, B('I (A) [ lived / have lived ] in Seoul for five years. I moved here when I (B) [ was / have been ] ten. Last year, I (C) [ joined / have joined ] the school band.'),
 ['have lived − was − joined', 'lived − was − joined', 'have lived − have been − joined', 'have lived − was − have joined', 'lived − have been − have joined'],
 "이유 ▶ (A) 5년째 살고 있음 → have lived (B) when + 과거 → was (C) Last year → joined\n오답 ▶ when절 · last year와 현재완료 ❌, (A)를 과거로 쓰면 지금은 안 산다는 뜻\n포인트 ▶ 문장마다 시간 표현 확인", [('join', '가입하다')])
T.flex('다음 문장에서 어색한 부분을 바르게 고친 것은?', P, B('I have been sick since three days.'),
 ['since → for', 'have been → was', 'sick → sickness', 'three days → three day', '고칠 필요 없음'],
 "이유 ▶ three days(기간) → for three days\n오답 ▶ {1} 지금도 아프므로 현재완료 ✔ {2} be + 형용사 ✔ {3} three + 복수 ✔ {4} 틀린 곳이 있음\n포인트 ▶ 숫자 + 기간 → for", [])
T.flex('다음 두 문장에 대한 설명으로 옳은 것은?', Y, B('(A) She has been to Spain.', '(B) She has gone to Spain.'),
 ['(A)는 스페인에 가 본 경험을, (B)는 스페인에 가서 지금 여기 없음을 나타낸다.', '(A)와 (B) 모두 그녀가 지금 스페인에 있다는 뜻이다.', '(A)는 그녀가 지금 스페인에 있다는 뜻이다.', '(B)는 그녀가 스페인에 갔다가 돌아왔다는 뜻이다.', '(A)와 (B)는 뜻이 같다.'],
 "이유 ▶ been to = 경험(갔다 옴) / gone to = 결과(가고 없음)\n오답 ▶ {1}·{4} 두 문장은 뜻이 다름 {2} 지금 스페인에 있는 것은 (B) {3} 돌아온 것은 (A)\n포인트 ▶ been to vs gone to", [], en=False)
T.flex('우리말에 맞게 주어진 단어를 배열한 것으로 알맞은 것은?', F, B('당신은 얼마나 오래 두통을 앓았습니까?', '( you / had / how long / have / a headache )'),
 ['How long have you had a headache?', 'How long you have had a headache?', 'How long have had you a headache?', 'How long has you had a headache?', 'How long did you have had a headache?'],
 "이유 ▶ How long + have + you + had(have-had-had) + a headache?\n오답 ▶ {1}·{2} 어순 ❌ {3} you → have {4} did ❌\n포인트 ▶ have had = 현재완료 have + p.p. had", [('headache', '두통')])
T.flex('다음 중 어법상 <u>어색한</u> 것은?', F, '',
 ['She has not be to New York yet.', "I haven't seen my dog. Have you?", 'He has listened to the song twice.', 'Have you read the book that you bought a week ago?', 'They have just had lunch.'],
 "이유 ▶ be → been: She has not been to New York yet.\n오답 ▶ {1} Have you (seen it)? ✔ {2} twice ✔ {3} bought a week ago는 관계절 속 과거 ✔ {4} have had ✔\n포인트 ▶ 관계절의 과거 시제는 문장 전체와 따로", [])
T.flex("다음 중 '계속' 용법의 개수는?", Y, B('ⓐ I have been busy since yesterday.', 'ⓑ Have you ever eaten tacos?', 'ⓒ How long have you known her?', 'ⓓ She has just left.', 'ⓔ He has lived here for a year.'),
 ['3개', '1개', '2개', '4개', '5개'],
 "이유 ▶ 계속: ⓐ since · ⓒ How long · ⓔ for → 3개\n오답 ▶ ⓑ ever(경험) ⓓ just(완료)\n포인트 ▶ for · since · How long = 계속", [('taco', '타코')])
T.flex('다음 우리말과 같도록 할 때 빈칸에 들어갈 말이 바르게 짝지어진 것은?', F, B('그는 그 영화를 두 번 봤지만, 나는 아직 못 봤다.', '→ He has seen the movie ' + BL + ', but I ' + BL + ' it yet.'),
 ["twice − haven't seen", "twice − haven't saw", "once − haven't seen", 'twice − have seen', "two times ago − haven't seen"],
 "이유 ▶ 두 번 → twice / 아직 못 봤다 → haven't seen ~ yet\n오답 ▶ {1} saw → seen {2} 한 번 ❌ {3} 긍정 ❌ {4} ago ❌\n포인트 ▶ 경험 횟수 + 부정 완료(yet)", [])
T.render()
