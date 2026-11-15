# 11/15 중2 동아(윤정미) 대화문 DAY(6과 k6a·k6b, 7과 k7a·k7b)에 '문장삽입' 단계 추가 (문장순서 바로 뒤)
# gen_m2d6dlg.py 를 다시 돌리면 이 스크립트도 다시 돌릴 것 (k6a/k6b 덮어씀). 여러 번 돌려도 같은 결과.
import sys, json, subprocess
sys.path.insert(0, '/tmp/claude-0/-home-claude/a9e3e882-1f02-5d62-8f70-aced81bc59d2/scratchpad')
from gencommon import write
path = sys.argv[1] if len(sys.argv) > 1 else '/home/claude/proj/data/m2-donga-yoon-L7.js'
PK = json.loads(subprocess.check_output(['node', '-e', "global.window={};require('%s');process.stdout.write(JSON.stringify(window.PKG))" % path]))
G = '주어진 문장(대화)이 들어가기에 가장 알맞은 곳을 고르세요. 앞뒤 말의 연결(질문 ↔ 대답, Then, Why? 등)을 확인해요.'

def blocks(d):
    out, cur = [], None
    for r in d['passage']:
        if r[0] == '#': cur = []; out.append(cur)
        else: cur.append(r[1])
    return out

SPEC = {
 'k6a': [(0, 0, 4, 2, "정답 ▶ ②\n이유: '나는 보통 공상 과학 소설을 읽어' → Then(그럼) 좋은 공상 과학 소설 하나 추천해 줄래? → How about The Time Machine?(추천)\n포인트 ▶ Then은 앞사람의 대답을 받고, 추천 요청 뒤에는 추천하는 말이 와요."),
         (1, 0, 4, 2, "정답 ▶ ②\n이유: 새 탄산음료를 추천해 줄래? → 체리 소다를 마셔 봐(Try ~) → 알았어, 한번 마셔 볼게(give it a try).\n포인트 ▶ it(=a cherry soda)이 가리키는 말이 앞에 있어야 해요."),
         (2, 0, 4, 2, "정답 ▶ ②\n이유: 스파이더맨이 가장 좋아하는 영화야 → 오, 나는 그거 안 봤어 → 안 봤다고?(You didn't?) 강력히 추천해.\n포인트 ▶ You didn't?는 바로 앞의 I didn't see it.에 대한 반응"),
         (3, 0, 4, 1, "정답 ▶ ①\n이유: 어떤 종류의 잡지가 있니? → 모든 종류의 잡지가 있어 → 나는 과학에 관심이 있어, 과학 잡지 추천해 줄래?\n포인트 ▶ What kinds of ~?(종류 묻기) 바로 뒤에 종류를 답하는 말")],
 'k6b': [(0, 0, 4, 1, "정답 ▶ ①\n이유: 숙제용 책을 찾아야 해 → 어떤 종류의 책을 찾고 있니? → 다른 사람을 도운 유명인에 관한 책을 찾고 있어.\n포인트 ▶ 질문(What kinds of books ~?) → 대답(I'm looking for books on ~)"),
         (0, 2, 6, 1, "정답 ▶ ①\n이유: 에세이를 써야 해 → 누구에 대해 쓰고 싶니? → Schweitzer 박사를 생각하고 있었는데, 다른 사람을 추천해 줄래?\n포인트 ▶ Who ~?에 대한 대답으로 사람(Dr. Schweitzer)이 나와요."),
         (0, 4, 8, 2, "정답 ▶ ②\n이유: Audrey Hepburn은 어때? → 유명한 배우인 건 알지만, 다른 사람을 돕기 위해 무엇을 했어? → 아이들을 위해 자원봉사를 많이 했어.\n포인트 ▶ she가 가리키는 Audrey Hepburn이 앞에, '무엇을 했는지'에 대한 대답이 뒤에"),
         (1, 1, 6, 3, "정답 ▶ ③\n이유: 음악에 대한 사랑을 잃은 피아니스트 → 새 출발을 위해 작은 마을로 이사 → There(그곳에서) 아이들을 가르치며 사랑을 되찾음.\n포인트 ▶ There는 앞의 a small town을 가리켜요.")],
 'k7a': [(0, 0, 4, 1, "정답 ▶ ①\n이유: 어느 것이 더 좋아? → 페이스 페인팅이 더 좋아. 너는 어때? → 나는 VR 게임을 하고 싶어.\n포인트 ▶ Which ~?(선호 묻기) 바로 뒤에 선호 답하기, What about you?에 대한 대답이 뒤에"),
         (1, 0, 4, 2, "정답 ▶ ②\n이유: 떡볶이가 훨씬 좋아, 매운 음식을 좋아해 → Then(그럼) 떡볶이를 주문하자 → 좋아, 너무 배고파!\n포인트 ▶ Then은 앞사람의 선호를 받아 제안하는 말"),
         (2, 0, 5, 3, "정답 ▶ ③\n이유: 티셔츠가 더 좋아 → 왜?(Why?) → 축제 그림이 있거든.\n포인트 ▶ 이유를 말하는 문장 바로 앞에 이유를 묻는 말"),
         (3, 0, 5, 3, "정답 ▶ ③\n이유: 노란 꽃이 더 좋아 → 왜 그것들이 더 좋니? → 노란색이 가장 좋아하는 색이거든.\n포인트 ▶ them = the yellow flowers")],
 'k7b': [(0, 0, 5, 3, "정답 ▶ ③\n이유: 중국, 이탈리아, 미국이 참가한대 → 한국을 잊지 마(Don't forget Korea) → 물론, 한국도.\n포인트 ▶ Of course, Korea, too.는 앞의 '한국을 잊지 마'에 대한 대답"),
         (0, 5, 9, 2, "정답 ▶ ②\n이유: 자전거를 타거나 보트를 탈 수 있어, 어느 것이 더 좋아? → 보트 타기, 더 재미있을 것 같아 → 그럼 보트 타러 가자.\n포인트 ▶ Which ~? 질문 바로 뒤에 하나를 고르는 대답"),
         (1, 2, 6, 1, "정답 ▶ ①\n이유: 인도 요리사 Kumar 씨를 초대했어요 → 인도 음식 좋아하세요? → Then(그렇다면) 요리 수업을 놓치지 마세요.\n포인트 ▶ Then은 앞의 질문(Do you like ~?)에 '예'라고 할 때를 가정한 말"),
         (3, 0, 5, 3, "정답 ▶ ③\n이유: 너무 크고 무거울 것 같아요 → 전혀요(Not at all). 크지만 아주 가벼워요 → 정말요? 그럼 살게요.\n포인트 ▶ Not at all은 앞의 '무거울 것 같다'를 부정하는 말")],
}
for d in PK['days']:
    if d['id'] not in SPEC: continue
    B = blocks(d); items = []
    for bi, a, b, g, ex in SPEC[d['id']]:
        lines = B[bi][a:b]; assert len(lines) == b - a and 1 <= g < len(lines) - 0, (d['id'], bi, a, b)
        items.append({'lines': lines, 'given': g, 'ex': ex})
    st = [s for s in d['steps'] if s.get('title') != '문장삽입']
    k = [i for i, s in enumerate(st) if s['type'] == 'order'][0]
    st.insert(k + 1, {'type': 'insert', 'title': '문장삽입', 'guide': G, 'items': items})
    d['steps'] = st
src = open(path, encoding='utf-8').read(); head = src[:src.index('window.PKG')]
if '대화문 문장삽입' not in head: head = head.rstrip('\n') + '\n/* 11/15: 6·7과 대화문 DAY에 문장삽입 추가 (generators/add_dlg_insert.py) */\n'
write(PK, path, head)
print('ok', [(d['id'], len(d['steps'])) for d in PK['days'] if d['id'] in SPEC])
