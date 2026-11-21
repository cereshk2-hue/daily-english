from jfw import *
R = PREP['35']['sents']; assert R[5].startswith('Regular pet check-ups')
S = [R[0] + ' ' + R[1], R[2], R[3], R[4], R[6]]
p = load(35, '35번 · 무관한 문장', sents=S)
VOCAB = words(35)
ORIG = box(raw(35) + '<br><small>' + ' '.join(Q['35']['foot']) + '</small>')
EXAM = [EXQ(35, '35. 다음 글에서 전체 흐름과 관계 없는 문장은?', ORIG, ["①", "②", "③", "④", "⑤"], 3,
 "정답 ▶ ④ (Regular pet check-ups can help identify health problems ~)\n이유: 글 전체 = 반려동물 돌봄의 기준은 '내가 원하는 것'이 아니라 '그들에게 실제로 필요한 것' → 그 예로 개 목욕 횟수(자주 씻기면 피부에 나쁨, 대부분 주기적 목욕 필요 없음) → ④ 정기 검진의 장점은 목욕 이야기에서 벗어남\n오답 ▶ ① 냄새 때문에 자주 씻기는 주인 ② 냄새가 걱정되면 물 없는 샴푸·빗질, 목욕은 주 1~2회까지 ③ 피부병이 아니면 정기 목욕 불필요 ⑤ 털이 두꺼운 개도 6~8주마다 — 모두 '목욕' 이야기\n포인트 ▶ 예시(For example)의 소재(목욕)에서 벗어난 문장 찾기", v=False),
 EXQ(35, '다음 글의 요지로 가장 적절한 것은?', p.full(), [
 "반려동물은 주인이 원하는 방식이 아니라 그들에게 필요한 방식으로 돌봐야 한다.", "개는 냄새를 없애기 위해 자주 목욕시켜야 한다.", "물 없는 샴푸는 개의 피부에 해롭다.",
 "털이 두꺼운 개일수록 더 자주 목욕시켜야 한다.", "수의사는 모든 개에게 약욕을 처방해야 한다."], 0,
 "정답 ▶ ①\n이유: 첫 문장(주제문) — 기준은 'What do I want?'가 아니라 'Is this what they actually need?'\n오답 ▶ ② 자주 씻기면 피부에 나쁨(반대) ③ 물 없는 샴푸는 권하는 방법 ④ 털이 두꺼워도 6~8주마다 ⑤ 피부병이 있을 때만"),
 EXQ(35, '다음 빈칸에 들어갈 말로 가장 적절한 것은?', p.blank('they are not good for a dog’s skin'), [
 "they are not good for a dog’s skin", "they make dogs smell better", "they are too expensive", "dogs enjoy them a lot", "they take too much time"], 0,
 "정답 ▶ ① 개의 피부에 좋지 않기 때문에\n이유: 수의 피부과 전문의(veterinary dermatologists)가 경고하는 이유 → 피부 건강\n오답 ▶ ② 냄새가 좋아진다(경고 이유가 아님) ③ 비싸다 ④ 개가 좋아한다 ⑤ 시간이 오래 걸린다")]
PICK1 = [PK(p, 'Our number one criterion', 'need', 'want', "정답 ▶ need (필요로 하다)\n오답 ▶ want (원하다)\n이유: rather than 'What do I want?'와 대비 → 그들이 실제로 '필요한' 것"),
 PK(p, 'For example, we have', 'avoid', 'enjoy', "정답 ▶ avoid (피하다)\n오답 ▶ enjoy (즐기다)\n이유: '개 냄새'를 피하고 싶어서 자주 씻김"),
 PK(p, 'For example, we have', 'warn against', 'recommend', "정답 ▶ warn against (~하지 말라고 경고하다)\n오답 ▶ recommend (권하다)\n이유: 개의 피부에 좋지 않으므로 → 경고"),
 PK(p, 'If someone is really concerned', 'down', 'up', "정답 ▶ down\n오답 ▶ up\n이유: keep ~ down to (~로 줄이다, 제한하다) — 기껏해야(at most) 주 1~2회"),
 PK(p, 'Unless they have', 'don’t need', 'need', "정답 ▶ don't need\n오답 ▶ need\n이유: 피부병이 없다면(Unless) → 정기 목욕이 필요 '없음'"),
 PK(p, 'Even dogs with thick', 'only', 'often', "정답 ▶ only\n오답 ▶ often\n이유: 털이 두꺼운 개조차도 6~8주마다 '만' — 자주 씻길 필요 없음")]
TF = [TF(p, "Our first question should be what our pets actually need.", True, "Is this what they actually need?", "정답 ▶ T\n이유: 첫 번째 기준은 '그들이 실제로 필요한 것인가'예요."),
 TF(p, "Veterinary dermatologists recommend bathing dogs several times a week.", False, "veterinary dermatologists warn against such practices", "정답 ▶ F\n이유: 그런 관행을 하지 말라고 경고해요."),
 TF(p, "Owners worried about their dog’s smell can use waterless shampoo.", True, "they can use waterless shampoo", "정답 ▶ T\n이유: 물 없는 샴푸를 쓰고 매일 빗질할 수 있어요."),
 TF(p, "Most dogs need regular baths even without a skin condition.", False, "most dogs don’t need to be bathed on a regular basis", "정답 ▶ F\n이유: 피부병이 없다면 대부분 정기 목욕이 필요 없어요."),
 TF(p, "Dogs with thick coats generally need baths every 6 to 8 weeks.", True, "only need baths every 6 to 8 weeks", "정답 ▶ T\n이유: 털이 두꺼운 개도 보통 6~8주마다예요.")]
MC = [MC(p, "글의 내용과 일치하지 <u>않는</u> 것은?", [
 "Bathing dogs often is good for their skin.", "Some owners bathe their dogs many times a week.", "Owners should limit baths to once or twice a week at most.",
 "A vet may prescribe medicated baths for a skin condition.", "Our needs should not be the first standard for pet care."],
 "정답 ▶ Bathing dogs often is good for their skin.\n이유: they are not good for a dog’s skin — 자주 씻기는 건 피부에 좋지 않아요.",
 [["개를 자주 목욕시키는 것은 피부에 좋다.", "they are not good for a dog’s skin", "✗ 반대"], ["어떤 주인들은 일주일에 여러 번 개를 씻긴다.", "bathe their dogs religiously multiple times a week", "일치"], ["목욕은 기껏해야 주 1~2회로 제한해야 한다.", "keep the baths down to once or twice a week at most", "일치"],
  ["수의사는 피부병에 약욕을 처방할 수 있다.", "a skin condition for which a vet has prescribed medicated baths", "일치"], ["우리의 바람이 반려동물 돌봄의 첫 기준이 되어서는 안 된다.", "rather than, “What do I want?”", "일치"]])]
PICK2 = [PK(p, 'Our number one criterion', 'what', 'that', "정답 ▶ what\n이유: is의 보어 + need의 목적어가 없음 → 선행사를 품은 what"),
 PK(p, 'For example, we have', 'who bathe', 'who bathes', "정답 ▶ who bathe\n이유: 선행사 many dog owners(복수) → 복수 동사"),
 PK(p, 'For example, we have', 'to avoid', 'avoiding', "정답 ▶ to avoid\n이유: want + to부정사"),
 PK(p, 'If someone is really concerned', 'thoroughly', 'thorough', "정답 ▶ thoroughly\n이유: 동사 brush를 꾸미는 부사"),
 PK(p, 'Unless they have', 'for which', 'which', "정답 ▶ for which\n이유: 뒤 절이 완전(a vet has prescribed medicated baths) → 전치사 + 관계대명사(prescribe A for B)"),
 PK(p, 'Unless they have', 'to be bathed', 'to bathe', "정답 ▶ to be bathed\n이유: 개가 '목욕되는'(수동) → need to be p.p.")]
VERB = [VB(p, 'Unless they have', 'prescribed', 'prescribe', "정답 ▶ prescribed\n이유: has + p.p. 현재완료"),
 VB(p, 'For example, we have', 'encountered', 'encounter', "정답 ▶ encountered\n이유: have + p.p. 현재완료(경험)"),
 VB(p, 'Our number one criterion', 'impacting', 'impact', "정답 ▶ impacting\n이유: is + -ing 현재진행")]
ERR = [ER(p, 'Unless they have', [('for which', 'which'), 'don’t need', 'to be bathed'], 0, 'for which', "틀린 곳 ▶ ① which → for which\n이유: 뒤 절이 완전 → 전치사 + 관계대명사 (prescribe medicated baths for a skin condition)\n나머지 ▶ ② 주어 most dogs(복수) ✔ ③ 수동 to be bathed ✔"),
 ER(p, 'If someone is really concerned', ['concerned', ('thoroughly', 'thorough'), 'keep'], 1, 'thoroughly', "틀린 곳 ▶ ② thorough → thoroughly\n이유: 동사 brush를 꾸미는 부사 자리\n나머지 ▶ ① be concerned about ✔ ③ can use ~ and brush ~ but keep — 조동사 can 뒤 동사원형 병렬 ✔")]
SCR = [0, 2, 3, 4]
ORDER = [[0, 1, 2, 3, 4]]
INSERT = [([1, 2, 3, 4], 2, "정답 ▶ ③ (Unless ~, most dogs don't need to be bathed ~)\n이유: 냄새가 걱정되면 목욕은 주 1~2회까지 → (그리고) 피부병이 없다면 대부분 정기 목욕이 필요 없다 → (심지어) 털이 두꺼운 개도 6~8주마다. 점점 '덜 씻겨도 된다'로 강해지는 흐름")]
ODD = [([0, 1, "Cats usually sleep for more than twelve hours a day.", 2], 2, "정답 ▶ ③\n이유: 개 목욕을 예로 '필요한 돌봄'을 설명하는 흐름이에요. 고양이 수면 시간은 관계없어요.")]
BLANK = [BL(p, 'For example, we have', 'the ‘doggy’ smell', ["the bath water", "the dog’s skin", "the vet’s advice"], "정답 ▶ the 'doggy' smell (개 냄새)\n이유: 다음 문장 If someone is really concerned about their dog's smell\n오답 ▶ 목욕물 · 개의 피부 · 수의사의 조언"),
 BL(p, 'Even dogs with thick', 'every 6 to 8 weeks', ["every day", "twice a day", "every other day"], "정답 ▶ every 6 to 8 weeks (6~8주마다)\n이유: Even(심지어) 털이 두꺼운 개도 only — 자주 씻길 필요가 없다는 흐름\n오답 ▶ 매일 · 하루 두 번 · 이틀마다 — 모두 자주 씻기는 쪽")]
GRAM = [{'q': "빈칸에 알맞은 것은?<br><b>Is this ______ they actually need?</b>", 'opts': ["what", "that", "which", "who"], 'ex': "정답 ▶ what\n이유: 보어 자리 + need의 목적어 없음"},
 {'q': "빈칸에 알맞은 것은?<br><b>Most dogs don't need ______ on a regular basis.</b>", 'opts': ["to be bathed", "to bathe", "bathed", "bathing them"], 'ex': "정답 ▶ to be bathed\n이유: 개가 목욕'되는' → 수동"},
 {'q': "빈칸에 알맞은 것은?<br><b>They have a skin condition ______ a vet has prescribed medicated baths.</b>", 'opts': ["for which", "which", "what", "who"], 'ex': "정답 ▶ for which\n이유: 완전한 절 앞 → 전치사 + 관계대명사"}]
SUMQ = [SUM(p, "When caring for pets, we should consider what they actually (A) ______ rather than what we want; for example, most dogs do not need (B) ______ baths.", [
 "(A) need – (B) frequent", "(A) need – (B) occasional", "(A) like – (B) frequent", "(A) cost – (B) warm", "(A) eat – (B) medicated"],
 "정답 ▶ (A) need – (B) frequent\n(A) Is this what they actually need? → need\n(B) 대부분 정기 목욕 불필요, 털이 두꺼워도 6~8주마다 → frequent(잦은)\n오답 ▶ occasional(가끔의) 목욕은 필요함 · like 좋아하다 · cost 비용이 들다 · medicated 약용의(피부병일 때만)",
 ["Is this what they actually need?", "most dogs don’t need to be bathed on a regular basis"])]
