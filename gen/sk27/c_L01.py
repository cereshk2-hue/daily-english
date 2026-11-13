# 01강 글의 목적 파악 (26005-0001~0005)
A = {
1: dict(
 why="편지 앞부분은 배경이에요. 더 다양한 동아리를 원한다는 요청이 있었고, 학교가 동아리 수를 늘리기로 했다는 내용이에요. 목적은 Therefore 뒤에 나와요. I am encouraging you to submit a proposal for a new club(새 동아리 제안서를 내 달라)과 Please turn this in to my office(제 사무실로 내 주세요) → 동아리 개설 제안서 제출을 독려하는 글이에요.",
 wrong={1: "만족도 조사(survey)는 나오지 않아요.", 3: "체험 활동 '결과 보고서'가 아니라 새 동아리 '제안서'예요. (submit만 보고 고르면 함정)", 4: "기존 동아리의 신규 회원 모집이 아니라 새 동아리를 '만들라'는 내용이에요.", 5: "extracurricular activities(과외 활동)가 나오지만, 방과 후 프로그램을 설명하는 글은 아니에요."},
 point="목적 문제는 Therefore, I am encouraging you to ~ / Please ~ 처럼 요청·부탁이 나오는 문장이 답이에요. 앞부분은 배경이에요.",
 kt=["이것은 학생들에게 추가 동아리를 만들 기회를 제공한다.", "따라서 저는 여러분이 만들고 싶은 새로운 동아리에 대한 제안서를 제출하기를 권합니다."],
 voc=[("semester", "학기"), ("diverse", "다양한"), ("expand", "확대하다"), ("extracurricular activity", "과외 활동"), ("additional", "추가의"), ("submit", "제출하다"), ("proposal", "제안서"), ("turn in", "~을 제출하다")]),
2: dict(
 why="학교가 전 세계 가정의 전통 요리를 모은 요리책(a recipe book)을 만들었다고 소개해요. 이어서 We encourage you to try some of these recipes together(함께 만들어 보시길 권합니다)와 You can download this online recipe book from our school website(학교 웹사이트에서 내려받을 수 있습니다) → 학교에서 만든 온라인 요리책을 이용하라고 권하는 글이에요.",
 wrong={1: "해외 교류 프로그램은 나오지 않아요. 26개국은 요리법의 출처예요.", 2: "학생 요리 실습 '계획'이 아니라 가정에서 자녀와 함께 해 보라는 권장이에요.", 4: "학부모 설명회 개최는 나오지 않아요.", 5: "cultural diversity(문화적 다양성)는 소재일 뿐, 다문화 축제 참여를 부탁하는 글이 아니에요."},
 point="학부모에게 보내는 안내문은 '무엇을 하라고 권하는가'를 찾아요 → We encourage you to ~ / You can download ~.",
 kt=["우리는 전 세계 가정의 전통과 맛을 기념하기 위해 만들어진, 우리의 특별한 새 프로젝트인 요리책을 여러분과 공유하게 되어 매우 기쁩니다.", "그것은 세계의 요리를 탐험하고 자녀와 의미 있는 순간을 나눌 특별한 기회를 제공합니다."],
 voc=[("take pride in", "~에 자부심을 갖다"), ("cultural diversity", "문화적 다양성"), ("enrich", "풍요롭게 하다"), ("flavor", "맛, 풍미"), ("feature", "특징으로 하다, 담고 있다"), ("beloved", "사랑받는"), ("pass down", "(후대에) 전하다"), ("cuisine", "요리(법)"), ("unity", "화합, 통합"), ("continued", "지속적인")]),
3: dict(
 why="원고 수정 마감일(12월 27일)이 다가오니 검토자 의견을 반영해 달라는 편지예요. 결정적 문장은 Please review these comments carefully and submit a revised version of your manuscript(의견을 검토하고 수정본을 제출해 주세요) → 검토 의견에 따라 원고를 고쳐 내 달라는 요청이에요.",
 wrong={1: "게재되지 않은 이유를 설명하는 게 아니에요. 오히려 수정하면 게재되기를 바란다고 했어요.", 2: "편집이 늦어져서 사과하는 게 아니라, 휴가 중에 연락해서 사과했어요. (apologize 함정)", 3: "연휴에도 수정해 달라고 부탁하는 글이에요. 검토가 불가능하다는 말은 없어요.", 4: "원고를 '검토'해 달라는 게 아니라, 받은 검토 의견대로 '수정'해 달라는 거예요. 원고를 쓴 사람이 받는 편지예요."},
 point="처음의 사과(apologize)는 인사말일 뿐이에요. Please ~ / we kindly ask for ~ 문장이 목적이에요.",
 kt=["의견들을 신중히 검토하고 원고의 수정본을 제출해 주십시오.", "우리는 수정된 원고가 검토자들을 만족시키고 우리 학술지에 게재 승인되기를 바랍니다."],
 voc=[("manuscript", "원고"), ("revision", "수정"), ("deadline", "마감일"), ("cooperation", "협조"), ("address", "(문제 등을) 다루다, 처리하다"), ("thoroughly", "철저히"), ("evaluate", "평가하다"), ("insightful", "통찰력 있는"), ("revise", "수정하다"), ("incorporate", "포함시키다, 반영하다"), ("claim", "주장"), ("journal", "학술지")]),
4: dict(
 why="1년 전 결혼식 부케 실수는 '배경'이에요(그때는 항의하지 않았어요). 이번에 결혼 1주년으로 주문한 꽃이 도착했을 때 lifeless, spotted, and browning(생기 없고 얼룩지고 갈색으로 변함)이었어요. 그래서 I do expect a refund for this order / I would appreciate a full refund → 구매한 꽃의 환불을 요청하는 글이에요.",
 wrong={2: "배달이 '늦었다'는 말은 없어요. 꽃의 상태가 문제예요.", 3: "이미 주문해서 받은 꽃에 대한 불만이에요. 새로 주문하는 글이 아니에요.", 4: "결혼식장 꽃 장식을 문의하는 글이 아니에요.", 5: "만족이 아니라 불만이에요."},
 point="Before I get to my main point(본론에 앞서) 뒤의 과거 이야기는 배경이에요. main point는 마지막 요청(a full refund)이에요.",
 kt=["그러나 오늘 받은 꽃은 도착했을 때 생기가 없고, 얼룩이 있고, 갈색으로 변하고 있었습니다.", "이번에는 이 문제를 해결하기 위한 조치를 취해 달라고 요청하는 것이 정당하다고 생각합니다."],
 voc=[("to whom it may concern", "관계자분께"), ("bouquet", "꽃다발, 부케"), ("file a complaint", "불만을 제기하다"), ("anniversary", "기념일"), ("lifeless", "생기 없는"), ("spotted", "얼룩진"), ("upon arrival", "도착 시에"), ("resolve", "해결하다"), ("compensation", "보상"), ("refund", "환불")]),
5: dict(
 why="새 직장 안부는 인사말이에요. 목적은 We're writing to ask when we can expect repayment of the $1,500 loan(1,500달러 대출금을 언제 갚을지 묻습니다)이에요. You agreed to pay ~ by June(6월까지 갚기로 동의함)과 we do need to receive at least half(최소 절반은 꼭 받아야 함) → 차량 구매 대출금을 갚아야 한다는 것을 일깨우는 글이에요.",
 wrong={1: "자동차 구입은 이미 끝났어요(We were glad to help you with the purchase). 정보 제공이 아니에요.", 3: "자동차 판매원이 된 게 아니라 '새 일자리'로 출퇴근하려고 차를 샀어요.", 4: "할부 구입 절차를 안내하는 글이 아니에요.", 5: "글쓴이가 묻는 쪽(재무 고문)이에요. 지불 방법을 묻는 게 아니라 언제 갚을지 확인하는 거예요."},
 point="We're writing to ~ / I'm writing to ~ 뒤가 바로 목적이에요. 앞의 안부와 뒤의 덕담(차 마음에 들기를)은 꾸밈이에요.",
 kt=["우리는 귀하의 자동차 대출금 1,500달러의 상환을 언제 기대할 수 있는지 묻기 위해 글을 씁니다.", "만약 귀하가 1,500달러 전액을 한 번에 상환할 수 없다고 결정했다면, 우리는 이해합니다."],
 voc=[("settle into", "~에 자리 잡다, 적응하다"), ("enthusiastic", "열정적인"), ("tiresome", "지루한, 성가신"), ("all in all", "대체로"), ("repayment", "상환"), ("loan", "대출(금)"), ("transportation", "교통수단"), ("back and forth", "왔다 갔다"), ("at once", "한 번에"), ("financial advisor", "재무 고문")]),
}
