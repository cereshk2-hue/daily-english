from jfw import *
S = PREP['33']['sents'][:]; assert S[7].endswith('_.'); S[7] = re.sub(r'_+', 'does not sufficiently define art', S[7])
p = load(33, '33번 · 빈칸', sents=S)
VOCAB = words(33)
O = [re.sub(r'^[①-⑤]\s*', '', x) for x in Q['33']['opts']]
EXAM = [EXQ(33, '33. 다음 빈칸에 들어갈 말로 가장 적절한 것은?', p.blank('does not sufficiently define art'), O, 0,
 "정답 ▶ ① does not sufficiently define art (예술을 충분히 정의하지 못한다)\n이유: '현실을 모방하는 것'이라는 예술의 정의에는 문제가 있다(has a problem) → Pollock은 아무것도 모방하지 않은 작품을 만드는 데 성공 → 모방(mimesis)이라는 그리스 예술관은 예술을 충분히 정의하지 못함\n오답 ▶ ② 역사적으로 추상 예술보다 선호된다 ③ 현대 예술만큼 비판받을 수 없다 ④ 시대와 상관없이 예술이 보편적임을 증명한다 ⑤ 현대 예술가들이 그리스 양식을 되살리도록 영감을 준다 — 모두 '정의의 문제'와 무관\n포인트 ▶ though(하지만)가 있는 문장이 주제문: This definition ~ has a problem", v=False),
 EXQ(33, '다음 글의 주제로 가장 적절한 것은?', p.full(), [
 "limitations of defining art as copying reality", "reasons ancient Greek paintings disappeared", "the realism of ancient Greek pottery",
 "how Pollock learned from Greek sculpture", "the popularity of the New York School"], 0,
 "정답 ▶ ① 예술을 현실의 모방으로 정의하는 것의 한계\n이유: 그리스인의 예술관(모방) → 그 정의의 문제 → Pollock의 반례 → 충분한 정의가 아님\n오답 ▶ ② 그림이 사라진 이유는 일부 내용 ③ 일부 예시 ④ Pollock은 '모방하지 않음' ⑤ 인기 이야기 없음"),
 EXQ(33, '다음 빈칸에 들어갈 말로 가장 적절한 것은?', p.blank('copy visual experience'), [
 "copy visual experience", "express inner feelings", "avoid real objects", "please the gods", "sell artwork"], 0,
 "정답 ▶ ① copy visual experience (시각적 경험을 모방하다)\n이유: 바로 뒤 '이 접근(This approach)이 그리스 조각·도자기의 사실주의(realism)에 나타남' + this definition of art as copying reality\n오답 ▶ ② 내면 감정 표현 ③ 실제 사물 피하기(Pollock 쪽) ④ 신을 기쁘게 하기 ⑤ 작품 판매")]
PICK1 = [PK(p, 'This approach appears', 'realism', 'abstraction', "정답 ▶ realism (사실주의)\n오답 ▶ abstraction (추상)\n이유: 시각적 경험을 '모방'하는 접근 → 사실주의"),
 PK(p, 'We must sadly note', 'no paintings', 'many paintings', "정답 ▶ no paintings\n오답 ▶ many paintings\n이유: 시간과 날씨의 작용 때문에 → 오늘날 '하나도' 남아 있지 않음 → 그래서 짐작(surmise)만 할 수 있음"),
 PK(p, 'We can only surmise', 'surmise', 'prove', "정답 ▶ surmise (짐작하다)\n오답 ▶ prove (증명하다)\n이유: 그림이 남아 있지 않음 → only + 짐작할 수밖에 없음"),
 PK(p, 'Jackson Pollock', 'intentionally', 'accidentally', "정답 ▶ intentionally (의도적으로)\n오답 ▶ accidentally (우연히)\n이유: 다음 문장 consciously avoid(의식적으로 피했다)"),
 PK(p, 'While painting these works', 'avoid', 'enjoy', "정답 ▶ avoid (피하다)\n오답 ▶ enjoy (즐기다)\n이유: 아무것도 모방하지 않은 작품 → 알아볼 수 있는 사물을 닮은 흔적은 '피함'")]
TF = [TF(p, "The ancient Greeks believed that artists should copy visual experience.", True, "the visual artist’s goal was to copy visual experience", "정답 ▶ T\n이유: 시각 예술가의 목표는 시각적 경험을 모방하는 것이라고 생각했어요."),
 TF(p, "Many paintings by ancient Greek artists still exist today.", False, "no paintings from ancient Greek artists exist today", "정답 ▶ F\n이유: 오늘날 하나도 남아 있지 않아요."),
 TF(p, "We can guess the quality of Greek paintings from drawings on pottery.", True, "drawings that survive on ancient Greek pottery", "정답 ▶ T\n이유: 도자기에 남은 그림 등을 바탕으로 짐작해요."),
 TF(p, "Pollock tried to copy existing objects in his art.", False, "intentionally did not copy existing objects in his art", "정답 ▶ F\n이유: 의도적으로 모방하지 않았어요."),
 TF(p, "Pollock and his fellow artists created artwork that copied nothing.", True, "They succeeded at making artwork that did not copy anything", "정답 ▶ T\n이유: 아무것도 모방하지 않은 작품을 만드는 데 성공했어요.")]
MC = [MC(p, "글의 내용과 일치하지 <u>않는</u> 것은?", [
 "Pollock’s works proved that copying reality is the only goal of art.", "The realism of Greek sculpture reflects the Greek view of art.", "Time and weather destroyed ancient Greek paintings.",
 "Pollock was a leader in the New York School of the 1950s.", "Pollock’s group avoided marks that looked like recognizable objects."],
 "정답 ▶ Pollock’s works proved that copying reality is the only goal of art.\n이유: 오히려 모방하지 않은 작품으로 모방이 예술을 충분히 정의하지 못함을 보여 주었어요.",
 [["Pollock의 작품은 현실 모방이 예술의 유일한 목표임을 증명했다.", "thus demonstrating that the ancient Greek view of art as mimesis", "✗ 반대"], ["그리스 조각의 사실주의는 그리스 예술관을 반영한다.", "This approach appears in the realism of ancient Greek sculpture", "일치"],
  ["시간과 날씨가 고대 그리스 회화를 파괴했다.", "due to the action of time and weather", "일치"], ["Pollock은 1950년대 뉴욕 화파의 리더였다.", "a leader in the New York School of the 1950’s", "일치"], ["Pollock 일행은 알아볼 수 있는 사물처럼 보이는 흔적을 피했다.", "consciously avoid making marks or passages that resembled recognizable objects", "일치"]])]
PICK2 = [PK(p, 'The ancient Greeks felt', 'to copy', 'copy', "정답 ▶ to copy\n이유: be동사(was)의 보어 — '모방하는 것' to부정사"),
 PK(p, 'We must sadly note', 'due to', 'because', "정답 ▶ due to\n이유: 뒤에 명사구(the action of time and weather) → 전치사구 due to (because는 절)"),
 PK(p, 'We can only surmise', 'that survive', 'which survives', "정답 ▶ that survive\n이유: 선행사 drawings(복수) → 관계절 동사도 복수 survive"),
 PK(p, 'While painting these works', 'making', 'to make', "정답 ▶ making\n이유: avoid + 동명사"),
 PK(p, 'While painting these works', 'resembled', 'resembled to', "정답 ▶ resembled\n이유: resemble은 타동사 — 전치사 없이 목적어"),
 PK(p, 'They succeeded', 'demonstrating', 'demonstrated', "정답 ▶ demonstrating\n이유: thus + 분사구문(그리하여 ~을 보여 주면서)")]
VERB = [VB(p, 'They succeeded', 'making', 'make', "정답 ▶ making\n이유: succeed at(in) + 동명사"),
 VB(p, 'Jackson Pollock', 'existing', 'exist', "정답 ▶ existing\n이유: '존재하는' 사물 → objects를 꾸미는 현재분사"),
 VB(p, 'We can only surmise', 'based', 'base', "정답 ▶ based\n이유: based on ~ (~을 바탕으로) — 과거분사 관용 표현")]
ERR = [ER(p, 'While painting these works', ['painting', ('making', 'to make'), 'that'], 1, 'making', "틀린 곳 ▶ ② to make → making\n이유: avoid는 동명사를 목적어로\n나머지 ▶ ① 접속사 While + 분사 ✔ ③ 주격 관계대명사 that ✔"),
 ER(p, 'They succeeded', [('making', 'make'), 'did not copy', 'demonstrating'], 0, 'making', "틀린 곳 ▶ ① make → making\n이유: 전치사 at 뒤 동명사\n나머지 ▶ ② 관계절 동사 ✔ ③ 분사구문 ✔")]
SCR = [0, 1, 4, 5, 7]
ORDER = [[0, 1, 2, 3], [4, 5, 6, 7]]
INSERT = [([3, 4, 5, 6], 1, "정답 ▶ ② (This definition ~ has a problem, though.)\n이유: 그리스 예술의 질은 짐작만 가능(그리스 이야기 끝) → 하지만(though) 이 정의에는 문제가 있다 → 그 반례: Pollock. 흐름이 '소개 → 문제 제기'로 바뀌는 곳")]
ODD = [([0, 1, "Greek food is famous for its use of olive oil and fresh vegetables.", 2], 2, "정답 ▶ ③\n이유: 그리스인의 예술관(모방)과 남아 있는 작품 이야기예요. 그리스 음식 이야기는 관계없어요.")]
BLANK = [BL(p, 'This definition of art', 'a problem', ["no limit", "a reward", "a history"], "정답 ▶ a problem (문제)\n이유: though(하지만) + 뒤에 Pollock이라는 반례 → 정의에 '문제'가 있음\n오답 ▶ 한계 없음 · 보상 · 역사"),
 BL(p, 'They succeeded', 'did not copy anything', ["copied nature", "copied Greek art", "sold well"], "정답 ▶ did not copy anything (아무것도 모방하지 않은)\n이유: 앞 문장 — 알아볼 수 있는 사물을 닮은 흔적을 의식적으로 피함\n오답 ▶ 자연을 모방한 · 그리스 예술을 모방한 · 잘 팔린")]
GRAM = [{'q': "빈칸에 알맞은 것은?<br><b>Pollock would consciously avoid ______ marks that resembled objects.</b>", 'opts': ["making", "to make", "make", "made"], 'ex': "정답 ▶ making\n이유: avoid + 동명사"},
 {'q': "빈칸에 알맞은 것은?<br><b>No paintings exist today ______ the action of time and weather.</b>", 'opts': ["due to", "because", "although", "so that"], 'ex': "정답 ▶ due to\n이유: 뒤에 명사구 → 전치사"},
 {'q': "빈칸에 알맞은 것은?<br><b>They succeeded at making artwork, thus ______ that the Greek view was limited.</b>", 'opts': ["demonstrating", "demonstrate", "demonstrated", "to demonstrated"], 'ex': "정답 ▶ demonstrating\n이유: thus + 분사구문"}]
SUMQ = [SUM(p, "The Greek idea that art means (A) ______ reality is not enough, as Pollock created artwork that (B) ______ nothing.", [
 "(A) copying – (B) copied", "(A) copying – (B) ignored", "(A) changing – (B) copied", "(A) selling – (B) explained", "(A) avoiding – (B) praised"],
 "정답 ▶ (A) copying – (B) copied\n(A) art as copying reality → copying\n(B) artwork that did not copy anything → copied nothing\n오답 ▶ ignored nothing(아무것도 무시하지 않음 — 뜻이 거꾸로) · changing 바꾸기 · selling 팔기",
 ["This definition of art as copying reality", "did not copy anything"])]
