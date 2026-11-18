from jfw import *
R = PREP['40']['sents'][:9]; R[8] = R[8].split(' 󰀻')[0].strip(); assert R[8].endswith('environment.')
K = PREP['40']['ko'][:9]
p = P(40, '40번 · 요약문', list(zip(R, K)), ' '.join(Q['40']['foot']))
SUMS = "A dolphin’s auditory cortex processes the different aspects of echolocation signals (A)______ in its distinct areas, thereby (B)______ the reduction of the cognitive load and the rapid responses to changes in its environment."
VOCAB = words(40)
EXAM = [EXQ(40, '40. 다음 글의 내용을 한 문장으로 요약하고자 한다. 빈칸 (A), (B)에 들어갈 말로 가장 적절한 것은?', p.full() + box('<b>↓</b><br>' + SUMS), [
 "(A) serially – (B) disrupting", "(A) independently – (B) preventing", "(A) randomly – (B) facilitating", "(A) simultaneously – (B) enabling", "(A) sequentially – (B) allowing"], 3,
 "정답 ▶ ④ (A) simultaneously – (B) enabling\n(A) 특화된 구역들이 타이밍·주파수·강도를 나눠 맡아 → 순차적이 아니라 '병렬로'(in parallel, rather than sequentially) = 동시에\n(B) 병렬 처리가 인지 부하를 줄이고 빠른 반응을 '가능하게 함'(allowing dolphins to react quickly)\n오답 ▶ ① serially·⑤ sequentially 순차적으로 — 본문이 부정한 방식 ② independently는 그럴듯하지만 preventing(막다)이 반대 ③ randomly 무작위로 — 구역마다 맡은 일이 정해져 있음\n포인트 ▶ in parallel = simultaneously ↔ sequentially = serially", v=False),
 EXQ(40, '다음 글의 주제로 가장 적절한 것은?', p.full(), [
 "how dolphins’ specialized brains process echolocation signals in parallel", "why dolphins hear better than all other animals", "how factories divide work among workers",
 "the dangers of noise pollution for dolphins", "why dolphins need more energy to hunt"], 0,
 "정답 ▶ ① 돌고래의 특화된 뇌가 반향 정위 신호를 병렬로 처리하는 방식\n이유: 특화된 청각 피질 → 구역마다 다른 측면 담당 → 병렬 처리 → 빠르고 효율적, 인지 부하 감소\n오답 ▶ ② 모든 동물보다 잘 듣는다는 말 없음 ③ 공장은 비유일 뿐 ④ 소음 공해 없음 ⑤ 더 '적은' 에너지\n포인트 ▶ 비유(assembly line)는 주제가 아니라 설명 도구"),
 EXQ(40, '다음 빈칸에 들어갈 말로 가장 적절한 것은?', p.blank('in parallel, rather than sequentially'), [
 "in parallel, rather than sequentially", "one by one, rather than together", "slowly, rather than quickly", "randomly, rather than in order", "alone, rather than with other areas"], 0,
 "정답 ▶ ① 순차적이 아니라 병렬로\n이유: 구역마다 타이밍·주파수·강도를 '나눠 동시에' 처리 → 조립 라인 비유 → 훨씬 빠르게\n오답 ▶ ② 하나씩(순차) ③ 느리게(반대) ④ 무작위(맡은 일이 정해짐) ⑤ 혼자서 — 여러 구역이 분담\n포인트 ▶ dividing the work among specialized areas")]
PICK1 = [PK(p, 'Dolphins’ brains have', 'less', 'more', "정답 ▶ less (더 적은)\n오답 ▶ more (더 많은)\n이유: 특화된 구역 → 더 빠르고 '더 적은' 에너지로 처리"),
 PK(p, 'The signals from', 'rapidly', 'slowly', "정답 ▶ rapidly (빠르게)\n오답 ▶ slowly (느리게)\n이유: 귀의 신호가 청각 피질로 '빠르게' 전달"),
 PK(p, 'However, unlike many', 'specialized', 'simple', "정답 ▶ specialized (특화된)\n오답 ▶ simple (단순한)\n이유: 다른 포유류와 '달리' 구역마다 역할이 나뉜 '특화된' 피질"),
 PK(p, 'Imagine a factory', 'different tasks', 'the same task', "정답 ▶ different tasks (서로 다른 과업들)\n오답 ▶ the same task (같은 과업)\n이유: 조립 라인 — 노동자마다 '다른' 일을 맡음(분업)"),
 PK(p, 'By dividing the work', 'efficiently', 'wastefully', "정답 ▶ efficiently (효율적으로)\n오답 ▶ wastefully (낭비적으로)\n이유: 일을 나누면 훨씬 빠르고 '효율적'"),
 PK(p, 'This parallel processing', 'reduces', 'increases', "정답 ▶ reduces (줄이다)\n오답 ▶ increases (늘리다)\n이유: 병렬 처리 → 인지 부하를 '줄여' 빠르게 반응")]
TF = [TF(p, "Dolphins’ brains process sound information with less energy.", True, "more quickly and with less energy", "정답 ▶ T\n이유: 더 빠르고 더 적은 에너지로 처리해요."),
 TF(p, "Dolphins have the same auditory cortex as most other mammals.", False, "unlike many other mammals, dolphins have a highly specialized auditory cortex", "정답 ▶ F\n이유: 다른 포유류와 달리 고도로 특화된 청각 피질을 가졌어요."),
 TF(p, "Some areas of the cortex analyze the timing of echoes.", True, "Some areas may be responsible for analyzing the timing of echoes", "정답 ▶ T\n이유: 일부 구역은 반사파의 타이밍을 분석해요."),
 TF(p, "Dolphins process echo information one piece at a time.", False, "in parallel, rather than sequentially", "정답 ▶ F\n이유: 순차적이 아니라 병렬로 처리해요.\n어휘 ▶ one piece at a time = sequentially"),
 TF(p, "The writer compares the dolphin’s brain to a factory assembly line.", True, "Imagine a factory assembly line", "정답 ▶ T\n이유: 공장 조립 라인에 비유해요."),
 TF(p, "Parallel processing makes dolphins react more slowly.", False, "allowing dolphins to react quickly", "정답 ▶ F\n이유: 빠르게 반응하게 해 줘요.")]
MC = [MC(p, "글의 내용과 일치하지 <u>않는</u> 것은?", [
 "All areas of the dolphin’s auditory cortex do the same job.", "Signals from the ears go quickly to the auditory cortex.", "Some areas focus on the frequency or intensity of sound.",
 "Dividing work makes processing faster.", "Parallel processing reduces the cognitive load."],
 "정답 ▶ All areas of the dolphin’s auditory cortex do the same job.\n이유: distinct areas dedicated to processing different aspects (구역마다 다른 측면 담당)\n포인트 ▶ distinct = 개별의, 뚜렷이 다른",
 [["돌고래 청각 피질의 모든 구역은 같은 일을 한다.", "distinct areas dedicated to processing different aspects", "✗ 다른 측면"], ["귀의 신호는 청각 피질로 빠르게 간다.", "rapidly transmitted to the auditory cortex", "일치"], ["일부 구역은 소리의 주파수나 강도에 집중한다.", "focus on the frequency content or the intensity", "일치"], ["일을 나누면 처리가 빨라진다.", "much faster and more efficiently", "일치"], ["병렬 처리는 인지 부하를 줄인다.", "reduces the cognitive load", "일치"]]),
 MC(p, "글의 내용과 <u>일치하는</u> 것은?", ["돌고래의 뇌는 반향 정위 전용 구역을 진화시켰다.", "청각 피질은 시각 정보를 처리한다.", "돌고래는 반사파 정보를 순차적으로 처리한다.", "병렬 처리는 인지 부하를 늘린다.", "조립 라인에서는 모든 노동자가 같은 일을 한다."],
 "정답 ▶ 돌고래의 뇌는 반향 정위 전용 구역을 진화시켰다.\n이유: Dolphins’ brains have evolved specialized areas dedicated to echolocation\n오답 ▶ ② 소리 처리 ③ 병렬 ④ 줄임 ⑤ 서로 다른 과업",
 [["", "have evolved specialized areas dedicated to echolocation", "일치 ✔"], ["", "responsible for processing sound", "소리"], ["", "rather than sequentially", "병렬"], ["", "reduces the cognitive load", "줄임"], ["", "different workers are responsible for different tasks", "다른 일"]])]
PICK2 = [PK(p, 'Dolphins’ brains have', 'allowing', 'allowed', "정답 ▶ allowing\n이유: 분사구문, 특화된 구역이 처리를 '가능하게 하는' 능동"),
 PK(p, 'The signals from', 'are rapidly transmitted', 'rapidly transmit', "정답 ▶ are rapidly transmitted\n이유: 신호가 '전달되는' 수동"),
 PK(p, 'The signals from', 'responsible for', 'responsible to', "정답 ▶ responsible for\n이유: be responsible for ~ (~을 담당하다)"),
 PK(p, 'Some areas may be', 'analyzing', 'analyze', "정답 ▶ analyzing\n이유: 전치사 for 뒤 동명사"),
 PK(p, 'Imagine a factory', 'where', 'which', "정답 ▶ where\n이유: 선행사 a factory assembly line(장소) + 완전한 절 → 관계부사 where"),
 PK(p, 'By dividing the work', 'dividing', 'divide', "정답 ▶ dividing\n이유: 전치사 By 뒤 동명사 (By -ing ~함으로써)")]
VERB = [VB(p, 'Dolphins’ brains have', 'evolved', 'evolve', "정답 ▶ evolved\n이유: have + p.p. 현재완료"),
 VB(p, 'This specialization allows', 'to process', 'process', "정답 ▶ to process\n이유: allow + 목적어 + to부정사"),
 VB(p, 'This parallel processing', 'associated', 'associate', "정답 ▶ associated\n이유: the cognitive load를 꾸미는 과거분사 — associated with ~ (~와 연관된)"),
 VB(p, 'This parallel processing', 'to react', 'react', "정답 ▶ to react\n이유: allowing + 목적어 + to부정사")]
VERB = [v for v in VERB if v['v'] != v['a'][0]]
ERR = [ER(p, 'This specialization allows', [('allows', 'allow'), 'to process', 'rather than'], 0, 'allows', "틀린 곳 ▶ ① allow → allows\n이유: 주어 This specialization(단수)\n나머지 ▶ ② allow + 목적어 + to V ✔ ③ A rather than B ✔"),
 ER(p, 'Imagine a factory', ['Imagine', ('where', 'which'), 'responsible'], 1, 'where', "틀린 곳 ▶ ② which → where\n이유: 장소 선행사 + 완전한 절(different workers are responsible ~) → 관계부사 where\n나머지 ▶ ① 명령문 동사원형 ✔ ③ be responsible for ✔"),
 ER(p, 'This parallel processing', ['reduces', ('associated', 'associating'), 'allowing'], 1, 'associated', "틀린 곳 ▶ ② associating → associated\n이유: 인지 부하가 반향 정위와 '연관된' 수동 → associated with\n나머지 ▶ ① 주어 This parallel processing → reduces ✔ ③ 능동 분사구문 ✔")]
SCR = [0, 3, 5, 7, 8]
ORDER = [[0, 1, 2, 3], [5, 6, 7, 8]]
INSERT = [([3, 4, 5, 6], 2, "정답 ▶ ② (This specialization ~ 문장)\n이유: 구역마다 타이밍·주파수 담당 → 이러한 특화(This specialization)가 병렬 처리 가능 → 조립 라인 비유"),
 ([6, 7, 8], 2, "정답 ▶ ② (This parallel processing ~ 문장)\n이유: 일을 나누면 빠르고 효율적 → 이 병렬 처리가 인지 부하를 줄임")]
ODD = [([4, 5, "Dolphins are known to sleep with one half of their brain at a time.", 6], 2, "정답 ▶ ③\n이유: 특화된 청각 피질의 병렬 처리가 흐름이에요. 돌고래의 수면 방식은 관계없어요.")]
BLANK = [BL(p, 'Dolphins’ brains have', 'acoustic', ["visual", "chemical", "magnetic"], "정답 ▶ acoustic (음향의)\n이유: 반향 정위 = 소리(초음파)로 위치 파악 → '음향' 정보\n오답 ▶ visual 시각의 · chemical 화학의 · magnetic 자기의"),
 BL(p, 'Some areas may be', 'frequency', ["color", "weight", "temperature"], "정답 ▶ frequency (주파수)\n이유: 소리의 성질: 타이밍, '주파수', 강도\n오답 ▶ color · weight · temperature"),
 BL(p, 'This parallel processing', 'cognitive load', ["body weight", "water pressure", "food supply"], "정답 ▶ cognitive load (인지 부하)\n이유: 뇌가 정보를 처리하는 '부담'이 줄어듦 → 빠른 반응\n오답 ▶ 체중 · 수압 · 식량 공급")]
GRAM = [{'q': "빈칸에 알맞은 것은?<br><b>The specialization allows the brain ______ information in parallel.</b>", 'opts': ["to process", "process", "processing", "processed"], 'ex': "정답 ▶ to process\n이유: allow + 목적어 + to부정사"},
 {'q': "빈칸에 알맞은 것은?<br><b>Imagine an assembly line, ______ workers do different tasks.</b>", 'opts': ["where", "which", "what", "that"], 'ex': "정답 ▶ where\n이유: 장소 선행사 + 완전한 절 → 관계부사 where (콤마 뒤 that 불가)"},
 {'q': "빈칸에 알맞은 것은?<br><b>______ the work among areas, the brain works faster.</b>", 'opts': ["By dividing", "By divide", "Divided", "To dividing"], 'ex': "정답 ▶ By dividing\n이유: By + 동명사 (~함으로써)"},
 {'q': "빈칸에 알맞은 것은?<br><b>It reduces the load ______ with echolocation.</b>", 'opts': ["associated", "associating", "associate", "associates"], 'ex': "정답 ▶ associated\n이유: 명사를 꾸미는 과거분사 associated with (~와 연관된)"}]
SUMQ = [SUM(p, "Because the dolphin’s auditory cortex has (A) ______ areas for different aspects of echoes, it can process them in parallel and respond to changes more (B) ______.", [
 "(A) specialized – (B) quickly", "(A) specialized – (B) slowly", "(A) identical – (B) quickly", "(A) damaged – (B) carefully", "(A) empty – (B) randomly"],
 "정답 ▶ (A) specialized – (B) quickly\n(A) a highly specialized auditory cortex with distinct areas (B) allowing dolphins to react quickly\n오답 ▶ slowly(반대) · identical 동일한: 구역마다 '다른' 일",
 ["a highly specialized auditory cortex", "allowing dolphins to react quickly"])]
