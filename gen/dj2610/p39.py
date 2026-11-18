from jfw import *
R = PREP['39']['sents']; G = PREP['39']['given']
S = R[:6] + [G] + R[6:]
p = load(39, '39번 · 문장 삽입', sents=S)
VOCAB = words(39)
EXAM = [EXQ(39, '39. 글의 흐름으로 보아, 주어진 문장이 들어가기에 가장 적절한 곳은?', p.insert_q(6, [2, 3, 4, 5, 7]), SLOT, 4,
 "정답 ▶ ⑤\n이유: 사회사학자들도 엘리트(관료·고용주)가 만든 텍스트를 분석한다 → 주어진 문장: Yet 그것을 액면 그대로 받아들이지 않고 '결을 거슬러' 읽는다 → So, for example 노예 소유주의 법적 문서에서 공백·소문 등 노예의 힌트를 찾는다\n오답 ▶ ①~④ 기록의 편향(엘리트가 아닌 사람들의 기록 부족)을 설명하는 중 — such sources가 가리킬 '엘리트가 만든 자료'가 아직 안 나옴\n포인트 ▶ such sources = textual sources produced by ~ elites / Yet = 다른 역사학자들과의 차이", v=False),
 EXQ(39, '다음 글의 주제로 가장 적절한 것은?', p.full(), [
 "how social historians creatively read elite sources to study ordinary people", "why elites wrote more history books than ordinary people", "the importance of preserving archives for researchers",
 "how slaves recorded their own history", "the differences between legal and historical documents"], 0,
 "정답 ▶ ① 사회사학자들이 평범한 사람들을 연구하기 위해 엘리트의 자료를 창의적으로 읽는 방법\n이유: 평범한 사람들은 기록을 거의 남기지 못함(편향) → 창의적이어야 함 → 엘리트 자료를 결을 거슬러 읽음(예: 법적 문서의 공백·소문)\n오답 ▶ ② 엘리트가 역사책을 더 썼다는 이유 아님 ③ 보관소 보존 중요성 아님 ④ 노예가 직접 기록했다는 말 없음 ⑤ 문서 종류 비교 아님\n포인트 ▶ biases in the historical record → creative"),
 EXQ(39, '다음 빈칸에 들어갈 말로 가장 적절한 것은?', p.blank('creative'), [
 "creative", "careless", "traditional", "obedient", "silent"], 0,
 "정답 ▶ ① creative (창의적인)\n이유: 기록의 편향 → 평범한 사람에 대한 자료가 부족 → '창의적'이어야 함 → 엘리트 자료를 결을 거슬러 읽기\n오답 ▶ ② 부주의한 ③ 전통적인 — 액면 그대로 읽는 쪽 ④ 순종적인 ⑤ 침묵하는\n포인트 ▶ Because of such biases ~ = 원인 → 결과")]
PICK1 = [PK(p, 'Like all historians', 'variety', 'lack', "정답 ▶ variety (다양함)\n오답 ▶ lack (부족)\n이유: 모든 역사학자처럼 '다양한' 원자료를 가져다 씀"),
 PK(p, 'Social history often', 'ordinary', 'royal', "정답 ▶ ordinary (평범한)\n오답 ▶ royal (왕실의)\n이유: 엘리트보다 '평범한' 사람들을 강조 — rather than elites"),
 PK(p, 'Yet, in most places', 'lacked', 'enjoyed', "정답 ▶ lacked (부족했다)\n오답 ▶ enjoyed (누렸다)\n이유: 교육 기회가 '부족'해서 → 기록을 많이 만들지 못함(thus)"),
 PK(p, 'Even when they did', 'rarely', 'usually', "정답 ▶ rarely (거의 ~않게)\n오답 ▶ usually (대개)\n이유: 기록을 만들어도 보관소에 '거의' 남지 못함 → 기록의 편향"),
 PK(p, 'Because of such biases', 'biases', 'balances', "정답 ▶ biases (편향)\n오답 ▶ balances (균형)\n이유: 엘리트 기록은 많고 평범한 사람 기록은 적음 → 역사 기록의 '편향'"),
 PK(p, 'Because of such biases', 'creative', 'careless', "정답 ▶ creative (창의적인)\n오답 ▶ careless (부주의한)\n이유: 평범한 사람의 기록이 부족한 편향 → 엘리트 자료를 결을 거슬러 읽는 등 '창의적'이어야 함")]
TF = [TF(p, "Social historians use a variety of primary sources.", True, "draw from a variety of primary sources", "정답 ▶ T\n이유: 다양한 원자료를 가져다 써요."),
 TF(p, "Social history mainly focuses on elites.", False, "emphasizes ordinary people rather than elites", "정답 ▶ F\n이유: 엘리트보다 평범한 사람들을 강조해요."),
 TF(p, "Non-elites often had little access to education.", True, "non-elites lacked access to education", "정답 ▶ T\n이유: 교육 접근 기회가 부족했어요."),
 TF(p, "Documents made by non-elites were usually preserved in archives.", False, "these materials rarely ended up in archives", "정답 ▶ F\n이유: 보관소에 거의 남지 못했어요."),
 TF(p, "Social historians accept sources by elites exactly as they are.", False, "rather than simply take such sources at face value", "정답 ▶ F\n이유: 액면 그대로 받아들이지 않고 결을 거슬러 읽어요.\n어휘 ▶ at face value = 액면 그대로"),
 TF(p, "Rumors in legal documents can give hints about enslaved people.", True, "rumors, and other details that offer hints about the enslaved peoples’ attitudes", "정답 ▶ T\n이유: 공백·소문 등이 노예가 된 사람들에 대한 힌트를 줘요.")]
MC = [MC(p, "글의 내용과 일치하지 <u>않는</u> 것은?", [
 "Non-elites produced large amounts of documentation.", "Social historians analyze texts by government officials.", "Historical records are biased toward elites.",
 "Social historians must be creative in their work.", "Legal documents can reveal something about enslaved people."],
 "정답 ▶ Non-elites produced large amounts of documentation.\n이유: did not produce substantial amounts of documentation (상당한 양의 기록을 만들지 못함)\n포인트 ▶ substantial = large · biased = 편향된",
 [["엘리트가 아닌 사람들은 많은 양의 기록을 남겼다.", "did not produce substantial amounts of documentation", "✗ 못 남김"], ["사회사학자는 정부 관료의 텍스트를 분석한다.", "textual sources produced by government officials", "일치"], ["역사 기록은 엘리트 쪽으로 편향되어 있다.", "such biases in the historical record", "일치"], ["사회사학자는 작업에서 창의적이어야 한다.", "have to be very creative", "일치"], ["법적 문서는 노예가 된 사람들에 대해 무언가를 보여 줄 수 있다.", "offer hints about the enslaved peoples’ attitudes", "일치"]]),
 MC(p, "글의 내용과 <u>일치하는</u> 것은?", ["사회사학자는 법적 문서의 공백까지 조사한다.", "사회사는 엘리트의 삶을 주로 다룬다.", "평범한 사람들의 기록은 대부분 보관소에 남아 있다.", "사회사학자는 엘리트의 자료를 사용하지 않는다.", "노예 소유주의 '사실'만 그대로 받아들인다."],
 "정답 ▶ 사회사학자는 법적 문서의 공백까지 조사한다.\n이유: she will also examine the silences, interruptions, rumors\n오답 ▶ ② 평범한 사람 ③ 거의 남지 못함 ④ 분석함 ⑤ 결을 거슬러 읽음",
 [["", "examine the silences", "일치 ✔"], ["", "emphasizes ordinary people", "평범"], ["", "rarely ended up in archives", "거의 없음"], ["", "analyze textual sources produced by", "사용"], ["", "not only for the “facts”", "그 이상"]])]
PICK2 = [PK(p, 'Yet, in most places', 'did not produce', 'did not produced', "정답 ▶ did not produce\n이유: did not + 동사원형"),
 PK(p, 'Even when they did', 'did produce', 'did produced', "정답 ▶ did produce\n이유: 강조의 did + 동사원형 (정말로 생산했다)"),
 PK(p, 'Even when they did', 'where', 'which', "정답 ▶ where\n이유: 선행사 archives(장소) + 뒤가 완전한 절 → 관계부사 where"),
 PK(p, 'Even when they did', 'preserved', 'preserving', "정답 ▶ preserved\n이유: 자료가 '보존되는' 수동 → could be preserved"),
 PK(p, 'Like other historians', 'produced', 'producing', "정답 ▶ produced\n이유: textual sources를 꾸미는 과거분사 — 관료들에 '의해(by) 생산된'"),
 PK(p, 'So, for example', 'provided', 'providing', "정답 ▶ provided\n이유: the “facts”를 꾸미는 과거분사 — 노예 소유주에 '의해 제공된'")]
VERB = [VB(p, 'Social history often', 'emphasizes', 'emphasize', "정답 ▶ emphasizes\n이유: 주어 Social history(단수), 현재시제"),
 VB(p, 'Even when they did', 'ended', 'end', "정답 ▶ ended\n이유: 과거 사실 → 과거시제 (end up in ~)"),
 VB(p, 'Because of such biases', 'to be', 'be', "정답 ▶ to be\n이유: have to + 동사원형 → have to be"),
 VB(p, 'So, for example', 'enslaved', 'enslave', "정답 ▶ enslaved\n이유: '노예가 된' 사람들 → 과거분사(수동)")]
VERB = [v for v in VERB if v['v'] != v['a'][0]]
ERR = [ER(p, 'Even when they did', ['did produce', ('where', 'which'), 'made'], 1, 'where', "틀린 곳 ▶ ② which → where\n이유: 선행사 archives(장소), 뒤가 완전한 수동태 절(they could be preserved) → 관계부사 where\n나머지 ▶ ① 강조 did + 동사원형 ✔ ③ could be preserved and (be) made 병렬 ✔"),
 ER(p, 'Like other historians', ['Like', 'analyze', ('produced', 'producing')], 2, 'produced', "틀린 곳 ▶ ③ producing → produced\n이유: 자료가 관료들에 '의해(by)' 생산된 수동 → 과거분사\n나머지 ▶ ① 전치사 Like(~처럼) ✔ ② 주어 social historians(복수) → analyze ✔"),
 ER(p, 'Yet, in most places', ['lacked', 'thus', ('produce', 'producing')], 2, 'produce', "틀린 곳 ▶ ③ producing → produce\n이유: did not + 동사원형\n나머지 ▶ ① 과거시제 lacked ✔ ② 부사 thus(따라서) ✔")]
SCR = [0, 2, 4, 5, 6]
ORDER = [[0, 1, 2, 3], [4, 5, 6, 7]]
INSERT = [([1, 2, 3, 4], 2, "정답 ▶ ② (Even when they did produce ~ 문장)\n이유: 엘리트 아닌 사람들은 기록을 거의 못 남김 → '설령 남겼어도' 보관소에 거의 남지 못함 → 그러한 편향(such biases)"),
 ([5, 6, 7], 1, "정답 ▶ ① (Yet rather than simply take ~ 문장)\n이유: 엘리트가 만든 자료를 분석 → Yet 결을 거슬러 읽음 → So, for example 법적 문서의 공백 (원문항 ⑤번)")]
ODD = [([1, 2, "Many universities now offer online courses in history.", 3], 2, "정답 ▶ ③\n이유: 평범한 사람들의 기록이 부족해 사회사학자가 창의적이어야 한다는 흐름이에요. 온라인 강좌 이야기는 관계없어요.")]
BLANK = [BL(p, 'Yet, in most places', 'education', ["entertainment", "transportation", "medicine"], "정답 ▶ education (교육)\n이유: '교육' 기회가 없어서 → 글(기록)을 남기지 못함\n오답 ▶ entertainment · transportation · medicine"),
 BL(p, 'Even when they did', 'archives', ["markets", "kitchens", "theaters"], "정답 ▶ archives (기록 보관소)\n이유: 보존되고 연구자들이 이용할 수 있는 곳 = '기록 보관소'\n오답 ▶ markets · kitchens · theaters"),
 BL(p, 'Yet rather than simply', 'at face value', ["with suspicion", "in detail", "against the grain"], "정답 ▶ at face value (액면 그대로)\n이유: rather than(~하기보다) 뒤 → 결을 거슬러 읽기(against the grain)와 '반대'되는 읽기\n오답 ▶ with suspicion 의심하며 · in detail 자세히 · against the grain — 모두 사회사학자가 실제로 '하는' 방식 쪽")]
GRAM = [{'q': "빈칸에 알맞은 것은?<br><b>Even when they ______ produce records, few survived.</b>", 'opts': ["did", "were", "had", "do"], 'ex': "정답 ▶ did\n이유: 강조의 did + 동사원형 (과거)"},
 {'q': "빈칸에 알맞은 것은?<br><b>Records rarely ended up in archives ______ they could be preserved.</b>", 'opts': ["where", "which", "what", "who"], 'ex': "정답 ▶ where\n이유: 장소 선행사 + 완전한 절 → 관계부사 where"},
 {'q': "빈칸에 알맞은 것은?<br><b>They analyze textual sources ______ by elites.</b>", 'opts': ["produced", "producing", "produce", "to producing"], 'ex': "정답 ▶ produced\n이유: 명사를 꾸미는 과거분사(수동, by + 행위자)"},
 {'q': "빈칸에 알맞은 것은?<br><b>Rather than simply ______ such sources at face value, they read them differently.</b>", 'opts': ["take", "takes", "took", "taken"], 'ex': "정답 ▶ take\n이유: rather than 뒤 동사원형(원문) — 주절 동사 read와 비교되는 동작"}]
SUMQ = [SUM(p, "Because ordinary people left (A) ______ written records, social historians read elite sources (B) ______ to find hidden clues about them.", [
 "(A) few – (B) critically", "(A) few – (B) literally", "(A) many – (B) critically", "(A) secret – (B) quickly", "(A) official – (B) silently"],
 "정답 ▶ (A) few – (B) critically\n(A) did not produce substantial amounts of documentation (B) read them “against the grain”(액면 그대로가 아니라 비판적으로)\n오답 ▶ literally 문자 그대로 = at face value(반대) · many(반대)",
 ["did not produce substantial amounts of documentation", "against the grain"])]
