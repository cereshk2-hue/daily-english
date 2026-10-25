from ins import NOT, YES
G = '선택지는 본문 표현을 쉬운 말로 조금 바꿔 썼어요. 해설의 "바꿔 쓴 표현"을 꼭 확인하세요.'
A = lambda who, s: who + '에 관한 ' + s[3:]
Q = {
'm3-jihak-min-L7.js': (G, {
 1: [
  (['❶'], A('푸에블로', NOT),
   ["The walls of a pueblo are made of stone and wood.", "People climb a ladder to get into a pueblo.", "There is a secret opening on the top of the house.", "Pulling up the ladder can keep unwelcome visitors out.", "The roof of a pueblo is flat."],
   [["푸에블로의 벽은 돌과 나무로 만들어진다.", "The thick walls are made of earth, straw, and water", "불일치 → 흙, 지푸라기, 물"],
    ["사람들은 푸에블로에 들어가기 위해 사다리를 오른다.", "I would climb up a ladder to enter my house", "일치 (get into = enter)"],
    ["집 꼭대기에 비밀 구멍이 있다.", "There's a hidden opening on top of the house", "일치 (secret = hidden)"],
    ["사다리를 끌어 올리면 반갑지 않은 방문객을 막을 수 있다.", "I would pull the ladder up to stop them from entering", "일치 (keep ~ out = stop ~ from entering)"],
    ["푸에블로의 지붕은 평평하다.", "The house has a flat roof", "일치"]],
   "정답 근거: The thick walls are made of earth, straw, and water.\n· 바꿔 쓴 표현: get into = enter · secret = hidden · keep ~ out = stop ~ from entering\n· be made of : ~로 만들어지다 · straw : 지푸라기"),
  (['❷'], A('베니스', YES),
   ["The old Venetians moved there to protect themselves from invaders.", "Venice is made up of 18 large islands.", "A vaporetto is a kind of taxi on the road.", "It was easy to build houses on the swampy ground.", "Stone pillars support Venice today."],
   [["옛 베니스인들은 침략자로부터 자신을 지키려고 그곳으로 옮겨 갔다.", "to keep themselves safe from invaders", "일치 (protect A from B = keep A safe from B)"],
    ["베니스는 18개의 큰 섬으로 이루어져 있다.", "Venice has 118 small islands", "불일치 → 118개의 작은 섬"],
    ["바포레토는 도로 위의 택시의 일종이다.", "a vaporetto, a water bus", "불일치 → 수상 버스"],
    ["늪지에 집을 짓는 것은 쉬웠다.", "it was not easy for them to build their homes", "불일치 → 쉽지 않았음"],
    ["오늘날 돌기둥이 베니스를 받치고 있다.", "It is these wooden poles that support Venice", "불일치 → 나무 기둥"]],
   "정답 근거: The old Venetians decided to live there to keep themselves safe from invaders.\n· 바꿔 쓴 표현: protect A from B = keep A safe from B · be made up of : ~로 이루어지다 · pillar ≒ pole : 기둥\n· invader : 침략자 · swampy : 늪지의 · install : 설치하다"),
 ],
 2: [
  (['❸'], A('토루', NOT),
   ["People sleep on the first floor of a tulou.", "A tulou is a huge round house.", "A tulou usually has three to five floors.", "Food and tools are kept on the second floor.", "Most people in a tulou share the same family name."],
   [["사람들은 토루의 1층에서 잔다.", ["The first floor is used for cooking and eating", "My bedroom would be on the third or fourth floor"], "불일치 → 1층은 요리·식사, 침실은 3·4층"],
    ["토루는 거대하고 둥근 집이다.", "a huge round house", "일치"],
    ["토루는 보통 3~5층이다.", "there are usually three to five floors", "일치"],
    ["식량과 도구는 2층에 보관된다.", "people store food and tools on the second floor", "일치 (keep = store)"],
    ["토루 사람들 대부분은 성(姓)이 같다.", "mostly have the same family name", "일치 (share = have the same)"]],
   "정답 근거: The first floor is used for cooking and eating. / My bedroom would be on the third or fourth floor.\n· 바꿔 쓴 표현: keep = store · share the same = have the same\n· store : 보관하다 · house : 수용하다(동사)"),
  (['❸'], A('토루', YES),
   ["Some big tulou have room for as many as 50 families.", "People in a tulou rarely meet their neighbors.", "Families in a tulou work separately.", "Living in one building is dangerous for them.", "Homes are the same all over the world."],
   [["어떤 큰 토루는 50가구까지 들어갈 공간이 있다.", "Some large tulou can house up to 50 families", "일치 (have room for = house · as many as = up to)"],
    ["토루 사람들은 이웃을 거의 만나지 않는다.", "I would sometimes hear my neighbor calling me to come over", "불일치 → 이웃이 놀러 오라고 부름"],
    ["토루의 가족들은 따로 일한다.", "They work together and share many things", "불일치 → 함께 일함"],
    ["한 건물에 사는 것은 그들에게 위험하다.", "Living together in one building keeps them safe", "불일치 → 안전하게 지켜 줌"],
    ["집은 전 세계 어디나 똑같다.", "But they are different all over the world", "불일치 → 서로 다름"]],
   "정답 근거: Some large tulou can house up to 50 families.\n· 바꿔 쓴 표현: have room for = house (수용하다) · as many as = up to (최대 ~까지)\n· rarely : 거의 ~않다 · separately : 따로"),
 ]}),
}
