from jfw import *
S = PREP['32']['sents'][:]; S[5] = S[5].replace('______________________________', 'demonstrate that they listened'); assert S[5].endswith('listened.')
p = load(32, '32번 · 빈칸', sents=S)
VOCAB = words(32)
B = 'demonstrate that they listened'
EXAM = [EXQ(32, '32. 다음 빈칸에 들어갈 말로 가장 적절한 것은?', p.blank(B), [
 "avoid showing their feelings", "demonstrate that they listened", "figure out their hidden intention", "collect enough information before deciding", "consider whether their concern makes sense"], 1,
 "정답 ▶ ② 자신이 귀를 기울였다는 것을 보여 줘야\n이유: 경청받는다고 느끼려면 세 가지 — ① 주의를 기울였다(paid attention) ② 이해했다(understood) ③ ______. 뒤에서 반응이 없는 사람은 주의를 기울이고 이해했더라도 '들었음을 나타내는 외적인 신호(outward signal)'가 없으면 알 수 없다 → 셋째 = 들었다는 것을 '보여 주기'\n오답 ▶ ① 감정을 숨기기 — 신호가 필요하다는 것과 반대 ③ 숨은 의도 파악 ④ 결정 전 정보 수집 ⑤ 우려가 타당한지 고려 — 모두 '보여 주기'와 무관\n포인트 ▶ outward signal that indicates they listened = demonstrate that they listened", v=False),
 EXQ(32, '다음 글의 요지로 가장 적절한 것은?', p.full(), [
 "상대가 경청받는다고 느끼게 하려면 들었다는 신호를 겉으로 보여 줘야 한다.", "고객의 불만은 관리자가 직접 해결해야 한다.", "상대의 말을 완벽히 이해하는 것이 반응보다 중요하다.",
 "대화할 때는 말을 줄이고 조용히 듣기만 해야 한다.", "고객과 동료는 서로 다른 방식으로 대해야 한다."], 0,
 "정답 ▶ ① 상대가 경청받는다고 느끼게 하려면 들었다는 신호를 겉으로 보여 줘야 한다.\n이유: This last part is key. + without some sort of outward signal ~ it’s impossible to know\n오답 ▶ ② 관리자 해결 이야기 아님 ③ 이해만으로는 부족 ④ 반응 없이 듣기만 하면 알 수 없음 ⑤ whether customers or otherwise — 누구나 같음"),
 EXQ(32, '다음 빈칸에 들어갈 말로 가장 적절한 것은?', p.blank('no response'), ["no response", "a quick answer", "a warm smile", "useful advice", "many questions"], 0,
 "정답 ▶ ① no response (아무 반응도 없음)\n이유: 주의를 기울이고 이해했을지라도 '신호가 없으면' 알 수 없다는 상황을 상상 → 반응이 '없는' 사람\n오답 ▶ ②③④⑤ 모두 반응(신호)이 있는 경우 → 글의 예시와 반대")]
PICK1 = [PK(p, 'People, whether', 'heard', 'ignored', "정답 ▶ heard (경청받는)\n오답 ▶ ignored (무시당하는)\n이유: 사람들이 원하는 것 = 자신의 말이 '들리는' 것"),
 PK(p, 'When someone calls', 'listening', 'objecting', "정답 ▶ listening (귀 기울이는)\n오답 ▶ objecting (반대하는)\n이유: 우려 사항에 '귀 기울이고' 해결해 줄 것처럼 느끼길 원함"),
 PK(p, 'First, they', 'attention', 'objection', "정답 ▶ attention (주의)\n오답 ▶ objection (반대)\n이유: 첫째 조건 = 상대가 내 말에 '주의를 기울였다'"),
 PK(p, 'This last part', 'key', 'minor', "정답 ▶ key (핵심적인)\n오답 ▶ minor (사소한)\n이유: 뒤에서 이 셋째 조건이 없으면 알 수 없다고 설명 → '핵심'"),
 PK(p, 'But without', 'outward', 'inner', "정답 ▶ outward (외적인, 겉으로 드러나는)\n오답 ▶ inner (내적인)\n이유: 상대가 알 수 있으려면 '겉으로 보이는' 신호가 필요"),
 PK(p, 'But without', 'impossible', 'easy', "정답 ▶ impossible (불가능한)\n오답 ▶ easy (쉬운)\n이유: 신호가 '없이는(without)' 실제로 들었는지 알 수 없음")]
TF = [TF(p, "Only customers want to feel heard.", False, "whether customers or otherwise", "정답 ▶ F\n이유: 고객이든 아니든 모두 경청받기를 원해요."),
 TF(p, "According to the writer, three things are needed for someone to feel heard.", True, "three things have to happen", "정답 ▶ T\n이유: 경청받는다고 느끼려면 세 가지가 필요해요."),
 TF(p, "Feeling that the other person understood is one of the conditions.", True, "the other person understood what they said", "정답 ▶ T\n이유: 둘째 조건이에요."),
 TF(p, "The writer says the third condition is the least important.", False, "This last part is key", "정답 ▶ F\n이유: 이 마지막 부분이 핵심이에요."),
 TF(p, "A person who gives no response might still have understood everything.", True, "They might even have understood it completely", "정답 ▶ T\n이유: 반응이 없는 사람도 완전히 이해했을 수 있어요."),
 TF(p, "Without an outward signal, we can easily tell whether someone listened.", False, "it’s impossible to know whether or not they actually did", "정답 ▶ F\n이유: 외적인 신호 없이는 알 수 없어요.")]
MC = [MC(p, "글의 내용과 일치하지 <u>않는</u> 것은?", [
 "Paying attention is enough to make people feel heard.", "People want someone to address their concerns.", "Understanding what someone said is one condition for feeling heard.",
 "Someone with no response may have attended to everything.", "An outward signal shows that a person listened."],
 "정답 ▶ Paying attention is enough to make people feel heard.\n이유: 세 가지가 모두 필요하고, 특히 셋째(들었다는 걸 보여 주기)가 핵심\n포인트 ▶ address = 해결하다 · attend to = 주의를 기울이다 · indicate ≒ show",
 [["주의를 기울이는 것만으로 경청받는다고 느끼게 하기 충분하다.", "three things have to happen", "✗ 셋 다 필요"], ["사람들은 누군가 자신의 우려를 해결해 주길 원한다.", "going to address them", "일치"], ["말한 것을 이해하는 것은 한 가지 조건이다.", "understood what they said", "일치"], ["반응 없는 사람도 모든 것에 주의를 기울였을 수 있다.", "They might have attended to everything we said", "일치"], ["외적인 신호는 그 사람이 들었다는 것을 보여 준다.", "outward signal that indicates they listened", "show ≒ indicate"]])]
PICK2 = [PK(p, 'People, whether', 'or otherwise', 'and otherwise', "정답 ▶ or\n이유: whether A or B (A이든 B이든)"),
 PK(p, 'People, whether', 'heard', 'hearing', "정답 ▶ heard\n이유: feel + 과거분사 — 내 말이 '들리는' 수동 (feel heard)"),
 PK(p, 'But for someone', 'for someone', 'of someone', "정답 ▶ for\n이유: to부정사의 의미상 주어 for + 목적격"),
 PK(p, 'First, they', 'what they said', 'that they said', "정답 ▶ what\n이유: 전치사 to 뒤 + said의 목적어가 없는 불완전한 절 → what"),
 PK(p, 'Imagine talking', 'talking', 'to talk', "정답 ▶ talking\n이유: imagine + 동명사"),
 PK(p, 'Imagine talking', 'who provided', 'provided', "정답 ▶ who provided\n이유: someone을 꾸미는 관계절 — 주격 관계대명사 who 필요(provided만 쓰면 '제공받은'의 뜻이 되고 목적어 no response와 안 맞음)"),
 PK(p, 'They might even', 'completely', 'complete', "정답 ▶ completely\n이유: 동사 understood를 꾸미는 부사")]
VERB = [VB(p, 'When someone calls', 'to speak', 'speak', "정답 ▶ to speak\n이유: ask + to부정사 (~하기를 요청하다)"),
 VB(p, 'They might have', 'attended', 'attend', "정답 ▶ attended\n이유: might have + p.p. (~했을지도 모른다)"),
 VB(p, 'But without', 'to know', 'know', "정답 ▶ to know\n이유: 가주어 it ~ 진주어 to부정사")]
ERR = [ER(p, 'But for someone', ['for', ('to feel', 'feel'), 'have to'], 1, 'to feel', "틀린 곳 ▶ ② feel → to feel\n이유: '~하기 위해서는' 목적의 to부정사 (for someone to feel heard)\n나머지 ▶ ① 의미상 주어 ✔ ③ three things → have ✔"),
 ER(p, 'Imagine talking', ['Imagine', ('talking', 'to talk'), 'who'], 1, 'talking', "틀린 곳 ▶ ② to talk → talking\n이유: imagine은 동명사를 목적어로\n나머지 ▶ ① 명령문 동사원형 ✔ ③ 주격 관계대명사 ✔"),
 ER(p, 'But without', ['that indicates', ('to know', 'know'), 'whether'], 1, 'to know', "틀린 곳 ▶ ② know → to know\n이유: 가주어 it ~ 진주어 to부정사\n나머지 ▶ ① 주격 관계대명사 + 단수 동사(signal) ✔ ③ whether or not ✔")]
SCR = [1, 2, 3, 5, 7, 10]
ORDER = [[2, 3, 4, 5], [7, 8, 9, 10]]
INSERT = [([3, 4, 5, 6], 2, "정답 ▶ ② (And third ~ 문장)\n이유: First → Second → And third 순서. 그 뒤 This last part(이 마지막 부분)가 셋째를 가리켜요."),
 ([7, 8, 9, 10], 3, "정답 ▶ ③ (But without ~ 문장)\n이유: 주의를 기울였을 수도, 이해했을 수도 있다 → But 신호가 없으면 알 수 없다 — 양보 뒤의 But")]
ODD = [([1, 2, "Most customer service centers are open twenty-four hours a day.", 3], 2, "정답 ▶ ③\n이유: 경청받는다고 느끼는 세 가지 조건이 이어지는 흐름이에요. 고객 센터 운영 시간은 관계없어요.")]
BLANK = [BL(p, 'When someone calls', 'concerns', ["rewards", "schedules", "secrets"], "정답 ▶ concerns (우려 사항)\n이유: 고객 센터에 전화하고 관리자를 찾는 사람 → 걱정·불만을 들어 주고 해결해 주길 원함\n오답 ▶ rewards 보상 · schedules 일정 · secrets 비밀"),
 BL(p, 'Second, they', 'understood', ["forgot", "repeated", "ignored"], "정답 ▶ understood (이해했다)\n이유: 첫째 주의 → 둘째 이해 → 셋째 보여 주기. 뒤에서 They might even have understood it로 다시 등장\n오답 ▶ forgot 잊었다 · repeated 반복했다 · ignored 무시했다"),
 BL(p, 'But without', 'signal', ["silence", "doubt", "rule"], "정답 ▶ signal (신호)\n이유: 들었음을 '나타내는(indicates)' 것 → 신호\n오답 ▶ silence 침묵 · doubt 의심 · rule 규칙")]
GRAM = [{'q': "빈칸에 알맞은 것은?<br><b>People want to feel ______.</b>", 'opts': ["heard", "hearing", "to hear", "hear"], 'ex': "정답 ▶ heard\n이유: feel + 과거분사(수동) — '경청받는다고' 느끼다"},
 {'q': "빈칸에 알맞은 것은?<br><b>They have to feel like the other person paid attention to ______ they said.</b>", 'opts': ["what", "that", "which", "who"], 'ex': "정답 ▶ what\n이유: 선행사 없음 + 목적어 빠진 절 → what"},
 {'q': "빈칸에 알맞은 것은?<br><b>Imagine ______ to someone who provided no response.</b>", 'opts': ["talking", "to talk", "talk", "talked"], 'ex': "정답 ▶ talking\n이유: imagine + 동명사"},
 {'q': "빈칸에 알맞은 것은?<br><b>They might ______ attended to everything we said.</b>", 'opts': ["have", "had", "be", "having"], 'ex': "정답 ▶ have\n이유: might have + p.p. = ~했을지도 모른다(과거 추측)"}]
SUMQ = [SUM(p, "For people to feel heard, the listener must not only pay attention and understand but also give an (A) ______ sign that shows they (B) ______.", [
 "(A) outward – (B) listened", "(A) outward – (B) agreed", "(A) inner – (B) listened", "(A) hidden – (B) decided", "(A) honest – (B) apologized"],
 "정답 ▶ (A) outward – (B) listened\n(A) 겉으로 보이는 신호(outward signal) → outward\n(B) 들었다는 것을 보여 줌(indicates they listened) → listened\n오답 ▶ agreed 동의했다(동의가 아니라 '들었다') · inner/hidden 안 보이는 신호(반대)",
 ["outward signal that indicates they listened", "paid attention to what they said"])]
