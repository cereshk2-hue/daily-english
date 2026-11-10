from jfw import *
S = PREP['35']['sents'][:]; assert S[4].startswith('Individuals'); S = S[:4] + S[5:]
p = load(35, '35번 · 무관한 문장', sents=S)
VOCAB = words(35)
f = ' '.join(Q['35']['foot'])
ORIG = box(raw(35) + '<br><small>' + f + '</small>')
EXAM = [EXQ(35, '35. 다음 글에서 전체 흐름과 관계 없는 문장은?', ORIG, ["①", "②", "③", "④", "⑤"], 2,
 "정답 ▶ ③ Individuals can help themselves recover from burnout by changing patterns that contribute to stress.\n이유: 2019년 WHO가 번아웃을 직업적 현상으로 인정 → 개인 수준의 해결책에만 의존하지 말고 구조적 개입(①) → 임상의가 근본 원인 해결에 협력(②) → 번아웃을 개인의 실패가 아닌 조직 문화의 구조적 문제로 이해(④) → 개인에게만 부담을 지우지 않게 됨(⑤). ③은 '개인이 스스로' 회복할 수 있다는 개인 수준 해결책 → 글의 흐름(구조적 접근)과 반대\n오답 ▶ ①② 구조적 개입·근본 원인 ④⑤ 구조적 문제로의 전환 — 모두 흐름 유지\n포인트 ▶ individual-level remedies(개인 수준 해결책)에 '의존하지 말자'는 글에서 개인 해결책을 권하는 문장이 무관한 문장", v=False),
 EXQ(35, '다음 글의 요지로 가장 적절한 것은?', p.full(), [
 "번아웃은 개인이 아닌 조직과 사회 구조의 문제로 접근해야 한다.", "번아웃은 개인의 회복 탄력성을 키워 극복해야 한다.", "WHO는 번아웃을 질병으로 공식 분류했다.",
 "임상의는 환자의 개인 습관만을 관리해야 한다.", "직장 정신 건강은 정책과 무관한 개인의 문제이다."], 0,
 "정답 ▶ ① 번아웃은 개인이 아닌 조직과 사회 구조의 문제로 접근해야 한다.\n이유: understanding it as a structural issue rooted in organizational culture ~ / systemic interventions and policy-level changes rather than placing the burden solely on individuals\n오답 ▶ ② 개인의 회복 탄력성 문제로 보는 것에서 '벗어남' ③ '직업적 현상(occupational phenomenon)'으로 인정 — 질병이라고 하지 않음 ④ 산업 보건·지도부와 협력 ⑤ 정책 수준의 변화 필요"),
 EXQ(35, '다음 빈칸에 들어갈 말로 가장 적절한 것은?', p.blank('structural issue'), ["structural issue", "personal failing", "medical mystery", "temporary mood", "genetic disease"], 0,
 "정답 ▶ ① structural issue (구조적 문제)\n이유: shift away from(~에서 벗어나) 개인적 실패 → toward(~로 향하는) 조직 문화·지도부 관행·사회 경제적 맥락에 뿌리를 둔 '구조적' 문제\n오답 ▶ ② 개인적 실패 — 벗어나는 쪽(반대) ③ 의학적 수수께끼 ④ 일시적 기분 ⑤ 유전병 — 근거 없음\n포인트 ▶ shift away from A toward B = A에서 B로의 전환")]
PICK1 = [PK(p, 'The recognition', 'occupational', 'recreational', "정답 ▶ occupational (직업의)\n오답 ▶ recreational (여가의)\n이유: 직장 정신 건강(workplace mental health) 담론 → '직업적' 현상"),
 PK(p, 'This designation', 'systemic', 'individual', "정답 ▶ systemic (시스템 차원의)\n오답 ▶ individual (개인의)\n이유: 관심이 '시스템 차원'의 예방으로 이동 → 글 전체가 구조적 접근"),
 PK(p, 'It invites', 'structural', 'personal', "정답 ▶ structural (구조적인)\n오답 ▶ personal (개인적인)\n이유: rather than individual-level remedies와 대조 → '구조적' 개입"),
 PK(p, 'In practice', 'root causes', 'minor symptoms', "정답 ▶ root causes (근본 원인)\n오답 ▶ minor symptoms (가벼운 증상)\n이유: 조직·지도부와 협력해서 '근본 원인'을 다룸"),
 PK(p, 'It signaled', 'away from', 'back to', "정답 ▶ away from (~에서 벗어나)\n오답 ▶ back to (~로 되돌아가)\n이유: 개인의 실패로 보는 관점에서 '벗어나' 구조적 문제로 향하는 전환"),
 PK(p, 'This reframing', 'essential', 'harmful', "정답 ▶ essential (필수적인)\n오답 ▶ harmful (해로운)\n이유: as(왜냐하면) 시스템 차원의 개입과 정책 변화의 문을 열어 주니까 '필수적'")]
TF = [TF(p, "The WHO recognized burnout as an occupational phenomenon in 2019.", True, "by the WHO in 2019", "정답 ▶ T\n이유: 2019년 WHO가 번아웃을 직업적 현상으로 인정했어요."),
 TF(p, "The designation shifted attention to systemic prevention.", True, "shifting attention to systemic prevention", "정답 ▶ T\n이유: 관심을 시스템 차원의 예방으로 이동시켰어요."),
 TF(p, "Employers are encouraged to rely only on individual-level remedies.", False, "rather than relying solely on individual-level remedies", "정답 ▶ F\n이유: 개인 수준 해결책에만 의존하기보다 구조적 개입을 채택하라고 해요."),
 TF(p, "Clinicians should work with occupational health and leadership.", True, "clinicians should collaborate with occupational health and leadership", "정답 ▶ T\n이유: 산업 보건 부서 및 지도부와 협력해야 해요.\n어휘 ▶ work with = collaborate with"),
 TF(p, "Burnout is now viewed mainly as a personal failing.", False, "a shift away from viewing burnout as a personal failing", "정답 ▶ F\n이유: 개인적 실패로 보는 관점에서 벗어났어요."),
 TF(p, "The new view places the burden only on individuals to cope.", False, "rather than placing the burden solely on individuals", "정답 ▶ F\n이유: 개인에게만 부담을 지우지 않아요.")]
MC = [MC(p, "글의 내용과 일치하지 <u>않는</u> 것은?", [
 "The new view sees burnout as a matter of individual resilience.", "The WHO’s recognition was an important moment.", "Structural interventions are encouraged.",
 "Organizational culture is related to burnout.", "Policy-level changes can help deal with burnout."],
 "정답 ▶ The new view sees burnout as a matter of individual resilience.\n이유: a shift away from viewing burnout as ~ a matter of individual resilience (그런 관점에서 '벗어남')\n포인트 ▶ resilience = 회복 탄력성 · encourage ≒ invite",
 [["새로운 관점은 번아웃을 개인의 회복 탄력성 문제로 본다.", "a shift away from viewing burnout as a personal failing or a matter of individual resilience", "✗ 벗어남"], ["WHO의 인정은 중요한 순간이었다.", "marked an important moment", "일치"], ["구조적 개입이 권장된다.", "invites employers to adopt structural interventions", "encourage ≒ invite"], ["조직 문화는 번아웃과 관련이 있다.", "rooted in organizational culture", "일치"], ["정책 수준의 변화가 번아웃 대처에 도움이 될 수 있다.", "policy-level changes", "일치"]])]
PICK2 = [PK(p, 'The recognition', 'marked', 'marking', "정답 ▶ marked\n이유: 주어 The recognition의 동사 자리 → 과거시제 marked (marking이면 동사가 없음)"),
 PK(p, 'This designation', 'shifting', 'shifts', "정답 ▶ shifting\n이유: 동사 reframes가 이미 있음 → 콤마 뒤 분사구문(결과) shifting"),
 PK(p, 'It invites', 'to adopt', 'adopt', "정답 ▶ to adopt\n이유: invite + 목적어 + to부정사 (~하도록 이끌다)"),
 PK(p, 'It invites', 'relying', 'relies', "정답 ▶ relying\n이유: rather than + 동명사 (rather than 뒤 문법 형태 — 여기서는 -ing)"),
 PK(p, 'In practice', 'to address', 'address', "정답 ▶ to address\n이유: 목적의 to부정사 (~을 다루기 위해)"),
 PK(p, 'It signaled', 'rooted', 'is rooted', "정답 ▶ rooted\n이유: a structural issue를 뒤에서 꾸미는 과거분사(뿌리를 둔). 동사를 또 쓰면 안 돼요."),
 PK(p, 'This reframing', 'placing', 'place', "정답 ▶ placing\n이유: rather than + 동명사")]
VERB = [VB(p, 'It signaled', 'viewing', 'view', "정답 ▶ viewing\n이유: 전치사 from 뒤 동명사"),
 VB(p, 'It signaled', 'understanding', 'understand', "정답 ▶ understanding\n이유: 전치사 toward 뒤 동명사"),
 VB(p, 'This reframing', 'to cope', 'cope', "정답 ▶ to cope\n이유: place the burden on A to do — A에게 ~할 부담을 지우다(to부정사)")]
ERR = [ER(p, 'The recognition', ['occupational', ('marked', 'marking'), 'on'], 1, 'marked', "틀린 곳 ▶ ② marking → marked\n이유: 문장의 동사가 필요 → marked\n나머지 ▶ ① 형용사 ✔ ③ discourse on ✔"),
 ER(p, 'It invites', [('to adopt', 'adopt'), 'rather than', 'solely'], 0, 'to adopt', "틀린 곳 ▶ ① adopt → to adopt\n이유: invite + 목적어 + to부정사\n나머지 ▶ ② ✔ ③ 부사 ✔"),
 ER(p, 'It signaled', ['viewing', ('personal', 'personally'), 'rooted'], 1, 'personal', "틀린 곳 ▶ ② personally → personal\n이유: 명사 failing을 꾸미는 형용사\n나머지 ▶ ① from + 동명사 ✔ ③ 과거분사 수식 ✔")]
SCR = [0, 1, 2, 3, 5]
ORDER = [[0, 1, 2, 3], [2, 3, 4, 5]]
INSERT = [([1, 2, 3, 4], 2, "정답 ▶ ② (In practice ~ 문장)\n이유: 고용주에게 구조적 개입을 권함 → In practice(실제로) 임상의가 조직과 협력해 근본 원인을 다룬다는 뜻 → It signaled a shift …"),
 ([3, 4, 5], 2, "정답 ▶ ② (This reframing ~ 문장)\n이유: 개인 문제 → 구조적 문제로의 전환(재구성) → This reframing(이 재구성)이 필수적인 이유")]
ODD = [([1, 2, "Individuals can help themselves recover from burnout by changing patterns that contribute to stress.", 3], 2, "정답 ▶ ③ (원문항 ③번 문장)\n이유: 개인 수준 해결책에만 의존하지 말고 구조적으로 접근하자는 흐름이에요. 개인이 스스로 회복할 수 있다는 문장은 흐름과 반대예요.")]
BLANK = [BL(p, 'It invites', 'individual-level', ["company-wide", "nation-wide", "policy-level"], "정답 ▶ individual-level (개인 수준의)\n이유: rather than(~보다는) — 구조적 개입과 대조되는 '개인 수준' 해결책\n오답 ▶ company-wide 회사 전체의 · nation-wide 전국적인 · policy-level 정책 수준의 → 모두 구조적인 쪽"),
 BL(p, 'In practice', 'collaborate', ["compete", "argue", "interfere"], "정답 ▶ collaborate (협력하다)\n이유: 산업 보건 부서·지도부와 '함께' 근본 원인을 다룸\n오답 ▶ compete 경쟁하다 · argue 논쟁하다 · interfere 간섭하다"),
 BL(p, 'This reframing', 'burden', ["reward", "freedom", "honor"], "정답 ▶ burden (부담)\n이유: 개인에게만 대처·적응의 '부담'을 지우지 않음\n오답 ▶ reward 보상 · freedom 자유 · honor 영예")]
GRAM = [{'q': "빈칸에 알맞은 것은?<br><b>It invites employers ______ structural interventions.</b>", 'opts': ["to adopt", "adopt", "adopting", "adopted"], 'ex': "정답 ▶ to adopt\n이유: invite + 목적어 + to부정사"},
 {'q': "빈칸에 알맞은 것은?<br><b>This designation reframes clinical assessment, ______ attention to systemic prevention.</b>", 'opts': ["shifting", "shifts", "shifted", "to shifts"], 'ex': "정답 ▶ shifting\n이유: 동사가 이미 있음 → 분사구문"},
 {'q': "빈칸에 알맞은 것은?<br><b>It is a structural issue ______ in organizational culture.</b>", 'opts': ["rooted", "is rooted", "rooting", "roots"], 'ex': "정답 ▶ rooted\n이유: issue를 꾸미는 과거분사(~에 뿌리를 둔)"},
 {'q': "빈칸에 알맞은 것은?<br><b>It opens the door to change rather than ______ the burden on individuals.</b>", 'opts': ["placing", "place", "placed", "places"], 'ex': "정답 ▶ placing\n이유: rather than + 동명사 (~하는 대신). 본문: rather than placing the burden solely on individuals"}]
SUMQ = [SUM(p, "Since the WHO recognized burnout as an occupational phenomenon, it has been seen less as a personal (A) ______ and more as a (B) ______ problem.", [
 "(A) failing – (B) structural", "(A) failing – (B) private", "(A) success – (B) structural", "(A) choice – (B) medical", "(A) talent – (B) temporary"],
 "정답 ▶ (A) failing – (B) structural\n(A) 개인적 실패(a personal failing)로 보는 관점에서 벗어남 → failing\n(B) 구조적 문제(a structural issue) → structural\n오답 ▶ private 사적인(반대) · success 성공",
 ["viewing burnout as a personal failing", "a structural issue"])]
